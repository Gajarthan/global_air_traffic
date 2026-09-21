# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_00:12:17_UTC-green)

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

**Latest saved flight:** 2026-09-21 00:12:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 00:12:17 UTC

- **265,178** saved flights
- **78,172** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,178** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,213,940.8 tonnes** estimated CO2 emissions
- **186,315,408 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10496 |
| 2 | SkyWest Airlines | 9228 |
| 3 | EJA | 5156 |
| 4 | IndiGo | 4449 |
| 5 | American Airlines | 4143 |
| 6 | Southwest Airlines | 3905 |
| 7 | Delta Air Lines | 3303 |
| 8 | ENY | 3125 |
| 9 | LATAM Airlines | 2557 |
| 10 | AZU | 2497 |
| 11 | Vueling | 2226 |
| 12 | WIF | 2142 |
| 13 | LXJ | 2082 |
| 14 | Lufthansa | 2037 |
| 15 | easyJet | 1785 |
| 16 | Swiss International | 1745 |
| 17 | QLK | 1711 |
| 18 | EJU | 1674 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1624 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1527 |
| 23 | WMT | 1489 |
| 24 | PGT | 1488 |
| 25 | GLO | 1478 |
| 26 | Air France | 1451 |
| 27 | VIV | 1449 |
| 28 | Wizz Air | 1440 |
| 29 | CXK | 1284 |
| 30 | AEE | 1282 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220460 |
| 2 | 🇪🇸 ES | 16680 |
| 3 | 🇧🇷 BR | 15526 |
| 4 | 🇦🇺 AU | 15172 |
| 5 | 🇨🇦 CA | 14764 |
| 6 | 🇮🇹 IT | 14450 |
| 7 | 🇮🇳 IN | 14075 |
| 8 | 🇩🇪 DE | 12784 |
| 9 | 🇬🇧 GB | 12290 |
| 10 | 🇨🇴 CO | 12062 |
| 11 | 🇫🇷 FR | 10579 |
| 12 | 🇯🇵 JP | 10230 |
| 13 | 🇹🇷 TR | 8027 |
| 14 | 🇬🇷 GR | 7680 |
| 15 | 🇲🇽 MX | 7297 |
| 16 | 🇨🇭 CH | 7066 |
| 17 | 🇳🇴 NO | 6549 |
| 18 | 🇹🇭 TH | 4750 |
| 19 | 🇲🇾 MY | 4480 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4364 |
| 22 | 🇳🇿 NZ | 3687 |
| 23 | 🇵🇭 PH | 3524 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3026 |
| 26 | 🇰🇷 KR | 3003 |
| 27 | 🇲🇦 MA | 2653 |
| 28 | 🇲🇪 ME | 2482 |
| 29 | 🇳🇱 NL | 2377 |
| 30 | 🇮🇩 ID | 2220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5411 |
| 2 | Denver International Airport |  | US | 4297 |
| 3 | Indira Gandhi International Airport |  | IN | 3184 |
| 4 | Tokyo International Airport |  | JP | 3057 |
| 5 | Harry Reid International Airport |  | US | 2831 |
| 6 | El Dorado International Airport |  | CO | 2829 |
| 7 | Guaymaral Airport |  | CO | 2788 |
| 8 | Zurich Airport |  | CH | 2754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2661 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2563 |
| 12 | Salt Lake City International Airport |  | US | 2343 |
| 13 | Chicago O'Hare International Airport |  | US | 2278 |
| 14 | Congonhas Airport |  | BR | 2262 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2171 |
| 16 | Capua Airport |  | IT | 2078 |
| 17 | Madrid Barajas International Airport |  | ES | 2046 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2004 |
| 20 | Malpensa International Airport |  | IT | 1918 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1897 |
| 22 | Charles de Gaulle International Airport |  | FR | 1872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1864 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1850 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1807 |
| 26 | Macau International Airport |  | MO | 1766 |
| 27 | Ninoy Aquino International Airport |  | PH | 1731 |
| 28 | Charlotte/Douglas International Airport |  | US | 1656 |
| 29 | Barcelona International Airport |  | ES | 1656 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1635 |
| 31 | Viracopos International Airport |  | BR | 1609 |
| 32 | Kuala Lumpur International Airport |  | MY | 1606 |
| 33 | Seattle-Tacoma International Airport |  | US | 1558 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1548 |
| 35 | Calgary International Airport |  | CA | 1515 |
| 36 | Don Mueang International Airport |  | TH | 1507 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1492 |
| 39 | Vancouver International Airport |  | CA | 1484 |
| 40 | Antalya International Airport |  | TR | 1421 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1114 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 991 | 21m | 244 km | 4,172.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 730 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 665 | 1h 6m | 770 km | 8,834.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 659 | 24m | 225 km | 2,556.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 432 | 44m | 555 km | 4,136.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 339 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 329 | 26m | 215 km | 1,218.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 329 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 308 | 19m | 144 km | 766.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 288 | 1h 50m | 1,304 km | 6,479.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 286 | 42m | 535 km | 2,641.4 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 271 | 18m | 14 km | 67.8 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-20 17:42 UTC | 2026-09-21 00:12 UTC | 6h 29m |
| N155U |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-09-20 23:12 UTC | 2026-09-21 00:06 UTC | 53m |
| EJM37 | EJM | Nashville International Airport (KBNA) | Reno/Tahoe International Airport (KRNO) | 2026-09-20 19:48 UTC | 2026-09-20 23:56 UTC | 4h 8m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-20 22:47 UTC | 2026-09-20 23:53 UTC | 1h 5m |
| PAG908T | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-09-20 21:48 UTC | 2026-09-20 23:51 UTC | 2h 3m |
| N699SC |  | William P Hobby Airport (KHOU) | Henderson Executive Airport (KHND) | 2026-09-20 21:12 UTC | 2026-09-20 23:49 UTC | 2h 37m |
| N888WK |  | Republic Airport (KFRG) | Winchell Mountain Airport (41NK) | 2026-09-20 23:05 UTC | 2026-09-20 23:42 UTC | 36m |
| WUP668 | WUP | Philadelphia International Airport (KPHL) | Lehigh Valley International Airport (KABE) | 2026-09-20 23:18 UTC | 2026-09-20 23:41 UTC | 23m |
| N5855W |  | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-09-20 22:14 UTC | 2026-09-20 23:37 UTC | 1h 23m |
| N539PE |  | Dekalb-Peachtree Airport (KPDK) | Godspeed Airpark (8MS2) | 2026-09-20 22:41 UTC | 2026-09-20 23:36 UTC | 55m |
| SJJ49 | SJJ | Spirit Of St Louis Airport (KSUS) | K36U (K36U) | 2026-09-20 21:09 UTC | 2026-09-20 23:36 UTC | 2h 27m |
| VAL791 | VAL | Buctouche Airport (CDT5) | Bathurst Airport (CZBF) | 2026-09-20 23:12 UTC | 2026-09-20 23:36 UTC | 23m |
| ENY4192 | ENY | Phoenix Sky Harbor International Airport (KPHX) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-20 23:10 UTC | 2026-09-20 23:33 UTC | 23m |
| N98AV |  | Houma-Terrebonne Airport (KHUM) | 0TE6 (0TE6) | 2026-09-20 22:01 UTC | 2026-09-20 23:32 UTC | 1h 31m |
| ENY3789 | ENY | Dallas-Fort Worth International Airport (KDFW) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-09-20 22:53 UTC | 2026-09-20 23:32 UTC | 39m |
| SKW4975 | SkyWest Airlines | Dallas-Fort Worth International Airport (KDFW) | Bruce Field (KE30) | 2026-09-20 23:04 UTC | 2026-09-20 23:32 UTC | 27m |
| N333EW |  | Mckinney Ntl Airport (KTKI) | Magee Airport (42TX) | 2026-09-20 23:14 UTC | 2026-09-20 23:31 UTC | 17m |
| N68767 |  | William R Fairchild International Airport (KCLM) | Jim & Julie's Airport (96WA) | 2026-09-20 22:26 UTC | 2026-09-20 23:29 UTC | 1h 2m |
| N414TW |  | A Bar A Ranch Airport (WY11) | Rocky Mountain Metro Airport (KBJC) | 2026-09-20 23:05 UTC | 2026-09-20 23:29 UTC | 24m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-20 23:15 UTC | 2026-09-20 23:28 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
