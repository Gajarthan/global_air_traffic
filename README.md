# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_23:44:45_UTC-green)

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

**Latest saved flight:** 2026-04-22 23:44:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 23:44:45 UTC

- **48,993** saved flights
- **19,879** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,993** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **585,957.8 tonnes** estimated CO2 emissions
- **33,968,570 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2073 |
| 2 | SkyWest Airlines | 1897 |
| 3 | IndiGo | 1138 |
| 4 | EJA | 850 |
| 5 | American Airlines | 809 |
| 6 | Southwest Airlines | 701 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 550 |
| 9 | Vueling | 487 |
| 10 | AXM | 482 |
| 11 | LATAM Airlines | 480 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 417 |
| 14 | Delta Air Lines | 405 |
| 15 | WIF | 402 |
| 16 | QLK | 389 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 371 |
| 19 | AEE | 331 |
| 20 | Alaska Airlines | 328 |
| 21 | EJU | 318 |
| 22 | easyJet | 312 |
| 23 | VIV | 311 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 277 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | GLO | 246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39134 |
| 2 | 🇮🇳 IN | 3555 |
| 3 | 🇪🇸 ES | 3534 |
| 4 | 🇦🇺 AU | 3343 |
| 5 | 🇧🇷 BR | 2856 |
| 6 | 🇯🇵 JP | 2650 |
| 7 | 🇮🇹 IT | 2639 |
| 8 | 🇩🇪 DE | 2566 |
| 9 | 🇨🇦 CA | 2440 |
| 10 | 🇨🇴 CO | 2285 |
| 11 | 🇬🇧 GB | 2020 |
| 12 | 🇫🇷 FR | 1858 |
| 13 | 🇲🇽 MX | 1519 |
| 14 | 🇬🇷 GR | 1492 |
| 15 | 🇨🇭 CH | 1333 |
| 16 | 🇳🇴 NO | 1284 |
| 17 | 🇲🇾 MY | 1178 |
| 18 | 🇿🇦 ZA | 1002 |
| 19 | 🇳🇿 NZ | 932 |
| 20 | 🇹🇭 TH | 872 |
| 21 | 🇹🇷 TR | 859 |
| 22 | 🇵🇭 PH | 849 |
| 23 | 🇰🇷 KR | 796 |
| 24 | 🇵🇱 PL | 777 |
| 25 | 🇬🇹 GT | 757 |
| 26 | 🇲🇦 MA | 598 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 497 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1155 |
| 2 | Tokyo International Airport |  | JP | 900 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 785 |
| 5 | Indira Gandhi International Airport |  | IN | 752 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 737 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 641 |
| 9 | Zurich Airport |  | CH | 577 |
| 10 | La Aurora Airport |  | GT | 564 |
| 11 | Frankfurt am Main International Airport |  | DE | 526 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 485 |
| 14 | Kuala Lumpur International Airport |  | MY | 472 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 465 |
| 16 | Macau International Airport |  | MO | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 441 |
| 18 | Madrid Barajas International Airport |  | ES | 440 |
| 19 | Bengaluru International Airport |  | IN | 430 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 413 |
| 22 | Tenerife Norte Airport |  | ES | 405 |
| 23 | Malpensa International Airport |  | IT | 404 |
| 24 | Ninoy Aquino International Airport |  | PH | 393 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 373 |
| 26 | Salt Lake City International Airport |  | US | 368 |
| 27 | Daniel K Inouye International Airport |  | US | 363 |
| 28 | Charles de Gaulle International Airport |  | FR | 362 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 355 |
| 30 | Capua Airport |  | IT | 353 |
| 31 | Vitoria/Foronda Airport |  | ES | 334 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 333 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 325 |
| 36 | O. R. Tambo International Airport |  | ZA | 323 |
| 37 | Barcelona International Airport |  | ES | 321 |
| 38 | Calgary International Airport |  | CA | 297 |
| 39 | Don Mueang International Airport |  | TH | 295 |
| 40 | Viracopos International Airport |  | BR | 290 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 229 | 1h 7m | 706 km | 2,788.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 188 | 14m | 114 km | 368.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 168 | 24m | 225 km | 651.8 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 145 | 21m | 244 km | 610.6 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 115 | 26m | 275 km | 544.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 84 | 31m | 369 km | 534.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 69 | 1h 42m | 1,156 km | 1,376.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 0m | 695 km | 815.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6294Y |  | Fairbanks International Airport (PAFA) | Nenana Municipal Airport (PANN) | 2026-04-22 22:31 UTC | 2026-04-22 23:44 UTC | 1h 13m |
| N46299 |  | Orlando Apopka Airport (KX04) | Lake Wales Municipal Airport (KX07) | 2026-04-22 23:08 UTC | 2026-04-22 23:43 UTC | 35m |
| EQO | EQO | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-04-22 23:17 UTC | 2026-04-22 23:40 UTC | 23m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-22 23:15 UTC | 2026-04-22 23:34 UTC | 19m |
| N435GG |  | John Wayne/Orange County Airport (KSNA) | Henderson Executive Airport (KHND) | 2026-04-22 22:45 UTC | 2026-04-22 23:33 UTC | 48m |
| N937PC |  | Mc Clellan Airfield (KMCC) | San Carlos Airport (KSQL) | 2026-04-22 23:04 UTC | 2026-04-22 23:27 UTC | 22m |
| N9563A |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-04-22 22:37 UTC | 2026-04-22 23:24 UTC | 47m |
| ES803 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-04-22 22:46 UTC | 2026-04-22 23:23 UTC | 37m |
| N446BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-22 22:44 UTC | 2026-04-22 23:22 UTC | 38m |
| CHH7912 | CHH | London Heathrow Airport (EGLL) | Nida Airport (EYND) | 2026-04-22 21:16 UTC | 2026-04-22 23:20 UTC | 2h 4m |
| SCU15 | SCU | 84OL (84OL) | Hsh Airstrip (5OK9) | 2026-04-22 23:02 UTC | 2026-04-22 23:20 UTC | 17m |
| N6015F |  | Addison Airport (KADS) | Grove Hill Airport (5TX2) | 2026-04-22 22:00 UTC | 2026-04-22 23:18 UTC | 1h 18m |
| EJA593 | EJA | St Louis Lambert International Airport (KSTL) | Moffett Federal Airfield (KNUQ) | 2026-04-22 19:02 UTC | 2026-04-22 23:15 UTC | 4h 13m |
| N52858 |  | Camarillo Airport (KCMA) | Meadows Field (KBFL) | 2026-04-22 22:15 UTC | 2026-04-22 23:15 UTC | 59m |
| ZJF | ZJF | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-04-22 22:48 UTC | 2026-04-22 23:15 UTC | 26m |
| QLK581D | QLK | Adelaide International Airport (YPAD) | Port Lincoln Airport (YPLC) | 2026-04-22 22:35 UTC | 2026-04-22 23:14 UTC | 38m |
| KNG51 | KNG | RNZAF Base Ohakea (NZOH) | RNZAF Base Auckland-Whenuapai (NZWP) | 2026-04-22 21:57 UTC | 2026-04-22 23:12 UTC | 1h 15m |
| LXJ578 | LXJ | Meadows Field (KBFL) | Gansner Field (K2O1) | 2026-04-22 22:26 UTC | 2026-04-22 23:11 UTC | 44m |
| WSN1 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-22 22:32 UTC | 2026-04-22 23:09 UTC | 37m |
| N221ZT |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-04-22 22:59 UTC | 2026-04-22 23:09 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
