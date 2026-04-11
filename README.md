# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_18:11:15_UTC-green)

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

**Latest saved flight:** 2026-04-11 18:11:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 18:11:15 UTC

- **29,249** saved flights
- **13,550** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **29,249** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **355,615.9 tonnes** estimated CO2 emissions
- **20,615,417 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1201 |
| 2 | SkyWest Airlines | 1174 |
| 3 | IndiGo | 767 |
| 4 | EJA | 508 |
| 5 | American Airlines | 503 |
| 6 | Southwest Airlines | 416 |
| 7 | ENY | 389 |
| 8 | Lufthansa | 356 |
| 9 | AXM | 314 |
| 10 | Vueling | 301 |
| 11 | LATAM Airlines | 285 |
| 12 | All Nippon Airways | 263 |
| 13 | QLK | 254 |
| 14 | AZU | 252 |
| 15 | Delta Air Lines | 243 |
| 16 | LXJ | 235 |
| 17 | Swiss International | 216 |
| 18 | Alaska Airlines | 191 |
| 19 | EJU | 191 |
| 20 | Japan Airlines | 190 |
| 21 | VIV | 189 |
| 22 | easyJet | 188 |
| 23 | WIF | 187 |
| 24 | AEE | 184 |
| 25 | United Airlines | 174 |
| 26 | EDV | 172 |
| 27 | Avianca | 164 |
| 28 | JetBlue | 155 |
| 29 | Air France | 153 |
| 30 | AXB | 153 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23021 |
| 2 | 🇮🇳 IN | 2357 |
| 3 | 🇪🇸 ES | 2161 |
| 4 | 🇦🇺 AU | 2088 |
| 5 | 🇧🇷 BR | 1680 |
| 6 | 🇯🇵 JP | 1608 |
| 7 | 🇮🇹 IT | 1504 |
| 8 | 🇩🇪 DE | 1483 |
| 9 | 🇨🇴 CO | 1469 |
| 10 | 🇨🇦 CA | 1433 |
| 11 | 🇬🇧 GB | 1179 |
| 12 | 🇫🇷 FR | 1084 |
| 13 | 🇲🇽 MX | 930 |
| 14 | 🇬🇷 GR | 840 |
| 15 | 🇨🇭 CH | 835 |
| 16 | 🇲🇾 MY | 751 |
| 17 | 🇳🇿 NZ | 636 |
| 18 | 🇳🇴 NO | 630 |
| 19 | 🇿🇦 ZA | 609 |
| 20 | 🇵🇭 PH | 547 |
| 21 | 🇬🇹 GT | 541 |
| 22 | 🇹🇭 TH | 532 |
| 23 | 🇹🇷 TR | 529 |
| 24 | 🇰🇷 KR | 497 |
| 25 | 🇵🇱 PL | 443 |
| 26 | 🇲🇦 MA | 366 |
| 27 | 🇧🇸 BS | 310 |
| 28 | 🇲🇪 ME | 294 |
| 29 | 🇳🇱 NL | 284 |
| 30 | 🇮🇩 ID | 278 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 688 |
| 2 | Tokyo International Airport |  | JP | 540 |
| 3 | El Dorado International Airport |  | CO | 524 |
| 4 | Indira Gandhi International Airport |  | IN | 491 |
| 5 | Denver International Airport |  | US | 486 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 410 |
| 7 | La Aurora Airport |  | GT | 385 |
| 8 | Harry Reid International Airport |  | US | 372 |
| 9 | Zurich Airport |  | CH | 354 |
| 10 | Guaymaral Airport |  | CO | 344 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 305 |
| 12 | Chicago O'Hare International Airport |  | US | 300 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 299 |
| 14 | Frankfurt am Main International Airport |  | DE | 299 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 282 |
| 17 | Macau International Airport |  | MO | 269 |
| 18 | Bengaluru International Airport |  | IN | 268 |
| 19 | Charlotte/Douglas International Airport |  | US | 263 |
| 20 | Madrid Barajas International Airport |  | ES | 254 |
| 21 | Ninoy Aquino International Airport |  | PH | 251 |
| 22 | Tenerife Norte Airport |  | ES | 251 |
| 23 | Congonhas Airport |  | BR | 245 |
| 24 | Malpensa International Airport |  | IT | 230 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 227 |
| 26 | Daniel K Inouye International Airport |  | US | 222 |
| 27 | Salt Lake City International Airport |  | US | 222 |
| 28 | Reno/Tahoe International Airport |  | US | 214 |
| 29 | Charles de Gaulle International Airport |  | FR | 209 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 202 |
| 31 | Capua Airport |  | IT | 200 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 199 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 198 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 195 |
| 35 | Miami International Airport |  | US | 195 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Barcelona International Airport |  | ES | 187 |
| 38 | Vitoria/Foronda Airport |  | ES | 186 |
| 39 | Seattle-Tacoma International Airport |  | US | 182 |
| 40 | Don Mueang International Airport |  | TH | 179 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 139 | 1h 8m | 706 km | 1,692.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 133 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 121 | 14m | 114 km | 237.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 100 | 28m | 304 km | 524.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 86 | 1h 27m | 910 km | 1,349.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 74 | 19m | 165 km | 210.5 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 65 | 55m | 546 km | 612.0 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 62 | 9m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 60 | 27m | 275 km | 284.3 t |
| 16 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 56 | 31m | 369 km | 356.5 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 53 | 46m | 452 km | 413.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 52 | 52m | 556 km | 498.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 47 | 21m | 244 km | 197.9 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 47 | 13m | 99 km | 80.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 45 | 20m | 147 km | 113.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 41 | 1h 19m | 961 km | 679.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 40 | 12m | 15 km | 10.6 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 39 | 26m | 215 km | 144.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N862TW |  | Martin State Airport (KMTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-11 17:16 UTC | 2026-04-11 18:11 UTC | 54m |
| N4397Q |  | Dupage Airport (KDPA) | Schaumburg Regional Airport (K06C) | 2026-04-11 17:49 UTC | 2026-04-11 18:07 UTC | 18m |
| N2350E |  | Valkaria Airport (KX59) | Rlm Farms Airport (FD09) | 2026-04-11 17:21 UTC | 2026-04-11 18:06 UTC | 44m |
| NRL480 | NRL | Teterboro Airport (KTEB) | Toronto Pearson International Airport (CYYZ) | 2026-04-11 16:59 UTC | 2026-04-11 18:01 UTC | 1h 2m |
| CXK447 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-11 16:42 UTC | 2026-04-11 17:55 UTC | 1h 13m |
| N548EG |  | John Wayne/Orange County Airport (KSNA) | Hesperia Airport (KL26) | 2026-04-11 17:39 UTC | 2026-04-11 17:55 UTC | 15m |
| N479FG |  | Kissimmee Gateway Airport (KISM) | Macdill Afb Aux Field (KAGR) | 2026-04-11 17:28 UTC | 2026-04-11 17:54 UTC | 26m |
| N7GB |  | Miami Executive Airport (KTMB) | Chautauqua County/Dunkirk Airport (KDKK) | 2026-04-11 15:27 UTC | 2026-04-11 17:52 UTC | 2h 25m |
| N110SQ |  | Concord-Padgett Regional Airport (KJQF) | Mid-Carolina Regional Airport (KRUQ) | 2026-04-11 17:43 UTC | 2026-04-11 17:52 UTC | 8m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-11 17:23 UTC | 2026-04-11 17:49 UTC | 25m |
| N6333F |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-11 16:59 UTC | 2026-04-11 17:47 UTC | 47m |
| N916FT |  | Montgomery-Gibbs Executive Airport (KMYF) | Borrego Air Ranch Airport (58CL) | 2026-04-11 17:05 UTC | 2026-04-11 17:40 UTC | 35m |
| N337BG |  | Wood County Airport (K1G0) | 72OI (72OI) | 2026-04-11 17:25 UTC | 2026-04-11 17:39 UTC | 14m |
| N434BZ |  | Brandywine Regional Airport (KOQN) | Lehigh Valley International Airport (KABE) | 2026-04-11 17:14 UTC | 2026-04-11 17:39 UTC | 25m |
| JKY160 | JKY | RAF Woodvale (EGOW) | Hawarden Airport (EGNR) | 2026-04-11 17:12 UTC | 2026-04-11 17:38 UTC | 25m |
| N110SD |  | 36AZ (36AZ) | Mesa Gateway Airport (KIWA) | 2026-04-11 16:57 UTC | 2026-04-11 17:37 UTC | 40m |
| N734VX |  | Montgomery-Gibbs Executive Airport (KMYF) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-11 17:13 UTC | 2026-04-11 17:37 UTC | 23m |
| OAL3000 | OAL | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-11 17:14 UTC | 2026-04-11 17:34 UTC | 20m |
| N706PM |  | Phoenix Sky Harbor International Airport (KPHX) | Chapman Ranch Airstrip (58AZ) | 2026-04-11 17:10 UTC | 2026-04-11 17:34 UTC | 23m |
| AOJ98T | AOJ | Shenzhen Bao'an International Airport (ZGSZ) | UKFB (UKFB) | 2026-04-11 07:18 UTC | 2026-04-11 17:34 UTC | 10h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
