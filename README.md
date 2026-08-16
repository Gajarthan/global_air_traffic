# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_01:33:27_UTC-green)

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

**Latest saved flight:** 2026-08-16 01:33:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 01:33:27 UTC

- **202,034** saved flights
- **64,028** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **202,034** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,423,093.0 tonnes** estimated CO2 emissions
- **140,469,157 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7990 |
| 2 | SkyWest Airlines | 7298 |
| 3 | EJA | 3944 |
| 4 | IndiGo | 3449 |
| 5 | American Airlines | 3261 |
| 6 | Southwest Airlines | 3243 |
| 7 | ENY | 2513 |
| 8 | Delta Air Lines | 2511 |
| 9 | LATAM Airlines | 1900 |
| 10 | AZU | 1828 |
| 11 | Lufthansa | 1714 |
| 12 | Vueling | 1682 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1602 |
| 15 | easyJet | 1396 |
| 16 | Swiss International | 1351 |
| 17 | AXM | 1310 |
| 18 | EJU | 1242 |
| 19 | QLK | 1232 |
| 20 | Alaska Airlines | 1223 |
| 21 | All Nippon Airways | 1215 |
| 22 | United Airlines | 1186 |
| 23 | VIV | 1115 |
| 24 | GLO | 1089 |
| 25 | Air France | 1070 |
| 26 | PGT | 1069 |
| 27 | AEE | 1031 |
| 28 | CXK | 1011 |
| 29 | WMT | 1010 |
| 30 | JetBlue | 994 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 172042 |
| 2 | 🇪🇸 ES | 12977 |
| 3 | 🇧🇷 BR | 11603 |
| 4 | 🇦🇺 AU | 11267 |
| 5 | 🇨🇦 CA | 11124 |
| 6 | 🇮🇳 IN | 10776 |
| 7 | 🇮🇹 IT | 10520 |
| 8 | 🇩🇪 DE | 9976 |
| 9 | 🇬🇧 GB | 9450 |
| 10 | 🇯🇵 JP | 8211 |
| 11 | 🇨🇴 CO | 8030 |
| 12 | 🇫🇷 FR | 8023 |
| 13 | 🇬🇷 GR | 5929 |
| 14 | 🇲🇽 MX | 5711 |
| 15 | 🇹🇷 TR | 5639 |
| 16 | 🇨🇭 CH | 5416 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3440 |
| 19 | 🇿🇦 ZA | 3372 |
| 20 | 🇵🇱 PL | 3317 |
| 21 | 🇹🇭 TH | 3148 |
| 22 | 🇳🇿 NZ | 2797 |
| 23 | 🇵🇭 PH | 2660 |
| 24 | 🇬🇹 GT | 2553 |
| 25 | 🇰🇷 KR | 2456 |
| 26 | 🇭🇷 HR | 2139 |
| 27 | 🇲🇦 MA | 2033 |
| 28 | 🇳🇱 NL | 1799 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1647 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4235 |
| 2 | Denver International Airport |  | US | 3293 |
| 3 | Tokyo International Airport |  | JP | 2502 |
| 4 | Guaymaral Airport |  | CO | 2475 |
| 5 | Indira Gandhi International Airport |  | IN | 2445 |
| 6 | Harry Reid International Airport |  | US | 2297 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2118 |
| 8 | Zurich Airport |  | CH | 2109 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2096 |
| 10 | La Aurora Airport |  | GT | 1956 |
| 11 | El Dorado International Airport |  | CO | 1857 |
| 12 | Chicago O'Hare International Airport |  | US | 1830 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1805 |
| 14 | Salt Lake City International Airport |  | US | 1798 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1683 |
| 17 | Madrid Barajas International Airport |  | ES | 1584 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1543 |
| 19 | Capua Airport |  | IT | 1539 |
| 20 | Macau International Airport |  | MO | 1536 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1515 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1460 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1402 |
| 24 | Malpensa International Airport |  | IT | 1399 |
| 25 | Charles de Gaulle International Airport |  | FR | 1385 |
| 26 | Charlotte/Douglas International Airport |  | US | 1352 |
| 27 | Kuala Lumpur International Airport |  | MY | 1279 |
| 28 | Ninoy Aquino International Airport |  | PH | 1258 |
| 29 | Bengaluru International Airport |  | IN | 1258 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1254 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1226 |
| 32 | Barcelona International Airport |  | ES | 1211 |
| 33 | Seattle-Tacoma International Airport |  | US | 1180 |
| 34 | Viracopos International Airport |  | BR | 1171 |
| 35 | Calgary International Airport |  | CA | 1148 |
| 36 | Reno/Tahoe International Airport |  | US | 1130 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1117 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 490 | 1h 7m | 770 km | 6,509.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 467 | 24m | 225 km | 1,811.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 286 | 22m | 55 km | 271.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
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
| N561SR |  | 6CL4 (6CL4) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-16 01:08 UTC | 2026-08-16 01:33 UTC | 25m |
| N929TG |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-16 00:57 UTC | 2026-08-16 01:22 UTC | 25m |
| N71VS |  | Lake Tahoe Airport (KTVL) | Desert Creek Airport (NV97) | 2026-08-16 00:57 UTC | 2026-08-16 01:07 UTC | 10m |
| TKR184 | TKR | Ephrata Municipal Airport (KEPH) | 0WN9 (0WN9) | 2026-08-16 00:55 UTC | 2026-08-16 01:06 UTC | 11m |
| N917CA |  | Olney-Noble Airport (KOLY) | Mount Vernon Airport (KMVN) | 2026-08-16 00:45 UTC | 2026-08-16 01:03 UTC | 18m |
| TKR186 | TKR | WA70 (WA70) | 0WN9 (0WN9) | 2026-08-16 00:30 UTC | 2026-08-16 01:03 UTC | 32m |
| JRE836 | JRE | Boundary Bay Airport (CZBB) | Boeing Field/King County International Airport (KBFI) | 2026-08-16 00:29 UTC | 2026-08-16 00:54 UTC | 24m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-08-16 00:31 UTC | 2026-08-16 00:47 UTC | 16m |
| BOX313 | BOX | Cincinnati/Northern Kentucky International Airport (KCVG) | Buraimi Airport (OOBR) | 2026-08-15 11:05 UTC | 2026-08-16 00:38 UTC | 13h 33m |
| ENT4591 | ENT | Katowice International Airport (EPKT) | Antalya International Airport (LTAI) | 2026-08-15 22:18 UTC | 2026-08-16 00:38 UTC | 2h 20m |
| TKR15 | TKR | NV17 (NV17) | Samsarg Field (KN58) | 2026-08-16 00:29 UTC | 2026-08-16 00:34 UTC | 5m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-08-16 00:29 UTC | 2026-08-16 00:33 UTC | 3m |
| SKW3777 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | Harris River Ranch Airport (9CA7) | 2026-08-15 23:22 UTC | 2026-08-16 00:31 UTC | 1h 8m |
| XFB | XFB | Torquay Airport (YTQY) | Torquay Airport (YTQY) | 2026-08-16 00:29 UTC | 2026-08-16 00:31 UTC | 1m |
| N390BD |  | Crystal Airport (46CN) | Crystal Airport (46CN) | 2026-08-16 00:30 UTC | 2026-08-16 00:30 UTC | 0m |
| AAY213 | AAY | Myrtle Beach Hardee Airpark (SC21) | CT44 (CT44) | 2026-08-15 22:55 UTC | 2026-08-16 00:30 UTC | 1h 34m |
| G3343 |  | Columbia Airport (KO22) | Columbia Airport (KO22) | 2026-08-16 00:16 UTC | 2026-08-16 00:30 UTC | 13m |
| CAP428 | CAP | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-16 00:29 UTC | 2026-08-16 00:30 UTC | 0m |
| N530ME |  | PN06 (PN06) | PN06 (PN06) | 2026-08-16 00:29 UTC | 2026-08-16 00:29 UTC | 0m |
| AAL1071 | American Airlines | Charlotte/Douglas International Airport (KCLT) | New Castle Airport (KILG) | 2026-08-15 23:16 UTC | 2026-08-16 00:18 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
