"""Regenerate the Chinese Yangtze page, preserving the English page's markup and assets.

Run this after editing yangtze.html. New text requires a translation in
yangtze-zh-translations.json; incomplete translations fail before writing.
"""
from pathlib import Path
from html import escape, unescape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
translations = json.loads((ROOT / 'scripts/yangtze-zh-translations.json').read_text())
source = (ROOT / 'yangtze.html').read_text()
missing = set()

def translate(value, kind):
    clean = unescape(value.strip())
    if not clean:
        return value
    if clean not in translations[kind]:
        missing.add((kind, clean))
        return value
    # Preserve whitespace around inline elements.
    prefix = re.match(r'\s*', value).group()
    suffix = re.search(r'\s*$', value).group()
    return prefix + escape(translations[kind][clean], quote=kind == 'attributes') + suffix

result = re.sub(r'>([^<>]+)<', lambda m: '>' + translate(m[1], 'text') + '<', source)

def attribute(m):
    key, value = m[1], m[2]
    if not value or (key == 'content' and value.startswith(('#', 'width='))):
        return m[0]
    return key + '="' + translate(value, 'attributes') + '"'

result = re.sub(r'(alt|data-caption|aria-label|content)="([^"]*)"', attribute, result)
if missing:
    raise SystemExit('Missing translations:\n' + '\n'.join(str(x) for x in sorted(missing)))
result = result.replace('<html lang="en">', '<html lang="zh-Hans">')
result = result.replace('data-language-link aria-current="page">EN', 'data-language-link>EN')
result = result.replace('data-language-link>中文', 'data-language-link aria-current="page">中文')
result = result.replace('<h1 id="project-title">长江<br>作为 <em>水路运输体系</em></h1>',
                        '<h1 id="project-title">作为水路运输体系的<br><em>长江</em></h1>')
# Keep the navigation within this project's chosen language.
result = result.replace('<a href="yangtze.html">长江</a>', '<a href="yangtze-zh.html">长江</a>')
(ROOT / 'yangtze-zh.html').write_text(result)
print('Built yangtze-zh.html')
