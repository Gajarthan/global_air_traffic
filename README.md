# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_16:29:15_UTC-green)

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

**Latest saved flight:** 2026-08-12 16:29:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 16:29:15 UTC

- **189,855** saved flights
- **59,977** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,855** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,273,031.9 tonnes** estimated CO2 emissions
- **131,769,966 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7531 |
| 2 | SkyWest Airlines | 6870 |
| 3 | EJA | 3743 |
| 4 | IndiGo | 3305 |
| 5 | Southwest Airlines | 2963 |
| 6 | American Airlines | 2939 |
| 7 | ENY | 2350 |
| 8 | Delta Air Lines | 2227 |
| 9 | LATAM Airlines | 1778 |
| 10 | AZU | 1712 |
| 11 | Lufthansa | 1656 |
| 12 | WIF | 1578 |
| 13 | Vueling | 1576 |
| 14 | LXJ | 1484 |
| 15 | easyJet | 1308 |
| 16 | Swiss International | 1296 |
| 17 | AXM | 1253 |
| 18 | EJU | 1170 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1048 |
| 23 | GLO | 1024 |
| 24 | Air France | 993 |
| 25 | PGT | 977 |
| 26 | AEE | 973 |
| 27 | United Airlines | 972 |
| 28 | CXK | 971 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 944 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161692 |
| 2 | 🇪🇸 ES | 12245 |
| 3 | 🇧🇷 BR | 10914 |
| 4 | 🇦🇺 AU | 10654 |
| 5 | 🇨🇦 CA | 10397 |
| 6 | 🇮🇳 IN | 10360 |
| 7 | 🇮🇹 IT | 9854 |
| 8 | 🇩🇪 DE | 9387 |
| 9 | 🇬🇧 GB | 8837 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7597 |
| 12 | 🇨🇴 CO | 7263 |
| 13 | 🇬🇷 GR | 5563 |
| 14 | 🇲🇽 MX | 5391 |
| 15 | 🇨🇭 CH | 5099 |
| 16 | 🇹🇷 TR | 5043 |
| 17 | 🇳🇴 NO | 4896 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3207 |
| 20 | 🇵🇱 PL | 3144 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2404 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1942 |
| 27 | 🇲🇦 MA | 1924 |
| 28 | 🇳🇱 NL | 1697 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3933 |
| 2 | Denver International Airport |  | US | 3118 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2340 |
| 5 | Indira Gandhi International Airport |  | IN | 2333 |
| 6 | Harry Reid International Airport |  | US | 2216 |
| 7 | Zurich Airport |  | CH | 2020 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2013 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1964 |
| 10 | La Aurora Airport |  | GT | 1848 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1715 |
| 12 | El Dorado International Airport |  | CO | 1710 |
| 13 | Salt Lake City International Airport |  | US | 1684 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1624 |
| 16 | Congonhas Airport |  | BR | 1585 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1499 |
| 19 | Capua Airport |  | IT | 1473 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1471 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1400 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1362 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1309 |
| 25 | Charles de Gaulle International Airport |  | FR | 1301 |
| 26 | Charlotte/Douglas International Airport |  | US | 1269 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1187 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1165 |
| 32 | Barcelona International Airport |  | ES | 1136 |
| 33 | Viracopos International Airport |  | BR | 1102 |
| 34 | Reno/Tahoe International Airport |  | US | 1094 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1082 |
| 37 | Daniel K Inouye International Airport |  | US | 1066 |
| 38 | Oslo Gardermoen Airport |  | NO | 1062 |
| 39 | Tenerife Norte Airport |  | ES | 1041 |
| 40 | Vitoria/Foronda Airport |  | ES | 1030 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 966 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 694 | 21m | 244 km | 2,922.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 441 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 319 | 27m | 275 km | 1,511.6 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 294 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 275 | 22m | 55 km | 261.4 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 273 | 1h 49m | 1,423 km | 6,699.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 255 | 20m | 250 km | 1,101.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 238 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 226 | 24m | 218 km | 851.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 226 | 19m | 144 km | 562.2 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 207 | 1h 48m | 1,304 km | 4,657.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N457TL |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-08-12 16:18 UTC | 2026-08-12 16:29 UTC | 10m |
| N308LC |  | Angel's Field (FL52) | Angel's Field (FL52) | 2026-08-12 16:13 UTC | 2026-08-12 16:25 UTC | 11m |
| N228LR |  | Minden-Tahoe Airport (KMEV) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-12 15:10 UTC | 2026-08-12 16:24 UTC | 1h 13m |
| FAM3934 | FAM | Santa Lucia Air Force Base (MMSM) | Santa Lucia Air Force Base (MMSM) | 2026-08-12 15:28 UTC | 2026-08-12 16:23 UTC | 55m |
| N288SF |  | Flying H Ranch Airport (2AL5) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-12 15:55 UTC | 2026-08-12 16:22 UTC | 27m |
| SPGAA | SPG | Jastarnia Airport (EPJA) | Jastarnia Airport (EPJA) | 2026-08-12 15:40 UTC | 2026-08-12 16:19 UTC | 39m |
| CXK141 | CXK | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-12 15:26 UTC | 2026-08-12 16:18 UTC | 51m |
| N24981 |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-08-12 15:22 UTC | 2026-08-12 16:18 UTC | 55m |
| N17598 |  | Seattle Paine Field International Airport (KPAE) | Wilding Farm Airport (6WA5) | 2026-08-12 15:30 UTC | 2026-08-12 16:18 UTC | 47m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-12 15:06 UTC | 2026-08-12 16:15 UTC | 1h 8m |
| GFD50 | GFD | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-08-12 14:43 UTC | 2026-08-12 16:13 UTC | 1h 29m |
| N600TB |  | Miami-Opa Locka Executive Airport (KOPF) | Miami Executive Airport (KTMB) | 2026-08-12 15:36 UTC | 2026-08-12 16:12 UTC | 35m |
| CFFJK | CFF | Boundary Bay Airport (CZBB) | Boundary Bay Airport (CZBB) | 2026-08-12 15:33 UTC | 2026-08-12 16:08 UTC | 35m |
| NDU502 | NDU | Mesa Gateway Airport (KIWA) | Sarita Airport (37AZ) | 2026-08-12 15:19 UTC | 2026-08-12 16:08 UTC | 48m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-12 15:50 UTC | 2026-08-12 16:07 UTC | 17m |
| MAFIA11 | MAF | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-08-12 15:47 UTC | 2026-08-12 16:06 UTC | 19m |
| N520MD |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-08-12 15:50 UTC | 2026-08-12 16:05 UTC | 15m |
| N5197R |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-08-12 15:53 UTC | 2026-08-12 16:05 UTC | 12m |
| N8533X |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-12 15:40 UTC | 2026-08-12 16:04 UTC | 23m |
| ANE22XP | ANE | Madrid Barajas International Airport (LEMD) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-12 14:39 UTC | 2026-08-12 16:03 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
