# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_15:10:51_UTC-green)

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

**Latest saved flight:** 2026-04-26 15:10:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 15:10:51 UTC

- **55,413** saved flights
- **21,790** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,413** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **669,777.6 tonnes** estimated CO2 emissions
- **38,827,685 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2350 |
| 2 | SkyWest Airlines | 2077 |
| 3 | IndiGo | 1266 |
| 4 | EJA | 971 |
| 5 | American Airlines | 882 |
| 6 | Southwest Airlines | 782 |
| 7 | ENY | 694 |
| 8 | Lufthansa | 685 |
| 9 | Vueling | 558 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 533 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 466 |
| 14 | Delta Air Lines | 456 |
| 15 | WIF | 456 |
| 16 | Swiss International | 435 |
| 17 | QLK | 429 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 367 |
| 21 | EJU | 359 |
| 22 | easyJet | 355 |
| 23 | VIV | 352 |
| 24 | Air France | 322 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 312 |
| 27 | AXB | 300 |
| 28 | AIQ | 283 |
| 29 | JetBlue | 281 |
| 30 | GLO | 280 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43802 |
| 2 | 🇪🇸 ES | 4051 |
| 3 | 🇮🇳 IN | 4000 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3195 |
| 6 | 🇩🇪 DE | 3034 |
| 7 | 🇮🇹 IT | 3020 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2734 |
| 10 | 🇨🇴 CO | 2499 |
| 11 | 🇬🇧 GB | 2336 |
| 12 | 🇫🇷 FR | 2194 |
| 13 | 🇲🇽 MX | 1739 |
| 14 | 🇬🇷 GR | 1649 |
| 15 | 🇨🇭 CH | 1577 |
| 16 | 🇳🇴 NO | 1482 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1145 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1008 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 895 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 826 |
| 26 | 🇲🇦 MA | 705 |
| 27 | 🇲🇪 ME | 607 |
| 28 | 🇳🇱 NL | 575 |
| 29 | 🇲🇴 MO | 569 |
| 30 | 🇧🇸 BS | 477 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1252 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 912 |
| 4 | Indira Gandhi International Airport |  | IN | 849 |
| 5 | El Dorado International Airport |  | CO | 844 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 813 |
| 7 | Guaymaral Airport |  | CO | 757 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Frankfurt am Main International Airport |  | DE | 671 |
| 10 | Zurich Airport |  | CH | 667 |
| 11 | La Aurora Airport |  | GT | 619 |
| 12 | Macau International Airport |  | MO | 569 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 537 |
| 15 | Kuala Lumpur International Airport |  | MY | 523 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 518 |
| 17 | Madrid Barajas International Airport |  | ES | 516 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 477 |
| 20 | Bengaluru International Airport |  | IN | 473 |
| 21 | Congonhas Airport |  | BR | 456 |
| 22 | Charlotte/Douglas International Airport |  | US | 447 |
| 23 | Tenerife Norte Airport |  | ES | 444 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 426 |
| 26 | Salt Lake City International Airport |  | US | 418 |
| 27 | Capua Airport |  | IT | 411 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 29 | Daniel K Inouye International Airport |  | US | 407 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 399 |
| 31 | Vitoria/Foronda Airport |  | ES | 383 |
| 32 | Barcelona International Airport |  | ES | 378 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 371 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 370 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 363 |
| 37 | O. R. Tambo International Airport |  | ZA | 357 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Viracopos International Airport |  | BR | 325 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 308 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 202 | 14m | 114 km | 396.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 129 | 26m | 275 km | 611.3 t |
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
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 76 | 13m | 99 km | 130.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 73 | 58m | 493 km | 621.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 69 | 1h 42m | 1,423 km | 1,693.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-26 08:28 UTC | 2026-04-26 15:10 UTC | 6h 42m |
| ETD7MA | Etihad Airways | Abu Dhabi International Airport (OMAA) | Queen Alia International Airport (OJAI) | 2026-04-26 11:33 UTC | 2026-04-26 15:04 UTC | 3h 30m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:23 UTC | 2026-04-26 15:00 UTC | 37m |
| XBOLM | XBO | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:34 UTC | 2026-04-26 15:00 UTC | 25m |
| XBONC | XBO | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:22 UTC | 2026-04-26 15:00 UTC | 37m |
| XBSJZ | XBS | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:25 UTC | 2026-04-26 15:00 UTC | 35m |
| XABNB | XAB | Licenciado Benito Juarez International Airport (MMMX) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:45 UTC | 2026-04-26 15:00 UTC | 14m |
| XBJMV | XBJ | MM62 (MM62) | MM62 (MM62) | 2026-04-26 14:14 UTC | 2026-04-26 15:00 UTC | 45m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 14:43 UTC | 2026-04-26 15:00 UTC | 16m |
| N445BL |  | Orlando Sanford International Airport (KSFB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-04-26 14:13 UTC | 2026-04-26 14:58 UTC | 45m |
| DFL5840 | DFL | Stockholm-Bromma Airport (ESSB) | Stockholm-Bromma Airport (ESSB) | 2026-04-26 14:52 UTC | 2026-04-26 14:58 UTC | 5m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-26 14:42 UTC | 2026-04-26 14:56 UTC | 14m |
| N48868 |  | Roberts Field (KRDM) | Prineville Airport (KS39) | 2026-04-26 14:15 UTC | 2026-04-26 14:45 UTC | 29m |
| FDB3PR | flydubai | Ihtiman Airport (LBHT) | Queen Alia International Airport (OJAI) | 2026-04-26 12:52 UTC | 2026-04-26 14:35 UTC | 1h 42m |
| PYN04 | PYN | Manchester Airport (EGCC) | Newquay Cornwall Airport (EGHQ) | 2026-04-26 13:38 UTC | 2026-04-26 14:34 UTC | 55m |
| N38BL |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-26 14:11 UTC | 2026-04-26 14:31 UTC | 19m |
| RYR17TD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Brindisi / Casale Airport (LIBR) | 2026-04-26 13:03 UTC | 2026-04-26 14:27 UTC | 1h 23m |
| DU202 |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-04-26 14:24 UTC | 2026-04-26 14:27 UTC | 2m |
| RYR78HC | Ryanair | Barcelona International Airport (LEBL) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-26 12:50 UTC | 2026-04-26 14:24 UTC | 1h 33m |
| WIF850 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-26 14:11 UTC | 2026-04-26 14:24 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
