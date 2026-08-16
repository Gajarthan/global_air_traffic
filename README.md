# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_20:48:34_UTC-green)

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

**Latest saved flight:** 2026-08-16 20:48:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 20:48:34 UTC

- **206,166** saved flights
- **65,752** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,166** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,479,198.4 tonnes** estimated CO2 emissions
- **143,721,644 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8137 |
| 2 | SkyWest Airlines | 7410 |
| 3 | EJA | 4003 |
| 4 | IndiGo | 3522 |
| 5 | American Airlines | 3436 |
| 6 | Southwest Airlines | 3318 |
| 7 | Delta Air Lines | 2651 |
| 8 | ENY | 2571 |
| 9 | LATAM Airlines | 1935 |
| 10 | AZU | 1866 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1708 |
| 13 | WIF | 1656 |
| 14 | LXJ | 1628 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1374 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1302 |
| 19 | Alaska Airlines | 1278 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1132 |
| 24 | GLO | 1113 |
| 25 | Air France | 1103 |
| 26 | PGT | 1100 |
| 27 | JetBlue | 1056 |
| 28 | AEE | 1052 |
| 29 | WMT | 1039 |
| 30 | CXK | 1015 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175210 |
| 2 | 🇪🇸 ES | 13178 |
| 3 | 🇧🇷 BR | 11812 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11379 |
| 6 | 🇮🇳 IN | 10990 |
| 7 | 🇮🇹 IT | 10751 |
| 8 | 🇩🇪 DE | 10205 |
| 9 | 🇬🇧 GB | 9619 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇨🇴 CO | 8194 |
| 12 | 🇫🇷 FR | 8165 |
| 13 | 🇬🇷 GR | 6068 |
| 14 | 🇹🇷 TR | 5845 |
| 15 | 🇲🇽 MX | 5798 |
| 16 | 🇨🇭 CH | 5510 |
| 17 | 🇳🇴 NO | 5132 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3401 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2620 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2207 |
| 27 | 🇲🇦 MA | 2080 |
| 28 | 🇳🇱 NL | 1838 |
| 29 | 🇲🇪 ME | 1737 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4336 |
| 2 | Denver International Airport |  | US | 3368 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Guaymaral Airport |  | CO | 2494 |
| 5 | Indira Gandhi International Airport |  | IN | 2494 |
| 6 | Harry Reid International Airport |  | US | 2327 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 8 | Zurich Airport |  | CH | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2143 |
| 10 | La Aurora Airport |  | GT | 1998 |
| 11 | Chicago O'Hare International Airport |  | US | 1912 |
| 12 | El Dorado International Airport |  | CO | 1884 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1841 |
| 14 | Salt Lake City International Airport |  | US | 1825 |
| 15 | Congonhas Airport |  | BR | 1722 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1617 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1573 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1569 |
| 20 | Capua Airport |  | IT | 1567 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1491 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1407 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1275 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1242 |
| 32 | Barcelona International Airport |  | ES | 1227 |
| 33 | Seattle-Tacoma International Airport |  | US | 1221 |
| 34 | Viracopos International Airport |  | BR | 1195 |
| 35 | Calgary International Airport |  | CA | 1167 |
| 36 | Reno/Tahoe International Airport |  | US | 1140 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Tenerife Norte Airport |  | ES | 1104 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 469 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 398 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 250 | 19m | 99 km | 428.2 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 224 | 28m | 152 km | 585.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N901ST |  | 75IS (75IS) | Staton Airport (4LL1) | 2026-08-16 20:35 UTC | 2026-08-16 20:48 UTC | 13m |
| AFR52VY | Air France | Charles de Gaulle International Airport (LFPG) | Vilar Da Luz Airport (LPVL) | 2026-08-16 18:53 UTC | 2026-08-16 20:44 UTC | 1h 50m |
| TAP76EN | TAP Air Portugal | Oslo Gardermoen Airport (ENGM) | Sintra Airport (LPST) | 2026-08-16 17:03 UTC | 2026-08-16 20:44 UTC | 3h 41m |
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 20:06 UTC | 2026-08-16 20:42 UTC | 35m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 19:28 UTC | 2026-08-16 20:32 UTC | 1h 3m |
| N878CC |  | Centennial Airport (KAPA) | Centennial Airport (KAPA) | 2026-08-16 19:55 UTC | 2026-08-16 20:29 UTC | 33m |
| ES801 |  | Castle Airport (KMER) | Sacramento Mather Airport (KMHR) | 2026-08-16 19:41 UTC | 2026-08-16 20:24 UTC | 42m |
| N616EM |  | Victoria Regional Airport (KVCT) | Addison Airport (KADS) | 2026-08-16 19:16 UTC | 2026-08-16 20:21 UTC | 1h 4m |
| N938AX |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-16 19:33 UTC | 2026-08-16 20:21 UTC | 47m |
| N874EB |  | Bend Municipal Airport (KBDN) | Josephine Ranch Airport (2ID3) | 2026-08-16 18:32 UTC | 2026-08-16 20:15 UTC | 1h 42m |
| EJA240 | EJA | Quonset State Airport (KOQU) | Northeast Philadelphia Airport (KPNE) | 2026-08-16 19:27 UTC | 2026-08-16 20:14 UTC | 47m |
| CGMPY | CGM | Edmonton International Airport (CYEG) | Regina Beach Airport (CKL9) | 2026-08-16 18:52 UTC | 2026-08-16 20:14 UTC | 1h 21m |
| CGMPE | CGM | High River Airport (CEN4) | Lumsden (Colhoun) Airport (CKH8) | 2026-08-16 18:59 UTC | 2026-08-16 20:14 UTC | 1h 14m |
| N9758H |  | Tangier Island Airport (KTGI) | Central Jersey Regional Airport (K47N) | 2026-08-16 18:55 UTC | 2026-08-16 20:12 UTC | 1h 16m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-08-16 19:56 UTC | 2026-08-16 20:09 UTC | 13m |
| N53540 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-16 19:37 UTC | 2026-08-16 20:07 UTC | 30m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 19:53 UTC | 2026-08-16 20:06 UTC | 12m |
| JTZ814 | JTZ | Pontotoc County Airport (K22M) | Travis Airport (LA63) | 2026-08-16 19:41 UTC | 2026-08-16 20:06 UTC | 25m |
| N525HM |  | Gillespie County Airport (KT82) | Panola County-Sharpe Field (K4F2) | 2026-08-16 19:15 UTC | 2026-08-16 20:05 UTC | 49m |
| EJA871 | EJA | Oxnard Airport (KOXR) | Moffett Federal Airfield (KNUQ) | 2026-08-16 19:22 UTC | 2026-08-16 20:01 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
