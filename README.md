# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_13:59:59_UTC-green)

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

**Latest saved flight:** 2026-08-01 13:59:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 13:59:59 UTC

- **164,476** saved flights
- **54,068** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **164,476** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,977,232.8 tonnes** estimated CO2 emissions
- **114,622,193 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6570 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2898 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2580 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1960 |
| 9 | LATAM Airlines | 1536 |
| 10 | Lufthansa | 1534 |
| 11 | AZU | 1445 |
| 12 | WIF | 1387 |
| 13 | Vueling | 1361 |
| 14 | LXJ | 1275 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1129 |
| 17 | easyJet | 1080 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1011 |
| 20 | All Nippon Airways | 1009 |
| 21 | EJU | 1006 |
| 22 | VIV | 907 |
| 23 | CXK | 880 |
| 24 | Cathay Pacific | 874 |
| 25 | United Airlines | 866 |
| 26 | AEE | 863 |
| 27 | GLO | 859 |
| 28 | Air France | 850 |
| 29 | MXY | 849 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141899 |
| 2 | 🇪🇸 ES | 10531 |
| 3 | 🇧🇷 BR | 9376 |
| 4 | 🇦🇺 AU | 9255 |
| 5 | 🇮🇳 IN | 9096 |
| 6 | 🇨🇦 CA | 8942 |
| 7 | 🇮🇹 IT | 8494 |
| 8 | 🇩🇪 DE | 8241 |
| 9 | 🇬🇧 GB | 7577 |
| 10 | 🇯🇵 JP | 6657 |
| 11 | 🇫🇷 FR | 6522 |
| 12 | 🇨🇴 CO | 5892 |
| 13 | 🇬🇷 GR | 4740 |
| 14 | 🇲🇽 MX | 4705 |
| 15 | 🇳🇴 NO | 4336 |
| 16 | 🇨🇭 CH | 4331 |
| 17 | 🇹🇷 TR | 3939 |
| 18 | 🇲🇾 MY | 2967 |
| 19 | 🇵🇱 PL | 2791 |
| 20 | 🇿🇦 ZA | 2683 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2366 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇰🇷 KR | 2132 |
| 25 | 🇬🇹 GT | 2119 |
| 26 | 🇲🇦 MA | 1658 |
| 27 | 🇭🇷 HR | 1551 |
| 28 | 🇲🇪 ME | 1541 |
| 29 | 🇳🇱 NL | 1494 |
| 30 | 🇲🇴 MO | 1392 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2069 |
| 5 | Indira Gandhi International Airport |  | IN | 2014 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1813 |
| 8 | Zurich Airport |  | CH | 1753 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1727 |
| 10 | La Aurora Airport |  | GT | 1641 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1506 |
| 13 | Frankfurt am Main International Airport |  | DE | 1490 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1478 |
| 16 | Macau International Airport |  | MO | 1392 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1378 |
| 18 | Congonhas Airport |  | BR | 1357 |
| 19 | Madrid Barajas International Airport |  | ES | 1297 |
| 20 | Capua Airport |  | IT | 1289 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1163 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Kuala Lumpur International Airport |  | MY | 1124 |
| 26 | Charles de Gaulle International Airport |  | FR | 1123 |
| 27 | Malpensa International Airport |  | IT | 1091 |
| 28 | Bengaluru International Airport |  | IN | 1079 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 974 |
| 33 | Daniel K Inouye International Airport |  | US | 960 |
| 34 | Seattle-Tacoma International Airport |  | US | 952 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 935 |
| 37 | Tenerife Norte Airport |  | ES | 918 |
| 38 | Oslo Gardermoen Airport |  | NO | 917 |
| 39 | Scottsdale Airport |  | US | 917 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 864 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 598 | 21m | 244 km | 2,518.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 392 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 306 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 246 | 22m | 55 km | 233.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 211 | 20m | 250 km | 911.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GIZMO11 | GIZ | Ramey 1 Airport (0OK8) | Lariat Ranch Airport (OK42) | 2026-08-01 13:46 UTC | 2026-08-01 13:59 UTC | 13m |
| N783FM |  | Fort Meade Executive Airport (KFME) | Fort Meade Executive Airport (KFME) | 2026-08-01 13:44 UTC | 2026-08-01 13:57 UTC | 13m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-01 13:39 UTC | 2026-08-01 13:56 UTC | 17m |
| ZSHBO | ZSH | Ysterplaat Air Force Base (FAYP) | Ysterplaat Air Force Base (FAYP) | 2026-08-01 13:44 UTC | 2026-08-01 13:56 UTC | 12m |
| A7GQB |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-08-01 12:34 UTC | 2026-08-01 13:51 UTC | 1h 16m |
| VAR469 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-08-01 13:23 UTC | 2026-08-01 13:47 UTC | 24m |
| GIZMO11 | GIZ | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-08-01 13:25 UTC | 2026-08-01 13:46 UTC | 20m |
| FDX157 | FDX | Frederick W Smith International Airport (KMEM) | Fox Creek Airport (CED4) | 2026-08-01 09:52 UTC | 2026-08-01 13:44 UTC | 3h 51m |
| N312CT |  | Lubbock Executive Airpark (KF82) | Terry County Airport (KBFE) | 2026-08-01 13:17 UTC | 2026-08-01 13:44 UTC | 26m |
| TORA11 | TOR | Flying E Ranch Airport (OK16) | Sopwith Ldg Airport (OK56) | 2026-08-01 13:29 UTC | 2026-08-01 13:43 UTC | 14m |
| HBZVU | HBZ | Bellechasse Airport (LSTB) | Bellechasse Airport (LSTB) | 2026-08-01 10:57 UTC | 2026-08-01 13:34 UTC | 2h 36m |
| MGL138 | MGL | Frankfurt am Main International Airport (EDDF) | Pruszcz Gdański Airport (EPPR) | 2026-08-01 12:35 UTC | 2026-08-01 13:32 UTC | 56m |
| N103UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-01 13:07 UTC | 2026-08-01 13:31 UTC | 24m |
| HK5463X |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-08-01 13:12 UTC | 2026-08-01 13:26 UTC | 14m |
| N8786E |  | Ada Regional Airport (KADH) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-01 12:37 UTC | 2026-08-01 13:24 UTC | 46m |
| DRAG382 | DRA | L'alpe D'huez Airport (LFHU) | L'alpe D'huez Airport (LFHU) | 2026-08-01 13:22 UTC | 2026-08-01 13:24 UTC | 1m |
| ERU856 | ERU | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-08-01 13:21 UTC | 2026-08-01 13:23 UTC | 2m |
| N600AR |  | Elkhart Municipal Airport (KEKM) | Antrim County Airport (KACB) | 2026-08-01 12:50 UTC | 2026-08-01 13:19 UTC | 28m |
| N252BS |  | Rocky Mountain Metro Airport (KBJC) | CO86 (CO86) | 2026-08-01 13:03 UTC | 2026-08-01 13:18 UTC | 14m |
| VTE7611 | VTE | Westchester County Airport (KHPN) | Westerly State Airport (KWST) | 2026-08-01 12:35 UTC | 2026-08-01 13:16 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
