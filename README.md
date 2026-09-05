# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_20:05:40_UTC-green)

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

**Latest saved flight:** 2026-09-05 20:05:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 20:05:40 UTC

- **248,756** saved flights
- **74,873** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,756** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,993,045.2 tonnes** estimated CO2 emissions
- **173,509,864 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9961 |
| 2 | SkyWest Airlines | 8690 |
| 3 | EJA | 4802 |
| 4 | IndiGo | 4153 |
| 5 | American Airlines | 3983 |
| 6 | Southwest Airlines | 3700 |
| 7 | Delta Air Lines | 3156 |
| 8 | ENY | 2974 |
| 9 | LATAM Airlines | 2399 |
| 10 | AZU | 2316 |
| 11 | Vueling | 2122 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1974 |
| 14 | LXJ | 1932 |
| 15 | easyJet | 1718 |
| 16 | Swiss International | 1669 |
| 17 | AXM | 1627 |
| 18 | EJU | 1603 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1561 |
| 21 | Alaska Airlines | 1484 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1409 |
| 24 | GLO | 1388 |
| 25 | VIV | 1366 |
| 26 | PGT | 1364 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1343 |
| 29 | JetBlue | 1225 |
| 30 | AEE | 1223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206354 |
| 2 | 🇪🇸 ES | 15927 |
| 3 | 🇧🇷 BR | 14539 |
| 4 | 🇦🇺 AU | 14105 |
| 5 | 🇨🇦 CA | 13824 |
| 6 | 🇮🇹 IT | 13633 |
| 7 | 🇮🇳 IN | 12951 |
| 8 | 🇩🇪 DE | 12221 |
| 9 | 🇬🇧 GB | 11683 |
| 10 | 🇨🇴 CO | 10883 |
| 11 | 🇫🇷 FR | 10022 |
| 12 | 🇯🇵 JP | 9815 |
| 13 | 🇹🇷 TR | 7413 |
| 14 | 🇬🇷 GR | 7329 |
| 15 | 🇲🇽 MX | 6885 |
| 16 | 🇨🇭 CH | 6709 |
| 17 | 🇳🇴 NO | 6156 |
| 18 | 🇹🇭 TH | 4491 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4160 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3383 |
| 24 | 🇬🇹 GT | 3117 |
| 25 | 🇰🇷 KR | 2886 |
| 26 | 🇭🇷 HR | 2860 |
| 27 | 🇲🇦 MA | 2513 |
| 28 | 🇲🇪 ME | 2331 |
| 29 | 🇳🇱 NL | 2238 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5123 |
| 2 | Denver International Airport |  | US | 4020 |
| 3 | Indira Gandhi International Airport |  | IN | 3026 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2726 |
| 6 | Harry Reid International Airport |  | US | 2651 |
| 7 | Zurich Airport |  | CH | 2604 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2528 |
| 9 | El Dorado International Airport |  | CO | 2497 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2471 |
| 11 | La Aurora Airport |  | GT | 2374 |
| 12 | Salt Lake City International Airport |  | US | 2206 |
| 13 | Chicago O'Hare International Airport |  | US | 2180 |
| 14 | Congonhas Airport |  | BR | 2138 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2051 |
| 16 | Capua Airport |  | IT | 1960 |
| 17 | Madrid Barajas International Airport |  | ES | 1955 |
| 18 | Frankfurt am Main International Airport |  | DE | 1945 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1869 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1789 |
| 22 | Charles de Gaulle International Airport |  | FR | 1747 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1647 |
| 26 | Macau International Airport |  | MO | 1639 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1636 |
| 28 | Charlotte/Douglas International Airport |  | US | 1575 |
| 29 | Barcelona International Airport |  | ES | 1574 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1527 |
| 32 | Viracopos International Airport |  | BR | 1484 |
| 33 | Seattle-Tacoma International Airport |  | US | 1463 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1447 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1431 |
| 37 | Bengaluru International Airport |  | IN | 1429 |
| 38 | Oslo Gardermoen Airport |  | NO | 1398 |
| 39 | Vancouver International Airport |  | CA | 1390 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1349 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1101 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 924 | 21m | 244 km | 3,890.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 558 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 370 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 297 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 285 | 19m | 144 km | 708.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-05 19:21 UTC | 2026-09-05 20:05 UTC | 44m |
| AFR1414 | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-09-05 19:16 UTC | 2026-09-05 20:04 UTC | 48m |
| IBE0699 | Iberia | Madrid Barajas International Airport (LEMD) | Olbia / Costa Smeralda Airport (LIEO) | 2026-09-05 18:34 UTC | 2026-09-05 20:02 UTC | 1h 27m |
| MNB8187 | MNB | Chhatrapati Shivaji International Airport (VABB) | Zhuhai Airport (ZGSD) | 2026-09-05 14:45 UTC | 2026-09-05 20:01 UTC | 5h 15m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-05 19:48 UTC | 2026-09-05 19:59 UTC | 10m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-05 05:55 UTC | 2026-09-05 19:58 UTC | 14h 3m |
| N87WS |  | Henderson Executive Airport (KHND) | Lincoln County Airport (K1L1) | 2026-09-05 19:24 UTC | 2026-09-05 19:51 UTC | 26m |
| QTR8022 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-05 12:00 UTC | 2026-09-05 19:51 UTC | 7h 50m |
| N394LE |  | 6PA6 (6PA6) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-05 19:08 UTC | 2026-09-05 19:44 UTC | 35m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-05 16:45 UTC | 2026-09-05 19:37 UTC | 2h 51m |
| TIBEZ | TIB | Juan Santamaria International Airport (MROC) | Tobias Bolanos International Airport (MRPV) | 2026-09-05 19:23 UTC | 2026-09-05 19:36 UTC | 13m |
| N694DA |  | Fort Morgan Municipal Airport (KFMM) | Fort Morgan Municipal Airport (KFMM) | 2026-09-05 19:20 UTC | 2026-09-05 19:33 UTC | 13m |
| EJA276 | EJA | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-05 18:14 UTC | 2026-09-05 19:32 UTC | 1h 17m |
| N787FA |  | Oxnard Airport (KOXR) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-05 17:52 UTC | 2026-09-05 19:28 UTC | 1h 35m |
| N372TW |  | Culley Acres Airport (3IN9) | 99IN (99IN) | 2026-09-05 19:13 UTC | 2026-09-05 19:23 UTC | 9m |
| ANE80FD | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-09-05 18:43 UTC | 2026-09-05 19:22 UTC | 38m |
| N207NX |  | Cortez Municipal Airport (KCEZ) | Durango-La Plata County Airport (KDRO) | 2026-09-05 19:05 UTC | 2026-09-05 19:20 UTC | 14m |
| HOTT2 | HOT | San Carlos Apache Airport (KP13) | Phoenix Sky Harbor International Airport (KPHX) | 2026-09-05 19:03 UTC | 2026-09-05 19:19 UTC | 16m |
| PTR2373 | PTR | Ottawa / Macdonald-Cartier International Airport (CYOW) | Havelock Airport (CCS5) | 2026-09-05 18:00 UTC | 2026-09-05 19:19 UTC | 1h 18m |
| N453F |  | Martin State Airport (KMTN) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-09-05 17:16 UTC | 2026-09-05 19:17 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
