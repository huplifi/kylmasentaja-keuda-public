"""Fail-closed content/build validation; only referenced, inert SVG symbols are public."""
import argparse
from collections import Counter
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

FORBIDDEN = re.compile(r'Liitteet[/\\]|31[ -]Harjoittelupaikat|\.codex|Arkisto[/\\]|00[ -]Etusivu|03[ -]Yhteystiedot|90[ -]Tehtävät|99[ -]Saapuneet|IMG_\d+\.(?:jpe?g|png)', re.I)
SECRETS = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[\w]+|sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|[\w.+-]+@[\w.-]+\.[a-z]{2,}|(?<!\d)(?:\+358[ -]?(?:\d[ -]?){6,11}|0[45]\d(?:[ -]?\d){6,8})(?!\d)', re.I)
SVG_PATH = re.compile(r'(?:symbolit|kaaviot)/[a-z0-9-]+\.svg')
SVG_NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG_NS)
NUMERIC = re.compile(r'[-+0-9.eE,\s]+')
DIAGRAM_VIEWBOX = re.compile(r'0 0 ([1-9][0-9]{0,3}) ([1-9][0-9]{0,3})')
HEX_COLOR = re.compile(r'#[0-9a-f]{3}(?:[0-9a-f]{3})?', re.I)
GEOMETRY = {'path', 'circle', 'ellipse', 'line', 'rect', 'polyline', 'polygon', 'g'}
NUMERIC_ATTRS = {'x', 'y', 'x1', 'y1', 'x2', 'y2', 'cx', 'cy', 'r', 'rx', 'ry', 'width', 'height', 'stroke-width', 'stroke-miterlimit', 'stroke-dasharray', 'stroke-dashoffset', 'points'}


def check_text(text):
    decoded = html.unescape(unquote(unquote(text)))
    if FORBIDDEN.search(decoded) or SECRETS.search(decoded):
        raise ValueError('Yksityisyystarkistus epäonnistui (sisältöä ei tulosteta).')


def sanitize_svg(text, *, diagram=False):
    """Rebuild passive geometry. Strip source metadata and reject active XML."""
    if len(text.encode('utf-8')) > 65536 or re.search(r'<!|<\?(?!xml\s)', text, re.I):
        raise ValueError('SVG: liian suuri tiedosto tai kielletty XML-rakenne.')
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError('SVG: virheellinen XML.') from exc
    viewbox = root.get('viewBox', '')
    dimensions = DIAGRAM_VIEWBOX.fullmatch(viewbox)
    valid_viewbox = (
        dimensions is not None and all(int(n) <= 1600 for n in dimensions.groups())
        if diagram else viewbox == '0 0 64 64'
    )
    if root.tag != f'{{{SVG_NS}}}svg' or not valid_viewbox:
        raise ValueError('SVG: virheellinen viewBox.')
    shapes = 0

    def rebuild(node, is_root=False):
        nonlocal shapes
        if not isinstance(node.tag, str) or not node.tag.startswith(f'{{{SVG_NS}}}'):
            raise ValueError('SVG: kielletty nimiavaruus.')
        tag = node.tag.split('}', 1)[1]
        if tag in ('title', 'desc'):
            return None  # Source labels can contain private provenance; the page supplies alt text.
        if tag not in GEOMETRY and not (is_root and tag == 'svg'):
            raise ValueError('SVG: vain passiivinen vektorigrafiikka sallitaan.')
        if (node.text or '').strip():
            raise ValueError('SVG: ylimääräinen tekstisisältö.')
        attrs = {}
        for name, value in node.attrib.items():
            if name in ('id', 'role', 'aria-label', 'aria-labelledby', 'aria-describedby'):
                continue
            if name == 'viewBox' and is_root:
                valid = value == viewbox
            elif name in ('fill', 'stroke', 'color'):
                valid = value in ('none', 'currentColor', 'black', '#000', '#000000')
                if diagram:
                    valid = valid or value == 'white' or HEX_COLOR.fullmatch(value) is not None
            elif name in NUMERIC_ATTRS:
                valid = bool(NUMERIC.fullmatch(value))
            elif name == 'd':
                valid = bool(re.fullmatch(r'[MmZzLlHhVvCcSsQqTtAa0-9eE+.,\s-]+', value))
            elif name == 'transform':
                valid = bool(re.fullmatch(r'\s*(?:(?:matrix|translate|scale|rotate|skewX|skewY)\([-+0-9.eE,\s]+\)\s*)+', value))
            elif name in ('stroke-linecap', 'stroke-linejoin'):
                valid = value in ('round', 'butt', 'square', 'miter', 'bevel')
            elif name in ('fill-rule', 'clip-rule'):
                valid = value in ('nonzero', 'evenodd')
            else:
                valid = False
            if not valid:
                raise ValueError('SVG: kielletty tai virheellinen attribuutti.')
            attrs[name] = value
        if is_root:
            attrs['color'] = '#000000'  # External SVGs cannot inherit the page's currentColor.
        if tag not in ('svg', 'g'):
            shapes += 1
        clean = ET.Element(node.tag, dict(sorted(attrs.items())))
        for child in node:
            if (child.tail or '').strip():
                raise ValueError('SVG: ylimääräinen tekstisisältö.')
            safe = rebuild(child)
            if safe is not None:
                clean.append(safe)
        return clean

    clean = rebuild(root, True)
    if not shapes:
        raise ValueError('SVG: tyhjä symboli.')
    ET.indent(clean, space='  ')
    return ET.tostring(clean, encoding='unicode', short_empty_elements=True) + '\n'


def check_svg_file(p, canonical=True):
    if p.is_symlink() or not p.is_file() or p.parent.is_symlink():
        raise ValueError('SVG: puuttuva tiedosto tai symbolinen linkki.')
    original = p.read_text(encoding='utf-8')
    safe = sanitize_svg(original, diagram=p.parent.name == 'kaaviot')
    if canonical and safe != original:
        raise ValueError('SVG: julkaisutiedostoa ei ole puhdistettu.')
    return safe


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.assets, self.images = set(), [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.assets.append(a['src'])
        if tag == 'img' and a.get('src'): self.images.append(a['src'])
        if tag == 'link' and a.get('href'): self.assets.append(a['href'])


def content_files(content):
    """Only root Markdown and explicitly scoped SVG directories."""
    if content.is_symlink() or not content.is_dir():
        raise ValueError('Kielletty content-polku.')
    files = []
    for p in content.iterdir():
        if p.is_symlink(): raise ValueError('Kielletty content-polku.')
        if p.name in ('symbolit', 'kaaviot') and p.is_dir():
            for asset in p.iterdir():
                rel = asset.relative_to(content).as_posix()
                if asset.is_symlink() or not asset.is_file() or not SVG_PATH.fullmatch(rel):
                    raise ValueError('Kielletty SVG-polku.')
                files.append(rel)
        elif p.is_file() and re.fullmatch(r'[a-z0-9-]+\.md', p.name):
            files.append(p.name)
        else:
            raise ValueError('Kielletty content-polku.')
    return sorted(files)


def validate(content, build=None):
    manifest = json.loads((content.parent / 'content-manifest.json').read_text())
    actual = content_files(content)
    if actual != sorted(manifest) or 'index.md' not in actual:
        raise ValueError('Content poikkeaa hyväksytystä manifestista.')
    notes = [name for name in actual if name.endswith('.md')]
    assets = set(actual) - set(notes)
    expected_images = {}
    for name in actual:
        p = content / name
        if hashlib.sha256(p.read_bytes()).hexdigest() != manifest[name]:
            raise ValueError('Contentin tarkistussumma ei täsmää.')
        if name in assets:
            check_svg_file(p)
            continue
        text = p.read_text()
        check_text(text)
        if not re.match(r'---\ntitle: "[^\n]+"\npublish: true\n---\n', text):
            raise ValueError('Contentin opt-in metadata puuttuu.')
        expected_images[name] = Counter(re.findall(r'!\[[^\]\n]*\]\((' + SVG_PATH.pattern + r')\)', text))
    referenced = set().union(*(set(v) for v in expected_images.values()))
    if assets != referenced:
        raise ValueError('SVG-tiedostot ja muistiinpanojen kuvaviitteet eivät täsmää.')
    if build is None:
        print(f'Content tarkistettu: {len(notes)} sivua, {len(assets)} SVG-kuvaa.')
        return
    pages = {}
    expected = {str(Path(p).with_suffix('.html')) for p in notes} | {'404.html'}
    allowed = expected | assets | {
        'index.css', 'prescript.js', 'postscript.js', 'sitemap.xml',
        'favicon.ico', 'static/icon.png', 'static/og-image.png', 'static/contentIndex.json',
        'static/giscus/light.css', 'static/giscus/dark.css',
    }
    found_assets = set()
    for p in build.rglob('*'):
        if p.is_symlink() or any(part.startswith('.') for part in p.relative_to(build).parts):
            raise ValueError('Kielletty build-polku.')
        if not p.is_file(): continue
        rel = p.relative_to(build).as_posix()
        if rel not in allowed: raise ValueError('Buildissa tiedosto sallitun listan ulkopuolelta.')
        if FORBIDDEN.search(rel): raise ValueError('Kielletty build-polku.')
        if rel in assets:
            check_svg_file(p)
            if hashlib.sha256(p.read_bytes()).hexdigest() != manifest[rel]:
                raise ValueError('Buildin SVG ei vastaa tarkistettua lähdettä.')
            found_assets.add(rel)
        elif p.suffix in ('.html', '.json', '.xml', '.txt'):
            check_text(p.read_text())
        if p.suffix == '.html': pages[p.resolve()] = Page(p.read_text())
    if found_assets != assets:
        raise ValueError('Buildista puuttuu SVG-kuvia.')
    if {str(p.relative_to(build.resolve())) for p in pages} != expected:
        raise ValueError('Buildissa odottamattomia tai puuttuvia sivuja.')

    def resolve_asset(p, href):
        url = urlsplit(href)
        if url.scheme in ('https', 'http') or url.netloc: return None
        if url.scheme: raise ValueError('Kielletty linkkiprotokolla.')
        route = unquote(url.path)
        if route == '/kylmasentaja-keuda-public':
            target = build / 'index.html'
        elif route.startswith('/kylmasentaja-keuda-public/'):
            target = build / route.removeprefix('/kylmasentaja-keuda-public/')
        elif route.startswith('/'):
            raise ValueError(f'Odottamaton absoluuttinen linkki: {href}')
        else:
            target = p.parent / route if route else p
        if target.is_dir(): target = target / 'index.html'
        if not target.is_file() and not target.suffix: target = target.with_suffix('.html')
        target = target.resolve()
        if not target.is_relative_to(build.resolve()) or not target.is_file():
            raise ValueError(f'Rikkinäinen linkki: {p.name} -> {href}')
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            raise ValueError(f'Rikkinäinen otsikkolinkki: {p.name} -> {href}')
        return target

    checked = 0
    for p, page in pages.items():
        for href in page.links + page.assets:
            if resolve_asset(p, href) is not None: checked += 1
        wanted = expected_images.get(p.with_suffix('.md').name, Counter())
        rendered = Counter()
        for src in page.images:
            target = resolve_asset(p, src)
            if target is not None:
                rendered[target.relative_to(build.resolve()).as_posix()] += 1
        if any(rendered[name] < count for name, count in wanted.items()):
            raise ValueError(f'HTML:stä puuttuu odotettu SVG-kuva: {p.name}')
    search = json.loads((build/'static/contentIndex.json').read_text())
    if set(search) != {Path(p).stem for p in notes}:
        raise ValueError('Hakuindeksin sivut eivät vastaa sallittua sisältöä.')
    print(f'Build tarkistettu: {len(pages)} HTML-sivua, {len(assets)} SVG-kuvaa, {checked} sisäistä linkkiä/resurssia, kuvaviitteet ja yksityisyysrajat.')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--content', type=Path, default=Path('content'))
    p.add_argument('--build', type=Path)
    p.add_argument('--sanitize-svg', type=Path)
    p.add_argument('--check-svg', type=Path)
    args = p.parse_args()
    if args.sanitize_svg:
        print(check_svg_file(args.sanitize_svg, canonical=False), end='')
    elif args.check_svg:
        check_svg_file(args.check_svg)
    else:
        validate(args.content, args.build)
