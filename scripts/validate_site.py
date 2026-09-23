"""Fail-closed content/build validation; no network requests or source-vault access."""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

FORBIDDEN = re.compile(r'Liitteet[/\\]|31[ -]Harjoittelupaikat|\.codex|Arkisto[/\\]|00[ -]Etusivu|03[ -]Yhteystiedot|90[ -]Tehtävät|99[ -]Saapuneet|IMG_\d+\.(?:jpe?g|png)', re.I)
SECRETS = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[\w]+|sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|[\w.+-]+@[\w.-]+\.[a-z]{2,}|(?<!\d)(?:\+358[ -]?(?:\d[ -]?){6,11}|0[45]\d(?:[ -]?\d){6,8})(?!\d)', re.I)

def check_text(text):
    decoded = html.unescape(unquote(unquote(text)))
    if FORBIDDEN.search(decoded) or SECRETS.search(decoded):
        raise ValueError('Yksityisyystarkistus epäonnistui (sisältöä ei tulosteta).')

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.assets = set(), [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.assets.append(a['src'])
        if tag == 'link' and a.get('href'): self.assets.append(a['href'])

def validate(content, build=None):
    manifest_path = content.parent / 'content-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    actual = sorted(p.name for p in content.iterdir())
    if actual != sorted(manifest) or 'index.md' not in actual:
        raise ValueError('Content poikkeaa hyväksytystä manifestista.')
    import hashlib
    for p in content.iterdir():
        if p.is_symlink() or not p.is_file() or not re.fullmatch(r'[a-z0-9-]+\.md', p.name):
            raise ValueError('Kielletty content-polku.')
        if hashlib.sha256(p.read_bytes()).hexdigest() != manifest[p.name]:
            raise ValueError('Contentin tarkistussumma ei täsmää.')
        check_text(p.read_text())
        if not re.match(r'---\ntitle: "[^\n]+"\npublish: true\n---\n', p.read_text()):
            raise ValueError('Contentin opt-in metadata puuttuu.')
    if build is None:
        print(f'Content tarkistettu: {len(actual)} sivua.')
        return
    pages = {}
    allowed = {str(Path(p).with_suffix('.html')) for p in actual} | {
        '404.html', 'index.css', 'prescript.js', 'postscript.js', 'sitemap.xml',
        'favicon.ico', 'static/icon.png', 'static/og-image.png', 'static/contentIndex.json',
        'static/giscus/light.css', 'static/giscus/dark.css',
    }
    for p in build.rglob('*'):
        if p.is_symlink() or any(part.startswith('.') for part in p.relative_to(build).parts):
            raise ValueError('Kielletty build-polku.')
        if not p.is_file(): continue
        if str(p.relative_to(build)) not in allowed: raise ValueError('Buildissa tiedosto sallitun listan ulkopuolelta.')
        if FORBIDDEN.search(str(p.relative_to(build))): raise ValueError('Kielletty build-polku.')
        if p.suffix in ('.html', '.json', '.xml', '.txt'):
            check_text(p.read_text())
        if p.suffix == '.html': pages[p.resolve()] = Page(p.read_text())
    expected = {str(Path(p).with_suffix('.html')) for p in actual} | {'404.html'}
    if {str(p.relative_to(build.resolve())) for p in pages} != expected:
        raise ValueError('Buildissa odottamattomia tai puuttuvia sivuja.')
    checked = 0
    for p, page in pages.items():
        for href in page.links + page.assets:
            url = urlsplit(href)
            if url.scheme in ('https','http') or url.netloc: continue
            if url.scheme: raise ValueError('Kielletty linkkiprotokolla.')
            route = unquote(url.path)
            if route == '/kylmasentaja-keuda-public':
                target = build / 'index.html'
            elif route.startswith('/kylmasentaja-keuda-public/'):
                target = build / route.removeprefix('/kylmasentaja-keuda-public/')
            elif route.startswith('/'):
                raise ValueError(f'Odottamaton absoluuttinen linkki: {href}')
            else: target = p.parent / route if route else p
            if target.is_dir(): target = target / 'index.html'
            if not target.is_file() and not target.suffix: target = target.with_suffix('.html')
            target = target.resolve()
            if not target.is_relative_to(build.resolve()) or not target.is_file():
                raise ValueError(f'Rikkinäinen linkki: {p.name} -> {href}')
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                raise ValueError(f'Rikkinäinen otsikkolinkki: {p.name} -> {href}')
            checked += 1
    search = json.loads((build/'static/contentIndex.json').read_text())
    if set(search) != {Path(p).stem for p in actual}:
        raise ValueError('Hakuindeksin sivut eivät vastaa sallittua sisältöä.')
    print(f'Build tarkistettu: {len(pages)} HTML-sivua, {checked} sisäistä linkkiä/resurssia, hakuindeksi ja yksityisyysrajat.')

if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('--content',type=Path,default=Path('content')); p.add_argument('--build',type=Path)
    args=p.parse_args()
    validate(args.content,args.build)
