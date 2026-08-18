# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_16:29:52_UTC-green)

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

**Latest saved flight:** 2026-08-18 16:29:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 16:29:52 UTC

- **212,507** saved flights
- **67,320** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **212,507** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,554,369.3 tonnes** estimated CO2 emissions
- **148,079,379 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8427 |
| 2 | SkyWest Airlines | 7615 |
| 3 | EJA | 4129 |
| 4 | IndiGo | 3639 |
| 5 | American Airlines | 3540 |
| 6 | Southwest Airlines | 3387 |
| 7 | Delta Air Lines | 2738 |
| 8 | ENY | 2633 |
| 9 | LATAM Airlines | 2006 |
| 10 | AZU | 1932 |
| 11 | Lufthansa | 1781 |
| 12 | Vueling | 1777 |
| 13 | WIF | 1709 |
| 14 | LXJ | 1675 |
| 15 | easyJet | 1473 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1390 |
| 18 | United Airlines | 1343 |
| 19 | QLK | 1320 |
| 20 | EJU | 1305 |
| 21 | Alaska Airlines | 1303 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1168 |
| 24 | GLO | 1150 |
| 25 | PGT | 1149 |
| 26 | Air France | 1148 |
| 27 | WMT | 1092 |
| 28 | JetBlue | 1081 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1059 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179463 |
| 2 | 🇪🇸 ES | 13619 |
| 3 | 🇧🇷 BR | 12207 |
| 4 | 🇦🇺 AU | 11962 |
| 5 | 🇨🇦 CA | 11738 |
| 6 | 🇮🇳 IN | 11343 |
| 7 | 🇮🇹 IT | 11181 |
| 8 | 🇩🇪 DE | 10511 |
| 9 | 🇬🇧 GB | 9919 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8578 |
| 12 | 🇫🇷 FR | 8448 |
| 13 | 🇬🇷 GR | 6221 |
| 14 | 🇹🇷 TR | 6093 |
| 15 | 🇲🇽 MX | 5949 |
| 16 | 🇨🇭 CH | 5646 |
| 17 | 🇳🇴 NO | 5297 |
| 18 | 🇲🇾 MY | 3673 |
| 19 | 🇿🇦 ZA | 3592 |
| 20 | 🇵🇱 PL | 3510 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2721 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2310 |
| 27 | 🇲🇦 MA | 2142 |
| 28 | 🇳🇱 NL | 1896 |
| 29 | 🇲🇪 ME | 1831 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4459 |
| 2 | Denver International Airport |  | US | 3466 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2589 |
| 5 | Guaymaral Airport |  | CO | 2542 |
| 6 | Harry Reid International Airport |  | US | 2379 |
| 7 | Zurich Airport |  | CH | 2219 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2189 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2188 |
| 10 | La Aurora Airport |  | GT | 2068 |
| 11 | Chicago O'Hare International Airport |  | US | 1961 |
| 12 | El Dorado International Airport |  | CO | 1959 |
| 13 | Salt Lake City International Airport |  | US | 1877 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1876 |
| 15 | Congonhas Airport |  | BR | 1778 |
| 16 | Frankfurt am Main International Airport |  | DE | 1735 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1601 |
| 19 | Capua Airport |  | IT | 1600 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1598 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1556 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1475 |
| 25 | Charles de Gaulle International Airport |  | FR | 1462 |
| 26 | Charlotte/Douglas International Airport |  | US | 1430 |
| 27 | Kuala Lumpur International Airport |  | MY | 1354 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1308 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1288 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1235 |
| 35 | Calgary International Airport |  | CA | 1203 |
| 36 | Oslo Gardermoen Airport |  | NO | 1177 |
| 37 | Vitoria/Foronda Airport |  | ES | 1171 |
| 38 | Reno/Tahoe International Airport |  | US | 1155 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1148 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1041 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 755 | 21m | 244 km | 3,179.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 442 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 312 | 1h 49m | 1,423 km | 7,657.0 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 311 | 44m | 241 km | 1,291.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 278 | 21m | 250 km | 1,200.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 251 | 1h 14m | 961 km | 4,160.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 243 | 19m | 144 km | 604.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 228 | 1h 49m | 1,304 km | 5,129.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BHL200B | BHL | Aberdeen Dyce Airport (EGPD) | Aberdeen Dyce Airport (EGPD) | 2026-08-18 15:48 UTC | 2026-08-18 16:29 UTC | 41m |
| N511CR |  | Henderson Executive Airport (KHND) | Riverside Airport (KRAL) | 2026-08-18 15:39 UTC | 2026-08-18 16:25 UTC | 45m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-18 07:16 UTC | 2026-08-18 16:23 UTC | 9h 6m |
| N133GX |  | Schaumburg Regional Airport (K06C) | Colonial Acres Airport (4LL8) | 2026-08-18 15:47 UTC | 2026-08-18 16:20 UTC | 33m |
| N8687Q |  | Long Beach (Daugherty Field) Airport (KLGB) | Van Nuys Airport (KVNY) | 2026-08-18 15:23 UTC | 2026-08-18 16:20 UTC | 56m |
| N1377M |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-18 15:36 UTC | 2026-08-18 16:17 UTC | 41m |
| N311LS |  | Georgetown-Scott County Regional Airport (K27K) | Georgetown-Scott County Regional Airport (K27K) | 2026-08-18 16:05 UTC | 2026-08-18 16:15 UTC | 10m |
| N98EG |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-18 14:22 UTC | 2026-08-18 16:15 UTC | 1h 53m |
| LS04 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-18 15:18 UTC | 2026-08-18 16:15 UTC | 57m |
| N84050 |  | Homer Airport (PAHO) | Soldotna Airport (PASX) | 2026-08-18 15:29 UTC | 2026-08-18 16:14 UTC | 44m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-18 14:27 UTC | 2026-08-18 16:12 UTC | 1h 44m |
| MXY123 | MXY | Tampa International Airport (KTPA) | Key West International Airport (KEYW) | 2026-08-18 15:22 UTC | 2026-08-18 16:10 UTC | 47m |
| AUB1319 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-08-18 15:09 UTC | 2026-08-18 16:07 UTC | 57m |
| N245DS |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-18 15:44 UTC | 2026-08-18 16:05 UTC | 21m |
| AFR19BX | Air France | Charles de Gaulle International Airport (LFPG) | Montpellier-Mediterranee Airport (LFMT) | 2026-08-18 15:08 UTC | 2026-08-18 16:02 UTC | 54m |
| N955JA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-18 16:02 UTC | 2026-08-18 16:02 UTC | 0m |
| N493LG |  | CO54 (CO54) | 7CO1 (7CO1) | 2026-08-18 15:42 UTC | 2026-08-18 15:59 UTC | 16m |
| N993AK |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-08-18 15:34 UTC | 2026-08-18 15:57 UTC | 23m |
| PBR615 | PBR | Nanaimo Airport (CYCD) | Alert Bay Airport (CYAL) | 2026-08-18 15:14 UTC | 2026-08-18 15:55 UTC | 41m |
|  |  | Walker County/Bevill Field (KJFX) | Walker County/Bevill Field (KJFX) | 2026-08-18 15:53 UTC | 2026-08-18 15:53 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
