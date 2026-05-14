# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_15:13:40_UTC-green)

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

**Latest saved flight:** 2026-05-14 15:13:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 15:13:40 UTC

- **81,743** saved flights
- **29,615** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,743** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,006,656.3 tonnes** estimated CO2 emissions
- **58,356,889 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3506 |
| 2 | SkyWest Airlines | 3022 |
| 3 | IndiGo | 1797 |
| 4 | EJA | 1529 |
| 5 | American Airlines | 1262 |
| 6 | Southwest Airlines | 1191 |
| 7 | Lufthansa | 1060 |
| 8 | ENY | 1021 |
| 9 | Delta Air Lines | 896 |
| 10 | Vueling | 776 |
| 11 | AXM | 746 |
| 12 | LATAM Airlines | 742 |
| 13 | WIF | 710 |
| 14 | All Nippon Airways | 646 |
| 15 | AZU | 642 |
| 16 | Swiss International | 639 |
| 17 | QLK | 608 |
| 18 | LXJ | 593 |
| 19 | Alaska Airlines | 578 |
| 20 | easyJet | 543 |
| 21 | EJU | 528 |
| 22 | AEE | 521 |
| 23 | Cathay Pacific | 510 |
| 24 | Air France | 483 |
| 25 | VIV | 483 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 441 |
| 28 | CXK | 425 |
| 29 | AIQ | 407 |
| 30 | United Airlines | 405 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66543 |
| 2 | 🇪🇸 ES | 5809 |
| 3 | 🇮🇳 IN | 5613 |
| 4 | 🇦🇺 AU | 5262 |
| 5 | 🇩🇪 DE | 4593 |
| 6 | 🇮🇹 IT | 4523 |
| 7 | 🇧🇷 BR | 4510 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4062 |
| 10 | 🇬🇧 GB | 3498 |
| 11 | 🇫🇷 FR | 3262 |
| 12 | 🇨🇴 CO | 2722 |
| 13 | 🇲🇽 MX | 2458 |
| 14 | 🇬🇷 GR | 2385 |
| 15 | 🇳🇴 NO | 2292 |
| 16 | 🇨🇭 CH | 2197 |
| 17 | 🇲🇾 MY | 1873 |
| 18 | 🇿🇦 ZA | 1548 |
| 19 | 🇹🇷 TR | 1453 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1436 |
| 22 | 🇵🇱 PL | 1364 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇰🇷 KR | 1252 |
| 25 | 🇬🇹 GT | 1248 |
| 26 | 🇲🇦 MA | 956 |
| 27 | 🇲🇴 MO | 938 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 845 |
| 30 | 🇭🇷 HR | 729 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1788 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1370 |
| 4 | Indira Gandhi International Airport |  | IN | 1192 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1167 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1016 |
| 8 | Zurich Airport |  | CH | 977 |
| 9 | La Aurora Airport |  | GT | 943 |
| 10 | Macau International Airport |  | MO | 938 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 920 |
| 12 | Guaymaral Airport |  | CO | 914 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 791 |
| 16 | Madrid Barajas International Airport |  | ES | 751 |
| 17 | Kuala Lumpur International Airport |  | MY | 747 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 714 |
| 19 | Malpensa International Airport |  | IT | 692 |
| 20 | Bengaluru International Airport |  | IN | 690 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 22 | Salt Lake City International Airport |  | US | 673 |
| 23 | Capua Airport |  | IT | 668 |
| 24 | Charles de Gaulle International Airport |  | FR | 643 |
| 25 | Charlotte/Douglas International Airport |  | US | 638 |
| 26 | Congonhas Airport |  | BR | 636 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Ninoy Aquino International Airport |  | PH | 596 |
| 29 | Daniel K Inouye International Airport |  | US | 592 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 550 |
| 32 | Barcelona International Airport |  | ES | 548 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 542 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 530 |
| 35 | Don Mueang International Airport |  | TH | 517 |
| 36 | Vitoria/Foronda Airport |  | ES | 514 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 512 |
| 38 | Amsterdam Airport Schiphol |  | NL | 509 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 481 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 295 | 21m | 244 km | 1,242.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 209 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 171 | 26m | 275 km | 810.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 121 | 27m | 215 km | 448.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 121 | 27m | 152 km | 316.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 120 | 20m | 147 km | 303.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 111 | 23m | 55 km | 105.5 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 102 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5470K |  | Orlando Sanford International Airport (KSFB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-05-14 14:41 UTC | 2026-05-14 15:13 UTC | 31m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-05-14 14:39 UTC | 2026-05-14 15:07 UTC | 27m |
| N39688 |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-05-14 14:22 UTC | 2026-05-14 15:06 UTC | 43m |
| BOMR734 | BOM | Waldron Field Nolf Airport (KNWL) | XS10 (XS10) | 2026-05-14 14:32 UTC | 2026-05-14 15:04 UTC | 31m |
| BB229 |  | South Alabama Regional At Bill Benton Field (K79J) | Marianna Municipal Airport (KMAI) | 2026-05-14 14:24 UTC | 2026-05-14 15:02 UTC | 38m |
| IFG623 | IFG | Treasure Coast International Airport (KFPR) | Treasure Coast International Airport (KFPR) | 2026-05-14 14:42 UTC | 2026-05-14 15:02 UTC | 19m |
| N215U |  | Page Field (KFMY) | La Belle Municipal Airport (KX14) | 2026-05-14 14:24 UTC | 2026-05-14 15:00 UTC | 35m |
| N85HA |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Akron-Canton Regional Airport (KCAK) | 2026-05-14 14:09 UTC | 2026-05-14 15:00 UTC | 50m |
| N739ZW |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-05-14 14:13 UTC | 2026-05-14 14:58 UTC | 44m |
| N67265 |  | Wheeler-Sack Army Air Field (KGTB) | Wheeler-Sack Army Air Field (KGTB) | 2026-05-14 13:30 UTC | 2026-05-14 14:57 UTC | 1h 26m |
| CHH754 | CHH | Manchester Airport (EGCC) | Ukhta Airport (UUYH) | 2026-05-14 11:17 UTC | 2026-05-14 14:55 UTC | 3h 38m |
| N932EC |  | Melanie's Airport (05FA) | Dothan Regional Airport (KDHN) | 2026-05-14 14:30 UTC | 2026-05-14 14:53 UTC | 22m |
| DRAG154 | DRA | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Asiago Airport (LIDA) | 2026-05-14 14:11 UTC | 2026-05-14 14:52 UTC | 41m |
| NORST4 | NOR | Bagwell Airport (NC99) | Bagwell Airport (NC99) | 2026-05-14 14:22 UTC | 2026-05-14 14:51 UTC | 29m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-14 14:40 UTC | 2026-05-14 14:51 UTC | 11m |
| 00000000 |  | Dothan Regional Airport (KDHN) | Chilton County Airport (K02A) | 2026-05-14 14:28 UTC | 2026-05-14 14:49 UTC | 20m |
| N313JM |  | Centennial Airport (KAPA) | 28IS (28IS) | 2026-05-14 12:21 UTC | 2026-05-14 14:44 UTC | 2h 23m |
| CXK508 | CXK | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-14 14:28 UTC | 2026-05-14 14:43 UTC | 14m |
| ARCAT55 | ARC | Gillespie Field (KSEE) | Apple Valley Airport (KAPV) | 2026-05-14 14:17 UTC | 2026-05-14 14:42 UTC | 24m |
| N481LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-14 13:50 UTC | 2026-05-14 14:41 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
