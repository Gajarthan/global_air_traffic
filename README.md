# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_04:39:58_UTC-green)

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

**Latest saved flight:** 2026-08-12 04:39:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 04:39:58 UTC

- **188,632** saved flights
- **59,716** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,632** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,260,959.5 tonnes** estimated CO2 emissions
- **131,070,117 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7479 |
| 2 | SkyWest Airlines | 6863 |
| 3 | EJA | 3722 |
| 4 | IndiGo | 3279 |
| 5 | Southwest Airlines | 2956 |
| 6 | American Airlines | 2934 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2220 |
| 9 | LATAM Airlines | 1762 |
| 10 | AZU | 1698 |
| 11 | Lufthansa | 1647 |
| 12 | Vueling | 1564 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1248 |
| 18 | EJU | 1163 |
| 19 | QLK | 1161 |
| 20 | All Nippon Airways | 1149 |
| 21 | Alaska Airlines | 1129 |
| 22 | VIV | 1045 |
| 23 | GLO | 1017 |
| 24 | Air France | 978 |
| 25 | PGT | 971 |
| 26 | AEE | 969 |
| 27 | United Airlines | 969 |
| 28 | CXK | 966 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161104 |
| 2 | 🇪🇸 ES | 12134 |
| 3 | 🇧🇷 BR | 10833 |
| 4 | 🇦🇺 AU | 10562 |
| 5 | 🇨🇦 CA | 10336 |
| 6 | 🇮🇳 IN | 10276 |
| 7 | 🇮🇹 IT | 9761 |
| 8 | 🇩🇪 DE | 9303 |
| 9 | 🇬🇧 GB | 8760 |
| 10 | 🇯🇵 JP | 7697 |
| 11 | 🇫🇷 FR | 7528 |
| 12 | 🇨🇴 CO | 7178 |
| 13 | 🇬🇷 GR | 5520 |
| 14 | 🇲🇽 MX | 5382 |
| 15 | 🇨🇭 CH | 5034 |
| 16 | 🇹🇷 TR | 4990 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3267 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3123 |
| 21 | 🇹🇭 TH | 2911 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2494 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2321 |
| 26 | 🇲🇦 MA | 1915 |
| 27 | 🇭🇷 HR | 1910 |
| 28 | 🇲🇪 ME | 1685 |
| 29 | 🇳🇱 NL | 1679 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3115 |
| 3 | Tokyo International Airport |  | JP | 2380 |
| 4 | Indira Gandhi International Airport |  | IN | 2314 |
| 5 | Guaymaral Airport |  | CO | 2312 |
| 6 | Harry Reid International Airport |  | US | 2210 |
| 7 | Zurich Airport |  | CH | 2001 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1956 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1698 |
| 13 | Salt Lake City International Airport |  | US | 1680 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1617 |
| 16 | Congonhas Airport |  | BR | 1575 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1465 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1350 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1314 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1223 |
| 28 | Bengaluru International Airport |  | IN | 1211 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1183 |
| 30 | Ninoy Aquino International Airport |  | PH | 1178 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1128 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1090 |
| 35 | Seattle-Tacoma International Airport |  | US | 1089 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1062 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 953 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 690 | 21m | 244 km | 2,905.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 456 | 1h 7m | 770 km | 6,057.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 439 | 24m | 225 km | 1,703.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
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
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 224 | 19m | 144 km | 557.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 206 | 1h 48m | 1,304 km | 4,634.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A7GHZ |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-12 03:50 UTC | 2026-08-12 04:39 UTC | 49m |
| N619FB |  | John Wayne/Orange County Airport (KSNA) | North Las Vegas Airport (KVGT) | 2026-08-12 03:30 UTC | 2026-08-12 04:38 UTC | 1h 8m |
| JAL3316 | Japan Airlines | New Chitose Airport (RJCC) | Ashiya Airport (RJFA) | 2026-08-12 02:48 UTC | 2026-08-12 04:35 UTC | 1h 46m |
| OKFUG94 | OKF | Vrchlabi Airport (LKVR) | Nove Mesto Airport (LKNM) | 2026-08-12 04:10 UTC | 2026-08-12 04:28 UTC | 18m |
| OXF9610 | OXF | Falcon Field (KFFZ) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-12 03:25 UTC | 2026-08-12 04:21 UTC | 56m |
| FIN4J | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-08-12 03:30 UTC | 2026-08-12 04:20 UTC | 49m |
| LIFELN3 | LIF | Deelen Air Base (EHDL) | Volkel Air Base (EHVK) | 2026-08-12 04:13 UTC | 2026-08-12 04:19 UTC | 6m |
| N316VB |  | Teterboro Airport (KTEB) | Bangor International Airport (KBGR) | 2026-08-12 03:23 UTC | 2026-08-12 04:19 UTC | 55m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-12 03:12 UTC | 2026-08-12 04:17 UTC | 1h 5m |
| VAR425 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-12 03:44 UTC | 2026-08-12 04:17 UTC | 32m |
| VAR507 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-12 03:31 UTC | 2026-08-12 04:15 UTC | 43m |
| N390KT |  | Bobcat Field (1MT6) | Coeur D'Alene Airport (KCOE) | 2026-08-12 03:40 UTC | 2026-08-12 04:14 UTC | 34m |
| ANA251 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-12 03:03 UTC | 2026-08-12 04:12 UTC | 1h 8m |
| KAL806 | Korean Air | Tianjin Binhai International Airport (ZBTJ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-12 03:47 UTC | 2026-08-12 04:12 UTC | 24m |
| OXK | OXK | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-12 03:57 UTC | 2026-08-12 04:08 UTC | 10m |
| LDACE11 | LDA | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-12 03:31 UTC | 2026-08-12 04:03 UTC | 31m |
| B88999 |  | Taipei Songshan Airport (RCSS) | Taipei Songshan Airport (RCSS) | 2026-08-12 03:43 UTC | 2026-08-12 03:59 UTC | 16m |
| DAL2113 | Delta Air Lines | John Glenn Columbus International Airport (KCMH) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-12 02:18 UTC | 2026-08-12 03:53 UTC | 1h 35m |
| PGT1861 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-08-12 03:00 UTC | 2026-08-12 03:52 UTC | 52m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-08-12 03:21 UTC | 2026-08-12 03:51 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
