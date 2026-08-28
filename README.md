# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_12:25:52_UTC-green)

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

**Latest saved flight:** 2026-08-28 12:25:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-28 12:25:52 UTC

- **240,306** saved flights
- **73,006** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,306** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,893,464.5 tonnes** estimated CO2 emissions
- **167,737,070 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9650 |
| 2 | SkyWest Airlines | 8432 |
| 3 | EJA | 4652 |
| 4 | IndiGo | 4050 |
| 5 | American Airlines | 3874 |
| 6 | Southwest Airlines | 3619 |
| 7 | Delta Air Lines | 3063 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2306 |
| 10 | AZU | 2238 |
| 11 | Vueling | 2066 |
| 12 | Lufthansa | 1937 |
| 13 | WIF | 1905 |
| 14 | LXJ | 1863 |
| 15 | easyJet | 1671 |
| 16 | Swiss International | 1612 |
| 17 | AXM | 1593 |
| 18 | EJU | 1540 |
| 19 | QLK | 1536 |
| 20 | United Airlines | 1512 |
| 21 | Alaska Airlines | 1436 |
| 22 | All Nippon Airways | 1426 |
| 23 | WMT | 1353 |
| 24 | GLO | 1338 |
| 25 | VIV | 1319 |
| 26 | Air France | 1315 |
| 27 | PGT | 1312 |
| 28 | Wizz Air | 1292 |
| 29 | AEE | 1190 |
| 30 | JetBlue | 1190 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199082 |
| 2 | 🇪🇸 ES | 15471 |
| 3 | 🇧🇷 BR | 14016 |
| 4 | 🇦🇺 AU | 13659 |
| 5 | 🇨🇦 CA | 13355 |
| 6 | 🇮🇹 IT | 13152 |
| 7 | 🇮🇳 IN | 12615 |
| 8 | 🇩🇪 DE | 11873 |
| 9 | 🇬🇧 GB | 11353 |
| 10 | 🇨🇴 CO | 10303 |
| 11 | 🇫🇷 FR | 9691 |
| 12 | 🇯🇵 JP | 9674 |
| 13 | 🇹🇷 TR | 7128 |
| 14 | 🇬🇷 GR | 7080 |
| 15 | 🇲🇽 MX | 6642 |
| 16 | 🇨🇭 CH | 6432 |
| 17 | 🇳🇴 NO | 5935 |
| 18 | 🇹🇭 TH | 4353 |
| 19 | 🇲🇾 MY | 4268 |
| 20 | 🇿🇦 ZA | 4213 |
| 21 | 🇵🇱 PL | 4021 |
| 22 | 🇵🇭 PH | 3299 |
| 23 | 🇳🇿 NZ | 3299 |
| 24 | 🇬🇹 GT | 3016 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2774 |
| 27 | 🇲🇦 MA | 2432 |
| 28 | 🇲🇪 ME | 2247 |
| 29 | 🇳🇱 NL | 2175 |
| 30 | 🇮🇩 ID | 2108 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4963 |
| 2 | Denver International Airport |  | US | 3877 |
| 3 | Indira Gandhi International Airport |  | IN | 2936 |
| 4 | Tokyo International Airport |  | JP | 2881 |
| 5 | Guaymaral Airport |  | CO | 2694 |
| 6 | Harry Reid International Airport |  | US | 2552 |
| 7 | Zurich Airport |  | CH | 2513 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2460 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2399 |
| 10 | El Dorado International Airport |  | CO | 2327 |
| 11 | La Aurora Airport |  | GT | 2301 |
| 12 | Chicago O'Hare International Airport |  | US | 2142 |
| 13 | Salt Lake City International Airport |  | US | 2117 |
| 14 | Congonhas Airport |  | BR | 2050 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1997 |
| 16 | Frankfurt am Main International Airport |  | DE | 1902 |
| 17 | Madrid Barajas International Airport |  | ES | 1895 |
| 18 | Capua Airport |  | IT | 1895 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1807 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1768 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1687 |
| 24 | Charles de Gaulle International Airport |  | FR | 1683 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1601 |
| 27 | Kuala Lumpur International Airport |  | MY | 1543 |
| 28 | Charlotte/Douglas International Airport |  | US | 1538 |
| 29 | Barcelona International Airport |  | ES | 1531 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1528 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1454 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1404 |
| 34 | Bengaluru International Airport |  | IN | 1404 |
| 35 | Seattle-Tacoma International Airport |  | US | 1399 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1397 |
| 37 | Calgary International Airport |  | CA | 1380 |
| 38 | Oslo Gardermoen Airport |  | NO | 1347 |
| 39 | Vancouver International Airport |  | CA | 1320 |
| 40 | O. R. Tambo International Airport |  | ZA | 1313 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1091 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 884 | 21m | 244 km | 3,722.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 618 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 610 | 24m | 225 km | 2,366.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 543 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 378 | 1h 50m | 1,423 km | 9,276.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 364 | 44m | 555 km | 3,485.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 348 | 44m | 241 km | 1,445.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 327 | 24m | 218 km | 1,231.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 319 | 1h 40m | 1,156 km | 6,363.9 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 298 | 19m | 99 km | 510.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 293 | 27m | 215 km | 1,085.1 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 278 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 277 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TGNLA | TGN | La Aurora Airport (MGGT) | San Jose Airport (MGSJ) | 2026-08-28 12:01 UTC | 2026-08-28 12:25 UTC | 24m |
| MXY1602 | MXY | Tampa International Airport (KTPA) | Cistern Field (MYX5) | 2026-08-28 11:35 UTC | 2026-08-28 12:17 UTC | 41m |
| OEDLU | OED | LOKR (LOKR) | Graz Airport (LOWG) | 2026-08-28 11:47 UTC | 2026-08-28 12:16 UTC | 28m |
| ABX2250 | ABX | Norfolk Ns (Chambers Field) Airport (KNGU) | Great Harbour Cay Airport (MYBG) | 2026-08-28 10:24 UTC | 2026-08-28 12:14 UTC | 1h 50m |
| HLE01 | HLE | Bodmin Airfield (EGLA) | Newquay Cornwall Airport (EGHQ) | 2026-08-28 11:53 UTC | 2026-08-28 12:13 UTC | 19m |
| A6KWB |  | Umm Al Quwain (OMUQ) | Umm Al Quwain (OMUQ) | 2026-08-28 12:02 UTC | 2026-08-28 12:12 UTC | 9m |
| N52522 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-28 12:00 UTC | 2026-08-28 12:08 UTC | 7m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-28 11:47 UTC | 2026-08-28 12:01 UTC | 14m |
| LBQ651 | LBQ | New Century Aircenter Airport (KIXD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-28 09:59 UTC | 2026-08-28 12:00 UTC | 2h 0m |
| N38BL |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-28 11:47 UTC | 2026-08-28 11:57 UTC | 10m |
| QUE10 | QUE | Québec City Jean Lesage International Airport (CYQB) | Du Rocher-Perce (Pabok) Airport (CTG3) | 2026-08-28 11:18 UTC | 2026-08-28 11:57 UTC | 38m |
| N57GA |  | Fort Scott Municipal Airport (KFSK) | Searcy County Airport (K4A5) | 2026-08-28 11:24 UTC | 2026-08-28 11:56 UTC | 31m |
| EFY7812 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-08-28 10:41 UTC | 2026-08-28 11:51 UTC | 1h 10m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-08-28 11:06 UTC | 2026-08-28 11:48 UTC | 42m |
| N52522 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-28 11:36 UTC | 2026-08-28 11:47 UTC | 11m |
| TJT35DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-28 10:36 UTC | 2026-08-28 11:47 UTC | 1h 10m |
| TAM3148 | LATAM Airlines | Congonhas Airport (SBSP) | Sao Joaquim Airport (SSSQ) | 2026-08-28 10:47 UTC | 2026-08-28 11:44 UTC | 56m |
| GBHBT | GBH | Chichester/Goodwood Airport (EGHR) | Chichester/Goodwood Airport (EGHR) | 2026-08-28 11:38 UTC | 2026-08-28 11:39 UTC | 1m |
|  |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-08-28 11:37 UTC | 2026-08-28 11:38 UTC | 0m |
| UFX31 | UFX | Humberside Airport (EGNJ) | Fadmoor Airfield (EG19) | 2026-08-28 11:04 UTC | 2026-08-28 11:36 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
