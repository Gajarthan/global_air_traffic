# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_11:29:58_UTC-green)

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

**Latest saved flight:** 2026-03-30 11:29:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 11:29:58 UTC

- **4,174** saved flights
- **2,991** unique routes
- **102** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **4,174** saved routes in the archive
- **1h 20m** average flight duration

### Carbon Footprint Estimate

- **55,475.8 tonnes** estimated CO2 emissions
- **3,215,988 km** total distance flown
- **903 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 149 |
| 3 | IndiGo | 107 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | Lufthansa | 64 |
| 8 | ENY | 63 |
| 9 | AXM | 54 |
| 10 | Vueling | 44 |
| 11 | Delta Air Lines | 42 |
| 12 | LATAM Airlines | 42 |
| 13 | All Nippon Airways | 38 |
| 14 | LXJ | 37 |
| 15 | QLK | 33 |
| 16 | United Airlines | 33 |
| 17 | Japan Airlines | 32 |
| 18 | Swiss International | 31 |
| 19 | VIV | 31 |
| 20 | AXB | 30 |
| 21 | Cathay Pacific | 30 |
| 22 | Avianca | 28 |
| 23 | EDV | 27 |
| 24 | WIF | 27 |
| 25 | Alaska Airlines | 25 |
| 26 | AZU | 24 |
| 27 | VOE | 22 |
| 28 | ARE | 21 |
| 29 | MXY | 21 |
| 30 | JST | 20 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3572 |
| 2 | 🇮🇳 IN | 326 |
| 3 | 🇪🇸 ES | 318 |
| 4 | 🇦🇺 AU | 285 |
| 5 | 🇯🇵 JP | 234 |
| 6 | 🇨🇴 CO | 227 |
| 7 | 🇧🇷 BR | 193 |
| 8 | 🇩🇪 DE | 190 |
| 9 | 🇮🇹 IT | 175 |
| 10 | 🇨🇦 CA | 167 |
| 11 | 🇲🇽 MX | 161 |
| 12 | 🇬🇧 GB | 139 |
| 13 | 🇲🇾 MY | 116 |
| 14 | 🇫🇷 FR | 115 |
| 15 | 🇿🇦 ZA | 109 |
| 16 | 🇵🇭 PH | 101 |
| 17 | 🇬🇹 GT | 98 |
| 18 | 🇨🇭 CH | 97 |
| 19 | 🇳🇴 NO | 89 |
| 20 | 🇬🇷 GR | 83 |
| 21 | 🇹🇷 TR | 66 |
| 22 | 🇳🇿 NZ | 63 |
| 23 | 🇹🇭 TH | 60 |
| 24 | 🇮🇩 ID | 55 |
| 25 | 🇲🇴 MO | 55 |
| 26 | 🇵🇱 PL | 52 |
| 27 | 🇰🇷 KR | 49 |
| 28 | 🇲🇦 MA | 47 |
| 29 | 🇧🇸 BS | 46 |
| 30 | 🇫🇮 FI | 41 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | Tokyo International Airport |  | JP | 78 |
| 5 | Indira Gandhi International Airport |  | IN | 76 |
| 6 | Frankfurt am Main International Airport |  | DE | 66 |
| 7 | La Aurora Airport |  | GT | 64 |
| 8 | Macau International Airport |  | MO | 55 |
| 9 | Guaymaral Airport |  | CO | 54 |
| 10 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 11 | Tenerife Norte Airport |  | ES | 52 |
| 12 | Zurich Airport |  | CH | 51 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 14 | Harry Reid International Airport |  | US | 48 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 46 |
| 16 | Chicago O'Hare International Airport |  | US | 45 |
| 17 | Ninoy Aquino International Airport |  | PH | 44 |
| 18 | Kuala Lumpur International Airport |  | MY | 42 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 20 | Charlotte/Douglas International Airport |  | US | 38 |
| 21 | O. R. Tambo International Airport |  | ZA | 38 |
| 22 | Eleftherios Venizelos International Airport |  | GR | 37 |
| 23 | Madrid Barajas International Airport |  | ES | 37 |
| 24 | Reno/Tahoe International Airport |  | US | 33 |
| 25 | Miami International Airport |  | US | 33 |
| 26 | Vitoria/Foronda Airport |  | ES | 33 |
| 27 | Bengaluru International Airport |  | IN | 33 |
| 28 | Los Angeles International Airport |  | US | 32 |
| 29 | Centennial Airport |  | US | 32 |
| 30 | Charles de Gaulle International Airport |  | FR | 31 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 31 |
| 32 | Salt Lake City International Airport |  | US | 31 |
| 33 | Daniel K Inouye International Airport |  | US | 30 |
| 34 | Amsterdam Airport Schiphol |  | NL | 30 |
| 35 | Malpensa International Airport |  | IT | 29 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 29 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 38 | CO86 |  |  | 28 |
| 39 | Tampa International Airport |  | US | 28 |
| 40 | Austin-Bergstrom International Airport |  | US | 28 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 23 | 24m | 225 km | 89.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 4 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 17 | 30m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 16 | 1h 6m | 706 km | 194.8 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 13 | 1h 39m | 1,423 km | 319.0 t |
| 9 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 13 | 23m | 252 km | 56.4 t |
| 10 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 12 | 15m | 206 km | 42.7 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 11 | 1h 25m | 910 km | 172.6 t |
| 13 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 11 | 30m | 369 km | 70.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 11 | 21m | 165 km | 31.3 t |
| 15 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 10 | 28m | 304 km | 52.4 t |
| 17 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 10 | 29m | 275 km | 47.4 t |
| 18 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 10 | 1h 10m | 770 km | 132.8 t |
| 19 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 10 | 11m | 127 km | 21.9 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 10 | 4m | - | - |
| 23 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 9 | 52m | 546 km | 84.7 t |
| 24 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 9 | 33m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 8 | 1h 58m | 1,156 km | 159.6 t |
| 26 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 28 | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 8 | 8h 30m | 38 km | 5.2 t |
| 29 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N441WF |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-03-30 11:14 UTC | 2026-03-30 11:29 UTC | 15m |
| 0000000 |  | Pompano Beach Airpark (KPMP) | Southwest Georgia Regional Airport (KABY) | 2026-03-30 09:44 UTC | 2026-03-30 11:25 UTC | 1h 40m |
| CXK421 | CXK | Raleigh-Durham International Airport (KRDU) | Raleigh Regional At Person County Airport (KTDF) | 2026-03-30 10:59 UTC | 2026-03-30 11:15 UTC | 16m |
| TCF643 | TCF | Melbourne Orlando International Airport (KMLB) | Tampa Executive Airport (KVDF) | 2026-03-30 10:27 UTC | 2026-03-30 11:15 UTC | 47m |
| N2477S |  | Danville Regional Airport (KDAN) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-03-30 10:36 UTC | 2026-03-30 11:14 UTC | 38m |
| CXK482 | CXK | Concord-Padgett Regional Airport (KJQF) | Mid-Carolina Regional Airport (KRUQ) | 2026-03-30 10:54 UTC | 2026-03-30 11:13 UTC | 19m |
| HKC6652 | HKC | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-03-30 08:21 UTC | 2026-03-30 11:09 UTC | 2h 47m |
| SEH5ML | SEH | Milos Airport (LGML) | Eleftherios Venizelos International Airport (LGAV) | 2026-03-30 10:44 UTC | 2026-03-30 11:08 UTC | 23m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-03-30 10:39 UTC | 2026-03-30 10:50 UTC | 11m |
| YQP | YQP | Adelaide Parafield Airport (YPPF) | Kadina Airport (YKDI) | 2026-03-30 09:40 UTC | 2026-03-30 10:43 UTC | 1h 2m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-03-30 10:05 UTC | 2026-03-30 10:40 UTC | 35m |
| DLH2TR | Lufthansa | Frankfurt am Main International Airport (EDDF) | Lista Airport (ENLI) | 2026-03-30 09:16 UTC | 2026-03-30 10:38 UTC | 1h 22m |
| FFM2892 | FFM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-30 10:12 UTC | 2026-03-30 10:37 UTC | 24m |
| WMT7GM | WMT | Glasgow International Airport (EGPF) | Malpensa International Airport (LIMC) | 2026-03-30 08:39 UTC | 2026-03-30 10:36 UTC | 1h 56m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-03-30 10:15 UTC | 2026-03-30 10:36 UTC | 20m |
| DLH7LL | Lufthansa | Munich International Airport (EDDM) | Munster Osnabruck Airport (EDDG) | 2026-03-30 09:44 UTC | 2026-03-30 10:35 UTC | 51m |
| ZSMFS | ZSM | O. R. Tambo International Airport (FAOR) | Rooiberg Airport (FARO) | 2026-03-30 10:01 UTC | 2026-03-30 10:35 UTC | 33m |
| VLG6UA | Vueling | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-03-30 10:10 UTC | 2026-03-30 10:33 UTC | 23m |
| KAL1847 | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-03-30 10:04 UTC | 2026-03-30 10:32 UTC | 27m |
| RYR13QJ | Ryanair | Luqa Airport (LMML) | Salerno / Pontecagnano Airport (LIRI) | 2026-03-30 09:45 UTC | 2026-03-30 10:31 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
