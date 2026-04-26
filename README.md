# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_15:51:09_UTC-green)

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

**Latest saved flight:** 2026-04-26 15:51:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 15:51:09 UTC

- **55,513** saved flights
- **21,824** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,513** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **670,884.3 tonnes** estimated CO2 emissions
- **38,891,845 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2355 |
| 2 | SkyWest Airlines | 2080 |
| 3 | IndiGo | 1271 |
| 4 | EJA | 973 |
| 5 | American Airlines | 884 |
| 6 | Southwest Airlines | 782 |
| 7 | ENY | 698 |
| 8 | Lufthansa | 687 |
| 9 | Vueling | 559 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 535 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 466 |
| 14 | Delta Air Lines | 457 |
| 15 | WIF | 457 |
| 16 | Swiss International | 437 |
| 17 | QLK | 429 |
| 18 | LXJ | 398 |
| 19 | AEE | 369 |
| 20 | Alaska Airlines | 368 |
| 21 | EJU | 360 |
| 22 | easyJet | 355 |
| 23 | VIV | 355 |
| 24 | Air France | 323 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 312 |
| 27 | AXB | 302 |
| 28 | AIQ | 283 |
| 29 | GLO | 283 |
| 30 | JetBlue | 282 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43860 |
| 2 | 🇪🇸 ES | 4063 |
| 3 | 🇮🇳 IN | 4012 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3209 |
| 6 | 🇩🇪 DE | 3047 |
| 7 | 🇮🇹 IT | 3031 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2734 |
| 10 | 🇨🇴 CO | 2507 |
| 11 | 🇬🇧 GB | 2339 |
| 12 | 🇫🇷 FR | 2196 |
| 13 | 🇲🇽 MX | 1751 |
| 14 | 🇬🇷 GR | 1655 |
| 15 | 🇨🇭 CH | 1581 |
| 16 | 🇳🇴 NO | 1486 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1145 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1014 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 897 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 826 |
| 26 | 🇲🇦 MA | 706 |
| 27 | 🇲🇪 ME | 608 |
| 28 | 🇳🇱 NL | 577 |
| 29 | 🇲🇴 MO | 570 |
| 30 | 🇧🇸 BS | 481 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1256 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 912 |
| 4 | Indira Gandhi International Airport |  | IN | 849 |
| 5 | El Dorado International Airport |  | CO | 846 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 816 |
| 7 | Guaymaral Airport |  | CO | 760 |
| 8 | Harry Reid International Airport |  | US | 705 |
| 9 | Frankfurt am Main International Airport |  | DE | 672 |
| 10 | Zurich Airport |  | CH | 669 |
| 11 | La Aurora Airport |  | GT | 619 |
| 12 | Macau International Airport |  | MO | 570 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 546 |
| 14 | Chicago O'Hare International Airport |  | US | 539 |
| 15 | Kuala Lumpur International Airport |  | MY | 523 |
| 16 | Madrid Barajas International Airport |  | ES | 520 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 518 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 477 |
| 20 | Bengaluru International Airport |  | IN | 477 |
| 21 | Congonhas Airport |  | BR | 462 |
| 22 | Charlotte/Douglas International Airport |  | US | 448 |
| 23 | Tenerife Norte Airport |  | ES | 444 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 427 |
| 26 | Salt Lake City International Airport |  | US | 419 |
| 27 | Capua Airport |  | IT | 414 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 410 |
| 29 | Daniel K Inouye International Airport |  | US | 407 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 401 |
| 31 | Vitoria/Foronda Airport |  | ES | 384 |
| 32 | Barcelona International Airport |  | ES | 379 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 372 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 371 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 363 |
| 37 | O. R. Tambo International Airport |  | ZA | 357 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Amsterdam Airport Schiphol |  | NL | 327 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 309 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 203 | 14m | 114 km | 398.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 92 | 27m | 215 km | 340.7 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 84 | 27m | 152 km | 219.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 78 | 1h 1m | 695 km | 935.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 72 | 1h 19m | 961 km | 1,193.4 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 69 | 1h 42m | 1,423 km | 1,693.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| S5PIF |  | Avernas-le-Bauduin Airport (EBAV) | Avernas-le-Bauduin Airport (EBAV) | 2026-04-26 15:36 UTC | 2026-04-26 15:51 UTC | 15m |
| N336ST |  | Southbridge Municipal Airport (K3B0) | Orange Municipal Airport (KORE) | 2026-04-26 15:24 UTC | 2026-04-26 15:41 UTC | 16m |
| N734BB |  | Goering Ranches / Chocheta Estates Airport (50OR) | Bend Municipal Airport (KBDN) | 2026-04-26 15:25 UTC | 2026-04-26 15:37 UTC | 11m |
| VAR488 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-26 15:18 UTC | 2026-04-26 15:34 UTC | 15m |
| CHX29 | CHX | Hamburg Airport (EDDH) | Lubeck Blankensee Airport (EDHL) | 2026-04-26 15:26 UTC | 2026-04-26 15:33 UTC | 6m |
| N423R |  | Jekyll Island Airport (K09J) | K4R4 (K4R4) | 2026-04-26 13:10 UTC | 2026-04-26 15:31 UTC | 2h 21m |
| HKC9486 | HKC | Istanbul Hezarfen Airfield (LTBW) | Macau International Airport (VMMC) | 2026-04-26 03:30 UTC | 2026-04-26 15:26 UTC | 11h 55m |
| RFD9002 | RFD | Plan De Guadalupe International Airport (MMIO) | Plan De Guadalupe International Airport (MMIO) | 2026-04-26 15:07 UTC | 2026-04-26 15:23 UTC | 15m |
| N2221 |  | Bonanza Hills Airport (34CN) | Lake Tahoe Airport (KTVL) | 2026-04-26 14:46 UTC | 2026-04-26 15:21 UTC | 34m |
| N248PH |  | Redding Regional Airport (KRDD) | Weed Airport (KO46) | 2026-04-26 14:56 UTC | 2026-04-26 15:12 UTC | 16m |
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-26 08:28 UTC | 2026-04-26 15:10 UTC | 6h 42m |
| ANE89CU | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-04-26 14:32 UTC | 2026-04-26 15:07 UTC | 35m |
| JTL505 | JTL | Rocky Mountain Metro Airport (KBJC) | Morning Shadows Ranch Airport (CD69) | 2026-04-26 14:36 UTC | 2026-04-26 15:04 UTC | 28m |
| ETD7MA | Etihad Airways | Abu Dhabi International Airport (OMAA) | Queen Alia International Airport (OJAI) | 2026-04-26 11:33 UTC | 2026-04-26 15:04 UTC | 3h 30m |
| AEE6SM | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-26 14:28 UTC | 2026-04-26 15:01 UTC | 33m |
| TWY41 | TWY | Sacramento International Airport (KSMF) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-26 14:39 UTC | 2026-04-26 15:01 UTC | 22m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:23 UTC | 2026-04-26 15:00 UTC | 37m |
| XBOLM | XBO | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:34 UTC | 2026-04-26 15:00 UTC | 25m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:22 UTC | 2026-04-26 15:00 UTC | 37m |
| XBSJZ | XBS | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:25 UTC | 2026-04-26 15:00 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
