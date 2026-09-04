# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_13:13:41_UTC-green)

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

**Latest saved flight:** 2026-09-04 13:13:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 13:13:41 UTC

- **246,957** saved flights
- **74,484** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,957** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,971,192.6 tonnes** estimated CO2 emissions
- **172,243,049 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9898 |
| 2 | SkyWest Airlines | 8630 |
| 3 | EJA | 4760 |
| 4 | IndiGo | 4130 |
| 5 | American Airlines | 3963 |
| 6 | Southwest Airlines | 3682 |
| 7 | Delta Air Lines | 3133 |
| 8 | ENY | 2952 |
| 9 | LATAM Airlines | 2383 |
| 10 | AZU | 2296 |
| 11 | Vueling | 2113 |
| 12 | WIF | 1977 |
| 13 | Lufthansa | 1969 |
| 14 | LXJ | 1913 |
| 15 | easyJet | 1712 |
| 16 | Swiss International | 1659 |
| 17 | AXM | 1619 |
| 18 | EJU | 1588 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1553 |
| 21 | Alaska Airlines | 1476 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1391 |
| 24 | GLO | 1378 |
| 25 | VIV | 1356 |
| 26 | PGT | 1353 |
| 27 | Air France | 1349 |
| 28 | Wizz Air | 1336 |
| 29 | JetBlue | 1217 |
| 30 | AEE | 1215 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204689 |
| 2 | 🇪🇸 ES | 15836 |
| 3 | 🇧🇷 BR | 14430 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13733 |
| 6 | 🇮🇹 IT | 13519 |
| 7 | 🇮🇳 IN | 12884 |
| 8 | 🇩🇪 DE | 12158 |
| 9 | 🇬🇧 GB | 11615 |
| 10 | 🇨🇴 CO | 10750 |
| 11 | 🇫🇷 FR | 9956 |
| 12 | 🇯🇵 JP | 9788 |
| 13 | 🇹🇷 TR | 7342 |
| 14 | 🇬🇷 GR | 7272 |
| 15 | 🇲🇽 MX | 6818 |
| 16 | 🇨🇭 CH | 6649 |
| 17 | 🇳🇴 NO | 6130 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4345 |
| 20 | 🇿🇦 ZA | 4277 |
| 21 | 🇵🇱 PL | 4139 |
| 22 | 🇳🇿 NZ | 3378 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3086 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2835 |
| 27 | 🇲🇦 MA | 2499 |
| 28 | 🇲🇪 ME | 2306 |
| 29 | 🇳🇱 NL | 2232 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5081 |
| 2 | Denver International Airport |  | US | 3990 |
| 3 | Indira Gandhi International Airport |  | IN | 3011 |
| 4 | Tokyo International Airport |  | JP | 2920 |
| 5 | Guaymaral Airport |  | CO | 2722 |
| 6 | Harry Reid International Airport |  | US | 2631 |
| 7 | Zurich Airport |  | CH | 2586 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2512 |
| 9 | El Dorado International Airport |  | CO | 2460 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2456 |
| 11 | La Aurora Airport |  | GT | 2348 |
| 12 | Salt Lake City International Airport |  | US | 2188 |
| 13 | Chicago O'Hare International Airport |  | US | 2168 |
| 14 | Congonhas Airport |  | BR | 2118 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2035 |
| 16 | Capua Airport |  | IT | 1941 |
| 17 | Frankfurt am Main International Airport |  | DE | 1939 |
| 18 | Madrid Barajas International Airport |  | ES | 1935 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1860 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1806 |
| 21 | Malpensa International Airport |  | IT | 1770 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 23 | Charles de Gaulle International Airport |  | FR | 1735 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1726 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1608 |
| 28 | Charlotte/Douglas International Airport |  | US | 1570 |
| 29 | Barcelona International Airport |  | ES | 1566 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1507 |
| 32 | Viracopos International Airport |  | BR | 1470 |
| 33 | Seattle-Tacoma International Airport |  | US | 1451 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1437 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Bengaluru International Airport |  | IN | 1425 |
| 37 | Calgary International Airport |  | CA | 1420 |
| 38 | Oslo Gardermoen Airport |  | NO | 1391 |
| 39 | Vancouver International Airport |  | CA | 1380 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1345 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 917 | 21m | 244 km | 3,861.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 646 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 620 | 1h 6m | 770 km | 8,236.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 553 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 406 | 27m | 275 km | 1,923.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 393 | 1h 50m | 1,423 km | 9,644.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 364 | 44m | 241 km | 1,512.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 343 | 24m | 218 km | 1,292.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 332 | 23m | 55 km | 315.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 305 | 26m | 215 km | 1,129.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 268 | 1h 50m | 1,304 km | 6,029.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AVL122 | AVL | Washington Manassas/Harry P Davis Field (KHEF) | Currituck County Regional Airport (KONX) | 2026-09-04 11:43 UTC | 2026-09-04 13:13 UTC | 1h 30m |
| LFA546 | LFA | Orlando Sanford International Airport (KSFB) | Witham Field (KSUA) | 2026-09-04 11:56 UTC | 2026-09-04 13:13 UTC | 1h 16m |
| ECNIB | ECN | A Coruna Airport (LECO) | Cuatro Vientos Airport (LECU) | 2026-09-04 11:57 UTC | 2026-09-04 13:08 UTC | 1h 11m |
| YRGVB | YRG | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-09-04 12:44 UTC | 2026-09-04 13:06 UTC | 22m |
| GIZMO11 | GIZ | Flysooner Field (OK50) | Good Life Ranch Airport (17OK) | 2026-09-04 12:46 UTC | 2026-09-04 13:02 UTC | 16m |
| KLM1959 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Istanbul Hezarfen Airfield (LTBW) | 2026-09-04 10:29 UTC | 2026-09-04 12:57 UTC | 2h 27m |
| N99VC |  | Springdale Municipal Airport (KASG) | Huntsville Municipal Airport (KH34) | 2026-09-04 12:41 UTC | 2026-09-04 12:57 UTC | 15m |
| N317GW |  | Denton Enterprise Airport (KDTO) | Ardmore Downtown Executive Airport (K1F0) | 2026-09-04 12:28 UTC | 2026-09-04 12:53 UTC | 25m |
| NSZ3204 | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-09-04 11:57 UTC | 2026-09-04 12:52 UTC | 55m |
| N2054S |  | Lewis University Airport (KLOT) | IS95 (IS95) | 2026-09-04 12:25 UTC | 2026-09-04 12:51 UTC | 25m |
| NIT298 | NIT | Cochran Airport (K48A) | Taylor Field (GA16) | 2026-09-04 11:41 UTC | 2026-09-04 12:50 UTC | 1h 9m |
| PRE315 | PRE | Centennial Airport (KAPA) | Torrington Municipal Airport (KTOR) | 2026-09-04 12:05 UTC | 2026-09-04 12:41 UTC | 36m |
| DHK528 | DHK | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-04 02:15 UTC | 2026-09-04 12:40 UTC | 10h 25m |
| N475LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-09-04 09:57 UTC | 2026-09-04 12:36 UTC | 2h 39m |
| DFICA | DFI | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-09-04 11:38 UTC | 2026-09-04 12:36 UTC | 57m |
| N443BB |  | Sarasota/Bradenton International Airport (KSRQ) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-04 10:43 UTC | 2026-09-04 12:35 UTC | 1h 51m |
| LUA162T | LUA | Geneva Cointrin International Airport (LSGG) | Hamburg Airport (EDDH) | 2026-09-04 11:14 UTC | 2026-09-04 12:35 UTC | 1h 21m |
| N44668 |  | Westfield-Barnes Regional Airport (KBAF) | Hadley Airport (03MA) | 2026-09-04 11:59 UTC | 2026-09-04 12:35 UTC | 36m |
| LOT3KL | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Katowice International Airport (EPKT) | 2026-09-04 11:58 UTC | 2026-09-04 12:29 UTC | 30m |
| AIP1563 | AIP | Hector International Airport (KFAR) | Tappen Airstrip (8NA0) | 2026-09-04 11:57 UTC | 2026-09-04 12:28 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
