# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_00:56:41_UTC-green)

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

**Latest saved flight:** 2026-07-31 00:56:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 00:56:41 UTC

- **161,789** saved flights
- **53,382** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **161,789** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,939,547.3 tonnes** estimated CO2 emissions
- **112,437,524 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6463 |
| 2 | SkyWest Airlines | 5910 |
| 3 | EJA | 3209 |
| 4 | IndiGo | 2832 |
| 5 | American Airlines | 2560 |
| 6 | Southwest Airlines | 2537 |
| 7 | ENY | 2017 |
| 8 | Delta Air Lines | 1923 |
| 9 | LATAM Airlines | 1523 |
| 10 | Lufthansa | 1520 |
| 11 | AZU | 1422 |
| 12 | WIF | 1366 |
| 13 | Vueling | 1339 |
| 14 | LXJ | 1260 |
| 15 | AXM | 1123 |
| 16 | Swiss International | 1112 |
| 17 | easyJet | 1057 |
| 18 | Alaska Airlines | 1005 |
| 19 | QLK | 997 |
| 20 | EJU | 994 |
| 21 | All Nippon Airways | 993 |
| 22 | VIV | 891 |
| 23 | CXK | 864 |
| 24 | United Airlines | 855 |
| 25 | Cathay Pacific | 849 |
| 26 | GLO | 849 |
| 27 | AEE | 846 |
| 28 | MXY | 840 |
| 29 | Air France | 837 |
| 30 | JetBlue | 827 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 139910 |
| 2 | 🇪🇸 ES | 10348 |
| 3 | 🇧🇷 BR | 9248 |
| 4 | 🇦🇺 AU | 9136 |
| 5 | 🇮🇳 IN | 8912 |
| 6 | 🇨🇦 CA | 8803 |
| 7 | 🇮🇹 IT | 8325 |
| 8 | 🇩🇪 DE | 8140 |
| 9 | 🇬🇧 GB | 7413 |
| 10 | 🇯🇵 JP | 6547 |
| 11 | 🇫🇷 FR | 6391 |
| 12 | 🇨🇴 CO | 5755 |
| 13 | 🇲🇽 MX | 4650 |
| 14 | 🇬🇷 GR | 4634 |
| 15 | 🇳🇴 NO | 4267 |
| 16 | 🇨🇭 CH | 4231 |
| 17 | 🇹🇷 TR | 3853 |
| 18 | 🇲🇾 MY | 2918 |
| 19 | 🇵🇱 PL | 2742 |
| 20 | 🇿🇦 ZA | 2601 |
| 21 | 🇳🇿 NZ | 2376 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2124 |
| 24 | 🇰🇷 KR | 2115 |
| 25 | 🇬🇹 GT | 2077 |
| 26 | 🇲🇦 MA | 1629 |
| 27 | 🇲🇪 ME | 1527 |
| 28 | 🇭🇷 HR | 1508 |
| 29 | 🇳🇱 NL | 1480 |
| 30 | 🇲🇴 MO | 1341 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3309 |
| 2 | Denver International Airport |  | US | 2694 |
| 3 | Tokyo International Airport |  | JP | 2067 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1983 |
| 6 | Harry Reid International Airport |  | US | 1966 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1785 |
| 8 | Zurich Airport |  | CH | 1721 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1701 |
| 10 | La Aurora Airport |  | GT | 1613 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1506 |
| 12 | El Dorado International Airport |  | CO | 1482 |
| 13 | Frankfurt am Main International Airport |  | DE | 1471 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1353 |
| 17 | Congonhas Airport |  | BR | 1345 |
| 18 | Macau International Airport |  | MO | 1341 |
| 19 | Madrid Barajas International Airport |  | ES | 1278 |
| 20 | Capua Airport |  | IT | 1271 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1237 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1153 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1148 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1113 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1068 |
| 28 | Bengaluru International Airport |  | IN | 1059 |
| 29 | Ninoy Aquino International Airport |  | PH | 997 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 991 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 983 |
| 32 | Barcelona International Airport |  | ES | 958 |
| 33 | Daniel K Inouye International Airport |  | US | 950 |
| 34 | Seattle-Tacoma International Airport |  | US | 940 |
| 35 | Calgary International Airport |  | CA | 927 |
| 36 | Viracopos International Airport |  | BR | 921 |
| 37 | Tenerife Norte Airport |  | ES | 907 |
| 38 | Scottsdale Airport |  | US | 907 |
| 39 | Oslo Gardermoen Airport |  | NO | 897 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 589 | 21m | 244 km | 2,480.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 370 | 1h 9m | 770 km | 4,915.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 238 | 19m | 165 km | 677.0 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 238 | 22m | 55 km | 226.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 231 | 44m | 241 km | 959.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 196 | 30m | 49 km | 165.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 193 | 1h 15m | 961 km | 3,199.1 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 193 | 28m | 152 km | 504.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 181 | 1h 39m | 1,156 km | 3,610.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 178 | 44m | 452 km | 1,387.3 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 49m | 1,304 km | 3,892.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BCS516 | BCS | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-07-30 17:21 UTC | 2026-07-31 00:56 UTC | 7h 34m |
| R20658 |  | Blair Lake Airport (2AK1) | Ladd Army Air Field (PAFB) | 2026-07-31 00:23 UTC | 2026-07-31 00:50 UTC | 26m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-07-30 17:38 UTC | 2026-07-31 00:49 UTC | 7h 11m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Ocean City Municipal Airport (KOXB) | 2026-07-30 23:37 UTC | 2026-07-31 00:49 UTC | 1h 11m |
| N616PR |  | Portland-Hillsboro Airport (KHIO) | Redding Regional Airport (KRDD) | 2026-07-30 23:39 UTC | 2026-07-31 00:43 UTC | 1h 3m |
| RFS709 | RFS | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-07-30 23:59 UTC | 2026-07-31 00:43 UTC | 43m |
| N52789 |  | Oakland San Francisco Bay Airport (KOAK) | Sacramento Executive Airport (KSAC) | 2026-07-31 00:01 UTC | 2026-07-31 00:42 UTC | 41m |
| N958MG |  | Dubuque Regional Airport (KDBQ) | Turner Airport (4WI4) | 2026-07-31 00:05 UTC | 2026-07-31 00:42 UTC | 37m |
| N18LA |  | Whiteman Airport (KWHP) | Santa Monica Municipal Airport (KSMO) | 2026-07-31 00:13 UTC | 2026-07-31 00:42 UTC | 28m |
| AER180 | AER | King Salmon Airport (PAKN) | Homer Airport (PAHO) | 2026-07-30 23:54 UTC | 2026-07-31 00:41 UTC | 46m |
| N104LU |  | Boca Raton Airport (KBCT) | Orlando Executive Airport (KORL) | 2026-07-30 22:55 UTC | 2026-07-31 00:41 UTC | 1h 46m |
| URSA32 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-30 22:23 UTC | 2026-07-31 00:40 UTC | 2h 16m |
| TKR160 | TKR | Hill Afb Airport (KHIF) | Thunder Ridge Airpark (UT83) | 2026-07-31 00:18 UTC | 2026-07-31 00:39 UTC | 20m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-07-31 00:22 UTC | 2026-07-31 00:37 UTC | 14m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-07-30 20:08 UTC | 2026-07-31 00:36 UTC | 4h 28m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | Sanpete County Regional Airport (K41U) | 2026-07-31 00:14 UTC | 2026-07-31 00:36 UTC | 21m |
| TKR132 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-31 00:23 UTC | 2026-07-31 00:34 UTC | 11m |
| N654BH |  | Yolo County Airport (KDWA) | Palo Alto Airport (KPAO) | 2026-07-30 23:59 UTC | 2026-07-31 00:32 UTC | 33m |
| PRE388 | PRE | Imperial Municipal Airport (KIML) | Rocky Mountain Metro Airport (KBJC) | 2026-07-30 23:41 UTC | 2026-07-31 00:31 UTC | 49m |
| TKR102 | TKR | Coeur D'Alene/Pappy Boyington Field (KCOE) | Libby Airport (KS59) | 2026-07-31 00:16 UTC | 2026-07-31 00:29 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
