# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_14:15:14_UTC-green)

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

**Latest saved flight:** 2026-09-06 14:15:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 14:15:14 UTC

- **249,418** saved flights
- **74,983** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **249,418** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,002,851.0 tonnes** estimated CO2 emissions
- **174,078,321 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9984 |
| 2 | SkyWest Airlines | 8704 |
| 3 | EJA | 4812 |
| 4 | IndiGo | 4170 |
| 5 | American Airlines | 3990 |
| 6 | Southwest Airlines | 3705 |
| 7 | Delta Air Lines | 3162 |
| 8 | ENY | 2983 |
| 9 | LATAM Airlines | 2405 |
| 10 | AZU | 2323 |
| 11 | Vueling | 2129 |
| 12 | WIF | 1991 |
| 13 | Lufthansa | 1977 |
| 14 | LXJ | 1936 |
| 15 | easyJet | 1721 |
| 16 | Swiss International | 1677 |
| 17 | AXM | 1628 |
| 18 | EJU | 1607 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1565 |
| 21 | Alaska Airlines | 1491 |
| 22 | All Nippon Airways | 1465 |
| 23 | WMT | 1414 |
| 24 | GLO | 1391 |
| 25 | PGT | 1368 |
| 26 | VIV | 1368 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1356 |
| 29 | JetBlue | 1226 |
| 30 | AEE | 1225 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206760 |
| 2 | 🇪🇸 ES | 15969 |
| 3 | 🇧🇷 BR | 14572 |
| 4 | 🇦🇺 AU | 14152 |
| 5 | 🇨🇦 CA | 13851 |
| 6 | 🇮🇹 IT | 13677 |
| 7 | 🇮🇳 IN | 13011 |
| 8 | 🇩🇪 DE | 12272 |
| 9 | 🇬🇧 GB | 11706 |
| 10 | 🇨🇴 CO | 10934 |
| 11 | 🇫🇷 FR | 10057 |
| 12 | 🇯🇵 JP | 9861 |
| 13 | 🇹🇷 TR | 7433 |
| 14 | 🇬🇷 GR | 7339 |
| 15 | 🇲🇽 MX | 6893 |
| 16 | 🇨🇭 CH | 6728 |
| 17 | 🇳🇴 NO | 6171 |
| 18 | 🇹🇭 TH | 4504 |
| 19 | 🇲🇾 MY | 4368 |
| 20 | 🇿🇦 ZA | 4299 |
| 21 | 🇵🇱 PL | 4172 |
| 22 | 🇳🇿 NZ | 3405 |
| 23 | 🇵🇭 PH | 3394 |
| 24 | 🇬🇹 GT | 3123 |
| 25 | 🇰🇷 KR | 2895 |
| 26 | 🇭🇷 HR | 2870 |
| 27 | 🇲🇦 MA | 2520 |
| 28 | 🇲🇪 ME | 2341 |
| 29 | 🇳🇱 NL | 2256 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5139 |
| 2 | Denver International Airport |  | US | 4029 |
| 3 | Indira Gandhi International Airport |  | IN | 3035 |
| 4 | Tokyo International Airport |  | JP | 2944 |
| 5 | Guaymaral Airport |  | CO | 2730 |
| 6 | Harry Reid International Airport |  | US | 2652 |
| 7 | Zurich Airport |  | CH | 2613 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2533 |
| 9 | El Dorado International Airport |  | CO | 2514 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2473 |
| 11 | La Aurora Airport |  | GT | 2380 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2182 |
| 14 | Congonhas Airport |  | BR | 2140 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2055 |
| 16 | Capua Airport |  | IT | 1966 |
| 17 | Madrid Barajas International Airport |  | ES | 1962 |
| 18 | Frankfurt am Main International Airport |  | DE | 1948 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1872 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1817 |
| 21 | Malpensa International Airport |  | IT | 1797 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 23 | Charles de Gaulle International Airport |  | FR | 1748 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1736 |
| 25 | Ninoy Aquino International Airport |  | PH | 1654 |
| 26 | Macau International Airport |  | MO | 1646 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Barcelona International Airport |  | ES | 1580 |
| 29 | Charlotte/Douglas International Airport |  | US | 1577 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1528 |
| 32 | Viracopos International Airport |  | BR | 1493 |
| 33 | Seattle-Tacoma International Airport |  | US | 1467 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1442 |
| 36 | Calgary International Airport |  | CA | 1433 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1403 |
| 39 | Vancouver International Airport |  | CA | 1395 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1356 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 561 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 388 | 44m | 555 km | 3,715.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 370 | 44m | 241 km | 1,536.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 308 | 26m | 215 km | 1,140.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 288 | 1h 14m | 961 km | 4,773.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 288 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 286 | 19m | 144 km | 711.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N126VA |  | 5TA7 (5TA7) | TE77 (TE77) | 2026-09-06 13:57 UTC | 2026-09-06 14:15 UTC | 17m |
| N263SF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-09-06 13:09 UTC | 2026-09-06 14:07 UTC | 58m |
| DMSGW | DMS | Altenstadt Army Airfield (ETHA) | Altenstadt Army Airfield (ETHA) | 2026-09-06 13:59 UTC | 2026-09-06 14:00 UTC | 1m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-09-06 13:48 UTC | 2026-09-06 14:00 UTC | 11m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-09-06 13:34 UTC | 2026-09-06 13:49 UTC | 15m |
| N494SM |  | Wright Army Air Field (Fort Stewart)/Midcoast Regional Airport (KLHW) | Cypress Lakes Airport (GA35) | 2026-09-06 12:53 UTC | 2026-09-06 13:44 UTC | 50m |
| RVP516 | RVP | Cascais Airport (LPCS) | Sintra Airport (LPST) | 2026-09-06 12:05 UTC | 2026-09-06 13:43 UTC | 1h 38m |
| N143NE |  | Rhode Island Tf Green International Airport (KPVD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-06 13:15 UTC | 2026-09-06 13:43 UTC | 28m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-09-06 13:29 UTC | 2026-09-06 13:42 UTC | 12m |
| EVA872 | EVA Air | Chek Lap Kok International Airport (VHHH) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-06 12:26 UTC | 2026-09-06 13:41 UTC | 1h 15m |
| CFTOX | CFT | Pitt Meadows Airport (CYPK) | Chilliwack Airport (CYCW) | 2026-09-06 13:28 UTC | 2026-09-06 13:39 UTC | 11m |
| N387CS |  | Centennial Airport (KAPA) | Laramie Regional Airport (KLAR) | 2026-09-06 12:44 UTC | 2026-09-06 13:39 UTC | 54m |
| LTA663 | LTA | Moton Field Municipal Airport (K06A) | AL73 (AL73) | 2026-09-06 12:26 UTC | 2026-09-06 13:38 UTC | 1h 11m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-09-06 13:26 UTC | 2026-09-06 13:38 UTC | 11m |
| DEDLG | DED | Gundelfingen Airport (EDMU) | Gundelfingen Airport (EDMU) | 2026-09-06 12:56 UTC | 2026-09-06 13:35 UTC | 38m |
| DENNN | DEN | Siegerland Airport (EDGS) | Siegerland Airport (EDGS) | 2026-09-06 13:27 UTC | 2026-09-06 13:34 UTC | 7m |
| CTN344 | CTN | LDZI (LDZI) | Visoko Sport Airfield (LQVI) | 2026-09-06 13:04 UTC | 2026-09-06 13:33 UTC | 28m |
| ETD947 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-09-06 06:17 UTC | 2026-09-06 13:31 UTC | 7h 13m |
| N2404Z |  | Gainesville Municipal Airport (KGLE) | Gainesville Municipal Airport (KGLE) | 2026-09-06 13:14 UTC | 2026-09-06 13:28 UTC | 13m |
| A6FTS |  | Al Minhad Air Base (OMDM) | Dubai International Airport (OMDB) | 2026-09-06 11:58 UTC | 2026-09-06 13:27 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
