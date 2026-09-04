# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_00:03:13_UTC-green)

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

**Latest saved flight:** 2026-09-04 00:03:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 00:03:13 UTC

- **246,633** saved flights
- **74,430** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,633** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,967,105.2 tonnes** estimated CO2 emissions
- **172,006,098 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9876 |
| 2 | SkyWest Airlines | 8630 |
| 3 | EJA | 4758 |
| 4 | IndiGo | 4122 |
| 5 | American Airlines | 3963 |
| 6 | Southwest Airlines | 3682 |
| 7 | Delta Air Lines | 3131 |
| 8 | ENY | 2952 |
| 9 | LATAM Airlines | 2377 |
| 10 | AZU | 2293 |
| 11 | Vueling | 2110 |
| 12 | WIF | 1975 |
| 13 | Lufthansa | 1968 |
| 14 | LXJ | 1913 |
| 15 | easyJet | 1710 |
| 16 | Swiss International | 1658 |
| 17 | AXM | 1616 |
| 18 | EJU | 1588 |
| 19 | QLK | 1579 |
| 20 | United Airlines | 1552 |
| 21 | Alaska Airlines | 1472 |
| 22 | All Nippon Airways | 1449 |
| 23 | WMT | 1387 |
| 24 | GLO | 1378 |
| 25 | VIV | 1356 |
| 26 | PGT | 1350 |
| 27 | Air France | 1347 |
| 28 | Wizz Air | 1335 |
| 29 | JetBlue | 1217 |
| 30 | AEE | 1214 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 204564 |
| 2 | 🇪🇸 ES | 15806 |
| 3 | 🇧🇷 BR | 14406 |
| 4 | 🇦🇺 AU | 14019 |
| 5 | 🇨🇦 CA | 13727 |
| 6 | 🇮🇹 IT | 13500 |
| 7 | 🇮🇳 IN | 12854 |
| 8 | 🇩🇪 DE | 12142 |
| 9 | 🇬🇧 GB | 11599 |
| 10 | 🇨🇴 CO | 10734 |
| 11 | 🇫🇷 FR | 9945 |
| 12 | 🇯🇵 JP | 9775 |
| 13 | 🇹🇷 TR | 7318 |
| 14 | 🇬🇷 GR | 7264 |
| 15 | 🇲🇽 MX | 6816 |
| 16 | 🇨🇭 CH | 6630 |
| 17 | 🇳🇴 NO | 6122 |
| 18 | 🇹🇭 TH | 4446 |
| 19 | 🇲🇾 MY | 4331 |
| 20 | 🇿🇦 ZA | 4275 |
| 21 | 🇵🇱 PL | 4131 |
| 22 | 🇳🇿 NZ | 3372 |
| 23 | 🇵🇭 PH | 3364 |
| 24 | 🇬🇹 GT | 3086 |
| 25 | 🇰🇷 KR | 2880 |
| 26 | 🇭🇷 HR | 2834 |
| 27 | 🇲🇦 MA | 2492 |
| 28 | 🇲🇪 ME | 2302 |
| 29 | 🇳🇱 NL | 2229 |
| 30 | 🇮🇩 ID | 2142 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5081 |
| 2 | Denver International Airport |  | US | 3990 |
| 3 | Indira Gandhi International Airport |  | IN | 3002 |
| 4 | Tokyo International Airport |  | JP | 2915 |
| 5 | Guaymaral Airport |  | CO | 2721 |
| 6 | Harry Reid International Airport |  | US | 2629 |
| 7 | Zurich Airport |  | CH | 2585 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2511 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2454 |
| 10 | El Dorado International Airport |  | CO | 2452 |
| 11 | La Aurora Airport |  | GT | 2348 |
| 12 | Salt Lake City International Airport |  | US | 2187 |
| 13 | Chicago O'Hare International Airport |  | US | 2168 |
| 14 | Congonhas Airport |  | BR | 2116 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2034 |
| 16 | Capua Airport |  | IT | 1940 |
| 17 | Frankfurt am Main International Airport |  | DE | 1938 |
| 18 | Madrid Barajas International Airport |  | ES | 1930 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1855 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1806 |
| 21 | Malpensa International Airport |  | IT | 1765 |
| 22 | Charles de Gaulle International Airport |  | FR | 1733 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1727 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1726 |
| 25 | Ninoy Aquino International Airport |  | PH | 1637 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1608 |
| 28 | Charlotte/Douglas International Airport |  | US | 1570 |
| 29 | Barcelona International Airport |  | ES | 1563 |
| 30 | Kuala Lumpur International Airport |  | MY | 1560 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1507 |
| 32 | Viracopos International Airport |  | BR | 1467 |
| 33 | Seattle-Tacoma International Airport |  | US | 1450 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1436 |
| 35 | Don Mueang International Airport |  | TH | 1428 |
| 36 | Bengaluru International Airport |  | IN | 1424 |
| 37 | Calgary International Airport |  | CA | 1420 |
| 38 | Oslo Gardermoen Airport |  | NO | 1389 |
| 39 | Vancouver International Airport |  | CA | 1380 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1343 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 913 | 21m | 244 km | 3,844.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 646 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 553 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 406 | 27m | 275 km | 1,923.9 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 390 | 1h 50m | 1,423 km | 9,571.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 364 | 44m | 241 km | 1,512.0 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 343 | 24m | 218 km | 1,292.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 332 | 23m | 55 km | 315.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 331 | 1h 39m | 1,156 km | 6,603.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 305 | 26m | 215 km | 1,129.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 291 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 285 | 1h 14m | 961 km | 4,724.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 281 | 19m | 144 km | 699.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 268 | 1h 50m | 1,304 km | 6,029.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N239FG |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-09-03 23:24 UTC | 2026-09-04 00:03 UTC | 38m |
| N957DJ |  | Brackett Field (KPOC) | Van Nuys Airport (KVNY) | 2026-09-03 23:47 UTC | 2026-09-04 00:01 UTC | 13m |
| REPR12 | REP | Newcastle Airport (YWLM) | Gloucester Airport (YGCR) | 2026-09-03 23:02 UTC | 2026-09-03 23:58 UTC | 56m |
| OUA34 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Jirik Field (OL23) | 2026-09-03 23:07 UTC | 2026-09-03 23:53 UTC | 45m |
| CHX87 | CHX | Landshut Airport (EDML) | Oberschleisheim Airfield (EDNX) | 2026-09-03 23:33 UTC | 2026-09-03 23:52 UTC | 18m |
| JBU2954 | JetBlue | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-03 22:37 UTC | 2026-09-03 23:49 UTC | 1h 11m |
| N971MB |  | 5NE6 (5NE6) | Eagle Soaring Airport (1CD4) | 2026-09-03 23:02 UTC | 2026-09-03 23:47 UTC | 44m |
| N605LF |  | Springfield-Branson Ntl Airport (KSGF) | Nashville International Airport (KBNA) | 2026-09-03 22:44 UTC | 2026-09-03 23:44 UTC | 1h 0m |
| N323CW |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-09-03 23:40 UTC | 2026-09-03 23:44 UTC | 3m |
| N222VR |  | Montgomery-Gibbs Executive Airport (KMYF) | Phoenix Sky Harbor International Airport (KPHX) | 2026-09-03 22:52 UTC | 2026-09-03 23:44 UTC | 51m |
| N520MD |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-09-03 23:23 UTC | 2026-09-03 23:42 UTC | 19m |
| N1WG |  | Rocky Mountain Metro Airport (KBJC) | Mesa 1 Airport (81CO) | 2026-09-03 23:19 UTC | 2026-09-03 23:38 UTC | 18m |
| N221RC |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-09-03 22:56 UTC | 2026-09-03 23:36 UTC | 39m |
| CGSWV | CGS | Vancouver International Airport (CYVR) | Schmidt Ranch Airport (1WN0) | 2026-09-03 22:31 UTC | 2026-09-03 23:34 UTC | 1h 2m |
| NJL | NJL | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-03 23:19 UTC | 2026-09-03 23:33 UTC | 13m |
| N9918Q |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-09-03 23:07 UTC | 2026-09-03 23:32 UTC | 25m |
| N707PV |  | Pegasus Airpark (5AZ3) | Payson Airport (KPAN) | 2026-09-03 21:42 UTC | 2026-09-03 23:32 UTC | 1h 49m |
| 404LR |  | John C Tune Airport (KJWN) | Hawkins County Airport (KRVN) | 2026-09-03 22:57 UTC | 2026-09-03 23:31 UTC | 33m |
| N466UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-09-03 20:08 UTC | 2026-09-03 23:27 UTC | 3h 18m |
| N66049 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-03 22:57 UTC | 2026-09-03 23:24 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
