# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_04:40:38_UTC-green)

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

**Latest saved flight:** 2026-05-01 04:40:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 04:40:38 UTC

- **61,646** saved flights
- **23,716** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,646** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **751,543.4 tonnes** estimated CO2 emissions
- **43,567,733 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2582 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1407 |
| 4 | EJA | 1117 |
| 5 | American Airlines | 962 |
| 6 | Southwest Airlines | 877 |
| 7 | Lufthansa | 779 |
| 8 | ENY | 765 |
| 9 | Vueling | 607 |
| 10 | AXM | 602 |
| 11 | LATAM Airlines | 585 |
| 12 | All Nippon Airways | 542 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 502 |
| 16 | QLK | 490 |
| 17 | Swiss International | 479 |
| 18 | LXJ | 439 |
| 19 | Alaska Airlines | 426 |
| 20 | AEE | 403 |
| 21 | easyJet | 400 |
| 22 | EJU | 394 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 375 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 358 |
| 27 | AXB | 338 |
| 28 | AIQ | 312 |
| 29 | CXK | 306 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48926 |
| 2 | 🇮🇳 IN | 4443 |
| 3 | 🇪🇸 ES | 4430 |
| 4 | 🇦🇺 AU | 4241 |
| 5 | 🇧🇷 BR | 3493 |
| 6 | 🇩🇪 DE | 3403 |
| 7 | 🇯🇵 JP | 3348 |
| 8 | 🇮🇹 IT | 3345 |
| 9 | 🇨🇦 CA | 3054 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2603 |
| 12 | 🇫🇷 FR | 2410 |
| 13 | 🇲🇽 MX | 1948 |
| 14 | 🇬🇷 GR | 1822 |
| 15 | 🇨🇭 CH | 1711 |
| 16 | 🇳🇴 NO | 1698 |
| 17 | 🇲🇾 MY | 1464 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1179 |
| 20 | 🇹🇭 TH | 1107 |
| 21 | 🇹🇷 TR | 1091 |
| 22 | 🇵🇭 PH | 1054 |
| 23 | 🇵🇱 PL | 989 |
| 24 | 🇰🇷 KR | 989 |
| 25 | 🇬🇹 GT | 922 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 691 |
| 28 | 🇲🇪 ME | 670 |
| 29 | 🇳🇱 NL | 644 |
| 30 | 🇮🇩 ID | 520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1367 |
| 2 | Tokyo International Airport |  | JP | 1131 |
| 3 | Denver International Airport |  | US | 1025 |
| 4 | Indira Gandhi International Airport |  | IN | 939 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 896 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 788 |
| 9 | Frankfurt am Main International Airport |  | DE | 774 |
| 10 | Zurich Airport |  | CH | 734 |
| 11 | Macau International Airport |  | MO | 691 |
| 12 | La Aurora Airport |  | GT | 691 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Chicago O'Hare International Airport |  | US | 583 |
| 15 | Kuala Lumpur International Airport |  | MY | 578 |
| 16 | Madrid Barajas International Airport |  | ES | 572 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 563 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 550 |
| 19 | Bengaluru International Airport |  | IN | 533 |
| 20 | Malpensa International Airport |  | IT | 532 |
| 21 | Congonhas Airport |  | BR | 504 |
| 22 | Charlotte/Douglas International Airport |  | US | 491 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Ninoy Aquino International Airport |  | PH | 478 |
| 25 | Charles de Gaulle International Airport |  | FR | 476 |
| 26 | Tenerife Norte Airport |  | ES | 474 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 459 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 446 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 446 |
| 31 | Barcelona International Airport |  | ES | 413 |
| 32 | Vitoria/Foronda Airport |  | ES | 411 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 409 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 401 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 389 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 380 |
| 39 | Amsterdam Airport Schiphol |  | NL | 379 |
| 40 | Calgary International Airport |  | CA | 366 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 337 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 206 | 21m | 244 km | 867.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 194 | 24m | 225 km | 752.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 181 | 1h 27m | 910 km | 2,840.3 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 152 | 19m | 165 km | 432.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 148 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 130 | 1h 12m | 770 km | 1,726.9 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 104 | 31m | 369 km | 662.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 82 | 14m | 154 km | 217.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA2093 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-30 14:17 UTC | 2026-05-01 04:40 UTC | 14h 22m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-30 14:19 UTC | 2026-05-01 04:38 UTC | 14h 18m |
| N410LF |  | Hawk Haven Airport (ID27) | Ox Meadows Airport (04WA) | 2026-05-01 04:23 UTC | 2026-05-01 04:35 UTC | 12m |
| N2087E |  | Corona Municipal Airport (KAJO) | Riverside Airport (KRAL) | 2026-05-01 04:25 UTC | 2026-05-01 04:35 UTC | 10m |
| ETD925 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-04-30 21:56 UTC | 2026-05-01 04:34 UTC | 6h 37m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-01 04:16 UTC | 2026-05-01 04:28 UTC | 11m |
| 231166 |  | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-05-01 04:08 UTC | 2026-05-01 04:25 UTC | 17m |
| LT611 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-01 04:25 UTC | 2026-05-01 04:25 UTC | 0m |
| VALK81 | VAL | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-05-01 03:01 UTC | 2026-05-01 04:21 UTC | 1h 20m |
| N611MS |  | Bowerman Field (KHQM) | Auburn Municipal Airport (KS50) | 2026-05-01 03:50 UTC | 2026-05-01 04:20 UTC | 29m |
| CCA111 | Air China | Shenzhen Bao'an International Airport (ZGSZ) | Macau International Airport (VMMC) | 2026-04-30 13:23 UTC | 2026-05-01 04:17 UTC | 14h 54m |
| WJA1092 | WJA | Calgary International Airport (CYYC) | Harry Reid International Airport (KLAS) | 2026-05-01 01:53 UTC | 2026-05-01 04:14 UTC | 2h 20m |
| N431ET |  | Kingston Ranch Airport (04NV) | Santa Monica Municipal Airport (KSMO) | 2026-05-01 03:10 UTC | 2026-05-01 04:13 UTC | 1h 2m |
| CXK523 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-05-01 03:17 UTC | 2026-05-01 04:08 UTC | 50m |
| ZKLTE | ZKL | Martinborough Airport (NZMT) | Martinborough Airport (NZMT) | 2026-05-01 02:32 UTC | 2026-05-01 04:07 UTC | 1h 34m |
| UBG121 | UBG | VGZR (VGZR) | Jessore Airport (VGJR) | 2026-05-01 03:36 UTC | 2026-05-01 04:05 UTC | 29m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-30 16:31 UTC | 2026-05-01 04:05 UTC | 11h 34m |
| LCT815 | LCT | Abraham Gonzalez International Airport (MMCS) | Leon Gonzales Pie De La Cuesta Airport (MM41) | 2026-04-30 23:36 UTC | 2026-05-01 04:00 UTC | 4h 23m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-01 03:47 UTC | 2026-05-01 04:00 UTC | 12m |
| N413JM |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-05-01 02:49 UTC | 2026-05-01 03:59 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
