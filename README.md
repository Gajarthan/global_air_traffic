# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_21:43:27_UTC-green)

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

**Latest saved flight:** 2026-04-17 21:43:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 21:43:27 UTC

- **40,158** saved flights
- **17,163** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,158** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **484,006.8 tonnes** estimated CO2 emissions
- **28,058,364 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1692 |
| 2 | SkyWest Airlines | 1568 |
| 3 | IndiGo | 978 |
| 4 | EJA | 700 |
| 5 | American Airlines | 675 |
| 6 | Southwest Airlines | 562 |
| 7 | ENY | 520 |
| 8 | AXM | 413 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 396 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 356 |
| 13 | All Nippon Airways | 351 |
| 14 | Delta Air Lines | 342 |
| 15 | QLK | 327 |
| 16 | LXJ | 322 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 269 |
| 20 | AEE | 266 |
| 21 | easyJet | 264 |
| 22 | EJU | 262 |
| 23 | VIV | 258 |
| 24 | Japan Airlines | 238 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 216 |
| 28 | EDV | 215 |
| 29 | GLO | 208 |
| 30 | AIQ | 203 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 31855 |
| 2 | 🇮🇳 IN | 2981 |
| 3 | 🇪🇸 ES | 2977 |
| 4 | 🇦🇺 AU | 2789 |
| 5 | 🇧🇷 BR | 2380 |
| 6 | 🇯🇵 JP | 2135 |
| 7 | 🇮🇹 IT | 2099 |
| 8 | 🇩🇪 DE | 2016 |
| 9 | 🇨🇦 CA | 1988 |
| 10 | 🇨🇴 CO | 1949 |
| 11 | 🇬🇧 GB | 1638 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1273 |
| 14 | 🇬🇷 GR | 1203 |
| 15 | 🇨🇭 CH | 1099 |
| 16 | 🇳🇴 NO | 1005 |
| 17 | 🇲🇾 MY | 1003 |
| 18 | 🇿🇦 ZA | 827 |
| 19 | 🇳🇿 NZ | 817 |
| 20 | 🇵🇭 PH | 722 |
| 21 | 🇹🇭 TH | 716 |
| 22 | 🇹🇷 TR | 705 |
| 23 | 🇬🇹 GT | 684 |
| 24 | 🇰🇷 KR | 641 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 497 |
| 27 | 🇳🇱 NL | 405 |
| 28 | 🇲🇪 ME | 401 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 367 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 939 |
| 2 | Tokyo International Airport |  | JP | 728 |
| 3 | El Dorado International Airport |  | CO | 686 |
| 4 | Denver International Airport |  | US | 667 |
| 5 | Indira Gandhi International Airport |  | IN | 641 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 599 |
| 7 | Harry Reid International Airport |  | US | 518 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 504 |
| 10 | Zurich Airport |  | CH | 484 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 394 |
| 12 | Kuala Lumpur International Airport |  | MY | 394 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 393 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 379 |
| 16 | Macau International Airport |  | MO | 367 |
| 17 | Madrid Barajas International Airport |  | ES | 363 |
| 18 | Charlotte/Douglas International Airport |  | US | 357 |
| 19 | Tenerife Norte Airport |  | ES | 356 |
| 20 | Frankfurt am Main International Airport |  | DE | 350 |
| 21 | Bengaluru International Airport |  | IN | 348 |
| 22 | Congonhas Airport |  | BR | 347 |
| 23 | Ninoy Aquino International Airport |  | PH | 335 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 314 |
| 26 | Salt Lake City International Airport |  | US | 310 |
| 27 | Daniel K Inouye International Airport |  | US | 300 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 286 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 277 |
| 31 | Vitoria/Foronda Airport |  | ES | 276 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 274 |
| 33 | Capua Airport |  | IT | 274 |
| 34 | Reno/Tahoe International Airport |  | US | 271 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Viracopos International Airport |  | BR | 245 |
| 39 | Calgary International Airport |  | CA | 243 |
| 40 | Don Mueang International Airport |  | TH | 240 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 183 | 1h 8m | 706 km | 2,228.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 114 | 28m | 304 km | 597.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 105 | 21m | 244 km | 442.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 105 | 19m | 165 km | 298.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 102 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 101 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 77 | 45m | 452 km | 600.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 73 | 27m | 152 km | 190.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 72 | 31m | 369 km | 458.3 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 63 | 52m | 556 km | 603.9 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 57 | 1h 53m | 1,304 km | 1,282.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 56 | 59m | 695 km | 671.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-17 21:21 UTC | 2026-04-17 21:43 UTC | 21m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-17 10:40 UTC | 2026-04-17 21:42 UTC | 11h 2m |
| N6989M |  | Harnett Regional Jetport Airport (KHRJ) | Robertson Field (NC63) | 2026-04-17 20:59 UTC | 2026-04-17 21:41 UTC | 41m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-04-17 10:49 UTC | 2026-04-17 21:39 UTC | 10h 49m |
| N758LW |  | Nampa Municipal Airport (KMAN) | Symms Airport (08ID) | 2026-04-17 21:19 UTC | 2026-04-17 21:39 UTC | 19m |
| ANZ613 | ANZ | Auckland International Airport (NZAA) | Queenstown International Airport (NZQN) | 2026-04-17 20:16 UTC | 2026-04-17 21:36 UTC | 1h 20m |
| N407DV |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-17 21:14 UTC | 2026-04-17 21:33 UTC | 18m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-04-17 10:50 UTC | 2026-04-17 21:30 UTC | 10h 40m |
| N438SP |  | Hesler/Noble Field (KLUL) | Lakefront Airport (KNEW) | 2026-04-17 21:06 UTC | 2026-04-17 21:29 UTC | 23m |
| YNH | YNH | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-04-17 20:46 UTC | 2026-04-17 21:29 UTC | 42m |
| N971MB |  | 5NE6 (5NE6) | Yampa Valley Airport (KHDN) | 2026-04-17 20:32 UTC | 2026-04-17 21:27 UTC | 55m |
| N5114U |  | Caldwell Executive Airport (KEUL) | Lemons Field (2ID6) | 2026-04-17 20:45 UTC | 2026-04-17 21:18 UTC | 33m |
| N49MR |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-17 20:01 UTC | 2026-04-17 21:10 UTC | 1h 9m |
| HRD32 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-17 21:10 UTC | 2026-04-17 21:10 UTC | 0m |
| RYR593D | Ryanair | Palma De Mallorca Airport (LEPA) | Malpensa International Airport (LIMC) | 2026-04-17 19:38 UTC | 2026-04-17 21:10 UTC | 1h 32m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-04-17 17:45 UTC | 2026-04-17 21:08 UTC | 3h 22m |
| N26379 |  | Sanctuary Ranch Airport (7TS4) | XS92 (XS92) | 2026-04-17 20:54 UTC | 2026-04-17 21:06 UTC | 12m |
| N735KT |  | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-17 20:38 UTC | 2026-04-17 21:04 UTC | 26m |
| CFGMF | CFG | Brampton Airport (CNC3) | CCR9 (CCR9) | 2026-04-17 20:40 UTC | 2026-04-17 21:01 UTC | 20m |
| N74KM |  | Louis Armstrong New Orleans International Airport (KMSY) | Stuart Airstrip (LA51) | 2026-04-17 20:20 UTC | 2026-04-17 21:00 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
