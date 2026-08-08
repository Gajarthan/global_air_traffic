# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_03:16:50_UTC-green)

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

**Latest saved flight:** 2026-08-08 03:16:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 03:16:50 UTC

- **177,320** saved flights
- **57,098** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,320** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,130,929.1 tonnes** estimated CO2 emissions
- **123,532,120 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7015 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3506 |
| 4 | IndiGo | 3104 |
| 5 | Southwest Airlines | 2799 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1644 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1580 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1200 |
| 17 | AXM | 1198 |
| 18 | QLK | 1084 |
| 19 | EJU | 1082 |
| 20 | Alaska Airlines | 1077 |
| 21 | All Nippon Airways | 1073 |
| 22 | VIV | 976 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 942 |
| 25 | GLO | 937 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 894 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152640 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10129 |
| 4 | 🇦🇺 AU | 10010 |
| 5 | 🇮🇳 IN | 9727 |
| 6 | 🇨🇦 CA | 9720 |
| 7 | 🇮🇹 IT | 9143 |
| 8 | 🇩🇪 DE | 8742 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7110 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6524 |
| 13 | 🇬🇷 GR | 5151 |
| 14 | 🇲🇽 MX | 5083 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4401 |
| 18 | 🇲🇾 MY | 3124 |
| 19 | 🇵🇱 PL | 2940 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2630 |
| 22 | 🇳🇿 NZ | 2574 |
| 23 | 🇵🇭 PH | 2338 |
| 24 | 🇬🇹 GT | 2266 |
| 25 | 🇰🇷 KR | 2210 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1741 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2216 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2161 |
| 6 | Harry Reid International Airport |  | US | 2112 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1914 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1743 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1626 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1589 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1470 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1427 |
| 19 | Capua Airport |  | IT | 1383 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1252 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1240 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1177 |
| 28 | Bengaluru International Airport |  | IN | 1157 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1100 |
| 30 | Ninoy Aquino International Airport |  | PH | 1100 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1097 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1025 |
| 34 | Daniel K Inouye International Airport |  | US | 1020 |
| 35 | Viracopos International Airport |  | BR | 1015 |
| 36 | Calgary International Airport |  | CA | 1011 |
| 37 | Reno/Tahoe International Airport |  | US | 1010 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 650 | 21m | 244 km | 2,737.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 415 | 24m | 225 km | 1,610.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 408 | 1h 8m | 770 km | 5,420.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 219 | 20m | 99 km | 375.1 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 193 | 1h 2m | 695 km | 2,313.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 021464 |  | Redding Regional Airport (KRDD) | CA38 (CA38) | 2026-08-08 02:54 UTC | 2026-08-08 03:16 UTC | 22m |
| MAFFS4 | MAF | Redding Regional Airport (KRDD) | CA38 (CA38) | 2026-08-08 02:47 UTC | 2026-08-08 03:12 UTC | 24m |
| N343KT |  | Fort Crosby Airport (8AK5) | Nugget Bench Airport (33AK) | 2026-08-08 02:48 UTC | 2026-08-08 03:10 UTC | 21m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-08-08 02:59 UTC | 2026-08-08 03:09 UTC | 10m |
| FRLD51 | FRL | Redding Regional Airport (KRDD) | CA38 (CA38) | 2026-08-08 02:44 UTC | 2026-08-08 03:09 UTC | 25m |
| N6036Y |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-08-08 02:09 UTC | 2026-08-08 03:09 UTC | 59m |
| PKRJS | PKR | Halim Perdanakusuma International Airport (WIHH) | Halim Perdanakusuma International Airport (WIHH) | 2026-08-08 02:59 UTC | 2026-08-08 03:07 UTC | 7m |
| N424KT |  | Mc Kinley Country Airport (81AK) | Helio Airport (2AK7) | 2026-08-08 02:45 UTC | 2026-08-08 03:05 UTC | 20m |
| N465DF |  | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-08 02:37 UTC | 2026-08-08 03:03 UTC | 25m |
| ZFN | ZFN | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-08 02:25 UTC | 2026-08-08 03:01 UTC | 36m |
| HGB383 | HGB | Fukuoka Airport (RJFF) | Chek Lap Kok International Airport (VHHH) | 2026-08-08 00:00 UTC | 2026-08-08 03:01 UTC | 3h 0m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-08 02:14 UTC | 2026-08-08 02:58 UTC | 44m |
| ASA1250 | Alaska Airlines | Bradshaw Army Airfield (PHSF) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-08 02:42 UTC | 2026-08-08 02:57 UTC | 15m |
| TOG923 | TOG | 6CL6 (6CL6) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-08 02:29 UTC | 2026-08-08 02:57 UTC | 27m |
| N88765 |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-08 02:25 UTC | 2026-08-08 02:54 UTC | 29m |
| CXK448 | CXK | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-08-08 02:04 UTC | 2026-08-08 02:47 UTC | 42m |
| BBC535 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-08 02:19 UTC | 2026-08-08 02:44 UTC | 25m |
| IGO6190 | IndiGo | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-08-08 02:23 UTC | 2026-08-08 02:43 UTC | 20m |
| ANX1204 | ANX | Licenciado Benito Juarez International Airport (MMMX) | Chilpancingo Airport (MMCH) | 2026-08-08 02:20 UTC | 2026-08-08 02:41 UTC | 21m |
| JAL2823 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-08-08 01:49 UTC | 2026-08-08 02:41 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
