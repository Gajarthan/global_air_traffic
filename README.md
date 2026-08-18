# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_11:19:30_UTC-green)

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

**Latest saved flight:** 2026-08-18 11:19:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 11:19:30 UTC

- **211,584** saved flights
- **67,139** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,584** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,544,363.8 tonnes** estimated CO2 emissions
- **147,499,348 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8377 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3621 |
| 5 | American Airlines | 3534 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1914 |
| 11 | Lufthansa | 1775 |
| 12 | Vueling | 1768 |
| 13 | WIF | 1700 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1468 |
| 16 | Swiss International | 1418 |
| 17 | AXM | 1386 |
| 18 | United Airlines | 1341 |
| 19 | QLK | 1320 |
| 20 | Alaska Airlines | 1302 |
| 21 | EJU | 1299 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1164 |
| 24 | Air France | 1142 |
| 25 | GLO | 1140 |
| 26 | PGT | 1134 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1079 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1052 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178895 |
| 2 | 🇪🇸 ES | 13553 |
| 3 | 🇧🇷 BR | 12102 |
| 4 | 🇦🇺 AU | 11954 |
| 5 | 🇨🇦 CA | 11696 |
| 6 | 🇮🇳 IN | 11286 |
| 7 | 🇮🇹 IT | 11086 |
| 8 | 🇩🇪 DE | 10442 |
| 9 | 🇬🇧 GB | 9861 |
| 10 | 🇯🇵 JP | 8778 |
| 11 | 🇨🇴 CO | 8486 |
| 12 | 🇫🇷 FR | 8407 |
| 13 | 🇬🇷 GR | 6201 |
| 14 | 🇹🇷 TR | 6044 |
| 15 | 🇲🇽 MX | 5931 |
| 16 | 🇨🇭 CH | 5613 |
| 17 | 🇳🇴 NO | 5269 |
| 18 | 🇲🇾 MY | 3659 |
| 19 | 🇿🇦 ZA | 3563 |
| 20 | 🇵🇱 PL | 3494 |
| 21 | 🇹🇭 TH | 3425 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2821 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2579 |
| 26 | 🇭🇷 HR | 2289 |
| 27 | 🇲🇦 MA | 2132 |
| 28 | 🇳🇱 NL | 1884 |
| 29 | 🇲🇪 ME | 1814 |
| 30 | 🇮🇩 ID | 1766 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4448 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2631 |
| 4 | Indira Gandhi International Airport |  | IN | 2576 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2374 |
| 7 | Zurich Airport |  | CH | 2208 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2184 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1940 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1760 |
| 16 | Frankfurt am Main International Airport |  | DE | 1728 |
| 17 | Madrid Barajas International Airport |  | ES | 1659 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1593 |
| 21 | Macau International Airport |  | MO | 1553 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1540 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1467 |
| 25 | Charles de Gaulle International Airport |  | FR | 1455 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1350 |
| 28 | Ninoy Aquino International Airport |  | PH | 1337 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1297 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1277 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1172 |
| 37 | Vitoria/Foronda Airport |  | ES | 1169 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1143 |
| 40 | Don Mueang International Airport |  | TH | 1132 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 752 | 21m | 244 km | 3,166.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 523 | 1h 7m | 770 km | 6,947.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 352 | 27m | 275 km | 1,668.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 274 | 21m | 250 km | 1,183.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 259 | 1h 38m | 1,156 km | 5,167.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 250 | 19m | 165 km | 711.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 242 | 31m | 369 km | 1,540.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 242 | 19m | 144 km | 602.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N283KS |  | Nassau Airport (83FL) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-18 10:07 UTC | 2026-08-18 11:19 UTC | 1h 11m |
| CAN07 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-18 10:49 UTC | 2026-08-18 11:18 UTC | 28m |
| ONI11 | ONI | Kisarazu Airport (RJTK) | Kisarazu Airport (RJTK) | 2026-08-18 10:42 UTC | 2026-08-18 11:15 UTC | 32m |
| OKANN | OKA | Mnichovo Hradiste Airport (LKMH) | Mnichovo Hradiste Airport (LKMH) | 2026-08-18 10:38 UTC | 2026-08-18 11:13 UTC | 35m |
| TCTZG | TCT | Balikesir Korfez Airport (LTFD) | Balikesir Korfez Airport (LTFD) | 2026-08-18 11:04 UTC | 2026-08-18 11:07 UTC | 3m |
| UFX61 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-18 10:14 UTC | 2026-08-18 11:06 UTC | 52m |
| UAE9422 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-18 03:51 UTC | 2026-08-18 11:06 UTC | 7h 14m |
| EFC51A | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-18 10:41 UTC | 2026-08-18 11:05 UTC | 23m |
| GNY4376 | GNY | Helgoland-Dune Airport (EDXH) | Nordholz-Spieka Airport (EDXN) | 2026-08-18 10:22 UTC | 2026-08-18 11:05 UTC | 42m |
| EAG4SU | EAG | George Best Belfast City Airport (EGAC) | Southampton Airport (EGHI) | 2026-08-18 09:43 UTC | 2026-08-18 11:05 UTC | 1h 21m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-18 10:11 UTC | 2026-08-18 10:59 UTC | 48m |
| AAL962 | American Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-18 01:26 UTC | 2026-08-18 10:59 UTC | 9h 33m |
| UAE9798 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-08-18 03:30 UTC | 2026-08-18 10:58 UTC | 7h 28m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-18 10:41 UTC | 2026-08-18 10:55 UTC | 14m |
| N224JD |  | Tulsa Riverside Airport (KRVS) | Brickey Airport (AR43) | 2026-08-18 10:21 UTC | 2026-08-18 10:55 UTC | 33m |
| SGA2563 | SGA | Sharjah International Airport (OMSJ) | Zhuhai Airport (ZGSD) | 2026-08-18 03:12 UTC | 2026-08-18 10:52 UTC | 7h 39m |
| NSZ3085 | NSZ | Aalborg Airport (EKYT) | Copenhagen Kastrup Airport (EKCH) | 2026-08-18 10:22 UTC | 2026-08-18 10:51 UTC | 29m |
| R21200 |  | Scotts Airport (0AK0) | Ladd Army Air Field (PAFB) | 2026-08-18 10:16 UTC | 2026-08-18 10:51 UTC | 34m |
| N704VY |  | Ocala International-Jim Taylor Field (KOCF) | Williston Regional Airport (KX60) | 2026-08-18 10:22 UTC | 2026-08-18 10:50 UTC | 28m |
| ZAM40 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-18 10:34 UTC | 2026-08-18 10:50 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
