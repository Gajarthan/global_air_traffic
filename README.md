# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_14:57:28_UTC-green)

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

**Latest saved flight:** 2026-04-25 14:57:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 14:57:28 UTC

- **53,553** saved flights
- **21,281** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,553** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **642,177.3 tonnes** estimated CO2 emissions
- **37,227,667 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2257 |
| 2 | SkyWest Airlines | 2008 |
| 3 | IndiGo | 1222 |
| 4 | EJA | 947 |
| 5 | American Airlines | 857 |
| 6 | Southwest Airlines | 754 |
| 7 | ENY | 671 |
| 8 | Lufthansa | 628 |
| 9 | Vueling | 540 |
| 10 | AXM | 522 |
| 11 | LATAM Airlines | 516 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 455 |
| 14 | WIF | 446 |
| 15 | Delta Air Lines | 441 |
| 16 | QLK | 416 |
| 17 | Swiss International | 414 |
| 18 | LXJ | 393 |
| 19 | AEE | 359 |
| 20 | Alaska Airlines | 353 |
| 21 | easyJet | 344 |
| 22 | VIV | 340 |
| 23 | EJU | 339 |
| 24 | Japan Airlines | 313 |
| 25 | Air France | 309 |
| 26 | AXB | 285 |
| 27 | Cathay Pacific | 284 |
| 28 | AIQ | 277 |
| 29 | JetBlue | 272 |
| 30 | United Airlines | 272 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42511 |
| 2 | 🇪🇸 ES | 3887 |
| 3 | 🇮🇳 IN | 3850 |
| 4 | 🇦🇺 AU | 3621 |
| 5 | 🇧🇷 BR | 3103 |
| 6 | 🇮🇹 IT | 2889 |
| 7 | 🇯🇵 JP | 2889 |
| 8 | 🇩🇪 DE | 2864 |
| 9 | 🇨🇦 CA | 2660 |
| 10 | 🇨🇴 CO | 2457 |
| 11 | 🇬🇧 GB | 2251 |
| 12 | 🇫🇷 FR | 2093 |
| 13 | 🇲🇽 MX | 1649 |
| 14 | 🇬🇷 GR | 1611 |
| 15 | 🇨🇭 CH | 1522 |
| 16 | 🇳🇴 NO | 1447 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1016 |
| 20 | 🇹🇭 TH | 975 |
| 21 | 🇹🇷 TR | 963 |
| 22 | 🇵🇭 PH | 915 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 864 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 668 |
| 27 | 🇲🇪 ME | 576 |
| 28 | 🇳🇱 NL | 545 |
| 29 | 🇲🇴 MO | 528 |
| 30 | 🇧🇸 BS | 465 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1217 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 882 |
| 4 | El Dorado International Airport |  | CO | 833 |
| 5 | Indira Gandhi International Airport |  | IN | 818 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 796 |
| 7 | Guaymaral Airport |  | CO | 738 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 638 |
| 10 | La Aurora Airport |  | GT | 617 |
| 11 | Frankfurt am Main International Airport |  | DE | 613 |
| 12 | Macau International Airport |  | MO | 528 |
| 13 | Chicago O'Hare International Airport |  | US | 525 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 520 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 506 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 497 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 458 |
| 20 | Malpensa International Airport |  | IT | 451 |
| 21 | Congonhas Airport |  | BR | 447 |
| 22 | Charlotte/Douglas International Airport |  | US | 435 |
| 23 | Tenerife Norte Airport |  | ES | 426 |
| 24 | Ninoy Aquino International Airport |  | PH | 422 |
| 25 | Charles de Gaulle International Airport |  | FR | 405 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 399 |
| 27 | Salt Lake City International Airport |  | US | 396 |
| 28 | Daniel K Inouye International Airport |  | US | 388 |
| 29 | Capua Airport |  | IT | 385 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 384 |
| 31 | Vitoria/Foronda Airport |  | ES | 367 |
| 32 | Barcelona International Airport |  | ES | 361 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 357 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 35 | Reno/Tahoe International Airport |  | US | 356 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 355 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 317 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 299 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 163 | 21m | 244 km | 686.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 124 | 26m | 275 km | 587.6 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 76 | 1h 41m | 1,156 km | 1,516.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 70 | 1h 19m | 961 km | 1,160.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 70 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 70 | 1h 53m | 1,304 km | 1,574.8 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 69 | 24m | 55 km | 65.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5361K |  | Brookhaven Airport (KHWV) | Brookhaven Airport (KHWV) | 2026-04-25 14:31 UTC | 2026-04-25 14:57 UTC | 25m |
| DMDEK | DMD | Anspach/Taunus Airport (EDFA) | Anspach/Taunus Airport (EDFA) | 2026-04-25 14:15 UTC | 2026-04-25 14:54 UTC | 38m |
| N308AD |  | Ballykelly Airport (EGQB) | Ballykelly Airport (EGQB) | 2026-04-25 14:31 UTC | 2026-04-25 14:50 UTC | 18m |
| N745TW |  | KU42 (KU42) | KU42 (KU42) | 2026-04-25 14:34 UTC | 2026-04-25 14:46 UTC | 11m |
| N737YU |  | Lake Elmo Airport (K21D) | Winona Municipal/Max Conrad Field (KONA) | 2026-04-25 13:02 UTC | 2026-04-25 14:45 UTC | 1h 42m |
| BOX500 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-25 04:12 UTC | 2026-04-25 14:41 UTC | 10h 29m |
| N59TW |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-04-25 14:06 UTC | 2026-04-25 14:37 UTC | 31m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-25 07:59 UTC | 2026-04-25 14:37 UTC | 6h 38m |
| N3755G |  | Rogue Valley International/Medford Airport (KMFR) | Prospect State Airport (K64S) | 2026-04-25 14:14 UTC | 2026-04-25 14:37 UTC | 22m |
| BCS538 | BCS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-25 03:57 UTC | 2026-04-25 14:35 UTC | 10h 37m |
| N232DS |  | Westwater Airport (UT42) | Pinyon Airport (CO43) | 2026-04-25 13:59 UTC | 2026-04-25 14:35 UTC | 36m |
| N399MA |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-04-25 14:01 UTC | 2026-04-25 14:34 UTC | 33m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 14:17 UTC | 2026-04-25 14:33 UTC | 15m |
| DHK524 | DHK | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-25 03:56 UTC | 2026-04-25 14:23 UTC | 10h 27m |
| N1723H |  | Double Eagle Ii Airport (KAEG) | Socorro Municipal Airport (KONM) | 2026-04-25 13:58 UTC | 2026-04-25 14:20 UTC | 22m |
| N13658 |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-04-25 13:36 UTC | 2026-04-25 14:18 UTC | 41m |
| HB3384 |  | Gruyeres Airport (LSGT) | Sollieres Sardieres Airport (LFKD) | 2026-04-25 09:54 UTC | 2026-04-25 14:17 UTC | 4h 23m |
| N33AA |  | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2026-04-25 14:00 UTC | 2026-04-25 14:15 UTC | 15m |
| DERFB | DER | Sarre Union Airport (LFQU) | Sarre Union Airport (LFQU) | 2026-04-25 14:02 UTC | 2026-04-25 14:12 UTC | 10m |
| DMAOB | DMA | Altenburg-Nobitz Airport (EDAC) | Altenburg-Nobitz Airport (EDAC) | 2026-04-25 14:11 UTC | 2026-04-25 14:12 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
