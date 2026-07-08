# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_10:29:36_UTC-green)

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

**Latest saved flight:** 2026-07-08 10:29:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-08 10:29:36 UTC

- **132,940** saved flights
- **45,076** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **132,940** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,600,583.2 tonnes** estimated CO2 emissions
- **92,787,431 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5394 |
| 2 | SkyWest Airlines | 4906 |
| 3 | EJA | 2607 |
| 4 | IndiGo | 2483 |
| 5 | American Airlines | 2077 |
| 6 | Southwest Airlines | 2000 |
| 7 | ENY | 1669 |
| 8 | Delta Air Lines | 1591 |
| 9 | Lufthansa | 1381 |
| 10 | LATAM Airlines | 1223 |
| 11 | Vueling | 1164 |
| 12 | WIF | 1157 |
| 13 | AZU | 1128 |
| 14 | LXJ | 1020 |
| 15 | AXM | 1017 |
| 16 | Swiss International | 944 |
| 17 | All Nippon Airways | 871 |
| 18 | easyJet | 851 |
| 19 | Alaska Airlines | 845 |
| 20 | QLK | 830 |
| 21 | EJU | 817 |
| 22 | VIV | 734 |
| 23 | AEE | 723 |
| 24 | Air France | 718 |
| 25 | Cathay Pacific | 718 |
| 26 | CXK | 713 |
| 27 | United Airlines | 705 |
| 28 | JetBlue | 700 |
| 29 | MXY | 687 |
| 30 | GLO | 680 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 113926 |
| 2 | 🇪🇸 ES | 8826 |
| 3 | 🇮🇳 IN | 7777 |
| 4 | 🇦🇺 AU | 7692 |
| 5 | 🇧🇷 BR | 7491 |
| 6 | 🇨🇦 CA | 7028 |
| 7 | 🇩🇪 DE | 6949 |
| 8 | 🇮🇹 IT | 6920 |
| 9 | 🇬🇧 GB | 5938 |
| 10 | 🇯🇵 JP | 5713 |
| 11 | 🇫🇷 FR | 5277 |
| 12 | 🇨🇴 CO | 4167 |
| 13 | 🇲🇽 MX | 3877 |
| 14 | 🇬🇷 GR | 3809 |
| 15 | 🇳🇴 NO | 3599 |
| 16 | 🇨🇭 CH | 3436 |
| 17 | 🇹🇷 TR | 2991 |
| 18 | 🇲🇾 MY | 2643 |
| 19 | 🇿🇦 ZA | 2189 |
| 20 | 🇵🇱 PL | 2189 |
| 21 | 🇳🇿 NZ | 2097 |
| 22 | 🇹🇭 TH | 2049 |
| 23 | 🇰🇷 KR | 1972 |
| 24 | 🇵🇭 PH | 1830 |
| 25 | 🇬🇹 GT | 1808 |
| 26 | 🇲🇦 MA | 1411 |
| 27 | 🇲🇪 ME | 1319 |
| 28 | 🇳🇱 NL | 1249 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2771 |
| 2 | Denver International Airport |  | US | 2250 |
| 3 | Tokyo International Airport |  | JP | 1869 |
| 4 | Indira Gandhi International Airport |  | IN | 1718 |
| 5 | Harry Reid International Airport |  | US | 1649 |
| 6 | Guaymaral Airport |  | CO | 1621 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1562 |
| 8 | Zurich Airport |  | CH | 1480 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1412 |
| 10 | La Aurora Airport |  | GT | 1396 |
| 11 | Frankfurt am Main International Airport |  | DE | 1338 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1282 |
| 13 | Chicago O'Hare International Airport |  | US | 1275 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1184 |
| 16 | Salt Lake City International Airport |  | US | 1181 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1151 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1089 |
| 19 | Madrid Barajas International Airport |  | ES | 1086 |
| 20 | Capua Airport |  | IT | 1084 |
| 21 | Congonhas Airport |  | BR | 1061 |
| 22 | Kuala Lumpur International Airport |  | MY | 1028 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 966 |
| 25 | Charles de Gaulle International Airport |  | FR | 957 |
| 26 | Bengaluru International Airport |  | IN | 936 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 911 |
| 28 | Malpensa International Airport |  | IT | 882 |
| 29 | Ninoy Aquino International Airport |  | PH | 850 |
| 30 | Daniel K Inouye International Airport |  | US | 830 |
| 31 | Barcelona International Airport |  | ES | 817 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 812 |
| 33 | Tenerife Norte Airport |  | ES | 799 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 781 |
| 35 | Calgary International Airport |  | CA | 775 |
| 36 | Seattle-Tacoma International Airport |  | US | 766 |
| 37 | Scottsdale Airport |  | US | 761 |
| 38 | Viracopos International Airport |  | BR | 757 |
| 39 | Vitoria/Foronda Airport |  | ES | 757 |
| 40 | Amsterdam Airport Schiphol |  | NL | 751 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 681 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 482 | 21m | 244 km | 2,029.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 333 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 321 | 1h 10m | 770 km | 4,264.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 250 | 26m | 275 km | 1,184.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 242 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 194 | 22m | 55 km | 184.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 185 | 44m | 241 km | 768.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 165 | 31m | 369 km | 1,050.3 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 159 | 44m | 452 km | 1,239.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N472LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-08 08:49 UTC | 2026-07-08 10:29 UTC | 1h 39m |
| UAY93 | UAY | DCAE Cosford Airport (EGWC) | DCAE Cosford Airport (EGWC) | 2026-07-08 10:05 UTC | 2026-07-08 10:29 UTC | 23m |
| UPS1014 | UPS | Louisville Muhammad Ali International Airport (KSDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-08 08:34 UTC | 2026-07-08 10:21 UTC | 1h 47m |
| SERCE44 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-07-08 10:00 UTC | 2026-07-08 10:18 UTC | 17m |
| 340 |  | LL1A (LL1A) | LL1A (LL1A) | 2026-07-08 10:08 UTC | 2026-07-08 10:16 UTC | 8m |
| SERCE34 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-07-08 09:58 UTC | 2026-07-08 10:13 UTC | 15m |
| EFC58U | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-07-08 09:53 UTC | 2026-07-08 10:10 UTC | 17m |
| RYR3DZ | Ryanair | Shannon Airport (EINN) | Lanzarote Airport (GCRR) | 2026-07-08 06:41 UTC | 2026-07-08 10:10 UTC | 3h 29m |
| FDX1704 | FDX | Indianapolis International Airport (KIND) | Philadelphia International Airport (KPHL) | 2026-07-08 08:54 UTC | 2026-07-08 10:06 UTC | 1h 12m |
| CFH24 | CFH | Coffs Harbour Airport (YSCH) | Wollomombi Airport (YWMM) | 2026-07-08 09:49 UTC | 2026-07-08 10:06 UTC | 17m |
| SERCE39 | SER | Yalova Airport (LTBP) | Yalova Airport (LTBP) | 2026-07-08 09:52 UTC | 2026-07-08 09:57 UTC | 4m |
| DFALB | DFA | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-07-08 09:15 UTC | 2026-07-08 09:56 UTC | 41m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-07-08 09:06 UTC | 2026-07-08 09:53 UTC | 46m |
| HBZZV | HBZ | Sion Airport (LSGS) | Raron Airport (LSTA) | 2026-07-08 09:34 UTC | 2026-07-08 09:49 UTC | 15m |
| IBB18XQ | IBB | Gran Canaria Airport (GCLP) | Federico Garcia Lorca Airport (LEGR) | 2026-07-08 07:55 UTC | 2026-07-08 09:46 UTC | 1h 51m |
| HKS40 | HKS | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-07-08 09:16 UTC | 2026-07-08 09:43 UTC | 26m |
| QTR61E | Qatar Airways | Hamad International Airport (OTHH) | UKFB (UKFB) | 2026-07-08 05:32 UTC | 2026-07-08 09:40 UTC | 4h 8m |
| DEFUK | DEF | Bayreuth Airport (EDQD) | Hasfurt-Schweinfurt Airport (EDQT) | 2026-07-08 09:06 UTC | 2026-07-08 09:40 UTC | 33m |
| CES2036 | China Eastern | VGZR (VGZR) | VYNT (VYNT) | 2026-07-08 08:35 UTC | 2026-07-08 09:38 UTC | 1h 3m |
| CES9620 | China Eastern | Chiang Mai International Airport (VTCC) | Ban Huoeisay Airport (VLHS) | 2026-07-08 09:18 UTC | 2026-07-08 09:38 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
