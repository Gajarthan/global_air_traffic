# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_15:19:40_UTC-green)

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

**Latest saved flight:** 2026-05-03 15:19:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 15:19:40 UTC

- **65,954** saved flights
- **24,942** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,954** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **809,608.4 tonnes** estimated CO2 emissions
- **46,933,822 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2813 |
| 2 | SkyWest Airlines | 2421 |
| 3 | IndiGo | 1534 |
| 4 | EJA | 1162 |
| 5 | American Airlines | 1014 |
| 6 | Southwest Airlines | 924 |
| 7 | Lufthansa | 850 |
| 8 | ENY | 809 |
| 9 | Vueling | 653 |
| 10 | AXM | 648 |
| 11 | LATAM Airlines | 615 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 551 |
| 14 | WIF | 550 |
| 15 | AZU | 533 |
| 16 | QLK | 513 |
| 17 | Swiss International | 508 |
| 18 | LXJ | 471 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 440 |
| 21 | AEE | 429 |
| 22 | EJU | 427 |
| 23 | VIV | 411 |
| 24 | Cathay Pacific | 397 |
| 25 | Japan Airlines | 388 |
| 26 | Air France | 387 |
| 27 | AXB | 371 |
| 28 | AIQ | 339 |
| 29 | CXK | 336 |
| 30 | GLO | 322 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51934 |
| 2 | 🇪🇸 ES | 4855 |
| 3 | 🇮🇳 IN | 4818 |
| 4 | 🇦🇺 AU | 4408 |
| 5 | 🇧🇷 BR | 3713 |
| 6 | 🇩🇪 DE | 3702 |
| 7 | 🇮🇹 IT | 3607 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3218 |
| 10 | 🇬🇧 GB | 2858 |
| 11 | 🇨🇴 CO | 2649 |
| 12 | 🇫🇷 FR | 2621 |
| 13 | 🇲🇽 MX | 2081 |
| 14 | 🇬🇷 GR | 1979 |
| 15 | 🇨🇭 CH | 1858 |
| 16 | 🇳🇴 NO | 1795 |
| 17 | 🇲🇾 MY | 1597 |
| 18 | 🇿🇦 ZA | 1352 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1192 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1090 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1011 |
| 26 | 🇲🇦 MA | 811 |
| 27 | 🇲🇴 MO | 742 |
| 28 | 🇲🇪 ME | 718 |
| 29 | 🇳🇱 NL | 701 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1440 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 1004 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 962 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 850 |
| 8 | Guaymaral Airport |  | CO | 844 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 786 |
| 11 | La Aurora Airport |  | GT | 757 |
| 12 | Macau International Airport |  | MO | 742 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 643 |
| 14 | Kuala Lumpur International Airport |  | MY | 637 |
| 15 | Madrid Barajas International Airport |  | ES | 633 |
| 16 | Chicago O'Hare International Airport |  | US | 628 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 591 |
| 18 | Bengaluru International Airport |  | IN | 589 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 569 |
| 21 | Congonhas Airport |  | BR | 535 |
| 22 | Tenerife Norte Airport |  | ES | 529 |
| 23 | Charlotte/Douglas International Airport |  | US | 521 |
| 24 | Charles de Gaulle International Airport |  | FR | 519 |
| 25 | Salt Lake City International Airport |  | US | 516 |
| 26 | Ninoy Aquino International Airport |  | PH | 504 |
| 27 | Capua Airport |  | IT | 498 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 486 |
| 29 | Daniel K Inouye International Airport |  | US | 482 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 467 |
| 31 | Barcelona International Airport |  | ES | 451 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 442 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 441 |
| 34 | Vitoria/Foronda Airport |  | ES | 441 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 412 |
| 38 | Amsterdam Airport Schiphol |  | NL | 411 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 384 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 348 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 223 | 21m | 244 km | 939.0 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 166 | 20m | 165 km | 472.2 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 161 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 118 | 21m | 99 km | 202.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 104 | 28m | 152 km | 271.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 102 | 27m | 215 km | 377.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 99 | 20m | 147 km | 250.5 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 93 | 57m | 493 km | 791.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 53m | 1,304 km | 2,024.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 87 | 1h 42m | 1,423 km | 2,135.1 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RTV4T | RTV | Vilar Da Luz Airport (LPVL) | Vila Real Airport (LPVR) | 2026-05-03 14:37 UTC | 2026-05-03 15:19 UTC | 41m |
| SPSMD | SPS | Poznań-Ławica Airport (EPPO) | Bydgoszcz-Biedaszkowo Airport (EPBD) | 2026-05-03 14:31 UTC | 2026-05-03 15:19 UTC | 47m |
| N90D |  | Plan De Guadalupe International Airport (MMIO) | Plan De Guadalupe International Airport (MMIO) | 2026-05-03 13:59 UTC | 2026-05-03 15:17 UTC | 1h 17m |
| N8297N |  | Aero Country Airport (KT31) | Commerce Municipal Airport (K2F7) | 2026-05-03 14:49 UTC | 2026-05-03 15:13 UTC | 23m |
| KENLEY | KEN | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-05-03 14:54 UTC | 2026-05-03 15:11 UTC | 16m |
| N3641R |  | Somerset Airport (KSMQ) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-05-03 14:20 UTC | 2026-05-03 15:07 UTC | 47m |
| N234WL |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-05-03 14:26 UTC | 2026-05-03 15:05 UTC | 39m |
| CPA336 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-03 07:50 UTC | 2026-05-03 15:05 UTC | 7h 15m |
| N6461Z |  | Double Eagle Ii Airport (KAEG) | Grants-Milan Municipal Airport (KGNT) | 2026-05-03 14:33 UTC | 2026-05-03 15:05 UTC | 32m |
| IHFRT | IHF | Lugano Airport (LSZA) | Milano / Bresso Airport (LIMB) | 2026-05-03 14:46 UTC | 2026-05-03 15:02 UTC | 16m |
| CXK178 | CXK | Georgetown-Scott County Regional Airport (K27K) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-03 14:26 UTC | 2026-05-03 15:02 UTC | 36m |
| AIZ994 | AIZ | John F Kennedy International Airport (KJFK) | Herzliya Airport (LLHZ) | 2026-05-03 04:47 UTC | 2026-05-03 14:58 UTC | 10h 11m |
| SCU59 | SCU | 19OK (19OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-05-03 14:48 UTC | 2026-05-03 14:58 UTC | 10m |
| N333CT |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-05-03 14:15 UTC | 2026-05-03 14:56 UTC | 40m |
| N5001U |  | Sumter Airport (KSMS) | Hilton Head Airport (KHXD) | 2026-05-03 13:36 UTC | 2026-05-03 14:56 UTC | 1h 20m |
| FHGTF | FHG | Voghera-Rivanazzano Airport (LILH) | Voghera-Rivanazzano Airport (LILH) | 2026-05-03 14:32 UTC | 2026-05-03 14:53 UTC | 21m |
| N150RJ |  | Robertson Ranch Airport (0TE0) | Cavern City Air Trml Airport (KCNM) | 2026-05-03 14:20 UTC | 2026-05-03 14:52 UTC | 32m |
| N1923F |  | Cobb County International/Mccollum Field (KRYY) | Cobb County International/Mccollum Field (KRYY) | 2026-05-03 14:48 UTC | 2026-05-03 14:51 UTC | 3m |
| OUA10 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Gregg Airport (7OK1) | 2026-05-03 14:03 UTC | 2026-05-03 14:51 UTC | 48m |
| JFA32D | JFA | Bern Belp Airport (LSZB) | Graz Airport (LOWG) | 2026-05-03 13:40 UTC | 2026-05-03 14:45 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
