# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_17:19:07_UTC-green)

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

**Latest saved flight:** 2026-04-01 17:19:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 17:19:07 UTC

- **9,188** saved flights
- **5,566** unique routes
- **109** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,188** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **111,264.1 tonnes** estimated CO2 emissions
- **6,450,090 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 407 |
| 2 | Ryanair | 353 |
| 3 | IndiGo | 259 |
| 4 | EJA | 183 |
| 5 | American Airlines | 161 |
| 6 | Lufthansa | 159 |
| 7 | Southwest Airlines | 138 |
| 8 | ENY | 126 |
| 9 | AXM | 102 |
| 10 | Vueling | 102 |
| 11 | LATAM Airlines | 90 |
| 12 | LXJ | 84 |
| 13 | All Nippon Airways | 79 |
| 14 | WIF | 76 |
| 15 | Delta Air Lines | 74 |
| 16 | Swiss International | 71 |
| 17 | QLK | 70 |
| 18 | AXB | 62 |
| 19 | VIV | 62 |
| 20 | AZU | 61 |
| 21 | Japan Airlines | 60 |
| 22 | Alaska Airlines | 56 |
| 23 | BRC | 55 |
| 24 | EDV | 55 |
| 25 | United Airlines | 55 |
| 26 | EJU | 53 |
| 27 | easyJet | 52 |
| 28 | Avianca | 50 |
| 29 | Cathay Pacific | 49 |
| 30 | AEE | 47 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 7511 |
| 2 | 🇮🇳 IN | 795 |
| 3 | 🇪🇸 ES | 725 |
| 4 | 🇦🇺 AU | 696 |
| 5 | 🇩🇪 DE | 511 |
| 6 | 🇯🇵 JP | 461 |
| 7 | 🇧🇷 BR | 455 |
| 8 | 🇨🇴 CO | 439 |
| 9 | 🇨🇦 CA | 438 |
| 10 | 🇮🇹 IT | 410 |
| 11 | 🇬🇧 GB | 330 |
| 12 | 🇲🇽 MX | 320 |
| 13 | 🇫🇷 FR | 289 |
| 14 | 🇳🇴 NO | 248 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 218 |
| 17 | 🇨🇭 CH | 217 |
| 18 | 🇿🇦 ZA | 199 |
| 19 | 🇳🇿 NZ | 197 |
| 20 | 🇬🇹 GT | 187 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇰🇷 KR | 157 |
| 23 | 🇹🇷 TR | 154 |
| 24 | 🇵🇱 PL | 124 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇹🇭 TH | 112 |
| 27 | 🇲🇦 MA | 108 |
| 28 | 🇲🇴 MO | 92 |
| 29 | 🇳🇱 NL | 87 |
| 30 | 🇲🇪 ME | 85 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 214 |
| 2 | Indira Gandhi International Airport |  | IN | 175 |
| 3 | Tokyo International Airport |  | JP | 165 |
| 4 | Frankfurt am Main International Airport |  | DE | 162 |
| 5 | Denver International Airport |  | US | 161 |
| 6 | El Dorado International Airport |  | CO | 142 |
| 7 | La Aurora Airport |  | GT | 132 |
| 8 | Harry Reid International Airport |  | US | 125 |
| 9 | Guaymaral Airport |  | CO | 123 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 110 |
| 11 | Zurich Airport |  | CH | 108 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 105 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 92 |
| 15 | Chicago O'Hare International Airport |  | US | 92 |
| 16 | Macau International Airport |  | MO | 92 |
| 17 | Tenerife Norte Airport |  | ES | 90 |
| 18 | Bengaluru International Airport |  | IN | 85 |
| 19 | Kuala Lumpur International Airport |  | MY | 85 |
| 20 | Madrid Barajas International Airport |  | ES | 82 |
| 21 | Reno/Tahoe International Airport |  | US | 80 |
| 22 | Charlotte/Douglas International Airport |  | US | 79 |
| 23 | Ninoy Aquino International Airport |  | PH | 78 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 74 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 72 |
| 26 | Malpensa International Airport |  | IT | 70 |
| 27 | Daniel K Inouye International Airport |  | US | 67 |
| 28 | Vitoria/Foronda Airport |  | ES | 67 |
| 29 | Pune Airport |  | IN | 66 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 66 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 66 |
| 32 | Barcelona International Airport |  | ES | 65 |
| 33 | Salt Lake City International Airport |  | US | 65 |
| 34 | Charles de Gaulle International Airport |  | FR | 64 |
| 35 | Congonhas Airport |  | BR | 64 |
| 36 | Seattle-Tacoma International Airport |  | US | 61 |
| 37 | Miami International Airport |  | US | 60 |
| 38 | Gimpo International Airport |  | KR | 60 |
| 39 | Bodø Airport |  | NO | 58 |
| 40 | O. R. Tambo International Airport |  | ZA | 57 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 49 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 40 | 14m | 114 km | 78.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 29 | 1h 45m | 1,156 km | 578.5 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 27 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 26 | 27m | 152 km | 67.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 25 | 23m | 99 km | 42.8 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 24 | 15m | 206 km | 85.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 22 | 1h 42m | 1,423 km | 539.9 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 22 | 52m | 556 km | 210.9 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 21 | 28m | 275 km | 99.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 18 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 21 | 9m | - | - |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 20 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 18 | 1h 1m | 723 km | 224.4 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 27 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 15 | 1h 56m | 1,304 km | 337.5 t |
| 29 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 14 | 34m | 431 km | 104.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2529X |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-04-01 16:49 UTC | 2026-04-01 17:19 UTC | 29m |
| N9562Q |  | Caldwell Executive Airport (KEUL) | Lanham Field (04ID) | 2026-04-01 16:51 UTC | 2026-04-01 17:13 UTC | 21m |
| N73054 |  | Felts Field (KSFF) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-04-01 16:59 UTC | 2026-04-01 17:12 UTC | 13m |
| N697JB |  | Caldwell Executive Airport (KEUL) | Caldwell Executive Airport (KEUL) | 2026-04-01 16:58 UTC | 2026-04-01 17:09 UTC | 10m |
| N135CG |  | San Antonio International Airport (KSAT) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-04-01 14:35 UTC | 2026-04-01 17:08 UTC | 2h 32m |
| N67490 |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-04-01 15:59 UTC | 2026-04-01 17:05 UTC | 1h 6m |
| FUSION91 | FUS | Hughes Ranch Airport (50XS) | Maverick County Memorial International Airport (K5T9) | 2026-04-01 16:51 UTC | 2026-04-01 17:02 UTC | 10m |
| LS16 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 15:56 UTC | 2026-04-01 17:00 UTC | 1h 4m |
| 00000000 |  | Tucson International Airport (KTUS) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-01 15:53 UTC | 2026-04-01 17:00 UTC | 1h 7m |
| N374BL |  | Winter Haven Regional Airport (KGIF) | Lake Wales Municipal Airport (KX07) | 2026-04-01 16:18 UTC | 2026-04-01 16:57 UTC | 39m |
| OEGFB | OEG | Brussels Airport (EBBR) | Leipzig Halle Airport (EDDP) | 2026-04-01 15:50 UTC | 2026-04-01 16:53 UTC | 1h 3m |
| GJADN | GJA | Fife Airport (EGPJ) | Cranfield Airport (EGTC) | 2026-04-01 15:46 UTC | 2026-04-01 16:51 UTC | 1h 5m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-01 16:34 UTC | 2026-04-01 16:50 UTC | 16m |
| N33SF |  | Raleigh Regional At Person County Airport (KTDF) | Raleigh Regional At Person County Airport (KTDF) | 2026-04-01 16:49 UTC | 2026-04-01 16:50 UTC | 0m |
| MATTI | MAT | Václav Havel Airport (LKPR) | Raron Airport (LSTA) | 2026-04-01 15:23 UTC | 2026-04-01 16:50 UTC | 1h 26m |
| HK5178G |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-04-01 16:32 UTC | 2026-04-01 16:48 UTC | 16m |
| N421P |  | Scottsdale Airport (KSDL) | Gene Wash Reservoir Airport (5CL7) | 2026-04-01 15:57 UTC | 2026-04-01 16:40 UTC | 43m |
| CXK456 | CXK | Wright Army Air Field (Fort Stewart)/Midcoast Regional Airport (KLHW) | 9GA2 (9GA2) | 2026-04-01 16:14 UTC | 2026-04-01 16:39 UTC | 25m |
| FFL8109 | FFL | Teterboro Airport (KTEB) | Green Bank Observatory Airport (WV52) | 2026-04-01 15:42 UTC | 2026-04-01 16:38 UTC | 56m |
| TGSED | TGS | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-01 16:33 UTC | 2026-04-01 16:37 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
