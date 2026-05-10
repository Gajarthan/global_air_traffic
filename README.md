# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_17:23:02_UTC-green)

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

**Latest saved flight:** 2026-05-10 17:23:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 17:23:02 UTC

- **77,239** saved flights
- **28,247** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,239** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **957,368.8 tonnes** estimated CO2 emissions
- **55,499,642 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3316 |
| 2 | SkyWest Airlines | 2858 |
| 3 | IndiGo | 1723 |
| 4 | EJA | 1414 |
| 5 | American Airlines | 1206 |
| 6 | Southwest Airlines | 1132 |
| 7 | Lufthansa | 1011 |
| 8 | ENY | 965 |
| 9 | Delta Air Lines | 807 |
| 10 | Vueling | 741 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 664 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 614 |
| 16 | QLK | 591 |
| 17 | Swiss International | 585 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 542 |
| 20 | easyJet | 517 |
| 21 | EJU | 502 |
| 22 | Cathay Pacific | 498 |
| 23 | AEE | 497 |
| 24 | VIV | 461 |
| 25 | Air France | 456 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 430 |
| 28 | CXK | 395 |
| 29 | AIQ | 386 |
| 30 | MXY | 382 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62222 |
| 2 | 🇪🇸 ES | 5536 |
| 3 | 🇮🇳 IN | 5406 |
| 4 | 🇦🇺 AU | 5029 |
| 5 | 🇩🇪 DE | 4380 |
| 6 | 🇧🇷 BR | 4297 |
| 7 | 🇮🇹 IT | 4266 |
| 8 | 🇯🇵 JP | 4017 |
| 9 | 🇨🇦 CA | 3831 |
| 10 | 🇬🇧 GB | 3327 |
| 11 | 🇫🇷 FR | 3071 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2365 |
| 14 | 🇬🇷 GR | 2284 |
| 15 | 🇳🇴 NO | 2121 |
| 16 | 🇨🇭 CH | 2086 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇳🇿 NZ | 1391 |
| 20 | 🇹🇷 TR | 1388 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1291 |
| 23 | 🇵🇭 PH | 1242 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1201 |
| 26 | 🇲🇦 MA | 913 |
| 27 | 🇲🇴 MO | 911 |
| 28 | 🇲🇪 ME | 824 |
| 29 | 🇳🇱 NL | 809 |
| 30 | 🇭🇷 HR | 673 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1710 |
| 2 | Tokyo International Airport |  | JP | 1348 |
| 3 | Denver International Airport |  | US | 1288 |
| 4 | Indira Gandhi International Airport |  | IN | 1142 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1121 |
| 6 | Frankfurt am Main International Airport |  | DE | 1012 |
| 7 | Harry Reid International Airport |  | US | 958 |
| 8 | Macau International Airport |  | MO | 911 |
| 9 | Zurich Airport |  | CH | 911 |
| 10 | La Aurora Airport |  | GT | 902 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 778 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 772 |
| 15 | Chicago O'Hare International Airport |  | US | 755 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 717 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 683 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 672 |
| 20 | Malpensa International Airport |  | IT | 671 |
| 21 | Bengaluru International Airport |  | IN | 670 |
| 22 | Salt Lake City International Airport |  | US | 629 |
| 23 | Capua Airport |  | IT | 613 |
| 24 | Charles de Gaulle International Airport |  | FR | 609 |
| 25 | Charlotte/Douglas International Airport |  | US | 607 |
| 26 | Congonhas Airport |  | BR | 607 |
| 27 | Tenerife Norte Airport |  | ES | 575 |
| 28 | Ninoy Aquino International Airport |  | PH | 565 |
| 29 | Daniel K Inouye International Airport |  | US | 560 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 555 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 525 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 523 |
| 33 | Barcelona International Airport |  | ES | 523 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 505 |
| 35 | Don Mueang International Airport |  | TH | 490 |
| 36 | Vitoria/Foronda Airport |  | ES | 489 |
| 37 | Amsterdam Airport Schiphol |  | NL | 487 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 481 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 459 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 275 | 21m | 244 km | 1,157.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 196 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 184 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 165 | 26m | 275 km | 781.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 118 | 27m | 215 km | 437.0 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 98 | 1h 3m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 96 | 18m | 144 km | 238.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N535DM |  | Central Il Regional/Bloomington-Normal Airport (KBMI) | General Downing - Peoria International Airport (KPIA) | 2026-05-10 17:09 UTC | 2026-05-10 17:23 UTC | 13m |
| N8080A |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | K5W8 (K5W8) | 2026-05-10 17:01 UTC | 2026-05-10 17:22 UTC | 20m |
| N875ST |  | 6PA1 (6PA1) | PN85 (PN85) | 2026-05-10 15:37 UTC | 2026-05-10 17:15 UTC | 1h 38m |
| N15CG |  | Lee Gilmer Memorial Airport (KGVL) | Smyrna Airport (KMQY) | 2026-05-10 16:12 UTC | 2026-05-10 17:13 UTC | 1h 0m |
| TRP7 | TRP | 5MD8 (5MD8) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-05-10 16:58 UTC | 2026-05-10 17:10 UTC | 11m |
| TOM4GE | TOM | Paphos International Airport (LCPH) | Manchester Airport (EGCC) | 2026-05-10 12:21 UTC | 2026-05-10 17:05 UTC | 4h 43m |
| DLX50 | DLX | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-05-10 16:01 UTC | 2026-05-10 17:00 UTC | 59m |
| N43138 |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-05-10 16:40 UTC | 2026-05-10 16:55 UTC | 14m |
| CGSGP | CGS | Kerry Airport (EIKY) | Bantry Aerodrome (EIBN) | 2026-05-10 16:19 UTC | 2026-05-10 16:54 UTC | 35m |
| N800WE |  | Calgary International Airport (CYYC) | Sparwood Elk Valley Airport (CYSW) | 2026-05-10 14:37 UTC | 2026-05-10 16:51 UTC | 2h 13m |
| TTJ603 | TTJ | M. R. Stefanik Airport (LZIB) | Letnany Airport (LKLT) | 2026-05-10 16:03 UTC | 2026-05-10 16:50 UTC | 46m |
| GDK56R | GDK | Vienna International Airport (LOWW) | Trento / Mattarello Airport (LIDT) | 2026-05-10 15:39 UTC | 2026-05-10 16:49 UTC | 1h 10m |
| N942MB |  | Middle Georgia Regional Airport (KMCN) | Tupelo Regional Airport (KTUP) | 2026-05-10 16:05 UTC | 2026-05-10 16:47 UTC | 42m |
| DAL2156 | Delta Air Lines | Norman Y Mineta San Jose International Airport (KSJC) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 13:21 UTC | 2026-05-10 16:46 UTC | 3h 25m |
| ILMBD | ILM | Bergamo / Orio Al Serio Airport (LIME) | Linate Airport (LIML) | 2026-05-10 16:37 UTC | 2026-05-10 16:45 UTC | 8m |
| KSF12 | KSF | Kent State University Airport (K1G3) | Akron-Canton Regional Airport (KCAK) | 2026-05-10 16:25 UTC | 2026-05-10 16:45 UTC | 19m |
| N40RF |  | Chico Regional Airport (KCIC) | Sacramento Executive Airport (KSAC) | 2026-05-10 15:50 UTC | 2026-05-10 16:45 UTC | 54m |
|  |  | Kingston Ranch Airport (04NV) | Kingston Ranch Airport (04NV) | 2026-05-10 16:44 UTC | 2026-05-10 16:44 UTC | 0m |
| N10FZ |  | KSOY (KSOY) | Glenwood Municipal Airport (KGHW) | 2026-05-10 16:03 UTC | 2026-05-10 16:42 UTC | 39m |
| N121SK |  | Cloverdale Municipal Airport (KO60) | CA38 (CA38) | 2026-05-10 15:57 UTC | 2026-05-10 16:42 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
