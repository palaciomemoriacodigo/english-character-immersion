"""Browser acceptance smoke test. Run after scripts/build.py with Playwright installed."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'dist' / 'start'
OUT = ROOT / 'dist' / 'browser-review'

def main():
    OUT.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=SITE))
    Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}/'
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context(viewport={'width': 1440, 'height': 1000}, permissions=['clipboard-read', 'clipboard-write'], accept_downloads=True)
            page = context.new_page()
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.goto(url)
            page.locator('#copy').click()
            expect(page.locator('#copy-status')).to_contain_text('copiadas')
            assert page.evaluate('navigator.clipboard.readText()') == (SITE / '01_Instrucciones.txt').read_text(encoding='utf-8')
            for name, selector in [('01_Instrucciones.txt', 'a[download="01_Instrucciones.txt"]'), ('02_English_Immersion.md', '#download-source')]:
                with page.expect_download() as download:
                    page.locator(selector).click()
                assert download.value.suggested_filename == name
                assert Path(download.value.path()).read_bytes() == (SITE / name).read_bytes()
            for i in range(1, 7):
                page.locator(f'input[data-step="{i}"]').check()
            expect(page.locator('#finish')).to_be_visible()
            expect(page.locator('#progress-label')).to_have_text('6 / 6')
            page.reload()
            expect(page.locator('#progress-label')).to_have_text('6 / 6')
            page.locator('.language').click()
            expect(page.locator('html')).to_have_attribute('lang', 'en')
            expect(page.locator('#progress-label')).to_have_text('6 / 6')
            page.locator('#reset-progress').click()
            expect(page.locator('#progress-label')).to_have_text('0 / 6')
            expect(page.locator('#finish')).to_be_hidden()
            page.locator('details').last.locator('summary').click()
            expect(page.locator('details').last).to_have_attribute('open', '')
            page.goto(url)
            page.evaluate('Object.defineProperty(navigator,"clipboard",{value:undefined,configurable:true})')
            page.locator('#copy').click()
            expect(page.locator('#manual')).to_have_attribute('open','')
            assert page.locator('#instructions').evaluate('(t)=>t.selectionEnd-t.selectionStart') == len((SITE/'01_Instrucciones.txt').read_text(encoding='utf-8').encode('utf-16-le'))//2
            # Check the legal page and both languages in the actual browser.
            page.goto(url + 'legal.html')
            expect(page.locator('h1')).to_contain_text('Aviso legal')
            assert page.evaluate("getComputedStyle(document.documentElement).colorScheme") == 'dark'
            for width in (320, 390, 768, 1440):
                page.set_viewport_size({'width': width, 'height': 900})
                page.goto(url + 'legal.html')
                assert page.evaluate('document.documentElement.scrollWidth') <= width
                page.goto(url + 'en.html')
                assert page.evaluate('document.documentElement.scrollWidth') <= width
                expect(page.locator('.feature')).to_have_count(5)
            for width in (320, 390, 768, 1440):
                page.set_viewport_size({'width': width, 'height': 900})
                page.goto(url)
                page.evaluate('Promise.all(Array.from(document.images, i=>i.decode()))')
                assert page.evaluate('document.documentElement.scrollWidth') <= width, f'Horizontal overflow at {width}px'
                assert page.locator('img').count() == 6
                expect(page.locator('.feature')).to_have_count(5)
                expect(page.locator('#journey-title')).to_be_visible()
                assert page.evaluate("getComputedStyle(document.documentElement).colorScheme") == 'dark'
                page.screenshot(path=OUT/f'landing-{width}.png', full_page=True, animations='disabled')
                if width in (390, 1440):
                    page.screenshot(path=OUT/f'hero-{width}.png', animations='disabled')
            assert not errors, errors
            browser.close()
        print('PASS: clipboard, manual fallback, exact downloads, progress persistence/reset, language, FAQ and four viewport widths.')
    finally:
        server.shutdown()

if __name__ == '__main__':
    main()
