"""Conservative pre-publication checks. Never print matched values.

Scans current tracked files and optionally the exact generated landing and ZIPs.
Not a history scanner, OCR system, or proof that no private data exists.
"""
import argparse
import re
import subprocess
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
EMAIL = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PUBLIC_EMAIL = re.compile(r"(?:[0-9]+\+)?[A-Za-z0-9-]+@users\.noreply\.github\.com", re.I)
RULES = {
    "credential-like token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{35}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----"),
    "local user path": re.compile(r"[A-Za-z]:[\\/]Users[\\/][^\\/\s]+|/(?:home|Users)/[A-Za-z0-9._-]+"),
    "credential assignment": re.compile(r"""(?:password|api[_-]?key|secret|access[_-]?token)\s*[:=]\s*["'][^"'\n]{8,}["']""", re.I),
    "phone-like number": re.compile(r"(?:\+34[ -]?)?[679]\d{2}[ -]\d{3}[ -]\d{3}\b"),
}
PRIVATE_DIRS = {"private", "personal", "reports", "reportes", "checkpoints", "transcripts", "conversations", "session_exports", "analisis_resultados", "secrets", ".aws", ".ssh", ".gnupg"}
PRIVATE_SUFFIXES = {".pem", ".key", ".pfx", ".p12", ".kdbx", ".db", ".sqlite", ".sqlite3", ".ipynb", ".jsonl", ".log", ".jks", ".keystore"}
PRIVATE_NAMES = {"credentials.json", "secrets.json", ".env", ".envrc"}
TEMPLATE_NAMES = {"Session_Errors_TEMPLATE.csv", "Session_Review_TEMPLATE.md", "Campaign_Checkpoint_TEMPLATE.md"}

def text_findings(text):
    results = []
    for number, line in enumerate(text.splitlines(), 1):
        if any(not PUBLIC_EMAIL.fullmatch(m.group()) for m in EMAIL.finditer(line)):
            results.append((number, "email address"))
        for label, pattern in RULES.items():
            if pattern.search(line):
                results.append((number, label))
    return results

def private_path(name):
    p = PurePosixPath(name)
    base = p.name
    if p.is_absolute() or ".." in p.parts or "\\" in name:
        return True
    if any(part.lower() in PRIVATE_DIRS for part in p.parts[:-1]):
        return True
    if base.lower() in PRIVATE_NAMES or base.lower().startswith(".env.") or p.suffix.lower() in PRIVATE_SUFFIXES:
        return True
    if base in TEMPLATE_NAMES:
        return False
    if p.suffix.lower() == ".csv" or re.match(r"Session_(?:Review|Errors)_|Campaign_.*Checkpoint_", base):
        return True
    return False

def jpeg_findings(data):
    # Reject metadata-bearing APP segments and comments before the first image scan.
    # Only ordinary JFIF and Adobe marker headers are allowed.
    if not data.startswith(b"\xff\xd8"):
        return ["invalid JPEG"]
    pos = 2
    while pos < len(data):
        if data[pos] != 255:
            return ["invalid JPEG marker"]
        while pos < len(data) and data[pos] == 255:
            pos += 1
        if pos >= len(data):
            break
        marker = data[pos]
        pos += 1
        if marker in (0xda, 0xd9):
            return []
        if pos + 2 > len(data):
            break
        length = int.from_bytes(data[pos:pos+2], "big")
        if length < 2 or pos + length > len(data):
            return ["invalid JPEG segment"]
        payload = data[pos+2:pos+length]
        if marker == 0xfe:
            return ["JPEG comment"]
        if 0xe0 <= marker <= 0xef:
            allowed = (marker == 0xe0 and payload.startswith(b"JFIF\x00")) or (marker == 0xee and payload.startswith(b"Adobe"))
            if not allowed:
                return ["JPEG application metadata"]
        pos += length
    return ["truncated JPEG"]

def check_bytes(name, data):
    if private_path(name) or text_findings(name):
        return ["private or suspicious filename"]
    if name.lower().endswith((".jpg", ".jpeg")):
        return jpeg_findings(data)
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return ["unreviewed binary format"]
    if "\x00" in text:
        return ["unreviewed binary format"]
    return [f"line {number}: {kind}" for number, kind in text_findings(text)]

def scan_tracked():
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    for name in raw.decode("utf-8").split("\0"):
        if not name:
            continue
        path = ROOT / name
        if path.is_symlink():
            yield name, ["symlink requires manual review"]
        elif path.is_file():
            yield name, check_bytes(name, path.read_bytes())
        else:
            yield name, ["tracked file missing or not regular"]

def scan_generated():
    site = ROOT / "dist" / "start"
    if not (site / "index.html").is_file():
        raise ValueError("Generated landing missing; build before scanning")
    for path in sorted(site.rglob("*")):
        name = path.relative_to(site).as_posix()
        if path.is_symlink():
            yield name, ["symlink requires manual review"]
        elif path.is_file():
            yield name, check_bytes(name, path.read_bytes())
    packages = sorted((ROOT / "dist").glob("English_Immersion_*.zip"))
    if not packages:
        raise ValueError("Generated package missing")
    for package in packages:
        with ZipFile(package) as archive:
            for info in archive.infolist():
                if not info.is_dir():
                    yield info.filename, check_bytes(info.filename, archive.read(info))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generated", action="store_true", help="also scan built landing and packages")
    args = parser.parse_args()
    scans = [scan_tracked()]
    if args.generated:
        scans.append(scan_generated())
    checked = failures = 0
    for scan in scans:
        for name, issues in scan:
            checked += 1
            if issues:
                failures += 1
                # Avoid displaying a suspicious filename or any matched content.
                display = "[redacted filename]" if private_path(name) or text_findings(name) else name
                print(f"Privacy check: {display}: {', '.join(issues)}")
    print(f"Privacy check: {checked} files inspected; {failures} requiring review.")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
