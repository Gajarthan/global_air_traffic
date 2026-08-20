# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_15:07:42_UTC-green)

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

**Latest saved flight:** 2026-08-20 15:07:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 15:07:42 UTC

- **219,472** saved flights
- **68,934** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,472** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,642,851.2 tonnes** estimated CO2 emissions
- **153,208,764 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8804 |
| 2 | SkyWest Airlines | 7814 |
| 3 | EJA | 4252 |
| 4 | IndiGo | 3727 |
| 5 | American Airlines | 3640 |
| 6 | Southwest Airlines | 3473 |
| 7 | Delta Air Lines | 2827 |
| 8 | ENY | 2699 |
| 9 | LATAM Airlines | 2081 |
| 10 | AZU | 2011 |
| 11 | Vueling | 1847 |
| 12 | Lufthansa | 1821 |
| 13 | WIF | 1755 |
| 14 | LXJ | 1731 |
| 15 | easyJet | 1521 |
| 16 | Swiss International | 1460 |
| 17 | AXM | 1443 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1370 |
| 21 | Alaska Airlines | 1339 |
| 22 | All Nippon Airways | 1319 |
| 23 | VIV | 1199 |
| 24 | GLO | 1196 |
| 25 | Air France | 1191 |
| 26 | PGT | 1190 |
| 27 | WMT | 1155 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1114 |
| 30 | AEE | 1099 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184504 |
| 2 | 🇪🇸 ES | 14080 |
| 3 | 🇧🇷 BR | 12668 |
| 4 | 🇦🇺 AU | 12416 |
| 5 | 🇨🇦 CA | 12101 |
| 6 | 🇮🇹 IT | 11697 |
| 7 | 🇮🇳 IN | 11619 |
| 8 | 🇩🇪 DE | 10847 |
| 9 | 🇬🇧 GB | 10317 |
| 10 | 🇨🇴 CO | 9004 |
| 11 | 🇯🇵 JP | 8959 |
| 12 | 🇫🇷 FR | 8749 |
| 13 | 🇬🇷 GR | 6402 |
| 14 | 🇹🇷 TR | 6318 |
| 15 | 🇲🇽 MX | 6103 |
| 16 | 🇨🇭 CH | 5811 |
| 17 | 🇳🇴 NO | 5452 |
| 18 | 🇲🇾 MY | 3818 |
| 19 | 🇿🇦 ZA | 3751 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3642 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2959 |
| 24 | 🇬🇹 GT | 2778 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2429 |
| 27 | 🇲🇦 MA | 2213 |
| 28 | 🇳🇱 NL | 1953 |
| 29 | 🇲🇪 ME | 1940 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4594 |
| 2 | Denver International Airport |  | US | 3580 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2663 |
| 5 | Guaymaral Airport |  | CO | 2597 |
| 6 | Harry Reid International Airport |  | US | 2420 |
| 7 | Zurich Airport |  | CH | 2277 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2250 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2230 |
| 10 | La Aurora Airport |  | GT | 2116 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2009 |
| 13 | Salt Lake City International Airport |  | US | 1932 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1900 |
| 15 | Congonhas Airport |  | BR | 1852 |
| 16 | Frankfurt am Main International Airport |  | DE | 1787 |
| 17 | Madrid Barajas International Airport |  | ES | 1724 |
| 18 | Capua Airport |  | IT | 1675 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1620 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1612 |
| 22 | Macau International Airport |  | MO | 1577 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1511 |
| 26 | Charlotte/Douglas International Airport |  | US | 1462 |
| 27 | Ninoy Aquino International Airport |  | PH | 1407 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1333 |
| 31 | Bengaluru International Airport |  | IN | 1324 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1285 |
| 35 | Calgary International Airport |  | CA | 1237 |
| 36 | Vitoria/Foronda Airport |  | ES | 1218 |
| 37 | Oslo Gardermoen Airport |  | NO | 1216 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1207 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1180 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 497 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 487 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 368 | 27m | 275 km | 1,743.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 295 | 22m | 55 km | 280.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 289 | 21m | 250 km | 1,248.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 273 | 1h 38m | 1,156 km | 5,446.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 271 | 24m | 218 km | 1,021.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 270 | 27m | 215 km | 1,000.0 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 261 | 13m | - | - |
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
| CGMTG | CGM | Victoria International Airport (CYYJ) | Pitt Meadows Airport (CYPK) | 2026-08-20 14:40 UTC | 2026-08-20 15:07 UTC | 26m |
| QTR69X | Qatar Airways | Hamad International Airport (OTHH) | Sheremetyevo International Airport (UUEE) | 2026-08-20 06:30 UTC | 2026-08-20 15:00 UTC | 8h 29m |
| N999AF |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-20 14:58 UTC | 2026-08-20 14:58 UTC | 0m |
| PREY21 | PRE | Bailey Airport (2TS8) | Tee Pee Creek Airport (8TE0) | 2026-08-20 14:35 UTC | 2026-08-20 14:52 UTC | 17m |
| DSU08 | DSU | Cleveland Municipal Airport (KRNV) | West Bolivar Flying Service Airport (MS37) | 2026-08-20 14:38 UTC | 2026-08-20 14:50 UTC | 11m |
| N1449C |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-20 14:28 UTC | 2026-08-20 14:46 UTC | 17m |
| FNA77C | FNA | Reykjavik Airport (BIRK) | Forsaeti Airport (BIFZ) | 2026-08-20 14:33 UTC | 2026-08-20 14:45 UTC | 11m |
| N1356U |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-08-20 14:26 UTC | 2026-08-20 14:44 UTC | 17m |
|  |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-20 14:40 UTC | 2026-08-20 14:40 UTC | 0m |
| CXK601 | CXK | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-20 14:30 UTC | 2026-08-20 14:38 UTC | 7m |
| N550WR |  | 5TA4 (5TA4) | Wildlife/Stroud Airport (TS80) | 2026-08-20 14:11 UTC | 2026-08-20 14:37 UTC | 25m |
| LFA553 | LFA | Flying Dutchman Ranch Airport (FD29) | FL47 (FL47) | 2026-08-20 13:46 UTC | 2026-08-20 14:36 UTC | 50m |
| N5522X |  | Tulsa Riverside Airport (KRVS) | Gregg Airport (7OK1) | 2026-08-20 14:00 UTC | 2026-08-20 14:35 UTC | 34m |
| N6309B |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-20 14:19 UTC | 2026-08-20 14:34 UTC | 14m |
| CNS1010 | CNS | North Fork Valley Airport (K7V2) | 1CO7 (1CO7) | 2026-08-20 14:01 UTC | 2026-08-20 14:33 UTC | 31m |
| CGNNQ | CGN | Colonial Airport (NY24) | Niagara South Airport (CNF9) | 2026-08-20 13:10 UTC | 2026-08-20 14:32 UTC | 1h 21m |
| SKED02 | SKE | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-08-20 13:59 UTC | 2026-08-20 14:29 UTC | 29m |
| SWR2HY | Swiss International | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Zurich Airport (LSZH) | 2026-08-20 13:33 UTC | 2026-08-20 14:26 UTC | 53m |
| CPA3144 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-08-20 09:46 UTC | 2026-08-20 14:26 UTC | 4h 39m |
| WIF7DT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-20 14:12 UTC | 2026-08-20 14:24 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
