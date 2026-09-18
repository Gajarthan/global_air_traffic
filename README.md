# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_22:24:19_UTC-green)

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

**Latest saved flight:** 2026-09-18 22:24:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 22:24:19 UTC

- **262,925** saved flights
- **77,736** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,925** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,185,055.0 tonnes** estimated CO2 emissions
- **184,640,868 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10405 |
| 2 | SkyWest Airlines | 9151 |
| 3 | EJA | 5100 |
| 4 | IndiGo | 4416 |
| 5 | American Airlines | 4125 |
| 6 | Southwest Airlines | 3859 |
| 7 | Delta Air Lines | 3284 |
| 8 | ENY | 3100 |
| 9 | LATAM Airlines | 2530 |
| 10 | AZU | 2470 |
| 11 | Vueling | 2212 |
| 12 | WIF | 2125 |
| 13 | LXJ | 2061 |
| 14 | Lufthansa | 2030 |
| 15 | easyJet | 1777 |
| 16 | Swiss International | 1736 |
| 17 | QLK | 1699 |
| 18 | EJU | 1656 |
| 19 | AXM | 1655 |
| 20 | United Airlines | 1610 |
| 21 | Alaska Airlines | 1558 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1479 |
| 24 | PGT | 1475 |
| 25 | GLO | 1469 |
| 26 | Air France | 1441 |
| 27 | VIV | 1437 |
| 28 | Wizz Air | 1428 |
| 29 | TKR | 1275 |
| 30 | CXK | 1274 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218489 |
| 2 | 🇪🇸 ES | 16584 |
| 3 | 🇧🇷 BR | 15383 |
| 4 | 🇦🇺 AU | 15079 |
| 5 | 🇨🇦 CA | 14642 |
| 6 | 🇮🇹 IT | 14287 |
| 7 | 🇮🇳 IN | 13950 |
| 8 | 🇩🇪 DE | 12707 |
| 9 | 🇬🇧 GB | 12215 |
| 10 | 🇨🇴 CO | 11905 |
| 11 | 🇫🇷 FR | 10511 |
| 12 | 🇯🇵 JP | 10179 |
| 13 | 🇹🇷 TR | 7956 |
| 14 | 🇬🇷 GR | 7628 |
| 15 | 🇲🇽 MX | 7235 |
| 16 | 🇨🇭 CH | 7016 |
| 17 | 🇳🇴 NO | 6500 |
| 18 | 🇹🇭 TH | 4707 |
| 19 | 🇲🇾 MY | 4463 |
| 20 | 🇿🇦 ZA | 4432 |
| 21 | 🇵🇱 PL | 4334 |
| 22 | 🇳🇿 NZ | 3643 |
| 23 | 🇵🇭 PH | 3500 |
| 24 | 🇬🇹 GT | 3351 |
| 25 | 🇭🇷 HR | 3000 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2631 |
| 28 | 🇲🇪 ME | 2467 |
| 29 | 🇳🇱 NL | 2347 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5376 |
| 2 | Denver International Airport |  | US | 4251 |
| 3 | Indira Gandhi International Airport |  | IN | 3157 |
| 4 | Tokyo International Airport |  | JP | 3038 |
| 5 | Harry Reid International Airport |  | US | 2796 |
| 6 | El Dorado International Airport |  | CO | 2782 |
| 7 | Guaymaral Airport |  | CO | 2779 |
| 8 | Zurich Airport |  | CH | 2738 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2644 |
| 10 | La Aurora Airport |  | GT | 2547 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2547 |
| 12 | Salt Lake City International Airport |  | US | 2323 |
| 13 | Chicago O'Hare International Airport |  | US | 2264 |
| 14 | Congonhas Airport |  | BR | 2246 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2149 |
| 16 | Capua Airport |  | IT | 2052 |
| 17 | Madrid Barajas International Airport |  | ES | 2033 |
| 18 | Frankfurt am Main International Airport |  | DE | 2004 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1981 |
| 20 | Malpensa International Airport |  | IT | 1889 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1885 |
| 22 | Charles de Gaulle International Airport |  | FR | 1859 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1820 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1798 |
| 26 | Macau International Airport |  | MO | 1746 |
| 27 | Ninoy Aquino International Airport |  | PH | 1717 |
| 28 | Barcelona International Airport |  | ES | 1643 |
| 29 | Charlotte/Douglas International Airport |  | US | 1640 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1617 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1595 |
| 33 | Seattle-Tacoma International Airport |  | US | 1544 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1531 |
| 35 | Calgary International Airport |  | CA | 1499 |
| 36 | Don Mueang International Airport |  | TH | 1498 |
| 37 | Bengaluru International Airport |  | IN | 1493 |
| 38 | Oslo Gardermoen Airport |  | NO | 1481 |
| 39 | Vancouver International Airport |  | CA | 1471 |
| 40 | Antalya International Airport |  | TR | 1406 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 981 | 21m | 244 km | 4,130.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 720 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 426 | 44m | 555 km | 4,079.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 371 | 24m | 218 km | 1,397.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 360 | 21m | 250 km | 1,555.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 329 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 280 | 42m | 535 km | 2,586.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 280 | 28m | 152 km | 731.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N38BL |  | John F Kennedy International Airport (KJFK) | Teterboro Airport (KTEB) | 2026-09-18 22:14 UTC | 2026-09-18 22:24 UTC | 10m |
| N564LM |  | Addison Airport (KADS) | Addison Airport (KADS) | 2026-09-18 21:01 UTC | 2026-09-18 22:17 UTC | 1h 16m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-09-18 07:07 UTC | 2026-09-18 22:16 UTC | 15h 8m |
| IJA309 | IJA | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-09-18 21:14 UTC | 2026-09-18 22:16 UTC | 1h 1m |
| N893AP |  | General Edward Lawrence Logan International Airport (KBOS) | Laguardia Airport (KLGA) | 2026-09-18 20:59 UTC | 2026-09-18 22:13 UTC | 1h 14m |
| ACA713 | Air Canada | Laguardia Airport (KLGA) | Toronto Pearson International Airport (CYYZ) | 2026-09-18 21:07 UTC | 2026-09-18 22:10 UTC | 1h 2m |
| N4525B |  | Bob Maxwell Memorial Airfield (KOKB) | French Valley Airport (KF70) | 2026-09-18 21:50 UTC | 2026-09-18 22:07 UTC | 16m |
| N32AZ |  | Pratermill Flight Park Airport (GA72) | Flying G Ranch Airport (86GA) | 2026-09-18 21:47 UTC | 2026-09-18 22:05 UTC | 17m |
| N9838V |  | Mckinney Ntl Airport (KTKI) | Card Aerodrome (0TX9) | 2026-09-18 21:35 UTC | 2026-09-18 22:00 UTC | 24m |
| CUL558 | CUL | Lee Vining Airport (KO24) | 6CL4 (6CL4) | 2026-09-18 21:45 UTC | 2026-09-18 21:58 UTC | 13m |
| N213RT |  | Mobile International Airport (KBFM) | Greensboro Municipal Airport (K7A0) | 2026-09-18 21:38 UTC | 2026-09-18 21:57 UTC | 19m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-09-18 10:18 UTC | 2026-09-18 21:57 UTC | 11h 38m |
| N501KT |  | K3A1 (K3A1) | Auburn University Regional Airport (KAUO) | 2026-09-18 21:29 UTC | 2026-09-18 21:56 UTC | 26m |
| N560SM |  | Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-09-18 21:25 UTC | 2026-09-18 21:55 UTC | 29m |
| BSM32 | BSM | Durant Regional/Eaker Field (KDUA) | Durant Regional/Eaker Field (KDUA) | 2026-09-18 21:41 UTC | 2026-09-18 21:55 UTC | 14m |
| N536HF |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-18 21:39 UTC | 2026-09-18 21:55 UTC | 15m |
| N987FA |  | Atlantic City International Airport (KACY) | Atlantic City International Airport (KACY) | 2026-09-18 21:53 UTC | 2026-09-18 21:54 UTC | 0m |
| SHWK414 | SHW | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-18 20:34 UTC | 2026-09-18 21:53 UTC | 1h 18m |
| N41520 |  | Montgomery-Gibbs Executive Airport (KMYF) | Brown Field Municipal Airport (KSDM) | 2026-09-18 21:16 UTC | 2026-09-18 21:52 UTC | 36m |
| BCS694 | BCS | Bengaluru International Airport (VOBL) | Macau International Airport (VMMC) | 2026-09-18 16:50 UTC | 2026-09-18 21:52 UTC | 5h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
