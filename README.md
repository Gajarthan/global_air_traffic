# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_22:21:07_UTC-green)

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

**Latest saved flight:** 2026-08-18 22:21:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 22:21:07 UTC

- **213,715** saved flights
- **67,593** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,715** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,570,155.6 tonnes** estimated CO2 emissions
- **148,994,527 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8484 |
| 2 | SkyWest Airlines | 7678 |
| 3 | EJA | 4173 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3572 |
| 6 | Southwest Airlines | 3419 |
| 7 | Delta Air Lines | 2754 |
| 8 | ENY | 2653 |
| 9 | LATAM Airlines | 2013 |
| 10 | AZU | 1953 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1687 |
| 15 | easyJet | 1482 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1358 |
| 19 | QLK | 1321 |
| 20 | EJU | 1315 |
| 21 | Alaska Airlines | 1311 |
| 22 | All Nippon Airways | 1287 |
| 23 | VIV | 1178 |
| 24 | GLO | 1160 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1088 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180733 |
| 2 | 🇪🇸 ES | 13681 |
| 3 | 🇧🇷 BR | 12289 |
| 4 | 🇦🇺 AU | 11968 |
| 5 | 🇨🇦 CA | 11814 |
| 6 | 🇮🇳 IN | 11357 |
| 7 | 🇮🇹 IT | 11266 |
| 8 | 🇩🇪 DE | 10537 |
| 9 | 🇬🇧 GB | 9965 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8691 |
| 12 | 🇫🇷 FR | 8486 |
| 13 | 🇬🇷 GR | 6261 |
| 14 | 🇹🇷 TR | 6128 |
| 15 | 🇲🇽 MX | 5996 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3676 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2953 |
| 23 | 🇵🇭 PH | 2831 |
| 24 | 🇬🇹 GT | 2728 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1848 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4498 |
| 2 | Denver International Airport |  | US | 3500 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2593 |
| 5 | Guaymaral Airport |  | CO | 2559 |
| 6 | Harry Reid International Airport |  | US | 2388 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2203 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2074 |
| 11 | El Dorado International Airport |  | CO | 1978 |
| 12 | Chicago O'Hare International Airport |  | US | 1975 |
| 13 | Salt Lake City International Airport |  | US | 1890 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1886 |
| 15 | Congonhas Airport |  | BR | 1790 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1617 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1614 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1604 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1563 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Malpensa International Airport |  | IT | 1491 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 25 | Charles de Gaulle International Airport |  | FR | 1472 |
| 26 | Charlotte/Douglas International Airport |  | US | 1439 |
| 27 | Kuala Lumpur International Airport |  | MY | 1357 |
| 28 | Ninoy Aquino International Airport |  | PH | 1342 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1317 |
| 30 | Barcelona International Airport |  | ES | 1304 |
| 31 | Bengaluru International Airport |  | IN | 1304 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1285 |
| 33 | Seattle-Tacoma International Airport |  | US | 1268 |
| 34 | Viracopos International Airport |  | BR | 1249 |
| 35 | Calgary International Airport |  | CA | 1212 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1160 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1046 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 760 | 21m | 244 km | 3,200.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 482 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 456 | 8m | - | - |
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
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 240 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 230 | 1h 49m | 1,304 km | 5,174.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N92N |  | John F Kennedy International Airport (KJFK) | John F Kennedy International Airport (KJFK) | 2026-08-18 21:59 UTC | 2026-08-18 22:21 UTC | 21m |
| SWA4064 | Southwest Airlines | Luis Munoz Marin International Airport (TJSJ) | Garner Field (02MD) | 2026-08-18 18:49 UTC | 2026-08-18 22:19 UTC | 3h 29m |
| CPA698 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-08-18 10:16 UTC | 2026-08-18 22:15 UTC | 11h 58m |
| N734VQ |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-18 21:55 UTC | 2026-08-18 22:13 UTC | 17m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-18 06:40 UTC | 2026-08-18 22:10 UTC | 15h 30m |
| N669FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-18 21:17 UTC | 2026-08-18 22:10 UTC | 52m |
| RYR16GW | Ryanair | Luxembourg-Findel International Airport (ELLX) | Santa Cruz Airport (LPSC) | 2026-08-18 19:32 UTC | 2026-08-18 22:10 UTC | 2h 37m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-18 17:10 UTC | 2026-08-18 22:08 UTC | 4h 58m |
| SXS5XQ | SXS | London Stansted Airport (EGSS) | Kaklic Airport (LTFA) | 2026-08-18 19:14 UTC | 2026-08-18 22:02 UTC | 2h 47m |
| AMMO79 | AMM | Edwards Af Aux North Base Airport (K9L2) | Boron Airstrip (57CL) | 2026-08-18 21:49 UTC | 2026-08-18 21:59 UTC | 10m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-18 21:44 UTC | 2026-08-18 21:56 UTC | 12m |
| SXS7AM | SXS | Vienna International Airport (LOWW) | Kaklic Airport (LTFA) | 2026-08-18 20:15 UTC | 2026-08-18 21:51 UTC | 1h 36m |
| MWT200 | MWT | Joe Foss Field (KFSD) | SD66 (SD66) | 2026-08-18 20:56 UTC | 2026-08-18 21:51 UTC | 55m |
| VPCNR | VPC | Bob Hope Airport (KBUR) | Bob Hope Airport (KBUR) | 2026-08-18 21:44 UTC | 2026-08-18 21:48 UTC | 3m |
| N160WP |  | Atlanta Regional Falcon Field (KFFC) | Thomaston-Upson County Airport (KOPN) | 2026-08-18 21:22 UTC | 2026-08-18 21:46 UTC | 23m |
| GT322 |  | Prince Albert (Glass Field) Airport (CYPA) | Regina Beach Airport (CKL9) | 2026-08-18 21:17 UTC | 2026-08-18 21:46 UTC | 28m |
| N798BP |  | Sky River Ranch Airport (WA78) | Sky River Ranch Airport (WA78) | 2026-08-18 20:28 UTC | 2026-08-18 21:44 UTC | 1h 15m |
| N26BQ |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-18 21:20 UTC | 2026-08-18 21:43 UTC | 22m |
| SXS5VF | SXS | Dublin Airport (EIDW) | Kaklic Airport (LTFA) | 2026-08-18 18:28 UTC | 2026-08-18 21:43 UTC | 3h 14m |
| N402MT |  | Detroit Metro Wayne County Airport (KDTW) | Auburn University Regional Airport (KAUO) | 2026-08-18 20:00 UTC | 2026-08-18 21:41 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
