# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_05:40:36_UTC-green)

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

**Latest saved flight:** 2026-08-14 05:40:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 05:40:36 UTC

- **194,344** saved flights
- **61,138** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **194,344** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,322,277.4 tonnes** estimated CO2 emissions
- **134,624,779 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7712 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3834 |
| 4 | IndiGo | 3349 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3014 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1825 |
| 10 | AZU | 1752 |
| 11 | Lufthansa | 1673 |
| 12 | Vueling | 1615 |
| 13 | WIF | 1604 |
| 14 | LXJ | 1541 |
| 15 | easyJet | 1337 |
| 16 | Swiss International | 1316 |
| 17 | AXM | 1262 |
| 18 | QLK | 1197 |
| 19 | EJU | 1193 |
| 20 | All Nippon Airways | 1179 |
| 21 | Alaska Airlines | 1155 |
| 22 | VIV | 1071 |
| 23 | GLO | 1046 |
| 24 | Air France | 1011 |
| 25 | PGT | 1011 |
| 26 | United Airlines | 994 |
| 27 | AEE | 992 |
| 28 | CXK | 989 |
| 29 | WMT | 965 |
| 30 | Wizz Air | 962 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165657 |
| 2 | 🇪🇸 ES | 12506 |
| 3 | 🇧🇷 BR | 11177 |
| 4 | 🇦🇺 AU | 10936 |
| 5 | 🇨🇦 CA | 10653 |
| 6 | 🇮🇳 IN | 10484 |
| 7 | 🇮🇹 IT | 10083 |
| 8 | 🇩🇪 DE | 9590 |
| 9 | 🇬🇧 GB | 9070 |
| 10 | 🇯🇵 JP | 7927 |
| 11 | 🇫🇷 FR | 7732 |
| 12 | 🇨🇴 CO | 7569 |
| 13 | 🇬🇷 GR | 5680 |
| 14 | 🇲🇽 MX | 5509 |
| 15 | 🇹🇷 TR | 5245 |
| 16 | 🇨🇭 CH | 5210 |
| 17 | 🇳🇴 NO | 4965 |
| 18 | 🇲🇾 MY | 3308 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3190 |
| 21 | 🇹🇭 TH | 3008 |
| 22 | 🇳🇿 NZ | 2734 |
| 23 | 🇵🇭 PH | 2566 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2359 |
| 26 | 🇭🇷 HR | 2012 |
| 27 | 🇲🇦 MA | 1970 |
| 28 | 🇳🇱 NL | 1742 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1562 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4052 |
| 2 | Denver International Airport |  | US | 3183 |
| 3 | Tokyo International Airport |  | JP | 2436 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2363 |
| 6 | Harry Reid International Airport |  | US | 2249 |
| 7 | Zurich Airport |  | CH | 2055 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2049 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1774 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1640 |
| 16 | Congonhas Airport |  | BR | 1627 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1527 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 20 | Capua Airport |  | IT | 1492 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1436 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1396 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1356 |
| 24 | Malpensa International Airport |  | IT | 1344 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1237 |
| 28 | Kuala Lumpur International Airport |  | MY | 1234 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 30 | Ninoy Aquino International Airport |  | PH | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1196 |
| 32 | Barcelona International Airport |  | ES | 1161 |
| 33 | Viracopos International Airport |  | BR | 1128 |
| 34 | Seattle-Tacoma International Airport |  | US | 1119 |
| 35 | Calgary International Airport |  | CA | 1111 |
| 36 | Reno/Tahoe International Airport |  | US | 1103 |
| 37 | Oslo Gardermoen Airport |  | NO | 1088 |
| 38 | Daniel K Inouye International Airport |  | US | 1085 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 713 | 21m | 244 km | 3,002.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 471 | 1h 7m | 770 km | 6,256.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 450 | 24m | 225 km | 1,745.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 289 | 44m | 241 km | 1,200.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 238 | 24m | 218 km | 896.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 228 | 1h 38m | 1,156 km | 4,548.5 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 221 | 31m | 369 km | 1,406.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL1558 | United Airlines | Newark Liberty International Airport (KEWR) | San Francisco International Airport (KSFO) | 2026-08-14 00:09 UTC | 2026-08-14 05:40 UTC | 5h 31m |
| VAR425 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-14 04:55 UTC | 2026-08-14 05:32 UTC | 36m |
| EQF | EQF | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-14 04:39 UTC | 2026-08-14 05:28 UTC | 49m |
| FR120 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-14 05:19 UTC | 2026-08-14 05:27 UTC | 7m |
| NJZ196 | NJZ | John Wayne/Orange County Airport (KSNA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-14 04:28 UTC | 2026-08-14 05:21 UTC | 53m |
| LBQ650 | LBQ | Reading Regional/Carl A Spaatz Field (KRDG) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-14 03:12 UTC | 2026-08-14 05:16 UTC | 2h 3m |
| VLG960 | Vueling | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-08-14 03:54 UTC | 2026-08-14 05:04 UTC | 1h 10m |
| VLW | VLW | Cessnock Airport (YCNK) | Dunmore Manila Airport (YDNR) | 2026-08-14 04:14 UTC | 2026-08-14 05:00 UTC | 45m |
| EFC30M | EFC | Al Maktoum International Airport (OMDW) | Al Minhad Air Base (OMDM) | 2026-08-14 04:05 UTC | 2026-08-14 04:58 UTC | 53m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-08-14 04:37 UTC | 2026-08-14 04:57 UTC | 19m |
| LFT05 | LFT | Hamilton International Airport (NZHN) | Whakatane Airport (NZWK) | 2026-08-14 04:28 UTC | 2026-08-14 04:55 UTC | 26m |
| AIQ3923 | AIQ | Don Mueang International Airport (VTBD) | Khunan Phumipol Airport (VTPY) | 2026-08-14 04:19 UTC | 2026-08-14 04:54 UTC | 34m |
| N40200 |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-08-14 03:16 UTC | 2026-08-14 04:49 UTC | 1h 32m |
| NPN | NPN | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-14 04:07 UTC | 2026-08-14 04:48 UTC | 41m |
| OCN1000 | OCN | Frankfurt am Main International Airport (EDDF) | Munich International Airport (EDDM) | 2026-08-14 04:11 UTC | 2026-08-14 04:47 UTC | 35m |
| ANA1607 | All Nippon Airways | Osaka International Airport (RJOO) | Tokushima Airport (RJOS) | 2026-08-14 04:32 UTC | 2026-08-14 04:46 UTC | 14m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-13 17:35 UTC | 2026-08-14 04:45 UTC | 11h 9m |
| KFB825 | KFB | John Wayne/Orange County Airport (KSNA) | Westwater Airport (UT42) | 2026-08-14 03:33 UTC | 2026-08-14 04:43 UTC | 1h 9m |
|  |  | Delaurentis Airport (KOKH) | Shelby Airport (KSBX) | 2026-08-14 03:34 UTC | 2026-08-14 04:43 UTC | 1h 9m |
| WMT5843 | WMT | Henri Coanda International Airport (LROP) | Mikonos Airport (LGMK) | 2026-08-14 03:25 UTC | 2026-08-14 04:42 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
