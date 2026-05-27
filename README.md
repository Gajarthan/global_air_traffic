# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_06:08:31_UTC-green)

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

**Latest saved flight:** 2026-05-27 06:08:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-27 06:08:31 UTC

- **95,253** saved flights
- **33,550** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,253** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,170,394.8 tonnes** estimated CO2 emissions
- **67,848,972 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4009 |
| 2 | SkyWest Airlines | 3538 |
| 3 | IndiGo | 1980 |
| 4 | EJA | 1797 |
| 5 | American Airlines | 1444 |
| 6 | Southwest Airlines | 1387 |
| 7 | ENY | 1176 |
| 8 | Lufthansa | 1142 |
| 9 | Delta Air Lines | 1044 |
| 10 | Vueling | 907 |
| 11 | LATAM Airlines | 858 |
| 12 | AXM | 845 |
| 13 | WIF | 831 |
| 14 | AZU | 762 |
| 15 | LXJ | 721 |
| 16 | Swiss International | 712 |
| 17 | All Nippon Airways | 707 |
| 18 | QLK | 663 |
| 19 | Alaska Airlines | 662 |
| 20 | easyJet | 623 |
| 21 | EJU | 610 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 573 |
| 24 | VIV | 564 |
| 25 | Air France | 562 |
| 26 | CXK | 507 |
| 27 | MXY | 505 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 482 |
| 30 | AIQ | 461 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78643 |
| 2 | 🇪🇸 ES | 6666 |
| 3 | 🇮🇳 IN | 6243 |
| 4 | 🇦🇺 AU | 5872 |
| 5 | 🇩🇪 DE | 5228 |
| 6 | 🇧🇷 BR | 5226 |
| 7 | 🇮🇹 IT | 5161 |
| 8 | 🇨🇦 CA | 4823 |
| 9 | 🇯🇵 JP | 4575 |
| 10 | 🇬🇧 GB | 4068 |
| 11 | 🇫🇷 FR | 3850 |
| 12 | 🇨🇴 CO | 3286 |
| 13 | 🇲🇽 MX | 2926 |
| 14 | 🇬🇷 GR | 2741 |
| 15 | 🇳🇴 NO | 2650 |
| 16 | 🇨🇭 CH | 2502 |
| 17 | 🇲🇾 MY | 2143 |
| 18 | 🇹🇷 TR | 1761 |
| 19 | 🇿🇦 ZA | 1715 |
| 20 | 🇳🇿 NZ | 1632 |
| 21 | 🇹🇭 TH | 1622 |
| 22 | 🇰🇷 KR | 1575 |
| 23 | 🇵🇱 PL | 1560 |
| 24 | 🇵🇭 PH | 1442 |
| 25 | 🇬🇹 GT | 1425 |
| 26 | 🇲🇦 MA | 1087 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 958 |
| 29 | 🇲🇪 ME | 941 |
| 30 | 🇭🇷 HR | 866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2057 |
| 2 | Denver International Airport |  | US | 1614 |
| 3 | Tokyo International Airport |  | JP | 1518 |
| 4 | Indira Gandhi International Airport |  | IN | 1353 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1258 |
| 6 | Harry Reid International Airport |  | US | 1228 |
| 7 | Frankfurt am Main International Airport |  | DE | 1156 |
| 8 | Guaymaral Airport |  | CO | 1153 |
| 9 | Zurich Airport |  | CH | 1115 |
| 10 | La Aurora Airport |  | GT | 1091 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1031 |
| 13 | El Dorado International Airport |  | CO | 1030 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 952 |
| 15 | Chicago O'Hare International Airport |  | US | 919 |
| 16 | Kuala Lumpur International Airport |  | MY | 850 |
| 17 | Madrid Barajas International Airport |  | ES | 845 |
| 18 | Salt Lake City International Airport |  | US | 802 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 801 |
| 20 | Capua Airport |  | IT | 789 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 762 |
| 22 | Malpensa International Airport |  | IT | 752 |
| 23 | Bengaluru International Airport |  | IN | 748 |
| 24 | Charles de Gaulle International Airport |  | FR | 743 |
| 25 | Congonhas Airport |  | BR | 726 |
| 26 | Charlotte/Douglas International Airport |  | US | 723 |
| 27 | Daniel K Inouye International Airport |  | US | 682 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 658 |
| 30 | Barcelona International Airport |  | ES | 641 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 640 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 618 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 612 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Don Mueang International Airport |  | TH | 592 |
| 36 | Amsterdam Airport Schiphol |  | NL | 591 |
| 37 | Vitoria/Foronda Airport |  | ES | 589 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 569 |
| 39 | Calgary International Airport |  | CA | 563 |
| 40 | O. R. Tambo International Airport |  | ZA | 544 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 473 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 352 | 21m | 244 km | 1,482.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 260 | 24m | 225 km | 1,008.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 253 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 239 | 28m | 304 km | 1,252.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 144 | 14m | 154 km | 381.5 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 143 | 27m | 215 km | 529.6 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 124 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 119 | 1h 39m | 1,156 km | 2,374.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 52m | 1,304 km | 2,587.2 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N479LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-27 05:21 UTC | 2026-05-27 06:08 UTC | 46m |
| YHT | YHT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-27 05:34 UTC | 2026-05-27 05:59 UTC | 25m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-05-27 05:32 UTC | 2026-05-27 05:40 UTC | 7m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-05-27 04:58 UTC | 2026-05-27 05:37 UTC | 38m |
| WZZ5009 | Wizz Air | John Paul II International Airport Kraków-Balice Airport (EPKK) | Vilnius International Airport (EYVI) | 2026-05-27 04:36 UTC | 2026-05-27 05:35 UTC | 59m |
| LN949BW |  | Solomon State Field (AK26) | Elim Airport (PFEL) | 2026-05-27 05:17 UTC | 2026-05-27 05:35 UTC | 17m |
| EJU31ZN | EJU | Paris-Orly Airport (LFPO) | Linate Airport (LIML) | 2026-05-27 04:25 UTC | 2026-05-27 05:35 UTC | 1h 9m |
| STA611 | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-05-27 05:20 UTC | 2026-05-27 05:32 UTC | 11m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-05-27 05:08 UTC | 2026-05-27 05:30 UTC | 21m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-05-27 04:56 UTC | 2026-05-27 05:29 UTC | 33m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-05-27 04:29 UTC | 2026-05-27 05:25 UTC | 56m |
| R03326 |  | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | 2026-05-27 03:52 UTC | 2026-05-27 05:18 UTC | 1h 25m |
| THA570 | Thai Airways | Suvarnabhumi Airport (VTBS) | Xieng Khouang Airport (VLXK) | 2026-05-27 04:34 UTC | 2026-05-27 05:17 UTC | 43m |
| AEA27GB | AEA | Madrid Barajas International Airport (LEMD) | Bilbao Airport (LEBB) | 2026-05-27 04:46 UTC | 2026-05-27 05:16 UTC | 29m |
| ANA1233 | All Nippon Airways | Komatsu Airport (RJNK) | Hofu Airport (RJOF) | 2026-05-27 04:19 UTC | 2026-05-27 05:14 UTC | 54m |
| DEPAA | DEP | Dimokritos Airport (LGAL) | Plovdiv International Airport (LBPD) | 2026-05-27 04:24 UTC | 2026-05-27 05:14 UTC | 49m |
| LR455 |  | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-05-27 04:34 UTC | 2026-05-27 05:13 UTC | 38m |
| LLR821 | LLR | Indira Gandhi International Airport (VIDP) | Kalka Airport (VI71) | 2026-05-27 04:31 UTC | 2026-05-27 05:12 UTC | 40m |
| IGO7573 | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-05-27 04:38 UTC | 2026-05-27 05:11 UTC | 33m |
| IGO479 | IndiGo | Sardar Vallabhbhai Patel International Airport (VAAH) | Coimbatore Air Force Station (VOSX) | 2026-05-27 01:35 UTC | 2026-05-27 05:10 UTC | 3h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
