# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_11:17:10_UTC-green)

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

**Latest saved flight:** 2026-08-15 11:17:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 11:17:10 UTC

- **198,237** saved flights
- **62,032** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,237** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,368,314.7 tonnes** estimated CO2 emissions
- **137,293,604 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7872 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3897 |
| 4 | IndiGo | 3432 |
| 5 | Southwest Airlines | 3070 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2345 |
| 9 | LATAM Airlines | 1857 |
| 10 | AZU | 1791 |
| 11 | Lufthansa | 1701 |
| 12 | Vueling | 1662 |
| 13 | WIF | 1633 |
| 14 | LXJ | 1571 |
| 15 | easyJet | 1361 |
| 16 | Swiss International | 1341 |
| 17 | AXM | 1303 |
| 18 | EJU | 1228 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1093 |
| 23 | GLO | 1070 |
| 24 | Air France | 1048 |
| 25 | PGT | 1042 |
| 26 | AEE | 1020 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1005 |
| 29 | WMT | 999 |
| 30 | Wizz Air | 982 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168189 |
| 2 | 🇪🇸 ES | 12804 |
| 3 | 🇧🇷 BR | 11383 |
| 4 | 🇦🇺 AU | 11145 |
| 5 | 🇨🇦 CA | 10843 |
| 6 | 🇮🇳 IN | 10723 |
| 7 | 🇮🇹 IT | 10362 |
| 8 | 🇩🇪 DE | 9833 |
| 9 | 🇬🇧 GB | 9299 |
| 10 | 🇯🇵 JP | 8150 |
| 11 | 🇫🇷 FR | 7899 |
| 12 | 🇨🇴 CO | 7810 |
| 13 | 🇬🇷 GR | 5841 |
| 14 | 🇲🇽 MX | 5605 |
| 15 | 🇹🇷 TR | 5448 |
| 16 | 🇨🇭 CH | 5365 |
| 17 | 🇳🇴 NO | 5060 |
| 18 | 🇲🇾 MY | 3411 |
| 19 | 🇿🇦 ZA | 3346 |
| 20 | 🇵🇱 PL | 3278 |
| 21 | 🇹🇭 TH | 3108 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2635 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2413 |
| 26 | 🇭🇷 HR | 2089 |
| 27 | 🇲🇦 MA | 2003 |
| 28 | 🇳🇱 NL | 1778 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1626 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2491 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2429 |
| 6 | Harry Reid International Airport |  | US | 2269 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2097 |
| 8 | Zurich Airport |  | CH | 2097 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1817 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1760 |
| 14 | Chicago O'Hare International Airport |  | US | 1737 |
| 15 | Frankfurt am Main International Airport |  | DE | 1669 |
| 16 | Congonhas Airport |  | BR | 1666 |
| 17 | Madrid Barajas International Airport |  | ES | 1559 |
| 18 | Macau International Airport |  | MO | 1534 |
| 19 | Capua Airport |  | IT | 1515 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1509 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1458 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 24 | Malpensa International Airport |  | IT | 1380 |
| 25 | Charles de Gaulle International Airport |  | FR | 1362 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1270 |
| 28 | Bengaluru International Airport |  | IN | 1253 |
| 29 | Ninoy Aquino International Airport |  | PH | 1246 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1236 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1192 |
| 33 | Viracopos International Airport |  | BR | 1151 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1117 |
| 37 | Reno/Tahoe International Airport |  | US | 1116 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1090 |
| 40 | Tenerife Norte Airport |  | ES | 1086 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 486 | 1h 7m | 770 km | 6,456.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 333 | 27m | 275 km | 1,577.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 298 | 44m | 241 km | 1,237.8 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 288 | 1h 49m | 1,423 km | 7,068.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 247 | 26m | 215 km | 914.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 247 | 24m | 218 km | 930.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 232 | 19m | 144 km | 577.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEOFF | DEO | Stade Airport (EDHS) | Stade Airport (EDHS) | 2026-08-15 10:25 UTC | 2026-08-15 11:17 UTC | 51m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-15 10:28 UTC | 2026-08-15 11:14 UTC | 45m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-15 10:40 UTC | 2026-08-15 11:07 UTC | 26m |
| AEZ2631 | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-15 10:16 UTC | 2026-08-15 11:06 UTC | 50m |
| AEZ2914 | AEZ | Trieste / Ronchi Dei Legionari (LIPQ) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-15 09:40 UTC | 2026-08-15 11:04 UTC | 1h 24m |
| UPS1482 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Detroit Metro Wayne County Airport (KDTW) | 2026-08-15 09:55 UTC | 2026-08-15 10:42 UTC | 46m |
| GBWXB | GBW | Chichester/Goodwood Airport (EGHR) | Chichester/Goodwood Airport (EGHR) | 2026-08-15 10:10 UTC | 2026-08-15 10:34 UTC | 24m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-15 10:23 UTC | 2026-08-15 10:33 UTC | 10m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-15 10:03 UTC | 2026-08-15 10:30 UTC | 26m |
| DMMWK | DMM | Werdohl-Kuntrop Airport (EDKW) | Werdohl-Kuntrop Airport (EDKW) | 2026-08-15 10:08 UTC | 2026-08-15 10:20 UTC | 12m |
| SAS2301 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Vinnu Airport (ENSU) | 2026-08-15 09:49 UTC | 2026-08-15 10:17 UTC | 28m |
| JMA8664 | JMA | Jomo Kenyatta International Airport (HKJK) | Nakuru Airport (HKNK) | 2026-08-15 09:52 UTC | 2026-08-15 10:16 UTC | 23m |
| BBC389 | BBC | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-08-15 09:21 UTC | 2026-08-15 10:15 UTC | 53m |
| NAY74RF | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-08-15 10:02 UTC | 2026-08-15 10:12 UTC | 10m |
| OKBWR | OKB | LKSP (LKSP) | LKSP (LKSP) | 2026-08-15 10:03 UTC | 2026-08-15 10:11 UTC | 7m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-15 09:23 UTC | 2026-08-15 10:10 UTC | 47m |
| EAI34N | EAI | Aberdeen Dyce Airport (EGPD) | Dublin Airport (EIDW) | 2026-08-15 08:48 UTC | 2026-08-15 10:09 UTC | 1h 20m |
| WIF153 | WIF | Sogndal Airport (ENSG) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-15 09:47 UTC | 2026-08-15 10:06 UTC | 18m |
| OEXKY | OEX | Nikolsdorf Airport (LOKL) | Nikolsdorf Airport (LOKL) | 2026-08-15 09:56 UTC | 2026-08-15 10:06 UTC | 9m |
| EXS81HT | EXS | Manchester Airport (EGCC) | Adnan Menderes International Airport (LTBJ) | 2026-08-15 06:42 UTC | 2026-08-15 10:06 UTC | 3h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
