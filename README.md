# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_14:24:45_UTC-green)

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

**Latest saved flight:** 2026-07-29 14:24:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 14:24:45 UTC

- **158,261** saved flights
- **52,437** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **158,261** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,899,785.7 tonnes** estimated CO2 emissions
- **110,132,506 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6363 |
| 2 | SkyWest Airlines | 5778 |
| 3 | EJA | 3124 |
| 4 | IndiGo | 2797 |
| 5 | American Airlines | 2516 |
| 6 | Southwest Airlines | 2483 |
| 7 | ENY | 1969 |
| 8 | Delta Air Lines | 1874 |
| 9 | Lufthansa | 1514 |
| 10 | LATAM Airlines | 1482 |
| 11 | AZU | 1393 |
| 12 | WIF | 1335 |
| 13 | Vueling | 1331 |
| 14 | LXJ | 1217 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1091 |
| 17 | easyJet | 1034 |
| 18 | Alaska Airlines | 991 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 968 |
| 22 | VIV | 868 |
| 23 | CXK | 838 |
| 24 | United Airlines | 838 |
| 25 | Cathay Pacific | 833 |
| 26 | GLO | 829 |
| 27 | AEE | 828 |
| 28 | Air France | 823 |
| 29 | MXY | 823 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136382 |
| 2 | 🇪🇸 ES | 10189 |
| 3 | 🇧🇷 BR | 9041 |
| 4 | 🇦🇺 AU | 8951 |
| 5 | 🇮🇳 IN | 8797 |
| 6 | 🇨🇦 CA | 8567 |
| 7 | 🇮🇹 IT | 8176 |
| 8 | 🇩🇪 DE | 8037 |
| 9 | 🇬🇧 GB | 7270 |
| 10 | 🇯🇵 JP | 6480 |
| 11 | 🇫🇷 FR | 6268 |
| 12 | 🇨🇴 CO | 5544 |
| 13 | 🇲🇽 MX | 4536 |
| 14 | 🇬🇷 GR | 4534 |
| 15 | 🇳🇴 NO | 4186 |
| 16 | 🇨🇭 CH | 4158 |
| 17 | 🇹🇷 TR | 3789 |
| 18 | 🇲🇾 MY | 2892 |
| 19 | 🇵🇱 PL | 2692 |
| 20 | 🇿🇦 ZA | 2566 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2274 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2027 |
| 26 | 🇲🇦 MA | 1614 |
| 27 | 🇲🇪 ME | 1520 |
| 28 | 🇭🇷 HR | 1464 |
| 29 | 🇳🇱 NL | 1447 |
| 30 | 🇲🇴 MO | 1311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3244 |
| 2 | Denver International Airport |  | US | 2640 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 1984 |
| 5 | Indira Gandhi International Airport |  | IN | 1957 |
| 6 | Harry Reid International Airport |  | US | 1928 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1754 |
| 8 | Zurich Airport |  | CH | 1698 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1658 |
| 10 | La Aurora Airport |  | GT | 1572 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1475 |
| 12 | Frankfurt am Main International Airport |  | DE | 1461 |
| 13 | El Dorado International Airport |  | CO | 1439 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1422 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Macau International Airport |  | MO | 1311 |
| 18 | Congonhas Airport |  | BR | 1306 |
| 19 | Madrid Barajas International Airport |  | ES | 1256 |
| 20 | Capua Airport |  | IT | 1245 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1213 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1136 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1125 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1087 |
| 27 | Bengaluru International Airport |  | IN | 1048 |
| 28 | Malpensa International Airport |  | IT | 1040 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 962 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 956 |
| 32 | Barcelona International Airport |  | ES | 947 |
| 33 | Daniel K Inouye International Airport |  | US | 933 |
| 34 | Seattle-Tacoma International Airport |  | US | 923 |
| 35 | Calgary International Airport |  | CA | 908 |
| 36 | Viracopos International Airport |  | BR | 904 |
| 37 | Tenerife Norte Airport |  | ES | 896 |
| 38 | Scottsdale Airport |  | US | 893 |
| 39 | Oslo Gardermoen Airport |  | NO | 879 |
| 40 | Amsterdam Airport Schiphol |  | NL | 870 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 833 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 572 | 21m | 244 km | 2,408.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 377 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 292 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 278 | 27m | 275 km | 1,317.3 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 223 | 44m | 241 km | 926.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 208 | 26m | 215 km | 770.3 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 203 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 187 | 1h 15m | 961 km | 3,099.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 179 | 50m | 556 km | 1,715.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 177 | 1h 39m | 1,156 km | 3,531.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 175 | 1h 1m | 695 km | 2,097.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 49m | 1,304 km | 3,779.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N43813 |  | Northeast Philadelphia Airport (KPNE) | Wings Field (KLOM) | 2026-07-29 13:03 UTC | 2026-07-29 14:24 UTC | 1h 20m |
| N226DH |  | 93LL (93LL) | 72IS (72IS) | 2026-07-29 13:58 UTC | 2026-07-29 14:20 UTC | 22m |
| N111MP |  | KFTG (KFTG) | Morris Airport (CD13) | 2026-07-29 14:04 UTC | 2026-07-29 14:19 UTC | 15m |
| N1432C |  | Knoxville Downtown Island Airport (KDKX) | Knoxville Downtown Island Airport (KDKX) | 2026-07-29 14:05 UTC | 2026-07-29 14:17 UTC | 11m |
| SCU24 | SCU | 2OL2 (2OL2) | Gregg Airport (7OK1) | 2026-07-29 13:40 UTC | 2026-07-29 14:15 UTC | 35m |
| CXK448 | CXK | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-07-29 13:38 UTC | 2026-07-29 14:15 UTC | 36m |
| HB3384 |  | Gruyeres Airport (LSGT) | Raron Airport (LSTA) | 2026-07-29 11:58 UTC | 2026-07-29 14:15 UTC | 2h 16m |
| N151GD |  | 2TS6 (2TS6) | Mid-Way Regional Airport (KJWY) | 2026-07-29 13:45 UTC | 2026-07-29 14:15 UTC | 29m |
| CSN3193 | China Southern | Shenzhen Bao'an International Airport (ZGSZ) | Macau International Airport (VMMC) | 2026-07-29 04:55 UTC | 2026-07-29 14:14 UTC | 9h 19m |
| MONEY51 | MON | Flysooner Field (OK50) | Thomas Municipal Airport (K1O4) | 2026-07-29 14:02 UTC | 2026-07-29 14:14 UTC | 12m |
| N80866 |  | NM74 (NM74) | Manzano Mtn Air Ranch Airport (NM89) | 2026-07-29 13:33 UTC | 2026-07-29 14:13 UTC | 39m |
| N7871W |  | Grove Hill Airport (5TX2) | Jones Field (KF00) | 2026-07-29 13:45 UTC | 2026-07-29 14:12 UTC | 27m |
| N402AA |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-07-29 13:33 UTC | 2026-07-29 14:07 UTC | 33m |
| N716PV |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-07-29 13:21 UTC | 2026-07-29 14:06 UTC | 45m |
| N399AA |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-07-29 13:58 UTC | 2026-07-29 14:03 UTC | 5m |
| PTO6613 | PTO | Rostock-Laage Airport (ETNL) | Lubeck Blankensee Airport (EDHL) | 2026-07-29 12:20 UTC | 2026-07-29 14:02 UTC | 1h 42m |
| N218AC |  | Paros Airport (LGPA) | Paros Airport (LGPA) | 2026-07-29 13:47 UTC | 2026-07-29 14:02 UTC | 14m |
| N14C |  | Deland Municipal-Sidney H Taylor Field (KDED) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-07-29 14:00 UTC | 2026-07-29 14:01 UTC | 1m |
| SCU20 | SCU | Pheasant Wings Airport (26OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-07-29 13:45 UTC | 2026-07-29 14:01 UTC | 16m |
| N7644G |  | 8OA9 (8OA9) | Wayne County Airport (KBJJ) | 2026-07-29 13:50 UTC | 2026-07-29 14:01 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
