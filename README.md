# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_15:45:03_UTC-green)

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

**Latest saved flight:** 2026-04-13 15:45:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 15:45:03 UTC

- **32,385** saved flights
- **14,558** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,385** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **398,400.5 tonnes** estimated CO2 emissions
- **23,095,681 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1374 |
| 2 | SkyWest Airlines | 1299 |
| 3 | IndiGo | 835 |
| 4 | EJA | 565 |
| 5 | American Airlines | 557 |
| 6 | Southwest Airlines | 467 |
| 7 | ENY | 432 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 344 |
| 10 | Vueling | 329 |
| 11 | LATAM Airlines | 327 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 287 |
| 14 | Delta Air Lines | 268 |
| 15 | QLK | 266 |
| 16 | LXJ | 256 |
| 17 | Swiss International | 248 |
| 18 | WIF | 219 |
| 19 | EJU | 216 |
| 20 | Alaska Airlines | 215 |
| 21 | easyJet | 214 |
| 22 | VIV | 208 |
| 23 | AEE | 206 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | Air France | 174 |
| 28 | GLO | 174 |
| 29 | Avianca | 172 |
| 30 | JetBlue | 172 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25321 |
| 2 | 🇮🇳 IN | 2552 |
| 3 | 🇪🇸 ES | 2436 |
| 4 | 🇦🇺 AU | 2252 |
| 5 | 🇧🇷 BR | 1910 |
| 6 | 🇯🇵 JP | 1778 |
| 7 | 🇮🇹 IT | 1721 |
| 8 | 🇩🇪 DE | 1650 |
| 9 | 🇨🇴 CO | 1614 |
| 10 | 🇨🇦 CA | 1570 |
| 11 | 🇬🇧 GB | 1328 |
| 12 | 🇫🇷 FR | 1203 |
| 13 | 🇲🇽 MX | 1029 |
| 14 | 🇬🇷 GR | 944 |
| 15 | 🇨🇭 CH | 913 |
| 16 | 🇲🇾 MY | 834 |
| 17 | 🇳🇴 NO | 735 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 671 |
| 20 | 🇵🇭 PH | 612 |
| 21 | 🇹🇷 TR | 599 |
| 22 | 🇹🇭 TH | 596 |
| 23 | 🇬🇹 GT | 593 |
| 24 | 🇰🇷 KR | 559 |
| 25 | 🇵🇱 PL | 503 |
| 26 | 🇲🇦 MA | 419 |
| 27 | 🇧🇸 BS | 336 |
| 28 | 🇲🇪 ME | 323 |
| 29 | 🇳🇱 NL | 313 |
| 30 | 🇮🇩 ID | 311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 767 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 572 |
| 4 | Indira Gandhi International Airport |  | IN | 541 |
| 5 | Denver International Airport |  | US | 540 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 462 |
| 7 | La Aurora Airport |  | GT | 430 |
| 8 | Harry Reid International Airport |  | US | 420 |
| 9 | Zurich Airport |  | CH | 405 |
| 10 | Guaymaral Airport |  | CO | 394 |
| 11 | Chicago O'Hare International Airport |  | US | 333 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 328 |
| 14 | Frankfurt am Main International Airport |  | DE | 323 |
| 15 | Kuala Lumpur International Airport |  | MY | 320 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 305 |
| 18 | Madrid Barajas International Airport |  | ES | 295 |
| 19 | Bengaluru International Airport |  | IN | 294 |
| 20 | Charlotte/Douglas International Airport |  | US | 292 |
| 21 | Tenerife Norte Airport |  | ES | 288 |
| 22 | Ninoy Aquino International Airport |  | PH | 283 |
| 23 | Congonhas Airport |  | BR | 280 |
| 24 | Malpensa International Airport |  | IT | 262 |
| 25 | Daniel K Inouye International Airport |  | US | 247 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 245 |
| 27 | Salt Lake City International Airport |  | US | 245 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 236 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 231 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 225 |
| 32 | Capua Airport |  | IT | 224 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 223 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 220 |
| 35 | O. R. Tambo International Airport |  | ZA | 219 |
| 36 | Vitoria/Foronda Airport |  | ES | 217 |
| 37 | Miami International Airport |  | US | 212 |
| 38 | Barcelona International Airport |  | ES | 207 |
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
| 14 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 68 | 21m | 244 km | 286.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 56 | 20m | 250 km | 241.9 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 51 | 1h 41m | 1,423 km | 1,251.6 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 45 | 12m | 15 km | 11.9 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 45 | 1h 21m | 961 km | 745.9 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N264SF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-13 15:11 UTC | 2026-04-13 15:45 UTC | 33m |
| N435GG |  | Grassy Meadows/Sky Ranch Landowners Assn Airport (UT47) | Telluride Regional Airport (KTEX) | 2026-04-13 14:46 UTC | 2026-04-13 15:34 UTC | 48m |
| SKW4888 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Bermuda Dunes Airport (KUDD) | 2026-04-13 15:06 UTC | 2026-04-13 15:28 UTC | 21m |
| N480LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-13 14:30 UTC | 2026-04-13 15:21 UTC | 50m |
| N766LF |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Coastal Carolina Regional Airport (KEWN) | 2026-04-13 14:58 UTC | 2026-04-13 15:18 UTC | 20m |
| N139PS |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-13 15:12 UTC | 2026-04-13 15:16 UTC | 3m |
| N478LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-13 14:23 UTC | 2026-04-13 15:14 UTC | 51m |
| PDU67 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-13 14:50 UTC | 2026-04-13 15:10 UTC | 19m |
| LYRE71 | LYR | Burris Ranch Airport (2TE6) | Burris Ranch Airport (2TE6) | 2026-04-13 14:42 UTC | 2026-04-13 15:06 UTC | 24m |
| N79BA |  | Lancaster Airport (KLNS) | Donegal Springs Airpark (KN71) | 2026-04-13 14:51 UTC | 2026-04-13 15:04 UTC | 12m |
| LUZON41 | LUZ | Bailey Airport (2TS8) | Bailey Airport (2TS8) | 2026-04-13 14:43 UTC | 2026-04-13 15:03 UTC | 19m |
| N53265 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-13 14:40 UTC | 2026-04-13 15:03 UTC | 23m |
| HBKGO | HBK | Bern Belp Airport (LSZB) | Bern Belp Airport (LSZB) | 2026-04-13 14:36 UTC | 2026-04-13 15:01 UTC | 25m |
| PPJCA | PPJ | Campo de Marte Airport (SBMT) | Campo Fontenelle Airport (SBYS) | 2026-04-13 14:24 UTC | 2026-04-13 14:59 UTC | 35m |
| N50TT |  | Van Nuys Airport (KVNY) | Visalia Municipal Airport (KVIS) | 2026-04-13 14:26 UTC | 2026-04-13 14:58 UTC | 32m |
| N699GG |  | Sundance Airport (KHSD) | Morrilton Airport (07AR) | 2026-04-13 14:22 UTC | 2026-04-13 14:58 UTC | 35m |
| N330DK |  | Jim Hamilton L B Owens Airport (KCUB) | Quanah Municipal Airport (KF01) | 2026-04-13 11:43 UTC | 2026-04-13 14:55 UTC | 3h 12m |
| RPA5733 | Republic Airways | John F Kennedy International Airport (KJFK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-13 14:13 UTC | 2026-04-13 14:54 UTC | 40m |
| NDU646 | NDU | Mesa Gateway Airport (KIWA) | Tombstone Municipal Airport (KP29) | 2026-04-13 13:27 UTC | 2026-04-13 14:53 UTC | 1h 26m |
| IGO266K | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-13 14:08 UTC | 2026-04-13 14:51 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
