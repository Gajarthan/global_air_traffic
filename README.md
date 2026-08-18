# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_18:39:52_UTC-green)

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

**Latest saved flight:** 2026-08-18 18:39:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 18:39:52 UTC

- **213,027** saved flights
- **67,436** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,027** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,561,400.5 tonnes** estimated CO2 emissions
- **148,486,985 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8450 |
| 2 | SkyWest Airlines | 7632 |
| 3 | EJA | 4147 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3553 |
| 6 | Southwest Airlines | 3400 |
| 7 | Delta Air Lines | 2746 |
| 8 | ENY | 2646 |
| 9 | LATAM Airlines | 2007 |
| 10 | AZU | 1940 |
| 11 | Lufthansa | 1784 |
| 12 | Vueling | 1781 |
| 13 | WIF | 1711 |
| 14 | LXJ | 1680 |
| 15 | easyJet | 1479 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1347 |
| 19 | QLK | 1320 |
| 20 | EJU | 1312 |
| 21 | Alaska Airlines | 1306 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1173 |
| 24 | GLO | 1154 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1096 |
| 28 | JetBlue | 1086 |
| 29 | AEE | 1076 |
| 30 | Wizz Air | 1063 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179964 |
| 2 | 🇪🇸 ES | 13645 |
| 3 | 🇧🇷 BR | 12236 |
| 4 | 🇦🇺 AU | 11964 |
| 5 | 🇨🇦 CA | 11760 |
| 6 | 🇮🇳 IN | 11355 |
| 7 | 🇮🇹 IT | 11225 |
| 8 | 🇩🇪 DE | 10530 |
| 9 | 🇬🇧 GB | 9936 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8627 |
| 12 | 🇫🇷 FR | 8474 |
| 13 | 🇬🇷 GR | 6244 |
| 14 | 🇹🇷 TR | 6114 |
| 15 | 🇲🇽 MX | 5972 |
| 16 | 🇨🇭 CH | 5649 |
| 17 | 🇳🇴 NO | 5307 |
| 18 | 🇲🇾 MY | 3674 |
| 19 | 🇿🇦 ZA | 3604 |
| 20 | 🇵🇱 PL | 3514 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2723 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2317 |
| 27 | 🇲🇦 MA | 2150 |
| 28 | 🇳🇱 NL | 1901 |
| 29 | 🇲🇪 ME | 1838 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4479 |
| 2 | Denver International Airport |  | US | 3474 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2550 |
| 6 | Harry Reid International Airport |  | US | 2381 |
| 7 | Zurich Airport |  | CH | 2221 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2197 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2194 |
| 10 | La Aurora Airport |  | GT | 2070 |
| 11 | El Dorado International Airport |  | CO | 1968 |
| 12 | Chicago O'Hare International Airport |  | US | 1967 |
| 13 | Salt Lake City International Airport |  | US | 1881 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1877 |
| 15 | Congonhas Airport |  | BR | 1784 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Capua Airport |  | IT | 1610 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1609 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1602 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1556 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1483 |
| 25 | Charles de Gaulle International Airport |  | FR | 1470 |
| 26 | Charlotte/Douglas International Airport |  | US | 1434 |
| 27 | Kuala Lumpur International Airport |  | MY | 1355 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1311 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1292 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1241 |
| 35 | Calgary International Airport |  | CA | 1204 |
| 36 | Oslo Gardermoen Airport |  | NO | 1181 |
| 37 | Vitoria/Foronda Airport |  | ES | 1175 |
| 38 | Reno/Tahoe International Airport |  | US | 1157 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1150 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1044 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 758 | 21m | 244 km | 3,191.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 449 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 280 | 21m | 250 km | 1,209.4 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 252 | 1h 14m | 961 km | 4,177.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 229 | 1h 49m | 1,304 km | 5,151.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WMU17 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Hillsdale Municipal Airport (KJYM) | 2026-08-18 17:51 UTC | 2026-08-18 18:39 UTC | 48m |
| N49202 |  | Cable Airport (KCCB) | San Gabriel Valley Airport (KEMT) | 2026-08-18 17:59 UTC | 2026-08-18 18:37 UTC | 37m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-18 18:14 UTC | 2026-08-18 18:32 UTC | 18m |
| N734M |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-08-18 17:29 UTC | 2026-08-18 18:30 UTC | 1h 0m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-18 09:30 UTC | 2026-08-18 18:28 UTC | 8h 57m |
| N440MC |  | Draughon-Miller Central Texas Regional Airport (KTPL) | Addison Airport (KADS) | 2026-08-18 17:59 UTC | 2026-08-18 18:28 UTC | 28m |
| N117TP |  | Phoenix Deer Valley Airport (KDVT) | Glendale Regional Airport (KGEU) | 2026-08-18 18:13 UTC | 2026-08-18 18:26 UTC | 12m |
| KLM877 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Juhu Aerodrome (VAJJ) | 2026-08-18 10:55 UTC | 2026-08-18 18:26 UTC | 7h 30m |
| FFL1275 | FFL | Indianapolis International Airport (KIND) | Darnell's Landings Airport (45TN) | 2026-08-18 17:47 UTC | 2026-08-18 18:24 UTC | 37m |
| CXK674 | CXK | Double Eagle Ii Airport (KAEG) | NM74 (NM74) | 2026-08-18 17:55 UTC | 2026-08-18 18:22 UTC | 27m |
| N4075J |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-18 17:44 UTC | 2026-08-18 18:21 UTC | 36m |
| ABY597 | ABY | Sharjah International Airport (OMSJ) | Hulwan (HE15) | 2026-08-18 15:19 UTC | 2026-08-18 18:20 UTC | 3h 1m |
| BOMR721 | BOM | Waldron Field Nolf Airport (KNWL) | Mustang Beach Airport (KRAS) | 2026-08-18 17:33 UTC | 2026-08-18 18:19 UTC | 46m |
| N44526 |  | Ames Municipal Airport (KAMW) | Ames Municipal Airport (KAMW) | 2026-08-18 17:47 UTC | 2026-08-18 18:17 UTC | 29m |
| SRG375 | SRG | RNAS Lee-On-Solent (EGHF) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-18 17:06 UTC | 2026-08-18 18:14 UTC | 1h 7m |
| N976E |  | Fairbanks International Airport (PAFA) | Indian Mountain Lrrs Airport (PAIM) | 2026-08-18 16:50 UTC | 2026-08-18 18:13 UTC | 1h 23m |
| N407AP |  | Lake Tahoe Airport (KTVL) | Alpine County Airport (KM45) | 2026-08-18 17:43 UTC | 2026-08-18 18:13 UTC | 30m |
| SEKFY | SEK | Koping Airport (ESVQ) | Koping Airport (ESVQ) | 2026-08-18 17:49 UTC | 2026-08-18 18:12 UTC | 22m |
| N251SF |  | Adkins Airport (8IL0) | Willadae Farms Airport (4LL7) | 2026-08-18 17:55 UTC | 2026-08-18 18:11 UTC | 16m |
| LYM4210 | LYM | Denver International Airport (KDEN) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-18 17:44 UTC | 2026-08-18 18:11 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
