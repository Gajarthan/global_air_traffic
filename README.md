# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_23:17:37_UTC-green)

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

**Latest saved flight:** 2026-09-08 23:17:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 23:17:37 UTC

- **252,118** saved flights
- **75,558** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,118** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,037,678.3 tonnes** estimated CO2 emissions
- **176,097,292 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10081 |
| 2 | SkyWest Airlines | 8808 |
| 3 | EJA | 4873 |
| 4 | IndiGo | 4222 |
| 5 | American Airlines | 4024 |
| 6 | Southwest Airlines | 3732 |
| 7 | Delta Air Lines | 3188 |
| 8 | ENY | 3012 |
| 9 | LATAM Airlines | 2425 |
| 10 | AZU | 2343 |
| 11 | Vueling | 2145 |
| 12 | WIF | 2019 |
| 13 | Lufthansa | 1991 |
| 14 | LXJ | 1967 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1693 |
| 17 | AXM | 1629 |
| 18 | QLK | 1619 |
| 19 | EJU | 1617 |
| 20 | United Airlines | 1573 |
| 21 | Alaska Airlines | 1503 |
| 22 | All Nippon Airways | 1474 |
| 23 | WMT | 1429 |
| 24 | GLO | 1399 |
| 25 | PGT | 1383 |
| 26 | VIV | 1379 |
| 27 | Air France | 1376 |
| 28 | Wizz Air | 1373 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1232 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209238 |
| 2 | 🇪🇸 ES | 16093 |
| 3 | 🇧🇷 BR | 14697 |
| 4 | 🇦🇺 AU | 14323 |
| 5 | 🇨🇦 CA | 14010 |
| 6 | 🇮🇹 IT | 13793 |
| 7 | 🇮🇳 IN | 13192 |
| 8 | 🇩🇪 DE | 12365 |
| 9 | 🇬🇧 GB | 11801 |
| 10 | 🇨🇴 CO | 11127 |
| 11 | 🇫🇷 FR | 10139 |
| 12 | 🇯🇵 JP | 9906 |
| 13 | 🇹🇷 TR | 7541 |
| 14 | 🇬🇷 GR | 7395 |
| 15 | 🇲🇽 MX | 6955 |
| 16 | 🇨🇭 CH | 6796 |
| 17 | 🇳🇴 NO | 6241 |
| 18 | 🇹🇭 TH | 4538 |
| 19 | 🇲🇾 MY | 4379 |
| 20 | 🇿🇦 ZA | 4321 |
| 21 | 🇵🇱 PL | 4198 |
| 22 | 🇳🇿 NZ | 3442 |
| 23 | 🇵🇭 PH | 3412 |
| 24 | 🇬🇹 GT | 3141 |
| 25 | 🇰🇷 KR | 2909 |
| 26 | 🇭🇷 HR | 2898 |
| 27 | 🇲🇦 MA | 2548 |
| 28 | 🇲🇪 ME | 2372 |
| 29 | 🇳🇱 NL | 2273 |
| 30 | 🇮🇩 ID | 2153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5204 |
| 2 | Denver International Airport |  | US | 4078 |
| 3 | Indira Gandhi International Airport |  | IN | 3063 |
| 4 | Tokyo International Airport |  | JP | 2955 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2678 |
| 7 | Zurich Airport |  | CH | 2639 |
| 8 | El Dorado International Airport |  | CO | 2568 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2556 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2489 |
| 11 | La Aurora Airport |  | GT | 2396 |
| 12 | Salt Lake City International Airport |  | US | 2227 |
| 13 | Chicago O'Hare International Airport |  | US | 2199 |
| 14 | Congonhas Airport |  | BR | 2154 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2072 |
| 16 | Capua Airport |  | IT | 1987 |
| 17 | Madrid Barajas International Airport |  | ES | 1980 |
| 18 | Frankfurt am Main International Airport |  | DE | 1961 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1888 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1833 |
| 21 | Malpensa International Airport |  | IT | 1812 |
| 22 | Charles de Gaulle International Airport |  | FR | 1769 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1757 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1678 |
| 26 | Ninoy Aquino International Airport |  | PH | 1666 |
| 27 | Macau International Airport |  | MO | 1662 |
| 28 | Barcelona International Airport |  | ES | 1590 |
| 29 | Charlotte/Douglas International Airport |  | US | 1589 |
| 30 | Kuala Lumpur International Airport |  | MY | 1577 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1549 |
| 32 | Viracopos International Airport |  | BR | 1506 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1462 |
| 35 | Don Mueang International Airport |  | TH | 1453 |
| 36 | Calgary International Airport |  | CA | 1452 |
| 37 | Bengaluru International Airport |  | IN | 1438 |
| 38 | Oslo Gardermoen Airport |  | NO | 1421 |
| 39 | Vancouver International Airport |  | CA | 1411 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1363 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 935 | 21m | 244 km | 3,937.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 672 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 632 | 1h 6m | 770 km | 8,395.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 396 | 44m | 555 km | 3,791.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 376 | 44m | 241 km | 1,561.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 351 | 24m | 218 km | 1,322.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 294 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 273 | 1h 50m | 1,304 km | 6,141.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 261 | 41m | 535 km | 2,410.5 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KSF33 | KSF | 5PA9 (5PA9) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-09-08 22:49 UTC | 2026-09-08 23:17 UTC | 28m |
| WMU70 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-09-08 22:13 UTC | 2026-09-08 23:15 UTC | 1h 2m |
| ZKIEN | ZKI | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-09-08 22:23 UTC | 2026-09-08 23:15 UTC | 51m |
| N215LP |  | Pocono Mountains Regional Airport (KMPO) | Lehigh Valley International Airport (KABE) | 2026-09-08 22:48 UTC | 2026-09-08 23:10 UTC | 21m |
| CLX9932 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-09-08 12:16 UTC | 2026-09-08 23:09 UTC | 10h 52m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-08 22:26 UTC | 2026-09-08 23:07 UTC | 41m |
| OXM | OXM | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-08 22:53 UTC | 2026-09-08 23:06 UTC | 13m |
| BDA481 | BDA | Indira Gandhi International Airport (VIDP) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 19:54 UTC | 2026-09-08 23:03 UTC | 3h 9m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-08 22:48 UTC | 2026-09-08 23:01 UTC | 13m |
| SGA2554 | SGA | Damascus International Airport (OSDI) | Macau International Airport (VMMC) | 2026-09-08 09:25 UTC | 2026-09-08 23:01 UTC | 13h 36m |
| N9544X |  | Arlington Municipal Airport (KAWO) | William R Fairchild International Airport (KCLM) | 2026-09-08 22:31 UTC | 2026-09-08 23:01 UTC | 30m |
| GFA056 | Gulf Air | Bahrain International Airport (OBBI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 19:54 UTC | 2026-09-08 23:00 UTC | 3h 6m |
| IGO1202 | IndiGo | Bahrain International Airport (OBBI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 20:01 UTC | 2026-09-08 22:59 UTC | 2h 57m |
| N2624N |  | Lawrence Municipal Airport (KLWM) | Boire Field (KASH) | 2026-09-08 22:39 UTC | 2026-09-08 22:58 UTC | 18m |
| N560JW |  | David Wayne Hooks Memorial Airport (KDWH) | Z M Jack Stell Field (KCRT) | 2026-09-08 22:00 UTC | 2026-09-08 22:53 UTC | 53m |
| IGO6140 | IndiGo | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-08 21:32 UTC | 2026-09-08 22:52 UTC | 1h 20m |
| EB723 |  | Whiting Field Nas South Airport (KNDZ) | Collier/Pine Barren Airpark (FD89) | 2026-09-08 22:33 UTC | 2026-09-08 22:50 UTC | 17m |
| N298PC |  | Olympia Regional Airport (KOLM) | Mahlon Sweet Field (KEUG) | 2026-09-08 22:13 UTC | 2026-09-08 22:49 UTC | 35m |
| VIR358 | Virgin Atlantic | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 14:17 UTC | 2026-09-08 22:46 UTC | 8h 29m |
| N113VG |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-09-08 22:26 UTC | 2026-09-08 22:46 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
