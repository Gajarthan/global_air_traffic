# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_03:39:04_UTC-green)

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

**Latest saved flight:** 2026-05-09 03:39:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 03:39:04 UTC

- **74,801** saved flights
- **27,627** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,801** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **920,488.8 tonnes** estimated CO2 emissions
- **53,361,669 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3201 |
| 2 | SkyWest Airlines | 2787 |
| 3 | IndiGo | 1672 |
| 4 | EJA | 1387 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1088 |
| 7 | Lufthansa | 963 |
| 8 | ENY | 937 |
| 9 | Vueling | 725 |
| 10 | AXM | 700 |
| 11 | Delta Air Lines | 696 |
| 12 | LATAM Airlines | 693 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 607 |
| 15 | AZU | 601 |
| 16 | QLK | 579 |
| 17 | Swiss International | 566 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 529 |
| 20 | easyJet | 490 |
| 21 | EJU | 479 |
| 22 | AEE | 478 |
| 23 | Cathay Pacific | 469 |
| 24 | VIV | 454 |
| 25 | Japan Airlines | 436 |
| 26 | Air France | 431 |
| 27 | AXB | 413 |
| 28 | CXK | 384 |
| 29 | AIQ | 367 |
| 30 | MXY | 363 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60394 |
| 2 | 🇪🇸 ES | 5376 |
| 3 | 🇮🇳 IN | 5254 |
| 4 | 🇦🇺 AU | 4934 |
| 5 | 🇧🇷 BR | 4195 |
| 6 | 🇩🇪 DE | 4169 |
| 7 | 🇮🇹 IT | 4062 |
| 8 | 🇯🇵 JP | 3893 |
| 9 | 🇨🇦 CA | 3739 |
| 10 | 🇬🇧 GB | 3197 |
| 11 | 🇫🇷 FR | 2940 |
| 12 | 🇨🇴 CO | 2690 |
| 13 | 🇲🇽 MX | 2325 |
| 14 | 🇬🇷 GR | 2198 |
| 15 | 🇳🇴 NO | 2076 |
| 16 | 🇨🇭 CH | 2017 |
| 17 | 🇲🇾 MY | 1748 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1359 |
| 20 | 🇹🇷 TR | 1329 |
| 21 | 🇹🇭 TH | 1319 |
| 22 | 🇵🇱 PL | 1244 |
| 23 | 🇵🇭 PH | 1210 |
| 24 | 🇬🇹 GT | 1184 |
| 25 | 🇰🇷 KR | 1169 |
| 26 | 🇲🇦 MA | 885 |
| 27 | 🇲🇴 MO | 863 |
| 28 | 🇲🇪 ME | 796 |
| 29 | 🇳🇱 NL | 775 |
| 30 | 🇧🇸 BS | 627 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1309 |
| 3 | Denver International Airport |  | US | 1258 |
| 4 | Indira Gandhi International Airport |  | IN | 1108 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1077 |
| 6 | Frankfurt am Main International Airport |  | DE | 960 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | La Aurora Airport |  | GT | 888 |
| 9 | Guaymaral Airport |  | CO | 885 |
| 10 | El Dorado International Airport |  | CO | 878 |
| 11 | Zurich Airport |  | CH | 877 |
| 12 | Macau International Airport |  | MO | 863 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 728 |
| 15 | Kuala Lumpur International Airport |  | MY | 702 |
| 16 | Madrid Barajas International Airport |  | ES | 700 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 664 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 648 |
| 19 | Bengaluru International Airport |  | IN | 647 |
| 20 | Malpensa International Airport |  | IT | 644 |
| 21 | Salt Lake City International Airport |  | US | 617 |
| 22 | Congonhas Airport |  | BR | 596 |
| 23 | Charlotte/Douglas International Airport |  | US | 590 |
| 24 | Charles de Gaulle International Airport |  | FR | 577 |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 575 |
| 26 | Capua Airport |  | IT | 575 |
| 27 | Tenerife Norte Airport |  | ES | 559 |
| 28 | Ninoy Aquino International Airport |  | PH | 549 |
| 29 | Daniel K Inouye International Airport |  | US | 548 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 535 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 518 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 503 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 468 |
| 37 | Amsterdam Airport Schiphol |  | NL | 467 |
| 38 | Don Mueang International Airport |  | TH | 464 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 270 | 1h 8m | 706 km | 3,287.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 265 | 21m | 244 km | 1,115.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 218 | 24m | 225 km | 845.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 210 | 28m | 304 km | 1,100.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 205 | 1h 27m | 910 km | 3,216.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 180 | 20m | 165 km | 512.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 137 | 21m | 99 km | 234.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 108 | 14m | 154 km | 286.2 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 102 | 1h 2m | 695 km | 1,222.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 100 | 1h 42m | 1,423 km | 2,454.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK126 | CXK | Centennial Airport (KAPA) | Northern Colorado Regional Airport (KFNL) | 2026-05-09 03:04 UTC | 2026-05-09 03:39 UTC | 34m |
| N734VJ |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-05-09 03:09 UTC | 2026-05-09 03:23 UTC | 13m |
| DAL170 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 02:38 UTC | 2026-05-09 03:19 UTC | 40m |
| DAL2138 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 03:11 UTC | 2026-05-09 03:11 UTC | 0m |
| RPA5743 | Republic Airways | John F Kennedy International Airport (KJFK) | Fort Meade Executive Airport (KFME) | 2026-05-09 02:11 UTC | 2026-05-09 03:01 UTC | 50m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 02:07 UTC | 2026-05-09 02:58 UTC | 50m |
| N371LL |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Cloquet/Carlton County Airport (KCOQ) | 2026-05-09 02:28 UTC | 2026-05-09 02:56 UTC | 28m |
| N505TJ |  | 3NY9 (3NY9) | Fort Erie Airport (CNJ3) | 2026-05-09 02:45 UTC | 2026-05-09 02:54 UTC | 9m |
| N500FE |  | Flying Cloud Airport (KFCM) | 0SD6 (0SD6) | 2026-05-09 01:15 UTC | 2026-05-09 02:51 UTC | 1h 36m |
| DAL2138 | Delta Air Lines | Chicago O'Hare International Airport (KORD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 01:43 UTC | 2026-05-09 02:46 UTC | 1h 3m |
| RDK5 | RDK | Lauderdale Airport (49TA) | William P Hobby Airport (KHOU) | 2026-05-09 02:28 UTC | 2026-05-09 02:46 UTC | 18m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-05-09 02:22 UTC | 2026-05-09 02:45 UTC | 23m |
| XUM2593 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-05-09 02:03 UTC | 2026-05-09 02:43 UTC | 39m |
| QLK205D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-05-09 01:37 UTC | 2026-05-09 02:36 UTC | 58m |
| DAL1220 | Delta Air Lines | Denver International Airport (KDEN) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 01:00 UTC | 2026-05-09 02:35 UTC | 1h 34m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-05-09 02:07 UTC | 2026-05-09 02:33 UTC | 25m |
| VIV7017 | VIV | Leon Gonzales Pie De La Cuesta Airport (MM41) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-09 01:57 UTC | 2026-05-09 02:31 UTC | 33m |
| SWA3569 | Southwest Airlines | Oakland San Francisco Bay Airport (KOAK) | Palm Springs International Airport (KPSP) | 2026-05-09 01:35 UTC | 2026-05-09 02:31 UTC | 55m |
| HKE600 | HKE | Chek Lap Kok International Airport (VHHH) | Saga Airport (RJFS) | 2026-05-08 23:54 UTC | 2026-05-09 02:30 UTC | 2h 36m |
| FFT3315 | FFT | Los Angeles International Airport (KLAX) | Sacramento International Airport (KSMF) | 2026-05-09 01:20 UTC | 2026-05-09 02:30 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
