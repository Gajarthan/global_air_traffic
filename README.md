# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_18:50:30_UTC-green)

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

**Latest saved flight:** 2026-08-25 18:50:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 18:50:30 UTC

- **236,223** saved flights
- **72,163** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,223** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,844,507.1 tonnes** estimated CO2 emissions
- **164,898,965 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9470 |
| 2 | SkyWest Airlines | 8330 |
| 3 | EJA | 4583 |
| 4 | IndiGo | 3985 |
| 5 | American Airlines | 3835 |
| 6 | Southwest Airlines | 3602 |
| 7 | Delta Air Lines | 3007 |
| 8 | ENY | 2869 |
| 9 | LATAM Airlines | 2268 |
| 10 | AZU | 2203 |
| 11 | Vueling | 2023 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1879 |
| 14 | LXJ | 1847 |
| 15 | easyJet | 1649 |
| 16 | Swiss International | 1587 |
| 17 | AXM | 1575 |
| 18 | EJU | 1516 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1490 |
| 21 | Alaska Airlines | 1419 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1320 |
| 24 | GLO | 1315 |
| 25 | VIV | 1304 |
| 26 | PGT | 1288 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1263 |
| 29 | AEE | 1174 |
| 30 | JetBlue | 1173 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196199 |
| 2 | 🇪🇸 ES | 15188 |
| 3 | 🇧🇷 BR | 13792 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13062 |
| 6 | 🇮🇹 IT | 12886 |
| 7 | 🇮🇳 IN | 12415 |
| 8 | 🇩🇪 DE | 11655 |
| 9 | 🇬🇧 GB | 11153 |
| 10 | 🇨🇴 CO | 10010 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9491 |
| 13 | 🇹🇷 TR | 7012 |
| 14 | 🇬🇷 GR | 6965 |
| 15 | 🇲🇽 MX | 6559 |
| 16 | 🇨🇭 CH | 6313 |
| 17 | 🇳🇴 NO | 5859 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4145 |
| 21 | 🇵🇱 PL | 3939 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2960 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2723 |
| 27 | 🇲🇦 MA | 2391 |
| 28 | 🇲🇪 ME | 2198 |
| 29 | 🇳🇱 NL | 2122 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4904 |
| 2 | Denver International Airport |  | US | 3815 |
| 3 | Indira Gandhi International Airport |  | IN | 2882 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2685 |
| 6 | Harry Reid International Airport |  | US | 2524 |
| 7 | Zurich Airport |  | CH | 2475 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2414 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2366 |
| 10 | La Aurora Airport |  | GT | 2256 |
| 11 | El Dorado International Airport |  | CO | 2242 |
| 12 | Chicago O'Hare International Airport |  | US | 2127 |
| 13 | Salt Lake City International Airport |  | US | 2078 |
| 14 | Congonhas Airport |  | BR | 2012 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1977 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Madrid Barajas International Airport |  | ES | 1857 |
| 18 | Capua Airport |  | IT | 1856 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1775 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1743 |
| 21 | Malpensa International Airport |  | IT | 1693 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1674 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1523 |
| 29 | Barcelona International Airport |  | ES | 1493 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1473 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1430 |
| 32 | Viracopos International Airport |  | BR | 1411 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1383 |
| 35 | Seattle-Tacoma International Airport |  | US | 1381 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1351 |
| 38 | Oslo Gardermoen Airport |  | NO | 1327 |
| 39 | Vancouver International Airport |  | CA | 1290 |
| 40 | O. R. Tambo International Airport |  | ZA | 1288 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 867 | 21m | 244 km | 3,650.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 597 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 529 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 342 | 44m | 241 km | 1,420.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 334 | 21m | 250 km | 1,442.7 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 313 | 1h 40m | 1,156 km | 6,244.2 t |
| 16 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 311 | 22m | 55 km | 295.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 293 | 19m | 99 km | 501.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 253 | 1h 50m | 1,304 km | 5,691.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-25 18:04 UTC | 2026-08-25 18:50 UTC | 46m |
| N315EF |  | Hammond Northshore Regional Airport (KHDC) | Stennis International Airport (KHSA) | 2026-08-25 18:15 UTC | 2026-08-25 18:48 UTC | 32m |
| C6051 |  | St Elmo Airport (K2R5) | St Elmo Airport (K2R5) | 2026-08-25 18:20 UTC | 2026-08-25 18:48 UTC | 27m |
| N6812W |  | Quilchena Airport (CBT6) | Quilchena Airport (CBT6) | 2026-08-25 18:14 UTC | 2026-08-25 18:43 UTC | 29m |
| N503WA |  | Three Rivers Municipal/Dr Haines Airport (KHAI) | Goshen Municipal Airport (KGSH) | 2026-08-25 18:20 UTC | 2026-08-25 18:40 UTC | 20m |
| BYF30 | BYF | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-08-25 18:02 UTC | 2026-08-25 18:40 UTC | 38m |
| N4KT |  | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-08-25 18:07 UTC | 2026-08-25 18:39 UTC | 31m |
| SMGLR23 | SMG | Namest Air Base (LKNA) | Kbely Air Base (LKKB) | 2026-08-25 18:02 UTC | 2026-08-25 18:37 UTC | 34m |
| N926CR |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-08-25 17:38 UTC | 2026-08-25 18:37 UTC | 58m |
| N555YS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-25 18:10 UTC | 2026-08-25 18:36 UTC | 26m |
| N4343Z |  | 0OR9 (0OR9) | 0OR9 (0OR9) | 2026-08-25 18:22 UTC | 2026-08-25 18:36 UTC | 13m |
| N222KH |  | Tacoma Narrows Airport (KTIW) | Tacoma Narrows Airport (KTIW) | 2026-08-25 17:34 UTC | 2026-08-25 18:32 UTC | 58m |
| WAKE71 | WAK | Albuquerque International Sunport Airport (KABQ) | Albuquerque International Sunport Airport (KABQ) | 2026-08-25 18:05 UTC | 2026-08-25 18:32 UTC | 26m |
| ROGUE9 | ROG | Sells Airport (KE78) | Sells Airport (KE78) | 2026-08-25 18:18 UTC | 2026-08-25 18:30 UTC | 12m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 18:16 UTC | 2026-08-25 18:28 UTC | 12m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 18:15 UTC | 2026-08-25 18:28 UTC | 12m |
| N569FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-25 18:16 UTC | 2026-08-25 18:27 UTC | 10m |
| N107BZ |  | On The Rocks Airport (1CA6) | On The Rocks Airport (1CA6) | 2026-08-25 18:08 UTC | 2026-08-25 18:22 UTC | 14m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-25 17:18 UTC | 2026-08-25 18:21 UTC | 1h 2m |
| N8344V |  | Phyllis Field (6IL2) | Lake In The Hills Airport (K3CK) | 2026-08-25 17:42 UTC | 2026-08-25 18:21 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
