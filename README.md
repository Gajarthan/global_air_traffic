# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_07:54:22_UTC-green)

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

**Latest saved flight:** 2026-08-26 07:54:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 07:54:22 UTC

- **237,737** saved flights
- **72,414** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **237,737** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,863,344.6 tonnes** estimated CO2 emissions
- **165,990,994 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9515 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4006 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3613 |
| 7 | Delta Air Lines | 3034 |
| 8 | ENY | 2881 |
| 9 | LATAM Airlines | 2283 |
| 10 | AZU | 2216 |
| 11 | Vueling | 2035 |
| 12 | Lufthansa | 1923 |
| 13 | WIF | 1887 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1657 |
| 16 | Swiss International | 1591 |
| 17 | AXM | 1588 |
| 18 | QLK | 1524 |
| 19 | EJU | 1522 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1416 |
| 23 | GLO | 1329 |
| 24 | WMT | 1327 |
| 25 | VIV | 1312 |
| 26 | PGT | 1297 |
| 27 | Air France | 1285 |
| 28 | Wizz Air | 1269 |
| 29 | JetBlue | 1180 |
| 30 | AEE | 1177 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197423 |
| 2 | 🇪🇸 ES | 15241 |
| 3 | 🇧🇷 BR | 13885 |
| 4 | 🇦🇺 AU | 13539 |
| 5 | 🇨🇦 CA | 13175 |
| 6 | 🇮🇹 IT | 12954 |
| 7 | 🇮🇳 IN | 12490 |
| 8 | 🇩🇪 DE | 11692 |
| 9 | 🇬🇧 GB | 11185 |
| 10 | 🇨🇴 CO | 10123 |
| 11 | 🇯🇵 JP | 9622 |
| 12 | 🇫🇷 FR | 9513 |
| 13 | 🇹🇷 TR | 7055 |
| 14 | 🇬🇷 GR | 6998 |
| 15 | 🇲🇽 MX | 6603 |
| 16 | 🇨🇭 CH | 6341 |
| 17 | 🇳🇴 NO | 5872 |
| 18 | 🇹🇭 TH | 4277 |
| 19 | 🇲🇾 MY | 4256 |
| 20 | 🇿🇦 ZA | 4159 |
| 21 | 🇵🇱 PL | 3946 |
| 22 | 🇳🇿 NZ | 3290 |
| 23 | 🇵🇭 PH | 3283 |
| 24 | 🇬🇹 GT | 2978 |
| 25 | 🇰🇷 KR | 2809 |
| 26 | 🇭🇷 HR | 2739 |
| 27 | 🇲🇦 MA | 2396 |
| 28 | 🇲🇪 ME | 2212 |
| 29 | 🇳🇱 NL | 2128 |
| 30 | 🇮🇩 ID | 2080 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3851 |
| 3 | Indira Gandhi International Airport |  | IN | 2904 |
| 4 | Tokyo International Airport |  | JP | 2865 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2538 |
| 7 | Zurich Airport |  | CH | 2485 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2436 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2375 |
| 10 | El Dorado International Airport |  | CO | 2277 |
| 11 | La Aurora Airport |  | GT | 2269 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2024 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1882 |
| 17 | Capua Airport |  | IT | 1870 |
| 18 | Madrid Barajas International Airport |  | ES | 1864 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1794 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1752 |
| 21 | Malpensa International Airport |  | IT | 1705 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1677 |
| 24 | Charles de Gaulle International Airport |  | FR | 1647 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1590 |
| 27 | Kuala Lumpur International Airport |  | MY | 1539 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1504 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1492 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1442 |
| 32 | Viracopos International Airport |  | BR | 1418 |
| 33 | Seattle-Tacoma International Airport |  | US | 1392 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 35 | Bengaluru International Airport |  | IN | 1390 |
| 36 | Don Mueang International Airport |  | TH | 1383 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1329 |
| 39 | Vancouver International Airport |  | CA | 1302 |
| 40 | O. R. Tambo International Airport |  | ZA | 1293 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 876 | 21m | 244 km | 3,688.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 608 | 24m | 225 km | 2,358.8 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 605 | 1h 6m | 770 km | 8,037.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 392 | 27m | 275 km | 1,857.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 370 | 1h 50m | 1,423 km | 9,080.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 364 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 353 | 44m | 555 km | 3,380.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 344 | 44m | 241 km | 1,428.9 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 337 | 21m | 250 km | 1,455.6 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 320 | 1h 7m | 706 km | 3,896.0 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 319 | 24m | 218 km | 1,201.8 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 316 | 1h 40m | 1,156 km | 6,304.1 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 296 | 19m | 99 km | 507.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 291 | 27m | 215 km | 1,077.7 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 276 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR83B | Qatar Airways | Jomo Kenyatta International Airport (HKJK) | Hamad International Airport (OTHH) | 2026-08-25 22:43 UTC | 2026-08-26 07:54 UTC | 9h 10m |
| BPO807 | BPO | Neumunster Airport (EDHN) | Nordholz Airport (ETMN) | 2026-08-26 07:30 UTC | 2026-08-26 07:51 UTC | 21m |
| EIN151 | Aer Lingus | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-26 06:51 UTC | 2026-08-26 07:47 UTC | 55m |
|  |  | Chennai International Airport (VOMM) | Zhuhai Airport (ZGSD) | 2026-08-26 03:03 UTC | 2026-08-26 07:46 UTC | 4h 43m |
| DAL176 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Dublin Airport (EIDW) | 2026-08-26 00:35 UTC | 2026-08-26 07:44 UTC | 7h 9m |
| QLK575D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-26 06:56 UTC | 2026-08-26 07:28 UTC | 31m |
| DFSRT | DFS | Marl Loemuhle Airport (EDLM) | Marl Loemuhle Airport (EDLM) | 2026-08-26 07:06 UTC | 2026-08-26 07:27 UTC | 20m |
| J041KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-08-26 06:58 UTC | 2026-08-26 07:24 UTC | 25m |
| BKA776 | BKA | Indianapolis International Airport (KIND) | Teterboro Airport (KTEB) | 2026-08-26 05:41 UTC | 2026-08-26 07:10 UTC | 1h 28m |
| FC79 |  | G 802 Airport (RKD1) | Sacheon Air Base (RKPS) | 2026-08-26 06:52 UTC | 2026-08-26 07:09 UTC | 17m |
| N487LP |  | AZ00 (AZ00) | Glendale Regional Airport (KGEU) | 2026-08-26 06:01 UTC | 2026-08-26 07:07 UTC | 1h 5m |
| VOZ1595 | Virgin Australia | Melbourne International Airport (YMML) | Newcastle Airport (YWLM) | 2026-08-26 05:50 UTC | 2026-08-26 07:03 UTC | 1h 12m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-26 06:41 UTC | 2026-08-26 07:03 UTC | 21m |
| UBG145 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-26 06:35 UTC | 2026-08-26 07:00 UTC | 24m |
| WIF1X | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-26 06:45 UTC | 2026-08-26 06:57 UTC | 12m |
| ZSDCA | ZSD | Cape Town International Airport (FACT) | Morningside Farm Airport (FAMS) | 2026-08-26 05:23 UTC | 2026-08-26 06:56 UTC | 1h 33m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-25 19:43 UTC | 2026-08-26 06:56 UTC | 11h 13m |
| TRA37G | TRA | Amsterdam Airport Schiphol (EHAM) | Faro Airport (LPFR) | 2026-08-26 03:53 UTC | 2026-08-26 06:56 UTC | 3h 2m |
| VOE76TX | VOE | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Corte Airport (LFKT) | 2026-08-26 06:08 UTC | 2026-08-26 06:54 UTC | 46m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-08-26 00:10 UTC | 2026-08-26 06:54 UTC | 6h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
