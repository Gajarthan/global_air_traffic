# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_05:14:16_UTC-green)

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

**Latest saved flight:** 2026-04-12 05:14:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 05:14:16 UTC

- **30,026** saved flights
- **13,791** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,026** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **366,884.0 tonnes** estimated CO2 emissions
- **21,268,636 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1230 |
| 2 | Ryanair | 1228 |
| 3 | IndiGo | 778 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 360 |
| 9 | AXM | 321 |
| 10 | Vueling | 306 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 270 |
| 13 | AZU | 262 |
| 14 | QLK | 256 |
| 15 | Delta Air Lines | 246 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 217 |
| 18 | Alaska Airlines | 201 |
| 19 | VIV | 196 |
| 20 | EJU | 193 |
| 21 | easyJet | 193 |
| 22 | Japan Airlines | 193 |
| 23 | AEE | 188 |
| 24 | WIF | 187 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | GLO | 160 |
| 29 | JetBlue | 159 |
| 30 | AXB | 155 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23798 |
| 2 | 🇮🇳 IN | 2392 |
| 3 | 🇪🇸 ES | 2212 |
| 4 | 🇦🇺 AU | 2131 |
| 5 | 🇧🇷 BR | 1732 |
| 6 | 🇯🇵 JP | 1646 |
| 7 | 🇮🇹 IT | 1534 |
| 8 | 🇨🇴 CO | 1518 |
| 9 | 🇩🇪 DE | 1496 |
| 10 | 🇨🇦 CA | 1477 |
| 11 | 🇬🇧 GB | 1203 |
| 12 | 🇫🇷 FR | 1098 |
| 13 | 🇲🇽 MX | 974 |
| 14 | 🇬🇷 GR | 851 |
| 15 | 🇨🇭 CH | 840 |
| 16 | 🇲🇾 MY | 769 |
| 17 | 🇳🇿 NZ | 660 |
| 18 | 🇳🇴 NO | 632 |
| 19 | 🇿🇦 ZA | 610 |
| 20 | 🇵🇭 PH | 565 |
| 21 | 🇬🇹 GT | 553 |
| 22 | 🇹🇷 TR | 544 |
| 23 | 🇹🇭 TH | 541 |
| 24 | 🇰🇷 KR | 509 |
| 25 | 🇵🇱 PL | 450 |
| 26 | 🇲🇦 MA | 373 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 298 |
| 29 | 🇳🇱 NL | 286 |
| 30 | 🇮🇩 ID | 286 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 552 |
| 3 | El Dorado International Airport |  | CO | 541 |
| 4 | Denver International Airport |  | US | 512 |
| 5 | Indira Gandhi International Airport |  | IN | 502 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 416 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 391 |
| 9 | Guaymaral Airport |  | CO | 359 |
| 10 | Zurich Airport |  | CH | 358 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 303 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 297 |
| 16 | Kuala Lumpur International Airport |  | MY | 290 |
| 17 | Macau International Airport |  | MO | 284 |
| 18 | Charlotte/Douglas International Airport |  | US | 271 |
| 19 | Bengaluru International Airport |  | IN | 271 |
| 20 | Madrid Barajas International Airport |  | ES | 263 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Ninoy Aquino International Airport |  | PH | 260 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 240 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 231 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 211 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 31 | Capua Airport |  | IT | 205 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 202 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 201 |
| 34 | Miami International Airport |  | US | 201 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 200 |
| 36 | O. R. Tambo International Airport |  | ZA | 194 |
| 37 | Vitoria/Foronda Airport |  | ES | 193 |
| 38 | Seattle-Tacoma International Airport |  | US | 191 |
| 39 | Barcelona International Airport |  | ES | 189 |
| 40 | Viracopos International Airport |  | BR | 183 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 140 | 1h 8m | 706 km | 1,704.5 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 111 | 24m | 225 km | 430.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 101 | 28m | 304 km | 529.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 88 | 1h 27m | 910 km | 1,380.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 77 | 19m | 165 km | 219.0 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 68 | 55m | 546 km | 640.2 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 64 | 1h 12m | 770 km | 850.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 59 | 31m | 369 km | 375.5 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 54 | 45m | 452 km | 420.9 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 23 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 46 | 20m | 147 km | 116.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Los Angeles International Airport (KLAX) | Reno/Tahoe International Airport (KRNO) | 40 | 55m | 630 km | 434.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-12 00:57 UTC | 2026-04-12 05:14 UTC | 4h 16m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-11 17:32 UTC | 2026-04-12 05:10 UTC | 11h 38m |
| N912KC |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-12 02:22 UTC | 2026-04-12 05:08 UTC | 2h 45m |
| DLH6EJ | Lufthansa | Billund Airport (EKBI) | Frankfurt am Main International Airport (EDDF) | 2026-04-12 04:05 UTC | 2026-04-12 05:06 UTC | 1h 0m |
| BTK6267 | BTK | Halim Perdanakusuma International Airport (WIHH) | Halim Perdanakusuma International Airport (WIHH) | 2026-04-12 04:43 UTC | 2026-04-12 04:57 UTC | 13m |
| CFG | CFG | Caloundra Airport (YCDR) | Caloundra Airport (YCDR) | 2026-04-12 04:46 UTC | 2026-04-12 04:52 UTC | 6m |
| N607FJ |  | Fairbanks International Airport (PAFA) | Malnarick Park Airport (AK80) | 2026-04-12 04:21 UTC | 2026-04-12 04:46 UTC | 24m |
| N887CE |  | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-04-12 03:57 UTC | 2026-04-12 04:43 UTC | 45m |
| CPA632 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-11 17:10 UTC | 2026-04-12 04:42 UTC | 11h 31m |
| 4XHYI |  | LL59 (LL59) | LL59 (LL59) | 2026-04-12 04:22 UTC | 2026-04-12 04:40 UTC | 17m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-04-12 04:18 UTC | 2026-04-12 04:35 UTC | 17m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-11 17:03 UTC | 2026-04-12 04:29 UTC | 11h 25m |
| N505TJ |  | Buffalo Niagara International Airport (KBUF) | Buffalo Niagara International Airport (KBUF) | 2026-04-12 04:24 UTC | 2026-04-12 04:28 UTC | 3m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-12 04:06 UTC | 2026-04-12 04:26 UTC | 20m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-12 03:47 UTC | 2026-04-12 04:21 UTC | 34m |
| PGT2940 | PGT | Yalova Airport (LTBP) | Balikesir Korfez Airport (LTFD) | 2026-04-12 03:52 UTC | 2026-04-12 04:19 UTC | 26m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-12 03:58 UTC | 2026-04-12 04:17 UTC | 18m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-12 03:49 UTC | 2026-04-12 04:15 UTC | 26m |
| GAP2041 | GAP | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-12 03:51 UTC | 2026-04-12 04:15 UTC | 24m |
| N702SS |  | Harry Reid International Airport (KLAS) | Scottsdale Airport (KSDL) | 2026-04-12 03:28 UTC | 2026-04-12 04:15 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
