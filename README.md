# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_23:36:35_UTC-green)

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

**Latest saved flight:** 2026-08-08 23:36:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 23:36:35 UTC

- **179,960** saved flights
- **57,683** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **179,960** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,163,368.5 tonnes** estimated CO2 emissions
- **125,412,669 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7126 |
| 2 | SkyWest Airlines | 6576 |
| 3 | EJA | 3549 |
| 4 | IndiGo | 3145 |
| 5 | Southwest Airlines | 2838 |
| 6 | American Airlines | 2814 |
| 7 | ENY | 2247 |
| 8 | Delta Air Lines | 2138 |
| 9 | LATAM Airlines | 1678 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1487 |
| 14 | LXJ | 1406 |
| 15 | easyJet | 1228 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1211 |
| 18 | EJU | 1095 |
| 19 | QLK | 1093 |
| 20 | Alaska Airlines | 1091 |
| 21 | All Nippon Airways | 1088 |
| 22 | VIV | 993 |
| 23 | GLO | 963 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 936 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 903 |
| 30 | PGT | 895 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154462 |
| 2 | 🇪🇸 ES | 11553 |
| 3 | 🇧🇷 BR | 10338 |
| 4 | 🇦🇺 AU | 10081 |
| 5 | 🇮🇳 IN | 9861 |
| 6 | 🇨🇦 CA | 9829 |
| 7 | 🇮🇹 IT | 9285 |
| 8 | 🇩🇪 DE | 8896 |
| 9 | 🇬🇧 GB | 8306 |
| 10 | 🇯🇵 JP | 7231 |
| 11 | 🇫🇷 FR | 7152 |
| 12 | 🇨🇴 CO | 6701 |
| 13 | 🇬🇷 GR | 5243 |
| 14 | 🇲🇽 MX | 5154 |
| 15 | 🇨🇭 CH | 4789 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4581 |
| 18 | 🇲🇾 MY | 3160 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2719 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2368 |
| 24 | 🇬🇹 GT | 2292 |
| 25 | 🇰🇷 KR | 2243 |
| 26 | 🇲🇦 MA | 1816 |
| 27 | 🇭🇷 HR | 1793 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3727 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2246 |
| 4 | Guaymaral Airport |  | CO | 2222 |
| 5 | Indira Gandhi International Airport |  | IN | 2196 |
| 6 | Harry Reid International Airport |  | US | 2123 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1934 |
| 8 | Zurich Airport |  | CH | 1909 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1761 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1647 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | El Dorado International Airport |  | CO | 1611 |
| 14 | Salt Lake City International Airport |  | US | 1610 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1498 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Madrid Barajas International Airport |  | ES | 1409 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1349 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1283 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1240 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1215 |
| 27 | Kuala Lumpur International Airport |  | MY | 1191 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1120 |
| 30 | Ninoy Aquino International Airport |  | PH | 1114 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1106 |
| 32 | Barcelona International Airport |  | ES | 1072 |
| 33 | Seattle-Tacoma International Airport |  | US | 1039 |
| 34 | Viracopos International Airport |  | BR | 1036 |
| 35 | Daniel K Inouye International Airport |  | US | 1033 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1028 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 663 | 21m | 244 km | 2,791.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 421 | 1h 8m | 770 km | 5,592.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 421 | 24m | 225 km | 1,633.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 217 | 1h 15m | 961 km | 3,596.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 215 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 210 | 1h 38m | 1,156 km | 4,189.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 207 | 31m | 369 km | 1,317.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 196 | 1h 2m | 695 km | 2,349.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N703LB |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-08 23:19 UTC | 2026-08-08 23:36 UTC | 17m |
| ZFN | ZFN | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-08 23:02 UTC | 2026-08-08 23:35 UTC | 32m |
| N950TT |  | Wheeler Army Air Field (PHHI) | Kawaihapai Airfield (PHDH) | 2026-08-08 23:15 UTC | 2026-08-08 23:26 UTC | 10m |
| N15000 |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-08 22:21 UTC | 2026-08-08 23:23 UTC | 1h 1m |
| N611AC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-08 17:01 UTC | 2026-08-08 23:22 UTC | 6h 21m |
| 051465 |  | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-08 23:10 UTC | 2026-08-08 23:21 UTC | 11m |
| N539SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-08 23:09 UTC | 2026-08-08 23:21 UTC | 11m |
| N3546T |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-08 17:00 UTC | 2026-08-08 23:19 UTC | 6h 19m |
| N1436J |  | General Dewitt Spain Airport (KM01) | 0AR2 (0AR2) | 2026-08-08 22:50 UTC | 2026-08-08 23:09 UTC | 18m |
|  |  | Independence Airport (K2O7) | Baker & Hall Airport (77CL) | 2026-08-08 22:42 UTC | 2026-08-08 23:07 UTC | 25m |
| TKR15 | TKR | Boise Air Trml/Gowen Field (KBOI) | Cascade Airport (KU70) | 2026-08-08 22:54 UTC | 2026-08-08 23:06 UTC | 11m |
| BSM | BSM | Toowoomba Airport (YTWB) | Ballina Byron Gateway Airport (YBNA) | 2026-08-08 22:30 UTC | 2026-08-08 23:04 UTC | 33m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-08 22:44 UTC | 2026-08-08 23:00 UTC | 16m |
| N127BH |  | Telluride Regional Airport (KTEX) | Telluride Regional Airport (KTEX) | 2026-08-08 22:46 UTC | 2026-08-08 22:59 UTC | 13m |
| DLX622 | DLX | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-08 22:05 UTC | 2026-08-08 22:56 UTC | 51m |
| N51XP |  | Cricket Field (4WA2) | Chehalis-Centralia Airport (KCLS) | 2026-08-08 22:19 UTC | 2026-08-08 22:54 UTC | 34m |
| TKR210 | TKR | Animas Air Park (K00C) | Hill Afb Airport (KHIF) | 2026-08-08 21:53 UTC | 2026-08-08 22:51 UTC | 58m |
| N721XL |  | Dallas Love Field (KDAL) | Miller-Herrold Airport (28MI) | 2026-08-08 20:39 UTC | 2026-08-08 22:49 UTC | 2h 9m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-08 22:31 UTC | 2026-08-08 22:48 UTC | 16m |
| N66KA |  | Flying D Airport (7TN5) | Wings Field (2TN2) | 2026-08-08 22:39 UTC | 2026-08-08 22:47 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
