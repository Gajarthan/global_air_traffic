# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_20:31:48_UTC-green)

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

**Latest saved flight:** 2026-08-07 20:31:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 20:31:48 UTC

- **176,594** saved flights
- **56,939** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,594** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,123,137.0 tonnes** estimated CO2 emissions
- **123,080,406 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6996 |
| 2 | SkyWest Airlines | 6452 |
| 3 | EJA | 3491 |
| 4 | IndiGo | 3093 |
| 5 | Southwest Airlines | 2781 |
| 6 | American Airlines | 2763 |
| 7 | ENY | 2198 |
| 8 | Delta Air Lines | 2084 |
| 9 | LATAM Airlines | 1634 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1572 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1457 |
| 14 | LXJ | 1389 |
| 15 | Swiss International | 1205 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1195 |
| 18 | EJU | 1082 |
| 19 | QLK | 1082 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1068 |
| 22 | VIV | 971 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 938 |
| 25 | GLO | 930 |
| 26 | AEE | 921 |
| 27 | United Airlines | 916 |
| 28 | Air France | 911 |
| 29 | MXY | 889 |
| 30 | JetBlue | 872 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151859 |
| 2 | 🇪🇸 ES | 11315 |
| 3 | 🇧🇷 BR | 10077 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9695 |
| 6 | 🇨🇦 CA | 9663 |
| 7 | 🇮🇹 IT | 9127 |
| 8 | 🇩🇪 DE | 8739 |
| 9 | 🇬🇧 GB | 8161 |
| 10 | 🇯🇵 JP | 7077 |
| 11 | 🇫🇷 FR | 7021 |
| 12 | 🇨🇴 CO | 6482 |
| 13 | 🇬🇷 GR | 5143 |
| 14 | 🇲🇽 MX | 5045 |
| 15 | 🇨🇭 CH | 4684 |
| 16 | 🇳🇴 NO | 4604 |
| 17 | 🇹🇷 TR | 4388 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2935 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2260 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1785 |
| 27 | 🇭🇷 HR | 1732 |
| 28 | 🇲🇪 ME | 1606 |
| 29 | 🇳🇱 NL | 1589 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3648 |
| 2 | Denver International Airport |  | US | 2924 |
| 3 | Tokyo International Airport |  | JP | 2209 |
| 4 | Guaymaral Airport |  | CO | 2166 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2103 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1913 |
| 8 | Zurich Airport |  | CH | 1877 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1846 |
| 10 | La Aurora Airport |  | GT | 1738 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1620 |
| 12 | Chicago O'Hare International Airport |  | US | 1590 |
| 13 | El Dorado International Airport |  | CO | 1581 |
| 14 | Salt Lake City International Airport |  | US | 1576 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1464 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1381 |
| 20 | Madrid Barajas International Airport |  | ES | 1377 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1315 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1241 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1208 |
| 25 | Malpensa International Airport |  | IT | 1207 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1093 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1091 |
| 32 | Barcelona International Airport |  | ES | 1049 |
| 33 | Daniel K Inouye International Airport |  | US | 1014 |
| 34 | Seattle-Tacoma International Airport |  | US | 1014 |
| 35 | Viracopos International Airport |  | BR | 1007 |
| 36 | Reno/Tahoe International Airport |  | US | 1006 |
| 37 | Calgary International Airport |  | CA | 1000 |
| 38 | Oslo Gardermoen Airport |  | NO | 987 |
| 39 | Tenerife Norte Airport |  | ES | 970 |
| 40 | Amsterdam Airport Schiphol |  | NL | 955 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 644 | 21m | 244 km | 2,711.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 413 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
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
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 217 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 211 | 1h 15m | 961 km | 3,497.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 192 | 1h 2m | 695 km | 2,301.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RAM819I | Royal Air Maroc | Manchester Airport (EGCC) | Tit Mellil Airport (GMMT) | 2026-08-07 17:34 UTC | 2026-08-07 20:31 UTC | 2h 57m |
| N719CG |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-08-07 19:46 UTC | 2026-08-07 20:26 UTC | 39m |
| ASLAN03 | ASL | Cildir Airport (LTBD) | Imsik Airport (LTBV) | 2026-08-07 18:36 UTC | 2026-08-07 20:26 UTC | 1h 49m |
| N300EX |  | Arlington Municipal Airport (KAWO) | Arlington Municipal Airport (KAWO) | 2026-08-07 19:59 UTC | 2026-08-07 20:24 UTC | 24m |
| N412TB |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-07 19:19 UTC | 2026-08-07 20:21 UTC | 1h 1m |
| N216CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-07 20:16 UTC | 2026-08-07 20:21 UTC | 5m |
| ROKT71 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-08-07 20:03 UTC | 2026-08-07 20:20 UTC | 16m |
| N582BL |  | Hinton Field (NC72) | Johnston Regional Airport (KJNX) | 2026-08-07 19:47 UTC | 2026-08-07 20:19 UTC | 32m |
| JUMP17 | JUM | MT88 (MT88) | Carson Field (MT53) | 2026-08-07 20:04 UTC | 2026-08-07 20:15 UTC | 11m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-07 20:07 UTC | 2026-08-07 20:13 UTC | 5m |
| TKR168 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-07 20:04 UTC | 2026-08-07 20:11 UTC | 7m |
| N8379Z |  | Daniel K Inouye International Airport (PHNL) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-08-07 19:58 UTC | 2026-08-07 20:10 UTC | 12m |
| N135RF |  | Lee Vining Airport (KO24) | Groveland/Yosemite Airport (KE45) | 2026-08-07 19:30 UTC | 2026-08-07 20:09 UTC | 38m |
| N240TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-07 20:06 UTC | 2026-08-07 20:09 UTC | 3m |
| N66MJ |  | Usaf Academy Davis Airfield (KAFF) | Limon Municipal Airport (KLIC) | 2026-08-07 19:40 UTC | 2026-08-07 20:08 UTC | 28m |
| BOE001 | BOE | Boeing Field/King County International Airport (KBFI) | Sacramento Mather Airport (KMHR) | 2026-08-07 18:19 UTC | 2026-08-07 20:07 UTC | 1h 48m |
| N229HL |  | 3IL1 (3IL1) | 3IL1 (3IL1) | 2026-08-07 20:02 UTC | 2026-08-07 20:03 UTC | 0m |
| BOM1 | BOM | Zurich Airport (LSZH) | Malpensa International Airport (LIMC) | 2026-08-07 19:25 UTC | 2026-08-07 20:02 UTC | 37m |
| TGCYO | TGC | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-08-07 19:32 UTC | 2026-08-07 20:02 UTC | 30m |
| SCHNR06 | SCH | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-08-07 19:44 UTC | 2026-08-07 20:01 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
