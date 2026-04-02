# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_22:38:00_UTC-green)

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

**Latest saved flight:** 2026-04-02 22:38:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-02 22:38:00 UTC

- **12,310** saved flights
- **7,039** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,310** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **153,067.4 tonnes** estimated CO2 emissions
- **8,873,475 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 546 |
| 2 | Ryanair | 482 |
| 3 | IndiGo | 329 |
| 4 | EJA | 244 |
| 5 | American Airlines | 229 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 184 |
| 8 | ENY | 160 |
| 9 | Vueling | 131 |
| 10 | LATAM Airlines | 125 |
| 11 | AXM | 120 |
| 12 | LXJ | 116 |
| 13 | All Nippon Airways | 103 |
| 14 | QLK | 101 |
| 15 | Delta Air Lines | 95 |
| 16 | Swiss International | 95 |
| 17 | WIF | 95 |
| 18 | AZU | 92 |
| 19 | VIV | 89 |
| 20 | Alaska Airlines | 84 |
| 21 | United Airlines | 82 |
| 22 | AXB | 81 |
| 23 | Cathay Pacific | 79 |
| 24 | EDV | 77 |
| 25 | easyJet | 77 |
| 26 | Japan Airlines | 77 |
| 27 | EJU | 73 |
| 28 | BRC | 71 |
| 29 | Avianca | 70 |
| 30 | GLO | 69 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10048 |
| 2 | 🇮🇳 IN | 1020 |
| 3 | 🇪🇸 ES | 955 |
| 4 | 🇦🇺 AU | 924 |
| 5 | 🇧🇷 BR | 689 |
| 6 | 🇩🇪 DE | 670 |
| 7 | 🇨🇴 CO | 607 |
| 8 | 🇯🇵 JP | 597 |
| 9 | 🇨🇦 CA | 572 |
| 10 | 🇮🇹 IT | 558 |
| 11 | 🇬🇧 GB | 465 |
| 12 | 🇲🇽 MX | 444 |
| 13 | 🇫🇷 FR | 399 |
| 14 | 🇬🇷 GR | 305 |
| 15 | 🇳🇴 NO | 301 |
| 16 | 🇨🇭 CH | 297 |
| 17 | 🇳🇿 NZ | 280 |
| 18 | 🇲🇾 MY | 273 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇬🇹 GT | 232 |
| 21 | 🇵🇭 PH | 218 |
| 22 | 🇹🇷 TR | 213 |
| 23 | 🇰🇷 KR | 204 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 150 |
| 26 | 🇲🇴 MO | 147 |
| 27 | 🇲🇦 MA | 145 |
| 28 | 🇮🇩 ID | 143 |
| 29 | 🇧🇸 BS | 125 |
| 30 | 🇲🇪 ME | 121 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 302 |
| 2 | Denver International Airport |  | US | 226 |
| 3 | Indira Gandhi International Airport |  | IN | 221 |
| 4 | Tokyo International Airport |  | JP | 213 |
| 5 | El Dorado International Airport |  | CO | 210 |
| 6 | Frankfurt am Main International Airport |  | DE | 184 |
| 7 | Harry Reid International Airport |  | US | 167 |
| 8 | La Aurora Airport |  | GT | 162 |
| 9 | Guaymaral Airport |  | CO | 153 |
| 10 | Zurich Airport |  | CH | 148 |
| 11 | Macau International Airport |  | MO | 147 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 140 |
| 13 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 135 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 121 |
| 16 | Chicago O'Hare International Airport |  | US | 119 |
| 17 | Bengaluru International Airport |  | IN | 114 |
| 18 | Charlotte/Douglas International Airport |  | US | 109 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 108 |
| 20 | Madrid Barajas International Airport |  | ES | 108 |
| 21 | Congonhas Airport |  | BR | 107 |
| 22 | Tenerife Norte Airport |  | ES | 106 |
| 23 | Kuala Lumpur International Airport |  | MY | 104 |
| 24 | Ninoy Aquino International Airport |  | PH | 98 |
| 25 | Reno/Tahoe International Airport |  | US | 97 |
| 26 | Daniel K Inouye International Airport |  | US | 93 |
| 27 | Vitoria/Foronda Airport |  | ES | 92 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 29 | Salt Lake City International Airport |  | US | 92 |
| 30 | Malpensa International Airport |  | IT | 91 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 90 |
| 32 | Charles de Gaulle International Airport |  | FR | 87 |
| 33 | Barcelona International Airport |  | ES | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 84 |
| 35 | Seattle-Tacoma International Airport |  | US | 83 |
| 36 | Austin-Bergstrom International Airport |  | US | 82 |
| 37 | Pune Airport |  | IN | 82 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 80 |
| 39 | Miami International Airport |  | US | 78 |
| 40 | Bodø Airport |  | NO | 78 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 58 | 14m | 114 km | 113.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 52 | 1h 7m | 706 km | 633.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 42 | 24m | 225 km | 162.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 40 | 29m | 304 km | 209.7 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 34 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 31 | 23m | 99 km | 53.1 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 29 | 1h 26m | 910 km | 455.1 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 26 | 53m | 546 km | 244.8 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 26 | 30m | 369 km | 165.5 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 25 | 1h 56m | 1,304 km | 562.4 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 21 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 22 | 1h 10m | 770 km | 292.3 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 21 | 23m | 252 km | 91.2 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 21 | 11m | 127 km | 46.0 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 20 | 1h 1m | 723 km | 249.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 20 | 13m | 99 km | 34.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 27 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 18 | 8h 30m | 38 km | 11.7 t |
| 29 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 18 | 26m | 69 km | 21.5 t |
| 30 | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 18 | 21m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-02 22:08 UTC | 2026-04-02 22:38 UTC | 29m |
| BRG570 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-02 22:07 UTC | 2026-04-02 22:35 UTC | 27m |
| N50CU |  | Jonesville Airport (KL32) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-02 21:21 UTC | 2026-04-02 22:31 UTC | 1h 10m |
| CGIAC | CGI | Toronto Pearson International Airport (CYYZ) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-02 19:27 UTC | 2026-04-02 22:31 UTC | 3h 3m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-02 14:18 UTC | 2026-04-02 22:30 UTC | 8h 12m |
| N669BB |  | Dallas Love Field (KDAL) | XS61 (XS61) | 2026-04-02 21:58 UTC | 2026-04-02 22:28 UTC | 30m |
| RIPPER2 | RIP | OK79 (OK79) | Pierce Airport (TE10) | 2026-04-02 22:07 UTC | 2026-04-02 22:28 UTC | 21m |
| AAE242 | AAE | Henri Coanda International Airport (LROP) | Macau International Airport (VMMC) | 2026-04-02 13:00 UTC | 2026-04-02 22:28 UTC | 9h 27m |
| N916QT |  | Elizabeth City Cg Air Station/Regional Airport (KECG) | Hampton Roads Executive Airport (KPVG) | 2026-04-02 21:22 UTC | 2026-04-02 22:27 UTC | 1h 4m |
| YNL | YNL | Adelaide Parafield Airport (YPPF) | Balaklava Airport (YBVA) | 2026-04-02 22:10 UTC | 2026-04-02 22:26 UTC | 16m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-02 21:47 UTC | 2026-04-02 22:24 UTC | 37m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-02 11:44 UTC | 2026-04-02 22:20 UTC | 10h 36m |
| STMPD19 | STM | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Borrego Air Ranch Airport (58CL) | 2026-04-02 22:00 UTC | 2026-04-02 22:18 UTC | 18m |
| XBM | XBM | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-02 21:40 UTC | 2026-04-02 22:18 UTC | 37m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-02 11:05 UTC | 2026-04-02 22:18 UTC | 11h 12m |
| N420FJ |  | Sequoia Field (KD86) | Telluride Regional Airport (KTEX) | 2026-04-02 20:35 UTC | 2026-04-02 22:13 UTC | 1h 37m |
| LXJ339 | LXJ | Tucson International Airport (KTUS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-02 20:20 UTC | 2026-04-02 22:11 UTC | 1h 51m |
| N491LG |  | Tall Timber Airport (CD28) | La Garita Creek Ranch Airport (5CO6) | 2026-04-02 21:57 UTC | 2026-04-02 22:07 UTC | 10m |
| N413CE |  | Bob Hope Airport (KBUR) | San Gabriel Valley Airport (KEMT) | 2026-04-02 22:00 UTC | 2026-04-02 22:05 UTC | 4m |
| N9303N |  | Addington Field (4TX8) | Lazy 9 Ranch Airport (TX64) | 2026-04-02 21:41 UTC | 2026-04-02 21:57 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
