# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_17:38:50_UTC-green)

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

**Latest saved flight:** 2026-09-11 17:38:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 17:38:50 UTC

- **255,086** saved flights
- **76,169** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,086** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,078,406.7 tonnes** estimated CO2 emissions
- **178,458,361 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10169 |
| 2 | SkyWest Airlines | 8887 |
| 3 | EJA | 4926 |
| 4 | IndiGo | 4273 |
| 5 | American Airlines | 4042 |
| 6 | Southwest Airlines | 3756 |
| 7 | Delta Air Lines | 3200 |
| 8 | ENY | 3033 |
| 9 | LATAM Airlines | 2457 |
| 10 | AZU | 2378 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2049 |
| 13 | Lufthansa | 1998 |
| 14 | LXJ | 1992 |
| 15 | easyJet | 1739 |
| 16 | Swiss International | 1710 |
| 17 | QLK | 1646 |
| 18 | AXM | 1638 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1583 |
| 21 | Alaska Airlines | 1516 |
| 22 | All Nippon Airways | 1489 |
| 23 | WMT | 1443 |
| 24 | GLO | 1420 |
| 25 | PGT | 1404 |
| 26 | Air France | 1394 |
| 27 | VIV | 1393 |
| 28 | Wizz Air | 1389 |
| 29 | JetBlue | 1240 |
| 30 | AEE | 1238 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211735 |
| 2 | 🇪🇸 ES | 16247 |
| 3 | 🇧🇷 BR | 14894 |
| 4 | 🇦🇺 AU | 14555 |
| 5 | 🇨🇦 CA | 14196 |
| 6 | 🇮🇹 IT | 13955 |
| 7 | 🇮🇳 IN | 13381 |
| 8 | 🇩🇪 DE | 12464 |
| 9 | 🇬🇧 GB | 11914 |
| 10 | 🇨🇴 CO | 11330 |
| 11 | 🇫🇷 FR | 10256 |
| 12 | 🇯🇵 JP | 9979 |
| 13 | 🇹🇷 TR | 7643 |
| 14 | 🇬🇷 GR | 7450 |
| 15 | 🇲🇽 MX | 7025 |
| 16 | 🇨🇭 CH | 6851 |
| 17 | 🇳🇴 NO | 6333 |
| 18 | 🇹🇭 TH | 4589 |
| 19 | 🇲🇾 MY | 4405 |
| 20 | 🇿🇦 ZA | 4354 |
| 21 | 🇵🇱 PL | 4230 |
| 22 | 🇳🇿 NZ | 3511 |
| 23 | 🇵🇭 PH | 3441 |
| 24 | 🇬🇹 GT | 3180 |
| 25 | 🇰🇷 KR | 2930 |
| 26 | 🇭🇷 HR | 2925 |
| 27 | 🇲🇦 MA | 2573 |
| 28 | 🇲🇪 ME | 2398 |
| 29 | 🇳🇱 NL | 2297 |
| 30 | 🇮🇩 ID | 2175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5235 |
| 2 | Denver International Airport |  | US | 4117 |
| 3 | Indira Gandhi International Airport |  | IN | 3085 |
| 4 | Tokyo International Airport |  | JP | 2978 |
| 5 | Guaymaral Airport |  | CO | 2758 |
| 6 | Harry Reid International Airport |  | US | 2701 |
| 7 | Zurich Airport |  | CH | 2672 |
| 8 | El Dorado International Airport |  | CO | 2616 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2575 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2500 |
| 11 | La Aurora Airport |  | GT | 2426 |
| 12 | Salt Lake City International Airport |  | US | 2251 |
| 13 | Chicago O'Hare International Airport |  | US | 2221 |
| 14 | Congonhas Airport |  | BR | 2186 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2085 |
| 16 | Capua Airport |  | IT | 2012 |
| 17 | Madrid Barajas International Airport |  | ES | 1993 |
| 18 | Frankfurt am Main International Airport |  | DE | 1972 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1911 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1847 |
| 21 | Malpensa International Airport |  | IT | 1834 |
| 22 | Charles de Gaulle International Airport |  | FR | 1797 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1791 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1773 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1714 |
| 26 | Macau International Airport |  | MO | 1686 |
| 27 | Ninoy Aquino International Airport |  | PH | 1682 |
| 28 | Barcelona International Airport |  | ES | 1606 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1586 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1564 |
| 32 | Viracopos International Airport |  | BR | 1526 |
| 33 | Seattle-Tacoma International Airport |  | US | 1497 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1482 |
| 35 | Don Mueang International Airport |  | TH | 1469 |
| 36 | Calgary International Airport |  | CA | 1468 |
| 37 | Bengaluru International Airport |  | IN | 1449 |
| 38 | Oslo Gardermoen Airport |  | NO | 1444 |
| 39 | Vancouver International Airport |  | CA | 1429 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1377 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 947 | 21m | 244 km | 3,987.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 682 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 639 | 1h 6m | 770 km | 8,488.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 572 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 408 | 44m | 555 km | 3,906.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 385 | 44m | 241 km | 1,599.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 355 | 24m | 218 km | 1,337.4 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 310 | 19m | 99 km | 531.0 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 301 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 293 | 1h 14m | 961 km | 4,856.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 292 | 19m | 144 km | 726.3 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 262 | 28m | 152 km | 684.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFR218 | Air France | Charles de Gaulle International Airport (LFPG) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-11 09:19 UTC | 2026-09-11 17:38 UTC | 8h 19m |
| N1816T |  | Northeast Philadelphia Airport (KPNE) | Northumberland County Airport (KN79) | 2026-09-11 16:34 UTC | 2026-09-11 17:36 UTC | 1h 1m |
| N562X |  | Huey Airport (DE14) | Chorman Airport (KD74) | 2026-09-11 17:21 UTC | 2026-09-11 17:26 UTC | 4m |
| N941TW |  | Buchanan Field (KCCR) | Buchanan Field (KCCR) | 2026-09-11 16:24 UTC | 2026-09-11 17:25 UTC | 1h 1m |
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Tucson International Airport (KTUS) | 2026-09-11 16:31 UTC | 2026-09-11 17:22 UTC | 50m |
| CXK1085 | CXK | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-09-11 16:57 UTC | 2026-09-11 17:19 UTC | 22m |
| XSN82 | XSN | Napa County Airport (KAPC) | Agape Farm Airport (OR42) | 2026-09-11 16:01 UTC | 2026-09-11 17:18 UTC | 1h 17m |
| N33NE |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-09-11 15:55 UTC | 2026-09-11 17:18 UTC | 1h 23m |
| NSE6534 | NSE | Enrique Olaya Herrera Airport (SKMD) | Tunja Airport (SKTJ) | 2026-09-11 16:35 UTC | 2026-09-11 17:18 UTC | 42m |
| N6382D |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-09-11 15:43 UTC | 2026-09-11 17:15 UTC | 1h 31m |
| N465FA |  | Capital City Airport (KCXY) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-11 16:43 UTC | 2026-09-11 17:14 UTC | 30m |
| BRG681 | BRG | Ralph Wien Memorial Airport (PAOT) | Noatak Airport (PAWN) | 2026-09-11 16:41 UTC | 2026-09-11 17:09 UTC | 28m |
| HNL24B | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-09-11 16:27 UTC | 2026-09-11 17:09 UTC | 41m |
| AVL220 | AVL | Leesburg Executive Airport (KJYO) | Leesburg Executive Airport (KJYO) | 2026-09-11 17:05 UTC | 2026-09-11 17:09 UTC | 3m |
| JPR41 | JPR | Alpine County Airport (KM45) | Alpine County Airport (KM45) | 2026-09-11 17:04 UTC | 2026-09-11 17:08 UTC | 3m |
| N213PF |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-11 15:37 UTC | 2026-09-11 17:05 UTC | 1h 27m |
| SCU48 | SCU | Jirik Field (OL23) | Neversweat Airport (1OK0) | 2026-09-11 16:45 UTC | 2026-09-11 17:05 UTC | 19m |
| RNGR841 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Corpus Christi Nas (Truax Field) Airport (KNGP) | 2026-09-11 16:32 UTC | 2026-09-11 17:04 UTC | 32m |
| N3020A |  | Nantucket Memorial Airport (KACK) | Bunting's Field (4MD1) | 2026-09-11 15:37 UTC | 2026-09-11 17:04 UTC | 1h 27m |
| VTAHI | VTA | Al Maktoum International Airport (OMDW) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-11 14:21 UTC | 2026-09-11 17:03 UTC | 2h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
