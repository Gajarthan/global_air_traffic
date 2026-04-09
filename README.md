# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_11:32:31_UTC-green)

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

**Latest saved flight:** 2026-04-09 11:32:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 11:32:31 UTC

- **24,874** saved flights
- **11,950** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,874** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **309,045.7 tonnes** estimated CO2 emissions
- **17,915,693 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1028 |
| 2 | SkyWest Airlines | 1021 |
| 3 | IndiGo | 687 |
| 4 | American Airlines | 448 |
| 5 | EJA | 447 |
| 6 | Southwest Airlines | 354 |
| 7 | Lufthansa | 326 |
| 8 | ENY | 324 |
| 9 | Vueling | 258 |
| 10 | AXM | 256 |
| 11 | LATAM Airlines | 246 |
| 12 | All Nippon Airways | 230 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 209 |
| 15 | LXJ | 198 |
| 16 | AZU | 195 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 169 |
| 20 | VIV | 165 |
| 21 | easyJet | 164 |
| 22 | EJU | 160 |
| 23 | AEE | 155 |
| 24 | WIF | 155 |
| 25 | United Airlines | 149 |
| 26 | Avianca | 145 |
| 27 | EDV | 145 |
| 28 | AXB | 141 |
| 29 | Cathay Pacific | 131 |
| 30 | ANZ | 128 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19359 |
| 2 | 🇮🇳 IN | 2105 |
| 3 | 🇪🇸 ES | 1873 |
| 4 | 🇦🇺 AU | 1872 |
| 5 | 🇯🇵 JP | 1423 |
| 6 | 🇧🇷 BR | 1384 |
| 7 | 🇩🇪 DE | 1299 |
| 8 | 🇮🇹 IT | 1265 |
| 9 | 🇨🇴 CO | 1257 |
| 10 | 🇨🇦 CA | 1155 |
| 11 | 🇬🇧 GB | 1007 |
| 12 | 🇫🇷 FR | 915 |
| 13 | 🇲🇽 MX | 789 |
| 14 | 🇬🇷 GR | 708 |
| 15 | 🇨🇭 CH | 695 |
| 16 | 🇲🇾 MY | 612 |
| 17 | 🇳🇿 NZ | 550 |
| 18 | 🇳🇴 NO | 531 |
| 19 | 🇿🇦 ZA | 522 |
| 20 | 🇬🇹 GT | 482 |
| 21 | 🇹🇷 TR | 478 |
| 22 | 🇵🇭 PH | 476 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 418 |
| 25 | 🇵🇱 PL | 368 |
| 26 | 🇲🇦 MA | 306 |
| 27 | 🇮🇩 ID | 258 |
| 28 | 🇲🇪 ME | 254 |
| 29 | 🇲🇴 MO | 253 |
| 30 | 🇧🇸 BS | 251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 585 |
| 2 | Tokyo International Airport |  | JP | 475 |
| 3 | El Dorado International Airport |  | CO | 467 |
| 4 | Indira Gandhi International Airport |  | IN | 435 |
| 5 | Denver International Airport |  | US | 433 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 342 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 326 |
| 9 | Zurich Airport |  | CH | 298 |
| 10 | Frankfurt am Main International Airport |  | DE | 271 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 259 |
| 12 | Guaymaral Airport |  | CO | 259 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 256 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 15 | Macau International Airport |  | MO | 253 |
| 16 | Chicago O'Hare International Airport |  | US | 253 |
| 17 | Bengaluru International Airport |  | IN | 232 |
| 18 | Charlotte/Douglas International Airport |  | US | 230 |
| 19 | Kuala Lumpur International Airport |  | MY | 224 |
| 20 | Ninoy Aquino International Airport |  | PH | 221 |
| 21 | Madrid Barajas International Airport |  | ES | 216 |
| 22 | Tenerife Norte Airport |  | ES | 214 |
| 23 | Malpensa International Airport |  | IT | 200 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 199 |
| 25 | Congonhas Airport |  | BR | 198 |
| 26 | Salt Lake City International Airport |  | US | 194 |
| 27 | Daniel K Inouye International Airport |  | US | 193 |
| 28 | Reno/Tahoe International Airport |  | US | 184 |
| 29 | Charles de Gaulle International Airport |  | FR | 177 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 176 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 173 |
| 32 | Miami International Airport |  | US | 165 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 164 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 164 |
| 35 | O. R. Tambo International Airport |  | ZA | 163 |
| 36 | Seattle-Tacoma International Airport |  | US | 162 |
| 37 | Barcelona International Airport |  | ES | 161 |
| 38 | Pune Airport |  | IN | 160 |
| 39 | Vitoria/Foronda Airport |  | ES | 157 |
| 40 | Calgary International Airport |  | CA | 147 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 120 | 1h 8m | 706 km | 1,461.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 96 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 73 | 1h 27m | 910 km | 1,145.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 64 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 62 | 19m | 165 km | 176.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 51 | 27m | 275 km | 241.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 49 | 31m | 369 km | 311.9 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 42 | 1h 42m | 1,423 km | 1,030.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 37 | 20m | 147 km | 93.6 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OEXPH | OEX | Graz Airport (LOWG) | Graz Airport (LOWG) | 2026-04-09 11:00 UTC | 2026-04-09 11:32 UTC | 31m |
| R21234 |  | Nenana Municipal Airport (PANN) | Ladd Army Air Field (PAFB) | 2026-04-09 10:21 UTC | 2026-04-09 11:25 UTC | 1h 4m |
| YOA | YOA | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-09 10:49 UTC | 2026-04-09 11:21 UTC | 31m |
| FHTLI | FHT | Toulouse-Lasbordes Airport (LFCL) | Gaillac Lisle Sur Tarn Airport (LFDG) | 2026-04-09 10:56 UTC | 2026-04-09 11:12 UTC | 16m |
| CAL5663 | CAL | Indira Gandhi International Airport (VIDP) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-09 02:21 UTC | 2026-04-09 11:07 UTC | 8h 46m |
| CFG4WT | CFG | Václav Havel Airport (LKPR) | Wiesbaden Army Airfield (ETOU) | 2026-04-09 10:12 UTC | 2026-04-09 11:03 UTC | 51m |
| DHK813 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-09 00:21 UTC | 2026-04-09 10:57 UTC | 10h 35m |
| IGO910 | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-09 09:10 UTC | 2026-04-09 10:55 UTC | 1h 45m |
| HYD164 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-04-09 10:04 UTC | 2026-04-09 10:51 UTC | 47m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-09 10:38 UTC | 2026-04-09 10:50 UTC | 12m |
|  |  | Fazenda Entre Rios Airport (SDEO) | Fazenda Entre Rios Airport (SDEO) | 2026-04-09 10:47 UTC | 2026-04-09 10:47 UTC | 0m |
| EJU698R | EJU | Nice-Cote d'Azur Airport (LFMN) | Paris-Orly Airport (LFPO) | 2026-04-09 09:36 UTC | 2026-04-09 10:44 UTC | 1h 7m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-08 20:03 UTC | 2026-04-09 10:39 UTC | 14h 35m |
| RYR801W | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-04-09 09:43 UTC | 2026-04-09 10:37 UTC | 54m |
| OAL068 | OAL | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-09 10:16 UTC | 2026-04-09 10:35 UTC | 18m |
| SAS2728 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Turku Airport (EFTU) | 2026-04-09 10:05 UTC | 2026-04-09 10:34 UTC | 29m |
| RYR399Y | Ryanair | Copenhagen Kastrup Airport (EKCH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-09 09:20 UTC | 2026-04-09 10:33 UTC | 1h 12m |
| AEE242 | AEE | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-09 10:03 UTC | 2026-04-09 10:31 UTC | 28m |
| TVS3J | TVS | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-04-09 09:41 UTC | 2026-04-09 10:28 UTC | 46m |
| HTY206 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-09 10:01 UTC | 2026-04-09 10:27 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
