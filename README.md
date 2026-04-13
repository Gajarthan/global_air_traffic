# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_16:59:17_UTC-green)

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

**Latest saved flight:** 2026-04-13 16:59:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 16:59:17 UTC

- **32,535** saved flights
- **14,628** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,535** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **399,963.8 tonnes** estimated CO2 emissions
- **23,186,309 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1384 |
| 2 | SkyWest Airlines | 1303 |
| 3 | IndiGo | 837 |
| 4 | EJA | 569 |
| 5 | American Airlines | 560 |
| 6 | Southwest Airlines | 468 |
| 7 | ENY | 434 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 344 |
| 10 | Vueling | 331 |
| 11 | LATAM Airlines | 328 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 288 |
| 14 | Delta Air Lines | 270 |
| 15 | QLK | 266 |
| 16 | LXJ | 262 |
| 17 | Swiss International | 248 |
| 18 | WIF | 223 |
| 19 | EJU | 218 |
| 20 | Alaska Airlines | 216 |
| 21 | easyJet | 216 |
| 22 | VIV | 211 |
| 23 | AEE | 209 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 189 |
| 26 | United Airlines | 185 |
| 27 | Air France | 177 |
| 28 | GLO | 175 |
| 29 | Avianca | 172 |
| 30 | JetBlue | 172 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25453 |
| 2 | 🇮🇳 IN | 2558 |
| 3 | 🇪🇸 ES | 2448 |
| 4 | 🇦🇺 AU | 2252 |
| 5 | 🇧🇷 BR | 1916 |
| 6 | 🇯🇵 JP | 1778 |
| 7 | 🇮🇹 IT | 1735 |
| 8 | 🇩🇪 DE | 1654 |
| 9 | 🇨🇴 CO | 1620 |
| 10 | 🇨🇦 CA | 1579 |
| 11 | 🇬🇧 GB | 1336 |
| 12 | 🇫🇷 FR | 1213 |
| 13 | 🇲🇽 MX | 1036 |
| 14 | 🇬🇷 GR | 951 |
| 15 | 🇨🇭 CH | 914 |
| 16 | 🇲🇾 MY | 834 |
| 17 | 🇳🇴 NO | 742 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 680 |
| 20 | 🇵🇭 PH | 613 |
| 21 | 🇹🇷 TR | 605 |
| 22 | 🇹🇭 TH | 596 |
| 23 | 🇬🇹 GT | 593 |
| 24 | 🇰🇷 KR | 559 |
| 25 | 🇵🇱 PL | 509 |
| 26 | 🇲🇦 MA | 421 |
| 27 | 🇧🇸 BS | 336 |
| 28 | 🇲🇪 ME | 324 |
| 29 | 🇳🇱 NL | 315 |
| 30 | 🇮🇩 ID | 311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 772 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 574 |
| 4 | Denver International Airport |  | US | 542 |
| 5 | Indira Gandhi International Airport |  | IN | 542 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 464 |
| 7 | La Aurora Airport |  | GT | 430 |
| 8 | Harry Reid International Airport |  | US | 422 |
| 9 | Zurich Airport |  | CH | 405 |
| 10 | Guaymaral Airport |  | CO | 396 |
| 11 | Chicago O'Hare International Airport |  | US | 333 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 331 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 329 |
| 14 | Frankfurt am Main International Airport |  | DE | 324 |
| 15 | Kuala Lumpur International Airport |  | MY | 320 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 306 |
| 18 | Madrid Barajas International Airport |  | ES | 297 |
| 19 | Bengaluru International Airport |  | IN | 295 |
| 20 | Charlotte/Douglas International Airport |  | US | 292 |
| 21 | Tenerife Norte Airport |  | ES | 288 |
| 22 | Ninoy Aquino International Airport |  | PH | 284 |
| 23 | Congonhas Airport |  | BR | 282 |
| 24 | Malpensa International Airport |  | IT | 265 |
| 25 | Daniel K Inouye International Airport |  | US | 249 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 248 |
| 27 | Salt Lake City International Airport |  | US | 247 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 239 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 232 |
| 31 | Capua Airport |  | IT | 227 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 224 |
| 34 | O. R. Tambo International Airport |  | ZA | 223 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 220 |
| 36 | Vitoria/Foronda Airport |  | ES | 218 |
| 37 | Miami International Airport |  | US | 212 |
| 38 | Barcelona International Airport |  | ES | 208 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Don Mueang International Airport |  | TH | 201 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 153 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 135 | 14m | 114 km | 264.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 78 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 72 | 27m | 275 km | 341.2 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 69 | 21m | 244 km | 290.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 51 | 1h 41m | 1,423 km | 1,251.6 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 46 | 12m | 15 km | 12.1 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 45 | 1h 21m | 961 km | 745.9 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC5QS | Air India | Netaji Subhash Chandra Bose International Airport (VECC) | Bakshi Ka Talab Air Force Station (VIBL) | 2026-04-13 15:38 UTC | 2026-04-13 16:59 UTC | 1h 20m |
| BOMR843 | BOM | Farm Services Inc Airport (XS64) | Waldron Field Nolf Airport (KNWL) | 2026-04-13 16:34 UTC | 2026-04-13 16:58 UTC | 23m |
| TVR4701 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-13 10:14 UTC | 2026-04-13 16:53 UTC | 6h 39m |
| LXJ447 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | San Francisco International Airport (KSFO) | 2026-04-13 16:27 UTC | 2026-04-13 16:52 UTC | 25m |
| BLZR275 | BLZ | Shofner Farms Airport (2TS2) | El Coyote Ranch Airport (2TA8) | 2026-04-13 16:33 UTC | 2026-04-13 16:47 UTC | 14m |
| N712JJ |  | K3M3 (K3M3) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-13 15:44 UTC | 2026-04-13 16:45 UTC | 1h 1m |
| IOZZP | IOZ | Bologna / Borgo Panigale Airport (LIPE) | Bologna / Borgo Panigale Airport (LIPE) | 2026-04-13 16:16 UTC | 2026-04-13 16:43 UTC | 27m |
| CXK318 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-13 16:10 UTC | 2026-04-13 16:36 UTC | 26m |
| ERU820 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-04-13 15:15 UTC | 2026-04-13 16:34 UTC | 1h 19m |
| N395WJ |  | Centennial Airport (KAPA) | Prentice Airport (K5N2) | 2026-04-13 14:57 UTC | 2026-04-13 16:34 UTC | 1h 37m |
| CGTSN | CGT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-04-13 15:10 UTC | 2026-04-13 16:32 UTC | 1h 21m |
| N525US |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-04-13 16:01 UTC | 2026-04-13 16:26 UTC | 24m |
| EPI232 | EPI | KFTG (KFTG) | KFTG (KFTG) | 2026-04-13 16:06 UTC | 2026-04-13 16:22 UTC | 16m |
| N9968L |  | Stanly County Airport (KVUJ) | Stanly County Airport (KVUJ) | 2026-04-13 16:14 UTC | 2026-04-13 16:21 UTC | 7m |
| ASL63P | ASL | Belgrade Nikola Tesla Airport (LYBE) | Tuzla International Airport (LQTZ) | 2026-04-13 15:47 UTC | 2026-04-13 16:17 UTC | 30m |
| YV3153 |  | General Manuel Carlos Piar International Airport (SVPR) | Guasipati Airport (SVGT) | 2026-04-13 16:01 UTC | 2026-04-13 16:16 UTC | 15m |
| ASA1003 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Lihue Airport (PHLI) | 2026-04-13 15:55 UTC | 2026-04-13 16:11 UTC | 15m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-04-13 15:45 UTC | 2026-04-13 16:10 UTC | 25m |
| N446BB |  | 65XS (65XS) | 5TX4 (5TX4) | 2026-04-13 15:43 UTC | 2026-04-13 16:10 UTC | 27m |
| RYR2FF | Ryanair | London Stansted Airport (EGSS) | Malpensa International Airport (LIMC) | 2026-04-13 14:36 UTC | 2026-04-13 16:10 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
