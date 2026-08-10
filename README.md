# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_05:25:10_UTC-green)

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

**Latest saved flight:** 2026-08-10 05:25:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 05:25:10 UTC

- **183,338** saved flights
- **58,477** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,338** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,203,373.4 tonnes** estimated CO2 emissions
- **127,731,792 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7265 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3200 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1716 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1511 |
| 13 | Vueling | 1508 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1255 |
| 16 | Swiss International | 1253 |
| 17 | AXM | 1229 |
| 18 | QLK | 1125 |
| 19 | EJU | 1124 |
| 20 | All Nippon Airways | 1116 |
| 21 | Alaska Airlines | 1103 |
| 22 | VIV | 1012 |
| 23 | GLO | 984 |
| 24 | AEE | 956 |
| 25 | CXK | 953 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 929 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156974 |
| 2 | 🇪🇸 ES | 11755 |
| 3 | 🇧🇷 BR | 10535 |
| 4 | 🇦🇺 AU | 10256 |
| 5 | 🇮🇳 IN | 10020 |
| 6 | 🇨🇦 CA | 9993 |
| 7 | 🇮🇹 IT | 9477 |
| 8 | 🇩🇪 DE | 9061 |
| 9 | 🇬🇧 GB | 8489 |
| 10 | 🇯🇵 JP | 7443 |
| 11 | 🇫🇷 FR | 7285 |
| 12 | 🇨🇴 CO | 6864 |
| 13 | 🇬🇷 GR | 5373 |
| 14 | 🇲🇽 MX | 5248 |
| 15 | 🇨🇭 CH | 4881 |
| 16 | 🇹🇷 TR | 4760 |
| 17 | 🇳🇴 NO | 4699 |
| 18 | 🇲🇾 MY | 3203 |
| 19 | 🇵🇱 PL | 3068 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2822 |
| 22 | 🇳🇿 NZ | 2627 |
| 23 | 🇵🇭 PH | 2427 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2276 |
| 26 | 🇲🇦 MA | 1852 |
| 27 | 🇭🇷 HR | 1828 |
| 28 | 🇲🇪 ME | 1651 |
| 29 | 🇳🇱 NL | 1643 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2306 |
| 4 | Indira Gandhi International Airport |  | IN | 2240 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2148 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1965 |
| 8 | Zurich Airport |  | CH | 1954 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1645 |
| 13 | Salt Lake City International Airport |  | US | 1638 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1438 |
| 20 | Capua Airport |  | IT | 1435 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1280 |
| 24 | Malpensa International Airport |  | IT | 1267 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1202 |
| 28 | Bengaluru International Airport |  | IN | 1189 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1148 |
| 30 | Ninoy Aquino International Airport |  | PH | 1144 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Calgary International Airport |  | CA | 1046 |
| 37 | Daniel K Inouye International Airport |  | US | 1045 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 1000 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 673 | 21m | 244 km | 2,833.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 435 | 1h 8m | 770 km | 5,778.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 230 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 213 | 31m | 369 km | 1,355.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-08-10 05:00 UTC | 2026-08-10 05:25 UTC | 24m |
| N339CA |  | Lizzy Lizard Airport (8AZ5) | Bisbee Douglas International Airport (KDUG) | 2026-08-10 04:34 UTC | 2026-08-10 05:10 UTC | 35m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-08-10 04:28 UTC | 2026-08-10 05:09 UTC | 40m |
| RYR13KA | Ryanair | Torino / Caselle International Airport (LIMF) | Decimomannu Airport (LIED) | 2026-08-10 04:11 UTC | 2026-08-10 05:05 UTC | 54m |
| RAM272C | Royal Air Maroc | Mohammed V International Airport (GMMN) | HE42 (HE42) | 2026-08-10 00:27 UTC | 2026-08-10 04:58 UTC | 4h 30m |
| BH772 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-10 04:47 UTC | 2026-08-10 04:58 UTC | 10m |
| N214NX |  | Aurora State Airport (KUAO) | 2ID7 (2ID7) | 2026-08-10 03:36 UTC | 2026-08-10 04:56 UTC | 1h 19m |
| SNJ15 | SNJ | Tokyo International Airport (RJTT) | Kumamoto Airport (RJFT) | 2026-08-10 03:42 UTC | 2026-08-10 04:52 UTC | 1h 9m |
| RYR5RT | Ryanair | Bari / Palese International Airport (LIBD) | Ohrid St. Paul the Apostle Airport (LWOH) | 2026-08-10 04:25 UTC | 2026-08-10 04:47 UTC | 21m |
| SWR2EY | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-08-10 04:14 UTC | 2026-08-10 04:45 UTC | 30m |
| FRS143 | FRS | Al Ain International Airport (OMAL) | Lekhwair Airport (OOLK) | 2026-08-10 04:28 UTC | 2026-08-10 04:44 UTC | 16m |
| WMT5843 | WMT | Henri Coanda International Airport (LROP) | Santorini Airport (LGSR) | 2026-08-10 03:28 UTC | 2026-08-10 04:44 UTC | 1h 16m |
| CRABA | CRA | Kamphaeng Saen Airport (VTBK) | Photharam Airport (VTPR) | 2026-08-10 04:11 UTC | 2026-08-10 04:42 UTC | 30m |
| EFC65D | EFC | Ras Al Khaimah International Airport (OMRK) | Ras Al Khaimah International Airport (OMRK) | 2026-08-10 04:29 UTC | 2026-08-10 04:42 UTC | 12m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-08-10 04:24 UTC | 2026-08-10 04:41 UTC | 16m |
| FLJ63T | FLJ | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-08-10 04:15 UTC | 2026-08-10 04:39 UTC | 23m |
| HYS253 | HYS | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-08-10 04:12 UTC | 2026-08-10 04:39 UTC | 26m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-08-10 03:56 UTC | 2026-08-10 04:36 UTC | 40m |
| WIF150 | WIF | Ørsta-Volda Airport Hovden (ENOV) | Sogndal Airport (ENSG) | 2026-08-10 04:18 UTC | 2026-08-10 04:33 UTC | 15m |
| JAL981 | Japan Airlines | Tokyo International Airport (RJTT) | Kerama Airport (ROKR) | 2026-08-10 02:29 UTC | 2026-08-10 04:32 UTC | 2h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
