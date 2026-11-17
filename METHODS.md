# Separating commodities from historical map symbols

This account was checked against the saved registration, extraction, correction, and final-layout records on 17 November 2026. The Yangtze and Pearl River projects use different representations. Their feature counts describe different kinds of objects.

## Why color alone was insufficient

The historical maps combine colored bands, fills, and textures. Several commodities overlap, while fading, overprinting, text, and reference geography complicate extraction. Similar colors can have different meanings: red sugar patches and railways, purple tea and hemp outlines, or green tobacco texture and water tint.

Extraction combined color tests with local texture density, reviewed windows, and comparison with the supplied classification samples. The windows restricted where a color could be interpreted as a commodity. They did not turn the procedure into an independent measure of historical production.

## Yangtze: interpreting regions

The main map was registered using seven graticule points for fitting and two independent grid checks. A constrained quadratic model accommodated scan distortion. Legends, paper margins, the mineral inset, and the river-defence inset were excluded from the main commodity regions.

Sugar, tobacco, and tea were extracted from filled or textured marks. Hemp, silk, cotton, and rice were interpreted as areas enclosed by printed loops. Short interruptions were closed locally; longer missing portions were inferred from visible contours within reviewed windows. Inferred boundary segments were saved separately for inspection.

Review changed the geometry. Four fragmented hemp polygons were replaced by two continuous loops, including the Chengdu loop crossing the sugar patch. Two rice fragments across Hubei and Hunan were joined. The current tea edit state and a tobacco deletion were included in the final GeoJSON export.

| Commodity | Final features |
|---|---:|
| Sugar | 2 |
| Hemp | 2 |
| Tobacco | 44 |
| Tea | 19 |
| Silk | 10 |
| Cotton | 5 |
| Rice | 9 |
| Total | 91 |

The earlier extraction had 95 features. The 91-feature export supersedes that count. Commodity layers retain their overlaps and were not forced into mutually exclusive zones.

The final layout selectively hides hemp segments where they compete with other symbols. That is a presentation choice. The source geometries retain the overlapping regions, so an omitted segment in the rendered map cannot establish an absence of hemp production.

## Pearl River: preserving the marks

The whole continuous main view was registered, including its coverage beyond the modern drainage basin. Separate insets, the legend, and the title frame were excluded from the extraction.

Rice, sugar, silk, and tussah silk retain the widths and natural breaks of the printed bands. Tea and tobacco retain their filled or textured patches. Separate fragments were not joined by long gap bridges. Silk edges were smoothed within each component without connecting components.

| Commodity | Disconnected fragments |
|---|---:|
| Tussah silk | 8 |
| Tobacco | 9 |
| Sugar | 67 |
| Silk | 21 |
| Tea | 16 |
| Rice | 67 |
| Total | 188 |

These are fragments of source symbols, not counts of agricultural regions. A band can be stored as a valid Polygon or MultiPolygon while retaining interruptions along its path. Filling its large interior holes would change what the geometry represents.

“Natural gaps” refers to discontinuities in the printed bands. It does not refer to Jenks Natural Breaks or a statistical classification of production values.

## What the accuracy checks establish

| Check | Recorded result | Interpretation |
|---|---|---|
| Yangtze independent graticule checks | RMSE ≈ 7.45 source pixels; ≈ 7.1 km | Registration check, not absolute historical accuracy |
| Pearl River held-out graticule comparison | RMSE ≈ 8.6 source pixels | Model comparison before the final refit |
| Pearl River final internal graticule fit | RMSE ≈ 3.2 source pixels | Internal fit using all seven controls |
| Pearl River comparison with 13 historical city symbols | RMSE ≈ 20.7 km | Includes schematic geography, symbol displacement, matching, and scan effects |

The city-symbol check was not used to fit the Pearl River transformation. Areas beyond the fitted graticule range involve extrapolation. WGS84 coordinates support GIS exchange; they do not establish a precise transformation from a known historical datum. Neither commodity dataset should be used to calculate actual cultivated area.

## Record trail

The following saved records informed this account. They remain with the working GIS materials and are not bundled here as a fully reproducible processing pipeline.

- `配准与七类区域成果/使用说明与精度说明.txt` and `复现与像素证据/build_zones.py`
- `配准与七类区域成果/麻米大面修正版_v2/修正记录.json`
- `完整七类_GeoJSON/使用说明.txt` and `导出来源与核查.json`
- `粤江流域形势_主视图配准/使用与精度说明.txt`
- `粤江流域形势_物产GeoJSON_自然断口/使用说明.txt`, `提取与核验记录.json`, and `技术记录/extract_natural_masks.py`
- `长江绘图最新/麻美化版/版本说明.txt`

See [SOURCES.md](SOURCES.md) for the distinction between historical thematic material and later reference geography.
