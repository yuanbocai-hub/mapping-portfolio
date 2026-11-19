"""Build the transport schematic from saved Natural Earth lake geometry."""
from pathlib import Path
import json
import math
from html import escape

ROOT = Path(__file__).resolve().parents[1]
features = json.loads((ROOT / 'assets/yangtze-lake-outlines.geojson').read_text())['features']
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="710" viewBox="0 0 1240 710" role="img" aria-labelledby="title description">
<title id="title">Yangtze transport connections and lake networks</title>
<desc id="description">Shanghai to Hankow is Worcester’s lower river; Hankow to Ichang the middle river; above Ichang the upper river. Poyang Lake connects at Hukou, Dongting Lake at Chenglingji, and the Wu River at Fu-chou. Dashed lines indicate interpretive cargo connections between the lake networks and Ichang via the main stem, not direct routes. Contemporary Natural Earth outlines represent the lakes at independent scales.</desc>
<rect width="1240" height="710" fill="#f5f2ea"/>
<style>
text{fill:#203d3e;font-family:Georgia,'Times New Roman','Songti TC','Noto Serif CJK TC',serif}
.city{font-size:25px}.zh{font-size:21px}.small{font:18px Arial,'PingFang TC',sans-serif}.note{font:20px Arial,'PingFang TC',sans-serif}.region{font-size:25px;font-style:italic}.accent{fill:#a94e33}
.water{fill:none;stroke:#23666b;stroke-width:3}.cargo{fill:none;stroke:#a94e33;stroke-width:2.5;stroke-dasharray:8 7}.bracket{fill:none;stroke:#87998c;stroke-width:1.5}.port{fill:#f5f2ea;stroke:#23666b;stroke-width:3}.transfer{fill:#a94e33;stroke:#a94e33;stroke-width:3}
</style>''']

def text(x, y, value, cls='city', anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

for left,right,label in [(65,470,'Lower river'),(470,750,'Middle river'),(750,1170,'Upper river')]:
    text((left+right)/2, 45, label, 'region')
    parts.append(f'<path class="bracket" d="M{left} 61v14 M{left} 68H{right} M{right} 61v14"/>')
parts.append('<path class="water" d="M65 172H1170 M975 172V550"/>')

for x,en,zh in [(65,'Shanghai','上海'),(470,'Hankow','漢口'),(750,'Ichang','宜昌'),(975,'Fu-chou','涪州'),(1170,'Chungking','重慶')]:
    text(x,115,en);text(x,146,zh,'zh')
    cls='transfer' if x in [750,975] else 'port'
    parts.append(f'<circle class="{cls}" cx="{x}" cy="172" r="9"/>')

def lake(name, cx, cy, width, height):
    feature=next(f for f in features if f['properties']['name']==name)
    rings=feature['geometry']['coordinates']
    coords=[p for ring in rings for p in ring]
    lat=sum(p[1] for p in coords)/len(coords)
    coslat=math.cos(math.radians(lat))
    project=lambda p:(p[0]*coslat,-p[1])
    flat=[project(p) for p in coords]
    xmin,xmax=min(p[0] for p in flat),max(p[0] for p in flat)
    ymin,ymax=min(p[1] for p in flat),max(p[1] for p in flat)
    scale=min(width/(xmax-xmin),height/(ymax-ymin))
    transform=lambda p:(cx+(project(p)[0]-(xmin+xmax)/2)*scale,cy+(project(p)[1]-(ymin+ymax)/2)*scale)
    paths=[]
    for ring in rings:
        paths.append('M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in map(transform,ring))+' Z')
    # Connect to the northern edge of the outline; ports remain schematic.
    north=transform(min(coords,key=lambda p:project(p)[1]))
    parts.append(f'<path class="water" d="M{cx} 172V250H{north[0]:.2f}V{north[1]:.2f}"/>')
    parts.append(f'<path d="{" ".join(paths)}" fill="#d5e5e2" stroke="#23666b" stroke-width="1.8" fill-rule="evenodd"/>')

lake('Poyang Hu',250,425,170,205)
lake('Dongting Hu',595,425,230,180)
for x,en,zh in [(250,'Hukou','湖口'),(595,'Chenglingji','城陵磯')]:
    parts.append(f'<circle class="port" cx="{x}" cy="172" r="5"/>')
    text(x+14,207,en,'small','start');text(x+14,233,zh,'small','start')

# Cargo relationships are distinct from the solid water connections.
parts.append('<path class="cargo" d="M318 390 C355 275 665 325 743 184 M700 423 C760 365 775 260 755 184"/>')
text(467,300,'Cargo connections','note accent')
text(467,325,'via the main stem','small')
text(250,561,'Poyang Lake','city');text(250,590,'鄱陽湖','zh')
text(595,561,'Dongting Lake','city');text(595,590,'洞庭湖','zh')

text(790,236,'Transfer to craft suited','small','start')
text(790,261,'to upstream rapids','small','start')
text(1000,320,'Salt transferred to','small','start')
text(1000,345,'Wu River boats','small','start')
text(947,366,'Wu Chiang','note accent','end');text(947,394,'烏江','zh accent','end')
for y,en,zh in [(437,'Kung-t’an','龔灘'),(550,'Upper Wu Chiang','烏江上游')]:
    parts.append(f'<circle class="port" cx="975" cy="{y}" r="8"/>')
    text(998,y+6,en,'city','start');text(998,y+34,zh,'zh','start')
text(998,495,'Further transfers','small','start')
text(998,518,'upstream','small','start')

parts.append('<path class="water" d="M65 641H115"/><path class="cargo" d="M465 641H515"/>')
text(129,648,'Waterway connections','small','start');text(529,648,'Cargo connections (schematic)','small','start')
text(65,686,'Not to scale. Lake outlines shown at independent scales; north is up within each outline.','small','start')
parts.append('</svg>')
(ROOT/'assets/yangtze-transport-schematic.svg').write_text('\n'.join(parts))
print('Built assets/yangtze-transport-schematic.svg')
