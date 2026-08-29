# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_15:13:54_UTC-green)

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

**Latest saved flight:** 2026-08-29 15:13:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 15:13:54 UTC

- **240,914** saved flights
- **73,138** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,914** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,900,078.1 tonnes** estimated CO2 emissions
- **168,120,469 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9672 |
| 2 | SkyWest Airlines | 8445 |
| 3 | EJA | 4660 |
| 4 | IndiGo | 4067 |
| 5 | American Airlines | 3880 |
| 6 | Southwest Airlines | 3624 |
| 7 | Delta Air Lines | 3069 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2313 |
| 10 | AZU | 2240 |
| 11 | Vueling | 2068 |
| 12 | Lufthansa | 1941 |
| 13 | WIF | 1909 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1680 |
| 16 | Swiss International | 1624 |
| 17 | AXM | 1597 |
| 18 | EJU | 1543 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1513 |
| 21 | Alaska Airlines | 1439 |
| 22 | All Nippon Airways | 1429 |
| 23 | WMT | 1356 |
| 24 | GLO | 1345 |
| 25 | VIV | 1322 |
| 26 | Air France | 1318 |
| 27 | PGT | 1316 |
| 28 | Wizz Air | 1297 |
| 29 | AEE | 1192 |
| 30 | JetBlue | 1191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199519 |
| 2 | 🇪🇸 ES | 15496 |
| 3 | 🇧🇷 BR | 14053 |
| 4 | 🇦🇺 AU | 13676 |
| 5 | 🇨🇦 CA | 13392 |
| 6 | 🇮🇹 IT | 13179 |
| 7 | 🇮🇳 IN | 12660 |
| 8 | 🇩🇪 DE | 11905 |
| 9 | 🇬🇧 GB | 11391 |
| 10 | 🇨🇴 CO | 10343 |
| 11 | 🇫🇷 FR | 9716 |
| 12 | 🇯🇵 JP | 9686 |
| 13 | 🇹🇷 TR | 7151 |
| 14 | 🇬🇷 GR | 7099 |
| 15 | 🇲🇽 MX | 6657 |
| 16 | 🇨🇭 CH | 6459 |
| 17 | 🇳🇴 NO | 5949 |
| 18 | 🇹🇭 TH | 4380 |
| 19 | 🇲🇾 MY | 4278 |
| 20 | 🇿🇦 ZA | 4217 |
| 21 | 🇵🇱 PL | 4041 |
| 22 | 🇳🇿 NZ | 3310 |
| 23 | 🇵🇭 PH | 3309 |
| 24 | 🇬🇹 GT | 3031 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2783 |
| 27 | 🇲🇦 MA | 2433 |
| 28 | 🇲🇪 ME | 2252 |
| 29 | 🇳🇱 NL | 2183 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4968 |
| 2 | Denver International Airport |  | US | 3882 |
| 3 | Indira Gandhi International Airport |  | IN | 2946 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2696 |
| 6 | Harry Reid International Airport |  | US | 2557 |
| 7 | Zurich Airport |  | CH | 2526 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2463 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2402 |
| 10 | El Dorado International Airport |  | CO | 2341 |
| 11 | La Aurora Airport |  | GT | 2311 |
| 12 | Chicago O'Hare International Airport |  | US | 2143 |
| 13 | Salt Lake City International Airport |  | US | 2121 |
| 14 | Congonhas Airport |  | BR | 2054 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1998 |
| 16 | Frankfurt am Main International Airport |  | DE | 1909 |
| 17 | Capua Airport |  | IT | 1899 |
| 18 | Madrid Barajas International Airport |  | ES | 1898 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1812 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1769 |
| 21 | Malpensa International Airport |  | IT | 1723 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 24 | Charles de Gaulle International Airport |  | FR | 1687 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1607 |
| 27 | Kuala Lumpur International Airport |  | MY | 1545 |
| 28 | Charlotte/Douglas International Airport |  | US | 1542 |
| 29 | Barcelona International Airport |  | ES | 1536 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1533 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1456 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1410 |
| 34 | Bengaluru International Airport |  | IN | 1407 |
| 35 | Seattle-Tacoma International Airport |  | US | 1404 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1402 |
| 37 | Calgary International Airport |  | CA | 1381 |
| 38 | Oslo Gardermoen Airport |  | NO | 1353 |
| 39 | Vancouver International Airport |  | CA | 1324 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1317 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1092 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 886 | 21m | 244 km | 3,730.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 620 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 612 | 24m | 225 km | 2,374.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 379 | 1h 50m | 1,423 km | 9,301.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 367 | 44m | 555 km | 3,514.2 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 350 | 44m | 241 km | 1,453.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 328 | 24m | 218 km | 1,235.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 321 | 1h 40m | 1,156 km | 6,403.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 294 | 26m | 215 km | 1,088.9 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 279 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 279 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 275 | 1h 14m | 961 km | 4,558.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 271 | 19m | 144 km | 674.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 258 | 1h 50m | 1,304 km | 5,804.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DKAGB | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-08-29 14:58 UTC | 2026-08-29 15:13 UTC | 15m |
| ACA167 | Air Canada | Toronto Pearson International Airport (CYYZ) | CCN4 (CCN4) | 2026-08-29 14:43 UTC | 2026-08-29 15:06 UTC | 22m |
| N9022J |  | Reno/Tahoe International Airport (KRNO) | NV44 (NV44) | 2026-08-29 14:52 UTC | 2026-08-29 15:05 UTC | 13m |
| QTR8464 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-29 07:38 UTC | 2026-08-29 15:05 UTC | 7h 27m |
| N13587 |  | Medina Municipal Airport (K1G5) | Seneca County Airport (K16G) | 2026-08-29 14:18 UTC | 2026-08-29 15:01 UTC | 42m |
| CXK305 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-29 14:13 UTC | 2026-08-29 14:58 UTC | 45m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-29 14:23 UTC | 2026-08-29 14:55 UTC | 31m |
| N4363T |  | David Wayne Hooks Memorial Airport (KDWH) | Navasota Municipal Airport (K60R) | 2026-08-29 14:28 UTC | 2026-08-29 14:50 UTC | 21m |
| N825JC |  | 2OL2 (2OL2) | Haskell Airport (K2K9) | 2026-08-29 14:10 UTC | 2026-08-29 14:49 UTC | 38m |
| NSZ2CP | NSZ | Malaga Airport (LEMG) | Stockholm-Arlanda Airport (ESSA) | 2026-08-29 11:01 UTC | 2026-08-29 14:47 UTC | 3h 46m |
| N43MJ |  | Allen Airstrip (3NJ9) | Flying W Airport (KN14) | 2026-08-29 14:23 UTC | 2026-08-29 14:46 UTC | 22m |
| N259SC |  | French Valley Airport (KF70) | Crystal Airport (46CN) | 2026-08-29 14:26 UTC | 2026-08-29 14:45 UTC | 19m |
| N817FG |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-08-29 14:30 UTC | 2026-08-29 14:42 UTC | 11m |
| SD1 |  | Wiener Neustadt West Airport (LOXN) | Wiener Neustadt West Airport (LOXN) | 2026-08-29 14:20 UTC | 2026-08-29 14:40 UTC | 19m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-29 14:27 UTC | 2026-08-29 14:40 UTC | 13m |
| CFXCM | CFX | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-08-29 14:13 UTC | 2026-08-29 14:38 UTC | 24m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-08-29 14:24 UTC | 2026-08-29 14:36 UTC | 11m |
| JME633C | JME | Bremen Airport (EDDW) | Liverpool John Lennon Airport (EGGP) | 2026-08-29 13:20 UTC | 2026-08-29 14:35 UTC | 1h 14m |
| N608AB |  | Fort Worth Meacham International Airport (KFTW) | 5TA4 (5TA4) | 2026-08-29 13:49 UTC | 2026-08-29 14:34 UTC | 45m |
| DFINA | DFI | Saulgau Airport (EDTU) | Saulgau Airport (EDTU) | 2026-08-29 13:28 UTC | 2026-08-29 14:34 UTC | 1h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
