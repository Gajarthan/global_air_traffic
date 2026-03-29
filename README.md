# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_06:19:34_UTC-green)

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

**Latest saved flight:** 2026-03-29 06:19:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 06:19:34 UTC

- **1,375** saved flights
- **1,161** unique routes
- **72** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,375** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **17,204.0 tonnes** estimated CO2 emissions
- **997,333 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Southwest Airlines | 40 |
| 3 | Ryanair | 38 |
| 4 | American Airlines | 33 |
| 5 | EJA | 33 |
| 6 | ENY | 30 |
| 7 | United Airlines | 21 |
| 8 | Delta Air Lines | 20 |
| 9 | IndiGo | 20 |
| 10 | BRC | 17 |
| 11 | LXJ | 17 |
| 12 | LATAM Airlines | 15 |
| 13 | Alaska Airlines | 13 |
| 14 | Avianca | 12 |
| 15 | EDV | 11 |
| 16 | VIV | 11 |
| 17 | AXM | 10 |
| 18 | Cathay Pacific | 10 |
| 19 | Vueling | 10 |
| 20 | QLK | 9 |
| 21 | AZU | 8 |
| 22 | Japan Airlines | 8 |
| 23 | LYM | 8 |
| 24 | SFR | 8 |
| 25 | TGC | 8 |
| 26 | APG | 7 |
| 27 | ARE | 7 |
| 28 | CXK | 7 |
| 29 | All Nippon Airways | 6 |
| 30 | Lufthansa | 6 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1537 |
| 2 | 🇦🇺 AU | 89 |
| 3 | 🇨🇴 CO | 89 |
| 4 | 🇨🇦 CA | 69 |
| 5 | 🇲🇽 MX | 65 |
| 6 | 🇪🇸 ES | 64 |
| 7 | 🇮🇳 IN | 58 |
| 8 | 🇬🇹 GT | 55 |
| 9 | 🇯🇵 JP | 54 |
| 10 | 🇧🇷 BR | 53 |
| 11 | 🇮🇹 IT | 42 |
| 12 | 🇬🇧 GB | 34 |
| 13 | 🇵🇭 PH | 32 |
| 14 | 🇲🇾 MY | 23 |
| 15 | 🇳🇿 NZ | 20 |
| 16 | 🇩🇪 DE | 19 |
| 17 | 🇫🇷 FR | 18 |
| 18 | 🇿🇦 ZA | 18 |
| 19 | 🇧🇸 BS | 16 |
| 20 | 🇹🇭 TH | 15 |
| 21 | 🇭🇳 HN | 14 |
| 22 | 🇬🇷 GR | 13 |
| 23 | 🇲🇦 MA | 13 |
| 24 | 🇮🇩 ID | 13 |
| 25 | 🇹🇷 TR | 13 |
| 26 | 🇵🇱 PL | 12 |
| 27 | 🇲🇴 MO | 12 |
| 28 | 🇨🇭 CH | 11 |
| 29 | 🇳🇱 NL | 9 |
| 30 | 🇰🇷 KR | 9 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | La Aurora Airport |  | GT | 34 |
| 4 | El Dorado International Airport |  | CO | 32 |
| 5 | Guaymaral Airport |  | CO | 24 |
| 6 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 7 | Chicago O'Hare International Airport |  | US | 22 |
| 8 | Harry Reid International Airport |  | US | 21 |
| 9 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 10 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 11 | Miami International Airport |  | US | 17 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 16 |
| 13 | Los Angeles International Airport |  | US | 15 |
| 14 | Seattle-Tacoma International Airport |  | US | 15 |
| 15 | Salt Lake City International Airport |  | US | 15 |
| 16 | Ninoy Aquino International Airport |  | PH | 14 |
| 17 | Tampa International Airport |  | US | 14 |
| 18 | CO86 |  |  | 13 |
| 19 | The Florida Keys Marathon International Airport |  | US | 13 |
| 20 | Reno/Tahoe International Airport |  | US | 13 |
| 21 | Vancouver International Airport |  | CA | 13 |
| 22 | Tenerife Norte Airport |  | ES | 13 |
| 23 | Tokyo International Airport |  | JP | 13 |
| 24 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 25 | Daniel K Inouye International Airport |  | US | 12 |
| 26 | Yampa Valley Airport |  | US | 12 |
| 27 | Indira Gandhi International Airport |  | IN | 12 |
| 28 | Macau International Airport |  | MO | 12 |
| 29 | Centennial Airport |  | US | 12 |
| 30 | Rocky Mountain Metro Airport |  | US | 12 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 11 |
| 32 | Provo Municipal Airport |  | US | 11 |
| 33 | George Bush Intcntl/Houston Airport |  | US | 11 |
| 34 | Charlotte/Douglas International Airport |  | US | 10 |
| 35 | Wasig Airport |  | PH | 10 |
| 36 | Kuala Lumpur International Airport |  | MY | 10 |
| 37 | Albuquerque International Sunport Airport |  | US | 10 |
| 38 | Capua Airport |  | IT | 10 |
| 39 | Dallas Love Field |  | US | 10 |
| 40 | Nephi Municipal Airport |  | US | 10 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 9 | 23m | 225 km | 34.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 7 | 20m | 250 km | 30.2 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 8 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 9 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 10 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 4 | 29m | 275 km | 19.0 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 4 | 1h 40m | 1,423 km | 98.2 t |
| 13 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 14 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 15 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 17 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 18 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |
| 19 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 3 | 1h 50m | - | - |
| 20 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 3 | 1h 20m | 967 km | 50.0 t |
| 21 | Harry Reid International Airport (KLAS) | Baker & Hall Airport (77CL) | 3 | 35m | 364 km | 18.8 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 3 | 21m | 252 km | 13.0 t |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 3 | 55m | 723 km | 37.4 t |
| 24 | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 3 | 39m | 330 km | 17.1 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 3 | 30m | 369 km | 19.1 t |
| 26 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 3 | 52m | 645 km | 33.4 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 3 | 2h 3m | 1,652 km | 85.5 t |
| 28 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 3 | 29m | - | - |
| 29 | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 3 | 1h 1m | 177 km | 9.2 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 3 | 54m | 630 km | 32.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LT617 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | San Clemente Island Nalf Airport (KNUC) | 2026-03-29 04:40 UTC | 2026-03-29 06:19 UTC | 1h 38m |
| JA02NA |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-03-29 05:44 UTC | 2026-03-29 06:00 UTC | 15m |
| N496AE |  | Spirit Of St Louis Airport (KSUS) | Spirit Of St Louis Airport (KSUS) | 2026-03-29 05:19 UTC | 2026-03-29 05:49 UTC | 30m |
| N851MB |  | Greeley-Weld County Airport (KGXY) | Buckley Space Force Base Airport (KBKF) | 2026-03-29 05:12 UTC | 2026-03-29 05:36 UTC | 23m |
| WZZ9445 | Wizz Air | Larnaca International Airport (LCLK) | Gyumri Shirak Airport (UDSG) | 2026-03-29 03:28 UTC | 2026-03-29 05:34 UTC | 2h 5m |
| XSN82 | XSN | Marina Municipal Airport (KOAR) | San Carlos Airport (KSQL) | 2026-03-29 05:12 UTC | 2026-03-29 05:31 UTC | 18m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-03-29 05:04 UTC | 2026-03-29 05:29 UTC | 25m |
| XSN06 | XSN | Marina Municipal Airport (KOAR) | San Carlos Airport (KSQL) | 2026-03-29 05:10 UTC | 2026-03-29 05:28 UTC | 17m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-03-29 04:05 UTC | 2026-03-29 05:27 UTC | 1h 21m |
| UBG145 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-03-29 04:49 UTC | 2026-03-29 05:21 UTC | 31m |
| RXA2119 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-03-29 04:36 UTC | 2026-03-29 05:19 UTC | 43m |
| DLH9KX | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-03-29 04:34 UTC | 2026-03-29 05:19 UTC | 45m |
| BBC371 | BBC | VGZR (VGZR) | VE89 (VE89) | 2026-03-29 04:30 UTC | 2026-03-29 05:18 UTC | 48m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-03-29 04:41 UTC | 2026-03-29 05:18 UTC | 37m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 14:40 UTC | 2026-03-29 05:15 UTC | 14h 35m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-03-29 04:50 UTC | 2026-03-29 05:14 UTC | 23m |
| JST656 | JST | Brisbane International Airport (YBBN) | Braidwood Airport (YBAO) | 2026-03-29 04:02 UTC | 2026-03-29 05:14 UTC | 1h 11m |
| RYR53RZ | Ryanair | Václav Havel Airport (LKPR) | Otocac Airport (LDRO) | 2026-03-29 04:24 UTC | 2026-03-29 05:14 UTC | 50m |
| ESF612 | ESF | Miami International Airport (KMIA) | Atizapan De Zaragoza Airport (MMJC) | 2026-03-29 00:11 UTC | 2026-03-29 05:11 UTC | 4h 59m |
| CFH3 | CFH | YSMB (YSMB) | Sydney Bankstown Airport (YSBK) | 2026-03-29 04:51 UTC | 2026-03-29 05:10 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
