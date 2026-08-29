# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_03:32:11_UTC-green)

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

**Latest saved flight:** 2026-08-29 03:32:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-29 03:32:11 UTC

- **240,601** saved flights
- **73,061** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **240,601** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,896,253.3 tonnes** estimated CO2 emissions
- **167,898,740 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9654 |
| 2 | SkyWest Airlines | 8444 |
| 3 | EJA | 4658 |
| 4 | IndiGo | 4057 |
| 5 | American Airlines | 3878 |
| 6 | Southwest Airlines | 3624 |
| 7 | Delta Air Lines | 3065 |
| 8 | ENY | 2903 |
| 9 | LATAM Airlines | 2310 |
| 10 | AZU | 2239 |
| 11 | Vueling | 2067 |
| 12 | Lufthansa | 1937 |
| 13 | WIF | 1905 |
| 14 | LXJ | 1869 |
| 15 | easyJet | 1673 |
| 16 | Swiss International | 1613 |
| 17 | AXM | 1595 |
| 18 | EJU | 1540 |
| 19 | QLK | 1538 |
| 20 | United Airlines | 1513 |
| 21 | Alaska Airlines | 1438 |
| 22 | All Nippon Airways | 1428 |
| 23 | WMT | 1353 |
| 24 | GLO | 1340 |
| 25 | VIV | 1321 |
| 26 | Air France | 1315 |
| 27 | PGT | 1314 |
| 28 | Wizz Air | 1292 |
| 29 | AEE | 1190 |
| 30 | JetBlue | 1190 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 199370 |
| 2 | 🇪🇸 ES | 15475 |
| 3 | 🇧🇷 BR | 14030 |
| 4 | 🇦🇺 AU | 13675 |
| 5 | 🇨🇦 CA | 13383 |
| 6 | 🇮🇹 IT | 13158 |
| 7 | 🇮🇳 IN | 12630 |
| 8 | 🇩🇪 DE | 11878 |
| 9 | 🇬🇧 GB | 11361 |
| 10 | 🇨🇴 CO | 10339 |
| 11 | 🇫🇷 FR | 9693 |
| 12 | 🇯🇵 JP | 9682 |
| 13 | 🇹🇷 TR | 7137 |
| 14 | 🇬🇷 GR | 7084 |
| 15 | 🇲🇽 MX | 6653 |
| 16 | 🇨🇭 CH | 6433 |
| 17 | 🇳🇴 NO | 5935 |
| 18 | 🇹🇭 TH | 4362 |
| 19 | 🇲🇾 MY | 4274 |
| 20 | 🇿🇦 ZA | 4213 |
| 21 | 🇵🇱 PL | 4025 |
| 22 | 🇳🇿 NZ | 3310 |
| 23 | 🇵🇭 PH | 3303 |
| 24 | 🇬🇹 GT | 3026 |
| 25 | 🇰🇷 KR | 2849 |
| 26 | 🇭🇷 HR | 2777 |
| 27 | 🇲🇦 MA | 2432 |
| 28 | 🇲🇪 ME | 2251 |
| 29 | 🇳🇱 NL | 2176 |
| 30 | 🇮🇩 ID | 2112 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4968 |
| 2 | Denver International Airport |  | US | 3882 |
| 3 | Indira Gandhi International Airport |  | IN | 2938 |
| 4 | Tokyo International Airport |  | JP | 2883 |
| 5 | Guaymaral Airport |  | CO | 2696 |
| 6 | Harry Reid International Airport |  | US | 2556 |
| 7 | Zurich Airport |  | CH | 2514 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2461 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2399 |
| 10 | El Dorado International Airport |  | CO | 2339 |
| 11 | La Aurora Airport |  | GT | 2306 |
| 12 | Chicago O'Hare International Airport |  | US | 2143 |
| 13 | Salt Lake City International Airport |  | US | 2121 |
| 14 | Congonhas Airport |  | BR | 2052 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1998 |
| 16 | Frankfurt am Main International Airport |  | DE | 1903 |
| 17 | Madrid Barajas International Airport |  | ES | 1896 |
| 18 | Capua Airport |  | IT | 1896 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1810 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1768 |
| 21 | Malpensa International Airport |  | IT | 1721 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1696 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1689 |
| 24 | Charles de Gaulle International Airport |  | FR | 1683 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1604 |
| 27 | Kuala Lumpur International Airport |  | MY | 1545 |
| 28 | Charlotte/Douglas International Airport |  | US | 1539 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1533 |
| 30 | Barcelona International Airport |  | ES | 1532 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1455 |
| 32 | Viracopos International Airport |  | BR | 1434 |
| 33 | Don Mueang International Airport |  | TH | 1406 |
| 34 | Bengaluru International Airport |  | IN | 1405 |
| 35 | Seattle-Tacoma International Airport |  | US | 1404 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1402 |
| 37 | Calgary International Airport |  | CA | 1381 |
| 38 | Oslo Gardermoen Airport |  | NO | 1347 |
| 39 | Vancouver International Airport |  | CA | 1324 |
| 40 | O. R. Tambo International Airport |  | ZA | 1313 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1092 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 886 | 21m | 244 km | 3,730.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 620 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 611 | 24m | 225 km | 2,370.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 610 | 1h 6m | 770 km | 8,103.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 544 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 398 | 27m | 275 km | 1,886.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 378 | 1h 50m | 1,423 km | 9,276.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 366 | 44m | 555 km | 3,504.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 348 | 44m | 241 km | 1,445.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 345 | 21m | 250 km | 1,490.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 327 | 24m | 218 km | 1,231.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 320 | 1h 40m | 1,156 km | 6,383.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 299 | 19m | 99 km | 512.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 293 | 27m | 215 km | 1,085.1 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 279 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 278 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 274 | 1h 14m | 961 km | 4,541.7 t |
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
| MULE44 | MUL | Mcchord Field (Joint Base Lewis-Mcchord) Airport (KTCM) | Travis Afb Airport (KSUU) | 2026-08-29 01:28 UTC | 2026-08-29 03:32 UTC | 2h 3m |
| VAR479 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-29 03:11 UTC | 2026-08-29 03:25 UTC | 13m |
| N57MQ |  | Trent Lott International Airport (KPQL) | Smith County Airport (MS39) | 2026-08-29 02:45 UTC | 2026-08-29 03:00 UTC | 15m |
| LBQ791 | LBQ | Brown County Airport (KGEO) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-29 02:51 UTC | 2026-08-29 02:59 UTC | 7m |
| N5641X |  | Marv Skie-Lincoln County Airport (KY14) | Sheldon Regional Airport (KSHL) | 2026-08-29 02:40 UTC | 2026-08-29 02:55 UTC | 15m |
| N149AH |  | KXFL (KXFL) | Peter O Knight Airport (KTPF) | 2026-08-29 01:57 UTC | 2026-08-29 02:54 UTC | 57m |
| PSBRR | PSB | Professor Urbano Ernesto Stumpf Airport (SBSJ) | Catanduva Airport (SDCD) | 2026-08-29 01:45 UTC | 2026-08-29 02:50 UTC | 1h 5m |
| N1920F |  | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-08-29 01:34 UTC | 2026-08-29 02:49 UTC | 1h 14m |
| IGO6190 | IndiGo | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-08-29 02:31 UTC | 2026-08-29 02:49 UTC | 17m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-08-29 02:21 UTC | 2026-08-29 02:48 UTC | 27m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Paihia Private Airport (NZPA) | 2026-08-29 02:16 UTC | 2026-08-29 02:47 UTC | 30m |
| N460AK |  | Ontario International Airport (KONT) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-29 01:56 UTC | 2026-08-29 02:46 UTC | 49m |
| QLK205D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-29 01:50 UTC | 2026-08-29 02:45 UTC | 54m |
| N805FA |  | Palo Alto Airport (KPAO) | Sierraville Dearwater Airport (KO79) | 2026-08-29 02:02 UTC | 2026-08-29 02:44 UTC | 42m |
| ZKHUP | ZKH | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-08-29 02:39 UTC | 2026-08-29 02:42 UTC | 3m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-29 02:21 UTC | 2026-08-29 02:42 UTC | 21m |
| AIC1AF | Air India | Juhu Aerodrome (VAJJ) | VARK (VARK) | 2026-08-29 02:07 UTC | 2026-08-29 02:42 UTC | 35m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-08-29 02:16 UTC | 2026-08-29 02:41 UTC | 25m |
| N456MT |  | Ocean County Airport (KMJX) | Central Jersey Regional Airport (K47N) | 2026-08-29 02:16 UTC | 2026-08-29 02:34 UTC | 18m |
| SWA236 | Southwest Airlines | Denver International Airport (KDEN) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-29 00:20 UTC | 2026-08-29 02:33 UTC | 2h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
