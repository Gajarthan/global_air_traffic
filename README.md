# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_06:02:59_UTC-green)

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

**Latest saved flight:** 2026-03-30 06:02:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-03-30 06:02:59 UTC

- **3,856** saved flights
- **2,816** unique routes
- **99** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **3,856** saved routes in the archive
- **1h 18m** average flight duration

### Carbon Footprint Estimate

- **49,558.1 tonnes** estimated CO2 emissions
- **2,872,933 km** total distance flown
- **879 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 214 |
| 2 | Ryanair | 129 |
| 3 | IndiGo | 93 |
| 4 | EJA | 92 |
| 5 | American Airlines | 84 |
| 6 | Southwest Airlines | 70 |
| 7 | ENY | 63 |
| 8 | Lufthansa | 53 |
| 9 | AXM | 46 |
| 10 | Delta Air Lines | 42 |
| 11 | LATAM Airlines | 39 |
| 12 | LXJ | 37 |
| 13 | Vueling | 36 |
| 14 | United Airlines | 33 |
| 15 | VIV | 31 |
| 16 | All Nippon Airways | 30 |
| 17 | Avianca | 28 |
| 18 | QLK | 28 |
| 19 | Cathay Pacific | 27 |
| 20 | EDV | 27 |
| 21 | Alaska Airlines | 25 |
| 22 | AXB | 25 |
| 23 | Japan Airlines | 24 |
| 24 | WIF | 24 |
| 25 | AZU | 22 |
| 26 | Swiss International | 22 |
| 27 | ARE | 21 |
| 28 | MXY | 21 |
| 29 | JST | 19 |
| 30 | JIA | 18 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 3530 |
| 2 | 🇪🇸 ES | 275 |
| 3 | 🇮🇳 IN | 271 |
| 4 | 🇦🇺 AU | 252 |
| 5 | 🇨🇴 CO | 227 |
| 6 | 🇯🇵 JP | 186 |
| 7 | 🇧🇷 BR | 177 |
| 8 | 🇨🇦 CA | 165 |
| 9 | 🇩🇪 DE | 162 |
| 10 | 🇲🇽 MX | 161 |
| 11 | 🇮🇹 IT | 138 |
| 12 | 🇬🇧 GB | 120 |
| 13 | 🇲🇾 MY | 99 |
| 14 | 🇬🇹 GT | 98 |
| 15 | 🇫🇷 FR | 94 |
| 16 | 🇵🇭 PH | 89 |
| 17 | 🇿🇦 ZA | 84 |
| 18 | 🇨🇭 CH | 74 |
| 19 | 🇳🇴 NO | 73 |
| 20 | 🇬🇷 GR | 72 |
| 21 | 🇳🇿 NZ | 58 |
| 22 | 🇹🇷 TR | 50 |
| 23 | 🇮🇩 ID | 49 |
| 24 | 🇹🇭 TH | 49 |
| 25 | 🇧🇸 BS | 46 |
| 26 | 🇵🇱 PL | 43 |
| 27 | 🇰🇷 KR | 41 |
| 28 | 🇲🇦 MA | 41 |
| 29 | 🇲🇴 MO | 40 |
| 30 | 🇫🇮 FI | 38 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 110 |
| 2 | El Dorado International Airport |  | CO | 83 |
| 3 | Denver International Airport |  | US | 81 |
| 4 | La Aurora Airport |  | GT | 64 |
| 5 | Indira Gandhi International Airport |  | IN | 62 |
| 6 | Tokyo International Airport |  | JP | 61 |
| 7 | Frankfurt am Main International Airport |  | DE | 55 |
| 8 | Guaymaral Airport |  | CO | 54 |
| 9 | Phoenix Sky Harbor International Airport |  | US | 52 |
| 10 | Hartsfield/Jackson Atlanta International Airport |  | US | 50 |
| 11 | Tenerife Norte Airport |  | ES | 49 |
| 12 | Harry Reid International Airport |  | US | 46 |
| 13 | Chicago O'Hare International Airport |  | US | 45 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 41 |
| 15 | Atizapan De Zaragoza Airport |  | MX | 41 |
| 16 | Macau International Airport |  | MO | 40 |
| 17 | Ninoy Aquino International Airport |  | PH | 39 |
| 18 | Charlotte/Douglas International Airport |  | US | 38 |
| 19 | Kuala Lumpur International Airport |  | MY | 38 |
| 20 | Zurich Airport |  | CH | 37 |
| 21 | Reno/Tahoe International Airport |  | US | 33 |
| 22 | Miami International Airport |  | US | 33 |
| 23 | Eleftherios Venizelos International Airport |  | GR | 31 |
| 24 | Los Angeles International Airport |  | US | 31 |
| 25 | Centennial Airport |  | US | 31 |
| 26 | Salt Lake City International Airport |  | US | 31 |
| 27 | O. R. Tambo International Airport |  | ZA | 30 |
| 28 | Madrid Barajas International Airport |  | ES | 29 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 29 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 29 |
| 31 | Daniel K Inouye International Airport |  | US | 28 |
| 32 | CO86 |  |  | 28 |
| 33 | Tampa International Airport |  | US | 28 |
| 34 | Vitoria/Foronda Airport |  | ES | 28 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 28 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 28 |
| 37 | General Edward Lawrence Logan International Airport |  | US | 27 |
| 38 | Seattle-Tacoma International Airport |  | US | 27 |
| 39 | Austin-Bergstrom International Airport |  | US | 26 |
| 40 | Bengaluru International Airport |  | IN | 26 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 26 | 14m | 114 km | 51.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 21 | 27m | - | - |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 20 | 24m | 225 km | 77.6 t |
| 4 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 16 | 25m | 99 km | 27.4 t |
| 5 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 14 | 25m | 152 km | 36.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 13 | 30m | - | - |
| 7 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 13 | 20m | 250 km | 56.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 12 | 1h 39m | 1,423 km | 294.5 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 12 | 1h 6m | 706 km | 146.1 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 11 | 15m | 206 km | 39.1 t |
| 11 | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 11 | 29m | 69 km | 13.1 t |
| 12 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 10 | 30m | 369 km | 63.7 t |
| 13 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 10 | 12m | 99 km | 17.1 t |
| 14 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 10 | 1h 56m | 1,304 km | 225.0 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 9 | 29m | 275 km | 42.6 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 9 | 22m | 252 km | 39.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 9 | 21m | 165 km | 25.6 t |
| 18 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 9 | 4m | - | - |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 8 | 28m | 304 km | 41.9 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 8 | 52m | 546 km | 75.3 t |
| 21 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 8 | 18m | 183 km | 25.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Karad Airport (VA1M) | 8 | 1h 46m | 1,290 km | 178.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 8 | 11m | 127 km | 17.5 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 8 | 1h 26m | 910 km | 125.5 t |
| 25 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 8 | 36m | 431 km | 59.5 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 8 | 52m | 136 km | 18.8 t |
| 27 | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 8 | 12m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 7 | 1h 59m | 1,156 km | 139.6 t |
| 29 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 7 | 1h 10m | 770 km | 93.0 t |
| 30 | El Dorado International Airport (SKBO) | Alfonso Lopez Pumarejo Airport (SKVP) | 7 | 51m | 645 km | 77.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QXE2062 | QXE | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-03-30 05:04 UTC | 2026-03-30 06:02 UTC | 58m |
| CES5033 | China Eastern | Shenzhen Bao'an International Airport (ZGSZ) | Incheon International Airport (RKSI) | 2026-03-29 23:27 UTC | 2026-03-30 05:59 UTC | 6h 31m |
| XNV | XNV | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-03-30 05:12 UTC | 2026-03-30 05:54 UTC | 41m |
| KEQ | KEQ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-03-30 04:46 UTC | 2026-03-30 05:38 UTC | 52m |
| KAOS14 | KAO | Nowra Airport (YSNW) | Cooma Snowy Mountains Airport (YCOM) | 2026-03-30 04:46 UTC | 2026-03-30 05:35 UTC | 48m |
| ASA1196 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Kaluakoi Airport (HI49) | 2026-03-30 04:57 UTC | 2026-03-30 05:22 UTC | 25m |
| LT612 |  | Ensenada Airport (MMES) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-03-29 23:44 UTC | 2026-03-30 05:21 UTC | 5h 37m |
| KAL699T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-03-30 04:48 UTC | 2026-03-30 05:14 UTC | 25m |
| N35519 |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-03-30 04:59 UTC | 2026-03-30 05:13 UTC | 14m |
| LLR802 | LLR | Dehradun Airport (VIDN) | Shimla Airport (VISM) | 2026-03-30 04:50 UTC | 2026-03-30 05:13 UTC | 23m |
| UBG533 | UBG | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-03-30 04:49 UTC | 2026-03-30 05:12 UTC | 23m |
| EWG6T | EWG | Stuttgart Airport (EDDS) | Visoko Sport Airfield (LQVI) | 2026-03-30 04:07 UTC | 2026-03-30 05:11 UTC | 1h 4m |
| ELV | ELV | Watts Bridge Airport (YWSG) | Brisbane Archerfield Airport (YBAF) | 2026-03-30 04:34 UTC | 2026-03-30 05:07 UTC | 32m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-03-30 04:13 UTC | 2026-03-30 05:06 UTC | 53m |
| IGO126F | IndiGo | Pune Airport (VAPO) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-03-30 00:18 UTC | 2026-03-30 05:05 UTC | 4h 47m |
| DAL428 | Delta Air Lines | Los Angeles International Airport (KLAX) | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | 2026-03-29 23:22 UTC | 2026-03-30 05:05 UTC | 5h 42m |
| JA576A |  | Ashiya Airport (RJFA) | Saga Airport (RJFS) | 2026-03-30 04:47 UTC | 2026-03-30 05:05 UTC | 17m |
| KAL499T | Korean Air | Gimpo International Airport (RKSS) | Daegu Airport (RKTN) | 2026-03-30 04:37 UTC | 2026-03-30 05:00 UTC | 23m |
| N936EA |  | Chenango Bridge Airport (1NK8) | Tweed/New Haven Airport (KHVN) | 2026-03-30 04:33 UTC | 2026-03-30 05:00 UTC | 27m |
| NIU | NIU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-03-30 04:45 UTC | 2026-03-30 04:59 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
