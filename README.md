# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_23:31:58_UTC-green)

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

**Latest saved flight:** 2026-08-10 23:31:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 23:31:58 UTC

- **185,549** saved flights
- **58,962** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,549** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,227,448.7 tonnes** estimated CO2 emissions
- **129,127,463 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7354 |
| 2 | SkyWest Airlines | 6771 |
| 3 | EJA | 3673 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2916 |
| 6 | American Airlines | 2896 |
| 7 | ENY | 2316 |
| 8 | Delta Air Lines | 2187 |
| 9 | LATAM Airlines | 1738 |
| 10 | AZU | 1670 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1457 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1235 |
| 18 | EJU | 1146 |
| 19 | QLK | 1136 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1109 |
| 22 | VIV | 1022 |
| 23 | GLO | 996 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | United Airlines | 948 |
| 28 | Cathay Pacific | 947 |
| 29 | PGT | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158729 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10667 |
| 4 | 🇦🇺 AU | 10322 |
| 5 | 🇨🇦 CA | 10141 |
| 6 | 🇮🇳 IN | 10141 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9153 |
| 9 | 🇬🇧 GB | 8605 |
| 10 | 🇯🇵 JP | 7516 |
| 11 | 🇫🇷 FR | 7405 |
| 12 | 🇨🇴 CO | 7010 |
| 13 | 🇬🇷 GR | 5438 |
| 14 | 🇲🇽 MX | 5297 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4865 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3222 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3090 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2633 |
| 23 | 🇵🇭 PH | 2445 |
| 24 | 🇬🇹 GT | 2373 |
| 25 | 🇰🇷 KR | 2288 |
| 26 | 🇲🇦 MA | 1876 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3857 |
| 2 | Denver International Airport |  | US | 3068 |
| 3 | Tokyo International Airport |  | JP | 2330 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2272 |
| 6 | Harry Reid International Airport |  | US | 2175 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1930 |
| 10 | La Aurora Airport |  | GT | 1821 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1694 |
| 12 | El Dorado International Airport |  | CO | 1665 |
| 13 | Salt Lake City International Airport |  | US | 1656 |
| 14 | Chicago O'Hare International Airport |  | US | 1652 |
| 15 | Frankfurt am Main International Airport |  | DE | 1596 |
| 16 | Congonhas Airport |  | BR | 1552 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1453 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1385 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1327 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1265 |
| 26 | Charlotte/Douglas International Airport |  | US | 1255 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1162 |
| 30 | Ninoy Aquino International Airport |  | PH | 1153 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1137 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Viracopos International Airport |  | BR | 1070 |
| 34 | Seattle-Tacoma International Airport |  | US | 1068 |
| 35 | Reno/Tahoe International Airport |  | US | 1067 |
| 36 | Calgary International Airport |  | CA | 1058 |
| 37 | Daniel K Inouye International Airport |  | US | 1052 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 680 | 21m | 244 km | 2,863.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 445 | 1h 8m | 770 km | 5,911.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 225 | 50m | 556 km | 2,156.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 216 | 31m | 369 km | 1,374.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR90C | Qatar Airways | Hamad International Airport (OTHH) | Jendarata Airport (WMAJ) | 2026-08-10 16:49 UTC | 2026-08-10 23:31 UTC | 6h 42m |
| N455NC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-10 21:47 UTC | 2026-08-10 23:31 UTC | 1h 44m |
| N23TL |  | Beatrice Municipal Airport (KBIE) | Lincoln Airport (KLNK) | 2026-08-10 21:21 UTC | 2026-08-10 23:24 UTC | 2h 3m |
| N317BF |  | Indianapolis Regional Airport (KMQJ) | Indianapolis Regional Airport (KMQJ) | 2026-08-10 23:11 UTC | 2026-08-10 23:23 UTC | 11m |
| SCU34 | SCU | Bartlesville Municipal Airport (KBVO) | 84OL (84OL) | 2026-08-10 23:03 UTC | 2026-08-10 23:22 UTC | 18m |
| URSA22 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-10 22:38 UTC | 2026-08-10 23:15 UTC | 36m |
| TKR137 | TKR | Mc Clellan Airfield (KMCC) | Sierraville Dearwater Airport (KO79) | 2026-08-10 22:57 UTC | 2026-08-10 23:11 UTC | 13m |
| N739LT |  | Butler County Regional/Hogan Field (KHAO) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-10 22:54 UTC | 2026-08-10 23:11 UTC | 16m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-08-10 22:52 UTC | 2026-08-10 23:05 UTC | 13m |
| AWH67T | AWH | Hannover Airport (EDDV) | Stockholm-Arlanda Airport (ESSA) | 2026-08-10 21:40 UTC | 2026-08-10 23:04 UTC | 1h 24m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 22:47 UTC | 2026-08-10 23:02 UTC | 15m |
| N4982E |  | Knoxville Downtown Island Airport (KDKX) | Landing At River's Edge Airport (98TN) | 2026-08-10 22:35 UTC | 2026-08-10 23:02 UTC | 27m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 22:46 UTC | 2026-08-10 23:01 UTC | 15m |
| ZJH | ZJH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-10 22:42 UTC | 2026-08-10 23:01 UTC | 19m |
| TKR169 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-10 22:54 UTC | 2026-08-10 22:58 UTC | 4m |
| N511EX |  | Friday Harbor Airport (KFHR) | Skagit Regional Airport (KBVS) | 2026-08-10 21:58 UTC | 2026-08-10 22:55 UTC | 57m |
| N43PC |  | Kearney Regional Airport (KEAR) | Brookings Regional Airport (KBKX) | 2026-08-10 21:54 UTC | 2026-08-10 22:55 UTC | 1h 1m |
| TKR912 | TKR | Mc Clellan Airfield (KMCC) | Sierraville Dearwater Airport (KO79) | 2026-08-10 22:40 UTC | 2026-08-10 22:55 UTC | 14m |
| HYTEK44 | HYT | 3FL8 (3FL8) | North American Farms Airport (56FD) | 2026-08-10 22:24 UTC | 2026-08-10 22:54 UTC | 29m |
| ENY4113 | ENY | Dallas-Fort Worth International Airport (KDFW) | Herington Regional Airport (KHRU) | 2026-08-10 21:55 UTC | 2026-08-10 22:49 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
