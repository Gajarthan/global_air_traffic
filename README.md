# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_15:52:12_UTC-green)

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

**Latest saved flight:** 2026-04-30 15:52:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 15:52:12 UTC

- **60,745** saved flights
- **23,403** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,745** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **740,163.3 tonnes** estimated CO2 emissions
- **42,908,017 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2571 |
| 2 | SkyWest Airlines | 2257 |
| 3 | IndiGo | 1399 |
| 4 | EJA | 1085 |
| 5 | American Airlines | 946 |
| 6 | Southwest Airlines | 857 |
| 7 | Lufthansa | 776 |
| 8 | ENY | 751 |
| 9 | Vueling | 605 |
| 10 | AXM | 595 |
| 11 | LATAM Airlines | 579 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 516 |
| 14 | Delta Air Lines | 505 |
| 15 | AZU | 496 |
| 16 | Swiss International | 479 |
| 17 | QLK | 478 |
| 18 | LXJ | 429 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 402 |
| 21 | easyJet | 400 |
| 22 | EJU | 390 |
| 23 | VIV | 380 |
| 24 | Cathay Pacific | 362 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 334 |
| 28 | AIQ | 311 |
| 29 | JetBlue | 300 |
| 30 | CXK | 299 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47895 |
| 2 | 🇮🇳 IN | 4416 |
| 3 | 🇪🇸 ES | 4414 |
| 4 | 🇦🇺 AU | 4149 |
| 5 | 🇧🇷 BR | 3441 |
| 6 | 🇩🇪 DE | 3392 |
| 7 | 🇮🇹 IT | 3325 |
| 8 | 🇯🇵 JP | 3315 |
| 9 | 🇨🇦 CA | 2999 |
| 10 | 🇨🇴 CO | 2619 |
| 11 | 🇬🇧 GB | 2584 |
| 12 | 🇫🇷 FR | 2403 |
| 13 | 🇲🇽 MX | 1896 |
| 14 | 🇬🇷 GR | 1811 |
| 15 | 🇨🇭 CH | 1708 |
| 16 | 🇳🇴 NO | 1692 |
| 17 | 🇲🇾 MY | 1447 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1139 |
| 20 | 🇹🇭 TH | 1103 |
| 21 | 🇹🇷 TR | 1084 |
| 22 | 🇵🇭 PH | 1023 |
| 23 | 🇵🇱 PL | 987 |
| 24 | 🇰🇷 KR | 985 |
| 25 | 🇬🇹 GT | 888 |
| 26 | 🇲🇦 MA | 755 |
| 27 | 🇲🇴 MO | 675 |
| 28 | 🇲🇪 ME | 667 |
| 29 | 🇳🇱 NL | 640 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1341 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1006 |
| 4 | Indira Gandhi International Airport |  | IN | 931 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 890 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 814 |
| 8 | Harry Reid International Airport |  | US | 770 |
| 9 | Frankfurt am Main International Airport |  | DE | 770 |
| 10 | Zurich Airport |  | CH | 732 |
| 11 | Macau International Airport |  | MO | 675 |
| 12 | La Aurora Airport |  | GT | 668 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 601 |
| 14 | Chicago O'Hare International Airport |  | US | 574 |
| 15 | Kuala Lumpur International Airport |  | MY | 570 |
| 16 | Madrid Barajas International Airport |  | ES | 567 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Bengaluru International Airport |  | IN | 530 |
| 20 | Malpensa International Airport |  | IT | 528 |
| 21 | Congonhas Airport |  | BR | 496 |
| 22 | Charlotte/Douglas International Airport |  | US | 483 |
| 23 | Tenerife Norte Airport |  | ES | 474 |
| 24 | Charles de Gaulle International Airport |  | FR | 474 |
| 25 | Salt Lake City International Airport |  | US | 470 |
| 26 | Ninoy Aquino International Airport |  | PH | 468 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 454 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 443 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 31 | Barcelona International Airport |  | ES | 412 |
| 32 | Vitoria/Foronda Airport |  | ES | 410 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 405 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 400 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 385 |
| 37 | Reno/Tahoe International Airport |  | US | 383 |
| 38 | Don Mueang International Airport |  | TH | 379 |
| 39 | Amsterdam Airport Schiphol |  | NL | 375 |
| 40 | Calgary International Airport |  | CA | 358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 333 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 179 | 1h 27m | 910 km | 2,808.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 150 | 19m | 165 km | 426.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 145 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 102 | 31m | 369 km | 649.3 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 102 | 20m | 99 km | 174.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 85 | 1h 42m | 1,156 km | 1,695.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 78 | 14m | 154 km | 206.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RFS713 | RFS | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-30 15:32 UTC | 2026-04-30 15:52 UTC | 19m |
| N53695 |  | Miami Executive Airport (KTMB) | Miami-Opa Locka Executive Airport (KOPF) | 2026-04-30 15:15 UTC | 2026-04-30 15:47 UTC | 32m |
| N1866M |  | Frederick W Smith International Airport (KMEM) | Jonesboro Municipal Airport (KJBR) | 2026-04-30 15:27 UTC | 2026-04-30 15:47 UTC | 19m |
| N55BF |  | KU77 (KU77) | KU77 (KU77) | 2026-04-30 15:23 UTC | 2026-04-30 15:46 UTC | 23m |
| N955JA |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-30 14:27 UTC | 2026-04-30 15:43 UTC | 1h 16m |
| N586T |  | Corona Municipal Airport (KAJO) | Big Bear City Airport (KL35) | 2026-04-30 15:12 UTC | 2026-04-30 15:41 UTC | 28m |
| REV6LX | REV | Inverness Airport (EGPE) | Inverness Airport (EGPE) | 2026-04-30 14:59 UTC | 2026-04-30 15:40 UTC | 41m |
| IGO6041 | IndiGo | Shimla Airport (VISM) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-30 13:06 UTC | 2026-04-30 15:38 UTC | 2h 31m |
| BOX738 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-30 01:55 UTC | 2026-04-30 15:37 UTC | 13h 42m |
| N630CB |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-30 14:45 UTC | 2026-04-30 15:36 UTC | 51m |
| DBOLT | DBO | Munich International Airport (EDDM) | Dortmund Airport (EDLW) | 2026-04-30 14:46 UTC | 2026-04-30 15:32 UTC | 45m |
| N9849H |  | Grand Junction Regional Airport (KGJT) | Pinyon Airport (CO43) | 2026-04-30 15:19 UTC | 2026-04-30 15:31 UTC | 11m |
| BOMR843 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Gritz Field (XS46) | 2026-04-30 15:00 UTC | 2026-04-30 15:30 UTC | 29m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-04-30 15:16 UTC | 2026-04-30 15:28 UTC | 12m |
| C6044 |  | Mobile Regional Airport (KMOB) | Mobile Regional Airport (KMOB) | 2026-04-30 14:54 UTC | 2026-04-30 15:28 UTC | 33m |
| N507EZ |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-30 15:14 UTC | 2026-04-30 15:27 UTC | 13m |
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-04-30 08:26 UTC | 2026-04-30 15:27 UTC | 7h 0m |
| N2441D |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-30 14:55 UTC | 2026-04-30 15:26 UTC | 31m |
| N79565 |  | Tampa North Aero Park Airport (KX39) | Tampa North Aero Park Airport (KX39) | 2026-04-30 14:48 UTC | 2026-04-30 15:26 UTC | 37m |
| OEEKZ | OEE | Frankfurt-Egelsbach Airport (EDFE) | St. Johann In Tirol Airport (LOIJ) | 2026-04-30 14:32 UTC | 2026-04-30 15:26 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
