# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_17:12:32_UTC-green)

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

**Latest saved flight:** 2026-05-03 17:12:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 17:12:32 UTC

- **66,272** saved flights
- **25,054** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,272** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **813,337.2 tonnes** estimated CO2 emissions
- **47,149,983 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2832 |
| 2 | SkyWest Airlines | 2434 |
| 3 | IndiGo | 1543 |
| 4 | EJA | 1169 |
| 5 | American Airlines | 1021 |
| 6 | Southwest Airlines | 931 |
| 7 | Lufthansa | 854 |
| 8 | ENY | 815 |
| 9 | Vueling | 655 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 616 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 556 |
| 14 | WIF | 553 |
| 15 | AZU | 534 |
| 16 | QLK | 513 |
| 17 | Swiss International | 512 |
| 18 | LXJ | 476 |
| 19 | Alaska Airlines | 449 |
| 20 | easyJet | 441 |
| 21 | AEE | 433 |
| 22 | EJU | 431 |
| 23 | VIV | 413 |
| 24 | Cathay Pacific | 397 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 374 |
| 28 | AIQ | 339 |
| 29 | CXK | 338 |
| 30 | GLO | 323 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52237 |
| 2 | 🇪🇸 ES | 4880 |
| 3 | 🇮🇳 IN | 4847 |
| 4 | 🇦🇺 AU | 4410 |
| 5 | 🇩🇪 DE | 3726 |
| 6 | 🇧🇷 BR | 3721 |
| 7 | 🇮🇹 IT | 3631 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3230 |
| 10 | 🇬🇧 GB | 2868 |
| 11 | 🇨🇴 CO | 2651 |
| 12 | 🇫🇷 FR | 2642 |
| 13 | 🇲🇽 MX | 2093 |
| 14 | 🇬🇷 GR | 1990 |
| 15 | 🇨🇭 CH | 1866 |
| 16 | 🇳🇴 NO | 1802 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1196 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1095 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1030 |
| 26 | 🇲🇦 MA | 815 |
| 27 | 🇲🇴 MO | 744 |
| 28 | 🇲🇪 ME | 719 |
| 29 | 🇳🇱 NL | 706 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1448 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1084 |
| 4 | Indira Gandhi International Airport |  | IN | 1009 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 969 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 859 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 824 |
| 10 | Zurich Airport |  | CH | 791 |
| 11 | La Aurora Airport |  | GT | 769 |
| 12 | Macau International Airport |  | MO | 744 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 649 |
| 14 | Kuala Lumpur International Airport |  | MY | 639 |
| 15 | Madrid Barajas International Airport |  | ES | 636 |
| 16 | Chicago O'Hare International Airport |  | US | 630 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 594 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 572 |
| 21 | Congonhas Airport |  | BR | 536 |
| 22 | Tenerife Norte Airport |  | ES | 530 |
| 23 | Charlotte/Douglas International Airport |  | US | 522 |
| 24 | Charles de Gaulle International Airport |  | FR | 522 |
| 25 | Salt Lake City International Airport |  | US | 521 |
| 26 | Ninoy Aquino International Airport |  | PH | 504 |
| 27 | Capua Airport |  | IT | 503 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 484 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 467 |
| 31 | Barcelona International Airport |  | ES | 454 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 445 |
| 33 | Vitoria/Foronda Airport |  | ES | 443 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 442 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Amsterdam Airport Schiphol |  | NL | 415 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 414 |
| 39 | Reno/Tahoe International Airport |  | US | 400 |
| 40 | Calgary International Airport |  | CA | 385 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 224 | 21m | 244 km | 943.2 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 162 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 119 | 21m | 99 km | 203.8 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 106 | 28m | 152 km | 277.0 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 99 | 20m | 147 km | 250.5 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 93 | 1h 42m | 1,156 km | 1,855.3 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 53m | 1,304 km | 2,024.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N109LD |  | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-03 15:51 UTC | 2026-05-03 17:12 UTC | 1h 20m |
| N1322K |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-03 16:49 UTC | 2026-05-03 17:06 UTC | 16m |
| N592DR |  | Mc Clellan-Palomar Airport (KCRQ) | Santa Barbara Municipal Airport (KSBA) | 2026-05-03 16:26 UTC | 2026-05-03 17:05 UTC | 39m |
| 3AMTT |  | La Mole Airport (LFTZ) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-03 16:40 UTC | 2026-05-03 17:01 UTC | 20m |
| SVI1102 | SVI | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-05-03 12:00 UTC | 2026-05-03 16:57 UTC | 4h 57m |
| N6461Z |  | Grants-Milan Municipal Airport (KGNT) | Grants-Milan Municipal Airport (KGNT) | 2026-05-03 15:38 UTC | 2026-05-03 16:57 UTC | 1h 18m |
| N4304L |  | Casper/Natrona County International Airport (KCPR) | Willow Creek Ranch Airport (10WY) | 2026-05-03 16:26 UTC | 2026-05-03 16:51 UTC | 24m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-03 16:34 UTC | 2026-05-03 16:48 UTC | 13m |
| EZS68GV | EZS | Geneva Cointrin International Airport (LSGG) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-03 14:31 UTC | 2026-05-03 16:47 UTC | 2h 16m |
| N396FS |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-03 16:23 UTC | 2026-05-03 16:47 UTC | 24m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-03 16:25 UTC | 2026-05-03 16:44 UTC | 19m |
| N228YK |  | Knape Airport (2XA2) | TE77 (TE77) | 2026-05-03 16:23 UTC | 2026-05-03 16:42 UTC | 19m |
| JRE863 | JRE | Louisville Muhammad Ali International Airport (KSDF) | Dubuque Regional Airport (KDBQ) | 2026-05-03 15:30 UTC | 2026-05-03 16:41 UTC | 1h 11m |
| N9736Y |  | Eagle Soaring Airport (1CD4) | Yampa Valley Airport (KHDN) | 2026-05-03 16:23 UTC | 2026-05-03 16:40 UTC | 17m |
| N25995 |  | Stocker Airport (XA72) | TX39 (TX39) | 2026-05-03 16:10 UTC | 2026-05-03 16:40 UTC | 29m |
| N124RK |  | Sky Ranch At Carefree Airport (18AZ) | Montezuma Airport (19AZ) | 2026-05-03 16:20 UTC | 2026-05-03 16:35 UTC | 14m |
| N802CC |  | 11TX (11TX) | 5TA6 (5TA6) | 2026-05-03 16:07 UTC | 2026-05-03 16:35 UTC | 27m |
| N733K |  | Dallas Love Field (KDAL) | San Antonio International Airport (KSAT) | 2026-05-03 15:47 UTC | 2026-05-03 16:34 UTC | 46m |
| N16LV |  | Birmingham-Shuttlesworth International Airport (KBHM) | Selfs Airport (KMMS) | 2026-05-03 16:02 UTC | 2026-05-03 16:31 UTC | 28m |
| PFT250 | PFT | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-05-03 16:13 UTC | 2026-05-03 16:29 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
