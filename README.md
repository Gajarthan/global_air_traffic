# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_02:54:16_UTC-green)

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

**Latest saved flight:** 2026-08-16 02:54:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 02:54:16 UTC

- **203,362** saved flights
- **65,111** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,362** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,443,699.4 tonnes** estimated CO2 emissions
- **141,663,732 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7990 |
| 2 | SkyWest Airlines | 7346 |
| 3 | EJA | 3953 |
| 4 | IndiGo | 3461 |
| 5 | American Airlines | 3397 |
| 6 | Southwest Airlines | 3303 |
| 7 | Delta Air Lines | 2608 |
| 8 | ENY | 2545 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1835 |
| 11 | Lufthansa | 1719 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1397 |
| 16 | Swiss International | 1352 |
| 17 | AXM | 1313 |
| 18 | United Airlines | 1288 |
| 19 | Alaska Airlines | 1273 |
| 20 | QLK | 1245 |
| 21 | EJU | 1242 |
| 22 | All Nippon Airways | 1231 |
| 23 | VIV | 1118 |
| 24 | GLO | 1094 |
| 25 | PGT | 1078 |
| 26 | Air France | 1077 |
| 27 | JetBlue | 1049 |
| 28 | AEE | 1032 |
| 29 | CXK | 1011 |
| 30 | WMT | 1010 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173623 |
| 2 | 🇪🇸 ES | 12988 |
| 3 | 🇧🇷 BR | 11642 |
| 4 | 🇦🇺 AU | 11368 |
| 5 | 🇨🇦 CA | 11259 |
| 6 | 🇮🇳 IN | 10813 |
| 7 | 🇮🇹 IT | 10524 |
| 8 | 🇩🇪 DE | 10003 |
| 9 | 🇬🇧 GB | 9462 |
| 10 | 🇯🇵 JP | 8315 |
| 11 | 🇨🇴 CO | 8042 |
| 12 | 🇫🇷 FR | 8032 |
| 13 | 🇬🇷 GR | 5945 |
| 14 | 🇲🇽 MX | 5733 |
| 15 | 🇹🇷 TR | 5668 |
| 16 | 🇨🇭 CH | 5419 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3450 |
| 19 | 🇿🇦 ZA | 3374 |
| 20 | 🇵🇱 PL | 3332 |
| 21 | 🇹🇭 TH | 3166 |
| 22 | 🇳🇿 NZ | 2817 |
| 23 | 🇵🇭 PH | 2677 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2477 |
| 26 | 🇭🇷 HR | 2139 |
| 27 | 🇲🇦 MA | 2037 |
| 28 | 🇳🇱 NL | 1801 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1655 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4286 |
| 2 | Denver International Airport |  | US | 3334 |
| 3 | Tokyo International Airport |  | JP | 2520 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2456 |
| 6 | Harry Reid International Airport |  | US | 2319 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2119 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2110 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1901 |
| 12 | El Dorado International Airport |  | CO | 1860 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1825 |
| 14 | Salt Lake City International Airport |  | US | 1806 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1683 |
| 17 | Madrid Barajas International Airport |  | ES | 1585 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1563 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1554 |
| 20 | Capua Airport |  | IT | 1539 |
| 21 | Macau International Airport |  | MO | 1536 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1423 |
| 24 | Malpensa International Airport |  | IT | 1399 |
| 25 | Charlotte/Douglas International Airport |  | US | 1389 |
| 26 | Charles de Gaulle International Airport |  | FR | 1387 |
| 27 | Kuala Lumpur International Airport |  | MY | 1283 |
| 28 | Ninoy Aquino International Airport |  | PH | 1266 |
| 29 | Bengaluru International Airport |  | IN | 1261 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1255 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1231 |
| 32 | Barcelona International Airport |  | ES | 1213 |
| 33 | Seattle-Tacoma International Airport |  | US | 1210 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1156 |
| 36 | Reno/Tahoe International Airport |  | US | 1131 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 492 | 1h 7m | 770 km | 6,535.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 469 | 24m | 225 km | 1,819.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 228 | 31m | 369 km | 1,451.3 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100BW |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-16 02:23 UTC | 2026-08-16 02:54 UTC | 30m |
| XFB | XFB | Torquay Airport (YTQY) | Torquay Airport (YTQY) | 2026-08-16 02:50 UTC | 2026-08-16 02:50 UTC | 0m |
| SKW3799 | SkyWest Airlines | Spokane International Airport (KGEG) | Van Nuys Airport (KVNY) | 2026-08-16 00:34 UTC | 2026-08-16 02:50 UTC | 2h 16m |
| N539SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-16 02:49 UTC | 2026-08-16 02:50 UTC | 0m |
| TOM77K | TOM | Larnaca International Airport (LCLK) | Chambley Airport (LF52) | 2026-08-15 23:04 UTC | 2026-08-16 02:38 UTC | 3h 33m |
| AAL132 | American Airlines | Dallas Love Field (KDAL) | Tobermory Airport (CNR4) | 2026-08-16 00:29 UTC | 2026-08-16 02:36 UTC | 2h 6m |
| AAL1389 | American Airlines | Miami International Airport (KMIA) | Branham Mill Airpark (VG29) | 2026-08-16 00:47 UTC | 2026-08-16 02:36 UTC | 1h 48m |
| AAL1843 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Oag Unmanned Center Airport (MD85) | 2026-08-16 01:47 UTC | 2026-08-16 02:36 UTC | 49m |
| AAL2549 | American Airlines | Chicago O'Hare International Airport (KORD) | CRM5 (CRM5) | 2026-08-16 01:57 UTC | 2026-08-16 02:36 UTC | 38m |
| AAL3151 | American Airlines | Mesquite Airport (K67L) | LL33 (LL33) | 2026-08-16 00:29 UTC | 2026-08-16 02:36 UTC | 2h 6m |
| AAL528 | American Airlines | Mc Allen International Airport (KMFE) | TS53 (TS53) | 2026-08-16 01:39 UTC | 2026-08-16 02:36 UTC | 56m |
| AAL54 | American Airlines | Chicago O'Hare International Airport (KORD) | Oakland Southwest Airport (KY47) | 2026-08-16 02:07 UTC | 2026-08-16 02:36 UTC | 28m |
| AAL9828 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Garner Airport (3VA8) | 2026-08-16 02:01 UTC | 2026-08-16 02:36 UTC | 34m |
| AAL993 | American Airlines | Charlotte/Douglas International Airport (KCLT) | VA80 (VA80) | 2026-08-16 02:00 UTC | 2026-08-16 02:36 UTC | 35m |
| ASA481 | Alaska Airlines | Norman Y Mineta San Jose International Airport (KSJC) | Double Creek Airpark (CN42) | 2026-08-16 02:03 UTC | 2026-08-16 02:36 UTC | 32m |
| ASH4012 | ASH | Washington Dulles International Airport (KIAD) | MD43 (MD43) | 2026-08-16 02:23 UTC | 2026-08-16 02:36 UTC | 12m |
| BAW12TB | British Airways | Tampa International Airport (KTPA) | Brookins Air Strip (73FD) | 2026-08-16 02:20 UTC | 2026-08-16 02:36 UTC | 15m |
| DAL1489 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Hidden Lake Airport (FA40) | 2026-08-16 01:48 UTC | 2026-08-16 02:36 UTC | 47m |
| DAL1531 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Healdton Municipal Airport (KF32) | 2026-08-16 01:05 UTC | 2026-08-16 02:36 UTC | 1h 30m |
| DAL1636 | Delta Air Lines | John F Kennedy International Airport (KJFK) | Trenton-Robbinsville Airport (KN87) | 2026-08-16 02:25 UTC | 2026-08-16 02:36 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
