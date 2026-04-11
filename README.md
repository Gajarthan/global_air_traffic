# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_05:00:25_UTC-green)

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

**Latest saved flight:** 2026-04-11 05:00:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 05:00:25 UTC

- **28,135** saved flights
- **13,212** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,135** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **341,582.6 tonnes** estimated CO2 emissions
- **19,801,890 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1154 |
| 2 | Ryanair | 1140 |
| 3 | IndiGo | 733 |
| 4 | EJA | 502 |
| 5 | American Airlines | 493 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 293 |
| 10 | Vueling | 283 |
| 11 | LATAM Airlines | 275 |
| 12 | QLK | 251 |
| 13 | All Nippon Airways | 250 |
| 14 | Delta Air Lines | 239 |
| 15 | AZU | 232 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 196 |
| 18 | Alaska Airlines | 189 |
| 19 | VIV | 183 |
| 20 | easyJet | 181 |
| 21 | Japan Airlines | 181 |
| 22 | AEE | 179 |
| 23 | EJU | 179 |
| 24 | WIF | 179 |
| 25 | United Airlines | 171 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | JetBlue | 150 |
| 29 | AXB | 147 |
| 30 | PGT | 143 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22432 |
| 2 | 🇮🇳 IN | 2255 |
| 3 | 🇦🇺 AU | 2055 |
| 4 | 🇪🇸 ES | 2047 |
| 5 | 🇧🇷 BR | 1589 |
| 6 | 🇯🇵 JP | 1522 |
| 7 | 🇨🇴 CO | 1407 |
| 8 | 🇮🇹 IT | 1400 |
| 9 | 🇩🇪 DE | 1392 |
| 10 | 🇨🇦 CA | 1391 |
| 11 | 🇬🇧 GB | 1121 |
| 12 | 🇫🇷 FR | 1024 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 803 |
| 15 | 🇨🇭 CH | 756 |
| 16 | 🇲🇾 MY | 698 |
| 17 | 🇳🇿 NZ | 631 |
| 18 | 🇳🇴 NO | 605 |
| 19 | 🇿🇦 ZA | 567 |
| 20 | 🇵🇭 PH | 528 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 509 |
| 23 | 🇹🇭 TH | 489 |
| 24 | 🇰🇷 KR | 477 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 345 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 278 |
| 29 | 🇮🇩 ID | 271 |
| 30 | 🇳🇱 NL | 270 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 674 |
| 2 | Tokyo International Airport |  | JP | 513 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Denver International Airport |  | US | 478 |
| 5 | Indira Gandhi International Airport |  | IN | 468 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 391 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 364 |
| 9 | Zurich Airport |  | CH | 327 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 292 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 14 | Frankfurt am Main International Airport |  | DE | 289 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 286 |
| 16 | Macau International Airport |  | MO | 261 |
| 17 | Kuala Lumpur International Airport |  | MY | 260 |
| 18 | Charlotte/Douglas International Airport |  | US | 257 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 244 |
| 21 | Madrid Barajas International Airport |  | ES | 237 |
| 22 | Tenerife Norte Airport |  | ES | 237 |
| 23 | Congonhas Airport |  | BR | 227 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 25 | Salt Lake City International Airport |  | US | 220 |
| 26 | Daniel K Inouye International Airport |  | US | 218 |
| 27 | Malpensa International Airport |  | IT | 217 |
| 28 | Reno/Tahoe International Airport |  | US | 209 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 193 |
| 31 | Miami International Airport |  | US | 189 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 188 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Seattle-Tacoma International Airport |  | US | 179 |
| 37 | Barcelona International Airport |  | ES | 175 |
| 38 | Capua Airport |  | IT | 175 |
| 39 | Vitoria/Foronda Airport |  | ES | 174 |
| 40 | Calgary International Airport |  | CA | 170 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 130 | 1h 8m | 706 km | 1,582.8 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 105 | 24m | 225 km | 407.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 80 | 1h 27m | 910 km | 1,255.4 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 70 | 19m | 165 km | 199.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 61 | 55m | 546 km | 574.3 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 61 | 1h 12m | 770 km | 810.3 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 54 | 31m | 369 km | 343.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 52 | 46m | 452 km | 405.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 44 | 20m | 147 km | 111.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 43 | 21m | 244 km | 181.1 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFG | CFG | Caloundra Airport (YCDR) | Caloundra Airport (YCDR) | 2026-04-11 04:45 UTC | 2026-04-11 05:00 UTC | 14m |
| CFL08 | CFL | Martinborough Airport (NZMT) | Hood Airport (NZMS) | 2026-04-11 04:24 UTC | 2026-04-11 04:35 UTC | 10m |
| SLG1 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Maidstone Airport (CJH3) | 2026-04-11 03:58 UTC | 2026-04-11 04:30 UTC | 31m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-11 03:50 UTC | 2026-04-11 04:27 UTC | 37m |
| ERU67 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Phoenix Deer Valley Airport (KDVT) | 2026-04-11 03:44 UTC | 2026-04-11 04:21 UTC | 37m |
| DSU56 | DSU | Ruleville-Drew Airport (KM37) | Cleveland Municipal Airport (KRNV) | 2026-04-11 03:15 UTC | 2026-04-11 04:20 UTC | 1h 4m |
| DAL534 | Delta Air Lines | Daniel K Inouye International Airport (PHNL) | UT40 (UT40) | 2026-04-10 22:37 UTC | 2026-04-11 04:18 UTC | 5h 41m |
| SWA2786 | Southwest Airlines | Harry Reid International Airport (KLAS) | Salt Lake City International Airport (KSLC) | 2026-04-11 03:17 UTC | 2026-04-11 04:18 UTC | 1h 1m |
| AM222 |  | Sydney Kingsford Smith International Airport (YSSY) | Adaminaby Airport (YADI) | 2026-04-11 03:37 UTC | 2026-04-11 04:17 UTC | 40m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-11 04:01 UTC | 2026-04-11 04:15 UTC | 14m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-11 03:46 UTC | 2026-04-11 04:14 UTC | 27m |
| ERU70 | ERU | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-11 03:53 UTC | 2026-04-11 04:10 UTC | 17m |
| N650NR |  | Addison Airport (KADS) | Iron Mountain Pumping Plant Airport (72CL) | 2026-04-11 01:59 UTC | 2026-04-11 04:08 UTC | 2h 8m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Sariang Airport (VTCS) | 2026-04-11 03:41 UTC | 2026-04-11 04:04 UTC | 22m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-11 03:43 UTC | 2026-04-11 04:03 UTC | 19m |
| UBG121 | UBG | VGZR (VGZR) | Jessore Airport (VGJR) | 2026-04-11 03:36 UTC | 2026-04-11 04:03 UTC | 26m |
| AVA9817 | Avianca | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 2026-04-11 03:47 UTC | 2026-04-11 04:03 UTC | 15m |
| QLK334D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-04-11 03:29 UTC | 2026-04-11 04:02 UTC | 32m |
| LOK | LOK | Caloundra Airport (YCDR) | Caloundra Airport (YCDR) | 2026-04-11 03:47 UTC | 2026-04-11 04:02 UTC | 14m |
| RNA230 | RNA | Tribhuvan International Airport (VNKT) | Simara Airport (VNSI) | 2026-04-10 18:23 UTC | 2026-04-11 03:57 UTC | 9h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
