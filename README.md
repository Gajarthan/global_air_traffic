# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_14:15:38_UTC-green)

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

**Latest saved flight:** 2026-09-13 14:15:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 14:15:38 UTC

- **257,231** saved flights
- **76,582** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,231** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,111,512.4 tonnes** estimated CO2 emissions
- **180,377,530 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10223 |
| 2 | SkyWest Airlines | 8957 |
| 3 | EJA | 4966 |
| 4 | IndiGo | 4317 |
| 5 | American Airlines | 4064 |
| 6 | Southwest Airlines | 3783 |
| 7 | Delta Air Lines | 3221 |
| 8 | ENY | 3048 |
| 9 | LATAM Airlines | 2472 |
| 10 | AZU | 2400 |
| 11 | Vueling | 2177 |
| 12 | WIF | 2060 |
| 13 | Lufthansa | 2014 |
| 14 | LXJ | 2007 |
| 15 | easyJet | 1758 |
| 16 | Swiss International | 1721 |
| 17 | QLK | 1660 |
| 18 | AXM | 1646 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1592 |
| 21 | Alaska Airlines | 1527 |
| 22 | All Nippon Airways | 1497 |
| 23 | WMT | 1453 |
| 24 | GLO | 1433 |
| 25 | PGT | 1427 |
| 26 | VIV | 1407 |
| 27 | Air France | 1404 |
| 28 | Wizz Air | 1398 |
| 29 | TKR | 1247 |
| 30 | AEE | 1246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213419 |
| 2 | 🇪🇸 ES | 16342 |
| 3 | 🇧🇷 BR | 15007 |
| 4 | 🇦🇺 AU | 14660 |
| 5 | 🇨🇦 CA | 14325 |
| 6 | 🇮🇹 IT | 14044 |
| 7 | 🇮🇳 IN | 13539 |
| 8 | 🇩🇪 DE | 12539 |
| 9 | 🇬🇧 GB | 12000 |
| 10 | 🇨🇴 CO | 11521 |
| 11 | 🇫🇷 FR | 10339 |
| 12 | 🇯🇵 JP | 10042 |
| 13 | 🇹🇷 TR | 7738 |
| 14 | 🇬🇷 GR | 7496 |
| 15 | 🇲🇽 MX | 7096 |
| 16 | 🇨🇭 CH | 6909 |
| 17 | 🇳🇴 NO | 6357 |
| 18 | 🇹🇭 TH | 4639 |
| 19 | 🇲🇾 MY | 4425 |
| 20 | 🇿🇦 ZA | 4380 |
| 21 | 🇵🇱 PL | 4268 |
| 22 | 🇳🇿 NZ | 3556 |
| 23 | 🇵🇭 PH | 3466 |
| 24 | 🇬🇹 GT | 3257 |
| 25 | 🇭🇷 HR | 2953 |
| 26 | 🇰🇷 KR | 2948 |
| 27 | 🇲🇦 MA | 2586 |
| 28 | 🇲🇪 ME | 2421 |
| 29 | 🇳🇱 NL | 2316 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5267 |
| 2 | Denver International Airport |  | US | 4156 |
| 3 | Indira Gandhi International Airport |  | IN | 3114 |
| 4 | Tokyo International Airport |  | JP | 2997 |
| 5 | Guaymaral Airport |  | CO | 2762 |
| 6 | Harry Reid International Airport |  | US | 2724 |
| 7 | Zurich Airport |  | CH | 2694 |
| 8 | El Dorado International Airport |  | CO | 2677 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2594 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2511 |
| 11 | La Aurora Airport |  | GT | 2474 |
| 12 | Salt Lake City International Airport |  | US | 2265 |
| 13 | Chicago O'Hare International Airport |  | US | 2239 |
| 14 | Congonhas Airport |  | BR | 2201 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2098 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2007 |
| 18 | Frankfurt am Main International Airport |  | DE | 1986 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1928 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1857 |
| 21 | Malpensa International Airport |  | IT | 1853 |
| 22 | Charles de Gaulle International Airport |  | FR | 1812 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1808 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1782 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1740 |
| 26 | Macau International Airport |  | MO | 1706 |
| 27 | Ninoy Aquino International Airport |  | PH | 1697 |
| 28 | Barcelona International Airport |  | ES | 1617 |
| 29 | Charlotte/Douglas International Airport |  | US | 1608 |
| 30 | Kuala Lumpur International Airport |  | MY | 1592 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1576 |
| 32 | Viracopos International Airport |  | BR | 1542 |
| 33 | Seattle-Tacoma International Airport |  | US | 1506 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1493 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1471 |
| 37 | Bengaluru International Airport |  | IN | 1462 |
| 38 | Oslo Gardermoen Airport |  | NO | 1452 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1389 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 691 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 388 | 44m | 241 km | 1,611.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 360 | 24m | 218 km | 1,356.3 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 318 | 26m | 215 km | 1,177.7 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 306 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 298 | 19m | 144 km | 741.3 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 296 | 1h 14m | 961 km | 4,906.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-09-13 14:01 UTC | 2026-09-13 14:15 UTC | 14m |
| N5128D |  | Lakeland Linder International Airport (KLAL) | Bartow Executive Airport (KBOW) | 2026-09-13 13:54 UTC | 2026-09-13 14:09 UTC | 14m |
| CXK601 | CXK | Tucson International Airport (KTUS) | Ryan Field (KRYN) | 2026-09-13 13:24 UTC | 2026-09-13 14:03 UTC | 39m |
| CXK663 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-13 12:32 UTC | 2026-09-13 14:02 UTC | 1h 29m |
| N690TW |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-09-13 13:45 UTC | 2026-09-13 13:55 UTC | 10m |
| CAP4221 | CAP | Majors Airport (KGVT) | Commerce Municipal Airport (K2F7) | 2026-09-13 13:31 UTC | 2026-09-13 13:52 UTC | 21m |
| N393CF |  | Guaymaral Airport (SKGY) | La Nubia Airport (SKMZ) | 2026-09-13 13:23 UTC | 2026-09-13 13:51 UTC | 27m |
| CAL163 | CAL | Incheon International Airport (RKSI) | Hsinchu Air Base (RCPO) | 2026-09-13 11:43 UTC | 2026-09-13 13:49 UTC | 2h 5m |
| CPA742 | Cathay Pacific | Wuzhou Xijiang Airport (ZGWZ) | Zhuhai Airport (ZGSD) | 2026-09-13 13:19 UTC | 2026-09-13 13:44 UTC | 25m |
| N132TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-13 13:21 UTC | 2026-09-13 13:41 UTC | 19m |
| N744TT |  | K4A7 (K4A7) | K4A7 (K4A7) | 2026-09-13 13:38 UTC | 2026-09-13 13:40 UTC | 2m |
| AKJ585 | AKJ | Abu Dhabi International Airport (OMAA) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 11:01 UTC | 2026-09-13 13:40 UTC | 2h 38m |
| N53037 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-13 13:08 UTC | 2026-09-13 13:39 UTC | 31m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-09-13 06:36 UTC | 2026-09-13 13:34 UTC | 6h 57m |
| N1286C |  | Falcon Field (KFFZ) | San Carlos Apache Airport (KP13) | 2026-09-13 13:07 UTC | 2026-09-13 13:30 UTC | 23m |
| N1377M |  | De Kalb Taylor Municipal Airport (KDKB) | De Kalb Taylor Municipal Airport (KDKB) | 2026-09-13 13:28 UTC | 2026-09-13 13:28 UTC | 0m |
| N1653F |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-13 12:52 UTC | 2026-09-13 13:28 UTC | 35m |
| CXK1079 | CXK | Perry County Municipal Airport (KTEL) | Clark Regional Airport (KJVY) | 2026-09-13 12:55 UTC | 2026-09-13 13:25 UTC | 29m |
| IGO626M | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-13 11:28 UTC | 2026-09-13 13:24 UTC | 1h 55m |
| ETD947 | Etihad Airways | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-09-12 13:59 UTC | 2026-09-13 13:23 UTC | 23h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
