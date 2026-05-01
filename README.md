# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_21:38:18_UTC-green)

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

**Latest saved flight:** 2026-05-01 21:38:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 21:38:18 UTC

- **63,191** saved flights
- **24,192** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,191** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **771,092.5 tonnes** estimated CO2 emissions
- **44,701,013 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2656 |
| 2 | SkyWest Airlines | 2352 |
| 3 | IndiGo | 1435 |
| 4 | EJA | 1140 |
| 5 | American Airlines | 983 |
| 6 | Southwest Airlines | 896 |
| 7 | Lufthansa | 811 |
| 8 | ENY | 778 |
| 9 | Vueling | 616 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 591 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 524 |
| 15 | AZU | 517 |
| 16 | QLK | 498 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 452 |
| 19 | Alaska Airlines | 435 |
| 20 | easyJet | 411 |
| 21 | AEE | 409 |
| 22 | EJU | 403 |
| 23 | VIV | 396 |
| 24 | Cathay Pacific | 382 |
| 25 | Japan Airlines | 366 |
| 26 | Air France | 364 |
| 27 | AXB | 348 |
| 28 | AIQ | 320 |
| 29 | CXK | 318 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50236 |
| 2 | 🇪🇸 ES | 4562 |
| 3 | 🇮🇳 IN | 4530 |
| 4 | 🇦🇺 AU | 4289 |
| 5 | 🇧🇷 BR | 3586 |
| 6 | 🇩🇪 DE | 3510 |
| 7 | 🇮🇹 IT | 3432 |
| 8 | 🇯🇵 JP | 3412 |
| 9 | 🇨🇦 CA | 3113 |
| 10 | 🇬🇧 GB | 2689 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2479 |
| 13 | 🇲🇽 MX | 2002 |
| 14 | 🇬🇷 GR | 1874 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1491 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1183 |
| 20 | 🇹🇭 TH | 1128 |
| 21 | 🇹🇷 TR | 1112 |
| 22 | 🇵🇭 PH | 1063 |
| 23 | 🇵🇱 PL | 1022 |
| 24 | 🇰🇷 KR | 1008 |
| 25 | 🇬🇹 GT | 988 |
| 26 | 🇲🇦 MA | 774 |
| 27 | 🇲🇴 MO | 706 |
| 28 | 🇲🇪 ME | 685 |
| 29 | 🇳🇱 NL | 659 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1396 |
| 2 | Tokyo International Airport |  | JP | 1153 |
| 3 | Denver International Airport |  | US | 1041 |
| 4 | Indira Gandhi International Airport |  | IN | 953 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 914 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 811 |
| 9 | Harry Reid International Airport |  | US | 805 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 739 |
| 12 | Macau International Airport |  | MO | 706 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 623 |
| 14 | Chicago O'Hare International Airport |  | US | 599 |
| 15 | Madrid Barajas International Airport |  | ES | 594 |
| 16 | Kuala Lumpur International Airport |  | MY | 591 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 574 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 545 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 518 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 499 |
| 24 | Tenerife Norte Airport |  | ES | 488 |
| 25 | Charles de Gaulle International Airport |  | FR | 488 |
| 26 | Ninoy Aquino International Airport |  | PH | 483 |
| 27 | Daniel K Inouye International Airport |  | US | 468 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 456 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 456 |
| 31 | Barcelona International Airport |  | ES | 425 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 422 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 414 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 395 |
| 37 | Reno/Tahoe International Airport |  | US | 393 |
| 38 | Amsterdam Airport Schiphol |  | NL | 392 |
| 39 | Don Mueang International Airport |  | TH | 388 |
| 40 | Calgary International Airport |  | CA | 373 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 213 | 21m | 244 km | 896.9 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 156 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 102 | 28m | 152 km | 266.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 1m | 695 km | 1,042.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 86 | 1h 53m | 1,304 km | 1,934.8 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 81 | 1h 43m | 1,423 km | 1,987.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-01 17:23 UTC | 2026-05-01 21:38 UTC | 4h 15m |
| NDL765 | NDL | John C. Munro Hamilton International Airport (CYHM) | Montréal / St-Hubert Airport (CYHU) | 2026-05-01 20:22 UTC | 2026-05-01 21:36 UTC | 1h 14m |
| N103UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-05-01 20:40 UTC | 2026-05-01 21:34 UTC | 54m |
| N504PS |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Arlington Municipal Airport (KGKY) | 2026-05-01 20:16 UTC | 2026-05-01 21:32 UTC | 1h 15m |
| N5996J |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-05-01 19:50 UTC | 2026-05-01 21:32 UTC | 1h 41m |
| BOE001 | BOE | Warden Airport (K2S4) | Sheffels Ranch Airport (42WA) | 2026-05-01 19:32 UTC | 2026-05-01 21:32 UTC | 2h 0m |
| DCM6072 | DCM | KFTG (KFTG) | Scottsdale Airport (KSDL) | 2026-05-01 20:02 UTC | 2026-05-01 21:32 UTC | 1h 29m |
| N756UJ |  | Skydive Iowa Airport (09IA) | Skydive Iowa Airport (09IA) | 2026-05-01 21:12 UTC | 2026-05-01 21:31 UTC | 19m |
| N9842G |  | Auburn Municipal Airport (KAUN) | Sacramento Mather Airport (KMHR) | 2026-05-01 20:14 UTC | 2026-05-01 21:31 UTC | 1h 16m |
| CXK217 | CXK | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-05-01 19:51 UTC | 2026-05-01 21:29 UTC | 1h 37m |
| N231MR |  | San Carlos Airport (KSQL) | Dayton Valley Airpark (KA34) | 2026-05-01 20:49 UTC | 2026-05-01 21:29 UTC | 40m |
| N246SF |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-05-01 20:25 UTC | 2026-05-01 21:28 UTC | 1h 3m |
| FHY743 | FHY | Antalya International Airport (LTAI) | Varna Airport (LBWN) | 2026-05-01 20:27 UTC | 2026-05-01 21:26 UTC | 58m |
| HAWK271 | HAW | Kingsville Nas Airport (KNQI) | Van Es Ranch Airport (13TS) | 2026-05-01 21:06 UTC | 2026-05-01 21:24 UTC | 17m |
| N73929 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-01 20:44 UTC | 2026-05-01 21:24 UTC | 39m |
| ANVIL97 | ANV | West Virginia International Yeager Airport (KCRW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-05-01 20:56 UTC | 2026-05-01 21:22 UTC | 26m |
| N3547H |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Sacramento Mather Airport (KMHR) | 2026-05-01 20:17 UTC | 2026-05-01 21:19 UTC | 1h 1m |
| NDU92T | NDU | MN38 (MN38) | Willis Airport (7MN8) | 2026-05-01 21:04 UTC | 2026-05-01 21:19 UTC | 15m |
| EJA279 | EJA | Moffett Federal Airfield (KNUQ) | Santa Barbara Municipal Airport (KSBA) | 2026-05-01 20:28 UTC | 2026-05-01 21:18 UTC | 50m |
| SIL1405 | SIL | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-05-01 20:35 UTC | 2026-05-01 21:18 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
