# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_16:10:08_UTC-green)

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

**Latest saved flight:** 2026-05-03 16:10:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 16:10:08 UTC

- **66,109** saved flights
- **24,991** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,109** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **811,395.7 tonnes** estimated CO2 emissions
- **47,037,430 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2821 |
| 2 | SkyWest Airlines | 2427 |
| 3 | IndiGo | 1540 |
| 4 | EJA | 1164 |
| 5 | American Airlines | 1016 |
| 6 | Southwest Airlines | 928 |
| 7 | Lufthansa | 853 |
| 8 | ENY | 812 |
| 9 | Vueling | 654 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 615 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 554 |
| 14 | WIF | 552 |
| 15 | AZU | 533 |
| 16 | QLK | 513 |
| 17 | Swiss International | 510 |
| 18 | LXJ | 472 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 440 |
| 21 | AEE | 430 |
| 22 | EJU | 428 |
| 23 | VIV | 411 |
| 24 | Cathay Pacific | 397 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 373 |
| 28 | AIQ | 339 |
| 29 | CXK | 336 |
| 30 | GLO | 322 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52064 |
| 2 | 🇪🇸 ES | 4869 |
| 3 | 🇮🇳 IN | 4833 |
| 4 | 🇦🇺 AU | 4410 |
| 5 | 🇧🇷 BR | 3715 |
| 6 | 🇩🇪 DE | 3715 |
| 7 | 🇮🇹 IT | 3620 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3227 |
| 10 | 🇬🇧 GB | 2864 |
| 11 | 🇨🇴 CO | 2651 |
| 12 | 🇫🇷 FR | 2633 |
| 13 | 🇲🇽 MX | 2087 |
| 14 | 🇬🇷 GR | 1984 |
| 15 | 🇨🇭 CH | 1862 |
| 16 | 🇳🇴 NO | 1799 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1193 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1094 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1023 |
| 26 | 🇲🇦 MA | 813 |
| 27 | 🇲🇴 MO | 743 |
| 28 | 🇲🇪 ME | 719 |
| 29 | 🇳🇱 NL | 703 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1443 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1081 |
| 4 | Indira Gandhi International Airport |  | IN | 1005 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 964 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 856 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 822 |
| 10 | Zurich Airport |  | CH | 789 |
| 11 | La Aurora Airport |  | GT | 765 |
| 12 | Macau International Airport |  | MO | 743 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 644 |
| 14 | Kuala Lumpur International Airport |  | MY | 639 |
| 15 | Madrid Barajas International Airport |  | ES | 636 |
| 16 | Chicago O'Hare International Airport |  | US | 628 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 593 |
| 18 | Bengaluru International Airport |  | IN | 593 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 572 |
| 21 | Congonhas Airport |  | BR | 535 |
| 22 | Tenerife Norte Airport |  | ES | 530 |
| 23 | Charlotte/Douglas International Airport |  | US | 522 |
| 24 | Charles de Gaulle International Airport |  | FR | 522 |
| 25 | Salt Lake City International Airport |  | US | 518 |
| 26 | Ninoy Aquino International Airport |  | PH | 504 |
| 27 | Capua Airport |  | IT | 499 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 487 |
| 29 | Daniel K Inouye International Airport |  | US | 483 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 467 |
| 31 | Barcelona International Airport |  | ES | 452 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 442 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 442 |
| 34 | Vitoria/Foronda Airport |  | ES | 442 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Amsterdam Airport Schiphol |  | NL | 413 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 412 |
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
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 118 | 21m | 99 km | 202.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 106 | 28m | 152 km | 277.0 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 99 | 20m | 147 km | 250.5 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 53m | 1,304 km | 2,024.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 88 | 1h 42m | 1,423 km | 2,159.7 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 0 |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-05-03 15:42 UTC | 2026-05-03 16:10 UTC | 28m |
| N46SD |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | Kaslo Airport (CBR2) | 2026-05-03 15:01 UTC | 2026-05-03 16:09 UTC | 1h 7m |
| N734UZ |  | San Luis Obispo County Regional Airport (KSBP) | Santa Barbara Municipal Airport (KSBA) | 2026-05-03 15:09 UTC | 2026-05-03 16:00 UTC | 51m |
| N469AA |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-05-03 15:59 UTC | 2026-05-03 16:00 UTC | 0m |
| GWARX | GWA | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-05-03 15:45 UTC | 2026-05-03 15:58 UTC | 13m |
| N344BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-05-03 14:23 UTC | 2026-05-03 15:58 UTC | 1h 35m |
| N4976G |  | Double W Airport (3OK7) | Tulsa Riverside Airport (KRVS) | 2026-05-03 15:13 UTC | 2026-05-03 15:56 UTC | 43m |
| N8137U |  | Fort Worth Meacham International Airport (KFTW) | Jim Sears Airport (3TA7) | 2026-05-03 14:06 UTC | 2026-05-03 15:56 UTC | 1h 50m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-03 15:42 UTC | 2026-05-03 15:54 UTC | 11m |
| TGRIO | TGR | Esquipulas Airport (MGES) | La Aurora Airport (MGGT) | 2026-05-03 15:36 UTC | 2026-05-03 15:54 UTC | 17m |
| N832CA |  | Crystal Springs Ranch Airport (UT54) | North Las Vegas Airport (KVGT) | 2026-05-03 15:00 UTC | 2026-05-03 15:53 UTC | 52m |
| OXF9846 | OXF | Payson Airport (KPAN) | Rimrock Airport (48AZ) | 2026-05-03 15:40 UTC | 2026-05-03 15:51 UTC | 11m |
| N379NL |  | Delaware Coastal Airport (KGED) | Pine Island Airport (7NC2) | 2026-05-03 14:29 UTC | 2026-05-03 15:50 UTC | 1h 20m |
| FDB573 | flydubai | Dubai International Airport (OMDB) | Simara Airport (VNSI) | 2026-05-03 12:20 UTC | 2026-05-03 15:47 UTC | 3h 27m |
| CGPMK | CGP | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-05-03 15:15 UTC | 2026-05-03 15:46 UTC | 31m |
| N912BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-05-03 15:44 UTC | 2026-05-03 15:44 UTC | 0m |
| N106PA |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-03 15:20 UTC | 2026-05-03 15:43 UTC | 22m |
| N169BA |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-05-03 15:33 UTC | 2026-05-03 15:42 UTC | 9m |
| SCU59 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Barcus Field (95OK) | 2026-05-03 15:12 UTC | 2026-05-03 15:39 UTC | 27m |
| RYR19SY | Ryanair | Ireland West Knock Airport (EIKN) | East Midlands Airport (EGNX) | 2026-05-03 14:46 UTC | 2026-05-03 15:39 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
