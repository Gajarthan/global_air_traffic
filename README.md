# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_04:58:35_UTC-green)

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

**Latest saved flight:** 2026-04-26 04:58:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 04:58:35 UTC

- **54,650** saved flights
- **21,599** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,650** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **658,647.9 tonnes** estimated CO2 emissions
- **38,182,486 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2297 |
| 2 | SkyWest Airlines | 2073 |
| 3 | IndiGo | 1232 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 642 |
| 9 | Vueling | 547 |
| 10 | AXM | 526 |
| 11 | LATAM Airlines | 526 |
| 12 | All Nippon Airways | 482 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | Swiss International | 419 |
| 17 | QLK | 417 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 366 |
| 20 | AEE | 363 |
| 21 | VIV | 352 |
| 22 | EJU | 349 |
| 23 | easyJet | 349 |
| 24 | Japan Airlines | 317 |
| 25 | Air France | 313 |
| 26 | Cathay Pacific | 308 |
| 27 | AXB | 287 |
| 28 | JetBlue | 280 |
| 29 | AIQ | 279 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43658 |
| 2 | 🇪🇸 ES | 3952 |
| 3 | 🇮🇳 IN | 3881 |
| 4 | 🇦🇺 AU | 3670 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2946 |
| 7 | 🇯🇵 JP | 2919 |
| 8 | 🇩🇪 DE | 2916 |
| 9 | 🇨🇦 CA | 2717 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2283 |
| 12 | 🇫🇷 FR | 2124 |
| 13 | 🇲🇽 MX | 1720 |
| 14 | 🇬🇷 GR | 1625 |
| 15 | 🇨🇭 CH | 1537 |
| 16 | 🇳🇴 NO | 1455 |
| 17 | 🇲🇾 MY | 1276 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1037 |
| 20 | 🇹🇷 TR | 987 |
| 21 | 🇹🇭 TH | 981 |
| 22 | 🇵🇭 PH | 932 |
| 23 | 🇰🇷 KR | 881 |
| 24 | 🇵🇱 PL | 874 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 685 |
| 27 | 🇲🇪 ME | 589 |
| 28 | 🇲🇴 MO | 554 |
| 29 | 🇳🇱 NL | 553 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1247 |
| 2 | Tokyo International Airport |  | JP | 992 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 824 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 802 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 703 |
| 9 | Zurich Airport |  | CH | 646 |
| 10 | Frankfurt am Main International Airport |  | DE | 628 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 554 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 544 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 509 |
| 17 | Madrid Barajas International Airport |  | ES | 504 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 480 |
| 19 | Malpensa International Airport |  | IT | 468 |
| 20 | Bengaluru International Airport |  | IN | 463 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 430 |
| 25 | Salt Lake City International Airport |  | US | 415 |
| 26 | Charles de Gaulle International Airport |  | FR | 413 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 405 |
| 29 | Capua Airport |  | IT | 398 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 387 |
| 31 | Vitoria/Foronda Airport |  | ES | 372 |
| 32 | Barcelona International Airport |  | ES | 369 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 358 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 334 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 248 | 1h 7m | 706 km | 3,019.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 177 | 24m | 225 km | 686.7 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 173 | 21m | 244 km | 728.5 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 156 | 1h 27m | 910 km | 2,448.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 126 | 26m | 275 km | 597.1 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 102 | 1h 11m | 770 km | 1,355.0 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 94 | 31m | 369 km | 598.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-25 17:34 UTC | 2026-04-26 04:58 UTC | 11h 24m |
| SIA212 | Singapore Airlines | Sydney Kingsford Smith International Airport (YSSY) | Hang Nadim Airport (WIDD) | 2026-04-25 21:25 UTC | 2026-04-26 04:54 UTC | 7h 29m |
| DLA5RK | DLA | Bologna / Borgo Panigale Airport (LIPE) | Oberpfaffenhofen Airport (EDMO) | 2026-04-26 04:06 UTC | 2026-04-26 04:53 UTC | 46m |
| LHX5YY | LHX | Hannover Airport (EDDV) | Griesau Airport (EDPG) | 2026-04-26 04:01 UTC | 2026-04-26 04:53 UTC | 51m |
| JBU993 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Denver International Airport (KDEN) | 2026-04-26 00:33 UTC | 2026-04-26 04:41 UTC | 4h 7m |
| HLTK203 | HLT | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-04-26 04:20 UTC | 2026-04-26 04:32 UTC | 11m |
| AFL1242 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-04-26 03:42 UTC | 2026-04-26 04:31 UTC | 48m |
| EDG92 | EDG | Phoenix Sky Harbor International Airport (KPHX) | Henderson Executive Airport (KHND) | 2026-04-26 03:43 UTC | 2026-04-26 04:24 UTC | 41m |
| CPQ | CPQ | Southport Airport (YSPT) | Brisbane Archerfield Airport (YBAF) | 2026-04-26 04:10 UTC | 2026-04-26 04:24 UTC | 14m |
| KDJ | KDJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-26 03:38 UTC | 2026-04-26 04:22 UTC | 44m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-26 03:48 UTC | 2026-04-26 04:22 UTC | 34m |
| CTN3T | CTN | Pula Airport (LDPL) | Otocac Airport (LDRO) | 2026-04-26 04:07 UTC | 2026-04-26 04:17 UTC | 10m |
| JBU277 | JetBlue | Fort Lauderdale/Hollywood International Airport (KFLL) | Pecos Municipal Airport (KPEQ) | 2026-04-26 00:47 UTC | 2026-04-26 04:04 UTC | 3h 16m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-26 02:48 UTC | 2026-04-26 04:01 UTC | 1h 13m |
| JST650 | JST | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 2026-04-26 02:51 UTC | 2026-04-26 04:00 UTC | 1h 8m |
| N3844Q |  | 8FD2 (8FD2) | Ott's Landing Airport (0FA1) | 2026-04-26 01:44 UTC | 2026-04-26 03:50 UTC | 2h 6m |
| LFG223 | LFG | Mc Clellan-Palomar Airport (KCRQ) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-26 02:46 UTC | 2026-04-26 03:49 UTC | 1h 3m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-04-25 17:26 UTC | 2026-04-26 03:47 UTC | 10h 21m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-26 03:27 UTC | 2026-04-26 03:46 UTC | 19m |
| IGO146 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Shillong Airport (VEBI) | 2026-04-26 02:30 UTC | 2026-04-26 03:44 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
