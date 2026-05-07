# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_01:08:42_UTC-green)

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

**Latest saved flight:** 2026-05-07 01:08:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 01:08:42 UTC

- **71,641** saved flights
- **26,637** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,641** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **883,028.0 tonnes** estimated CO2 emissions
- **51,190,027 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3081 |
| 2 | SkyWest Airlines | 2670 |
| 3 | IndiGo | 1621 |
| 4 | EJA | 1314 |
| 5 | American Airlines | 1123 |
| 6 | Southwest Airlines | 1045 |
| 7 | Lufthansa | 922 |
| 8 | ENY | 900 |
| 9 | Vueling | 702 |
| 10 | AXM | 682 |
| 11 | LATAM Airlines | 668 |
| 12 | WIF | 611 |
| 13 | Delta Air Lines | 601 |
| 14 | All Nippon Airways | 594 |
| 15 | AZU | 580 |
| 16 | QLK | 551 |
| 17 | Swiss International | 551 |
| 18 | LXJ | 521 |
| 19 | Alaska Airlines | 504 |
| 20 | easyJet | 476 |
| 21 | AEE | 460 |
| 22 | EJU | 459 |
| 23 | Cathay Pacific | 445 |
| 24 | VIV | 445 |
| 25 | Japan Airlines | 422 |
| 26 | Air France | 418 |
| 27 | AXB | 395 |
| 28 | AIQ | 358 |
| 29 | CXK | 357 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57314 |
| 2 | 🇪🇸 ES | 5203 |
| 3 | 🇮🇳 IN | 5091 |
| 4 | 🇦🇺 AU | 4769 |
| 5 | 🇧🇷 BR | 4020 |
| 6 | 🇩🇪 DE | 3983 |
| 7 | 🇮🇹 IT | 3921 |
| 8 | 🇯🇵 JP | 3804 |
| 9 | 🇨🇦 CA | 3563 |
| 10 | 🇬🇧 GB | 3087 |
| 11 | 🇫🇷 FR | 2815 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2260 |
| 14 | 🇬🇷 GR | 2126 |
| 15 | 🇳🇴 NO | 1964 |
| 16 | 🇨🇭 CH | 1951 |
| 17 | 🇲🇾 MY | 1700 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1314 |
| 20 | 🇹🇷 TR | 1287 |
| 21 | 🇹🇭 TH | 1285 |
| 22 | 🇵🇱 PL | 1189 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1140 |
| 25 | 🇰🇷 KR | 1133 |
| 26 | 🇲🇦 MA | 853 |
| 27 | 🇲🇴 MO | 832 |
| 28 | 🇲🇪 ME | 767 |
| 29 | 🇳🇱 NL | 744 |
| 30 | 🇧🇸 BS | 605 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1602 |
| 2 | Tokyo International Airport |  | JP | 1282 |
| 3 | Denver International Airport |  | US | 1200 |
| 4 | Indira Gandhi International Airport |  | IN | 1072 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1040 |
| 6 | Frankfurt am Main International Airport |  | DE | 915 |
| 7 | Harry Reid International Airport |  | US | 898 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | La Aurora Airport |  | GT | 849 |
| 11 | Zurich Airport |  | CH | 849 |
| 12 | Macau International Airport |  | MO | 832 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 724 |
| 14 | Chicago O'Hare International Airport |  | US | 699 |
| 15 | Kuala Lumpur International Airport |  | MY | 682 |
| 16 | Madrid Barajas International Airport |  | ES | 678 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 641 |
| 18 | Malpensa International Airport |  | IT | 625 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 621 |
| 20 | Bengaluru International Airport |  | IN | 616 |
| 21 | Salt Lake City International Airport |  | US | 581 |
| 22 | Congonhas Airport |  | BR | 570 |
| 23 | Charlotte/Douglas International Airport |  | US | 564 |
| 24 | Capua Airport |  | IT | 562 |
| 25 | Charles de Gaulle International Airport |  | FR | 559 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 527 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 491 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 480 |
| 34 | Vitoria/Foronda Airport |  | ES | 471 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 452 |
| 37 | Amsterdam Airport Schiphol |  | NL | 444 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Calgary International Airport |  | CA | 430 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 251 | 21m | 244 km | 1,056.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 179 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 175 | 20m | 165 km | 497.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 134 | 21m | 99 km | 229.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 102 | 14m | 154 km | 270.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 95 | 1h 43m | 1,423 km | 2,331.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TMN1D | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-06 22:04 UTC | 2026-05-07 01:08 UTC | 3h 4m |
| LXJ601 | LXJ | General Edward Lawrence Logan International Airport (KBOS) | Teterboro Airport (KTEB) | 2026-05-06 23:29 UTC | 2026-05-07 01:05 UTC | 1h 35m |
| EDG96 | EDG | Van Nuys Airport (KVNY) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-07 00:09 UTC | 2026-05-07 00:55 UTC | 46m |
| N579WA |  | Lompoc Airport (KLPC) | Sacramento Executive Airport (KSAC) | 2026-05-06 23:43 UTC | 2026-05-07 00:46 UTC | 1h 3m |
| N3035F |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-06 23:28 UTC | 2026-05-07 00:39 UTC | 1h 10m |
| URSA22 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-07 00:16 UTC | 2026-05-07 00:38 UTC | 21m |
| BRG605 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-05-07 00:10 UTC | 2026-05-07 00:37 UTC | 27m |
| N2881 |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-05-06 23:58 UTC | 2026-05-07 00:33 UTC | 34m |
| N507AF |  | Addison Airport (KADS) | Jones Field (KF00) | 2026-05-06 23:33 UTC | 2026-05-07 00:32 UTC | 59m |
| AM333 |  | Milawa Vineyard Airport (YILA) | Mount Hotham Airport (YHOT) | 2026-05-07 00:15 UTC | 2026-05-07 00:29 UTC | 13m |
| N342T |  | City Of Colorado Springs Municipal Airport (KCOS) | Spring Canyon Airport (CO94) | 2026-05-06 23:47 UTC | 2026-05-07 00:28 UTC | 41m |
| N2474Y |  | Logan-Cache Airport (KLGU) | Shepard Strip (07ID) | 2026-05-06 23:46 UTC | 2026-05-07 00:27 UTC | 41m |
| N908PA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-05-07 00:00 UTC | 2026-05-07 00:26 UTC | 25m |
| N272CB |  | Long Beach (Daugherty Field) Airport (KLGB) | Santa Barbara Municipal Airport (KSBA) | 2026-05-06 23:31 UTC | 2026-05-07 00:25 UTC | 54m |
| MTN7475 | MTN | Raleigh County Memorial Airport (KBKW) | Crazy Horse Airport (12WV) | 2026-05-07 00:03 UTC | 2026-05-07 00:25 UTC | 22m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bombala Airport (YBOM) | 2026-05-06 23:38 UTC | 2026-05-07 00:21 UTC | 43m |
| BELLS90 | Brussels Airlines | Buckley Space Force Base Airport (KBKF) | Limon Municipal Airport (KLIC) | 2026-05-06 23:41 UTC | 2026-05-07 00:21 UTC | 39m |
| JL2323 |  | Osaka International Airport (RJOO) | Hiroshima Airport (RJOA) | 2026-05-07 00:06 UTC | 2026-05-07 00:18 UTC | 11m |
| SKW466U | SkyWest Airlines | Denver International Airport (KDEN) | Laramie Regional Airport (KLAR) | 2026-05-06 23:59 UTC | 2026-05-07 00:17 UTC | 18m |
| PUH | PUH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-06 23:39 UTC | 2026-05-07 00:16 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
