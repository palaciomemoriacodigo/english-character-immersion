"""Verify the actual installation ZIPs, not just source structure."""
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import build, GROUPS
from validate import MODULES, TEMPLATES
from simple import SOURCE_NAME, INSTRUCTIONS_NAME
from html.parser import HTMLParser

class PackageTests(unittest.TestCase):
    def test_default_and_advanced_editions(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = build(Path(tmp) / 'first', advanced=True)
            second = build(Path(tmp) / 'second', advanced=True)
            default = build(Path(tmp) / 'default')
            self.assertEqual(len(default), 1)
            self.assertEqual(default[0].name, first[-1].name)
            self.assertEqual(default[0].read_bytes(), first[-1].read_bytes())
            self.assertEqual(list((Path(tmp)/'default').glob('*.zip')), default)
            self.assertEqual(len(first), 3)
            for a, b in zip(first, second):
                self.assertEqual(a.read_bytes(), b.read_bytes())
                with ZipFile(a) as z:
                    self.assertIsNone(z.testzip())
                    names = z.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    for legal_file in ('LICENSE', 'NOTICE.md', 'LICENSES/MIT.txt', 'LICENSES/CC-BY-NC-4.0.md'):
                        self.assertIn(legal_file, names)
                        self.assertEqual(z.read(legal_file), (ROOT/legal_file).read_bytes())
                    self.assertNotIn('LICENSES/CC-BY-4.0.md', names)
                    self.assertTrue(all(not n.startswith('/') and '..' not in Path(n).parts for n in names))
                    if '_Empezar_' in a.name:
                        self.assertIn('index.html', names)
                        self.assertIn('en.html', names)
                        self.assertIn('legal.html', names)
                        self.assertIn('theme.css', names)
                        self.assertEqual(z.read('theme.css'), (ROOT/'site/theme.css').read_bytes())
                        legal = GuideParser()
                        legal.feed(z.read('legal.html').decode('utf-8'))
                        for href in legal.links:
                            if href.startswith('#'):
                                self.assertIn(href[1:], legal.ids)
                            elif not href.startswith('https://'):
                                self.assertIn(href, names)
                        self.assertIn(INSTRUCTIONS_NAME, names)
                        self.assertEqual([n for n in names if n.startswith('02_')], [SOURCE_NAME])
                        self.assertNotIn('analytics/analizar_errores.py', names)
                        prompt = z.read(INSTRUCTIONS_NAME).decode('utf-8')
                        source = z.read(SOURCE_NAME).decode('utf-8')
                        self.assertLessEqual(len(prompt), 8000)
                        self.assertIn(SOURCE_NAME, prompt)
                        self.assertIn('CC BY-NC 4.0', prompt)
                        self.assertIn('CC BY-NC 4.0', source)
                        for name in MODULES + TEMPLATES:
                            self.assertIn('# Source section: ' + name, source)
                        for page in ('index.html', 'en.html'):
                            parser = GuideParser()
                            text = z.read(page).decode('utf-8')
                            parser.feed(text)
                            self.assertNotIn('@@', text)
                            self.assertIn('datetime="2026-12-13"', text)
                            self.assertIn('href="VERSION"', text)
                            self.assertIn('legal.html', parser.links)
                            self.assertIn('href="theme.css"', text)
                            self.assertIn('orbit-art', text)
                            self.assertIn('id="journey-title"', text)
                            self.assertNotIn('candidata de prueba, no publicación estable', text)
                            self.assertNotIn('test candidate, not a stable release', text)
                            self.assertEqual(''.join(parser.instructions), prompt)
                            for href in parser.links:
                                if href.startswith('#'):
                                    self.assertIn(href[1:], parser.ids)
                                elif not href.startswith('https://'):
                                    self.assertIn(href, names)
                            self.assertEqual(parser.images, [f'images/guia-paso-{i:02d}.jpg' for i in range(1, 7)])
                            self.assertEqual(parser.checks, ['1','2','3','4','5','6'])
                            self.assertEqual(parser.downloads, [INSTRUCTIONS_NAME, SOURCE_NAME])
                            for image in parser.images:
                                self.assertIn(image, names)
                                self.assertTrue(z.read(image).startswith(b'\xff\xd8'))
                            self.assertIn(SOURCE_NAME, parser.links)
                            self.assertIn(INSTRUCTIONS_NAME, parser.links)
                        for name in names:
                            self.assertEqual(z.read(name), (Path(tmp)/'first'/'start'/name).read_bytes())
                        for name in (INSTRUCTIONS_NAME, SOURCE_NAME):
                            self.assertEqual(z.read(name), (ROOT/'empezar'/name).read_bytes(), 'Run python scripts/sync_start.py to refresh beginner files')
                        continue
                    expected = set(MODULES + ['USER_MANUAL.md', 'Session_Review_TEMPLATE.md', 'Session_Errors_TEMPLATE.csv']) if '_Full_' in a.name else set(GROUPS)
                    self.assertEqual({n.removeprefix('upload/') for n in names if n.startswith('upload/')}, expected)
                    prompt = z.read('PROJECT_INSTRUCTIONS.md').decode('utf-8')
                    self.assertLessEqual(len(prompt), 8000)
                    self.assertIn('analytics/analizar_errores.py', names)
                    self.assertIn('docs/en/ANALYTICS.md', names)
                    self.assertIn('docs/es/ANALYTICS.md', names)
                    self.assertIn('LICENSE', names)
                    self.assertFalse(any(n.startswith(('private/', 'personal/', 'reports/', 'reportes/', 'checkpoints/')) for n in names))
                    for name in expected:
                        if name != 'USER_MANUAL.md':
                            if name.endswith('TEMPLATE.csv') or name.endswith('TEMPLATE.md'):
                                self.assertIn(name, prompt)
                            elif '_Lite_' in a.name or name in MODULES:
                                self.assertIn(name, prompt)

class GuideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.images = []
        self.checks = []
        self.downloads = []
        self.instructions = []
        self.in_instructions = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError('Duplicate id: '+attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'img':
            self.images.append(attrs['src'])
            if not attrs.get('alt'):
                raise ValueError('Image missing alt text')
        if tag == 'input' and attrs.get('type') == 'checkbox':
            self.checks.append(attrs.get('data-step'))
        if tag == 'a' and 'download' in attrs:
            self.downloads.append(attrs['href'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'textarea' and attrs.get('id') == 'instructions':
            self.in_instructions = True
    def handle_endtag(self, tag):
        if tag == 'textarea':
            self.in_instructions = False
    def handle_data(self, data):
        if self.in_instructions:
            self.instructions.append(data)
