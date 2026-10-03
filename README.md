# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_02:11:18_UTC-green)

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

**Latest saved flight:** 2026-10-03 02:11:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-03 02:11:18 UTC

- **275,092** saved flights
- **80,176** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,092** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,328,423.7 tonnes** estimated CO2 emissions
- **192,952,096 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10787 |
| 2 | SkyWest Airlines | 9572 |
| 3 | EJA | 5391 |
| 4 | IndiGo | 4580 |
| 5 | American Airlines | 4257 |
| 6 | Southwest Airlines | 4043 |
| 7 | Delta Air Lines | 3418 |
| 8 | ENY | 3220 |
| 9 | LATAM Airlines | 2663 |
| 10 | AZU | 2586 |
| 11 | Vueling | 2281 |
| 12 | WIF | 2241 |
| 13 | LXJ | 2173 |
| 14 | Lufthansa | 2070 |
| 15 | easyJet | 1828 |
| 16 | Swiss International | 1801 |
| 17 | QLK | 1774 |
| 18 | EJU | 1710 |
| 19 | AXM | 1689 |
| 20 | United Airlines | 1678 |
| 21 | Alaska Airlines | 1620 |
| 22 | All Nippon Airways | 1572 |
| 23 | PGT | 1546 |
| 24 | GLO | 1536 |
| 25 | WMT | 1530 |
| 26 | Air France | 1509 |
| 27 | VIV | 1509 |
| 28 | Wizz Air | 1485 |
| 29 | CXK | 1356 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 229570 |
| 2 | 🇪🇸 ES | 17190 |
| 3 | 🇧🇷 BR | 16152 |
| 4 | 🇦🇺 AU | 15875 |
| 5 | 🇨🇦 CA | 15342 |
| 6 | 🇮🇹 IT | 14817 |
| 7 | 🇮🇳 IN | 14496 |
| 8 | 🇩🇪 DE | 13159 |
| 9 | 🇨🇴 CO | 12757 |
| 10 | 🇬🇧 GB | 12658 |
| 11 | 🇫🇷 FR | 10871 |
| 12 | 🇯🇵 JP | 10497 |
| 13 | 🇹🇷 TR | 8310 |
| 14 | 🇬🇷 GR | 7894 |
| 15 | 🇲🇽 MX | 7604 |
| 16 | 🇨🇭 CH | 7295 |
| 17 | 🇳🇴 NO | 6788 |
| 18 | 🇹🇭 TH | 4928 |
| 19 | 🇲🇾 MY | 4572 |
| 20 | 🇿🇦 ZA | 4558 |
| 21 | 🇵🇱 PL | 4484 |
| 22 | 🇳🇿 NZ | 3905 |
| 23 | 🇵🇭 PH | 3629 |
| 24 | 🇬🇹 GT | 3454 |
| 25 | 🇭🇷 HR | 3129 |
| 26 | 🇰🇷 KR | 3095 |
| 27 | 🇲🇦 MA | 2714 |
| 28 | 🇲🇪 ME | 2576 |
| 29 | 🇳🇱 NL | 2457 |
| 30 | 🇮🇩 ID | 2273 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5584 |
| 2 | Denver International Airport |  | US | 4490 |
| 3 | Indira Gandhi International Airport |  | IN | 3281 |
| 4 | Tokyo International Airport |  | JP | 3147 |
| 5 | El Dorado International Airport |  | CO | 3041 |
| 6 | Harry Reid International Airport |  | US | 2962 |
| 7 | Zurich Airport |  | CH | 2854 |
| 8 | Guaymaral Airport |  | CO | 2849 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2748 |
| 10 | La Aurora Airport |  | GT | 2626 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2626 |
| 12 | Salt Lake City International Airport |  | US | 2444 |
| 13 | Congonhas Airport |  | BR | 2351 |
| 14 | Chicago O'Hare International Airport |  | US | 2325 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2250 |
| 16 | Capua Airport |  | IT | 2133 |
| 17 | Madrid Barajas International Airport |  | ES | 2114 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2096 |
| 19 | Frankfurt am Main International Airport |  | DE | 2067 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1951 |
| 22 | Charles de Gaulle International Airport |  | FR | 1945 |
| 23 | Malpensa International Airport |  | IT | 1943 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1839 |
| 26 | Macau International Airport |  | MO | 1792 |
| 27 | Ninoy Aquino International Airport |  | PH | 1784 |
| 28 | Charlotte/Douglas International Airport |  | US | 1717 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1712 |
| 30 | Barcelona International Airport |  | ES | 1697 |
| 31 | Viracopos International Airport |  | BR | 1646 |
| 32 | Kuala Lumpur International Airport |  | MY | 1637 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1618 |
| 34 | Seattle-Tacoma International Airport |  | US | 1614 |
| 35 | Calgary International Airport |  | CA | 1563 |
| 36 | Don Mueang International Airport |  | TH | 1554 |
| 37 | Vancouver International Airport |  | CA | 1544 |
| 38 | Oslo Gardermoen Airport |  | NO | 1542 |
| 39 | Bengaluru International Airport |  | IN | 1536 |
| 40 | Reno/Tahoe International Airport |  | US | 1492 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1133 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1036 | 21m | 244 km | 4,362.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 695 | 1h 6m | 770 km | 9,232.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 691 | 24m | 225 km | 2,680.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 610 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 459 | 44m | 555 km | 4,395.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 443 | 27m | 275 km | 2,099.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 434 | 1h 50m | 1,423 km | 10,651.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 393 | 24m | 218 km | 1,480.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 372 | 23m | 55 km | 353.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 349 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 346 | 1h 6m | 706 km | 4,212.6 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 320 | 19m | 144 km | 796.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 316 | 18m | 14 km | 79.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 309 | 42m | 535 km | 2,853.8 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 273 | 44m | 431 km | 2,031.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N24998 |  | Oakland San Francisco Bay Airport (KOAK) | Byron Airport (KC83) | 2026-10-03 01:17 UTC | 2026-10-03 02:11 UTC | 53m |
| N54983 |  | Merrill Field (PAMR) | Homer Airport (PAHO) | 2026-10-03 00:43 UTC | 2026-10-03 01:55 UTC | 1h 12m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-10-03 01:39 UTC | 2026-10-03 01:51 UTC | 12m |
| N493LG |  | CO54 (CO54) | 7CO1 (7CO1) | 2026-10-03 01:33 UTC | 2026-10-03 01:47 UTC | 14m |
| N874BU |  | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-10-03 01:45 UTC | 2026-10-03 01:46 UTC | 1m |
| N714F |  | Washington Dulles International Airport (KIAD) | Logan-Cache Airport (KLGU) | 2026-10-02 21:38 UTC | 2026-10-03 01:42 UTC | 4h 4m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-10-03 01:23 UTC | 2026-10-03 01:38 UTC | 15m |
| N316PM |  | Grand Junction Regional Airport (KGJT) | CD82 (CD82) | 2026-10-03 01:09 UTC | 2026-10-03 01:35 UTC | 25m |
| N865PC |  | Dyersburg Regional Airport (KDYR) | Calico Rock Municipal Airport (K37T) | 2026-10-03 01:07 UTC | 2026-10-03 01:28 UTC | 20m |
| AIQ3140 | AIQ | Don Mueang International Airport (VTBD) | Kawthoung Airport (VYKT) | 2026-10-03 00:48 UTC | 2026-10-03 01:27 UTC | 38m |
| NYT302D | NYT | Langtang Airport (VNLT) | Langtang Airport (VNLT) | 2026-10-03 01:23 UTC | 2026-10-03 01:26 UTC | 2m |
| NWE | NWE | Beechworth Airport (YBCH) | Albury Airport (YMAY) | 2026-10-03 01:07 UTC | 2026-10-03 01:23 UTC | 16m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-10-02 18:30 UTC | 2026-10-03 01:23 UTC | 6h 52m |
| CPA660 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-10-02 20:24 UTC | 2026-10-03 01:22 UTC | 4h 58m |
| ZKNZO | ZKN | Glentanner Airport (NZGT) | Queenstown International Airport (NZQN) | 2026-10-03 01:08 UTC | 2026-10-03 01:20 UTC | 12m |
| TDY007 | TDY | Boeing Field/King County International Airport (KBFI) | Portland International Airport (KPDX) | 2026-10-03 00:39 UTC | 2026-10-03 01:20 UTC | 40m |
| IRJAH | IRJ | Brescia / Montichiari Airport (LIPO) | Ghedi Airport (LIPL) | 2026-10-03 01:11 UTC | 2026-10-03 01:19 UTC | 7m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Kerikeri Airport (NZKK) | 2026-10-03 00:51 UTC | 2026-10-03 01:19 UTC | 27m |
| ANA383 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-10-03 00:26 UTC | 2026-10-03 01:15 UTC | 48m |
| JA01EE |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-10-03 01:13 UTC | 2026-10-03 01:14 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
