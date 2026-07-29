# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_17:22:14_UTC-green)

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

**Latest saved flight:** 2026-07-29 17:22:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 17:22:14 UTC

- **158,686** saved flights
- **52,557** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **158,686** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,904,032.3 tonnes** estimated CO2 emissions
- **110,378,683 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6378 |
| 2 | SkyWest Airlines | 5788 |
| 3 | EJA | 3139 |
| 4 | IndiGo | 2801 |
| 5 | American Airlines | 2516 |
| 6 | Southwest Airlines | 2487 |
| 7 | ENY | 1975 |
| 8 | Delta Air Lines | 1879 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1489 |
| 11 | AZU | 1398 |
| 12 | WIF | 1345 |
| 13 | Vueling | 1332 |
| 14 | LXJ | 1224 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1094 |
| 17 | easyJet | 1034 |
| 18 | Alaska Airlines | 992 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 971 |
| 22 | VIV | 870 |
| 23 | CXK | 842 |
| 24 | United Airlines | 838 |
| 25 | GLO | 834 |
| 26 | AEE | 833 |
| 27 | Cathay Pacific | 833 |
| 28 | Air France | 828 |
| 29 | MXY | 824 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136801 |
| 2 | 🇪🇸 ES | 10213 |
| 3 | 🇧🇷 BR | 9078 |
| 4 | 🇦🇺 AU | 8954 |
| 5 | 🇮🇳 IN | 8808 |
| 6 | 🇨🇦 CA | 8590 |
| 7 | 🇮🇹 IT | 8203 |
| 8 | 🇩🇪 DE | 8056 |
| 9 | 🇬🇧 GB | 7284 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6292 |
| 12 | 🇨🇴 CO | 5573 |
| 13 | 🇲🇽 MX | 4553 |
| 14 | 🇬🇷 GR | 4550 |
| 15 | 🇳🇴 NO | 4207 |
| 16 | 🇨🇭 CH | 4162 |
| 17 | 🇹🇷 TR | 3792 |
| 18 | 🇲🇾 MY | 2892 |
| 19 | 🇵🇱 PL | 2699 |
| 20 | 🇿🇦 ZA | 2572 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2274 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2033 |
| 26 | 🇲🇦 MA | 1616 |
| 27 | 🇲🇪 ME | 1523 |
| 28 | 🇭🇷 HR | 1469 |
| 29 | 🇳🇱 NL | 1451 |
| 30 | 🇲🇴 MO | 1311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3247 |
| 2 | Denver International Airport |  | US | 2642 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 1989 |
| 5 | Indira Gandhi International Airport |  | IN | 1959 |
| 6 | Harry Reid International Airport |  | US | 1932 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1761 |
| 8 | Zurich Airport |  | CH | 1701 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1664 |
| 10 | La Aurora Airport |  | GT | 1577 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1477 |
| 12 | Frankfurt am Main International Airport |  | DE | 1463 |
| 13 | El Dorado International Airport |  | CO | 1449 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1423 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1325 |
| 17 | Congonhas Airport |  | BR | 1314 |
| 18 | Macau International Airport |  | MO | 1311 |
| 19 | Madrid Barajas International Airport |  | ES | 1262 |
| 20 | Capua Airport |  | IT | 1249 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1216 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1137 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1130 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1092 |
| 27 | Bengaluru International Airport |  | IN | 1049 |
| 28 | Malpensa International Airport |  | IT | 1048 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 965 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 964 |
| 32 | Barcelona International Airport |  | ES | 947 |
| 33 | Daniel K Inouye International Airport |  | US | 935 |
| 34 | Seattle-Tacoma International Airport |  | US | 924 |
| 35 | Calgary International Airport |  | CA | 909 |
| 36 | Viracopos International Airport |  | BR | 908 |
| 37 | Scottsdale Airport |  | US | 897 |
| 38 | Tenerife Norte Airport |  | ES | 896 |
| 39 | Oslo Gardermoen Airport |  | NO | 883 |
| 40 | Amsterdam Airport Schiphol |  | NL | 873 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 834 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 574 | 21m | 244 km | 2,417.0 t |
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
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 225 | 44m | 241 km | 934.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 188 | 1h 15m | 961 km | 3,116.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 180 | 50m | 556 km | 1,725.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 178 | 1h 39m | 1,156 km | 3,551.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 169 | 23m | 218 km | 636.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N229HL |  | Greenville Airport (KGRE) | 8LL0 (8LL0) | 2026-07-29 17:07 UTC | 2026-07-29 17:22 UTC | 15m |
| AWH94S | AWH | Dusseldorf International Airport (EDDL) | EPMX (EPMX) | 2026-07-29 15:49 UTC | 2026-07-29 17:18 UTC | 1h 29m |
| N5588F |  | Chehalis-Centralia Airport (KCLS) | 20WA (20WA) | 2026-07-29 16:40 UTC | 2026-07-29 17:12 UTC | 32m |
| N250AW |  | Cecil Ranch Airport (37CN) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-29 16:37 UTC | 2026-07-29 17:11 UTC | 34m |
| WMT8064 | WMT | London Luton Airport (EGGW) | Malpensa International Airport (LIMC) | 2026-07-29 15:38 UTC | 2026-07-29 17:10 UTC | 1h 31m |
| N646AT |  | Merrill Field (PAMR) | Skwentna Airport (PASW) | 2026-07-29 16:43 UTC | 2026-07-29 17:09 UTC | 26m |
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-07-29 16:48 UTC | 2026-07-29 17:09 UTC | 20m |
| N4627F |  | Lake In The Hills Airport (K3CK) | Ruder Airport (59IL) | 2026-07-29 16:54 UTC | 2026-07-29 17:07 UTC | 13m |
| N5085K |  | Lincoln County Regional Airport (KIPJ) | Lincoln County Regional Airport (KIPJ) | 2026-07-29 16:54 UTC | 2026-07-29 17:04 UTC | 9m |
| SMOKN51 | SMO | Laughlin Afb Aux Nr 1 Airport (KT70) | 6TA4 (6TA4) | 2026-07-29 16:41 UTC | 2026-07-29 17:01 UTC | 20m |
| N721FJ |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-07-29 15:58 UTC | 2026-07-29 16:54 UTC | 56m |
| N624ES |  | French Valley Airport (KF70) | Big Bear City Airport (KL35) | 2026-07-29 16:26 UTC | 2026-07-29 16:50 UTC | 24m |
| N169PS |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-07-29 15:40 UTC | 2026-07-29 16:50 UTC | 1h 10m |
| WUP661 | WUP | Bradley International Airport (KBDL) | Mohawk Air Park (27NK) | 2026-07-29 16:21 UTC | 2026-07-29 16:49 UTC | 28m |
| N712HA |  | Columbia Metro Airport (KCAE) | SC14 (SC14) | 2026-07-29 16:23 UTC | 2026-07-29 16:49 UTC | 26m |
| EVAL62 | EVA Air | Redstone Army Air Field (KHUA) | Redstone Army Air Field (KHUA) | 2026-07-29 14:35 UTC | 2026-07-29 16:48 UTC | 2h 12m |
| N567PW |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-29 15:58 UTC | 2026-07-29 16:47 UTC | 48m |
| HK5220 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-29 16:27 UTC | 2026-07-29 16:45 UTC | 18m |
| N26CG |  | Darr Field (NC03) | Cape Fear Regional Jetport/Howie Franklin Field (KSUT) | 2026-07-29 11:11 UTC | 2026-07-29 16:45 UTC | 5h 33m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-07-29 15:30 UTC | 2026-07-29 16:43 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
