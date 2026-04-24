# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_17:24:42_UTC-green)

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

**Latest saved flight:** 2026-04-24 17:24:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 17:24:42 UTC

- **51,824** saved flights
- **20,734** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **51,824** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **619,281.3 tonnes** estimated CO2 emissions
- **35,900,364 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2185 |
| 2 | SkyWest Airlines | 1955 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 897 |
| 5 | American Airlines | 830 |
| 6 | Southwest Airlines | 731 |
| 7 | ENY | 658 |
| 8 | Lufthansa | 607 |
| 9 | Vueling | 520 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 498 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 437 |
| 14 | WIF | 432 |
| 15 | Delta Air Lines | 423 |
| 16 | QLK | 412 |
| 17 | Swiss International | 396 |
| 18 | LXJ | 386 |
| 19 | AEE | 351 |
| 20 | Alaska Airlines | 338 |
| 21 | EJU | 331 |
| 22 | easyJet | 329 |
| 23 | VIV | 326 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 302 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 272 |
| 28 | JetBlue | 267 |
| 29 | United Airlines | 265 |
| 30 | AIQ | 264 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 41062 |
| 2 | 🇮🇳 IN | 3767 |
| 3 | 🇪🇸 ES | 3754 |
| 4 | 🇦🇺 AU | 3570 |
| 5 | 🇧🇷 BR | 2982 |
| 6 | 🇯🇵 JP | 2809 |
| 7 | 🇮🇹 IT | 2788 |
| 8 | 🇩🇪 DE | 2779 |
| 9 | 🇨🇦 CA | 2579 |
| 10 | 🇨🇴 CO | 2392 |
| 11 | 🇬🇧 GB | 2159 |
| 12 | 🇫🇷 FR | 2016 |
| 13 | 🇲🇽 MX | 1597 |
| 14 | 🇬🇷 GR | 1573 |
| 15 | 🇨🇭 CH | 1462 |
| 16 | 🇳🇴 NO | 1402 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1077 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 936 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 832 |
| 25 | 🇬🇹 GT | 795 |
| 26 | 🇲🇦 MA | 637 |
| 27 | 🇲🇪 ME | 551 |
| 28 | 🇳🇱 NL | 526 |
| 29 | 🇲🇴 MO | 497 |
| 30 | 🇧🇸 BS | 454 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1183 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 855 |
| 4 | El Dorado International Airport |  | CO | 815 |
| 5 | Indira Gandhi International Airport |  | IN | 803 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 779 |
| 7 | Guaymaral Airport |  | CO | 708 |
| 8 | Harry Reid International Airport |  | US | 670 |
| 9 | Zurich Airport |  | CH | 611 |
| 10 | La Aurora Airport |  | GT | 593 |
| 11 | Frankfurt am Main International Airport |  | DE | 593 |
| 12 | Chicago O'Hare International Airport |  | US | 510 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 503 |
| 14 | Macau International Airport |  | MO | 497 |
| 15 | Kuala Lumpur International Airport |  | MY | 491 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 488 |
| 17 | Madrid Barajas International Airport |  | ES | 474 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 432 |
| 21 | Charlotte/Douglas International Airport |  | US | 429 |
| 22 | Malpensa International Airport |  | IT | 428 |
| 23 | Ninoy Aquino International Airport |  | PH | 414 |
| 24 | Tenerife Norte Airport |  | ES | 413 |
| 25 | Charles de Gaulle International Airport |  | FR | 395 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 387 |
| 27 | Salt Lake City International Airport |  | US | 379 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 29 | Daniel K Inouye International Airport |  | US | 376 |
| 30 | Capua Airport |  | IT | 361 |
| 31 | Vitoria/Foronda Airport |  | ES | 352 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 349 |
| 33 | Barcelona International Airport |  | ES | 349 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 346 |
| 35 | Reno/Tahoe International Airport |  | US | 346 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 344 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 312 |
| 40 | Viracopos International Airport |  | BR | 303 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 287 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 197 | 14m | 114 km | 386.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 155 | 21m | 244 km | 652.7 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 128 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 121 | 26m | 275 km | 573.4 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 86 | 26m | 215 km | 318.5 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 81 | 52m | 556 km | 776.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 78 | 27m | 152 km | 203.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 74 | 1h 41m | 1,156 km | 1,476.3 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 74 | 1h 0m | 695 km | 887.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 67 | 13m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 66 | 1h 20m | 961 km | 1,094.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2382R |  | Tampa Executive Airport (KVDF) | Ocala International-Jim Taylor Field (KOCF) | 2026-04-24 16:40 UTC | 2026-04-24 17:24 UTC | 44m |
| N52380 |  | Mcnary Field (KSLE) | Corvallis Municipal Airport (KCVO) | 2026-04-24 16:56 UTC | 2026-04-24 17:19 UTC | 23m |
| N661LF |  | Bradshaw Army Airfield (PHSF) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-04-24 17:00 UTC | 2026-04-24 17:19 UTC | 18m |
| ERU934 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-24 16:06 UTC | 2026-04-24 17:17 UTC | 1h 10m |
| N48FG |  | Addison Airport (KADS) | Austin-Bergstrom International Airport (KAUS) | 2026-04-24 16:28 UTC | 2026-04-24 17:17 UTC | 48m |
| N985AA |  | Sanctuary Ranch Airport (7TS4) | Carter-Norman Airport (TA87) | 2026-04-24 16:39 UTC | 2026-04-24 17:09 UTC | 30m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-04-24 16:51 UTC | 2026-04-24 17:09 UTC | 17m |
| N774MA |  | French Valley Airport (KF70) | Borrego Valley Airport (KL08) | 2026-04-24 16:58 UTC | 2026-04-24 17:08 UTC | 10m |
| FSF797A | FSF | Biella / Cerrione Airport (LILE) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-24 16:23 UTC | 2026-04-24 17:05 UTC | 41m |
| HK4303G |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-04-24 16:48 UTC | 2026-04-24 17:02 UTC | 14m |
| N55449 |  | 1NY9 (1NY9) | Oswego County Airport (KFZY) | 2026-04-24 16:45 UTC | 2026-04-24 17:01 UTC | 16m |
| SH208 |  | Atmore Municipal Airport (K0R1) | 49FL (49FL) | 2026-04-24 16:58 UTC | 2026-04-24 17:00 UTC | 1m |
| CXK483 | CXK | Lake In The Hills Airport (K3CK) | Lake In The Hills Airport (K3CK) | 2026-04-24 16:28 UTC | 2026-04-24 16:59 UTC | 31m |
| N31532 |  | New Garden Airport (KN57) | Chester County G O Carlson Airport (KMQS) | 2026-04-24 16:35 UTC | 2026-04-24 16:59 UTC | 24m |
| N45ME |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-04-24 16:49 UTC | 2026-04-24 16:58 UTC | 8m |
| AXEL90 | AXE | Robert Gray Army Air Field (KGRK) | KI58 (KI58) | 2026-04-24 15:49 UTC | 2026-04-24 16:56 UTC | 1h 7m |
| AMMO79 | AMM | 0CL8 (0CL8) | 0CL8 (0CL8) | 2026-04-24 16:39 UTC | 2026-04-24 16:56 UTC | 16m |
| CXK126 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-24 16:27 UTC | 2026-04-24 16:54 UTC | 27m |
| N600HN |  | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-24 16:42 UTC | 2026-04-24 16:54 UTC | 11m |
| N425CB |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Lawrence Smith Memorial Airport (KLRY) | 2026-04-24 16:31 UTC | 2026-04-24 16:53 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
