# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_02:36:11_UTC-green)

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

**Latest saved flight:** 2026-08-16 02:36:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 02:36:11 UTC

- **202,260** saved flights
- **64,210** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **202,260** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,425,814.9 tonnes** estimated CO2 emissions
- **140,626,948 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7990 |
| 2 | SkyWest Airlines | 7302 |
| 3 | EJA | 3947 |
| 4 | IndiGo | 3450 |
| 5 | American Airlines | 3292 |
| 6 | Southwest Airlines | 3243 |
| 7 | Delta Air Lines | 2527 |
| 8 | ENY | 2515 |
| 9 | LATAM Airlines | 1900 |
| 10 | AZU | 1828 |
| 11 | Lufthansa | 1714 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1603 |
| 15 | easyJet | 1396 |
| 16 | Swiss International | 1351 |
| 17 | AXM | 1310 |
| 18 | EJU | 1242 |
| 19 | QLK | 1233 |
| 20 | Alaska Airlines | 1225 |
| 21 | All Nippon Airways | 1216 |
| 22 | United Airlines | 1203 |
| 23 | VIV | 1115 |
| 24 | GLO | 1089 |
| 25 | Air France | 1072 |
| 26 | PGT | 1070 |
| 27 | AEE | 1031 |
| 28 | JetBlue | 1017 |
| 29 | CXK | 1011 |
| 30 | WMT | 1010 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 172365 |
| 2 | 🇪🇸 ES | 12982 |
| 3 | 🇧🇷 BR | 11603 |
| 4 | 🇦🇺 AU | 11271 |
| 5 | 🇨🇦 CA | 11134 |
| 6 | 🇮🇳 IN | 10778 |
| 7 | 🇮🇹 IT | 10520 |
| 8 | 🇩🇪 DE | 9981 |
| 9 | 🇬🇧 GB | 9451 |
| 10 | 🇯🇵 JP | 8215 |
| 11 | 🇨🇴 CO | 8035 |
| 12 | 🇫🇷 FR | 8027 |
| 13 | 🇬🇷 GR | 5929 |
| 14 | 🇲🇽 MX | 5715 |
| 15 | 🇹🇷 TR | 5642 |
| 16 | 🇨🇭 CH | 5418 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3442 |
| 19 | 🇿🇦 ZA | 3373 |
| 20 | 🇵🇱 PL | 3318 |
| 21 | 🇹🇭 TH | 3149 |
| 22 | 🇳🇿 NZ | 2803 |
| 23 | 🇵🇭 PH | 2664 |
| 24 | 🇬🇹 GT | 2555 |
| 25 | 🇰🇷 KR | 2458 |
| 26 | 🇭🇷 HR | 2139 |
| 27 | 🇲🇦 MA | 2034 |
| 28 | 🇳🇱 NL | 1799 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1647 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4240 |
| 2 | Denver International Airport |  | US | 3293 |
| 3 | Tokyo International Airport |  | JP | 2504 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2446 |
| 6 | Harry Reid International Airport |  | US | 2298 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2118 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2099 |
| 10 | La Aurora Airport |  | GT | 1957 |
| 11 | El Dorado International Airport |  | CO | 1858 |
| 12 | Chicago O'Hare International Airport |  | US | 1836 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1808 |
| 14 | Salt Lake City International Airport |  | US | 1798 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1683 |
| 17 | Madrid Barajas International Airport |  | ES | 1585 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1549 |
| 19 | Capua Airport |  | IT | 1539 |
| 20 | Macau International Airport |  | MO | 1536 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1520 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1460 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1402 |
| 24 | Malpensa International Airport |  | IT | 1399 |
| 25 | Charles de Gaulle International Airport |  | FR | 1385 |
| 26 | Charlotte/Douglas International Airport |  | US | 1361 |
| 27 | Kuala Lumpur International Airport |  | MY | 1280 |
| 28 | Ninoy Aquino International Airport |  | PH | 1260 |
| 29 | Bengaluru International Airport |  | IN | 1258 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1254 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1228 |
| 32 | Barcelona International Airport |  | ES | 1211 |
| 33 | Seattle-Tacoma International Airport |  | US | 1182 |
| 34 | Viracopos International Airport |  | BR | 1171 |
| 35 | Calgary International Airport |  | CA | 1148 |
| 36 | Reno/Tahoe International Airport |  | US | 1130 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 491 | 1h 7m | 770 km | 6,522.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 468 | 24m | 225 km | 1,815.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 228 | 31m | 369 km | 1,451.3 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAL1389 | American Airlines | Miami International Airport (KMIA) | Branham Mill Airpark (VG29) | 2026-08-16 00:47 UTC | 2026-08-16 02:36 UTC | 1h 48m |
| AAL1843 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Oag Unmanned Center Airport (MD85) | 2026-08-16 01:47 UTC | 2026-08-16 02:36 UTC | 49m |
| AAL9828 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Garner Airport (3VA8) | 2026-08-16 02:01 UTC | 2026-08-16 02:36 UTC | 34m |
| AAL993 | American Airlines | Charlotte/Douglas International Airport (KCLT) | VA80 (VA80) | 2026-08-16 02:00 UTC | 2026-08-16 02:36 UTC | 35m |
| ASH4012 | ASH | Washington Dulles International Airport (KIAD) | MD43 (MD43) | 2026-08-16 02:23 UTC | 2026-08-16 02:36 UTC | 12m |
| DAL1636 | Delta Air Lines | John F Kennedy International Airport (KJFK) | Trenton-Robbinsville Airport (KN87) | 2026-08-16 02:25 UTC | 2026-08-16 02:36 UTC | 10m |
| DAL1689 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Perry-Warsaw Airport (K01G) | 2026-08-16 02:01 UTC | 2026-08-16 02:36 UTC | 34m |
| DAL2416 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Dunlea Airpark (PN66) | 2026-08-16 01:28 UTC | 2026-08-16 02:36 UTC | 1h 7m |
| EDV5326 | EDV | John F Kennedy International Airport (KJFK) | Crisfield-Somerset County Airport (KW41) | 2026-08-16 02:04 UTC | 2026-08-16 02:36 UTC | 32m |
| JBU2066 | JetBlue | Southwest Florida International Airport (KRSW) | Bagwell Airport (NC99) | 2026-08-16 01:14 UTC | 2026-08-16 02:36 UTC | 1h 21m |
| JBU438 | JetBlue | Orlando International Airport (KMCO) | 7NJ7 (7NJ7) | 2026-08-16 00:47 UTC | 2026-08-16 02:36 UTC | 1h 48m |
| JBU591 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | Scottbrook Farm Airport (2NC4) | 2026-08-16 01:18 UTC | 2026-08-16 02:36 UTC | 1h 17m |
| JIA5438 | JIA | Ronald Reagan Washington Ntl Airport (KDCA) | Monmouth Executive Airport (KBLM) | 2026-08-16 02:02 UTC | 2026-08-16 02:36 UTC | 33m |
| N600EB |  | Laguardia Airport (KLGA) | Spruce Airport (CT43) | 2026-08-16 02:18 UTC | 2026-08-16 02:36 UTC | 17m |
| N917BB |  | Washington Manassas/Harry P Davis Field (KHEF) | Lake Ridge Aero Park Airport (8NC8) | 2026-08-16 01:58 UTC | 2026-08-16 02:36 UTC | 37m |
| QTR50J | Qatar Airways | Toronto Pearson International Airport (CYYZ) | CFB Trenton (CYTR) | 2026-08-16 02:20 UTC | 2026-08-16 02:36 UTC | 16m |
| RPA3578 | Republic Airways | Newark Liberty International Airport (KEWR) | Harris Airport (3PA8) | 2026-08-16 02:17 UTC | 2026-08-16 02:36 UTC | 18m |
| SKW4892 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Kearny Airport (KE67) | 2026-08-16 02:23 UTC | 2026-08-16 02:36 UTC | 13m |
| UAL138 | United Airlines | Newark Liberty International Airport (KEWR) | K3B4 (K3B4) | 2026-08-16 02:04 UTC | 2026-08-16 02:36 UTC | 31m |
| AAL1075 | American Airlines | Philadelphia International Airport (KPHL) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-16 02:25 UTC | 2026-08-16 02:36 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
