# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_01:22:59_UTC-green)

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

**Latest saved flight:** 2026-09-14 01:22:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-14 01:22:59 UTC

- **258,108** saved flights
- **76,776** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,108** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,124,290.1 tonnes** estimated CO2 emissions
- **181,118,269 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10250 |
| 2 | SkyWest Airlines | 8996 |
| 3 | EJA | 5005 |
| 4 | IndiGo | 4330 |
| 5 | American Airlines | 4080 |
| 6 | Southwest Airlines | 3801 |
| 7 | Delta Air Lines | 3232 |
| 8 | ENY | 3061 |
| 9 | LATAM Airlines | 2484 |
| 10 | AZU | 2415 |
| 11 | Vueling | 2183 |
| 12 | WIF | 2070 |
| 13 | LXJ | 2018 |
| 14 | Lufthansa | 2016 |
| 15 | easyJet | 1761 |
| 16 | Swiss International | 1724 |
| 17 | QLK | 1664 |
| 18 | AXM | 1647 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1531 |
| 22 | All Nippon Airways | 1498 |
| 23 | WMT | 1456 |
| 24 | GLO | 1439 |
| 25 | PGT | 1433 |
| 26 | VIV | 1410 |
| 27 | Air France | 1409 |
| 28 | Wizz Air | 1402 |
| 29 | JetBlue | 1249 |
| 30 | TKR | 1248 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214331 |
| 2 | 🇪🇸 ES | 16369 |
| 3 | 🇧🇷 BR | 15085 |
| 4 | 🇦🇺 AU | 14709 |
| 5 | 🇨🇦 CA | 14371 |
| 6 | 🇮🇹 IT | 14068 |
| 7 | 🇮🇳 IN | 13599 |
| 8 | 🇩🇪 DE | 12561 |
| 9 | 🇬🇧 GB | 12029 |
| 10 | 🇨🇴 CO | 11582 |
| 11 | 🇫🇷 FR | 10367 |
| 12 | 🇯🇵 JP | 10059 |
| 13 | 🇹🇷 TR | 7767 |
| 14 | 🇬🇷 GR | 7516 |
| 15 | 🇲🇽 MX | 7117 |
| 16 | 🇨🇭 CH | 6919 |
| 17 | 🇳🇴 NO | 6375 |
| 18 | 🇹🇭 TH | 4640 |
| 19 | 🇲🇾 MY | 4429 |
| 20 | 🇿🇦 ZA | 4388 |
| 21 | 🇵🇱 PL | 4275 |
| 22 | 🇳🇿 NZ | 3570 |
| 23 | 🇵🇭 PH | 3472 |
| 24 | 🇬🇹 GT | 3263 |
| 25 | 🇭🇷 HR | 2963 |
| 26 | 🇰🇷 KR | 2949 |
| 27 | 🇲🇦 MA | 2592 |
| 28 | 🇲🇪 ME | 2427 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5296 |
| 2 | Denver International Airport |  | US | 4176 |
| 3 | Indira Gandhi International Airport |  | IN | 3118 |
| 4 | Tokyo International Airport |  | JP | 3001 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2739 |
| 7 | Zurich Airport |  | CH | 2702 |
| 8 | El Dorado International Airport |  | CO | 2696 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2603 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2518 |
| 11 | La Aurora Airport |  | GT | 2479 |
| 12 | Salt Lake City International Airport |  | US | 2276 |
| 13 | Chicago O'Hare International Airport |  | US | 2246 |
| 14 | Congonhas Airport |  | BR | 2212 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2112 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2011 |
| 18 | Frankfurt am Main International Airport |  | DE | 1989 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1939 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1862 |
| 21 | Malpensa International Airport |  | IT | 1856 |
| 22 | Charles de Gaulle International Airport |  | FR | 1819 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1816 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1786 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1751 |
| 26 | Macau International Airport |  | MO | 1710 |
| 27 | Ninoy Aquino International Airport |  | PH | 1700 |
| 28 | Barcelona International Airport |  | ES | 1620 |
| 29 | Charlotte/Douglas International Airport |  | US | 1616 |
| 30 | Kuala Lumpur International Airport |  | MY | 1594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1583 |
| 32 | Viracopos International Airport |  | BR | 1554 |
| 33 | Seattle-Tacoma International Airport |  | US | 1516 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1507 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1477 |
| 37 | Bengaluru International Airport |  | IN | 1465 |
| 38 | Oslo Gardermoen Airport |  | NO | 1455 |
| 39 | Vancouver International Airport |  | CA | 1448 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 695 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 647 | 1h 6m | 770 km | 8,594.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 577 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 390 | 44m | 241 km | 1,620.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 361 | 24m | 218 km | 1,360.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 319 | 26m | 215 km | 1,181.4 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 315 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 308 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 276 | 1h 50m | 1,304 km | 6,209.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N803CP |  | Martin State Airport (KMTN) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-09-14 00:48 UTC | 2026-09-14 01:22 UTC | 34m |
| MJF19E | MJF | London Luton Airport (EGGW) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 16:27 UTC | 2026-09-14 01:20 UTC | 8h 52m |
| N6382D |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-09-13 23:39 UTC | 2026-09-14 01:17 UTC | 1h 38m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-09-13 18:19 UTC | 2026-09-14 01:15 UTC | 6h 56m |
| ZFO | ZFO | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-14 00:46 UTC | 2026-09-14 01:14 UTC | 27m |
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-14 00:45 UTC | 2026-09-14 01:13 UTC | 28m |
| TRF581 | TRF | Conroe/North Houston Regional Airport (KCXO) | Bass Breeze Ranch Airport (0TS5) | 2026-09-14 00:21 UTC | 2026-09-14 01:04 UTC | 42m |
| QTR90A | Qatar Airways | Hamad International Airport (OTHH) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 22:19 UTC | 2026-09-14 01:02 UTC | 2h 42m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-14 00:53 UTC | 2026-09-14 01:00 UTC | 7m |
| EJM736 | EJM | Edmonton International Airport (CYEG) | Scottsdale Airport (KSDL) | 2026-09-13 21:50 UTC | 2026-09-14 00:57 UTC | 3h 7m |
| CPA624 | Cathay Pacific | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-09-13 20:13 UTC | 2026-09-14 00:55 UTC | 4h 42m |
| N46090 |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Orlando Executive Airport (KORL) | 2026-09-14 00:05 UTC | 2026-09-14 00:51 UTC | 46m |
| N42SH |  | Sacramento Executive Airport (KSAC) | Silver Creek Ranch Airport (41CA) | 2026-09-13 23:55 UTC | 2026-09-14 00:50 UTC | 55m |
| SKW6269 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Santa Fe Regional Airport (KSAF) | 2026-09-13 23:57 UTC | 2026-09-14 00:48 UTC | 51m |
| N7255T |  | David G Joyce Airport (K0R5) | Shreveport Downtown Airport (KDTN) | 2026-09-14 00:19 UTC | 2026-09-14 00:48 UTC | 29m |
| YGN | YGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-14 00:09 UTC | 2026-09-14 00:45 UTC | 36m |
| N739AT |  | Chino Airport (KCNO) | Ramona Airport (KRNM) | 2026-09-13 23:55 UTC | 2026-09-14 00:45 UTC | 50m |
| XKV | XKV | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-13 23:59 UTC | 2026-09-14 00:42 UTC | 43m |
| JA01HR |  | Okadama Airport (RJCO) | Asahikawa Airport (RJEC) | 2026-09-14 00:28 UTC | 2026-09-14 00:41 UTC | 12m |
| EJA422 | EJA | Laurence G Hanscom Field (KBED) | Lehigh Valley International Airport (KABE) | 2026-09-13 23:49 UTC | 2026-09-14 00:39 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
