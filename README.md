# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_17:19:11_UTC-green)

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

**Latest saved flight:** 2026-04-09 17:19:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 17:19:11 UTC

- **25,334** saved flights
- **12,134** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **25,334** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **313,460.6 tonnes** estimated CO2 emissions
- **18,171,626 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1047 |
| 2 | SkyWest Airlines | 1031 |
| 3 | IndiGo | 701 |
| 4 | American Airlines | 454 |
| 5 | EJA | 452 |
| 6 | Southwest Airlines | 358 |
| 7 | Lufthansa | 332 |
| 8 | ENY | 326 |
| 9 | Vueling | 263 |
| 10 | AXM | 260 |
| 11 | LATAM Airlines | 250 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 211 |
| 15 | LXJ | 199 |
| 16 | AZU | 198 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 175 |
| 19 | Japan Airlines | 171 |
| 20 | VIV | 170 |
| 21 | EJU | 167 |
| 22 | easyJet | 166 |
| 23 | WIF | 162 |
| 24 | AEE | 160 |
| 25 | United Airlines | 150 |
| 26 | EDV | 148 |
| 27 | Avianca | 146 |
| 28 | AXB | 143 |
| 29 | Air France | 132 |
| 30 | BRC | 132 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 19708 |
| 2 | 🇮🇳 IN | 2146 |
| 3 | 🇪🇸 ES | 1910 |
| 4 | 🇦🇺 AU | 1876 |
| 5 | 🇯🇵 JP | 1434 |
| 6 | 🇧🇷 BR | 1415 |
| 7 | 🇩🇪 DE | 1323 |
| 8 | 🇮🇹 IT | 1303 |
| 9 | 🇨🇴 CO | 1280 |
| 10 | 🇨🇦 CA | 1175 |
| 11 | 🇬🇧 GB | 1028 |
| 12 | 🇫🇷 FR | 948 |
| 13 | 🇲🇽 MX | 819 |
| 14 | 🇬🇷 GR | 729 |
| 15 | 🇨🇭 CH | 708 |
| 16 | 🇲🇾 MY | 624 |
| 17 | 🇳🇴 NO | 550 |
| 18 | 🇳🇿 NZ | 550 |
| 19 | 🇿🇦 ZA | 528 |
| 20 | 🇹🇷 TR | 484 |
| 21 | 🇬🇹 GT | 482 |
| 22 | 🇵🇭 PH | 478 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 432 |
| 25 | 🇵🇱 PL | 378 |
| 26 | 🇲🇦 MA | 313 |
| 27 | 🇮🇩 ID | 258 |
| 28 | 🇧🇸 BS | 258 |
| 29 | 🇲🇪 ME | 257 |
| 30 | 🇳🇱 NL | 255 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 590 |
| 2 | Tokyo International Airport |  | JP | 480 |
| 3 | El Dorado International Airport |  | CO | 475 |
| 4 | Indira Gandhi International Airport |  | IN | 442 |
| 5 | Denver International Airport |  | US | 434 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 354 |
| 7 | La Aurora Airport |  | GT | 332 |
| 8 | Harry Reid International Airport |  | US | 330 |
| 9 | Zurich Airport |  | CH | 300 |
| 10 | Frankfurt am Main International Airport |  | DE | 278 |
| 11 | Guaymaral Airport |  | CO | 268 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 263 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 258 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 15 | Chicago O'Hare International Airport |  | US | 255 |
| 16 | Macau International Airport |  | MO | 253 |
| 17 | Bengaluru International Airport |  | IN | 235 |
| 18 | Charlotte/Douglas International Airport |  | US | 233 |
| 19 | Kuala Lumpur International Airport |  | MY | 231 |
| 20 | Ninoy Aquino International Airport |  | PH | 222 |
| 21 | Tenerife Norte Airport |  | ES | 220 |
| 22 | Madrid Barajas International Airport |  | ES | 218 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 204 |
| 24 | Malpensa International Airport |  | IT | 204 |
| 25 | Congonhas Airport |  | BR | 200 |
| 26 | Salt Lake City International Airport |  | US | 195 |
| 27 | Daniel K Inouye International Airport |  | US | 194 |
| 28 | Reno/Tahoe International Airport |  | US | 186 |
| 29 | Charles de Gaulle International Airport |  | FR | 182 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 179 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 175 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 167 |
| 33 | Miami International Airport |  | US | 167 |
| 34 | O. R. Tambo International Airport |  | ZA | 166 |
| 35 | Barcelona International Airport |  | ES | 165 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 165 |
| 37 | Seattle-Tacoma International Airport |  | US | 162 |
| 38 | Vitoria/Foronda Airport |  | ES | 160 |
| 39 | Pune Airport |  | IN | 160 |
| 40 | Capua Airport |  | IT | 152 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 122 | 1h 8m | 706 km | 1,485.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 103 | 14m | 114 km | 202.0 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 100 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 95 | 24m | 225 km | 368.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 86 | 28m | 304 km | 450.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 74 | 1h 27m | 910 km | 1,161.2 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 65 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 64 | 19m | 165 km | 182.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 59 | 1h 12m | 770 km | 783.8 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 54 | 55m | 546 km | 508.4 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 52 | 27m | 275 km | 246.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 50 | 31m | 369 km | 318.3 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 45 | 20m | 250 km | 194.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 24 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 42 | 13m | 99 km | 72.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 37 | 12m | 15 km | 9.8 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 35 | 1h 21m | 961 km | 580.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N482DT |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-04-09 16:36 UTC | 2026-04-09 17:19 UTC | 43m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-09 17:00 UTC | 2026-04-09 17:18 UTC | 17m |
| N644BB |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-04-09 16:47 UTC | 2026-04-09 17:14 UTC | 27m |
| EVAL33 | EVA Air | Huntsville Executive Tom Sharp Jr Field (KMDQ) | Redstone Army Air Field (KHUA) | 2026-04-09 17:01 UTC | 2026-04-09 17:13 UTC | 12m |
| PAT17 | PAT | Davison Army Air Field (KDAA) | Ocean City Municipal Airport (KOXB) | 2026-04-09 15:29 UTC | 2026-04-09 17:09 UTC | 1h 40m |
| RFS702 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-04-09 15:50 UTC | 2026-04-09 17:08 UTC | 1h 17m |
| N292SP |  | Ocean County Airport (KMJX) | NJ69 (NJ69) | 2026-04-09 16:29 UTC | 2026-04-09 17:00 UTC | 31m |
| N99FF |  | Nanaimo Airport (CYCD) | Boeing Field/King County International Airport (KBFI) | 2026-04-09 16:26 UTC | 2026-04-09 16:55 UTC | 29m |
| N46210 |  | Deland Municipal-Sidney H Taylor Field (KDED) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-04-09 15:52 UTC | 2026-04-09 16:49 UTC | 57m |
| TWY235 | TWY | Pittsburgh International Airport (KPIT) | Laguardia Airport (KLGA) | 2026-04-09 15:51 UTC | 2026-04-09 16:47 UTC | 56m |
| N147Z |  | Ogden-Hinckley Airport (KOGD) | K36U (K36U) | 2026-04-09 16:25 UTC | 2026-04-09 16:46 UTC | 21m |
| GRD830 | GRD | Los Alamitos Army Air Field (KSLI) | Hemet-Ryan Airport (KHMT) | 2026-04-09 16:10 UTC | 2026-04-09 16:46 UTC | 35m |
| FGDTJ | FGD | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-09 16:34 UTC | 2026-04-09 16:45 UTC | 11m |
| HB2471 |  | Ambri Airport (LSPM) | Ambri Airport (LSPM) | 2026-04-09 14:34 UTC | 2026-04-09 16:43 UTC | 2h 8m |
| OAL8NJ | OAL | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-09 16:22 UTC | 2026-04-09 16:42 UTC | 19m |
| CGHAN | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-09 16:24 UTC | 2026-04-09 16:39 UTC | 15m |
| N920CF |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-09 16:24 UTC | 2026-04-09 16:37 UTC | 13m |
| N486BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-09 16:19 UTC | 2026-04-09 16:34 UTC | 15m |
| N522PM |  | Centennial Airport (KAPA) | Perry Stokes Airport (KTAD) | 2026-04-09 15:42 UTC | 2026-04-09 16:34 UTC | 52m |
| BRCAT07 | BRC | Roswell Air Center Airport (KROW) | 81NM (81NM) | 2026-04-09 15:59 UTC | 2026-04-09 16:33 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
