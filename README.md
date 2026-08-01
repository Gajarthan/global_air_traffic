# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_11:10:57_UTC-green)

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

**Latest saved flight:** 2026-08-01 11:10:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 11:10:57 UTC

- **164,235** saved flights
- **54,016** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,235** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,973,878.0 tonnes** estimated CO2 emissions
- **114,427,712 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6558 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2889 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2578 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1959 |
| 9 | LATAM Airlines | 1533 |
| 10 | Lufthansa | 1532 |
| 11 | AZU | 1439 |
| 12 | WIF | 1384 |
| 13 | Vueling | 1358 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1138 |
| 16 | Swiss International | 1128 |
| 17 | easyJet | 1077 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1006 |
| 21 | EJU | 1003 |
| 22 | VIV | 907 |
| 23 | CXK | 879 |
| 24 | Cathay Pacific | 873 |
| 25 | United Airlines | 865 |
| 26 | AEE | 861 |
| 27 | GLO | 858 |
| 28 | Air France | 850 |
| 29 | MXY | 846 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141819 |
| 2 | 🇪🇸 ES | 10509 |
| 3 | 🇧🇷 BR | 9355 |
| 4 | 🇦🇺 AU | 9253 |
| 5 | 🇮🇳 IN | 9074 |
| 6 | 🇨🇦 CA | 8940 |
| 7 | 🇮🇹 IT | 8464 |
| 8 | 🇩🇪 DE | 8224 |
| 9 | 🇬🇧 GB | 7543 |
| 10 | 🇯🇵 JP | 6637 |
| 11 | 🇫🇷 FR | 6503 |
| 12 | 🇨🇴 CO | 5866 |
| 13 | 🇬🇷 GR | 4729 |
| 14 | 🇲🇽 MX | 4705 |
| 15 | 🇳🇴 NO | 4330 |
| 16 | 🇨🇭 CH | 4318 |
| 17 | 🇹🇷 TR | 3926 |
| 18 | 🇲🇾 MY | 2961 |
| 19 | 🇵🇱 PL | 2785 |
| 20 | 🇿🇦 ZA | 2679 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2351 |
| 23 | 🇵🇭 PH | 2164 |
| 24 | 🇰🇷 KR | 2129 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1656 |
| 27 | 🇭🇷 HR | 1548 |
| 28 | 🇲🇪 ME | 1540 |
| 29 | 🇳🇱 NL | 1491 |
| 30 | 🇲🇴 MO | 1389 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2090 |
| 4 | Guaymaral Airport |  | CO | 2063 |
| 5 | Indira Gandhi International Airport |  | IN | 2012 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1810 |
| 8 | Zurich Airport |  | CH | 1748 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1504 |
| 13 | Frankfurt am Main International Airport |  | DE | 1488 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1478 |
| 16 | Macau International Airport |  | MO | 1389 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1378 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1296 |
| 20 | Capua Airport |  | IT | 1287 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1161 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Charles de Gaulle International Airport |  | FR | 1123 |
| 26 | Kuala Lumpur International Airport |  | MY | 1122 |
| 27 | Malpensa International Airport |  | IT | 1085 |
| 28 | Bengaluru International Airport |  | IN | 1077 |
| 29 | Ninoy Aquino International Airport |  | PH | 1017 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 971 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 930 |
| 37 | Tenerife Norte Airport |  | ES | 917 |
| 38 | Scottsdale Airport |  | US | 917 |
| 39 | Oslo Gardermoen Airport |  | NO | 916 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 375 | 1h 9m | 770 km | 4,981.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 306 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 244 | 22m | 55 km | 231.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 214 | 26m | 215 km | 792.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 210 | 20m | 250 km | 907.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 208 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 193 | 18m | 144 km | 480.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N552TJ |  | 0PA7 (0PA7) | South Jersey Regional Airport (KVAY) | 2026-08-01 10:59 UTC | 2026-08-01 11:10 UTC | 11m |
| ANA266 | All Nippon Airways | Fukuoka Airport (RJFF) | Tokyo International Airport (RJTT) | 2026-08-01 09:44 UTC | 2026-08-01 11:05 UTC | 1h 21m |
| C2 |  | Ottenschlag Airport (LOAA) | Krems Airport (LOAG) | 2026-08-01 11:00 UTC | 2026-08-01 11:04 UTC | 4m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-08-01 10:49 UTC | 2026-08-01 11:01 UTC | 11m |
| N203BH |  | Francisco de Sá Carneiro Airport (LPPR) | A Coruna Airport (LECO) | 2026-08-01 10:33 UTC | 2026-08-01 11:01 UTC | 28m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-08-01 10:43 UTC | 2026-08-01 11:00 UTC | 16m |
| N782AL |  | Centennial Airport (KAPA) | Four Corners Regional Airport (KFMN) | 2026-08-01 10:04 UTC | 2026-08-01 10:58 UTC | 53m |
| DMCFC | DMC | Augsburg Airport (EDMA) | Hoefen Airport (LOIR) | 2026-08-01 09:52 UTC | 2026-08-01 10:51 UTC | 59m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-01 10:18 UTC | 2026-08-01 10:46 UTC | 28m |
| UAL145 | United Airlines | Washington Dulles International Airport (KIAD) | Barcelona International Airport (LEBL) | 2026-07-31 22:08 UTC | 2026-08-01 10:46 UTC | 12h 37m |
| EAI2DM | EAI | Cork Airport (EICK) | Bristol International Airport (EGGD) | 2026-08-01 09:41 UTC | 2026-08-01 10:43 UTC | 1h 1m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-01 10:09 UTC | 2026-08-01 10:41 UTC | 31m |
| CSN6386 | China Southern | Shenzhen Bao'an International Airport (ZGSZ) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-01 02:34 UTC | 2026-08-01 10:40 UTC | 8h 5m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-01 10:29 UTC | 2026-08-01 10:39 UTC | 10m |
| AXM393 | AXM | Kuala Lumpur International Airport (WMKK) | Tebing Tinggi Airport (WIMT) | 2026-08-01 10:03 UTC | 2026-08-01 10:29 UTC | 26m |
| DFPAR | DFP | Johannisberg Airport (ESSX) | Johannisberg Airport (ESSX) | 2026-08-01 09:56 UTC | 2026-08-01 10:26 UTC | 29m |
| N102TP |  | Pecos Municipal Airport (KPEQ) | 2XA0 (2XA0) | 2026-08-01 09:26 UTC | 2026-08-01 10:25 UTC | 59m |
| RYR7SY | Ryanair | Poznań-Ławica Airport (EPPO) | Otocac Airport (LDRO) | 2026-08-01 09:14 UTC | 2026-08-01 10:25 UTC | 1h 10m |
| RYR77HE | Ryanair | Ciampino Airport (LIRA) | Vilnius International Airport (EYVI) | 2026-08-01 08:13 UTC | 2026-08-01 10:25 UTC | 2h 11m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-08-01 09:38 UTC | 2026-08-01 10:24 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
