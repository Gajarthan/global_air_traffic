# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_21:55:59_UTC-green)

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

**Latest saved flight:** 2026-09-27 21:55:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 21:55:59 UTC

- **271,321** saved flights
- **79,416** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **271,321** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,290,081.2 tonnes** estimated CO2 emissions
- **190,729,348 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10679 |
| 2 | SkyWest Airlines | 9446 |
| 3 | EJA | 5309 |
| 4 | IndiGo | 4537 |
| 5 | American Airlines | 4215 |
| 6 | Southwest Airlines | 3995 |
| 7 | Delta Air Lines | 3369 |
| 8 | ENY | 3186 |
| 9 | LATAM Airlines | 2609 |
| 10 | AZU | 2546 |
| 11 | Vueling | 2257 |
| 12 | WIF | 2205 |
| 13 | LXJ | 2140 |
| 14 | Lufthansa | 2058 |
| 15 | easyJet | 1814 |
| 16 | Swiss International | 1778 |
| 17 | QLK | 1744 |
| 18 | EJU | 1698 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1659 |
| 21 | Alaska Airlines | 1601 |
| 22 | All Nippon Airways | 1557 |
| 23 | PGT | 1531 |
| 24 | WMT | 1515 |
| 25 | GLO | 1514 |
| 26 | Air France | 1492 |
| 27 | VIV | 1483 |
| 28 | Wizz Air | 1473 |
| 29 | CXK | 1335 |
| 30 | AEE | 1298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226083 |
| 2 | 🇪🇸 ES | 16985 |
| 3 | 🇧🇷 BR | 15887 |
| 4 | 🇦🇺 AU | 15569 |
| 5 | 🇨🇦 CA | 15127 |
| 6 | 🇮🇹 IT | 14666 |
| 7 | 🇮🇳 IN | 14356 |
| 8 | 🇩🇪 DE | 13013 |
| 9 | 🇬🇧 GB | 12549 |
| 10 | 🇨🇴 CO | 12469 |
| 11 | 🇫🇷 FR | 10782 |
| 12 | 🇯🇵 JP | 10401 |
| 13 | 🇹🇷 TR | 8216 |
| 14 | 🇬🇷 GR | 7818 |
| 15 | 🇲🇽 MX | 7486 |
| 16 | 🇨🇭 CH | 7214 |
| 17 | 🇳🇴 NO | 6699 |
| 18 | 🇹🇭 TH | 4847 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4524 |
| 21 | 🇵🇱 PL | 4452 |
| 22 | 🇳🇿 NZ | 3806 |
| 23 | 🇵🇭 PH | 3587 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3093 |
| 26 | 🇰🇷 KR | 3060 |
| 27 | 🇲🇦 MA | 2691 |
| 28 | 🇲🇪 ME | 2547 |
| 29 | 🇳🇱 NL | 2439 |
| 30 | 🇮🇩 ID | 2258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5525 |
| 2 | Denver International Airport |  | US | 4420 |
| 3 | Indira Gandhi International Airport |  | IN | 3243 |
| 4 | Tokyo International Airport |  | JP | 3113 |
| 5 | El Dorado International Airport |  | CO | 2959 |
| 6 | Harry Reid International Airport |  | US | 2912 |
| 7 | Guaymaral Airport |  | CO | 2826 |
| 8 | Zurich Airport |  | CH | 2811 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2720 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2396 |
| 13 | Congonhas Airport |  | BR | 2313 |
| 14 | Chicago O'Hare International Airport |  | US | 2313 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2218 |
| 16 | Capua Airport |  | IT | 2096 |
| 17 | Madrid Barajas International Airport |  | ES | 2090 |
| 18 | Frankfurt am Main International Airport |  | DE | 2052 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2050 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1930 |
| 22 | Charles de Gaulle International Airport |  | FR | 1928 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1910 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1896 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1761 |
| 28 | Charlotte/Douglas International Airport |  | US | 1697 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1689 |
| 30 | Barcelona International Airport |  | ES | 1683 |
| 31 | Viracopos International Airport |  | BR | 1633 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1592 |
| 34 | Seattle-Tacoma International Airport |  | US | 1589 |
| 35 | Calgary International Airport |  | CA | 1545 |
| 36 | Don Mueang International Airport |  | TH | 1533 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1521 |
| 39 | Vancouver International Airport |  | CA | 1518 |
| 40 | Reno/Tahoe International Airport |  | US | 1450 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1017 | 21m | 244 km | 4,282.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 751 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 451 | 44m | 555 km | 4,318.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 436 | 27m | 275 km | 2,066.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 428 | 1h 50m | 1,423 km | 10,503.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 415 | 44m | 241 km | 1,723.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 346 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 315 | 19m | 144 km | 783.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 307 | 1h 14m | 961 km | 5,088.7 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 300 | 42m | 535 km | 2,770.7 t |
| 25 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 298 | 18m | 14 km | 74.5 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 293 | 1h 50m | 1,304 km | 6,591.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SCU12 | SCU | Farney Field (42KS) | Tulsa International Airport (KTUL) | 2026-09-27 20:48 UTC | 2026-09-27 21:55 UTC | 1h 7m |
| CXK198 | CXK | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-09-27 21:16 UTC | 2026-09-27 21:46 UTC | 30m |
| ERU894 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-09-27 21:30 UTC | 2026-09-27 21:42 UTC | 11m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-09-27 19:43 UTC | 2026-09-27 21:26 UTC | 1h 43m |
| N1920F |  | Sacramento Executive Airport (KSAC) | Sacramento Executive Airport (KSAC) | 2026-09-27 21:03 UTC | 2026-09-27 21:26 UTC | 22m |
| N71HR |  | Atlantic City International Airport (KACY) | Tampa International Airport (KTPA) | 2026-09-27 19:22 UTC | 2026-09-27 21:25 UTC | 2h 3m |
| IJA309 | IJA | Denver International Airport (KDEN) | Geary Ranch Airport (CO65) | 2026-09-27 20:51 UTC | 2026-09-27 21:24 UTC | 33m |
| QFA501 | Qantas | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-27 20:15 UTC | 2026-09-27 21:24 UTC | 1h 8m |
| N7806G |  | Peter Prince Field (K2R4) | George T Mc Cutchan Airport (8FL6) | 2026-09-27 20:32 UTC | 2026-09-27 21:24 UTC | 52m |
| N74ZC |  | Boeing Field/King County International Airport (KBFI) | MT88 (MT88) | 2026-09-27 20:40 UTC | 2026-09-27 21:23 UTC | 42m |
| N235SF |  | Washington Municipal Airport (KAWG) | Iowa City Municipal Airport (KIOW) | 2026-09-27 21:03 UTC | 2026-09-27 21:19 UTC | 16m |
| N850TS |  | Monterey Regional Airport (KMRY) | Emory Ranch Airport (0CA6) | 2026-09-27 19:51 UTC | 2026-09-27 21:15 UTC | 1h 24m |
| N4422R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-27 20:42 UTC | 2026-09-27 21:14 UTC | 31m |
| N261HB |  | City Of Colorado Springs Municipal Airport (KCOS) | Scenic Mesa Ranch Airport (CD02) | 2026-09-27 20:22 UTC | 2026-09-27 21:11 UTC | 48m |
| PSKMO | PSK | Fazenda Santa Rita de Cassia Airport (SWEZ) | Fazenda Agua Verde Airport (SWAV) | 2026-09-27 20:45 UTC | 2026-09-27 21:11 UTC | 26m |
| EJA841 | EJA | Mineta San Jose International Airport (KSJC) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-27 20:03 UTC | 2026-09-27 21:08 UTC | 1h 4m |
| XSN06 | XSN | Buchanan Field (KCCR) | Weed Airport (KO46) | 2026-09-27 20:17 UTC | 2026-09-27 21:07 UTC | 49m |
| SWA158 | Southwest Airlines | Mineta San Jose International Airport (KSJC) | K4SD (K4SD) | 2026-09-27 20:32 UTC | 2026-09-27 21:03 UTC | 30m |
| N277JJ |  | Washington Manassas/Harry P Davis Field (KHEF) | Robert F Swinnie Airport (KPHH) | 2026-09-27 19:46 UTC | 2026-09-27 21:03 UTC | 1h 16m |
| HK3966G |  | Guaymaral Airport (SKGY) | Tunja Airport (SKTJ) | 2026-09-27 20:28 UTC | 2026-09-27 21:02 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
