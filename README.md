# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_13:58:31_UTC-green)

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

**Latest saved flight:** 2026-05-01 13:58:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 13:58:31 UTC

- **62,115** saved flights
- **23,839** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **62,115** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **758,516.3 tonnes** estimated CO2 emissions
- **43,971,957 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2608 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1421 |
| 4 | EJA | 1118 |
| 5 | American Airlines | 966 |
| 6 | Southwest Airlines | 879 |
| 7 | Lufthansa | 793 |
| 8 | ENY | 765 |
| 9 | Vueling | 611 |
| 10 | AXM | 607 |
| 11 | LATAM Airlines | 587 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 525 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 506 |
| 16 | QLK | 498 |
| 17 | Swiss International | 480 |
| 18 | LXJ | 441 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 406 |
| 21 | easyJet | 404 |
| 22 | EJU | 398 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 360 |
| 27 | AXB | 343 |
| 28 | AIQ | 319 |
| 29 | CXK | 306 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49062 |
| 2 | 🇪🇸 ES | 4490 |
| 3 | 🇮🇳 IN | 4486 |
| 4 | 🇦🇺 AU | 4285 |
| 5 | 🇧🇷 BR | 3515 |
| 6 | 🇩🇪 DE | 3448 |
| 7 | 🇯🇵 JP | 3408 |
| 8 | 🇮🇹 IT | 3373 |
| 9 | 🇨🇦 CA | 3061 |
| 10 | 🇬🇧 GB | 2647 |
| 11 | 🇨🇴 CO | 2633 |
| 12 | 🇫🇷 FR | 2445 |
| 13 | 🇲🇽 MX | 1949 |
| 14 | 🇬🇷 GR | 1846 |
| 15 | 🇨🇭 CH | 1742 |
| 16 | 🇳🇴 NO | 1718 |
| 17 | 🇲🇾 MY | 1485 |
| 18 | 🇿🇦 ZA | 1267 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1127 |
| 21 | 🇹🇷 TR | 1100 |
| 22 | 🇵🇭 PH | 1062 |
| 23 | 🇰🇷 KR | 1008 |
| 24 | 🇵🇱 PL | 997 |
| 25 | 🇬🇹 GT | 927 |
| 26 | 🇲🇦 MA | 764 |
| 27 | 🇲🇴 MO | 700 |
| 28 | 🇲🇪 ME | 677 |
| 29 | 🇳🇱 NL | 647 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1370 |
| 2 | Tokyo International Airport |  | JP | 1151 |
| 3 | Denver International Airport |  | US | 1026 |
| 4 | Indira Gandhi International Airport |  | IN | 944 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 905 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 828 |
| 8 | Frankfurt am Main International Airport |  | DE | 793 |
| 9 | Harry Reid International Airport |  | US | 792 |
| 10 | Zurich Airport |  | CH | 739 |
| 11 | Macau International Airport |  | MO | 700 |
| 12 | La Aurora Airport |  | GT | 695 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Kuala Lumpur International Airport |  | MY | 588 |
| 15 | Chicago O'Hare International Airport |  | US | 584 |
| 16 | Madrid Barajas International Airport |  | ES | 579 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 565 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 538 |
| 20 | Malpensa International Airport |  | IT | 537 |
| 21 | Congonhas Airport |  | BR | 505 |
| 22 | Charlotte/Douglas International Airport |  | US | 493 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Tenerife Norte Airport |  | ES | 484 |
| 25 | Ninoy Aquino International Airport |  | PH | 482 |
| 26 | Charles de Gaulle International Airport |  | FR | 481 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 461 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 450 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 447 |
| 31 | Barcelona International Airport |  | ES | 417 |
| 32 | Vitoria/Foronda Airport |  | ES | 414 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 410 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 405 |
| 35 | O. R. Tambo International Airport |  | ZA | 399 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 391 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 387 |
| 39 | Amsterdam Airport Schiphol |  | NL | 381 |
| 40 | Calgary International Airport |  | CA | 367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 340 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 208 | 21m | 244 km | 875.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 155 | 20m | 165 km | 440.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 149 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 139 | 26m | 275 km | 658.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 101 | 20m | 250 km | 436.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 94 | 20m | 147 km | 237.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 93 | 28m | 152 km | 243.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N714XB |  | Addington Field (4TX8) | Addington Field (4TX8) | 2026-05-01 13:36 UTC | 2026-05-01 13:58 UTC | 21m |
| N994DS |  | Delaware Airpark (K33N) | Lancaster Airport (KLNS) | 2026-05-01 12:56 UTC | 2026-05-01 13:52 UTC | 56m |
| CPA392 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-01 06:32 UTC | 2026-05-01 13:46 UTC | 7h 13m |
| QTR8428 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-01 06:39 UTC | 2026-05-01 13:43 UTC | 7h 3m |
| OKFUI17 | OKF | Mlada Boleslav Airport (LKMB) | Mlada Boleslav Airport (LKMB) | 2026-05-01 13:16 UTC | 2026-05-01 13:42 UTC | 25m |
| N724GT |  | Philadelphia International Airport (KPHL) | Orlando Executive Airport (KORL) | 2026-05-01 11:27 UTC | 2026-05-01 13:36 UTC | 2h 9m |
| OECHB | OEC | Udine / Campoformido Air Base (LIPD) | Salgareda Carrer Airport (LIDW) | 2026-05-01 13:04 UTC | 2026-05-01 13:34 UTC | 29m |
| EJA942 | EJA | Williamsport Airpark (SC86) | Cottonwood Farm Airport (87VA) | 2026-05-01 12:53 UTC | 2026-05-01 13:34 UTC | 40m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-01 13:22 UTC | 2026-05-01 13:34 UTC | 11m |
| R01970 |  | Orange County Airport (KMGJ) | Lancaster Airport (KLNS) | 2026-05-01 12:31 UTC | 2026-05-01 13:33 UTC | 1h 1m |
| HK5309G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-01 13:19 UTC | 2026-05-01 13:32 UTC | 12m |
| N84RJ |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-01 13:04 UTC | 2026-05-01 13:31 UTC | 26m |
| EW585SL |  | Borovaya Airfield (UMMB) | Borovaya Airfield (UMMB) | 2026-05-01 13:26 UTC | 2026-05-01 13:30 UTC | 4m |
| N415HS |  | Tampa International Airport (KTPA) | Orlando Executive Airport (KORL) | 2026-05-01 13:05 UTC | 2026-05-01 13:29 UTC | 24m |
| TWY79 | TWY | Chicago Executive Airport (KPWK) | Lincoln Airport (KLNK) | 2026-05-01 12:13 UTC | 2026-05-01 13:29 UTC | 1h 15m |
| OZN905 | OZN | Oasis Ranger Station-U S Government Airport (9FL7) | Lakeland Linder International Airport (KLAL) | 2026-05-01 12:01 UTC | 2026-05-01 13:29 UTC | 1h 27m |
| IXR830 | IXR | Paris-Le Bourget Airport (LFPB) | Saint-Affrique-Belmont Airport (LFIF) | 2026-05-01 12:18 UTC | 2026-05-01 13:25 UTC | 1h 6m |
| SUI059 | SUI | Buochs Airport (LSZC) | Bad Ragaz Airport (LSZE) | 2026-05-01 13:05 UTC | 2026-05-01 13:23 UTC | 18m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 12:56 UTC | 2026-05-01 13:22 UTC | 25m |
| RTV4T | RTV | Vilar Da Luz Airport (LPVL) | Braga Municipal Aerodrome (LPBR) | 2026-05-01 12:14 UTC | 2026-05-01 13:22 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
