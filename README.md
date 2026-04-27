# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_03:43:02_UTC-green)

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

**Latest saved flight:** 2026-04-27 03:43:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 03:43:02 UTC

- **56,408** saved flights
- **22,141** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,408** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **683,526.1 tonnes** estimated CO2 emissions
- **39,624,703 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2390 |
| 2 | SkyWest Airlines | 2134 |
| 3 | IndiGo | 1281 |
| 4 | EJA | 1012 |
| 5 | American Airlines | 900 |
| 6 | Southwest Airlines | 804 |
| 7 | ENY | 714 |
| 8 | Lufthansa | 691 |
| 9 | Vueling | 566 |
| 10 | AXM | 548 |
| 11 | LATAM Airlines | 547 |
| 12 | All Nippon Airways | 497 |
| 13 | AZU | 475 |
| 14 | Delta Air Lines | 466 |
| 15 | WIF | 466 |
| 16 | Swiss International | 439 |
| 17 | QLK | 438 |
| 18 | LXJ | 404 |
| 19 | Alaska Airlines | 380 |
| 20 | AEE | 371 |
| 21 | EJU | 361 |
| 22 | VIV | 361 |
| 23 | easyJet | 358 |
| 24 | Air France | 327 |
| 25 | Japan Airlines | 324 |
| 26 | Cathay Pacific | 321 |
| 27 | AXB | 306 |
| 28 | JetBlue | 288 |
| 29 | GLO | 285 |
| 30 | United Airlines | 285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44805 |
| 2 | 🇪🇸 ES | 4115 |
| 3 | 🇮🇳 IN | 4040 |
| 4 | 🇦🇺 AU | 3783 |
| 5 | 🇧🇷 BR | 3257 |
| 6 | 🇩🇪 DE | 3070 |
| 7 | 🇮🇹 IT | 3065 |
| 8 | 🇯🇵 JP | 3013 |
| 9 | 🇨🇦 CA | 2789 |
| 10 | 🇨🇴 CO | 2558 |
| 11 | 🇬🇧 GB | 2363 |
| 12 | 🇫🇷 FR | 2213 |
| 13 | 🇲🇽 MX | 1799 |
| 14 | 🇬🇷 GR | 1666 |
| 15 | 🇨🇭 CH | 1587 |
| 16 | 🇳🇴 NO | 1508 |
| 17 | 🇲🇾 MY | 1330 |
| 18 | 🇿🇦 ZA | 1151 |
| 19 | 🇳🇿 NZ | 1068 |
| 20 | 🇹🇷 TR | 1028 |
| 21 | 🇹🇭 TH | 1007 |
| 22 | 🇵🇭 PH | 958 |
| 23 | 🇵🇱 PL | 908 |
| 24 | 🇰🇷 KR | 900 |
| 25 | 🇬🇹 GT | 842 |
| 26 | 🇲🇦 MA | 714 |
| 27 | 🇲🇪 ME | 610 |
| 28 | 🇳🇱 NL | 589 |
| 29 | 🇲🇴 MO | 588 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1284 |
| 2 | Tokyo International Airport |  | JP | 1025 |
| 3 | Denver International Airport |  | US | 939 |
| 4 | El Dorado International Airport |  | CO | 864 |
| 5 | Indira Gandhi International Airport |  | IN | 854 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 820 |
| 7 | Guaymaral Airport |  | CO | 778 |
| 8 | Harry Reid International Airport |  | US | 719 |
| 9 | Frankfurt am Main International Airport |  | DE | 677 |
| 10 | Zurich Airport |  | CH | 674 |
| 11 | La Aurora Airport |  | GT | 633 |
| 12 | Macau International Airport |  | MO | 588 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 562 |
| 14 | Chicago O'Hare International Airport |  | US | 551 |
| 15 | Madrid Barajas International Airport |  | ES | 528 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 525 |
| 17 | Kuala Lumpur International Airport |  | MY | 524 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 498 |
| 19 | Malpensa International Airport |  | IT | 486 |
| 20 | Bengaluru International Airport |  | IN | 483 |
| 21 | Congonhas Airport |  | BR | 468 |
| 22 | Charlotte/Douglas International Airport |  | US | 456 |
| 23 | Tenerife Norte Airport |  | ES | 451 |
| 24 | Ninoy Aquino International Airport |  | PH | 441 |
| 25 | Salt Lake City International Airport |  | US | 433 |
| 26 | Charles de Gaulle International Airport |  | FR | 432 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 419 |
| 28 | Capua Airport |  | IT | 417 |
| 29 | Daniel K Inouye International Airport |  | US | 416 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 405 |
| 31 | Barcelona International Airport |  | ES | 386 |
| 32 | Vitoria/Foronda Airport |  | ES | 385 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 382 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 373 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 368 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 360 |
| 38 | Don Mueang International Airport |  | TH | 342 |
| 39 | Calgary International Airport |  | CA | 337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 336 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 317 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 208 | 14m | 114 km | 408.0 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 180 | 21m | 244 km | 757.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 180 | 24m | 225 km | 698.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 162 | 1h 27m | 910 km | 2,542.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 139 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 136 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 108 | 44m | 452 km | 841.7 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 1m | 695 km | 970.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 53m | 1,304 km | 1,732.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 74 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-27 03:29 UTC | 2026-04-27 03:43 UTC | 13m |
| N460AK |  | Ames Municipal Airport (KAMW) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-27 00:13 UTC | 2026-04-27 03:35 UTC | 3h 22m |
| N47354 |  | Addington Field (4TX8) | Decatur Municipal Airport (KLUD) | 2026-04-27 03:12 UTC | 2026-04-27 03:24 UTC | 12m |
| BOX718 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-26 16:32 UTC | 2026-04-27 03:04 UTC | 10h 32m |
| JAL2791 | Japan Airlines | Hakodate Airport (RJCH) | Aomori Airport (RJSA) | 2026-04-27 02:48 UTC | 2026-04-27 03:00 UTC | 12m |
| N7392J |  | Harrisburg International Airport (KMDT) | Washington Dulles International Airport (KIAD) | 2026-04-27 01:57 UTC | 2026-04-27 03:00 UTC | 1h 3m |
| AM398 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-04-27 02:39 UTC | 2026-04-27 03:00 UTC | 20m |
| UAE9780 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-26 20:30 UTC | 2026-04-27 02:59 UTC | 6h 29m |
| MPH9471 | MPH | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-26 15:49 UTC | 2026-04-27 02:58 UTC | 11h 8m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-27 02:21 UTC | 2026-04-27 02:58 UTC | 36m |
| LR8569 |  | Brisbane International Airport (YBBN) | Woodville Airport (YWVL) | 2026-04-27 02:01 UTC | 2026-04-27 02:49 UTC | 47m |
| HGB839 | HGB | Macau International Airport (VMMC) | Chek Lap Kok International Airport (VHHH) | 2026-04-27 02:38 UTC | 2026-04-27 02:44 UTC | 5m |
| XUM2593 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-04-27 02:06 UTC | 2026-04-27 02:43 UTC | 36m |
| XSN06 | XSN | Weed Airport (KO46) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-27 01:50 UTC | 2026-04-27 02:43 UTC | 53m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-04-27 02:15 UTC | 2026-04-27 02:42 UTC | 27m |
| AAL1223 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Harris River Ranch Airport (9CA7) | 2026-04-26 23:41 UTC | 2026-04-27 02:42 UTC | 3h 0m |
| QLK281 | QLK | Brisbane International Airport (YBBN) | Wellington International Airport (NZWN) | 2026-04-26 23:27 UTC | 2026-04-27 02:40 UTC | 3h 13m |
| N909GF |  | Stanton Airport (KI50) | Blue Grass Airport (KLEX) | 2026-04-27 02:20 UTC | 2026-04-27 02:39 UTC | 19m |
| FD607 |  | Perth Jandakot Airport (YPJT) | Manjimup Airport (YMJM) | 2026-04-27 01:57 UTC | 2026-04-27 02:38 UTC | 41m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Brunei International Airport (WBSB) | 2026-04-27 02:18 UTC | 2026-04-27 02:38 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
