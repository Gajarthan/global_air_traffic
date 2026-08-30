# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_17:13:48_UTC-green)

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

**Latest saved flight:** 2026-08-30 17:13:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-30 17:13:48 UTC

- **241,917** saved flights
- **73,347** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **241,917** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,912,045.7 tonnes** estimated CO2 emissions
- **168,814,244 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9706 |
| 2 | SkyWest Airlines | 8483 |
| 3 | EJA | 4674 |
| 4 | IndiGo | 4076 |
| 5 | American Airlines | 3895 |
| 6 | Southwest Airlines | 3636 |
| 7 | Delta Air Lines | 3081 |
| 8 | ENY | 2916 |
| 9 | LATAM Airlines | 2316 |
| 10 | AZU | 2244 |
| 11 | Vueling | 2079 |
| 12 | Lufthansa | 1946 |
| 13 | WIF | 1916 |
| 14 | LXJ | 1874 |
| 15 | easyJet | 1687 |
| 16 | Swiss International | 1633 |
| 17 | AXM | 1599 |
| 18 | EJU | 1550 |
| 19 | QLK | 1544 |
| 20 | United Airlines | 1519 |
| 21 | Alaska Airlines | 1444 |
| 22 | All Nippon Airways | 1431 |
| 23 | WMT | 1360 |
| 24 | GLO | 1349 |
| 25 | VIV | 1326 |
| 26 | Air France | 1323 |
| 27 | PGT | 1323 |
| 28 | Wizz Air | 1307 |
| 29 | JetBlue | 1197 |
| 30 | AEE | 1196 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200431 |
| 2 | 🇪🇸 ES | 15557 |
| 3 | 🇧🇷 BR | 14082 |
| 4 | 🇦🇺 AU | 13712 |
| 5 | 🇨🇦 CA | 13454 |
| 6 | 🇮🇹 IT | 13248 |
| 7 | 🇮🇳 IN | 12687 |
| 8 | 🇩🇪 DE | 11946 |
| 9 | 🇬🇧 GB | 11425 |
| 10 | 🇨🇴 CO | 10413 |
| 11 | 🇫🇷 FR | 9758 |
| 12 | 🇯🇵 JP | 9702 |
| 13 | 🇹🇷 TR | 7177 |
| 14 | 🇬🇷 GR | 7134 |
| 15 | 🇲🇽 MX | 6675 |
| 16 | 🇨🇭 CH | 6506 |
| 17 | 🇳🇴 NO | 5970 |
| 18 | 🇹🇭 TH | 4390 |
| 19 | 🇲🇾 MY | 4285 |
| 20 | 🇿🇦 ZA | 4223 |
| 21 | 🇵🇱 PL | 4064 |
| 22 | 🇳🇿 NZ | 3328 |
| 23 | 🇵🇭 PH | 3317 |
| 24 | 🇬🇹 GT | 3037 |
| 25 | 🇰🇷 KR | 2856 |
| 26 | 🇭🇷 HR | 2793 |
| 27 | 🇲🇦 MA | 2447 |
| 28 | 🇲🇪 ME | 2259 |
| 29 | 🇳🇱 NL | 2191 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4996 |
| 2 | Denver International Airport |  | US | 3901 |
| 3 | Indira Gandhi International Airport |  | IN | 2956 |
| 4 | Tokyo International Airport |  | JP | 2889 |
| 5 | Guaymaral Airport |  | CO | 2705 |
| 6 | Harry Reid International Airport |  | US | 2570 |
| 7 | Zurich Airport |  | CH | 2542 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2473 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2411 |
| 10 | El Dorado International Airport |  | CO | 2358 |
| 11 | La Aurora Airport |  | GT | 2314 |
| 12 | Chicago O'Hare International Airport |  | US | 2149 |
| 13 | Salt Lake City International Airport |  | US | 2130 |
| 14 | Congonhas Airport |  | BR | 2059 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2001 |
| 16 | Frankfurt am Main International Airport |  | DE | 1917 |
| 17 | Capua Airport |  | IT | 1909 |
| 18 | Madrid Barajas International Airport |  | ES | 1901 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1815 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1781 |
| 21 | Malpensa International Airport |  | IT | 1731 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1708 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1697 |
| 24 | Charles de Gaulle International Airport |  | FR | 1693 |
| 25 | Macau International Airport |  | MO | 1616 |
| 26 | Ninoy Aquino International Airport |  | PH | 1611 |
| 27 | Charlotte/Douglas International Airport |  | US | 1548 |
| 28 | Kuala Lumpur International Airport |  | MY | 1546 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1542 |
| 30 | Barcelona International Airport |  | ES | 1542 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1461 |
| 32 | Viracopos International Airport |  | BR | 1435 |
| 33 | Don Mueang International Airport |  | TH | 1413 |
| 34 | Seattle-Tacoma International Airport |  | US | 1411 |
| 35 | Bengaluru International Airport |  | IN | 1407 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1404 |
| 37 | Calgary International Airport |  | CA | 1388 |
| 38 | Oslo Gardermoen Airport |  | NO | 1358 |
| 39 | Vancouver International Airport |  | CA | 1337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1321 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1096 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 891 | 21m | 244 km | 3,751.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 623 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 615 | 24m | 225 km | 2,385.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 370 | 44m | 555 km | 3,542.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 352 | 44m | 241 km | 1,462.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 331 | 24m | 218 km | 1,247.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 301 | 19m | 99 km | 515.6 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 295 | 26m | 215 km | 1,092.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 284 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 280 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 276 | 1h 14m | 961 km | 4,574.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 273 | 19m | 144 km | 679.1 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 259 | 1h 50m | 1,304 km | 5,826.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 248 | 28m | 152 km | 648.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N43375 |  | Crow Island Airport (8MA4) | Sids Airport (MA52) | 2026-08-30 15:52 UTC | 2026-08-30 17:13 UTC | 1h 21m |
| MVK55 | MVK | Mankato Regional Airport (KMKT) | 6MN8 (6MN8) | 2026-08-30 16:29 UTC | 2026-08-30 17:08 UTC | 38m |
| N278FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-30 16:11 UTC | 2026-08-30 17:04 UTC | 53m |
| SPSCZ | SPS | Tocna Praha Glider Airport (LKTC) | Wrocław-Szymanow Airport (EPWS) | 2026-08-30 16:07 UTC | 2026-08-30 17:03 UTC | 55m |
| SKW5819 | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | Carlson Airport (9WI9) | 2026-08-30 16:02 UTC | 2026-08-30 17:00 UTC | 58m |
| ZKICU | ZKI | Gore3 Airport (NZGC) | Invercargill Airport (NZNV) | 2026-08-30 16:28 UTC | 2026-08-30 16:59 UTC | 31m |
| N61633 |  | Danbury Municipal Airport (KDXR) | CT66 (CT66) | 2026-08-30 16:29 UTC | 2026-08-30 16:57 UTC | 28m |
|  |  | Joseph A Hardy Connellsville Airport (KVVS) | Joseph A Hardy Connellsville Airport (KVVS) | 2026-08-30 16:50 UTC | 2026-08-30 16:50 UTC | 0m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-08-30 16:11 UTC | 2026-08-30 16:45 UTC | 34m |
| N814SS |  | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-08-30 16:27 UTC | 2026-08-30 16:43 UTC | 16m |
| N400DG |  | Colonel James Jabara Airport (KAAO) | Miller Airport (MO99) | 2026-08-30 16:08 UTC | 2026-08-30 16:40 UTC | 32m |
| N2AV |  | Mulino State Airport (K4S9) | Mulino State Airport (K4S9) | 2026-08-30 16:26 UTC | 2026-08-30 16:40 UTC | 14m |
| MNB1300 | MNB | Istanbul Hezarfen Airfield (LTBW) | Zhuhai Airport (ZGSD) | 2026-08-30 04:23 UTC | 2026-08-30 16:39 UTC | 12h 16m |
| QTR8500 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-30 08:56 UTC | 2026-08-30 16:36 UTC | 7h 40m |
| N350BV |  | Meadows Field (KBFL) | Palm Springs International Airport (KPSP) | 2026-08-30 16:06 UTC | 2026-08-30 16:35 UTC | 29m |
| N354WG |  | Scottsdale Airport (KSDL) | NM25 (NM25) | 2026-08-30 15:50 UTC | 2026-08-30 16:35 UTC | 45m |
| N7277F |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-30 16:21 UTC | 2026-08-30 16:35 UTC | 13m |
| N229LA |  | Compton/Woodley Airport (KCPM) | Bob Hope Airport (KBUR) | 2026-08-30 15:12 UTC | 2026-08-30 16:33 UTC | 1h 21m |
| HBFPC | HBF | Reggio Calabria Airport (LICR) | Sion Airport (LSGS) | 2026-08-30 13:41 UTC | 2026-08-30 16:30 UTC | 2h 49m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-08-30 15:54 UTC | 2026-08-30 16:30 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
