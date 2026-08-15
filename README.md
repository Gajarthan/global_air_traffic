# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_04:55:36_UTC-green)

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

**Latest saved flight:** 2026-08-15 04:55:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 04:55:36 UTC

- **197,560** saved flights
- **61,925** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,560** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,358,832.8 tonnes** estimated CO2 emissions
- **136,743,931 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7837 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3895 |
| 4 | IndiGo | 3402 |
| 5 | Southwest Airlines | 3068 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2344 |
| 9 | LATAM Airlines | 1856 |
| 10 | AZU | 1790 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1570 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1288 |
| 18 | EJU | 1222 |
| 19 | QLK | 1221 |
| 20 | All Nippon Airways | 1194 |
| 21 | Alaska Airlines | 1172 |
| 22 | VIV | 1091 |
| 23 | GLO | 1070 |
| 24 | Air France | 1034 |
| 25 | PGT | 1030 |
| 26 | AEE | 1013 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1005 |
| 29 | WMT | 986 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168123 |
| 2 | 🇪🇸 ES | 12719 |
| 3 | 🇧🇷 BR | 11379 |
| 4 | 🇦🇺 AU | 11108 |
| 5 | 🇨🇦 CA | 10833 |
| 6 | 🇮🇳 IN | 10634 |
| 7 | 🇮🇹 IT | 10271 |
| 8 | 🇩🇪 DE | 9778 |
| 9 | 🇬🇧 GB | 9252 |
| 10 | 🇯🇵 JP | 8046 |
| 11 | 🇫🇷 FR | 7846 |
| 12 | 🇨🇴 CO | 7801 |
| 13 | 🇬🇷 GR | 5791 |
| 14 | 🇲🇽 MX | 5604 |
| 15 | 🇹🇷 TR | 5388 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5044 |
| 18 | 🇲🇾 MY | 3367 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3255 |
| 21 | 🇹🇭 TH | 3057 |
| 22 | 🇳🇿 NZ | 2761 |
| 23 | 🇵🇭 PH | 2609 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2396 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1621 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2468 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2406 |
| 6 | Harry Reid International Airport |  | US | 2268 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2081 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1815 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1758 |
| 14 | Chicago O'Hare International Airport |  | US | 1736 |
| 15 | Congonhas Airport |  | BR | 1665 |
| 16 | Frankfurt am Main International Airport |  | DE | 1663 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1532 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1508 |
| 20 | Capua Airport |  | IT | 1506 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1458 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1376 |
| 24 | Malpensa International Airport |  | IT | 1369 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1257 |
| 28 | Bengaluru International Airport |  | IN | 1248 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1236 |
| 30 | Ninoy Aquino International Airport |  | PH | 1234 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1211 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1151 |
| 34 | Seattle-Tacoma International Airport |  | US | 1139 |
| 35 | Calgary International Airport |  | CA | 1126 |
| 36 | Reno/Tahoe International Airport |  | US | 1116 |
| 37 | Oslo Gardermoen Airport |  | NO | 1112 |
| 38 | Daniel K Inouye International Airport |  | US | 1100 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 727 | 21m | 244 km | 3,061.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 479 | 1h 7m | 770 km | 6,363.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 458 | 24m | 225 km | 1,776.8 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 305 | 1h 7m | 706 km | 3,713.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 285 | 1h 49m | 1,423 km | 6,994.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 281 | 22m | 55 km | 267.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 224 | 31m | 369 km | 1,425.8 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N23DD |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-15 04:14 UTC | 2026-08-15 04:55 UTC | 40m |
| MII | MII | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-15 04:26 UTC | 2026-08-15 04:40 UTC | 14m |
| VAR513 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 04:15 UTC | 2026-08-15 04:35 UTC | 20m |
| NPN | NPN | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-15 04:07 UTC | 2026-08-15 04:33 UTC | 26m |
| OZG | OZG | Southport Airport (YSPT) | Southport Airport (YSPT) | 2026-08-15 04:23 UTC | 2026-08-15 04:33 UTC | 9m |
| TQR | TQR | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-08-15 04:01 UTC | 2026-08-15 04:26 UTC | 25m |
| VAR512 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 04:19 UTC | 2026-08-15 04:26 UTC | 6m |
| FD614 |  | Perth Jandakot Airport (YPJT) | Carnarmah Airport (YCNH) | 2026-08-15 03:41 UTC | 2026-08-15 04:18 UTC | 37m |
| ERU52 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Scottsdale Airport (KSDL) | 2026-08-15 03:33 UTC | 2026-08-15 04:15 UTC | 42m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-08-15 03:37 UTC | 2026-08-15 04:09 UTC | 31m |
| FFAB123 | FFA | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-15 03:27 UTC | 2026-08-15 04:06 UTC | 39m |
| VAR512 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 03:26 UTC | 2026-08-15 04:05 UTC | 39m |
| VAR513 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 03:27 UTC | 2026-08-15 04:02 UTC | 34m |
| KDJ | KDJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-08-15 03:06 UTC | 2026-08-15 04:01 UTC | 54m |
| VAR496 | VAR | Phoenix Goodyear Airport (KGYR) | Chiriaco Summit Airport (KL77) | 2026-08-15 02:41 UTC | 2026-08-15 04:01 UTC | 1h 19m |
| A7GAC |  | Persian Gulf International Airport (OIBP) | Persian Gulf International Airport (OIBP) | 2026-08-15 04:00 UTC | 2026-08-15 04:00 UTC | 0m |
| VIV7283 | VIV | Xoxocotlan International Airport (MMOX) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-15 03:23 UTC | 2026-08-15 03:59 UTC | 36m |
| LBQ783 | LBQ | Orlando International Airport (KMCO) | Bird Field (FA11) | 2026-08-15 03:08 UTC | 2026-08-15 03:54 UTC | 45m |
|  |  | Futenma Marine Corps Air Station (ROTM) | Yoron Airport (RORY) | 2026-08-15 03:37 UTC | 2026-08-15 03:49 UTC | 12m |
| AXM346 | AXM | Kuala Lumpur International Airport (WMKK) | Cibeureum Airport (WICM) | 2026-08-15 01:54 UTC | 2026-08-15 03:48 UTC | 1h 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
