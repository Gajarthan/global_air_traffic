# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_00:29:09_UTC-green)

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

**Latest saved flight:** 2026-09-07 00:29:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-07 00:29:09 UTC

- **250,184** saved flights
- **75,146** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **250,184** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,012,150.5 tonnes** estimated CO2 emissions
- **174,617,423 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10014 |
| 2 | SkyWest Airlines | 8736 |
| 3 | EJA | 4832 |
| 4 | IndiGo | 4178 |
| 5 | American Airlines | 4003 |
| 6 | Southwest Airlines | 3717 |
| 7 | Delta Air Lines | 3171 |
| 8 | ENY | 2995 |
| 9 | LATAM Airlines | 2416 |
| 10 | AZU | 2329 |
| 11 | Vueling | 2135 |
| 12 | WIF | 1999 |
| 13 | Lufthansa | 1983 |
| 14 | LXJ | 1940 |
| 15 | easyJet | 1724 |
| 16 | Swiss International | 1680 |
| 17 | AXM | 1628 |
| 18 | EJU | 1609 |
| 19 | QLK | 1605 |
| 20 | United Airlines | 1566 |
| 21 | Alaska Airlines | 1495 |
| 22 | All Nippon Airways | 1466 |
| 23 | WMT | 1419 |
| 24 | GLO | 1392 |
| 25 | PGT | 1374 |
| 26 | VIV | 1372 |
| 27 | Air France | 1361 |
| 28 | Wizz Air | 1360 |
| 29 | AEE | 1228 |
| 30 | JetBlue | 1227 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 207498 |
| 2 | 🇪🇸 ES | 16000 |
| 3 | 🇧🇷 BR | 14612 |
| 4 | 🇦🇺 AU | 14204 |
| 5 | 🇨🇦 CA | 13904 |
| 6 | 🇮🇹 IT | 13702 |
| 7 | 🇮🇳 IN | 13033 |
| 8 | 🇩🇪 DE | 12297 |
| 9 | 🇬🇧 GB | 11735 |
| 10 | 🇨🇴 CO | 10989 |
| 11 | 🇫🇷 FR | 10079 |
| 12 | 🇯🇵 JP | 9867 |
| 13 | 🇹🇷 TR | 7463 |
| 14 | 🇬🇷 GR | 7356 |
| 15 | 🇲🇽 MX | 6915 |
| 16 | 🇨🇭 CH | 6744 |
| 17 | 🇳🇴 NO | 6190 |
| 18 | 🇹🇭 TH | 4504 |
| 19 | 🇲🇾 MY | 4370 |
| 20 | 🇿🇦 ZA | 4307 |
| 21 | 🇵🇱 PL | 4179 |
| 22 | 🇳🇿 NZ | 3417 |
| 23 | 🇵🇭 PH | 3398 |
| 24 | 🇬🇹 GT | 3133 |
| 25 | 🇰🇷 KR | 2898 |
| 26 | 🇭🇷 HR | 2875 |
| 27 | 🇲🇦 MA | 2530 |
| 28 | 🇲🇪 ME | 2352 |
| 29 | 🇳🇱 NL | 2261 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5168 |
| 2 | Denver International Airport |  | US | 4045 |
| 3 | Indira Gandhi International Airport |  | IN | 3041 |
| 4 | Tokyo International Airport |  | JP | 2946 |
| 5 | Guaymaral Airport |  | CO | 2737 |
| 6 | Harry Reid International Airport |  | US | 2660 |
| 7 | Zurich Airport |  | CH | 2618 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2539 |
| 9 | El Dorado International Airport |  | CO | 2533 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2478 |
| 11 | La Aurora Airport |  | GT | 2389 |
| 12 | Salt Lake City International Airport |  | US | 2213 |
| 13 | Chicago O'Hare International Airport |  | US | 2185 |
| 14 | Congonhas Airport |  | BR | 2146 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2058 |
| 16 | Capua Airport |  | IT | 1971 |
| 17 | Madrid Barajas International Airport |  | ES | 1966 |
| 18 | Frankfurt am Main International Airport |  | DE | 1952 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1880 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1823 |
| 21 | Malpensa International Airport |  | IT | 1802 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1756 |
| 23 | Charles de Gaulle International Airport |  | FR | 1752 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1745 |
| 25 | Ninoy Aquino International Airport |  | PH | 1657 |
| 26 | Macau International Airport |  | MO | 1648 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1585 |
| 29 | Barcelona International Airport |  | ES | 1583 |
| 30 | Kuala Lumpur International Airport |  | MY | 1573 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1533 |
| 32 | Viracopos International Airport |  | BR | 1496 |
| 33 | Seattle-Tacoma International Airport |  | US | 1474 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1452 |
| 35 | Don Mueang International Airport |  | TH | 1442 |
| 36 | Calgary International Airport |  | CA | 1440 |
| 37 | Bengaluru International Airport |  | IN | 1432 |
| 38 | Oslo Gardermoen Airport |  | NO | 1409 |
| 39 | Vancouver International Airport |  | CA | 1400 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 929 | 21m | 244 km | 3,911.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 629 | 1h 6m | 770 km | 8,355.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 563 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 398 | 1h 50m | 1,423 km | 9,767.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 388 | 44m | 555 km | 3,715.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 371 | 44m | 241 km | 1,541.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 309 | 26m | 215 km | 1,144.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 289 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 287 | 19m | 144 km | 713.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC308 | Air India | Indira Gandhi International Airport (VIDP) | Naypyidaw Airport (VYEL) | 2026-09-06 22:00 UTC | 2026-09-07 00:29 UTC | 2h 28m |
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-06 17:37 UTC | 2026-09-07 00:19 UTC | 6h 42m |
| EOV | EOV | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-09-06 23:53 UTC | 2026-09-07 00:15 UTC | 22m |
| YQK | YQK | Toowoomba Airport (YTWB) | Boonah Airport (YBOA) | 2026-09-06 23:48 UTC | 2026-09-07 00:11 UTC | 22m |
| N570D |  | Mbs International Airport (KMBS) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-06 22:41 UTC | 2026-09-07 00:05 UTC | 1h 23m |
| JZA784 | JZA | Toronto Pearson International Airport (CYYZ) | Fort Meade Executive Airport (KFME) | 2026-09-06 22:48 UTC | 2026-09-07 00:03 UTC | 1h 14m |
| MXY881 | MXY | Long Island Mac Arthur Airport (KISP) | 5MD7 (5MD7) | 2026-09-06 22:58 UTC | 2026-09-07 00:03 UTC | 1h 5m |
| N1932H |  | Spencer Municipal Airport (KSPW) | Iowa City Municipal Airport (KIOW) | 2026-09-06 23:03 UTC | 2026-09-07 00:01 UTC | 57m |
| N62JB |  | Truckee-Tahoe Airport (KTRK) | Reno/Tahoe International Airport (KRNO) | 2026-09-06 23:46 UTC | 2026-09-07 00:00 UTC | 13m |
| RXA6518 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Cudal Airport (YCUA) | 2026-09-06 23:20 UTC | 2026-09-06 23:55 UTC | 35m |
| SH461 |  | Port Augusta Airport (YPAG) | Wirrealpa Airport (YWPA) | 2026-09-06 23:25 UTC | 2026-09-06 23:51 UTC | 26m |
| AER180 | AER | Ted Stevens Anchorage International Airport (PANC) | Igiugig Airport (PAIG) | 2026-09-06 22:52 UTC | 2026-09-06 23:49 UTC | 57m |
| QLK320D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-09-06 23:20 UTC | 2026-09-06 23:49 UTC | 28m |
| MXY2855 | MXY | Portsmouth International At Pease Airport (KPSM) | Raleigh-Durham International Airport (KRDU) | 2026-09-06 22:05 UTC | 2026-09-06 23:46 UTC | 1h 40m |
| EJA868 | EJA | Monterey Regional Airport (KMRY) | Sedona Airport (KSEZ) | 2026-09-06 22:31 UTC | 2026-09-06 23:39 UTC | 1h 7m |
| UTY3352 | UTY | Brisbane International Airport (YBBN) | Miles Airport (YMLS) | 2026-09-06 23:07 UTC | 2026-09-06 23:39 UTC | 31m |
| LPE2213 | LPE | Jorge Chavez International Airport (SPJC) | Pacasmayo Airport (SPYO) | 2026-09-06 22:49 UTC | 2026-09-06 23:37 UTC | 47m |
| CGPCI | CGP | Vancouver International Airport (CYVR) | Grand Forks Airport (CZGF) | 2026-09-06 22:42 UTC | 2026-09-06 23:35 UTC | 52m |
|  |  | Victoria International Airport (CYYJ) | Tipella Airport (CBB7) | 2026-09-06 23:01 UTC | 2026-09-06 23:34 UTC | 32m |
| QLK28D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-09-06 23:05 UTC | 2026-09-06 23:33 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
