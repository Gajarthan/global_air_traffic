# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_04:44:24_UTC-green)

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

**Latest saved flight:** 2026-09-16 04:44:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 04:44:24 UTC

- **259,922** saved flights
- **77,117** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,922** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,148,159.1 tonnes** estimated CO2 emissions
- **182,501,976 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10287 |
| 2 | SkyWest Airlines | 9065 |
| 3 | EJA | 5044 |
| 4 | IndiGo | 4358 |
| 5 | American Airlines | 4097 |
| 6 | Southwest Airlines | 3822 |
| 7 | Delta Air Lines | 3248 |
| 8 | ENY | 3077 |
| 9 | LATAM Airlines | 2502 |
| 10 | AZU | 2439 |
| 11 | Vueling | 2193 |
| 12 | WIF | 2087 |
| 13 | LXJ | 2034 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1766 |
| 16 | Swiss International | 1731 |
| 17 | QLK | 1681 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1602 |
| 21 | Alaska Airlines | 1545 |
| 22 | All Nippon Airways | 1508 |
| 23 | WMT | 1465 |
| 24 | GLO | 1450 |
| 25 | PGT | 1449 |
| 26 | VIV | 1426 |
| 27 | Air France | 1419 |
| 28 | Wizz Air | 1413 |
| 29 | TKR | 1260 |
| 30 | AEE | 1255 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215874 |
| 2 | 🇪🇸 ES | 16440 |
| 3 | 🇧🇷 BR | 15197 |
| 4 | 🇦🇺 AU | 14871 |
| 5 | 🇨🇦 CA | 14473 |
| 6 | 🇮🇹 IT | 14133 |
| 7 | 🇮🇳 IN | 13731 |
| 8 | 🇩🇪 DE | 12609 |
| 9 | 🇬🇧 GB | 12086 |
| 10 | 🇨🇴 CO | 11698 |
| 11 | 🇫🇷 FR | 10418 |
| 12 | 🇯🇵 JP | 10108 |
| 13 | 🇹🇷 TR | 7842 |
| 14 | 🇬🇷 GR | 7551 |
| 15 | 🇲🇽 MX | 7174 |
| 16 | 🇨🇭 CH | 6969 |
| 17 | 🇳🇴 NO | 6414 |
| 18 | 🇹🇭 TH | 4666 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4289 |
| 22 | 🇳🇿 NZ | 3607 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3317 |
| 25 | 🇭🇷 HR | 2971 |
| 26 | 🇰🇷 KR | 2965 |
| 27 | 🇲🇦 MA | 2605 |
| 28 | 🇲🇪 ME | 2445 |
| 29 | 🇳🇱 NL | 2329 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5327 |
| 2 | Denver International Airport |  | US | 4212 |
| 3 | Indira Gandhi International Airport |  | IN | 3136 |
| 4 | Tokyo International Airport |  | JP | 3017 |
| 5 | Guaymaral Airport |  | CO | 2769 |
| 6 | Harry Reid International Airport |  | US | 2760 |
| 7 | El Dorado International Airport |  | CO | 2728 |
| 8 | Zurich Airport |  | CH | 2720 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2613 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2529 |
| 11 | La Aurora Airport |  | GT | 2516 |
| 12 | Salt Lake City International Airport |  | US | 2295 |
| 13 | Chicago O'Hare International Airport |  | US | 2253 |
| 14 | Congonhas Airport |  | BR | 2223 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2126 |
| 16 | Capua Airport |  | IT | 2028 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1956 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1870 |
| 21 | Malpensa International Airport |  | IT | 1868 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1834 |
| 23 | Charles de Gaulle International Airport |  | FR | 1830 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1790 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1770 |
| 26 | Macau International Airport |  | MO | 1722 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1625 |
| 29 | Charlotte/Douglas International Airport |  | US | 1624 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1600 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1571 |
| 33 | Seattle-Tacoma International Airport |  | US | 1527 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1513 |
| 35 | Don Mueang International Airport |  | TH | 1491 |
| 36 | Calgary International Airport |  | CA | 1486 |
| 37 | Bengaluru International Airport |  | IN | 1475 |
| 38 | Oslo Gardermoen Airport |  | NO | 1461 |
| 39 | Vancouver International Airport |  | CA | 1456 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1397 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 970 | 21m | 244 km | 4,084.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 702 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 651 | 1h 6m | 770 km | 8,648.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 583 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 422 | 44m | 555 km | 4,040.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 394 | 44m | 241 km | 1,636.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 330 | 19m | 99 km | 565.3 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 327 | 1h 6m | 706 km | 3,981.2 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 324 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 315 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 299 | 1h 14m | 961 km | 4,956.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 275 | 28m | 152 km | 718.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO24V | IndiGo | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-15 19:37 UTC | 2026-09-16 04:44 UTC | 9h 7m |
| UAL1389 | United Airlines | Denver International Airport (KDEN) | San Francisco International Airport (KSFO) | 2026-09-16 02:08 UTC | 2026-09-16 04:38 UTC | 2h 30m |
| N208TW |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-09-16 04:11 UTC | 2026-09-16 04:36 UTC | 24m |
| ZKTHG | ZKT | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-09-16 03:54 UTC | 2026-09-16 04:33 UTC | 38m |
| JAL6777 | Japan Airlines | Narita International Airport (RJAA) | Tianjin Binhai International Airport (ZBTJ) | 2026-09-16 01:14 UTC | 2026-09-16 04:28 UTC | 3h 13m |
| ENY3782 | ENY | Dallas-Fort Worth International Airport (KDFW) | Abilene Municipal Airport (KK78) | 2026-09-16 03:11 UTC | 2026-09-16 04:24 UTC | 1h 12m |
|  |  | Jomo Kenyatta International Airport (HKJK) | Nyeri Airport (HKNI) | 2026-09-16 04:11 UTC | 2026-09-16 04:23 UTC | 11m |
| N78PF |  | Daniel K Inouye International Airport (PHNL) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-09-16 03:51 UTC | 2026-09-16 04:20 UTC | 28m |
| AEE240 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-09-16 03:40 UTC | 2026-09-16 04:09 UTC | 29m |
| BH971 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-09-16 04:06 UTC | 2026-09-16 04:06 UTC | 0m |
| A05T |  | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-09-16 03:48 UTC | 2026-09-16 04:04 UTC | 16m |
| SHR12 | SHR | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-16 03:51 UTC | 2026-09-16 04:04 UTC | 13m |
| MTR | MTR | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-09-16 03:44 UTC | 2026-09-16 04:01 UTC | 17m |
| BLINR47 | BLI | Travis Afb Airport (KSUU) | Gansner Field (K2O1) | 2026-09-16 02:38 UTC | 2026-09-16 04:00 UTC | 1h 21m |
| PQR | PQR | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-09-16 03:00 UTC | 2026-09-16 03:54 UTC | 54m |
| BDOG200 | BDO | RAAF Base Richmond (YSRI) | Orange Airport (YORG) | 2026-09-16 03:32 UTC | 2026-09-16 03:51 UTC | 18m |
| N158U |  | Downey/Hyde Memorial/ Airport (KU58) | Simko Field (1ID9) | 2026-09-16 03:34 UTC | 2026-09-16 03:50 UTC | 15m |
| SDE752 | SDE | Edmonton International Airport (CYEG) | Boyle Airport (CFM7) | 2026-09-16 03:35 UTC | 2026-09-16 03:47 UTC | 12m |
| N743TH |  | Napa County Airport (KAPC) | Sacramento Mather Airport (KMHR) | 2026-09-16 03:05 UTC | 2026-09-16 03:47 UTC | 42m |
| URSA22 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-09-16 03:17 UTC | 2026-09-16 03:47 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
