# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_15:57:56_UTC-green)

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

**Latest saved flight:** 2026-08-18 15:57:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 15:57:56 UTC

- **212,367** saved flights
- **67,292** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **212,367** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,552,871.4 tonnes** estimated CO2 emissions
- **147,992,546 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8419 |
| 2 | SkyWest Airlines | 7608 |
| 3 | EJA | 4126 |
| 4 | IndiGo | 3636 |
| 5 | American Airlines | 3539 |
| 6 | Southwest Airlines | 3387 |
| 7 | Delta Air Lines | 2735 |
| 8 | ENY | 2631 |
| 9 | LATAM Airlines | 2004 |
| 10 | AZU | 1931 |
| 11 | Lufthansa | 1780 |
| 12 | Vueling | 1775 |
| 13 | WIF | 1706 |
| 14 | LXJ | 1675 |
| 15 | easyJet | 1471 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1390 |
| 18 | United Airlines | 1343 |
| 19 | QLK | 1320 |
| 20 | EJU | 1305 |
| 21 | Alaska Airlines | 1303 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1168 |
| 24 | PGT | 1149 |
| 25 | GLO | 1148 |
| 26 | Air France | 1146 |
| 27 | WMT | 1092 |
| 28 | JetBlue | 1080 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1058 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179351 |
| 2 | 🇪🇸 ES | 13611 |
| 3 | 🇧🇷 BR | 12198 |
| 4 | 🇦🇺 AU | 11962 |
| 5 | 🇨🇦 CA | 11729 |
| 6 | 🇮🇳 IN | 11333 |
| 7 | 🇮🇹 IT | 11174 |
| 8 | 🇩🇪 DE | 10506 |
| 9 | 🇬🇧 GB | 9908 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8560 |
| 12 | 🇫🇷 FR | 8441 |
| 13 | 🇬🇷 GR | 6217 |
| 14 | 🇹🇷 TR | 6087 |
| 15 | 🇲🇽 MX | 5946 |
| 16 | 🇨🇭 CH | 5645 |
| 17 | 🇳🇴 NO | 5290 |
| 18 | 🇲🇾 MY | 3673 |
| 19 | 🇿🇦 ZA | 3588 |
| 20 | 🇵🇱 PL | 3508 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2719 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2308 |
| 27 | 🇲🇦 MA | 2141 |
| 28 | 🇳🇱 NL | 1894 |
| 29 | 🇲🇪 ME | 1829 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4457 |
| 2 | Denver International Airport |  | US | 3461 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2586 |
| 5 | Guaymaral Airport |  | CO | 2538 |
| 6 | Harry Reid International Airport |  | US | 2379 |
| 7 | Zurich Airport |  | CH | 2219 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2188 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2186 |
| 10 | La Aurora Airport |  | GT | 2066 |
| 11 | Chicago O'Hare International Airport |  | US | 1960 |
| 12 | El Dorado International Airport |  | CO | 1956 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1876 |
| 14 | Salt Lake City International Airport |  | US | 1875 |
| 15 | Congonhas Airport |  | BR | 1773 |
| 16 | Frankfurt am Main International Airport |  | DE | 1734 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1600 |
| 19 | Capua Airport |  | IT | 1600 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1598 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1556 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1473 |
| 25 | Charles de Gaulle International Airport |  | FR | 1459 |
| 26 | Charlotte/Douglas International Airport |  | US | 1428 |
| 27 | Kuala Lumpur International Airport |  | MY | 1354 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1308 |
| 30 | Bengaluru International Airport |  | IN | 1303 |
| 31 | Barcelona International Airport |  | ES | 1287 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1235 |
| 35 | Calgary International Airport |  | CA | 1203 |
| 36 | Oslo Gardermoen Airport |  | NO | 1176 |
| 37 | Vitoria/Foronda Airport |  | ES | 1171 |
| 38 | Reno/Tahoe International Airport |  | US | 1153 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1147 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1040 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 754 | 21m | 244 km | 3,174.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 480 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 440 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 311 | 1h 49m | 1,423 km | 7,632.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 311 | 44m | 241 km | 1,291.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 291 | 22m | 55 km | 276.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 277 | 21m | 250 km | 1,196.5 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 263 | 1h 38m | 1,156 km | 5,246.8 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 259 | 27m | 215 km | 959.2 t |
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
| N993AK |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-08-18 15:34 UTC | 2026-08-18 15:57 UTC | 23m |
| ANE2442 | ANE | Valencia Airport (LEVC) | Palma De Mallorca Airport (LEPA) | 2026-08-18 14:49 UTC | 2026-08-18 15:51 UTC | 1h 1m |
| EMB201 | EMB | Fazenda Cambuhy Airport (SDMY) | Usina de Jose Bonifacio Airport (SNHJ) | 2026-08-18 15:36 UTC | 2026-08-18 15:51 UTC | 14m |
| TGBEF | TGB | La Aurora Airport (MGGT) | San Jose Airport (MGSJ) | 2026-08-18 15:28 UTC | 2026-08-18 15:46 UTC | 17m |
| N251SR |  | Spicewood Airport (K88R) | Austin Executive Airport (KEDC) | 2026-08-18 15:29 UTC | 2026-08-18 15:44 UTC | 14m |
| N216AR |  | Laurence G Hanscom Field (KBED) | Patrick Leahy Burlington International Airport (KBTV) | 2026-08-18 14:39 UTC | 2026-08-18 15:42 UTC | 1h 2m |
| CGIZI | CGI | Kitchener / Waterloo Airport (CYKF) | Palmerston Airport (CPR3) | 2026-08-18 14:46 UTC | 2026-08-18 15:42 UTC | 56m |
| N439H |  | General Edward Lawrence Logan International Airport (KBOS) | Laguardia Airport (KLGA) | 2026-08-18 14:18 UTC | 2026-08-18 15:37 UTC | 1h 18m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-18 15:14 UTC | 2026-08-18 15:33 UTC | 18m |
| VAR485 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-18 15:14 UTC | 2026-08-18 15:33 UTC | 19m |
| AWH92B | AWH | Munster Osnabruck Airport (EDDG) | Brussels Airport (EBBR) | 2026-08-18 14:48 UTC | 2026-08-18 15:33 UTC | 45m |
| N9455U |  | Yates Airport (IL29) | Yates Airport (IL29) | 2026-08-18 15:33 UTC | 2026-08-18 15:33 UTC | 0m |
| RYR49RT | Ryanair | M. R. Stefanik Airport (LZIB) | Palma De Mallorca Airport (LEPA) | 2026-08-18 13:36 UTC | 2026-08-18 15:31 UTC | 1h 55m |
| N163EA |  | Nephi Municipal Airport (KU14) | Provo Municipal Airport (KPVU) | 2026-08-18 15:11 UTC | 2026-08-18 15:28 UTC | 16m |
| N202WG |  | Indiana County/Jimmy Stewart Field (KIDI) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-08-18 15:16 UTC | 2026-08-18 15:26 UTC | 10m |
| TOPCT25 | TOP | Offutt Afb Airport (KOFF) | SD47 (SD47) | 2026-08-18 14:29 UTC | 2026-08-18 15:23 UTC | 54m |
| N666AS |  | Uelzen Airport (EDVU) | Fassberg Airport (ETHS) | 2026-08-18 15:10 UTC | 2026-08-18 15:22 UTC | 12m |
| N423LL |  | Jugtown Mountain Airport (2NJ1) | Herr Brothers Airport (NJ95) | 2026-08-18 15:02 UTC | 2026-08-18 15:22 UTC | 20m |
| N84809 |  | Denton Enterprise Airport (KDTO) | Jones Field (KF00) | 2026-08-18 14:47 UTC | 2026-08-18 15:21 UTC | 34m |
| N704UW |  | Aurora Municipal Airport (KARR) | Wade Airport (56LL) | 2026-08-18 14:48 UTC | 2026-08-18 15:20 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
