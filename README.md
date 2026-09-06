# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_17:05:25_UTC-green)

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

**Latest saved flight:** 2026-09-06 17:05:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 17:05:25 UTC

- **249,616** saved flights
- **75,028** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **249,616** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,004,581.4 tonnes** estimated CO2 emissions
- **174,178,629 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9990 |
| 2 | SkyWest Airlines | 8711 |
| 3 | EJA | 4816 |
| 4 | IndiGo | 4172 |
| 5 | American Airlines | 3993 |
| 6 | Southwest Airlines | 3707 |
| 7 | Delta Air Lines | 3165 |
| 8 | ENY | 2988 |
| 9 | LATAM Airlines | 2405 |
| 10 | AZU | 2323 |
| 11 | Vueling | 2130 |
| 12 | WIF | 1995 |
| 13 | Lufthansa | 1979 |
| 14 | LXJ | 1937 |
| 15 | easyJet | 1722 |
| 16 | Swiss International | 1677 |
| 17 | AXM | 1628 |
| 18 | EJU | 1608 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1565 |
| 21 | Alaska Airlines | 1491 |
| 22 | All Nippon Airways | 1465 |
| 23 | WMT | 1415 |
| 24 | GLO | 1392 |
| 25 | PGT | 1370 |
| 26 | VIV | 1369 |
| 27 | Air France | 1361 |
| 28 | Wizz Air | 1357 |
| 29 | AEE | 1227 |
| 30 | JetBlue | 1226 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206959 |
| 2 | 🇪🇸 ES | 15979 |
| 3 | 🇧🇷 BR | 14574 |
| 4 | 🇦🇺 AU | 14152 |
| 5 | 🇨🇦 CA | 13855 |
| 6 | 🇮🇹 IT | 13682 |
| 7 | 🇮🇳 IN | 13019 |
| 8 | 🇩🇪 DE | 12286 |
| 9 | 🇬🇧 GB | 11714 |
| 10 | 🇨🇴 CO | 10943 |
| 11 | 🇫🇷 FR | 10069 |
| 12 | 🇯🇵 JP | 9861 |
| 13 | 🇹🇷 TR | 7441 |
| 14 | 🇬🇷 GR | 7347 |
| 15 | 🇲🇽 MX | 6900 |
| 16 | 🇨🇭 CH | 6737 |
| 17 | 🇳🇴 NO | 6178 |
| 18 | 🇹🇭 TH | 4504 |
| 19 | 🇲🇾 MY | 4368 |
| 20 | 🇿🇦 ZA | 4305 |
| 21 | 🇵🇱 PL | 4173 |
| 22 | 🇳🇿 NZ | 3405 |
| 23 | 🇵🇭 PH | 3394 |
| 24 | 🇬🇹 GT | 3126 |
| 25 | 🇰🇷 KR | 2895 |
| 26 | 🇭🇷 HR | 2871 |
| 27 | 🇲🇦 MA | 2524 |
| 28 | 🇲🇪 ME | 2344 |
| 29 | 🇳🇱 NL | 2259 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5147 |
| 2 | Denver International Airport |  | US | 4034 |
| 3 | Indira Gandhi International Airport |  | IN | 3038 |
| 4 | Tokyo International Airport |  | JP | 2944 |
| 5 | Guaymaral Airport |  | CO | 2731 |
| 6 | Harry Reid International Airport |  | US | 2652 |
| 7 | Zurich Airport |  | CH | 2615 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2533 |
| 9 | El Dorado International Airport |  | CO | 2518 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2476 |
| 11 | La Aurora Airport |  | GT | 2383 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2183 |
| 14 | Congonhas Airport |  | BR | 2141 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2055 |
| 16 | Capua Airport |  | IT | 1969 |
| 17 | Madrid Barajas International Airport |  | ES | 1963 |
| 18 | Frankfurt am Main International Airport |  | DE | 1951 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1872 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1820 |
| 21 | Malpensa International Airport |  | IT | 1798 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 23 | Charles de Gaulle International Airport |  | FR | 1750 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1740 |
| 25 | Ninoy Aquino International Airport |  | PH | 1654 |
| 26 | Macau International Airport |  | MO | 1646 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1581 |
| 29 | Barcelona International Airport |  | ES | 1581 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1530 |
| 32 | Viracopos International Airport |  | BR | 1493 |
| 33 | Seattle-Tacoma International Airport |  | US | 1468 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1442 |
| 36 | Calgary International Airport |  | CA | 1433 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1404 |
| 39 | Vancouver International Airport |  | CA | 1395 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 562 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 398 | 1h 50m | 1,423 km | 9,767.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 388 | 44m | 555 km | 3,715.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 370 | 44m | 241 km | 1,536.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 289 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BPX253 | BPX | Augusta Regional At Bush Field (KAGS) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-06 16:10 UTC | 2026-09-06 17:05 UTC | 54m |
| BPX262 | BPX | Augusta Regional At Bush Field (KAGS) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-06 16:06 UTC | 2026-09-06 17:01 UTC | 55m |
| N692CK |  | Burke Lakefront Airport (KBKL) | Burke Lakefront Airport (KBKL) | 2026-09-06 16:48 UTC | 2026-09-06 17:01 UTC | 12m |
| N125PM |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-09-06 14:31 UTC | 2026-09-06 16:58 UTC | 2h 27m |
| N2YV |  | Fort Crosby Airport (8AK5) | Helio Airport (2AK7) | 2026-09-06 16:36 UTC | 2026-09-06 16:52 UTC | 15m |
| N432FM |  | Schaumburg Regional Airport (K06C) | Hutfly Airport (KFCY) | 2026-09-06 14:18 UTC | 2026-09-06 16:50 UTC | 2h 32m |
| N202EH |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-09-06 16:26 UTC | 2026-09-06 16:40 UTC | 14m |
| N82616 |  | K3M3 (K3M3) | W N C  Air Museum Airport (8NC9) | 2026-09-06 15:37 UTC | 2026-09-06 16:39 UTC | 1h 2m |
| N40JF |  | 0OI4 (0OI4) | 1OI1 (1OI1) | 2026-09-06 16:18 UTC | 2026-09-06 16:33 UTC | 15m |
| CXK126 | CXK | Double Eagle Ii Airport (KAEG) | Socorro Municipal Airport (KONM) | 2026-09-06 15:49 UTC | 2026-09-06 16:32 UTC | 42m |
| HBCQM | HBC | Hausen am Albis Airport (LSZN) | Ambri Airport (LSPM) | 2026-09-06 16:08 UTC | 2026-09-06 16:30 UTC | 21m |
| N71114 |  | Front Royal-Warren County Airport (KFRR) | Front Royal-Warren County Airport (KFRR) | 2026-09-06 16:14 UTC | 2026-09-06 16:27 UTC | 12m |
| N991AK |  | Merrill Field (PAMR) | Big Mountain Airport (PABM) | 2026-09-06 15:41 UTC | 2026-09-06 16:26 UTC | 45m |
| BPX254 | BPX | Augusta Regional At Bush Field (KAGS) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-06 15:25 UTC | 2026-09-06 16:25 UTC | 1h 0m |
| N222KU |  | White Airport (69TS) | Telluride Regional Airport (KTEX) | 2026-09-06 14:37 UTC | 2026-09-06 16:24 UTC | 1h 46m |
| BPX280 | BPX | Augusta Regional At Bush Field (KAGS) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-06 15:22 UTC | 2026-09-06 16:24 UTC | 1h 2m |
| N733FF |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-09-06 16:08 UTC | 2026-09-06 16:23 UTC | 14m |
| BPX269 | BPX | Augusta Regional At Bush Field (KAGS) | Savannah/Hilton Head International Airport (KSAV) | 2026-09-06 15:23 UTC | 2026-09-06 16:22 UTC | 58m |
| JIA5315 | JIA | Charlotte/Douglas International Airport (KCLT) | Weaver Field (SC94) | 2026-09-06 16:01 UTC | 2026-09-06 16:21 UTC | 20m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-09-06 16:06 UTC | 2026-09-06 16:20 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
