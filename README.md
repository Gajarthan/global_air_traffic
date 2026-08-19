# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_23:42:38_UTC-green)

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

**Latest saved flight:** 2026-08-18 23:42:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 23:42:38 UTC

- **213,953** saved flights
- **67,642** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,953** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,572,694.8 tonnes** estimated CO2 emissions
- **149,141,726 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8487 |
| 2 | SkyWest Airlines | 7685 |
| 3 | EJA | 4180 |
| 4 | IndiGo | 3644 |
| 5 | American Airlines | 3576 |
| 6 | Southwest Airlines | 3423 |
| 7 | Delta Air Lines | 2761 |
| 8 | ENY | 2659 |
| 9 | LATAM Airlines | 2025 |
| 10 | AZU | 1960 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1692 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1360 |
| 19 | QLK | 1323 |
| 20 | EJU | 1316 |
| 21 | Alaska Airlines | 1312 |
| 22 | All Nippon Airways | 1287 |
| 23 | VIV | 1180 |
| 24 | GLO | 1163 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1090 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181000 |
| 2 | 🇪🇸 ES | 13681 |
| 3 | 🇧🇷 BR | 12335 |
| 4 | 🇦🇺 AU | 11988 |
| 5 | 🇨🇦 CA | 11823 |
| 6 | 🇮🇳 IN | 11360 |
| 7 | 🇮🇹 IT | 11267 |
| 8 | 🇩🇪 DE | 10541 |
| 9 | 🇬🇧 GB | 9971 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8701 |
| 12 | 🇫🇷 FR | 8488 |
| 13 | 🇬🇷 GR | 6263 |
| 14 | 🇹🇷 TR | 6133 |
| 15 | 🇲🇽 MX | 6008 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3676 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2959 |
| 23 | 🇵🇭 PH | 2843 |
| 24 | 🇬🇹 GT | 2730 |
| 25 | 🇰🇷 KR | 2586 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1849 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4510 |
| 2 | Denver International Airport |  | US | 3505 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2594 |
| 5 | Guaymaral Airport |  | CO | 2559 |
| 6 | Harry Reid International Airport |  | US | 2391 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2210 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2076 |
| 11 | El Dorado International Airport |  | CO | 1981 |
| 12 | Chicago O'Hare International Airport |  | US | 1977 |
| 13 | Salt Lake City International Airport |  | US | 1892 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1888 |
| 15 | Congonhas Airport |  | BR | 1797 |
| 16 | Frankfurt am Main International Airport |  | DE | 1741 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1617 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1616 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1572 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1492 |
| 24 | Malpensa International Airport |  | IT | 1491 |
| 25 | Charles de Gaulle International Airport |  | FR | 1472 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1357 |
| 28 | Ninoy Aquino International Airport |  | PH | 1348 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1304 |
| 31 | Bengaluru International Airport |  | IN | 1304 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1285 |
| 33 | Seattle-Tacoma International Airport |  | US | 1273 |
| 34 | Viracopos International Airport |  | BR | 1253 |
| 35 | Calgary International Airport |  | CA | 1214 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1161 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Enrique Olaya Herrera Airport |  | CO | 1139 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1046 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 761 | 21m | 244 km | 3,204.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 494 | 24m | 225 km | 1,916.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 266 | 19m | 99 km | 455.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 265 | 1h 38m | 1,156 km | 5,286.7 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 246 | 31m | 369 km | 1,565.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 241 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N859BT |  | Blue Grass Airport (KLEX) | Georgetown-Scott County Regional Airport (K27K) | 2026-08-18 23:25 UTC | 2026-08-18 23:42 UTC | 17m |
| RMRNR53 | RMR | North Island Nas (Halsey Field) Airport (KNZY) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-18 23:14 UTC | 2026-08-18 23:38 UTC | 24m |
| FFAB123 | FFA | FD48 (FD48) | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | 2026-08-18 22:56 UTC | 2026-08-18 23:38 UTC | 41m |
| N496PJ |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-18 22:43 UTC | 2026-08-18 23:36 UTC | 53m |
| SYH3831 | SYH | Hancock County/Bar Harbor Airport (KBHB) | Tweed/New Haven Airport (KHVN) | 2026-08-18 21:39 UTC | 2026-08-18 23:30 UTC | 1h 51m |
| UPS2846 | UPS | Chicago/Rockford International Airport (KRFD) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-18 20:26 UTC | 2026-08-18 23:26 UTC | 2h 59m |
| N702QV |  | Durham Tees Valley Airport (EGNV) | Bangor International Airport (KBGR) | 2026-08-18 17:13 UTC | 2026-08-18 23:22 UTC | 6h 9m |
| N8636Q |  | Meadowmist Airport (WN35) | Boeing Field/King County International Airport (KBFI) | 2026-08-18 22:42 UTC | 2026-08-18 23:21 UTC | 39m |
| N582BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-18 22:39 UTC | 2026-08-18 23:21 UTC | 41m |
| N2366W |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-08-18 23:15 UTC | 2026-08-18 23:19 UTC | 4m |
| N441LF |  | E Northrop Grumman Airport (07UT) | Salt Lake City International Airport (KSLC) | 2026-08-18 22:40 UTC | 2026-08-18 23:18 UTC | 38m |
| N6409D |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-08-18 22:08 UTC | 2026-08-18 23:18 UTC | 1h 9m |
| N640TC |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-08-18 22:26 UTC | 2026-08-18 23:17 UTC | 50m |
| N914BD |  | Santa Maria Ranch Airport (0TE5) | Gurdon Lowe Field (K5M8) | 2026-08-18 22:13 UTC | 2026-08-18 23:16 UTC | 1h 3m |
| EJA843 | EJA | Rocky Mountain Metro Airport (KBJC) | Sacramento International Airport (KSMF) | 2026-08-18 21:14 UTC | 2026-08-18 23:16 UTC | 2h 1m |
| N206FS |  | Teterboro Airport (KTEB) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-18 21:51 UTC | 2026-08-18 23:15 UTC | 1h 24m |
| N888YW |  | Brackett Field (KPOC) | San Gabriel Valley Airport (KEMT) | 2026-08-18 22:52 UTC | 2026-08-18 23:13 UTC | 21m |
| TWY271 | TWY | William P Hobby Airport (KHOU) | Cavern City Air Trml Airport (KCNM) | 2026-08-18 21:56 UTC | 2026-08-18 23:11 UTC | 1h 14m |
| N36HF |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-18 22:30 UTC | 2026-08-18 23:11 UTC | 40m |
| CGPCR | CGP | Vancouver International Airport (CYVR) | Big Andy Airport (7WA0) | 2026-08-18 22:48 UTC | 2026-08-18 23:10 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
