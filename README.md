# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_18:27:19_UTC-green)

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

**Latest saved flight:** 2026-08-12 18:27:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 18:27:19 UTC

- **190,260** saved flights
- **60,092** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,260** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,277,732.6 tonnes** estimated CO2 emissions
- **132,042,473 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7541 |
| 2 | SkyWest Airlines | 6887 |
| 3 | EJA | 3754 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2973 |
| 6 | American Airlines | 2947 |
| 7 | ENY | 2355 |
| 8 | Delta Air Lines | 2231 |
| 9 | LATAM Airlines | 1784 |
| 10 | AZU | 1716 |
| 11 | Lufthansa | 1658 |
| 12 | Vueling | 1581 |
| 13 | WIF | 1579 |
| 14 | LXJ | 1488 |
| 15 | easyJet | 1312 |
| 16 | Swiss International | 1298 |
| 17 | AXM | 1253 |
| 18 | EJU | 1176 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1133 |
| 22 | VIV | 1049 |
| 23 | GLO | 1027 |
| 24 | Air France | 994 |
| 25 | PGT | 982 |
| 26 | United Airlines | 974 |
| 27 | AEE | 973 |
| 28 | CXK | 972 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 945 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162093 |
| 2 | 🇪🇸 ES | 12270 |
| 3 | 🇧🇷 BR | 10942 |
| 4 | 🇦🇺 AU | 10658 |
| 5 | 🇨🇦 CA | 10431 |
| 6 | 🇮🇳 IN | 10368 |
| 7 | 🇮🇹 IT | 9878 |
| 8 | 🇩🇪 DE | 9413 |
| 9 | 🇬🇧 GB | 8859 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7619 |
| 12 | 🇨🇴 CO | 7301 |
| 13 | 🇬🇷 GR | 5568 |
| 14 | 🇲🇽 MX | 5396 |
| 15 | 🇨🇭 CH | 5105 |
| 16 | 🇹🇷 TR | 5063 |
| 17 | 🇳🇴 NO | 4901 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3209 |
| 20 | 🇵🇱 PL | 3147 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2408 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1951 |
| 27 | 🇲🇦 MA | 1928 |
| 28 | 🇳🇱 NL | 1699 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3944 |
| 2 | Denver International Airport |  | US | 3126 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2349 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2219 |
| 7 | Zurich Airport |  | CH | 2022 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2013 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1967 |
| 10 | La Aurora Airport |  | GT | 1852 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1719 |
| 12 | El Dorado International Airport |  | CO | 1716 |
| 13 | Salt Lake City International Airport |  | US | 1685 |
| 14 | Chicago O'Hare International Airport |  | US | 1663 |
| 15 | Frankfurt am Main International Airport |  | DE | 1625 |
| 16 | Congonhas Airport |  | BR | 1589 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1500 |
| 19 | Capua Airport |  | IT | 1475 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1474 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1403 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1367 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1313 |
| 25 | Charles de Gaulle International Airport |  | FR | 1304 |
| 26 | Charlotte/Douglas International Airport |  | US | 1274 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1189 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1167 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1103 |
| 34 | Reno/Tahoe International Airport |  | US | 1095 |
| 35 | Seattle-Tacoma International Airport |  | US | 1092 |
| 36 | Calgary International Airport |  | CA | 1086 |
| 37 | Daniel K Inouye International Airport |  | US | 1068 |
| 38 | Oslo Gardermoen Airport |  | NO | 1063 |
| 39 | Tenerife Norte Airport |  | ES | 1043 |
| 40 | Vitoria/Foronda Airport |  | ES | 1031 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 970 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 696 | 21m | 244 km | 2,930.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 443 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 319 | 27m | 275 km | 1,511.6 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 299 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 255 | 20m | 250 km | 1,101.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 238 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 227 | 19m | 144 km | 564.7 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 226 | 24m | 218 km | 851.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 207 | 1h 48m | 1,304 km | 4,657.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8903C |  | Felts Field (KSFF) | Lewiston/Nez Perce County Airport (KLWS) | 2026-08-12 17:31 UTC | 2026-08-12 18:27 UTC | 55m |
| TAP217C | TAP Air Portugal | Lisbon Portela Airport (LPPT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-12 11:22 UTC | 2026-08-12 18:27 UTC | 7h 5m |
| DAL277 | Delta Air Lines | Nice-Cote d'Azur Airport (LFMN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-12 10:35 UTC | 2026-08-12 18:25 UTC | 7h 49m |
| PHJMM | PHJ | Vilseck Army Air Field (ETOI) | Vilseck Army Air Field (ETOI) | 2026-08-12 17:56 UTC | 2026-08-12 18:25 UTC | 28m |
| DKLCT | DKL | Altdorf-Wallburg Airport (EDSW) | Altdorf-Wallburg Airport (EDSW) | 2026-08-12 17:55 UTC | 2026-08-12 18:24 UTC | 29m |
| EXS8T | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 17:36 UTC | 2026-08-12 18:23 UTC | 47m |
| N115GK |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-08-12 17:59 UTC | 2026-08-12 18:22 UTC | 23m |
| N605T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-12 17:47 UTC | 2026-08-12 18:22 UTC | 34m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-12 17:59 UTC | 2026-08-12 18:17 UTC | 17m |
| N3134J |  | Winterset Municipal Airport (K3Y3) | Winterset Municipal Airport (K3Y3) | 2026-08-12 17:43 UTC | 2026-08-12 18:14 UTC | 30m |
| N118JK |  | Tehachapi Municipal Airport (KTSP) | Meadows Field (KBFL) | 2026-08-12 18:02 UTC | 2026-08-12 18:14 UTC | 12m |
| N1416W |  | Gainesville Regional Airport (KGNV) | 8FD2 (8FD2) | 2026-08-12 17:37 UTC | 2026-08-12 18:13 UTC | 35m |
| N738BG |  | Burlington/Alamance Regional Airport (KBUY) | Burlington/Alamance Regional Airport (KBUY) | 2026-08-12 17:33 UTC | 2026-08-12 18:12 UTC | 38m |
| N384ME |  | San Carlos Airport (KSQL) | Franklin Field (KF72) | 2026-08-12 17:33 UTC | 2026-08-12 18:10 UTC | 37m |
| N9145G |  | Corona Municipal Airport (KAJO) | Big Bear City Airport (KL35) | 2026-08-12 17:45 UTC | 2026-08-12 18:09 UTC | 23m |
| ROU1997 | ROU | Toronto Pearson International Airport (CYYZ) | Vernon Airport (CYVK) | 2026-08-12 13:20 UTC | 2026-08-12 18:08 UTC | 4h 47m |
| N2777E |  | Corona Municipal Airport (KAJO) | Corona Municipal Airport (KAJO) | 2026-08-12 17:37 UTC | 2026-08-12 18:08 UTC | 30m |
| N5373T |  | K4A7 (K4A7) | K4A7 (K4A7) | 2026-08-12 17:28 UTC | 2026-08-12 18:07 UTC | 39m |
| AMF8002 | AMF | Rogue Valley International/Medford Airport (KMFR) | Illinois Valley Airport (K3S4) | 2026-08-12 17:33 UTC | 2026-08-12 18:05 UTC | 32m |
| N5196P |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-08-12 17:26 UTC | 2026-08-12 18:05 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
