# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_22:23:20_UTC-green)

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

**Latest saved flight:** 2026-09-14 22:23:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-14 22:23:20 UTC

- **258,763** saved flights
- **76,898** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **258,763** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,133,317.0 tonnes** estimated CO2 emissions
- **181,641,563 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10263 |
| 2 | SkyWest Airlines | 9017 |
| 3 | EJA | 5023 |
| 4 | IndiGo | 4340 |
| 5 | American Airlines | 4086 |
| 6 | Southwest Airlines | 3806 |
| 7 | Delta Air Lines | 3236 |
| 8 | ENY | 3068 |
| 9 | LATAM Airlines | 2489 |
| 10 | AZU | 2426 |
| 11 | Vueling | 2189 |
| 12 | WIF | 2076 |
| 13 | LXJ | 2024 |
| 14 | Lufthansa | 2018 |
| 15 | easyJet | 1763 |
| 16 | Swiss International | 1727 |
| 17 | QLK | 1667 |
| 18 | AXM | 1647 |
| 19 | EJU | 1641 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1536 |
| 22 | All Nippon Airways | 1498 |
| 23 | WMT | 1462 |
| 24 | GLO | 1442 |
| 25 | PGT | 1437 |
| 26 | VIV | 1416 |
| 27 | Air France | 1414 |
| 28 | Wizz Air | 1409 |
| 29 | AEE | 1250 |
| 30 | JetBlue | 1250 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214856 |
| 2 | 🇪🇸 ES | 16404 |
| 3 | 🇧🇷 BR | 15126 |
| 4 | 🇦🇺 AU | 14738 |
| 5 | 🇨🇦 CA | 14405 |
| 6 | 🇮🇹 IT | 14097 |
| 7 | 🇮🇳 IN | 13643 |
| 8 | 🇩🇪 DE | 12584 |
| 9 | 🇬🇧 GB | 12057 |
| 10 | 🇨🇴 CO | 11629 |
| 11 | 🇫🇷 FR | 10394 |
| 12 | 🇯🇵 JP | 10068 |
| 13 | 🇹🇷 TR | 7798 |
| 14 | 🇬🇷 GR | 7532 |
| 15 | 🇲🇽 MX | 7133 |
| 16 | 🇨🇭 CH | 6941 |
| 17 | 🇳🇴 NO | 6389 |
| 18 | 🇹🇭 TH | 4647 |
| 19 | 🇲🇾 MY | 4433 |
| 20 | 🇿🇦 ZA | 4392 |
| 21 | 🇵🇱 PL | 4283 |
| 22 | 🇳🇿 NZ | 3573 |
| 23 | 🇵🇭 PH | 3475 |
| 24 | 🇬🇹 GT | 3270 |
| 25 | 🇭🇷 HR | 2967 |
| 26 | 🇰🇷 KR | 2955 |
| 27 | 🇲🇦 MA | 2597 |
| 28 | 🇲🇪 ME | 2436 |
| 29 | 🇳🇱 NL | 2323 |
| 30 | 🇮🇩 ID | 2193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5307 |
| 2 | Denver International Airport |  | US | 4182 |
| 3 | Indira Gandhi International Airport |  | IN | 3125 |
| 4 | Tokyo International Airport |  | JP | 3003 |
| 5 | Guaymaral Airport |  | CO | 2767 |
| 6 | Harry Reid International Airport |  | US | 2747 |
| 7 | Zurich Airport |  | CH | 2713 |
| 8 | El Dorado International Airport |  | CO | 2709 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2608 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2523 |
| 11 | La Aurora Airport |  | GT | 2484 |
| 12 | Salt Lake City International Airport |  | US | 2281 |
| 13 | Chicago O'Hare International Airport |  | US | 2249 |
| 14 | Congonhas Airport |  | BR | 2215 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2116 |
| 16 | Capua Airport |  | IT | 2025 |
| 17 | Madrid Barajas International Airport |  | ES | 2013 |
| 18 | Frankfurt am Main International Airport |  | DE | 1992 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1947 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1866 |
| 21 | Malpensa International Airport |  | IT | 1862 |
| 22 | Charles de Gaulle International Airport |  | FR | 1822 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1819 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1788 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1760 |
| 26 | Macau International Airport |  | MO | 1712 |
| 27 | Ninoy Aquino International Airport |  | PH | 1703 |
| 28 | Barcelona International Airport |  | ES | 1623 |
| 29 | Charlotte/Douglas International Airport |  | US | 1620 |
| 30 | Kuala Lumpur International Airport |  | MY | 1595 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1588 |
| 32 | Viracopos International Airport |  | BR | 1563 |
| 33 | Seattle-Tacoma International Airport |  | US | 1520 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1508 |
| 35 | Don Mueang International Airport |  | TH | 1486 |
| 36 | Calgary International Airport |  | CA | 1482 |
| 37 | Bengaluru International Airport |  | IN | 1469 |
| 38 | Oslo Gardermoen Airport |  | NO | 1458 |
| 39 | Vancouver International Airport |  | CA | 1451 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 965 | 21m | 244 km | 4,063.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 698 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 648 | 1h 6m | 770 km | 8,608.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 646 | 24m | 225 km | 2,506.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 578 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 419 | 27m | 275 km | 1,985.5 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 419 | 44m | 555 km | 4,012.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 392 | 44m | 241 km | 1,628.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 364 | 24m | 218 km | 1,371.3 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 344 | 23m | 55 km | 327.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 322 | 19m | 99 km | 551.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 316 | 12m | - | - |
| 20 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 310 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 298 | 1h 14m | 961 km | 4,939.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 278 | 1h 50m | 1,304 km | 6,254.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 274 | 42m | 535 km | 2,530.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N505U |  | Waco Regional Airport (KACT) | Clifton Municipal/Isenhower Field (K7F7) | 2026-09-14 21:52 UTC | 2026-09-14 22:23 UTC | 31m |
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-14 14:51 UTC | 2026-09-14 22:19 UTC | 7h 27m |
| BDA481 | BDA | Indira Gandhi International Airport (VIDP) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-14 18:44 UTC | 2026-09-14 22:16 UTC | 3h 31m |
| BTZ603 | BTZ | South Lafourche Leonard Miller Jr Airport (KGAO) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-14 22:00 UTC | 2026-09-14 22:14 UTC | 13m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Zhuhai Airport (ZGSD) | 2026-09-14 11:59 UTC | 2026-09-14 22:13 UTC | 10h 13m |
| N1653F |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-14 22:01 UTC | 2026-09-14 22:13 UTC | 11m |
| WLFPK12 | WLF | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-09-14 21:41 UTC | 2026-09-14 22:10 UTC | 29m |
| TOGO22 | TOG | Allen Army Air Field (PABI) | Elmendorf Afb Airport (PAED) | 2026-09-14 21:04 UTC | 2026-09-14 22:09 UTC | 1h 5m |
| HANG51 | HAN | Enix Airport (OK51) | Enix Airport (OK51) | 2026-09-14 21:32 UTC | 2026-09-14 22:08 UTC | 35m |
| N6533W |  | Modesto City-County-Harry Sham Field (KMOD) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-14 21:42 UTC | 2026-09-14 22:07 UTC | 25m |
| N15760 |  | Chester Airport (KSNC) | Newport State Airport (KUUU) | 2026-09-14 21:30 UTC | 2026-09-14 22:04 UTC | 34m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Zhuhai Airport (ZGSD) | 2026-09-14 11:15 UTC | 2026-09-14 22:04 UTC | 10h 48m |
| N441EE |  | Joplin Regional Airport (KJLN) | Kansas City/Lee's Summit Regional Airport (KLXT) | 2026-09-14 21:35 UTC | 2026-09-14 22:01 UTC | 26m |
| N906MD |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-09-14 21:23 UTC | 2026-09-14 22:00 UTC | 37m |
| N956LA |  | Compton/Woodley Airport (KCPM) | Brackett Field (KPOC) | 2026-09-14 21:21 UTC | 2026-09-14 21:59 UTC | 37m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-09-14 10:19 UTC | 2026-09-14 21:58 UTC | 11h 38m |
| CFMPA | CFM | Prince George Airport (CYXS) | Terrace Airport (CYXT) | 2026-09-14 20:51 UTC | 2026-09-14 21:57 UTC | 1h 6m |
| N716AT |  | Red Dog Airport (PADG) | Robert/Bob/Curtis Memorial Airport (PFNO) | 2026-09-14 21:24 UTC | 2026-09-14 21:57 UTC | 33m |
| N70200 |  | Talaheim Airport (1AK8) | Wasilla Airport (PAWS) | 2026-09-14 21:22 UTC | 2026-09-14 21:55 UTC | 32m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-14 11:07 UTC | 2026-09-14 21:54 UTC | 10h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
