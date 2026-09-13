# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_21:29:59_UTC-green)

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

**Latest saved flight:** 2026-09-13 21:29:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 21:29:59 UTC

- **257,820** saved flights
- **76,716** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,820** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,120,029.8 tonnes** estimated CO2 emissions
- **180,871,295 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10249 |
| 2 | SkyWest Airlines | 8979 |
| 3 | EJA | 4997 |
| 4 | IndiGo | 4326 |
| 5 | American Airlines | 4074 |
| 6 | Southwest Airlines | 3791 |
| 7 | Delta Air Lines | 3225 |
| 8 | ENY | 3053 |
| 9 | LATAM Airlines | 2476 |
| 10 | AZU | 2410 |
| 11 | Vueling | 2183 |
| 12 | WIF | 2070 |
| 13 | Lufthansa | 2016 |
| 14 | LXJ | 2016 |
| 15 | easyJet | 1761 |
| 16 | Swiss International | 1724 |
| 17 | QLK | 1660 |
| 18 | AXM | 1646 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1595 |
| 21 | Alaska Airlines | 1529 |
| 22 | All Nippon Airways | 1497 |
| 23 | WMT | 1456 |
| 24 | GLO | 1436 |
| 25 | PGT | 1431 |
| 26 | Air France | 1409 |
| 27 | VIV | 1409 |
| 28 | Wizz Air | 1402 |
| 29 | JetBlue | 1248 |
| 30 | AEE | 1247 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214021 |
| 2 | 🇪🇸 ES | 16367 |
| 3 | 🇧🇷 BR | 15046 |
| 4 | 🇦🇺 AU | 14663 |
| 5 | 🇨🇦 CA | 14355 |
| 6 | 🇮🇹 IT | 14068 |
| 7 | 🇮🇳 IN | 13582 |
| 8 | 🇩🇪 DE | 12560 |
| 9 | 🇬🇧 GB | 12023 |
| 10 | 🇨🇴 CO | 11568 |
| 11 | 🇫🇷 FR | 10363 |
| 12 | 🇯🇵 JP | 10042 |
| 13 | 🇹🇷 TR | 7761 |
| 14 | 🇬🇷 GR | 7515 |
| 15 | 🇲🇽 MX | 7110 |
| 16 | 🇨🇭 CH | 6919 |
| 17 | 🇳🇴 NO | 6375 |
| 18 | 🇹🇭 TH | 4640 |
| 19 | 🇲🇾 MY | 4425 |
| 20 | 🇿🇦 ZA | 4388 |
| 21 | 🇵🇱 PL | 4273 |
| 22 | 🇳🇿 NZ | 3558 |
| 23 | 🇵🇭 PH | 3466 |
| 24 | 🇬🇹 GT | 3261 |
| 25 | 🇭🇷 HR | 2963 |
| 26 | 🇰🇷 KR | 2948 |
| 27 | 🇲🇦 MA | 2592 |
| 28 | 🇲🇪 ME | 2427 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5284 |
| 2 | Denver International Airport |  | US | 4169 |
| 3 | Indira Gandhi International Airport |  | IN | 3116 |
| 4 | Tokyo International Airport |  | JP | 2997 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2731 |
| 7 | Zurich Airport |  | CH | 2702 |
| 8 | El Dorado International Airport |  | CO | 2691 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2599 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2518 |
| 11 | La Aurora Airport |  | GT | 2477 |
| 12 | Salt Lake City International Airport |  | US | 2271 |
| 13 | Chicago O'Hare International Airport |  | US | 2243 |
| 14 | Congonhas Airport |  | BR | 2207 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2106 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2010 |
| 18 | Frankfurt am Main International Airport |  | DE | 1988 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1931 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1860 |
| 21 | Malpensa International Airport |  | IT | 1856 |
| 22 | Charles de Gaulle International Airport |  | FR | 1818 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1809 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1784 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1750 |
| 26 | Macau International Airport |  | MO | 1708 |
| 27 | Ninoy Aquino International Airport |  | PH | 1697 |
| 28 | Barcelona International Airport |  | ES | 1620 |
| 29 | Charlotte/Douglas International Airport |  | US | 1613 |
| 30 | Kuala Lumpur International Airport |  | MY | 1592 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1581 |
| 32 | Viracopos International Airport |  | BR | 1550 |
| 33 | Seattle-Tacoma International Airport |  | US | 1511 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1505 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1476 |
| 37 | Bengaluru International Airport |  | IN | 1463 |
| 38 | Oslo Gardermoen Airport |  | NO | 1455 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 695 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 390 | 44m | 241 km | 1,620.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 361 | 24m | 218 km | 1,360.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 319 | 26m | 215 km | 1,181.4 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 312 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 308 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FXC66 | FXC | John F Kennedy International Airport (KJFK) | Teterboro Airport (KTEB) | 2026-09-13 21:17 UTC | 2026-09-13 21:29 UTC | 12m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-13 20:26 UTC | 2026-09-13 21:26 UTC | 1h 0m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-09-13 17:48 UTC | 2026-09-13 21:25 UTC | 3h 37m |
| N6382D |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-09-13 19:50 UTC | 2026-09-13 21:20 UTC | 1h 29m |
| CES214 | China Eastern | London Gatwick Airport (EGKK) | Ukhta Airport (UUYH) | 2026-09-13 17:23 UTC | 2026-09-13 21:17 UTC | 3h 54m |
| N646CB |  | Long Beach (Daugherty Field) Airport (KLGB) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-13 20:30 UTC | 2026-09-13 21:11 UTC | 41m |
| BRG570 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-09-13 20:36 UTC | 2026-09-13 21:07 UTC | 31m |
| N400PV |  | Colonel James Jabara Airport (KAAO) | 14TE (14TE) | 2026-09-13 20:01 UTC | 2026-09-13 21:07 UTC | 1h 5m |
| ETD206 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 18:46 UTC | 2026-09-13 21:06 UTC | 2h 20m |
| N562DB |  | Falcon Field (KFFZ) | Monte Prieto Ranch Airport (57NM) | 2026-09-13 20:15 UTC | 2026-09-13 21:03 UTC | 48m |
| N6539H |  | Hayward Executive Airport (KHWD) | Sacramento Mather Airport (KMHR) | 2026-09-13 20:12 UTC | 2026-09-13 21:01 UTC | 48m |
| N707KA |  | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-09-13 20:18 UTC | 2026-09-13 20:59 UTC | 41m |
| AHY064 | AHY | Berlin Brandenburg Airport (EDDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 09:34 UTC | 2026-09-13 20:58 UTC | 11h 23m |
| SLH818 | SLH | Napa County Airport (KAPC) | Antelope County Airport (K4V9) | 2026-09-13 18:16 UTC | 2026-09-13 20:58 UTC | 2h 41m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-09-13 20:24 UTC | 2026-09-13 20:56 UTC | 31m |
| N248PA |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-09-13 20:44 UTC | 2026-09-13 20:53 UTC | 9m |
| AAE117 | AAE | Budapest Ferenc Liszt International Airport (LHBP) | Zhuhai Airport (ZGSD) | 2026-09-13 10:37 UTC | 2026-09-13 20:53 UTC | 10h 15m |
| JCM615 | JCM | St Louis Downtown Airport (KCPS) | San Luis Valley Regional/Bergman Field (KALS) | 2026-09-13 19:01 UTC | 2026-09-13 20:53 UTC | 1h 52m |
| ABY526 | ABY | Sharjah International Airport (OMSJ) | Fujairah International Airport (OMFJ) | 2026-09-13 20:42 UTC | 2026-09-13 20:53 UTC | 10m |
| N971MT |  | Greenville Downtown Airport (KGMU) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-13 20:20 UTC | 2026-09-13 20:51 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
