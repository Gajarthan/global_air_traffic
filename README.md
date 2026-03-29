# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_07:47:40_UTC-green)

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

**Latest saved flight:** 2026-03-29 07:47:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 07:47:40 UTC

- **1,473** saved flights
- **1,221** unique routes
- **75** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,473** saved routes in the archive
- **1h 18m** average flight duration

### Carbon Footprint Estimate

- **18,664.9 tonnes** estimated CO2 emissions
- **1,082,023 km** total distance flown
- **873 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 41 |
| 3 | Southwest Airlines | 40 |
| 4 | American Airlines | 33 |
| 5 | EJA | 33 |
| 6 | ENY | 30 |
| 7 | IndiGo | 26 |
| 8 | United Airlines | 22 |
| 9 | Delta Air Lines | 20 |
| 10 | BRC | 17 |
| 11 | LXJ | 17 |
| 12 | LATAM Airlines | 15 |
| 13 | Alaska Airlines | 13 |
| 14 | Avianca | 12 |
| 15 | AXM | 12 |
| 16 | Cathay Pacific | 12 |
| 17 | Vueling | 12 |
| 18 | APG | 11 |
| 19 | EDV | 11 |
| 20 | Japan Airlines | 11 |
| 21 | QLK | 11 |
| 22 | VIV | 11 |
| 23 | Lufthansa | 10 |
| 24 | SFR | 10 |
| 25 | JST | 9 |
| 26 | All Nippon Airways | 8 |
| 27 | AZU | 8 |
| 28 | LYM | 8 |
| 29 | TGC | 8 |
| 30 | ARE | 7 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1546 |
| 2 | 🇦🇺 AU | 105 |
| 3 | 🇨🇴 CO | 89 |
| 4 | 🇪🇸 ES | 78 |
| 5 | 🇯🇵 JP | 74 |
| 6 | 🇮🇳 IN | 72 |
| 7 | 🇨🇦 CA | 69 |
| 8 | 🇲🇽 MX | 65 |
| 9 | 🇬🇹 GT | 55 |
| 10 | 🇧🇷 BR | 53 |
| 11 | 🇵🇭 PH | 47 |
| 12 | 🇮🇹 IT | 45 |
| 13 | 🇬🇧 GB | 34 |
| 14 | 🇩🇪 DE | 33 |
| 15 | 🇲🇾 MY | 29 |
| 16 | 🇿🇦 ZA | 26 |
| 17 | 🇳🇿 NZ | 22 |
| 18 | 🇬🇷 GR | 20 |
| 19 | 🇮🇩 ID | 19 |
| 20 | 🇫🇷 FR | 19 |
| 21 | 🇨🇭 CH | 19 |
| 22 | 🇹🇭 TH | 17 |
| 23 | 🇰🇷 KR | 16 |
| 24 | 🇧🇸 BS | 16 |
| 25 | 🇹🇷 TR | 16 |
| 26 | 🇲🇴 MO | 15 |
| 27 | 🇭🇳 HN | 14 |
| 28 | 🇲🇦 MA | 14 |
| 29 | 🇵🇱 PL | 14 |
| 30 | 🇧🇪 BE | 11 |

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
| 9 | Tokyo International Airport |  | JP | 21 |
| 10 | Ninoy Aquino International Airport |  | PH | 21 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 12 | Sydney Kingsford Smith International Airport |  | AU | 18 |
| 13 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 14 | Miami International Airport |  | US | 17 |
| 15 | Indira Gandhi International Airport |  | IN | 16 |
| 16 | Salt Lake City International Airport |  | US | 16 |
| 17 | Los Angeles International Airport |  | US | 15 |
| 18 | Tenerife Norte Airport |  | ES | 15 |
| 19 | Seattle-Tacoma International Airport |  | US | 15 |
| 20 | Macau International Airport |  | MO | 15 |
| 21 | Wasig Airport |  | PH | 14 |
| 22 | Tampa International Airport |  | US | 14 |
| 23 | CO86 |  |  | 13 |
| 24 | The Florida Keys Marathon International Airport |  | US | 13 |
| 25 | Reno/Tahoe International Airport |  | US | 13 |
| 26 | Vancouver International Airport |  | CA | 13 |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 28 | Daniel K Inouye International Airport |  | US | 12 |
| 29 | Yampa Valley Airport |  | US | 12 |
| 30 | Kuala Lumpur International Airport |  | MY | 12 |
| 31 | Frankfurt am Main International Airport |  | DE | 12 |
| 32 | Centennial Airport |  | US | 12 |
| 33 | Rocky Mountain Metro Airport |  | US | 12 |
| 34 | Vitoria/Foronda Airport |  | ES | 11 |
| 35 | Albuquerque International Sunport Airport |  | US | 11 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 11 |
| 37 | Provo Municipal Airport |  | US | 11 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 11 |
| 39 | Eleftherios Venizelos International Airport |  | GR | 10 |
| 40 | Soekarno-Hatta International Airport |  | ID | 10 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 13 | 23m | 225 km | 50.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 8 | 20m | 250 km | 34.6 t |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 6 | 29m | 275 km | 28.4 t |
| 9 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 5 | 29m | - | - |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 12 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 13 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 4 | 1h 40m | 1,423 km | 98.2 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 4 | 22m | 252 km | 17.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 4 | 30m | 369 km | 25.5 t |
| 17 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 19 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 20 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 4 | 37m | 431 km | 29.7 t |
| 21 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 23 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 24 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |
| 25 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 3 | 1h 50m | - | - |
| 26 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 3 | 1h 20m | 967 km | 50.0 t |
| 27 | Harry Reid International Airport (KLAS) | Baker & Hall Airport (77CL) | 3 | 35m | 364 km | 18.8 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 3 | 28m | 304 km | 15.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 3 | 26m | 178 km | 9.2 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 3 | 41m | 431 km | 22.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CCA109 | Air China | Ninoy Aquino International Airport (RPLL) | Macau International Airport (VMMC) | 2026-03-28 22:38 UTC | 2026-03-29 07:47 UTC | 9h 9m |
| CPA3068 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-03-28 20:09 UTC | 2026-03-29 07:30 UTC | 11h 21m |
| N267LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-03-29 06:19 UTC | 2026-03-29 07:23 UTC | 1h 4m |
| ABB858 | ABB | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-03-28 18:55 UTC | 2026-03-29 07:20 UTC | 12h 25m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-03-29 07:09 UTC | 2026-03-29 07:16 UTC | 6m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-28 23:36 UTC | 2026-03-29 07:10 UTC | 7h 33m |
| SFJ25 | SFJ | Tokyo International Airport (RJTT) | Yao Airport (RJOY) | 2026-03-29 06:29 UTC | 2026-03-29 07:09 UTC | 40m |
| HSORJ2 | HSO | Borkum Airport (EDWR) | Borkum Airport (EDWR) | 2026-03-29 06:31 UTC | 2026-03-29 07:03 UTC | 31m |
| SWR4PC | Swiss International | Zurich Airport (LSZH) | Visoko Sport Airfield (LQVI) | 2026-03-29 05:51 UTC | 2026-03-29 06:54 UTC | 1h 3m |
| CLX4796 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-03-28 19:36 UTC | 2026-03-29 06:54 UTC | 11h 18m |
| PGT27QB | PGT | Milas Bodrum International Airport (LTFE) | Bandirma Airport (LTBG) | 2026-03-29 06:23 UTC | 2026-03-29 06:54 UTC | 30m |
| NAY4BX | NAY | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-03-29 06:42 UTC | 2026-03-29 06:54 UTC | 11m |
| APG223 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-03-29 06:22 UTC | 2026-03-29 06:47 UTC | 25m |
| RYR46SV | Ryanair | Poznań-Ławica Airport (EPPO) | Tortoli' / Arbatax Airport (LIET) | 2026-03-29 04:51 UTC | 2026-03-29 06:46 UTC | 1h 55m |
| AWH98A | AWH | Hannover Airport (EDDV) | Hamburg Airport (EDDH) | 2026-03-29 06:17 UTC | 2026-03-29 06:45 UTC | 27m |
| WZZ3BR | Wizz Air | M. R. Stefanik Airport (LZIB) | Pristina International Airport (BKPR) | 2026-03-29 05:43 UTC | 2026-03-29 06:43 UTC | 1h 0m |
| AXB1083 | AXB | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 2026-03-29 05:02 UTC | 2026-03-29 06:42 UTC | 1h 40m |
| AE976 |  | Sydney Bankstown Airport (YSBK) | Mudgee Airport (YMDG) | 2026-03-29 06:17 UTC | 2026-03-29 06:40 UTC | 23m |
| IGO7304 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Yongphulla Airport (VQ10) | 2026-03-29 05:27 UTC | 2026-03-29 06:38 UTC | 1h 10m |
| JST219 | JST | Melbourne International Airport (YMML) | Queenstown International Airport (NZQN) | 2026-03-29 03:57 UTC | 2026-03-29 06:37 UTC | 2h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
