# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_14:45:09_UTC-green)

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

**Latest saved flight:** 2026-08-16 14:45:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 14:45:09 UTC

- **204,808** saved flights
- **65,434** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,808** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,462,658.7 tonnes** estimated CO2 emissions
- **142,762,821 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8070 |
| 2 | SkyWest Airlines | 7354 |
| 3 | EJA | 3958 |
| 4 | IndiGo | 3508 |
| 5 | American Airlines | 3404 |
| 6 | Southwest Airlines | 3305 |
| 7 | Delta Air Lines | 2618 |
| 8 | ENY | 2549 |
| 9 | LATAM Airlines | 1918 |
| 10 | AZU | 1848 |
| 11 | Lufthansa | 1744 |
| 12 | Vueling | 1697 |
| 13 | WIF | 1648 |
| 14 | LXJ | 1608 |
| 15 | easyJet | 1416 |
| 16 | Swiss International | 1366 |
| 17 | AXM | 1338 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1253 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1126 |
| 24 | GLO | 1098 |
| 25 | Air France | 1094 |
| 26 | PGT | 1091 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1047 |
| 29 | WMT | 1024 |
| 30 | CXK | 1012 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173966 |
| 2 | 🇪🇸 ES | 13099 |
| 3 | 🇧🇷 BR | 11698 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11294 |
| 6 | 🇮🇳 IN | 10949 |
| 7 | 🇮🇹 IT | 10657 |
| 8 | 🇩🇪 DE | 10136 |
| 9 | 🇬🇧 GB | 9563 |
| 10 | 🇯🇵 JP | 8452 |
| 11 | 🇫🇷 FR | 8116 |
| 12 | 🇨🇴 CO | 8075 |
| 13 | 🇬🇷 GR | 6030 |
| 14 | 🇹🇷 TR | 5784 |
| 15 | 🇲🇽 MX | 5754 |
| 16 | 🇨🇭 CH | 5488 |
| 17 | 🇳🇴 NO | 5105 |
| 18 | 🇲🇾 MY | 3527 |
| 19 | 🇿🇦 ZA | 3440 |
| 20 | 🇵🇱 PL | 3375 |
| 21 | 🇹🇭 TH | 3242 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2566 |
| 25 | 🇰🇷 KR | 2503 |
| 26 | 🇭🇷 HR | 2188 |
| 27 | 🇲🇦 MA | 2061 |
| 28 | 🇳🇱 NL | 1828 |
| 29 | 🇲🇪 ME | 1714 |
| 30 | 🇮🇩 ID | 1684 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4291 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2549 |
| 4 | Indira Gandhi International Airport |  | IN | 2483 |
| 5 | Guaymaral Airport |  | CO | 2481 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2142 |
| 8 | Zurich Airport |  | CH | 2137 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2121 |
| 10 | La Aurora Airport |  | GT | 1964 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1867 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1809 |
| 15 | Congonhas Airport |  | BR | 1704 |
| 16 | Frankfurt am Main International Airport |  | DE | 1699 |
| 17 | Madrid Barajas International Airport |  | ES | 1604 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1565 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1554 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1478 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1409 |
| 25 | Charles de Gaulle International Airport |  | FR | 1402 |
| 26 | Charlotte/Douglas International Airport |  | US | 1393 |
| 27 | Kuala Lumpur International Airport |  | MY | 1307 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1272 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1260 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1222 |
| 33 | Seattle-Tacoma International Airport |  | US | 1216 |
| 34 | Viracopos International Airport |  | BR | 1186 |
| 35 | Calgary International Airport |  | CA | 1158 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Vitoria/Foronda Airport |  | ES | 1130 |
| 38 | Oslo Gardermoen Airport |  | NO | 1129 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1021 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 343 | 27m | 275 km | 1,625.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 301 | 44m | 241 km | 1,250.3 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 254 | 24m | 218 km | 956.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 246 | 19m | 99 km | 421.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 240 | 1h 37m | 1,156 km | 4,787.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 217 | 28m | 152 km | 567.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9287M |  | Westchester County Airport (KHPN) | Tweed/New Haven Airport (KHVN) | 2026-08-16 14:05 UTC | 2026-08-16 14:45 UTC | 39m |
| N515TW |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-16 14:14 UTC | 2026-08-16 14:43 UTC | 28m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-16 14:24 UTC | 2026-08-16 14:39 UTC | 14m |
| BEL3CP | Brussels Airlines | Brussels Airport (EBBR) | Francisco de Sá Carneiro Airport (LPPR) | 2026-08-16 12:37 UTC | 2026-08-16 14:39 UTC | 2h 2m |
| DMPFB | DMP | Bohlen Airport (EDOE) | Bohlen Airport (EDOE) | 2026-08-16 14:19 UTC | 2026-08-16 14:38 UTC | 18m |
| N41DZ |  | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-08-16 14:22 UTC | 2026-08-16 14:37 UTC | 14m |
| OUA6 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Gregg Airport (7OK1) | 2026-08-16 13:51 UTC | 2026-08-16 14:35 UTC | 43m |
| FFY592 | FFY | St Augustine Airport (KSGJ) | St Augustine Airport (KSGJ) | 2026-08-16 14:18 UTC | 2026-08-16 14:35 UTC | 16m |
| N21ME |  | K8A0 (K8A0) | Boone Inc Airport (NC14) | 2026-08-16 13:56 UTC | 2026-08-16 14:32 UTC | 35m |
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 13:58 UTC | 2026-08-16 14:30 UTC | 31m |
| SLH814 | SLH | Lincoln Airport (KLNK) | Ohkay Owingeh Airport (KE14) | 2026-08-16 12:43 UTC | 2026-08-16 14:18 UTC | 1h 35m |
| N330V |  | Cy Nunnally Memorial Airport (KD73) | Kintail Farm Airport (GA00) | 2026-08-16 14:07 UTC | 2026-08-16 14:18 UTC | 10m |
| N105CD |  | Boyd Field (NC49) | Auburn University Regional Airport (KAUO) | 2026-08-16 13:03 UTC | 2026-08-16 14:16 UTC | 1h 12m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-16 13:59 UTC | 2026-08-16 14:16 UTC | 16m |
| N490LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-08-16 13:12 UTC | 2026-08-16 14:16 UTC | 1h 3m |
| TGJOE | TGJ | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-16 13:47 UTC | 2026-08-16 14:16 UTC | 28m |
| SWR2BK | Swiss International | Zurich Airport (LSZH) | Sintra Airport (LPST) | 2026-08-16 11:45 UTC | 2026-08-16 14:14 UTC | 2h 28m |
| N306SR |  | North Fork Valley Airport (K7V2) | Lake County Airport (KLXV) | 2026-08-16 13:35 UTC | 2026-08-16 14:10 UTC | 35m |
| N3040F |  | Greeneville Municipal Airport (KGCY) | Greeneville Municipal Airport (KGCY) | 2026-08-16 13:59 UTC | 2026-08-16 14:10 UTC | 11m |
| UAE62P | Emirates | Dubai International Airport (OMDB) | Melbourne International Airport (YMML) | 2026-08-16 01:28 UTC | 2026-08-16 14:09 UTC | 12h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
