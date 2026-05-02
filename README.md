# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_03:20:40_UTC-green)

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

**Latest saved flight:** 2026-05-02 03:20:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 03:20:40 UTC

- **63,440** saved flights
- **24,261** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,440** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **774,533.7 tonnes** estimated CO2 emissions
- **44,900,502 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2656 |
| 2 | SkyWest Airlines | 2364 |
| 3 | IndiGo | 1442 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 989 |
| 6 | Southwest Airlines | 902 |
| 7 | Lufthansa | 811 |
| 8 | ENY | 784 |
| 9 | Vueling | 616 |
| 10 | AXM | 612 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 554 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 528 |
| 15 | AZU | 517 |
| 16 | QLK | 500 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 438 |
| 20 | easyJet | 411 |
| 21 | AEE | 409 |
| 22 | EJU | 403 |
| 23 | VIV | 399 |
| 24 | Cathay Pacific | 384 |
| 25 | Japan Airlines | 369 |
| 26 | Air France | 364 |
| 27 | AXB | 351 |
| 28 | AIQ | 323 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50490 |
| 2 | 🇪🇸 ES | 4563 |
| 3 | 🇮🇳 IN | 4555 |
| 4 | 🇦🇺 AU | 4315 |
| 5 | 🇧🇷 BR | 3593 |
| 6 | 🇩🇪 DE | 3510 |
| 7 | 🇯🇵 JP | 3439 |
| 8 | 🇮🇹 IT | 3432 |
| 9 | 🇨🇦 CA | 3132 |
| 10 | 🇬🇧 GB | 2690 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2480 |
| 13 | 🇲🇽 MX | 2017 |
| 14 | 🇬🇷 GR | 1874 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1503 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1199 |
| 20 | 🇹🇭 TH | 1142 |
| 21 | 🇹🇷 TR | 1112 |
| 22 | 🇵🇭 PH | 1069 |
| 23 | 🇵🇱 PL | 1022 |
| 24 | 🇰🇷 KR | 1019 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 774 |
| 27 | 🇲🇴 MO | 709 |
| 28 | 🇲🇪 ME | 685 |
| 29 | 🇳🇱 NL | 661 |
| 30 | 🇮🇩 ID | 534 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1161 |
| 3 | Denver International Airport |  | US | 1045 |
| 4 | Indira Gandhi International Airport |  | IN | 957 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 914 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 811 |
| 9 | Harry Reid International Airport |  | US | 806 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 709 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 625 |
| 14 | Chicago O'Hare International Airport |  | US | 606 |
| 15 | Kuala Lumpur International Airport |  | MY | 597 |
| 16 | Madrid Barajas International Airport |  | ES | 595 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 561 |
| 19 | Bengaluru International Airport |  | IN | 549 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 501 |
| 24 | Charles de Gaulle International Airport |  | FR | 489 |
| 25 | Tenerife Norte Airport |  | ES | 488 |
| 26 | Ninoy Aquino International Airport |  | PH | 486 |
| 27 | Daniel K Inouye International Airport |  | US | 470 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 459 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 32 | Barcelona International Airport |  | ES | 425 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 414 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 37 | Reno/Tahoe International Airport |  | US | 394 |
| 38 | Don Mueang International Airport |  | TH | 394 |
| 39 | Amsterdam Airport Schiphol |  | NL | 392 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 257 | 1h 7m | 706 km | 3,129.0 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 214 | 21m | 244 km | 901.1 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 196 | 24m | 225 km | 760.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 186 | 1h 27m | 910 km | 2,918.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 180 | 28m | 304 km | 943.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 148 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 116 | 44m | 452 km | 904.1 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 85 | 14m | 154 km | 225.2 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 81 | 1h 43m | 1,423 km | 1,987.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N616F |  | Livermore Municipal Airport (KLVK) | San Carlos Airport (KSQL) | 2026-05-02 01:56 UTC | 2026-05-02 03:20 UTC | 1h 24m |
| N239DC |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-02 01:54 UTC | 2026-05-02 03:14 UTC | 1h 20m |
| ETD42B | Etihad Airways | London Heathrow Airport (EGLL) | Al Bateen Executive Airport (OMAD) | 2026-05-01 20:58 UTC | 2026-05-02 03:05 UTC | 6h 7m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-02 02:22 UTC | 2026-05-02 03:05 UTC | 42m |
| N994SD |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-05-02 01:05 UTC | 2026-05-02 03:02 UTC | 1h 57m |
| MAS627 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Hang Nadim Airport (WIDD) | 2026-05-02 02:19 UTC | 2026-05-02 02:59 UTC | 40m |
| THA433 | Thai Airways | Suvarnabhumi Airport (VTBS) | Changi Air Base (WSAC) | 2026-05-02 01:15 UTC | 2026-05-02 02:59 UTC | 1h 44m |
| HLC282 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-05-02 02:57 UTC | 2026-05-02 02:57 UTC | 0m |
| ZKRDY | ZKR | Rangiora Airfield (NZRT) | Rangiora Airfield (NZRT) | 2026-05-02 01:30 UTC | 2026-05-02 02:55 UTC | 1h 25m |
| SFY201 | SFY | Vero Beach Regional Airport (KVRB) | Broocke Air Patch Airport (FL95) | 2026-05-02 02:25 UTC | 2026-05-02 02:54 UTC | 29m |
| QTR8M | Qatar Airways | Melbourne International Airport (YMML) | Arzanah Airport (OMAR) | 2026-05-01 13:13 UTC | 2026-05-02 02:52 UTC | 13h 39m |
| ETD5FA | Etihad Airways | Dublin Airport (EIDW) | Al Bateen Executive Airport (OMAD) | 2026-05-01 20:11 UTC | 2026-05-02 02:46 UTC | 6h 34m |
| N734VE |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-02 01:42 UTC | 2026-05-02 02:44 UTC | 1h 2m |
| ETD104A | Etihad Airways | Madrid Barajas International Airport (LEMD) | Al Bateen Executive Airport (OMAD) | 2026-05-01 20:46 UTC | 2026-05-02 02:43 UTC | 5h 57m |
| NOK100 | NOK | Don Mueang International Airport (VTBD) | Mong Hsat Airport (VYMS) | 2026-05-02 01:48 UTC | 2026-05-02 02:37 UTC | 48m |
| AWA431 | AWA | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-05-02 02:14 UTC | 2026-05-02 02:28 UTC | 13m |
| TRP6 | TRP | Roseland Airport (32MD) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-05-02 02:10 UTC | 2026-05-02 02:26 UTC | 15m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-05-02 01:56 UTC | 2026-05-02 02:23 UTC | 27m |
| IGO697L | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-05-02 02:00 UTC | 2026-05-02 02:20 UTC | 19m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-05-02 02:01 UTC | 2026-05-02 02:20 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
