"""Refresh the two beginner files linked directly from the README."""
from pathlib import Path
import tempfile
from build import build, ROOT
from simple import INSTRUCTIONS_NAME, SOURCE_NAME

def sync():
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp)
        target = ROOT / 'empezar'
        target.mkdir(exist_ok=True)
        for name in (INSTRUCTIONS_NAME, SOURCE_NAME):
            (target / name).write_bytes((Path(tmp) / 'start' / name).read_bytes())
            print('Updated', target / name)

if __name__ == '__main__':
    sync()
