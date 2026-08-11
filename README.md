# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_23:18:00_UTC-green)

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

**Latest saved flight:** 2026-08-11 23:18:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 23:18:00 UTC

- **188,322** saved flights
- **59,631** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,322** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,258,084.3 tonnes** estimated CO2 emissions
- **130,903,437 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7478 |
| 2 | SkyWest Airlines | 6851 |
| 3 | EJA | 3719 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2950 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2341 |
| 8 | Delta Air Lines | 2216 |
| 9 | LATAM Airlines | 1761 |
| 10 | AZU | 1697 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1564 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1476 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1156 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1125 |
| 22 | VIV | 1043 |
| 23 | GLO | 1017 |
| 24 | Air France | 978 |
| 25 | AEE | 969 |
| 26 | PGT | 966 |
| 27 | United Airlines | 966 |
| 28 | CXK | 965 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160806 |
| 2 | 🇪🇸 ES | 12134 |
| 3 | 🇧🇷 BR | 10829 |
| 4 | 🇦🇺 AU | 10496 |
| 5 | 🇨🇦 CA | 10316 |
| 6 | 🇮🇳 IN | 10266 |
| 7 | 🇮🇹 IT | 9760 |
| 8 | 🇩🇪 DE | 9299 |
| 9 | 🇬🇧 GB | 8758 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7528 |
| 12 | 🇨🇴 CO | 7170 |
| 13 | 🇬🇷 GR | 5518 |
| 14 | 🇲🇽 MX | 5374 |
| 15 | 🇨🇭 CH | 5033 |
| 16 | 🇹🇷 TR | 4982 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3120 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2678 |
| 23 | 🇵🇭 PH | 2481 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2315 |
| 26 | 🇲🇦 MA | 1915 |
| 27 | 🇭🇷 HR | 1910 |
| 28 | 🇲🇪 ME | 1685 |
| 29 | 🇳🇱 NL | 1677 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3921 |
| 2 | Denver International Airport |  | US | 3109 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Guaymaral Airport |  | CO | 2312 |
| 5 | Indira Gandhi International Airport |  | IN | 2311 |
| 6 | Harry Reid International Airport |  | US | 2206 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 8 | Zurich Airport |  | CH | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1953 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1710 |
| 12 | El Dorado International Airport |  | CO | 1696 |
| 13 | Salt Lake City International Airport |  | US | 1676 |
| 14 | Chicago O'Hare International Airport |  | US | 1660 |
| 15 | Frankfurt am Main International Airport |  | DE | 1616 |
| 16 | Congonhas Airport |  | BR | 1574 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1463 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1396 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1182 |
| 30 | Ninoy Aquino International Airport |  | PH | 1171 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1160 |
| 32 | Barcelona International Airport |  | ES | 1128 |
| 33 | Reno/Tahoe International Airport |  | US | 1091 |
| 34 | Viracopos International Airport |  | BR | 1089 |
| 35 | Seattle-Tacoma International Airport |  | US | 1086 |
| 36 | Calgary International Airport |  | CA | 1072 |
| 37 | Daniel K Inouye International Airport |  | US | 1060 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 688 | 21m | 244 km | 2,897.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 316 | 27m | 275 km | 1,497.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 306 | 14m | 114 km | 600.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 232 | 50m | 556 km | 2,223.9 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 231 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 224 | 19m | 144 km | 557.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 205 | 1h 49m | 1,304 km | 4,612.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR912 | TKR | Mc Clellan Airfield (KMCC) | NV17 (NV17) | 2026-08-11 22:53 UTC | 2026-08-11 23:18 UTC | 24m |
| N454NC |  | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-11 23:03 UTC | 2026-08-11 23:16 UTC | 12m |
| TKR910 | TKR | Mc Clellan Airfield (KMCC) | NV17 (NV17) | 2026-08-11 22:54 UTC | 2026-08-11 23:12 UTC | 17m |
| COBRA74 | COB | Mojave Air & Space Port/Rutan Field (KMHV) | Edwards Af Aux North Base Airport (K9L2) | 2026-08-11 22:21 UTC | 2026-08-11 23:09 UTC | 47m |
| PNC0926 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-11 22:22 UTC | 2026-08-11 23:06 UTC | 44m |
| N2334J |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-11 22:53 UTC | 2026-08-11 23:06 UTC | 12m |
| ASA521 | Alaska Airlines | Norman Y Mineta San Jose International Airport (KSJC) | Seattle-Tacoma International Airport (KSEA) | 2026-08-11 21:30 UTC | 2026-08-11 23:05 UTC | 1h 35m |
| BOE494 | BOE | Seattle Paine Field International Airport (KPAE) | Franz Ranch Airport (33WA) | 2026-08-11 21:36 UTC | 2026-08-11 23:05 UTC | 1h 29m |
| WSN530 | WSN | Oakland San Francisco Bay Airport (KOAK) | California Redwood Coast-Humboldt County Airport (KACV) | 2026-08-11 22:16 UTC | 2026-08-11 22:49 UTC | 32m |
| DZR355 | DZR | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-08-11 22:12 UTC | 2026-08-11 22:40 UTC | 27m |
| R20658 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-11 21:34 UTC | 2026-08-11 22:37 UTC | 1h 2m |
| N7091G |  | Hartford-Brainard Airport (KHFD) | New Bedford Regional Airport (KEWB) | 2026-08-11 21:52 UTC | 2026-08-11 22:34 UTC | 42m |
| EJA651 | EJA | Blue Grass Airport (KLEX) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-11 22:05 UTC | 2026-08-11 22:32 UTC | 27m |
| N60HL |  | Marv Skie-Lincoln County Airport (KY14) | Westerlind Airport (2ND1) | 2026-08-11 21:07 UTC | 2026-08-11 22:32 UTC | 1h 25m |
| VTE3390 | VTE | Phoenix Sky Harbor International Airport (KPHX) | UT09 (UT09) | 2026-08-11 21:29 UTC | 2026-08-11 22:30 UTC | 1h 1m |
| N480K |  | New Farm Airport (NV47) | New Farm Airport (NV47) | 2026-08-11 22:09 UTC | 2026-08-11 22:30 UTC | 20m |
| N835DH |  | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-11 22:27 UTC | 2026-08-11 22:29 UTC | 2m |
| MAFFS4 | MAF | Mc Clellan Airfield (KMCC) | NV44 (NV44) | 2026-08-11 22:02 UTC | 2026-08-11 22:29 UTC | 26m |
| VTE3552 | VTE | Dallas-Fort Worth International Airport (KDFW) | Wells Airport (MO85) | 2026-08-11 21:32 UTC | 2026-08-11 22:28 UTC | 56m |
| FFAB123 | FFA | Eagle Ridge Ranch Airport (6CA6) | Lake Tahoe Airport (KTVL) | 2026-08-11 22:10 UTC | 2026-08-11 22:25 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
