# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_06:32:28_UTC-green)

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

**Latest saved flight:** 2026-08-19 06:32:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 06:32:28 UTC

- **214,479** saved flights
- **67,750** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,479** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,578,310.0 tonnes** estimated CO2 emissions
- **149,467,245 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8497 |
| 2 | SkyWest Airlines | 7695 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3662 |
| 5 | American Airlines | 3579 |
| 6 | Southwest Airlines | 3430 |
| 7 | Delta Air Lines | 2767 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2027 |
| 10 | AZU | 1962 |
| 11 | Vueling | 1793 |
| 12 | Lufthansa | 1785 |
| 13 | WIF | 1716 |
| 14 | LXJ | 1694 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1429 |
| 17 | AXM | 1402 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1339 |
| 20 | Alaska Airlines | 1324 |
| 21 | EJU | 1317 |
| 22 | All Nippon Airways | 1298 |
| 23 | VIV | 1182 |
| 24 | GLO | 1163 |
| 25 | PGT | 1156 |
| 26 | Air France | 1154 |
| 27 | WMT | 1104 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1081 |
| 30 | Wizz Air | 1071 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181379 |
| 2 | 🇪🇸 ES | 13690 |
| 3 | 🇧🇷 BR | 12342 |
| 4 | 🇦🇺 AU | 12108 |
| 5 | 🇨🇦 CA | 11848 |
| 6 | 🇮🇳 IN | 11399 |
| 7 | 🇮🇹 IT | 11281 |
| 8 | 🇩🇪 DE | 10551 |
| 9 | 🇬🇧 GB | 9974 |
| 10 | 🇯🇵 JP | 8826 |
| 11 | 🇨🇴 CO | 8743 |
| 12 | 🇫🇷 FR | 8496 |
| 13 | 🇬🇷 GR | 6270 |
| 14 | 🇹🇷 TR | 6139 |
| 15 | 🇲🇽 MX | 6020 |
| 16 | 🇨🇭 CH | 5665 |
| 17 | 🇳🇴 NO | 5316 |
| 18 | 🇲🇾 MY | 3706 |
| 19 | 🇿🇦 ZA | 3608 |
| 20 | 🇵🇱 PL | 3530 |
| 21 | 🇹🇭 TH | 3470 |
| 22 | 🇳🇿 NZ | 2995 |
| 23 | 🇵🇭 PH | 2873 |
| 24 | 🇬🇹 GT | 2732 |
| 25 | 🇰🇷 KR | 2599 |
| 26 | 🇭🇷 HR | 2331 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1904 |
| 29 | 🇲🇪 ME | 1854 |
| 30 | 🇮🇩 ID | 1792 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4513 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2651 |
| 4 | Indira Gandhi International Airport |  | IN | 2604 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2395 |
| 7 | Zurich Airport |  | CH | 2227 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2201 |
| 10 | La Aurora Airport |  | GT | 2077 |
| 11 | El Dorado International Airport |  | CO | 1998 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1744 |
| 17 | Madrid Barajas International Airport |  | ES | 1668 |
| 18 | Capua Airport |  | IT | 1620 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1617 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1573 |
| 22 | Macau International Airport |  | MO | 1559 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1510 |
| 24 | Malpensa International Airport |  | IT | 1494 |
| 25 | Charles de Gaulle International Airport |  | FR | 1473 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1367 |
| 28 | Ninoy Aquino International Airport |  | PH | 1364 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Bengaluru International Airport |  | IN | 1309 |
| 31 | Barcelona International Airport |  | ES | 1306 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1254 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1179 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1153 |
| 40 | Don Mueang International Airport |  | TH | 1146 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 530 | 1h 7m | 770 km | 7,040.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 503 | 24m | 225 km | 1,951.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 354 | 27m | 275 km | 1,677.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 315 | 1h 49m | 1,423 km | 7,730.6 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 267 | 1h 38m | 1,156 km | 5,326.5 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 267 | 19m | 99 km | 457.4 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 262 | 27m | 215 km | 970.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 252 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 249 | 31m | 369 km | 1,584.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-19 05:39 UTC | 2026-08-19 06:32 UTC | 52m |
| ASA7096 | Alaska Airlines | Ted Stevens Anchorage International Airport (PANC) | Gustavus Airport (PAGS) | 2026-08-19 05:23 UTC | 2026-08-19 06:29 UTC | 1h 6m |
| XCN70 | XCN | Grant County International Airport (KMWH) | Fowler Field (02WN) | 2026-08-19 05:38 UTC | 2026-08-19 06:16 UTC | 37m |
| EFC70P | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-19 06:05 UTC | 2026-08-19 06:16 UTC | 10m |
| N883CE |  | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-08-19 05:21 UTC | 2026-08-19 06:12 UTC | 50m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-19 05:45 UTC | 2026-08-19 06:11 UTC | 25m |
| FD536 |  | Adelaide International Airport (YPAD) | Welbourn Hill Airport (YWLB) | 2026-08-18 23:50 UTC | 2026-08-19 06:10 UTC | 6h 19m |
| PSU224A | PSU | Barcelona International Airport (LEBL) | Cannes-Mandelieu Airport (LFMD) | 2026-08-19 05:00 UTC | 2026-08-19 06:05 UTC | 1h 5m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Zhuhai Airport (ZGSD) | 2026-08-18 19:43 UTC | 2026-08-19 06:02 UTC | 10h 19m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-19 05:35 UTC | 2026-08-19 06:00 UTC | 24m |
| RYR2RF | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Otocac Airport (LDRO) | 2026-08-19 05:32 UTC | 2026-08-19 05:59 UTC | 26m |
| CDX550 | CDX | Beirut Rafic Hariri International Airport (OLBA) | Diagoras Airport (LGRP) | 2026-08-19 04:51 UTC | 2026-08-19 05:58 UTC | 1h 6m |
| RYR7YT | Ryanair | Alicante International Airport (LEAL) | Niederrhein Airport (EDLV) | 2026-08-19 03:56 UTC | 2026-08-19 05:57 UTC | 2h 1m |
| AM281 |  | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-19 05:20 UTC | 2026-08-19 05:52 UTC | 32m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Osmany International Airport (VGSY) | 2026-08-19 02:21 UTC | 2026-08-19 05:51 UTC | 3h 30m |
| VLG883P | Vueling | Paris-Orly Airport (LFPO) | Garray Airport (LEGY) | 2026-08-19 04:45 UTC | 2026-08-19 05:50 UTC | 1h 4m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-08-19 05:10 UTC | 2026-08-19 05:49 UTC | 38m |
| AMU668 | AMU | Macau International Airport (VMMC) | Kaohsiung International Airport (RCKH) | 2026-08-19 04:38 UTC | 2026-08-19 05:48 UTC | 1h 10m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-19 05:25 UTC | 2026-08-19 05:47 UTC | 21m |
| GPMMC | GPM | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-08-19 05:46 UTC | 2026-08-19 05:46 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
