# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_18:14:17_UTC-green)

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

**Latest saved flight:** 2026-09-12 18:14:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 18:14:17 UTC

- **256,415** saved flights
- **76,436** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **256,415** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,097,849.1 tonnes** estimated CO2 emissions
- **179,585,453 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10202 |
| 2 | SkyWest Airlines | 8928 |
| 3 | EJA | 4952 |
| 4 | IndiGo | 4300 |
| 5 | American Airlines | 4059 |
| 6 | Southwest Airlines | 3775 |
| 7 | Delta Air Lines | 3206 |
| 8 | ENY | 3043 |
| 9 | LATAM Airlines | 2468 |
| 10 | AZU | 2386 |
| 11 | Vueling | 2167 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2010 |
| 14 | LXJ | 2001 |
| 15 | easyJet | 1751 |
| 16 | Swiss International | 1720 |
| 17 | QLK | 1653 |
| 18 | AXM | 1642 |
| 19 | EJU | 1635 |
| 20 | United Airlines | 1588 |
| 21 | Alaska Airlines | 1523 |
| 22 | All Nippon Airways | 1493 |
| 23 | WMT | 1450 |
| 24 | GLO | 1430 |
| 25 | PGT | 1414 |
| 26 | VIV | 1404 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1395 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1245 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212854 |
| 2 | 🇪🇸 ES | 16294 |
| 3 | 🇧🇷 BR | 14958 |
| 4 | 🇦🇺 AU | 14613 |
| 5 | 🇨🇦 CA | 14286 |
| 6 | 🇮🇹 IT | 14009 |
| 7 | 🇮🇳 IN | 13473 |
| 8 | 🇩🇪 DE | 12509 |
| 9 | 🇬🇧 GB | 11965 |
| 10 | 🇨🇴 CO | 11439 |
| 11 | 🇫🇷 FR | 10305 |
| 12 | 🇯🇵 JP | 10017 |
| 13 | 🇹🇷 TR | 7698 |
| 14 | 🇬🇷 GR | 7481 |
| 15 | 🇲🇽 MX | 7080 |
| 16 | 🇨🇭 CH | 6888 |
| 17 | 🇳🇴 NO | 6347 |
| 18 | 🇹🇭 TH | 4613 |
| 19 | 🇲🇾 MY | 4415 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4255 |
| 22 | 🇳🇿 NZ | 3537 |
| 23 | 🇵🇭 PH | 3446 |
| 24 | 🇬🇹 GT | 3245 |
| 25 | 🇭🇷 HR | 2943 |
| 26 | 🇰🇷 KR | 2938 |
| 27 | 🇲🇦 MA | 2584 |
| 28 | 🇲🇪 ME | 2411 |
| 29 | 🇳🇱 NL | 2313 |
| 30 | 🇮🇩 ID | 2178 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5257 |
| 2 | Denver International Airport |  | US | 4142 |
| 3 | Indira Gandhi International Airport |  | IN | 3102 |
| 4 | Tokyo International Airport |  | JP | 2991 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2713 |
| 7 | Zurich Airport |  | CH | 2687 |
| 8 | El Dorado International Airport |  | CO | 2651 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2583 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2508 |
| 11 | La Aurora Airport |  | GT | 2466 |
| 12 | Salt Lake City International Airport |  | US | 2260 |
| 13 | Chicago O'Hare International Airport |  | US | 2231 |
| 14 | Congonhas Airport |  | BR | 2197 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2093 |
| 16 | Capua Airport |  | IT | 2020 |
| 17 | Madrid Barajas International Airport |  | ES | 2003 |
| 18 | Frankfurt am Main International Airport |  | DE | 1981 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1925 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1853 |
| 21 | Malpensa International Airport |  | IT | 1845 |
| 22 | Charles de Gaulle International Airport |  | FR | 1803 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1799 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1779 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1732 |
| 26 | Macau International Airport |  | MO | 1698 |
| 27 | Ninoy Aquino International Airport |  | PH | 1685 |
| 28 | Barcelona International Airport |  | ES | 1612 |
| 29 | Charlotte/Douglas International Airport |  | US | 1607 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1572 |
| 32 | Viracopos International Airport |  | BR | 1530 |
| 33 | Seattle-Tacoma International Airport |  | US | 1501 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1488 |
| 35 | Don Mueang International Airport |  | TH | 1475 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1457 |
| 38 | Oslo Gardermoen Airport |  | NO | 1449 |
| 39 | Vancouver International Airport |  | CA | 1441 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1386 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 956 | 21m | 244 km | 4,025.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 688 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 643 | 1h 6m | 770 km | 8,541.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 640 | 24m | 225 km | 2,482.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 575 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 412 | 44m | 555 km | 3,945.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 409 | 1h 50m | 1,423 km | 10,037.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 358 | 24m | 218 km | 1,348.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 318 | 19m | 99 km | 544.7 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 309 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 294 | 19m | 144 km | 731.3 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 269 | 41m | 535 km | 2,484.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXJ429 | LXJ | Allen Airport (8OI3) | Teterboro Airport (KTEB) | 2026-09-12 17:22 UTC | 2026-09-12 18:14 UTC | 52m |
| N733KG |  | Essex County Airport (KCDW) | Somerset Airport (KSMQ) | 2026-09-12 17:46 UTC | 2026-09-12 18:07 UTC | 20m |
| CAP582 | CAP | City Of Colorado Springs Municipal Airport (KCOS) | Lowe Airstrip (CD01) | 2026-09-12 17:20 UTC | 2026-09-12 18:04 UTC | 44m |
| N80JF |  | Orange Municipal Airport (KORE) | Orange Municipal Airport (KORE) | 2026-09-12 17:12 UTC | 2026-09-12 18:02 UTC | 49m |
| CXK104 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-09-12 16:39 UTC | 2026-09-12 17:59 UTC | 1h 20m |
| N568CA |  | Akron/Jesson Field (K9G3) | Akron/Jesson Field (K9G3) | 2026-09-12 17:39 UTC | 2026-09-12 17:58 UTC | 18m |
| N8409L |  | St Simons Island Airport (KSSI) | Brunswick Golden Isles Airport (KBQK) | 2026-09-12 17:54 UTC | 2026-09-12 17:57 UTC | 2m |
| N9897F |  | Mc Clellan-Palomar Airport (KCRQ) | San Bernardino International Airport (KSBD) | 2026-09-12 17:12 UTC | 2026-09-12 17:54 UTC | 42m |
| N273ND |  | II19 (II19) | De Ford Airport (4II0) | 2026-09-12 17:18 UTC | 2026-09-12 17:53 UTC | 35m |
| N661DS |  | San Gabriel Valley Airport (KEMT) | Brackett Field (KPOC) | 2026-09-12 17:11 UTC | 2026-09-12 17:52 UTC | 41m |
| ERU35 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Cottonwood Airport (KP52) | 2026-09-12 17:36 UTC | 2026-09-12 17:47 UTC | 11m |
| N135RF |  | Casas Adobes Airpark (NM69) | Casas Adobes Airpark (NM69) | 2026-09-12 17:35 UTC | 2026-09-12 17:47 UTC | 12m |
| N960PD |  | Hayward Executive Airport (KHWD) | Meadows Field (KBFL) | 2026-09-12 16:02 UTC | 2026-09-12 17:45 UTC | 1h 42m |
| DLH067 | Lufthansa | Dresden Airport (EDDC) | Frankfurt am Main International Airport (EDDF) | 2026-09-12 17:02 UTC | 2026-09-12 17:44 UTC | 42m |
| ERU41 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Cottonwood Airport (KP52) | 2026-09-12 17:31 UTC | 2026-09-12 17:42 UTC | 11m |
| N132TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-12 17:06 UTC | 2026-09-12 17:42 UTC | 36m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-12 16:49 UTC | 2026-09-12 17:40 UTC | 50m |
| AIC4218 | Air India | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-12 15:06 UTC | 2026-09-12 17:40 UTC | 2h 33m |
| G72471 |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-12 17:35 UTC | 2026-09-12 17:40 UTC | 4m |
| PERRIS1 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-09-12 15:30 UTC | 2026-09-12 17:39 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
