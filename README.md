# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_06:32:26_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-09-23 06:32:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 06:32:26 UTC

- **267,027** saved flights
- **78,499** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,027** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,238,675.5 tonnes** estimated CO2 emissions
- **187,749,302 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10543 |
| 2 | SkyWest Airlines | 9290 |
| 3 | EJA | 5192 |
| 4 | IndiGo | 4480 |
| 5 | American Airlines | 4162 |
| 6 | Southwest Airlines | 3930 |
| 7 | Delta Air Lines | 3321 |
| 8 | ENY | 3139 |
| 9 | LATAM Airlines | 2577 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2239 |
| 12 | WIF | 2163 |
| 13 | LXJ | 2095 |
| 14 | Lufthansa | 2042 |
| 15 | easyJet | 1792 |
| 16 | Swiss International | 1758 |
| 17 | QLK | 1722 |
| 18 | EJU | 1684 |
| 19 | AXM | 1671 |
| 20 | United Airlines | 1638 |
| 21 | Alaska Airlines | 1580 |
| 22 | All Nippon Airways | 1541 |
| 23 | PGT | 1504 |
| 24 | WMT | 1499 |
| 25 | GLO | 1491 |
| 26 | Air France | 1467 |
| 27 | VIV | 1461 |
| 28 | Wizz Air | 1452 |
| 29 | CXK | 1299 |
| 30 | AEE | 1286 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221980 |
| 2 | 🇪🇸 ES | 16766 |
| 3 | 🇧🇷 BR | 15628 |
| 4 | 🇦🇺 AU | 15354 |
| 5 | 🇨🇦 CA | 14884 |
| 6 | 🇮🇹 IT | 14510 |
| 7 | 🇮🇳 IN | 14169 |
| 8 | 🇩🇪 DE | 12842 |
| 9 | 🇬🇧 GB | 12379 |
| 10 | 🇨🇴 CO | 12188 |
| 11 | 🇫🇷 FR | 10649 |
| 12 | 🇯🇵 JP | 10294 |
| 13 | 🇹🇷 TR | 8086 |
| 14 | 🇬🇷 GR | 7721 |
| 15 | 🇲🇽 MX | 7365 |
| 16 | 🇨🇭 CH | 7117 |
| 17 | 🇳🇴 NO | 6607 |
| 18 | 🇹🇭 TH | 4792 |
| 19 | 🇲🇾 MY | 4506 |
| 20 | 🇿🇦 ZA | 4470 |
| 21 | 🇵🇱 PL | 4383 |
| 22 | 🇳🇿 NZ | 3726 |
| 23 | 🇵🇭 PH | 3547 |
| 24 | 🇬🇹 GT | 3386 |
| 25 | 🇭🇷 HR | 3042 |
| 26 | 🇰🇷 KR | 3029 |
| 27 | 🇲🇦 MA | 2663 |
| 28 | 🇲🇪 ME | 2502 |
| 29 | 🇳🇱 NL | 2387 |
| 30 | 🇮🇩 ID | 2230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5441 |
| 2 | Denver International Airport |  | US | 4339 |
| 3 | Indira Gandhi International Airport |  | IN | 3204 |
| 4 | Tokyo International Airport |  | JP | 3078 |
| 5 | El Dorado International Airport |  | CO | 2873 |
| 6 | Harry Reid International Airport |  | US | 2855 |
| 7 | Guaymaral Airport |  | CO | 2800 |
| 8 | Zurich Airport |  | CH | 2776 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2677 |
| 10 | La Aurora Airport |  | GT | 2572 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2570 |
| 12 | Salt Lake City International Airport |  | US | 2357 |
| 13 | Chicago O'Hare International Airport |  | US | 2293 |
| 14 | Congonhas Airport |  | BR | 2276 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2181 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2053 |
| 18 | Frankfurt am Main International Airport |  | DE | 2031 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1924 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1904 |
| 22 | Charles de Gaulle International Airport |  | FR | 1894 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1874 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1873 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1813 |
| 26 | Macau International Airport |  | MO | 1778 |
| 27 | Ninoy Aquino International Airport |  | PH | 1741 |
| 28 | Charlotte/Douglas International Airport |  | US | 1666 |
| 29 | Barcelona International Airport |  | ES | 1664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1614 |
| 33 | Seattle-Tacoma International Airport |  | US | 1565 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1562 |
| 35 | Calgary International Airport |  | CA | 1527 |
| 36 | Don Mueang International Airport |  | TH | 1517 |
| 37 | Bengaluru International Airport |  | IN | 1509 |
| 38 | Oslo Gardermoen Airport |  | NO | 1502 |
| 39 | Vancouver International Airport |  | CA | 1497 |
| 40 | Antalya International Airport |  | TR | 1428 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1117 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1001 | 21m | 244 km | 4,214.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 672 | 1h 6m | 770 km | 8,927.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 594 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 406 | 44m | 241 km | 1,686.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 341 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 335 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 331 | 26m | 215 km | 1,225.9 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 282 | 18m | 14 km | 70.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZDM | ZDM | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 2026-09-23 05:28 UTC | 2026-09-23 06:32 UTC | 1h 4m |
| IGO357L | IndiGo | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-09-23 04:57 UTC | 2026-09-23 06:26 UTC | 1h 28m |
| XAMSL | XAM | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-09-23 05:46 UTC | 2026-09-23 06:16 UTC | 30m |
| ETH644 | Ethiopian Airlines | Yaounde Nsimalen International Airport (FKYS) | Macau International Airport (VMMC) | 2026-09-22 11:56 UTC | 2026-09-23 06:12 UTC | 18h 15m |
| WPH | WPH | Lismore Airport (YLIS) | Brisbane Archerfield Airport (YBAF) | 2026-09-23 05:43 UTC | 2026-09-23 06:07 UTC | 24m |
| ICL982 | ICL | John F Kennedy International Airport (KJFK) | Ben Gurion International Airport (LLBG) | 2026-09-22 20:50 UTC | 2026-09-23 06:06 UTC | 9h 15m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-09-23 05:37 UTC | 2026-09-23 06:03 UTC | 26m |
| BLINR47 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-09-23 05:38 UTC | 2026-09-23 05:58 UTC | 20m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-09-23 05:20 UTC | 2026-09-23 05:52 UTC | 32m |
| DICCB | DIC | Mannheim-City Airport (EDFM) | Zurich Airport (LSZH) | 2026-09-23 05:16 UTC | 2026-09-23 05:50 UTC | 34m |
| N3386E |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-09-23 04:30 UTC | 2026-09-23 05:49 UTC | 1h 19m |
| JST415 | JST | Gold Coast Airport (YBCG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-23 04:47 UTC | 2026-09-23 05:49 UTC | 1h 1m |
| TBA9701 | TBA | Wuzhou Xijiang Airport (ZGWZ) | Zhuhai Airport (ZGSD) | 2026-09-23 05:23 UTC | 2026-09-23 05:47 UTC | 23m |
| WMT20 | WMT | Torino / Caselle International Airport (LIMF) | Bilbao Airport (LEBB) | 2026-09-23 04:26 UTC | 2026-09-23 05:45 UTC | 1h 19m |
| HBZTO | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-09-23 05:21 UTC | 2026-09-23 05:45 UTC | 23m |
| N117TF |  | Frederick W Smith International/Memphis Airport (KMEM) | Mc Elroy Airfield (K20V) | 2026-09-23 03:47 UTC | 2026-09-23 05:42 UTC | 1h 55m |
| MAL8062 | MAL | Toronto Pearson International Airport (CYYZ) | Havelock Airport (CCS5) | 2026-09-23 04:23 UTC | 2026-09-23 05:41 UTC | 1h 17m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-09-23 04:49 UTC | 2026-09-23 05:41 UTC | 51m |
| GNS100 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-23 05:29 UTC | 2026-09-23 05:40 UTC | 11m |
| PFU | PFU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-23 05:15 UTC | 2026-09-23 05:39 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
