# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_23:11:03_UTC-green)

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

**Latest saved flight:** 2026-05-06 23:11:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 23:11:03 UTC

- **71,493** saved flights
- **26,595** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,493** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **881,633.0 tonnes** estimated CO2 emissions
- **51,109,157 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3081 |
| 2 | SkyWest Airlines | 2664 |
| 3 | IndiGo | 1621 |
| 4 | EJA | 1313 |
| 5 | American Airlines | 1123 |
| 6 | Southwest Airlines | 1042 |
| 7 | Lufthansa | 922 |
| 8 | ENY | 896 |
| 9 | Vueling | 702 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 668 |
| 12 | WIF | 611 |
| 13 | Delta Air Lines | 600 |
| 14 | All Nippon Airways | 591 |
| 15 | AZU | 580 |
| 16 | Swiss International | 551 |
| 17 | QLK | 547 |
| 18 | LXJ | 518 |
| 19 | Alaska Airlines | 502 |
| 20 | easyJet | 476 |
| 21 | AEE | 460 |
| 22 | EJU | 459 |
| 23 | VIV | 445 |
| 24 | Cathay Pacific | 444 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 418 |
| 27 | AXB | 395 |
| 28 | AIQ | 358 |
| 29 | CXK | 355 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57146 |
| 2 | 🇪🇸 ES | 5202 |
| 3 | 🇮🇳 IN | 5091 |
| 4 | 🇦🇺 AU | 4726 |
| 5 | 🇧🇷 BR | 4020 |
| 6 | 🇩🇪 DE | 3979 |
| 7 | 🇮🇹 IT | 3920 |
| 8 | 🇯🇵 JP | 3779 |
| 9 | 🇨🇦 CA | 3556 |
| 10 | 🇬🇧 GB | 3087 |
| 11 | 🇫🇷 FR | 2815 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2260 |
| 14 | 🇬🇷 GR | 2126 |
| 15 | 🇳🇴 NO | 1964 |
| 16 | 🇨🇭 CH | 1951 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1309 |
| 20 | 🇹🇷 TR | 1286 |
| 21 | 🇹🇭 TH | 1285 |
| 22 | 🇵🇱 PL | 1189 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1140 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 853 |
| 27 | 🇲🇴 MO | 829 |
| 28 | 🇲🇪 ME | 767 |
| 29 | 🇳🇱 NL | 744 |
| 30 | 🇧🇸 BS | 605 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1598 |
| 2 | Tokyo International Airport |  | JP | 1275 |
| 3 | Denver International Airport |  | US | 1197 |
| 4 | Indira Gandhi International Airport |  | IN | 1072 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1040 |
| 6 | Frankfurt am Main International Airport |  | DE | 915 |
| 7 | Harry Reid International Airport |  | US | 894 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | La Aurora Airport |  | GT | 849 |
| 11 | Zurich Airport |  | CH | 849 |
| 12 | Macau International Airport |  | MO | 829 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 721 |
| 14 | Chicago O'Hare International Airport |  | US | 697 |
| 15 | Kuala Lumpur International Airport |  | MY | 679 |
| 16 | Madrid Barajas International Airport |  | ES | 678 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 639 |
| 18 | Malpensa International Airport |  | IT | 624 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 614 |
| 21 | Salt Lake City International Airport |  | US | 579 |
| 22 | Congonhas Airport |  | BR | 570 |
| 23 | Charlotte/Douglas International Airport |  | US | 562 |
| 24 | Capua Airport |  | IT | 562 |
| 25 | Charles de Gaulle International Airport |  | FR | 559 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 526 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 489 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 480 |
| 34 | Vitoria/Foronda Airport |  | ES | 471 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 452 |
| 37 | Amsterdam Airport Schiphol |  | NL | 444 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Calgary International Airport |  | CA | 429 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 251 | 21m | 244 km | 1,056.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 179 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 134 | 21m | 99 km | 229.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 95 | 1h 43m | 1,423 km | 2,331.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-05-06 22:12 UTC | 2026-05-06 23:11 UTC | 58m |
| RPA4684 | Republic Airways | Raleigh-Durham International Airport (KRDU) | Finagin Airfield (MD05) | 2026-05-06 22:21 UTC | 2026-05-06 23:10 UTC | 49m |
| N1873L |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-06 22:38 UTC | 2026-05-06 23:00 UTC | 22m |
| N405DC |  | Boca Raton Airport (KBCT) | Ohkay Owingeh Airport (KE14) | 2026-05-06 18:53 UTC | 2026-05-06 22:58 UTC | 4h 5m |
| N12AN |  | Henryetta Municipal Airport (KF10) | 19OK (19OK) | 2026-05-06 22:30 UTC | 2026-05-06 22:55 UTC | 25m |
| N280PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-06 22:34 UTC | 2026-05-06 22:54 UTC | 20m |
| N8844 |  | Lake Havasu City Airport (KHII) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-05-06 22:35 UTC | 2026-05-06 22:53 UTC | 17m |
| LTA855 | LTA | Indianapolis International Airport (KIND) | Crawfordsville Regional Airport (KCFJ) | 2026-05-06 21:07 UTC | 2026-05-06 22:52 UTC | 1h 45m |
| LYM507 | LYM | Clifford Field (1CO4) | 3CO0 (3CO0) | 2026-05-06 22:31 UTC | 2026-05-06 22:51 UTC | 19m |
| THY170 | Turkish Airlines | Ataturk International Airport (LTBA) | Zhuhai Airport (ZGSD) | 2026-05-06 13:45 UTC | 2026-05-06 22:51 UTC | 9h 5m |
| CHP14 | CHP | Bodad Airport (CA11) | Bodad Airport (CA11) | 2026-05-06 22:18 UTC | 2026-05-06 22:50 UTC | 32m |
| N18MG |  | Alpine County Airport (KM45) | Carson City Airport (KCXP) | 2026-05-06 21:51 UTC | 2026-05-06 22:49 UTC | 58m |
| CGCBY | CGC | Pitt Meadows Airport (CYPK) | Pitt Meadows Airport (CYPK) | 2026-05-06 22:42 UTC | 2026-05-06 22:49 UTC | 7m |
| VOZ726 | Virgin Australia | Gold Coast Airport (YBCG) | Melbourne International Airport (YMML) | 2026-05-06 20:13 UTC | 2026-05-06 22:46 UTC | 2h 32m |
| N186SG |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-05-06 22:12 UTC | 2026-05-06 22:42 UTC | 30m |
| LR453 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-06 22:04 UTC | 2026-05-06 22:41 UTC | 36m |
| GXA6102 | GXA | Spring Creek Field (79TX) | La Aurora Airport (MGGT) | 2026-05-06 18:48 UTC | 2026-05-06 22:40 UTC | 3h 51m |
| CXK168 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-05-06 21:19 UTC | 2026-05-06 22:35 UTC | 1h 16m |
| JANET51 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-05-06 22:18 UTC | 2026-05-06 22:35 UTC | 16m |
| UCA4327 | UCA | Washington Dulles International Airport (KIAD) | Gastonia Municipal Airport (KAKH) | 2026-05-06 21:31 UTC | 2026-05-06 22:34 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
