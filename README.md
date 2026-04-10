# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_21:56:57_UTC-green)

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

**Latest saved flight:** 2026-04-10 21:56:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 21:56:57 UTC

- **27,816** saved flights
- **13,087** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,816** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **339,054.2 tonnes** estimated CO2 emissions
- **19,655,314 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1143 |
| 2 | Ryanair | 1137 |
| 3 | IndiGo | 733 |
| 4 | EJA | 496 |
| 5 | American Airlines | 491 |
| 6 | Southwest Airlines | 399 |
| 7 | ENY | 374 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 283 |
| 11 | LATAM Airlines | 272 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 235 |
| 15 | LXJ | 230 |
| 16 | AZU | 228 |
| 17 | Swiss International | 196 |
| 18 | Alaska Airlines | 186 |
| 19 | VIV | 182 |
| 20 | easyJet | 181 |
| 21 | EJU | 179 |
| 22 | WIF | 179 |
| 23 | AEE | 178 |
| 24 | Japan Airlines | 177 |
| 25 | United Airlines | 169 |
| 26 | EDV | 163 |
| 27 | Avianca | 156 |
| 28 | JetBlue | 148 |
| 29 | AXB | 147 |
| 30 | PGT | 142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22116 |
| 2 | 🇮🇳 IN | 2250 |
| 3 | 🇪🇸 ES | 2046 |
| 4 | 🇦🇺 AU | 1998 |
| 5 | 🇧🇷 BR | 1566 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇮🇹 IT | 1398 |
| 8 | 🇨🇴 CO | 1393 |
| 9 | 🇩🇪 DE | 1392 |
| 10 | 🇨🇦 CA | 1355 |
| 11 | 🇬🇧 GB | 1120 |
| 12 | 🇫🇷 FR | 1023 |
| 13 | 🇲🇽 MX | 888 |
| 14 | 🇬🇷 GR | 799 |
| 15 | 🇨🇭 CH | 756 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 608 |
| 18 | 🇳🇴 NO | 603 |
| 19 | 🇿🇦 ZA | 567 |
| 20 | 🇬🇹 GT | 521 |
| 21 | 🇵🇭 PH | 512 |
| 22 | 🇹🇷 TR | 507 |
| 23 | 🇹🇭 TH | 481 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 344 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 278 |
| 29 | 🇳🇱 NL | 270 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 666 |
| 2 | El Dorado International Airport |  | CO | 504 |
| 3 | Tokyo International Airport |  | JP | 500 |
| 4 | Denver International Airport |  | US | 474 |
| 5 | Indira Gandhi International Airport |  | IN | 466 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 389 |
| 7 | La Aurora Airport |  | GT | 367 |
| 8 | Harry Reid International Airport |  | US | 360 |
| 9 | Zurich Airport |  | CH | 327 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 293 |
| 12 | Chicago O'Hare International Airport |  | US | 290 |
| 13 | Frankfurt am Main International Airport |  | DE | 289 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 285 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 16 | Macau International Airport |  | MO | 261 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Charlotte/Douglas International Airport |  | US | 252 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 237 |
| 22 | Madrid Barajas International Airport |  | ES | 236 |
| 23 | Congonhas Airport |  | BR | 222 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 219 |
| 25 | Malpensa International Airport |  | IT | 216 |
| 26 | Salt Lake City International Airport |  | US | 216 |
| 27 | Daniel K Inouye International Airport |  | US | 214 |
| 28 | Reno/Tahoe International Airport |  | US | 203 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 190 |
| 31 | Miami International Airport |  | US | 189 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 187 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Seattle-Tacoma International Airport |  | US | 175 |
| 37 | Barcelona International Airport |  | ES | 175 |
| 38 | Capua Airport |  | IT | 175 |
| 39 | Vitoria/Foronda Airport |  | ES | 174 |
| 40 | Don Mueang International Airport |  | TH | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
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
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 54 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 49 | 52m | 556 km | 469.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 40 | 21m | 244 km | 168.4 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100PC |  | Homer Airport (PAHO) | Longmere Lake Air Strip (AK07) | 2026-04-10 21:39 UTC | 2026-04-10 21:56 UTC | 17m |
| N424W |  | Mc Kinnon Airpark (48FL) | Mc Kinnon Airpark (48FL) | 2026-04-10 21:27 UTC | 2026-04-10 21:53 UTC | 25m |
| CFLOE | CFL | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Cooking Lake Airport (CEZ3) | 2026-04-10 21:39 UTC | 2026-04-10 21:51 UTC | 12m |
| N70LC |  | 54TX (54TX) | Boerne Stage Airfield (K5C1) | 2026-04-10 20:54 UTC | 2026-04-10 21:49 UTC | 55m |
| NWX580 | NWX | Aero Valley Airport (K52F) | 69XA (69XA) | 2026-04-10 21:20 UTC | 2026-04-10 21:49 UTC | 28m |
| N313RR |  | Johnston Farm Airport (10NC) | Northeastern Regional Airport (KEDE) | 2026-04-10 21:19 UTC | 2026-04-10 21:49 UTC | 30m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-10 21:27 UTC | 2026-04-10 21:45 UTC | 17m |
| AMMO75 | AMM | Edwards Af Aux North Base Airport (K9L2) | Boron Airstrip (57CL) | 2026-04-10 21:33 UTC | 2026-04-10 21:44 UTC | 10m |
| N489AM |  | San Antonio International Airport (KSAT) | Owen Field (4XA3) | 2026-04-10 21:13 UTC | 2026-04-10 21:42 UTC | 28m |
| N668PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-04-10 20:18 UTC | 2026-04-10 21:40 UTC | 1h 22m |
| STT60 | STT | Santa Monica Municipal Airport (KSMO) | Santa Ynez/Kunkle Field (KIZA) | 2026-04-10 21:07 UTC | 2026-04-10 21:34 UTC | 26m |
| N642PF |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-04-10 21:30 UTC | 2026-04-10 21:32 UTC | 1m |
| N924S |  | Gulf Shores International/Jack Edwards Field (KJKA) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-10 21:02 UTC | 2026-04-10 21:29 UTC | 27m |
| SLH363 | SLH | Olson Field (NE30) | Lincoln Airport (KLNK) | 2026-04-10 21:02 UTC | 2026-04-10 21:25 UTC | 23m |
| N310TY |  | Long Island Mac Arthur Airport (KISP) | Boyle's Landing Airport (NK91) | 2026-04-10 18:07 UTC | 2026-04-10 21:25 UTC | 3h 18m |
| CPA085 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-10 07:12 UTC | 2026-04-10 21:24 UTC | 14h 11m |
| N492SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-10 21:08 UTC | 2026-04-10 21:20 UTC | 12m |
| N57HR |  | Witham Field (KSUA) | North Perry Airport (KHWO) | 2026-04-10 20:45 UTC | 2026-04-10 21:17 UTC | 32m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-10 20:52 UTC | 2026-04-10 21:16 UTC | 24m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-10 21:00 UTC | 2026-04-10 21:13 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
