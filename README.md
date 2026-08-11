# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_21:46:19_UTC-green)

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

**Latest saved flight:** 2026-08-11 21:46:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 21:46:19 UTC

- **188,117** saved flights
- **59,584** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,117** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,255,958.4 tonnes** estimated CO2 emissions
- **130,780,198 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7476 |
| 2 | SkyWest Airlines | 6839 |
| 3 | EJA | 3711 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2943 |
| 6 | American Airlines | 2930 |
| 7 | ENY | 2334 |
| 8 | Delta Air Lines | 2212 |
| 9 | LATAM Airlines | 1757 |
| 10 | AZU | 1692 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1563 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1474 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1155 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1120 |
| 22 | VIV | 1040 |
| 23 | GLO | 1014 |
| 24 | Air France | 978 |
| 25 | AEE | 969 |
| 26 | PGT | 966 |
| 27 | CXK | 965 |
| 28 | United Airlines | 962 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160570 |
| 2 | 🇪🇸 ES | 12128 |
| 3 | 🇧🇷 BR | 10803 |
| 4 | 🇦🇺 AU | 10484 |
| 5 | 🇨🇦 CA | 10293 |
| 6 | 🇮🇳 IN | 10266 |
| 7 | 🇮🇹 IT | 9759 |
| 8 | 🇩🇪 DE | 9297 |
| 9 | 🇬🇧 GB | 8755 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7527 |
| 12 | 🇨🇴 CO | 7149 |
| 13 | 🇬🇷 GR | 5517 |
| 14 | 🇲🇽 MX | 5360 |
| 15 | 🇨🇭 CH | 5033 |
| 16 | 🇹🇷 TR | 4979 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3120 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2672 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1913 |
| 27 | 🇭🇷 HR | 1910 |
| 28 | 🇲🇪 ME | 1684 |
| 29 | 🇳🇱 NL | 1677 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3906 |
| 2 | Denver International Airport |  | US | 3102 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2310 |
| 6 | Harry Reid International Airport |  | US | 2203 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 8 | Zurich Airport |  | CH | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1948 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1709 |
| 12 | El Dorado International Airport |  | CO | 1691 |
| 13 | Salt Lake City International Airport |  | US | 1676 |
| 14 | Chicago O'Hare International Airport |  | US | 1657 |
| 15 | Frankfurt am Main International Airport |  | DE | 1614 |
| 16 | Congonhas Airport |  | BR | 1573 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1460 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1396 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1345 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1178 |
| 30 | Ninoy Aquino International Airport |  | PH | 1169 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1156 |
| 32 | Barcelona International Airport |  | ES | 1127 |
| 33 | Reno/Tahoe International Airport |  | US | 1084 |
| 34 | Viracopos International Airport |  | BR | 1084 |
| 35 | Seattle-Tacoma International Airport |  | US | 1080 |
| 36 | Calgary International Airport |  | CA | 1069 |
| 37 | Daniel K Inouye International Airport |  | US | 1059 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1034 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 952 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 687 | 21m | 244 km | 2,892.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 316 | 27m | 275 km | 1,497.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 305 | 14m | 114 km | 598.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 282 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 231 | 50m | 556 km | 2,214.3 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 231 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 224 | 19m | 144 km | 557.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 204 | 1h 49m | 1,304 km | 4,589.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TEX02 | TEX | RNZAF Base Ohakea (NZOH) | RNZAF Base Ohakea (NZOH) | 2026-08-11 21:19 UTC | 2026-08-11 21:46 UTC | 27m |
| NASA806 | NAS | Husky Ranch Airport (MT40) | 7 Oaks Flight Park Airport (K7S1) | 2026-08-11 19:54 UTC | 2026-08-11 21:45 UTC | 1h 51m |
| N54855 |  | Tulsa International Airport (KTUL) | 84OL (84OL) | 2026-08-11 21:27 UTC | 2026-08-11 21:43 UTC | 16m |
| TKR912 | TKR | Mc Clellan Airfield (KMCC) | NV17 (NV17) | 2026-08-11 21:21 UTC | 2026-08-11 21:39 UTC | 18m |
| N5479D |  | Cricket Field (4WA2) | Olympia Regional Airport (KOLM) | 2026-08-11 20:34 UTC | 2026-08-11 21:34 UTC | 1h 0m |
| EDGE92 | EDG | 4OL3 (4OL3) | Ksa Orchards Airport (OK11) | 2026-08-11 20:59 UTC | 2026-08-11 21:33 UTC | 33m |
| N280AF |  | Dekalb-Peachtree Airport (KPDK) | Morristown Municipal Airport (KMMU) | 2026-08-11 19:43 UTC | 2026-08-11 21:31 UTC | 1h 47m |
| BB201 |  | Skypark Estates Owners Assoc Airport (18FD) | Brewton Municipal Airport (K12J) | 2026-08-11 21:17 UTC | 2026-08-11 21:31 UTC | 13m |
|  |  | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-08-11 20:55 UTC | 2026-08-11 21:25 UTC | 30m |
| N789FA |  | Meadows Field (KBFL) | Visalia Municipal Airport (KVIS) | 2026-08-11 20:19 UTC | 2026-08-11 21:25 UTC | 1h 5m |
| SUNDG22 | SUN | TA29 (TA29) | Four Square Ranch Airport (3TA0) | 2026-08-11 21:05 UTC | 2026-08-11 21:23 UTC | 18m |
| SUNDG21 | SUN | Four Square Ranch Airport (3TA0) | Four Square Ranch Airport (3TA0) | 2026-08-11 21:08 UTC | 2026-08-11 21:23 UTC | 14m |
| N8157K |  | Wahoo Municipal Airport (KAHQ) | Wahoo Municipal Airport (KAHQ) | 2026-08-11 21:20 UTC | 2026-08-11 21:20 UTC | 0m |
| EJM652 | EJM | Washington Dulles International Airport (KIAD) | Ohkay Owingeh Airport (KE14) | 2026-08-11 17:53 UTC | 2026-08-11 21:19 UTC | 3h 25m |
| N939SP |  | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-08-11 20:48 UTC | 2026-08-11 21:18 UTC | 30m |
| N454NC |  | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-11 21:06 UTC | 2026-08-11 21:18 UTC | 12m |
| BELIGOUC | Brussels Airlines | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-08-11 20:17 UTC | 2026-08-11 21:17 UTC | 59m |
| N1530W |  | Sacramento Mather Airport (KMHR) | Hayward Executive Airport (KHWD) | 2026-08-11 20:44 UTC | 2026-08-11 21:14 UTC | 30m |
| ARCAS16 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-08-11 20:56 UTC | 2026-08-11 21:11 UTC | 15m |
| JRE853 | JRE | San Diego International Airport (KSAN) | Jacqueline Cochran Regional Airport (KTRM) | 2026-08-11 20:51 UTC | 2026-08-11 21:11 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
