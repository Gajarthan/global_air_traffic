# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_00:42:10_UTC-green)

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

**Latest saved flight:** 2026-04-11 00:42:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 00:42:10 UTC

- **28,061** saved flights
- **13,192** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,061** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **340,960.1 tonnes** estimated CO2 emissions
- **19,765,803 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1154 |
| 2 | Ryanair | 1139 |
| 3 | IndiGo | 733 |
| 4 | EJA | 501 |
| 5 | American Airlines | 493 |
| 6 | Southwest Airlines | 404 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 286 |
| 10 | Vueling | 283 |
| 11 | LATAM Airlines | 275 |
| 12 | QLK | 249 |
| 13 | All Nippon Airways | 246 |
| 14 | Delta Air Lines | 238 |
| 15 | AZU | 232 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 196 |
| 18 | Alaska Airlines | 188 |
| 19 | VIV | 183 |
| 20 | easyJet | 181 |
| 21 | EJU | 179 |
| 22 | Japan Airlines | 179 |
| 23 | WIF | 179 |
| 24 | AEE | 178 |
| 25 | United Airlines | 170 |
| 26 | EDV | 166 |
| 27 | Avianca | 158 |
| 28 | JetBlue | 150 |
| 29 | AXB | 147 |
| 30 | GLO | 142 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22398 |
| 2 | 🇮🇳 IN | 2250 |
| 3 | 🇪🇸 ES | 2047 |
| 4 | 🇦🇺 AU | 2031 |
| 5 | 🇧🇷 BR | 1589 |
| 6 | 🇯🇵 JP | 1506 |
| 7 | 🇨🇴 CO | 1403 |
| 8 | 🇮🇹 IT | 1399 |
| 9 | 🇩🇪 DE | 1392 |
| 10 | 🇨🇦 CA | 1387 |
| 11 | 🇬🇧 GB | 1120 |
| 12 | 🇫🇷 FR | 1024 |
| 13 | 🇲🇽 MX | 894 |
| 14 | 🇬🇷 GR | 799 |
| 15 | 🇨🇭 CH | 756 |
| 16 | 🇲🇾 MY | 688 |
| 17 | 🇳🇿 NZ | 623 |
| 18 | 🇳🇴 NO | 605 |
| 19 | 🇿🇦 ZA | 567 |
| 20 | 🇬🇹 GT | 523 |
| 21 | 🇵🇭 PH | 522 |
| 22 | 🇹🇷 TR | 508 |
| 23 | 🇹🇭 TH | 481 |
| 24 | 🇰🇷 KR | 477 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 345 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 278 |
| 29 | 🇳🇱 NL | 270 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 674 |
| 2 | El Dorado International Airport |  | CO | 509 |
| 3 | Tokyo International Airport |  | JP | 507 |
| 4 | Denver International Airport |  | US | 478 |
| 5 | Indira Gandhi International Airport |  | IN | 466 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 389 |
| 7 | La Aurora Airport |  | GT | 369 |
| 8 | Harry Reid International Airport |  | US | 362 |
| 9 | Zurich Airport |  | CH | 327 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 292 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 14 | Frankfurt am Main International Airport |  | DE | 289 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 284 |
| 16 | Macau International Airport |  | MO | 261 |
| 17 | Charlotte/Douglas International Airport |  | US | 257 |
| 18 | Kuala Lumpur International Airport |  | MY | 256 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 242 |
| 21 | Madrid Barajas International Airport |  | ES | 237 |
| 22 | Tenerife Norte Airport |  | ES | 237 |
| 23 | Congonhas Airport |  | BR | 227 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 219 |
| 25 | Salt Lake City International Airport |  | US | 219 |
| 26 | Malpensa International Airport |  | IT | 216 |
| 27 | Daniel K Inouye International Airport |  | US | 215 |
| 28 | Reno/Tahoe International Airport |  | US | 207 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 193 |
| 31 | Miami International Airport |  | US | 189 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 187 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Seattle-Tacoma International Airport |  | US | 179 |
| 37 | Barcelona International Airport |  | ES | 175 |
| 38 | Capua Airport |  | IT | 175 |
| 39 | Vitoria/Foronda Airport |  | ES | 174 |
| 40 | Calgary International Airport |  | CA | 169 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 113 | 14m | 114 km | 221.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 105 | 24m | 225 km | 407.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 79 | 1h 27m | 910 km | 1,239.7 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 73 | 21m | 99 km | 125.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 69 | 19m | 165 km | 196.3 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 59 | 55m | 546 km | 555.5 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 51 | 46m | 452 km | 397.5 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 50 | 52m | 556 km | 479.3 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 41 | 21m | 244 km | 172.6 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MNL14 | MNL | Reno/Tahoe International Airport (KRNO) | San Carlos Airport (KSQL) | 2026-04-10 23:52 UTC | 2026-04-11 00:42 UTC | 49m |
| N628LA |  | Falcon Field (KFFZ) | 4AZ0 (4AZ0) | 2026-04-10 23:52 UTC | 2026-04-11 00:39 UTC | 47m |
| BULET47 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-10 23:01 UTC | 2026-04-11 00:38 UTC | 1h 37m |
| N665PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-10 22:49 UTC | 2026-04-11 00:34 UTC | 1h 44m |
| GUEPT2 | GUE | Moorea Airport (NTTM) | Moorea Airport (NTTM) | 2026-04-11 00:09 UTC | 2026-04-11 00:32 UTC | 23m |
| N71670 |  | Howard Field (TA02) | 7TS0 (7TS0) | 2026-04-10 23:55 UTC | 2026-04-11 00:25 UTC | 30m |
| ERU33 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Payson Airport (KPAN) | 2026-04-10 23:28 UTC | 2026-04-11 00:21 UTC | 53m |
| AJ5 |  | Melbourne Essendon Airport (YMEN) | Prairie Airport (YPRA) | 2026-04-10 23:57 UTC | 2026-04-11 00:18 UTC | 20m |
| CGDHU | CGD | Highwood Airport (CED6) | Highwood Airport (CED6) | 2026-04-11 00:11 UTC | 2026-04-11 00:16 UTC | 4m |
| CGLLV | CGL | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-04-10 23:41 UTC | 2026-04-11 00:12 UTC | 30m |
| N26379 |  | Sanctuary Ranch Airport (7TS4) | XA10 (XA10) | 2026-04-11 00:08 UTC | 2026-04-11 00:10 UTC | 2m |
| ZKLTL | ZKL | New Plymouth Airport (NZNP) | New Plymouth Airport (NZNP) | 2026-04-10 22:13 UTC | 2026-04-11 00:09 UTC | 1h 56m |
| FFT1692 | FFT | Orlando International Airport (KMCO) | Buffalo Niagara International Airport (KBUF) | 2026-04-10 21:53 UTC | 2026-04-11 00:08 UTC | 2h 15m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-10 23:21 UTC | 2026-04-11 00:06 UTC | 45m |
| N722LU |  | New London Airport (KW90) | 94VA (94VA) | 2026-04-10 23:20 UTC | 2026-04-11 00:05 UTC | 45m |
| N578JZ |  | Mc Clellan Airfield (KMCC) | CA38 (CA38) | 2026-04-10 23:48 UTC | 2026-04-11 00:05 UTC | 17m |
| SWA433 | Southwest Airlines | Denver International Airport (KDEN) | NV13 (NV13) | 2026-04-10 22:06 UTC | 2026-04-11 00:04 UTC | 1h 57m |
| N473CA |  | Oxnard Airport (KOXR) | Oxnard Airport (KOXR) | 2026-04-10 23:52 UTC | 2026-04-11 00:03 UTC | 11m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-10 23:23 UTC | 2026-04-11 00:02 UTC | 39m |
| ERU67 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-10 23:41 UTC | 2026-04-11 00:02 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
