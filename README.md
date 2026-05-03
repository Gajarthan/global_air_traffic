# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_22:40:56_UTC-green)

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

**Latest saved flight:** 2026-05-03 22:40:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 22:40:56 UTC

- **66,912** saved flights
- **25,260** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,912** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **821,412.5 tonnes** estimated CO2 emissions
- **47,618,117 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2857 |
| 2 | SkyWest Airlines | 2482 |
| 3 | IndiGo | 1546 |
| 4 | EJA | 1197 |
| 5 | American Airlines | 1036 |
| 6 | Southwest Airlines | 942 |
| 7 | Lufthansa | 857 |
| 8 | ENY | 823 |
| 9 | Vueling | 661 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 622 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 560 |
| 14 | WIF | 559 |
| 15 | AZU | 541 |
| 16 | Swiss International | 514 |
| 17 | QLK | 513 |
| 18 | LXJ | 487 |
| 19 | Alaska Airlines | 453 |
| 20 | easyJet | 444 |
| 21 | AEE | 436 |
| 22 | EJU | 432 |
| 23 | VIV | 417 |
| 24 | Cathay Pacific | 402 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 376 |
| 28 | CXK | 342 |
| 29 | AIQ | 339 |
| 30 | MXY | 326 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52990 |
| 2 | 🇪🇸 ES | 4909 |
| 3 | 🇮🇳 IN | 4858 |
| 4 | 🇦🇺 AU | 4415 |
| 5 | 🇧🇷 BR | 3758 |
| 6 | 🇩🇪 DE | 3742 |
| 7 | 🇮🇹 IT | 3656 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3279 |
| 10 | 🇬🇧 GB | 2892 |
| 11 | 🇫🇷 FR | 2652 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2127 |
| 14 | 🇬🇷 GR | 2000 |
| 15 | 🇨🇭 CH | 1869 |
| 16 | 🇳🇴 NO | 1816 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1240 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1205 |
| 22 | 🇵🇭 PH | 1110 |
| 23 | 🇵🇱 PL | 1099 |
| 24 | 🇬🇹 GT | 1081 |
| 25 | 🇰🇷 KR | 1076 |
| 26 | 🇲🇦 MA | 821 |
| 27 | 🇲🇴 MO | 752 |
| 28 | 🇲🇪 ME | 724 |
| 29 | 🇳🇱 NL | 708 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1475 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1105 |
| 4 | Indira Gandhi International Airport |  | IN | 1014 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 974 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 863 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 833 |
| 10 | La Aurora Airport |  | GT | 803 |
| 11 | Zurich Airport |  | CH | 793 |
| 12 | Macau International Airport |  | MO | 752 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 658 |
| 14 | Chicago O'Hare International Airport |  | US | 640 |
| 15 | Madrid Barajas International Airport |  | ES | 640 |
| 16 | Kuala Lumpur International Airport |  | MY | 639 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 599 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 581 |
| 20 | Malpensa International Airport |  | IT | 577 |
| 21 | Congonhas Airport |  | BR | 539 |
| 22 | Tenerife Norte Airport |  | ES | 533 |
| 23 | Salt Lake City International Airport |  | US | 532 |
| 24 | Charlotte/Douglas International Airport |  | US | 528 |
| 25 | Charles de Gaulle International Airport |  | FR | 524 |
| 26 | Ninoy Aquino International Airport |  | PH | 505 |
| 27 | Capua Airport |  | IT | 505 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 487 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 471 |
| 31 | Barcelona International Airport |  | ES | 459 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 450 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 444 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 420 |
| 38 | Amsterdam Airport Schiphol |  | NL | 416 |
| 39 | Reno/Tahoe International Airport |  | US | 404 |
| 40 | Calgary International Airport |  | CA | 390 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 227 | 21m | 244 km | 955.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 167 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 127 | 21m | 99 km | 217.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 111 | 31m | 369 km | 706.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 111 | 27m | 152 km | 290.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 96 | 1h 41m | 1,156 km | 1,915.2 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N605WM |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-05-03 21:52 UTC | 2026-05-03 22:40 UTC | 48m |
| UAE9796 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-05-03 16:13 UTC | 2026-05-03 22:34 UTC | 6h 21m |
| N5339L |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-03 21:40 UTC | 2026-05-03 22:33 UTC | 52m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-05-03 10:46 UTC | 2026-05-03 22:32 UTC | 11h 45m |
| JRT20 | JRT | Ellington Airport (KEFD) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-05-03 21:44 UTC | 2026-05-03 22:26 UTC | 41m |
| N626AA |  | Addington Field (4TX8) | Richards Airport (TA47) | 2026-05-03 21:56 UTC | 2026-05-03 22:23 UTC | 27m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-05-03 20:46 UTC | 2026-05-03 22:23 UTC | 1h 36m |
| KAP111 | KAP | General Edward Lawrence Logan International Airport (KBOS) | Martha's Vineyard Airport (KMVY) | 2026-05-03 22:00 UTC | 2026-05-03 22:22 UTC | 22m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-03 15:20 UTC | 2026-05-03 22:16 UTC | 6h 56m |
| N321RJ |  | Warrenton/Fauquier Airport (KHWY) | Warrenton/Fauquier Airport (KHWY) | 2026-05-03 22:12 UTC | 2026-05-03 22:16 UTC | 4m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 22:04 UTC | 2026-05-03 22:16 UTC | 12m |
| ZKFPO | ZKF | Turangi Airport (NZTN) | Waiouru Airport (NZRU) | 2026-05-03 22:01 UTC | 2026-05-03 22:12 UTC | 10m |
| N554CN |  | Meadows Field (KBFL) | Mc Alester Regional Airport (KMLC) | 2026-05-03 19:41 UTC | 2026-05-03 22:10 UTC | 2h 29m |
| N797BK |  | Shreveport Regional Airport (KSHV) | Telluride Regional Airport (KTEX) | 2026-05-03 19:38 UTC | 2026-05-03 22:10 UTC | 2h 31m |
| CXK192 | CXK | Mckinney Ntl Airport (KTKI) | 0TX9 (0TX9) | 2026-05-03 21:45 UTC | 2026-05-03 22:07 UTC | 21m |
| N911LK |  | Miami Homestead General Aviation Airport (KX51) | Miami Executive Airport (KTMB) | 2026-05-03 21:53 UTC | 2026-05-03 22:06 UTC | 13m |
| ASP877 | ASP | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-05-03 22:05 UTC | 2026-05-03 22:05 UTC | 0m |
| N472QS |  | Tampa International Airport (KTPA) | Auxiliary Airfield (MYGM) | 2026-05-03 21:28 UTC | 2026-05-03 22:04 UTC | 35m |
| N774EB |  | Auburn Municipal Airport (KS50) | Umpqua Rv Park Fly In Airport (94OR) | 2026-05-03 20:35 UTC | 2026-05-03 22:03 UTC | 1h 28m |
| CFRT90 | CFR | Porterville Municipal Airport (KPTV) | Kern Valley Airport (KL05) | 2026-05-03 21:55 UTC | 2026-05-03 22:03 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
