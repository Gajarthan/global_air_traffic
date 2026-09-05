# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_21:57:35_UTC-green)

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

**Latest saved flight:** 2026-09-05 21:57:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 21:57:35 UTC

- **248,892** saved flights
- **74,895** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,892** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,995,546.6 tonnes** estimated CO2 emissions
- **173,654,873 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9965 |
| 2 | SkyWest Airlines | 8697 |
| 3 | EJA | 4805 |
| 4 | IndiGo | 4153 |
| 5 | American Airlines | 3986 |
| 6 | Southwest Airlines | 3702 |
| 7 | Delta Air Lines | 3158 |
| 8 | ENY | 2976 |
| 9 | LATAM Airlines | 2402 |
| 10 | AZU | 2317 |
| 11 | Vueling | 2122 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1974 |
| 14 | LXJ | 1935 |
| 15 | easyJet | 1718 |
| 16 | Swiss International | 1669 |
| 17 | AXM | 1627 |
| 18 | EJU | 1603 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1564 |
| 21 | Alaska Airlines | 1487 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1409 |
| 24 | GLO | 1390 |
| 25 | VIV | 1367 |
| 26 | PGT | 1364 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1343 |
| 29 | JetBlue | 1225 |
| 30 | AEE | 1223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206498 |
| 2 | 🇪🇸 ES | 15928 |
| 3 | 🇧🇷 BR | 14554 |
| 4 | 🇦🇺 AU | 14105 |
| 5 | 🇨🇦 CA | 13833 |
| 6 | 🇮🇹 IT | 13639 |
| 7 | 🇮🇳 IN | 12951 |
| 8 | 🇩🇪 DE | 12221 |
| 9 | 🇬🇧 GB | 11684 |
| 10 | 🇨🇴 CO | 10902 |
| 11 | 🇫🇷 FR | 10025 |
| 12 | 🇯🇵 JP | 9815 |
| 13 | 🇹🇷 TR | 7415 |
| 14 | 🇬🇷 GR | 7330 |
| 15 | 🇲🇽 MX | 6891 |
| 16 | 🇨🇭 CH | 6709 |
| 17 | 🇳🇴 NO | 6156 |
| 18 | 🇹🇭 TH | 4491 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4162 |
| 22 | 🇳🇿 NZ | 3399 |
| 23 | 🇵🇭 PH | 3383 |
| 24 | 🇬🇹 GT | 3121 |
| 25 | 🇰🇷 KR | 2886 |
| 26 | 🇭🇷 HR | 2860 |
| 27 | 🇲🇦 MA | 2514 |
| 28 | 🇲🇪 ME | 2331 |
| 29 | 🇳🇱 NL | 2242 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5130 |
| 2 | Denver International Airport |  | US | 4026 |
| 3 | Indira Gandhi International Airport |  | IN | 3026 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2730 |
| 6 | Harry Reid International Airport |  | US | 2651 |
| 7 | Zurich Airport |  | CH | 2604 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2530 |
| 9 | El Dorado International Airport |  | CO | 2502 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2471 |
| 11 | La Aurora Airport |  | GT | 2378 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2181 |
| 14 | Congonhas Airport |  | BR | 2140 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2051 |
| 16 | Capua Airport |  | IT | 1960 |
| 17 | Madrid Barajas International Airport |  | ES | 1956 |
| 18 | Frankfurt am Main International Airport |  | DE | 1945 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1871 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1790 |
| 22 | Charles de Gaulle International Airport |  | FR | 1748 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1730 |
| 25 | Ninoy Aquino International Airport |  | PH | 1647 |
| 26 | Macau International Airport |  | MO | 1640 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1575 |
| 29 | Barcelona International Airport |  | ES | 1574 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1527 |
| 32 | Viracopos International Airport |  | BR | 1486 |
| 33 | Seattle-Tacoma International Airport |  | US | 1464 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1448 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1432 |
| 37 | Bengaluru International Airport |  | IN | 1429 |
| 38 | Oslo Gardermoen Airport |  | NO | 1398 |
| 39 | Vancouver International Airport |  | CA | 1391 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1351 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 925 | 21m | 244 km | 3,894.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 560 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 370 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 299 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 288 | 1h 14m | 961 km | 4,773.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 285 | 19m | 144 km | 708.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA095 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-09-05 07:08 UTC | 2026-09-05 21:57 UTC | 14h 48m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Macau International Airport (VMMC) | 2026-09-05 11:14 UTC | 2026-09-05 21:52 UTC | 10h 37m |
| N227WW |  | MI50 (MI50) | MI50 (MI50) | 2026-09-05 21:00 UTC | 2026-09-05 21:50 UTC | 50m |
| N277GT |  | Trenton Mercer Airport (KTTN) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-05 19:59 UTC | 2026-09-05 21:41 UTC | 1h 41m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-05 11:08 UTC | 2026-09-05 21:41 UTC | 10h 32m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-05 10:53 UTC | 2026-09-05 21:37 UTC | 10h 43m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-09-05 17:42 UTC | 2026-09-05 21:34 UTC | 3h 52m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-05 19:52 UTC | 2026-09-05 21:34 UTC | 1h 42m |
| PERRIS2 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-09-05 21:18 UTC | 2026-09-05 21:33 UTC | 15m |
| N303EH |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-09-05 19:58 UTC | 2026-09-05 21:28 UTC | 1h 30m |
| N336MC |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-09-05 20:55 UTC | 2026-09-05 21:27 UTC | 31m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-09-05 11:17 UTC | 2026-09-05 21:25 UTC | 10h 7m |
| SD1 |  | 52TA (52TA) | 52TA (52TA) | 2026-09-05 20:30 UTC | 2026-09-05 21:23 UTC | 53m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-09-05 20:40 UTC | 2026-09-05 21:23 UTC | 42m |
|  |  | Cottonwood Airport (0MT5) | Cottonwood Airport (0MT5) | 2026-09-05 21:21 UTC | 2026-09-05 21:21 UTC | 0m |
| N117PC |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-09-05 21:17 UTC | 2026-09-05 21:21 UTC | 4m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-05 10:46 UTC | 2026-09-05 21:20 UTC | 10h 33m |
| SAS742 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Ronneby Airport (ESDF) | 2026-09-05 21:00 UTC | 2026-09-05 21:19 UTC | 19m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-05 20:25 UTC | 2026-09-05 21:18 UTC | 53m |
| N915CM |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-09-05 20:08 UTC | 2026-09-05 21:16 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
