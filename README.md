# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_11:07:58_UTC-green)

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

**Latest saved flight:** 2026-08-16 11:07:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 11:07:58 UTC

- **204,307** saved flights
- **65,334** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,307** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,456,537.0 tonnes** estimated CO2 emissions
- **142,407,941 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8037 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3496 |
| 5 | American Airlines | 3401 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2612 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1837 |
| 11 | Lufthansa | 1741 |
| 12 | Vueling | 1693 |
| 13 | WIF | 1643 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1412 |
| 16 | Swiss International | 1361 |
| 17 | AXM | 1334 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1261 |
| 21 | EJU | 1249 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1119 |
| 24 | GLO | 1095 |
| 25 | Air France | 1089 |
| 26 | PGT | 1089 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1043 |
| 29 | WMT | 1019 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173789 |
| 2 | 🇪🇸 ES | 13062 |
| 3 | 🇧🇷 BR | 11647 |
| 4 | 🇦🇺 AU | 11480 |
| 5 | 🇨🇦 CA | 11281 |
| 6 | 🇮🇳 IN | 10915 |
| 7 | 🇮🇹 IT | 10593 |
| 8 | 🇩🇪 DE | 10106 |
| 9 | 🇬🇧 GB | 9526 |
| 10 | 🇯🇵 JP | 8438 |
| 11 | 🇫🇷 FR | 8091 |
| 12 | 🇨🇴 CO | 8046 |
| 13 | 🇬🇷 GR | 6007 |
| 14 | 🇹🇷 TR | 5743 |
| 15 | 🇲🇽 MX | 5742 |
| 16 | 🇨🇭 CH | 5470 |
| 17 | 🇳🇴 NO | 5091 |
| 18 | 🇲🇾 MY | 3512 |
| 19 | 🇿🇦 ZA | 3414 |
| 20 | 🇵🇱 PL | 3353 |
| 21 | 🇹🇭 TH | 3227 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2719 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2500 |
| 26 | 🇭🇷 HR | 2169 |
| 27 | 🇲🇦 MA | 2051 |
| 28 | 🇳🇱 NL | 1817 |
| 29 | 🇲🇪 ME | 1704 |
| 30 | 🇮🇩 ID | 1678 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2545 |
| 4 | Indira Gandhi International Airport |  | IN | 2477 |
| 5 | Guaymaral Airport |  | CO | 2476 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2136 |
| 8 | Zurich Airport |  | CH | 2126 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1861 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Frankfurt am Main International Airport |  | DE | 1695 |
| 16 | Congonhas Airport |  | BR | 1694 |
| 17 | Madrid Barajas International Airport |  | ES | 1596 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1549 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1404 |
| 25 | Charles de Gaulle International Airport |  | FR | 1396 |
| 26 | Charlotte/Douglas International Airport |  | US | 1391 |
| 27 | Kuala Lumpur International Airport |  | MY | 1302 |
| 28 | Ninoy Aquino International Airport |  | PH | 1288 |
| 29 | Bengaluru International Airport |  | IN | 1270 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1221 |
| 33 | Seattle-Tacoma International Airport |  | US | 1213 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1126 |
| 38 | Vitoria/Foronda Airport |  | ES | 1126 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 498 | 1h 7m | 770 km | 6,615.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 342 | 27m | 275 km | 1,620.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 300 | 44m | 241 km | 1,246.1 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 295 | 1h 49m | 1,423 km | 7,239.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 265 | 21m | 250 km | 1,144.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 253 | 24m | 218 km | 953.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 240 | 1h 37m | 1,156 km | 4,787.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 235 | 19m | 144 km | 584.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 230 | 31m | 369 km | 1,464.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-16 10:38 UTC | 2026-08-16 11:07 UTC | 29m |
| SXS9LY | SXS | Vienna International Airport (LOWW) | Karain Airport (LTXE) | 2026-08-16 08:30 UTC | 2026-08-16 11:02 UTC | 2h 31m |
| PH1074 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-16 09:46 UTC | 2026-08-16 10:48 UTC | 1h 1m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 09:52 UTC | 2026-08-16 10:41 UTC | 48m |
| ASL987 | ASL | Belgrade Nikola Tesla Airport (LYBE) | Smolensk North Airport (XUBS) | 2026-08-15 12:32 UTC | 2026-08-16 10:31 UTC | 21h 59m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-16 09:58 UTC | 2026-08-16 10:31 UTC | 32m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-08-16 09:43 UTC | 2026-08-16 10:29 UTC | 46m |
| LNX06AR | LNX | Newcastle Airport (EGNT) | RAF Northolt (EGWU) | 2026-08-16 09:42 UTC | 2026-08-16 10:27 UTC | 45m |
| CTV764 | CTV | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-08-16 09:38 UTC | 2026-08-16 10:25 UTC | 46m |
| PGT51MR | PGT | Sabiha Gokcen International Airport (LTFJ) | Gaziemir Airport (LTBK) | 2026-08-16 09:50 UTC | 2026-08-16 10:25 UTC | 35m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-16 09:48 UTC | 2026-08-16 10:23 UTC | 35m |
| OC61 |  | Nagasaki Airport (RJFU) | Iki Airport (RJDB) | 2026-08-16 10:10 UTC | 2026-08-16 10:22 UTC | 12m |
| OAL4MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-08-16 10:03 UTC | 2026-08-16 10:21 UTC | 17m |
| 5YZBF |  | Nairobi Wilson Airport (HKNW) | Jomo Kenyatta International Airport (HKJK) | 2026-08-16 10:02 UTC | 2026-08-16 10:20 UTC | 17m |
| RYR2XA | Ryanair | Trieste / Ronchi Dei Legionari (LIPQ) | Dublin Airport (EIDW) | 2026-08-16 07:42 UTC | 2026-08-16 10:17 UTC | 2h 35m |
| GFBPS | GFB | EG32 (EG32) | EG32 (EG32) | 2026-08-16 09:03 UTC | 2026-08-16 10:17 UTC | 1h 13m |
| ENT6062 | ENT | Dusseldorf International Airport (EDDL) | Kukes Airport (LAKU) | 2026-08-16 08:34 UTC | 2026-08-16 10:17 UTC | 1h 42m |
| QTR74N | Qatar Airways | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-08-16 09:07 UTC | 2026-08-16 10:16 UTC | 1h 8m |
| WZZ7WD | Wizz Air | Warsaw Chopin Airport (EPWA) | Otocac Airport (LDRO) | 2026-08-16 09:01 UTC | 2026-08-16 10:16 UTC | 1h 14m |
| IGO7172 | IndiGo | Chennai International Airport (VOMM) | Mysore Airport (VOMY) | 2026-08-16 05:03 UTC | 2026-08-16 10:14 UTC | 5h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
