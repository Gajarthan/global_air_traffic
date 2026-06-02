# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_21:37:16_UTC-green)

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

**Latest saved flight:** 2026-06-02 21:37:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-02 21:37:16 UTC

- **101,126** saved flights
- **35,881** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **101,126** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,237,730.7 tonnes** estimated CO2 emissions
- **71,752,506 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4183 |
| 2 | SkyWest Airlines | 3802 |
| 3 | IndiGo | 2036 |
| 4 | EJA | 1928 |
| 5 | American Airlines | 1634 |
| 6 | Southwest Airlines | 1532 |
| 7 | ENY | 1259 |
| 8 | Delta Air Lines | 1187 |
| 9 | Lufthansa | 1184 |
| 10 | Vueling | 944 |
| 11 | LATAM Airlines | 898 |
| 12 | WIF | 888 |
| 13 | AXM | 871 |
| 14 | AZU | 814 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 736 |
| 17 | All Nippon Airways | 717 |
| 18 | Alaska Airlines | 706 |
| 19 | QLK | 678 |
| 20 | easyJet | 658 |
| 21 | EJU | 636 |
| 22 | Cathay Pacific | 608 |
| 23 | AEE | 589 |
| 24 | Air France | 586 |
| 25 | VIV | 585 |
| 26 | United Airlines | 566 |
| 27 | CXK | 543 |
| 28 | MXY | 541 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 500 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84788 |
| 2 | 🇪🇸 ES | 7003 |
| 3 | 🇮🇳 IN | 6439 |
| 4 | 🇦🇺 AU | 6109 |
| 5 | 🇧🇷 BR | 5522 |
| 6 | 🇩🇪 DE | 5470 |
| 7 | 🇮🇹 IT | 5396 |
| 8 | 🇨🇦 CA | 5231 |
| 9 | 🇯🇵 JP | 4687 |
| 10 | 🇬🇧 GB | 4298 |
| 11 | 🇫🇷 FR | 4036 |
| 12 | 🇨🇴 CO | 3497 |
| 13 | 🇲🇽 MX | 3056 |
| 14 | 🇬🇷 GR | 2881 |
| 15 | 🇳🇴 NO | 2813 |
| 16 | 🇨🇭 CH | 2604 |
| 17 | 🇲🇾 MY | 2219 |
| 18 | 🇹🇷 TR | 1919 |
| 19 | 🇿🇦 ZA | 1765 |
| 20 | 🇳🇿 NZ | 1695 |
| 21 | 🇹🇭 TH | 1679 |
| 22 | 🇰🇷 KR | 1639 |
| 23 | 🇵🇱 PL | 1625 |
| 24 | 🇬🇹 GT | 1498 |
| 25 | 🇵🇭 PH | 1473 |
| 26 | 🇲🇦 MA | 1132 |
| 27 | 🇲🇴 MO | 1069 |
| 28 | 🇳🇱 NL | 1008 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 892 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2203 |
| 2 | Denver International Airport |  | US | 1739 |
| 3 | Tokyo International Airport |  | JP | 1556 |
| 4 | Indira Gandhi International Airport |  | IN | 1401 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1296 |
| 6 | Harry Reid International Airport |  | US | 1294 |
| 7 | Guaymaral Airport |  | CO | 1264 |
| 8 | Frankfurt am Main International Airport |  | DE | 1184 |
| 9 | Zurich Airport |  | CH | 1155 |
| 10 | La Aurora Airport |  | GT | 1152 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1093 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1069 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1026 |
| 15 | Chicago O'Hare International Airport |  | US | 1013 |
| 16 | Madrid Barajas International Airport |  | ES | 880 |
| 17 | Kuala Lumpur International Airport |  | MY | 878 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 868 |
| 19 | Salt Lake City International Airport |  | US | 855 |
| 20 | Capua Airport |  | IT | 838 |
| 21 | Charlotte/Douglas International Airport |  | US | 785 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 784 |
| 23 | Charles de Gaulle International Airport |  | FR | 778 |
| 24 | Malpensa International Airport |  | IT | 770 |
| 25 | Bengaluru International Airport |  | IN | 769 |
| 26 | Congonhas Airport |  | BR | 768 |
| 27 | Daniel K Inouye International Airport |  | US | 698 |
| 28 | Tenerife Norte Airport |  | ES | 697 |
| 29 | Ninoy Aquino International Airport |  | PH | 673 |
| 30 | Barcelona International Airport |  | ES | 669 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 658 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 658 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 644 |
| 34 | Amsterdam Airport Schiphol |  | NL | 623 |
| 35 | Don Mueang International Airport |  | TH | 616 |
| 36 | Vitoria/Foronda Airport |  | ES | 614 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 593 |
| 39 | Seattle-Tacoma International Airport |  | US | 581 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 521 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 367 | 21m | 244 km | 1,545.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 271 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 265 | 24m | 225 km | 1,028.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 248 | 1h 26m | 910 km | 3,891.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 244 | 28m | 304 km | 1,279.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 211 | 19m | 165 km | 600.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 199 | 26m | 275 km | 943.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 158 | 20m | 99 km | 270.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 147 | 22m | 55 km | 139.7 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 146 | 14m | 154 km | 386.8 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 135 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N921AZ |  | Regeneration Airport (5AZ9) | Phoenix Sky Harbor International Airport (KPHX) | 2026-06-02 21:10 UTC | 2026-06-02 21:37 UTC | 26m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-06-02 10:36 UTC | 2026-06-02 21:33 UTC | 10h 56m |
| N7621G |  | Lincoln County Regional Airport (KIPJ) | Hickory Regional Airport (KHKY) | 2026-06-02 21:18 UTC | 2026-06-02 21:31 UTC | 13m |
| SCU20 | SCU | Cherokee Ranch Airport (OK25) | Haskell Airport (K2K9) | 2026-06-02 20:40 UTC | 2026-06-02 21:27 UTC | 47m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-06-02 17:43 UTC | 2026-06-02 21:25 UTC | 3h 42m |
| C6539 |  | San Francisco International Airport (KSFO) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-02 20:48 UTC | 2026-06-02 21:19 UTC | 31m |
| CXK421 | CXK | Concord-Padgett Regional Airport (KJQF) | Gold Hill Airport (NC25) | 2026-06-02 20:57 UTC | 2026-06-02 21:14 UTC | 17m |
| N399W |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-06-02 20:50 UTC | 2026-06-02 21:13 UTC | 23m |
| N918CA |  | Long Beach (Daugherty Field) Airport (KLGB) | Oakland San Francisco Bay Airport (KOAK) | 2026-06-02 19:47 UTC | 2026-06-02 21:12 UTC | 1h 24m |
| ERU9 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-06-02 20:59 UTC | 2026-06-02 21:11 UTC | 12m |
| RYR25ZN | Ryanair | Luqa Airport (LMML) | Bari / Palese International Airport (LIBD) | 2026-06-02 20:12 UTC | 2026-06-02 21:09 UTC | 57m |
| N172LK |  | Mc Clellan-Palomar Airport (KCRQ) | Bob Maxwell Memorial Airfield (KOKB) | 2026-06-02 20:46 UTC | 2026-06-02 21:08 UTC | 21m |
| RYR8PE | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Inowrocław Military Air Base (EPIR) | 2026-06-02 20:36 UTC | 2026-06-02 21:01 UTC | 25m |
| SR1 |  | Hood Field (66NC) | NC87 (NC87) | 2026-06-02 20:27 UTC | 2026-06-02 20:58 UTC | 31m |
| CFYKT | CFY | Rockton Airport (CPT3) | Rockton Airport (CPT3) | 2026-06-02 16:28 UTC | 2026-06-02 20:58 UTC | 4h 30m |
| SCU22 | SCU | 2OL2 (2OL2) | Haskell Airport (K2K9) | 2026-06-02 20:41 UTC | 2026-06-02 20:57 UTC | 16m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Richie Rich Airport (8TE1) | 2026-06-02 20:21 UTC | 2026-06-02 20:57 UTC | 35m |
| CGCUL | CGC | Calgary International Airport (CYYC) | Ponoka Industrial Airport (CEH3) | 2026-06-02 20:41 UTC | 2026-06-02 20:56 UTC | 15m |
| N108RF |  | IS63 (IS63) | De Kalb Taylor Municipal Airport (KDKB) | 2026-06-02 20:12 UTC | 2026-06-02 20:55 UTC | 43m |
| N118UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-06-02 20:36 UTC | 2026-06-02 20:53 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
