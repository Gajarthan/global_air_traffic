# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_00:52:25_UTC-green)

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

**Latest saved flight:** 2026-04-08 00:52:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 00:52:25 UTC

- **22,526** saved flights
- **11,081** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,526** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **278,275.9 tonnes** estimated CO2 emissions
- **16,131,938 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 969 |
| 2 | Ryanair | 929 |
| 3 | IndiGo | 624 |
| 4 | EJA | 422 |
| 5 | American Airlines | 419 |
| 6 | Southwest Airlines | 329 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 230 |
| 11 | AXM | 218 |
| 12 | All Nippon Airways | 198 |
| 13 | Delta Air Lines | 197 |
| 14 | QLK | 195 |
| 15 | LXJ | 189 |
| 16 | AZU | 178 |
| 17 | Swiss International | 162 |
| 18 | VIV | 161 |
| 19 | Alaska Airlines | 155 |
| 20 | Japan Airlines | 151 |
| 21 | easyJet | 149 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | EDV | 135 |
| 27 | WIF | 134 |
| 28 | AXB | 126 |
| 29 | Air France | 119 |
| 30 | JetBlue | 116 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17891 |
| 2 | 🇮🇳 IN | 1903 |
| 3 | 🇪🇸 ES | 1739 |
| 4 | 🇦🇺 AU | 1615 |
| 5 | 🇧🇷 BR | 1278 |
| 6 | 🇯🇵 JP | 1238 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1128 |
| 9 | 🇩🇪 DE | 1111 |
| 10 | 🇨🇦 CA | 1015 |
| 11 | 🇬🇧 GB | 882 |
| 12 | 🇫🇷 FR | 818 |
| 13 | 🇲🇽 MX | 741 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 604 |
| 16 | 🇲🇾 MY | 511 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇴 NO | 467 |
| 19 | 🇬🇹 GT | 467 |
| 20 | 🇳🇿 NZ | 464 |
| 21 | 🇹🇷 TR | 431 |
| 22 | 🇵🇭 PH | 423 |
| 23 | 🇰🇷 KR | 395 |
| 24 | 🇹🇭 TH | 349 |
| 25 | 🇵🇱 PL | 321 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 416 |
| 4 | Denver International Airport |  | US | 406 |
| 5 | Indira Gandhi International Airport |  | IN | 383 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Harry Reid International Airport |  | US | 304 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 9 | Zurich Airport |  | CH | 269 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Chicago O'Hare International Airport |  | US | 237 |
| 14 | Guaymaral Airport |  | CO | 236 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 227 |
| 16 | Charlotte/Douglas International Airport |  | US | 214 |
| 17 | Bengaluru International Airport |  | IN | 214 |
| 18 | Macau International Airport |  | MO | 204 |
| 19 | Tenerife Norte Airport |  | ES | 202 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Ninoy Aquino International Airport |  | PH | 194 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 23 | Congonhas Airport |  | BR | 186 |
| 24 | Kuala Lumpur International Airport |  | MY | 183 |
| 25 | Salt Lake City International Airport |  | US | 182 |
| 26 | Malpensa International Airport |  | IT | 174 |
| 27 | Reno/Tahoe International Airport |  | US | 174 |
| 28 | Daniel K Inouye International Airport |  | US | 173 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 164 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 155 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 151 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 36 | Pune Airport |  | IN | 151 |
| 37 | Seattle-Tacoma International Airport |  | US | 148 |
| 38 | Vitoria/Foronda Airport |  | ES | 147 |
| 39 | Barcelona International Airport |  | ES | 145 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 105 | 1h 8m | 706 km | 1,278.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 84 | 24m | 225 km | 325.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 52 | 19m | 165 km | 147.9 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 48 | 55m | 546 km | 451.9 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 40 | 46m | 452 km | 311.7 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NINJA48 | NIN | Atsugi Naval Air Facility (RJTA) | Miyakejima Airport (RJTQ) | 2026-04-08 00:15 UTC | 2026-04-08 00:52 UTC | 36m |
| N53695 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-04-08 00:25 UTC | 2026-04-08 00:43 UTC | 17m |
| CXK184 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-04-07 23:20 UTC | 2026-04-08 00:37 UTC | 1h 16m |
| PCJ20 | PCJ | Oxnard Airport (KOXR) | Santa Monica Municipal Airport (KSMO) | 2026-04-08 00:21 UTC | 2026-04-08 00:37 UTC | 15m |
| YHJ | YHJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-08 00:12 UTC | 2026-04-08 00:31 UTC | 19m |
| PRE54 | PRE | Bridger Creek Airport (WY34) | Rocky Mountain Metro Airport (KBJC) | 2026-04-07 23:15 UTC | 2026-04-08 00:29 UTC | 1h 13m |
| N729JF |  | Colonel James Jabara Airport (KAAO) | Ness City Municipal Airport (K48K) | 2026-04-08 00:03 UTC | 2026-04-08 00:28 UTC | 25m |
| MNL99 | MNL | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-04-07 23:49 UTC | 2026-04-08 00:27 UTC | 37m |
| SKW5397 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Bermuda Dunes Airport (KUDD) | 2026-04-07 23:58 UTC | 2026-04-08 00:21 UTC | 23m |
| N911LL |  | Gaines County Airport (KGNC) | Gaines County Airport (KGNC) | 2026-04-08 00:17 UTC | 2026-04-08 00:18 UTC | 1m |
| R43542 |  | Wheeler-Sack Army Air Field (KGTB) | Wheeler-Sack Army Air Field (KGTB) | 2026-04-07 23:07 UTC | 2026-04-08 00:18 UTC | 1h 10m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-04-07 23:22 UTC | 2026-04-08 00:18 UTC | 55m |
| N733WT |  | Ramona Airport (KRNM) | Ramona Airport (KRNM) | 2026-04-08 00:06 UTC | 2026-04-08 00:17 UTC | 11m |
| SAMU44 | SAM | Chateaubriant Pouance Airport (LFTQ) | Nantes Atlantique Airport (LFRS) | 2026-04-07 23:57 UTC | 2026-04-08 00:13 UTC | 16m |
| BOSOX37 | BOS | Plymouth Municipal Airport (KPYM) | Cape Cod Coast Guard Air Station (KFMH) | 2026-04-07 23:24 UTC | 2026-04-08 00:11 UTC | 46m |
| N680MC |  | Phoenix Sky Harbor International Airport (KPHX) | Iron Mountain Pumping Plant Airport (72CL) | 2026-04-07 23:39 UTC | 2026-04-08 00:05 UTC | 26m |
| NJZ196 | NJZ | Mesa Gateway Airport (KIWA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-07 22:29 UTC | 2026-04-08 00:05 UTC | 1h 36m |
| MXY207 | MXY | Harry Reid International Airport (KLAS) | Akron-Canton Regional Airport (KCAK) | 2026-04-07 20:16 UTC | 2026-04-08 00:05 UTC | 3h 48m |
| AXM6048 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-07 23:42 UTC | 2026-04-08 00:03 UTC | 21m |
| N607SA |  | Sacramento Mather Airport (KMHR) | Tracy Municipal Airport (KTCY) | 2026-04-07 23:27 UTC | 2026-04-08 00:03 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
