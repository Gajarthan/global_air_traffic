# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_00:53:14_UTC-green)

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

**Latest saved flight:** 2026-07-09 00:53:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 00:53:14 UTC

- **133,655** saved flights
- **45,273** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,655** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,608,586.0 tonnes** estimated CO2 emissions
- **93,251,365 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5424 |
| 2 | SkyWest Airlines | 4937 |
| 3 | EJA | 2623 |
| 4 | IndiGo | 2487 |
| 5 | American Airlines | 2090 |
| 6 | Southwest Airlines | 2009 |
| 7 | ENY | 1681 |
| 8 | Delta Air Lines | 1599 |
| 9 | Lufthansa | 1383 |
| 10 | LATAM Airlines | 1227 |
| 11 | Vueling | 1171 |
| 12 | WIF | 1162 |
| 13 | AZU | 1137 |
| 14 | LXJ | 1026 |
| 15 | AXM | 1020 |
| 16 | Swiss International | 946 |
| 17 | All Nippon Airways | 872 |
| 18 | easyJet | 861 |
| 19 | Alaska Airlines | 850 |
| 20 | QLK | 836 |
| 21 | EJU | 821 |
| 22 | VIV | 738 |
| 23 | AEE | 725 |
| 24 | Cathay Pacific | 719 |
| 25 | CXK | 719 |
| 26 | Air France | 718 |
| 27 | United Airlines | 709 |
| 28 | JetBlue | 705 |
| 29 | MXY | 693 |
| 30 | GLO | 681 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114719 |
| 2 | 🇪🇸 ES | 8866 |
| 3 | 🇮🇳 IN | 7796 |
| 4 | 🇦🇺 AU | 7741 |
| 5 | 🇧🇷 BR | 7524 |
| 6 | 🇨🇦 CA | 7056 |
| 7 | 🇩🇪 DE | 6965 |
| 8 | 🇮🇹 IT | 6945 |
| 9 | 🇬🇧 GB | 5977 |
| 10 | 🇯🇵 JP | 5723 |
| 11 | 🇫🇷 FR | 5302 |
| 12 | 🇨🇴 CO | 4173 |
| 13 | 🇲🇽 MX | 3896 |
| 14 | 🇬🇷 GR | 3823 |
| 15 | 🇳🇴 NO | 3617 |
| 16 | 🇨🇭 CH | 3446 |
| 17 | 🇹🇷 TR | 3021 |
| 18 | 🇲🇾 MY | 2649 |
| 19 | 🇵🇱 PL | 2202 |
| 20 | 🇿🇦 ZA | 2195 |
| 21 | 🇳🇿 NZ | 2102 |
| 22 | 🇹🇭 TH | 2054 |
| 23 | 🇰🇷 KR | 1973 |
| 24 | 🇵🇭 PH | 1838 |
| 25 | 🇬🇹 GT | 1810 |
| 26 | 🇲🇦 MA | 1418 |
| 27 | 🇲🇪 ME | 1328 |
| 28 | 🇳🇱 NL | 1252 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1184 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2788 |
| 2 | Denver International Airport |  | US | 2262 |
| 3 | Tokyo International Airport |  | JP | 1871 |
| 4 | Indira Gandhi International Airport |  | IN | 1721 |
| 5 | Harry Reid International Airport |  | US | 1663 |
| 6 | Guaymaral Airport |  | CO | 1627 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1567 |
| 8 | Zurich Airport |  | CH | 1485 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1421 |
| 10 | La Aurora Airport |  | GT | 1398 |
| 11 | Frankfurt am Main International Airport |  | DE | 1339 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1291 |
| 13 | Chicago O'Hare International Airport |  | US | 1278 |
| 14 | Salt Lake City International Airport |  | US | 1190 |
| 15 | Macau International Airport |  | MO | 1186 |
| 16 | El Dorado International Airport |  | CO | 1184 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1157 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1096 |
| 19 | Capua Airport |  | IT | 1095 |
| 20 | Madrid Barajas International Airport |  | ES | 1093 |
| 21 | Congonhas Airport |  | BR | 1065 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 970 |
| 25 | Charles de Gaulle International Airport |  | FR | 958 |
| 26 | Bengaluru International Airport |  | IN | 941 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 917 |
| 28 | Malpensa International Airport |  | IT | 883 |
| 29 | Ninoy Aquino International Airport |  | PH | 854 |
| 30 | Daniel K Inouye International Airport |  | US | 832 |
| 31 | Barcelona International Airport |  | ES | 821 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 817 |
| 33 | Tenerife Norte Airport |  | ES | 802 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 787 |
| 35 | Calgary International Airport |  | CA | 776 |
| 36 | Seattle-Tacoma International Airport |  | US | 767 |
| 37 | Scottsdale Airport |  | US | 764 |
| 38 | Viracopos International Airport |  | BR | 761 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 752 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 684 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 484 | 21m | 244 km | 2,038.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 334 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 322 | 1h 10m | 770 km | 4,277.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 242 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 186 | 44m | 241 km | 772.6 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 155 | 1h 16m | 961 km | 2,569.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-07-09 00:37 UTC | 2026-07-09 00:53 UTC | 16m |
| OXW | OXW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-07-09 00:35 UTC | 2026-07-09 00:50 UTC | 15m |
| SGE | SGE | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-07-09 00:32 UTC | 2026-07-09 00:46 UTC | 13m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-07-08 23:39 UTC | 2026-07-09 00:41 UTC | 1h 1m |
| N288SF |  | Raleigh-Durham International Airport (KRDU) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-07-08 23:46 UTC | 2026-07-09 00:41 UTC | 54m |
| KING44 | KIN | Fellsmere Airport (4FL3) | Patrick Space Force Base Airport (KCOF) | 2026-07-08 23:51 UTC | 2026-07-09 00:40 UTC | 48m |
| LJY976 | LJY | Addison Airport (KADS) | Anniston Regional Airport (KANB) | 2026-07-08 23:12 UTC | 2026-07-09 00:38 UTC | 1h 26m |
| NPN | NPN | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-07-08 23:54 UTC | 2026-07-09 00:34 UTC | 39m |
| N68767 |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-07-09 00:15 UTC | 2026-07-09 00:27 UTC | 11m |
| N6206 |  | Boeing Field/King County International Airport (KBFI) | Boeing Field/King County International Airport (KBFI) | 2026-07-09 00:10 UTC | 2026-07-09 00:26 UTC | 16m |
| N80945 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-08 23:51 UTC | 2026-07-09 00:25 UTC | 34m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-08 23:56 UTC | 2026-07-09 00:25 UTC | 29m |
| N526BL |  | Oakland/Troy Airport (KVLL) | Dupont/Lapeer Airport (KD95) | 2026-07-08 23:33 UTC | 2026-07-09 00:25 UTC | 51m |
| N256J |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-07-08 23:22 UTC | 2026-07-09 00:24 UTC | 1h 2m |
| N3396Q |  | Appalachee Bluff Riverfront Airpark (67GA) | Kintail Farm Airport (GA00) | 2026-07-09 00:10 UTC | 2026-07-09 00:23 UTC | 13m |
| N814SS |  | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-07-09 00:15 UTC | 2026-07-09 00:23 UTC | 7m |
| N137MH |  | Flying W Airport (KN14) | NJ96 (NJ96) | 2026-07-09 00:07 UTC | 2026-07-09 00:21 UTC | 14m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Wings Field (KLOM) | 2026-07-08 23:48 UTC | 2026-07-09 00:17 UTC | 29m |
| N240MW |  | Black River Ranch Airport (1MI3) | Akron-Canton Regional Airport (KCAK) | 2026-07-08 23:16 UTC | 2026-07-09 00:13 UTC | 56m |
| N986BT |  | Beaver County Airport (KBVI) | Wynkoop Airport (K6G4) | 2026-07-08 23:17 UTC | 2026-07-09 00:12 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
