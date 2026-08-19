# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_01:32:07_UTC-green)

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

**Latest saved flight:** 2026-08-19 01:32:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 01:32:07 UTC

- **214,090** saved flights
- **67,679** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **214,090** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,573,775.0 tonnes** estimated CO2 emissions
- **149,204,350 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8487 |
| 2 | SkyWest Airlines | 7691 |
| 3 | EJA | 4183 |
| 4 | IndiGo | 3645 |
| 5 | American Airlines | 3578 |
| 6 | Southwest Airlines | 3427 |
| 7 | Delta Air Lines | 2764 |
| 8 | ENY | 2660 |
| 9 | LATAM Airlines | 2026 |
| 10 | AZU | 1960 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1693 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1393 |
| 18 | United Airlines | 1360 |
| 19 | QLK | 1324 |
| 20 | EJU | 1316 |
| 21 | Alaska Airlines | 1313 |
| 22 | All Nippon Airways | 1289 |
| 23 | VIV | 1180 |
| 24 | GLO | 1163 |
| 25 | Air France | 1154 |
| 26 | PGT | 1154 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1091 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181157 |
| 2 | 🇪🇸 ES | 13682 |
| 3 | 🇧🇷 BR | 12337 |
| 4 | 🇦🇺 AU | 12008 |
| 5 | 🇨🇦 CA | 11833 |
| 6 | 🇮🇳 IN | 11360 |
| 7 | 🇮🇹 IT | 11267 |
| 8 | 🇩🇪 DE | 10541 |
| 9 | 🇬🇧 GB | 9971 |
| 10 | 🇯🇵 JP | 8796 |
| 11 | 🇨🇴 CO | 8715 |
| 12 | 🇫🇷 FR | 8490 |
| 13 | 🇬🇷 GR | 6263 |
| 14 | 🇹🇷 TR | 6135 |
| 15 | 🇲🇽 MX | 6011 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3682 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3454 |
| 22 | 🇳🇿 NZ | 2967 |
| 23 | 🇵🇭 PH | 2847 |
| 24 | 🇬🇹 GT | 2730 |
| 25 | 🇰🇷 KR | 2589 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1849 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4512 |
| 2 | Denver International Airport |  | US | 3507 |
| 3 | Tokyo International Airport |  | JP | 2639 |
| 4 | Indira Gandhi International Airport |  | IN | 2594 |
| 5 | Guaymaral Airport |  | CO | 2561 |
| 6 | Harry Reid International Airport |  | US | 2392 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2211 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2076 |
| 11 | El Dorado International Airport |  | CO | 1987 |
| 12 | Chicago O'Hare International Airport |  | US | 1977 |
| 13 | Salt Lake City International Airport |  | US | 1898 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1798 |
| 16 | Frankfurt am Main International Airport |  | DE | 1741 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1617 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1616 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1572 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1496 |
| 24 | Malpensa International Airport |  | IT | 1491 |
| 25 | Charles de Gaulle International Airport |  | FR | 1473 |
| 26 | Charlotte/Douglas International Airport |  | US | 1442 |
| 27 | Kuala Lumpur International Airport |  | MY | 1359 |
| 28 | Ninoy Aquino International Airport |  | PH | 1350 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 30 | Barcelona International Airport |  | ES | 1305 |
| 31 | Bengaluru International Airport |  | IN | 1304 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1274 |
| 34 | Viracopos International Airport |  | BR | 1253 |
| 35 | Calgary International Airport |  | CA | 1215 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1161 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Don Mueang International Airport |  | TH | 1140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1047 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 763 | 21m | 244 km | 3,212.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 527 | 1h 7m | 770 km | 7,000.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 495 | 24m | 225 km | 1,920.4 t |
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
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 252 | 19m | 165 km | 716.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 247 | 31m | 369 km | 1,572.2 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 242 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR182 | TKR | Coeur D'Alene Airport (KCOE) | MT98 (MT98) | 2026-08-19 01:19 UTC | 2026-08-19 01:32 UTC | 12m |
|  |  | Ronald Reagan Washington Ntl Airport (KDCA) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-19 00:07 UTC | 2026-08-19 01:28 UTC | 1h 21m |
| N96FE |  | Battle Creek Executive At Kellogg Field (KBTL) | Akron-Canton Regional Airport (KCAK) | 2026-08-19 00:48 UTC | 2026-08-19 01:26 UTC | 37m |
| BLVH | BLV | Chek Lap Kok International Airport (VHHH) | Shek Kong Air Base (VHSK) | 2026-08-19 01:07 UTC | 2026-08-19 01:25 UTC | 17m |
| N24857 |  | North Perry Airport (KHWO) | Miami Executive Airport (KTMB) | 2026-08-19 00:51 UTC | 2026-08-19 01:24 UTC | 32m |
| N154PS |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-08-19 01:13 UTC | 2026-08-19 01:23 UTC | 10m |
| SXI | SXI | Cessnock Airport (YCNK) | Cessnock Airport (YCNK) | 2026-08-19 00:17 UTC | 2026-08-19 01:18 UTC | 1h 0m |
| N714KV |  | Conroe/North Houston Regional Airport (KCXO) | Austin-Bergstrom International Airport (KAUS) | 2026-08-19 00:43 UTC | 2026-08-19 01:14 UTC | 31m |
| SKQ55 | SKQ | Burlington/Alamance Regional Airport (KBUY) | Asplundh Airport (MD64) | 2026-08-18 23:58 UTC | 2026-08-19 01:08 UTC | 1h 9m |
| DTCHMN41 | DTC | North Island Nas (Halsey Field) Airport (KNZY) | San Clemente Island Nalf Airport (KNUC) | 2026-08-19 00:30 UTC | 2026-08-19 01:06 UTC | 35m |
| CXK416 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-08-18 23:45 UTC | 2026-08-19 00:51 UTC | 1h 6m |
| N95539 |  | Portland-Hillsboro Airport (KHIO) | Corvallis Municipal Airport (KCVO) | 2026-08-19 00:00 UTC | 2026-08-19 00:51 UTC | 50m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-19 00:39 UTC | 2026-08-19 00:50 UTC | 11m |
| DSU93 | DSU | MS85 (MS85) | Cleveland Municipal Airport (KRNV) | 2026-08-19 00:14 UTC | 2026-08-19 00:49 UTC | 34m |
| N856FG |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-08-19 00:05 UTC | 2026-08-19 00:47 UTC | 41m |
| TWY281 | TWY | Moffett Federal Airfield (KNUQ) | Truckee-Tahoe Airport (KTRK) | 2026-08-19 00:16 UTC | 2026-08-19 00:45 UTC | 29m |
| NSE8722 | NSE | El Dorado International Airport (SKBO) | Aguas Claras Airport (SKOC) | 2026-08-18 23:59 UTC | 2026-08-19 00:45 UTC | 45m |
| NTR716 | NTR | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-08-18 23:56 UTC | 2026-08-19 00:44 UTC | 47m |
| N407MA |  | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-19 00:40 UTC | 2026-08-19 00:44 UTC | 3m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-18 23:08 UTC | 2026-08-19 00:42 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
