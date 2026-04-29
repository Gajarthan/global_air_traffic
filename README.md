# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_12:42:40_UTC-green)

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

**Latest saved flight:** 2026-04-29 12:42:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 12:42:40 UTC

- **59,023** saved flights
- **22,892** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,023** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **716,865.9 tonnes** estimated CO2 emissions
- **41,557,442 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2512 |
| 2 | SkyWest Airlines | 2204 |
| 3 | IndiGo | 1354 |
| 4 | EJA | 1039 |
| 5 | American Airlines | 924 |
| 6 | Southwest Airlines | 839 |
| 7 | Lufthansa | 754 |
| 8 | ENY | 732 |
| 9 | Vueling | 591 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 561 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 495 |
| 14 | AZU | 487 |
| 15 | Delta Air Lines | 487 |
| 16 | Swiss International | 468 |
| 17 | QLK | 463 |
| 18 | LXJ | 416 |
| 19 | Alaska Airlines | 404 |
| 20 | AEE | 395 |
| 21 | easyJet | 389 |
| 22 | EJU | 384 |
| 23 | VIV | 372 |
| 24 | Air France | 348 |
| 25 | Japan Airlines | 346 |
| 26 | Cathay Pacific | 340 |
| 27 | AXB | 326 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 296 |
| 30 | United Airlines | 295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46542 |
| 2 | 🇪🇸 ES | 4292 |
| 3 | 🇮🇳 IN | 4284 |
| 4 | 🇦🇺 AU | 4025 |
| 5 | 🇧🇷 BR | 3337 |
| 6 | 🇩🇪 DE | 3282 |
| 7 | 🇮🇹 IT | 3249 |
| 8 | 🇯🇵 JP | 3225 |
| 9 | 🇨🇦 CA | 2910 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2496 |
| 12 | 🇫🇷 FR | 2345 |
| 13 | 🇲🇽 MX | 1855 |
| 14 | 🇬🇷 GR | 1773 |
| 15 | 🇨🇭 CH | 1655 |
| 16 | 🇳🇴 NO | 1616 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1206 |
| 19 | 🇳🇿 NZ | 1108 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1067 |
| 22 | 🇵🇭 PH | 1002 |
| 23 | 🇵🇱 PL | 958 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 862 |
| 26 | 🇲🇦 MA | 742 |
| 27 | 🇲🇪 ME | 643 |
| 28 | 🇲🇴 MO | 635 |
| 29 | 🇳🇱 NL | 622 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1321 |
| 2 | Tokyo International Airport |  | JP | 1096 |
| 3 | Denver International Airport |  | US | 982 |
| 4 | Indira Gandhi International Airport |  | IN | 897 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 874 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 750 |
| 9 | Frankfurt am Main International Airport |  | DE | 743 |
| 10 | Zurich Airport |  | CH | 713 |
| 11 | La Aurora Airport |  | GT | 650 |
| 12 | Macau International Airport |  | MO | 635 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 581 |
| 14 | Chicago O'Hare International Airport |  | US | 561 |
| 15 | Kuala Lumpur International Airport |  | MY | 555 |
| 16 | Madrid Barajas International Airport |  | ES | 547 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 543 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 19 | Malpensa International Airport |  | IT | 515 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 481 |
| 22 | Charlotte/Douglas International Airport |  | US | 468 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 460 |
| 25 | Charles de Gaulle International Airport |  | FR | 460 |
| 26 | Capua Airport |  | IT | 459 |
| 27 | Salt Lake City International Airport |  | US | 454 |
| 28 | Daniel K Inouye International Airport |  | US | 442 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 427 |
| 31 | Barcelona International Airport |  | ES | 404 |
| 32 | Vitoria/Foronda Airport |  | ES | 397 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 391 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 389 |
| 35 | O. R. Tambo International Airport |  | ZA | 386 |
| 36 | Reno/Tahoe International Airport |  | US | 376 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 375 |
| 38 | Don Mueang International Airport |  | TH | 366 |
| 39 | Amsterdam Airport Schiphol |  | NL | 363 |
| 40 | Calgary International Airport |  | CA | 347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 195 | 21m | 244 km | 821.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 168 | 28m | 304 km | 880.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 126 | 1h 12m | 770 km | 1,673.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 99 | 31m | 369 km | 630.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 97 | 27m | 215 km | 359.2 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 95 | 20m | 250 km | 410.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 88 | 20m | 147 km | 222.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 82 | 57m | 493 km | 697.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 81 | 1h 43m | 1,156 km | 1,615.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 75 | 14m | 154 km | 198.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASV704 | ASV | Narita International Airport (RJAA) | Oki Airport (RJNO) | 2026-04-29 11:34 UTC | 2026-04-29 12:42 UTC | 1h 8m |
| AFL1443 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-28 18:50 UTC | 2026-04-29 12:35 UTC | 17h 45m |
| MERCS12 | MER | A 511 Airport (RKSG) | A 511 Airport (RKSG) | 2026-04-29 11:57 UTC | 2026-04-29 12:30 UTC | 32m |
| NAK701 | NAK | Saint-Yan Airport (LFLN) | St Galmier Airport (LFKM) | 2026-04-29 11:56 UTC | 2026-04-29 12:28 UTC | 32m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-04-28 21:55 UTC | 2026-04-29 12:25 UTC | 14h 30m |
| OOSKU | OOS | Ostend-Bruges International Airport (EBOS) | Tournai/Maubray Airport (EBTY) | 2026-04-29 12:00 UTC | 2026-04-29 12:21 UTC | 21m |
| POL5440 | POL | Stockholm-Arlanda Airport (ESSA) | Stockholm-Arlanda Airport (ESSA) | 2026-04-29 11:26 UTC | 2026-04-29 12:20 UTC | 54m |
| N439H |  | Bradley International Airport (KBDL) | Laguardia Airport (KLGA) | 2026-04-29 11:35 UTC | 2026-04-29 12:19 UTC | 44m |
| CHX89 | CHX | Regensburg-Oberhub Airport (EDNR) | Griesau Airport (EDPG) | 2026-04-29 12:10 UTC | 2026-04-29 12:17 UTC | 7m |
| GAF434 | GAF | Wunstorf Airport (ETNW) | Siegerland Airport (EDGS) | 2026-04-29 11:43 UTC | 2026-04-29 12:14 UTC | 31m |
| EZY9 | easyJet | Durham Tees Valley Airport (EGNV) | Durham Tees Valley Airport (EGNV) | 2026-04-29 10:54 UTC | 2026-04-29 12:14 UTC | 1h 19m |
| N254EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-29 11:09 UTC | 2026-04-29 12:03 UTC | 53m |
| AUA679 | Austrian Airlines | Vienna International Airport (LOWW) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-29 11:26 UTC | 2026-04-29 12:01 UTC | 35m |
| AXM6038 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-29 11:35 UTC | 2026-04-29 11:59 UTC | 24m |
| SPEGR | SPE | Pobiednik Wielki Airport (EPKP) | Nowy Targ Airport (EPNT) | 2026-04-29 11:34 UTC | 2026-04-29 11:54 UTC | 20m |
| OAL069 | OAL | Paros Airport (LGPA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-29 11:28 UTC | 2026-04-29 11:52 UTC | 23m |
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-04-29 11:04 UTC | 2026-04-29 11:50 UTC | 46m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-29 11:34 UTC | 2026-04-29 11:49 UTC | 15m |
| KLM59J | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Słupsk-Krępa Airport (EPSR) | 2026-04-29 10:31 UTC | 2026-04-29 11:47 UTC | 1h 15m |
| CGEPQ | CGE | Brampton Airport (CNC3) | Grand Valley / Luther Field (CGV2) | 2026-04-29 11:27 UTC | 2026-04-29 11:47 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
