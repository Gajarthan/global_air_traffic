# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_21:01:50_UTC-green)

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

**Latest saved flight:** 2026-07-30 21:01:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 21:01:50 UTC

- **161,343** saved flights
- **53,274** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,343** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,935,056.9 tonnes** estimated CO2 emissions
- **112,177,210 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6459 |
| 2 | SkyWest Airlines | 5886 |
| 3 | EJA | 3197 |
| 4 | IndiGo | 2832 |
| 5 | American Airlines | 2551 |
| 6 | Southwest Airlines | 2527 |
| 7 | ENY | 2008 |
| 8 | Delta Air Lines | 1921 |
| 9 | Lufthansa | 1520 |
| 10 | LATAM Airlines | 1514 |
| 11 | AZU | 1416 |
| 12 | WIF | 1366 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1252 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1112 |
| 17 | easyJet | 1055 |
| 18 | Alaska Airlines | 1004 |
| 19 | EJU | 994 |
| 20 | QLK | 991 |
| 21 | All Nippon Airways | 990 |
| 22 | VIV | 888 |
| 23 | CXK | 863 |
| 24 | United Airlines | 854 |
| 25 | Cathay Pacific | 848 |
| 26 | GLO | 848 |
| 27 | AEE | 846 |
| 28 | Air France | 837 |
| 29 | MXY | 835 |
| 30 | JetBlue | 826 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139373 |
| 2 | 🇪🇸 ES | 10343 |
| 3 | 🇧🇷 BR | 9214 |
| 4 | 🇦🇺 AU | 9082 |
| 5 | 🇮🇳 IN | 8911 |
| 6 | 🇨🇦 CA | 8760 |
| 7 | 🇮🇹 IT | 8321 |
| 8 | 🇩🇪 DE | 8140 |
| 9 | 🇬🇧 GB | 7408 |
| 10 | 🇯🇵 JP | 6531 |
| 11 | 🇫🇷 FR | 6389 |
| 12 | 🇨🇴 CO | 5729 |
| 13 | 🇬🇷 GR | 4633 |
| 14 | 🇲🇽 MX | 4632 |
| 15 | 🇳🇴 NO | 4265 |
| 16 | 🇨🇭 CH | 4231 |
| 17 | 🇹🇷 TR | 3851 |
| 18 | 🇲🇾 MY | 2909 |
| 19 | 🇵🇱 PL | 2737 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2368 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2117 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2071 |
| 26 | 🇲🇦 MA | 1629 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1507 |
| 29 | 🇳🇱 NL | 1479 |
| 30 | 🇲🇴 MO | 1339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3293 |
| 2 | Denver International Airport |  | US | 2687 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1982 |
| 6 | Harry Reid International Airport |  | US | 1959 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1785 |
| 8 | Zurich Airport |  | CH | 1721 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1698 |
| 10 | La Aurora Airport |  | GT | 1607 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1502 |
| 12 | El Dorado International Airport |  | CO | 1478 |
| 13 | Frankfurt am Main International Airport |  | DE | 1471 |
| 14 | Chicago O'Hare International Airport |  | US | 1466 |
| 15 | Salt Lake City International Airport |  | US | 1453 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1349 |
| 17 | Congonhas Airport |  | BR | 1339 |
| 18 | Macau International Airport |  | MO | 1339 |
| 19 | Madrid Barajas International Airport |  | ES | 1277 |
| 20 | Capua Airport |  | IT | 1270 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1235 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1143 |
| 24 | Charlotte/Douglas International Airport |  | US | 1132 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1068 |
| 28 | Bengaluru International Airport |  | IN | 1059 |
| 29 | Ninoy Aquino International Airport |  | PH | 993 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 986 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 980 |
| 32 | Barcelona International Airport |  | ES | 958 |
| 33 | Daniel K Inouye International Airport |  | US | 948 |
| 34 | Seattle-Tacoma International Airport |  | US | 936 |
| 35 | Calgary International Airport |  | CA | 923 |
| 36 | Viracopos International Airport |  | BR | 918 |
| 37 | Scottsdale Airport |  | US | 907 |
| 38 | Tenerife Norte Airport |  | ES | 904 |
| 39 | Oslo Gardermoen Airport |  | NO | 897 |
| 40 | Reno/Tahoe International Airport |  | US | 886 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 587 | 21m | 244 km | 2,471.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 385 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 238 | 22m | 55 km | 226.2 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 231 | 44m | 241 km | 959.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 194 | 30m | 49 km | 164.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 192 | 1h 15m | 961 km | 3,182.5 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 192 | 28m | 152 km | 501.8 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 185 | 50m | 556 km | 1,773.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 185 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 181 | 1h 39m | 1,156 km | 3,610.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 178 | 1h 1m | 695 km | 2,133.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 172 | 23m | 218 km | 648.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK583 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-30 20:39 UTC | 2026-07-30 21:01 UTC | 22m |
| TKR137 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Libby Airport (KS59) | 2026-07-30 20:47 UTC | 2026-07-30 20:58 UTC | 11m |
| N410W |  | 71IS (71IS) | Frasca Field (KC16) | 2026-07-30 20:44 UTC | 2026-07-30 20:57 UTC | 13m |
| LXJ438 | LXJ | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-30 20:40 UTC | 2026-07-30 20:51 UTC | 11m |
| ZKWWH | ZKW | Motiti Island Airport (NZOI) | Motiti Island Airport (NZOI) | 2026-07-30 20:48 UTC | 2026-07-30 20:49 UTC | 0m |
| TKR102 | TKR | Cabin Creek Landing Airport (97MT) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-30 20:34 UTC | 2026-07-30 20:45 UTC | 11m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-30 20:26 UTC | 2026-07-30 20:44 UTC | 18m |
| N545AM |  | Bellefontaine Regional Airport (KEDJ) | Bellefontaine Regional Airport (KEDJ) | 2026-07-30 20:42 UTC | 2026-07-30 20:44 UTC | 1m |
| RYR5BQ | Ryanair | Palermo / Punta Raisi Airport (LICJ) | Malpensa International Airport (LIMC) | 2026-07-30 19:26 UTC | 2026-07-30 20:43 UTC | 1h 16m |
| N19TF |  | Anderson Regional Airport (KAND) | Anderson Regional Airport (KAND) | 2026-07-30 20:11 UTC | 2026-07-30 20:42 UTC | 30m |
| KANZA54 | KAN | Mc Connell Afb Airport (KIAB) | G Bar F Ranch Airport (NM84) | 2026-07-30 18:29 UTC | 2026-07-30 20:42 UTC | 2h 12m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-07-30 20:26 UTC | 2026-07-30 20:41 UTC | 15m |
| TKR184 | TKR | Grant County International Airport (KMWH) | 0WN9 (0WN9) | 2026-07-30 20:26 UTC | 2026-07-30 20:40 UTC | 13m |
| CES214 | China Eastern | London Gatwick Airport (EGKK) | Kotlas Airport (ULKK) | 2026-07-30 17:22 UTC | 2026-07-30 20:39 UTC | 3h 16m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-07-30 06:13 UTC | 2026-07-30 20:37 UTC | 14h 24m |
| N869FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-07-30 19:40 UTC | 2026-07-30 20:36 UTC | 55m |
| N536SH |  | Hp Field (5KY6) | Pumpkin Field (92KY) | 2026-07-30 16:54 UTC | 2026-07-30 20:32 UTC | 3h 38m |
| TKR186 | TKR | Grant County International Airport (KMWH) | 0WN9 (0WN9) | 2026-07-30 20:18 UTC | 2026-07-30 20:31 UTC | 13m |
| N613LG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-30 19:45 UTC | 2026-07-30 20:31 UTC | 45m |
| N155TV |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-07-30 19:35 UTC | 2026-07-30 20:30 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
