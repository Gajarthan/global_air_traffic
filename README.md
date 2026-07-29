# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_19:46:50_UTC-green)

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

**Latest saved flight:** 2026-07-29 19:46:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 19:46:50 UTC

- **159,073** saved flights
- **52,661** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,073** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,908,486.4 tonnes** estimated CO2 emissions
- **110,636,894 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6387 |
| 2 | SkyWest Airlines | 5811 |
| 3 | EJA | 3154 |
| 4 | IndiGo | 2802 |
| 5 | American Airlines | 2519 |
| 6 | Southwest Airlines | 2496 |
| 7 | ENY | 1979 |
| 8 | Delta Air Lines | 1887 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1494 |
| 11 | AZU | 1402 |
| 12 | WIF | 1350 |
| 13 | Vueling | 1335 |
| 14 | LXJ | 1224 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1098 |
| 17 | easyJet | 1036 |
| 18 | Alaska Airlines | 995 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 975 |
| 22 | VIV | 873 |
| 23 | CXK | 845 |
| 24 | United Airlines | 841 |
| 25 | GLO | 839 |
| 26 | AEE | 837 |
| 27 | Cathay Pacific | 834 |
| 28 | Air France | 829 |
| 29 | MXY | 828 |
| 30 | JetBlue | 818 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 137248 |
| 2 | 🇪🇸 ES | 10232 |
| 3 | 🇧🇷 BR | 9111 |
| 4 | 🇦🇺 AU | 8957 |
| 5 | 🇮🇳 IN | 8813 |
| 6 | 🇨🇦 CA | 8620 |
| 7 | 🇮🇹 IT | 8228 |
| 8 | 🇩🇪 DE | 8062 |
| 9 | 🇬🇧 GB | 7298 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6301 |
| 12 | 🇨🇴 CO | 5596 |
| 13 | 🇲🇽 MX | 4573 |
| 14 | 🇬🇷 GR | 4564 |
| 15 | 🇳🇴 NO | 4218 |
| 16 | 🇨🇭 CH | 4167 |
| 17 | 🇹🇷 TR | 3799 |
| 18 | 🇲🇾 MY | 2893 |
| 19 | 🇵🇱 PL | 2707 |
| 20 | 🇿🇦 ZA | 2572 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2275 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2034 |
| 26 | 🇲🇦 MA | 1616 |
| 27 | 🇲🇪 ME | 1523 |
| 28 | 🇭🇷 HR | 1475 |
| 29 | 🇳🇱 NL | 1452 |
| 30 | 🇲🇴 MO | 1315 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3252 |
| 2 | Denver International Airport |  | US | 2650 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 2000 |
| 5 | Indira Gandhi International Airport |  | IN | 1963 |
| 6 | Harry Reid International Airport |  | US | 1940 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1766 |
| 8 | Zurich Airport |  | CH | 1705 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1668 |
| 10 | La Aurora Airport |  | GT | 1578 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1485 |
| 12 | Frankfurt am Main International Airport |  | DE | 1464 |
| 13 | El Dorado International Airport |  | CO | 1453 |
| 14 | Chicago O'Hare International Airport |  | US | 1438 |
| 15 | Salt Lake City International Airport |  | US | 1428 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1326 |
| 17 | Congonhas Airport |  | BR | 1321 |
| 18 | Macau International Airport |  | MO | 1315 |
| 19 | Madrid Barajas International Airport |  | ES | 1263 |
| 20 | Capua Airport |  | IT | 1254 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1220 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1138 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1134 |
| 24 | Charlotte/Douglas International Airport |  | US | 1116 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Malpensa International Airport |  | IT | 1052 |
| 28 | Bengaluru International Airport |  | IN | 1049 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 968 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 968 |
| 32 | Barcelona International Airport |  | ES | 950 |
| 33 | Daniel K Inouye International Airport |  | US | 939 |
| 34 | Seattle-Tacoma International Airport |  | US | 927 |
| 35 | Calgary International Airport |  | CA | 910 |
| 36 | Viracopos International Airport |  | BR | 909 |
| 37 | Scottsdale Airport |  | US | 900 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 874 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 839 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 578 | 21m | 244 km | 2,433.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 189 | 1h 15m | 961 km | 3,132.8 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 181 | 50m | 556 km | 1,735.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1954V |  | Rocket Ranch Airport (OK90) | Nuggs Flying M Airport (TE68) | 2026-07-29 19:15 UTC | 2026-07-29 19:46 UTC | 31m |
| CPA875 | Cathay Pacific | Dallas-Fort Worth International Airport (KDFW) | Macau International Airport (VMMC) | 2026-07-29 04:40 UTC | 2026-07-29 19:43 UTC | 15h 2m |
| N7881W |  | Corona Municipal Airport (KAJO) | Corona Municipal Airport (KAJO) | 2026-07-29 18:26 UTC | 2026-07-29 19:39 UTC | 1h 12m |
| TOPCT35 | TOP | Offutt Afb Airport (KOFF) | Mott Municipal Airport (K3P3) | 2026-07-29 18:31 UTC | 2026-07-29 19:36 UTC | 1h 5m |
| N272FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-29 18:47 UTC | 2026-07-29 19:35 UTC | 48m |
| OUZO31 | OUZ | Ramey 1 Airport (0OK8) | Ramey 1 Airport (0OK8) | 2026-07-29 19:16 UTC | 2026-07-29 19:29 UTC | 13m |
| SKW5465 | SkyWest Airlines | Raleigh-Durham International Airport (KRDU) | Chicago O'Hare International Airport (KORD) | 2026-07-29 17:33 UTC | 2026-07-29 19:28 UTC | 1h 54m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | Sanpete County Regional Airport (K41U) | 2026-07-29 19:07 UTC | 2026-07-29 19:26 UTC | 19m |
| NCJ98 | NCJ | Flying Cloud Airport (KFCM) | Lincoln Airport (KLNK) | 2026-07-29 18:37 UTC | 2026-07-29 19:25 UTC | 48m |
| N1814E |  | French Valley Airport (KF70) | Big Bear City Airport (KL35) | 2026-07-29 19:06 UTC | 2026-07-29 19:24 UTC | 18m |
| N21J |  | Hesler/Noble Field (KLUL) | Calhoun County Airport (K04M) | 2026-07-29 18:59 UTC | 2026-07-29 19:21 UTC | 22m |
| N734TS |  | Mc Clellan-Palomar Airport (KCRQ) | San Bernardino International Airport (KSBD) | 2026-07-29 17:57 UTC | 2026-07-29 19:16 UTC | 1h 19m |
| SWR8CM | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-07-29 18:13 UTC | 2026-07-29 19:16 UTC | 1h 3m |
| SST913 | SST | Winnipeg James Armstrong Richardson International Airport (CYWG) | Matheson Island Airport (CJT2) | 2026-07-29 18:38 UTC | 2026-07-29 19:16 UTC | 37m |
| SEAFOX3 | SEA | Haass Field (TE57) | Haass Field (TE57) | 2026-07-29 19:07 UTC | 2026-07-29 19:14 UTC | 6m |
| N904LR |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Barstow-Daggett Airport (KDAG) | 2026-07-29 16:37 UTC | 2026-07-29 19:10 UTC | 2h 32m |
| N8488M |  | Carson City Airport (KCXP) | K4SD (K4SD) | 2026-07-29 18:51 UTC | 2026-07-29 19:09 UTC | 17m |
| CFUDF | CFU | Beiseker Airport (CFV2) | Beiseker Airport (CFV2) | 2026-07-29 18:47 UTC | 2026-07-29 19:08 UTC | 21m |
| UAV15 | UAV | El Mirage Field Adelanto Airport (99CL) | Sun Hill Ranch Airport (CA70) | 2026-07-29 18:57 UTC | 2026-07-29 19:08 UTC | 11m |
| N814SS |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-29 18:42 UTC | 2026-07-29 19:03 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
