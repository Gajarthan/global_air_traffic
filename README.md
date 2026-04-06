# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_02:14:48_UTC-green)

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

**Latest saved flight:** 2026-04-06 02:14:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-06 02:14:48 UTC

- **19,374** saved flights
- **9,793** unique routes
- **115** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **19,374** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **244,429.2 tonnes** estimated CO2 emissions
- **14,169,812 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 855 |
| 2 | Ryanair | 789 |
| 3 | IndiGo | 544 |
| 4 | American Airlines | 377 |
| 5 | EJA | 364 |
| 6 | Southwest Airlines | 282 |
| 7 | ENY | 267 |
| 8 | Lufthansa | 256 |
| 9 | Vueling | 210 |
| 10 | LATAM Airlines | 208 |
| 11 | AXM | 191 |
| 12 | Delta Air Lines | 176 |
| 13 | LXJ | 171 |
| 14 | All Nippon Airways | 165 |
| 15 | QLK | 157 |
| 16 | AZU | 149 |
| 17 | VIV | 148 |
| 18 | Swiss International | 142 |
| 19 | Alaska Airlines | 132 |
| 20 | United Airlines | 132 |
| 21 | Avianca | 130 |
| 22 | Japan Airlines | 126 |
| 23 | easyJet | 124 |
| 24 | EJU | 122 |
| 25 | AEE | 121 |
| 26 | EDV | 118 |
| 27 | WIF | 116 |
| 28 | AXB | 113 |
| 29 | Air France | 105 |
| 30 | Cathay Pacific | 105 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 15326 |
| 2 | 🇮🇳 IN | 1650 |
| 3 | 🇪🇸 ES | 1569 |
| 4 | 🇦🇺 AU | 1350 |
| 5 | 🇧🇷 BR | 1124 |
| 6 | 🇨🇴 CO | 1056 |
| 7 | 🇯🇵 JP | 1024 |
| 8 | 🇩🇪 DE | 966 |
| 9 | 🇮🇹 IT | 908 |
| 10 | 🇨🇦 CA | 855 |
| 11 | 🇬🇧 GB | 744 |
| 12 | 🇫🇷 FR | 700 |
| 13 | 🇲🇽 MX | 677 |
| 14 | 🇬🇷 GR | 539 |
| 15 | 🇨🇭 CH | 505 |
| 16 | 🇬🇹 GT | 452 |
| 17 | 🇲🇾 MY | 443 |
| 18 | 🇳🇿 NZ | 414 |
| 19 | 🇿🇦 ZA | 411 |
| 20 | 🇳🇴 NO | 391 |
| 21 | 🇹🇷 TR | 371 |
| 22 | 🇵🇭 PH | 364 |
| 23 | 🇰🇷 KR | 330 |
| 24 | 🇹🇭 TH | 285 |
| 25 | 🇵🇱 PL | 278 |
| 26 | 🇲🇦 MA | 241 |
| 27 | 🇧🇸 BS | 215 |
| 28 | 🇮🇩 ID | 205 |
| 29 | 🇲🇴 MO | 198 |
| 30 | 🇲🇪 ME | 196 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 481 |
| 2 | El Dorado International Airport |  | CO | 404 |
| 3 | Denver International Airport |  | US | 361 |
| 4 | Tokyo International Airport |  | JP | 349 |
| 5 | Indira Gandhi International Airport |  | IN | 344 |
| 6 | La Aurora Airport |  | GT | 309 |
| 7 | Harry Reid International Airport |  | US | 255 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 254 |
| 9 | Zurich Airport |  | CH | 233 |
| 10 | Frankfurt am Main International Airport |  | DE | 228 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 215 |
| 12 | Chicago O'Hare International Airport |  | US | 210 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 210 |
| 14 | Guaymaral Airport |  | CO | 201 |
| 15 | Macau International Airport |  | MO | 198 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 196 |
| 17 | Charlotte/Douglas International Airport |  | US | 190 |
| 18 | Madrid Barajas International Airport |  | ES | 184 |
| 19 | Bengaluru International Airport |  | IN | 184 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 178 |
| 21 | Tenerife Norte Airport |  | ES | 174 |
| 22 | Congonhas Airport |  | BR | 167 |
| 23 | Ninoy Aquino International Airport |  | PH | 166 |
| 24 | Salt Lake City International Airport |  | US | 157 |
| 25 | Reno/Tahoe International Airport |  | US | 156 |
| 26 | Kuala Lumpur International Airport |  | MY | 155 |
| 27 | Daniel K Inouye International Airport |  | US | 153 |
| 28 | Malpensa International Airport |  | IT | 146 |
| 29 | Vitoria/Foronda Airport |  | ES | 145 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 144 |
| 31 | Charles de Gaulle International Airport |  | FR | 143 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 141 |
| 33 | Miami International Airport |  | US | 140 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 131 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 131 |
| 36 | Pune Airport |  | IN | 131 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 130 |
| 38 | Barcelona International Airport |  | ES | 130 |
| 39 | O. R. Tambo International Airport |  | ZA | 127 |
| 40 | Seattle-Tacoma International Airport |  | US | 126 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 89 | 14m | 114 km | 174.6 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 88 | 1h 8m | 706 km | 1,071.4 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 73 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 70 | 24m | 225 km | 271.6 t |
| 5 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 67 | 22m | 99 km | 114.8 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 64 | 28m | 304 km | 335.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 56 | 1h 43m | 1,156 km | 1,117.2 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 55 | 1h 27m | 910 km | 863.1 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 54 | 16m | 206 km | 192.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 54 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 45 | 19m | 165 km | 128.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 44 | 1h 53m | 1,304 km | 989.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 41 | 1h 12m | 770 km | 544.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 40 | 30m | 369 km | 254.6 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 39 | 23m | 252 km | 169.3 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 39 | 52m | 556 km | 373.8 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 38 | 54m | 546 km | 357.8 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 38 | 4m | - | - |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 37 | 1h 43m | 1,423 km | 908.0 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 37 | 9m | - | - |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 36 | 13m | 99 km | 61.7 t |
| 24 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 35 | 58m | 723 km | 436.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 34 | 46m | 452 km | 265.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 31 | 16m | 183 km | 97.8 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 30 | 12m | 15 km | 7.9 t |
| 30 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 30 | 20m | 250 km | 129.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6089F |  | Spectre Field (XA07) | Fort Worth Meacham International Airport (KFTW) | 2026-04-06 01:46 UTC | 2026-04-06 02:14 UTC | 28m |
| TRF577 | TRF | Addison Airport (KADS) | Sulphur Springs Municipal Airport (KSLR) | 2026-04-06 01:29 UTC | 2026-04-06 02:11 UTC | 41m |
| EXV | EXV | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-06 01:44 UTC | 2026-04-06 02:03 UTC | 19m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-05 23:41 UTC | 2026-04-06 02:00 UTC | 2h 19m |
| UAL1654 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | Denver International Airport (KDEN) | 2026-04-05 23:52 UTC | 2026-04-06 01:53 UTC | 2h 1m |
| LXJ342 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-06 01:40 UTC | 2026-04-06 01:53 UTC | 12m |
| J9 |  | Cildir Airport (LTBD) | Adnan Menderes International Airport (LTBJ) | 2026-04-05 23:34 UTC | 2026-04-06 01:52 UTC | 2h 17m |
| N455LF |  | Easton State Airport (KESW) | Boeing Field/King County International Airport (KBFI) | 2026-04-06 01:28 UTC | 2026-04-06 01:47 UTC | 18m |
| USC240 | USC | Portland International Airport (KPDX) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-06 00:25 UTC | 2026-04-06 01:46 UTC | 1h 20m |
| CDG | CDG | Gold Coast Airport (YBCG) | Bathurst Airport (YBTH) | 2026-04-06 00:21 UTC | 2026-04-06 01:34 UTC | 1h 12m |
| N8345C |  | De Kalb Taylor Municipal Airport (KDKB) | 0IL8 (0IL8) | 2026-04-06 01:25 UTC | 2026-04-06 01:29 UTC | 4m |
| XSN06 | XSN | Montgomery-Gibbs Executive Airport (KMYF) | San Carlos Airport (KSQL) | 2026-04-05 23:44 UTC | 2026-04-06 01:18 UTC | 1h 33m |
| N64FB |  | Buchanan Field (KCCR) | Reno/Tahoe International Airport (KRNO) | 2026-04-06 00:40 UTC | 2026-04-06 01:15 UTC | 34m |
| EJA424 | EJA | Palm Beach International Airport (KPBI) | Carrabelle-Thompson Airport (KX13) | 2026-04-06 00:17 UTC | 2026-04-06 01:14 UTC | 56m |
| SKW5854 | SkyWest Airlines | San Francisco International Airport (KSFO) | Lee Vining Airport (KO24) | 2026-04-06 00:42 UTC | 2026-04-06 01:13 UTC | 30m |
| SWA2516 | Southwest Airlines | Long Beach (Daugherty Field) Airport (KLGB) | Reno/Tahoe International Airport (KRNO) | 2026-04-06 00:17 UTC | 2026-04-06 01:10 UTC | 53m |
| NV115 |  | Melbourne Essendon Airport (YMEN) | Lethbridge Park Airport (YLED) | 2026-04-06 00:38 UTC | 2026-04-06 01:08 UTC | 29m |
| VIV9451 | VIV | Quetzalcoatl International Airport (MMNL) | Atizapan De Zaragoza Airport (MMJC) | 2026-04-05 23:52 UTC | 2026-04-06 01:07 UTC | 1h 14m |
| SKY791 | SKY | Hyakuri Airport (RJAH) | New Chitose Airport (RJCC) | 2026-04-05 23:53 UTC | 2026-04-06 01:03 UTC | 1h 10m |
| CAP1893 | CAP | Fort Meade Executive Airport (KFME) | Fort Meade Executive Airport (KFME) | 2026-04-06 01:00 UTC | 2026-04-06 01:02 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
