# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_19:50:09_UTC-green)

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

**Latest saved flight:** 2026-05-02 19:50:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 19:50:09 UTC

- **64,836** saved flights
- **24,650** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,836** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **794,708.5 tonnes** estimated CO2 emissions
- **46,070,058 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2756 |
| 2 | SkyWest Airlines | 2390 |
| 3 | IndiGo | 1495 |
| 4 | EJA | 1154 |
| 5 | American Airlines | 1002 |
| 6 | Southwest Airlines | 912 |
| 7 | Lufthansa | 834 |
| 8 | ENY | 793 |
| 9 | Vueling | 640 |
| 10 | AXM | 631 |
| 11 | LATAM Airlines | 601 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 536 |
| 15 | AZU | 525 |
| 16 | QLK | 502 |
| 17 | Swiss International | 499 |
| 18 | LXJ | 465 |
| 19 | Alaska Airlines | 443 |
| 20 | easyJet | 425 |
| 21 | AEE | 420 |
| 22 | EJU | 415 |
| 23 | VIV | 406 |
| 24 | Cathay Pacific | 390 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 377 |
| 27 | AXB | 363 |
| 28 | AIQ | 330 |
| 29 | CXK | 330 |
| 30 | GLO | 316 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51259 |
| 2 | 🇪🇸 ES | 4747 |
| 3 | 🇮🇳 IN | 4707 |
| 4 | 🇦🇺 AU | 4343 |
| 5 | 🇧🇷 BR | 3651 |
| 6 | 🇩🇪 DE | 3636 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3525 |
| 9 | 🇨🇦 CA | 3174 |
| 10 | 🇬🇧 GB | 2786 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2569 |
| 13 | 🇲🇽 MX | 2049 |
| 14 | 🇬🇷 GR | 1941 |
| 15 | 🇨🇭 CH | 1820 |
| 16 | 🇳🇴 NO | 1764 |
| 17 | 🇲🇾 MY | 1546 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1161 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇵🇱 PL | 1061 |
| 24 | 🇰🇷 KR | 1056 |
| 25 | 🇬🇹 GT | 998 |
| 26 | 🇲🇦 MA | 796 |
| 27 | 🇲🇴 MO | 730 |
| 28 | 🇲🇪 ME | 698 |
| 29 | 🇳🇱 NL | 683 |
| 30 | 🇮🇩 ID | 545 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1420 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1062 |
| 4 | Indira Gandhi International Airport |  | IN | 988 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 945 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 834 |
| 9 | Harry Reid International Airport |  | US | 813 |
| 10 | Zurich Airport |  | CH | 769 |
| 11 | La Aurora Airport |  | GT | 748 |
| 12 | Macau International Airport |  | MO | 730 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 633 |
| 14 | Madrid Barajas International Airport |  | ES | 617 |
| 15 | Chicago O'Hare International Airport |  | US | 614 |
| 16 | Kuala Lumpur International Airport |  | MY | 614 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 578 |
| 18 | Bengaluru International Airport |  | IN | 570 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 559 |
| 21 | Congonhas Airport |  | BR | 526 |
| 22 | Tenerife Norte Airport |  | ES | 517 |
| 23 | Salt Lake City International Airport |  | US | 513 |
| 24 | Charlotte/Douglas International Airport |  | US | 511 |
| 25 | Charles de Gaulle International Airport |  | FR | 505 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Capua Airport |  | IT | 479 |
| 28 | Daniel K Inouye International Airport |  | US | 477 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 474 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 463 |
| 31 | Barcelona International Airport |  | ES | 442 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 432 |
| 33 | Vitoria/Foronda Airport |  | ES | 431 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 430 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 403 |
| 38 | Amsterdam Airport Schiphol |  | NL | 401 |
| 39 | Reno/Tahoe International Airport |  | US | 398 |
| 40 | Calgary International Airport |  | CA | 382 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 220 | 21m | 244 km | 926.4 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 159 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 147 | 26m | 275 km | 696.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
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
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 53m | 1,304 km | 1,979.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 86 | 23m | 55 km | 81.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13469 |  | K4A7 (K4A7) | Perry-Houston County Airport (KPXE) | 2026-05-02 19:12 UTC | 2026-05-02 19:50 UTC | 37m |
| N56601 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-02 18:56 UTC | 2026-05-02 19:45 UTC | 48m |
| N937AS |  | Dayton/Wright Brothers Airport (KMGY) | Richmond Municipal Airport (KRID) | 2026-05-02 19:23 UTC | 2026-05-02 19:43 UTC | 20m |
| N669JW |  | Sanderson Field (KSHN) | Sanderson Field (KSHN) | 2026-05-02 19:21 UTC | 2026-05-02 19:36 UTC | 14m |
| N124CD |  | Laurel Municipal Airport (K6S8) | Laurel Municipal Airport (K6S8) | 2026-05-02 19:22 UTC | 2026-05-02 19:35 UTC | 13m |
| SD3 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-05-02 18:57 UTC | 2026-05-02 19:32 UTC | 35m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-02 19:17 UTC | 2026-05-02 19:31 UTC | 14m |
|  |  | General Manuel Carlos Piar International Airport (SVPR) | Guasipati Airport (SVGT) | 2026-05-02 19:10 UTC | 2026-05-02 19:29 UTC | 18m |
| N3712V |  | Payson Airport (KPAN) | 4AZ7 (4AZ7) | 2026-05-02 18:44 UTC | 2026-05-02 19:24 UTC | 40m |
| N9136S |  | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-05-02 19:09 UTC | 2026-05-02 19:21 UTC | 12m |
| N86SF |  | Tyler Pounds Regional Airport (KTYR) | Kay Ranch Airport (TA61) | 2026-05-02 19:08 UTC | 2026-05-02 19:14 UTC | 6m |
| RTY690 | RTY | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-05-02 18:45 UTC | 2026-05-02 19:12 UTC | 27m |
| N168F |  | Reading Regional/Carl A Spaatz Field (KRDG) | Harrisburg International Airport (KMDT) | 2026-05-02 18:48 UTC | 2026-05-02 19:12 UTC | 24m |
| N2645F |  | Frederick Municipal Airport (KFDK) | Penn Valley Airport (KSEG) | 2026-05-02 18:28 UTC | 2026-05-02 19:12 UTC | 43m |
| N27BN |  | Pueblo Memorial Airport (KPUB) | Mesawood Airport (6CO2) | 2026-05-02 18:28 UTC | 2026-05-02 19:09 UTC | 40m |
| N232TB |  | Arlington Municipal Airport (KAWO) | 89WA (89WA) | 2026-05-02 19:04 UTC | 2026-05-02 19:07 UTC | 3m |
| N3514T |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-05-02 19:00 UTC | 2026-05-02 19:06 UTC | 6m |
| QTR963 | Qatar Airways | Kijang Airport (WIDN) | Al Hamra Airport (OMAH) | 2026-05-02 12:31 UTC | 2026-05-02 19:06 UTC | 6h 35m |
| N32993 |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-05-02 18:43 UTC | 2026-05-02 19:05 UTC | 22m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-02 18:49 UTC | 2026-05-02 19:05 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
