# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_08:02:12_UTC-green)

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

**Latest saved flight:** 2026-08-17 08:02:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 08:02:12 UTC

- **207,310** saved flights
- **65,977** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,310** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,493,034.9 tonnes** estimated CO2 emissions
- **144,523,763 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8172 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3542 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2666 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1755 |
| 12 | Vueling | 1715 |
| 13 | WIF | 1664 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1380 |
| 17 | AXM | 1354 |
| 18 | United Airlines | 1304 |
| 19 | QLK | 1291 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1263 |
| 22 | All Nippon Airways | 1258 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | PGT | 1107 |
| 26 | Air France | 1103 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1056 |
| 29 | WMT | 1045 |
| 30 | Wizz Air | 1020 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176059 |
| 2 | 🇪🇸 ES | 13213 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11694 |
| 5 | 🇨🇦 CA | 11459 |
| 6 | 🇮🇳 IN | 11041 |
| 7 | 🇮🇹 IT | 10799 |
| 8 | 🇩🇪 DE | 10232 |
| 9 | 🇬🇧 GB | 9631 |
| 10 | 🇯🇵 JP | 8576 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8182 |
| 13 | 🇬🇷 GR | 6091 |
| 14 | 🇹🇷 TR | 5874 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5526 |
| 17 | 🇳🇴 NO | 5156 |
| 18 | 🇲🇾 MY | 3568 |
| 19 | 🇿🇦 ZA | 3458 |
| 20 | 🇵🇱 PL | 3412 |
| 21 | 🇹🇭 TH | 3300 |
| 22 | 🇳🇿 NZ | 2886 |
| 23 | 🇵🇭 PH | 2763 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2528 |
| 26 | 🇭🇷 HR | 2213 |
| 27 | 🇲🇦 MA | 2085 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1749 |
| 30 | 🇮🇩 ID | 1714 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2580 |
| 4 | Indira Gandhi International Airport |  | IN | 2508 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2160 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2157 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1920 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1856 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1710 |
| 17 | Madrid Barajas International Airport |  | ES | 1622 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1571 |
| 21 | Macau International Airport |  | MO | 1543 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1465 |
| 24 | Malpensa International Airport |  | IT | 1431 |
| 25 | Charles de Gaulle International Airport |  | FR | 1415 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1319 |
| 28 | Ninoy Aquino International Airport |  | PH | 1309 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1280 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1236 |
| 33 | Barcelona International Airport |  | ES | 1234 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1143 |
| 38 | Vitoria/Foronda Airport |  | ES | 1138 |
| 39 | Daniel K Inouye International Airport |  | US | 1110 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 509 | 1h 7m | 770 km | 6,761.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 485 | 24m | 225 km | 1,881.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 346 | 27m | 275 km | 1,639.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 343 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 304 | 44m | 241 km | 1,262.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 300 | 1h 49m | 1,423 km | 7,362.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 252 | 27m | 215 km | 933.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 245 | 1h 37m | 1,156 km | 4,887.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-08-17 07:44 UTC | 2026-08-17 08:02 UTC | 17m |
| FHNDE | FHN | Bernay St Martin Airport (LFPD) | Rouen Airport (LFOP) | 2026-08-17 07:47 UTC | 2026-08-17 07:58 UTC | 11m |
| N242EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-17 04:29 UTC | 2026-08-17 07:35 UTC | 3h 6m |
| N491LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-17 04:25 UTC | 2026-08-17 07:32 UTC | 3h 6m |
| ZSBBA | ZSB | Rand Airport (FAGM) | Witbank Airport (FAWI) | 2026-08-17 06:59 UTC | 2026-08-17 07:26 UTC | 27m |
| N664LF |  | Boise Air Trml/Gowen Field (KBOI) | Deer Creek Airport (95ID) | 2026-08-17 06:44 UTC | 2026-08-17 07:26 UTC | 41m |
| MRL17 | MRL | San Javier Airport (LELC) | Albacete-Los Llanos Airport (LEAB) | 2026-08-17 06:54 UTC | 2026-08-17 07:21 UTC | 27m |
| BLVJ | BLV | Chek Lap Kok International Airport (VHHH) | Chek Lap Kok International Airport (VHHH) | 2026-08-17 07:17 UTC | 2026-08-17 07:17 UTC | 0m |
| SAS2301 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Vinnu Airport (ENSU) | 2026-08-17 06:44 UTC | 2026-08-17 07:16 UTC | 32m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-17 07:03 UTC | 2026-08-17 07:16 UTC | 13m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-08-17 06:51 UTC | 2026-08-17 07:15 UTC | 24m |
| VOE3LL | VOE | Paris-Orly Airport (LFPO) | Gueret St Laurent Airport (LFCE) | 2026-08-17 06:42 UTC | 2026-08-17 07:13 UTC | 30m |
| RYR86XQ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Gioia Del Colle Airport (LIBV) | 2026-08-17 06:11 UTC | 2026-08-17 07:11 UTC | 59m |
| A6FHE |  | Das Island Airport (OMAS) | Das Island Airport (OMAS) | 2026-08-17 06:42 UTC | 2026-08-17 07:10 UTC | 27m |
| MJO | MJO | Tangalooma Resort Airport (YXTA) | Tangalooma Resort Airport (YXTA) | 2026-08-17 06:40 UTC | 2026-08-17 07:07 UTC | 27m |
| N229MT |  | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-17 07:00 UTC | 2026-08-17 07:04 UTC | 3m |
| BHA357 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-08-17 06:56 UTC | 2026-08-17 07:02 UTC | 6m |
| TVJ204 | TVJ | Suvarnabhumi Airport (VTBS) | Khon Kaen Airport (VTUK) | 2026-08-17 06:23 UTC | 2026-08-17 07:00 UTC | 36m |
| SAS85G | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Stavanger Airport Sola (ENZV) | 2026-08-17 06:06 UTC | 2026-08-17 06:58 UTC | 51m |
| JST834 | JST | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-08-17 05:30 UTC | 2026-08-17 06:56 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
