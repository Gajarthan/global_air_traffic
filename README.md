# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_20:59:07_UTC-green)

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

**Latest saved flight:** 2026-05-03 20:59:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 20:59:07 UTC

- **66,759** saved flights
- **25,209** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **66,759** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **819,396.8 tonnes** estimated CO2 emissions
- **47,501,265 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2856 |
| 2 | SkyWest Airlines | 2469 |
| 3 | IndiGo | 1546 |
| 4 | EJA | 1192 |
| 5 | American Airlines | 1036 |
| 6 | Southwest Airlines | 941 |
| 7 | Lufthansa | 857 |
| 8 | ENY | 821 |
| 9 | Vueling | 660 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 618 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 559 |
| 14 | WIF | 558 |
| 15 | AZU | 538 |
| 16 | Swiss International | 514 |
| 17 | QLK | 513 |
| 18 | LXJ | 486 |
| 19 | Alaska Airlines | 451 |
| 20 | easyJet | 444 |
| 21 | AEE | 435 |
| 22 | EJU | 432 |
| 23 | VIV | 416 |
| 24 | Cathay Pacific | 398 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 375 |
| 28 | CXK | 340 |
| 29 | AIQ | 339 |
| 30 | MXY | 326 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 52819 |
| 2 | 🇪🇸 ES | 4906 |
| 3 | 🇮🇳 IN | 4855 |
| 4 | 🇦🇺 AU | 4411 |
| 5 | 🇩🇪 DE | 3741 |
| 6 | 🇧🇷 BR | 3739 |
| 7 | 🇮🇹 IT | 3652 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3263 |
| 10 | 🇬🇧 GB | 2892 |
| 11 | 🇨🇴 CO | 2651 |
| 12 | 🇫🇷 FR | 2650 |
| 13 | 🇲🇽 MX | 2120 |
| 14 | 🇬🇷 GR | 1997 |
| 15 | 🇨🇭 CH | 1869 |
| 16 | 🇳🇴 NO | 1814 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1228 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1204 |
| 22 | 🇵🇭 PH | 1108 |
| 23 | 🇵🇱 PL | 1099 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1071 |
| 26 | 🇲🇦 MA | 819 |
| 27 | 🇲🇴 MO | 746 |
| 28 | 🇲🇪 ME | 723 |
| 29 | 🇳🇱 NL | 708 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1469 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1102 |
| 4 | Indira Gandhi International Airport |  | IN | 1012 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 972 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 863 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 829 |
| 10 | La Aurora Airport |  | GT | 795 |
| 11 | Zurich Airport |  | CH | 793 |
| 12 | Macau International Airport |  | MO | 746 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 657 |
| 14 | Chicago O'Hare International Airport |  | US | 640 |
| 15 | Madrid Barajas International Airport |  | ES | 639 |
| 16 | Kuala Lumpur International Airport |  | MY | 639 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 599 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 580 |
| 20 | Malpensa International Airport |  | IT | 576 |
| 21 | Congonhas Airport |  | BR | 538 |
| 22 | Tenerife Norte Airport |  | ES | 533 |
| 23 | Salt Lake City International Airport |  | US | 531 |
| 24 | Charlotte/Douglas International Airport |  | US | 526 |
| 25 | Charles de Gaulle International Airport |  | FR | 523 |
| 26 | Capua Airport |  | IT | 505 |
| 27 | Ninoy Aquino International Airport |  | PH | 504 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 486 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 471 |
| 31 | Barcelona International Airport |  | ES | 459 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 448 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 444 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Amsterdam Airport Schiphol |  | NL | 416 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 415 |
| 39 | Reno/Tahoe International Airport |  | US | 404 |
| 40 | Calgary International Airport |  | CA | 388 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 226 | 21m | 244 km | 951.6 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 165 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 125 | 21m | 99 km | 214.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 109 | 27m | 152 km | 284.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 96 | 1h 41m | 1,156 km | 1,915.2 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JY91 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-03 19:43 UTC | 2026-05-03 20:59 UTC | 1h 15m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-03 06:35 UTC | 2026-05-03 20:49 UTC | 14h 13m |
| N738KA |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-05-03 20:19 UTC | 2026-05-03 20:45 UTC | 26m |
| N224VS |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-05-03 19:46 UTC | 2026-05-03 20:44 UTC | 58m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 20:30 UTC | 2026-05-03 20:42 UTC | 11m |
| N43451 |  | Denton Enterprise Airport (KDTO) | Vance Field (TE76) | 2026-05-03 20:07 UTC | 2026-05-03 20:39 UTC | 31m |
| N77MV |  | 3WA1 (3WA1) | Boeing Field/King County International Airport (KBFI) | 2026-05-03 20:08 UTC | 2026-05-03 20:37 UTC | 29m |
| THY4TX | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Queen Alia International Airport (OJAI) | 2026-05-03 19:33 UTC | 2026-05-03 20:37 UTC | 1h 4m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-05-03 19:30 UTC | 2026-05-03 20:34 UTC | 1h 3m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-05-03 19:50 UTC | 2026-05-03 20:27 UTC | 37m |
| N695GD |  | Savannah/Hilton Head International Airport (KSAV) | Eldon Model Airpark (KH79) | 2026-05-03 18:51 UTC | 2026-05-03 20:27 UTC | 1h 35m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-03 20:12 UTC | 2026-05-03 20:27 UTC | 14m |
| TMN121 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-05-03 11:06 UTC | 2026-05-03 20:25 UTC | 9h 18m |
| N811CE |  | Kissimmee Gateway Airport (KISM) | Virginia Highlands Airport (KVJI) | 2026-05-03 19:09 UTC | 2026-05-03 20:24 UTC | 1h 15m |
| N82TX |  | Rocky Mountain Metro Airport (KBJC) | Austin-Bergstrom International Airport (KAUS) | 2026-05-03 18:42 UTC | 2026-05-03 20:22 UTC | 1h 40m |
| EJA877 | EJA | Teterboro Airport (KTEB) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-03 14:55 UTC | 2026-05-03 20:22 UTC | 5h 27m |
| ETD947 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-05-03 13:55 UTC | 2026-05-03 20:19 UTC | 6h 24m |
| N25XM |  | Santa Ynez/Kunkle Field (KIZA) | Reno/Tahoe International Airport (KRNO) | 2026-05-03 19:08 UTC | 2026-05-03 20:19 UTC | 1h 10m |
| N619FB |  | North Las Vegas Airport (KVGT) | Santa Monica Municipal Airport (KSMO) | 2026-05-03 16:31 UTC | 2026-05-03 20:17 UTC | 3h 46m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-03 19:55 UTC | 2026-05-03 20:16 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
