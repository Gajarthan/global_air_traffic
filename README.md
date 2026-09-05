# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_09:29:52_UTC-green)

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

**Latest saved flight:** 2026-09-05 09:29:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 09:29:52 UTC

- **248,103** saved flights
- **74,744** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,103** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,984,784.3 tonnes** estimated CO2 emissions
- **173,030,971 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9937 |
| 2 | SkyWest Airlines | 8670 |
| 3 | EJA | 4792 |
| 4 | IndiGo | 4144 |
| 5 | American Airlines | 3975 |
| 6 | Southwest Airlines | 3694 |
| 7 | Delta Air Lines | 3152 |
| 8 | ENY | 2966 |
| 9 | LATAM Airlines | 2392 |
| 10 | AZU | 2312 |
| 11 | Vueling | 2119 |
| 12 | WIF | 1984 |
| 13 | Lufthansa | 1971 |
| 14 | LXJ | 1927 |
| 15 | easyJet | 1714 |
| 16 | Swiss International | 1663 |
| 17 | AXM | 1626 |
| 18 | EJU | 1591 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1559 |
| 21 | Alaska Airlines | 1482 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1401 |
| 24 | GLO | 1382 |
| 25 | VIV | 1365 |
| 26 | PGT | 1358 |
| 27 | Air France | 1356 |
| 28 | Wizz Air | 1339 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205849 |
| 2 | 🇪🇸 ES | 15885 |
| 3 | 🇧🇷 BR | 14506 |
| 4 | 🇦🇺 AU | 14103 |
| 5 | 🇨🇦 CA | 13792 |
| 6 | 🇮🇹 IT | 13582 |
| 7 | 🇮🇳 IN | 12925 |
| 8 | 🇩🇪 DE | 12187 |
| 9 | 🇬🇧 GB | 11651 |
| 10 | 🇨🇴 CO | 10823 |
| 11 | 🇫🇷 FR | 9985 |
| 12 | 🇯🇵 JP | 9809 |
| 13 | 🇹🇷 TR | 7383 |
| 14 | 🇬🇷 GR | 7299 |
| 15 | 🇲🇽 MX | 6866 |
| 16 | 🇨🇭 CH | 6683 |
| 17 | 🇳🇴 NO | 6149 |
| 18 | 🇹🇭 TH | 4477 |
| 19 | 🇲🇾 MY | 4360 |
| 20 | 🇿🇦 ZA | 4287 |
| 21 | 🇵🇱 PL | 4147 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3379 |
| 24 | 🇬🇹 GT | 3100 |
| 25 | 🇰🇷 KR | 2885 |
| 26 | 🇭🇷 HR | 2850 |
| 27 | 🇲🇦 MA | 2508 |
| 28 | 🇲🇪 ME | 2313 |
| 29 | 🇳🇱 NL | 2235 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5108 |
| 2 | Denver International Airport |  | US | 4008 |
| 3 | Indira Gandhi International Airport |  | IN | 3021 |
| 4 | Tokyo International Airport |  | JP | 2926 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2649 |
| 7 | Zurich Airport |  | CH | 2594 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2523 |
| 9 | El Dorado International Airport |  | CO | 2479 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2464 |
| 11 | La Aurora Airport |  | GT | 2359 |
| 12 | Salt Lake City International Airport |  | US | 2199 |
| 13 | Chicago O'Hare International Airport |  | US | 2176 |
| 14 | Congonhas Airport |  | BR | 2129 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2045 |
| 16 | Capua Airport |  | IT | 1952 |
| 17 | Madrid Barajas International Airport |  | ES | 1946 |
| 18 | Frankfurt am Main International Airport |  | DE | 1942 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1864 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1812 |
| 21 | Malpensa International Airport |  | IT | 1781 |
| 22 | Charles de Gaulle International Airport |  | FR | 1743 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1645 |
| 26 | Macau International Airport |  | MO | 1635 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1625 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Barcelona International Airport |  | ES | 1570 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1521 |
| 32 | Viracopos International Airport |  | BR | 1482 |
| 33 | Seattle-Tacoma International Airport |  | US | 1462 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1446 |
| 35 | Don Mueang International Airport |  | TH | 1438 |
| 36 | Calgary International Airport |  | CA | 1430 |
| 37 | Bengaluru International Airport |  | IN | 1426 |
| 38 | Oslo Gardermoen Airport |  | NO | 1396 |
| 39 | Vancouver International Airport |  | CA | 1388 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 921 | 21m | 244 km | 3,878.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 653 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 622 | 1h 6m | 770 km | 8,262.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 396 | 1h 50m | 1,423 km | 9,718.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 385 | 44m | 555 km | 3,686.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 347 | 24m | 218 km | 1,307.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 284 | 19m | 144 km | 706.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GBPCL | GBP | North Weald Airport (EGSX) | Earls Colne Airfield (EGSR) | 2026-09-05 09:14 UTC | 2026-09-05 09:29 UTC | 15m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-04 22:14 UTC | 2026-09-05 09:24 UTC | 11h 10m |
| AXM1511 | AXM | Fukuoka Airport (RJFF) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-05 07:35 UTC | 2026-09-05 09:24 UTC | 1h 48m |
| HBXDI | HBX | Dubendorf Airport (LSMD) | Muenster Aero Airport (LSPU) | 2026-09-05 08:07 UTC | 2026-09-05 09:10 UTC | 1h 3m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-04 22:11 UTC | 2026-09-05 09:05 UTC | 10h 54m |
| DEUPS | DEU | Mainz-Finthen Airport (EDFZ) | Mainz-Finthen Airport (EDFZ) | 2026-09-05 08:37 UTC | 2026-09-05 09:00 UTC | 23m |
| N808MT |  | Mc Alester Regional Airport (KMLC) | Mc Alester Regional Airport (KMLC) | 2026-09-05 08:58 UTC | 2026-09-05 08:59 UTC | 1m |
| FHCJQ | FHC | Biarritz-Anglet-Bayonne Airport (LFBZ) | Itxassou Airport (LFIX) | 2026-09-05 08:48 UTC | 2026-09-05 08:58 UTC | 10m |
| N959LA |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-09-05 08:16 UTC | 2026-09-05 08:56 UTC | 39m |
| GOZIE | GOZ | Sleap Airport (EGCV) | Leicester Airport (EGBG) | 2026-09-05 08:15 UTC | 2026-09-05 08:46 UTC | 31m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-05 08:29 UTC | 2026-09-05 08:46 UTC | 16m |
| PCH60D | PCH | Buochs Airport (LSZC) | Buochs Airport (LSZC) | 2026-09-05 07:43 UTC | 2026-09-05 08:44 UTC | 1h 0m |
| DHK885 | DHK | Belfast International Airport (EGAA) | Brussels Airport (EBBR) | 2026-09-05 07:34 UTC | 2026-09-05 08:42 UTC | 1h 7m |
| OEFRA | OEF | Foligno Airport (LIAF) | L'Aquila / Preturo Airport (LIAP) | 2026-09-05 07:48 UTC | 2026-09-05 08:35 UTC | 47m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-09-04 21:44 UTC | 2026-09-05 08:34 UTC | 10h 49m |
| TGZ1778 | TGZ | Tbilisi International Airport (UGTB) | Trento / Mattarello Airport (LIDT) | 2026-09-05 05:00 UTC | 2026-09-05 08:31 UTC | 3h 31m |
| VOR02 | VOR | Hamad International Airport (OTHH) | Doha International Airport (OTBD) | 2026-09-05 07:58 UTC | 2026-09-05 08:30 UTC | 32m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-09-05 08:11 UTC | 2026-09-05 08:29 UTC | 18m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-09-05 08:02 UTC | 2026-09-05 08:29 UTC | 27m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-09-05 08:21 UTC | 2026-09-05 08:29 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
