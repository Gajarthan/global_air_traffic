# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_02:40:25_UTC-green)

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

**Latest saved flight:** 2026-08-24 02:40:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 02:40:25 UTC

- **230,726** saved flights
- **71,173** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,726** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,782,019.2 tonnes** estimated CO2 emissions
- **161,276,474 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9252 |
| 2 | SkyWest Airlines | 8202 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3889 |
| 5 | American Airlines | 3784 |
| 6 | Southwest Airlines | 3571 |
| 7 | Delta Air Lines | 2956 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2223 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1823 |
| 14 | WIF | 1813 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1526 |
| 18 | EJU | 1470 |
| 19 | United Airlines | 1469 |
| 20 | QLK | 1454 |
| 21 | Alaska Airlines | 1390 |
| 22 | All Nippon Airways | 1373 |
| 23 | GLO | 1289 |
| 24 | VIV | 1270 |
| 25 | WMT | 1262 |
| 26 | PGT | 1261 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1150 |
| 30 | AEE | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192721 |
| 2 | 🇪🇸 ES | 14784 |
| 3 | 🇧🇷 BR | 13512 |
| 4 | 🇦🇺 AU | 13035 |
| 5 | 🇨🇦 CA | 12742 |
| 6 | 🇮🇹 IT | 12477 |
| 7 | 🇮🇳 IN | 12114 |
| 8 | 🇩🇪 DE | 11331 |
| 9 | 🇬🇧 GB | 10847 |
| 10 | 🇨🇴 CO | 9601 |
| 11 | 🇯🇵 JP | 9341 |
| 12 | 🇫🇷 FR | 9220 |
| 13 | 🇹🇷 TR | 6808 |
| 14 | 🇬🇷 GR | 6771 |
| 15 | 🇲🇽 MX | 6424 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5659 |
| 18 | 🇲🇾 MY | 4079 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 4004 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3195 |
| 23 | 🇵🇭 PH | 3159 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2710 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2338 |
| 28 | 🇲🇪 ME | 2112 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1992 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3759 |
| 3 | Indira Gandhi International Airport |  | IN | 2805 |
| 4 | Tokyo International Airport |  | JP | 2789 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2489 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2143 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2036 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1957 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1736 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1718 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1655 |
| 22 | Malpensa International Airport |  | IT | 1649 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1618 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1518 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1477 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1399 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Seattle-Tacoma International Airport |  | US | 1360 |
| 34 | Bengaluru International Airport |  | IN | 1359 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1357 |
| 36 | Calgary International Airport |  | CA | 1314 |
| 37 | Don Mueang International Airport |  | TH | 1309 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vitoria/Foronda Airport |  | ES | 1252 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 840 | 21m | 244 km | 3,537.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 579 | 1h 6m | 770 km | 7,691.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 572 | 24m | 225 km | 2,219.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 354 | 1h 50m | 1,423 km | 8,687.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 299 | 1h 38m | 1,156 km | 5,964.9 t |
| 17 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 273 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 242 | 15m | 154 km | 641.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HGB702 | HGB | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-08-24 01:19 UTC | 2026-08-24 02:40 UTC | 1h 20m |
| TLM394 | TLM | Don Mueang International Airport (VTBD) | Hsinchu Air Base (RCPO) | 2026-08-23 23:20 UTC | 2026-08-24 02:29 UTC | 3h 8m |
| N539SH |  | Healy River Airport (PAHV) | Healy River Airport (PAHV) | 2026-08-24 01:16 UTC | 2026-08-24 02:26 UTC | 1h 10m |
| NINJA91 | NIN | Atsugi Naval Air Facility (RJTA) | Atsugi Naval Air Facility (RJTA) | 2026-08-24 00:08 UTC | 2026-08-24 02:25 UTC | 2h 16m |
| N991MH |  | Rollins Airport (GA53) | Rollins Airport (GA53) | 2026-08-24 01:38 UTC | 2026-08-24 02:20 UTC | 42m |
| N889CE |  | Salt Lake City International Airport (KSLC) | NV13 (NV13) | 2026-08-24 01:23 UTC | 2026-08-24 02:19 UTC | 55m |
| TKR136 | TKR | Boise Air Trml/Gowen Field (KBOI) | Bald Mountain Airport (OG45) | 2026-08-24 01:58 UTC | 2026-08-24 02:17 UTC | 19m |
| EQV | EQV | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-24 01:29 UTC | 2026-08-24 02:07 UTC | 37m |
| TKR910 | TKR | Grant County International Airport (KMWH) | Rugg Ranches Airport (45OG) | 2026-08-24 01:45 UTC | 2026-08-24 02:01 UTC | 16m |
| N566VR |  | Aurora State Airport (KUAO) | Hoverhawk Ranch Airport (WN17) | 2026-08-24 01:32 UTC | 2026-08-24 02:00 UTC | 28m |
| ETD440 | Etihad Airways | Al Bateen Executive Airport (OMAD) | Naypyidaw Airport (VYEL) | 2026-08-23 20:45 UTC | 2026-08-24 01:56 UTC | 5h 11m |
| N245DJ |  | Bob Hope Airport (KBUR) | Moffett Federal Airfield (KNUQ) | 2026-08-24 01:05 UTC | 2026-08-24 01:55 UTC | 50m |
| USC240 | USC | Portland International Airport (KPDX) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-24 00:29 UTC | 2026-08-24 01:53 UTC | 1h 24m |
| TEXSIL | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-08-24 01:06 UTC | 2026-08-24 01:52 UTC | 45m |
| N42TX |  | Pegasus Airpark (5AZ3) | Las Cruces International Airport (KLRU) | 2026-08-24 00:16 UTC | 2026-08-24 01:52 UTC | 1h 35m |
| NSE8722 | NSE | El Dorado International Airport (SKBO) | SKSR (SKSR) | 2026-08-24 00:45 UTC | 2026-08-24 01:50 UTC | 1h 4m |
| N706RM |  | Thomaston-Upson County Airport (KOPN) | 84OL (84OL) | 2026-08-24 00:01 UTC | 2026-08-24 01:37 UTC | 1h 36m |
| JJP125 | JJP | Narita International Airport (RJAA) | New Chitose Airport (RJCC) | 2026-08-24 00:06 UTC | 2026-08-24 01:35 UTC | 1h 29m |
| IGO6633 | IndiGo | Bengaluru International Airport (VOBL) | Ambala Air Force Station (VIAM) | 2026-08-23 23:13 UTC | 2026-08-24 01:35 UTC | 2h 22m |
| SWA4620 | Southwest Airlines | Salt Lake City International Airport (KSLC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-24 00:09 UTC | 2026-08-24 01:34 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
