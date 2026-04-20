# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_11:27:16_UTC-green)

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

**Latest saved flight:** 2026-04-20 11:27:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 11:27:16 UTC

- **44,876** saved flights
- **18,564** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,876** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **542,459.8 tonnes** estimated CO2 emissions
- **31,446,946 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1898 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1079 |
| 4 | EJA | 779 |
| 5 | American Airlines | 741 |
| 6 | Southwest Airlines | 642 |
| 7 | ENY | 584 |
| 8 | Lufthansa | 455 |
| 9 | AXM | 453 |
| 10 | Vueling | 449 |
| 11 | LATAM Airlines | 447 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 389 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 366 |
| 16 | LXJ | 354 |
| 17 | WIF | 351 |
| 18 | Swiss International | 348 |
| 19 | Alaska Airlines | 308 |
| 20 | AEE | 307 |
| 21 | EJU | 296 |
| 22 | easyJet | 289 |
| 23 | VIV | 285 |
| 24 | Japan Airlines | 274 |
| 25 | Air France | 257 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 237 |
| 28 | AXB | 236 |
| 29 | GLO | 234 |
| 30 | Cathay Pacific | 232 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35435 |
| 2 | 🇮🇳 IN | 3346 |
| 3 | 🇪🇸 ES | 3293 |
| 4 | 🇦🇺 AU | 3126 |
| 5 | 🇧🇷 BR | 2666 |
| 6 | 🇯🇵 JP | 2480 |
| 7 | 🇮🇹 IT | 2403 |
| 8 | 🇩🇪 DE | 2297 |
| 9 | 🇨🇦 CA | 2177 |
| 10 | 🇨🇴 CO | 2061 |
| 11 | 🇬🇧 GB | 1826 |
| 12 | 🇫🇷 FR | 1704 |
| 13 | 🇲🇽 MX | 1399 |
| 14 | 🇬🇷 GR | 1388 |
| 15 | 🇨🇭 CH | 1226 |
| 16 | 🇳🇴 NO | 1115 |
| 17 | 🇲🇾 MY | 1110 |
| 18 | 🇿🇦 ZA | 946 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 808 |
| 21 | 🇵🇭 PH | 805 |
| 22 | 🇹🇷 TR | 794 |
| 23 | 🇰🇷 KR | 744 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 714 |
| 26 | 🇲🇦 MA | 554 |
| 27 | 🇲🇪 ME | 476 |
| 28 | 🇳🇱 NL | 457 |
| 29 | 🇲🇴 MO | 419 |
| 30 | 🇧🇸 BS | 411 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1051 |
| 2 | Tokyo International Airport |  | JP | 845 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | Indira Gandhi International Airport |  | IN | 724 |
| 5 | El Dorado International Airport |  | CO | 721 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 688 |
| 7 | Harry Reid International Airport |  | US | 581 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 539 |
| 11 | Chicago O'Hare International Airport |  | US | 442 |
| 12 | Kuala Lumpur International Airport |  | MY | 442 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Frankfurt am Main International Airport |  | DE | 427 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 420 |
| 17 | Macau International Airport |  | MO | 419 |
| 18 | Madrid Barajas International Airport |  | ES | 400 |
| 19 | Bengaluru International Airport |  | IN | 397 |
| 20 | Tenerife Norte Airport |  | ES | 392 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Congonhas Airport |  | BR | 382 |
| 23 | Malpensa International Airport |  | IT | 381 |
| 24 | Ninoy Aquino International Airport |  | PH | 373 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Daniel K Inouye International Airport |  | US | 334 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 334 |
| 29 | Charles de Gaulle International Airport |  | FR | 332 |
| 30 | Capua Airport |  | IT | 315 |
| 31 | Reno/Tahoe International Airport |  | US | 311 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 311 |
| 33 | Vitoria/Foronda Airport |  | ES | 309 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 303 |
| 35 | O. R. Tambo International Airport |  | ZA | 302 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 301 |
| 37 | Barcelona International Airport |  | ES | 289 |
| 38 | Calgary International Airport |  | CA | 273 |
| 39 | Don Mueang International Airport |  | TH | 273 |
| 40 | Viracopos International Airport |  | BR | 270 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 211 | 1h 7m | 706 km | 2,568.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 136 | 28m | 304 km | 712.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 128 | 21m | 244 km | 539.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 121 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 121 | 19m | 165 km | 344.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 103 | 26m | 275 km | 488.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 97 | 54m | 546 km | 913.3 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 75 | 20m | 250 km | 324.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 69 | 26m | 215 km | 255.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 65 | 13m | 99 km | 111.5 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 62 | 57m | 493 km | 527.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHH762 | CHH | Budapest Ferenc Liszt International Airport (LHBP) | Smolensk North Airport (XUBS) | 2026-04-20 10:01 UTC | 2026-04-20 11:27 UTC | 1h 25m |
| ETP08 | ETP | MoD Boscombe Down Airport (EGDM) | Old Sarum Airfield (EGLS) | 2026-04-20 10:23 UTC | 2026-04-20 11:24 UTC | 1h 1m |
| AVA9252 | Avianca | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 2026-04-20 10:42 UTC | 2026-04-20 10:54 UTC | 11m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-20 10:40 UTC | 2026-04-20 10:51 UTC | 11m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-04-20 10:23 UTC | 2026-04-20 10:51 UTC | 28m |
| TUCAN35 | TUC | Alcantarilla Airport (LERI) | Alcantarilla Airport (LERI) | 2026-04-20 10:27 UTC | 2026-04-20 10:50 UTC | 23m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-20 10:16 UTC | 2026-04-20 10:50 UTC | 33m |
|  |  | Gullknapp Flpl Airport (ENGK) | Gullknapp Flpl Airport (ENGK) | 2026-04-20 10:43 UTC | 2026-04-20 10:49 UTC | 6m |
| N1219M |  | Gerald R Ford International Airport (KGRR) | Campbell-Pratt Airport (KY65) | 2026-04-20 10:17 UTC | 2026-04-20 10:44 UTC | 27m |
| HNL04B | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-04-20 10:15 UTC | 2026-04-20 10:44 UTC | 29m |
| RK11 |  | Malmen Air Base (ESCF) | Karlsborg Air Base (ESIA) | 2026-04-20 10:28 UTC | 2026-04-20 10:39 UTC | 11m |
| EZY72EJ | easyJet | Belfast International Airport (EGAA) | Newcastle Airport (EGNT) | 2026-04-20 10:03 UTC | 2026-04-20 10:37 UTC | 33m |
| DLH4HU | Lufthansa | John Paul II International Airport Kraków-Balice Airport (EPKK) | Frankfurt am Main International Airport (EDDF) | 2026-04-20 09:28 UTC | 2026-04-20 10:34 UTC | 1h 6m |
| VUMAB | VUM | Willingdon Island Air Base (VOCC) | VEVZ (VEVZ) | 2026-04-20 07:49 UTC | 2026-04-20 10:33 UTC | 2h 43m |
| AXB1407 | AXB | Bengaluru International Airport (VOBL) | Suketar Airport (VNTJ) | 2026-04-20 08:32 UTC | 2026-04-20 10:32 UTC | 2h 0m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-04-20 09:54 UTC | 2026-04-20 10:31 UTC | 36m |
| LNK651R | LNK | Cape Town International Airport (FACT) | Barberton Airport (FABR) | 2026-04-20 08:46 UTC | 2026-04-20 10:30 UTC | 1h 43m |
| KEEP12 | KEE | A 511 Airport (RKSG) | A 511 Airport (RKSG) | 2026-04-20 09:35 UTC | 2026-04-20 10:30 UTC | 55m |
| ANE1099 | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-04-20 10:02 UTC | 2026-04-20 10:28 UTC | 25m |
| AXM6220 | AXM | Kuala Lumpur International Airport (WMKK) | Sungai Tiang Airport (WMAN) | 2026-04-20 10:12 UTC | 2026-04-20 10:28 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
