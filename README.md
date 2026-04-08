# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_11:44:42_UTC-green)

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

**Latest saved flight:** 2026-04-08 11:44:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 11:44:42 UTC

- **23,198** saved flights
- **11,281** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,198** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **288,124.1 tonnes** estimated CO2 emissions
- **16,702,846 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 962 |
| 3 | IndiGo | 654 |
| 4 | EJA | 422 |
| 5 | American Airlines | 421 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 297 |
| 9 | Vueling | 242 |
| 10 | AXM | 241 |
| 11 | LATAM Airlines | 231 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 200 |
| 15 | LXJ | 189 |
| 16 | AZU | 183 |
| 17 | Swiss International | 171 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 158 |
| 22 | EJU | 152 |
| 23 | United Airlines | 147 |
| 24 | AEE | 146 |
| 25 | WIF | 142 |
| 26 | Avianca | 139 |
| 27 | EDV | 135 |
| 28 | AXB | 132 |
| 29 | Air France | 124 |
| 30 | ANZ | 118 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18029 |
| 2 | 🇮🇳 IN | 1987 |
| 3 | 🇪🇸 ES | 1793 |
| 4 | 🇦🇺 AU | 1746 |
| 5 | 🇯🇵 JP | 1347 |
| 6 | 🇧🇷 BR | 1296 |
| 7 | 🇮🇹 IT | 1188 |
| 8 | 🇨🇴 CO | 1181 |
| 9 | 🇩🇪 DE | 1173 |
| 10 | 🇨🇦 CA | 1034 |
| 11 | 🇬🇧 GB | 932 |
| 12 | 🇫🇷 FR | 856 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 672 |
| 15 | 🇨🇭 CH | 644 |
| 16 | 🇲🇾 MY | 570 |
| 17 | 🇿🇦 ZA | 504 |
| 18 | 🇳🇿 NZ | 497 |
| 19 | 🇳🇴 NO | 493 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇹🇷 TR | 444 |
| 22 | 🇵🇭 PH | 444 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 377 |
| 25 | 🇵🇱 PL | 340 |
| 26 | 🇲🇦 MA | 282 |
| 27 | 🇮🇩 ID | 250 |
| 28 | 🇧🇸 BS | 243 |
| 29 | 🇲🇪 ME | 240 |
| 30 | 🇳🇱 NL | 235 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 551 |
| 2 | Tokyo International Airport |  | JP | 448 |
| 3 | El Dorado International Airport |  | CO | 442 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 406 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 326 |
| 7 | La Aurora Airport |  | GT | 322 |
| 8 | Harry Reid International Airport |  | US | 309 |
| 9 | Zurich Airport |  | CH | 283 |
| 10 | Frankfurt am Main International Airport |  | DE | 258 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 14 | Chicago O'Hare International Airport |  | US | 238 |
| 15 | Guaymaral Airport |  | CO | 236 |
| 16 | Macau International Airport |  | MO | 224 |
| 17 | Bengaluru International Airport |  | IN | 222 |
| 18 | Charlotte/Douglas International Airport |  | US | 214 |
| 19 | Madrid Barajas International Airport |  | ES | 208 |
| 20 | Kuala Lumpur International Airport |  | MY | 207 |
| 21 | Tenerife Norte Airport |  | ES | 206 |
| 22 | Ninoy Aquino International Airport |  | PH | 204 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Malpensa International Airport |  | IT | 189 |
| 25 | Congonhas Airport |  | BR | 188 |
| 26 | Salt Lake City International Airport |  | US | 182 |
| 27 | Daniel K Inouye International Airport |  | US | 177 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Charles de Gaulle International Airport |  | FR | 172 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 156 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 156 |
| 34 | O. R. Tambo International Airport |  | ZA | 156 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 36 | Pune Airport |  | IN | 152 |
| 37 | Seattle-Tacoma International Airport |  | US | 150 |
| 38 | Vitoria/Foronda Airport |  | ES | 150 |
| 39 | Barcelona International Airport |  | ES | 148 |
| 40 | Gimpo International Airport |  | KR | 141 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 57 | 19m | 165 km | 162.1 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 43 | 20m | 250 km | 185.7 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 34 | 20m | 147 km | 86.0 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PHSVD | PHS | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-04-08 11:18 UTC | 2026-04-08 11:44 UTC | 26m |
| DEGTQ | DEG | Babenhausen Airport (EDEF) | Babenhausen Airport (EDEF) | 2026-04-08 11:04 UTC | 2026-04-08 11:21 UTC | 17m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 10:56 UTC | 2026-04-08 11:20 UTC | 24m |
| N2666U |  | Decatur Municipal Airport (KLUD) | Bridgeport Municipal Airport (KXBP) | 2026-04-08 10:18 UTC | 2026-04-08 11:13 UTC | 55m |
| DLH1UL | Lufthansa | Budapest Ferenc Liszt International Airport (LHBP) | Frankfurt am Main International Airport (EDDF) | 2026-04-08 09:48 UTC | 2026-04-08 11:13 UTC | 1h 24m |
| LLR831 | LLR | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-04-08 10:40 UTC | 2026-04-08 11:10 UTC | 29m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 10:47 UTC | 2026-04-08 11:10 UTC | 23m |
| DHK814 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-08 00:27 UTC | 2026-04-08 11:05 UTC | 10h 37m |
| YGZ | YGZ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-08 10:38 UTC | 2026-04-08 11:03 UTC | 24m |
| N615FB |  | Smyrna Airport (KMQY) | Meadowlake Airport (12TN) | 2026-04-08 10:43 UTC | 2026-04-08 11:01 UTC | 18m |
| EJU63PB | EJU | Nantes Atlantique Airport (LFRS) | Václav Havel Airport (LKPR) | 2026-04-08 09:04 UTC | 2026-04-08 11:00 UTC | 1h 55m |
| RYR8XK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Crotone Airport (LIBC) | 2026-04-08 09:52 UTC | 2026-04-08 10:58 UTC | 1h 5m |
| EQN | EQN | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-04-08 10:18 UTC | 2026-04-08 10:57 UTC | 39m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-08 10:40 UTC | 2026-04-08 10:53 UTC | 13m |
| DEKSD | DEK | Augsburg Airport (EDMA) | Augsburg Airport (EDMA) | 2026-04-08 09:17 UTC | 2026-04-08 10:51 UTC | 1h 33m |
| RYR91QQ | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Malpensa International Airport (LIMC) | 2026-04-08 08:31 UTC | 2026-04-08 10:50 UTC | 2h 19m |
| MYJ339 | MYJ | Vienna International Airport (LOWW) | M. R. Stefanik Airport (LZIB) | 2026-04-08 10:31 UTC | 2026-04-08 10:50 UTC | 18m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-04-08 10:21 UTC | 2026-04-08 10:49 UTC | 28m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-08 10:25 UTC | 2026-04-08 10:49 UTC | 23m |
| MAS1276 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-04-08 10:31 UTC | 2026-04-08 10:47 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
