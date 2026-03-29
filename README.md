# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_21:11:31_UTC-green)

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

**Latest saved flight:** 2026-03-29 21:11:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 21:11:31 UTC

- **3,259** saved flights
- **2,473** unique routes
- **96** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,259** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **43,273.0 tonnes** estimated CO2 emissions
- **2,508,579 km** total distance flown
- **904 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 174 |
| 2 | Ryanair | 120 |
| 3 | IndiGo | 80 |
| 4 | EJA | 76 |
| 5 | American Airlines | 70 |
| 6 | Southwest Airlines | 62 |
| 7 | ENY | 55 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 37 |
| 11 | LXJ | 35 |
| 12 | Vueling | 35 |
| 13 | LATAM Airlines | 34 |
| 14 | United Airlines | 29 |
| 15 | Avianca | 24 |
| 16 | Cathay Pacific | 24 |
| 17 | VIV | 23 |
| 18 | Swiss International | 22 |
| 19 | WIF | 21 |
| 20 | All Nippon Airways | 20 |
| 21 | ARE | 19 |
| 22 | AXB | 19 |
| 23 | EDV | 19 |
| 24 | Alaska Airlines | 18 |
| 25 | Japan Airlines | 18 |
| 26 | VOE | 18 |
| 27 | AZU | 17 |
| 28 | BRC | 17 |
| 29 | MXY | 17 |
| 30 | AEE | 16 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2944 |
| 2 | 🇪🇸 ES | 263 |
| 3 | 🇮🇳 IN | 223 |
| 4 | 🇨🇴 CO | 205 |
| 5 | 🇩🇪 DE | 157 |
| 6 | 🇧🇷 BR | 149 |
| 7 | 🇨🇦 CA | 136 |
| 8 | 🇯🇵 JP | 134 |
| 9 | 🇮🇹 IT | 133 |
| 10 | 🇦🇺 AU | 130 |
| 11 | 🇲🇽 MX | 122 |
| 12 | 🇬🇧 GB | 119 |
| 13 | 🇬🇹 GT | 93 |
| 14 | 🇫🇷 FR | 91 |
| 15 | 🇿🇦 ZA | 84 |
| 16 | 🇲🇾 MY | 81 |
| 17 | 🇨🇭 CH | 74 |
| 18 | 🇳🇴 NO | 67 |
| 19 | 🇬🇷 GR | 66 |
| 20 | 🇵🇭 PH | 63 |
| 21 | 🇹🇷 TR | 48 |
| 22 | 🇹🇭 TH | 45 |
| 23 | 🇵🇱 PL | 42 |
| 24 | 🇧🇸 BS | 42 |
| 25 | 🇲🇦 MA | 39 |
| 26 | 🇫🇮 FI | 38 |
| 27 | 🇮🇩 ID | 37 |
| 28 | 🇲🇴 MO | 36 |
| 29 | 🇳🇿 NZ | 34 |
| 30 | 🇳🇱 NL | 31 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 88 |
| 2 | El Dorado International Airport |  | CO | 72 |
| 3 | Denver International Airport |  | US | 66 |
| 4 | La Aurora Airport |  | GT | 60 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 54 |
| 7 | Indira Gandhi International Airport |  | IN | 50 |
| 8 | Tenerife Norte Airport |  | ES | 46 |
| 9 | Tokyo International Airport |  | JP | 44 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 43 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 42 |
| 12 | Harry Reid International Airport |  | US | 40 |
| 13 | Chicago O'Hare International Airport |  | US | 37 |
| 14 | Zurich Airport |  | CH | 37 |
| 15 | Macau International Airport |  | MO | 36 |
| 16 | Kuala Lumpur International Airport |  | MY | 33 |
| 17 | Charlotte/Douglas International Airport |  | US | 32 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 31 |
| 19 | Miami International Airport |  | US | 30 |
| 20 | O. R. Tambo International Airport |  | ZA | 30 |
| 21 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 22 | Reno/Tahoe International Airport |  | US | 28 |
| 23 | Madrid Barajas International Airport |  | ES | 28 |
| 24 | Salt Lake City International Airport |  | US | 28 |
| 25 | Vitoria/Foronda Airport |  | ES | 27 |
| 26 | Ninoy Aquino International Airport |  | PH | 26 |
| 27 | CO86 |  |  | 25 |
| 28 | George Bush Intcntl/Houston Airport |  | US | 25 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 25 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 25 |
| 32 | Amsterdam Airport Schiphol |  | NL | 24 |
| 33 | Los Angeles International Airport |  | US | 23 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 23 |
| 35 | Charles de Gaulle International Airport |  | FR | 23 |
| 36 | Bengaluru International Airport |  | IN | 23 |
| 37 | Perales Airport |  | CO | 23 |
| 38 | Centennial Airport |  | US | 23 |
| 39 | VGZR |  |  | 21 |
| 40 | Tampa International Airport |  | US | 21 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 23 | 14m | 114 km | 45.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 15 | 26m | 99 km | 25.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 10 | 14m | 206 km | 35.6 t |
| 10 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 10 | 30m | 69 km | 12.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 17 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 8 | 1h 55m | 1,304 km | 180.0 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 21 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 23 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 6 | 1h 49m | - | - |
| 24 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 25 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 26 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 6 | 52m | 645 km | 66.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 29 | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 6 | 16h 7m | 12,992 km | 1,344.6 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA640 | Cathay Pacific | Biratnagar Airport (VNVT) | Macau International Airport (VMMC) | 2026-03-29 18:09 UTC | 2026-03-29 21:11 UTC | 3h 1m |
| UAE9964 | Emirates | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-03-28 21:14 UTC | 2026-03-29 21:02 UTC | 23h 48m |
| N71JT |  | Rosenberg Airport (MY80) | Estherville Municipal Airport (KEST) | 2026-03-29 20:40 UTC | 2026-03-29 21:00 UTC | 19m |
| N123DT |  | Morgan County Airport (K42U) | Morgan County Airport (K42U) | 2026-03-29 20:04 UTC | 2026-03-29 20:58 UTC | 53m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-29 06:08 UTC | 2026-03-29 20:56 UTC | 14h 47m |
| CPA085 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-29 05:50 UTC | 2026-03-29 20:54 UTC | 15h 3m |
| CFYUL | CFY | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-03-29 20:36 UTC | 2026-03-29 20:53 UTC | 17m |
| N953PC |  | Boise Air Trml/Gowen Field (KBOI) | Flournoy Valley Airport (95OR) | 2026-03-29 19:50 UTC | 2026-03-29 20:53 UTC | 1h 3m |
| N425FP |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-03-29 19:54 UTC | 2026-03-29 20:51 UTC | 56m |
| N265LD |  | Long Beach (Daugherty Field) Airport (KLGB) | Fullerton Municipal Airport (KFUL) | 2026-03-29 20:40 UTC | 2026-03-29 20:50 UTC | 10m |
| N759RV |  | Sahoma Lake Airport (03OK) | 19OK (19OK) | 2026-03-29 19:55 UTC | 2026-03-29 20:49 UTC | 53m |
| EJA241 | EJA | Monterey Regional Airport (KMRY) | K4SD (K4SD) | 2026-03-29 20:08 UTC | 2026-03-29 20:42 UTC | 33m |
| MNL14 | MNL | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-03-29 20:04 UTC | 2026-03-29 20:41 UTC | 36m |
| N627KW |  | Mc Clellan-Palomar Airport (KCRQ) | Lee Gilmer Memorial Airport (KGVL) | 2026-03-29 19:30 UTC | 2026-03-29 20:35 UTC | 1h 4m |
| N750CD |  | Easterwood Field (KCLL) | Locker Brothers Airport (1TE0) | 2026-03-29 18:04 UTC | 2026-03-29 20:33 UTC | 2h 29m |
| N6102P |  | Thomasville Regional Airport (KTVI) | Thomasville Regional Airport (KTVI) | 2026-03-29 20:07 UTC | 2026-03-29 20:32 UTC | 25m |
| N4892S |  | J R's Airport (66FD) | Lake Wales Municipal Airport (KX07) | 2026-03-29 19:46 UTC | 2026-03-29 20:32 UTC | 46m |
| N29WN |  | Peter O Knight Airport (KTPF) | Peter O Knight Airport (KTPF) | 2026-03-29 20:15 UTC | 2026-03-29 20:31 UTC | 15m |
| RYR18MQ | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Gioia Del Colle Airport (LIBV) | 2026-03-29 19:43 UTC | 2026-03-29 20:31 UTC | 47m |
| N977MR |  | Stephenville Clark Regional Airport (KSEP) | Esenada Airport (NM48) | 2026-03-29 19:08 UTC | 2026-03-29 20:30 UTC | 1h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
