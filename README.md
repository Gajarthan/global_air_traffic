# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_19:50:55_UTC-green)

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

**Latest saved flight:** 2026-08-13 19:50:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 19:50:55 UTC

- **193,398** saved flights
- **60,850** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **193,398** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,311,858.4 tonnes** estimated CO2 emissions
- **134,020,779 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7691 |
| 2 | SkyWest Airlines | 6980 |
| 3 | EJA | 3811 |
| 4 | IndiGo | 3343 |
| 5 | Southwest Airlines | 3009 |
| 6 | American Airlines | 2993 |
| 7 | ENY | 2396 |
| 8 | Delta Air Lines | 2284 |
| 9 | LATAM Airlines | 1815 |
| 10 | AZU | 1745 |
| 11 | Lufthansa | 1673 |
| 12 | Vueling | 1612 |
| 13 | WIF | 1602 |
| 14 | LXJ | 1527 |
| 15 | easyJet | 1336 |
| 16 | Swiss International | 1315 |
| 17 | AXM | 1258 |
| 18 | EJU | 1191 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1146 |
| 22 | VIV | 1064 |
| 23 | GLO | 1041 |
| 24 | Air France | 1011 |
| 25 | PGT | 1004 |
| 26 | AEE | 991 |
| 27 | CXK | 989 |
| 28 | United Airlines | 988 |
| 29 | WMT | 963 |
| 30 | Wizz Air | 961 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 164638 |
| 2 | 🇪🇸 ES | 12490 |
| 3 | 🇧🇷 BR | 11119 |
| 4 | 🇦🇺 AU | 10812 |
| 5 | 🇨🇦 CA | 10584 |
| 6 | 🇮🇳 IN | 10467 |
| 7 | 🇮🇹 IT | 10056 |
| 8 | 🇩🇪 DE | 9582 |
| 9 | 🇬🇧 GB | 9055 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7727 |
| 12 | 🇨🇴 CO | 7511 |
| 13 | 🇬🇷 GR | 5663 |
| 14 | 🇲🇽 MX | 5471 |
| 15 | 🇹🇷 TR | 5210 |
| 16 | 🇨🇭 CH | 5205 |
| 17 | 🇳🇴 NO | 4961 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3184 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2463 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 2008 |
| 27 | 🇲🇦 MA | 1962 |
| 28 | 🇳🇱 NL | 1739 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4018 |
| 2 | Denver International Airport |  | US | 3170 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2405 |
| 5 | Indira Gandhi International Airport |  | IN | 2358 |
| 6 | Harry Reid International Airport |  | US | 2242 |
| 7 | Zurich Airport |  | CH | 2052 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2043 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2000 |
| 10 | La Aurora Airport |  | GT | 1894 |
| 11 | El Dorado International Airport |  | CO | 1757 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1738 |
| 13 | Salt Lake City International Airport |  | US | 1723 |
| 14 | Chicago O'Hare International Airport |  | US | 1693 |
| 15 | Frankfurt am Main International Airport |  | DE | 1639 |
| 16 | Congonhas Airport |  | BR | 1619 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1526 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1489 |
| 20 | Capua Airport |  | IT | 1489 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1428 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1388 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1343 |
| 24 | Malpensa International Airport |  | IT | 1339 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1288 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1206 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1181 |
| 32 | Barcelona International Airport |  | ES | 1158 |
| 33 | Viracopos International Airport |  | BR | 1124 |
| 34 | Seattle-Tacoma International Airport |  | US | 1107 |
| 35 | Calgary International Airport |  | CA | 1105 |
| 36 | Reno/Tahoe International Airport |  | US | 1102 |
| 37 | Oslo Gardermoen Airport |  | NO | 1086 |
| 38 | Daniel K Inouye International Airport |  | US | 1082 |
| 39 | Tenerife Norte Airport |  | ES | 1061 |
| 40 | Vitoria/Foronda Airport |  | ES | 1060 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 994 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 710 | 21m | 244 km | 2,989.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 454 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 317 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 288 | 44m | 241 km | 1,196.3 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 242 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 237 | 24m | 218 km | 892.9 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 235 | 1h 15m | 961 km | 3,895.2 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 235 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 209 | 1h 48m | 1,304 km | 4,702.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VVAJ712 | VVA | Jacksonville Nas (Towers Field) Airport (KNIP) | Whitehouse Nolf Airport (KNEN) | 2026-08-13 19:35 UTC | 2026-08-13 19:50 UTC | 15m |
| N250RM |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-08-13 19:28 UTC | 2026-08-13 19:49 UTC | 20m |
| N982LF |  | Worcester Regional Airport (KORH) | Southbridge Municipal Airport (K3B0) | 2026-08-13 19:35 UTC | 2026-08-13 19:49 UTC | 14m |
| DLH39E | Lufthansa | Thessaloniki Macedonia International Airport (LGTS) | Frankfurt am Main International Airport (EDDF) | 2026-08-13 17:36 UTC | 2026-08-13 19:45 UTC | 2h 9m |
| GOLEM21 | GOL | 75OK (75OK) | Cherokee Municipal Airport (K4O5) | 2026-08-13 19:20 UTC | 2026-08-13 19:43 UTC | 23m |
| N8328D |  | Chesapeake Regional Airport (KCPK) | Currituck County Regional Airport (KONX) | 2026-08-13 18:45 UTC | 2026-08-13 19:39 UTC | 54m |
| THY8EV | Turkish Airlines | Antalya International Airport (LTAI) | Pskov Airport (ULOO) | 2026-08-13 16:42 UTC | 2026-08-13 19:37 UTC | 2h 55m |
| TKR40 | TKR | Casper/Natrona County International Airport (KCPR) | 46CO (46CO) | 2026-08-13 18:36 UTC | 2026-08-13 19:36 UTC | 59m |
| N509FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-13 19:07 UTC | 2026-08-13 19:34 UTC | 27m |
| N404YZ |  | Crystal Airport (KMIC) | Flying Cloud Airport (KFCM) | 2026-08-13 18:36 UTC | 2026-08-13 19:33 UTC | 56m |
| ES805 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-08-13 18:56 UTC | 2026-08-13 19:30 UTC | 34m |
| N207JB |  | Moffett Federal Airfield (KNUQ) | Van Nuys Airport (KVNY) | 2026-08-13 18:44 UTC | 2026-08-13 19:30 UTC | 46m |
| N7057Q |  | Council Bluffs Municipal Airport (KCBF) | Ridge Airport (IA01) | 2026-08-13 19:14 UTC | 2026-08-13 19:30 UTC | 15m |
| N584CC |  | NJ58 (NJ58) | NJ58 (NJ58) | 2026-08-13 19:29 UTC | 2026-08-13 19:30 UTC | 1m |
| BOE101 | BOE | Boeing Field/King County International Airport (KBFI) | OR73 (OR73) | 2026-08-13 17:57 UTC | 2026-08-13 19:29 UTC | 1h 31m |
| N4641P |  | Jirik Field (OL23) | Flying G Ranch Airport (3OK8) | 2026-08-13 19:03 UTC | 2026-08-13 19:28 UTC | 25m |
| ES803 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-08-13 18:54 UTC | 2026-08-13 19:28 UTC | 33m |
| N28DC |  | Shannon Airport (EINN) | Bangor International Airport (KBGR) | 2026-08-13 13:41 UTC | 2026-08-13 19:26 UTC | 5h 45m |
| N2884U |  | Sky Ranch Airport (TN98) | Landing At River's Edge Airport (98TN) | 2026-08-13 18:59 UTC | 2026-08-13 19:26 UTC | 26m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | 6CO3 (6CO3) | 2026-08-13 19:08 UTC | 2026-08-13 19:26 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
