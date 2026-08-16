# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_18:03:28_UTC-green)

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

**Latest saved flight:** 2026-08-16 18:03:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 18:03:28 UTC

- **205,514** saved flights
- **65,588** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,514** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,470,530.9 tonnes** estimated CO2 emissions
- **143,219,182 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8101 |
| 2 | SkyWest Airlines | 7380 |
| 3 | EJA | 3978 |
| 4 | IndiGo | 3520 |
| 5 | American Airlines | 3414 |
| 6 | Southwest Airlines | 3311 |
| 7 | Delta Air Lines | 2632 |
| 8 | ENY | 2560 |
| 9 | LATAM Airlines | 1928 |
| 10 | AZU | 1856 |
| 11 | Lufthansa | 1748 |
| 12 | Vueling | 1702 |
| 13 | WIF | 1655 |
| 14 | LXJ | 1620 |
| 15 | easyJet | 1420 |
| 16 | Swiss International | 1372 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1297 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1128 |
| 24 | GLO | 1106 |
| 25 | Air France | 1100 |
| 26 | PGT | 1096 |
| 27 | JetBlue | 1053 |
| 28 | AEE | 1051 |
| 29 | WMT | 1035 |
| 30 | CXK | 1014 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174577 |
| 2 | 🇪🇸 ES | 13140 |
| 3 | 🇧🇷 BR | 11751 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11330 |
| 6 | 🇮🇳 IN | 10983 |
| 7 | 🇮🇹 IT | 10720 |
| 8 | 🇩🇪 DE | 10177 |
| 9 | 🇬🇧 GB | 9589 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8149 |
| 12 | 🇨🇴 CO | 8131 |
| 13 | 🇬🇷 GR | 6055 |
| 14 | 🇹🇷 TR | 5814 |
| 15 | 🇲🇽 MX | 5764 |
| 16 | 🇨🇭 CH | 5500 |
| 17 | 🇳🇴 NO | 5125 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3393 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2592 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2199 |
| 27 | 🇲🇦 MA | 2073 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1727 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4313 |
| 2 | Denver International Airport |  | US | 3353 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2491 |
| 5 | Guaymaral Airport |  | CO | 2488 |
| 6 | Harry Reid International Airport |  | US | 2325 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2148 |
| 8 | Zurich Airport |  | CH | 2145 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2130 |
| 10 | La Aurora Airport |  | GT | 1980 |
| 11 | Chicago O'Hare International Airport |  | US | 1906 |
| 12 | El Dorado International Airport |  | CO | 1872 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1831 |
| 14 | Salt Lake City International Airport |  | US | 1818 |
| 15 | Congonhas Airport |  | BR | 1713 |
| 16 | Frankfurt am Main International Airport |  | DE | 1704 |
| 17 | Madrid Barajas International Airport |  | ES | 1612 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1572 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1562 |
| 20 | Capua Airport |  | IT | 1559 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1486 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1409 |
| 26 | Charlotte/Douglas International Airport |  | US | 1400 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1261 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1235 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1219 |
| 34 | Viracopos International Airport |  | BR | 1189 |
| 35 | Calgary International Airport |  | CA | 1160 |
| 36 | Reno/Tahoe International Airport |  | US | 1138 |
| 37 | Oslo Gardermoen Airport |  | NO | 1135 |
| 38 | Vitoria/Foronda Airport |  | ES | 1133 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1024 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 468 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 392 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 256 | 24m | 218 km | 964.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 247 | 19m | 99 km | 423.1 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 241 | 1h 37m | 1,156 km | 4,807.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 218 | 28m | 152 km | 569.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N198AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-16 17:02 UTC | 2026-08-16 18:03 UTC | 1h 0m |
| DAL654 | Delta Air Lines | Norman Y Mineta San Jose International Airport (KSJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-08-16 13:45 UTC | 2026-08-16 17:59 UTC | 4h 13m |
| PAT825 | PAT | K4SD (K4SD) | Sacramento Mather Airport (KMHR) | 2026-08-16 16:26 UTC | 2026-08-16 17:58 UTC | 1h 31m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 17:31 UTC | 2026-08-16 17:52 UTC | 21m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-16 17:40 UTC | 2026-08-16 17:51 UTC | 10m |
| N3040F |  | Nelson Airfield (TN99) | Greeneville Municipal Airport (KGCY) | 2026-08-16 17:37 UTC | 2026-08-16 17:47 UTC | 10m |
| N540W |  | Santa Barbara Municipal Airport (KSBA) | Telluride Regional Airport (KTEX) | 2026-08-16 16:19 UTC | 2026-08-16 17:41 UTC | 1h 22m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-16 17:20 UTC | 2026-08-16 17:38 UTC | 17m |
| N294RT |  | Gulf Shores International/Jack Edwards Field (KJKA) | Greensboro Municipal Airport (K7A0) | 2026-08-16 17:10 UTC | 2026-08-16 17:36 UTC | 26m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-16 16:58 UTC | 2026-08-16 17:35 UTC | 36m |
| N828CF |  | Shawano Municipal Airport (KEZS) | Wolf River Landing Strip (8WI5) | 2026-08-16 17:15 UTC | 2026-08-16 17:34 UTC | 19m |
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 17:01 UTC | 2026-08-16 17:33 UTC | 31m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-16 16:42 UTC | 2026-08-16 17:32 UTC | 50m |
| N330V |  | Kintail Farm Airport (GA00) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 17:19 UTC | 2026-08-16 17:31 UTC | 12m |
| VOE63CM | VOE | Ajaccio-Napoleon Bonaparte Airport (LFKJ) | Montpellier-Mediterranee Airport (LFMT) | 2026-08-16 16:41 UTC | 2026-08-16 17:31 UTC | 50m |
| CAN11 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-16 17:15 UTC | 2026-08-16 17:31 UTC | 15m |
| N797CB |  | Elizabeth Field (K0B8) | Addison Airport (KADS) | 2026-08-16 14:12 UTC | 2026-08-16 17:30 UTC | 3h 17m |
| N29263 |  | Paulding Northwest Atlanta Airport (KPUJ) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-08-16 17:25 UTC | 2026-08-16 17:28 UTC | 2m |
| GFOXP | GFO | EG32 (EG32) | EG32 (EG32) | 2026-08-16 17:03 UTC | 2026-08-16 17:26 UTC | 23m |
| CFR440 | CFR | Columbia Airport (KO22) | Bear Valley Airport (73CA) | 2026-08-16 16:54 UTC | 2026-08-16 17:26 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
