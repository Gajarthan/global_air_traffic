# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_23:09:10_UTC-green)

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

**Latest saved flight:** 2026-09-04 23:09:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-04 23:09:10 UTC

- **247,801** saved flights
- **74,689** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,801** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,980,692.0 tonnes** estimated CO2 emissions
- **172,793,739 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9930 |
| 2 | SkyWest Airlines | 8662 |
| 3 | EJA | 4789 |
| 4 | IndiGo | 4134 |
| 5 | American Airlines | 3975 |
| 6 | Southwest Airlines | 3692 |
| 7 | Delta Air Lines | 3147 |
| 8 | ENY | 2966 |
| 9 | LATAM Airlines | 2392 |
| 10 | AZU | 2311 |
| 11 | Vueling | 2117 |
| 12 | WIF | 1983 |
| 13 | Lufthansa | 1970 |
| 14 | LXJ | 1925 |
| 15 | easyJet | 1714 |
| 16 | Swiss International | 1662 |
| 17 | AXM | 1619 |
| 18 | EJU | 1591 |
| 19 | QLK | 1588 |
| 20 | United Airlines | 1557 |
| 21 | Alaska Airlines | 1479 |
| 22 | All Nippon Airways | 1452 |
| 23 | WMT | 1398 |
| 24 | GLO | 1382 |
| 25 | VIV | 1361 |
| 26 | PGT | 1355 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1337 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205626 |
| 2 | 🇪🇸 ES | 15869 |
| 3 | 🇧🇷 BR | 14500 |
| 4 | 🇦🇺 AU | 14071 |
| 5 | 🇨🇦 CA | 13783 |
| 6 | 🇮🇹 IT | 13565 |
| 7 | 🇮🇳 IN | 12897 |
| 8 | 🇩🇪 DE | 12178 |
| 9 | 🇬🇧 GB | 11641 |
| 10 | 🇨🇴 CO | 10818 |
| 11 | 🇫🇷 FR | 9978 |
| 12 | 🇯🇵 JP | 9788 |
| 13 | 🇹🇷 TR | 7367 |
| 14 | 🇬🇷 GR | 7285 |
| 15 | 🇲🇽 MX | 6853 |
| 16 | 🇨🇭 CH | 6671 |
| 17 | 🇳🇴 NO | 6147 |
| 18 | 🇹🇭 TH | 4462 |
| 19 | 🇲🇾 MY | 4345 |
| 20 | 🇿🇦 ZA | 4281 |
| 21 | 🇵🇱 PL | 4146 |
| 22 | 🇳🇿 NZ | 3388 |
| 23 | 🇵🇭 PH | 3372 |
| 24 | 🇬🇹 GT | 3097 |
| 25 | 🇰🇷 KR | 2884 |
| 26 | 🇭🇷 HR | 2844 |
| 27 | 🇲🇦 MA | 2505 |
| 28 | 🇲🇪 ME | 2313 |
| 29 | 🇳🇱 NL | 2234 |
| 30 | 🇮🇩 ID | 2145 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5106 |
| 2 | Denver International Airport |  | US | 4004 |
| 3 | Indira Gandhi International Airport |  | IN | 3015 |
| 4 | Tokyo International Airport |  | JP | 2920 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2647 |
| 7 | Zurich Airport |  | CH | 2592 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2521 |
| 9 | El Dorado International Airport |  | CO | 2477 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2459 |
| 11 | La Aurora Airport |  | GT | 2357 |
| 12 | Salt Lake City International Airport |  | US | 2194 |
| 13 | Chicago O'Hare International Airport |  | US | 2174 |
| 14 | Congonhas Airport |  | BR | 2129 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2042 |
| 16 | Capua Airport |  | IT | 1948 |
| 17 | Madrid Barajas International Airport |  | ES | 1944 |
| 18 | Frankfurt am Main International Airport |  | DE | 1941 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1862 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1812 |
| 21 | Malpensa International Airport |  | IT | 1777 |
| 22 | Charles de Gaulle International Airport |  | FR | 1739 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1736 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1727 |
| 25 | Ninoy Aquino International Airport |  | PH | 1641 |
| 26 | Macau International Airport |  | MO | 1633 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1625 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Barcelona International Airport |  | ES | 1567 |
| 30 | Kuala Lumpur International Airport |  | MY | 1565 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1515 |
| 32 | Viracopos International Airport |  | BR | 1481 |
| 33 | Seattle-Tacoma International Airport |  | US | 1459 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1443 |
| 35 | Don Mueang International Airport |  | TH | 1434 |
| 36 | Calgary International Airport |  | CA | 1429 |
| 37 | Bengaluru International Airport |  | IN | 1426 |
| 38 | Oslo Gardermoen Airport |  | NO | 1395 |
| 39 | Vancouver International Airport |  | CA | 1387 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1346 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 919 | 21m | 244 km | 3,869.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 653 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 628 | 24m | 225 km | 2,436.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 620 | 1h 6m | 770 km | 8,236.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 394 | 1h 50m | 1,423 km | 9,669.4 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 382 | 44m | 555 km | 3,657.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 346 | 24m | 218 km | 1,303.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 292 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 269 | 1h 50m | 1,304 km | 6,051.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AUA73 | Austrian Airlines | Vienna International Airport (LOWW) | HE12 (HE12) | 2026-09-04 20:22 UTC | 2026-09-04 23:09 UTC | 2h 47m |
| N4146P |  | Lakeway Airpark (K3R9) | Burnet Municipal/Kate Craddock Field (KBMQ) | 2026-09-04 22:49 UTC | 2026-09-04 23:05 UTC | 15m |
| CXK605 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-04 22:16 UTC | 2026-09-04 23:05 UTC | 48m |
| BLK2385 | BLK | Van Nuys Airport (KVNY) | Mesawood Airport (6CO2) | 2026-09-04 21:41 UTC | 2026-09-04 23:04 UTC | 1h 23m |
| N415XT |  | Watsonville Municipal Airport (KWVI) | Santa Monica Municipal Airport (KSMO) | 2026-09-04 21:56 UTC | 2026-09-04 22:58 UTC | 1h 2m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-04 22:40 UTC | 2026-09-04 22:58 UTC | 17m |
| N32WX |  | General Dick Stout Field (K1L8) | Crystal Springs Ranch Airport (UT54) | 2026-09-04 19:52 UTC | 2026-09-04 22:52 UTC | 2h 59m |
| TWY944 | TWY | Charles M Schulz/Sonoma County Airport (KSTS) | Telluride Regional Airport (KTEX) | 2026-09-04 21:16 UTC | 2026-09-04 22:44 UTC | 1h 27m |
| N1620 |  | Fulton County Executive/Charlie Brown Field (KFTY) | Gaylord Regional Airport (KGLR) | 2026-09-04 21:10 UTC | 2026-09-04 22:40 UTC | 1h 29m |
| N33079 |  | Treasure Coast International Airport (KFPR) | Treasure Coast International Airport (KFPR) | 2026-09-04 22:38 UTC | 2026-09-04 22:38 UTC | 0m |
| N420DP |  | William P Hobby Airport (KHOU) | Travis Airport (LA63) | 2026-09-04 21:57 UTC | 2026-09-04 22:35 UTC | 38m |
| N869CP |  | French Valley Airport (KF70) | Whiteman Airport (KWHP) | 2026-09-04 21:39 UTC | 2026-09-04 22:34 UTC | 55m |
| N470BC |  | Watsonville Municipal Airport (KWVI) | Rogers Field (KO05) | 2026-09-04 21:27 UTC | 2026-09-04 22:31 UTC | 1h 3m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-09-04 22:11 UTC | 2026-09-04 22:29 UTC | 18m |
| N562LD |  | Long Beach (Daugherty Field) Airport (KLGB) | Meadows Field (KBFL) | 2026-09-04 22:05 UTC | 2026-09-04 22:28 UTC | 22m |
| N842WF |  | Boeing Field/King County International Airport (KBFI) | WA47 (WA47) | 2026-09-04 22:02 UTC | 2026-09-04 22:27 UTC | 25m |
| N6182A |  | Bolingbrook's Clow International Airport (K1C5) | Eldon Model Airpark (KH79) | 2026-09-04 21:17 UTC | 2026-09-04 22:27 UTC | 1h 9m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-04 20:34 UTC | 2026-09-04 22:27 UTC | 1h 52m |
| N650MC |  | Mc Clellan-Palomar Airport (KCRQ) | K36U (K36U) | 2026-09-04 20:35 UTC | 2026-09-04 22:26 UTC | 1h 51m |
| N416NH |  | Des Moines International Airport (KDSM) | Jesse Viertel Memorial Airport (KVER) | 2026-09-04 21:50 UTC | 2026-09-04 22:25 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
