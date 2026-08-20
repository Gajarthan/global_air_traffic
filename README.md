# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_14:36:24_UTC-green)

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

**Latest saved flight:** 2026-08-20 14:36:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 14:36:24 UTC

- **219,388** saved flights
- **68,918** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,388** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,641,995.9 tonnes** estimated CO2 emissions
- **153,159,181 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8800 |
| 2 | SkyWest Airlines | 7813 |
| 3 | EJA | 4249 |
| 4 | IndiGo | 3726 |
| 5 | American Airlines | 3640 |
| 6 | Southwest Airlines | 3472 |
| 7 | Delta Air Lines | 2826 |
| 8 | ENY | 2698 |
| 9 | LATAM Airlines | 2081 |
| 10 | AZU | 2011 |
| 11 | Vueling | 1847 |
| 12 | Lufthansa | 1821 |
| 13 | WIF | 1753 |
| 14 | LXJ | 1731 |
| 15 | easyJet | 1521 |
| 16 | Swiss International | 1460 |
| 17 | AXM | 1443 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1368 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1198 |
| 24 | GLO | 1193 |
| 25 | Air France | 1190 |
| 26 | PGT | 1189 |
| 27 | WMT | 1154 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1114 |
| 30 | AEE | 1099 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184448 |
| 2 | 🇪🇸 ES | 14072 |
| 3 | 🇧🇷 BR | 12663 |
| 4 | 🇦🇺 AU | 12416 |
| 5 | 🇨🇦 CA | 12092 |
| 6 | 🇮🇹 IT | 11693 |
| 7 | 🇮🇳 IN | 11616 |
| 8 | 🇩🇪 DE | 10840 |
| 9 | 🇬🇧 GB | 10316 |
| 10 | 🇨🇴 CO | 8998 |
| 11 | 🇯🇵 JP | 8959 |
| 12 | 🇫🇷 FR | 8746 |
| 13 | 🇬🇷 GR | 6399 |
| 14 | 🇹🇷 TR | 6316 |
| 15 | 🇲🇽 MX | 6101 |
| 16 | 🇨🇭 CH | 5811 |
| 17 | 🇳🇴 NO | 5449 |
| 18 | 🇲🇾 MY | 3818 |
| 19 | 🇿🇦 ZA | 3747 |
| 20 | 🇹🇭 TH | 3653 |
| 21 | 🇵🇱 PL | 3640 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2959 |
| 24 | 🇬🇹 GT | 2773 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2425 |
| 27 | 🇲🇦 MA | 2211 |
| 28 | 🇳🇱 NL | 1953 |
| 29 | 🇲🇪 ME | 1938 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4593 |
| 2 | Denver International Airport |  | US | 3580 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2662 |
| 5 | Guaymaral Airport |  | CO | 2596 |
| 6 | Harry Reid International Airport |  | US | 2420 |
| 7 | Zurich Airport |  | CH | 2277 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2248 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2229 |
| 10 | La Aurora Airport |  | GT | 2111 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2009 |
| 13 | Salt Lake City International Airport |  | US | 1932 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1851 |
| 16 | Frankfurt am Main International Airport |  | DE | 1786 |
| 17 | Madrid Barajas International Airport |  | ES | 1722 |
| 18 | Capua Airport |  | IT | 1673 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1620 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1610 |
| 22 | Macau International Airport |  | MO | 1577 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1510 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1407 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1333 |
| 31 | Bengaluru International Airport |  | IN | 1323 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1285 |
| 35 | Calgary International Airport |  | CA | 1236 |
| 36 | Vitoria/Foronda Airport |  | ES | 1217 |
| 37 | Oslo Gardermoen Airport |  | NO | 1215 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1205 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1180 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 495 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 486 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 367 | 27m | 275 km | 1,739.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 321 | 44m | 241 km | 1,333.4 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 289 | 21m | 250 km | 1,248.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 271 | 24m | 218 km | 1,021.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 270 | 27m | 215 km | 1,000.0 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 260 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 250 | 19m | 144 km | 621.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA553 | LFA | Flying Dutchman Ranch Airport (FD29) | FL47 (FL47) | 2026-08-20 13:46 UTC | 2026-08-20 14:36 UTC | 50m |
| CGNNQ | CGN | Colonial Airport (NY24) | Niagara South Airport (CNF9) | 2026-08-20 13:10 UTC | 2026-08-20 14:32 UTC | 1h 21m |
| SKED02 | SKE | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-08-20 13:59 UTC | 2026-08-20 14:29 UTC | 29m |
| SWR2HY | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-08-20 13:33 UTC | 2026-08-20 14:26 UTC | 53m |
| CPA3144 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-08-20 09:46 UTC | 2026-08-20 14:26 UTC | 4h 39m |
| N733FF |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-20 14:11 UTC | 2026-08-20 14:22 UTC | 10m |
| CHOSEN1 | CHO | Kickapoo Downtown Airport (KCWC) | 85OL (85OL) | 2026-08-20 13:56 UTC | 2026-08-20 14:21 UTC | 25m |
| N5102D |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-20 13:19 UTC | 2026-08-20 14:21 UTC | 1h 2m |
| CXK601 | CXK | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-20 13:34 UTC | 2026-08-20 14:19 UTC | 45m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 07:24 UTC | 2026-08-20 14:16 UTC | 6h 51m |
| N13WD |  | CD82 (CD82) | CD82 (CD82) | 2026-08-20 14:04 UTC | 2026-08-20 14:15 UTC | 11m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-20 13:24 UTC | 2026-08-20 14:15 UTC | 50m |
| N300LX |  | Phoenix Deer Valley Airport (KDVT) | 2AZ7 (2AZ7) | 2026-08-20 14:05 UTC | 2026-08-20 14:14 UTC | 8m |
| BOX500 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-08-20 04:01 UTC | 2026-08-20 14:13 UTC | 10h 11m |
| RTY186 | RTY | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-08-20 13:25 UTC | 2026-08-20 14:11 UTC | 46m |
| N272FC |  | Lee Gilmer Memorial Airport (KGVL) | Bangor International Airport (KBGR) | 2026-08-20 12:10 UTC | 2026-08-20 14:10 UTC | 2h 0m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-08-20 13:38 UTC | 2026-08-20 14:06 UTC | 28m |
| EAI65Y | EAI | Birmingham International Airport (EGBB) | Dublin Airport (EIDW) | 2026-08-20 13:09 UTC | 2026-08-20 14:05 UTC | 55m |
|  |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-08-20 14:03 UTC | 2026-08-20 14:03 UTC | 0m |
| N640TC |  | KU42 (KU42) | KU42 (KU42) | 2026-08-20 13:41 UTC | 2026-08-20 14:03 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
