# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_16:59:41_UTC-green)

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

**Latest saved flight:** 2026-08-13 16:59:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 16:59:41 UTC

- **192,828** saved flights
- **60,702** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **192,828** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,305,520.3 tonnes** estimated CO2 emissions
- **133,653,349 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7674 |
| 2 | SkyWest Airlines | 6953 |
| 3 | EJA | 3791 |
| 4 | IndiGo | 3341 |
| 5 | Southwest Airlines | 3002 |
| 6 | American Airlines | 2984 |
| 7 | ENY | 2386 |
| 8 | Delta Air Lines | 2276 |
| 9 | LATAM Airlines | 1809 |
| 10 | AZU | 1739 |
| 11 | Lufthansa | 1671 |
| 12 | Vueling | 1606 |
| 13 | WIF | 1598 |
| 14 | LXJ | 1520 |
| 15 | easyJet | 1328 |
| 16 | Swiss International | 1312 |
| 17 | AXM | 1258 |
| 18 | EJU | 1189 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1060 |
| 23 | GLO | 1036 |
| 24 | Air France | 1009 |
| 25 | PGT | 1000 |
| 26 | CXK | 988 |
| 27 | AEE | 987 |
| 28 | United Airlines | 980 |
| 29 | WMT | 958 |
| 30 | Wizz Air | 957 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 164057 |
| 2 | 🇪🇸 ES | 12446 |
| 3 | 🇧🇷 BR | 11077 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10553 |
| 6 | 🇮🇳 IN | 10463 |
| 7 | 🇮🇹 IT | 10029 |
| 8 | 🇩🇪 DE | 9554 |
| 9 | 🇬🇧 GB | 9030 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7712 |
| 12 | 🇨🇴 CO | 7465 |
| 13 | 🇬🇷 GR | 5645 |
| 14 | 🇲🇽 MX | 5445 |
| 15 | 🇨🇭 CH | 5198 |
| 16 | 🇹🇷 TR | 5184 |
| 17 | 🇳🇴 NO | 4954 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3181 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2447 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 1996 |
| 27 | 🇲🇦 MA | 1959 |
| 28 | 🇳🇱 NL | 1733 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3998 |
| 2 | Denver International Airport |  | US | 3156 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2395 |
| 5 | Indira Gandhi International Airport |  | IN | 2358 |
| 6 | Harry Reid International Airport |  | US | 2237 |
| 7 | Zurich Airport |  | CH | 2047 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2038 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1991 |
| 10 | La Aurora Airport |  | GT | 1880 |
| 11 | El Dorado International Airport |  | CO | 1751 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1733 |
| 13 | Salt Lake City International Airport |  | US | 1715 |
| 14 | Chicago O'Hare International Airport |  | US | 1687 |
| 15 | Frankfurt am Main International Airport |  | DE | 1637 |
| 16 | Congonhas Airport |  | BR | 1612 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1520 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1485 |
| 20 | Capua Airport |  | IT | 1484 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1425 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1383 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1332 |
| 25 | Charles de Gaulle International Airport |  | FR | 1324 |
| 26 | Charlotte/Douglas International Airport |  | US | 1282 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1203 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1179 |
| 32 | Barcelona International Airport |  | ES | 1153 |
| 33 | Viracopos International Airport |  | BR | 1119 |
| 34 | Seattle-Tacoma International Airport |  | US | 1106 |
| 35 | Calgary International Airport |  | CA | 1102 |
| 36 | Reno/Tahoe International Airport |  | US | 1101 |
| 37 | Oslo Gardermoen Airport |  | NO | 1084 |
| 38 | Daniel K Inouye International Airport |  | US | 1080 |
| 39 | Tenerife Norte Airport |  | ES | 1060 |
| 40 | Vitoria/Foronda Airport |  | ES | 1054 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 990 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 708 | 21m | 244 km | 2,981.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 450 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 324 | 27m | 275 km | 1,535.3 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 311 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 288 | 44m | 241 km | 1,196.3 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 241 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 235 | 24m | 218 km | 885.3 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 209 | 28m | 152 km | 546.2 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 1m | 695 km | 2,493.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRP4 | TRP | Pokety Airport (3MD8) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-08-13 16:37 UTC | 2026-08-13 16:59 UTC | 22m |
| N9588V |  | Stampede Valley Airport (6TS4) | TS29 (TS29) | 2026-08-13 16:31 UTC | 2026-08-13 16:57 UTC | 26m |
| N513LA |  | Flying J Airport (86TX) | Stinson Municipal Airport (KSSF) | 2026-08-13 16:38 UTC | 2026-08-13 16:54 UTC | 16m |
| ARCAS02 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-08-13 16:31 UTC | 2026-08-13 16:52 UTC | 21m |
|  |  | Winter Haven Regional Airport (KGIF) | Orlampa Inc Airport (FA08) | 2026-08-13 16:44 UTC | 2026-08-13 16:50 UTC | 6m |
| 00000000 |  | Divinopolis Airport (SNDV) | Congonhas Airport (SBSP) | 2026-08-13 16:00 UTC | 2026-08-13 16:46 UTC | 46m |
| VIRAL24 | Virgin Atlantic | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-08-13 16:30 UTC | 2026-08-13 16:43 UTC | 12m |
| XSN82 | XSN | CL36 (CL36) | Truckee-Tahoe Airport (KTRK) | 2026-08-13 16:06 UTC | 2026-08-13 16:38 UTC | 32m |
| LXJ600 | LXJ | San Francisco International Airport (KSFO) | Van Nuys Airport (KVNY) | 2026-08-13 15:40 UTC | 2026-08-13 16:36 UTC | 55m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Jecan Airport (06CO) | 2026-08-13 16:16 UTC | 2026-08-13 16:35 UTC | 18m |
| N9131H |  | Washington Manassas/Harry P Davis Field (KHEF) | Pleasantdale Field (4VA9) | 2026-08-13 16:10 UTC | 2026-08-13 16:34 UTC | 24m |
| N492ND |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-08-13 16:26 UTC | 2026-08-13 16:34 UTC | 8m |
| N708RE |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-08-13 15:27 UTC | 2026-08-13 16:33 UTC | 1h 5m |
| 2CYFR |  | Gloucestershire Airport (EGBJ) | Blackpool International Airport (EGNH) | 2026-08-13 15:37 UTC | 2026-08-13 16:29 UTC | 52m |
| SENTRY2 | SEN | Maryland Airport (K2W5) | Davison Army Air Field (KDAA) | 2026-08-13 16:23 UTC | 2026-08-13 16:27 UTC | 4m |
| N190BM |  | Salt Lake City International Airport (KSLC) | UT99 (UT99) | 2026-08-13 16:00 UTC | 2026-08-13 16:26 UTC | 25m |
| HK5065G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-13 16:18 UTC | 2026-08-13 16:23 UTC | 5m |
| N773MD |  | Phoenix Deer Valley Airport (KDVT) | Cottonwood Airport (KP52) | 2026-08-13 14:37 UTC | 2026-08-13 16:23 UTC | 1h 46m |
| CXK581 | CXK | Austin-Bergstrom International Airport (KAUS) | Taylor Municipal Airport (KT74) | 2026-08-13 15:26 UTC | 2026-08-13 16:23 UTC | 57m |
| EPI271 | EPI | North Texas Regional/Perrin Field (KGYI) | Sandy Creek Ranch Airport (TX47) | 2026-08-13 16:03 UTC | 2026-08-13 16:23 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
