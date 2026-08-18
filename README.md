# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_12:48:14_UTC-green)

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

**Latest saved flight:** 2026-08-18 12:48:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 12:48:14 UTC

- **211,753** saved flights
- **67,178** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,753** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,546,282.4 tonnes** estimated CO2 emissions
- **147,610,575 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8389 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3624 |
| 5 | American Airlines | 3534 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2731 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1990 |
| 10 | AZU | 1919 |
| 11 | Lufthansa | 1778 |
| 12 | Vueling | 1770 |
| 13 | WIF | 1700 |
| 14 | LXJ | 1670 |
| 15 | easyJet | 1469 |
| 16 | Swiss International | 1418 |
| 17 | AXM | 1389 |
| 18 | United Airlines | 1341 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1303 |
| 21 | EJU | 1301 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1164 |
| 24 | Air France | 1142 |
| 25 | GLO | 1142 |
| 26 | PGT | 1139 |
| 27 | WMT | 1081 |
| 28 | JetBlue | 1080 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1053 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178940 |
| 2 | 🇪🇸 ES | 13567 |
| 3 | 🇧🇷 BR | 12124 |
| 4 | 🇦🇺 AU | 11956 |
| 5 | 🇨🇦 CA | 11696 |
| 6 | 🇮🇳 IN | 11297 |
| 7 | 🇮🇹 IT | 11112 |
| 8 | 🇩🇪 DE | 10467 |
| 9 | 🇬🇧 GB | 9879 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8504 |
| 12 | 🇫🇷 FR | 8412 |
| 13 | 🇬🇷 GR | 6207 |
| 14 | 🇹🇷 TR | 6055 |
| 15 | 🇲🇽 MX | 5931 |
| 16 | 🇨🇭 CH | 5615 |
| 17 | 🇳🇴 NO | 5269 |
| 18 | 🇲🇾 MY | 3671 |
| 19 | 🇿🇦 ZA | 3572 |
| 20 | 🇵🇱 PL | 3498 |
| 21 | 🇹🇭 TH | 3433 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2825 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2294 |
| 27 | 🇲🇦 MA | 2135 |
| 28 | 🇳🇱 NL | 1887 |
| 29 | 🇲🇪 ME | 1818 |
| 30 | 🇮🇩 ID | 1769 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4448 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2579 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2375 |
| 7 | Zurich Airport |  | CH | 2208 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2186 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1943 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1764 |
| 16 | Frankfurt am Main International Airport |  | DE | 1731 |
| 17 | Madrid Barajas International Airport |  | ES | 1661 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1596 |
| 20 | Capua Airport |  | IT | 1596 |
| 21 | Macau International Airport |  | MO | 1554 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1542 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1468 |
| 25 | Charles de Gaulle International Airport |  | FR | 1456 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1353 |
| 28 | Ninoy Aquino International Airport |  | PH | 1339 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1298 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1279 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1228 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1172 |
| 37 | Vitoria/Foronda Airport |  | ES | 1170 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1143 |
| 40 | Don Mueang International Airport |  | TH | 1135 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 752 | 21m | 244 km | 3,166.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 434 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 352 | 27m | 275 km | 1,668.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 274 | 21m | 250 km | 1,183.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 260 | 1h 38m | 1,156 km | 5,186.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 250 | 19m | 165 km | 711.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 243 | 31m | 369 km | 1,546.8 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 243 | 19m | 144 km | 604.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SKYVAN4 | SKY | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-08-18 12:34 UTC | 2026-08-18 12:48 UTC | 13m |
| LXJ429 | LXJ | Westchester County Airport (KHPN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-18 12:14 UTC | 2026-08-18 12:47 UTC | 32m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-08-18 11:33 UTC | 2026-08-18 12:47 UTC | 1h 13m |
| N442CA |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-08-18 12:08 UTC | 2026-08-18 12:44 UTC | 35m |
| N999VP |  | 93LL (93LL) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-18 12:26 UTC | 2026-08-18 12:43 UTC | 17m |
| BPX262 | BPX | Cobb County International/Mccollum Field (KRYY) | Grayhill Airport (GA98) | 2026-08-18 11:47 UTC | 2026-08-18 12:43 UTC | 55m |
| THNDR12 | THN | New River Mcas (Mccutcheon Field) Airport (KNCA) | Topsail Airpark (01NC) | 2026-08-18 12:26 UTC | 2026-08-18 12:41 UTC | 14m |
| N44AE |  | Fort Worth Meacham International Airport (KFTW) | Buffalo Chips Airpark (TE45) | 2026-08-18 12:02 UTC | 2026-08-18 12:31 UTC | 28m |
| IAM3183 | IAM | Ciampino Airport (LIRA) | Gioia Del Colle Airport (LIBV) | 2026-08-18 12:01 UTC | 2026-08-18 12:30 UTC | 29m |
| N124LL |  | Wellington Aero Club Airport (FD38) | Belle Glade State Municipal Airport (KX10) | 2026-08-18 12:16 UTC | 2026-08-18 12:27 UTC | 10m |
| RYR6EK | Ryanair | Birmingham International Airport (EGBB) | Dublin Airport (EIDW) | 2026-08-18 11:44 UTC | 2026-08-18 12:26 UTC | 41m |
| N500RH |  | Concord-Padgett Regional Airport (KJQF) | Dekalb-Peachtree Airport (KPDK) | 2026-08-18 11:43 UTC | 2026-08-18 12:26 UTC | 42m |
| N739CD |  | Mc Alester Regional Airport (KMLC) | 19OK (19OK) | 2026-08-18 11:40 UTC | 2026-08-18 12:16 UTC | 36m |
| RYR4764 | Ryanair | Liverpool John Lennon Airport (EGGP) | Cork Airport (EICK) | 2026-08-18 11:26 UTC | 2026-08-18 12:15 UTC | 49m |
| OEADW | OEA | Voslau Airport (LOAV) | Voslau Airport (LOAV) | 2026-08-18 11:48 UTC | 2026-08-18 12:09 UTC | 20m |
| N939AC |  | Venice Municipal Airport (KVNC) | Punta Gorda Airport (KPGD) | 2026-08-18 11:40 UTC | 2026-08-18 12:09 UTC | 28m |
| N600HN |  | Carr Airport (WV65) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-18 12:02 UTC | 2026-08-18 12:07 UTC | 5m |
| TUTOR983 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-18 11:37 UTC | 2026-08-18 11:58 UTC | 21m |
| UFX61 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-18 11:20 UTC | 2026-08-18 11:57 UTC | 36m |
| SWU1953 | SWU | Dusseldorf International Airport (EDDL) | Trento / Mattarello Airport (LIDT) | 2026-08-18 10:45 UTC | 2026-08-18 11:52 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
