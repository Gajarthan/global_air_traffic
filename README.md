# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_11:23:05_UTC-green)

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

**Latest saved flight:** 2026-03-29 11:23:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 11:23:05 UTC

- **1,734** saved flights
- **1,401** unique routes
- **85** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **1,734** saved routes in the archive
- **1h 23m** average flight duration

### Carbon Footprint Estimate

- **24,273.1 tonnes** estimated CO2 emissions
- **1,407,138 km** total distance flown
- **948 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 91 |
| 2 | Ryanair | 53 |
| 3 | IndiGo | 49 |
| 4 | Southwest Airlines | 40 |
| 5 | American Airlines | 33 |
| 6 | EJA | 33 |
| 7 | ENY | 30 |
| 8 | AXM | 25 |
| 9 | Lufthansa | 23 |
| 10 | United Airlines | 22 |
| 11 | Delta Air Lines | 20 |
| 12 | All Nippon Airways | 19 |
| 13 | BRC | 17 |
| 14 | Cathay Pacific | 17 |
| 15 | Japan Airlines | 17 |
| 16 | LXJ | 17 |
| 17 | LATAM Airlines | 15 |
| 18 | Vueling | 15 |
| 19 | Alaska Airlines | 13 |
| 20 | QLK | 13 |
| 21 | SFR | 13 |
| 22 | Avianca | 12 |
| 23 | APG | 11 |
| 24 | EDV | 11 |
| 25 | VIV | 11 |
| 26 | AXB | 10 |
| 27 | JST | 10 |
| 28 | Swiss International | 10 |
| 29 | VOE | 10 |
| 30 | AZU | 9 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1557 |
| 2 | 🇮🇳 IN | 134 |
| 3 | 🇯🇵 JP | 122 |
| 4 | 🇦🇺 AU | 119 |
| 5 | 🇪🇸 ES | 116 |
| 6 | 🇨🇴 CO | 89 |
| 7 | 🇩🇪 DE | 71 |
| 8 | 🇨🇦 CA | 69 |
| 9 | 🇲🇽 MX | 65 |
| 10 | 🇮🇹 IT | 61 |
| 11 | 🇵🇭 PH | 57 |
| 12 | 🇧🇷 BR | 55 |
| 13 | 🇬🇹 GT | 55 |
| 14 | 🇿🇦 ZA | 54 |
| 15 | 🇬🇧 GB | 53 |
| 16 | 🇲🇾 MY | 52 |
| 17 | 🇬🇷 GR | 38 |
| 18 | 🇫🇷 FR | 34 |
| 19 | 🇹🇭 TH | 33 |
| 20 | 🇨🇭 CH | 29 |
| 21 | 🇮🇩 ID | 27 |
| 22 | 🇰🇷 KR | 26 |
| 23 | 🇲🇴 MO | 25 |
| 24 | 🇹🇷 TR | 23 |
| 25 | 🇳🇿 NZ | 22 |
| 26 | 🇵🇱 PL | 21 |
| 27 | 🇫🇮 FI | 21 |
| 28 | 🇨🇳 CN | 17 |
| 29 | 🇲🇦 MA | 17 |
| 30 | 🇧🇸 BS | 16 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 42 |
| 2 | Tokyo International Airport |  | JP | 39 |
| 3 | Denver International Airport |  | US | 35 |
| 4 | La Aurora Airport |  | GT | 34 |
| 5 | El Dorado International Airport |  | CO | 32 |
| 6 | Indira Gandhi International Airport |  | IN | 30 |
| 7 | Frankfurt am Main International Airport |  | DE | 29 |
| 8 | Macau International Airport |  | MO | 25 |
| 9 | Guaymaral Airport |  | CO | 24 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 23 |
| 11 | Ninoy Aquino International Airport |  | PH | 23 |
| 12 | Chicago O'Hare International Airport |  | US | 22 |
| 13 | Kuala Lumpur International Airport |  | MY | 22 |
| 14 | Harry Reid International Airport |  | US | 21 |
| 15 | Tenerife Norte Airport |  | ES | 21 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 20 |
| 17 | O. R. Tambo International Airport |  | ZA | 20 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 18 |
| 20 | Netaji Subhash Chandra Bose International Airport |  | IN | 18 |
| 21 | Miami International Airport |  | US | 17 |
| 22 | Zurich Airport |  | CH | 17 |
| 23 | Zhuhai Airport |  | CN | 16 |
| 24 | Wasig Airport |  | PH | 16 |
| 25 | Salt Lake City International Airport |  | US | 16 |
| 26 | Eleftherios Venizelos International Airport |  | GR | 15 |
| 27 | Los Angeles International Airport |  | US | 15 |
| 28 | Vitoria/Foronda Airport |  | ES | 15 |
| 29 | Bengaluru International Airport |  | IN | 15 |
| 30 | Seattle-Tacoma International Airport |  | US | 15 |
| 31 | Amsterdam Airport Schiphol |  | NL | 15 |
| 32 | Tampa International Airport |  | US | 14 |
| 33 | Soekarno-Hatta International Airport |  | ID | 13 |
| 34 | CO86 |  |  | 13 |
| 35 | The Florida Keys Marathon International Airport |  | US | 13 |
| 36 | Reno/Tahoe International Airport |  | US | 13 |
| 37 | Vancouver International Airport |  | CA | 13 |
| 38 | Charles de Gaulle International Airport |  | FR | 13 |
| 39 | Don Mueang International Airport |  | TH | 13 |
| 40 | VGZR |  |  | 13 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 10 | 26m | - | - |
| 3 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 10 | 20m | 250 km | 43.2 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 9 | 14m | 114 km | 17.7 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 9 | 29m | - | - |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 9 | 25m | 99 km | 15.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 7 | 29m | 275 km | 33.2 t |
| 9 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 7 | 22m | 252 km | 30.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 7 | 1h 7m | 706 km | 85.2 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 7 | 25m | 152 km | 18.3 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 6 | 1h 40m | 1,423 km | 147.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 5 | 52m | 546 km | 47.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 17 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 5 | 1h 27m | 910 km | 78.5 t |
| 19 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |
| 22 | Tokyo International Airport (RJTT) | Akeno Airport (RJOE) | 4 | 30m | 305 km | 21.0 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 4 | 12m | 99 km | 6.9 t |
| 24 | Diosdado Macapagal International Airport (RPLC) | Mamburao Airport (RPUM) | 4 | 32m | 220 km | 15.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 4 | 1h 43m | 1,290 km | 89.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 4 | 2h 2m | 1,652 km | 114.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 4 | 11m | 127 km | 8.8 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 4 | 22m | 165 km | 11.4 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 4 | 9m | - | - |
| 30 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 4 | 9h 26m | 38 km | 2.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXBDZ | SXB | Megara Airport (LGMG) | Syros Airport (LGSO) | 2026-03-29 10:01 UTC | 2026-03-29 11:23 UTC | 1h 21m |
| AZG998 | AZG | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-03-28 16:21 UTC | 2026-03-29 11:06 UTC | 18h 44m |
| BRU949 | BRU | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-03-29 10:50 UTC | 2026-03-29 11:04 UTC | 14m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-03-28 23:12 UTC | 2026-03-29 10:43 UTC | 11h 30m |
| DLH99H | Lufthansa | Munich International Airport (EDDM) | Fayence Airport (LFMF) | 2026-03-29 09:38 UTC | 2026-03-29 10:39 UTC | 1h 1m |
| HB2633 |  | Lodrino Air Base (LSML) | Sondrio Caiolo Airport (LILO) | 2026-03-29 09:59 UTC | 2026-03-29 10:39 UTC | 39m |
| N75UM |  | Livingston County/Spencer J Hardy Airport (KOZW) | Black River Ranch Airport (1MI3) | 2026-03-29 10:12 UTC | 2026-03-29 10:39 UTC | 26m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-03-28 22:29 UTC | 2026-03-29 10:36 UTC | 12h 6m |
| EZY86ZC | easyJet | London Gatwick Airport (EGKK) | Tivat Airport (LYTV) | 2026-03-29 08:24 UTC | 2026-03-29 10:29 UTC | 2h 5m |
| FNG8 | FNG | Genbole Airport (EFGE) | Kymi Airport (EFKY) | 2026-03-29 09:52 UTC | 2026-03-29 10:26 UTC | 34m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-03-29 09:56 UTC | 2026-03-29 10:25 UTC | 28m |
| N66HR |  | Damme Airport (EDWC) | Leer-Papenburg Airport (EDWF) | 2026-03-29 10:06 UTC | 2026-03-29 10:22 UTC | 15m |
| CMA576 | CMA | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-03-28 22:02 UTC | 2026-03-29 10:21 UTC | 12h 19m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-03-29 09:24 UTC | 2026-03-29 10:20 UTC | 56m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 19:32 UTC | 2026-03-29 10:13 UTC | 14h 40m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-29 09:45 UTC | 2026-03-29 10:12 UTC | 26m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-03-29 09:24 UTC | 2026-03-29 10:08 UTC | 43m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-03-29 09:18 UTC | 2026-03-29 10:06 UTC | 47m |
| CSB507 | CSB | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-03-29 07:57 UTC | 2026-03-29 10:04 UTC | 2h 7m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-03-28 20:03 UTC | 2026-03-29 10:03 UTC | 13h 59m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
