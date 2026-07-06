# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_16:28:06_UTC-green)

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

**Latest saved flight:** 2026-07-06 16:28:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 16:28:06 UTC

- **131,099** saved flights
- **44,554** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,099** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,581,907.9 tonnes** estimated CO2 emissions
- **91,704,809 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5334 |
| 2 | SkyWest Airlines | 4853 |
| 3 | EJA | 2569 |
| 4 | IndiGo | 2458 |
| 5 | American Airlines | 2029 |
| 6 | Southwest Airlines | 1974 |
| 7 | ENY | 1646 |
| 8 | Delta Air Lines | 1573 |
| 9 | Lufthansa | 1370 |
| 10 | LATAM Airlines | 1202 |
| 11 | Vueling | 1157 |
| 12 | WIF | 1142 |
| 13 | AZU | 1115 |
| 14 | AXM | 1012 |
| 15 | LXJ | 1012 |
| 16 | Swiss International | 917 |
| 17 | All Nippon Airways | 863 |
| 18 | easyJet | 841 |
| 19 | Alaska Airlines | 838 |
| 20 | QLK | 820 |
| 21 | EJU | 812 |
| 22 | VIV | 724 |
| 23 | Cathay Pacific | 716 |
| 24 | Air France | 714 |
| 25 | AEE | 713 |
| 26 | CXK | 703 |
| 27 | United Airlines | 697 |
| 28 | JetBlue | 689 |
| 29 | MXY | 684 |
| 30 | GLO | 673 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112250 |
| 2 | 🇪🇸 ES | 8745 |
| 3 | 🇮🇳 IN | 7704 |
| 4 | 🇦🇺 AU | 7567 |
| 5 | 🇧🇷 BR | 7389 |
| 6 | 🇨🇦 CA | 6906 |
| 7 | 🇩🇪 DE | 6874 |
| 8 | 🇮🇹 IT | 6843 |
| 9 | 🇬🇧 GB | 5855 |
| 10 | 🇯🇵 JP | 5653 |
| 11 | 🇫🇷 FR | 5219 |
| 12 | 🇨🇴 CO | 4105 |
| 13 | 🇲🇽 MX | 3825 |
| 14 | 🇬🇷 GR | 3750 |
| 15 | 🇳🇴 NO | 3551 |
| 16 | 🇨🇭 CH | 3377 |
| 17 | 🇹🇷 TR | 2913 |
| 18 | 🇲🇾 MY | 2623 |
| 19 | 🇿🇦 ZA | 2171 |
| 20 | 🇵🇱 PL | 2153 |
| 21 | 🇳🇿 NZ | 2082 |
| 22 | 🇹🇭 TH | 2034 |
| 23 | 🇰🇷 KR | 1966 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1782 |
| 26 | 🇲🇦 MA | 1398 |
| 27 | 🇲🇪 ME | 1297 |
| 28 | 🇳🇱 NL | 1232 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2735 |
| 2 | Denver International Airport |  | US | 2225 |
| 3 | Tokyo International Airport |  | JP | 1856 |
| 4 | Indira Gandhi International Airport |  | IN | 1700 |
| 5 | Harry Reid International Airport |  | US | 1630 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1547 |
| 8 | Zurich Airport |  | CH | 1446 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1397 |
| 10 | La Aurora Airport |  | GT | 1378 |
| 11 | Frankfurt am Main International Airport |  | DE | 1326 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1267 |
| 13 | Chicago O'Hare International Airport |  | US | 1259 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1174 |
| 16 | Salt Lake City International Airport |  | US | 1164 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1120 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1077 |
| 19 | Madrid Barajas International Airport |  | ES | 1076 |
| 20 | Capua Airport |  | IT | 1075 |
| 21 | Congonhas Airport |  | BR | 1042 |
| 22 | Kuala Lumpur International Airport |  | MY | 1018 |
| 23 | Charlotte/Douglas International Airport |  | US | 975 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 952 |
| 26 | Bengaluru International Airport |  | IN | 930 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 896 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 821 |
| 31 | Barcelona International Airport |  | ES | 814 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 798 |
| 33 | Tenerife Norte Airport |  | ES | 793 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 771 |
| 35 | Calgary International Airport |  | CA | 764 |
| 36 | Seattle-Tacoma International Airport |  | US | 756 |
| 37 | Viracopos International Airport |  | BR | 752 |
| 38 | Vitoria/Foronda Airport |  | ES | 752 |
| 39 | Scottsdale Airport |  | US | 748 |
| 40 | Amsterdam Airport Schiphol |  | NL | 744 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 474 | 21m | 244 km | 1,995.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 317 | 1h 10m | 770 km | 4,211.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 248 | 26m | 275 km | 1,175.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 183 | 26m | 215 km | 677.8 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 173 | 1h 46m | 1,423 km | 4,245.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 161 | 18m | 144 km | 400.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 158 | 44m | 452 km | 1,231.4 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 157 | 30m | 49 km | 132.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CHX45 | CHX | Leutkirch-Unterzeil Airport (EDNL) | Friedrichshafen Airport (EDNY) | 2026-07-06 16:05 UTC | 2026-07-06 16:28 UTC | 22m |
| N8348M |  | San Marcos Regional Airport (KHYI) | San Marcos Regional Airport (KHYI) | 2026-07-06 16:10 UTC | 2026-07-06 16:25 UTC | 15m |
| N53SL |  | Frederick Municipal Airport (KFDK) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-06 15:24 UTC | 2026-07-06 16:22 UTC | 57m |
| JIA5640 | JIA | John Glenn Columbus International Airport (KCMH) | Philadelphia International Airport (KPHL) | 2026-07-06 15:06 UTC | 2026-07-06 16:20 UTC | 1h 14m |
| N600MU |  | Rocky Mountain Metro Airport (KBJC) | Hendricks Field At West Creek Ranch Airport (63CO) | 2026-07-06 15:11 UTC | 2026-07-06 16:14 UTC | 1h 2m |
| N865PH |  | Lincoln Regional/Karl Harder Field (KLHM) | Truckee-Tahoe Airport (KTRK) | 2026-07-06 15:38 UTC | 2026-07-06 16:13 UTC | 34m |
| CFVZM | CFV | Edson Airport (CYET) | Edson Airport (CYET) | 2026-07-06 15:18 UTC | 2026-07-06 16:10 UTC | 51m |
| N152SA |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-07-06 15:42 UTC | 2026-07-06 16:09 UTC | 27m |
| N513BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-07-06 14:59 UTC | 2026-07-06 16:08 UTC | 1h 8m |
| JCB3 | JCB | Tatenhill Airfield (EGBM) | RAF Brize Norton (EGVN) | 2026-07-06 15:40 UTC | 2026-07-06 16:07 UTC | 26m |
| N19629 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-07-06 15:29 UTC | 2026-07-06 16:07 UTC | 37m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-07-06 15:51 UTC | 2026-07-06 16:05 UTC | 13m |
| OST6 | OST | Stillwater Regional Airport (KSWO) | Mulberry Hill Airport (6OK9) | 2026-07-06 15:33 UTC | 2026-07-06 16:03 UTC | 30m |
| N702 |  | Rocky Mountain Metro Airport (KBJC) | Lux Field (25CD) | 2026-07-06 14:31 UTC | 2026-07-06 15:58 UTC | 1h 27m |
| N354WG |  | Boerne Stage Airfield (K5C1) | Skeen Ranch Airport (82NM) | 2026-07-06 15:01 UTC | 2026-07-06 15:58 UTC | 57m |
| N129NB |  | Talaheim Airport (1AK8) | Flyway Farm Airstrip (36AK) | 2026-07-06 15:31 UTC | 2026-07-06 15:55 UTC | 23m |
| CXK166 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-07-06 14:32 UTC | 2026-07-06 15:55 UTC | 1h 22m |
| EAI62N | EAI | Dublin Airport (EIDW) | Newquay Cornwall Airport (EGHQ) | 2026-07-06 14:55 UTC | 2026-07-06 15:53 UTC | 58m |
| N257MM |  | Chester County G O Carlson Airport (KMQS) | Paramount Air Airport (JY04) | 2026-07-06 15:30 UTC | 2026-07-06 15:52 UTC | 21m |
| N9989E |  | Nampa Municipal Airport (KMAN) | Lanham Field (04ID) | 2026-07-06 15:30 UTC | 2026-07-06 15:51 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
