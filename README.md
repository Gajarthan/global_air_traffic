# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_04:07:45_UTC-green)

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

**Latest saved flight:** 2026-08-04 04:07:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 04:07:45 UTC

- **169,865** saved flights
- **55,391** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **169,865** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,047,203.9 tonnes** estimated CO2 emissions
- **118,678,484 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6761 |
| 2 | SkyWest Airlines | 6222 |
| 3 | EJA | 3376 |
| 4 | IndiGo | 2988 |
| 5 | Southwest Airlines | 2681 |
| 6 | American Airlines | 2679 |
| 7 | ENY | 2124 |
| 8 | Delta Air Lines | 2025 |
| 9 | LATAM Airlines | 1578 |
| 10 | Lufthansa | 1558 |
| 11 | AZU | 1495 |
| 12 | WIF | 1419 |
| 13 | Vueling | 1398 |
| 14 | LXJ | 1334 |
| 15 | AXM | 1173 |
| 16 | Swiss International | 1159 |
| 17 | easyJet | 1139 |
| 18 | Alaska Airlines | 1039 |
| 19 | EJU | 1039 |
| 20 | QLK | 1038 |
| 21 | All Nippon Airways | 1027 |
| 22 | VIV | 938 |
| 23 | Cathay Pacific | 910 |
| 24 | CXK | 899 |
| 25 | United Airlines | 896 |
| 26 | GLO | 890 |
| 27 | AEE | 887 |
| 28 | Air France | 871 |
| 29 | MXY | 868 |
| 30 | JetBlue | 854 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 146572 |
| 2 | 🇪🇸 ES | 10869 |
| 3 | 🇧🇷 BR | 9664 |
| 4 | 🇦🇺 AU | 9477 |
| 5 | 🇮🇳 IN | 9363 |
| 6 | 🇨🇦 CA | 9221 |
| 7 | 🇮🇹 IT | 8751 |
| 8 | 🇩🇪 DE | 8449 |
| 9 | 🇬🇧 GB | 7876 |
| 10 | 🇯🇵 JP | 6816 |
| 11 | 🇫🇷 FR | 6714 |
| 12 | 🇨🇴 CO | 6173 |
| 13 | 🇬🇷 GR | 4924 |
| 14 | 🇲🇽 MX | 4866 |
| 15 | 🇨🇭 CH | 4463 |
| 16 | 🇳🇴 NO | 4426 |
| 17 | 🇹🇷 TR | 4124 |
| 18 | 🇲🇾 MY | 3047 |
| 19 | 🇵🇱 PL | 2860 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇳🇿 NZ | 2471 |
| 22 | 🇹🇭 TH | 2465 |
| 23 | 🇵🇭 PH | 2239 |
| 24 | 🇬🇹 GT | 2192 |
| 25 | 🇰🇷 KR | 2157 |
| 26 | 🇲🇦 MA | 1713 |
| 27 | 🇭🇷 HR | 1634 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1445 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3503 |
| 2 | Denver International Airport |  | US | 2820 |
| 3 | Tokyo International Airport |  | JP | 2139 |
| 4 | Guaymaral Airport |  | CO | 2107 |
| 5 | Indira Gandhi International Airport |  | IN | 2077 |
| 6 | Harry Reid International Airport |  | US | 2047 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1855 |
| 8 | Zurich Airport |  | CH | 1799 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1791 |
| 10 | La Aurora Airport |  | GT | 1691 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1568 |
| 12 | El Dorado International Airport |  | CO | 1546 |
| 13 | Chicago O'Hare International Airport |  | US | 1544 |
| 14 | Salt Lake City International Airport |  | US | 1528 |
| 15 | Frankfurt am Main International Airport |  | DE | 1519 |
| 16 | Macau International Airport |  | MO | 1445 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1401 |
| 18 | Congonhas Airport |  | BR | 1391 |
| 19 | Madrid Barajas International Airport |  | ES | 1333 |
| 20 | Capua Airport |  | IT | 1321 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1288 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1202 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1191 |
| 24 | Charlotte/Douglas International Airport |  | US | 1183 |
| 25 | Charles de Gaulle International Airport |  | FR | 1151 |
| 26 | Kuala Lumpur International Airport |  | MY | 1149 |
| 27 | Malpensa International Airport |  | IT | 1142 |
| 28 | Bengaluru International Airport |  | IN | 1112 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1057 |
| 30 | Ninoy Aquino International Airport |  | PH | 1053 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1050 |
| 32 | Barcelona International Airport |  | ES | 1005 |
| 33 | Daniel K Inouye International Airport |  | US | 986 |
| 34 | Seattle-Tacoma International Airport |  | US | 983 |
| 35 | Viracopos International Airport |  | BR | 965 |
| 36 | Calgary International Airport |  | CA | 962 |
| 37 | Reno/Tahoe International Airport |  | US | 953 |
| 38 | Tenerife Norte Airport |  | ES | 943 |
| 39 | Oslo Gardermoen Airport |  | NO | 941 |
| 40 | Scottsdale Airport |  | US | 936 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 875 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 619 | 21m | 244 km | 2,606.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 404 | 24m | 225 km | 1,567.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 251 | 44m | 241 km | 1,042.6 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 202 | 19m | 144 km | 502.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 201 | 50m | 556 km | 1,926.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 200 | 1h 15m | 961 km | 3,315.1 t |
| 24 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 199 | 12m | - | - |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 190 | 1h 38m | 1,156 km | 3,790.4 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 183 | 8m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL2305 | Delta Air Lines | General Edward Lawrence Logan International Airport (KBOS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-04 00:39 UTC | 2026-08-04 04:07 UTC | 3h 28m |
| UPS260 | UPS | Cologne Bonn Airport (EDDK) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-08-04 02:54 UTC | 2026-08-04 04:02 UTC | 1h 7m |
| SKY009 | SKY | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-04 02:50 UTC | 2026-08-04 03:54 UTC | 1h 4m |
| BHA251 | BHA | Tribhuvan International Airport (VNKT) | Tikapur Airport (VNTP) | 2026-08-04 02:43 UTC | 2026-08-04 03:48 UTC | 1h 4m |
| EJA969 | EJA | Santa Barbara Municipal Airport (KSBA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-04 03:07 UTC | 2026-08-04 03:45 UTC | 37m |
| VPCJH | VPC | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-08-04 01:14 UTC | 2026-08-04 03:45 UTC | 2h 31m |
| BH971 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-04 03:27 UTC | 2026-08-04 03:43 UTC | 16m |
| SWA3017 | Southwest Airlines | San Diego International Airport (KSAN) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-04 02:31 UTC | 2026-08-04 03:34 UTC | 1h 2m |
| N239FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-04 02:47 UTC | 2026-08-04 03:31 UTC | 44m |
| SWA792 | Southwest Airlines | Harry Reid International Airport (KLAS) | Carson City Airport (KCXP) | 2026-08-04 02:27 UTC | 2026-08-04 03:18 UTC | 50m |
| ETD2133 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-08-03 20:00 UTC | 2026-08-04 03:16 UTC | 7h 16m |
| CFR610 | CFR | Christensen Ranch Airport (9CL2) | Calaveras County/Maury Rasmussen Field (KCPU) | 2026-08-04 02:02 UTC | 2026-08-04 03:15 UTC | 1h 13m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-04 02:46 UTC | 2026-08-04 03:12 UTC | 26m |
| JA139R |  | Shizuhama Airport (RJNY) | Matsumoto Airport (RJAF) | 2026-08-04 02:49 UTC | 2026-08-04 03:10 UTC | 20m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-04 02:44 UTC | 2026-08-04 03:09 UTC | 25m |
| TKR138 | TKR | Wilson Creek Airport (K5W1) | Anderson Field (KS97) | 2026-08-04 02:57 UTC | 2026-08-04 03:08 UTC | 10m |
| AXM6320 | AXM | Kuala Lumpur International Airport (WMKK) | Penang International Airport (WMKP) | 2026-08-04 02:37 UTC | 2026-08-04 03:02 UTC | 25m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-08-04 02:35 UTC | 2026-08-04 03:02 UTC | 26m |
| RXA6528 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-08-04 02:29 UTC | 2026-08-04 03:00 UTC | 30m |
| ANZ607 | ANZ | Wellington International Airport (NZWN) | Omarama Glider Airport (NZOA) | 2026-08-04 02:10 UTC | 2026-08-04 02:57 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
