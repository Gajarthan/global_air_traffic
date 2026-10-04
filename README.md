# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_02:24:35_UTC-green)

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

**Latest saved flight:** 2026-10-04 02:24:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-04 02:24:35 UTC

- **275,892** saved flights
- **80,310** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,892** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,339,656.5 tonnes** estimated CO2 emissions
- **193,603,273 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10811 |
| 2 | SkyWest Airlines | 9604 |
| 3 | EJA | 5405 |
| 4 | IndiGo | 4597 |
| 5 | American Airlines | 4270 |
| 6 | Southwest Airlines | 4054 |
| 7 | Delta Air Lines | 3427 |
| 8 | ENY | 3225 |
| 9 | LATAM Airlines | 2672 |
| 10 | AZU | 2594 |
| 11 | Vueling | 2285 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2182 |
| 14 | Lufthansa | 2074 |
| 15 | easyJet | 1833 |
| 16 | Swiss International | 1805 |
| 17 | QLK | 1777 |
| 18 | EJU | 1714 |
| 19 | AXM | 1691 |
| 20 | United Airlines | 1682 |
| 21 | Alaska Airlines | 1629 |
| 22 | All Nippon Airways | 1575 |
| 23 | PGT | 1551 |
| 24 | GLO | 1540 |
| 25 | WMT | 1534 |
| 26 | VIV | 1512 |
| 27 | Air France | 1511 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1362 |
| 30 | AEE | 1311 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230258 |
| 2 | 🇪🇸 ES | 17247 |
| 3 | 🇧🇷 BR | 16198 |
| 4 | 🇦🇺 AU | 15910 |
| 5 | 🇨🇦 CA | 15376 |
| 6 | 🇮🇹 IT | 14860 |
| 7 | 🇮🇳 IN | 14545 |
| 8 | 🇩🇪 DE | 13178 |
| 9 | 🇨🇴 CO | 12814 |
| 10 | 🇬🇧 GB | 12700 |
| 11 | 🇫🇷 FR | 10898 |
| 12 | 🇯🇵 JP | 10513 |
| 13 | 🇹🇷 TR | 8331 |
| 14 | 🇬🇷 GR | 7910 |
| 15 | 🇲🇽 MX | 7621 |
| 16 | 🇨🇭 CH | 7325 |
| 17 | 🇳🇴 NO | 6800 |
| 18 | 🇹🇭 TH | 4946 |
| 19 | 🇲🇾 MY | 4581 |
| 20 | 🇿🇦 ZA | 4562 |
| 21 | 🇵🇱 PL | 4502 |
| 22 | 🇳🇿 NZ | 3917 |
| 23 | 🇵🇭 PH | 3641 |
| 24 | 🇬🇹 GT | 3462 |
| 25 | 🇭🇷 HR | 3137 |
| 26 | 🇰🇷 KR | 3105 |
| 27 | 🇲🇦 MA | 2722 |
| 28 | 🇲🇪 ME | 2588 |
| 29 | 🇳🇱 NL | 2462 |
| 30 | 🇮🇩 ID | 2280 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5597 |
| 2 | Denver International Airport |  | US | 4505 |
| 3 | Indira Gandhi International Airport |  | IN | 3286 |
| 4 | Tokyo International Airport |  | JP | 3154 |
| 5 | El Dorado International Airport |  | CO | 3065 |
| 6 | Harry Reid International Airport |  | US | 2973 |
| 7 | Zurich Airport |  | CH | 2865 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2756 |
| 10 | La Aurora Airport |  | GT | 2634 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2631 |
| 12 | Salt Lake City International Airport |  | US | 2454 |
| 13 | Congonhas Airport |  | BR | 2355 |
| 14 | Chicago O'Hare International Airport |  | US | 2328 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2258 |
| 16 | Capua Airport |  | IT | 2141 |
| 17 | Madrid Barajas International Airport |  | ES | 2124 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2106 |
| 19 | Frankfurt am Main International Airport |  | DE | 2072 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1958 |
| 22 | Malpensa International Airport |  | IT | 1949 |
| 23 | Charles de Gaulle International Airport |  | FR | 1949 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1840 |
| 26 | Macau International Airport |  | MO | 1796 |
| 27 | Ninoy Aquino International Airport |  | PH | 1791 |
| 28 | Charlotte/Douglas International Airport |  | US | 1722 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1714 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1652 |
| 32 | Kuala Lumpur International Airport |  | MY | 1643 |
| 33 | Seattle-Tacoma International Airport |  | US | 1624 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1622 |
| 35 | Calgary International Airport |  | CA | 1568 |
| 36 | Don Mueang International Airport |  | TH | 1559 |
| 37 | Vancouver International Airport |  | CA | 1547 |
| 38 | Oslo Gardermoen Airport |  | NO | 1546 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1497 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1042 | 21m | 244 km | 4,387.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 698 | 1h 6m | 770 km | 9,272.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 695 | 24m | 225 km | 2,696.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 436 | 1h 50m | 1,423 km | 10,700.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 354 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 347 | 1h 6m | 706 km | 4,224.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 321 | 19m | 144 km | 798.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 320 | 18m | 14 km | 80.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-10-04 01:43 UTC | 2026-10-04 02:24 UTC | 41m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-04 02:03 UTC | 2026-10-04 02:14 UTC | 10m |
| COOL14 | COO | Davis Monthan Afb Airport (KDMA) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-10-04 01:48 UTC | 2026-10-04 02:14 UTC | 26m |
| TAY401 | TAY | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-10-03 19:04 UTC | 2026-10-04 02:02 UTC | 6h 57m |
| ICL771 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-10-03 16:49 UTC | 2026-10-04 01:59 UTC | 9h 9m |
| UAL419 | United Airlines | San Francisco International Airport (KSFO) | Silver Creek Ranch Airport (41CA) | 2026-10-04 01:23 UTC | 2026-10-04 01:54 UTC | 31m |
| N505BB |  | San Antonio International Airport (KSAT) | Jicarilla Apache Nation Airport (K24N) | 2026-10-03 23:15 UTC | 2026-10-04 01:48 UTC | 2h 33m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-04 01:31 UTC | 2026-10-04 01:46 UTC | 14m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-10-04 01:27 UTC | 2026-10-04 01:43 UTC | 16m |
| COOL48 | COO | Davis Monthan Afb Airport (KDMA) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-10-04 01:17 UTC | 2026-10-04 01:43 UTC | 26m |
| SDE562 | SDE | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-10-04 00:30 UTC | 2026-10-04 01:40 UTC | 1h 10m |
| N960DT |  | Hollywood Burbank Airport (KBUR) | Centennial Airport (KAPA) | 2026-10-03 23:55 UTC | 2026-10-04 01:36 UTC | 1h 41m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Paihia Private Airport (NZPA) | 2026-10-04 01:03 UTC | 2026-10-04 01:31 UTC | 27m |
| RXA3472 | RXA | Melbourne International Airport (YMML) | Bombala Airport (YBOM) | 2026-10-04 00:36 UTC | 2026-10-04 01:29 UTC | 52m |
| SWA3456 | Southwest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 2026-10-04 00:13 UTC | 2026-10-04 01:29 UTC | 1h 15m |
| YOF | YOF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-10-04 00:50 UTC | 2026-10-04 01:28 UTC | 37m |
| N6268D |  | Olympia Regional Airport (KOLM) | Olympia Regional Airport (KOLM) | 2026-10-04 01:15 UTC | 2026-10-04 01:28 UTC | 12m |
| CPA660 | Cathay Pacific | Chhatrapati Shivaji International Airport (VABB) | Zhuhai Airport (ZGSD) | 2026-10-03 20:26 UTC | 2026-10-04 01:26 UTC | 5h 0m |
| N999PT |  | Oakland San Francisco Bay Airport (KOAK) | K4SD (K4SD) | 2026-10-04 00:50 UTC | 2026-10-04 01:26 UTC | 35m |
| JAL2731 | Japan Airlines | Okadama Airport (RJCO) | RJCS (RJCS) | 2026-10-04 00:53 UTC | 2026-10-04 01:25 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
