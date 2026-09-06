# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_19:00:55_UTC-green)

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

**Latest saved flight:** 2026-09-06 19:00:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 19:00:55 UTC

- **249,816** saved flights
- **75,069** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **249,816** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,007,399.6 tonnes** estimated CO2 emissions
- **174,342,006 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10003 |
| 2 | SkyWest Airlines | 8717 |
| 3 | EJA | 4823 |
| 4 | IndiGo | 4175 |
| 5 | American Airlines | 3998 |
| 6 | Southwest Airlines | 3711 |
| 7 | Delta Air Lines | 3166 |
| 8 | ENY | 2990 |
| 9 | LATAM Airlines | 2410 |
| 10 | AZU | 2325 |
| 11 | Vueling | 2133 |
| 12 | WIF | 1997 |
| 13 | Lufthansa | 1982 |
| 14 | LXJ | 1938 |
| 15 | easyJet | 1723 |
| 16 | Swiss International | 1679 |
| 17 | AXM | 1628 |
| 18 | EJU | 1609 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1566 |
| 21 | Alaska Airlines | 1491 |
| 22 | All Nippon Airways | 1465 |
| 23 | WMT | 1418 |
| 24 | GLO | 1392 |
| 25 | VIV | 1371 |
| 26 | PGT | 1370 |
| 27 | Air France | 1361 |
| 28 | Wizz Air | 1359 |
| 29 | AEE | 1228 |
| 30 | JetBlue | 1226 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207149 |
| 2 | 🇪🇸 ES | 15991 |
| 3 | 🇧🇷 BR | 14590 |
| 4 | 🇦🇺 AU | 14152 |
| 5 | 🇨🇦 CA | 13866 |
| 6 | 🇮🇹 IT | 13693 |
| 7 | 🇮🇳 IN | 13025 |
| 8 | 🇩🇪 DE | 12295 |
| 9 | 🇬🇧 GB | 11723 |
| 10 | 🇨🇴 CO | 10957 |
| 11 | 🇫🇷 FR | 10074 |
| 12 | 🇯🇵 JP | 9861 |
| 13 | 🇹🇷 TR | 7450 |
| 14 | 🇬🇷 GR | 7352 |
| 15 | 🇲🇽 MX | 6904 |
| 16 | 🇨🇭 CH | 6742 |
| 17 | 🇳🇴 NO | 6185 |
| 18 | 🇹🇭 TH | 4504 |
| 19 | 🇲🇾 MY | 4369 |
| 20 | 🇿🇦 ZA | 4305 |
| 21 | 🇵🇱 PL | 4174 |
| 22 | 🇳🇿 NZ | 3405 |
| 23 | 🇵🇭 PH | 3395 |
| 24 | 🇬🇹 GT | 3131 |
| 25 | 🇰🇷 KR | 2896 |
| 26 | 🇭🇷 HR | 2874 |
| 27 | 🇲🇦 MA | 2526 |
| 28 | 🇲🇪 ME | 2348 |
| 29 | 🇳🇱 NL | 2259 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5155 |
| 2 | Denver International Airport |  | US | 4038 |
| 3 | Indira Gandhi International Airport |  | IN | 3038 |
| 4 | Tokyo International Airport |  | JP | 2944 |
| 5 | Guaymaral Airport |  | CO | 2736 |
| 6 | Harry Reid International Airport |  | US | 2654 |
| 7 | Zurich Airport |  | CH | 2617 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2535 |
| 9 | El Dorado International Airport |  | CO | 2521 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2478 |
| 11 | La Aurora Airport |  | GT | 2387 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2185 |
| 14 | Congonhas Airport |  | BR | 2144 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2056 |
| 16 | Capua Airport |  | IT | 1970 |
| 17 | Madrid Barajas International Airport |  | ES | 1965 |
| 18 | Frankfurt am Main International Airport |  | DE | 1952 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1874 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1820 |
| 21 | Malpensa International Airport |  | IT | 1800 |
| 22 | Charles de Gaulle International Airport |  | FR | 1751 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1741 |
| 25 | Ninoy Aquino International Airport |  | PH | 1655 |
| 26 | Macau International Airport |  | MO | 1646 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1583 |
| 29 | Barcelona International Airport |  | ES | 1582 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1531 |
| 32 | Viracopos International Airport |  | BR | 1495 |
| 33 | Seattle-Tacoma International Airport |  | US | 1468 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1442 |
| 36 | Calgary International Airport |  | CA | 1435 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1407 |
| 39 | Vancouver International Airport |  | CA | 1396 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 398 | 1h 50m | 1,423 km | 9,767.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 388 | 44m | 555 km | 3,715.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 371 | 44m | 241 km | 1,541.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 289 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1904 | IndiGo | Eleftherios Venizelos International Airport (LGAV) | Pune Airport (VAPO) | 2026-09-06 12:07 UTC | 2026-09-06 19:00 UTC | 6h 53m |
| DLH756 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-06 11:35 UTC | 2026-09-06 18:58 UTC | 7h 22m |
| EZS79EL | EZS | Geneva Cointrin International Airport (LSGG) | Brussels Airport (EBBR) | 2026-09-06 17:59 UTC | 2026-09-06 18:54 UTC | 55m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-09-06 18:47 UTC | 2026-09-06 18:49 UTC | 1m |
| N40JF |  | 0OI4 (0OI4) | 1OI1 (1OI1) | 2026-09-06 18:31 UTC | 2026-09-06 18:47 UTC | 16m |
| QAV30E | QAV | Palma De Mallorca Airport (LEPA) | Poznań-Ławica Airport (EPPO) | 2026-09-06 16:12 UTC | 2026-09-06 18:45 UTC | 2h 32m |
| N911ZE |  | Tyler Pounds Regional Airport (KTYR) | Gregory M Simmons Memorial Airport (KGZN) | 2026-09-06 17:55 UTC | 2026-09-06 18:44 UTC | 49m |
| N1UK |  | Quakertown Airport (KUKT) | Heritage Field (KPTW) | 2026-09-06 18:30 UTC | 2026-09-06 18:42 UTC | 11m |
| IGO1186 | IndiGo | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-06 14:22 UTC | 2026-09-06 18:36 UTC | 4h 14m |
| 00000000 |  | La Aurora Airport (MGGT) | El Palmer Airport (MSSA) | 2026-09-06 18:20 UTC | 2026-09-06 18:34 UTC | 14m |
| N223LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-06 17:48 UTC | 2026-09-06 18:33 UTC | 45m |
| PTORI | PTO | Fazenda Agua Limpa Airport (SJAF) | Fazenda Panflora Airport (SWRJ) | 2026-09-06 18:01 UTC | 2026-09-06 18:31 UTC | 29m |
| N8720K |  | Pegasus Airpark (5AZ3) | Montezuma Airport (19AZ) | 2026-09-06 18:00 UTC | 2026-09-06 18:30 UTC | 29m |
| N114JR |  | French Valley Airport (KF70) | Riverside Airport (KRAL) | 2026-09-06 18:10 UTC | 2026-09-06 18:30 UTC | 19m |
| ASI541 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-09-06 18:07 UTC | 2026-09-06 18:29 UTC | 22m |
| UBG307 | UBG | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-09-06 17:33 UTC | 2026-09-06 18:29 UTC | 56m |
| N715TW |  | Mcminn County Airport (KMMI) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-06 17:10 UTC | 2026-09-06 18:26 UTC | 1h 16m |
| N350KR |  | Baton Rouge Metro, Ryan Field (KBTR) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-06 17:21 UTC | 2026-09-06 18:26 UTC | 1h 5m |
| EJA833 | EJA | Chumchal Farms Airport (71TA) | Henderson Executive Airport (KHND) | 2026-09-06 16:42 UTC | 2026-09-06 18:25 UTC | 1h 43m |
| IGO1856 | IndiGo | Seychelles International Airport (FSIA) | Pune Airport (VAPO) | 2026-09-06 14:15 UTC | 2026-09-06 18:25 UTC | 4h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
