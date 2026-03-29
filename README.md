# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_15:36:25_UTC-green)

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

**Latest saved flight:** 2026-03-29 15:36:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-29 15:36:25 UTC

- **2,216** saved flights
- **1,737** unique routes
- **89** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **2,216** saved routes in the archive
- **1h 21m** average flight duration

### Carbon Footprint Estimate

- **30,283.0 tonnes** estimated CO2 emissions
- **1,755,539 km** total distance flown
- **922 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 94 |
| 2 | Ryanair | 77 |
| 3 | IndiGo | 66 |
| 4 | Southwest Airlines | 42 |
| 5 | Lufthansa | 41 |
| 6 | EJA | 40 |
| 7 | AXM | 38 |
| 8 | American Airlines | 37 |
| 9 | ENY | 36 |
| 10 | Delta Air Lines | 23 |
| 11 | LATAM Airlines | 22 |
| 12 | United Airlines | 22 |
| 13 | Vueling | 22 |
| 14 | Cathay Pacific | 21 |
| 15 | All Nippon Airways | 20 |
| 16 | Japan Airlines | 18 |
| 17 | Swiss International | 18 |
| 18 | BRC | 17 |
| 19 | LXJ | 17 |
| 20 | Avianca | 16 |
| 21 | AXB | 16 |
| 22 | VIV | 15 |
| 23 | ARE | 14 |
| 24 | SFR | 14 |
| 25 | VOE | 14 |
| 26 | APG | 13 |
| 27 | Alaska Airlines | 13 |
| 28 | EDV | 13 |
| 29 | QLK | 13 |
| 30 | AEE | 12 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 1791 |
| 2 | 🇮🇳 IN | 186 |
| 3 | 🇪🇸 ES | 176 |
| 4 | 🇨🇴 CO | 138 |
| 5 | 🇯🇵 JP | 132 |
| 6 | 🇦🇺 AU | 125 |
| 7 | 🇩🇪 DE | 120 |
| 8 | 🇧🇷 BR | 91 |
| 9 | 🇮🇹 IT | 90 |
| 10 | 🇬🇧 GB | 81 |
| 11 | 🇲🇾 MY | 79 |
| 12 | 🇨🇦 CA | 78 |
| 13 | 🇲🇽 MX | 75 |
| 14 | 🇿🇦 ZA | 74 |
| 15 | 🇵🇭 PH | 61 |
| 16 | 🇬🇹 GT | 61 |
| 17 | 🇫🇷 FR | 58 |
| 18 | 🇨🇭 CH | 55 |
| 19 | 🇬🇷 GR | 48 |
| 20 | 🇹🇭 TH | 44 |
| 21 | 🇹🇷 TR | 43 |
| 22 | 🇳🇴 NO | 38 |
| 23 | 🇮🇩 ID | 33 |
| 24 | 🇵🇱 PL | 31 |
| 25 | 🇲🇴 MO | 30 |
| 26 | 🇫🇮 FI | 28 |
| 27 | 🇲🇦 MA | 27 |
| 28 | 🇰🇷 KR | 26 |
| 29 | 🇲🇪 ME | 24 |
| 30 | 🇳🇱 NL | 24 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | El Dorado International Airport |  | CO | 50 |
| 2 | Dallas-Fort Worth International Airport |  | US | 49 |
| 3 | Tokyo International Airport |  | JP | 44 |
| 4 | Frankfurt am Main International Airport |  | DE | 44 |
| 5 | Indira Gandhi International Airport |  | IN | 42 |
| 6 | La Aurora Airport |  | GT | 39 |
| 7 | Denver International Airport |  | US | 35 |
| 8 | Guaymaral Airport |  | CO | 35 |
| 9 | Kuala Lumpur International Airport |  | MY | 32 |
| 10 | Macau International Airport |  | MO | 30 |
| 11 | Tenerife Norte Airport |  | ES | 29 |
| 12 | Zurich Airport |  | CH | 28 |
| 13 | O. R. Tambo International Airport |  | ZA | 27 |
| 14 | Ninoy Aquino International Airport |  | PH | 25 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 25 |
| 16 | Phoenix Sky Harbor International Airport |  | US | 24 |
| 17 | Chicago O'Hare International Airport |  | US | 24 |
| 18 | Harry Reid International Airport |  | US | 23 |
| 19 | Netaji Subhash Chandra Bose International Airport |  | IN | 23 |
| 20 | Eleftherios Venizelos International Airport |  | GR | 20 |
| 21 | Madrid Barajas International Airport |  | ES | 20 |
| 22 | Vitoria/Foronda Airport |  | ES | 20 |
| 23 | Charles de Gaulle International Airport |  | FR | 20 |
| 24 | Amsterdam Airport Schiphol |  | NL | 20 |
| 25 | Sydney Kingsford Smith International Airport |  | AU | 19 |
| 26 | VGZR |  |  | 19 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 19 |
| 28 | Miami International Airport |  | US | 18 |
| 29 | Bengaluru International Airport |  | IN | 18 |
| 30 | Zhuhai Airport |  | CN | 17 |
| 31 | Don Mueang International Airport |  | TH | 17 |
| 32 | Wasig Airport |  | PH | 16 |
| 33 | Perales Airport |  | CO | 16 |
| 34 | Centennial Airport |  | US | 16 |
| 35 | Salt Lake City International Airport |  | US | 16 |
| 36 | Newcastle Airport |  | ZA | 16 |
| 37 | Soekarno-Hatta International Airport |  | ID | 15 |
| 38 | Los Angeles International Airport |  | US | 15 |
| 39 | Helsinki Vantaa Airport |  | FI | 15 |
| 40 | Yongphulla Airport |  | BT | 15 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 16 | 14m | 114 km | 31.4 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 14 | 23m | 225 km | 54.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 14 | 26m | - | - |
| 4 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 5 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 12 | 30m | - | - |
| 6 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 10 | 1h 39m | 1,423 km | 245.4 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 10 | 24m | 99 km | 17.1 t |
| 8 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 9 | 1h 7m | 706 km | 109.6 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 9 | 25m | 152 km | 23.5 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 8 | 30m | 275 km | 37.9 t |
| 12 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 8 | 12m | 99 km | 13.7 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 7 | 28m | 304 km | 36.7 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 7 | 21m | 165 km | 19.9 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 6 | 14m | 206 km | 21.3 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 6 | 52m | 546 km | 56.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Sepulot Airport (WBKO) | 6 | 2h 4m | 1,652 km | 171.0 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 6 | 11m | 127 km | 13.1 t |
| 19 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 6 | 8h 51m | 38 km | 3.9 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 6 | 1h 27m | 910 km | 94.2 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 6 | 17m | 55 km | 5.7 t |
| 22 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 6 | 52m | 136 km | 14.1 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 5 | 29m | 369 km | 31.8 t |
| 24 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 5 | 1h 44m | 1,290 km | 111.3 t |
| 25 | O. R. Tambo International Airport (FAOR) | Durnacol Airport (FADH) | 5 | 22m | 275 km | 23.7 t |
| 26 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 5 | 36m | 431 km | 37.2 t |
| 27 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 5 | 27m | 69 km | 6.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 5 | 1h 55m | 1,304 km | 112.5 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 4 | 25m | 178 km | 12.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 4 | 42m | 431 km | 29.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MNB213 | MNB | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-03-28 16:20 UTC | 2026-03-29 15:36 UTC | 23h 15m |
| XAUVL | XAU | General Ignacio P. Garcia International Airport (MMHO) | General Ignacio P. Garcia International Airport (MMHO) | 2026-03-29 14:27 UTC | 2026-03-29 15:26 UTC | 58m |
| N507RP |  | Outlaw Field (KCKV) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-03-29 14:00 UTC | 2026-03-29 15:25 UTC | 1h 25m |
| N88ML |  | Joe Foss Field (KFSD) | 4MN4 (4MN4) | 2026-03-29 14:42 UTC | 2026-03-29 15:21 UTC | 39m |
| CFXIN | CFX | Burlington Executive (CZBA) | Burlington Executive (CZBA) | 2026-03-29 13:27 UTC | 2026-03-29 15:21 UTC | 1h 53m |
| IBE04GH | Iberia | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-03-29 14:33 UTC | 2026-03-29 15:18 UTC | 44m |
| N483LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 14:26 UTC | 2026-03-29 15:18 UTC | 51m |
| N8868E |  | Hidden Valley Airport (AZ43) | Hidden Valley Airport (AZ43) | 2026-03-29 15:09 UTC | 2026-03-29 15:14 UTC | 4m |
| N257EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 14:21 UTC | 2026-03-29 15:13 UTC | 51m |
| AFR93SM | Air France | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-03-29 14:08 UTC | 2026-03-29 15:12 UTC | 1h 4m |
| N252EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-03-29 14:18 UTC | 2026-03-29 15:11 UTC | 53m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-03-29 14:09 UTC | 2026-03-29 15:11 UTC | 1h 1m |
| N43138 |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-03-29 14:39 UTC | 2026-03-29 15:10 UTC | 30m |
| N73964 |  | Grosse Ile Municipal Airport (KONZ) | Grosse Ile Municipal Airport (KONZ) | 2026-03-29 15:04 UTC | 2026-03-29 15:05 UTC | 1m |
| FFL1356 | FFL | Hop Brook Farm Airport (NJ72) | Hop Brook Farm Airport (NJ72) | 2026-03-29 14:59 UTC | 2026-03-29 15:04 UTC | 4m |
| N331ST |  | Phoenix Deer Valley Airport (KDVT) | 42AZ (42AZ) | 2026-03-29 14:41 UTC | 2026-03-29 15:03 UTC | 22m |
| OXF3373 | OXF | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-03-29 14:29 UTC | 2026-03-29 15:02 UTC | 32m |
| N13715 |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-03-29 14:45 UTC | 2026-03-29 15:01 UTC | 16m |
| N2107L |  | Eby Field (II74) | Owensboro/Daviess County Regional Airport (KOWB) | 2026-03-29 13:31 UTC | 2026-03-29 15:00 UTC | 1h 29m |
| EJM736 | EJM | William P Hobby Airport (KHOU) | Lincoln Airport (KLNK) | 2026-03-29 13:17 UTC | 2026-03-29 14:58 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
