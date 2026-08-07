# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_22:44:36_UTC-green)

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

**Latest saved flight:** 2026-08-07 22:44:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 22:44:36 UTC

- **176,928** saved flights
- **57,022** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,928** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,126,982.6 tonnes** estimated CO2 emissions
- **123,303,342 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7014 |
| 2 | SkyWest Airlines | 6474 |
| 3 | EJA | 3501 |
| 4 | IndiGo | 3093 |
| 5 | Southwest Airlines | 2789 |
| 6 | American Airlines | 2769 |
| 7 | ENY | 2203 |
| 8 | Delta Air Lines | 2091 |
| 9 | LATAM Airlines | 1638 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1578 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1390 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1200 |
| 17 | AXM | 1196 |
| 18 | EJU | 1082 |
| 19 | QLK | 1082 |
| 20 | Alaska Airlines | 1070 |
| 21 | All Nippon Airways | 1069 |
| 22 | VIV | 974 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 939 |
| 25 | GLO | 935 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 891 |
| 30 | JetBlue | 874 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152225 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10110 |
| 4 | 🇦🇺 AU | 9959 |
| 5 | 🇮🇳 IN | 9697 |
| 6 | 🇨🇦 CA | 9693 |
| 7 | 🇮🇹 IT | 9143 |
| 8 | 🇩🇪 DE | 8740 |
| 9 | 🇬🇧 GB | 8173 |
| 10 | 🇯🇵 JP | 7079 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6513 |
| 13 | 🇬🇷 GR | 5150 |
| 14 | 🇲🇽 MX | 5062 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4607 |
| 17 | 🇹🇷 TR | 4389 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2938 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2624 |
| 22 | 🇳🇿 NZ | 2561 |
| 23 | 🇵🇭 PH | 2332 |
| 24 | 🇬🇹 GT | 2263 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1740 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3657 |
| 2 | Denver International Airport |  | US | 2935 |
| 3 | Tokyo International Airport |  | JP | 2210 |
| 4 | Guaymaral Airport |  | CO | 2174 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2107 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1914 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1850 |
| 10 | La Aurora Airport |  | GT | 1741 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1625 |
| 12 | Chicago O'Hare International Airport |  | US | 1596 |
| 13 | Salt Lake City International Airport |  | US | 1583 |
| 14 | El Dorado International Airport |  | CO | 1582 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1469 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1425 |
| 19 | Capua Airport |  | IT | 1383 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1318 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1246 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1097 |
| 30 | Ninoy Aquino International Airport |  | PH | 1097 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1093 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1018 |
| 34 | Daniel K Inouye International Airport |  | US | 1015 |
| 35 | Viracopos International Airport |  | BR | 1013 |
| 36 | Reno/Tahoe International Airport |  | US | 1008 |
| 37 | Calgary International Airport |  | CA | 1008 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 898 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 645 | 21m | 244 km | 2,715.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 407 | 1h 8m | 770 km | 5,406.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
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
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 222 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 193 | 1h 2m | 695 km | 2,313.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N190SW |  | Houma-Terrebonne Airport (KHUM) | Gulf Shores International/Jack Edwards Field (KJKA) | 2026-08-07 22:14 UTC | 2026-08-07 22:44 UTC | 30m |
| N851MB |  | Lemons Private Strip (CO10) | Greeley-Weld County Airport (KGXY) | 2026-08-07 22:05 UTC | 2026-08-07 22:40 UTC | 35m |
| N172RW |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-07 22:04 UTC | 2026-08-07 22:35 UTC | 31m |
| NASA529 | NAS | Boise Air Trml/Gowen Field (KBOI) | K43U (K43U) | 2026-08-07 20:50 UTC | 2026-08-07 22:33 UTC | 1h 42m |
| N6500L |  | Gnoss Field (KDVO) | Mc Clellan Airfield (KMCC) | 2026-08-07 22:06 UTC | 2026-08-07 22:32 UTC | 26m |
| N491LG |  | Tall Timber Airport (CD28) | Marshdale Airport (CO52) | 2026-08-07 22:16 UTC | 2026-08-07 22:31 UTC | 15m |
| N122JM |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-07 21:53 UTC | 2026-08-07 22:30 UTC | 37m |
| N145LF |  | Blackinton Airport (2CA4) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-08-07 22:06 UTC | 2026-08-07 22:23 UTC | 16m |
| SCU34 | SCU | Sahoma Lake Airport (03OK) | Tulsa International Airport (KTUL) | 2026-08-07 21:53 UTC | 2026-08-07 22:21 UTC | 27m |
| N54179 |  | John Wayne/Orange County Airport (KSNA) | Fullerton Municipal Airport (KFUL) | 2026-08-07 21:23 UTC | 2026-08-07 22:18 UTC | 55m |
| TKR186 | TKR | WN36 (WN36) | Pangborn Memorial Airport (KEAT) | 2026-08-07 21:25 UTC | 2026-08-07 22:14 UTC | 49m |
| EJA963 | EJA | 6CO0 (6CO0) | Barkley Regional Airport (KPAH) | 2026-08-07 20:01 UTC | 2026-08-07 22:13 UTC | 2h 11m |
| TGTUK | TGT | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-07 22:10 UTC | 2026-08-07 22:11 UTC | 1m |
| N53UB |  | Jack Mc Namara Field (KCEC) | Boeing Field/King County International Airport (KBFI) | 2026-08-07 21:07 UTC | 2026-08-07 22:11 UTC | 1h 3m |
| MAFIA91 | MAF | Marion County-Rankin Fite Airport (KHAB) | Robert Sibley Airport (KSZY) | 2026-08-07 21:46 UTC | 2026-08-07 22:10 UTC | 23m |
| TKR16 | TKR | Rogue Valley International/Medford Airport (KMFR) | Oakridge Ranch Airport (26OG) | 2026-08-07 22:01 UTC | 2026-08-07 22:08 UTC | 7m |
| XHD | XHD | Mittagong Airport (YMIG) | Goulburn Airport (YGLB) | 2026-08-07 21:44 UTC | 2026-08-07 22:06 UTC | 21m |
| N528MC |  | KU77 (KU77) | Carson City Airport (KCXP) | 2026-08-07 21:02 UTC | 2026-08-07 22:03 UTC | 1h 0m |
| WMU80 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-08-07 21:12 UTC | 2026-08-07 22:02 UTC | 49m |
| N510DJ |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | 5TA4 (5TA4) | 2026-08-07 21:01 UTC | 2026-08-07 22:00 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
