# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_01:39:26_UTC-green)

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

**Latest saved flight:** 2026-09-17 01:39:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 01:39:26 UTC

- **260,916** saved flights
- **77,318** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,916** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,160,395.4 tonnes** estimated CO2 emissions
- **183,211,325 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10323 |
| 2 | SkyWest Airlines | 9090 |
| 3 | EJA | 5059 |
| 4 | IndiGo | 4372 |
| 5 | American Airlines | 4103 |
| 6 | Southwest Airlines | 3837 |
| 7 | Delta Air Lines | 3262 |
| 8 | ENY | 3085 |
| 9 | LATAM Airlines | 2516 |
| 10 | AZU | 2449 |
| 11 | Vueling | 2197 |
| 12 | WIF | 2096 |
| 13 | LXJ | 2039 |
| 14 | Lufthansa | 2024 |
| 15 | easyJet | 1769 |
| 16 | Swiss International | 1733 |
| 17 | QLK | 1685 |
| 18 | AXM | 1649 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1549 |
| 22 | All Nippon Airways | 1514 |
| 23 | WMT | 1469 |
| 24 | GLO | 1454 |
| 25 | PGT | 1453 |
| 26 | Air France | 1431 |
| 27 | VIV | 1429 |
| 28 | Wizz Air | 1414 |
| 29 | TKR | 1274 |
| 30 | AEE | 1260 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216771 |
| 2 | 🇪🇸 ES | 16492 |
| 3 | 🇧🇷 BR | 15261 |
| 4 | 🇦🇺 AU | 14937 |
| 5 | 🇨🇦 CA | 14545 |
| 6 | 🇮🇹 IT | 14189 |
| 7 | 🇮🇳 IN | 13782 |
| 8 | 🇩🇪 DE | 12640 |
| 9 | 🇬🇧 GB | 12128 |
| 10 | 🇨🇴 CO | 11751 |
| 11 | 🇫🇷 FR | 10450 |
| 12 | 🇯🇵 JP | 10139 |
| 13 | 🇹🇷 TR | 7874 |
| 14 | 🇬🇷 GR | 7573 |
| 15 | 🇲🇽 MX | 7187 |
| 16 | 🇨🇭 CH | 6984 |
| 17 | 🇳🇴 NO | 6432 |
| 18 | 🇹🇭 TH | 4680 |
| 19 | 🇲🇾 MY | 4442 |
| 20 | 🇿🇦 ZA | 4406 |
| 21 | 🇵🇱 PL | 4304 |
| 22 | 🇳🇿 NZ | 3619 |
| 23 | 🇵🇭 PH | 3489 |
| 24 | 🇬🇹 GT | 3330 |
| 25 | 🇭🇷 HR | 2979 |
| 26 | 🇰🇷 KR | 2972 |
| 27 | 🇲🇦 MA | 2610 |
| 28 | 🇲🇪 ME | 2453 |
| 29 | 🇳🇱 NL | 2332 |
| 30 | 🇮🇩 ID | 2201 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5348 |
| 2 | Denver International Airport |  | US | 4220 |
| 3 | Indira Gandhi International Airport |  | IN | 3142 |
| 4 | Tokyo International Airport |  | JP | 3027 |
| 5 | Guaymaral Airport |  | CO | 2774 |
| 6 | Harry Reid International Airport |  | US | 2772 |
| 7 | El Dorado International Airport |  | CO | 2741 |
| 8 | Zurich Airport |  | CH | 2726 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2627 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2534 |
| 11 | La Aurora Airport |  | GT | 2527 |
| 12 | Salt Lake City International Airport |  | US | 2302 |
| 13 | Chicago O'Hare International Airport |  | US | 2260 |
| 14 | Congonhas Airport |  | BR | 2228 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2129 |
| 16 | Capua Airport |  | IT | 2034 |
| 17 | Madrid Barajas International Airport |  | ES | 2018 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1968 |
| 20 | Malpensa International Airport |  | IT | 1877 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1875 |
| 22 | Charles de Gaulle International Airport |  | FR | 1843 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1841 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1781 |
| 26 | Macau International Airport |  | MO | 1729 |
| 27 | Ninoy Aquino International Airport |  | PH | 1712 |
| 28 | Barcelona International Airport |  | ES | 1628 |
| 29 | Charlotte/Douglas International Airport |  | US | 1627 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1604 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1580 |
| 33 | Seattle-Tacoma International Airport |  | US | 1530 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1520 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1492 |
| 37 | Bengaluru International Airport |  | IN | 1479 |
| 38 | Oslo Gardermoen Airport |  | NO | 1465 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1111 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 973 | 21m | 244 km | 4,097.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 654 | 1h 6m | 770 km | 8,687.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 651 | 24m | 225 km | 2,525.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 585 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 421 | 27m | 275 km | 1,994.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 396 | 44m | 241 km | 1,644.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 366 | 24m | 218 km | 1,378.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 317 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 301 | 1h 14m | 961 km | 4,989.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 300 | 19m | 144 km | 746.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 282 | 1h 50m | 1,304 km | 6,344.3 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 277 | 42m | 535 km | 2,558.3 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RCH135 | RCH | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | 2026-09-17 01:04 UTC | 2026-09-17 01:39 UTC | 35m |
| ZKWKF | ZKW | Hamilton International Airport (NZHN) | Te Kowhai Airfield (NZTE) | 2026-09-17 01:18 UTC | 2026-09-17 01:35 UTC | 17m |
| NCR521 | NCR | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-09-16 18:39 UTC | 2026-09-17 01:33 UTC | 6h 54m |
| N9562Q |  | Caldwell Executive Airport (KEUL) | Reek Ranch Airport (ID63) | 2026-09-17 00:57 UTC | 2026-09-17 01:25 UTC | 27m |
| BAW135 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-16 17:03 UTC | 2026-09-17 01:22 UTC | 8h 19m |
| N912PF |  | CA40 (CA40) | Delano Municipal Airport (KDLO) | 2026-09-17 00:46 UTC | 2026-09-17 01:19 UTC | 32m |
| N5262Y |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-09-17 00:42 UTC | 2026-09-17 01:18 UTC | 36m |
| N125MG |  | Prineville Airport (KS39) | Dry Creek Airpark (OG21) | 2026-09-17 00:49 UTC | 2026-09-17 01:13 UTC | 24m |
| EJM377 | EJM | Washington Dulles International Airport (KIAD) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-17 00:07 UTC | 2026-09-17 01:11 UTC | 1h 4m |
| NPS | NPS | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-17 00:59 UTC | 2026-09-17 01:11 UTC | 12m |
| AAL957Q | American Airlines | Tampa International Airport (KTPA) | Dallas-Fort Worth International Airport (KDFW) | 2026-09-16 23:04 UTC | 2026-09-17 01:10 UTC | 2h 6m |
| N49RH |  | Colonel James Jabara Airport (KAAO) | Colonel James Jabara Airport (KAAO) | 2026-09-17 00:50 UTC | 2026-09-17 01:09 UTC | 19m |
| TWY564 | TWY | Pittsburgh International Airport (KPIT) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-16 20:54 UTC | 2026-09-17 01:09 UTC | 4h 14m |
| NBJ | NBJ | Adelaide Parafield Airport (YPPF) | Port Pirie Airport (YPIR) | 2026-09-17 00:05 UTC | 2026-09-17 01:07 UTC | 1h 1m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-17 00:39 UTC | 2026-09-17 01:04 UTC | 24m |
| N776TX |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-17 00:34 UTC | 2026-09-17 01:03 UTC | 29m |
| N714F |  | Dupage Airport (KDPA) | Logan-Cache Airport (KLGU) | 2026-09-16 22:10 UTC | 2026-09-17 01:01 UTC | 2h 51m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-09-16 18:00 UTC | 2026-09-17 01:00 UTC | 7h 0m |
| TKR210 | TKR | 5TA6 (5TA6) | Bruce Field (KE30) | 2026-09-17 00:15 UTC | 2026-09-17 00:59 UTC | 43m |
| WSN7 | WSN | Long Beach (Daugherty Field) Airport (KLGB) | Sun Hill Ranch Airport (CA70) | 2026-09-17 00:30 UTC | 2026-09-17 00:57 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
