# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_11:03:44_UTC-green)

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

**Latest saved flight:** 2026-04-27 11:03:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 11:03:44 UTC

- **56,659** saved flights
- **22,197** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,659** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **688,677.2 tonnes** estimated CO2 emissions
- **39,923,315 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2412 |
| 2 | SkyWest Airlines | 2134 |
| 3 | IndiGo | 1295 |
| 4 | EJA | 1012 |
| 5 | American Airlines | 900 |
| 6 | Southwest Airlines | 804 |
| 7 | ENY | 714 |
| 8 | Lufthansa | 702 |
| 9 | Vueling | 569 |
| 10 | AXM | 553 |
| 11 | LATAM Airlines | 548 |
| 12 | All Nippon Airways | 501 |
| 13 | AZU | 475 |
| 14 | WIF | 472 |
| 15 | Delta Air Lines | 466 |
| 16 | Swiss International | 447 |
| 17 | QLK | 439 |
| 18 | LXJ | 404 |
| 19 | Alaska Airlines | 380 |
| 20 | AEE | 372 |
| 21 | EJU | 366 |
| 22 | easyJet | 361 |
| 23 | VIV | 361 |
| 24 | Air France | 330 |
| 25 | Cathay Pacific | 327 |
| 26 | Japan Airlines | 327 |
| 27 | AXB | 311 |
| 28 | JetBlue | 289 |
| 29 | AIQ | 286 |
| 30 | GLO | 285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44820 |
| 2 | 🇪🇸 ES | 4143 |
| 3 | 🇮🇳 IN | 4083 |
| 4 | 🇦🇺 AU | 3808 |
| 5 | 🇧🇷 BR | 3259 |
| 6 | 🇩🇪 DE | 3110 |
| 7 | 🇮🇹 IT | 3096 |
| 8 | 🇯🇵 JP | 3046 |
| 9 | 🇨🇦 CA | 2791 |
| 10 | 🇨🇴 CO | 2558 |
| 11 | 🇬🇧 GB | 2386 |
| 12 | 🇫🇷 FR | 2231 |
| 13 | 🇲🇽 MX | 1799 |
| 14 | 🇬🇷 GR | 1677 |
| 15 | 🇨🇭 CH | 1601 |
| 16 | 🇳🇴 NO | 1526 |
| 17 | 🇲🇾 MY | 1342 |
| 18 | 🇿🇦 ZA | 1157 |
| 19 | 🇳🇿 NZ | 1072 |
| 20 | 🇹🇷 TR | 1036 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 964 |
| 23 | 🇵🇱 PL | 918 |
| 24 | 🇰🇷 KR | 903 |
| 25 | 🇬🇹 GT | 842 |
| 26 | 🇲🇦 MA | 717 |
| 27 | 🇲🇪 ME | 617 |
| 28 | 🇲🇴 MO | 604 |
| 29 | 🇳🇱 NL | 595 |
| 30 | 🇮🇩 ID | 488 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1284 |
| 2 | Tokyo International Airport |  | JP | 1034 |
| 3 | Denver International Airport |  | US | 939 |
| 4 | Indira Gandhi International Airport |  | IN | 865 |
| 5 | El Dorado International Airport |  | CO | 864 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 826 |
| 7 | Guaymaral Airport |  | CO | 778 |
| 8 | Harry Reid International Airport |  | US | 721 |
| 9 | Frankfurt am Main International Airport |  | DE | 690 |
| 10 | Zurich Airport |  | CH | 683 |
| 11 | La Aurora Airport |  | GT | 633 |
| 12 | Macau International Airport |  | MO | 604 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 562 |
| 14 | Chicago O'Hare International Airport |  | US | 551 |
| 15 | Madrid Barajas International Airport |  | ES | 531 |
| 16 | Kuala Lumpur International Airport |  | MY | 528 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 526 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 501 |
| 19 | Malpensa International Airport |  | IT | 492 |
| 20 | Bengaluru International Airport |  | IN | 489 |
| 21 | Congonhas Airport |  | BR | 468 |
| 22 | Charlotte/Douglas International Airport |  | US | 456 |
| 23 | Tenerife Norte Airport |  | ES | 455 |
| 24 | Ninoy Aquino International Airport |  | PH | 443 |
| 25 | Charles de Gaulle International Airport |  | FR | 436 |
| 26 | Salt Lake City International Airport |  | US | 433 |
| 27 | Capua Airport |  | IT | 423 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 419 |
| 29 | Daniel K Inouye International Airport |  | US | 417 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 408 |
| 31 | Barcelona International Airport |  | ES | 387 |
| 32 | Vitoria/Foronda Airport |  | ES | 387 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 382 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 377 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 368 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 363 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 340 |
| 40 | Calgary International Airport |  | CA | 337 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 317 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 208 | 14m | 114 km | 408.0 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 181 | 21m | 244 km | 762.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 163 | 1h 27m | 910 km | 2,557.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 136 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 111 | 1h 12m | 770 km | 1,474.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 109 | 44m | 452 km | 849.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 96 | 31m | 369 km | 611.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 1m | 695 km | 970.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 53m | 1,304 km | 1,732.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 72 | 1h 42m | 1,423 km | 1,767.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N946HC |  | Dekalb-Peachtree Airport (KPDK) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-04-27 10:41 UTC | 2026-04-27 11:03 UTC | 22m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-04-27 09:45 UTC | 2026-04-27 10:53 UTC | 1h 8m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-04-27 10:39 UTC | 2026-04-27 10:51 UTC | 11m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-26 19:54 UTC | 2026-04-27 10:50 UTC | 14h 56m |
| DEBPC | DEB | Munster Osnabruck Airport (EDDG) | Osnabruck-Atterheide Airport (EDWO) | 2026-04-27 10:16 UTC | 2026-04-27 10:48 UTC | 31m |
| LIFELN1 | LIF | Rotterdam Airport (EHRD) | Amsterdam Airport Schiphol (EHAM) | 2026-04-27 10:35 UTC | 2026-04-27 10:47 UTC | 12m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-27 10:17 UTC | 2026-04-27 10:30 UTC | 13m |
| RYR80NW | Ryanair | London Luton Airport (EGGW) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-27 08:23 UTC | 2026-04-27 10:21 UTC | 1h 57m |
| DRAGO74 | DRA | Sallanches Airport (LFHZ) | Sallanches Airport (LFHZ) | 2026-04-27 09:46 UTC | 2026-04-27 10:17 UTC | 31m |
| CGSAG | CGS | Montréal / St-Hubert Airport (CYHU) | Greenville Municipal Airport (K3B1) | 2026-04-27 09:08 UTC | 2026-04-27 10:09 UTC | 1h 0m |
| LGL4593 | LGL | Luxembourg-Findel International Airport (ELLX) | London City Airport (EGLC) | 2026-04-27 08:57 UTC | 2026-04-27 10:08 UTC | 1h 11m |
| VLG83CM | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-04-27 09:09 UTC | 2026-04-27 10:07 UTC | 58m |
| DLA6YF | DLA | Munich International Airport (EDDM) | Malpensa International Airport (LIMC) | 2026-04-27 09:19 UTC | 2026-04-27 10:07 UTC | 48m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-26 19:56 UTC | 2026-04-27 10:05 UTC | 14h 8m |
| AIQ3207 | AIQ | Don Mueang International Airport (VTBD) | VLXL (VLXL) | 2026-04-27 09:11 UTC | 2026-04-27 10:04 UTC | 52m |
| PBD414 | PBD | Maksimovka Airport (UWUM) | Bezymyanka Airfield (UWWG) | 2026-04-27 09:39 UTC | 2026-04-27 10:03 UTC | 24m |
| AGV01 | AGV | St Stephan Airport (LSTS) | Sion Airport (LSGS) | 2026-04-27 10:01 UTC | 2026-04-27 10:02 UTC | 0m |
| RYR4RZ | Ryanair | Toulouse-Blagnac Airport (LFBO) | Bruntingthorpe Airport (EG74) | 2026-04-27 08:29 UTC | 2026-04-27 10:01 UTC | 1h 32m |
| RYR5514 | Ryanair | Torino / Caselle International Airport (LIMF) | Oristano / Fenosu Airport (LIER) | 2026-04-27 09:10 UTC | 2026-04-27 10:01 UTC | 51m |
| AIC5NQ | Air India | Indira Gandhi International Airport (VIDP) | Kalka Airport (VI71) | 2026-04-27 09:32 UTC | 2026-04-27 10:00 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
