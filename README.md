# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_13:09:59_UTC-green)

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

**Latest saved flight:** 2026-05-12 13:09:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 13:09:59 UTC

- **78,845** saved flights
- **28,702** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,845** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **976,449.5 tonnes** estimated CO2 emissions
- **56,605,769 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3406 |
| 2 | SkyWest Airlines | 2924 |
| 3 | IndiGo | 1753 |
| 4 | EJA | 1450 |
| 5 | American Airlines | 1226 |
| 6 | Southwest Airlines | 1155 |
| 7 | Lufthansa | 1043 |
| 8 | ENY | 980 |
| 9 | Delta Air Lines | 858 |
| 10 | Vueling | 760 |
| 11 | AXM | 728 |
| 12 | LATAM Airlines | 716 |
| 13 | WIF | 681 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 622 |
| 16 | Swiss International | 610 |
| 17 | QLK | 592 |
| 18 | LXJ | 571 |
| 19 | Alaska Airlines | 553 |
| 20 | easyJet | 528 |
| 21 | EJU | 513 |
| 22 | AEE | 512 |
| 23 | Cathay Pacific | 503 |
| 24 | Air France | 467 |
| 25 | VIV | 467 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 437 |
| 28 | CXK | 405 |
| 29 | AIQ | 397 |
| 30 | MXY | 395 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63678 |
| 2 | 🇪🇸 ES | 5658 |
| 3 | 🇮🇳 IN | 5490 |
| 4 | 🇦🇺 AU | 5087 |
| 5 | 🇩🇪 DE | 4488 |
| 6 | 🇮🇹 IT | 4394 |
| 7 | 🇧🇷 BR | 4356 |
| 8 | 🇯🇵 JP | 4072 |
| 9 | 🇨🇦 CA | 3903 |
| 10 | 🇬🇧 GB | 3397 |
| 11 | 🇫🇷 FR | 3143 |
| 12 | 🇨🇴 CO | 2703 |
| 13 | 🇲🇽 MX | 2388 |
| 14 | 🇬🇷 GR | 2328 |
| 15 | 🇳🇴 NO | 2175 |
| 16 | 🇨🇭 CH | 2134 |
| 17 | 🇲🇾 MY | 1827 |
| 18 | 🇿🇦 ZA | 1502 |
| 19 | 🇹🇷 TR | 1428 |
| 20 | 🇹🇭 TH | 1408 |
| 21 | 🇳🇿 NZ | 1402 |
| 22 | 🇵🇱 PL | 1320 |
| 23 | 🇵🇭 PH | 1258 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 929 |
| 27 | 🇲🇴 MO | 922 |
| 28 | 🇲🇪 ME | 850 |
| 29 | 🇳🇱 NL | 822 |
| 30 | 🇭🇷 HR | 688 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1731 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1316 |
| 4 | Indira Gandhi International Airport |  | IN | 1159 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1142 |
| 6 | Frankfurt am Main International Airport |  | DE | 1046 |
| 7 | Harry Reid International Airport |  | US | 979 |
| 8 | Zurich Airport |  | CH | 937 |
| 9 | Macau International Airport |  | MO | 922 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 895 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 872 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 797 |
| 15 | Chicago O'Hare International Airport |  | US | 766 |
| 16 | Madrid Barajas International Airport |  | ES | 731 |
| 17 | Kuala Lumpur International Airport |  | MY | 729 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 696 |
| 19 | Malpensa International Airport |  | IT | 682 |
| 20 | Bengaluru International Airport |  | IN | 677 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 22 | Salt Lake City International Airport |  | US | 644 |
| 23 | Capua Airport |  | IT | 641 |
| 24 | Charlotte/Douglas International Airport |  | US | 621 |
| 25 | Charles de Gaulle International Airport |  | FR | 620 |
| 26 | Congonhas Airport |  | BR | 615 |
| 27 | Tenerife Norte Airport |  | ES | 588 |
| 28 | Ninoy Aquino International Airport |  | PH | 573 |
| 29 | Daniel K Inouye International Airport |  | US | 572 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 566 |
| 31 | Barcelona International Airport |  | ES | 533 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 531 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 518 |
| 35 | Don Mueang International Airport |  | TH | 504 |
| 36 | Vitoria/Foronda Airport |  | ES | 502 |
| 37 | Amsterdam Airport Schiphol |  | NL | 496 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 487 |
| 39 | O. R. Tambo International Airport |  | ZA | 474 |
| 40 | Calgary International Airport |  | CA | 465 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 372 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 284 | 21m | 244 km | 1,195.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 116 | 20m | 147 km | 293.5 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 105 | 57m | 493 km | 893.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 104 | 23m | 55 km | 98.8 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 100 | 18m | 144 km | 248.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 99 | 12m | - | - |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EPI927 | EPI | North Texas Regional/Perrin Field (KGYI) | Ardmore Downtown Executive Airport (K1F0) | 2026-05-12 12:46 UTC | 2026-05-12 13:09 UTC | 23m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-12 12:52 UTC | 2026-05-12 13:06 UTC | 14m |
| LTA948 | LTA | Indianapolis International Airport (KIND) | K4I7 (K4I7) | 2026-05-12 12:13 UTC | 2026-05-12 13:04 UTC | 51m |
| BAF70 | BAF | Brussels Airport (EBBR) | Tekirdag Corlu Airport (LTBU) | 2026-05-12 10:34 UTC | 2026-05-12 13:04 UTC | 2h 29m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-12 11:44 UTC | 2026-05-12 12:52 UTC | 1h 7m |
| T333 |  | St Stephan Airport (LSTS) | Reichenbach Air Base (LSGR) | 2026-05-12 11:30 UTC | 2026-05-12 12:44 UTC | 1h 13m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-05-12 12:25 UTC | 2026-05-12 12:38 UTC | 12m |
| UAE8UW | Emirates | John F Kennedy International Airport (KJFK) | Queen Alia International Airport (OJAI) | 2026-05-12 03:25 UTC | 2026-05-12 12:38 UTC | 9h 12m |
| ETD9SM | Etihad Airways | Fly Sky Airport (36NC) | Queen Alia International Airport (OJAI) | 2026-05-12 02:44 UTC | 2026-05-12 12:37 UTC | 9h 52m |
| QTR22B | Qatar Airways | 0OH7 (0OH7) | Queen Alia International Airport (OJAI) | 2026-05-12 02:44 UTC | 2026-05-12 12:36 UTC | 9h 52m |
| N6642J |  | Northern Colorado Regional Airport (KFNL) | Erie Municipal Airport (KEIK) | 2026-05-12 11:58 UTC | 2026-05-12 12:36 UTC | 37m |
| N708LA |  | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-05-12 12:15 UTC | 2026-05-12 12:34 UTC | 19m |
| N365PC |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-12 12:18 UTC | 2026-05-12 12:33 UTC | 15m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-05-12 12:10 UTC | 2026-05-12 12:24 UTC | 14m |
| CXK426 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-12 11:52 UTC | 2026-05-12 12:24 UTC | 31m |
| RYR8XK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Crotone Airport (LIBC) | 2026-05-12 11:25 UTC | 2026-05-12 12:23 UTC | 57m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-05-11 21:41 UTC | 2026-05-12 12:22 UTC | 14h 41m |
| SAS53C | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Copenhagen Kastrup Airport (EKCH) | 2026-05-12 11:25 UTC | 2026-05-12 12:21 UTC | 55m |
| SEH3TK | SEH | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-05-12 11:55 UTC | 2026-05-12 12:20 UTC | 25m |
| HBHHH | HBH | Buochs Airport (LSZC) | Wangen-Lachen Airport (LSPV) | 2026-05-12 12:04 UTC | 2026-05-12 12:19 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
