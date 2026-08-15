# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_13:21:05_UTC-green)

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

**Latest saved flight:** 2026-08-15 13:21:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 13:21:05 UTC

- **198,473** saved flights
- **62,075** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,473** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,371,155.5 tonnes** estimated CO2 emissions
- **137,458,288 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7884 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3897 |
| 4 | IndiGo | 3435 |
| 5 | Southwest Airlines | 3070 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2346 |
| 9 | LATAM Airlines | 1863 |
| 10 | AZU | 1794 |
| 11 | Lufthansa | 1701 |
| 12 | Vueling | 1665 |
| 13 | WIF | 1637 |
| 14 | LXJ | 1572 |
| 15 | easyJet | 1364 |
| 16 | Swiss International | 1343 |
| 17 | AXM | 1306 |
| 18 | EJU | 1230 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1094 |
| 23 | GLO | 1071 |
| 24 | Air France | 1049 |
| 25 | PGT | 1046 |
| 26 | AEE | 1022 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1007 |
| 29 | WMT | 1000 |
| 30 | Wizz Air | 982 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168225 |
| 2 | 🇪🇸 ES | 12823 |
| 3 | 🇧🇷 BR | 11405 |
| 4 | 🇦🇺 AU | 11146 |
| 5 | 🇨🇦 CA | 10845 |
| 6 | 🇮🇳 IN | 10736 |
| 7 | 🇮🇹 IT | 10380 |
| 8 | 🇩🇪 DE | 9863 |
| 9 | 🇬🇧 GB | 9331 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7915 |
| 12 | 🇨🇴 CO | 7827 |
| 13 | 🇬🇷 GR | 5853 |
| 14 | 🇲🇽 MX | 5607 |
| 15 | 🇹🇷 TR | 5484 |
| 16 | 🇨🇭 CH | 5388 |
| 17 | 🇳🇴 NO | 5069 |
| 18 | 🇲🇾 MY | 3421 |
| 19 | 🇿🇦 ZA | 3362 |
| 20 | 🇵🇱 PL | 3282 |
| 21 | 🇹🇭 TH | 3120 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2101 |
| 27 | 🇲🇦 MA | 2007 |
| 28 | 🇳🇱 NL | 1781 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1630 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2444 |
| 5 | Indira Gandhi International Airport |  | IN | 2434 |
| 6 | Harry Reid International Airport |  | US | 2269 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2101 |
| 8 | Zurich Airport |  | CH | 2100 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2050 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1823 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1760 |
| 14 | Chicago O'Hare International Airport |  | US | 1737 |
| 15 | Frankfurt am Main International Airport |  | DE | 1672 |
| 16 | Congonhas Airport |  | BR | 1670 |
| 17 | Madrid Barajas International Airport |  | ES | 1563 |
| 18 | Macau International Airport |  | MO | 1535 |
| 19 | Capua Airport |  | IT | 1518 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1510 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1459 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1428 |
| 23 | Malpensa International Airport |  | IT | 1381 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 25 | Charles de Gaulle International Airport |  | FR | 1363 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1274 |
| 28 | Bengaluru International Airport |  | IN | 1253 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1237 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1194 |
| 33 | Viracopos International Airport |  | BR | 1153 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1118 |
| 37 | Reno/Tahoe International Airport |  | US | 1116 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1091 |
| 40 | Tenerife Norte Airport |  | ES | 1089 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 357 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 333 | 27m | 275 km | 1,577.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 290 | 1h 49m | 1,423 km | 7,117.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 247 | 26m | 215 km | 914.8 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 232 | 19m | 144 km | 577.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEVAP | DEV | Nordhorn-Lingen Airport (EDWN) | Rheine-Eschendorf Airport (EDXE) | 2026-08-15 13:06 UTC | 2026-08-15 13:21 UTC | 14m |
| DMMFG | DMM | Treuchtlingen-Bubenheim Airport (EDNT) | Treuchtlingen-Bubenheim Airport (EDNT) | 2026-08-15 12:47 UTC | 2026-08-15 13:03 UTC | 15m |
| N20693 |  | WS10 (WS10) | WS10 (WS10) | 2026-08-15 12:43 UTC | 2026-08-15 12:57 UTC | 13m |
| LRS1102 | LRS | El Ron Ron Airport (MRER) | Tambor Airport (MRTR) | 2026-08-15 12:36 UTC | 2026-08-15 12:56 UTC | 19m |
| N8650E |  | K00V (K00V) | Limon Municipal Airport (KLIC) | 2026-08-15 12:05 UTC | 2026-08-15 12:55 UTC | 50m |
| TKJ3TY | TKJ | Sabiha Gokcen International Airport (LTFJ) | Gaziemir Airport (LTBK) | 2026-08-15 12:15 UTC | 2026-08-15 12:53 UTC | 38m |
| N525DW |  | Midland International Air And Space Port Airport (KMAF) | Mc Entire's Lazy V Ranch Airport (58XS) | 2026-08-15 12:37 UTC | 2026-08-15 12:51 UTC | 14m |
| CXK442 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-15 12:38 UTC | 2026-08-15 12:46 UTC | 7m |
| D6836 |  | Albstadt-Degerfeld Airport (EDSA) | Laichingen Airport (EDPJ) | 2026-08-15 10:14 UTC | 2026-08-15 12:43 UTC | 2h 29m |
| HK5231G |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-15 12:24 UTC | 2026-08-15 12:42 UTC | 18m |
| N37SJ |  | Mengen-Hohentengen Airport (EDTM) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-15 11:51 UTC | 2026-08-15 12:42 UTC | 50m |
| N733PN |  | Northeast Philadelphia Airport (KPNE) | Heritage Field (KPTW) | 2026-08-15 11:50 UTC | 2026-08-15 12:40 UTC | 50m |
| N5566A |  | Orlando Sanford International Airport (KSFB) | Orlando Executive Airport (KORL) | 2026-08-15 11:50 UTC | 2026-08-15 12:39 UTC | 48m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-08-15 12:22 UTC | 2026-08-15 12:39 UTC | 16m |
| N428CF |  | Fort Worth Meacham International Airport (KFTW) | Mid-Way Regional Airport (KJWY) | 2026-08-15 12:26 UTC | 2026-08-15 12:38 UTC | 12m |
| EAI81A | EAI | Bristol International Airport (EGGD) | Dublin Airport (EIDW) | 2026-08-15 11:31 UTC | 2026-08-15 12:36 UTC | 1h 4m |
| GOMTX | GOM | Farnborough Airport (EGLF) | Samedan Airport (LSZS) | 2026-08-15 11:15 UTC | 2026-08-15 12:35 UTC | 1h 19m |
| WIF5DY | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-08-15 12:04 UTC | 2026-08-15 12:33 UTC | 29m |
| EAI38D | EAI | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-15 11:43 UTC | 2026-08-15 12:33 UTC | 50m |
| N201HG |  | Bishop International Airport (KFNT) | Oakland County International Airport (KPTK) | 2026-08-15 12:19 UTC | 2026-08-15 12:32 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
