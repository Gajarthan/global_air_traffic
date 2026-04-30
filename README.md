# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_10:25:52_UTC-green)

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

**Latest saved flight:** 2026-04-30 10:25:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 10:25:52 UTC

- **60,405** saved flights
- **23,291** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,405** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **736,908.9 tonnes** estimated CO2 emissions
- **42,719,355 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2565 |
| 2 | SkyWest Airlines | 2253 |
| 3 | IndiGo | 1391 |
| 4 | EJA | 1082 |
| 5 | American Airlines | 941 |
| 6 | Southwest Airlines | 854 |
| 7 | Lufthansa | 769 |
| 8 | ENY | 748 |
| 9 | Vueling | 602 |
| 10 | AXM | 592 |
| 11 | LATAM Airlines | 576 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 509 |
| 14 | Delta Air Lines | 503 |
| 15 | AZU | 494 |
| 16 | QLK | 478 |
| 17 | Swiss International | 478 |
| 18 | LXJ | 428 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 401 |
| 21 | easyJet | 399 |
| 22 | EJU | 390 |
| 23 | VIV | 379 |
| 24 | Cathay Pacific | 362 |
| 25 | Air France | 357 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 331 |
| 28 | AIQ | 308 |
| 29 | JetBlue | 300 |
| 30 | United Airlines | 299 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47660 |
| 2 | 🇮🇳 IN | 4392 |
| 3 | 🇪🇸 ES | 4380 |
| 4 | 🇦🇺 AU | 4149 |
| 5 | 🇧🇷 BR | 3409 |
| 6 | 🇩🇪 DE | 3369 |
| 7 | 🇯🇵 JP | 3315 |
| 8 | 🇮🇹 IT | 3310 |
| 9 | 🇨🇦 CA | 2988 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2559 |
| 12 | 🇫🇷 FR | 2386 |
| 13 | 🇲🇽 MX | 1887 |
| 14 | 🇬🇷 GR | 1808 |
| 15 | 🇨🇭 CH | 1690 |
| 16 | 🇳🇴 NO | 1659 |
| 17 | 🇲🇾 MY | 1441 |
| 18 | 🇿🇦 ZA | 1234 |
| 19 | 🇳🇿 NZ | 1137 |
| 20 | 🇹🇭 TH | 1094 |
| 21 | 🇹🇷 TR | 1077 |
| 22 | 🇵🇭 PH | 1023 |
| 23 | 🇰🇷 KR | 983 |
| 24 | 🇵🇱 PL | 978 |
| 25 | 🇬🇹 GT | 876 |
| 26 | 🇲🇦 MA | 755 |
| 27 | 🇲🇴 MO | 672 |
| 28 | 🇲🇪 ME | 662 |
| 29 | 🇳🇱 NL | 636 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1339 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1005 |
| 4 | Indira Gandhi International Airport |  | IN | 926 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 889 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 765 |
| 9 | Frankfurt am Main International Airport |  | DE | 764 |
| 10 | Zurich Airport |  | CH | 729 |
| 11 | Macau International Airport |  | MO | 672 |
| 12 | La Aurora Airport |  | GT | 660 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 599 |
| 14 | Chicago O'Hare International Airport |  | US | 573 |
| 15 | Kuala Lumpur International Airport |  | MY | 567 |
| 16 | Madrid Barajas International Airport |  | ES | 560 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Malpensa International Airport |  | IT | 526 |
| 20 | Bengaluru International Airport |  | IN | 526 |
| 21 | Congonhas Airport |  | BR | 492 |
| 22 | Charlotte/Douglas International Airport |  | US | 478 |
| 23 | Charles de Gaulle International Airport |  | FR | 471 |
| 24 | Tenerife Norte Airport |  | ES | 469 |
| 25 | Salt Lake City International Airport |  | US | 468 |
| 26 | Ninoy Aquino International Airport |  | PH | 468 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 454 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 440 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 31 | Barcelona International Airport |  | ES | 411 |
| 32 | Vitoria/Foronda Airport |  | ES | 405 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 397 |
| 35 | O. R. Tambo International Airport |  | ZA | 391 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 383 |
| 38 | Don Mueang International Airport |  | TH | 376 |
| 39 | Amsterdam Airport Schiphol |  | NL | 372 |
| 40 | Calgary International Airport |  | CA | 358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 179 | 1h 27m | 910 km | 2,808.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 149 | 19m | 165 km | 423.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 144 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 143 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 136 | 26m | 275 km | 644.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 102 | 31m | 369 km | 649.3 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 99 | 27m | 215 km | 366.7 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 84 | 1h 42m | 1,156 km | 1,675.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 79 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 77 | 14m | 154 km | 204.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR646 | Qatar Airways | Hamad International Airport (OTHH) | Simara Airport (VNSI) | 2026-04-30 06:24 UTC | 2026-04-30 10:25 UTC | 4h 1m |
| RYR9227 | Ryanair | Bristol International Airport (EGGD) | Newquay Cornwall Airport (EGHQ) | 2026-04-30 09:49 UTC | 2026-04-30 10:20 UTC | 31m |
| HBEZE | HBE | St Gallen Altenrhein Airport (LSZR) | Bad Ragaz Airport (LSZE) | 2026-04-30 09:41 UTC | 2026-04-30 10:19 UTC | 37m |
| HSOPK4 | HSO | Emden Airport (EDWE) | Juist Airport (EDWJ) | 2026-04-30 09:55 UTC | 2026-04-30 10:16 UTC | 20m |
| DAKAY | DAK | Leipzig Halle Airport (EDDP) | Stuttgart Airport (EDDS) | 2026-04-30 09:27 UTC | 2026-04-30 10:10 UTC | 42m |
| UAE9836 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-30 03:35 UTC | 2026-04-30 10:09 UTC | 6h 33m |
| ZSERS | ZSE | Cape Town International Airport (FACT) | Sutherland Airport (FASL) | 2026-04-30 09:46 UTC | 2026-04-30 10:07 UTC | 20m |
| WZZ55 | Wizz Air | London Gatwick Airport (EGKK) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-30 07:49 UTC | 2026-04-30 10:05 UTC | 2h 15m |
| HBZYI | HBZ | Luzern-Beromunster Airport (LSZO) | LSMF (LSMF) | 2026-04-30 09:47 UTC | 2026-04-30 10:05 UTC | 18m |
| JME515U | JME | Oxford (Kidlington) Airport (EGTK) | Newcastle Airport (EGNT) | 2026-04-30 09:24 UTC | 2026-04-30 10:05 UTC | 40m |
| LTZ303 | LTZ | Wonderboom Airport (FAWB) | Nylstroom Airfield (FANY) | 2026-04-30 09:25 UTC | 2026-04-30 09:58 UTC | 33m |
| LR661 |  | Brisbane International Airport (YBBN) | Tamworth Airport (YSTW) | 2026-04-30 08:47 UTC | 2026-04-30 09:57 UTC | 1h 10m |
| VCJ79X | VCJ | Larnaca International Airport (LCLK) | Diagoras Airport (LGRP) | 2026-04-30 09:00 UTC | 2026-04-30 09:55 UTC | 55m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-04-30 09:18 UTC | 2026-04-30 09:55 UTC | 36m |
| HYD164 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Val-d'Or Airport (CYVO) | 2026-04-30 09:11 UTC | 2026-04-30 09:54 UTC | 43m |
| HNL03A | HNL | Ameland Airport (EHAL) | Ameland Airport (EHAL) | 2026-04-30 09:54 UTC | 2026-04-30 09:54 UTC | 0m |
| RYR1107 | Ryanair | Madrid Barajas International Airport (LEMD) | Ifrane Airport (GMFI) | 2026-04-30 08:50 UTC | 2026-04-30 09:53 UTC | 1h 3m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-04-30 09:13 UTC | 2026-04-30 09:53 UTC | 39m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-29 19:11 UTC | 2026-04-30 09:53 UTC | 14h 41m |
| IBB15WN | IBB | Tenerife Norte Airport (GCXO) | Almeria International Airport (LEAM) | 2026-04-30 07:53 UTC | 2026-04-30 09:52 UTC | 1h 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
