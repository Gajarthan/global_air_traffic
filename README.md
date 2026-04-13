# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_20:28:38_UTC-green)

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

**Latest saved flight:** 2026-04-13 20:28:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 20:28:38 UTC

- **32,878** saved flights
- **14,750** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,878** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **404,101.7 tonnes** estimated CO2 emissions
- **23,426,185 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1401 |
| 2 | SkyWest Airlines | 1324 |
| 3 | IndiGo | 839 |
| 4 | EJA | 572 |
| 5 | American Airlines | 569 |
| 6 | Southwest Airlines | 474 |
| 7 | ENY | 440 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 345 |
| 10 | Vueling | 339 |
| 11 | LATAM Airlines | 328 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 290 |
| 14 | Delta Air Lines | 275 |
| 15 | LXJ | 268 |
| 16 | QLK | 266 |
| 17 | Swiss International | 251 |
| 18 | WIF | 225 |
| 19 | EJU | 221 |
| 20 | easyJet | 221 |
| 21 | Alaska Airlines | 219 |
| 22 | AEE | 213 |
| 23 | VIV | 211 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 191 |
| 26 | United Airlines | 188 |
| 27 | GLO | 179 |
| 28 | Air France | 178 |
| 29 | JetBlue | 177 |
| 30 | Avianca | 175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25855 |
| 2 | 🇮🇳 IN | 2563 |
| 3 | 🇪🇸 ES | 2486 |
| 4 | 🇦🇺 AU | 2253 |
| 5 | 🇧🇷 BR | 1930 |
| 6 | 🇯🇵 JP | 1781 |
| 7 | 🇮🇹 IT | 1761 |
| 8 | 🇩🇪 DE | 1661 |
| 9 | 🇨🇴 CO | 1637 |
| 10 | 🇨🇦 CA | 1594 |
| 11 | 🇬🇧 GB | 1349 |
| 12 | 🇫🇷 FR | 1218 |
| 13 | 🇲🇽 MX | 1040 |
| 14 | 🇬🇷 GR | 963 |
| 15 | 🇨🇭 CH | 920 |
| 16 | 🇲🇾 MY | 835 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇹🇷 TR | 618 |
| 21 | 🇵🇭 PH | 613 |
| 22 | 🇬🇹 GT | 598 |
| 23 | 🇹🇭 TH | 597 |
| 24 | 🇰🇷 KR | 559 |
| 25 | 🇵🇱 PL | 515 |
| 26 | 🇲🇦 MA | 422 |
| 27 | 🇧🇸 BS | 338 |
| 28 | 🇲🇪 ME | 329 |
| 29 | 🇳🇱 NL | 320 |
| 30 | 🇮🇩 ID | 311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 779 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 579 |
| 4 | Denver International Airport |  | US | 553 |
| 5 | Indira Gandhi International Airport |  | IN | 543 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 471 |
| 7 | La Aurora Airport |  | GT | 435 |
| 8 | Harry Reid International Airport |  | US | 424 |
| 9 | Zurich Airport |  | CH | 411 |
| 10 | Guaymaral Airport |  | CO | 404 |
| 11 | Chicago O'Hare International Airport |  | US | 338 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 337 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 335 |
| 14 | Frankfurt am Main International Airport |  | DE | 325 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 307 |
| 18 | Madrid Barajas International Airport |  | ES | 302 |
| 19 | Charlotte/Douglas International Airport |  | US | 297 |
| 20 | Bengaluru International Airport |  | IN | 296 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 287 |
| 23 | Ninoy Aquino International Airport |  | PH | 284 |
| 24 | Malpensa International Airport |  | IT | 269 |
| 25 | Daniel K Inouye International Airport |  | US | 252 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 249 |
| 27 | Salt Lake City International Airport |  | US | 248 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 234 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 232 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 227 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 34 | O. R. Tambo International Airport |  | ZA | 223 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Barcelona International Airport |  | ES | 213 |
| 38 | Miami International Airport |  | US | 212 |
| 39 | Seattle-Tacoma International Airport |  | US | 203 |
| 40 | Don Mueang International Airport |  | TH | 202 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 136 | 14m | 114 km | 266.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 80 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 71 | 21m | 244 km | 299.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 52 | 20m | 147 km | 131.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 46 | 12m | 15 km | 12.1 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 45 | 1h 21m | 961 km | 745.9 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 45 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU958 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-04-13 20:02 UTC | 2026-04-13 20:28 UTC | 25m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-04-13 19:43 UTC | 2026-04-13 20:21 UTC | 37m |
| SHARP41 | SHA | 75OK (75OK) | Enix Airport (OK51) | 2026-04-13 19:45 UTC | 2026-04-13 20:10 UTC | 25m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-13 19:55 UTC | 2026-04-13 20:10 UTC | 14m |
| N52168 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-13 19:42 UTC | 2026-04-13 20:09 UTC | 27m |
| N110SQ |  | Concord-Padgett Regional Airport (KJQF) | Bradley Field (NC29) | 2026-04-13 20:01 UTC | 2026-04-13 20:09 UTC | 7m |
| FUSION52 | FUS | 2TX3 (2TX3) | 6TA4 (6TA4) | 2026-04-13 19:51 UTC | 2026-04-13 20:09 UTC | 17m |
| AFL1890 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-04-13 15:59 UTC | 2026-04-13 20:04 UTC | 4h 5m |
| STAB11 | STA | 75OK (75OK) | Good Life Ranch Airport (17OK) | 2026-04-13 19:20 UTC | 2026-04-13 19:58 UTC | 38m |
| N44996 |  | Sacramento Executive Airport (KSAC) | Franklin Field (KF72) | 2026-04-13 19:39 UTC | 2026-04-13 19:56 UTC | 16m |
| N426SD |  | Shishmaref Airport (PASH) | White Mountain Airport (PAWM) | 2026-04-13 19:30 UTC | 2026-04-13 19:54 UTC | 23m |
| CYO198 | CYO | Columbia Regional Airport (KCOU) | Airglades Airport (K2IS) | 2026-04-13 17:26 UTC | 2026-04-13 19:52 UTC | 2h 26m |
| N68BC |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-13 19:29 UTC | 2026-04-13 19:51 UTC | 21m |
| N282HV |  | 5TA4 (5TA4) | 2XA0 (2XA0) | 2026-04-13 19:31 UTC | 2026-04-13 19:48 UTC | 16m |
| SKW5310 | SkyWest Airlines | Denver International Airport (KDEN) | Ohkay Owingeh Airport (KE14) | 2026-04-13 18:59 UTC | 2026-04-13 19:42 UTC | 43m |
| N334AM |  | Cecil Ranch Airport (37CN) | Truckee-Tahoe Airport (KTRK) | 2026-04-13 19:07 UTC | 2026-04-13 19:42 UTC | 34m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-13 19:26 UTC | 2026-04-13 19:40 UTC | 14m |
| CRN511 | CRN | Kelowna Airport (CYLW) | Castlegar Airport (CYCG) | 2026-04-13 19:21 UTC | 2026-04-13 19:40 UTC | 18m |
| HK2978G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-13 19:10 UTC | 2026-04-13 19:40 UTC | 30m |
| N73498 |  | Lake Norman Airpark (K14A) | Welborn Farm Airport (3NC1) | 2026-04-13 19:19 UTC | 2026-04-13 19:40 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
