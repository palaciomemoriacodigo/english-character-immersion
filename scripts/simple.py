"""Generate a beginner-first offline guide and a one-source ChatGPT package."""
from datetime import date
import html
import json
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from validate import MODULES, TEMPLATES, ROOT

SOURCE_NAME = '02_English_Immersion.md'
INSTRUCTIONS_NAME = '01_Instrucciones.txt'
LEGAL_NOTE = "Licensing / Licencias (informational): MIT applies only to original software; CC BY-NC 4.0 applies only to specified original, franchise-independent educational material. Character dossiers, franchise-specific RPG and third-party protected material are excluded. No third-party permission is claimed. Full scope / Alcance: https://github.com/palaciomemoriacodigo/english-character-immersion/blob/main/LICENSE ; rights / derechos: https://github.com/palaciomemoriacodigo/english-character-immersion/blob/main/NOTICE.md ."
COMMON = ('LICENSE', 'NOTICE.md', 'PRIVACY.md', 'LICENSES/MIT.txt', 'LICENSES/CC-BY-NC-4.0.md', 'VERSION')
def build_simple(out, version, sources, instructions):
    out = Path(out)
    # Preserve the original identifiers as headings, not as separate files.
    names = [*MODULES, *TEMPLATES]
    intro = (
        '## One-file installation\n'
        'Only one reference source is installed: ' + SOURCE_NAME + '. '
        'Every original filename mentioned below or inside the source is a section identifier, not another required upload. '
        'Consult the matching section by its exact name; do not assume that separate files are missing. '
        'The CSV template is a schema in the source, not a separate uploaded CSV. '
        'Do not invent information if retrieval fails.\n\n'
    )
    prompt = instructions.replace('## Sources and priorities\n', intro + '## Sources and priorities\n', 1)
    prompt += '\n\n' + LEGAL_NOTE + '\n'
    if len(prompt) > 8000:
        raise ValueError('Simple instructions exceed design budget')
    source = '# English Immersion — reference source\n\nVersion: ' + version + '\n\n'
    source += LEGAL_NOTE + '\n\n'
    source += 'All original module and template names below are section identifiers. Project instructions take priority. Personal progress and campaign records must remain private; this source contains empty templates.\n\n'
    source += '## Index\n\n' + '\n'.join('- ' + name for name in names) + '\n\n'
    for name in names:
        source += '\n\n---\n\n# Source section: ' + name + '\n\n'
        if name.endswith('.csv'):
            source += '```csv\n' + sources[name].rstrip('\n') + '\n```\n'
        else:
            source += sources[name].rstrip() + '\n'
    template = (ROOT/'site/START_HERE.template.html').read_text(encoding='utf-8')
    payload = {INSTRUCTIONS_NAME: prompt.encode('utf-8'), SOURCE_NAME: source.encode('utf-8')}
    landing_strings = json.loads((ROOT/'site/landing_strings.json').read_text(encoding='utf-8'))
    for i in range(1, 7):
        name = f'guia-paso-{i:02d}.jpg'
        payload['images/'+name] = (ROOT/'docs/images'/name).read_bytes()
    announcement = json.loads((ROOT/'site/release_announcement.json').read_text(encoding='utf-8'))
    release_date = date.fromisoformat(announcement['date'])
    for lang in ('es', 'en'):
        values = landing_strings[lang]
        tokens = {key: html.escape(value, quote=True) for key, value in values.items()}
        public_version = 'v' + version.split('-', 1)[0]
        status = ('Acceso anticipado' if lang == 'es' else 'Early access') if '-' in version else ''
        tokens['VERSION_LINE'] = html.escape(public_version + (' · ' + status if status else ''))
        tokens['BUILD_LABEL'] = html.escape(('Versión técnica: ' if lang == 'es' else 'Build: ') + version)
        local = announcement[lang]
        tokens.update({key: html.escape(str(value), quote=True) for key, value in {
            'RELEASE_DATE': release_date.isoformat(), 'RELEASE_DAY': release_date.day,
            'RELEASE_MONTH': local['month'], 'RELEASE_YEAR': release_date.year,
            'RELEASE_KICKER': local['kicker'], 'RELEASE_TITLE': local['title'],
            'RELEASE_DESCRIPTION': local['description'],
        }.items()})
        tokens['INSTRUCTIONS'] = html.escape(prompt, quote=False)
        tokens['COPIED_JSON'] = json.dumps(values['COPIED'], ensure_ascii=False)
        tokens['FALLBACK_JSON'] = json.dumps(values['FALLBACK'], ensure_ascii=False)
        page = re.sub(r'@@([A-Z0-9_]+)@@', lambda m: tokens[m.group(1)], template)
        payload['index.html' if lang=='es' else 'en.html'] = page.encode('utf-8')
    payload['legal.html'] = (ROOT/'site/legal.html').read_bytes()
    payload['theme.css'] = (ROOT/'site/theme.css').read_bytes()
    for name in COMMON:
        payload[name] = (ROOT/name).read_bytes()
    # The identical payload can be hosted as static files after rights approval,
    # or opened locally after extracting the ZIP. Never deploy automatically.
    site_dir = out/'start'
    site_dir.mkdir(parents=True, exist_ok=True)
    for name, data in payload.items():
        dest = site_dir/name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    path = out/f'English_Immersion_Empezar_v{version}.zip'
    with ZipFile(path,'w',ZIP_DEFLATED) as z:
        for name, data in payload.items():
            entry = ZipInfo(name, date_time=(1980,1,1,0,0,0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            z.writestr(entry,data)
    print(path.name, '1 source to upload; open index.html')
    return path
