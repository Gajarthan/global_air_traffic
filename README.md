# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_03:48:46_UTC-green)

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

**Latest saved flight:** 2026-05-12 03:48:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 03:48:46 UTC

- **78,418** saved flights
- **28,618** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,418** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **971,294.9 tonnes** estimated CO2 emissions
- **56,306,949 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3376 |
| 2 | SkyWest Airlines | 2924 |
| 3 | IndiGo | 1733 |
| 4 | EJA | 1450 |
| 5 | American Airlines | 1225 |
| 6 | Southwest Airlines | 1154 |
| 7 | Lufthansa | 1023 |
| 8 | ENY | 980 |
| 9 | Delta Air Lines | 858 |
| 10 | Vueling | 752 |
| 11 | AXM | 721 |
| 12 | LATAM Airlines | 714 |
| 13 | WIF | 675 |
| 14 | All Nippon Airways | 628 |
| 15 | AZU | 620 |
| 16 | Swiss International | 599 |
| 17 | QLK | 591 |
| 18 | LXJ | 571 |
| 19 | Alaska Airlines | 552 |
| 20 | easyJet | 525 |
| 21 | EJU | 509 |
| 22 | AEE | 508 |
| 23 | Cathay Pacific | 500 |
| 24 | VIV | 467 |
| 25 | Air France | 462 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 435 |
| 28 | CXK | 402 |
| 29 | MXY | 394 |
| 30 | AIQ | 387 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63581 |
| 2 | 🇪🇸 ES | 5613 |
| 3 | 🇮🇳 IN | 5440 |
| 4 | 🇦🇺 AU | 5045 |
| 5 | 🇩🇪 DE | 4433 |
| 6 | 🇧🇷 BR | 4343 |
| 7 | 🇮🇹 IT | 4334 |
| 8 | 🇯🇵 JP | 4033 |
| 9 | 🇨🇦 CA | 3885 |
| 10 | 🇬🇧 GB | 3373 |
| 11 | 🇫🇷 FR | 3111 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2388 |
| 14 | 🇬🇷 GR | 2312 |
| 15 | 🇳🇴 NO | 2144 |
| 16 | 🇨🇭 CH | 2110 |
| 17 | 🇲🇾 MY | 1808 |
| 18 | 🇿🇦 ZA | 1486 |
| 19 | 🇹🇷 TR | 1418 |
| 20 | 🇳🇿 NZ | 1396 |
| 21 | 🇹🇭 TH | 1386 |
| 22 | 🇵🇱 PL | 1309 |
| 23 | 🇵🇭 PH | 1244 |
| 24 | 🇰🇷 KR | 1218 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 925 |
| 27 | 🇲🇴 MO | 916 |
| 28 | 🇲🇪 ME | 839 |
| 29 | 🇳🇱 NL | 816 |
| 30 | 🇭🇷 HR | 681 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1731 |
| 2 | Tokyo International Airport |  | JP | 1356 |
| 3 | Denver International Airport |  | US | 1316 |
| 4 | Indira Gandhi International Airport |  | IN | 1153 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1134 |
| 6 | Frankfurt am Main International Airport |  | DE | 1027 |
| 7 | Harry Reid International Airport |  | US | 974 |
| 8 | Zurich Airport |  | CH | 926 |
| 9 | Macau International Airport |  | MO | 916 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 872 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 797 |
| 15 | Chicago O'Hare International Airport |  | US | 765 |
| 16 | Kuala Lumpur International Airport |  | MY | 726 |
| 17 | Madrid Barajas International Airport |  | ES | 723 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 696 |
| 19 | Malpensa International Airport |  | IT | 678 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 674 |
| 21 | Bengaluru International Airport |  | IN | 672 |
| 22 | Salt Lake City International Airport |  | US | 644 |
| 23 | Capua Airport |  | IT | 629 |
| 24 | Charlotte/Douglas International Airport |  | US | 621 |
| 25 | Charles de Gaulle International Airport |  | FR | 616 |
| 26 | Congonhas Airport |  | BR | 614 |
| 27 | Tenerife Norte Airport |  | ES | 584 |
| 28 | Daniel K Inouye International Airport |  | US | 569 |
| 29 | Ninoy Aquino International Airport |  | PH | 566 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 558 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 531 |
| 32 | Barcelona International Airport |  | ES | 529 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 514 |
| 35 | Vitoria/Foronda Airport |  | ES | 498 |
| 36 | Don Mueang International Airport |  | TH | 494 |
| 37 | Amsterdam Airport Schiphol |  | NL | 492 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 485 |
| 39 | O. R. Tambo International Airport |  | ZA | 468 |
| 40 | Calgary International Airport |  | CA | 464 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 282 | 21m | 244 km | 1,187.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 185 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 173 | 1h 12m | 770 km | 2,298.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 111 | 14m | 154 km | 294.1 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 103 | 23m | 55 km | 97.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ELY5183 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-12 03:33 UTC | 2026-05-12 03:48 UTC | 15m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-05-12 03:30 UTC | 2026-05-12 03:46 UTC | 15m |
| ERU37 | ERU | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-05-12 03:26 UTC | 2026-05-12 03:45 UTC | 19m |
| ANA964 | All Nippon Airways | Tottori Airport (RJOR) | Tokyo International Airport (RJTT) | 2026-05-12 02:44 UTC | 2026-05-12 03:43 UTC | 58m |
| SCU28 | SCU | Airman Acres Airport (OK93) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-05-12 02:44 UTC | 2026-05-12 03:22 UTC | 38m |
| N410W |  | Central Il Regional/Bloomington-Normal Airport (KBMI) | Frasca Field (KC16) | 2026-05-12 02:48 UTC | 2026-05-12 03:22 UTC | 34m |
| G8524557 |  | KU42 (KU42) | KU42 (KU42) | 2026-05-12 02:59 UTC | 2026-05-12 03:19 UTC | 20m |
| N454DR |  | Midwest Ntl Air Center Airport (KGPH) | Abilene Municipal Airport (KK78) | 2026-05-12 02:44 UTC | 2026-05-12 03:07 UTC | 22m |
| ZHU | ZHU | Lilydale Airport (YLIL) | Melbourne Essendon Airport (YMEN) | 2026-05-12 02:44 UTC | 2026-05-12 02:57 UTC | 12m |
| N292P |  | Perkins Field (KU08) | Mesquite Airport (K67L) | 2026-05-12 02:44 UTC | 2026-05-12 02:55 UTC | 10m |
| IGO2121 | IndiGo | Chakulia Airport (VECK) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-12 02:44 UTC | 2026-05-12 02:55 UTC | 10m |
| XHI | XHI | Lilydale Airport (YLIL) | Melbourne Essendon Airport (YMEN) | 2026-05-12 02:44 UTC | 2026-05-12 02:53 UTC | 8m |
| KYOTE92 | KYO | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-12 02:49 UTC | 2026-05-12 02:50 UTC | 1m |
|  |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-05-11 19:04 UTC | 2026-05-11 20:36 UTC | 1h 32m |
| SCX6011 | SCX | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 18:17 UTC | 2026-05-11 20:36 UTC | 2h 18m |
| LOST42 | LOS | Norman Y Mineta San Jose International Airport (KSJC) | Meadows Field (KBFL) | 2026-05-11 19:29 UTC | 2026-05-11 20:35 UTC | 1h 5m |
| N734YM |  | 1NY9 (1NY9) | Oswego County Airport (KFZY) | 2026-05-11 20:23 UTC | 2026-05-11 20:34 UTC | 10m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-11 06:01 UTC | 2026-05-11 20:25 UTC | 14h 24m |
| BRG590 | BRG | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-05-11 20:09 UTC | 2026-05-11 20:24 UTC | 14m |
| CXK347 | CXK | Tucson International Airport (KTUS) | Tucson International Airport (KTUS) | 2026-05-11 19:46 UTC | 2026-05-11 20:21 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
