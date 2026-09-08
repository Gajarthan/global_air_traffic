# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_21:09:49_UTC-green)

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

**Latest saved flight:** 2026-09-08 21:09:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 21:09:49 UTC

- **251,947** saved flights
- **75,516** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,947** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,034,000.8 tonnes** estimated CO2 emissions
- **175,884,104 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10078 |
| 2 | SkyWest Airlines | 8803 |
| 3 | EJA | 4870 |
| 4 | IndiGo | 4218 |
| 5 | American Airlines | 4022 |
| 6 | Southwest Airlines | 3730 |
| 7 | Delta Air Lines | 3185 |
| 8 | ENY | 3008 |
| 9 | LATAM Airlines | 2423 |
| 10 | AZU | 2338 |
| 11 | Vueling | 2145 |
| 12 | WIF | 2019 |
| 13 | Lufthansa | 1991 |
| 14 | LXJ | 1966 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1693 |
| 17 | AXM | 1629 |
| 18 | QLK | 1619 |
| 19 | EJU | 1617 |
| 20 | United Airlines | 1571 |
| 21 | Alaska Airlines | 1502 |
| 22 | All Nippon Airways | 1474 |
| 23 | WMT | 1429 |
| 24 | GLO | 1397 |
| 25 | PGT | 1383 |
| 26 | VIV | 1379 |
| 27 | Air France | 1376 |
| 28 | Wizz Air | 1373 |
| 29 | JetBlue | 1234 |
| 30 | AEE | 1232 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209044 |
| 2 | 🇪🇸 ES | 16092 |
| 3 | 🇧🇷 BR | 14679 |
| 4 | 🇦🇺 AU | 14317 |
| 5 | 🇨🇦 CA | 13993 |
| 6 | 🇮🇹 IT | 13790 |
| 7 | 🇮🇳 IN | 13179 |
| 8 | 🇩🇪 DE | 12362 |
| 9 | 🇬🇧 GB | 11798 |
| 10 | 🇨🇴 CO | 11110 |
| 11 | 🇫🇷 FR | 10138 |
| 12 | 🇯🇵 JP | 9906 |
| 13 | 🇹🇷 TR | 7537 |
| 14 | 🇬🇷 GR | 7395 |
| 15 | 🇲🇽 MX | 6953 |
| 16 | 🇨🇭 CH | 6795 |
| 17 | 🇳🇴 NO | 6239 |
| 18 | 🇹🇭 TH | 4538 |
| 19 | 🇲🇾 MY | 4379 |
| 20 | 🇿🇦 ZA | 4321 |
| 21 | 🇵🇱 PL | 4198 |
| 22 | 🇳🇿 NZ | 3434 |
| 23 | 🇵🇭 PH | 3412 |
| 24 | 🇬🇹 GT | 3140 |
| 25 | 🇰🇷 KR | 2909 |
| 26 | 🇭🇷 HR | 2897 |
| 27 | 🇲🇦 MA | 2548 |
| 28 | 🇲🇪 ME | 2372 |
| 29 | 🇳🇱 NL | 2272 |
| 30 | 🇮🇩 ID | 2153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5198 |
| 2 | Denver International Airport |  | US | 4077 |
| 3 | Indira Gandhi International Airport |  | IN | 3061 |
| 4 | Tokyo International Airport |  | JP | 2955 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2677 |
| 7 | Zurich Airport |  | CH | 2638 |
| 8 | El Dorado International Airport |  | CO | 2562 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2553 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2489 |
| 11 | La Aurora Airport |  | GT | 2395 |
| 12 | Salt Lake City International Airport |  | US | 2227 |
| 13 | Chicago O'Hare International Airport |  | US | 2197 |
| 14 | Congonhas Airport |  | BR | 2152 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2071 |
| 16 | Capua Airport |  | IT | 1986 |
| 17 | Madrid Barajas International Airport |  | ES | 1979 |
| 18 | Frankfurt am Main International Airport |  | DE | 1960 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1885 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1832 |
| 21 | Malpensa International Airport |  | IT | 1811 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 23 | Charles de Gaulle International Airport |  | FR | 1768 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1755 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1674 |
| 26 | Ninoy Aquino International Airport |  | PH | 1666 |
| 27 | Macau International Airport |  | MO | 1655 |
| 28 | Barcelona International Airport |  | ES | 1590 |
| 29 | Charlotte/Douglas International Airport |  | US | 1588 |
| 30 | Kuala Lumpur International Airport |  | MY | 1577 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1548 |
| 32 | Viracopos International Airport |  | BR | 1502 |
| 33 | Seattle-Tacoma International Airport |  | US | 1486 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1462 |
| 35 | Don Mueang International Airport |  | TH | 1453 |
| 36 | Calgary International Airport |  | CA | 1449 |
| 37 | Bengaluru International Airport |  | IN | 1438 |
| 38 | Oslo Gardermoen Airport |  | NO | 1420 |
| 39 | Vancouver International Airport |  | CA | 1409 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1362 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 935 | 21m | 244 km | 3,937.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 670 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 632 | 1h 6m | 770 km | 8,395.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 396 | 44m | 555 km | 3,791.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 376 | 44m | 241 km | 1,561.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 351 | 24m | 218 km | 1,322.4 t |
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
| ENY4156 | ENY | Green Bay/Austin Straubel International Airport (KGRB) | Chicago O'Hare International Airport (KORD) | 2026-09-08 20:30 UTC | 2026-09-08 21:09 UTC | 39m |
| N516XX |  | NM28 (NM28) | NM71 (NM71) | 2026-09-08 20:46 UTC | 2026-09-08 21:02 UTC | 16m |
| VALOR77 | VAL | Dothan Regional Airport (KDHN) | Southwest Georgia Regional Airport (KABY) | 2026-09-08 19:25 UTC | 2026-09-08 21:01 UTC | 1h 35m |
| N513XX |  | El Paso International Airport (KELP) | NM71 (NM71) | 2026-09-08 20:30 UTC | 2026-09-08 20:59 UTC | 28m |
| N444GF |  | Mesquite Metro Airport (KHQZ) | Addison Airport (KADS) | 2026-09-08 19:50 UTC | 2026-09-08 20:59 UTC | 1h 8m |
| N202TL |  | Arlington Municipal Airport (KAWO) | Arlington Municipal Airport (KAWO) | 2026-09-08 20:43 UTC | 2026-09-08 20:58 UTC | 14m |
| GOLEM31 | GOL | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-09-08 20:42 UTC | 2026-09-08 20:55 UTC | 13m |
| N366EA |  | Glendale Regional Airport (KGEU) | Bagdad Airport (KE51) | 2026-09-08 19:45 UTC | 2026-09-08 20:55 UTC | 1h 9m |
| FH011 |  | Whiting Field Nas South Airport (KNDZ) | Santa Rosa Nolf Airport (KNGS) | 2026-09-08 20:28 UTC | 2026-09-08 20:51 UTC | 23m |
| N825AV |  | Meadows Field (KBFL) | Palm Springs International Airport (KPSP) | 2026-09-08 20:15 UTC | 2026-09-08 20:45 UTC | 30m |
| BOE121 | BOE | Seattle Paine Field International Airport (KPAE) | Franz Ranch Airport (33WA) | 2026-09-08 18:51 UTC | 2026-09-08 20:45 UTC | 1h 53m |
| TIGER60 | TIG | Hughes Ranch Airport (50XS) | Hughes Ranch Airport (50XS) | 2026-09-08 20:32 UTC | 2026-09-08 20:44 UTC | 11m |
| XDV | XDV | Bathurst Airport (YBTH) | Sydney Bankstown Airport (YSBK) | 2026-09-08 20:23 UTC | 2026-09-08 20:43 UTC | 19m |
| N5469K |  | Flying G Ranch Airport (86GA) | Flying G Ranch Airport (86GA) | 2026-09-08 20:39 UTC | 2026-09-08 20:42 UTC | 3m |
| N38549 |  | Lebanon Municipal Airport (KLEB) | Lebanon Municipal Airport (KLEB) | 2026-09-08 20:18 UTC | 2026-09-08 20:39 UTC | 20m |
| N71KV |  | Tallahassee International Airport (KTLH) | Tampa International Airport (KTPA) | 2026-09-08 19:58 UTC | 2026-09-08 20:39 UTC | 40m |
| N621T |  | KU42 (KU42) | K36U (K36U) | 2026-09-08 20:11 UTC | 2026-09-08 20:35 UTC | 23m |
| UAE500 | Emirates | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 18:12 UTC | 2026-09-08 20:33 UTC | 2h 21m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-09-08 20:17 UTC | 2026-09-08 20:28 UTC | 10m |
| N817FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-09-08 19:35 UTC | 2026-09-08 20:26 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
