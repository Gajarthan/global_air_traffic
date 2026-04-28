# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_13:03:25_UTC-green)

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

**Latest saved flight:** 2026-04-28 13:03:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 13:03:25 UTC

- **58,102** saved flights
- **22,628** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,102** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **707,147.1 tonnes** estimated CO2 emissions
- **40,994,033 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2470 |
| 2 | SkyWest Airlines | 2190 |
| 3 | IndiGo | 1332 |
| 4 | EJA | 1031 |
| 5 | American Airlines | 917 |
| 6 | Southwest Airlines | 831 |
| 7 | Lufthansa | 729 |
| 8 | ENY | 726 |
| 9 | Vueling | 577 |
| 10 | AXM | 570 |
| 11 | LATAM Airlines | 554 |
| 12 | All Nippon Airways | 517 |
| 13 | WIF | 485 |
| 14 | AZU | 482 |
| 15 | Delta Air Lines | 475 |
| 16 | Swiss International | 462 |
| 17 | QLK | 456 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 396 |
| 20 | AEE | 387 |
| 21 | easyJet | 383 |
| 22 | EJU | 376 |
| 23 | VIV | 369 |
| 24 | Air France | 341 |
| 25 | Japan Airlines | 338 |
| 26 | Cathay Pacific | 337 |
| 27 | AXB | 316 |
| 28 | AIQ | 295 |
| 29 | JetBlue | 294 |
| 30 | United Airlines | 290 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45906 |
| 2 | 🇪🇸 ES | 4228 |
| 3 | 🇮🇳 IN | 4187 |
| 4 | 🇦🇺 AU | 3957 |
| 5 | 🇧🇷 BR | 3300 |
| 6 | 🇩🇪 DE | 3200 |
| 7 | 🇮🇹 IT | 3184 |
| 8 | 🇯🇵 JP | 3157 |
| 9 | 🇨🇦 CA | 2866 |
| 10 | 🇨🇴 CO | 2605 |
| 11 | 🇬🇧 GB | 2468 |
| 12 | 🇫🇷 FR | 2291 |
| 13 | 🇲🇽 MX | 1831 |
| 14 | 🇬🇷 GR | 1732 |
| 15 | 🇨🇭 CH | 1638 |
| 16 | 🇳🇴 NO | 1577 |
| 17 | 🇲🇾 MY | 1381 |
| 18 | 🇿🇦 ZA | 1186 |
| 19 | 🇳🇿 NZ | 1092 |
| 20 | 🇹🇷 TR | 1058 |
| 21 | 🇹🇭 TH | 1056 |
| 22 | 🇵🇭 PH | 982 |
| 23 | 🇵🇱 PL | 937 |
| 24 | 🇰🇷 KR | 926 |
| 25 | 🇬🇹 GT | 851 |
| 26 | 🇲🇦 MA | 734 |
| 27 | 🇲🇪 ME | 631 |
| 28 | 🇲🇴 MO | 627 |
| 29 | 🇳🇱 NL | 604 |
| 30 | 🇮🇩 ID | 502 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1311 |
| 2 | Tokyo International Airport |  | JP | 1073 |
| 3 | Denver International Airport |  | US | 969 |
| 4 | Indira Gandhi International Airport |  | IN | 883 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 852 |
| 7 | Guaymaral Airport |  | CO | 801 |
| 8 | Harry Reid International Airport |  | US | 740 |
| 9 | Frankfurt am Main International Airport |  | DE | 718 |
| 10 | Zurich Airport |  | CH | 702 |
| 11 | La Aurora Airport |  | GT | 641 |
| 12 | Macau International Airport |  | MO | 627 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 575 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Kuala Lumpur International Airport |  | MY | 544 |
| 16 | Madrid Barajas International Airport |  | ES | 541 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 513 |
| 19 | Malpensa International Airport |  | IT | 502 |
| 20 | Bengaluru International Airport |  | IN | 499 |
| 21 | Congonhas Airport |  | BR | 476 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 452 |
| 25 | Salt Lake City International Airport |  | US | 449 |
| 26 | Charles de Gaulle International Airport |  | FR | 449 |
| 27 | Capua Airport |  | IT | 442 |
| 28 | Daniel K Inouye International Airport |  | US | 429 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 425 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 418 |
| 31 | Barcelona International Airport |  | ES | 394 |
| 32 | Vitoria/Foronda Airport |  | ES | 392 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 385 |
| 35 | O. R. Tambo International Airport |  | ZA | 378 |
| 36 | Reno/Tahoe International Airport |  | US | 374 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 370 |
| 38 | Don Mueang International Airport |  | TH | 359 |
| 39 | Amsterdam Airport Schiphol |  | NL | 348 |
| 40 | Calgary International Airport |  | CA | 342 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 188 | 21m | 244 km | 791.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 183 | 24m | 225 km | 710.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 171 | 1h 27m | 910 km | 2,683.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 139 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 132 | 26m | 275 km | 625.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 120 | 1h 12m | 770 km | 1,594.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 93 | 20m | 250 km | 401.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHUNI | FHU | Cannes-Mandelieu Airport (LFMD) | Calvi-Sainte-Catherine Airport (LFKC) | 2026-04-28 12:26 UTC | 2026-04-28 13:03 UTC | 37m |
| N105GP |  | Smyrna Airport (KMQY) | Barkley Regional Airport (KPAH) | 2026-04-28 12:21 UTC | 2026-04-28 12:55 UTC | 34m |
| HORUS30 | HOR | Uzes Airport (LFNU) | Nimes-Arles-Camargue Airport (LFTW) | 2026-04-28 12:40 UTC | 2026-04-28 12:54 UTC | 13m |
| N988WP |  | Mc Clellan Airfield (KMCC) | Buchanan Field (KCCR) | 2026-04-28 12:34 UTC | 2026-04-28 12:52 UTC | 17m |
| PHONX72 | PHO | RAF Waddington (EGXW) | RAF Waddington (EGXW) | 2026-04-28 12:26 UTC | 2026-04-28 12:48 UTC | 22m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-28 06:14 UTC | 2026-04-28 12:46 UTC | 6h 31m |
| FAG142 | FAG | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-28 12:40 UTC | 2026-04-28 12:45 UTC | 5m |
| CSR33 | CSR | Montpellier Candillargues Airport (LFNG) | Nimes-Arles-Camargue Airport (LFTW) | 2026-04-28 12:35 UTC | 2026-04-28 12:45 UTC | 10m |
| BPO320 | BPO | Siegerland Airport (EDGS) | Siegerland Airport (EDGS) | 2026-04-28 12:08 UTC | 2026-04-28 12:40 UTC | 32m |
| DFL5720 | DFL | Stockholm-Bromma Airport (ESSB) | Stockholm-Bromma Airport (ESSB) | 2026-04-28 12:32 UTC | 2026-04-28 12:39 UTC | 6m |
| JAL229 | Japan Airlines | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-28 11:59 UTC | 2026-04-28 12:38 UTC | 39m |
| AIZ745 | AIZ | Ben Gurion International Airport (LLBG) | Ben Gurion International Airport (LLBG) | 2026-04-28 12:22 UTC | 2026-04-28 12:36 UTC | 13m |
| WJF7KB | WJF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-04-28 12:22 UTC | 2026-04-28 12:32 UTC | 10m |
| ANA97 | All Nippon Airways | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-28 11:53 UTC | 2026-04-28 12:32 UTC | 38m |
| ITY1613 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bari / Palese International Airport (LIBD) | 2026-04-28 11:54 UTC | 2026-04-28 12:31 UTC | 37m |
| N6868P |  | Flying Cloud Airport (KFCM) | MY13 (MY13) | 2026-04-28 11:55 UTC | 2026-04-28 12:29 UTC | 34m |
| TRITON01 | TRI | Sindal Airport (EKSN) | Kristiansand Airport (ENCN) | 2026-04-28 12:05 UTC | 2026-04-28 12:28 UTC | 22m |
| QTR8438 | Qatar Airways | Zirku Airport (OMAZ) | Macau International Airport (VMMC) | 2026-04-28 05:33 UTC | 2026-04-28 12:27 UTC | 6h 53m |
| CPA332 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-28 04:36 UTC | 2026-04-28 12:24 UTC | 7h 47m |
| JANET77 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-04-28 12:12 UTC | 2026-04-28 12:24 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
