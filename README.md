# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_00:25:32_UTC-green)

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

**Latest saved flight:** 2026-08-31 00:25:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-31 00:25:32 UTC

- **242,430** saved flights
- **73,465** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **242,430** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,918,152.1 tonnes** estimated CO2 emissions
- **169,168,235 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9723 |
| 2 | SkyWest Airlines | 8507 |
| 3 | EJA | 4694 |
| 4 | IndiGo | 4076 |
| 5 | American Airlines | 3903 |
| 6 | Southwest Airlines | 3643 |
| 7 | Delta Air Lines | 3093 |
| 8 | ENY | 2924 |
| 9 | LATAM Airlines | 2322 |
| 10 | AZU | 2247 |
| 11 | Vueling | 2081 |
| 12 | Lufthansa | 1948 |
| 13 | WIF | 1921 |
| 14 | LXJ | 1878 |
| 15 | easyJet | 1690 |
| 16 | Swiss International | 1636 |
| 17 | AXM | 1599 |
| 18 | EJU | 1550 |
| 19 | QLK | 1550 |
| 20 | United Airlines | 1525 |
| 21 | Alaska Airlines | 1450 |
| 22 | All Nippon Airways | 1434 |
| 23 | WMT | 1364 |
| 24 | GLO | 1352 |
| 25 | VIV | 1330 |
| 26 | PGT | 1326 |
| 27 | Air France | 1323 |
| 28 | Wizz Air | 1311 |
| 29 | AEE | 1199 |
| 30 | JetBlue | 1197 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200950 |
| 2 | 🇪🇸 ES | 15582 |
| 3 | 🇧🇷 BR | 14111 |
| 4 | 🇦🇺 AU | 13755 |
| 5 | 🇨🇦 CA | 13490 |
| 6 | 🇮🇹 IT | 13269 |
| 7 | 🇮🇳 IN | 12691 |
| 8 | 🇩🇪 DE | 11956 |
| 9 | 🇬🇧 GB | 11439 |
| 10 | 🇨🇴 CO | 10466 |
| 11 | 🇫🇷 FR | 9763 |
| 12 | 🇯🇵 JP | 9712 |
| 13 | 🇹🇷 TR | 7191 |
| 14 | 🇬🇷 GR | 7145 |
| 15 | 🇲🇽 MX | 6692 |
| 16 | 🇨🇭 CH | 6514 |
| 17 | 🇳🇴 NO | 5988 |
| 18 | 🇹🇭 TH | 4390 |
| 19 | 🇲🇾 MY | 4286 |
| 20 | 🇿🇦 ZA | 4225 |
| 21 | 🇵🇱 PL | 4070 |
| 22 | 🇳🇿 NZ | 3336 |
| 23 | 🇵🇭 PH | 3321 |
| 24 | 🇬🇹 GT | 3050 |
| 25 | 🇰🇷 KR | 2859 |
| 26 | 🇭🇷 HR | 2797 |
| 27 | 🇲🇦 MA | 2457 |
| 28 | 🇲🇪 ME | 2264 |
| 29 | 🇳🇱 NL | 2192 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5011 |
| 2 | Denver International Airport |  | US | 3908 |
| 3 | Indira Gandhi International Airport |  | IN | 2957 |
| 4 | Tokyo International Airport |  | JP | 2892 |
| 5 | Guaymaral Airport |  | CO | 2705 |
| 6 | Harry Reid International Airport |  | US | 2574 |
| 7 | Zurich Airport |  | CH | 2548 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2480 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2415 |
| 10 | El Dorado International Airport |  | CO | 2372 |
| 11 | La Aurora Airport |  | GT | 2322 |
| 12 | Chicago O'Hare International Airport |  | US | 2149 |
| 13 | Salt Lake City International Airport |  | US | 2142 |
| 14 | Congonhas Airport |  | BR | 2066 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2009 |
| 16 | Frankfurt am Main International Airport |  | DE | 1918 |
| 17 | Capua Airport |  | IT | 1911 |
| 18 | Madrid Barajas International Airport |  | ES | 1905 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1818 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1784 |
| 21 | Malpensa International Airport |  | IT | 1734 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1711 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1701 |
| 24 | Charles de Gaulle International Airport |  | FR | 1695 |
| 25 | Macau International Airport |  | MO | 1617 |
| 26 | Ninoy Aquino International Airport |  | PH | 1614 |
| 27 | Charlotte/Douglas International Airport |  | US | 1551 |
| 28 | Enrique Olaya Herrera Airport |  | CO | 1549 |
| 29 | Kuala Lumpur International Airport |  | MY | 1546 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1466 |
| 32 | Viracopos International Airport |  | BR | 1437 |
| 33 | Seattle-Tacoma International Airport |  | US | 1422 |
| 34 | Don Mueang International Airport |  | TH | 1413 |
| 35 | Bengaluru International Airport |  | IN | 1408 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1407 |
| 37 | Calgary International Airport |  | CA | 1392 |
| 38 | Oslo Gardermoen Airport |  | NO | 1364 |
| 39 | Vancouver International Airport |  | CA | 1346 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1096 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 894 | 21m | 244 km | 3,764.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 625 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 615 | 24m | 225 km | 2,385.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 370 | 44m | 555 km | 3,542.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 332 | 24m | 218 km | 1,250.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 301 | 19m | 99 km | 515.6 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 295 | 26m | 215 km | 1,092.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 286 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 280 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 278 | 1h 14m | 961 km | 4,608.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 274 | 19m | 144 km | 681.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 261 | 1h 50m | 1,304 km | 5,871.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL2307 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Humann Private Airstrip (ND85) | 2026-08-30 23:33 UTC | 2026-08-31 00:25 UTC | 52m |
| NIJ | NIJ | Bendigo Airport (YBDG) | Melbourne Essendon Airport (YMEN) | 2026-08-30 23:42 UTC | 2026-08-31 00:23 UTC | 41m |
| OUC | OUC | Snowtown Airport (YSNT) | YCVA (YCVA) | 2026-08-30 23:53 UTC | 2026-08-31 00:23 UTC | 29m |
| GPD293 | GPD | Martha's Vineyard Airport (KMVY) | Teterboro Airport (KTEB) | 2026-08-30 23:34 UTC | 2026-08-31 00:22 UTC | 48m |
| UPS5982 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Boeing Field/King County International Airport (KBFI) | 2026-08-30 20:12 UTC | 2026-08-31 00:20 UTC | 4h 8m |
| MNL5 | MNL | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-08-30 23:31 UTC | 2026-08-31 00:09 UTC | 37m |
| N900AA |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-30 23:19 UTC | 2026-08-31 00:09 UTC | 49m |
| PSG | PSG | Heck Field Airport (YHEC) | Brisbane Archerfield Airport (YBAF) | 2026-08-30 23:53 UTC | 2026-08-31 00:08 UTC | 14m |
| BT617 |  | San Clemente Island Nalf Airport (KNUC) | San Nicolas Island Nolf Airport (KNSI) | 2026-08-30 23:46 UTC | 2026-08-31 00:06 UTC | 19m |
| TKR168 | TKR | UT80 (UT80) | Colorado City Municipal Airport (KAZC) | 2026-08-30 22:50 UTC | 2026-08-31 00:01 UTC | 1h 10m |
| USC240 | USC | Portland International Airport (KPDX) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-30 22:42 UTC | 2026-08-31 00:00 UTC | 1h 18m |
| TAM3074 | LATAM Airlines | Congonhas Airport (SBSP) | Congonhas Airport (SBSP) | 2026-08-30 23:14 UTC | 2026-08-30 23:59 UTC | 45m |
| N329TA |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-30 23:13 UTC | 2026-08-30 23:59 UTC | 46m |
| N399W |  | Sheboygan County Memorial International Airport (KSBM) | Miller-Herrold Airport (28MI) | 2026-08-30 23:39 UTC | 2026-08-30 23:58 UTC | 18m |
| CGPCL | CGP | Vancouver International Airport (CYVR) | Midway Airport (CBM6) | 2026-08-30 23:17 UTC | 2026-08-30 23:58 UTC | 40m |
| TKR12 | TKR | Citabriair Airport (UT43) | Colorado City Municipal Airport (KAZC) | 2026-08-30 23:47 UTC | 2026-08-30 23:57 UTC | 10m |
| N308SB |  | San Bernardino International Airport (KSBD) | Banning Municipal Airport (KBNG) | 2026-08-30 23:34 UTC | 2026-08-30 23:56 UTC | 22m |
|  |  | Mount Hotham Airport (YHOT) | Mount Hotham Airport (YHOT) | 2026-08-30 23:50 UTC | 2026-08-30 23:52 UTC | 1m |
| SH461 |  | Port Augusta Airport (YPAG) | Wirrealpa Airport (YWPA) | 2026-08-30 23:22 UTC | 2026-08-30 23:52 UTC | 29m |
| SKW6318 | SkyWest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Montrose Regional Airport (KMTJ) | 2026-08-30 22:59 UTC | 2026-08-30 23:51 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
