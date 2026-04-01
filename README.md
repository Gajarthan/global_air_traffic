# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_21:01:42_UTC-green)

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

**Latest saved flight:** 2026-04-01 21:01:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 21:01:42 UTC

- **9,742** saved flights
- **5,842** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,742** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **117,681.5 tonnes** estimated CO2 emissions
- **6,822,118 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 446 |
| 2 | Ryanair | 378 |
| 3 | IndiGo | 263 |
| 4 | EJA | 206 |
| 5 | American Airlines | 181 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 148 |
| 8 | ENY | 135 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 99 |
| 12 | LXJ | 95 |
| 13 | All Nippon Airways | 80 |
| 14 | WIF | 79 |
| 15 | Delta Air Lines | 77 |
| 16 | Swiss International | 73 |
| 17 | QLK | 70 |
| 18 | AZU | 67 |
| 19 | VIV | 66 |
| 20 | AXB | 63 |
| 21 | Alaska Airlines | 60 |
| 22 | EDV | 60 |
| 23 | Japan Airlines | 60 |
| 24 | United Airlines | 60 |
| 25 | BRC | 58 |
| 26 | easyJet | 56 |
| 27 | EJU | 55 |
| 28 | Avianca | 53 |
| 29 | AEE | 50 |
| 30 | Cathay Pacific | 50 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8111 |
| 2 | 🇮🇳 IN | 807 |
| 3 | 🇪🇸 ES | 761 |
| 4 | 🇦🇺 AU | 698 |
| 5 | 🇩🇪 DE | 525 |
| 6 | 🇧🇷 BR | 498 |
| 7 | 🇨🇴 CO | 484 |
| 8 | 🇨🇦 CA | 467 |
| 9 | 🇯🇵 JP | 463 |
| 10 | 🇮🇹 IT | 434 |
| 11 | 🇬🇧 GB | 349 |
| 12 | 🇲🇽 MX | 342 |
| 13 | 🇫🇷 FR | 300 |
| 14 | 🇳🇴 NO | 259 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 226 |
| 17 | 🇨🇭 CH | 225 |
| 18 | 🇳🇿 NZ | 211 |
| 19 | 🇿🇦 ZA | 203 |
| 20 | 🇬🇹 GT | 202 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇹🇷 TR | 159 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 115 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇪 ME | 96 |
| 29 | 🇲🇴 MO | 95 |
| 30 | 🇧🇸 BS | 94 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 240 |
| 2 | Indira Gandhi International Airport |  | IN | 177 |
| 3 | Denver International Airport |  | US | 173 |
| 4 | Tokyo International Airport |  | JP | 166 |
| 5 | Frankfurt am Main International Airport |  | DE | 166 |
| 6 | El Dorado International Airport |  | CO | 155 |
| 7 | La Aurora Airport |  | GT | 142 |
| 8 | Guaymaral Airport |  | CO | 141 |
| 9 | Harry Reid International Airport |  | US | 133 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 116 |
| 11 | Zurich Airport |  | CH | 113 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Chicago O'Hare International Airport |  | US | 103 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 98 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 97 |
| 16 | Macau International Airport |  | MO | 95 |
| 17 | Tenerife Norte Airport |  | ES | 91 |
| 18 | Madrid Barajas International Airport |  | ES | 90 |
| 19 | Charlotte/Douglas International Airport |  | US | 89 |
| 20 | Reno/Tahoe International Airport |  | US | 87 |
| 21 | Bengaluru International Airport |  | IN | 87 |
| 22 | Kuala Lumpur International Airport |  | MY | 85 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 82 |
| 24 | Ninoy Aquino International Airport |  | PH | 78 |
| 25 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 26 | Congonhas Airport |  | BR | 74 |
| 27 | Malpensa International Airport |  | IT | 73 |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 72 |
| 29 | Vitoria/Foronda Airport |  | ES | 71 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 71 |
| 31 | Pune Airport |  | IN | 70 |
| 32 | Salt Lake City International Airport |  | US | 70 |
| 33 | Daniel K Inouye International Airport |  | US | 69 |
| 34 | Charles de Gaulle International Airport |  | FR | 68 |
| 35 | Barcelona International Airport |  | ES | 68 |
| 36 | Seattle-Tacoma International Airport |  | US | 66 |
| 37 | Miami International Airport |  | US | 65 |
| 38 | Austin-Bergstrom International Airport |  | US | 63 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 63 |
| 40 | Bodø Airport |  | NO | 63 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 56 | 28m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 45 | 14m | 114 km | 88.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 29 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 28 | 23m | 99 km | 48.0 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 25 | 15m | 206 km | 88.9 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 13 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 25 | 52m | 556 km | 239.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 17 | 1h 56m | 1,304 km | 382.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 14 | 13m | 99 km | 24.0 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWA319 | Southwest Airlines | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-04-01 20:05 UTC | 2026-04-01 21:01 UTC | 56m |
| BOE952 | BOE | Renton Municipal Airport (KRNT) | Ochoa Field (6WA4) | 2026-04-01 19:28 UTC | 2026-04-01 20:59 UTC | 1h 31m |
| N850UW |  | Fort Atkinson Municipal Airport (K61C) | Dane County Regional/Truax Field (KMSN) | 2026-04-01 20:45 UTC | 2026-04-01 20:59 UTC | 14m |
| VAR425 | VAR | Phoenix Goodyear Airport (KGYR) | Rio Vista Hills Airport (AZ64) | 2026-04-01 20:06 UTC | 2026-04-01 20:59 UTC | 52m |
| EJA544 | EJA | Sugar Land Regional Airport (KSGR) | Witham Field (KSUA) | 2026-04-01 18:46 UTC | 2026-04-01 20:52 UTC | 2h 6m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-01 20:00 UTC | 2026-04-01 20:51 UTC | 51m |
| N909MM |  | Van Nuys Airport (KVNY) | Sequoia Field (KD86) | 2026-04-01 20:23 UTC | 2026-04-01 20:48 UTC | 25m |
| RB729 |  | 14FL (14FL) | 93FD (93FD) | 2026-04-01 19:41 UTC | 2026-04-01 20:46 UTC | 1h 5m |
| INTEL24 | INT | Chino Airport (KCNO) | Yucca Valley Airport (KL22) | 2026-04-01 20:24 UTC | 2026-04-01 20:44 UTC | 19m |
| N488K |  | North Perry Airport (KHWO) | Peter O Knight Airport (KTPF) | 2026-04-01 19:42 UTC | 2026-04-01 20:42 UTC | 59m |
| WAH | WAH | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-04-01 20:29 UTC | 2026-04-01 20:38 UTC | 8m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-01 20:02 UTC | 2026-04-01 20:37 UTC | 34m |
| N385MR |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-04-01 20:15 UTC | 2026-04-01 20:35 UTC | 19m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-01 20:14 UTC | 2026-04-01 20:35 UTC | 20m |
| N197SC |  | Cantrell Farms Airport (AR06) | Clinton Municipal Airport (KCCA) | 2026-04-01 20:28 UTC | 2026-04-01 20:33 UTC | 5m |
| HOOK64 | HOO | 75OK (75OK) | William R Pogue Municipal Airport (KOWP) | 2026-04-01 20:11 UTC | 2026-04-01 20:32 UTC | 21m |
| BOE790 | BOE | Renton Municipal Airport (KRNT) | Franz Ranch Airport (33WA) | 2026-04-01 18:49 UTC | 2026-04-01 20:30 UTC | 1h 40m |
| JEDI43 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Craig Field (KSEM) | 2026-04-01 19:57 UTC | 2026-04-01 20:29 UTC | 32m |
| RYR290W | Ryanair | Sofia Airport (LBSF) | Bari / Palese International Airport (LIBD) | 2026-04-01 19:38 UTC | 2026-04-01 20:27 UTC | 48m |
| N138BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-01 20:24 UTC | 2026-04-01 20:26 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
