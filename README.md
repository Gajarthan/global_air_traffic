# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_05:17:40_UTC-green)

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

**Latest saved flight:** 2026-08-11 05:17:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 05:17:40 UTC

- **185,919** saved flights
- **59,030** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,919** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,230,610.9 tonnes** estimated CO2 emissions
- **129,310,776 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7354 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3676 |
| 4 | IndiGo | 3242 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2901 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2192 |
| 9 | LATAM Airlines | 1739 |
| 10 | AZU | 1671 |
| 11 | Lufthansa | 1628 |
| 12 | WIF | 1533 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1459 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1242 |
| 18 | EJU | 1146 |
| 19 | QLK | 1145 |
| 20 | All Nippon Airways | 1138 |
| 21 | Alaska Airlines | 1116 |
| 22 | VIV | 1026 |
| 23 | GLO | 997 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | United Airlines | 950 |
| 28 | PGT | 948 |
| 29 | Cathay Pacific | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159054 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10675 |
| 4 | 🇦🇺 AU | 10390 |
| 5 | 🇮🇳 IN | 10164 |
| 6 | 🇨🇦 CA | 10162 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9155 |
| 9 | 🇬🇧 GB | 8608 |
| 10 | 🇯🇵 JP | 7575 |
| 11 | 🇫🇷 FR | 7406 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5439 |
| 14 | 🇲🇽 MX | 5313 |
| 15 | 🇨🇭 CH | 4950 |
| 16 | 🇹🇷 TR | 4874 |
| 17 | 🇳🇴 NO | 4763 |
| 18 | 🇲🇾 MY | 3240 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3093 |
| 21 | 🇹🇭 TH | 2878 |
| 22 | 🇳🇿 NZ | 2656 |
| 23 | 🇵🇭 PH | 2452 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2302 |
| 26 | 🇲🇦 MA | 1879 |
| 27 | 🇭🇷 HR | 1866 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3865 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2346 |
| 4 | Indira Gandhi International Airport |  | IN | 2284 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2182 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1597 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1329 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1297 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1266 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1214 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1164 |
| 30 | Ninoy Aquino International Airport |  | PH | 1157 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1142 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Reno/Tahoe International Airport |  | US | 1073 |
| 34 | Seattle-Tacoma International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 449 | 1h 7m | 770 km | 5,964.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 431 | 24m | 225 km | 1,672.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 263 | 1h 49m | 1,423 km | 6,454.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 221 | 1h 38m | 1,156 km | 4,408.9 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 217 | 31m | 369 km | 1,381.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BLINR17 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-11 03:28 UTC | 2026-08-11 05:17 UTC | 1h 49m |
| A7GQA |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-11 04:27 UTC | 2026-08-11 05:12 UTC | 44m |
| J981G |  | Adi Sutjipto International Airport (WARJ) | Adi Sutjipto International Airport (WARJ) | 2026-08-11 05:02 UTC | 2026-08-11 05:06 UTC | 4m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-08-11 04:45 UTC | 2026-08-11 05:04 UTC | 19m |
| TROJ57 | TRO | RAAF Base Richmond (YSRI) | Kelvin Station Airport (YKEL) | 2026-08-11 04:24 UTC | 2026-08-11 05:04 UTC | 40m |
| DAL565 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Seattle-Tacoma International Airport (KSEA) | 2026-08-11 00:23 UTC | 2026-08-11 05:04 UTC | 4h 41m |
| HBZUZ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-11 04:53 UTC | 2026-08-11 05:00 UTC | 7m |
| ASA424 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-11 01:32 UTC | 2026-08-11 04:53 UTC | 3h 20m |
| FIN9KC | Finnair | Helsinki Vantaa Airport (EFHK) | Khrabrovo Airport (UMKK) | 2026-08-11 04:19 UTC | 2026-08-11 04:51 UTC | 31m |
| RAM272C | Royal Air Maroc | Mohammed V International Airport (GMMN) | HE42 (HE42) | 2026-08-11 00:26 UTC | 2026-08-11 04:51 UTC | 4h 24m |
| A7GQE |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-08-11 04:23 UTC | 2026-08-11 04:45 UTC | 22m |
| INTEL12 | INT | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-08-11 04:38 UTC | 2026-08-11 04:44 UTC | 5m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-11 02:53 UTC | 2026-08-11 04:39 UTC | 1h 46m |
| N54983 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-08-11 04:19 UTC | 2026-08-11 04:32 UTC | 13m |
| SIS49 | SIS | Northwest Arkansas Ntl Airport (KXNA) | San Francisco International Airport (KSFO) | 2026-08-11 01:17 UTC | 2026-08-11 04:32 UTC | 3h 14m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-11 04:15 UTC | 2026-08-11 04:31 UTC | 15m |
| AM318 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-08-11 04:10 UTC | 2026-08-11 04:30 UTC | 20m |
| ZHJ | ZHJ | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-11 04:08 UTC | 2026-08-11 04:30 UTC | 22m |
| A7GQB |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-11 02:26 UTC | 2026-08-11 04:26 UTC | 2h 0m |
| NVD | NVD | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-11 04:14 UTC | 2026-08-11 04:26 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
