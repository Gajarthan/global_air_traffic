# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_09:23:02_UTC-green)

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

**Latest saved flight:** 2026-03-29 09:23:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 09:23:02 UTC

- **1,574** saved flights
- **1,290** unique routes
- **81** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,574** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **20,985.9 tonnes** estimated CO2 emissions
- **1,216,574 km** total distance flown
- **913 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 48 |
| 3 | Southwest Airlines | 40 |
| 4 | IndiGo | 34 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | ENY | 30 |
| 8 | United Airlines | 22 |
| 9 | Delta Air Lines | 20 |
| 10 | AXM | 18 |
| 11 | BRC | 17 |
| 12 | LXJ | 17 |
| 13 | Cathay Pacific | 15 |
| 14 | Japan Airlines | 15 |
| 15 | LATAM Airlines | 15 |
| 16 | Alaska Airlines | 13 |
| 17 | Lufthansa | 13 |
| 18 | Vueling | 13 |
| 19 | Avianca | 12 |
| 20 | QLK | 12 |
| 21 | All Nippon Airways | 11 |
| 22 | APG | 11 |
| 23 | EDV | 11 |
| 24 | VIV | 11 |
| 25 | JST | 10 |
| 26 | SFR | 10 |
| 27 | AZU | 8 |
| 28 | LYM | 8 |
| 29 | TGC | 8 |
| 30 | Air France | 7 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1548 |
| 2 | 🇦🇺 AU | 115 |
| 3 | 🇮🇳 IN | 97 |
| 4 | 🇯🇵 JP | 94 |
| 5 | 🇪🇸 ES | 90 |
| 6 | 🇨🇴 CO | 89 |
| 7 | 🇨🇦 CA | 69 |
| 8 | 🇲🇽 MX | 65 |
| 9 | 🇬🇹 GT | 55 |
| 10 | 🇧🇷 BR | 53 |
| 11 | 🇵🇭 PH | 51 |
| 12 | 🇮🇹 IT | 50 |
| 13 | 🇩🇪 DE | 48 |
| 14 | 🇬🇧 GB | 45 |
| 15 | 🇲🇾 MY | 38 |
| 16 | 🇿🇦 ZA | 32 |
| 17 | 🇬🇷 GR | 27 |
| 18 | 🇫🇷 FR | 25 |
| 19 | 🇹🇭 TH | 24 |
| 20 | 🇮🇩 ID | 22 |
| 21 | 🇨🇭 CH | 22 |
| 22 | 🇳🇿 NZ | 22 |
| 23 | 🇰🇷 KR | 21 |
| 24 | 🇲🇴 MO | 20 |
| 25 | 🇹🇷 TR | 19 |
| 26 | 🇲🇦 MA | 16 |
| 27 | 🇵🇱 PL | 16 |
| 28 | 🇧🇸 BS | 16 |
| 29 | 🇭🇳 HN | 14 |
| 30 | 🇧🇪 BE | 12 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | La Aurora Airport |  | GT | 34 |
| 4 | El Dorado International Airport |  | CO | 32 |
| 5 | Tokyo International Airport |  | JP | 28 |
| 6 | Guaymaral Airport |  | CO | 24 |
| 7 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 8 | Chicago O'Hare International Airport |  | US | 22 |
| 9 | Indira Gandhi International Airport |  | IN | 22 |
| 10 | Harry Reid International Airport |  | US | 21 |
| 11 | Ninoy Aquino International Airport |  | PH | 21 |
| 12 | Macau International Airport |  | MO | 20 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 15 | Frankfurt am Main International Airport |  | DE | 18 |
| 16 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 17 | Miami International Airport |  | US | 17 |
| 18 | Tenerife Norte Airport |  | ES | 17 |
| 19 | Salt Lake City International Airport |  | US | 16 |
| 20 | Los Angeles International Airport |  | US | 15 |
| 21 | Wasig Airport |  | PH | 15 |
| 22 | Seattle-Tacoma International Airport |  | US | 15 |
| 23 | Kuala Lumpur International Airport |  | MY | 14 |
| 24 | Tampa International Airport |  | US | 14 |
| 25 | CO86 |  |  | 13 |
| 26 | The Florida Keys Marathon International Airport |  | US | 13 |
| 27 | Reno/Tahoe International Airport |  | US | 13 |
| 28 | Vancouver International Airport |  | CA | 13 |
| 29 | Zurich Airport |  | CH | 13 |
| 30 | Bengaluru International Airport |  | IN | 13 |
| 31 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 32 | Eleftherios Venizelos International Airport |  | GR | 12 |
| 33 | Daniel K Inouye International Airport |  | US | 12 |
| 34 | Yampa Valley Airport |  | US | 12 |
| 35 | Vitoria/Foronda Airport |  | ES | 12 |
| 36 | Centennial Airport |  | US | 12 |
| 37 | Rocky Mountain Metro Airport |  | US | 12 |
| 38 | O. R. Tambo International Airport |  | ZA | 12 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 12 |
| 40 | Soekarno-Hatta International Airport |  | ID | 11 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 13 | 23m | 225 km | 50.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 5 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 9 | 20m | 250 km | 38.9 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 7 | 30m | - | - |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 6 | 29m | 275 km | 28.4 t |
| 10 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 6 | 22m | 252 km | 26.1 t |
| 11 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 12 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 5 | 28m | 304 km | 26.2 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 5 | 1h 40m | 1,423 km | 122.7 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 5 | 52m | 546 km | 47.1 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 5 | 1h 6m | 706 km | 60.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 17 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 4 | 30m | 369 km | 25.5 t |
| 20 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 22 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 4 | 9h 26m | 38 km | 2.6 t |
| 23 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 24 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 4 | 37m | 431 km | 29.7 t |
| 25 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 26 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 27 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 28 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |
| 29 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 3 | 1h 50m | - | - |
| 30 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 3 | 1h 20m | 967 km | 50.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SVA984 | Saudia | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-03-28 17:04 UTC | 2026-03-29 09:23 UTC | 16h 18m |
| N47296 |  | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-03-29 08:56 UTC | 2026-03-29 09:01 UTC | 5m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-03-29 01:18 UTC | 2026-03-29 08:53 UTC | 7h 35m |
| RXA2131 | RXA | Perth International Airport (YPPH) | Denmark Airport (YDEK) | 2026-03-29 07:57 UTC | 2026-03-29 08:41 UTC | 44m |
| AM317 |  | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-03-29 07:55 UTC | 2026-03-29 08:34 UTC | 39m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-03-29 08:21 UTC | 2026-03-29 08:34 UTC | 13m |
| CPA2252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-03-28 20:38 UTC | 2026-03-29 08:33 UTC | 11h 55m |
| HGO211 | HGO | East Midlands Airport (EGNX) | Zhuhai Airport (ZGSD) | 2026-03-28 20:23 UTC | 2026-03-29 08:33 UTC | 12h 9m |
| VOE7XB | VOE | Alicante International Airport (LEAL) | Vitoria/Foronda Airport (LEVT) | 2026-03-29 07:28 UTC | 2026-03-29 08:31 UTC | 1h 2m |
| BBC615 | BBC | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-03-29 08:11 UTC | 2026-03-29 08:31 UTC | 19m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-03-28 20:35 UTC | 2026-03-29 08:30 UTC | 11h 54m |
| SWR41D | Swiss International | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-03-29 07:47 UTC | 2026-03-29 08:30 UTC | 42m |
| SXARH | SXA | Syros Airport (LGSO) | Syros Airport (LGSO) | 2026-03-29 08:03 UTC | 2026-03-29 08:30 UTC | 26m |
| EIN65Y | Aer Lingus | Dublin Airport (EIDW) | Frankfurt am Main International Airport (EDDF) | 2026-03-29 06:55 UTC | 2026-03-29 08:27 UTC | 1h 32m |
| TRA37R | TRA | Salzburg Airport (LOWS) | Amsterdam Airport Schiphol (EHAM) | 2026-03-29 07:10 UTC | 2026-03-29 08:25 UTC | 1h 14m |
| AWA445 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-03-29 07:54 UTC | 2026-03-29 08:23 UTC | 29m |
| JST527 | JST | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-03-29 07:06 UTC | 2026-03-29 08:22 UTC | 1h 15m |
| AXM429 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-03-29 07:56 UTC | 2026-03-29 08:17 UTC | 21m |
| IGO5316 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Jaipur International Airport (VIJP) | 2026-03-29 06:53 UTC | 2026-03-29 08:13 UTC | 1h 20m |
| RYR55HB | Ryanair | London Stansted Airport (EGSS) | Perugia / San Egidio Airport (LIRZ) | 2026-03-29 06:31 UTC | 2026-03-29 08:12 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
