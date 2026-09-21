# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_20:47:13_UTC-green)

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

**Latest saved flight:** 2026-09-21 20:47:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 20:47:13 UTC

- **265,773** saved flights
- **78,272** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,773** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,221,563.0 tonnes** estimated CO2 emissions
- **186,757,274 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10521 |
| 2 | SkyWest Airlines | 9249 |
| 3 | EJA | 5166 |
| 4 | IndiGo | 4463 |
| 5 | American Airlines | 4150 |
| 6 | Southwest Airlines | 3912 |
| 7 | Delta Air Lines | 3307 |
| 8 | ENY | 3129 |
| 9 | LATAM Airlines | 2560 |
| 10 | AZU | 2499 |
| 11 | Vueling | 2233 |
| 12 | WIF | 2150 |
| 13 | LXJ | 2089 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1788 |
| 16 | Swiss International | 1752 |
| 17 | QLK | 1716 |
| 18 | EJU | 1677 |
| 19 | AXM | 1664 |
| 20 | United Airlines | 1629 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1530 |
| 23 | PGT | 1494 |
| 24 | WMT | 1493 |
| 25 | GLO | 1480 |
| 26 | Air France | 1460 |
| 27 | VIV | 1453 |
| 28 | Wizz Air | 1446 |
| 29 | CXK | 1290 |
| 30 | AEE | 1284 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220910 |
| 2 | 🇪🇸 ES | 16714 |
| 3 | 🇧🇷 BR | 15543 |
| 4 | 🇦🇺 AU | 15208 |
| 5 | 🇨🇦 CA | 14801 |
| 6 | 🇮🇹 IT | 14468 |
| 7 | 🇮🇳 IN | 14109 |
| 8 | 🇩🇪 DE | 12806 |
| 9 | 🇬🇧 GB | 12336 |
| 10 | 🇨🇴 CO | 12111 |
| 11 | 🇫🇷 FR | 10612 |
| 12 | 🇯🇵 JP | 10244 |
| 13 | 🇹🇷 TR | 8046 |
| 14 | 🇬🇷 GR | 7700 |
| 15 | 🇲🇽 MX | 7321 |
| 16 | 🇨🇭 CH | 7087 |
| 17 | 🇳🇴 NO | 6568 |
| 18 | 🇹🇭 TH | 4768 |
| 19 | 🇲🇾 MY | 4487 |
| 20 | 🇿🇦 ZA | 4466 |
| 21 | 🇵🇱 PL | 4371 |
| 22 | 🇳🇿 NZ | 3689 |
| 23 | 🇵🇭 PH | 3529 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3030 |
| 26 | 🇰🇷 KR | 3008 |
| 27 | 🇲🇦 MA | 2656 |
| 28 | 🇲🇪 ME | 2491 |
| 29 | 🇳🇱 NL | 2379 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5420 |
| 2 | Denver International Airport |  | US | 4313 |
| 3 | Indira Gandhi International Airport |  | IN | 3191 |
| 4 | Tokyo International Airport |  | JP | 3062 |
| 5 | El Dorado International Airport |  | CO | 2845 |
| 6 | Harry Reid International Airport |  | US | 2838 |
| 7 | Guaymaral Airport |  | CO | 2792 |
| 8 | Zurich Airport |  | CH | 2762 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2668 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2564 |
| 12 | Salt Lake City International Airport |  | US | 2348 |
| 13 | Chicago O'Hare International Airport |  | US | 2282 |
| 14 | Congonhas Airport |  | BR | 2265 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2174 |
| 16 | Capua Airport |  | IT | 2083 |
| 17 | Madrid Barajas International Airport |  | ES | 2049 |
| 18 | Frankfurt am Main International Airport |  | DE | 2025 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2007 |
| 20 | Malpensa International Airport |  | IT | 1920 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1899 |
| 22 | Charles de Gaulle International Airport |  | FR | 1884 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1869 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1862 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1809 |
| 26 | Macau International Airport |  | MO | 1767 |
| 27 | Ninoy Aquino International Airport |  | PH | 1733 |
| 28 | Charlotte/Douglas International Airport |  | US | 1660 |
| 29 | Barcelona International Airport |  | ES | 1660 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1640 |
| 31 | Viracopos International Airport |  | BR | 1612 |
| 32 | Kuala Lumpur International Airport |  | MY | 1609 |
| 33 | Seattle-Tacoma International Airport |  | US | 1558 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1553 |
| 35 | Calgary International Airport |  | CA | 1517 |
| 36 | Don Mueang International Airport |  | TH | 1513 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1496 |
| 39 | Vancouver International Airport |  | CA | 1484 |
| 40 | Antalya International Airport |  | TR | 1422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1115 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 993 | 21m | 244 km | 4,181.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 735 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 667 | 1h 6m | 770 km | 8,860.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 661 | 24m | 225 km | 2,564.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 438 | 44m | 555 km | 4,194.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 405 | 44m | 241 km | 1,682.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 339 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 335 | 1h 6m | 706 km | 4,078.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 332 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 330 | 26m | 215 km | 1,222.2 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 309 | 19m | 144 km | 768.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 288 | 42m | 535 km | 2,659.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 288 | 1h 50m | 1,304 km | 6,479.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 276 | 18m | 14 km | 69.0 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100LE |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-21 20:29 UTC | 2026-09-21 20:47 UTC | 17m |
| CGPOV | CGP | Ottawa / Rockcliffe Airport (CYRO) | Ottawa / Gatineau Airport (CYND) | 2026-09-21 20:08 UTC | 2026-09-21 20:43 UTC | 35m |
| N424TF |  | Giffin Ranch Airport (3XS8) | David Wayne Hooks Memorial Airport (KDWH) | 2026-09-21 20:26 UTC | 2026-09-21 20:40 UTC | 13m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-09-21 06:10 UTC | 2026-09-21 20:37 UTC | 14h 27m |
| TALON77 | TAL | Boise Air Trml/Gowen Field (KBOI) | Boise Air Trml/Gowen Field (KBOI) | 2026-09-21 20:13 UTC | 2026-09-21 20:36 UTC | 22m |
| N19MX |  | K61B (K61B) | K61B (K61B) | 2026-09-21 19:56 UTC | 2026-09-21 20:33 UTC | 36m |
| CSN6042 | China Southern | Frankfurt am Main International Airport (EDDF) | Staroselye Airport (UUBK) | 2026-09-21 17:32 UTC | 2026-09-21 20:32 UTC | 3h 0m |
| CXK1141 | CXK | Soggy Bottom Airport (2TN8) | KM33 (KM33) | 2026-09-21 19:54 UTC | 2026-09-21 20:32 UTC | 37m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-21 06:02 UTC | 2026-09-21 20:31 UTC | 14h 29m |
| SNAP7 | SNA | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | Spring Valley (North) Airport (CKP2) | 2026-09-21 20:05 UTC | 2026-09-21 20:30 UTC | 24m |
| N410LR |  | TX09 (TX09) | New Braunfels Ntl Airport (KBAZ) | 2026-09-21 19:08 UTC | 2026-09-21 20:29 UTC | 1h 20m |
| SH067 |  | South Alabama Regional At Bill Benton Field (K79J) | South Alabama Regional At Bill Benton Field (K79J) | 2026-09-21 20:14 UTC | 2026-09-21 20:24 UTC | 10m |
| N465MM |  | Grand Junction Regional Airport (KGJT) | Westwinds Airport (KD17) | 2026-09-21 20:15 UTC | 2026-09-21 20:23 UTC | 7m |
| CPA044 | Cathay Pacific | Chhatrapati Shivaji International Airport (VABB) | Zhuhai Airport (ZGSD) | 2026-09-21 15:11 UTC | 2026-09-21 20:21 UTC | 5h 9m |
| EJA866 | EJA | Harry Reid International Airport (KLAS) | Rocky Mountain Metro Airport (KBJC) | 2026-09-21 19:02 UTC | 2026-09-21 20:19 UTC | 1h 17m |
| N531RF |  | Richmond International Airport (KRIC) | Richmond International Airport (KRIC) | 2026-09-21 19:42 UTC | 2026-09-21 20:16 UTC | 33m |
| N460AK |  | Centennial Airport (KAPA) | Mineta San Jose International Airport (KSJC) | 2026-09-21 18:07 UTC | 2026-09-21 20:14 UTC | 2h 6m |
| YEL87 | YEL | Frederick W Smith International/Memphis Airport (KMEM) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-09-21 18:35 UTC | 2026-09-21 20:14 UTC | 1h 38m |
| N264FA |  | Wings Field (KLOM) | Chester County G O Carlson Airport (KMQS) | 2026-09-21 19:54 UTC | 2026-09-21 20:13 UTC | 19m |
| EJA879 | EJA | John Wayne/Orange County Airport (KSNA) | Mineta San Jose International Airport (KSJC) | 2026-09-21 19:17 UTC | 2026-09-21 20:09 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
