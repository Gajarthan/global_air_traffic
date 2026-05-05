# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_20:00:52_UTC-green)

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

**Latest saved flight:** 2026-05-05 20:00:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 20:00:52 UTC

- **69,610** saved flights
- **26,017** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,610** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **855,762.8 tonnes** estimated CO2 emissions
- **49,609,440 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2992 |
| 2 | SkyWest Airlines | 2591 |
| 3 | IndiGo | 1598 |
| 4 | EJA | 1260 |
| 5 | American Airlines | 1087 |
| 6 | Southwest Airlines | 996 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 860 |
| 9 | Vueling | 685 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 645 |
| 12 | WIF | 596 |
| 13 | All Nippon Airways | 585 |
| 14 | Delta Air Lines | 585 |
| 15 | AZU | 565 |
| 16 | Swiss International | 538 |
| 17 | QLK | 534 |
| 18 | LXJ | 504 |
| 19 | Alaska Airlines | 479 |
| 20 | easyJet | 467 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 433 |
| 24 | Cathay Pacific | 418 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 339 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55228 |
| 2 | 🇪🇸 ES | 5088 |
| 3 | 🇮🇳 IN | 5025 |
| 4 | 🇦🇺 AU | 4599 |
| 5 | 🇧🇷 BR | 3907 |
| 6 | 🇩🇪 DE | 3894 |
| 7 | 🇮🇹 IT | 3821 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3440 |
| 10 | 🇬🇧 GB | 3030 |
| 11 | 🇫🇷 FR | 2765 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2203 |
| 14 | 🇬🇷 GR | 2083 |
| 15 | 🇨🇭 CH | 1921 |
| 16 | 🇳🇴 NO | 1912 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1255 |
| 22 | 🇵🇭 PH | 1158 |
| 23 | 🇵🇱 PL | 1148 |
| 24 | 🇬🇹 GT | 1121 |
| 25 | 🇰🇷 KR | 1110 |
| 26 | 🇲🇦 MA | 840 |
| 27 | 🇲🇴 MO | 788 |
| 28 | 🇲🇪 ME | 752 |
| 29 | 🇳🇱 NL | 727 |
| 30 | 🇮🇩 ID | 587 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1544 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1143 |
| 4 | Indira Gandhi International Airport |  | IN | 1053 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1019 |
| 6 | Frankfurt am Main International Airport |  | DE | 894 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 867 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 833 |
| 11 | Zurich Airport |  | CH | 825 |
| 12 | Macau International Airport |  | MO | 788 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 694 |
| 14 | Kuala Lumpur International Airport |  | MY | 668 |
| 15 | Chicago O'Hare International Airport |  | US | 667 |
| 16 | Madrid Barajas International Airport |  | ES | 665 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 620 |
| 18 | Malpensa International Airport |  | IT | 607 |
| 19 | Bengaluru International Airport |  | IN | 605 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Salt Lake City International Airport |  | US | 563 |
| 22 | Congonhas Airport |  | BR | 556 |
| 23 | Charlotte/Douglas International Airport |  | US | 548 |
| 24 | Charles de Gaulle International Airport |  | FR | 548 |
| 25 | Tenerife Norte Airport |  | ES | 543 |
| 26 | Capua Airport |  | IT | 543 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 509 |
| 29 | Daniel K Inouye International Airport |  | US | 506 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 489 |
| 31 | Barcelona International Airport |  | ES | 483 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 473 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 438 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 434 |
| 38 | Amsterdam Airport Schiphol |  | NL | 429 |
| 39 | Reno/Tahoe International Airport |  | US | 413 |
| 40 | Calgary International Airport |  | CA | 413 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 238 | 21m | 244 km | 1,002.2 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 172 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| G26023 |  | Leaders Clear Lake Airport (K8Y6) | Maple Lake Municipal-Bill Mavencamp Sr Field (KMGG) | 2026-05-05 19:49 UTC | 2026-05-05 20:00 UTC | 11m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-05-05 19:39 UTC | 2026-05-05 19:46 UTC | 7m |
| N447KK |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-05-05 18:47 UTC | 2026-05-05 19:43 UTC | 56m |
| GJADN | GJA | Oxford (Kidlington) Airport (EGTK) | Guernsey Airport (EGJB) | 2026-05-05 18:59 UTC | 2026-05-05 19:40 UTC | 40m |
| N874BU |  | Pilot Country Airport (KX05) | Peter O Knight Airport (KTPF) | 2026-05-05 19:20 UTC | 2026-05-05 19:39 UTC | 18m |
| CPA875 | Cathay Pacific | Dallas-Fort Worth International Airport (KDFW) | Macau International Airport (VMMC) | 2026-05-05 04:19 UTC | 2026-05-05 19:36 UTC | 15h 16m |
| BOE443 | BOE | Renton Municipal Airport (KRNT) | 8WA5 (8WA5) | 2026-05-05 17:44 UTC | 2026-05-05 19:34 UTC | 1h 49m |
|  |  | Winston Field (KSNK) | Roy Ranch Airport (TS21) | 2026-05-05 18:56 UTC | 2026-05-05 19:31 UTC | 35m |
| THNDR12 | THN | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-05-05 19:08 UTC | 2026-05-05 19:30 UTC | 22m |
| SUMIT72 | SUM | Pueblo Memorial Airport (KPUB) | Pueblo Memorial Airport (KPUB) | 2026-05-05 18:51 UTC | 2026-05-05 19:29 UTC | 38m |
| N218SH |  | Crazy Horse Airport (12WV) | West Virginia International Yeager Airport (KCRW) | 2026-05-05 19:15 UTC | 2026-05-05 19:26 UTC | 11m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 19:13 UTC | 2026-05-05 19:26 UTC | 12m |
| TGCYO | TGC | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-05-05 18:53 UTC | 2026-05-05 19:25 UTC | 32m |
| SNAKE81 | SNA | French Valley Airport (KF70) | Borrego Valley Airport (KL08) | 2026-05-05 19:00 UTC | 2026-05-05 19:17 UTC | 17m |
| EJA950 | EJA | Piedmont Triad International Airport (KGSO) | Norfolk International Airport (KORF) | 2026-05-05 18:40 UTC | 2026-05-05 19:16 UTC | 36m |
|  |  | 89LL (89LL) | 89LL (89LL) | 2026-05-05 19:14 UTC | 2026-05-05 19:16 UTC | 1m |
| AAL446R | American Airlines | Chicago O'Hare International Airport (KORD) | Sacramento International Airport (KSMF) | 2026-05-05 15:01 UTC | 2026-05-05 19:15 UTC | 4h 14m |
| KELSY05 | KEL | Tinker Afb Airport (KTIK) | Coleman Municipal Airport (KCOM) | 2026-05-05 16:23 UTC | 2026-05-05 19:15 UTC | 2h 52m |
| EJA680 | EJA | Salt Lake City International Airport (KSLC) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-05 16:28 UTC | 2026-05-05 19:14 UTC | 2h 45m |
| N500BS |  | Downtown Airport (K3DW) | Rogers Executive - Carter Field (KROG) | 2026-05-05 18:27 UTC | 2026-05-05 19:13 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
