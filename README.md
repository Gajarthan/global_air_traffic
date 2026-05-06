# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_03:50:54_UTC-green)

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

**Latest saved flight:** 2026-05-06 03:50:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 03:50:54 UTC

- **70,163** saved flights
- **26,172** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,163** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **864,309.5 tonnes** estimated CO2 emissions
- **50,104,899 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3007 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1603 |
| 4 | EJA | 1282 |
| 5 | American Airlines | 1096 |
| 6 | Southwest Airlines | 1018 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 876 |
| 9 | Vueling | 690 |
| 10 | AXM | 672 |
| 11 | LATAM Airlines | 656 |
| 12 | WIF | 596 |
| 13 | Delta Air Lines | 593 |
| 14 | All Nippon Airways | 587 |
| 15 | AZU | 570 |
| 16 | QLK | 545 |
| 17 | Swiss International | 539 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 492 |
| 20 | easyJet | 468 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 441 |
| 24 | Cathay Pacific | 428 |
| 25 | Japan Airlines | 414 |
| 26 | Air France | 411 |
| 27 | AXB | 390 |
| 28 | AIQ | 356 |
| 29 | CXK | 349 |
| 30 | MXY | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55860 |
| 2 | 🇪🇸 ES | 5104 |
| 3 | 🇮🇳 IN | 5048 |
| 4 | 🇦🇺 AU | 4676 |
| 5 | 🇧🇷 BR | 3953 |
| 6 | 🇩🇪 DE | 3901 |
| 7 | 🇮🇹 IT | 3833 |
| 8 | 🇯🇵 JP | 3744 |
| 9 | 🇨🇦 CA | 3471 |
| 10 | 🇬🇧 GB | 3038 |
| 11 | 🇫🇷 FR | 2769 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2228 |
| 14 | 🇬🇷 GR | 2086 |
| 15 | 🇨🇭 CH | 1923 |
| 16 | 🇳🇴 NO | 1913 |
| 17 | 🇲🇾 MY | 1677 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1295 |
| 20 | 🇹🇭 TH | 1272 |
| 21 | 🇹🇷 TR | 1261 |
| 22 | 🇵🇭 PH | 1160 |
| 23 | 🇵🇱 PL | 1151 |
| 24 | 🇬🇹 GT | 1129 |
| 25 | 🇰🇷 KR | 1120 |
| 26 | 🇲🇦 MA | 843 |
| 27 | 🇲🇴 MO | 808 |
| 28 | 🇲🇪 ME | 755 |
| 29 | 🇳🇱 NL | 728 |
| 30 | 🇮🇩 ID | 591 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1569 |
| 2 | Tokyo International Airport |  | JP | 1263 |
| 3 | Denver International Airport |  | US | 1166 |
| 4 | Indira Gandhi International Airport |  | IN | 1059 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1021 |
| 6 | Frankfurt am Main International Airport |  | DE | 895 |
| 7 | Harry Reid International Airport |  | US | 879 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 839 |
| 11 | Zurich Airport |  | CH | 827 |
| 12 | Macau International Airport |  | MO | 808 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 703 |
| 14 | Chicago O'Hare International Airport |  | US | 675 |
| 15 | Kuala Lumpur International Airport |  | MY | 672 |
| 16 | Madrid Barajas International Airport |  | ES | 666 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 611 |
| 19 | Malpensa International Airport |  | IT | 609 |
| 20 | Bengaluru International Airport |  | IN | 607 |
| 21 | Salt Lake City International Airport |  | US | 568 |
| 22 | Congonhas Airport |  | BR | 562 |
| 23 | Charlotte/Douglas International Airport |  | US | 555 |
| 24 | Charles de Gaulle International Airport |  | FR | 550 |
| 25 | Tenerife Norte Airport |  | ES | 544 |
| 26 | Capua Airport |  | IT | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Daniel K Inouye International Airport |  | US | 513 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 513 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 495 |
| 31 | Barcelona International Airport |  | ES | 486 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 477 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 449 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 442 |
| 37 | O. R. Tambo International Airport |  | ZA | 438 |
| 38 | Amsterdam Airport Schiphol |  | NL | 430 |
| 39 | Reno/Tahoe International Airport |  | US | 416 |
| 40 | Calgary International Airport |  | CA | 416 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 263 | 1h 7m | 706 km | 3,202.0 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 243 | 21m | 244 km | 1,023.2 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 197 | 28m | 304 km | 1,032.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 196 | 1h 27m | 910 km | 3,075.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 175 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 173 | 20m | 165 km | 492.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 169 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 129 | 44m | 452 km | 1,005.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 100 | 14m | 154 km | 265.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 97 | 1h 2m | 695 km | 1,162.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HLTK201 | HLT | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-05-06 03:10 UTC | 2026-05-06 03:50 UTC | 40m |
| FFT4766 | FFT | Phoenix Sky Harbor International Airport (KPHX) | Denver International Airport (KDEN) | 2026-05-06 02:33 UTC | 2026-05-06 03:48 UTC | 1h 15m |
| KAI | KAI | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-05-06 03:26 UTC | 2026-05-06 03:43 UTC | 17m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-06 03:10 UTC | 2026-05-06 03:40 UTC | 30m |
| NPF | NPF | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-05-06 03:24 UTC | 2026-05-06 03:36 UTC | 12m |
| N1NJ |  | NJ16 (NJ16) | Morristown Municipal Airport (KMMU) | 2026-05-06 03:24 UTC | 2026-05-06 03:33 UTC | 8m |
| N21670 |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-05-06 03:25 UTC | 2026-05-06 03:30 UTC | 4m |
| N115FD |  | Mc Clellan Airfield (KMCC) | Van Vleck Airport (57CN) | 2026-05-06 02:59 UTC | 2026-05-06 03:27 UTC | 27m |
| FKH8062 | FKH | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-05 01:18 UTC | 2026-05-06 03:24 UTC | 26h 5m |
| ETH3790 | Ethiopian Airlines | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-05-05 16:35 UTC | 2026-05-06 03:16 UTC | 10h 40m |
| SWA826 | Southwest Airlines | Chicago Midway International Airport (KMDW) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-05 23:02 UTC | 2026-05-06 03:13 UTC | 4h 10m |
| N21670 |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-05-06 02:50 UTC | 2026-05-06 03:13 UTC | 22m |
| ALFT | ALF | Easton State Airport (KESW) | Boeing Field/King County International Airport (KBFI) | 2026-05-06 02:51 UTC | 2026-05-06 03:11 UTC | 20m |
| AZG5789 | AZG | Frankfurt-Hahn Airport (EDFH) | Macau International Airport (VMMC) | 2026-05-05 11:54 UTC | 2026-05-06 03:11 UTC | 15h 16m |
| ZJX | ZJX | Melbourne Essendon Airport (YMEN) | Melbourne Essendon Airport (YMEN) | 2026-05-06 02:48 UTC | 2026-05-06 03:10 UTC | 22m |
| DTCHMN42 | DTC | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-06 02:54 UTC | 2026-05-06 03:06 UTC | 11m |
| N1044L |  | Ugashik Narrows Airport (AA05) | Birchwood Airport (PABV) | 2026-05-06 02:47 UTC | 2026-05-06 03:00 UTC | 12m |
| WEN3404 | WEN | Edmonton International Airport (CYEG) | Moose Jaw Municipal Airport (CJS4) | 2026-05-06 01:52 UTC | 2026-05-06 02:57 UTC | 1h 5m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-05-06 02:45 UTC | 2026-05-06 02:57 UTC | 12m |
| SWA298 | Southwest Airlines | Portland International Airport (KPDX) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-06 01:41 UTC | 2026-05-06 02:57 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
