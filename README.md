# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_22:49:33_UTC-green)

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

**Latest saved flight:** 2026-09-10 22:49:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 22:49:33 UTC

- **254,328** saved flights
- **76,023** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,328** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,068,248.6 tonnes** estimated CO2 emissions
- **177,869,486 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10154 |
| 2 | SkyWest Airlines | 8868 |
| 3 | EJA | 4910 |
| 4 | IndiGo | 4254 |
| 5 | American Airlines | 4040 |
| 6 | Southwest Airlines | 3753 |
| 7 | Delta Air Lines | 3196 |
| 8 | ENY | 3030 |
| 9 | LATAM Airlines | 2445 |
| 10 | AZU | 2368 |
| 11 | Vueling | 2163 |
| 12 | WIF | 2037 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1990 |
| 15 | easyJet | 1738 |
| 16 | Swiss International | 1705 |
| 17 | QLK | 1638 |
| 18 | AXM | 1633 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1581 |
| 21 | Alaska Airlines | 1513 |
| 22 | All Nippon Airways | 1483 |
| 23 | WMT | 1438 |
| 24 | GLO | 1416 |
| 25 | PGT | 1396 |
| 26 | VIV | 1389 |
| 27 | Wizz Air | 1384 |
| 28 | Air France | 1383 |
| 29 | JetBlue | 1238 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211197 |
| 2 | 🇪🇸 ES | 16210 |
| 3 | 🇧🇷 BR | 14841 |
| 4 | 🇦🇺 AU | 14481 |
| 5 | 🇨🇦 CA | 14153 |
| 6 | 🇮🇹 IT | 13921 |
| 7 | 🇮🇳 IN | 13322 |
| 8 | 🇩🇪 DE | 12434 |
| 9 | 🇬🇧 GB | 11885 |
| 10 | 🇨🇴 CO | 11284 |
| 11 | 🇫🇷 FR | 10217 |
| 12 | 🇯🇵 JP | 9951 |
| 13 | 🇹🇷 TR | 7610 |
| 14 | 🇬🇷 GR | 7433 |
| 15 | 🇲🇽 MX | 7011 |
| 16 | 🇨🇭 CH | 6829 |
| 17 | 🇳🇴 NO | 6304 |
| 18 | 🇹🇭 TH | 4564 |
| 19 | 🇲🇾 MY | 4394 |
| 20 | 🇿🇦 ZA | 4339 |
| 21 | 🇵🇱 PL | 4223 |
| 22 | 🇳🇿 NZ | 3490 |
| 23 | 🇵🇭 PH | 3433 |
| 24 | 🇬🇹 GT | 3162 |
| 25 | 🇰🇷 KR | 2922 |
| 26 | 🇭🇷 HR | 2915 |
| 27 | 🇲🇦 MA | 2567 |
| 28 | 🇲🇪 ME | 2392 |
| 29 | 🇳🇱 NL | 2286 |
| 30 | 🇮🇩 ID | 2169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5229 |
| 2 | Denver International Airport |  | US | 4111 |
| 3 | Indira Gandhi International Airport |  | IN | 3081 |
| 4 | Tokyo International Airport |  | JP | 2968 |
| 5 | Guaymaral Airport |  | CO | 2755 |
| 6 | Harry Reid International Airport |  | US | 2696 |
| 7 | Zurich Airport |  | CH | 2659 |
| 8 | El Dorado International Airport |  | CO | 2611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2574 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2497 |
| 11 | La Aurora Airport |  | GT | 2412 |
| 12 | Salt Lake City International Airport |  | US | 2240 |
| 13 | Chicago O'Hare International Airport |  | US | 2217 |
| 14 | Congonhas Airport |  | BR | 2179 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2080 |
| 16 | Capua Airport |  | IT | 2006 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1966 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1902 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1845 |
| 21 | Malpensa International Airport |  | IT | 1827 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1783 |
| 23 | Charles de Gaulle International Airport |  | FR | 1783 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1768 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1704 |
| 26 | Macau International Airport |  | MO | 1680 |
| 27 | Ninoy Aquino International Airport |  | PH | 1679 |
| 28 | Barcelona International Airport |  | ES | 1603 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1583 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1560 |
| 32 | Viracopos International Airport |  | BR | 1521 |
| 33 | Seattle-Tacoma International Airport |  | US | 1496 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1477 |
| 35 | Calgary International Airport |  | CA | 1465 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1448 |
| 38 | Oslo Gardermoen Airport |  | NO | 1437 |
| 39 | Vancouver International Airport |  | CA | 1425 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1371 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1108 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 944 | 21m | 244 km | 3,974.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 638 | 1h 6m | 770 km | 8,475.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 569 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 404 | 1h 50m | 1,423 km | 9,914.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 402 | 44m | 555 km | 3,849.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 383 | 44m | 241 km | 1,590.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 373 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 354 | 24m | 218 km | 1,333.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 308 | 19m | 99 km | 527.6 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 306 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 297 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 291 | 1h 14m | 961 km | 4,823.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 290 | 19m | 144 km | 721.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 264 | 41m | 535 km | 2,438.2 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LSXX | LSX | Ramona Airport (KRNM) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-10 22:23 UTC | 2026-09-10 22:49 UTC | 26m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-09-10 12:00 UTC | 2026-09-10 22:49 UTC | 10h 48m |
| BDA481 | BDA | Indira Gandhi International Airport (VIDP) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-10 20:02 UTC | 2026-09-10 22:48 UTC | 2h 46m |
| RDHK723 | RDH | Aberdeen Field (31VA) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-09-10 22:21 UTC | 2026-09-10 22:44 UTC | 23m |
| N414UH |  | Bolinder Field/Tooele Valley Airport (KTVY) | UT41 (UT41) | 2026-09-10 22:31 UTC | 2026-09-10 22:44 UTC | 12m |
| XSN06 | XSN | San Carlos Airport (KSQL) | Lake Tahoe Airport (KTVL) | 2026-09-10 22:06 UTC | 2026-09-10 22:40 UTC | 34m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-10 17:57 UTC | 2026-09-10 22:39 UTC | 4h 41m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-09-10 21:24 UTC | 2026-09-10 22:38 UTC | 1h 14m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-09-10 11:19 UTC | 2026-09-10 22:37 UTC | 11h 18m |
| BCS692 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-09-10 17:04 UTC | 2026-09-10 22:29 UTC | 5h 24m |
| CLX1409 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-09-10 11:29 UTC | 2026-09-10 22:27 UTC | 10h 58m |
| N950TT |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-09-10 22:13 UTC | 2026-09-10 22:27 UTC | 14m |
| CXK564 | CXK | Ogden-Hinckley Airport (KOGD) | Brigham City Regional Airport (KBMC) | 2026-09-10 22:12 UTC | 2026-09-10 22:27 UTC | 14m |
| N1046X |  | Boone Municipal Airport (KBNW) | Boone Municipal Airport (KBNW) | 2026-09-10 22:09 UTC | 2026-09-10 22:27 UTC | 17m |
| TEXGLD | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-09-10 21:51 UTC | 2026-09-10 22:26 UTC | 35m |
| CGE72 | CGE | Nelson Airport (NZNS) | Takaka Airport (NZTK) | 2026-09-10 22:00 UTC | 2026-09-10 22:25 UTC | 25m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-09-10 12:01 UTC | 2026-09-10 22:24 UTC | 10h 23m |
| TRP6 | TRP | Easton/Newnam Field (KESN) | 6MD2 (6MD2) | 2026-09-10 22:11 UTC | 2026-09-10 22:23 UTC | 12m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-09-10 11:18 UTC | 2026-09-10 22:22 UTC | 11h 4m |
| AM341 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-09-10 21:56 UTC | 2026-09-10 22:20 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
