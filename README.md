# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_12:41:51_UTC-green)

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

**Latest saved flight:** 2026-09-12 12:41:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 12:41:51 UTC

- **255,978** saved flights
- **76,334** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,978** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,092,809.0 tonnes** estimated CO2 emissions
- **179,293,275 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10189 |
| 2 | SkyWest Airlines | 8919 |
| 3 | EJA | 4942 |
| 4 | IndiGo | 4291 |
| 5 | American Airlines | 4054 |
| 6 | Southwest Airlines | 3768 |
| 7 | Delta Air Lines | 3204 |
| 8 | ENY | 3039 |
| 9 | LATAM Airlines | 2464 |
| 10 | AZU | 2383 |
| 11 | Vueling | 2167 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2005 |
| 14 | LXJ | 1996 |
| 15 | easyJet | 1746 |
| 16 | Swiss International | 1715 |
| 17 | QLK | 1653 |
| 18 | AXM | 1642 |
| 19 | EJU | 1632 |
| 20 | United Airlines | 1587 |
| 21 | Alaska Airlines | 1521 |
| 22 | All Nippon Airways | 1493 |
| 23 | WMT | 1447 |
| 24 | GLO | 1427 |
| 25 | PGT | 1410 |
| 26 | VIV | 1402 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1391 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1243 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212466 |
| 2 | 🇪🇸 ES | 16269 |
| 3 | 🇧🇷 BR | 14938 |
| 4 | 🇦🇺 AU | 14613 |
| 5 | 🇨🇦 CA | 14249 |
| 6 | 🇮🇹 IT | 13986 |
| 7 | 🇮🇳 IN | 13449 |
| 8 | 🇩🇪 DE | 12490 |
| 9 | 🇬🇧 GB | 11949 |
| 10 | 🇨🇴 CO | 11407 |
| 11 | 🇫🇷 FR | 10279 |
| 12 | 🇯🇵 JP | 10016 |
| 13 | 🇹🇷 TR | 7681 |
| 14 | 🇬🇷 GR | 7471 |
| 15 | 🇲🇽 MX | 7063 |
| 16 | 🇨🇭 CH | 6878 |
| 17 | 🇳🇴 NO | 6346 |
| 18 | 🇹🇭 TH | 4611 |
| 19 | 🇲🇾 MY | 4415 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4243 |
| 22 | 🇳🇿 NZ | 3537 |
| 23 | 🇵🇭 PH | 3446 |
| 24 | 🇬🇹 GT | 3211 |
| 25 | 🇰🇷 KR | 2938 |
| 26 | 🇭🇷 HR | 2933 |
| 27 | 🇲🇦 MA | 2577 |
| 28 | 🇲🇪 ME | 2408 |
| 29 | 🇳🇱 NL | 2307 |
| 30 | 🇮🇩 ID | 2178 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5247 |
| 2 | Denver International Airport |  | US | 4135 |
| 3 | Indira Gandhi International Airport |  | IN | 3098 |
| 4 | Tokyo International Airport |  | JP | 2991 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2711 |
| 7 | Zurich Airport |  | CH | 2681 |
| 8 | El Dorado International Airport |  | CO | 2642 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2580 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2506 |
| 11 | La Aurora Airport |  | GT | 2444 |
| 12 | Salt Lake City International Airport |  | US | 2256 |
| 13 | Chicago O'Hare International Airport |  | US | 2228 |
| 14 | Congonhas Airport |  | BR | 2194 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2092 |
| 16 | Capua Airport |  | IT | 2016 |
| 17 | Madrid Barajas International Airport |  | ES | 1996 |
| 18 | Frankfurt am Main International Airport |  | DE | 1979 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1920 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1851 |
| 21 | Malpensa International Airport |  | IT | 1841 |
| 22 | Charles de Gaulle International Airport |  | FR | 1802 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1799 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1778 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1723 |
| 26 | Macau International Airport |  | MO | 1698 |
| 27 | Ninoy Aquino International Airport |  | PH | 1685 |
| 28 | Barcelona International Airport |  | ES | 1609 |
| 29 | Charlotte/Douglas International Airport |  | US | 1602 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1571 |
| 32 | Viracopos International Airport |  | BR | 1528 |
| 33 | Seattle-Tacoma International Airport |  | US | 1501 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1488 |
| 35 | Don Mueang International Airport |  | TH | 1474 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1455 |
| 38 | Oslo Gardermoen Airport |  | NO | 1448 |
| 39 | Vancouver International Airport |  | CA | 1436 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 953 | 21m | 244 km | 4,012.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 684 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 643 | 1h 6m | 770 km | 8,541.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 640 | 24m | 225 km | 2,482.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 411 | 44m | 555 km | 3,935.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 407 | 1h 50m | 1,423 km | 9,988.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 358 | 24m | 218 km | 1,348.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 342 | 23m | 55 km | 325.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 314 | 19m | 99 km | 537.9 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 309 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 269 | 41m | 535 km | 2,484.4 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 265 | 28m | 152 km | 692.5 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CES723 | China Eastern | Incheon International Airport (RKSI) | Chek Lap Kok International Airport (VHHH) | 2026-09-12 07:24 UTC | 2026-09-12 12:41 UTC | 5h 17m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-09-12 12:09 UTC | 2026-09-12 12:32 UTC | 22m |
| IGO279V | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-12 09:42 UTC | 2026-09-12 12:29 UTC | 2h 46m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-12 12:01 UTC | 2026-09-12 12:27 UTC | 26m |
| AXB1800 | AXB | Cochin International Airport (VOCI) | Pune Airport (VAPO) | 2026-09-12 10:58 UTC | 2026-09-12 12:27 UTC | 1h 28m |
| HBKLX | HBK | Yverdon-les-Bains Airport (LSGY) | Yverdon-les-Bains Airport (LSGY) | 2026-09-12 12:01 UTC | 2026-09-12 12:16 UTC | 14m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Zhuhai Airport (ZGSD) | 2026-09-11 21:50 UTC | 2026-09-12 12:14 UTC | 14h 23m |
| UBG165 | UBG | VGZR (VGZR) | Shah Mokhdum Airport (VGRJ) | 2026-09-12 11:37 UTC | 2026-09-12 12:07 UTC | 29m |
| LFA332 | LFA | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-09-12 12:01 UTC | 2026-09-12 12:02 UTC | 1m |
| TCAJM | TCA | Balikesir Korfez Airport (LTFD) | Balikesir Korfez Airport (LTFD) | 2026-09-12 11:51 UTC | 2026-09-12 12:00 UTC | 8m |
| OHFMZ | OHF | Immola Airport (EFIM) | Immola Airport (EFIM) | 2026-09-12 11:54 UTC | 2026-09-12 12:00 UTC | 5m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-09-12 11:37 UTC | 2026-09-12 11:59 UTC | 22m |
| CXK419 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-09-12 11:44 UTC | 2026-09-12 11:58 UTC | 14m |
| AAH56 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-09-12 11:36 UTC | 2026-09-12 11:57 UTC | 21m |
| PH1529 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-09-12 11:27 UTC | 2026-09-12 11:55 UTC | 27m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-12 11:20 UTC | 2026-09-12 11:48 UTC | 28m |
| SEH5JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-09-12 11:18 UTC | 2026-09-12 11:46 UTC | 28m |
| AIC4ZK | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-09-12 11:23 UTC | 2026-09-12 11:45 UTC | 21m |
| N80298 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-12 11:16 UTC | 2026-09-12 11:44 UTC | 27m |
| RYR2UH | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Berane Airport (LYBR) | 2026-09-12 10:39 UTC | 2026-09-12 11:43 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
