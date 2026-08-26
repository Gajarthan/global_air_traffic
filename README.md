# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_14:49:29_UTC-green)

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

**Latest saved flight:** 2026-08-26 14:49:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-26 14:49:29 UTC

- **238,756** saved flights
- **72,653** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **238,756** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,876,985.1 tonnes** estimated CO2 emissions
- **166,781,747 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9594 |
| 2 | SkyWest Airlines | 8392 |
| 3 | EJA | 4619 |
| 4 | IndiGo | 4031 |
| 5 | American Airlines | 3857 |
| 6 | Southwest Airlines | 3614 |
| 7 | Delta Air Lines | 3039 |
| 8 | ENY | 2884 |
| 9 | LATAM Airlines | 2293 |
| 10 | AZU | 2225 |
| 11 | Vueling | 2056 |
| 12 | Lufthansa | 1934 |
| 13 | WIF | 1898 |
| 14 | LXJ | 1852 |
| 15 | easyJet | 1666 |
| 16 | Swiss International | 1607 |
| 17 | AXM | 1591 |
| 18 | EJU | 1534 |
| 19 | QLK | 1527 |
| 20 | United Airlines | 1505 |
| 21 | Alaska Airlines | 1430 |
| 22 | All Nippon Airways | 1422 |
| 23 | WMT | 1341 |
| 24 | GLO | 1332 |
| 25 | VIV | 1314 |
| 26 | Air France | 1303 |
| 27 | PGT | 1303 |
| 28 | Wizz Air | 1281 |
| 29 | AEE | 1184 |
| 30 | JetBlue | 1183 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 197690 |
| 2 | 🇪🇸 ES | 15367 |
| 3 | 🇧🇷 BR | 13934 |
| 4 | 🇦🇺 AU | 13573 |
| 5 | 🇨🇦 CA | 13199 |
| 6 | 🇮🇹 IT | 13063 |
| 7 | 🇮🇳 IN | 12553 |
| 8 | 🇩🇪 DE | 11809 |
| 9 | 🇬🇧 GB | 11279 |
| 10 | 🇨🇴 CO | 10172 |
| 11 | 🇯🇵 JP | 9652 |
| 12 | 🇫🇷 FR | 9623 |
| 13 | 🇹🇷 TR | 7098 |
| 14 | 🇬🇷 GR | 7036 |
| 15 | 🇲🇽 MX | 6611 |
| 16 | 🇨🇭 CH | 6413 |
| 17 | 🇳🇴 NO | 5918 |
| 18 | 🇹🇭 TH | 4336 |
| 19 | 🇲🇾 MY | 4263 |
| 20 | 🇿🇦 ZA | 4199 |
| 21 | 🇵🇱 PL | 3978 |
| 22 | 🇵🇭 PH | 3292 |
| 23 | 🇳🇿 NZ | 3291 |
| 24 | 🇬🇹 GT | 2995 |
| 25 | 🇰🇷 KR | 2842 |
| 26 | 🇭🇷 HR | 2764 |
| 27 | 🇲🇦 MA | 2417 |
| 28 | 🇲🇪 ME | 2232 |
| 29 | 🇳🇱 NL | 2160 |
| 30 | 🇮🇩 ID | 2101 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4937 |
| 2 | Denver International Airport |  | US | 3854 |
| 3 | Indira Gandhi International Airport |  | IN | 2921 |
| 4 | Tokyo International Airport |  | JP | 2873 |
| 5 | Guaymaral Airport |  | CO | 2692 |
| 6 | Harry Reid International Airport |  | US | 2543 |
| 7 | Zurich Airport |  | CH | 2505 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2438 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2385 |
| 10 | El Dorado International Airport |  | CO | 2292 |
| 11 | La Aurora Airport |  | GT | 2285 |
| 12 | Chicago O'Hare International Airport |  | US | 2133 |
| 13 | Salt Lake City International Airport |  | US | 2096 |
| 14 | Congonhas Airport |  | BR | 2030 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1987 |
| 16 | Frankfurt am Main International Airport |  | DE | 1895 |
| 17 | Capua Airport |  | IT | 1881 |
| 18 | Madrid Barajas International Airport |  | ES | 1874 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1800 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1758 |
| 21 | Malpensa International Airport |  | IT | 1713 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1684 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1680 |
| 24 | Charles de Gaulle International Airport |  | FR | 1667 |
| 25 | Macau International Airport |  | MO | 1614 |
| 26 | Ninoy Aquino International Airport |  | PH | 1597 |
| 27 | Kuala Lumpur International Airport |  | MY | 1540 |
| 28 | Charlotte/Douglas International Airport |  | US | 1530 |
| 29 | Barcelona International Airport |  | ES | 1522 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1497 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1446 |
| 32 | Viracopos International Airport |  | BR | 1426 |
| 33 | Don Mueang International Airport |  | TH | 1400 |
| 34 | Bengaluru International Airport |  | IN | 1398 |
| 35 | Seattle-Tacoma International Airport |  | US | 1392 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1390 |
| 37 | Calgary International Airport |  | CA | 1369 |
| 38 | Oslo Gardermoen Airport |  | NO | 1344 |
| 39 | O. R. Tambo International Airport |  | ZA | 1308 |
| 40 | Vancouver International Airport |  | CA | 1305 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1090 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 877 | 21m | 244 km | 3,692.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 609 | 24m | 225 km | 2,362.6 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 607 | 1h 6m | 770 km | 8,063.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 605 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 539 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 394 | 27m | 275 km | 1,867.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 373 | 1h 50m | 1,423 km | 9,154.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 365 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 361 | 44m | 555 km | 3,456.7 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 346 | 44m | 241 km | 1,437.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 342 | 21m | 250 km | 1,477.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 323 | 24m | 218 km | 1,216.9 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 318 | 1h 40m | 1,156 km | 6,344.0 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 318 | 22m | 55 km | 302.3 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 297 | 19m | 99 km | 508.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 292 | 27m | 215 km | 1,081.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 277 | 13m | - | - |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 270 | 19m | 144 km | 671.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 263 | 15m | 154 km | 696.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 256 | 1h 50m | 1,304 km | 5,759.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BL50J |  | Pensacola International Airport (KPNS) | Peter Prince Field (K2R4) | 2026-08-26 13:59 UTC | 2026-08-26 14:49 UTC | 50m |
| SAMU66 | SAM | Ampuriabrava Airport (LEAP) | Perpignan-Rivesaltes (Llabanere) Airport (LFMP) | 2026-08-26 14:32 UTC | 2026-08-26 14:44 UTC | 12m |
| WING49 | WIN | St Pete-Clearwater International Airport (KPIE) | Macdill Afb Airport (KMCF) | 2026-08-26 12:20 UTC | 2026-08-26 14:43 UTC | 2h 22m |
| HBZPV | HBZ | Speck-Fehraltorf Airport (LSZK) | LSMF (LSMF) | 2026-08-26 14:07 UTC | 2026-08-26 14:40 UTC | 33m |
| N213MP |  | Wagner Field (1TN3) | Pryor Field Regional Airport (KDCU) | 2026-08-26 13:47 UTC | 2026-08-26 14:37 UTC | 50m |
| CONGO64 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-08-26 13:13 UTC | 2026-08-26 14:36 UTC | 1h 23m |
| CGJVM | CGJ | Montréal / St-Hubert Airport (CYHU) | Montréal / St-Hubert Airport (CYHU) | 2026-08-26 12:58 UTC | 2026-08-26 14:35 UTC | 1h 37m |
| CXK146 | CXK | Morristown Municipal Airport (KMMU) | Morristown Municipal Airport (KMMU) | 2026-08-26 13:58 UTC | 2026-08-26 14:35 UTC | 36m |
| N786FA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-26 13:55 UTC | 2026-08-26 14:33 UTC | 38m |
| TVF414K | TVF | Toulon-Hyeres Airport (LFTH) | Paris-Orly Airport (LFPO) | 2026-08-26 13:17 UTC | 2026-08-26 14:33 UTC | 1h 15m |
| SHERPA9 | SHE | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-08-26 14:17 UTC | 2026-08-26 14:29 UTC | 12m |
| CAN14 | CAN | Pescara International Airport (LIBP) | Pescara International Airport (LIBP) | 2026-08-26 13:16 UTC | 2026-08-26 14:29 UTC | 1h 12m |
| LSI113 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-26 03:33 UTC | 2026-08-26 14:28 UTC | 10h 55m |
| VAR479 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-26 14:06 UTC | 2026-08-26 14:28 UTC | 21m |
| MDEEP | MDE | Villacoublay-Velizy (BA 107) Air Base (LFPV) | Caen-Carpiquet Airport (LFRK) | 2026-08-26 13:42 UTC | 2026-08-26 14:27 UTC | 44m |
| N92N |  | Newark Liberty International Airport (KEWR) | John F Kennedy International Airport (KJFK) | 2026-08-26 14:06 UTC | 2026-08-26 14:25 UTC | 19m |
| N6384D |  | Reno/Tahoe International Airport (KRNO) | Reno/Tahoe International Airport (KRNO) | 2026-08-26 13:48 UTC | 2026-08-26 14:24 UTC | 35m |
| N5NJ |  | Trenton Mercer Airport (KTTN) | Princeton Airport (K39N) | 2026-08-26 14:16 UTC | 2026-08-26 14:21 UTC | 5m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-26 06:47 UTC | 2026-08-26 14:21 UTC | 7h 33m |
| LRS1066 | LRS | Juan Santamaria International Airport (MROC) | Ciruelas Airport (MRCI) | 2026-08-26 13:50 UTC | 2026-08-26 14:18 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
