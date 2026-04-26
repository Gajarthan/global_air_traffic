# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_14:06:11_UTC-green)

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

**Latest saved flight:** 2026-04-26 14:06:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 14:06:11 UTC

- **55,290** saved flights
- **21,758** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,290** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **668,190.9 tonnes** estimated CO2 emissions
- **38,735,707 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2343 |
| 2 | SkyWest Airlines | 2076 |
| 3 | IndiGo | 1261 |
| 4 | EJA | 968 |
| 5 | American Airlines | 880 |
| 6 | Southwest Airlines | 781 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 680 |
| 9 | Vueling | 557 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 531 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 466 |
| 14 | WIF | 455 |
| 15 | Delta Air Lines | 453 |
| 16 | Swiss International | 433 |
| 17 | QLK | 429 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 367 |
| 21 | EJU | 358 |
| 22 | easyJet | 355 |
| 23 | VIV | 352 |
| 24 | Air France | 321 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 312 |
| 27 | AXB | 297 |
| 28 | AIQ | 282 |
| 29 | JetBlue | 281 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43734 |
| 2 | 🇪🇸 ES | 4035 |
| 3 | 🇮🇳 IN | 3987 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3183 |
| 6 | 🇩🇪 DE | 3020 |
| 7 | 🇮🇹 IT | 3008 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2729 |
| 10 | 🇨🇴 CO | 2491 |
| 11 | 🇬🇧 GB | 2324 |
| 12 | 🇫🇷 FR | 2190 |
| 13 | 🇲🇽 MX | 1723 |
| 14 | 🇬🇷 GR | 1649 |
| 15 | 🇨🇭 CH | 1571 |
| 16 | 🇳🇴 NO | 1479 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1145 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1007 |
| 21 | 🇹🇭 TH | 1003 |
| 22 | 🇵🇭 PH | 944 |
| 23 | 🇰🇷 KR | 894 |
| 24 | 🇵🇱 PL | 893 |
| 25 | 🇬🇹 GT | 826 |
| 26 | 🇲🇦 MA | 703 |
| 27 | 🇲🇪 ME | 606 |
| 28 | 🇳🇱 NL | 571 |
| 29 | 🇲🇴 MO | 568 |
| 30 | 🇮🇩 ID | 476 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1249 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 912 |
| 4 | Indira Gandhi International Airport |  | IN | 845 |
| 5 | El Dorado International Airport |  | CO | 841 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 813 |
| 7 | Guaymaral Airport |  | CO | 755 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Zurich Airport |  | CH | 666 |
| 10 | Frankfurt am Main International Airport |  | DE | 661 |
| 11 | La Aurora Airport |  | GT | 619 |
| 12 | Macau International Airport |  | MO | 568 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 536 |
| 15 | Kuala Lumpur International Airport |  | MY | 523 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 17 | Madrid Barajas International Airport |  | ES | 512 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 475 |
| 20 | Bengaluru International Airport |  | IN | 471 |
| 21 | Congonhas Airport |  | BR | 456 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 442 |
| 24 | Ninoy Aquino International Airport |  | PH | 435 |
| 25 | Charles de Gaulle International Airport |  | FR | 425 |
| 26 | Salt Lake City International Airport |  | US | 415 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Capua Airport |  | IT | 409 |
| 29 | Daniel K Inouye International Airport |  | US | 407 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 398 |
| 31 | Vitoria/Foronda Airport |  | ES | 381 |
| 32 | Barcelona International Airport |  | ES | 377 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 368 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 368 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 362 |
| 37 | O. R. Tambo International Airport |  | ZA | 357 |
| 38 | Don Mueang International Airport |  | TH | 340 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Viracopos International Airport |  | BR | 325 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 307 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 201 | 14m | 114 km | 394.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 128 | 26m | 275 km | 606.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 92 | 27m | 215 km | 340.7 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 84 | 27m | 152 km | 219.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 73 | 58m | 493 km | 621.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DIFEF | DIF | Leutkirch-Unterzeil Airport (EDNL) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-26 13:07 UTC | 2026-04-26 14:06 UTC | 59m |
| AIZ102 | AIZ | Diagoras Airport (LGRP) | LLTN (LLTN) | 2026-04-26 12:54 UTC | 2026-04-26 14:03 UTC | 1h 9m |
| N55FA |  | Wings Field (KLOM) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-26 13:36 UTC | 2026-04-26 14:00 UTC | 24m |
| DEQHS | DEQ | Meschede-Schuren Airport (EDKM) | Meschede-Schuren Airport (EDKM) | 2026-04-26 13:58 UTC | 2026-04-26 13:59 UTC | 1m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-04-26 13:45 UTC | 2026-04-26 13:59 UTC | 13m |
| SRG199 | SRG | Cumbernauld Airport (EGPG) | Glasgow International Airport (EGPF) | 2026-04-26 13:39 UTC | 2026-04-26 13:54 UTC | 14m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-26 13:27 UTC | 2026-04-26 13:50 UTC | 22m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-26 13:31 UTC | 2026-04-26 13:43 UTC | 12m |
| GOHST | GOH | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-04-26 13:36 UTC | 2026-04-26 13:40 UTC | 3m |
| N9042H |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-26 13:35 UTC | 2026-04-26 13:35 UTC | 0m |
| N410UV |  | Fort Lauderdale Executive Airport (KFXE) | Palm Beach County Park Airport (KLNA) | 2026-04-26 13:13 UTC | 2026-04-26 13:35 UTC | 21m |
| GRAZE | GRA | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-04-26 12:10 UTC | 2026-04-26 13:34 UTC | 1h 24m |
| HLE60 | HLE | Redhill Aerodrome (EGKR) | Shoreham Airport (EGKA) | 2026-04-26 13:19 UTC | 2026-04-26 13:34 UTC | 15m |
| N7164C |  | FL61 (FL61) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-04-26 13:09 UTC | 2026-04-26 13:32 UTC | 23m |
| RYR7ZX | Ryanair | Luqa Airport (LMML) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-26 12:06 UTC | 2026-04-26 13:29 UTC | 1h 23m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-26 13:03 UTC | 2026-04-26 13:26 UTC | 23m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-04-26 13:16 UTC | 2026-04-26 13:25 UTC | 9m |
| WZZ4764 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Bari / Palese International Airport (LIBD) | 2026-04-26 12:05 UTC | 2026-04-26 13:19 UTC | 1h 14m |
| N9042H |  | Albert Whitted Airport (KSPG) | Winter Haven Regional Airport (KGIF) | 2026-04-26 12:44 UTC | 2026-04-26 13:19 UTC | 35m |
| EMO18 | EMO | Nice-Cote d'Azur Airport (LFMN) | Samedan Airport (LSZS) | 2026-04-26 12:39 UTC | 2026-04-26 13:18 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
