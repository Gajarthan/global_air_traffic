# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_15:34:32_UTC-green)

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

**Latest saved flight:** 2026-08-09 15:34:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 15:34:32 UTC

- **181,425** saved flights
- **57,950** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,425** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,180,587.7 tonnes** estimated CO2 emissions
- **126,410,880 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7200 |
| 2 | SkyWest Airlines | 6587 |
| 3 | EJA | 3558 |
| 4 | IndiGo | 3183 |
| 5 | Southwest Airlines | 2843 |
| 6 | American Airlines | 2820 |
| 7 | ENY | 2252 |
| 8 | Delta Air Lines | 2144 |
| 9 | LATAM Airlines | 1697 |
| 10 | AZU | 1626 |
| 11 | Lufthansa | 1613 |
| 12 | Vueling | 1503 |
| 13 | WIF | 1503 |
| 14 | LXJ | 1409 |
| 15 | easyJet | 1243 |
| 16 | Swiss International | 1243 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1110 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 998 |
| 23 | GLO | 971 |
| 24 | CXK | 949 |
| 25 | AEE | 947 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 938 |
| 28 | United Airlines | 931 |
| 29 | PGT | 912 |
| 30 | MXY | 909 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155019 |
| 2 | 🇪🇸 ES | 11690 |
| 3 | 🇧🇷 BR | 10424 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 9981 |
| 6 | 🇨🇦 CA | 9870 |
| 7 | 🇮🇹 IT | 9396 |
| 8 | 🇩🇪 DE | 9001 |
| 9 | 🇬🇧 GB | 8399 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7232 |
| 12 | 🇨🇴 CO | 6734 |
| 13 | 🇬🇷 GR | 5320 |
| 14 | 🇲🇽 MX | 5176 |
| 15 | 🇨🇭 CH | 4850 |
| 16 | 🇹🇷 TR | 4688 |
| 17 | 🇳🇴 NO | 4676 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3051 |
| 20 | 🇿🇦 ZA | 3009 |
| 21 | 🇹🇭 TH | 2802 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2301 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1836 |
| 27 | 🇭🇷 HR | 1811 |
| 28 | 🇲🇪 ME | 1644 |
| 29 | 🇳🇱 NL | 1634 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3739 |
| 2 | Denver International Airport |  | US | 2989 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2228 |
| 5 | Guaymaral Airport |  | CO | 2224 |
| 6 | Harry Reid International Airport |  | US | 2128 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1953 |
| 8 | Zurich Airport |  | CH | 1938 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1767 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1627 |
| 13 | Salt Lake City International Airport |  | US | 1618 |
| 14 | El Dorado International Airport |  | CO | 1617 |
| 15 | Frankfurt am Main International Airport |  | DE | 1576 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1512 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1440 |
| 19 | Madrid Barajas International Airport |  | ES | 1429 |
| 20 | Capua Airport |  | IT | 1418 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1353 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1297 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1252 |
| 25 | Charles de Gaulle International Airport |  | FR | 1233 |
| 26 | Charlotte/Douglas International Airport |  | US | 1226 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1186 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1127 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1045 |
| 34 | Daniel K Inouye International Airport |  | US | 1041 |
| 35 | Seattle-Tacoma International Airport |  | US | 1041 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1006 |
| 39 | Tenerife Norte Airport |  | ES | 992 |
| 40 | Amsterdam Airport Schiphol |  | NL | 984 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 418 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 306 | 27m | 275 km | 1,450.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 255 | 1h 48m | 1,423 km | 6,258.1 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 245 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 242 | 20m | 250 km | 1,045.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 219 | 1h 15m | 961 km | 3,630.0 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 211 | 24m | 218 km | 794.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHX1 | CHX | Oberschleisheim Airfield (EDNX) | Innsbruck Airport (LOWI) | 2026-08-09 15:14 UTC | 2026-08-09 15:34 UTC | 20m |
| N241MP |  | AL02 (AL02) | AL02 (AL02) | 2026-08-09 15:17 UTC | 2026-08-09 15:34 UTC | 17m |
| N283HG |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-08-09 15:17 UTC | 2026-08-09 15:32 UTC | 15m |
| CFGMF | CFG | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-09 14:59 UTC | 2026-08-09 15:30 UTC | 30m |
| N448ME |  | Weiblen Airport (TE13) | Kelly Field (KSKF) | 2026-08-09 15:21 UTC | 2026-08-09 15:28 UTC | 6m |
| N72194 |  | Addington Field (KEKX) | Addington Field (KEKX) | 2026-08-09 15:10 UTC | 2026-08-09 15:28 UTC | 17m |
| TRF688 | TRF | North Texas Regional/Perrin Field (KGYI) | Jones Field (KF00) | 2026-08-09 14:40 UTC | 2026-08-09 15:28 UTC | 47m |
| N853MH |  | Long Beach (Daugherty Field) Airport (KLGB) | Catalina Airport (KAVX) | 2026-08-09 15:10 UTC | 2026-08-09 15:23 UTC | 13m |
| N522ND |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-09 15:10 UTC | 2026-08-09 15:20 UTC | 10m |
| N8188Z |  | Hazleton Regional Airport (KHZL) | Hazleton Regional Airport (KHZL) | 2026-08-09 14:51 UTC | 2026-08-09 15:19 UTC | 27m |
| N129LA |  | K1J0 (K1J0) | K1J0 (K1J0) | 2026-08-09 15:06 UTC | 2026-08-09 15:18 UTC | 12m |
| N42PE |  | Bend Municipal Airport (KBDN) | Prineville Airport (KS39) | 2026-08-09 14:56 UTC | 2026-08-09 15:17 UTC | 21m |
| N357JG |  | Akron-Canton Regional Airport (KCAK) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-09 14:05 UTC | 2026-08-09 15:16 UTC | 1h 11m |
| N2361L |  | Lovell Field (KCHA) | Cleveland Regional Jetport Airport (KRZR) | 2026-08-09 14:59 UTC | 2026-08-09 15:16 UTC | 17m |
| MRS1203 | MRS | Saniat Rmel Airport (GMTN) | Kenitra Airport (GMMY) | 2026-08-09 14:54 UTC | 2026-08-09 15:16 UTC | 21m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-09 14:22 UTC | 2026-08-09 15:13 UTC | 51m |
| N650RA |  | Delta Flying Service Inc Airport (MS65) | Addison Airport (KADS) | 2026-08-09 14:09 UTC | 2026-08-09 15:11 UTC | 1h 2m |
| HSOMJ2 | HSO | Emden Airport (EDWE) | Juist Airport (EDWJ) | 2026-08-09 14:08 UTC | 2026-08-09 15:07 UTC | 58m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 14:55 UTC | 2026-08-09 15:06 UTC | 11m |
| N241MP |  | Tuscaloosa Ntl Airport (KTCL) | AL02 (AL02) | 2026-08-09 14:24 UTC | 2026-08-09 15:06 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
