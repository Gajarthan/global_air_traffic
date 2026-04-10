# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_16:20:52_UTC-green)

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

**Latest saved flight:** 2026-04-10 16:20:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 16:20:52 UTC

- **27,031** saved flights
- **12,774** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,031** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **330,738.4 tonnes** estimated CO2 emissions
- **19,173,239 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1110 |
| 2 | SkyWest Airlines | 1092 |
| 3 | IndiGo | 730 |
| 4 | American Airlines | 475 |
| 5 | EJA | 475 |
| 6 | Southwest Airlines | 383 |
| 7 | ENY | 358 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 275 |
| 11 | LATAM Airlines | 265 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 223 |
| 15 | AZU | 220 |
| 16 | LXJ | 219 |
| 17 | Swiss International | 189 |
| 18 | Alaska Airlines | 180 |
| 19 | VIV | 178 |
| 20 | easyJet | 177 |
| 21 | Japan Airlines | 177 |
| 22 | WIF | 177 |
| 23 | AEE | 175 |
| 24 | EJU | 173 |
| 25 | United Airlines | 159 |
| 26 | EDV | 158 |
| 27 | Avianca | 152 |
| 28 | AXB | 147 |
| 29 | JetBlue | 143 |
| 30 | Air France | 140 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21159 |
| 2 | 🇮🇳 IN | 2241 |
| 3 | 🇪🇸 ES | 2009 |
| 4 | 🇦🇺 AU | 1996 |
| 5 | 🇧🇷 BR | 1527 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇩🇪 DE | 1379 |
| 8 | 🇮🇹 IT | 1367 |
| 9 | 🇨🇴 CO | 1352 |
| 10 | 🇨🇦 CA | 1282 |
| 11 | 🇬🇧 GB | 1087 |
| 12 | 🇫🇷 FR | 1012 |
| 13 | 🇲🇽 MX | 856 |
| 14 | 🇬🇷 GR | 789 |
| 15 | 🇨🇭 CH | 745 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 595 |
| 19 | 🇿🇦 ZA | 564 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 503 |
| 22 | 🇬🇹 GT | 498 |
| 23 | 🇹🇭 TH | 479 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 412 |
| 26 | 🇲🇦 MA | 334 |
| 27 | 🇧🇸 BS | 284 |
| 28 | 🇲🇪 ME | 271 |
| 29 | 🇳🇱 NL | 268 |
| 30 | 🇮🇩 ID | 266 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 634 |
| 2 | Tokyo International Airport |  | JP | 500 |
| 3 | El Dorado International Airport |  | CO | 495 |
| 4 | Indira Gandhi International Airport |  | IN | 465 |
| 5 | Denver International Airport |  | US | 453 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 383 |
| 7 | Harry Reid International Airport |  | US | 349 |
| 8 | La Aurora Airport |  | GT | 346 |
| 9 | Zurich Airport |  | CH | 319 |
| 10 | Guaymaral Airport |  | CO | 291 |
| 11 | Frankfurt am Main International Airport |  | DE | 289 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 280 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 14 | Chicago O'Hare International Airport |  | US | 275 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 270 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Bengaluru International Airport |  | IN | 249 |
| 19 | Charlotte/Douglas International Airport |  | US | 246 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 232 |
| 22 | Madrid Barajas International Airport |  | ES | 231 |
| 23 | Congonhas Airport |  | BR | 212 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 211 |
| 25 | Malpensa International Airport |  | IT | 211 |
| 26 | Salt Lake City International Airport |  | US | 208 |
| 27 | Daniel K Inouye International Airport |  | US | 202 |
| 28 | Reno/Tahoe International Airport |  | US | 195 |
| 29 | Charles de Gaulle International Airport |  | FR | 194 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 187 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 186 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 181 |
| 33 | Miami International Airport |  | US | 180 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 179 |
| 35 | O. R. Tambo International Airport |  | ZA | 178 |
| 36 | Barcelona International Airport |  | ES | 174 |
| 37 | Vitoria/Foronda Airport |  | ES | 170 |
| 38 | Seattle-Tacoma International Airport |  | US | 169 |
| 39 | Capua Airport |  | IT | 168 |
| 40 | Don Mueang International Airport |  | TH | 167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 109 | 14m | 114 km | 213.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 109 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 72 | 21m | 99 km | 123.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
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
| ERU468 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-04-10 15:54 UTC | 2026-04-10 16:20 UTC | 25m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-10 16:04 UTC | 2026-04-10 16:16 UTC | 12m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-04-10 16:02 UTC | 2026-04-10 16:16 UTC | 13m |
| N56619 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-10 15:56 UTC | 2026-04-10 16:13 UTC | 17m |
| N734M |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-10 15:40 UTC | 2026-04-10 16:11 UTC | 31m |
| SLG3 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-10 15:39 UTC | 2026-04-10 16:11 UTC | 32m |
| LBQ600 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-10 14:48 UTC | 2026-04-10 16:02 UTC | 1h 14m |
| BNI5W | BNI | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-10 15:02 UTC | 2026-04-10 16:02 UTC | 1h 0m |
| RYR4KF | Ryanair | Verona / Villafranca Airport (LIPX) | Trapani / Birgi Airport (LICT) | 2026-04-10 14:57 UTC | 2026-04-10 15:59 UTC | 1h 1m |
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-04-10 14:14 UTC | 2026-04-10 15:58 UTC | 1h 44m |
| N240TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-10 15:24 UTC | 2026-04-10 15:58 UTC | 34m |
| HBKMW | HBK | Locarno Airport (LSZL) | Lugano Airport (LSZA) | 2026-04-10 15:25 UTC | 2026-04-10 15:55 UTC | 30m |
| N769SP |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Allison Farm Airport (XA34) | 2026-04-10 15:35 UTC | 2026-04-10 15:52 UTC | 17m |
| OHFMZ | OHF | Immola Airport (EFIM) | Immola Airport (EFIM) | 2026-04-10 15:42 UTC | 2026-04-10 15:48 UTC | 5m |
|  |  | Williams Field (11FL) | Tallahassee International Airport (KTLH) | 2026-04-10 13:45 UTC | 2026-04-10 15:45 UTC | 2h 0m |
| DAWG01 | DAW | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-10 14:39 UTC | 2026-04-10 15:44 UTC | 1h 5m |
| N366EA |  | Glendale Regional Airport (KGEU) | AZ86 (AZ86) | 2026-04-10 14:54 UTC | 2026-04-10 15:42 UTC | 47m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-10 15:26 UTC | 2026-04-10 15:42 UTC | 16m |
| LXJ537 | LXJ | Marina Municipal Airport (KOAR) | Truckee-Tahoe Airport (KTRK) | 2026-04-10 15:13 UTC | 2026-04-10 15:40 UTC | 27m |
| AAL2254 | American Airlines | Chicago O'Hare International Airport (KORD) | Harry Reid International Airport (KLAS) | 2026-04-10 12:03 UTC | 2026-04-10 15:39 UTC | 3h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
