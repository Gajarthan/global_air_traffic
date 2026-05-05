# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_21:06:32_UTC-green)

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

**Latest saved flight:** 2026-05-05 21:06:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 21:06:32 UTC

- **69,744** saved flights
- **26,056** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,744** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **857,883.9 tonnes** estimated CO2 emissions
- **49,732,399 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3003 |
| 2 | SkyWest Airlines | 2601 |
| 3 | IndiGo | 1599 |
| 4 | EJA | 1266 |
| 5 | American Airlines | 1092 |
| 6 | Southwest Airlines | 1001 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 863 |
| 9 | Vueling | 689 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 649 |
| 12 | WIF | 596 |
| 13 | All Nippon Airways | 585 |
| 14 | Delta Air Lines | 585 |
| 15 | AZU | 566 |
| 16 | Swiss International | 539 |
| 17 | QLK | 534 |
| 18 | LXJ | 504 |
| 19 | Alaska Airlines | 480 |
| 20 | easyJet | 468 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 434 |
| 24 | Cathay Pacific | 419 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 340 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55378 |
| 2 | 🇪🇸 ES | 5099 |
| 3 | 🇮🇳 IN | 5027 |
| 4 | 🇦🇺 AU | 4599 |
| 5 | 🇧🇷 BR | 3923 |
| 6 | 🇩🇪 DE | 3898 |
| 7 | 🇮🇹 IT | 3829 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3444 |
| 10 | 🇬🇧 GB | 3034 |
| 11 | 🇫🇷 FR | 2767 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2210 |
| 14 | 🇬🇷 GR | 2085 |
| 15 | 🇨🇭 CH | 1922 |
| 16 | 🇳🇴 NO | 1913 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1288 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1258 |
| 22 | 🇵🇭 PH | 1158 |
| 23 | 🇵🇱 PL | 1150 |
| 24 | 🇬🇹 GT | 1123 |
| 25 | 🇰🇷 KR | 1110 |
| 26 | 🇲🇦 MA | 841 |
| 27 | 🇲🇴 MO | 790 |
| 28 | 🇲🇪 ME | 754 |
| 29 | 🇳🇱 NL | 727 |
| 30 | 🇮🇩 ID | 588 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1551 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1151 |
| 4 | Indira Gandhi International Airport |  | IN | 1054 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1020 |
| 6 | Frankfurt am Main International Airport |  | DE | 894 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 867 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 835 |
| 11 | Zurich Airport |  | CH | 826 |
| 12 | Macau International Airport |  | MO | 790 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 697 |
| 14 | Chicago O'Hare International Airport |  | US | 668 |
| 15 | Kuala Lumpur International Airport |  | MY | 668 |
| 16 | Madrid Barajas International Airport |  | ES | 665 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 622 |
| 18 | Malpensa International Airport |  | IT | 609 |
| 19 | Bengaluru International Airport |  | IN | 605 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Salt Lake City International Airport |  | US | 563 |
| 22 | Congonhas Airport |  | BR | 558 |
| 23 | Charlotte/Douglas International Airport |  | US | 549 |
| 24 | Charles de Gaulle International Airport |  | FR | 549 |
| 25 | Tenerife Norte Airport |  | ES | 544 |
| 26 | Capua Airport |  | IT | 543 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 510 |
| 29 | Daniel K Inouye International Airport |  | US | 508 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 492 |
| 31 | Barcelona International Airport |  | ES | 484 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 473 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 438 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 436 |
| 38 | Amsterdam Airport Schiphol |  | NL | 429 |
| 39 | Reno/Tahoe International Airport |  | US | 414 |
| 40 | Calgary International Airport |  | CA | 413 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 239 | 21m | 244 km | 1,006.4 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 173 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 88 | 1h 19m | 961 km | 1,458.6 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RN185 |  | Mobile Regional Airport (KMOB) | Skywest Airpark (62AL) | 2026-05-05 20:50 UTC | 2026-05-05 21:06 UTC | 15m |
| N377MM |  | Brown Field (46NC) | Charlotte/Monroe Executive Airport (KEQY) | 2026-05-05 20:34 UTC | 2026-05-05 21:05 UTC | 30m |
| N129RR |  | Phoenix Deer Valley Airport (KDVT) | Glendale Regional Airport (KGEU) | 2026-05-05 20:52 UTC | 2026-05-05 21:03 UTC | 11m |
| N183TS |  | Nashville International Airport (KBNA) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-05 20:20 UTC | 2026-05-05 21:02 UTC | 41m |
| BOE339 | BOE | Boeing Field/King County International Airport (KBFI) | Hoverhawk Ranch Airport (WN17) | 2026-05-05 20:35 UTC | 2026-05-05 20:50 UTC | 14m |
| EJA123 | EJA | Newark Liberty International Airport (KEWR) | Washington Dulles International Airport (KIAD) | 2026-05-05 20:00 UTC | 2026-05-05 20:42 UTC | 41m |
| N90DT |  | Aero Country Airport (KT31) | Baylie Airport (66XS) | 2026-05-05 20:31 UTC | 2026-05-05 20:38 UTC | 7m |
| N54384 |  | Santa Barbara Municipal Airport (KSBA) | Santa Barbara Municipal Airport (KSBA) | 2026-05-05 20:00 UTC | 2026-05-05 20:36 UTC | 35m |
| EJA488 | EJA | Fort Worth Meacham International Airport (KFTW) | Austin-Bergstrom International Airport (KAUS) | 2026-05-05 20:02 UTC | 2026-05-05 20:35 UTC | 33m |
| BOX720 | BOX | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-05 16:27 UTC | 2026-05-05 20:34 UTC | 4h 7m |
| N554CN |  | Wiley Post Airport (KPWA) | Mc Alester Regional Airport (KMLC) | 2026-05-05 20:11 UTC | 2026-05-05 20:31 UTC | 20m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 20:19 UTC | 2026-05-05 20:31 UTC | 12m |
| DREAD81 | DRE | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Velox Airport (AL84) | 2026-05-05 19:56 UTC | 2026-05-05 20:31 UTC | 35m |
| MEDIC33 | MED | Porto Santo Airport (LPPS) | Lisbon Portela Airport (LPPT) | 2026-05-05 19:00 UTC | 2026-05-05 20:30 UTC | 1h 29m |
| DAGGER6 | DAG | Shenandoah Valley Farms Airport (0MS9) | Wade Field (MS76) | 2026-05-05 20:17 UTC | 2026-05-05 20:30 UTC | 12m |
| WAH | WAH | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-05-05 20:19 UTC | 2026-05-05 20:29 UTC | 10m |
| EXCEL06 | EXC | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-05-05 20:12 UTC | 2026-05-05 20:27 UTC | 15m |
| JUMP08 | JUM | Bertani Ranch Airport (23TS) | Terrell County Airport (K6R6) | 2026-05-05 20:16 UTC | 2026-05-05 20:27 UTC | 11m |
| TCAHE | TCA | Antalya International Airport (LTAI) | Sabiha Gokcen International Airport (LTFJ) | 2026-05-05 19:30 UTC | 2026-05-05 20:22 UTC | 51m |
| XBPDS | XBP | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-05 19:37 UTC | 2026-05-05 20:22 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
