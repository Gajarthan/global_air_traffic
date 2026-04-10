# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_18:18:34_UTC-green)

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

**Latest saved flight:** 2026-04-10 18:18:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 18:18:34 UTC

- **27,246** saved flights
- **12,858** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,246** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **332,668.7 tonnes** estimated CO2 emissions
- **19,285,143 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1118 |
| 2 | SkyWest Airlines | 1102 |
| 3 | IndiGo | 733 |
| 4 | EJA | 479 |
| 5 | American Airlines | 478 |
| 6 | Southwest Airlines | 385 |
| 7 | ENY | 361 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 279 |
| 11 | LATAM Airlines | 265 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 224 |
| 15 | AZU | 221 |
| 16 | LXJ | 221 |
| 17 | Swiss International | 191 |
| 18 | Alaska Airlines | 181 |
| 19 | AEE | 178 |
| 20 | easyJet | 178 |
| 21 | VIV | 178 |
| 22 | Japan Airlines | 177 |
| 23 | WIF | 177 |
| 24 | EJU | 175 |
| 25 | EDV | 160 |
| 26 | United Airlines | 160 |
| 27 | Avianca | 154 |
| 28 | AXB | 147 |
| 29 | JetBlue | 145 |
| 30 | Air France | 141 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21400 |
| 2 | 🇮🇳 IN | 2249 |
| 3 | 🇪🇸 ES | 2024 |
| 4 | 🇦🇺 AU | 1996 |
| 5 | 🇧🇷 BR | 1531 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇩🇪 DE | 1385 |
| 8 | 🇮🇹 IT | 1378 |
| 9 | 🇨🇴 CO | 1363 |
| 10 | 🇨🇦 CA | 1305 |
| 11 | 🇬🇧 GB | 1105 |
| 12 | 🇫🇷 FR | 1016 |
| 13 | 🇲🇽 MX | 863 |
| 14 | 🇬🇷 GR | 795 |
| 15 | 🇨🇭 CH | 747 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 595 |
| 19 | 🇿🇦 ZA | 564 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 506 |
| 22 | 🇬🇹 GT | 500 |
| 23 | 🇹🇭 TH | 480 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 416 |
| 26 | 🇲🇦 MA | 336 |
| 27 | 🇧🇸 BS | 288 |
| 28 | 🇲🇪 ME | 273 |
| 29 | 🇳🇱 NL | 269 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 641 |
| 2 | Tokyo International Airport |  | JP | 500 |
| 3 | El Dorado International Airport |  | CO | 498 |
| 4 | Indira Gandhi International Airport |  | IN | 466 |
| 5 | Denver International Airport |  | US | 453 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 387 |
| 7 | Harry Reid International Airport |  | US | 349 |
| 8 | La Aurora Airport |  | GT | 347 |
| 9 | Zurich Airport |  | CH | 321 |
| 10 | Guaymaral Airport |  | CO | 297 |
| 11 | Frankfurt am Main International Airport |  | DE | 289 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 285 |
| 13 | Chicago O'Hare International Airport |  | US | 279 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 273 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Bengaluru International Airport |  | IN | 251 |
| 19 | Charlotte/Douglas International Airport |  | US | 248 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Madrid Barajas International Airport |  | ES | 233 |
| 22 | Tenerife Norte Airport |  | ES | 233 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 215 |
| 24 | Malpensa International Airport |  | IT | 215 |
| 25 | Congonhas Airport |  | BR | 213 |
| 26 | Salt Lake City International Airport |  | US | 208 |
| 27 | Daniel K Inouye International Airport |  | US | 206 |
| 28 | Reno/Tahoe International Airport |  | US | 197 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 187 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 186 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 183 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 183 |
| 34 | Miami International Airport |  | US | 183 |
| 35 | O. R. Tambo International Airport |  | ZA | 178 |
| 36 | Barcelona International Airport |  | ES | 175 |
| 37 | Vitoria/Foronda Airport |  | ES | 172 |
| 38 | Capua Airport |  | IT | 171 |
| 39 | Seattle-Tacoma International Airport |  | US | 170 |
| 40 | Don Mueang International Airport |  | TH | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 112 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 110 | 14m | 114 km | 215.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 72 | 21m | 99 km | 123.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 55 | 27m | 275 km | 260.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 18 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 47 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-10 17:50 UTC | 2026-04-10 18:18 UTC | 27m |
| N628CT |  | Dubuque Regional Airport (KDBQ) | Platteville Municipal Airport (KPVB) | 2026-04-10 17:58 UTC | 2026-04-10 18:14 UTC | 16m |
| N872SP |  | Trenton Mercer Airport (KTTN) | Heritage Field (KPTW) | 2026-04-10 17:43 UTC | 2026-04-10 18:14 UTC | 31m |
| N284HG |  | Denton Enterprise Airport (KDTO) | Richards Airport (TA47) | 2026-04-10 17:08 UTC | 2026-04-10 17:57 UTC | 49m |
| N478LP |  | Glendale Regional Airport (KGEU) | AZ86 (AZ86) | 2026-04-10 17:12 UTC | 2026-04-10 17:56 UTC | 44m |
| N886SH |  | Marshfield Municipal Airport (KMFI) | Dubuque Regional Airport (KDBQ) | 2026-04-10 17:07 UTC | 2026-04-10 17:55 UTC | 47m |
| N20597 |  | Lancaster Airport (KLNS) | 6PA9 (6PA9) | 2026-04-10 17:07 UTC | 2026-04-10 17:53 UTC | 45m |
| N486LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-10 17:07 UTC | 2026-04-10 17:53 UTC | 45m |
| N94626 |  | Warsaw Municipal Airport (KASW) | Warsaw Municipal Airport (KASW) | 2026-04-10 17:45 UTC | 2026-04-10 17:53 UTC | 7m |
| CFMCN | CFM | Vancouver International Airport (CYVR) | Schmidt Ranch Airport (1WN0) | 2026-04-10 16:59 UTC | 2026-04-10 17:52 UTC | 53m |
| N79975 |  | Princeton Airport (K39N) | Paramount Air Airport (JY04) | 2026-04-10 16:58 UTC | 2026-04-10 17:49 UTC | 51m |
| N511PC |  | St Pete-Clearwater International Airport (KPIE) | St Pete-Clearwater International Airport (KPIE) | 2026-04-10 17:27 UTC | 2026-04-10 17:48 UTC | 21m |
| NIT269 | NIT | Baldwin County Regional Airport (KMLJ) | W H 'Bud' Barron Airport (KDBN) | 2026-04-10 17:17 UTC | 2026-04-10 17:47 UTC | 30m |
| LLN101 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | 5TS4 (5TS4) | 2026-04-10 17:33 UTC | 2026-04-10 17:47 UTC | 13m |
| CGBVV | CGB | Boundary Bay Airport (CZBB) | Pitt Meadows Airport (CYPK) | 2026-04-10 17:34 UTC | 2026-04-10 17:45 UTC | 10m |
|  |  | Robertson Field (K4B8) | Robertson Field (K4B8) | 2026-04-10 17:43 UTC | 2026-04-10 17:44 UTC | 0m |
| LXJ531 | LXJ | Lawrence Regional Airport (KLWC) | 9LA2 (9LA2) | 2026-04-10 16:36 UTC | 2026-04-10 17:41 UTC | 1h 4m |
| CRN911 | CRN | Kelowna Airport (CYLW) | Crawford Bay Airport (CAR2) | 2026-04-10 17:13 UTC | 2026-04-10 17:39 UTC | 25m |
| FAM5208 | FAM | Tizayuca Airport (MM28) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-10 17:01 UTC | 2026-04-10 17:39 UTC | 37m |
| N243SD |  | Brookings Regional Airport (KBKX) | Huron Regional Airport (KHON) | 2026-04-10 17:11 UTC | 2026-04-10 17:37 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
