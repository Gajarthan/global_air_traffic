# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_19:56:56_UTC-green)

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

**Latest saved flight:** 2026-08-14 19:56:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 19:56:56 UTC

- **196,434** saved flights
- **61,679** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **196,434** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,345,449.9 tonnes** estimated CO2 emissions
- **135,968,111 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7808 |
| 2 | SkyWest Airlines | 7060 |
| 3 | EJA | 3869 |
| 4 | IndiGo | 3384 |
| 5 | Southwest Airlines | 3046 |
| 6 | American Airlines | 3030 |
| 7 | ENY | 2427 |
| 8 | Delta Air Lines | 2320 |
| 9 | LATAM Airlines | 1840 |
| 10 | AZU | 1771 |
| 11 | Lufthansa | 1695 |
| 12 | Vueling | 1640 |
| 13 | WIF | 1627 |
| 14 | LXJ | 1557 |
| 15 | easyJet | 1349 |
| 16 | Swiss International | 1328 |
| 17 | AXM | 1277 |
| 18 | EJU | 1216 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1161 |
| 22 | VIV | 1082 |
| 23 | GLO | 1057 |
| 24 | Air France | 1034 |
| 25 | PGT | 1024 |
| 26 | AEE | 1010 |
| 27 | CXK | 1005 |
| 28 | United Airlines | 1000 |
| 29 | WMT | 984 |
| 30 | Wizz Air | 972 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167031 |
| 2 | 🇪🇸 ES | 12695 |
| 3 | 🇧🇷 BR | 11279 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10752 |
| 6 | 🇮🇳 IN | 10585 |
| 7 | 🇮🇹 IT | 10238 |
| 8 | 🇩🇪 DE | 9765 |
| 9 | 🇬🇧 GB | 9231 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7833 |
| 12 | 🇨🇴 CO | 7690 |
| 13 | 🇬🇷 GR | 5776 |
| 14 | 🇲🇽 MX | 5557 |
| 15 | 🇹🇷 TR | 5349 |
| 16 | 🇨🇭 CH | 5314 |
| 17 | 🇳🇴 NO | 5037 |
| 18 | 🇲🇾 MY | 3342 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3243 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2589 |
| 24 | 🇬🇹 GT | 2507 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2052 |
| 27 | 🇲🇦 MA | 1988 |
| 28 | 🇳🇱 NL | 1769 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1584 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4080 |
| 2 | Denver International Airport |  | US | 3203 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2435 |
| 5 | Indira Gandhi International Airport |  | IN | 2391 |
| 6 | Harry Reid International Airport |  | US | 2260 |
| 7 | Zurich Airport |  | CH | 2078 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2077 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2031 |
| 10 | La Aurora Airport |  | GT | 1921 |
| 11 | El Dorado International Airport |  | CO | 1789 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1755 |
| 13 | Salt Lake City International Airport |  | US | 1746 |
| 14 | Chicago O'Hare International Airport |  | US | 1714 |
| 15 | Frankfurt am Main International Airport |  | DE | 1662 |
| 16 | Congonhas Airport |  | BR | 1643 |
| 17 | Madrid Barajas International Airport |  | ES | 1547 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1502 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1498 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1450 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1411 |
| 23 | Malpensa International Airport |  | IT | 1364 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1302 |
| 27 | Kuala Lumpur International Airport |  | MY | 1246 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1227 |
| 30 | Ninoy Aquino International Airport |  | PH | 1224 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1202 |
| 32 | Barcelona International Airport |  | ES | 1181 |
| 33 | Viracopos International Airport |  | BR | 1139 |
| 34 | Seattle-Tacoma International Airport |  | US | 1126 |
| 35 | Calgary International Airport |  | CA | 1116 |
| 36 | Reno/Tahoe International Airport |  | US | 1111 |
| 37 | Oslo Gardermoen Airport |  | NO | 1108 |
| 38 | Daniel K Inouye International Airport |  | US | 1092 |
| 39 | Vitoria/Foronda Airport |  | ES | 1080 |
| 40 | Tenerife Norte Airport |  | ES | 1076 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1005 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 720 | 21m | 244 km | 3,031.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 457 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 339 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 296 | 44m | 241 km | 1,229.5 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 280 | 22m | 55 km | 266.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 242 | 24m | 218 km | 911.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 239 | 1h 15m | 961 km | 3,961.6 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 239 | 19m | 99 km | 409.4 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 232 | 1h 38m | 1,156 km | 4,628.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 214 | 28m | 152 km | 559.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 213 | 1h 3m | 695 km | 2,553.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4549F |  | Dubois Regional Airport (KDUJ) | Punxsutawney Municipal Airport (KN35) | 2026-08-14 19:25 UTC | 2026-08-14 19:56 UTC | 31m |
| N359DG |  | Visalia Municipal Airport (KVIS) | Henderson Executive Airport (KHND) | 2026-08-14 19:05 UTC | 2026-08-14 19:54 UTC | 49m |
| N372GG |  | Lawrence Regional Airport (KLWC) | Lawrence Regional Airport (KLWC) | 2026-08-14 19:45 UTC | 2026-08-14 19:45 UTC | 0m |
| N622TP |  | Wurtsboro/Sullivan County Airport (KN82) | Laguardia Airport (KLGA) | 2026-08-14 19:24 UTC | 2026-08-14 19:45 UTC | 21m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-08-14 08:41 UTC | 2026-08-14 19:39 UTC | 10h 58m |
| N685MA |  | Indianapolis Regional Airport (KMQJ) | Indianapolis Regional Airport (KMQJ) | 2026-08-14 18:53 UTC | 2026-08-14 19:38 UTC | 45m |
| N7756X |  | Fountains Airport (ID60) | Spokane International Airport (KGEG) | 2026-08-14 18:49 UTC | 2026-08-14 19:37 UTC | 47m |
| N605FB |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-08-14 18:53 UTC | 2026-08-14 19:36 UTC | 43m |
| CXK610 | CXK | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-14 19:05 UTC | 2026-08-14 19:35 UTC | 30m |
| BOX746 | BOX | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-14 09:55 UTC | 2026-08-14 19:33 UTC | 9h 37m |
| N351RB |  | Fort Worth Spinks Airport (KFWS) | Selfs Airport (KMMS) | 2026-08-14 18:12 UTC | 2026-08-14 19:31 UTC | 1h 19m |
| N76015 |  | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-08-14 18:38 UTC | 2026-08-14 19:29 UTC | 51m |
| ESPWB | ESP | Tallinn Airport (EETN) | Tallinn Airport (EETN) | 2026-08-14 19:04 UTC | 2026-08-14 19:24 UTC | 20m |
| N7874N |  | City Of Colorado Springs Municipal Airport (KCOS) | Southeast Colorado Regional Airport (KLAA) | 2026-08-14 18:17 UTC | 2026-08-14 19:21 UTC | 1h 3m |
| N100BW |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-14 18:50 UTC | 2026-08-14 19:21 UTC | 31m |
| LXJ440 | LXJ | Miami-Opa Locka Executive Airport (KOPF) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-14 14:05 UTC | 2026-08-14 19:20 UTC | 5h 15m |
| N4759R |  | Brigham City Regional Airport (KBMC) | Brigham City Regional Airport (KBMC) | 2026-08-14 19:04 UTC | 2026-08-14 19:20 UTC | 15m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-14 18:47 UTC | 2026-08-14 19:19 UTC | 32m |
| N1710A |  | CL36 (CL36) | Truckee-Tahoe Airport (KTRK) | 2026-08-14 18:34 UTC | 2026-08-14 19:18 UTC | 44m |
| BUBO31 | BUB | Flysooner Field (OK50) | 6OK0 (6OK0) | 2026-08-14 19:02 UTC | 2026-08-14 19:18 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
