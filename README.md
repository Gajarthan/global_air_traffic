# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_20:35:20_UTC-green)

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

**Latest saved flight:** 2026-03-29 20:35:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 20:35:20 UTC

- **3,166** saved flights
- **2,407** unique routes
- **95** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,166** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **41,772.8 tonnes** estimated CO2 emissions
- **2,421,613 km** total distance flown
- **898 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 168 |
| 2 | Ryanair | 117 |
| 3 | IndiGo | 80 |
| 4 | EJA | 73 |
| 5 | American Airlines | 64 |
| 6 | Southwest Airlines | 60 |
| 7 | ENY | 54 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 38 |
| 10 | Delta Air Lines | 37 |
| 11 | LXJ | 34 |
| 12 | Vueling | 32 |
| 13 | LATAM Airlines | 29 |
| 14 | United Airlines | 28 |
| 15 | Avianca | 24 |
| 16 | VIV | 23 |
| 17 | Swiss International | 22 |
| 18 | Cathay Pacific | 21 |
| 19 | WIF | 21 |
| 20 | All Nippon Airways | 20 |
| 21 | ARE | 19 |
| 22 | AXB | 19 |
| 23 | EDV | 19 |
| 24 | Japan Airlines | 18 |
| 25 | Alaska Airlines | 17 |
| 26 | BRC | 17 |
| 27 | VOE | 17 |
| 28 | AEE | 16 |
| 29 | AZU | 16 |
| 30 | JetBlue | 16 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 2834 |
| 2 | 🇪🇸 ES | 254 |
| 3 | 🇮🇳 IN | 223 |
| 4 | 🇨🇴 CO | 201 |
| 5 | 🇩🇪 DE | 157 |
| 6 | 🇨🇦 CA | 134 |
| 7 | 🇧🇷 BR | 133 |
| 8 | 🇯🇵 JP | 132 |
| 9 | 🇮🇹 IT | 130 |
| 10 | 🇦🇺 AU | 126 |
| 11 | 🇲🇽 MX | 118 |
| 12 | 🇬🇧 GB | 118 |
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
| 24 | 🇧🇸 BS | 41 |
| 25 | 🇫🇮 FI | 38 |
| 26 | 🇲🇦 MA | 38 |
| 27 | 🇮🇩 ID | 37 |
| 28 | 🇲🇴 MO | 32 |
| 29 | 🇳🇱 NL | 30 |
| 30 | 🇳🇿 NZ | 28 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 82 |
| 2 | El Dorado International Airport |  | CO | 70 |
| 3 | Denver International Airport |  | US | 65 |
| 4 | La Aurora Airport |  | GT | 60 |
| 5 | Frankfurt am Main International Airport |  | DE | 55 |
| 6 | Guaymaral Airport |  | CO | 53 |
| 7 | Indira Gandhi International Airport |  | IN | 50 |
| 8 | Tenerife Norte Airport |  | ES | 45 |
| 9 | Tokyo International Airport |  | JP | 44 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 42 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 41 |
| 12 | Harry Reid International Airport |  | US | 39 |
| 13 | Chicago O'Hare International Airport |  | US | 37 |
| 14 | Zurich Airport |  | CH | 37 |
| 15 | Kuala Lumpur International Airport |  | MY | 33 |
| 16 | Macau International Airport |  | MO | 32 |
| 17 | Atizapan De Zaragoza Airport |  | MX | 31 |
| 18 | Charlotte/Douglas International Airport |  | US | 30 |
| 19 | O. R. Tambo International Airport |  | ZA | 30 |
| 20 | Eleftherios Venizelos International Airport |  | GR | 28 |
| 21 | Reno/Tahoe International Airport |  | US | 28 |
| 22 | Madrid Barajas International Airport |  | ES | 28 |
| 23 | Salt Lake City International Airport |  | US | 28 |
| 24 | Miami International Airport |  | US | 27 |
| 25 | Vitoria/Foronda Airport |  | ES | 27 |
| 26 | Ninoy Aquino International Airport |  | PH | 26 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 25 |
| 28 | Amsterdam Airport Schiphol |  | NL | 24 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 24 |
| 30 | Los Angeles International Airport |  | US | 23 |
| 31 | CO86 |  |  | 23 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 23 |
| 33 | Charles de Gaulle International Airport |  | FR | 23 |
| 34 | Bengaluru International Airport |  | IN | 23 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 23 |
| 36 | Centennial Airport |  | US | 23 |
| 37 | Perales Airport |  | CO | 22 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 22 |
| 39 | VGZR |  |  | 21 |
| 40 | Sydney Kingsford Smith International Airport |  | AU | 20 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 22 | 14m | 114 km | 43.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 15 | 26m | 99 km | 25.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 11 | 1h 39m | 1,423 km | 270.0 t |
| 9 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 10 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 10 | 30m | 69 km | 12.0 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 9 | 15m | 206 km | 32.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 13 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 8 | 22m | 165 km | 22.8 t |
| 16 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 8 | 1h 55m | 1,304 km | 180.0 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 7 | 1h 44m | 1,290 km | 155.8 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 7 | 18m | 55 km | 6.7 t |
| 22 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 7 | 12m | - | - |
| 23 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 6 | 1h 19m | 967 km | 100.1 t |
| 24 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 25 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 6 | 52m | 645 km | 66.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 29 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 6 | 54m | 630 km | 65.2 t |
| 30 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N627KW |  | Mc Clellan-Palomar Airport (KCRQ) | Lee Gilmer Memorial Airport (KGVL) | 2026-03-29 19:30 UTC | 2026-03-29 20:35 UTC | 1h 4m |
| N6102P |  | Thomasville Regional Airport (KTVI) | Thomasville Regional Airport (KTVI) | 2026-03-29 20:07 UTC | 2026-03-29 20:32 UTC | 25m |
| CGVLF | CGV | Arnprior Airport (CNP3) | Smiths Falls-Montague (Russ Beach) Airport (CYSH) | 2026-03-29 20:03 UTC | 2026-03-29 20:22 UTC | 19m |
| N682AC |  | Hidden Valley Ranch Airport (TS90) | Bb Airpark (TE88) | 2026-03-29 20:01 UTC | 2026-03-29 20:16 UTC | 14m |
| N8180C |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-03-29 20:00 UTC | 2026-03-29 20:11 UTC | 10m |
| N513SK |  | Palm Springs International Airport (KPSP) | Teterboro Airport (KTEB) | 2026-03-29 15:48 UTC | 2026-03-29 20:10 UTC | 4h 22m |
| N48500 |  | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-03-29 19:35 UTC | 2026-03-29 20:08 UTC | 32m |
| N330LD |  | Chippewa Valley Regional Airport (KEAU) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-03-29 18:54 UTC | 2026-03-29 20:08 UTC | 1h 13m |
| N365PC |  | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-03-29 19:16 UTC | 2026-03-29 20:05 UTC | 49m |
| N555GP |  | Roscoe Turner Airport (KCRX) | Addison-Henley Field (0MS7) | 2026-03-29 19:48 UTC | 2026-03-29 20:04 UTC | 16m |
| N511CR |  | Stockton Metro Airport (KSCK) | Fresno Chandler Executive Airport (KFCH) | 2026-03-29 19:43 UTC | 2026-03-29 20:04 UTC | 21m |
| N39CD |  | K5T6 (K5T6) | Deming Municipal Airport (KDMN) | 2026-03-29 19:26 UTC | 2026-03-29 20:03 UTC | 36m |
| N65295 |  | Somerset County Airport (K2G9) | 2PN4 (2PN4) | 2026-03-29 19:49 UTC | 2026-03-29 20:02 UTC | 12m |
| N1464C |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-03-29 19:37 UTC | 2026-03-29 20:01 UTC | 23m |
| N496SP |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-03-29 19:49 UTC | 2026-03-29 20:00 UTC | 11m |
| N8876X |  | Salt Lake City International Airport (KSLC) | Wendover Airport (KENV) | 2026-03-29 19:18 UTC | 2026-03-29 20:00 UTC | 42m |
| N9259S |  | Greeley-Weld County Airport (KGXY) | Laramie Regional Airport (KLAR) | 2026-03-29 19:19 UTC | 2026-03-29 19:55 UTC | 35m |
| N40LB |  | Joe Foss Field (KFSD) | Waynesboro Municipal Airport (K2R0) | 2026-03-29 18:07 UTC | 2026-03-29 19:54 UTC | 1h 47m |
| N291ME |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-03-29 19:11 UTC | 2026-03-29 19:54 UTC | 42m |
| TRP1 | TRP | Forest Hill Airport (MD31) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-03-29 19:43 UTC | 2026-03-29 19:53 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
