# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_15:36:21_UTC-green)

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

**Latest saved flight:** 2026-08-25 15:36:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 15:36:21 UTC

- **235,482** saved flights
- **72,018** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,482** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,836,573.0 tonnes** estimated CO2 emissions
- **164,439,015 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9442 |
| 2 | SkyWest Airlines | 8305 |
| 3 | EJA | 4559 |
| 4 | IndiGo | 3983 |
| 5 | American Airlines | 3819 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2997 |
| 8 | ENY | 2857 |
| 9 | LATAM Airlines | 2263 |
| 10 | AZU | 2194 |
| 11 | Vueling | 2018 |
| 12 | Lufthansa | 1916 |
| 13 | WIF | 1874 |
| 14 | LXJ | 1845 |
| 15 | easyJet | 1644 |
| 16 | Swiss International | 1584 |
| 17 | AXM | 1575 |
| 18 | EJU | 1508 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1487 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1313 |
| 24 | GLO | 1312 |
| 25 | VIV | 1297 |
| 26 | PGT | 1283 |
| 27 | Air France | 1280 |
| 28 | Wizz Air | 1255 |
| 29 | AEE | 1169 |
| 30 | JetBlue | 1164 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195480 |
| 2 | 🇪🇸 ES | 15139 |
| 3 | 🇧🇷 BR | 13755 |
| 4 | 🇦🇺 AU | 13338 |
| 5 | 🇨🇦 CA | 13010 |
| 6 | 🇮🇹 IT | 12834 |
| 7 | 🇮🇳 IN | 12403 |
| 8 | 🇩🇪 DE | 11615 |
| 9 | 🇬🇧 GB | 11110 |
| 10 | 🇨🇴 CO | 9949 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9460 |
| 13 | 🇹🇷 TR | 6984 |
| 14 | 🇬🇷 GR | 6940 |
| 15 | 🇲🇽 MX | 6535 |
| 16 | 🇨🇭 CH | 6303 |
| 17 | 🇳🇴 NO | 5834 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4214 |
| 20 | 🇿🇦 ZA | 4131 |
| 21 | 🇵🇱 PL | 3930 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2949 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2709 |
| 27 | 🇲🇦 MA | 2388 |
| 28 | 🇲🇪 ME | 2189 |
| 29 | 🇳🇱 NL | 2116 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4878 |
| 2 | Denver International Airport |  | US | 3802 |
| 3 | Indira Gandhi International Airport |  | IN | 2876 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2682 |
| 6 | Harry Reid International Airport |  | US | 2522 |
| 7 | Zurich Airport |  | CH | 2469 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2401 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2359 |
| 10 | La Aurora Airport |  | GT | 2248 |
| 11 | El Dorado International Airport |  | CO | 2226 |
| 12 | Chicago O'Hare International Airport |  | US | 2121 |
| 13 | Salt Lake City International Airport |  | US | 2071 |
| 14 | Congonhas Airport |  | BR | 2006 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1876 |
| 17 | Madrid Barajas International Airport |  | ES | 1851 |
| 18 | Capua Airport |  | IT | 1850 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1773 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1735 |
| 21 | Malpensa International Airport |  | IT | 1688 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1668 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1640 |
| 25 | Macau International Airport |  | MO | 1612 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1517 |
| 29 | Barcelona International Airport |  | ES | 1490 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1462 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1423 |
| 32 | Viracopos International Airport |  | BR | 1404 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Seattle-Tacoma International Airport |  | US | 1379 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1378 |
| 36 | Don Mueang International Airport |  | TH | 1366 |
| 37 | Calgary International Airport |  | CA | 1346 |
| 38 | Oslo Gardermoen Airport |  | NO | 1322 |
| 39 | Vancouver International Airport |  | CA | 1285 |
| 40 | O. R. Tambo International Airport |  | ZA | 1284 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1087 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 863 | 21m | 244 km | 3,633.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 592 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 528 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 389 | 27m | 275 km | 1,843.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 364 | 1h 50m | 1,423 km | 8,933.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 341 | 44m | 555 km | 3,265.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 332 | 21m | 250 km | 1,434.0 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 310 | 1h 40m | 1,156 km | 6,184.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 289 | 27m | 215 km | 1,070.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 252 | 1h 50m | 1,304 km | 5,669.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N969TT |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-08-25 15:21 UTC | 2026-08-25 15:36 UTC | 14m |
| FISTA21 | FIS | 2TX3 (2TX3) | Chaparrosa Ranch Airport (72TE) | 2026-08-25 15:18 UTC | 2026-08-25 15:34 UTC | 15m |
| HSOPK4 | HSO | Husum-Schwesing Airport (EDXJ) | Westerland Sylt Airport (EDXW) | 2026-08-25 14:59 UTC | 2026-08-25 15:33 UTC | 33m |
| N5309F |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-25 15:13 UTC | 2026-08-25 15:29 UTC | 16m |
| N1100L |  | City Of Slaton/Larry T Neal Memorial Airport (KF49) | City Of Slaton/Larry T Neal Memorial Airport (KF49) | 2026-08-25 14:20 UTC | 2026-08-25 15:25 UTC | 1h 5m |
| FHNTS | FHN | Nantes Atlantique Airport (LFRS) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-25 14:54 UTC | 2026-08-25 15:25 UTC | 30m |
| LYM5910 | LYM | Alliance Municipal Airport (KAIA) | Alliance Municipal Airport (KAIA) | 2026-08-25 15:07 UTC | 2026-08-25 15:25 UTC | 17m |
| N84400 |  | Dekalb-Peachtree Airport (KPDK) | Barrow County Airport (KWDR) | 2026-08-25 14:34 UTC | 2026-08-25 15:22 UTC | 47m |
| UAL246 | United Airlines | Chicago O'Hare International Airport (KORD) | San Francisco International Airport (KSFO) | 2026-08-25 11:20 UTC | 2026-08-25 15:21 UTC | 4h 1m |
| N164BJ |  | Mahlon Sweet Field (KEUG) | Strauch Field (OR47) | 2026-08-25 15:19 UTC | 2026-08-25 15:21 UTC | 1m |
| RTV2M | RTV | Vilar Da Luz Airport (LPVL) | Vila Real Airport (LPVR) | 2026-08-25 14:38 UTC | 2026-08-25 15:20 UTC | 42m |
| N502HA |  | IA17 (IA17) | Northeast Iowa Regional Airport (KCCY) | 2026-08-25 15:04 UTC | 2026-08-25 15:20 UTC | 16m |
| HBZYU | HBZ | Bex Airport (LSGB) | Bex Airport (LSGB) | 2026-08-25 14:38 UTC | 2026-08-25 15:18 UTC | 40m |
| 3AMAX |  | Calvi-Sainte-Catherine Airport (LFKC) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-25 14:39 UTC | 2026-08-25 15:18 UTC | 39m |
| SHERPA6 | SHE | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-08-25 14:56 UTC | 2026-08-25 15:17 UTC | 20m |
| N1468T |  | Medina Municipal Airport (K1G5) | Somerset Airport (KSMQ) | 2026-08-25 13:01 UTC | 2026-08-25 15:17 UTC | 2h 15m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-25 14:02 UTC | 2026-08-25 15:17 UTC | 1h 14m |
| N779RJ |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-08-25 14:40 UTC | 2026-08-25 15:17 UTC | 36m |
| ZUMNT | ZUM | Lanseria Airport (FALA) | Lanseria Airport (FALA) | 2026-08-25 14:58 UTC | 2026-08-25 15:17 UTC | 18m |
| N19364 |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-08-25 14:47 UTC | 2026-08-25 15:17 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
