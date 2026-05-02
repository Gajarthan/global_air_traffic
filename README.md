# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_22:47:07_UTC-green)

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

**Latest saved flight:** 2026-05-02 22:47:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 22:47:07 UTC

- **65,084** saved flights
- **24,731** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,084** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **797,490.8 tonnes** estimated CO2 emissions
- **46,231,352 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2763 |
| 2 | SkyWest Airlines | 2416 |
| 3 | IndiGo | 1495 |
| 4 | EJA | 1157 |
| 5 | American Airlines | 1008 |
| 6 | Southwest Airlines | 916 |
| 7 | Lufthansa | 834 |
| 8 | ENY | 800 |
| 9 | Vueling | 640 |
| 10 | AXM | 631 |
| 11 | LATAM Airlines | 607 |
| 12 | All Nippon Airways | 566 |
| 13 | Delta Air Lines | 542 |
| 14 | WIF | 539 |
| 15 | AZU | 526 |
| 16 | QLK | 502 |
| 17 | Swiss International | 499 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 445 |
| 20 | easyJet | 425 |
| 21 | AEE | 420 |
| 22 | EJU | 416 |
| 23 | VIV | 407 |
| 24 | Cathay Pacific | 391 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 377 |
| 27 | AXB | 363 |
| 28 | CXK | 331 |
| 29 | AIQ | 330 |
| 30 | GLO | 317 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51597 |
| 2 | 🇪🇸 ES | 4756 |
| 3 | 🇮🇳 IN | 4707 |
| 4 | 🇦🇺 AU | 4347 |
| 5 | 🇧🇷 BR | 3669 |
| 6 | 🇩🇪 DE | 3637 |
| 7 | 🇮🇹 IT | 3529 |
| 8 | 🇯🇵 JP | 3527 |
| 9 | 🇨🇦 CA | 3187 |
| 10 | 🇬🇧 GB | 2796 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2571 |
| 13 | 🇲🇽 MX | 2067 |
| 14 | 🇬🇷 GR | 1943 |
| 15 | 🇨🇭 CH | 1820 |
| 16 | 🇳🇴 NO | 1766 |
| 17 | 🇲🇾 MY | 1546 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1211 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1165 |
| 22 | 🇵🇭 PH | 1091 |
| 23 | 🇵🇱 PL | 1061 |
| 24 | 🇰🇷 KR | 1056 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 800 |
| 27 | 🇲🇴 MO | 733 |
| 28 | 🇲🇪 ME | 701 |
| 29 | 🇳🇱 NL | 686 |
| 30 | 🇮🇩 ID | 545 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1431 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1077 |
| 4 | Indira Gandhi International Airport |  | IN | 988 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 945 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 834 |
| 9 | Harry Reid International Airport |  | US | 817 |
| 10 | Zurich Airport |  | CH | 769 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 733 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 638 |
| 14 | Madrid Barajas International Airport |  | ES | 619 |
| 15 | Chicago O'Hare International Airport |  | US | 618 |
| 16 | Kuala Lumpur International Airport |  | MY | 614 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 584 |
| 18 | Bengaluru International Airport |  | IN | 570 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 560 |
| 21 | Congonhas Airport |  | BR | 528 |
| 22 | Tenerife Norte Airport |  | ES | 518 |
| 23 | Charlotte/Douglas International Airport |  | US | 515 |
| 24 | Salt Lake City International Airport |  | US | 513 |
| 25 | Charles de Gaulle International Airport |  | FR | 505 |
| 26 | Ninoy Aquino International Airport |  | PH | 496 |
| 27 | Capua Airport |  | IT | 480 |
| 28 | Daniel K Inouye International Airport |  | US | 479 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 474 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 464 |
| 31 | Barcelona International Airport |  | ES | 442 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 433 |
| 33 | Vitoria/Foronda Airport |  | ES | 432 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 430 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 38 | Amsterdam Airport Schiphol |  | NL | 403 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 221 | 21m | 244 km | 930.6 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 148 | 26m | 275 km | 701.3 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N325HL |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-05-02 22:16 UTC | 2026-05-02 22:47 UTC | 30m |
| SAVER70 | SAV | Bomoen Airport (ENBM) | Bergen Airport Flesland (ENBR) | 2026-05-02 22:29 UTC | 2026-05-02 22:45 UTC | 15m |
| N222CF |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bermuda Dunes Airport (KUDD) | 2026-05-02 21:59 UTC | 2026-05-02 22:41 UTC | 41m |
| N7194G |  | Pfeffer & Son Farms Airport (4XS0) | 8TX7 (8TX7) | 2026-05-02 22:16 UTC | 2026-05-02 22:37 UTC | 20m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-02 21:32 UTC | 2026-05-02 22:35 UTC | 1h 3m |
| HMF006 | HMF | Kristianstad Airport (ESMK) | Ronneby Airport (ESDF) | 2026-05-02 22:12 UTC | 2026-05-02 22:34 UTC | 21m |
| VAR409 | VAR | Phoenix Goodyear Airport (KGYR) | Sun Valley Airport (KA20) | 2026-05-02 21:11 UTC | 2026-05-02 22:31 UTC | 1h 20m |
| N386NG |  | Mc Clellan-Palomar Airport (KCRQ) | Santa Ynez/Kunkle Field (KIZA) | 2026-05-02 21:45 UTC | 2026-05-02 22:30 UTC | 45m |
| QFA38 | Qantas | Plumbago Airport (YPMB) | Melbourne International Airport (YMML) | 2026-05-02 21:25 UTC | 2026-05-02 22:28 UTC | 1h 2m |
| N922AZ |  | Rimrock Airport (48AZ) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-02 21:55 UTC | 2026-05-02 22:25 UTC | 30m |
| N4593Y |  | Boulder Municipal Airport (KBDU) | Boulder Municipal Airport (KBDU) | 2026-05-02 22:15 UTC | 2026-05-02 22:24 UTC | 8m |
| N952JH |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-05-02 21:06 UTC | 2026-05-02 22:23 UTC | 1h 17m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-05-02 22:17 UTC | 2026-05-02 22:22 UTC | 4m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-02 21:40 UTC | 2026-05-02 22:15 UTC | 35m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-02 22:01 UTC | 2026-05-02 22:15 UTC | 14m |
| N2226N |  | KU77 (KU77) | KU77 (KU77) | 2026-05-02 21:59 UTC | 2026-05-02 22:14 UTC | 15m |
| TRP2 | TRP | Joint Base Andrews Airport (KADW) | Lee Airport (KANP) | 2026-05-02 22:04 UTC | 2026-05-02 22:14 UTC | 10m |
| N918PT |  | Nashville International Airport (KBNA) | Mc Lean/Gray County Airport (K2E7) | 2026-05-02 20:28 UTC | 2026-05-02 22:14 UTC | 1h 45m |
| N1490X |  | KU42 (KU42) | Logan-Cache Airport (KLGU) | 2026-05-02 21:21 UTC | 2026-05-02 22:10 UTC | 49m |
| N2539E |  | Indianapolis Executive Airport (KTYQ) | De Ford Airport (4II0) | 2026-05-02 21:52 UTC | 2026-05-02 22:09 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
