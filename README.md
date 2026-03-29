# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_12:23:37_UTC-green)

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

**Latest saved flight:** 2026-03-29 12:23:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 12:23:37 UTC

- **1,862** saved flights
- **1,493** unique routes
- **86** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,862** saved routes in the archive
- **1h 23m** average flight duration

### Carbon Footprint Estimate

- **26,312.0 tonnes** estimated CO2 emissions
- **1,525,334 km** total distance flown
- **950 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 60 |
| 3 | IndiGo | 57 |
| 4 | Southwest Airlines | 40 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | AXM | 30 |
| 8 | Lufthansa | 30 |
| 9 | ENY | 30 |
| 10 | United Airlines | 22 |
| 11 | All Nippon Airways | 20 |
| 12 | Delta Air Lines | 20 |
| 13 | Cathay Pacific | 18 |
| 14 | Japan Airlines | 18 |
| 15 | Vueling | 18 |
| 16 | BRC | 17 |
| 17 | LXJ | 17 |
| 18 | LATAM Airlines | 16 |
| 19 | SFR | 14 |
| 20 | Alaska Airlines | 13 |
| 21 | AXB | 13 |
| 22 | QLK | 13 |
| 23 | Avianca | 12 |
| 24 | Swiss International | 12 |
| 25 | APG | 11 |
| 26 | EDV | 11 |
| 27 | VIV | 11 |
| 28 | VOE | 11 |
| 29 | AEE | 10 |
| 30 | Finnair | 10 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1577 |
| 2 | 🇮🇳 IN | 157 |
| 3 | 🇪🇸 ES | 133 |
| 4 | 🇯🇵 JP | 132 |
| 5 | 🇦🇺 AU | 121 |
| 6 | 🇨🇴 CO | 95 |
| 7 | 🇩🇪 DE | 87 |
| 8 | 🇨🇦 CA | 69 |
| 9 | 🇮🇹 IT | 69 |
| 10 | 🇬🇧 GB | 68 |
| 11 | 🇿🇦 ZA | 66 |
| 12 | 🇲🇽 MX | 65 |
| 13 | 🇲🇾 MY | 63 |
| 14 | 🇧🇷 BR | 59 |
| 15 | 🇵🇭 PH | 57 |
| 16 | 🇬🇹 GT | 55 |
| 17 | 🇬🇷 GR | 43 |
| 18 | 🇫🇷 FR | 43 |
| 19 | 🇹🇭 TH | 38 |
| 20 | 🇨🇭 CH | 37 |
| 21 | 🇹🇷 TR | 32 |
| 22 | 🇮🇩 ID | 31 |
| 23 | 🇲🇴 MO | 27 |
| 24 | 🇵🇱 PL | 27 |
| 25 | 🇰🇷 KR | 26 |
| 26 | 🇫🇮 FI | 23 |
| 27 | 🇲🇦 MA | 22 |
| 28 | 🇳🇿 NZ | 22 |
| 29 | 🇲🇪 ME | 20 |
| 30 | 🇳🇴 NO | 19 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Tokyo International Airport |  | JP | 44 |
| 2 | Dallas-Fort Worth International Airport |  | US | 42 |
| 3 | Denver International Airport |  | US | 35 |
| 4 | Indira Gandhi International Airport |  | IN | 35 |
| 5 | El Dorado International Airport |  | CO | 34 |
| 6 | Frankfurt am Main International Airport |  | DE | 34 |
| 7 | La Aurora Airport |  | GT | 34 |
| 8 | Macau International Airport |  | MO | 27 |
| 9 | Tenerife Norte Airport |  | ES | 25 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 24 |
| 11 | Guaymaral Airport |  | CO | 24 |
| 12 | Kuala Lumpur International Airport |  | MY | 24 |
| 13 | O. R. Tambo International Airport |  | ZA | 24 |
| 14 | Ninoy Aquino International Airport |  | PH | 23 |
| 15 | Chicago O'Hare International Airport |  | US | 22 |
| 16 | Netaji Subhash Chandra Bose International Airport |  | IN | 22 |
| 17 | Harry Reid International Airport |  | US | 21 |
| 18 | Zurich Airport |  | CH | 20 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 21 | Eleftherios Venizelos International Airport |  | GR | 18 |
| 22 | Vitoria/Foronda Airport |  | ES | 18 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 24 | Miami International Airport |  | US | 17 |
| 25 | Zhuhai Airport |  | CN | 17 |
| 26 | Charles de Gaulle International Airport |  | FR | 16 |
| 27 | Bengaluru International Airport |  | IN | 16 |
| 28 | Wasig Airport |  | PH | 16 |
| 29 | Salt Lake City International Airport |  | US | 16 |
| 30 | Los Angeles International Airport |  | US | 15 |
| 31 | Don Mueang International Airport |  | TH | 15 |
| 32 | Seattle-Tacoma International Airport |  | US | 15 |
| 33 | Amsterdam Airport Schiphol |  | NL | 15 |
| 34 | Newcastle Airport |  | ZA | 15 |
| 35 | Soekarno-Hatta International Airport |  | ID | 14 |
| 36 | Tampa International Airport |  | US | 14 |
| 37 | CO86 |  |  | 13 |
| 38 | The Florida Keys Marathon International Airport |  | US | 13 |
| 39 | Reno/Tahoe International Airport |  | US | 13 |
| 40 | Vancouver International Airport |  | CA | 13 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 12 | 20m | 250 km | 51.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 9 | 29m | - | - |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 8 | 30m | 275 km | 37.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 8 | 1h 40m | 1,423 km | 196.3 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 8 | 22m | 252 km | 34.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 5 | 22m | 165 km | 14.2 t |
| 19 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 5 | 9h 6m | 38 km | 3.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 21 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 22 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |
| 25 | Tokyo International Airport (RJTT) | Akeno Airport (RJOE) | 4 | 30m | 305 km | 21.0 t |
| 26 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 4 | 1h 10m | 770 km | 53.1 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 28 | Diosdado Macapagal International Airport (RPLC) | Mamburao Airport (RPUM) | 4 | 32m | 220 km | 15.2 t |
| 29 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 4 | 1h 43m | 1,290 km | 89.0 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LEJ110 | LEJ | Linate Airport (LIML) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-29 10:19 UTC | 2026-03-29 12:23 UTC | 2h 4m |
| SAS1665 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Nittenau-Bruck Airport (EDNM) | 2026-03-29 11:03 UTC | 2026-03-29 12:23 UTC | 1h 19m |
| N20ER |  | K9A1 (K9A1) | K38J (K38J) | 2026-03-29 11:34 UTC | 2026-03-29 12:21 UTC | 47m |
| AXB1996 | AXB | Agartala Airport (VEAT) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-29 11:30 UTC | 2026-03-29 12:19 UTC | 49m |
| EAU404 | EAU | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-03-28 20:23 UTC | 2026-03-29 12:18 UTC | 15h 55m |
| AFL1459 | AFL | Spichenkovo Airport (UNWW) | Sheremetyevo International Airport (UUEE) | 2026-03-29 07:43 UTC | 2026-03-29 12:17 UTC | 4h 33m |
| HK4276 |  | Madrid Air Base (SKMA) | Madrid Air Base (SKMA) | 2026-03-29 12:00 UTC | 2026-03-29 12:17 UTC | 16m |
| N252EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 11:19 UTC | 2026-03-29 12:14 UTC | 54m |
| CPA331 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-29 04:26 UTC | 2026-03-29 12:13 UTC | 7h 47m |
| FDR334 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-03-29 11:40 UTC | 2026-03-29 12:11 UTC | 31m |
| N490LP |  | Glendale Regional Airport (KGEU) | Bagdad Airport (KE51) | 2026-03-29 10:57 UTC | 2026-03-29 12:09 UTC | 1h 12m |
| EWG6ND | EWG | Ibiza Airport (LEIB) | Hamburg Airport (EDDH) | 2026-03-29 09:29 UTC | 2026-03-29 12:08 UTC | 2h 38m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-03-29 11:24 UTC | 2026-03-29 12:08 UTC | 43m |
| PSGVA | PSG | Fazenda Monte Alegre Airport (SWGQ) | Fazenda Santa Rita de Cassia Airport (SWEZ) | 2026-03-29 11:49 UTC | 2026-03-29 12:07 UTC | 18m |
| KENLEY | KEN | London Biggin Hill Airport (EGKB) | London Biggin Hill Airport (EGKB) | 2026-03-29 12:04 UTC | 2026-03-29 12:07 UTC | 2m |
| RYR6743 | Ryanair | Ibn Batouta Airport (GMTT) | Angads Airport (GMFO) | 2026-03-29 11:34 UTC | 2026-03-29 12:06 UTC | 31m |
| RYR3615 | Ryanair | Brussels South Charleroi Airport (EBCI) | Visoko Sport Airfield (LQVI) | 2026-03-29 10:30 UTC | 2026-03-29 12:05 UTC | 1h 35m |
| N960JB |  | Toussus-le-Noble Airport (LFPN) | Perugia / San Egidio Airport (LIRZ) | 2026-03-29 10:10 UTC | 2026-03-29 12:05 UTC | 1h 54m |
| N247EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 11:11 UTC | 2026-03-29 12:04 UTC | 52m |
| HKC9488 | HKC | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-03-29 00:13 UTC | 2026-03-29 12:01 UTC | 11h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
