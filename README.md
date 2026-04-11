# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_07:23:49_UTC-green)

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

**Latest saved flight:** 2026-04-11 07:23:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 07:23:49 UTC

- **28,211** saved flights
- **13,228** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,211** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **342,697.8 tonnes** estimated CO2 emissions
- **19,866,536 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1155 |
| 2 | Ryanair | 1145 |
| 3 | IndiGo | 734 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 344 |
| 9 | AXM | 296 |
| 10 | Vueling | 286 |
| 11 | LATAM Airlines | 275 |
| 12 | QLK | 253 |
| 13 | All Nippon Airways | 251 |
| 14 | Delta Air Lines | 239 |
| 15 | AZU | 234 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 198 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 183 |
| 20 | VIV | 183 |
| 21 | easyJet | 181 |
| 22 | EJU | 180 |
| 23 | WIF | 180 |
| 24 | AEE | 179 |
| 25 | United Airlines | 172 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | JetBlue | 150 |
| 29 | AXB | 147 |
| 30 | PGT | 143 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22447 |
| 2 | 🇮🇳 IN | 2265 |
| 3 | 🇦🇺 AU | 2068 |
| 4 | 🇪🇸 ES | 2057 |
| 5 | 🇧🇷 BR | 1593 |
| 6 | 🇯🇵 JP | 1536 |
| 7 | 🇨🇴 CO | 1407 |
| 8 | 🇮🇹 IT | 1407 |
| 9 | 🇩🇪 DE | 1403 |
| 10 | 🇨🇦 CA | 1393 |
| 11 | 🇬🇧 GB | 1124 |
| 12 | 🇫🇷 FR | 1027 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 803 |
| 15 | 🇨🇭 CH | 762 |
| 16 | 🇲🇾 MY | 707 |
| 17 | 🇳🇿 NZ | 632 |
| 18 | 🇳🇴 NO | 607 |
| 19 | 🇿🇦 ZA | 571 |
| 20 | 🇵🇭 PH | 534 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 509 |
| 23 | 🇹🇭 TH | 491 |
| 24 | 🇰🇷 KR | 481 |
| 25 | 🇵🇱 PL | 419 |
| 26 | 🇲🇦 MA | 346 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 279 |
| 29 | 🇮🇩 ID | 272 |
| 30 | 🇳🇱 NL | 271 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 519 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Denver International Airport |  | US | 478 |
| 5 | Indira Gandhi International Airport |  | IN | 472 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 391 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 364 |
| 9 | Zurich Airport |  | CH | 330 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 293 |
| 13 | Frankfurt am Main International Airport |  | DE | 292 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 288 |
| 16 | Kuala Lumpur International Airport |  | MY | 264 |
| 17 | Macau International Airport |  | MO | 261 |
| 18 | Charlotte/Douglas International Airport |  | US | 257 |
| 19 | Bengaluru International Airport |  | IN | 251 |
| 20 | Ninoy Aquino International Airport |  | PH | 246 |
| 21 | Madrid Barajas International Airport |  | ES | 239 |
| 22 | Tenerife Norte Airport |  | ES | 237 |
| 23 | Congonhas Airport |  | BR | 227 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 25 | Salt Lake City International Airport |  | US | 220 |
| 26 | Daniel K Inouye International Airport |  | US | 219 |
| 27 | Malpensa International Airport |  | IT | 217 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 31 | Miami International Airport |  | US | 189 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 189 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 180 |
| 36 | Seattle-Tacoma International Airport |  | US | 179 |
| 37 | Barcelona International Airport |  | ES | 177 |
| 38 | Capua Airport |  | IT | 177 |
| 39 | Vitoria/Foronda Airport |  | ES | 176 |
| 40 | Calgary International Airport |  | CA | 170 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 132 | 1h 8m | 706 km | 1,607.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 107 | 24m | 225 km | 415.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 96 | 28m | 304 km | 503.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 82 | 1h 27m | 910 km | 1,286.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 70 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 70 | 19m | 165 km | 199.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 62 | 55m | 546 km | 583.7 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 61 | 1h 12m | 770 km | 810.3 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 57 | 27m | 275 km | 270.1 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 54 | 31m | 369 km | 343.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 52 | 46m | 452 km | 405.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 44 | 20m | 147 km | 111.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZSIZB | ZSI | Cape Town International Airport (FACT) | Grand Central Airport (FAGC) | 2026-04-11 05:10 UTC | 2026-04-11 07:23 UTC | 2h 13m |
| RNA206 | RNA | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-11 05:54 UTC | 2026-04-11 06:56 UTC | 1h 1m |
| UAL909 | United Airlines | Chicago O'Hare International Airport (KORD) | Amsterdam Airport Schiphol (EHAM) | 2026-04-10 23:25 UTC | 2026-04-11 06:46 UTC | 7h 20m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-10 18:56 UTC | 2026-04-11 06:34 UTC | 11h 38m |
| BBC435 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-11 06:09 UTC | 2026-04-11 06:34 UTC | 25m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-04-11 05:37 UTC | 2026-04-11 06:31 UTC | 54m |
| LLR873 | LLR | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-04-11 05:56 UTC | 2026-04-11 06:30 UTC | 33m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-04-11 05:12 UTC | 2026-04-11 06:29 UTC | 1h 16m |
| JVS | JVS | Sydney Bankstown Airport (YSBK) | RAAF Base Richmond (YSRI) | 2026-04-11 06:23 UTC | 2026-04-11 06:27 UTC | 3m |
| RYR40HE | Ryanair | Torino / Caselle International Airport (LIMF) | Decimomannu Airport (LIED) | 2026-04-11 05:33 UTC | 2026-04-11 06:26 UTC | 53m |
| JAL611 | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-04-11 04:52 UTC | 2026-04-11 06:24 UTC | 1h 32m |
| RXA6832 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-11 05:46 UTC | 2026-04-11 06:23 UTC | 37m |
| RYR64CZ | Ryanair | Brussels South Charleroi Airport (EBCI) | Capua Airport (LIAU) | 2026-04-11 04:44 UTC | 2026-04-11 06:18 UTC | 1h 34m |
| BTN700 | BTN | Bagdogra Airport (VEBD) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-11 05:10 UTC | 2026-04-11 06:18 UTC | 1h 7m |
| VLG49TV | Vueling | Barcelona International Airport (LEBL) | Alicante International Airport (LEAL) | 2026-04-11 05:29 UTC | 2026-04-11 06:16 UTC | 47m |
| AXM5305 | AXM | Kota Kinabalu International Airport (WBKK) | Seletar Airport (WSSL) | 2026-04-11 04:26 UTC | 2026-04-11 06:16 UTC | 1h 50m |
| FDA166 | FDA | New Chitose Airport (RJCC) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-04-11 04:43 UTC | 2026-04-11 06:15 UTC | 1h 32m |
| VTFTO | VTF | Hosur Airport (VO95) | Mysore Airport (VOMY) | 2026-04-11 05:27 UTC | 2026-04-11 06:14 UTC | 47m |
| WMT2306 | WMT | Bari / Palese International Airport (LIBD) | Kukes Airport (LAKU) | 2026-04-11 05:50 UTC | 2026-04-11 06:12 UTC | 22m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-11 04:17 UTC | 2026-04-11 06:10 UTC | 1h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
