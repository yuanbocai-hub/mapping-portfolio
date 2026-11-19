# Sources, reconstruction, and uncertainty

## Navigation chart

### Historical river photograph and model photography

- Supplied historical image: `歪屁股修复.png`, from the project author's local `歪屁股项目` folder. Preserved byte-for-byte as `assets/junk-model/river-boats-original-atmosphere.png`; JPEG display copy retains the original framing and tonal character. This is the original-atmosphere export, not the AI-generated reconstruction.
- Image identified by direct visual comparison with Duke's digitized negative: Sidney D. Gamble, *Twisted Stern Boats*, 1917, item `22A-115` / `gamble_022A_115`. The record identifies the location as Fuling/Fuzhou, Sichuan (涪州/涪陵, now Chongqing). Record: https://repository.duke.edu/dc/gamble/gamble_022A_115. Persistent identifier: https://idn.duke.edu/ark:/87924/r3862bq52. The supplied image omits the negative's black outer border.
- Preferred credit: *Twisted Stern Boats*, 22A-115, Sidney D. Gamble Photographs, David M. Rubenstein Rare Book & Manuscript Library, Duke University. The individual Duke record states CC0 1.0 / Free Re-Use. Date is 1917, not merely the broader collection series date of 1917–1919.
- The model stern caption describes the sweep arrangement as aiding directional control during a rapid descent. It follows the existing project interpretation of Worcester's drawings and the accompanying steering plates; it does not attribute a modern performance measurement to the model.
- Model photographs supplied in `歪屁股项目/产品实拍`, credited to YUE-FAN Studio as project material. Web copies are resized and JPEG-encoded without generative edits, cropping or retouching. File correspondence:
  - `9404df9c14ccaeb97b47717200515590.jpg` → `model-overview`.
  - `84883152d9832f5b0f29acf0630b15c9.jpg` → `model-stern`.
  - `5fa70a8c2f772ff8934f113d3f2ea1b1.jpg` → `model-opposite-view`.
  - `582f8b4a3cfde9bdb8ce349c8d4129f1.jpg` → `model-handheld`.
- Display copies are 1200 px on the long side, expanded views 2400 px. Originals remain in the supplied source folder.

### Introductory transport schematic

- `assets/yangtze-transport-schematic.svg`: selected waterway and cargo relationships, not a geographic route map. Main-stem sections meet at Hankow and Ichang. The figure follows the user-selected citation: G. R. G. Worcester, *The Junks and Sampans of the Yangtze* (1947–1948), two volumes. Catalogue: https://catalog.etoncollege.com/B18556.
- Solid lines indicate schematic waterway connections; dashed lake-to-Ichang lines summarize interpreted cargo relationships via the main stem, not direct navigation routes, scheduled services, or a claim that every shipment followed this sequence. The specific lake-to-Ichang reading was supplied by the project author; no page-specific quotation for both links has been independently verified here. Transshipment at Ichang is documented in the repository's Worcester port notes.
- Lake geometry: Natural Earth 1:10m Lakes, Poyang Hu (`ne_id` 1159114015) and Dongting Hu (`ne_id` 1159116351), downloaded 2026-11-19 from https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_lakes.geojson. These are generalized contemporary reference outlines, not dated historical shorelines. Source overview: https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-lakes/. Natural Earth data are public domain.
- The two original lake features are retained in `assets/yangtze-lake-outlines.geojson`. The build script preserves their north-up orientation and proportions using longitude scaled by the cosine of mean latitude, then fits each lake independently. Lake areas and route distances must not be compared from this schematic.
- Rebuild with `python3 scripts/build-yangtze-schematic.py`.

**Historical navigation:** G. R. G. Worcester, *Junks and Sampans of the Upper Yangtze* (Shanghai: Statistical Department of the Inspectorate General of Customs, 1940), Chapter V, “The Kungt’anho.” The research task supplied a photograph of the relevant chapter text. The chart’s bibliographic year was corrected from the earlier draft’s 1931 to 1940.

- Catalogue record: https://ci.nii.ac.jp/ncid/BA29337189
- River geometry: © OpenStreetMap contributors, ODbL, restored through public Nominatim geometry exports in November 2026. https://www.openstreetmap.org/copyright
- Relief: AWS Terrain Tiles, Terrarium RGB elevation encoding, derived from SRTM/GMTED and other public elevation datasets. https://registry.opendata.aws/terrain-tiles/
- Projection treatment: WGS 84 geographical coordinates transformed using non-uniform scaling to emphasize the Wu Kiang. A uniform linear scale is not implied.
- Hsin-t’an: approximate position interpolated along the river at two-thirds of the Yen-ho–Ch’ao-ti distance, using the historical 40-mile and 20-mile stages.
- Rapids: the count of 71 applies to the Kung-t’an–Ssu-nan reach as a whole. The map marks a corridor, not independently geolocated rapid points.
- Distances: historical estimates. The approved c. 224 km overview is retained; the four stage figures total 140 miles, approximately 225 km.

The original July river downloads were absent from the synced workspace. The rendering script was recovered from task history and geometry was restored from the same public data source. The present map should therefore not be described as a bit-for-bit reproduction of the July datasets.

## Commodity maps

The modern commodity maps identify **Hong Maoxi, compiler and cartographer, *Latest General Survey Map of China* (1935)** as their historical source. This attribution is recorded from the supplied modern maps. The separately supplied historical JPEGs do not by themselves provide a complete title-page or holding-institution citation; their full edition and reproduction provenance remains to be documented.

### Yangtze

- Historical reproduction: `长江流域物产_原件.jpg`, 1,440 × 1,025 pixels.
- Modern main map: `Yangtze_Products_1930s_EN_HighRes15MB.jpg`.
- Thematic companion: `yangtze_seven_panels_hydro_EN_600dpi.png`.
- Commodity categories: sugar, hemp, tobacco, tea, silk, cotton, rice.

### Pearl River basin and eastern Kuang-tung

- Historical reproduction: `粤江流域物产_原件.jpg`, 2,844 × 2,038 pixels.
- Modern map: `Pearl_River_Eastern_Kuangtung_EN_HighRes.png`.
- Its thematic categories and mineral indications follow its own legend; they should not be equated automatically with the Yangtze classification.

### Modern reference layers credited on the supplied maps

- CHGIS version 6, historical administrative boundaries (1911), Harvard University / Fudan University.
- Natural Earth land and reference geography.
- Shaded relief from SRTM Plus.
- HydroRIVERS v1.0; OpenStreetMap contributors where indicated.
- HydroBASINS v1c on the Pearl River map.

See the individual map footers for the layer attribution and projection specific to each image. Historical commodity boundaries represent source-derived regional indications rather than modern measured production boundaries. Historical thematic dates, 1911 administrative references, and modern physical basemaps describe different layers of evidence.

## Written research notes

The two Worcester notes are English translations of Chinese research documents based on the combined Chinese–English edition 《中国长江帆船通鉴（汉英双语）（全三册）》. Page references distinguish printed Chinese-text pages from combined-PDF pages. English passages translated from Chinese excerpts are not certified transcriptions of Worcester’s original English.

The five-category port classification is the research note’s analytical synthesis, not a formal classification proposed by Worcester. Its evidence labels and distinctions between ordinary mention, functional evidence, and explicit description must be retained.

The international trade-route guide draws principally on Iftekhar Iqbal, *The Range of the River: A Riverine History of Empire across China, India, and Southeast Asia*. Its source pages and route uncertainties remain in the guide. Its referenced GeoJSON datasets have not yet been supplied to this repository.

## File provenance

Original filenames are retained. `assets/` contains JPEG browsing derivatives, not replacement masters. `asset-manifest.json` records the supplied images’ dimensions, sizes, and SHA-256 checksums for later verification. Enlarging a low-resolution reproduction does not recover missing label detail.

## Codex-assisted navigation chart

The navigation chart is an experiment in drawing with Codex. Codex assisted the plotting and layout using the historical route information. Its role should be credited separately from the underlying navigation sources. The portfolio treats the chart as a related study; the Yangtze commodity reconstruction is the principal work.

## Commodity extraction records

[METHODS.md](METHODS.md) records the two extraction approaches, the corrected Yangtze class counts, the retained Pearl River band gaps, and the difference between source geometry and selective hiding in the final layout. It was checked against the saved GIS records and processing scripts on 17 November 2026.

## Vessel illustrations

- Upstream: YUE-FAN adaptation of plates 10 and 18 from G. R. G. Worcester, *Notes on the Crooked-bow and Crooked-stern Junks of Szechwan* (Shanghai: Statistical Department of the Inspectorate General of Customs, 1941). Bibliographic attribution follows the supplied diagram.
- Downstream: YUE-FAN adaptation of plate 30 from L. Audemard, *Les Jonques Chinoises*, vol. 5, *Haut Yang Tse Kiang* (1963). Attribution follows the supplied image; the photograph is used to identify equipment, not to establish a particular rapid descent.
- Plan, elevation, and perspective: supplied YUE-FAN drawing. Its original plate number is not established by the supplied file.

Original supplied figures are in `assets/figures/`; JPEG browsing copies are in `assets/`. Watermarks and existing image credits are retained. The page provides edited text descriptions of the annotations, also collected in [the figure notes](notes/figure-annotations.md). Embedded lettering in the supplied images has not been repainted.
