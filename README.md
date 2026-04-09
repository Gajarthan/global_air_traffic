# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_05:03:04_UTC-green)

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

**Latest saved flight:** 2026-04-09 05:03:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 05:03:04 UTC

- **24,548** saved flights
- **11,832** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,548** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **303,631.9 tonnes** estimated CO2 emissions
- **17,601,847 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1021 |
| 2 | Ryanair | 1000 |
| 3 | IndiGo | 677 |
| 4 | American Airlines | 448 |
| 5 | EJA | 447 |
| 6 | Southwest Airlines | 354 |
| 7 | ENY | 324 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 249 |
| 11 | LATAM Airlines | 244 |
| 12 | QLK | 225 |
| 13 | All Nippon Airways | 223 |
| 14 | Delta Air Lines | 208 |
| 15 | LXJ | 198 |
| 16 | AZU | 193 |
| 17 | Alaska Airlines | 174 |
| 18 | Swiss International | 174 |
| 19 | VIV | 165 |
| 20 | Japan Airlines | 164 |
| 21 | easyJet | 161 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 145 |
| 27 | EDV | 145 |
| 28 | AXB | 140 |
| 29 | Cathay Pacific | 129 |
| 30 | ANZ | 128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19335 |
| 2 | 🇮🇳 IN | 2063 |
| 3 | 🇦🇺 AU | 1834 |
| 4 | 🇪🇸 ES | 1832 |
| 5 | 🇯🇵 JP | 1384 |
| 6 | 🇧🇷 BR | 1371 |
| 7 | 🇨🇴 CO | 1257 |
| 8 | 🇩🇪 DE | 1239 |
| 9 | 🇮🇹 IT | 1231 |
| 10 | 🇨🇦 CA | 1144 |
| 11 | 🇬🇧 GB | 983 |
| 12 | 🇫🇷 FR | 891 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 590 |
| 17 | 🇳🇿 NZ | 547 |
| 18 | 🇳🇴 NO | 517 |
| 19 | 🇿🇦 ZA | 516 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 471 |
| 22 | 🇵🇭 PH | 465 |
| 23 | 🇰🇷 KR | 435 |
| 24 | 🇹🇭 TH | 402 |
| 25 | 🇵🇱 PL | 357 |
| 26 | 🇲🇦 MA | 295 |
| 27 | 🇮🇩 ID | 253 |
| 28 | 🇧🇸 BS | 251 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇲🇴 MO | 244 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 584 |
| 2 | El Dorado International Airport |  | CO | 467 |
| 3 | Tokyo International Airport |  | JP | 460 |
| 4 | Denver International Airport |  | US | 433 |
| 5 | Indira Gandhi International Airport |  | IN | 428 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 325 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 255 |
| 14 | Chicago O'Hare International Airport |  | US | 253 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 252 |
| 16 | Macau International Airport |  | MO | 244 |
| 17 | Charlotte/Douglas International Airport |  | US | 230 |
| 18 | Bengaluru International Airport |  | IN | 229 |
| 19 | Ninoy Aquino International Airport |  | PH | 215 |
| 20 | Kuala Lumpur International Airport |  | MY | 215 |
| 21 | Madrid Barajas International Airport |  | ES | 211 |
| 22 | Tenerife Norte Airport |  | ES | 209 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 196 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 192 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 174 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 171 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | Seattle-Tacoma International Airport |  | US | 161 |
| 35 | O. R. Tambo International Airport |  | ZA | 161 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 37 | Pune Airport |  | IN | 160 |
| 38 | Vitoria/Foronda Airport |  | ES | 155 |
| 39 | Barcelona International Airport |  | ES | 155 |
| 40 | Calgary International Airport |  | CA | 146 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 116 | 1h 8m | 706 km | 1,412.3 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 94 | 24m | 225 km | 364.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 85 | 28m | 304 km | 445.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 72 | 1h 27m | 910 km | 1,129.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 60 | 19m | 165 km | 170.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 54 | 1h 12m | 770 km | 717.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 53 | 55m | 546 km | 499.0 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 47 | 31m | 369 km | 299.2 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 45 | 45m | 452 km | 350.7 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 42 | 1h 42m | 1,423 km | 1,030.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-08 14:18 UTC | 2026-04-09 05:03 UTC | 14h 44m |
| N965LB |  | Zamperini Field (KTOA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-04-09 03:35 UTC | 2026-04-09 04:59 UTC | 1h 23m |
| CDG | CDG | Gold Coast Airport (YBCG) | Mudgee Airport (YMDG) | 2026-04-09 03:36 UTC | 2026-04-09 04:57 UTC | 1h 20m |
| N897TD |  | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-09 04:47 UTC | 2026-04-09 04:47 UTC | 0m |
| TRPR55 | TRP | Toowoomba Airport (YTWB) | Toowoomba Airport (YTWB) | 2026-04-09 04:45 UTC | 2026-04-09 04:46 UTC | 1m |
| PGT1870 | PGT | Isparta Airport (LTBM) | Gazipasa Airport (LTFG) | 2026-04-09 04:29 UTC | 2026-04-09 04:42 UTC | 12m |
| HKC9490 | HKC | Sabiha Gokcen International Airport (LTFJ) | Macau International Airport (VMMC) | 2026-04-08 16:56 UTC | 2026-04-09 04:42 UTC | 11h 45m |
| N9897Q |  | Oxnard Airport (KOXR) | Van Nuys Airport (KVNY) | 2026-04-09 04:00 UTC | 2026-04-09 04:34 UTC | 33m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-08 17:06 UTC | 2026-04-09 04:32 UTC | 11h 26m |
| N897TD |  | Laurence G Hanscom Field (KBED) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-08 22:20 UTC | 2026-04-09 04:31 UTC | 6h 11m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Chiang Mai International Airport (VTCC) | 2026-04-09 04:17 UTC | 2026-04-09 04:30 UTC | 13m |
| TVR4703 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-08 22:02 UTC | 2026-04-09 04:30 UTC | 6h 28m |
| N485JR |  | Dillingham Airport (PADL) | King Salmon Airport (PAKN) | 2026-04-09 04:05 UTC | 2026-04-09 04:29 UTC | 23m |
| QLK861D | QLK | Brisbane International Airport (YBBN) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-04-09 02:39 UTC | 2026-04-09 04:29 UTC | 1h 49m |
| N4962H |  | Hobby Field (K77S) | Mahlon Sweet Field (KEUG) | 2026-04-09 04:14 UTC | 2026-04-09 04:28 UTC | 14m |
| ASA1202 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-04-09 04:01 UTC | 2026-04-09 04:24 UTC | 23m |
| N315NG |  | Cortez Municipal Airport (KCEZ) | Animas Air Park (K00C) | 2026-04-09 04:12 UTC | 2026-04-09 04:23 UTC | 11m |
| TWY188 | TWY | Hector International Airport (KFAR) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-09 01:15 UTC | 2026-04-09 04:22 UTC | 3h 6m |
| N743TW |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-04-09 03:32 UTC | 2026-04-09 04:11 UTC | 39m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-09 03:53 UTC | 2026-04-09 04:09 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
