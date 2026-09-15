# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_10:12:23_UTC-green)

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

**Latest saved flight:** 2026-09-15 10:12:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 10:12:23 UTC

- **259,074** saved flights
- **76,940** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,074** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,138,276.2 tonnes** estimated CO2 emissions
- **181,929,055 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10269 |
| 2 | SkyWest Airlines | 9030 |
| 3 | EJA | 5024 |
| 4 | IndiGo | 4347 |
| 5 | American Airlines | 4088 |
| 6 | Southwest Airlines | 3810 |
| 7 | Delta Air Lines | 3237 |
| 8 | ENY | 3070 |
| 9 | LATAM Airlines | 2489 |
| 10 | AZU | 2428 |
| 11 | Vueling | 2191 |
| 12 | WIF | 2081 |
| 13 | LXJ | 2024 |
| 14 | Lufthansa | 2019 |
| 15 | easyJet | 1764 |
| 16 | Swiss International | 1729 |
| 17 | QLK | 1675 |
| 18 | AXM | 1649 |
| 19 | EJU | 1642 |
| 20 | United Airlines | 1598 |
| 21 | Alaska Airlines | 1538 |
| 22 | All Nippon Airways | 1503 |
| 23 | WMT | 1463 |
| 24 | GLO | 1443 |
| 25 | PGT | 1442 |
| 26 | VIV | 1419 |
| 27 | Air France | 1418 |
| 28 | Wizz Air | 1412 |
| 29 | AEE | 1254 |
| 30 | TKR | 1252 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215040 |
| 2 | 🇪🇸 ES | 16417 |
| 3 | 🇧🇷 BR | 15132 |
| 4 | 🇦🇺 AU | 14800 |
| 5 | 🇨🇦 CA | 14411 |
| 6 | 🇮🇹 IT | 14105 |
| 7 | 🇮🇳 IN | 13681 |
| 8 | 🇩🇪 DE | 12592 |
| 9 | 🇬🇧 GB | 12070 |
| 10 | 🇨🇴 CO | 11639 |
| 11 | 🇫🇷 FR | 10403 |
| 12 | 🇯🇵 JP | 10093 |
| 13 | 🇹🇷 TR | 7820 |
| 14 | 🇬🇷 GR | 7544 |
| 15 | 🇲🇽 MX | 7142 |
| 16 | 🇨🇭 CH | 6953 |
| 17 | 🇳🇴 NO | 6397 |
| 18 | 🇹🇭 TH | 4659 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4396 |
| 21 | 🇵🇱 PL | 4286 |
| 22 | 🇳🇿 NZ | 3590 |
| 23 | 🇵🇭 PH | 3478 |
| 24 | 🇬🇹 GT | 3270 |
| 25 | 🇭🇷 HR | 2967 |
| 26 | 🇰🇷 KR | 2961 |
| 27 | 🇲🇦 MA | 2597 |
| 28 | 🇲🇪 ME | 2439 |
| 29 | 🇳🇱 NL | 2325 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5311 |
| 2 | Denver International Airport |  | US | 4189 |
| 3 | Indira Gandhi International Airport |  | IN | 3129 |
| 4 | Tokyo International Airport |  | JP | 3010 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2752 |
| 7 | Zurich Airport |  | CH | 2716 |
| 8 | El Dorado International Airport |  | CO | 2712 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2609 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2527 |
| 11 | La Aurora Airport |  | GT | 2484 |
| 12 | Salt Lake City International Airport |  | US | 2287 |
| 13 | Chicago O'Hare International Airport |  | US | 2250 |
| 14 | Congonhas Airport |  | BR | 2215 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2118 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2014 |
| 18 | Frankfurt am Main International Airport |  | DE | 1993 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1947 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1867 |
| 21 | Malpensa International Airport |  | IT | 1862 |
| 22 | Charles de Gaulle International Airport |  | FR | 1827 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1826 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1788 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1760 |
| 26 | Macau International Airport |  | MO | 1719 |
| 27 | Ninoy Aquino International Airport |  | PH | 1705 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1621 |
| 30 | Kuala Lumpur International Airport |  | MY | 1595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1591 |
| 32 | Viracopos International Airport |  | BR | 1563 |
| 33 | Seattle-Tacoma International Airport |  | US | 1520 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1509 |
| 35 | Don Mueang International Airport |  | TH | 1489 |
| 36 | Calgary International Airport |  | CA | 1482 |
| 37 | Bengaluru International Airport |  | IN | 1470 |
| 38 | Oslo Gardermoen Airport |  | NO | 1458 |
| 39 | Vancouver International Airport |  | CA | 1452 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1393 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 966 | 21m | 244 km | 4,067.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 698 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 649 | 1h 6m | 770 km | 8,621.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 578 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 420 | 44m | 555 km | 4,021.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 392 | 44m | 241 km | 1,628.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 346 | 23m | 55 km | 328.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 322 | 19m | 99 km | 551.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 312 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 279 | 1h 50m | 1,304 km | 6,276.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SYS95 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-15 08:59 UTC | 2026-09-15 10:12 UTC | 1h 12m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-14 19:20 UTC | 2026-09-15 10:01 UTC | 14h 41m |
| CJT488 | CJT | Louisville Muhammad Ali International Airport (KSDF) | Toronto Pearson International Airport (CYYZ) | 2026-09-15 08:47 UTC | 2026-09-15 09:59 UTC | 1h 11m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-14 22:13 UTC | 2026-09-15 09:57 UTC | 11h 44m |
| CFL08 | CFL | Hood Airport (NZMS) | Wellington International Airport (NZWN) | 2026-09-15 09:24 UTC | 2026-09-15 09:52 UTC | 28m |
| SYS32 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-15 09:43 UTC | 2026-09-15 09:47 UTC | 4m |
| SWR1CA | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-09-15 08:45 UTC | 2026-09-15 09:38 UTC | 52m |
| DKYCK | DKY | EDJG (EDJG) | EDJG (EDJG) | 2026-09-15 09:27 UTC | 2026-09-15 09:36 UTC | 9m |
| IGO4EP | IndiGo | Chennai International Airport (VOMM) | Salem Airport (VOSM) | 2026-09-15 08:58 UTC | 2026-09-15 09:34 UTC | 35m |
| THS00031 | THS | Akinci Air Base (LTAE) | Akinci Air Base (LTAE) | 2026-09-15 09:06 UTC | 2026-09-15 09:29 UTC | 23m |
| RYR99PN | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Bihac Golubic Airport (LQBI) | 2026-09-15 08:54 UTC | 2026-09-15 09:28 UTC | 34m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-14 22:28 UTC | 2026-09-15 09:28 UTC | 10h 59m |
| WIF4DP | WIF | Bergen Airport Flesland (ENBR) | Stord Airport (ENSO) | 2026-09-15 09:13 UTC | 2026-09-15 09:27 UTC | 13m |
| CUCO317 | CUC | Gibraltar Airport (LXGB) | Gibraltar Airport (LXGB) | 2026-09-15 09:16 UTC | 2026-09-15 09:26 UTC | 10m |
| VLG7WT | Vueling | Asturias Airport (LEAS) | Son Bonet Airport (LESB) | 2026-09-15 08:00 UTC | 2026-09-15 09:26 UTC | 1h 26m |
| N5279F |  | William P Hobby Airport (KHOU) | KEYQ (KEYQ) | 2026-09-15 09:16 UTC | 2026-09-15 09:26 UTC | 9m |
| JL3555 |  | Fukuoka Airport (RJFF) | Izumo Airport (RJOC) | 2026-09-15 08:45 UTC | 2026-09-15 09:26 UTC | 40m |
| FIH40 | FIH | Hameenkyro Airport (EFHM) | Tampere-Pirkkala Airport (EFTP) | 2026-09-15 09:13 UTC | 2026-09-15 09:26 UTC | 12m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Bringeland Airport (ENBL) | 2026-09-15 09:07 UTC | 2026-09-15 09:25 UTC | 17m |
| RMB3 | RMB | Larnaca International Airport (LCLK) | Diagoras Airport (LGRP) | 2026-09-15 08:30 UTC | 2026-09-15 09:24 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
