# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_23:46:36_UTC-green)

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

**Latest saved flight:** 2026-05-01 23:46:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 23:46:36 UTC

- **63,345** saved flights
- **24,240** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,345** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **773,278.7 tonnes** estimated CO2 emissions
- **44,827,749 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2656 |
| 2 | SkyWest Airlines | 2364 |
| 3 | IndiGo | 1435 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 989 |
| 6 | Southwest Airlines | 899 |
| 7 | Lufthansa | 811 |
| 8 | ENY | 784 |
| 9 | Vueling | 616 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 527 |
| 15 | AZU | 517 |
| 16 | QLK | 498 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 454 |
| 19 | Alaska Airlines | 437 |
| 20 | easyJet | 411 |
| 21 | AEE | 409 |
| 22 | EJU | 403 |
| 23 | VIV | 398 |
| 24 | Cathay Pacific | 384 |
| 25 | Japan Airlines | 366 |
| 26 | Air France | 364 |
| 27 | AXB | 348 |
| 28 | AIQ | 320 |
| 29 | CXK | 319 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50443 |
| 2 | 🇪🇸 ES | 4562 |
| 3 | 🇮🇳 IN | 4530 |
| 4 | 🇦🇺 AU | 4300 |
| 5 | 🇧🇷 BR | 3593 |
| 6 | 🇩🇪 DE | 3510 |
| 7 | 🇮🇹 IT | 3432 |
| 8 | 🇯🇵 JP | 3416 |
| 9 | 🇨🇦 CA | 3130 |
| 10 | 🇬🇧 GB | 2689 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2480 |
| 13 | 🇲🇽 MX | 2013 |
| 14 | 🇬🇷 GR | 1874 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1491 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1189 |
| 20 | 🇹🇭 TH | 1128 |
| 21 | 🇹🇷 TR | 1112 |
| 22 | 🇵🇭 PH | 1067 |
| 23 | 🇵🇱 PL | 1022 |
| 24 | 🇰🇷 KR | 1012 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 774 |
| 27 | 🇲🇴 MO | 709 |
| 28 | 🇲🇪 ME | 685 |
| 29 | 🇳🇱 NL | 661 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1403 |
| 2 | Tokyo International Airport |  | JP | 1154 |
| 3 | Denver International Airport |  | US | 1045 |
| 4 | Indira Gandhi International Airport |  | IN | 953 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 914 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 811 |
| 9 | Harry Reid International Airport |  | US | 805 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 709 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 625 |
| 14 | Chicago O'Hare International Airport |  | US | 606 |
| 15 | Madrid Barajas International Airport |  | ES | 594 |
| 16 | Kuala Lumpur International Airport |  | MY | 591 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 559 |
| 19 | Bengaluru International Airport |  | IN | 545 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 501 |
| 24 | Charles de Gaulle International Airport |  | FR | 489 |
| 25 | Tenerife Norte Airport |  | ES | 488 |
| 26 | Ninoy Aquino International Airport |  | PH | 485 |
| 27 | Daniel K Inouye International Airport |  | US | 470 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 456 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 32 | Barcelona International Airport |  | ES | 425 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 414 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 37 | Reno/Tahoe International Airport |  | US | 394 |
| 38 | Amsterdam Airport Schiphol |  | NL | 392 |
| 39 | Don Mueang International Airport |  | TH | 388 |
| 40 | Calgary International Airport |  | CA | 377 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 256 | 1h 7m | 706 km | 3,116.8 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 214 | 21m | 244 km | 901.1 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 196 | 24m | 225 km | 760.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 81 | 1h 43m | 1,423 km | 1,987.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CLX7625 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-01 10:07 UTC | 2026-05-01 23:46 UTC | 13h 39m |
| NWX628 | NWX | Lebanon Municipal Airport (KM54) | Soggy Bottom Airport (2TN8) | 2026-05-01 23:13 UTC | 2026-05-01 23:42 UTC | 28m |
| N739GY |  | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-05-01 23:06 UTC | 2026-05-01 23:40 UTC | 33m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-01 23:08 UTC | 2026-05-01 23:39 UTC | 30m |
| N2872Q |  | Piedmont Triad International Airport (KGSO) | Danville Regional Airport (KDAN) | 2026-05-01 23:14 UTC | 2026-05-01 23:37 UTC | 22m |
| N74SW |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-05-01 22:14 UTC | 2026-05-01 23:32 UTC | 1h 18m |
| ASA408 | Alaska Airlines | Cecil Ranch Airport (37CN) | Auburn Municipal Airport (KS50) | 2026-05-01 21:47 UTC | 2026-05-01 23:28 UTC | 1h 41m |
| UAL568 | United Airlines | Toronto Pearson International Airport (CYYZ) | Denver International Airport (KDEN) | 2026-05-01 20:34 UTC | 2026-05-01 23:27 UTC | 2h 53m |
| LXJ339 | LXJ | Dallas Love Field (KDAL) | Austin-Bergstrom International Airport (KAUS) | 2026-05-01 22:40 UTC | 2026-05-01 23:22 UTC | 41m |
| N65411 |  | San Luis Obispo County Regional Airport (KSBP) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-01 22:38 UTC | 2026-05-01 23:17 UTC | 38m |
| N97FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-05-01 22:35 UTC | 2026-05-01 23:17 UTC | 41m |
| N900KA |  | 80WA (80WA) | Boeing Field/King County International Airport (KBFI) | 2026-05-01 22:57 UTC | 2026-05-01 23:14 UTC | 17m |
| N1464C |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-05-01 22:09 UTC | 2026-05-01 23:13 UTC | 1h 4m |
| EJM832 | EJM | Teterboro Airport (KTEB) | Lakefront Airport (KNEW) | 2026-05-01 20:08 UTC | 2026-05-01 23:12 UTC | 3h 4m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-01 23:03 UTC | 2026-05-01 23:11 UTC | 8m |
| N2095J |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 22:39 UTC | 2026-05-01 23:11 UTC | 31m |
| N1MM |  | Charles M Schulz/Sonoma County Airport (KSTS) | Scottsdale Airport (KSDL) | 2026-05-01 21:28 UTC | 2026-05-01 23:10 UTC | 1h 42m |
| SKW5848 | SkyWest Airlines | Joe Foss Field (KFSD) | Denver International Airport (KDEN) | 2026-05-01 22:03 UTC | 2026-05-01 23:10 UTC | 1h 7m |
| N3939X |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-05-01 22:31 UTC | 2026-05-01 23:09 UTC | 38m |
| EJA868 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Renton Municipal Airport (KRNT) | 2026-05-01 21:32 UTC | 2026-05-01 23:08 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
