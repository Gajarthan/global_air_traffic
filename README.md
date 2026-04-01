# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_21:46:57_UTC-green)

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

**Latest saved flight:** 2026-04-01 21:46:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-01 21:46:57 UTC

- **9,823** saved flights
- **5,877** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **9,823** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **118,692.6 tonnes** estimated CO2 emissions
- **6,880,730 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 454 |
| 2 | Ryanair | 379 |
| 3 | IndiGo | 263 |
| 4 | EJA | 208 |
| 5 | American Airlines | 181 |
| 6 | Lufthansa | 164 |
| 7 | Southwest Airlines | 151 |
| 8 | ENY | 136 |
| 9 | Vueling | 106 |
| 10 | AXM | 102 |
| 11 | LATAM Airlines | 101 |
| 12 | LXJ | 95 |
| 13 | All Nippon Airways | 80 |
| 14 | WIF | 80 |
| 15 | Delta Air Lines | 77 |
| 16 | Swiss International | 73 |
| 17 | QLK | 72 |
| 18 | VIV | 69 |
| 19 | AZU | 68 |
| 20 | AXB | 63 |
| 21 | United Airlines | 63 |
| 22 | Alaska Airlines | 60 |
| 23 | EDV | 60 |
| 24 | Japan Airlines | 60 |
| 25 | BRC | 58 |
| 26 | easyJet | 56 |
| 27 | EJU | 55 |
| 28 | Avianca | 53 |
| 29 | Cathay Pacific | 52 |
| 30 | AEE | 51 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 8185 |
| 2 | 🇮🇳 IN | 807 |
| 3 | 🇪🇸 ES | 761 |
| 4 | 🇦🇺 AU | 712 |
| 5 | 🇩🇪 DE | 526 |
| 6 | 🇧🇷 BR | 507 |
| 7 | 🇨🇴 CO | 493 |
| 8 | 🇨🇦 CA | 475 |
| 9 | 🇯🇵 JP | 465 |
| 10 | 🇮🇹 IT | 434 |
| 11 | 🇲🇽 MX | 353 |
| 12 | 🇬🇧 GB | 349 |
| 13 | 🇫🇷 FR | 301 |
| 14 | 🇳🇴 NO | 261 |
| 15 | 🇲🇾 MY | 229 |
| 16 | 🇬🇷 GR | 227 |
| 17 | 🇨🇭 CH | 225 |
| 18 | 🇳🇿 NZ | 213 |
| 19 | 🇬🇹 GT | 204 |
| 20 | 🇿🇦 ZA | 203 |
| 21 | 🇵🇭 PH | 172 |
| 22 | 🇹🇷 TR | 160 |
| 23 | 🇰🇷 KR | 157 |
| 24 | 🇵🇱 PL | 128 |
| 25 | 🇮🇩 ID | 119 |
| 26 | 🇲🇦 MA | 115 |
| 27 | 🇹🇭 TH | 114 |
| 28 | 🇲🇴 MO | 97 |
| 29 | 🇲🇪 ME | 97 |
| 30 | 🇧🇸 BS | 95 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 241 |
| 2 | Denver International Airport |  | US | 179 |
| 3 | Indira Gandhi International Airport |  | IN | 177 |
| 4 | Tokyo International Airport |  | JP | 166 |
| 5 | Frankfurt am Main International Airport |  | DE | 166 |
| 6 | El Dorado International Airport |  | CO | 156 |
| 7 | Guaymaral Airport |  | CO | 147 |
| 8 | La Aurora Airport |  | GT | 143 |
| 9 | Harry Reid International Airport |  | US | 135 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 118 |
| 11 | Zurich Airport |  | CH | 113 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 110 |
| 13 | Chicago O'Hare International Airport |  | US | 103 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 100 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 99 |
| 16 | Macau International Airport |  | MO | 97 |
| 17 | Tenerife Norte Airport |  | ES | 91 |
| 18 | Madrid Barajas International Airport |  | ES | 90 |
| 19 | Charlotte/Douglas International Airport |  | US | 89 |
| 20 | Reno/Tahoe International Airport |  | US | 88 |
| 21 | Bengaluru International Airport |  | IN | 87 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 85 |
| 23 | Kuala Lumpur International Airport |  | MY | 85 |
| 24 | Ninoy Aquino International Airport |  | PH | 78 |
| 25 | Congonhas Airport |  | BR | 76 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 74 |
| 27 | Malpensa International Airport |  | IT | 73 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 72 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 72 |
| 30 | Vitoria/Foronda Airport |  | ES | 71 |
| 31 | Salt Lake City International Airport |  | US | 71 |
| 32 | Pune Airport |  | IN | 70 |
| 33 | Daniel K Inouye International Airport |  | US | 69 |
| 34 | Charles de Gaulle International Airport |  | FR | 69 |
| 35 | Barcelona International Airport |  | ES | 68 |
| 36 | Seattle-Tacoma International Airport |  | US | 68 |
| 37 | Miami International Airport |  | US | 65 |
| 38 | Bodø Airport |  | NO | 65 |
| 39 | Austin-Bergstrom International Airport |  | US | 64 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 63 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 59 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 45 | 14m | 114 km | 88.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 40 | 1h 7m | 706 km | 487.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 34 | 24m | 225 km | 131.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 30 | 30m | 304 km | 157.3 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 30 | 1h 44m | 1,156 km | 598.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 30 | 30m | - | - |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 30 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 28 | 23m | 99 km | 48.0 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 28 | 26m | 152 km | 73.2 t |
| 11 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 26 | 52m | 556 km | 249.2 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 25 | 15m | 206 km | 88.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 25 | 20m | 165 km | 71.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 23 | 1h 43m | 1,423 km | 564.5 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 23 | 1h 26m | 910 km | 360.9 t |
| 16 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 22 | 28m | 275 km | 104.2 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 22 | 8m | - | - |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 21 | 30m | 369 km | 133.7 t |
| 19 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 19 | 1h 1m | 723 km | 236.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 19 | 53m | 546 km | 178.9 t |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 18 | 1h 10m | 770 km | 239.1 t |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 18 | 1h 56m | 1,304 km | 405.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 17 | 11m | 127 km | 37.2 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 17 | 20m | 250 km | 73.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 16 | 1h 46m | 1,290 km | 356.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 15 | 23m | 252 km | 65.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 15 | 20m | - | - |
| 28 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 15 | 28m | 69 km | 17.9 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 14 | 13m | 99 km | 24.0 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-01 21:35 UTC | 2026-04-01 21:46 UTC | 11m |
| N414EP |  | 3WA1 (3WA1) | Boeing Field/King County International Airport (KBFI) | 2026-04-01 21:13 UTC | 2026-04-01 21:45 UTC | 32m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-01 10:36 UTC | 2026-04-01 21:43 UTC | 11h 7m |
| CPA085 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-01 07:23 UTC | 2026-04-01 21:39 UTC | 14h 16m |
| N6565J |  | Seminole Municipal Airport (KSRE) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-01 21:22 UTC | 2026-04-01 21:39 UTC | 16m |
| KAI | KAI | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-01 21:26 UTC | 2026-04-01 21:38 UTC | 12m |
| BULET46 | BUL | John Nichol's Field (0CL3) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-01 21:24 UTC | 2026-04-01 21:33 UTC | 9m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-01 20:58 UTC | 2026-04-01 21:32 UTC | 33m |
| HK5077G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-01 21:07 UTC | 2026-04-01 21:21 UTC | 13m |
| N531WC |  | Agua Dulce Airport (KL70) | Agua Dulce Airport (KL70) | 2026-04-01 21:19 UTC | 2026-04-01 21:19 UTC | 0m |
| JKR56 | JKR | Republic Airport (KFRG) | Miami Executive Airport (KTMB) | 2026-04-01 18:46 UTC | 2026-04-01 21:16 UTC | 2h 29m |
| VVHK012 | VVH | Jacksonville Executive At Craig Airport (KCRG) | Whitehouse Nolf Airport (KNEN) | 2026-04-01 21:09 UTC | 2026-04-01 21:16 UTC | 7m |
| PGT1928 | PGT | Kutahya Airport (LTBN) | Ercan International Airport (LCEN) | 2026-04-01 20:23 UTC | 2026-04-01 21:16 UTC | 52m |
| CXK437 | CXK | Oxnard Airport (KOXR) | Meadows Field (KBFL) | 2026-04-01 20:08 UTC | 2026-04-01 21:15 UTC | 1h 6m |
| ERU878 | ERU | Daytona Beach International Airport (KDAB) | KXFL (KXFL) | 2026-04-01 20:36 UTC | 2026-04-01 21:14 UTC | 38m |
| N438WR |  | Green Bay/Austin Straubel International Airport (KGRB) | 1PS4 (1PS4) | 2026-04-01 20:07 UTC | 2026-04-01 21:14 UTC | 1h 6m |
| N220BG |  | Birmingham-Shuttlesworth International Airport (KBHM) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-01 20:43 UTC | 2026-04-01 21:13 UTC | 29m |
| TGLRN | TGL | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-04-01 20:22 UTC | 2026-04-01 21:13 UTC | 50m |
| BB011 |  | Bob Sikes Airport (KCEW) | Brewton Municipal Airport (K12J) | 2026-04-01 20:51 UTC | 2026-04-01 21:13 UTC | 21m |
| AM261 |  | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-04-01 20:29 UTC | 2026-04-01 21:09 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
