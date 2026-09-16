# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_23:31:01_UTC-green)

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

**Latest saved flight:** 2026-09-16 23:31:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 23:31:01 UTC

- **260,796** saved flights
- **77,295** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,796** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,158,920.3 tonnes** estimated CO2 emissions
- **183,125,817 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10323 |
| 2 | SkyWest Airlines | 9089 |
| 3 | EJA | 5056 |
| 4 | IndiGo | 4372 |
| 5 | American Airlines | 4102 |
| 6 | Southwest Airlines | 3833 |
| 7 | Delta Air Lines | 3259 |
| 8 | ENY | 3085 |
| 9 | LATAM Airlines | 2516 |
| 10 | AZU | 2449 |
| 11 | Vueling | 2197 |
| 12 | WIF | 2096 |
| 13 | LXJ | 2038 |
| 14 | Lufthansa | 2023 |
| 15 | easyJet | 1769 |
| 16 | Swiss International | 1733 |
| 17 | QLK | 1682 |
| 18 | AXM | 1649 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1549 |
| 22 | All Nippon Airways | 1511 |
| 23 | WMT | 1469 |
| 24 | GLO | 1454 |
| 25 | PGT | 1453 |
| 26 | Air France | 1431 |
| 27 | VIV | 1428 |
| 28 | Wizz Air | 1414 |
| 29 | TKR | 1270 |
| 30 | AEE | 1260 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216655 |
| 2 | 🇪🇸 ES | 16492 |
| 3 | 🇧🇷 BR | 15261 |
| 4 | 🇦🇺 AU | 14903 |
| 5 | 🇨🇦 CA | 14533 |
| 6 | 🇮🇹 IT | 14188 |
| 7 | 🇮🇳 IN | 13780 |
| 8 | 🇩🇪 DE | 12640 |
| 9 | 🇬🇧 GB | 12127 |
| 10 | 🇨🇴 CO | 11743 |
| 11 | 🇫🇷 FR | 10450 |
| 12 | 🇯🇵 JP | 10127 |
| 13 | 🇹🇷 TR | 7873 |
| 14 | 🇬🇷 GR | 7572 |
| 15 | 🇲🇽 MX | 7185 |
| 16 | 🇨🇭 CH | 6984 |
| 17 | 🇳🇴 NO | 6432 |
| 18 | 🇹🇭 TH | 4680 |
| 19 | 🇲🇾 MY | 4442 |
| 20 | 🇿🇦 ZA | 4406 |
| 21 | 🇵🇱 PL | 4304 |
| 22 | 🇳🇿 NZ | 3611 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3330 |
| 25 | 🇭🇷 HR | 2979 |
| 26 | 🇰🇷 KR | 2972 |
| 27 | 🇲🇦 MA | 2610 |
| 28 | 🇲🇪 ME | 2453 |
| 29 | 🇳🇱 NL | 2332 |
| 30 | 🇮🇩 ID | 2199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5347 |
| 2 | Denver International Airport |  | US | 4216 |
| 3 | Indira Gandhi International Airport |  | IN | 3141 |
| 4 | Tokyo International Airport |  | JP | 3022 |
| 5 | Guaymaral Airport |  | CO | 2774 |
| 6 | Harry Reid International Airport |  | US | 2767 |
| 7 | El Dorado International Airport |  | CO | 2737 |
| 8 | Zurich Airport |  | CH | 2726 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2625 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2534 |
| 11 | La Aurora Airport |  | GT | 2527 |
| 12 | Salt Lake City International Airport |  | US | 2299 |
| 13 | Chicago O'Hare International Airport |  | US | 2260 |
| 14 | Congonhas Airport |  | BR | 2228 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2129 |
| 16 | Capua Airport |  | IT | 2034 |
| 17 | Madrid Barajas International Airport |  | ES | 2018 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1968 |
| 20 | Malpensa International Airport |  | IT | 1876 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1874 |
| 22 | Charles de Gaulle International Airport |  | FR | 1843 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1837 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1781 |
| 26 | Macau International Airport |  | MO | 1726 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1628 |
| 29 | Charlotte/Douglas International Airport |  | US | 1627 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1604 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1580 |
| 33 | Seattle-Tacoma International Airport |  | US | 1530 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1520 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1490 |
| 37 | Bengaluru International Airport |  | IN | 1479 |
| 38 | Oslo Gardermoen Airport |  | NO | 1465 |
| 39 | Vancouver International Airport |  | CA | 1463 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1111 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 973 | 21m | 244 km | 4,097.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 653 | 1h 6m | 770 km | 8,674.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
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
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 328 | 1h 6m | 706 km | 3,993.4 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 326 | 12m | - | - |
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
| CXK613 | CXK | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-09-16 21:55 UTC | 2026-09-16 23:31 UTC | 1h 35m |
| ITY894 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | HE12 (HE12) | 2026-09-16 20:48 UTC | 2026-09-16 23:27 UTC | 2h 38m |
| TKR140 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-09-16 23:07 UTC | 2026-09-16 23:25 UTC | 18m |
| N3733D |  | St Charles County Regional/Smartt Field (KSET) | St Charles County Regional/Smartt Field (KSET) | 2026-09-16 21:47 UTC | 2026-09-16 23:22 UTC | 1h 35m |
| N174EM |  | Palo Alto Airport (KPAO) | San Carlos Airport (KSQL) | 2026-09-16 21:58 UTC | 2026-09-16 23:20 UTC | 1h 22m |
| ADZ5210 | ADZ | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-09-16 16:32 UTC | 2026-09-16 23:19 UTC | 6h 46m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-16 11:46 UTC | 2026-09-16 23:16 UTC | 11h 30m |
| IVW | IVW | Redcliffe Airport (YRED) | Sunshine Coast Airport (YBMC) | 2026-09-16 22:50 UTC | 2026-09-16 23:16 UTC | 25m |
| N834TA |  | Avon Park Executive Airport (KAVO) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-16 22:24 UTC | 2026-09-16 23:13 UTC | 49m |
| N791FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-09-16 22:30 UTC | 2026-09-16 23:08 UTC | 38m |
| N21TQ |  | Centennial Airport (KAPA) | Sheldon Regional Airport (KSHL) | 2026-09-16 22:03 UTC | 2026-09-16 23:08 UTC | 1h 5m |
| N171MD |  | MN38 (MN38) | Rucker Airport (SN29) | 2026-09-16 21:28 UTC | 2026-09-16 23:04 UTC | 1h 35m |
| VKG805 | VKG | Diagoras Airport (LGRP) | Kecskemet Airport (LHKE) | 2026-09-16 21:13 UTC | 2026-09-16 23:04 UTC | 1h 50m |
| GFA056 | Gulf Air | Bahrain International Airport (OBBI) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-16 19:59 UTC | 2026-09-16 23:02 UTC | 3h 3m |
| TGHSD | TGH | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-09-16 22:57 UTC | 2026-09-16 23:02 UTC | 4m |
| N389SR |  | Hollywood Burbank Airport (KBUR) | Meadows Field (KBFL) | 2026-09-16 22:37 UTC | 2026-09-16 23:01 UTC | 23m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-09-16 22:43 UTC | 2026-09-16 23:00 UTC | 16m |
| N118PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Kelso Valley Airport (CN37) | 2026-09-16 22:31 UTC | 2026-09-16 22:58 UTC | 27m |
| N92SK |  | South St Paul Municipal/Richard E Fleming Field (KSGS) | Stocktrade Airport (WI05) | 2026-09-16 22:21 UTC | 2026-09-16 22:58 UTC | 37m |
| TKR138 | TKR | 6CL6 (6CL6) | 6CL6 (6CL6) | 2026-09-16 22:35 UTC | 2026-09-16 22:57 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
