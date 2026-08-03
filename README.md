# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_03:41:37_UTC-green)

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

**Latest saved flight:** 2026-08-03 03:41:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 03:41:37 UTC

- **168,158** saved flights
- **54,951** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,158** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,027,643.4 tonnes** estimated CO2 emissions
- **117,544,543 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6701 |
| 2 | SkyWest Airlines | 6146 |
| 3 | EJA | 3348 |
| 4 | IndiGo | 2960 |
| 5 | American Airlines | 2656 |
| 6 | Southwest Airlines | 2650 |
| 7 | ENY | 2099 |
| 8 | Delta Air Lines | 2009 |
| 9 | LATAM Airlines | 1560 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1481 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1383 |
| 14 | LXJ | 1318 |
| 15 | AXM | 1160 |
| 16 | Swiss International | 1151 |
| 17 | easyJet | 1130 |
| 18 | EJU | 1033 |
| 19 | Alaska Airlines | 1030 |
| 20 | QLK | 1024 |
| 21 | All Nippon Airways | 1020 |
| 22 | VIV | 928 |
| 23 | Cathay Pacific | 897 |
| 24 | CXK | 892 |
| 25 | United Airlines | 889 |
| 26 | GLO | 882 |
| 27 | AEE | 880 |
| 28 | Air France | 865 |
| 29 | MXY | 864 |
| 30 | JetBlue | 850 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145105 |
| 2 | 🇪🇸 ES | 10763 |
| 3 | 🇧🇷 BR | 9578 |
| 4 | 🇦🇺 AU | 9384 |
| 5 | 🇮🇳 IN | 9276 |
| 6 | 🇨🇦 CA | 9114 |
| 7 | 🇮🇹 IT | 8675 |
| 8 | 🇩🇪 DE | 8370 |
| 9 | 🇬🇧 GB | 7807 |
| 10 | 🇯🇵 JP | 6769 |
| 11 | 🇫🇷 FR | 6660 |
| 12 | 🇨🇴 CO | 6062 |
| 13 | 🇬🇷 GR | 4881 |
| 14 | 🇲🇽 MX | 4816 |
| 15 | 🇨🇭 CH | 4417 |
| 16 | 🇳🇴 NO | 4385 |
| 17 | 🇹🇷 TR | 4062 |
| 18 | 🇲🇾 MY | 3022 |
| 19 | 🇵🇱 PL | 2831 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2448 |
| 22 | 🇹🇭 TH | 2434 |
| 23 | 🇵🇭 PH | 2227 |
| 24 | 🇬🇹 GT | 2176 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1703 |
| 27 | 🇭🇷 HR | 1608 |
| 28 | 🇲🇪 ME | 1553 |
| 29 | 🇳🇱 NL | 1527 |
| 30 | 🇲🇴 MO | 1428 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3457 |
| 2 | Denver International Airport |  | US | 2799 |
| 3 | Tokyo International Airport |  | JP | 2127 |
| 4 | Guaymaral Airport |  | CO | 2094 |
| 5 | Indira Gandhi International Airport |  | IN | 2054 |
| 6 | Harry Reid International Airport |  | US | 2026 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1770 |
| 10 | La Aurora Airport |  | GT | 1681 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1553 |
| 12 | Chicago O'Hare International Airport |  | US | 1525 |
| 13 | El Dorado International Airport |  | CO | 1524 |
| 14 | Frankfurt am Main International Airport |  | DE | 1511 |
| 15 | Salt Lake City International Airport |  | US | 1506 |
| 16 | Macau International Airport |  | MO | 1428 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1394 |
| 18 | Congonhas Airport |  | BR | 1380 |
| 19 | Madrid Barajas International Airport |  | ES | 1325 |
| 20 | Capua Airport |  | IT | 1307 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1187 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1179 |
| 24 | Charlotte/Douglas International Airport |  | US | 1171 |
| 25 | Charles de Gaulle International Airport |  | FR | 1144 |
| 26 | Kuala Lumpur International Airport |  | MY | 1139 |
| 27 | Malpensa International Airport |  | IT | 1129 |
| 28 | Bengaluru International Airport |  | IN | 1100 |
| 29 | Ninoy Aquino International Airport |  | PH | 1047 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1035 |
| 32 | Barcelona International Airport |  | ES | 991 |
| 33 | Daniel K Inouye International Airport |  | US | 979 |
| 34 | Seattle-Tacoma International Airport |  | US | 978 |
| 35 | Viracopos International Airport |  | BR | 960 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 938 |
| 38 | Reno/Tahoe International Airport |  | US | 936 |
| 39 | Oslo Gardermoen Airport |  | NO | 932 |
| 40 | Scottsdale Airport |  | US | 932 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 871 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 612 | 21m | 244 km | 2,577.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 402 | 24m | 225 km | 1,559.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 196 | 31m | 369 km | 1,247.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 188 | 1h 38m | 1,156 km | 3,750.5 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SIA277 | Singapore Airlines | Singapore Changi International Airport (WSSS) | Hang Nadim Airport (WIDD) | 2026-08-03 00:39 UTC | 2026-08-03 03:41 UTC | 3h 1m |
| PUH | PUH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-03 03:13 UTC | 2026-08-03 03:37 UTC | 24m |
| CLX4167 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-08-02 10:35 UTC | 2026-08-03 03:25 UTC | 16h 50m |
| CES5032 | China Eastern | Changi Air Base (WSAC) | Macau International Airport (VMMC) | 2026-08-02 17:15 UTC | 2026-08-03 03:15 UTC | 10h 0m |
| JJP507 | JJP | Narita International Airport (RJAA) | Ashiya Airport (RJFA) | 2026-08-03 01:58 UTC | 2026-08-03 03:12 UTC | 1h 13m |
| N100BW |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-03 02:30 UTC | 2026-08-03 02:59 UTC | 29m |
| N510PR |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-08-03 02:28 UTC | 2026-08-03 02:55 UTC | 26m |
| IBX69 | IBX | Osaka International Airport (RJOO) | Ashiya Airport (RJFA) | 2026-08-03 01:59 UTC | 2026-08-03 02:54 UTC | 55m |
| RSCU550 | RSC | Bridgewater Airport (YBGR) | Melbourne Essendon Airport (YMEN) | 2026-08-03 01:05 UTC | 2026-08-03 02:53 UTC | 1h 48m |
| N886LF |  | Felts Field (KSFF) | 8WA5 (8WA5) | 2026-08-03 02:34 UTC | 2026-08-03 02:53 UTC | 19m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-08-03 02:17 UTC | 2026-08-03 02:51 UTC | 34m |
| ANA249 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-03 01:31 UTC | 2026-08-03 02:49 UTC | 1h 17m |
| N974CS |  | Helio Airport (2AK7) | Summit Airport (PAST) | 2026-08-03 02:22 UTC | 2026-08-03 02:48 UTC | 25m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-03 02:17 UTC | 2026-08-03 02:46 UTC | 29m |
| SFJ45 | SFJ | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-03 01:26 UTC | 2026-08-03 02:46 UTC | 1h 19m |
| FDA144 | FDA | Fukuoka Airport (RJFF) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-08-03 01:40 UTC | 2026-08-03 02:43 UTC | 1h 3m |
| SWA3562 | Southwest Airlines | Nashville International Airport (KBNA) | Dallas Love Field (KDAL) | 2026-08-03 01:21 UTC | 2026-08-03 02:43 UTC | 1h 22m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-08-03 02:19 UTC | 2026-08-03 02:42 UTC | 23m |
| VIV7435 | VIV | General Heriberto Jara International Airport (MMVR) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-03 02:04 UTC | 2026-08-03 02:41 UTC | 37m |
| JBU349 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-03 00:33 UTC | 2026-08-03 02:40 UTC | 2h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
