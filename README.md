# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_13:49:48_UTC-green)

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

**Latest saved flight:** 2026-08-26 13:49:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 13:49:48 UTC

- **238,593** saved flights
- **72,619** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,593** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,875,387.6 tonnes** estimated CO2 emissions
- **166,689,138 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9583 |
| 2 | SkyWest Airlines | 8391 |
| 3 | EJA | 4617 |
| 4 | IndiGo | 4024 |
| 5 | American Airlines | 3855 |
| 6 | Southwest Airlines | 3614 |
| 7 | Delta Air Lines | 3037 |
| 8 | ENY | 2882 |
| 9 | LATAM Airlines | 2292 |
| 10 | AZU | 2221 |
| 11 | Vueling | 2056 |
| 12 | Lufthansa | 1934 |
| 13 | WIF | 1896 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1665 |
| 16 | Swiss International | 1607 |
| 17 | AXM | 1591 |
| 18 | EJU | 1533 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1341 |
| 24 | GLO | 1331 |
| 25 | VIV | 1312 |
| 26 | PGT | 1303 |
| 27 | Air France | 1302 |
| 28 | Wizz Air | 1279 |
| 29 | AEE | 1184 |
| 30 | JetBlue | 1182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197580 |
| 2 | 🇪🇸 ES | 15358 |
| 3 | 🇧🇷 BR | 13920 |
| 4 | 🇦🇺 AU | 13571 |
| 5 | 🇨🇦 CA | 13184 |
| 6 | 🇮🇹 IT | 13054 |
| 7 | 🇮🇳 IN | 12539 |
| 8 | 🇩🇪 DE | 11806 |
| 9 | 🇬🇧 GB | 11275 |
| 10 | 🇨🇴 CO | 10154 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9610 |
| 13 | 🇹🇷 TR | 7092 |
| 14 | 🇬🇷 GR | 7033 |
| 15 | 🇲🇽 MX | 6605 |
| 16 | 🇨🇭 CH | 6406 |
| 17 | 🇳🇴 NO | 5914 |
| 18 | 🇹🇭 TH | 4333 |
| 19 | 🇲🇾 MY | 4263 |
| 20 | 🇿🇦 ZA | 4193 |
| 21 | 🇵🇱 PL | 3974 |
| 22 | 🇳🇿 NZ | 3291 |
| 23 | 🇵🇭 PH | 3289 |
| 24 | 🇬🇹 GT | 2990 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2762 |
| 27 | 🇲🇦 MA | 2412 |
| 28 | 🇲🇪 ME | 2231 |
| 29 | 🇳🇱 NL | 2160 |
| 30 | 🇮🇩 ID | 2101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4936 |
| 2 | Denver International Airport |  | US | 3853 |
| 3 | Indira Gandhi International Airport |  | IN | 2918 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2691 |
| 6 | Harry Reid International Airport |  | US | 2541 |
| 7 | Zurich Airport |  | CH | 2505 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2438 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2385 |
| 10 | El Dorado International Airport |  | CO | 2289 |
| 11 | La Aurora Airport |  | GT | 2280 |
| 12 | Chicago O'Hare International Airport |  | US | 2133 |
| 13 | Salt Lake City International Airport |  | US | 2095 |
| 14 | Congonhas Airport |  | BR | 2029 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1895 |
| 17 | Capua Airport |  | IT | 1879 |
| 18 | Madrid Barajas International Airport |  | ES | 1873 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1799 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1755 |
| 21 | Malpensa International Airport |  | IT | 1712 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1683 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1666 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1594 |
| 27 | Kuala Lumpur International Airport |  | MY | 1540 |
| 28 | Charlotte/Douglas International Airport |  | US | 1529 |
| 29 | Barcelona International Airport |  | ES | 1522 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1494 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1444 |
| 32 | Viracopos International Airport |  | BR | 1422 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1397 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1367 |
| 38 | Oslo Gardermoen Airport |  | NO | 1343 |
| 39 | O. R. Tambo International Airport |  | ZA | 1306 |
| 40 | Vancouver International Airport |  | CA | 1304 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 877 | 21m | 244 km | 3,692.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 604 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 537 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 394 | 27m | 275 km | 1,867.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 373 | 1h 50m | 1,423 km | 9,154.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 345 | 44m | 241 km | 1,433.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 341 | 21m | 250 km | 1,472.9 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 323 | 24m | 218 km | 1,216.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 270 | 19m | 144 km | 671.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 255 | 1h 50m | 1,304 km | 5,736.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N682SA |  | Treasure Coast International Airport (KFPR) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-08-26 12:32 UTC | 2026-08-26 13:49 UTC | 1h 17m |
| JEDI52 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bass Field (02AL) | 2026-08-26 12:49 UTC | 2026-08-26 13:49 UTC | 1h 0m |
| GKA264 | GKA | Laurinburg/Maxton Airport (KMEB) | Laurinburg/Maxton Airport (KMEB) | 2026-08-26 11:26 UTC | 2026-08-26 13:46 UTC | 2h 19m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-26 12:59 UTC | 2026-08-26 13:45 UTC | 45m |
| N80807 |  | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-08-26 12:48 UTC | 2026-08-26 13:42 UTC | 54m |
| N7565G |  | Portage County Airport (KPOV) | Portage County Airport (KPOV) | 2026-08-26 13:13 UTC | 2026-08-26 13:41 UTC | 28m |
| CXK111 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-26 13:20 UTC | 2026-08-26 13:41 UTC | 20m |
| N403EA |  | Henderson Executive Airport (KHND) | North Las Vegas Airport (KVGT) | 2026-08-26 12:51 UTC | 2026-08-26 13:35 UTC | 43m |
| MTU92 | MTU | Stonewall Airpark (41TN) | Stonewall Airpark (41TN) | 2026-08-26 13:31 UTC | 2026-08-26 13:32 UTC | 0m |
| N870SP |  | Stuart Powell Field (KDVK) | Stuart Powell Field (KDVK) | 2026-08-26 13:29 UTC | 2026-08-26 13:30 UTC | 0m |
| HBZVU | HBZ | Megeve Airport (LFHM) | Muenster Aero Airport (LSPU) | 2026-08-26 13:17 UTC | 2026-08-26 13:28 UTC | 11m |
| SMGLR32 | SMG | Kbely Air Base (LKKB) | Pardubice Airport (LKPD) | 2026-08-26 12:44 UTC | 2026-08-26 13:28 UTC | 43m |
| N1TR |  | Arlington Municipal Airport (KGKY) | Liberty Municipal Airport (KT78) | 2026-08-26 12:32 UTC | 2026-08-26 13:27 UTC | 55m |
| QTR816 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-26 06:02 UTC | 2026-08-26 13:26 UTC | 7h 23m |
| N4460L |  | Albert Whitted Airport (KSPG) | Lake Wales Municipal Airport (KX07) | 2026-08-26 12:23 UTC | 2026-08-26 13:26 UTC | 1h 3m |
| DEFER | DEF | Braunschweig Wolfsburg Airport (EDVE) | Braunschweig Wolfsburg Airport (EDVE) | 2026-08-26 13:11 UTC | 2026-08-26 13:25 UTC | 14m |
| N621TK |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-26 12:53 UTC | 2026-08-26 13:25 UTC | 31m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-26 12:42 UTC | 2026-08-26 13:24 UTC | 41m |
| N1359U |  | Virginia Tech/Montgomery Executive Airport (KBCB) | New River Valley Airport (KPSK) | 2026-08-26 13:07 UTC | 2026-08-26 13:22 UTC | 14m |
| NASHMI1 | NAS | Larnaca International Airport (LCLK) | Larnaca International Airport (LCLK) | 2026-08-26 13:18 UTC | 2026-08-26 13:21 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
