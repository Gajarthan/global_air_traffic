# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_08:33:50_UTC-green)

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

**Latest saved flight:** 2026-03-29 08:33:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 08:33:50 UTC

- **1,531** saved flights
- **1,264** unique routes
- **80** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,531** saved routes in the archive
- **1h 19m** average flight duration

### Carbon Footprint Estimate

- **20,172.1 tonnes** estimated CO2 emissions
- **1,169,395 km** total distance flown
- **903 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 46 |
| 3 | Southwest Airlines | 40 |
| 4 | American Airlines | 33 |
| 5 | EJA | 33 |
| 6 | ENY | 30 |
| 7 | IndiGo | 30 |
| 8 | United Airlines | 22 |
| 9 | Delta Air Lines | 20 |
| 10 | BRC | 17 |
| 11 | LXJ | 17 |
| 12 | AXM | 16 |
| 13 | LATAM Airlines | 15 |
| 14 | Cathay Pacific | 14 |
| 15 | Alaska Airlines | 13 |
| 16 | Lufthansa | 13 |
| 17 | Japan Airlines | 13 |
| 18 | Vueling | 13 |
| 19 | Avianca | 12 |
| 20 | QLK | 12 |
| 21 | APG | 11 |
| 22 | EDV | 11 |
| 23 | VIV | 11 |
| 24 | SFR | 10 |
| 25 | All Nippon Airways | 9 |
| 26 | JST | 9 |
| 27 | AZU | 8 |
| 28 | LYM | 8 |
| 29 | TGC | 8 |
| 30 | ARE | 7 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1548 |
| 2 | 🇦🇺 AU | 109 |
| 3 | 🇨🇴 CO | 89 |
| 4 | 🇮🇳 IN | 88 |
| 5 | 🇪🇸 ES | 86 |
| 6 | 🇯🇵 JP | 82 |
| 7 | 🇨🇦 CA | 69 |
| 8 | 🇲🇽 MX | 65 |
| 9 | 🇬🇹 GT | 55 |
| 10 | 🇧🇷 BR | 53 |
| 11 | 🇵🇭 PH | 49 |
| 12 | 🇮🇹 IT | 48 |
| 13 | 🇩🇪 DE | 42 |
| 14 | 🇬🇧 GB | 40 |
| 15 | 🇲🇾 MY | 35 |
| 16 | 🇿🇦 ZA | 30 |
| 17 | 🇬🇷 GR | 25 |
| 18 | 🇳🇿 NZ | 22 |
| 19 | 🇫🇷 FR | 21 |
| 20 | 🇨🇭 CH | 20 |
| 21 | 🇹🇭 TH | 20 |
| 22 | 🇮🇩 ID | 19 |
| 23 | 🇰🇷 KR | 18 |
| 24 | 🇲🇴 MO | 18 |
| 25 | 🇹🇷 TR | 18 |
| 26 | 🇵🇱 PL | 16 |
| 27 | 🇧🇸 BS | 16 |
| 28 | 🇲🇦 MA | 15 |
| 29 | 🇭🇳 HN | 14 |
| 30 | 🇳🇱 NL | 12 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Denver International Airport |  | US | 35 |
| 3 | La Aurora Airport |  | GT | 34 |
| 4 | El Dorado International Airport |  | CO | 32 |
| 5 | Tokyo International Airport |  | JP | 25 |
| 6 | Guaymaral Airport |  | CO | 24 |
| 7 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 8 | Chicago O'Hare International Airport |  | US | 22 |
| 9 | Harry Reid International Airport |  | US | 21 |
| 10 | Indira Gandhi International Airport |  | IN | 21 |
| 11 | Ninoy Aquino International Airport |  | PH | 21 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 18 |
| 14 | Macau International Airport |  | MO | 18 |
| 15 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 16 | Miami International Airport |  | US | 17 |
| 17 | Salt Lake City International Airport |  | US | 16 |
| 18 | Los Angeles International Airport |  | US | 15 |
| 19 | Tenerife Norte Airport |  | ES | 15 |
| 20 | Seattle-Tacoma International Airport |  | US | 15 |
| 21 | Frankfurt am Main International Airport |  | DE | 15 |
| 22 | Wasig Airport |  | PH | 14 |
| 23 | Tampa International Airport |  | US | 14 |
| 24 | CO86 |  |  | 13 |
| 25 | The Florida Keys Marathon International Airport |  | US | 13 |
| 26 | Reno/Tahoe International Airport |  | US | 13 |
| 27 | Vancouver International Airport |  | CA | 13 |
| 28 | Kuala Lumpur International Airport |  | MY | 13 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 13 |
| 30 | Eleftherios Venizelos International Airport |  | GR | 12 |
| 31 | Daniel K Inouye International Airport |  | US | 12 |
| 32 | Yampa Valley Airport |  | US | 12 |
| 33 | Centennial Airport |  | US | 12 |
| 34 | Rocky Mountain Metro Airport |  | US | 12 |
| 35 | Vitoria/Foronda Airport |  | ES | 11 |
| 36 | Zurich Airport |  | CH | 11 |
| 37 | Bengaluru International Airport |  | IN | 11 |
| 38 | Amsterdam Airport Schiphol |  | NL | 11 |
| 39 | Albuquerque International Sunport Airport |  | US | 11 |
| 40 | O. R. Tambo International Airport |  | ZA | 11 |

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
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 6 | 30m | - | - |
| 10 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 5 | 52m | 546 km | 47.1 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 13 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 4 | 28m | 304 km | 21.0 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 4 | 1h 40m | 1,423 km | 98.2 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 4 | 22m | 252 km | 17.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 4 | 30m | 369 km | 25.5 t |
| 19 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 21 | Miami International Airport (KMIA) | The Florida Keys Marathon International Airport (KMTH) | 4 | 18m | 141 km | 9.8 t |
| 22 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 4 | 1h 6m | 706 km | 48.7 t |
| 23 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 4 | 37m | 431 km | 29.7 t |
| 24 | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 4 | 13m | - | - |
| 25 | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 4 | 32m | 127 km | 8.7 t |
| 26 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 4 | 12m | - | - |
| 27 | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 4 | 20m | - | - |
| 28 | Dallas-Fort Worth International Airport (KDFW) | CO86 (CO86) | 3 | 1h 50m | - | - |
| 29 | Phoenix Sky Harbor International Airport (KPHX) | Reno/Tahoe International Airport (KRNO) | 3 | 1h 20m | 967 km | 50.0 t |
| 30 | Harry Reid International Airport (KLAS) | Baker & Hall Airport (77CL) | 3 | 35m | 364 km | 18.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA2252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-03-28 20:38 UTC | 2026-03-29 08:33 UTC | 11h 55m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-03-28 20:35 UTC | 2026-03-29 08:30 UTC | 11h 54m |
| TRA37R | TRA | Salzburg Airport (LOWS) | Amsterdam Airport Schiphol (EHAM) | 2026-03-29 07:10 UTC | 2026-03-29 08:25 UTC | 1h 14m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-03-28 21:07 UTC | 2026-03-29 08:10 UTC | 11h 3m |
| KLM887 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-28 20:41 UTC | 2026-03-29 08:08 UTC | 11h 26m |
| CLX4806 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-03-28 20:45 UTC | 2026-03-29 08:06 UTC | 11h 20m |
| TRP7 | TRP | Sandy Point Airport (62MD) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-03-29 07:45 UTC | 2026-03-29 08:01 UTC | 15m |
| VAA010 | VAA | Mukhrani Airport (UGMM) | UGMS (UGMS) | 2026-03-29 07:19 UTC | 2026-03-29 07:50 UTC | 30m |
| AXM1493 | AXM | Tan Son Nhat International Airport (VVTS) | Mersing Airport (WMAU) | 2026-03-29 06:34 UTC | 2026-03-29 07:49 UTC | 1h 15m |
| CCA109 | Air China | Ninoy Aquino International Airport (RPLL) | Macau International Airport (VMMC) | 2026-03-28 22:38 UTC | 2026-03-29 07:47 UTC | 9h 9m |
| HST3453 | HST | Tallinn Airport (EETN) | Białystok-Krywlany Airport (EPBK) | 2026-03-29 06:48 UTC | 2026-03-29 07:47 UTC | 58m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-03-29 07:23 UTC | 2026-03-29 07:46 UTC | 23m |
| SEH2ZT | SEH | Eleftherios Venizelos International Airport (LGAV) | Andravida Airport (LGAD) | 2026-03-29 07:14 UTC | 2026-03-29 07:46 UTC | 31m |
| BAW850T | British Airways | London Heathrow Airport (EGLL) | Usti Nad Labem Airport (LKUL) | 2026-03-29 06:00 UTC | 2026-03-29 07:38 UTC | 1h 38m |
| SAS1769 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Ceska Lipa Airport (LKCE) | 2026-03-29 05:54 UTC | 2026-03-29 07:38 UTC | 1h 44m |
| RYR83SA | Ryanair | Memmingen Allgau Airport (EDJA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-03-29 06:29 UTC | 2026-03-29 07:38 UTC | 1h 9m |
| RYR91ZT | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Grosenhain Airport (EDAK) | 2026-03-29 06:20 UTC | 2026-03-29 07:38 UTC | 1h 18m |
| AFR78RT | Air France | Charles de Gaulle International Airport (LFPG) | Lyon Saint-Exupery Airport (LFLL) | 2026-03-29 06:45 UTC | 2026-03-29 07:33 UTC | 47m |
| CPA3068 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-03-28 20:09 UTC | 2026-03-29 07:30 UTC | 11h 21m |
| VOE3931 | VOE | Francisco de Sá Carneiro Airport (LPPR) | La Morgal Airport (LEMR) | 2026-03-29 06:46 UTC | 2026-03-29 07:24 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
