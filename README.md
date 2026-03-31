# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_20:06:42_UTC-green)

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

**Latest saved flight:** 2026-03-31 20:06:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-31 20:06:42 UTC

- **7,423** saved flights
- **4,777** unique routes
- **106** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **7,423** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **92,454.2 tonnes** estimated CO2 emissions
- **5,359,666 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 353 |
| 2 | Ryanair | 285 |
| 3 | IndiGo | 198 |
| 4 | EJA | 157 |
| 5 | American Airlines | 143 |
| 6 | Southwest Airlines | 117 |
| 7 | Lufthansa | 115 |
| 8 | ENY | 104 |
| 9 | AXM | 78 |
| 10 | Vueling | 78 |
| 11 | LATAM Airlines | 75 |
| 12 | LXJ | 67 |
| 13 | Delta Air Lines | 64 |
| 14 | WIF | 58 |
| 15 | All Nippon Airways | 57 |
| 16 | QLK | 56 |
| 17 | Swiss International | 55 |
| 18 | AXB | 51 |
| 19 | VIV | 51 |
| 20 | AZU | 50 |
| 21 | United Airlines | 49 |
| 22 | Alaska Airlines | 48 |
| 23 | EDV | 48 |
| 24 | Cathay Pacific | 47 |
| 25 | Japan Airlines | 47 |
| 26 | Avianca | 42 |
| 27 | EJU | 42 |
| 28 | easyJet | 41 |
| 29 | AEE | 39 |
| 30 | BRC | 39 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 6345 |
| 2 | 🇮🇳 IN | 602 |
| 3 | 🇪🇸 ES | 574 |
| 4 | 🇦🇺 AU | 510 |
| 5 | 🇩🇪 DE | 381 |
| 6 | 🇧🇷 BR | 368 |
| 7 | 🇮🇹 IT | 342 |
| 8 | 🇨🇴 CO | 342 |
| 9 | 🇯🇵 JP | 338 |
| 10 | 🇨🇦 CA | 335 |
| 11 | 🇬🇧 GB | 260 |
| 12 | 🇲🇽 MX | 258 |
| 13 | 🇫🇷 FR | 227 |
| 14 | 🇳🇴 NO | 194 |
| 15 | 🇲🇾 MY | 177 |
| 16 | 🇬🇷 GR | 175 |
| 17 | 🇨🇭 CH | 167 |
| 18 | 🇬🇹 GT | 165 |
| 19 | 🇿🇦 ZA | 161 |
| 20 | 🇹🇷 TR | 134 |
| 21 | 🇵🇭 PH | 132 |
| 22 | 🇳🇿 NZ | 124 |
| 23 | 🇹🇭 TH | 94 |
| 24 | 🇵🇱 PL | 92 |
| 25 | 🇲🇦 MA | 91 |
| 26 | 🇮🇩 ID | 89 |
| 27 | 🇲🇴 MO | 81 |
| 28 | 🇰🇷 KR | 77 |
| 29 | 🇧🇸 BS | 73 |
| 30 | 🇲🇪 ME | 71 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 181 |
| 2 | Indira Gandhi International Airport |  | IN | 136 |
| 3 | Denver International Airport |  | US | 135 |
| 4 | Tokyo International Airport |  | JP | 121 |
| 5 | El Dorado International Airport |  | CO | 117 |
| 6 | La Aurora Airport |  | GT | 117 |
| 7 | Frankfurt am Main International Airport |  | DE | 115 |
| 8 | Harry Reid International Airport |  | US | 103 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 91 |
| 10 | Zurich Airport |  | CH | 87 |
| 11 | Guaymaral Airport |  | CO | 86 |
| 12 | Eleftherios Venizelos International Airport |  | GR | 82 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 82 |
| 14 | Macau International Airport |  | MO | 81 |
| 15 | Chicago O'Hare International Airport |  | US | 80 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 75 |
| 17 | Tenerife Norte Airport |  | ES | 72 |
| 18 | Madrid Barajas International Airport |  | ES | 70 |
| 19 | Reno/Tahoe International Airport |  | US | 68 |
| 20 | Bengaluru International Airport |  | IN | 67 |
| 21 | Kuala Lumpur International Airport |  | MY | 65 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 63 |
| 23 | Charlotte/Douglas International Airport |  | US | 60 |
| 24 | Salt Lake City International Airport |  | US | 60 |
| 25 | Ninoy Aquino International Airport |  | PH | 59 |
| 26 | Vitoria/Foronda Airport |  | ES | 59 |
| 27 | Daniel K Inouye International Airport |  | US | 58 |
| 28 | Malpensa International Airport |  | IT | 57 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 56 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 55 |
| 31 | Miami International Airport |  | US | 54 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 54 |
| 33 | Seattle-Tacoma International Airport |  | US | 53 |
| 34 | Congonhas Airport |  | BR | 53 |
| 35 | Charles de Gaulle International Airport |  | FR | 52 |
| 36 | Pune Airport |  | IN | 51 |
| 37 | George Bush Intcntl/Houston Airport |  | US | 49 |
| 38 | Barcelona International Airport |  | ES | 48 |
| 39 | Centennial Airport |  | US | 47 |
| 40 | O. R. Tambo International Airport |  | ZA | 47 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 34 | 14m | 114 km | 66.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 34 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 28 | 1h 6m | 706 km | 340.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 27 | 24m | 225 km | 104.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 25 | 31m | - | - |
| 6 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 25 | 27m | 152 km | 65.3 t |
| 7 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 21 | 1h 47m | 1,156 km | 418.9 t |
| 8 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 21 | 4m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 21 | 24m | 99 km | 36.0 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 20 | 15m | 206 km | 71.1 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 20 | 28m | 275 km | 94.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 20 | 1h 42m | 1,423 km | 490.8 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 20 | 20m | 165 km | 56.9 t |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 19 | 29m | 304 km | 99.6 t |
| 15 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 18 | 8m | - | - |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 16 | 1h 25m | 910 km | 251.1 t |
| 17 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 16 | 1h 10m | 770 km | 212.5 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 16 | 51m | 556 km | 153.4 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 15 | 30m | 369 km | 95.5 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 14 | 23m | 252 km | 60.8 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 14 | 1h 0m | 723 km | 174.5 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 14 | 53m | 546 km | 131.8 t |
| 23 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 14 | 32m | - | - |
| 24 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 14 | 28m | 69 km | 16.7 t |
| 25 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 14 | 20m | 250 km | 60.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 13 | 1h 45m | 1,290 km | 289.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 13 | 11m | 127 km | 28.5 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 13 | 22m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 13 | 1h 55m | 1,304 km | 292.5 t |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 12 | 8h 41m | 38 km | 7.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N567L |  | Fairbanks International Airport (PAFA) | Nenana Municipal Airport (PANN) | 2026-03-31 19:07 UTC | 2026-03-31 20:06 UTC | 59m |
| N198X |  | John Wayne/Orange County Airport (KSNA) | Apple Valley Airport (KAPV) | 2026-03-31 19:47 UTC | 2026-03-31 20:05 UTC | 17m |
| N903NS |  | Roy Hurd Memorial Airport (KE01) | 74XS (74XS) | 2026-03-31 17:54 UTC | 2026-03-31 19:51 UTC | 1h 56m |
| BCS7823 | BCS | Ancona / Falconara Airport (LIPY) | Malpensa International Airport (LIMC) | 2026-03-31 18:56 UTC | 2026-03-31 19:44 UTC | 48m |
| RYR55HD | Ryanair | Edinburgh Airport (EGPH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-03-31 17:21 UTC | 2026-03-31 19:43 UTC | 2h 21m |
| N576CT |  | Brigham City Regional Airport (KBMC) | Downey/Hyde Memorial/ Airport (KU58) | 2026-03-31 18:46 UTC | 2026-03-31 19:41 UTC | 55m |
| N562DB |  | Falcon Field (KFFZ) | Henderson Executive Airport (KHND) | 2026-03-31 18:48 UTC | 2026-03-31 19:39 UTC | 51m |
| AMF7126 | AMF | Portland International Airport (KPDX) | Chiloquin State Airport (K2S7) | 2026-03-31 18:32 UTC | 2026-03-31 19:39 UTC | 1h 6m |
| N63177 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-03-31 19:37 UTC | 2026-03-31 19:38 UTC | 1m |
| HANG51 | HAN | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-03-31 19:13 UTC | 2026-03-31 19:37 UTC | 23m |
| WAH | WAH | Nikolai Creek Airport (9AK3) | Trading Bay Production Airport (5AK0) | 2026-03-31 19:24 UTC | 2026-03-31 19:32 UTC | 8m |
| TGARL | TGA | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-03-31 19:25 UTC | 2026-03-31 19:31 UTC | 6m |
| CXK549 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-03-31 19:06 UTC | 2026-03-31 19:31 UTC | 25m |
| TEXGLD | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-03-31 19:20 UTC | 2026-03-31 19:30 UTC | 10m |
| N459SP |  | Addison Airport (KADS) | J Ranch Airport (41TX) | 2026-03-31 18:43 UTC | 2026-03-31 19:29 UTC | 46m |
| STT62 | STT | San Francisco International Airport (KSFO) | OR73 (OR73) | 2026-03-31 18:12 UTC | 2026-03-31 19:28 UTC | 1h 16m |
| LW12 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-03-31 17:12 UTC | 2026-03-31 19:28 UTC | 2h 15m |
| BOE223 | BOE | Boeing Field/King County International Airport (KBFI) | 8WA5 (8WA5) | 2026-03-31 18:13 UTC | 2026-03-31 19:27 UTC | 1h 13m |
| N38RL |  | Sandpoint Airport (KSZT) | NV23 (NV23) | 2026-03-31 17:35 UTC | 2026-03-31 19:24 UTC | 1h 49m |
| N9421F |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-03-31 19:07 UTC | 2026-03-31 19:24 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
