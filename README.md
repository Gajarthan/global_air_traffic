# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_21:20:48_UTC-green)

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

**Latest saved flight:** 2026-08-07 21:20:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 21:20:48 UTC

- **176,715** saved flights
- **56,974** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,715** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,124,872.0 tonnes** estimated CO2 emissions
- **123,180,987 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7005 |
| 2 | SkyWest Airlines | 6457 |
| 3 | EJA | 3495 |
| 4 | IndiGo | 3093 |
| 5 | Southwest Airlines | 2785 |
| 6 | American Airlines | 2767 |
| 7 | ENY | 2200 |
| 8 | Delta Air Lines | 2085 |
| 9 | LATAM Airlines | 1636 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1573 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1458 |
| 14 | LXJ | 1390 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1197 |
| 17 | AXM | 1196 |
| 18 | EJU | 1082 |
| 19 | QLK | 1082 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1069 |
| 22 | VIV | 971 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 938 |
| 25 | GLO | 930 |
| 26 | AEE | 922 |
| 27 | United Airlines | 916 |
| 28 | Air France | 911 |
| 29 | MXY | 890 |
| 30 | JetBlue | 872 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151994 |
| 2 | 🇪🇸 ES | 11323 |
| 3 | 🇧🇷 BR | 10083 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9696 |
| 6 | 🇨🇦 CA | 9674 |
| 7 | 🇮🇹 IT | 9133 |
| 8 | 🇩🇪 DE | 8740 |
| 9 | 🇬🇧 GB | 8167 |
| 10 | 🇯🇵 JP | 7077 |
| 11 | 🇫🇷 FR | 7023 |
| 12 | 🇨🇴 CO | 6493 |
| 13 | 🇬🇷 GR | 5146 |
| 14 | 🇲🇽 MX | 5050 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4605 |
| 17 | 🇹🇷 TR | 4388 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2936 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2624 |
| 22 | 🇳🇿 NZ | 2559 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2260 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1790 |
| 27 | 🇭🇷 HR | 1737 |
| 28 | 🇲🇪 ME | 1607 |
| 29 | 🇳🇱 NL | 1590 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3652 |
| 2 | Denver International Airport |  | US | 2927 |
| 3 | Tokyo International Airport |  | JP | 2209 |
| 4 | Guaymaral Airport |  | CO | 2170 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2105 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1913 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1848 |
| 10 | La Aurora Airport |  | GT | 1738 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1623 |
| 12 | Chicago O'Hare International Airport |  | US | 1590 |
| 13 | Salt Lake City International Airport |  | US | 1581 |
| 14 | El Dorado International Airport |  | CO | 1581 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1465 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1425 |
| 19 | Capua Airport |  | IT | 1382 |
| 20 | Madrid Barajas International Airport |  | ES | 1379 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1315 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1242 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1211 |
| 25 | Malpensa International Airport |  | IT | 1207 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1093 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1093 |
| 32 | Barcelona International Airport |  | ES | 1050 |
| 33 | Seattle-Tacoma International Airport |  | US | 1016 |
| 34 | Daniel K Inouye International Airport |  | US | 1014 |
| 35 | Viracopos International Airport |  | BR | 1008 |
| 36 | Reno/Tahoe International Airport |  | US | 1006 |
| 37 | Calgary International Airport |  | CA | 1004 |
| 38 | Oslo Gardermoen Airport |  | NO | 988 |
| 39 | Tenerife Norte Airport |  | ES | 970 |
| 40 | Amsterdam Airport Schiphol |  | NL | 956 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 896 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 644 | 21m | 244 km | 2,711.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 413 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 218 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 211 | 1h 15m | 961 km | 3,497.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 192 | 1h 2m | 695 km | 2,301.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SCU10 | SCU | Sahoma Lake Airport (03OK) | William R Pogue Municipal Airport (KOWP) | 2026-08-07 20:02 UTC | 2026-08-07 21:20 UTC | 1h 18m |
| VAR453 | VAR | Avi Suquilla Airport (KP20) | Lake Havasu City Airport (KHII) | 2026-08-07 20:52 UTC | 2026-08-07 21:10 UTC | 17m |
| ARCAS11 | ARC | Danaher Airport (7TX0) | Arledge Field (KF56) | 2026-08-07 20:54 UTC | 2026-08-07 21:06 UTC | 11m |
| N259LA |  | Minder Airport (37IL) | Litchfield Airport (4IS7) | 2026-08-07 20:50 UTC | 2026-08-07 21:05 UTC | 15m |
| N138DM |  | Nashville International Airport (KBNA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-07 18:04 UTC | 2026-08-07 21:04 UTC | 2h 59m |
| BOE448 | BOE | Renton Municipal Airport (KRNT) | Othello Municipal Airport (KS70) | 2026-08-07 19:44 UTC | 2026-08-07 21:02 UTC | 1h 18m |
| C6065 |  | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-07 20:38 UTC | 2026-08-07 20:58 UTC | 19m |
| EJA374 | EJA | Buchanan Field (KCCR) | Redding Regional Airport (KRDD) | 2026-08-07 20:21 UTC | 2026-08-07 20:56 UTC | 34m |
| XACIC | XAC | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-08-07 20:44 UTC | 2026-08-07 20:54 UTC | 10m |
| TIFON5 | TIF | Guaymaral Airport (SKGY) | German Olano Air Base (SKPQ) | 2026-08-07 20:14 UTC | 2026-08-07 20:53 UTC | 38m |
| N717AF |  | Byron Airport (KC83) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-07 20:08 UTC | 2026-08-07 20:52 UTC | 44m |
| N747WG |  | Deland Municipal-Sidney H Taylor Field (KDED) | Blue Ridge Flightpark Airport (34FD) | 2026-08-07 20:26 UTC | 2026-08-07 20:51 UTC | 24m |
| TWY3 | TWY | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-08-07 20:32 UTC | 2026-08-07 20:50 UTC | 18m |
| N2822S |  | Georgetown Executive Airport (KGTU) | Taylor Municipal Airport (KT74) | 2026-08-07 20:32 UTC | 2026-08-07 20:48 UTC | 16m |
| CFR210 | CFR | Chico Regional Airport (KCIC) | Rogers Field (KO05) | 2026-08-07 20:35 UTC | 2026-08-07 20:47 UTC | 11m |
| N7ZT |  | San Luis Obispo County Regional Airport (KSBP) | K4SD (K4SD) | 2026-08-07 19:31 UTC | 2026-08-07 20:47 UTC | 1h 15m |
| XSN90 | XSN | Palo Alto Airport (KPAO) | Lake Tahoe Airport (KTVL) | 2026-08-07 20:11 UTC | 2026-08-07 20:45 UTC | 34m |
| N280YB |  | Washington Dulles International Airport (KIAD) | Tazewell County Airport (KJFZ) | 2026-08-07 20:01 UTC | 2026-08-07 20:43 UTC | 41m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Foremost Airport (CFD4) | 2026-08-07 20:15 UTC | 2026-08-07 20:42 UTC | 26m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-08-07 06:08 UTC | 2026-08-07 20:41 UTC | 14h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
