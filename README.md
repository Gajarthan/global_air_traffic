# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_11:32:26_UTC-green)

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

**Latest saved flight:** 2026-05-02 11:32:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 11:32:26 UTC

- **63,977** saved flights
- **24,383** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,977** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **784,624.3 tonnes** estimated CO2 emissions
- **45,485,466 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2692 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1471 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 992 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 821 |
| 8 | ENY | 784 |
| 9 | Vueling | 630 |
| 10 | AXM | 623 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 565 |
| 13 | WIF | 537 |
| 14 | Delta Air Lines | 531 |
| 15 | AZU | 518 |
| 16 | QLK | 502 |
| 17 | Swiss International | 493 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 420 |
| 21 | AEE | 413 |
| 22 | EJU | 410 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 388 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 371 |
| 27 | AXB | 355 |
| 28 | AIQ | 329 |
| 29 | CXK | 321 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50541 |
| 2 | 🇪🇸 ES | 4655 |
| 3 | 🇮🇳 IN | 4642 |
| 4 | 🇦🇺 AU | 4339 |
| 5 | 🇧🇷 BR | 3596 |
| 6 | 🇩🇪 DE | 3575 |
| 7 | 🇯🇵 JP | 3519 |
| 8 | 🇮🇹 IT | 3476 |
| 9 | 🇨🇦 CA | 3137 |
| 10 | 🇬🇧 GB | 2744 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2525 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1911 |
| 15 | 🇨🇭 CH | 1784 |
| 16 | 🇳🇴 NO | 1754 |
| 17 | 🇲🇾 MY | 1528 |
| 18 | 🇿🇦 ZA | 1308 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1170 |
| 21 | 🇹🇷 TR | 1136 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇰🇷 KR | 1048 |
| 24 | 🇵🇱 PL | 1043 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 782 |
| 27 | 🇲🇴 MO | 725 |
| 28 | 🇲🇪 ME | 691 |
| 29 | 🇳🇱 NL | 669 |
| 30 | 🇮🇩 ID | 541 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1185 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 975 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 930 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 824 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 760 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 725 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Chicago O'Hare International Airport |  | US | 607 |
| 15 | Kuala Lumpur International Airport |  | MY | 605 |
| 16 | Madrid Barajas International Airport |  | ES | 603 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 560 |
| 20 | Malpensa International Airport |  | IT | 549 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Tenerife Norte Airport |  | ES | 506 |
| 23 | Charlotte/Douglas International Airport |  | US | 502 |
| 24 | Salt Lake City International Airport |  | US | 502 |
| 25 | Charles de Gaulle International Airport |  | FR | 498 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 473 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 469 |
| 29 | Capua Airport |  | IT | 468 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 433 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 423 |
| 34 | Vitoria/Foronda Airport |  | ES | 422 |
| 35 | O. R. Tambo International Airport |  | ZA | 413 |
| 36 | Don Mueang International Airport |  | TH | 405 |
| 37 | Amsterdam Airport Schiphol |  | NL | 398 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 217 | 21m | 244 km | 913.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 188 | 1h 27m | 910 km | 2,950.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 187 | 28m | 304 km | 980.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 158 | 20m | 165 km | 449.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 142 | 26m | 275 km | 672.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 141 | 1h 11m | 770 km | 1,873.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 88 | 57m | 493 km | 748.7 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 88 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHX22 | CHX | Grabenstetten Airport (EDSG) | Erbach Airport (EDNE) | 2026-05-02 11:17 UTC | 2026-05-02 11:32 UTC | 14m |
| CXK206 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-02 11:11 UTC | 2026-05-02 11:31 UTC | 19m |
| AAL1912 | American Airlines | VT48 (VT48) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-05-02 10:01 UTC | 2026-05-02 11:23 UTC | 1h 22m |
| BCS642 | BCS | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-01 18:25 UTC | 2026-05-02 11:19 UTC | 16h 54m |
| DFALB | DFA | Saarlouis-Duren Airport (EDRJ) | Saarlouis-Duren Airport (EDRJ) | 2026-05-02 10:23 UTC | 2026-05-02 11:05 UTC | 42m |
| ZSBAS | ZSB | O. R. Tambo International Airport (FAOR) | Rooiberg Airport (FARO) | 2026-05-02 10:29 UTC | 2026-05-02 11:03 UTC | 34m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-05-02 10:10 UTC | 2026-05-02 11:02 UTC | 52m |
| CMD70 | CMD | Mc Clellan Airfield (KMCC) | 23CA (23CA) | 2026-05-02 10:14 UTC | 2026-05-02 11:02 UTC | 47m |
| DEGGO | DEG | Zweibrucken Airport (EDRZ) | Zweibrucken Airport (EDRZ) | 2026-05-02 09:45 UTC | 2026-05-02 10:58 UTC | 1h 12m |
| GAWGB | GAW | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-05-02 10:45 UTC | 2026-05-02 10:53 UTC | 7m |
| SAMU38 | SAM | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-05-02 10:40 UTC | 2026-05-02 10:52 UTC | 12m |
| DHK011 | DHK | East Midlands Airport (EGNX) | Macau International Airport (VMMC) | 2026-05-01 23:00 UTC | 2026-05-02 10:51 UTC | 11h 50m |
| N550AJ |  | Fayette Airport (WV59) | West Virginia International Yeager Airport (KCRW) | 2026-05-02 10:38 UTC | 2026-05-02 10:50 UTC | 11m |
| ZSDVT | ZSD | Microland Flight Park (FABA) | Dunnottar Airport (FADR) | 2026-05-02 10:32 UTC | 2026-05-02 10:49 UTC | 16m |
| YV671T |  | General Manuel Carlos Piar International Airport (SVPR) | Bocon Airport (SVBN) | 2026-05-02 10:06 UTC | 2026-05-02 10:47 UTC | 40m |
| MNE329 | MNE | Nantes Atlantique Airport (LFRS) | Tivat Airport (LYTV) | 2026-05-02 08:41 UTC | 2026-05-02 10:47 UTC | 2h 5m |
| RYR2ZA | Ryanair | Ciampino Airport (LIRA) | LHLI (LHLI) | 2026-05-02 09:26 UTC | 2026-05-02 10:46 UTC | 1h 19m |
| S5DOT |  | Novo Mesto Airport (LJNM) | Novo Mesto Airport (LJNM) | 2026-05-02 09:42 UTC | 2026-05-02 10:46 UTC | 1h 3m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-02 09:34 UTC | 2026-05-02 10:44 UTC | 1h 9m |
| AZG9602 | AZG | Oslo Gardermoen Airport (ENGM) | Zhuhai Airport (ZGSD) | 2026-05-01 19:34 UTC | 2026-05-02 10:44 UTC | 15h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
