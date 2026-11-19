# Mapping Portfolio

Cartography, historical GIS, interactive storytelling, and river photography by Yuanbo Cai.

**[Open the Mapping Portfolio](https://yuanbocai-hub.github.io/mapping-portfolio/)**

## The Yangtze as a river region

Reconstructing commodity patterns from a 1935 map to examine how production regions relate to the river network.

Hong Maoxi’s historical map puts seven commodity patterns onto a crowded sheet. I separated the symbols, reconstructed their geography, and redrew them alongside the Yangtze and its tributaries. The combined map shows how the patterns overlap; a seven-panel companion makes each commodity easier to inspect.

The project asks how dispersed areas of production might be connected through waterways, ports, and exchange. It also records the interpretive work behind the reconstruction: distinguishing colored outlines from filled regions, reviewing interrupted loops, and deciding what to show where symbols overlap.

**[Browse all portfolio projects](https://yuanbocai-hub.github.io/mapping-portfolio/)** · **[Open the Yangtze project](https://yuanbocai-hub.github.io/mapping-portfolio/yangtze.html)**

Related projects: [Corridors before Borders](https://yuanbocai-hub.github.io/mapping-portfolio/corridors.html) · [Following the Tsangpo](https://yuanbocai-hub.github.io/mapping-portfolio/tsangpo.html)

### Yangtze project languages

The project opens in English at `yangtze.html`. Its header links to the Chinese version, `yangtze-zh.html`, and back; switching preserves the current section. Both versions use the same photographs, maps, styles and interactive controls.

After changing English copy, update the matching strings in `scripts/yangtze-zh-translations.json`, then run `python3 scripts/build-yangtze-chinese.py`. This regenerates the Chinese page from the English structure and reports any untranslated text before writing. Edit the translation dictionary rather than editing the generated Chinese HTML directly.

## Principal work: the Yangtze commodity maps

[![Reconstructed Yangtze commodity regions](assets/yangtze-commodities.jpg)](Yangtze_Products_1930s_EN_HighRes15MB.jpg)

[Full-resolution map](Yangtze_Products_1930s_EN_HighRes15MB.jpg) · [Seven-panel companion](yangtze_seven_panels_hydro_EN_600dpi.png) · [Historical source reproduction](长江流域物产_原件.jpg)

Sugar, hemp, tobacco, tea, silk, cotton, and rice are shown against a clearer river network. The revised vector export has 91 features across seven classes. These are interpreted historical symbols, not measured agricultural parcels.

The portfolio page explains why light tints and interrupted bands were used, and develops a reflection on **形势 (xíngshì)** as a way of thinking about regional configurations. The source data preserve commodity overlaps; selected hemp segments are hidden only in the final presentation.

## Related study: drawing a navigation chart with Codex

[![Codex-assisted navigation chart for the crooked-stern junk](assets/wu-navigation.jpg)](歪屁股船英文_川江乌江航运体系_真实GIS版_EN_v10_400DPI.png)

I made this chart as an experiment in drawing with Codex. Codex assisted the plotting and layout, using historical route information from Worcester’s account. The chart follows transfers from the Yangtze into the Wu River system. The 71 difficult rapids refer to the Kung-t’an–Ssu-nan reach as a whole; Hsin-t’an is interpolated from historical distances. The layout uses non-uniform scaling.

### Upstream towing

[![Upstream towing: tracking beams, lifting line, and iron ring](assets/upstream.jpg)](assets/figures/upstream.png)

Bamboo towing lines attach to the tracking beams. A lifting line and iron ring raise the towing line over the bow when it changes sides. A separate shore line controls the boat’s distance from the bank. YUE-FAN adaptation of Worcester (1941), plates 10 and 18.

### Downstream steering

[![Downstream steering: elevated platform and long steering sweeps](assets/downstream.jpg)](assets/figures/downstream.png)

The elevated platform gives the stern operator room to work the long sweep. The raised stern provides a fulcrum and keeps the sweeps apart. YUE-FAN adaptation of Audemard (1963), volume 5, plate 30.

[Read the edited diagram annotations](notes/figure-annotations.md). Click either image to open the full figure.

## Comparative extension: the Pearl River

[![Pearl River and eastern Kuang-tung commodity map](assets/pearl-commodities.jpg)](Pearl_River_Eastern_Kuangtung_EN_HighRes.png)

[Full-resolution map](Pearl_River_Eastern_Kuangtung_EN_HighRes.png) · [Historical source reproduction](粤江流域物产_原件.jpg)

This reconstruction follows its own six-category legend. It retains breaks in the printed bands instead of forcing them into enclosed regions. Its 188 disconnected vector fragments describe pieces of ink, not 188 production areas.

## Methods and research notes

- [Commodity separation and reconstruction](METHODS.md)
- [Historical sources and reference geography](SOURCES.md)
- [Reflection on regional configurations](notes/regional-configurations.md)
- [Vessel inventory and Yangtze sections](Worcester_Junk_Inventory_and_Yangtze_Sections_EN.md)
- [Ports and their functions](Worcester_Yangtze_Ports_Five_Functional_Categories_and_Evidence_EN.md)
- [International trade-route dataset proposal](Chongqing_Yangtze_International_Trade_Routes_GeoJSON_Guide_EN.md)

The trade-route note describes a proposed dataset structure. The three GeoJSON datasets it references are not included here.

Cartography: Yuanbo Cai. Project illustrations: YUE-FAN Studio. Existing source credits remain in the images. See [rights and attribution](RIGHTS.md); this collection does not have a blanket reuse licence.
