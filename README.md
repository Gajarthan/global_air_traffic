# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_22:30:35_UTC-green)

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

**Latest saved flight:** 2026-08-13 22:30:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 22:30:35 UTC

- **193,829** saved flights
- **60,983** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **193,829** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,317,097.4 tonnes** estimated CO2 emissions
- **134,324,489 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7710 |
| 2 | SkyWest Airlines | 7005 |
| 3 | EJA | 3827 |
| 4 | IndiGo | 3345 |
| 5 | Southwest Airlines | 3015 |
| 6 | American Airlines | 3006 |
| 7 | ENY | 2400 |
| 8 | Delta Air Lines | 2292 |
| 9 | LATAM Airlines | 1819 |
| 10 | AZU | 1748 |
| 11 | Lufthansa | 1673 |
| 12 | Vueling | 1613 |
| 13 | WIF | 1603 |
| 14 | LXJ | 1538 |
| 15 | easyJet | 1337 |
| 16 | Swiss International | 1315 |
| 17 | AXM | 1258 |
| 18 | EJU | 1193 |
| 19 | QLK | 1187 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1151 |
| 22 | VIV | 1066 |
| 23 | GLO | 1042 |
| 24 | Air France | 1011 |
| 25 | PGT | 1007 |
| 26 | AEE | 991 |
| 27 | United Airlines | 990 |
| 28 | CXK | 989 |
| 29 | WMT | 964 |
| 30 | Wizz Air | 962 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165150 |
| 2 | 🇪🇸 ES | 12504 |
| 3 | 🇧🇷 BR | 11145 |
| 4 | 🇦🇺 AU | 10820 |
| 5 | 🇨🇦 CA | 10621 |
| 6 | 🇮🇳 IN | 10471 |
| 7 | 🇮🇹 IT | 10079 |
| 8 | 🇩🇪 DE | 9585 |
| 9 | 🇬🇧 GB | 9067 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7731 |
| 12 | 🇨🇴 CO | 7554 |
| 13 | 🇬🇷 GR | 5672 |
| 14 | 🇲🇽 MX | 5486 |
| 15 | 🇹🇷 TR | 5227 |
| 16 | 🇨🇭 CH | 5208 |
| 17 | 🇳🇴 NO | 4963 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3190 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2712 |
| 23 | 🇵🇭 PH | 2542 |
| 24 | 🇬🇹 GT | 2466 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 2011 |
| 27 | 🇲🇦 MA | 1970 |
| 28 | 🇳🇱 NL | 1742 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4032 |
| 2 | Denver International Airport |  | US | 3178 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2412 |
| 5 | Indira Gandhi International Airport |  | IN | 2359 |
| 6 | Harry Reid International Airport |  | US | 2244 |
| 7 | Zurich Airport |  | CH | 2054 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2046 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2009 |
| 10 | La Aurora Airport |  | GT | 1896 |
| 11 | El Dorado International Airport |  | CO | 1768 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1743 |
| 13 | Salt Lake City International Airport |  | US | 1730 |
| 14 | Chicago O'Hare International Airport |  | US | 1698 |
| 15 | Frankfurt am Main International Airport |  | DE | 1639 |
| 16 | Congonhas Airport |  | BR | 1623 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1527 |
| 19 | Capua Airport |  | IT | 1492 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1490 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1435 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1390 |
| 23 | Malpensa International Airport |  | IT | 1343 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1343 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1209 |
| 30 | Ninoy Aquino International Airport |  | PH | 1202 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1187 |
| 32 | Barcelona International Airport |  | ES | 1159 |
| 33 | Viracopos International Airport |  | BR | 1127 |
| 34 | Seattle-Tacoma International Airport |  | US | 1114 |
| 35 | Calgary International Airport |  | CA | 1109 |
| 36 | Reno/Tahoe International Airport |  | US | 1103 |
| 37 | Oslo Gardermoen Airport |  | NO | 1087 |
| 38 | Daniel K Inouye International Airport |  | US | 1083 |
| 39 | Tenerife Norte Airport |  | ES | 1067 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 996 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 711 | 21m | 244 km | 2,993.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 454 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 289 | 44m | 241 km | 1,200.4 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 242 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 238 | 24m | 218 km | 896.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 228 | 1h 38m | 1,156 km | 4,548.5 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 209 | 1h 3m | 695 km | 2,505.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N321HJ |  | Dupage Airport (KDPA) | Chester County G O Carlson Airport (KMQS) | 2026-08-13 20:50 UTC | 2026-08-13 22:30 UTC | 1h 40m |
| N8131L |  | South Lakeland Airport (KX49) | Wauchula Municipal Airport (KCHN) | 2026-08-13 21:44 UTC | 2026-08-13 22:30 UTC | 45m |
| VVHK031 | VVH | Jacksonville Nas (Towers Field) Airport (KNIP) | Jacksonville Nas (Towers Field) Airport (KNIP) | 2026-08-13 22:14 UTC | 2026-08-13 22:27 UTC | 13m |
| AAL1953 | American Airlines | John F Kennedy International Airport (KJFK) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-13 19:24 UTC | 2026-08-13 22:22 UTC | 2h 57m |
| N716HC |  | Asheboro Regional Airport (KHBI) | Lakewood Airport (KN12) | 2026-08-13 19:15 UTC | 2026-08-13 22:19 UTC | 3h 4m |
| YTK | YTK | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-13 21:26 UTC | 2026-08-13 22:15 UTC | 49m |
| N69F |  | John F Kennedy International Airport (KJFK) | Teterboro Airport (KTEB) | 2026-08-13 22:05 UTC | 2026-08-13 22:14 UTC | 8m |
| G72251 |  | South Texas International At Edinburg Airport (KEBG) | Brownsville/South Padre Island International Airport (KBRO) | 2026-08-13 21:32 UTC | 2026-08-13 22:13 UTC | 40m |
| ZJH | ZJH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-13 21:44 UTC | 2026-08-13 22:12 UTC | 27m |
| N164YF |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-08-13 21:18 UTC | 2026-08-13 22:10 UTC | 51m |
| N8314W |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-08-13 21:25 UTC | 2026-08-13 22:04 UTC | 38m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-08-13 20:58 UTC | 2026-08-13 22:04 UTC | 1h 6m |
| CAI9164 | CAI | Antalya International Airport (LTAI) | Tolyatti Airport (UWWT) | 2026-08-13 18:40 UTC | 2026-08-13 22:03 UTC | 3h 22m |
| N350DR |  | Mc Ghee Tyson Airport (KTYS) | Lee County Airport (K0VG) | 2026-08-13 21:45 UTC | 2026-08-13 22:03 UTC | 17m |
| N155SL |  | Moose Lodge Airport (26ID) | Telluride Regional Airport (KTEX) | 2026-08-13 20:14 UTC | 2026-08-13 22:01 UTC | 1h 47m |
| N9055F |  | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-08-13 21:10 UTC | 2026-08-13 22:01 UTC | 51m |
| TIBJJ | TIB | Juan Santamaria International Airport (MROC) | Juan Santamaria International Airport (MROC) | 2026-08-13 21:55 UTC | 2026-08-13 21:58 UTC | 3m |
| TAM3276 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Fazenda Thalia Airport (SSTH) | 2026-08-13 21:17 UTC | 2026-08-13 21:56 UTC | 38m |
| N970CC |  | Cuyahoga County Airport (KCGF) | Nashville International Airport (KBNA) | 2026-08-13 20:46 UTC | 2026-08-13 21:54 UTC | 1h 8m |
| N702PX |  | Central Jersey Regional Airport (K47N) | Old Plains Airport (9PA2) | 2026-08-13 21:25 UTC | 2026-08-13 21:50 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
