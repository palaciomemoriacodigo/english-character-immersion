"""Build reproducible installation packages from an explicit allowlist."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from validate import validate, MODULES, TEMPLATES
from simple import build_simple
ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    '01_Character_Profiles.md': MODULES[1:6],
    '02_Immersion_Protocol.md': MODULES[:1],
    '03_English_Learning_and_Tracking.md': MODULES[7:9],
    '04_RPG_Campaign_Engine.md': MODULES[9:10],
    '05_Memory_and_Templates.md': [MODULES[6], *TEMPLATES],
}

def build(output_dir=None, *, advanced=False):
    validate()
    version = (ROOT/'VERSION').read_text().strip()
    out = Path(output_dir) if output_dir is not None else ROOT/'dist'
    out.mkdir(parents=True, exist_ok=True)
    packages = []
    sources = {name: (ROOT / 'modules' / name).read_text(encoding='utf-8') for name in MODULES}
    sources.update({name: (ROOT / 'templates' / name).read_text(encoding='utf-8-sig') for name in TEMPLATES})
    if advanced:
        sources['USER_MANUAL.md'] = (ROOT/'docs/es/USER_MANUAL.md').read_text(encoding='utf-8')
    instructions = (ROOT/'config/PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    for edition in (('Full','Lite') if advanced else ()):
        path = out / f'English_Immersion_{edition}_v{version}.zip'
        files = {k:v for k,v in sources.items() if k != "Campaign_Checkpoint_TEMPLATE.md"}
        prompt = instructions
        if edition == 'Lite':
            mapping = {name: group for group, names in GROUPS.items() for name in names}
            def replace_names(text):
                for name, group in mapping.items():
                    text = text.replace(name, f'{group} (section {name[:-3] if name.endswith(".md") else name})')
                return text
            # Keep original module names as section headings for precise lookup.
            files = {group: '\n\n'.join(f'# Source section: {name[:-3] if name.endswith(".md") else name}\n\n'+replace_names(sources[name]) for name in names) for group,names in GROUPS.items()}
            prompt = replace_names(instructions) + '\nLite: consult named sections in the five grouped sources; the CSV schema is embedded in 05_Memory_and_Templates.md.\n'
            assert len(prompt) <= 8000
        with ZipFile(path,'w',ZIP_DEFLATED) as z:
            def write(name, data):
                entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                z.writestr(entry, data)
            write('PROJECT_INSTRUCTIONS.md',prompt)
            for name, data in files.items():
                write('upload/'+name, ('\ufeff' if name.endswith('.csv') else '')+data)
            for name in ['docs/es/INSTALLATION.md','docs/en/INSTALLATION.md','docs/es/UPDATE_GUIDE.md','docs/en/UPDATE_GUIDE.md','docs/es/USER_MANUAL.md','docs/en/USER_MANUAL.md','docs/es/ANALYTICS.md','docs/en/ANALYTICS.md','analytics/analizar_errores.py','CHANGELOG.md','LICENSE','NOTICE.md','PRIVACY.md','VERSION','LICENSES/MIT.txt','LICENSES/CC-BY-NC-4.0.md']:
                write(name, (ROOT/name).read_bytes())
            write('templates/Campaign_Checkpoint_TEMPLATE.md', (ROOT/'templates/Campaign_Checkpoint_TEMPLATE.md').read_bytes())
        print(path.name, len(files), 'upload files')
        packages.append(path)
    packages.append(build_simple(out, version, sources, instructions))
    return packages
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--advanced', action='store_true', help='Also build optional Full and Lite packages')
    build(advanced=parser.parse_args().advanced)
