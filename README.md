# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_23:33:29_UTC-green)

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

**Latest saved flight:** 2026-04-09 23:33:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 23:33:29 UTC

- **26,184** saved flights
- **12,500** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,184** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **322,654.6 tonnes** estimated CO2 emissions
- **18,704,616 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1082 |
| 2 | Ryanair | 1073 |
| 3 | IndiGo | 702 |
| 4 | American Airlines | 471 |
| 5 | EJA | 471 |
| 6 | Southwest Airlines | 379 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | Vueling | 266 |
| 10 | AXM | 260 |
| 11 | LATAM Airlines | 259 |
| 12 | QLK | 232 |
| 13 | All Nippon Airways | 231 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 209 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 176 |
| 20 | Japan Airlines | 171 |
| 21 | EJU | 169 |
| 22 | easyJet | 169 |
| 23 | WIF | 165 |
| 24 | AEE | 164 |
| 25 | United Airlines | 157 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 144 |
| 29 | JetBlue | 138 |
| 30 | Cathay Pacific | 136 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20749 |
| 2 | 🇮🇳 IN | 2152 |
| 3 | 🇪🇸 ES | 1944 |
| 4 | 🇦🇺 AU | 1894 |
| 5 | 🇧🇷 BR | 1480 |
| 6 | 🇯🇵 JP | 1438 |
| 7 | 🇩🇪 DE | 1342 |
| 8 | 🇮🇹 IT | 1326 |
| 9 | 🇨🇴 CO | 1319 |
| 10 | 🇨🇦 CA | 1252 |
| 11 | 🇬🇧 GB | 1046 |
| 12 | 🇫🇷 FR | 963 |
| 13 | 🇲🇽 MX | 846 |
| 14 | 🇬🇷 GR | 743 |
| 15 | 🇨🇭 CH | 716 |
| 16 | 🇲🇾 MY | 624 |
| 17 | 🇳🇿 NZ | 574 |
| 18 | 🇳🇴 NO | 559 |
| 19 | 🇿🇦 ZA | 532 |
| 20 | 🇹🇷 TR | 492 |
| 21 | 🇬🇹 GT | 489 |
| 22 | 🇵🇭 PH | 482 |
| 23 | 🇰🇷 KR | 450 |
| 24 | 🇹🇭 TH | 434 |
| 25 | 🇵🇱 PL | 385 |
| 26 | 🇲🇦 MA | 322 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇲🇪 ME | 260 |
| 29 | 🇲🇴 MO | 259 |
| 30 | 🇮🇩 ID | 258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 623 |
| 2 | El Dorado International Airport |  | CO | 490 |
| 3 | Tokyo International Airport |  | JP | 481 |
| 4 | Denver International Airport |  | US | 447 |
| 5 | Indira Gandhi International Airport |  | IN | 444 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 361 |
| 7 | Harry Reid International Airport |  | US | 341 |
| 8 | La Aurora Airport |  | GT | 339 |
| 9 | Zurich Airport |  | CH | 306 |
| 10 | Frankfurt am Main International Airport |  | DE | 283 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 13 | Chicago O'Hare International Airport |  | US | 272 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 267 |
| 15 | Macau International Airport |  | MO | 259 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 257 |
| 17 | Charlotte/Douglas International Airport |  | US | 242 |
| 18 | Bengaluru International Airport |  | IN | 235 |
| 19 | Kuala Lumpur International Airport |  | MY | 231 |
| 20 | Tenerife Norte Airport |  | ES | 228 |
| 21 | Ninoy Aquino International Airport |  | PH | 224 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 207 |
| 24 | Malpensa International Airport |  | IT | 205 |
| 25 | Congonhas Airport |  | BR | 205 |
| 26 | Salt Lake City International Airport |  | US | 204 |
| 27 | Daniel K Inouye International Airport |  | US | 200 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 185 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 180 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 175 |
| 34 | Seattle-Tacoma International Airport |  | US | 169 |
| 35 | Barcelona International Airport |  | ES | 168 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 37 | O. R. Tambo International Airport |  | ZA | 168 |
| 38 | Vitoria/Foronda Airport |  | ES | 163 |
| 39 | Capua Airport |  | IT | 161 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 123 | 1h 8m | 706 km | 1,497.5 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 96 | 24m | 225 km | 372.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 65 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 64 | 19m | 165 km | 182.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 51 | 31m | 369 km | 324.6 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 46 | 20m | 250 km | 198.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 25 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NTRDR12 | NTR | Corona Municipal Airport (KAJO) | Corona Municipal Airport (KAJO) | 2026-04-09 23:07 UTC | 2026-04-09 23:33 UTC | 25m |
| N611MV |  | Mc Clellan Airfield (KMCC) | Visalia Municipal Airport (KVIS) | 2026-04-09 22:36 UTC | 2026-04-09 23:19 UTC | 43m |
| N579M |  | Albuquerque International Sunport Airport (KABQ) | Sacaton Airport (NM16) | 2026-04-09 22:55 UTC | 2026-04-09 23:16 UTC | 20m |
| N746CX |  | Fremont Municipal Airport (KFET) | Eldon Model Airpark (KH79) | 2026-04-09 22:34 UTC | 2026-04-09 23:15 UTC | 40m |
| N822ST |  | Astoria Regional Airport (KAST) | Newport Municipal Airport (KONP) | 2026-04-09 22:34 UTC | 2026-04-09 23:14 UTC | 39m |
| N263BA |  | Sahoma Lake Airport (03OK) | Steamboat Springs/Bob Adams Field (KSBS) | 2026-04-09 20:47 UTC | 2026-04-09 23:09 UTC | 2h 22m |
| XSN82 | XSN | Meadows Field (KBFL) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-09 22:16 UTC | 2026-04-09 23:04 UTC | 47m |
| ZHT | ZHT | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-09 22:44 UTC | 2026-04-09 23:04 UTC | 19m |
| OAI | OAI | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-04-09 22:38 UTC | 2026-04-09 23:02 UTC | 24m |
| CXK520 | CXK | Raleigh Regional At Person County Airport (KTDF) | Raleigh Regional At Person County Airport (KTDF) | 2026-04-09 22:59 UTC | 2026-04-09 23:00 UTC | 1m |
| N447RM |  | Billings Logan International Airport (KBIL) | Cottonwood Airport (0MT5) | 2026-04-09 22:44 UTC | 2026-04-09 22:58 UTC | 13m |
| N459SP |  | Commerce Municipal Airport (K2F7) | Majors Airport (KGVT) | 2026-04-09 22:44 UTC | 2026-04-09 22:58 UTC | 14m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-09 22:21 UTC | 2026-04-09 22:58 UTC | 36m |
| N216BG |  | Augusta Regional At Bush Field (KAGS) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-09 22:20 UTC | 2026-04-09 22:55 UTC | 34m |
| PXT680 | PXT | San Francisco International Airport (KSFO) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-09 22:45 UTC | 2026-04-09 22:54 UTC | 8m |
| N715HL |  | Dillingham Airport (PADL) | King Salmon Airport (PAKN) | 2026-04-09 22:33 UTC | 2026-04-09 22:52 UTC | 19m |
| BOV709 | BOV | Ministro Pistarini International Airport (SAEZ) | Laja Airport (SLLJ) | 2026-04-09 18:17 UTC | 2026-04-09 22:51 UTC | 4h 33m |
|  |  | Deadwood Dam Airstrip (ID86) | Deadwood Dam Airstrip (ID86) | 2026-04-09 22:48 UTC | 2026-04-09 22:48 UTC | 0m |
| N97ML |  | Oakland County International Airport (KPTK) | St Clair County International Airport (KPHN) | 2026-04-09 22:17 UTC | 2026-04-09 22:48 UTC | 30m |
| N127KC |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-04-09 22:26 UTC | 2026-04-09 22:47 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
