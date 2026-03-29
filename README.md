# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_07:03:07_UTC-green)

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

**Latest saved flight:** 2026-03-29 07:03:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 07:03:07 UTC

- **1,417** saved flights
- **1,187** unique routes
- **75** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,417** saved routes in the archive
- **1h 17m** average flight duration

### Carbon Footprint Estimate

- **17,800.5 tonnes** estimated CO2 emissions
- **1,031,915 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Southwest Airlines | 40 |
| 3 | Ryanair | 38 |
| 4 | American Airlines | 33 |
| 5 | EJA | 33 |
| 6 | ENY | 30 |
| 7 | IndiGo | 23 |
| 8 | United Airlines | 22 |
| 9 | Delta Air Lines | 20 |
| 10 | BRC | 17 |
| 11 | LXJ | 17 |
| 12 | LATAM Airlines | 15 |
| 13 | Alaska Airlines | 13 |
| 14 | Avianca | 12 |
| 15 | Vueling | 12 |
| 16 | EDV | 11 |
| 17 | VIV | 11 |
| 18 | AXM | 10 |
| 19 | Cathay Pacific | 10 |
| 20 | QLK | 10 |
| 21 | Japan Airlines | 9 |
| 22 | SFR | 9 |
| 23 | All Nippon Airways | 8 |
| 24 | APG | 8 |
| 25 | AZU | 8 |
| 26 | Lufthansa | 8 |
| 27 | LYM | 8 |
| 28 | TGC | 8 |
| 29 | ARE | 7 |
| 30 | CXK | 7 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1542 |
| 2 | 🇦🇺 AU | 98 |
| 3 | 🇨🇴 CO | 89 |
| 4 | 🇪🇸 ES | 70 |
| 5 | 🇨🇦 CA | 69 |
| 6 | 🇲🇽 MX | 65 |
| 7 | 🇮🇳 IN | 65 |
| 8 | 🇯🇵 JP | 63 |
| 9 | 🇬🇹 GT | 55 |
| 10 | 🇧🇷 BR | 53 |
| 11 | 🇮🇹 IT | 43 |
| 12 | 🇵🇭 PH | 34 |
| 13 | 🇬🇧 GB | 34 |
| 14 | 🇩🇪 DE | 25 |
| 15 | 🇲🇾 MY | 25 |
| 16 | 🇿🇦 ZA | 22 |
| 17 | 🇳🇿 NZ | 21 |
| 18 | 🇫🇷 FR | 19 |
| 19 | 🇬🇷 GR | 17 |
| 20 | 🇰🇷 KR | 16 |
| 21 | 🇧🇸 BS | 16 |
| 22 | 🇹🇭 TH | 15 |
| 23 | 🇮🇩 ID | 15 |
| 24 | 🇭🇳 HN | 14 |
| 25 | 🇨🇭 CH | 13 |
| 26 | 🇲🇦 MA | 13 |
| 27 | 🇹🇷 TR | 13 |
| 28 | 🇵🇱 PL | 12 |
| 29 | 🇲🇴 MO | 12 |
| 30 | 🇮🇪 IE | 9 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | La Aurora Airport |  | GT | 34 |
| 4 | El Dorado International Airport |  | CO | 32 |
| 5 | Guaymaral Airport |  | CO | 24 |
| 6 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 7 | Chicago O'Hare International Airport |  | US | 22 |
| 8 | Harry Reid International Airport |  | US | 21 |
| 9 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 10 | Sydney Kingsford Smith International Airport |  | AU | 18 |
| 11 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 12 | Miami International Airport |  | US | 17 |
| 13 | Tokyo International Airport |  | JP | 17 |
| 14 | Los Angeles International Airport |  | US | 15 |
| 15 | Ninoy Aquino International Airport |  | PH | 15 |
| 16 | Seattle-Tacoma International Airport |  | US | 15 |
| 17 | Salt Lake City International Airport |  | US | 15 |
| 18 | Indira Gandhi International Airport |  | IN | 14 |
| 19 | Tampa International Airport |  | US | 14 |
| 20 | CO86 |  |  | 13 |
| 21 | The Florida Keys Marathon International Airport |  | US | 13 |
| 22 | Reno/Tahoe International Airport |  | US | 13 |
| 23 | Vancouver International Airport |  | CA | 13 |
| 24 | Tenerife Norte Airport |  | ES | 13 |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 26 | Daniel K Inouye International Airport |  | US | 12 |
| 27 | Yampa Valley Airport |  | US | 12 |
| 28 | Macau International Airport |  | MO | 12 |
| 29 | Centennial Airport |  | US | 12 |
| 30 | Rocky Mountain Metro Airport |  | US | 12 |
| 31 | Wasig Airport |  | PH | 11 |
| 32 | Kuala Lumpur International Airport |  | MY | 11 |
| 33 | Albuquerque International Sunport Airport |  | US | 11 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 11 |
| 35 | Provo Municipal Airport |  | US | 11 |
| 36 | George Bush Intcntl/Houston Airport |  | US | 11 |
| 37 | Charlotte/Douglas International Airport |  | US | 10 |
| 38 | San Francisco International Airport |  | US | 10 |
| 39 | Vitoria/Foronda Airport |  | ES | 10 |
| 40 | Capua Airport |  | IT | 10 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 10 | 23m | 225 km | 38.8 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 6 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 7 | 20m | 250 km | 30.2 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 8 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 5 | 29m | 275 km | 23.7 t |
| 10 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 11 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 4 | 1h 40m | 1,423 km | 98.2 t |
| 13 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 14 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 4 | 30m | - | - |
| 15 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 16 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 17 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 4 | 1h 28m | 910 km | 62.8 t |
| 18 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 20 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 21 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |
| 22 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 3 | 1h 50m | - | - |
| 23 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 3 | 1h 20m | 967 km | 50.0 t |
| 24 | Harry Reid International Airport (KLAS) | Baker & Hall Airport (77CL) | 3 | 35m | 364 km | 18.8 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 3 | 28m | 304 km | 15.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 3 | 26m | 178 km | 9.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 3 | 41m | 431 km | 22.3 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 3 | 21m | 252 km | 13.0 t |
| 29 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 3 | 55m | 723 km | 37.4 t |
| 30 | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 3 | 39m | 330 km | 17.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HSORJ2 | HSO | Borkum Airport (EDWR) | Borkum Airport (EDWR) | 2026-03-29 06:31 UTC | 2026-03-29 07:03 UTC | 31m |
| CLX4796 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-03-28 19:36 UTC | 2026-03-29 06:54 UTC | 11h 18m |
| AWH98A | AWH | Hannover Airport (EDDV) | Hamburg Airport (EDDH) | 2026-03-29 06:17 UTC | 2026-03-29 06:45 UTC | 27m |
| AE976 |  | Sydney Bankstown Airport (YSBK) | Mudgee Airport (YMDG) | 2026-03-29 06:17 UTC | 2026-03-29 06:40 UTC | 23m |
| ZSKXP | ZSK | Grand Central Airport (FAGC) | Warmbaths Airport (FAWA) | 2026-03-29 06:05 UTC | 2026-03-29 06:23 UTC | 18m |
| UAL341 | United Airlines | General Edward Lawrence Logan International Airport (KBOS) | San Francisco International Airport (KSFO) | 2026-03-29 00:06 UTC | 2026-03-29 06:22 UTC | 6h 15m |
| EAI34A | EAI | Dublin Airport (EIDW) | Donegal Airport (EIDL) | 2026-03-29 05:44 UTC | 2026-03-29 06:20 UTC | 35m |
| LT617 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | San Clemente Island Nalf Airport (KNUC) | 2026-03-29 04:40 UTC | 2026-03-29 06:19 UTC | 1h 38m |
| SEH2VS | SEH | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-29 05:26 UTC | 2026-03-29 06:18 UTC | 52m |
| JA02NA |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-03-29 05:44 UTC | 2026-03-29 06:00 UTC | 15m |
| GDK56R | GDK | Klagenfurt Airport (LOWK) | Bolzano Airport (LIPB) | 2026-03-29 05:29 UTC | 2026-03-29 05:57 UTC | 28m |
| ABL8817 | ABL | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-03-29 05:29 UTC | 2026-03-29 05:56 UTC | 27m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-03-29 05:30 UTC | 2026-03-29 05:53 UTC | 22m |
| ANA679 | All Nippon Airways | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-03-29 05:00 UTC | 2026-03-29 05:52 UTC | 52m |
| VLG8RK | Vueling | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-03-29 05:26 UTC | 2026-03-29 05:51 UTC | 25m |
| N496AE |  | Spirit Of St Louis Airport (KSUS) | Spirit Of St Louis Airport (KSUS) | 2026-03-29 05:19 UTC | 2026-03-29 05:49 UTC | 30m |
| AEE274 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-03-29 05:16 UTC | 2026-03-29 05:46 UTC | 30m |
| CSW610 | CSW | Mollis Airport (LSZM) | Kukes Airport (LAKU) | 2026-03-29 04:13 UTC | 2026-03-29 05:42 UTC | 1h 28m |
| KAL1819 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-03-29 05:10 UTC | 2026-03-29 05:41 UTC | 30m |
| JAL609 | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-03-29 04:16 UTC | 2026-03-29 05:40 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
