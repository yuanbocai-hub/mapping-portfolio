"""Build the compact transport diagram; interpretation remains HTML beside it."""
from pathlib import Path
from html import escape
import json
import math

ROOT = Path(__file__).resolve().parents[1]
features = json.loads((ROOT / 'assets/yangtze-lake-outlines.geojson').read_text())['features']
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="985" height="600" viewBox="0 110 985 600" role="img" aria-labelledby="title desc">
<title id="title">Yangtze transport connections, lake networks and Three Gorges</title>
<desc id="desc">Bilingual schematic with the approximate Three Gorges reach upstream of Ichang. An annotation directly beneath Ichang identifies transfer to craft suited to upstream rapids. Solid lines indicate waterways, dashed rust lines summarize cargo relationships via the main stem. Contemporary lake outlines are shown north up at independent scales. Not to scale.</desc>
<rect y="110" width="985" height="600" fill="#f5f2ea"/>
<style>
text{fill:#203d3e;font-family:Georgia,'Songti TC','Times New Roman',serif}
.heading{font-size:42px}.subheading{font-size:35px}.city{font-size:24px}.zh{font-size:21px}.region{font-size:25px;font-style:italic}
.body{font-family:Arial,'PingFang TC',sans-serif;font-size:22px}.small{font-family:Arial,'PingFang TC',sans-serif;font-size:18px}.meta{font-family:Arial,'PingFang TC',sans-serif;font-size:17px;fill:#53655f}.accent{fill:#a94e33}
.water{fill:none;stroke:#23666b;stroke-width:3}.cargo{fill:none;stroke:#a94e33;stroke-width:2.4;stroke-dasharray:7 6}.rule{fill:none;stroke:#a7b3a7;stroke-width:1}.port{fill:#f5f2ea;stroke:#23666b;stroke-width:3}.transfer{fill:#a94e33;stroke:#a94e33;stroke-width:3}
</style>''']
def text(x,y,value,cls='city',anchor='start'):
    role=cls.split()[0]
    size={'heading':42,'subheading':35,'city':24,'zh':21,'region':25,'body':22,'small':18,'meta':17}[role]
    family='Arial' if role in ['body','small','meta'] else ('Songti TC' if role=='zh' else 'Georgia')
    fill='#a94e33' if 'accent' in cls else ('#53655f' if role=='meta' else '#203d3e')
    italic=' font-style="italic"' if role=='region' else ''
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-family="{family}" fill="{fill}"{italic} text-anchor="{anchor}">{escape(value)}</text>')
def lines(x,y,values,cls='body',step=32):
    for n,value in enumerate(values):text(x,y+n*step,value,cls)


for a,b,name in [(70,350,'Lower river'),(350,570,'Middle river'),(570,925,'Upper river')]:
    text((a+b)/2,134,name,'region','middle')
    parts.append(f'<path class="rule" d="M{a} 150v13 M{a} 156H{b} M{b} 150v13"/>')
parts.append('<path d="M590 174v12 M710 174v12" fill="none" stroke="#7a8981" stroke-width="1.5"/>')
parts.append('<path d="M590 180H710" fill="none" stroke="#7a8981" stroke-width="1.5" stroke-dasharray="4 4"/>')
text(650,169,'Three Gorges','meta','middle')
parts.append('<g transform="translate(0,36)">')
parts.append('<path class="water" d="M70 224H925 M750 224V550"/>')
for x,en,zh in [(70,'Shanghai','上海'),(350,'Hankow','漢口'),(570,'Ichang','宜昌'),(750,'Fu-chou','涪州'),(925,'Chungking','重慶')]:
    text(x,184,en,'city','middle');text(x,210,zh,'zh','middle')
    cls='transfer' if x in [570,750] else 'port'
    parts.append(f'<circle cx="{x}" cy="224" r="8" class="{cls}"/>')

def lake(name,cx,cy,width,height):
    feature=next(f for f in features if f['properties']['name']==name)
    rings=feature['geometry']['coordinates'];points=[p for ring in rings for p in ring]
    coslat=math.cos(math.radians(sum(p[1] for p in points)/len(points)))
    project=lambda p:(p[0]*coslat,-p[1])
    pp=[project(p) for p in points]
    xmin,xmax=min(p[0] for p in pp),max(p[0] for p in pp)
    ymin,ymax=min(p[1] for p in pp),max(p[1] for p in pp)
    scale=min(width/(xmax-xmin),height/(ymax-ymin))
    tx=lambda p:(cx+(project(p)[0]-(xmin+xmax)/2)*scale,cy+(project(p)[1]-(ymin+ymax)/2)*scale)
    north=tx(min(points,key=lambda p:project(p)[1]))
    parts.append(f'<path class="water" d="M{cx} 224V320H{north[0]:.2f}V{north[1]:.2f}"/>')
    d=' '.join('M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in map(tx,ring))+' Z' for ring in rings)
    parts.append(f'<path d="{d}" fill="#d5e5e2" stroke="#23666b" stroke-width="1.8" fill-rule="evenodd"/>')

# Positions are schematic. Each outline preserves its own shape and orientation.
lake('Poyang Hu',235,440,145,175)
lake('Dongting Hu',470,450,185,145)
for x,en,zh in [(235,'Hukou','湖口'),(470,'Chenglingji','城陵磯')]:
    parts.append(f'<circle cx="{x}" cy="224" r="4.5" class="port"/>')
    text(x-12,278,en,'small','end');text(x-12,303,zh,'zh','end')
parts.append('<path class="cargo" d="M285 396 C320 315 440 345 480 300 L480 253 Q480 239 562 232 M551 430 C620 405 677 383 677 335 C677 265 650 242 578 232"/>')

text(235,566,'Poyang Lake','city','middle');text(235,594,'鄱陽湖','zh','middle')
text(470,566,'Dongting Lake','city','middle');text(470,594,'洞庭湖','zh','middle')
parts.append('<path class="rule" d="M570 238V250"/>')
for y,value in [(271,'Transfer to craft'),(296,'suited to'),(321,'upstream rapids')]:
    text(570,y,value,'small','middle')
lines(775,318,['Salt to','Wu River boats'],'small',25)
text(775,398,'Wu Chiang','city accent');text(775,427,'烏江','zh accent')
for y,en,zh in [(452,'Kung-t’an','龔灘'),(550,'Upper Wu Chiang','烏江上游')]:
    parts.append(f'<circle cx="750" cy="{y}" r="7" class="port"/>')
    text(775,y+5,en,'city');text(775,y+32,zh,'zh')
text(775,515,'Further transfers','small')

parts.append('<path class="water" d="M55 638H95"/><path class="cargo" d="M340 638H380"/>')
text(108,644,'Waterway connections','small');text(393,644,'Cargo connections','small')
parts.append('<circle cx="665" cy="638" r="6" class="transfer"/>')
text(681,644,'Transfer port','small')
parts.append('</g></svg>')
output=ROOT/'assets/yangtze-transport-schematic.svg'
output.write_text('\n'.join(parts))
print(output)
