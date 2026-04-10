# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_20:39:30_UTC-green)

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

**Latest saved flight:** 2026-04-10 20:39:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 20:39:30 UTC

- **27,676** saved flights
- **13,026** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,676** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **337,338.1 tonnes** estimated CO2 emissions
- **19,555,833 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1135 |
| 2 | Ryanair | 1133 |
| 3 | IndiGo | 733 |
| 4 | EJA | 493 |
| 5 | American Airlines | 485 |
| 6 | Southwest Airlines | 395 |
| 7 | ENY | 370 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 283 |
| 11 | LATAM Airlines | 271 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 234 |
| 15 | LXJ | 229 |
| 16 | AZU | 227 |
| 17 | Swiss International | 195 |
| 18 | Alaska Airlines | 185 |
| 19 | easyJet | 180 |
| 20 | VIV | 180 |
| 21 | EJU | 179 |
| 22 | WIF | 179 |
| 23 | AEE | 178 |
| 24 | Japan Airlines | 177 |
| 25 | United Airlines | 168 |
| 26 | EDV | 163 |
| 27 | Avianca | 156 |
| 28 | JetBlue | 148 |
| 29 | AXB | 147 |
| 30 | PGT | 142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21936 |
| 2 | 🇮🇳 IN | 2250 |
| 3 | 🇪🇸 ES | 2042 |
| 4 | 🇦🇺 AU | 1996 |
| 5 | 🇧🇷 BR | 1558 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇮🇹 IT | 1394 |
| 8 | 🇩🇪 DE | 1391 |
| 9 | 🇨🇴 CO | 1389 |
| 10 | 🇨🇦 CA | 1338 |
| 11 | 🇬🇧 GB | 1116 |
| 12 | 🇫🇷 FR | 1023 |
| 13 | 🇲🇽 MX | 881 |
| 14 | 🇬🇷 GR | 799 |
| 15 | 🇨🇭 CH | 755 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 604 |
| 18 | 🇳🇴 NO | 603 |
| 19 | 🇿🇦 ZA | 567 |
| 20 | 🇬🇹 GT | 513 |
| 21 | 🇵🇭 PH | 512 |
| 22 | 🇹🇷 TR | 507 |
| 23 | 🇹🇭 TH | 481 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 341 |
| 27 | 🇧🇸 BS | 295 |
| 28 | 🇲🇪 ME | 278 |
| 29 | 🇳🇱 NL | 269 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 661 |
| 2 | El Dorado International Airport |  | CO | 504 |
| 3 | Tokyo International Airport |  | JP | 500 |
| 4 | Denver International Airport |  | US | 470 |
| 5 | Indira Gandhi International Airport |  | IN | 466 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 389 |
| 7 | La Aurora Airport |  | GT | 359 |
| 8 | Harry Reid International Airport |  | US | 355 |
| 9 | Zurich Airport |  | CH | 326 |
| 10 | Guaymaral Airport |  | CO | 309 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 291 |
| 12 | Chicago O'Hare International Airport |  | US | 289 |
| 13 | Frankfurt am Main International Airport |  | DE | 289 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 282 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 16 | Macau International Airport |  | MO | 260 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Charlotte/Douglas International Airport |  | US | 252 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 236 |
| 22 | Madrid Barajas International Airport |  | ES | 235 |
| 23 | Congonhas Airport |  | BR | 218 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 217 |
| 25 | Malpensa International Airport |  | IT | 216 |
| 26 | Salt Lake City International Airport |  | US | 216 |
| 27 | Daniel K Inouye International Airport |  | US | 212 |
| 28 | Reno/Tahoe International Airport |  | US | 201 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 190 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 187 |
| 32 | Miami International Airport |  | US | 185 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Barcelona International Airport |  | ES | 175 |
| 37 | Capua Airport |  | IT | 175 |
| 38 | Vitoria/Foronda Airport |  | ES | 174 |
| 39 | Seattle-Tacoma International Airport |  | US | 173 |
| 40 | Don Mueang International Airport |  | TH | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 118 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 112 | 14m | 114 km | 219.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 73 | 21m | 99 km | 125.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 51 | 9m | - | - |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 48 | 52m | 556 km | 460.1 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 38 | 21m | 244 km | 160.0 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N305PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-04-10 20:01 UTC | 2026-04-10 20:39 UTC | 38m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-10 06:06 UTC | 2026-04-10 20:33 UTC | 14h 26m |
| N65619 |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-04-10 19:56 UTC | 2026-04-10 20:28 UTC | 32m |
| N405CM |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-04-10 20:02 UTC | 2026-04-10 20:26 UTC | 24m |
| CFBAQ | CFB | Red Deer / Truant Airfield (CRD5) | Rocky Mountain House Airport (CYRM) | 2026-04-10 20:10 UTC | 2026-04-10 20:23 UTC | 12m |
| SWR979E | Swiss International | Berlin Brandenburg Airport (EDDB) | Zurich Airport (LSZH) | 2026-04-10 19:17 UTC | 2026-04-10 20:19 UTC | 1h 2m |
| COBRA32 | COB | Dave Eby Field (4XA5) | Frederick Regional Airport (KFDR) | 2026-04-10 19:44 UTC | 2026-04-10 20:18 UTC | 34m |
| ERU68 | ERU | Morgan Ranch Airstrip (AZ46) | Pilots Rest Airport (AZ57) | 2026-04-10 19:56 UTC | 2026-04-10 20:16 UTC | 19m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-04-10 20:05 UTC | 2026-04-10 20:15 UTC | 10m |
| N908FG |  | Solberg/Hunterdon Airport (KN51) | Sky Manor Airport (KN40) | 2026-04-10 19:31 UTC | 2026-04-10 20:12 UTC | 40m |
| N415XT |  | Charles M Schulz/Sonoma County Airport (KSTS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-10 19:41 UTC | 2026-04-10 20:11 UTC | 30m |
| N969TT |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-10 18:37 UTC | 2026-04-10 20:06 UTC | 1h 29m |
| N345CD |  | Marion Airport (KC17) | Marion Airport (KC17) | 2026-04-10 19:25 UTC | 2026-04-10 20:06 UTC | 41m |
| N56578 |  | Somerset Airport (KSMQ) | 6NJ1 (6NJ1) | 2026-04-10 19:32 UTC | 2026-04-10 20:01 UTC | 29m |
| N786FA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-10 19:34 UTC | 2026-04-10 20:01 UTC | 27m |
| N48CW |  | Morgan County Airport (K42U) | Morgan County Airport (K42U) | 2026-04-10 19:48 UTC | 2026-04-10 19:58 UTC | 9m |
| CXK419 | CXK | Concord-Padgett Regional Airport (KJQF) | Mid-Carolina Regional Airport (KRUQ) | 2026-04-10 19:32 UTC | 2026-04-10 19:56 UTC | 23m |
| FFT3804 | FFT | Denver International Airport (KDEN) | Coral Creek Airport (FA54) | 2026-04-10 16:57 UTC | 2026-04-10 19:56 UTC | 2h 59m |
| ERU4 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-04-10 19:42 UTC | 2026-04-10 19:55 UTC | 13m |
| UAL1361 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | Coral Creek Airport (FA54) | 2026-04-10 18:23 UTC | 2026-04-10 19:54 UTC | 1h 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
