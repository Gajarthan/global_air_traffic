# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_20:48:24_UTC-green)

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

**Latest saved flight:** 2026-09-10 20:48:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 20:48:24 UTC

- **254,119** saved flights
- **75,972** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,119** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,064,199.5 tonnes** estimated CO2 emissions
- **177,634,753 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10151 |
| 2 | SkyWest Airlines | 8860 |
| 3 | EJA | 4905 |
| 4 | IndiGo | 4252 |
| 5 | American Airlines | 4035 |
| 6 | Southwest Airlines | 3752 |
| 7 | Delta Air Lines | 3195 |
| 8 | ENY | 3030 |
| 9 | LATAM Airlines | 2445 |
| 10 | AZU | 2363 |
| 11 | Vueling | 2163 |
| 12 | WIF | 2037 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1988 |
| 15 | easyJet | 1737 |
| 16 | Swiss International | 1705 |
| 17 | QLK | 1636 |
| 18 | AXM | 1633 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1580 |
| 21 | Alaska Airlines | 1513 |
| 22 | All Nippon Airways | 1483 |
| 23 | WMT | 1438 |
| 24 | GLO | 1413 |
| 25 | PGT | 1396 |
| 26 | VIV | 1388 |
| 27 | Wizz Air | 1384 |
| 28 | Air France | 1383 |
| 29 | JetBlue | 1238 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210969 |
| 2 | 🇪🇸 ES | 16207 |
| 3 | 🇧🇷 BR | 14823 |
| 4 | 🇦🇺 AU | 14471 |
| 5 | 🇨🇦 CA | 14142 |
| 6 | 🇮🇹 IT | 13915 |
| 7 | 🇮🇳 IN | 13313 |
| 8 | 🇩🇪 DE | 12431 |
| 9 | 🇬🇧 GB | 11879 |
| 10 | 🇨🇴 CO | 11266 |
| 11 | 🇫🇷 FR | 10216 |
| 12 | 🇯🇵 JP | 9949 |
| 13 | 🇹🇷 TR | 7606 |
| 14 | 🇬🇷 GR | 7431 |
| 15 | 🇲🇽 MX | 7000 |
| 16 | 🇨🇭 CH | 6829 |
| 17 | 🇳🇴 NO | 6304 |
| 18 | 🇹🇭 TH | 4564 |
| 19 | 🇲🇾 MY | 4394 |
| 20 | 🇿🇦 ZA | 4339 |
| 21 | 🇵🇱 PL | 4223 |
| 22 | 🇳🇿 NZ | 3474 |
| 23 | 🇵🇭 PH | 3432 |
| 24 | 🇬🇹 GT | 3160 |
| 25 | 🇰🇷 KR | 2922 |
| 26 | 🇭🇷 HR | 2915 |
| 27 | 🇲🇦 MA | 2567 |
| 28 | 🇲🇪 ME | 2391 |
| 29 | 🇳🇱 NL | 2286 |
| 30 | 🇮🇩 ID | 2169 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5227 |
| 2 | Denver International Airport |  | US | 4108 |
| 3 | Indira Gandhi International Airport |  | IN | 3078 |
| 4 | Tokyo International Airport |  | JP | 2967 |
| 5 | Guaymaral Airport |  | CO | 2751 |
| 6 | Harry Reid International Airport |  | US | 2693 |
| 7 | Zurich Airport |  | CH | 2659 |
| 8 | El Dorado International Airport |  | CO | 2605 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2571 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2497 |
| 11 | La Aurora Airport |  | GT | 2411 |
| 12 | Salt Lake City International Airport |  | US | 2240 |
| 13 | Chicago O'Hare International Airport |  | US | 2213 |
| 14 | Congonhas Airport |  | BR | 2178 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2080 |
| 16 | Capua Airport |  | IT | 2006 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1965 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1901 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1845 |
| 21 | Malpensa International Airport |  | IT | 1826 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1782 |
| 23 | Charles de Gaulle International Airport |  | FR | 1782 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1767 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1703 |
| 26 | Ninoy Aquino International Airport |  | PH | 1678 |
| 27 | Macau International Airport |  | MO | 1676 |
| 28 | Barcelona International Airport |  | ES | 1602 |
| 29 | Charlotte/Douglas International Airport |  | US | 1599 |
| 30 | Kuala Lumpur International Airport |  | MY | 1583 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1560 |
| 32 | Viracopos International Airport |  | BR | 1517 |
| 33 | Seattle-Tacoma International Airport |  | US | 1493 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1476 |
| 35 | Calgary International Airport |  | CA | 1463 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1447 |
| 38 | Oslo Gardermoen Airport |  | NO | 1437 |
| 39 | Vancouver International Airport |  | CA | 1424 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1371 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1106 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 944 | 21m | 244 km | 3,974.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 637 | 1h 6m | 770 km | 8,462.1 t |
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
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 307 | 19m | 99 km | 525.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 304 | 12m | - | - |
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
| ZKJBC | ZKJ | Whakatane Airport (NZWK) | Whakatane Airport (NZWK) | 2026-09-10 19:56 UTC | 2026-09-10 20:48 UTC | 51m |
| QTR8410 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-10 12:57 UTC | 2026-09-10 20:45 UTC | 7h 47m |
| BCAT01 | BCA | Leeming Airport (EGXE) | Leeming Airport (EGXE) | 2026-09-10 20:30 UTC | 2026-09-10 20:43 UTC | 12m |
| LSXX | LSX | Ramona Airport (KRNM) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-10 20:16 UTC | 2026-09-10 20:42 UTC | 26m |
| N16YF |  | Newark Liberty International Airport (KEWR) | Auburn University Regional Airport (KAUO) | 2026-09-10 18:53 UTC | 2026-09-10 20:40 UTC | 1h 46m |
| TVF864L | TVF | Paris-Orly Airport (LFPO) | Tit Mellil Airport (GMMT) | 2026-09-10 18:28 UTC | 2026-09-10 20:38 UTC | 2h 9m |
| WMU84 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Crippen Field (MI11) | 2026-09-10 20:23 UTC | 2026-09-10 20:36 UTC | 13m |
| N113RF |  | Hawks Run Airport (00WN) | La Grande/Union County Airport (KLGD) | 2026-09-10 15:54 UTC | 2026-09-10 20:30 UTC | 4h 36m |
| N84SP |  | Granite Mountain Lodge Airport (CO11) | Lake Creek Ranch Airport (92CO) | 2026-09-10 20:02 UTC | 2026-09-10 20:29 UTC | 27m |
| RAM801F | Royal Air Maroc | London Heathrow Airport (EGLL) | Mohammed V International Airport (GMMN) | 2026-09-10 17:59 UTC | 2026-09-10 20:29 UTC | 2h 29m |
| N9454F |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-10 20:17 UTC | 2026-09-10 20:25 UTC | 8m |
| C6058 |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | San Diego International Airport (KSAN) | 2026-09-10 19:16 UTC | 2026-09-10 20:25 UTC | 1h 9m |
| N651JD |  | Nashville International Airport (KBNA) | Lincoln Airport (KLNK) | 2026-09-10 18:59 UTC | 2026-09-10 20:24 UTC | 1h 24m |
| EJA363 | EJA | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Mineta San Jose International Airport (KSJC) | 2026-09-10 19:32 UTC | 2026-09-10 20:23 UTC | 50m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-09-10 19:47 UTC | 2026-09-10 20:22 UTC | 34m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-10 09:02 UTC | 2026-09-10 20:21 UTC | 11h 19m |
| N5218F |  | Zamperini Field (KTOA) | Van Nuys Airport (KVNY) | 2026-09-10 19:21 UTC | 2026-09-10 20:20 UTC | 58m |
| OTIS18 | OTI | Northeastern Regional Airport (KEDE) | PN21 (PN21) | 2026-09-10 18:45 UTC | 2026-09-10 20:19 UTC | 1h 33m |
| N118PA |  | Point Mugu Nas (Naval Base Ventura Co) Airport (KNTD) | Kelso Valley Airport (CN37) | 2026-09-10 19:45 UTC | 2026-09-10 20:15 UTC | 29m |
| BOX712 | BOX | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-09-10 13:10 UTC | 2026-09-10 20:11 UTC | 7h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
