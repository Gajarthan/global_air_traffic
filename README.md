# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_21:28:39_UTC-green)

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

**Latest saved flight:** 2026-05-24 21:28:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 21:28:39 UTC

- **94,325** saved flights
- **33,293** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,325** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,160,747.9 tonnes** estimated CO2 emissions
- **67,289,731 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3985 |
| 2 | SkyWest Airlines | 3508 |
| 3 | IndiGo | 1954 |
| 4 | EJA | 1782 |
| 5 | American Airlines | 1436 |
| 6 | Southwest Airlines | 1371 |
| 7 | ENY | 1170 |
| 8 | Lufthansa | 1136 |
| 9 | Delta Air Lines | 1034 |
| 10 | Vueling | 902 |
| 11 | LATAM Airlines | 848 |
| 12 | AXM | 835 |
| 13 | WIF | 822 |
| 14 | AZU | 752 |
| 15 | LXJ | 712 |
| 16 | Swiss International | 708 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 655 |
| 19 | QLK | 650 |
| 20 | easyJet | 621 |
| 21 | EJU | 607 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 568 |
| 24 | VIV | 559 |
| 25 | Air France | 557 |
| 26 | CXK | 502 |
| 27 | MXY | 500 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77959 |
| 2 | 🇪🇸 ES | 6623 |
| 3 | 🇮🇳 IN | 6172 |
| 4 | 🇦🇺 AU | 5748 |
| 5 | 🇩🇪 DE | 5188 |
| 6 | 🇧🇷 BR | 5176 |
| 7 | 🇮🇹 IT | 5121 |
| 8 | 🇨🇦 CA | 4785 |
| 9 | 🇯🇵 JP | 4524 |
| 10 | 🇬🇧 GB | 4031 |
| 11 | 🇫🇷 FR | 3814 |
| 12 | 🇨🇴 CO | 3266 |
| 13 | 🇲🇽 MX | 2899 |
| 14 | 🇬🇷 GR | 2708 |
| 15 | 🇳🇴 NO | 2627 |
| 16 | 🇨🇭 CH | 2480 |
| 17 | 🇲🇾 MY | 2111 |
| 18 | 🇹🇷 TR | 1742 |
| 19 | 🇿🇦 ZA | 1701 |
| 20 | 🇹🇭 TH | 1596 |
| 21 | 🇳🇿 NZ | 1594 |
| 22 | 🇵🇱 PL | 1549 |
| 23 | 🇰🇷 KR | 1515 |
| 24 | 🇵🇭 PH | 1420 |
| 25 | 🇬🇹 GT | 1415 |
| 26 | 🇲🇦 MA | 1081 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 951 |
| 29 | 🇲🇪 ME | 938 |
| 30 | 🇭🇷 HR | 860 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2045 |
| 2 | Denver International Airport |  | US | 1597 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1343 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1247 |
| 6 | Harry Reid International Airport |  | US | 1209 |
| 7 | Frankfurt am Main International Airport |  | DE | 1152 |
| 8 | Guaymaral Airport |  | CO | 1140 |
| 9 | Zurich Airport |  | CH | 1104 |
| 10 | La Aurora Airport |  | GT | 1082 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1027 |
| 13 | El Dorado International Airport |  | CO | 1026 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 943 |
| 15 | Chicago O'Hare International Airport |  | US | 908 |
| 16 | Madrid Barajas International Airport |  | ES | 841 |
| 17 | Kuala Lumpur International Airport |  | MY | 838 |
| 18 | Salt Lake City International Airport |  | US | 797 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 796 |
| 20 | Capua Airport |  | IT | 785 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 747 |
| 22 | Malpensa International Airport |  | IT | 743 |
| 23 | Charles de Gaulle International Airport |  | FR | 739 |
| 24 | Bengaluru International Airport |  | IN | 739 |
| 25 | Charlotte/Douglas International Airport |  | US | 718 |
| 26 | Congonhas Airport |  | BR | 717 |
| 27 | Daniel K Inouye International Airport |  | US | 676 |
| 28 | Tenerife Norte Airport |  | ES | 673 |
| 29 | Ninoy Aquino International Airport |  | PH | 649 |
| 30 | Barcelona International Airport |  | ES | 636 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 633 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 614 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 605 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Vitoria/Foronda Airport |  | ES | 587 |
| 36 | Amsterdam Airport Schiphol |  | NL | 586 |
| 37 | Don Mueang International Airport |  | TH | 585 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 561 |
| 40 | O. R. Tambo International Airport |  | ZA | 539 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 468 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 347 | 21m | 244 km | 1,461.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 140 | 27m | 215 km | 518.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 122 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 1m | 695 km | 1,450.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 121 | 18m | 144 km | 301.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 117 | 1h 40m | 1,156 km | 2,334.1 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 52m | 1,304 km | 2,542.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N794BC |  | Chicago/Rockford International Airport (KRFD) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-24 19:54 UTC | 2026-05-24 21:28 UTC | 1h 34m |
| N991FG |  | Triangle North Executive Airport (KLHZ) | Triangle North Executive Airport (KLHZ) | 2026-05-24 21:07 UTC | 2026-05-24 21:23 UTC | 16m |
| VLG6LX | Vueling | Barcelona International Airport (LEBL) | Tenerife Norte Airport (GCXO) | 2026-05-24 18:04 UTC | 2026-05-24 21:21 UTC | 3h 16m |
| N614JT |  | Mcnary Field (KSLE) | Lambert Field (4OR3) | 2026-05-24 21:13 UTC | 2026-05-24 21:20 UTC | 7m |
| N345P |  | Indianapolis International Airport (KIND) | Dubuque Regional Airport (KDBQ) | 2026-05-24 19:59 UTC | 2026-05-24 21:10 UTC | 1h 11m |
| N67DN |  | Renton Municipal Airport (KRNT) | Boeing Field/King County International Airport (KBFI) | 2026-05-24 20:46 UTC | 2026-05-24 21:03 UTC | 17m |
|  |  | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Moncton / McEwen Airport (CCG4) | 2026-05-24 20:11 UTC | 2026-05-24 21:03 UTC | 51m |
| N65411 |  | San Luis Obispo County Regional Airport (KSBP) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-24 20:22 UTC | 2026-05-24 21:01 UTC | 39m |
| N2569Q |  | Ogden-Hinckley Airport (KOGD) | K36U (K36U) | 2026-05-24 20:23 UTC | 2026-05-24 20:54 UTC | 31m |
| PFT605 | PFT | Los Angeles International Airport (KLAX) | Telluride Regional Airport (KTEX) | 2026-05-24 19:19 UTC | 2026-05-24 20:52 UTC | 1h 32m |
| EZY858W | easyJet | Bristol International Airport (EGGD) | Glasgow International Airport (EGPF) | 2026-05-24 19:56 UTC | 2026-05-24 20:51 UTC | 54m |
| 9ADWA |  | Maastricht Aachen Airport (EHBK) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-05-24 19:25 UTC | 2026-05-24 20:48 UTC | 1h 23m |
| UAL316 | United Airlines | Dublin Airport (EIDW) | Newark Liberty International Airport (KEWR) | 2026-05-24 13:42 UTC | 2026-05-24 20:44 UTC | 7h 1m |
| N66M |  | Boulder Creek Airstrip (44ID) | San Bernardino International Airport (KSBD) | 2026-05-24 18:59 UTC | 2026-05-24 20:43 UTC | 1h 43m |
| LIFELN3 | LIF | Cheyenne Regional/Jerry Olson Field (KCYS) | Crystal Lakes Airport (25CO) | 2026-05-24 20:21 UTC | 2026-05-24 20:38 UTC | 17m |
| N855RA |  | Las Cruces International Airport (KLRU) | Winona-Montgomery County Airport (K5A6) | 2026-05-24 18:36 UTC | 2026-05-24 20:38 UTC | 2h 2m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-05-24 19:16 UTC | 2026-05-24 20:38 UTC | 1h 22m |
| VLG9CD | Vueling | Palma De Mallorca Airport (LEPA) | Valencia Airport (LEVC) | 2026-05-24 20:05 UTC | 2026-05-24 20:34 UTC | 29m |
| EZY25DH | easyJet | Belfast International Airport (EGAA) | Manchester Airport (EGCC) | 2026-05-24 19:55 UTC | 2026-05-24 20:31 UTC | 36m |
| SWA1083 | Southwest Airlines | Austin-Bergstrom International Airport (KAUS) | Pensacola International Airport (KPNS) | 2026-05-24 19:03 UTC | 2026-05-24 20:31 UTC | 1h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
