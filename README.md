# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_15:39:58_UTC-green)

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

**Latest saved flight:** 2026-08-16 15:39:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 15:39:58 UTC

- **204,966** saved flights
- **65,460** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,966** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,464,334.5 tonnes** estimated CO2 emissions
- **142,859,974 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8076 |
| 2 | SkyWest Airlines | 7357 |
| 3 | EJA | 3962 |
| 4 | IndiGo | 3510 |
| 5 | American Airlines | 3406 |
| 6 | Southwest Airlines | 3307 |
| 7 | Delta Air Lines | 2621 |
| 8 | ENY | 2550 |
| 9 | LATAM Airlines | 1921 |
| 10 | AZU | 1852 |
| 11 | Lufthansa | 1745 |
| 12 | Vueling | 1697 |
| 13 | WIF | 1649 |
| 14 | LXJ | 1608 |
| 15 | easyJet | 1416 |
| 16 | Swiss International | 1369 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1293 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1254 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1126 |
| 24 | GLO | 1103 |
| 25 | Air France | 1095 |
| 26 | PGT | 1094 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1047 |
| 29 | WMT | 1027 |
| 30 | CXK | 1012 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174058 |
| 2 | 🇪🇸 ES | 13109 |
| 3 | 🇧🇷 BR | 11722 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11300 |
| 6 | 🇮🇳 IN | 10955 |
| 7 | 🇮🇹 IT | 10668 |
| 8 | 🇩🇪 DE | 10153 |
| 9 | 🇬🇧 GB | 9571 |
| 10 | 🇯🇵 JP | 8452 |
| 11 | 🇫🇷 FR | 8124 |
| 12 | 🇨🇴 CO | 8087 |
| 13 | 🇬🇷 GR | 6036 |
| 14 | 🇹🇷 TR | 5792 |
| 15 | 🇲🇽 MX | 5754 |
| 16 | 🇨🇭 CH | 5492 |
| 17 | 🇳🇴 NO | 5113 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3442 |
| 20 | 🇵🇱 PL | 3382 |
| 21 | 🇹🇭 TH | 3242 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2572 |
| 25 | 🇰🇷 KR | 2503 |
| 26 | 🇭🇷 HR | 2191 |
| 27 | 🇲🇦 MA | 2064 |
| 28 | 🇳🇱 NL | 1833 |
| 29 | 🇲🇪 ME | 1716 |
| 30 | 🇮🇩 ID | 1684 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4293 |
| 2 | Denver International Airport |  | US | 3341 |
| 3 | Tokyo International Airport |  | JP | 2549 |
| 4 | Indira Gandhi International Airport |  | IN | 2484 |
| 5 | Guaymaral Airport |  | CO | 2482 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2143 |
| 8 | Zurich Airport |  | CH | 2141 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2123 |
| 10 | La Aurora Airport |  | GT | 1967 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1868 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1810 |
| 15 | Congonhas Airport |  | BR | 1709 |
| 16 | Frankfurt am Main International Airport |  | DE | 1700 |
| 17 | Madrid Barajas International Airport |  | ES | 1606 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1566 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1556 |
| 20 | Capua Airport |  | IT | 1554 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1481 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1411 |
| 25 | Charles de Gaulle International Airport |  | FR | 1404 |
| 26 | Charlotte/Douglas International Airport |  | US | 1393 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1274 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1260 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1233 |
| 32 | Barcelona International Airport |  | ES | 1222 |
| 33 | Seattle-Tacoma International Airport |  | US | 1216 |
| 34 | Viracopos International Airport |  | BR | 1187 |
| 35 | Calgary International Airport |  | CA | 1159 |
| 36 | Reno/Tahoe International Airport |  | US | 1134 |
| 37 | Oslo Gardermoen Airport |  | NO | 1133 |
| 38 | Vitoria/Foronda Airport |  | ES | 1130 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1021 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 387 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 343 | 27m | 275 km | 1,625.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 302 | 44m | 241 km | 1,254.4 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 255 | 24m | 218 km | 960.7 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 246 | 19m | 99 km | 421.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 241 | 1h 37m | 1,156 km | 4,807.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 217 | 28m | 152 km | 567.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-16 15:21 UTC | 2026-08-16 15:39 UTC | 18m |
| CHX50 | CHX | Hamburg Airport (EDDH) | Hamburg Airport (EDDH) | 2026-08-16 15:24 UTC | 2026-08-16 15:39 UTC | 14m |
| N7274L |  | Auburn University Regional Airport (KAUO) | St Pete-Clearwater International Airport (KPIE) | 2026-08-16 14:09 UTC | 2026-08-16 15:35 UTC | 1h 26m |
| AFR93SM | Air France | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-08-16 14:30 UTC | 2026-08-16 15:31 UTC | 1h 0m |
| N224E |  | W N C  Air Museum Airport (8NC9) | SC75 (SC75) | 2026-08-16 15:19 UTC | 2026-08-16 15:30 UTC | 10m |
| N6069F |  | Morristown Municipal Airport (KMMU) | NK07 (NK07) | 2026-08-16 15:05 UTC | 2026-08-16 15:26 UTC | 21m |
| N9469H |  | Mckinney Ntl Airport (KTKI) | Commerce Municipal Airport (K2F7) | 2026-08-16 15:00 UTC | 2026-08-16 15:22 UTC | 22m |
| PH957 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-16 13:24 UTC | 2026-08-16 15:21 UTC | 1h 56m |
| SKW5562 | SkyWest Airlines | Meadows Field (KBFL) | San Francisco International Airport (KSFO) | 2026-08-16 14:34 UTC | 2026-08-16 15:16 UTC | 42m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-16 15:00 UTC | 2026-08-16 15:16 UTC | 16m |
| CGMQD | CGM | CAP9 (CAP9) | Wilderman Farm Airport (CFT2) | 2026-08-16 14:52 UTC | 2026-08-16 15:15 UTC | 23m |
| N275TB |  | New Century Aircenter Airport (KIXD) | Johnson County Executive Airport (KOJC) | 2026-08-16 14:58 UTC | 2026-08-16 15:13 UTC | 14m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-16 14:50 UTC | 2026-08-16 15:11 UTC | 20m |
| SPORP | SPO | Szczecin-Dąbie Airport (EPSD) | Szczecin-Dąbie Airport (EPSD) | 2026-08-16 14:44 UTC | 2026-08-16 15:08 UTC | 24m |
| HK3554G |  | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 2026-08-16 11:05 UTC | 2026-08-16 15:07 UTC | 4h 2m |
| N995DA |  | Charlotte/Monroe Executive Airport (KEQY) | Mid-Carolina Regional Airport (KRUQ) | 2026-08-16 14:48 UTC | 2026-08-16 15:07 UTC | 18m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-08-16 14:36 UTC | 2026-08-16 15:06 UTC | 29m |
| N330V |  | Kintail Farm Airport (GA00) | Kintail Farm Airport (GA00) | 2026-08-16 14:53 UTC | 2026-08-16 15:06 UTC | 12m |
| N842EB |  | Broocke Air Patch Airport (FL95) | Sebastian Municipal Airport (KX26) | 2026-08-16 14:43 UTC | 2026-08-16 15:02 UTC | 18m |
| AXM71 | AXM | Kuala Lumpur International Airport (WMKK) | Naypyidaw Airport (VYEL) | 2026-08-16 12:30 UTC | 2026-08-16 15:00 UTC | 2h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
