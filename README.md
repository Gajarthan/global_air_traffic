# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_13:42:51_UTC-green)

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

**Latest saved flight:** 2026-03-29 13:42:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 13:42:51 UTC

- **1,946** saved flights
- **1,550** unique routes
- **87** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,946** saved routes in the archive
- **1h 23m** average flight duration

### Carbon Footprint Estimate

- **27,395.0 tonnes** estimated CO2 emissions
- **1,588,119 km** total distance flown
- **948 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 66 |
| 3 | IndiGo | 60 |
| 4 | Southwest Airlines | 40 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | AXM | 32 |
| 8 | Lufthansa | 31 |
| 9 | ENY | 30 |
| 10 | United Airlines | 22 |
| 11 | All Nippon Airways | 20 |
| 12 | Delta Air Lines | 20 |
| 13 | Cathay Pacific | 19 |
| 14 | LATAM Airlines | 19 |
| 15 | Japan Airlines | 18 |
| 16 | Vueling | 18 |
| 17 | BRC | 17 |
| 18 | LXJ | 17 |
| 19 | SFR | 14 |
| 20 | Alaska Airlines | 13 |
| 21 | Avianca | 13 |
| 22 | AXB | 13 |
| 23 | QLK | 13 |
| 24 | Swiss International | 13 |
| 25 | APG | 12 |
| 26 | VOE | 12 |
| 27 | AEE | 11 |
| 28 | EDV | 11 |
| 29 | VIV | 11 |
| 30 | ARE | 10 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1600 |
| 2 | 🇮🇳 IN | 166 |
| 3 | 🇪🇸 ES | 143 |
| 4 | 🇯🇵 JP | 132 |
| 5 | 🇦🇺 AU | 121 |
| 6 | 🇨🇴 CO | 113 |
| 7 | 🇩🇪 DE | 94 |
| 8 | 🇮🇹 IT | 73 |
| 9 | 🇬🇧 GB | 72 |
| 10 | 🇿🇦 ZA | 70 |
| 11 | 🇨🇦 CA | 69 |
| 12 | 🇧🇷 BR | 69 |
| 13 | 🇲🇾 MY | 67 |
| 14 | 🇲🇽 MX | 65 |
| 15 | 🇵🇭 PH | 59 |
| 16 | 🇬🇹 GT | 59 |
| 17 | 🇫🇷 FR | 47 |
| 18 | 🇬🇷 GR | 44 |
| 19 | 🇨🇭 CH | 40 |
| 20 | 🇹🇭 TH | 38 |
| 21 | 🇹🇷 TR | 37 |
| 22 | 🇮🇩 ID | 31 |
| 23 | 🇳🇴 NO | 31 |
| 24 | 🇲🇴 MO | 28 |
| 25 | 🇵🇱 PL | 28 |
| 26 | 🇰🇷 KR | 26 |
| 27 | 🇫🇮 FI | 25 |
| 28 | 🇲🇦 MA | 23 |
| 29 | 🇳🇿 NZ | 22 |
| 30 | 🇲🇪 ME | 22 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Tokyo International Airport |  | JP | 44 |
| 2 | Dallas-Fort Worth International Airport |  | US | 42 |
| 3 | El Dorado International Airport |  | CO | 41 |
| 4 | La Aurora Airport |  | GT | 37 |
| 5 | Denver International Airport |  | US | 35 |
| 6 | Indira Gandhi International Airport |  | IN | 35 |
| 7 | Frankfurt am Main International Airport |  | DE | 35 |
| 8 | Macau International Airport |  | MO | 28 |
| 9 | Guaymaral Airport |  | CO | 28 |
| 10 | Tenerife Norte Airport |  | ES | 26 |
| 11 | Kuala Lumpur International Airport |  | MY | 26 |
| 12 | O. R. Tambo International Airport |  | ZA | 26 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 24 |
| 14 | Ninoy Aquino International Airport |  | PH | 24 |
| 15 | Chicago O'Hare International Airport |  | US | 23 |
| 16 | Zurich Airport |  | CH | 23 |
| 17 | Netaji Subhash Chandra Bose International Airport |  | IN | 22 |
| 18 | Harry Reid International Airport |  | US | 21 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 20 | Vitoria/Foronda Airport |  | ES | 19 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 18 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 24 | Miami International Airport |  | US | 17 |
| 25 | Zhuhai Airport |  | CN | 17 |
| 26 | Charles de Gaulle International Airport |  | FR | 17 |
| 27 | Bengaluru International Airport |  | IN | 17 |
| 28 | Wasig Airport |  | PH | 16 |
| 29 | Amsterdam Airport Schiphol |  | NL | 16 |
| 30 | Salt Lake City International Airport |  | US | 16 |
| 31 | Newcastle Airport |  | ZA | 16 |
| 32 | Los Angeles International Airport |  | US | 15 |
| 33 | Madrid Barajas International Airport |  | ES | 15 |
| 34 | Don Mueang International Airport |  | TH | 15 |
| 35 | Seattle-Tacoma International Airport |  | US | 15 |
| 36 | VGZR |  |  | 15 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 15 |
| 38 | Soekarno-Hatta International Airport |  | ID | 14 |
| 39 | Perales Airport |  | CO | 14 |
| 40 | Tampa International Airport |  | US | 14 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 14 | 14m | 114 km | 27.5 t |
| 3 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 11 | 25m | - | - |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 10 | 24m | 99 km | 17.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 9 | 29m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 8 | 30m | 275 km | 37.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 8 | 1h 40m | 1,423 km | 196.3 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 8 | 22m | 252 km | 34.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 6 | 22m | 165 km | 17.1 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 19 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 5 | 13m | 99 km | 8.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 5 | 2h 4m | 1,652 km | 142.5 t |
| 21 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 5 | 9h 6m | 38 km | 3.3 t |
| 22 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 23 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 4 | 1h 15m | 723 km | 49.9 t |
| 28 | Tokyo International Airport (RJTT) | Akeno Airport (RJOE) | 4 | 30m | 305 km | 21.0 t |
| 29 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 4 | 1h 10m | 770 km | 53.1 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 4 | 24m | 223 km | 15.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EXS82PX | EXS | Alicante International Airport (LEAL) | Durham Tees Valley Airport (EGNV) | 2026-03-29 10:30 UTC | 2026-03-29 13:42 UTC | 3h 12m |
| CPA807 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-03-28 22:21 UTC | 2026-03-29 13:37 UTC | 15h 15m |
| N3823X |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-03-29 13:23 UTC | 2026-03-29 13:30 UTC | 6m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-03-29 13:05 UTC | 2026-03-29 13:25 UTC | 20m |
| NHC47 | NHC | Wilhelmshaven-Mariensiel Airport (EDWI) | Wangerooge Airport (EDWG) | 2026-03-29 13:01 UTC | 2026-03-29 13:22 UTC | 20m |
| N212CP |  | Allegheny County Airport (KAGC) | Grant County Airport (KW99) | 2026-03-29 12:20 UTC | 2026-03-29 13:20 UTC | 59m |
| CXK1106 | CXK | Centennial Airport (KAPA) | Eads Municipal Airport (K9V7) | 2026-03-29 12:32 UTC | 2026-03-29 13:18 UTC | 45m |
| N14AN |  | Guthrie/Edmond Regional Airport (KGOK) | Barcus Field (95OK) | 2026-03-29 12:22 UTC | 2026-03-29 13:16 UTC | 53m |
| N70220 |  | Essex County Airport (KCDW) | Blairstown Airport (K1N7) | 2026-03-29 12:36 UTC | 2026-03-29 13:15 UTC | 39m |
| PSVTO | PSV | Campo de Marte Airport (SBMT) | Ubatuba Airport (SDUB) | 2026-03-29 12:44 UTC | 2026-03-29 13:04 UTC | 20m |
| AFR37PG | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-03-29 11:37 UTC | 2026-03-29 13:01 UTC | 1h 23m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-03-29 12:24 UTC | 2026-03-29 12:52 UTC | 27m |
| AXM6038 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-29 12:30 UTC | 2026-03-29 12:49 UTC | 19m |
| N621GZ |  | Redhead Airport (FD35) | Butler/Choctaw County Airport (K09A) | 2026-03-29 12:16 UTC | 2026-03-29 12:48 UTC | 31m |
| WIF1FY | WIF | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 2026-03-29 12:44 UTC | 2026-03-29 12:48 UTC | 4m |
| N101WJ |  | Erie International/Tom Ridge Field (KERI) | Roscommon County/Blodgett Memorial Airport (KHTL) | 2026-03-29 11:52 UTC | 2026-03-29 12:48 UTC | 55m |
| WIF5X | WIF | Bergen Airport Flesland (ENBR) | Haugesund Airport (ENHD) | 2026-03-29 12:30 UTC | 2026-03-29 12:46 UTC | 16m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Forsaeti Airport (BIFZ) | 2026-03-29 12:35 UTC | 2026-03-29 12:46 UTC | 10m |
| WIF5PH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-03-29 12:15 UTC | 2026-03-29 12:43 UTC | 27m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-03-29 12:15 UTC | 2026-03-29 12:42 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
