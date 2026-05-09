# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_20:12:23_UTC-green)

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

**Latest saved flight:** 2026-05-09 20:12:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 20:12:23 UTC

- **76,006** saved flights
- **27,926** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,006** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **937,627.7 tonnes** estimated CO2 emissions
- **54,355,228 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3249 |
| 2 | SkyWest Airlines | 2822 |
| 3 | IndiGo | 1696 |
| 4 | EJA | 1398 |
| 5 | American Airlines | 1187 |
| 6 | Southwest Airlines | 1109 |
| 7 | Lufthansa | 994 |
| 8 | ENY | 949 |
| 9 | Delta Air Lines | 752 |
| 10 | Vueling | 731 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 702 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 610 |
| 16 | QLK | 579 |
| 17 | Swiss International | 578 |
| 18 | LXJ | 560 |
| 19 | Alaska Airlines | 533 |
| 20 | easyJet | 502 |
| 21 | AEE | 490 |
| 22 | EJU | 489 |
| 23 | Cathay Pacific | 477 |
| 24 | VIV | 458 |
| 25 | Air France | 443 |
| 26 | Japan Airlines | 443 |
| 27 | AXB | 419 |
| 28 | CXK | 391 |
| 29 | AIQ | 377 |
| 30 | MXY | 372 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61334 |
| 2 | 🇪🇸 ES | 5439 |
| 3 | 🇮🇳 IN | 5315 |
| 4 | 🇦🇺 AU | 4954 |
| 5 | 🇩🇪 DE | 4286 |
| 6 | 🇧🇷 BR | 4254 |
| 7 | 🇮🇹 IT | 4160 |
| 8 | 🇯🇵 JP | 3960 |
| 9 | 🇨🇦 CA | 3791 |
| 10 | 🇬🇧 GB | 3260 |
| 11 | 🇫🇷 FR | 3013 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2347 |
| 14 | 🇬🇷 GR | 2238 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2069 |
| 17 | 🇲🇾 MY | 1773 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1366 |
| 20 | 🇹🇷 TR | 1363 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1272 |
| 23 | 🇵🇭 PH | 1216 |
| 24 | 🇬🇹 GT | 1197 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 897 |
| 27 | 🇲🇴 MO | 882 |
| 28 | 🇲🇪 ME | 807 |
| 29 | 🇳🇱 NL | 795 |
| 30 | 🇭🇷 HR | 649 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1682 |
| 2 | Tokyo International Airport |  | JP | 1330 |
| 3 | Denver International Airport |  | US | 1275 |
| 4 | Indira Gandhi International Airport |  | IN | 1116 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1099 |
| 6 | Frankfurt am Main International Airport |  | DE | 991 |
| 7 | Harry Reid International Airport |  | US | 947 |
| 8 | Zurich Airport |  | CH | 899 |
| 9 | La Aurora Airport |  | GT | 898 |
| 10 | Guaymaral Airport |  | CO | 890 |
| 11 | Macau International Airport |  | MO | 882 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 767 |
| 14 | Chicago O'Hare International Airport |  | US | 742 |
| 15 | Kuala Lumpur International Airport |  | MY | 713 |
| 16 | Madrid Barajas International Airport |  | ES | 709 |
| 17 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 679 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 675 |
| 19 | Bengaluru International Airport |  | IN | 660 |
| 20 | Malpensa International Airport |  | IT | 654 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 651 |
| 22 | Salt Lake City International Airport |  | US | 624 |
| 23 | Congonhas Airport |  | BR | 601 |
| 24 | Charlotte/Douglas International Airport |  | US | 597 |
| 25 | Charles de Gaulle International Airport |  | FR | 593 |
| 26 | Capua Airport |  | IT | 591 |
| 27 | Tenerife Norte Airport |  | ES | 564 |
| 28 | Daniel K Inouye International Airport |  | US | 554 |
| 29 | Ninoy Aquino International Airport |  | PH | 551 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 541 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 513 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 511 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 502 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Amsterdam Airport Schiphol |  | NL | 477 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 477 |
| 38 | Don Mueang International Airport |  | TH | 475 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 452 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 271 | 21m | 244 km | 1,141.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 194 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 94 | 1h 19m | 961 km | 1,558.1 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 94 | 52m | 556 km | 901.1 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N91630 |  | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-05-09 19:51 UTC | 2026-05-09 20:12 UTC | 21m |
| N73286 |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-05-09 19:52 UTC | 2026-05-09 20:08 UTC | 16m |
| AFR1610 | Air France | Charles de Gaulle International Airport (LFPG) | Hamburg Airport (EDDH) | 2026-05-09 18:53 UTC | 2026-05-09 19:59 UTC | 1h 6m |
| N111TD |  | Cole Ranch Airport (94XS) | West Houston Airport (KIWS) | 2026-05-09 19:51 UTC | 2026-05-09 19:58 UTC | 7m |
| CHP14 | CHP | CA53 (CA53) | 52CN (52CN) | 2026-05-09 19:26 UTC | 2026-05-09 19:54 UTC | 27m |
| FFT3045 | FFT | Hartsfield/Jackson Atlanta International Airport (KATL) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 17:41 UTC | 2026-05-09 19:53 UTC | 2h 12m |
| DAL1641 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 19:36 UTC | 2026-05-09 19:50 UTC | 13m |
| N48C |  | Camarillo Airport (KCMA) | St George Regional Airport (KSGU) | 2026-05-09 18:56 UTC | 2026-05-09 19:49 UTC | 53m |
| QTR8440 | Qatar Airways | Mong Hpayak Airport (VYMH) | Zhuhai Airport (ZGSD) | 2026-05-08 23:15 UTC | 2026-05-09 19:48 UTC | 20h 33m |
| N223WT |  | William R Fairchild International Airport (KCLM) | Tacoma Narrows Airport (KTIW) | 2026-05-09 18:59 UTC | 2026-05-09 19:48 UTC | 49m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-09 19:24 UTC | 2026-05-09 19:40 UTC | 16m |
| HLE27 | HLE | London City Airport (EGLC) | London City Airport (EGLC) | 2026-05-09 19:30 UTC | 2026-05-09 19:40 UTC | 9m |
| N776TX |  | Mc Clellan-Palomar Airport (KCRQ) | Riverside Airport (KRAL) | 2026-05-09 18:59 UTC | 2026-05-09 19:39 UTC | 39m |
| EJA670 | EJA | Allegheny County Airport (KAGC) | Teterboro Airport (KTEB) | 2026-05-09 18:47 UTC | 2026-05-09 19:36 UTC | 49m |
| DAL2185 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 19:25 UTC | 2026-05-09 19:35 UTC | 10m |
| N835ZT |  | Indianapolis Executive Airport (KTYQ) | Antrim County Airport (KACB) | 2026-05-09 18:47 UTC | 2026-05-09 19:34 UTC | 46m |
| OXF6978 | OXF | Falcon Field (KFFZ) | Coolidge Municipal Airport (KP08) | 2026-05-09 16:44 UTC | 2026-05-09 19:27 UTC | 2h 43m |
| QTR8464 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-09 12:42 UTC | 2026-05-09 19:26 UTC | 6h 44m |
| DAL2171 | Delta Air Lines | Harry Reid International Airport (KLAS) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 16:46 UTC | 2026-05-09 19:25 UTC | 2h 39m |
| N786FA |  | Oxnard Airport (KOXR) | Meadows Field (KBFL) | 2026-05-09 18:23 UTC | 2026-05-09 19:25 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
