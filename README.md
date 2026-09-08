# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_14:52:18_UTC-green)

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

**Latest saved flight:** 2026-09-08 14:52:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 14:52:18 UTC

- **251,548** saved flights
- **75,421** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,548** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,029,078.6 tonnes** estimated CO2 emissions
- **175,598,758 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10065 |
| 2 | SkyWest Airlines | 8787 |
| 3 | EJA | 4860 |
| 4 | IndiGo | 4216 |
| 5 | American Airlines | 4019 |
| 6 | Southwest Airlines | 3723 |
| 7 | Delta Air Lines | 3182 |
| 8 | ENY | 3002 |
| 9 | LATAM Airlines | 2420 |
| 10 | AZU | 2336 |
| 11 | Vueling | 2144 |
| 12 | WIF | 2018 |
| 13 | Lufthansa | 1990 |
| 14 | LXJ | 1965 |
| 15 | easyJet | 1729 |
| 16 | Swiss International | 1689 |
| 17 | AXM | 1629 |
| 18 | QLK | 1619 |
| 19 | EJU | 1614 |
| 20 | United Airlines | 1571 |
| 21 | Alaska Airlines | 1501 |
| 22 | All Nippon Airways | 1474 |
| 23 | WMT | 1429 |
| 24 | GLO | 1395 |
| 25 | PGT | 1381 |
| 26 | VIV | 1378 |
| 27 | Air France | 1372 |
| 28 | Wizz Air | 1370 |
| 29 | AEE | 1231 |
| 30 | JetBlue | 1231 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208589 |
| 2 | 🇪🇸 ES | 16075 |
| 3 | 🇧🇷 BR | 14656 |
| 4 | 🇦🇺 AU | 14315 |
| 5 | 🇨🇦 CA | 13954 |
| 6 | 🇮🇹 IT | 13779 |
| 7 | 🇮🇳 IN | 13162 |
| 8 | 🇩🇪 DE | 12356 |
| 9 | 🇬🇧 GB | 11789 |
| 10 | 🇨🇴 CO | 11082 |
| 11 | 🇫🇷 FR | 10124 |
| 12 | 🇯🇵 JP | 9906 |
| 13 | 🇹🇷 TR | 7525 |
| 14 | 🇬🇷 GR | 7391 |
| 15 | 🇲🇽 MX | 6944 |
| 16 | 🇨🇭 CH | 6790 |
| 17 | 🇳🇴 NO | 6233 |
| 18 | 🇹🇭 TH | 4537 |
| 19 | 🇲🇾 MY | 4379 |
| 20 | 🇿🇦 ZA | 4319 |
| 21 | 🇵🇱 PL | 4195 |
| 22 | 🇳🇿 NZ | 3432 |
| 23 | 🇵🇭 PH | 3412 |
| 24 | 🇬🇹 GT | 3139 |
| 25 | 🇰🇷 KR | 2907 |
| 26 | 🇭🇷 HR | 2891 |
| 27 | 🇲🇦 MA | 2541 |
| 28 | 🇲🇪 ME | 2367 |
| 29 | 🇳🇱 NL | 2270 |
| 30 | 🇮🇩 ID | 2153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5191 |
| 2 | Denver International Airport |  | US | 4073 |
| 3 | Indira Gandhi International Airport |  | IN | 3059 |
| 4 | Tokyo International Airport |  | JP | 2955 |
| 5 | Guaymaral Airport |  | CO | 2741 |
| 6 | Harry Reid International Airport |  | US | 2674 |
| 7 | Zurich Airport |  | CH | 2633 |
| 8 | El Dorado International Airport |  | CO | 2555 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2550 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2487 |
| 11 | La Aurora Airport |  | GT | 2394 |
| 12 | Salt Lake City International Airport |  | US | 2225 |
| 13 | Chicago O'Hare International Airport |  | US | 2191 |
| 14 | Congonhas Airport |  | BR | 2150 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2070 |
| 16 | Capua Airport |  | IT | 1986 |
| 17 | Madrid Barajas International Airport |  | ES | 1978 |
| 18 | Frankfurt am Main International Airport |  | DE | 1960 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1883 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1829 |
| 21 | Malpensa International Airport |  | IT | 1809 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 23 | Charles de Gaulle International Airport |  | FR | 1763 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1751 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1668 |
| 26 | Ninoy Aquino International Airport |  | PH | 1666 |
| 27 | Macau International Airport |  | MO | 1652 |
| 28 | Barcelona International Airport |  | ES | 1588 |
| 29 | Charlotte/Douglas International Airport |  | US | 1587 |
| 30 | Kuala Lumpur International Airport |  | MY | 1577 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1542 |
| 32 | Viracopos International Airport |  | BR | 1501 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1460 |
| 35 | Don Mueang International Airport |  | TH | 1453 |
| 36 | Calgary International Airport |  | CA | 1447 |
| 37 | Bengaluru International Airport |  | IN | 1438 |
| 38 | Oslo Gardermoen Airport |  | NO | 1416 |
| 39 | Vancouver International Airport |  | CA | 1404 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1362 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 933 | 21m | 244 km | 3,928.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 668 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 632 | 1h 6m | 770 km | 8,395.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 396 | 44m | 555 km | 3,791.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 375 | 44m | 241 km | 1,557.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 350 | 24m | 218 km | 1,318.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 336 | 23m | 55 km | 319.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 294 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 272 | 1h 50m | 1,304 km | 6,119.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 261 | 41m | 535 km | 2,410.5 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N820KE |  | Friday Harbor Airport (KFHR) | Bellingham International Airport (KBLI) | 2026-09-08 14:36 UTC | 2026-09-08 14:52 UTC | 15m |
| CGKGP | CGK | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-08 14:34 UTC | 2026-09-08 14:50 UTC | 16m |
| AXB1808 | AXB | Jamnagar Airport (VAJM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 13:59 UTC | 2026-09-08 14:48 UTC | 48m |
| N456PA |  | Maquoketa Municipal Airport (KOQW) | Dubuque Regional Airport (KDBQ) | 2026-09-08 14:30 UTC | 2026-09-08 14:48 UTC | 17m |
| N37PZ |  | UT37 (UT37) | Henderson Executive Airport (KHND) | 2026-09-08 14:13 UTC | 2026-09-08 14:45 UTC | 31m |
| CHH754 | CHH | Manchester Airport (EGCC) | Ukhta Airport (UUYH) | 2026-09-08 11:37 UTC | 2026-09-08 14:44 UTC | 3h 6m |
| UPS94D | UPS | Ted Stevens Anchorage International Airport (PANC) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-09-08 04:09 UTC | 2026-09-08 14:43 UTC | 10h 33m |
| N786SA |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-09-08 14:26 UTC | 2026-09-08 14:40 UTC | 13m |
| N945RF |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-09-08 13:46 UTC | 2026-09-08 14:40 UTC | 53m |
| N6123Q |  | KORC (KORC) | Brookings Regional Airport (KBKX) | 2026-09-08 13:35 UTC | 2026-09-08 14:40 UTC | 1h 4m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-09-08 14:17 UTC | 2026-09-08 14:36 UTC | 19m |
| N1382F |  | Washington County Airport (KAFJ) | Washington County Airport (KAFJ) | 2026-09-08 14:20 UTC | 2026-09-08 14:35 UTC | 14m |
|  |  | North Palm Beach County General Aviation Airport (KF45) | North Palm Beach County General Aviation Airport (KF45) | 2026-09-08 14:30 UTC | 2026-09-08 14:30 UTC | 0m |
| THY3MJ | Turkish Airlines | London Heathrow Airport (EGLL) | Istanbul Airport (LTFM) | 2026-09-08 11:21 UTC | 2026-09-08 14:26 UTC | 3h 5m |
| TIAZI | TIA | Juan Santamaria International Airport (MROC) | MRCJ (MRCJ) | 2026-09-08 14:08 UTC | 2026-09-08 14:24 UTC | 16m |
| N75398 |  | Beaufort Executive Airport (KARW) | Beaufort Executive Airport (KARW) | 2026-09-08 14:21 UTC | 2026-09-08 14:21 UTC | 0m |
| EFY9156 | EFY | Enrique Olaya Herrera Airport (SKMD) | Perales Airport (SKIB) | 2026-09-08 13:49 UTC | 2026-09-08 14:21 UTC | 32m |
| RDHK723 | RDH | Norfolk Ns (Chambers Field) Airport (KNGU) | Felker Army Air Field (KFAF) | 2026-09-08 14:10 UTC | 2026-09-08 14:20 UTC | 9m |
| ROGUE01 | ROG | Twenthe Airport (EHTW) | Eindhoven Airport (EHEH) | 2026-09-08 13:49 UTC | 2026-09-08 14:19 UTC | 30m |
| CXK438 | CXK | Kinston Regional Jetport At Stallings Field (KISO) | Henderson/Oxford Airport (KHNZ) | 2026-09-08 13:39 UTC | 2026-09-08 14:19 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
