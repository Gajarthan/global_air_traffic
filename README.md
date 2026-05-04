# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_23:20:37_UTC-green)

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

**Latest saved flight:** 2026-05-04 23:20:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 23:20:37 UTC

- **68,668** saved flights
- **25,764** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,668** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **844,209.5 tonnes** estimated CO2 emissions
- **48,939,683 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2948 |
| 2 | SkyWest Airlines | 2547 |
| 3 | IndiGo | 1581 |
| 4 | EJA | 1240 |
| 5 | American Airlines | 1066 |
| 6 | Southwest Airlines | 975 |
| 7 | Lufthansa | 880 |
| 8 | ENY | 847 |
| 9 | Vueling | 675 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 640 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 579 |
| 14 | Delta Air Lines | 578 |
| 15 | AZU | 559 |
| 16 | Swiss International | 529 |
| 17 | QLK | 525 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 471 |
| 20 | easyJet | 455 |
| 21 | AEE | 451 |
| 22 | EJU | 447 |
| 23 | VIV | 427 |
| 24 | Cathay Pacific | 415 |
| 25 | Air France | 404 |
| 26 | Japan Airlines | 399 |
| 27 | AXB | 387 |
| 28 | CXK | 348 |
| 29 | AIQ | 346 |
| 30 | MXY | 335 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54495 |
| 2 | 🇪🇸 ES | 5025 |
| 3 | 🇮🇳 IN | 4981 |
| 4 | 🇦🇺 AU | 4517 |
| 5 | 🇧🇷 BR | 3862 |
| 6 | 🇩🇪 DE | 3833 |
| 7 | 🇮🇹 IT | 3763 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3384 |
| 10 | 🇬🇧 GB | 2977 |
| 11 | 🇫🇷 FR | 2722 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2183 |
| 14 | 🇬🇷 GR | 2060 |
| 15 | 🇨🇭 CH | 1903 |
| 16 | 🇳🇴 NO | 1871 |
| 17 | 🇲🇾 MY | 1637 |
| 18 | 🇿🇦 ZA | 1373 |
| 19 | 🇳🇿 NZ | 1274 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1226 |
| 22 | 🇵🇭 PH | 1145 |
| 23 | 🇵🇱 PL | 1125 |
| 24 | 🇬🇹 GT | 1111 |
| 25 | 🇰🇷 KR | 1091 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 779 |
| 28 | 🇲🇪 ME | 742 |
| 29 | 🇳🇱 NL | 714 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1517 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1127 |
| 4 | Indira Gandhi International Airport |  | IN | 1043 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1006 |
| 6 | Frankfurt am Main International Airport |  | DE | 881 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 857 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 827 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 779 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 677 |
| 14 | Chicago O'Hare International Airport |  | US | 659 |
| 15 | Kuala Lumpur International Airport |  | MY | 656 |
| 16 | Madrid Barajas International Airport |  | ES | 654 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 615 |
| 18 | Bengaluru International Airport |  | IN | 603 |
| 19 | Malpensa International Airport |  | IT | 599 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 592 |
| 21 | Congonhas Airport |  | BR | 552 |
| 22 | Salt Lake City International Airport |  | US | 548 |
| 23 | Charlotte/Douglas International Airport |  | US | 543 |
| 24 | Tenerife Norte Airport |  | ES | 540 |
| 25 | Charles de Gaulle International Airport |  | FR | 539 |
| 26 | Capua Airport |  | IT | 528 |
| 27 | Ninoy Aquino International Airport |  | PH | 521 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 502 |
| 29 | Daniel K Inouye International Airport |  | US | 500 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 483 |
| 31 | Barcelona International Airport |  | ES | 477 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 466 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 457 |
| 34 | Vitoria/Foronda Airport |  | ES | 455 |
| 35 | O. R. Tambo International Airport |  | ZA | 434 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 430 |
| 38 | Amsterdam Airport Schiphol |  | NL | 421 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 406 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 235 | 21m | 244 km | 989.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 154 | 26m | 275 km | 729.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 130 | 21m | 99 km | 222.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 115 | 31m | 369 km | 732.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 96 | 14m | 154 km | 254.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 95 | 1h 2m | 695 km | 1,138.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R21202 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-04 21:46 UTC | 2026-05-04 23:20 UTC | 1h 33m |
| ROLR31 | ROL | Mount Hotham Airport (YHOT) | Mount Hotham Airport (YHOT) | 2026-05-04 22:38 UTC | 2026-05-04 23:18 UTC | 39m |
| SWA2315 | Southwest Airlines | San Francisco International Airport (KSFO) | Camarillo Airport (KCMA) | 2026-05-04 22:12 UTC | 2026-05-04 23:08 UTC | 56m |
| N563M |  | Eppley Airfield (KOMA) | Joe Foss Field (KFSD) | 2026-05-04 22:38 UTC | 2026-05-04 23:08 UTC | 29m |
| CGHHA | CGH | Vancouver International Airport (CYVR) | Vancouver International Airport (CYVR) | 2026-05-04 22:51 UTC | 2026-05-04 23:06 UTC | 14m |
| N1201F |  | Ogden-Hinckley Airport (KOGD) | Logan-Cache Airport (KLGU) | 2026-05-04 22:37 UTC | 2026-05-04 23:03 UTC | 25m |
| N632AA |  | North Palm Beach County General Aviation Airport (KF45) | William P Gwinn Airport (06FA) | 2026-05-04 22:41 UTC | 2026-05-04 23:01 UTC | 19m |
| N2305R |  | Montgomery County Airpark (KGAI) | Lancaster Airport (KLNS) | 2026-05-04 22:27 UTC | 2026-05-04 22:59 UTC | 31m |
| TORA11 | TOR | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Nelson High Point Airport (8OK7) | 2026-05-04 22:28 UTC | 2026-05-04 22:53 UTC | 25m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-04 11:45 UTC | 2026-05-04 22:52 UTC | 11h 6m |
| N121M |  | Nampa Municipal Airport (KMAN) | Reek Ranch Airport (ID63) | 2026-05-04 22:38 UTC | 2026-05-04 22:52 UTC | 13m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-05-04 11:33 UTC | 2026-05-04 22:50 UTC | 11h 17m |
| N549CP |  | Portland International Airport (KPDX) | Lincoln Airport (KLNK) | 2026-05-04 19:38 UTC | 2026-05-04 22:48 UTC | 3h 9m |
| N449BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-05-04 21:50 UTC | 2026-05-04 22:46 UTC | 56m |
| N345MJ |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-05-04 22:08 UTC | 2026-05-04 22:46 UTC | 37m |
| N911ZQ |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-05-04 22:36 UTC | 2026-05-04 22:45 UTC | 8m |
| N370MR |  | Felts Field (KSFF) | 4WA6 (4WA6) | 2026-05-04 22:20 UTC | 2026-05-04 22:40 UTC | 20m |
| LR453 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-05-04 22:05 UTC | 2026-05-04 22:38 UTC | 32m |
| T7SABAH |  | Sultan Abdul Aziz Shah International Airport (WMSA) | Kota Kinabalu International Airport (WBKK) | 2026-05-04 20:25 UTC | 2026-05-04 22:33 UTC | 2h 8m |
| CUL550 | CUL | Palm Springs International Airport (KPSP) | Bermuda Dunes Airport (KUDD) | 2026-05-04 22:17 UTC | 2026-05-04 22:31 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
