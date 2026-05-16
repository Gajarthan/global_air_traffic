# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_06:51:43_UTC-green)

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

**Latest saved flight:** 2026-05-16 06:51:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 06:51:43 UTC

- **84,265** saved flights
- **30,376** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,265** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,037,087.0 tonnes** estimated CO2 emissions
- **60,120,983 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3600 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1815 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1300 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1070 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 921 |
| 10 | Vueling | 796 |
| 11 | LATAM Airlines | 764 |
| 12 | AXM | 759 |
| 13 | WIF | 726 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 656 |
| 16 | Swiss International | 648 |
| 17 | QLK | 620 |
| 18 | LXJ | 619 |
| 19 | Alaska Airlines | 598 |
| 20 | easyJet | 552 |
| 21 | EJU | 535 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 528 |
| 24 | VIV | 505 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 472 |
| 27 | CXK | 446 |
| 28 | AXB | 445 |
| 29 | MXY | 420 |
| 30 | United Airlines | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69172 |
| 2 | 🇪🇸 ES | 5945 |
| 3 | 🇮🇳 IN | 5680 |
| 4 | 🇦🇺 AU | 5407 |
| 5 | 🇩🇪 DE | 4675 |
| 6 | 🇧🇷 BR | 4643 |
| 7 | 🇮🇹 IT | 4640 |
| 8 | 🇯🇵 JP | 4235 |
| 9 | 🇨🇦 CA | 4203 |
| 10 | 🇬🇧 GB | 3580 |
| 11 | 🇫🇷 FR | 3328 |
| 12 | 🇨🇴 CO | 2821 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2441 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2218 |
| 17 | 🇲🇾 MY | 1907 |
| 18 | 🇿🇦 ZA | 1578 |
| 19 | 🇹🇷 TR | 1495 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1461 |
| 22 | 🇵🇱 PL | 1395 |
| 23 | 🇵🇭 PH | 1319 |
| 24 | 🇰🇷 KR | 1290 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 977 |
| 27 | 🇲🇴 MO | 967 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 861 |
| 30 | 🇭🇷 HR | 753 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1849 |
| 2 | Denver International Airport |  | US | 1419 |
| 3 | Tokyo International Airport |  | JP | 1418 |
| 4 | Indira Gandhi International Airport |  | IN | 1209 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1184 |
| 6 | Frankfurt am Main International Airport |  | DE | 1083 |
| 7 | Harry Reid International Airport |  | US | 1060 |
| 8 | Zurich Airport |  | CH | 994 |
| 9 | Macau International Airport |  | MO | 967 |
| 10 | La Aurora Airport |  | GT | 965 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 768 |
| 17 | Kuala Lumpur International Airport |  | MY | 757 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 705 |
| 20 | Salt Lake City International Airport |  | US | 704 |
| 21 | Malpensa International Airport |  | IT | 703 |
| 22 | Bengaluru International Airport |  | IN | 696 |
| 23 | Capua Airport |  | IT | 684 |
| 24 | Charlotte/Douglas International Airport |  | US | 656 |
| 25 | Congonhas Airport |  | BR | 656 |
| 26 | Charles de Gaulle International Airport |  | FR | 655 |
| 27 | Daniel K Inouye International Airport |  | US | 611 |
| 28 | Tenerife Norte Airport |  | ES | 606 |
| 29 | Ninoy Aquino International Airport |  | PH | 604 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 590 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 563 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 561 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 532 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 530 |
| 37 | Don Mueang International Airport |  | TH | 527 |
| 38 | Amsterdam Airport Schiphol |  | NL | 522 |
| 39 | O. R. Tambo International Airport |  | ZA | 496 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 309 | 21m | 244 km | 1,301.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 274 | 1h 8m | 706 km | 3,336.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 217 | 14m | 114 km | 425.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 198 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 191 | 1h 11m | 770 km | 2,537.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 176 | 26m | 275 km | 834.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 130 | 31m | 369 km | 827.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 120 | 14m | 154 km | 318.0 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 111 | 57m | 493 km | 944.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-05-15 18:58 UTC | 2026-05-16 06:51 UTC | 11h 53m |
| DRAG38 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-05-16 06:39 UTC | 2026-05-16 06:49 UTC | 10m |
| JA24HB |  | Yokota Air Base (RJTY) | Yokota Air Base (RJTY) | 2026-05-16 06:30 UTC | 2026-05-16 06:46 UTC | 16m |
| CFG2CK | CFG | Berlin Brandenburg Airport (EDDB) | Frankfurt am Main International Airport (EDDF) | 2026-05-16 05:51 UTC | 2026-05-16 06:34 UTC | 42m |
| UAL20 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | Amsterdam Airport Schiphol (EHAM) | 2026-05-15 21:29 UTC | 2026-05-16 06:33 UTC | 9h 3m |
| SHAHD272 | SHA | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-05-16 06:03 UTC | 2026-05-16 06:22 UTC | 19m |
| MAC9900 | MAC | Vilnius International Airport (EYVI) | Alytus Airport (EYAL) | 2026-05-16 06:11 UTC | 2026-05-16 06:22 UTC | 10m |
| UAL1558 | United Airlines | Newark Liberty International Airport (KEWR) | San Francisco International Airport (KSFO) | 2026-05-16 00:38 UTC | 2026-05-16 06:20 UTC | 5h 42m |
| ESR626 | ESR | New Chitose Airport (RJCC) | Incheon International Airport (RKSI) | 2026-05-16 04:04 UTC | 2026-05-16 06:18 UTC | 2h 14m |
| OXK | OXK | Colac Airport (YOLA) | Melbourne Essendon Airport (YMEN) | 2026-05-16 05:35 UTC | 2026-05-16 06:12 UTC | 37m |
| 5BCMF |  | Larnaca International Airport (LCLK) | Larnaca International Airport (LCLK) | 2026-05-16 06:10 UTC | 2026-05-16 06:10 UTC | 0m |
| AEE2HO | AEE | Eleftherios Venizelos International Airport (LGAV) | Diagoras Airport (LGRP) | 2026-05-16 05:24 UTC | 2026-05-16 06:05 UTC | 41m |
| LOT9MA | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Szczecin-Goleniow Solidarność Airport (EPSC) | 2026-05-16 05:17 UTC | 2026-05-16 06:02 UTC | 45m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-16 05:35 UTC | 2026-05-16 06:01 UTC | 25m |
| 5BCMO |  | Larnaca International Airport (LCLK) | Queen Alia International Airport (OJAI) | 2026-05-16 05:39 UTC | 2026-05-16 05:58 UTC | 19m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-05-16 05:20 UTC | 2026-05-16 05:56 UTC | 35m |
| AUA877J | Austrian Airlines | Vienna International Airport (LOWW) | Skiathos Island National Airport (LGSK) | 2026-05-16 04:25 UTC | 2026-05-16 05:55 UTC | 1h 30m |
| VLG10ZA | Vueling | Barcelona International Airport (LEBL) | Ibiza Airport (LEIB) | 2026-05-16 05:20 UTC | 2026-05-16 05:55 UTC | 35m |
| EJU703L | EJU | Charles de Gaulle International Airport (LFPG) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-16 04:49 UTC | 2026-05-16 05:55 UTC | 1h 6m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-16 04:56 UTC | 2026-05-16 05:55 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
