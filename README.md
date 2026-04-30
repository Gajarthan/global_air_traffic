# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_23:52:53_UTC-green)

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

**Latest saved flight:** 2026-04-29 23:52:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 23:52:53 UTC

- **59,910** saved flights
- **23,181** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,910** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **727,774.3 tonnes** estimated CO2 emissions
- **42,189,817 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2548 |
| 2 | SkyWest Airlines | 2252 |
| 3 | IndiGo | 1362 |
| 4 | EJA | 1081 |
| 5 | American Airlines | 940 |
| 6 | Southwest Airlines | 851 |
| 7 | Lufthansa | 759 |
| 8 | ENY | 748 |
| 9 | Vueling | 597 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 573 |
| 12 | All Nippon Airways | 529 |
| 13 | Delta Air Lines | 503 |
| 14 | WIF | 501 |
| 15 | AZU | 492 |
| 16 | Swiss International | 473 |
| 17 | QLK | 467 |
| 18 | LXJ | 427 |
| 19 | Alaska Airlines | 411 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 378 |
| 24 | Cathay Pacific | 354 |
| 25 | Air France | 353 |
| 26 | Japan Airlines | 346 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 300 |
| 30 | CXK | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47544 |
| 2 | 🇪🇸 ES | 4338 |
| 3 | 🇮🇳 IN | 4313 |
| 4 | 🇦🇺 AU | 4076 |
| 5 | 🇧🇷 BR | 3398 |
| 6 | 🇩🇪 DE | 3312 |
| 7 | 🇮🇹 IT | 3289 |
| 8 | 🇯🇵 JP | 3239 |
| 9 | 🇨🇦 CA | 2975 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2524 |
| 12 | 🇫🇷 FR | 2366 |
| 13 | 🇲🇽 MX | 1877 |
| 14 | 🇬🇷 GR | 1786 |
| 15 | 🇨🇭 CH | 1665 |
| 16 | 🇳🇴 NO | 1637 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1116 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1073 |
| 22 | 🇵🇭 PH | 1011 |
| 23 | 🇵🇱 PL | 969 |
| 24 | 🇰🇷 KR | 956 |
| 25 | 🇬🇹 GT | 874 |
| 26 | 🇲🇦 MA | 749 |
| 27 | 🇲🇪 ME | 652 |
| 28 | 🇲🇴 MO | 648 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇧🇸 BS | 508 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1338 |
| 2 | Tokyo International Airport |  | JP | 1099 |
| 3 | Denver International Airport |  | US | 1004 |
| 4 | Indira Gandhi International Airport |  | IN | 908 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 880 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 764 |
| 9 | Frankfurt am Main International Airport |  | DE | 750 |
| 10 | Zurich Airport |  | CH | 721 |
| 11 | La Aurora Airport |  | GT | 659 |
| 12 | Macau International Airport |  | MO | 648 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 596 |
| 14 | Chicago O'Hare International Airport |  | US | 572 |
| 15 | Madrid Barajas International Airport |  | ES | 555 |
| 16 | Kuala Lumpur International Airport |  | MY | 555 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 523 |
| 19 | Malpensa International Airport |  | IT | 520 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 490 |
| 22 | Charlotte/Douglas International Airport |  | US | 478 |
| 23 | Salt Lake City International Airport |  | US | 468 |
| 24 | Charles de Gaulle International Airport |  | FR | 466 |
| 25 | Capua Airport |  | IT | 466 |
| 26 | Ninoy Aquino International Airport |  | PH | 463 |
| 27 | Tenerife Norte Airport |  | ES | 463 |
| 28 | Daniel K Inouye International Airport |  | US | 451 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 431 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 431 |
| 31 | Barcelona International Airport |  | ES | 409 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 33 | Vitoria/Foronda Airport |  | ES | 399 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 394 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 382 |
| 38 | Amsterdam Airport Schiphol |  | NL | 368 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 202 | 21m | 244 km | 850.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 188 | 24m | 225 km | 729.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 169 | 28m | 304 km | 885.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 143 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 142 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 127 | 1h 12m | 770 km | 1,687.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 112 | 44m | 452 km | 872.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 101 | 31m | 369 km | 642.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 90 | 20m | 147 km | 227.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 83 | 1h 43m | 1,156 km | 1,655.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 1m | 695 km | 994.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 78 | 1h 43m | 1,423 km | 1,914.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 76 | 1h 19m | 961 km | 1,259.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-29 22:53 UTC | 2026-04-29 23:52 UTC | 59m |
| NKZ | NKZ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-04-29 23:27 UTC | 2026-04-29 23:45 UTC | 17m |
| N13AN |  | 88OL (88OL) | Mc Alester Regional Airport (KMLC) | 2026-04-29 23:28 UTC | 2026-04-29 23:44 UTC | 16m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-29 23:10 UTC | 2026-04-29 23:39 UTC | 28m |
| N166WC |  | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-04-29 23:10 UTC | 2026-04-29 23:38 UTC | 28m |
| N66HC |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-29 23:21 UTC | 2026-04-29 23:31 UTC | 10m |
| N951DA |  | Barrow County Airport (KWDR) | Kintail Farm Airport (GA00) | 2026-04-29 23:27 UTC | 2026-04-29 23:31 UTC | 3m |
| N419CF |  | Granbury Regional Airport (KGDJ) | Nassau Bay Airport (0TX0) | 2026-04-29 23:25 UTC | 2026-04-29 23:29 UTC | 3m |
| LOOT19 | LOO | Good Life Ranch Airport (17OK) | 84OL (84OL) | 2026-04-29 22:52 UTC | 2026-04-29 23:26 UTC | 33m |
| N950LP |  | Addison Airport (KADS) | Gainesville Municipal Airport (KGLE) | 2026-04-29 22:27 UTC | 2026-04-29 23:25 UTC | 57m |
| TQR | TQR | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-04-29 23:01 UTC | 2026-04-29 23:21 UTC | 20m |
| EJA983 | EJA | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2026-04-29 23:08 UTC | 2026-04-29 23:21 UTC | 12m |
| 6938 |  | Kisarazu Airport (RJTK) | Kisarazu Airport (RJTK) | 2026-04-29 23:00 UTC | 2026-04-29 23:20 UTC | 19m |
| N273TA |  | Phoenix Sky Harbor International Airport (KPHX) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-29 22:58 UTC | 2026-04-29 23:19 UTC | 21m |
| N789FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Apple Valley Airport (KAPV) | 2026-04-29 22:20 UTC | 2026-04-29 23:19 UTC | 59m |
| N555WE |  | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-04-29 22:57 UTC | 2026-04-29 23:18 UTC | 21m |
| C6530 |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-04-29 23:02 UTC | 2026-04-29 23:17 UTC | 15m |
| JOLLY91 | JOL | Reid-Hillview Of Santa Clara County Airport (KRHV) | Moffett Federal Airfield (KNUQ) | 2026-04-29 21:46 UTC | 2026-04-29 23:16 UTC | 1h 29m |
| QUE10 | QUE | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-04-29 22:38 UTC | 2026-04-29 23:15 UTC | 37m |
| JSX203 | JSX | John Wayne/Orange County Airport (KSNA) | Harry Reid International Airport (KLAS) | 2026-04-29 22:27 UTC | 2026-04-29 23:11 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
