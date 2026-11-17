# Chongqing–Yangtze International Trade Routes: GeoJSON Guide

## I. Project purpose

This GeoJSON dataset depicts Yangtze shipping and cross-border trade networks centered on Chongqing around 1890–1910. Its focus is not Chongqing as an inland terminus of Yangtze navigation, but Chongqing as a trade interface facing in two directions: eastward through Yichang, Hankou, and Shanghai into maritime trade; and westward and southward through Sichuan, Yunnan, and the eastern Tibetan uplands toward Burma, Vietnam, northeastern India, and the Indian Ocean.

Within this narrative, Chongqing performs three related functions:

1. **Upper-Yangtze collection and distribution port:** gathering silk, white wax, medicinal materials, musk, mineral products, and other regional goods from the Sichuan Basin and the Yunnan direction.
2. **Entry node for international commodities:** receiving Indian cotton yarn, foreign textiles, dyes, marine products, and general imports carried upstream from Shanghai and other coastal ports.
3. **Inter-basin transshipment interface:** using upstream nodes such as Yibin and Chengdu to connect Yangtze water transport with mule-caravan and mountain-road transport, before goods re-enter navigation on the Irrawaddy, Red River, and Brahmaputra at Bhamo, Manhao, and Sadiya.

These routes therefore represent a composite network of successive transfers between river, pack-animal, overland, and maritime transport, rather than a set of isolated “ancient roads.”

## II. Historical period and geographical coverage

The dataset uses **circa 1900** as a common historical reference point, broadly covering 1890–1910. This period matters because:

- Chongqing had already emerged as a modern treaty port and upper-Yangtze commercial center;
- international trade increasingly influenced shipping along Shanghai–Hankou–Yichang–Chongqing;
- traditional mule-caravan routes remained active in Sichuan, Yunnan, and eastern Tibet;
- the Red River railway had not yet fully displaced traditional river navigation and mule transshipment;
- the Yunnan–Burma, Yunnan–Vietnam, and Sichuan–Tibet–Assam routes can be compared within a shared historical setting.

Coverage extends from Shanghai and the East China Sea in the east to eastern Tibet and northeastern India in the west, and south to Rangoon, Haiphong, and the Indian Ocean. It encompasses four major navigation systems: the Yangtze, Irrawaddy, Red River, and Brahmaputra.

*Naming convention: Chinese places generally use modern pinyin in this explanatory document. Established historical English names such as Bhamo, Rangoon, Haiphong, and Calcutta are retained where appropriate. The dataset’s `name_historical` field separately records historical English forms.*

## III. Principal trade routes

### 1. Shanghai–Hankou–Yichang–Chongqing–Yibin: the international Yangtze shipping axis

**Route:**

`Shanghai–Hankou–Yichang–Chongqing–Yibin`

This route provides the shipping backbone for the cross-border trading corridors. Shanghai connects to the East China Sea and international shipping; Hankou is a major commodity-distribution center on the middle Yangtze; Yichang lies at the transition from plains navigation to gorge navigation; and Chongqing is one of the upper Yangtze’s most important commercial distribution ports. The Chongqing–Yibin reach extends navigation into southern Sichuan, connecting at Yibin with overland trade routes toward Yunnan, Tibet, and Burma.

Gorges, rapids, and seasonal water-level changes made navigation between Yichang and Chongqing considerably more costly than downstream shipping. These difficulties did not isolate Chongqing from international trade. Instead, they reinforced its role in transshipment, warehousing, finance, and commodity distribution. Imports arriving from Shanghai were distributed to Sichuan and Yunnan, while regional products gathered here before moving downstream to Hankou and Shanghai.

On the map, this axis should use the thickest and most continuous water-transport line. Chongqing should receive the highest-ranking node symbol because the other three international corridor groups connect to this axis through Chongqing or its upstream nodes.

### 2. Chongqing–Yibin–Lijiang–Dali–Bhamo–Rangoon: the Yunnan–Burma–Indian Ocean corridor

**Route:**

`Chongqing–Yibin–Lijiang–Dali–Baoshan–Tengchong–Bhamo–Mandalay–Rangoon–Indian Ocean`

This route most clearly demonstrates Chongqing’s role as an interface with Indian Ocean trade. Goods travel by Yangtze shipping between Chongqing and Yibin. Beyond Yibin, continuously navigable waterways are unavailable, so cargo moves by mule caravans through southern Sichuan to Lijiang and Dali, then across Baoshan and Tengchong to Bhamo in Burma.

Bhamo occupies an important navigable position on the upper Irrawaddy and is a key transfer port between Yunnan caravans and Burmese river transport. Silk, tea, metalware, medicinal materials, and other goods from Yunnan enter Irrawaddy shipping here. Cotton, cotton yarn, textiles, and other imports from Burma, the Indian Ocean, and the British colonial trading system are transferred to pack animals for Dali, Lijiang, Yibin, and the Sichuan interior.

South of Bhamo, goods can follow the Irrawaddy to Mandalay, then use middle- and lower-river navigation and delta transport to reach Rangoon. Rangoon is the corridor’s maritime gateway, linked by Indian Ocean shipping to British India and wider world markets.

The route’s defining feature is the succession of transport-mode changes rather than a single continuous road:

`Yangtze shipping → Sichuan–Yunnan mule-caravan routes → transfer at Bhamo → Irrawaddy navigation → maritime shipping from Rangoon`

For mapping, use a solid Yangtze water-transport line for Chongqing–Yibin; a dashed caravan line for Yibin–Bhamo; a solid river line again for Bhamo–Rangoon; and a maritime arrow beyond Rangoon toward the Indian Ocean.

### 3. Chongqing–Yibin–Kunming–Mengzi–Haiphong: the Yunnan–Vietnam–Gulf of Tonkin corridor

**Route:**

`Chongqing–Yibin–Kunming–Mengzi–Manhao–Hekou/Lao Cai–Yen Bai–Hanoi–Haiphong–South China Sea`

This route connects the upper Yangtze with the Red River, Gulf of Tonkin, and South China Sea. Goods from Chongqing and Sichuan first reach Yibin by river, then travel overland through Sichuan and Yunnan to Kunming and Mengzi. Mengzi is an important market and customs node in southern Yunnan; Manhao is a major upstream head of navigation on the Red River. At Manhao, caravan cargo is transferred to wooden riverboats and carried downstream through Hekou, Lao Cai, Yen Bai, and Hanoi to Haiphong.

Compared with Bhamo, Manhao is closer to Kunming. The Red River consequently became an important seaward outlet for Yunnan in the late nineteenth century. Tin, copper, silk, and other Yunnan products traveled to Haiphong; Indian cotton yarn, salt, foreign textiles, and other imports moved from Haiphong and Hanoi upstream into Yunnan and could continue to Sichuan markets.

From Chongqing’s perspective, the route offers a third maritime outlet in addition to Shanghai and Rangoon:

- Shanghai leads to the East China Sea;
- Rangoon leads to the Indian Ocean;
- Haiphong leads to the Gulf of Tonkin and South China Sea.

Chongqing was thus not a one-directional inland port dependent solely on downstream Shanghai. Sichuan–Yunnan overland connections linked it to several maritime trading systems.

### 4. Chongqing–Chengdu–Batang–Zayul–Sadiya–Calcutta: the Sichuan–Tibet–Assam corridor

**Route:**

`Chongqing–Chengdu–Kangding/Tachienlu–Batang–Zayul–Sadiya–Dibrugarh–Guwahati–Sirajganj–Goalundo–Calcutta`

This route connects the upper Yangtze with eastern Tibet, Assam, the Brahmaputra, and the Bay of Bengal. Chongqing and Chengdu are linked by the Sichuan Basin’s internal land and water routes. From Chengdu, routes through Kangding and Batang enter the tea–horse trading network. Batang lies at a highland crossroads leading toward Chengdu, Lijiang, Lhasa, Zayul, and Sadiya and is an important transfer node for tea, horses, wool, musk, and other high-value, low-bulk commodities.

The mountain route from Batang through Zayul to Sadiya crosses complex watersheds between the upper Yangtze, Mekong, Salween, and Brahmaputra. At Sadiya, goods re-enter Brahmaputra navigation and descend through Assam and Bengal via Dibrugarh, Guwahati, Sirajganj, and Goalundo, eventually connecting with Calcutta and the Bay of Bengal.

Two historical layers must be distinguished:

- seasonal trade conducted by local merchants, Tibetans, and upland communities did exist;
- the continuous roads, railways, and large-scale modern transport schemes envisaged by British interests were not actually completed.

The GeoJSON therefore assigns this route low or medium-low certainty and depicts it with dashed lines or a broad approximate corridor. Its purpose is to show actual commercial orientations and geographical connections between Chongqing–Sichuan and South Asia, not to claim that a standardized international trunk route already existed.

### 5. Upper Irrawaddy–Sadiya branch

**Route:**

`Bhamo–Myitkyina–Nmai Hka basin–Hkamti Long–Sadiya`

This auxiliary branch connects the Yunnan–Burma corridor with Brahmaputra navigation. It shows that the Irrawaddy and Brahmaputra were not entirely separate transport systems: valleys, passes, and local trading routes north of Myitkyina could lead toward Sadiya in Assam.

Because the identification of historical places such as Hkamti Long, the positions of passes, and seasonal alignments remain uncertain, the branch should be shown only as a directional historical corridor, not a precise road. A lighter, thinner dashed line can indicate the lateral connection between the Yunnan–Burma and Sichuan–Tibet–Assam routes.

## IV. Relationship to the original route numbering

The dataset focuses on the following routes identified in earlier notes:

| Original route number | Original route theme | Representation in this dataset |
|---|---|---|
| Route 1 | Northern Brahmaputra–Yangtze route | Chongqing–Chengdu–Batang–Zayul–Sadiya–Calcutta |
| Route 2 | Brahmaputra–Irrawaddy circuit | Bhamo–Myitkyina–Hkamti Long–Sadiya branch, plus Bhamo–Mandalay–Rangoon main line |
| Route 5 | Red River route | Chongqing–Yibin–Kunming–Mengzi–Manhao–Hanoi–Haiphong |
| Route 6 | Yangtze–Yunnan–South Asia route | Shanghai–Chongqing Yangtze axis and extensions from Chongqing toward Bhamo and Sadiya |

Previously listed Route 3—the Salween–Chao Phraya–Chiang Mai–Bangkok/Moulmein route—is excluded from the principal data in these three GeoJSON files. This is deliberate: although useful for showing Yunnan’s Southeast Asian connections, its direct evidentiary link to Chongqing is weaker than those of the Yunnan–Burma and Yunnan–Vietnam routes. It could later be added as a separate layer for an expanded Yunnan-centered map.

## V. What the three GeoJSON files represent

### 1. `trade_nodes.geojson`: trade nodes

This is a **Point layer** containing 32 nodes. Node types include:

- international seaports;
- Yangtze and other river ports;
- upstream heads of navigation;
- land–water transshipment nodes;
- mule-caravan hubs;
- border markets and customs nodes;
- historical mountain relay areas.

Core fields:

| Field | Meaning |
|---|---|
| `node_id` | Unique node identifier linked to the route files |
| `name_zh` | Chinese name |
| `name_historical` | Historical English name or common older spelling around 1900 |
| `node_type` | Type, such as port, market, transfer point, or mountain passage |
| `hierarchy` | Node rank; smaller values indicate greater narrative importance |
| `narrative_role` | Function within the account of Chongqing’s international trade |
| `certainty` | Certainty of the historical place identification and coordinates |
| `source_pages` | Principal supporting pages in *The Range of the River* |

Chongqing has `node_type` = `river_port_trade_interface` and `hierarchy` = 0, making it the map’s sole highest-ranking node. Bhamo, Manhao, and Sadiya represent three important forms of inter-basin transshipment interface.

### 2. `trade_route_segments.geojson`: transport-route segments

This is a **LineString layer** with 24 segments. Rather than representing each international trading route as a continuous line of uniform character, it divides routes by transport mode and historical status.

For example, Chongqing–Rangoon is divided into:

1. Chongqing–Yibin: Yangtze shipping;
2. Yibin–Lijiang–Dali–Bhamo: mule-caravan transport;
3. Bhamo–Mandalay–Rangoon: Irrawaddy and delta navigation;
4. beyond Rangoon: connection to Indian Ocean maritime shipping.

Core fields:

| Field | Meaning |
|---|---|
| `route_group` | Larger route group |
| `segment_id` | Unique transport-segment identifier |
| `from_node` / `to_node` | Origin and destination, linked to the node file |
| `mode` | Transport mode, such as `river_main`, `river`, `caravan`, or `maritime` |
| `direction` | Commodity-flow direction; most entries are bidirectional |
| `route_status` | Status: actually used, seasonally used, difficult navigation, unrealized imperial scheme, etc. |
| `certainty` | Certainty of alignment and historical use |
| `commodity_examples` | Representative commodities |
| `source_pages` | Principal supporting historical-source pages |

This file is best suited to maps of transport modes and commodity flows. Classification by `route_group` distinguishes the Yangtze axis, Yunnan–Burma, Yunnan–Vietnam, and Sichuan–Tibet–Assam routes. Classification by `mode` highlights transitions between river and pack-animal transport.

### 3. `trade_corridors.geojson`: approximate historical corridors

This is also a **LineString layer**, but it does not represent precise road centerlines. It describes historical transport corridors based on the general directions, nodes, and basin relationships supported by the sources.

It contains four corridors:

1. upper Yangtze–western Yunnan–Bhamo;
2. Sichuan–Kunming–Mengzi–Red River;
3. Sichuan–Batang–Zayul–Sadiya;
4. upper Irrawaddy–Hkamti Long–Sadiya branch.

Core fields:

| Field | Meaning |
|---|---|
| `corridor_id` | Unique corridor identifier |
| `geometry_type` | Explicit designation as an approximate corridor centerline |
| `corridor_width_km` | Suggested display width to generate in mapping software |
| `route_status` | Character, such as local commercial use, seasonal use, or unrealized imperial infrastructure |
| `certainty` | Certainty of corridor location |
| `evidence` | Grounds for drawing the corridor and its principal limitations |
| `source_pages` | Supporting historical-source pages |

In QGIS, buffer the lines using `corridor_width_km` to create semi-transparent bands. This layer should not be compared directly with precise roads or modern highways, used to calculate historical travel distances, or used to identify particular passes.

## VI. Combining the three files

Each file answers a different question:

| File | Question |
|---|---|
| `trade_nodes.geojson` | Which ports, markets, and transfer points constitute the network? |
| `trade_route_segments.geojson` | By which transport modes did commodities move between nodes? |
| `trade_corridors.geojson` | Where precise routes cannot be reconstructed, in what general directions did historical trade develop? |

Suggested bottom-to-top layer order:

1. terrain and modern coastlines;
2. Yangtze and other major river systems;
3. `trade_corridors.geojson`, as broad, faint lines or buffered bands;
4. `trade_route_segments.geojson`, classified by transport mode;
5. `trade_nodes.geojson`, drawn last and labeled;
6. a top layer emphasizing Chongqing, with commodity-flow arrows and a legend.

## VII. Recommended cartographic styling

### Routes

- Yangtze shipping axis: thick, dark blue-green solid line;
- Irrawaddy and Brahmaputra navigation: slightly thinner blue-green solid lines;
- Red River navigation: green solid line;
- mule-caravan routes: ochre or purple dashed lines;
- maritime connections: blue solid lines with arrows;
- low-certainty routes or unrealized imperial schemes: pale purple dash-dot lines;
- historical corridors: broad bands at 20–30% transparency.

### Nodes

- Chongqing: the largest red or dark-orange node, with a pale outer ring;
- Shanghai, Rangoon, Haiphong, and Calcutta: large seaport symbols;
- Yichang, Yibin, Bhamo, Manhao, and Sadiya: transshipment symbols;
- ordinary river ports and caravan relay stations: medium or small circles.

The legend should explicitly explain that solid lines indicate water transport, dashed lines indicate overland or mule transport, and semi-transparent broad bands indicate approximate historical corridors rather than precisely reconstructed roads.

## VIII. Data accuracy and limitations

1. All coordinates use WGS 84, with longitude before latitude.
2. City coordinates generally identify modern centers or positions near identifiable historical sites.
3. Manhao, Hkamti Long, and the Zayul–Sadiya mountain route carry substantial positional uncertainty, recorded in their attributes.
4. River routes consist of historical nodes and schematic control points, not modern high-resolution river centerlines. For formal publication, replace them with authoritative hydrological data that have undergone topology checks.
5. Mountain trading routes commonly had several seasonal variants. This dataset represents directional corridors, not a single exclusive ancient road.
6. `route_status` must inform symbology. Routes actually used by local caravans must not receive the same line style as colonial railway or highway proposals that were never built.
7. The dataset supports regional-scale historical narrative maps. It is unsuitable for navigation, engineering analysis, large-scale archaeological site surveys, or judgments about modern administrative boundaries.

## IX. Principal historical sources

The main source is Iftekhar Iqbal, *The Range of the River: A Riverine History of Empire across China, India, and Southeast Asia*:

- pp. 24–29: Brahmaputra–Yangtze and Batang–Zayul–Sadiya routes;
- pp. 44–55: Bhamo, Myitkyina, and Irrawaddy–Yunnan trade;
- pp. 110–115: Mengzi, Manhao, Red River, and Haiphong routes;
- pp. 127–134: Shanghai–Chongqing–Yibin Yangtze axis and Yangtze–Yunnan–Burma connections;
- pp. 153–156: Yunnan mule transport, Bhamo–Dali routes, and inter-basin transshipment networks.

The materials most directly relevant to route reconstruction include travel accounts, route reports, and transport-history studies by Arthur Cotton, T. T. Cooper, Prince Henri d’Orléans, H. R. Davies, John Coryton, George Morrison, Andrew Forbes, and Nanny Kim.

## X. File list

- [`trade_nodes.geojson`](trade_nodes.geojson)
- [`trade_route_segments.geojson`](trade_route_segments.geojson)
- [`trade_corridors.geojson`](trade_corridors.geojson)

*Translation note: This guide translates the supplied Chinese documentation. Dataset counts, source-page references, uncertainty assessments, and relative links are retained as supplied; the three GeoJSON data files are not part of this translation deliverable.*
