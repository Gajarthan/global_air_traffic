# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_07:19:51_UTC-green)

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

**Latest saved flight:** 2026-09-06 07:19:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-06 07:19:51 UTC

- **249,159** saved flights
- **74,938** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **249,159** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,999,676.9 tonnes** estimated CO2 emissions
- **173,894,312 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9973 |
| 2 | SkyWest Airlines | 8703 |
| 3 | EJA | 4812 |
| 4 | IndiGo | 4162 |
| 5 | American Airlines | 3988 |
| 6 | Southwest Airlines | 3705 |
| 7 | Delta Air Lines | 3160 |
| 8 | ENY | 2983 |
| 9 | LATAM Airlines | 2404 |
| 10 | AZU | 2318 |
| 11 | Vueling | 2126 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1976 |
| 14 | LXJ | 1936 |
| 15 | easyJet | 1719 |
| 16 | Swiss International | 1672 |
| 17 | AXM | 1627 |
| 18 | EJU | 1604 |
| 19 | QLK | 1597 |
| 20 | United Airlines | 1565 |
| 21 | Alaska Airlines | 1491 |
| 22 | All Nippon Airways | 1460 |
| 23 | WMT | 1411 |
| 24 | GLO | 1391 |
| 25 | VIV | 1367 |
| 26 | PGT | 1366 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1343 |
| 29 | JetBlue | 1226 |
| 30 | AEE | 1224 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206685 |
| 2 | 🇪🇸 ES | 15946 |
| 3 | 🇧🇷 BR | 14562 |
| 4 | 🇦🇺 AU | 14150 |
| 5 | 🇨🇦 CA | 13846 |
| 6 | 🇮🇹 IT | 13650 |
| 7 | 🇮🇳 IN | 12984 |
| 8 | 🇩🇪 DE | 12231 |
| 9 | 🇬🇧 GB | 11691 |
| 10 | 🇨🇴 CO | 10920 |
| 11 | 🇫🇷 FR | 10034 |
| 12 | 🇯🇵 JP | 9841 |
| 13 | 🇹🇷 TR | 7423 |
| 14 | 🇬🇷 GR | 7335 |
| 15 | 🇲🇽 MX | 6891 |
| 16 | 🇨🇭 CH | 6713 |
| 17 | 🇳🇴 NO | 6158 |
| 18 | 🇹🇭 TH | 4498 |
| 19 | 🇲🇾 MY | 4366 |
| 20 | 🇿🇦 ZA | 4293 |
| 21 | 🇵🇱 PL | 4162 |
| 22 | 🇳🇿 NZ | 3405 |
| 23 | 🇵🇭 PH | 3392 |
| 24 | 🇬🇹 GT | 3123 |
| 25 | 🇰🇷 KR | 2891 |
| 26 | 🇭🇷 HR | 2863 |
| 27 | 🇲🇦 MA | 2516 |
| 28 | 🇲🇪 ME | 2333 |
| 29 | 🇳🇱 NL | 2245 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5139 |
| 2 | Denver International Airport |  | US | 4029 |
| 3 | Indira Gandhi International Airport |  | IN | 3032 |
| 4 | Tokyo International Airport |  | JP | 2937 |
| 5 | Guaymaral Airport |  | CO | 2730 |
| 6 | Harry Reid International Airport |  | US | 2652 |
| 7 | Zurich Airport |  | CH | 2606 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2530 |
| 9 | El Dorado International Airport |  | CO | 2509 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2472 |
| 11 | La Aurora Airport |  | GT | 2380 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2181 |
| 14 | Congonhas Airport |  | BR | 2140 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2055 |
| 16 | Capua Airport |  | IT | 1964 |
| 17 | Madrid Barajas International Airport |  | ES | 1960 |
| 18 | Frankfurt am Main International Airport |  | DE | 1947 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1872 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1792 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1750 |
| 23 | Charles de Gaulle International Airport |  | FR | 1748 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1731 |
| 25 | Ninoy Aquino International Airport |  | PH | 1652 |
| 26 | Macau International Airport |  | MO | 1644 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Barcelona International Airport |  | ES | 1576 |
| 29 | Charlotte/Douglas International Airport |  | US | 1575 |
| 30 | Kuala Lumpur International Airport |  | MY | 1572 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1527 |
| 32 | Viracopos International Airport |  | BR | 1488 |
| 33 | Seattle-Tacoma International Airport |  | US | 1467 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1441 |
| 36 | Calgary International Airport |  | CA | 1433 |
| 37 | Bengaluru International Airport |  | IN | 1431 |
| 38 | Oslo Gardermoen Airport |  | NO | 1399 |
| 39 | Vancouver International Airport |  | CA | 1395 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1354 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 928 | 21m | 244 km | 3,907.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 633 | 24m | 225 km | 2,455.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 627 | 1h 6m | 770 km | 8,329.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 561 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 288 | 1h 14m | 961 km | 4,773.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 285 | 19m | 144 km | 708.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 255 | 41m | 535 km | 2,355.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRD999T | BRD | Cologne Bonn Airport (EDDK) | Munster Osnabruck Airport (EDDG) | 2026-09-06 06:50 UTC | 2026-09-06 07:19 UTC | 29m |
| N8EU |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-09-06 07:12 UTC | 2026-09-06 07:18 UTC | 6m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-09-06 06:10 UTC | 2026-09-06 07:18 UTC | 1h 7m |
| EVA272 | EVA Air | Ninoy Aquino International Airport (RPLL) | Hsinchu Air Base (RCPO) | 2026-09-06 05:40 UTC | 2026-09-06 07:13 UTC | 1h 33m |
| TTW201 | TTW | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-06 03:47 UTC | 2026-09-06 06:59 UTC | 3h 11m |
| KLM807 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Hsinchu Air Base (RCPO) | 2026-09-05 19:17 UTC | 2026-09-06 06:58 UTC | 11h 40m |
| CFH24 | CFH | Coffs Harbour Airport (YSCH) | Wollomombi Airport (YWMM) | 2026-09-06 06:39 UTC | 2026-09-06 06:56 UTC | 16m |
| IGO7304 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-09-06 05:28 UTC | 2026-09-06 06:48 UTC | 1h 19m |
| RXA6178 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-09-06 06:23 UTC | 2026-09-06 06:47 UTC | 24m |
| RYR18PG | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Saiss Airport (GMFF) | 2026-09-06 04:10 UTC | 2026-09-06 06:40 UTC | 2h 30m |
| FIN4PK | Finnair | Helsinki Vantaa Airport (EFHK) | Kautokeino Air Base (ENKA) | 2026-09-06 03:42 UTC | 2026-09-06 06:40 UTC | 2h 58m |
| RYR539L | Ryanair | Bristol International Airport (EGGD) | Girona Airport (LEGE) | 2026-09-06 04:59 UTC | 2026-09-06 06:39 UTC | 1h 40m |
| AEE590 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Santorini Airport (LGSR) | 2026-09-06 05:58 UTC | 2026-09-06 06:39 UTC | 41m |
| RYR8463 | Ryanair | Palma De Mallorca Airport (LEPA) | Aarhus Airport (EKAH) | 2026-09-06 03:59 UTC | 2026-09-06 06:37 UTC | 2h 38m |
| YEO | YEO | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-06 06:16 UTC | 2026-09-06 06:36 UTC | 19m |
| SFJ81 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-06 05:31 UTC | 2026-09-06 06:35 UTC | 1h 3m |
| N353HP |  | KU42 (KU42) | K36U (K36U) | 2026-09-06 06:08 UTC | 2026-09-06 06:33 UTC | 25m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-09-05 19:08 UTC | 2026-09-06 06:31 UTC | 11h 23m |
| SXS8ZW | SXS | Antalya International Airport (LTAI) | Selcuk Efes Airport (LTFB) | 2026-09-06 05:53 UTC | 2026-09-06 06:29 UTC | 35m |
| QLK1299 | QLK | Coffs Harbour Airport (YSCH) | Melbourne International Airport (YMML) | 2026-09-06 04:39 UTC | 2026-09-06 06:27 UTC | 1h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
