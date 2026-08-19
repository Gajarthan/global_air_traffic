# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_13:42:43_UTC-green)

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

**Latest saved flight:** 2026-08-19 13:42:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 13:42:43 UTC

- **215,562** saved flights
- **68,047** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **215,562** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,593,801.6 tonnes** estimated CO2 emissions
- **150,365,309 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8605 |
| 2 | SkyWest Airlines | 7698 |
| 3 | EJA | 4184 |
| 4 | IndiGo | 3681 |
| 5 | American Airlines | 3584 |
| 6 | Southwest Airlines | 3432 |
| 7 | Delta Air Lines | 2772 |
| 8 | ENY | 2661 |
| 9 | LATAM Airlines | 2039 |
| 10 | AZU | 1967 |
| 11 | Vueling | 1816 |
| 12 | Lufthansa | 1807 |
| 13 | WIF | 1728 |
| 14 | LXJ | 1695 |
| 15 | easyJet | 1497 |
| 16 | Swiss International | 1437 |
| 17 | AXM | 1416 |
| 18 | United Airlines | 1362 |
| 19 | QLK | 1346 |
| 20 | EJU | 1341 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1183 |
| 24 | PGT | 1172 |
| 25 | Air France | 1165 |
| 26 | GLO | 1164 |
| 27 | WMT | 1121 |
| 28 | Wizz Air | 1094 |
| 29 | JetBlue | 1093 |
| 30 | AEE | 1083 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 181585 |
| 2 | 🇪🇸 ES | 13830 |
| 3 | 🇧🇷 BR | 12390 |
| 4 | 🇦🇺 AU | 12161 |
| 5 | 🇨🇦 CA | 11869 |
| 6 | 🇮🇳 IN | 11466 |
| 7 | 🇮🇹 IT | 11413 |
| 8 | 🇩🇪 DE | 10697 |
| 9 | 🇬🇧 GB | 10097 |
| 10 | 🇯🇵 JP | 8868 |
| 11 | 🇨🇴 CO | 8784 |
| 12 | 🇫🇷 FR | 8601 |
| 13 | 🇬🇷 GR | 6317 |
| 14 | 🇹🇷 TR | 6194 |
| 15 | 🇲🇽 MX | 6023 |
| 16 | 🇨🇭 CH | 5735 |
| 17 | 🇳🇴 NO | 5362 |
| 18 | 🇲🇾 MY | 3741 |
| 19 | 🇿🇦 ZA | 3660 |
| 20 | 🇵🇱 PL | 3558 |
| 21 | 🇹🇭 TH | 3527 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2735 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2360 |
| 27 | 🇲🇦 MA | 2169 |
| 28 | 🇳🇱 NL | 1920 |
| 29 | 🇲🇪 ME | 1876 |
| 30 | 🇮🇩 ID | 1813 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4516 |
| 2 | Denver International Airport |  | US | 3508 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2620 |
| 5 | Guaymaral Airport |  | CO | 2570 |
| 6 | Harry Reid International Airport |  | US | 2399 |
| 7 | Zurich Airport |  | CH | 2243 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2212 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2207 |
| 10 | La Aurora Airport |  | GT | 2079 |
| 11 | El Dorado International Airport |  | CO | 2009 |
| 12 | Chicago O'Hare International Airport |  | US | 1979 |
| 13 | Salt Lake City International Airport |  | US | 1900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1889 |
| 15 | Congonhas Airport |  | BR | 1804 |
| 16 | Frankfurt am Main International Airport |  | DE | 1767 |
| 17 | Madrid Barajas International Airport |  | ES | 1684 |
| 18 | Capua Airport |  | IT | 1640 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1618 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1606 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1582 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 24 | Malpensa International Airport |  | IT | 1511 |
| 25 | Charles de Gaulle International Airport |  | FR | 1482 |
| 26 | Charlotte/Douglas International Airport |  | US | 1448 |
| 27 | Kuala Lumpur International Airport |  | MY | 1377 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1322 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1319 |
| 31 | Bengaluru International Airport |  | IN | 1313 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1288 |
| 33 | Seattle-Tacoma International Airport |  | US | 1281 |
| 34 | Viracopos International Airport |  | BR | 1257 |
| 35 | Calgary International Airport |  | CA | 1217 |
| 36 | Oslo Gardermoen Airport |  | NO | 1196 |
| 37 | Vitoria/Foronda Airport |  | ES | 1192 |
| 38 | Reno/Tahoe International Airport |  | US | 1164 |
| 39 | Don Mueang International Airport |  | TH | 1164 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1163 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1051 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 769 | 21m | 244 km | 3,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 483 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 461 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 358 | 27m | 275 km | 1,696.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 316 | 1h 49m | 1,423 km | 7,755.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 283 | 21m | 250 km | 1,222.4 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 268 | 19m | 99 km | 459.1 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 264 | 27m | 215 km | 977.7 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 231 | 44m | 555 km | 2,211.9 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 231 | 1h 49m | 1,304 km | 5,196.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GECKO71 | GEC | Mackall Army Air Field (KHFF) | Mackall Army Air Field (KHFF) | 2026-08-19 13:08 UTC | 2026-08-19 13:42 UTC | 34m |
| N300PL |  | Warroad International Memorial Airport (KRRT) | Anoka County/Blaine (Janes Field) Airport (KANE) | 2026-08-19 12:50 UTC | 2026-08-19 13:41 UTC | 50m |
| TUTOR046 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-19 12:27 UTC | 2026-08-19 13:33 UTC | 1h 5m |
| CXK284 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-19 13:12 UTC | 2026-08-19 13:33 UTC | 20m |
| DENNN | DEN | Siegerland Airport (EDGS) | Siegerland Airport (EDGS) | 2026-08-19 12:38 UTC | 2026-08-19 13:32 UTC | 53m |
| FDB1595 | flydubai | Dubai International Airport (OMDB) | Simara Airport (VNSI) | 2026-08-19 09:44 UTC | 2026-08-19 13:30 UTC | 3h 46m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-19 12:44 UTC | 2026-08-19 13:29 UTC | 44m |
| SWR8PV | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-08-19 12:47 UTC | 2026-08-19 13:29 UTC | 41m |
| N954BS |  | Winter Haven Regional Airport (KGIF) | Gore Airport (4FL9) | 2026-08-19 13:16 UTC | 2026-08-19 13:28 UTC | 11m |
| N66P |  | SC52 (SC52) | Williamsport Airpark (SC86) | 2026-08-19 13:08 UTC | 2026-08-19 13:24 UTC | 16m |
| BBA35 | BBA | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Montréal (Mirabel) Airport (CYMX) | 2026-08-19 12:57 UTC | 2026-08-19 13:18 UTC | 21m |
| N677AA |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-08-19 13:02 UTC | 2026-08-19 13:18 UTC | 15m |
| LTA835 | LTA | Indianapolis International Airport (KIND) | Way West Airport (50II) | 2026-08-19 12:47 UTC | 2026-08-19 13:15 UTC | 28m |
| CXK160 | CXK | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-08-19 12:42 UTC | 2026-08-19 13:14 UTC | 31m |
| N564CH |  | Ocala International-Jim Taylor Field (KOCF) | Flying Cloud Airport (KFCM) | 2026-08-19 10:16 UTC | 2026-08-19 13:14 UTC | 2h 57m |
| N511R |  | Gwinnett County/Briscoe Field (KLZU) | K19A (K19A) | 2026-08-19 12:21 UTC | 2026-08-19 13:13 UTC | 52m |
| HBZJB | HBZ | LSMF (LSMF) | LSMF (LSMF) | 2026-08-19 12:54 UTC | 2026-08-19 13:12 UTC | 17m |
| GFLOH | GFL | Tilstock Airfield (EGCT) | Tilstock Airfield (EGCT) | 2026-08-19 12:11 UTC | 2026-08-19 13:11 UTC | 1h 0m |
| HBZVQ | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-08-19 12:26 UTC | 2026-08-19 13:11 UTC | 44m |
| ECKJQ | ECK | Zaragoza Air Base (LEZG) | Santander Airport (LEXJ) | 2026-08-19 12:21 UTC | 2026-08-19 13:10 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
