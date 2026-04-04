# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_12:46:10_UTC-green)

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

**Latest saved flight:** 2026-04-04 12:46:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 12:46:10 UTC

- **15,563** saved flights
- **8,358** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **15,563** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **193,329.5 tonnes** estimated CO2 emissions
- **11,207,508 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 615 |
| 3 | IndiGo | 455 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 226 |
| 7 | Lufthansa | 222 |
| 8 | ENY | 196 |
| 9 | Vueling | 167 |
| 10 | LATAM Airlines | 165 |
| 11 | AXM | 157 |
| 12 | All Nippon Airways | 141 |
| 13 | QLK | 137 |
| 14 | LXJ | 134 |
| 15 | Delta Air Lines | 125 |
| 16 | Swiss International | 121 |
| 17 | AZU | 117 |
| 18 | VIV | 111 |
| 19 | Japan Airlines | 107 |
| 20 | Alaska Airlines | 104 |
| 21 | EJU | 99 |
| 22 | WIF | 99 |
| 23 | United Airlines | 98 |
| 24 | AXB | 97 |
| 25 | AEE | 96 |
| 26 | Avianca | 96 |
| 27 | easyJet | 95 |
| 28 | EDV | 93 |
| 29 | Cathay Pacific | 88 |
| 30 | BRC | 87 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12282 |
| 2 | 🇮🇳 IN | 1386 |
| 3 | 🇪🇸 ES | 1227 |
| 4 | 🇦🇺 AU | 1205 |
| 5 | 🇧🇷 BR | 889 |
| 6 | 🇯🇵 JP | 858 |
| 7 | 🇩🇪 DE | 816 |
| 8 | 🇨🇴 CO | 756 |
| 9 | 🇨🇦 CA | 696 |
| 10 | 🇮🇹 IT | 693 |
| 11 | 🇬🇧 GB | 606 |
| 12 | 🇫🇷 FR | 557 |
| 13 | 🇲🇽 MX | 523 |
| 14 | 🇬🇷 GR | 433 |
| 15 | 🇨🇭 CH | 417 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 363 |
| 18 | 🇿🇦 ZA | 336 |
| 19 | 🇳🇴 NO | 325 |
| 20 | 🇵🇭 PH | 301 |
| 21 | 🇹🇷 TR | 290 |
| 22 | 🇰🇷 KR | 289 |
| 23 | 🇬🇹 GT | 268 |
| 24 | 🇵🇱 PL | 221 |
| 25 | 🇹🇭 TH | 220 |
| 26 | 🇲🇦 MA | 186 |
| 27 | 🇮🇩 ID | 173 |
| 28 | 🇲🇪 ME | 164 |
| 29 | 🇲🇴 MO | 162 |
| 30 | 🇧🇸 BS | 159 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 375 |
| 2 | Tokyo International Airport |  | JP | 298 |
| 3 | Indira Gandhi International Airport |  | IN | 287 |
| 4 | El Dorado International Airport |  | CO | 286 |
| 5 | Denver International Airport |  | US | 280 |
| 6 | Harry Reid International Airport |  | US | 214 |
| 7 | Frankfurt am Main International Airport |  | DE | 206 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 204 |
| 9 | Zurich Airport |  | CH | 191 |
| 10 | La Aurora Airport |  | GT | 188 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 162 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 153 |
| 16 | Bengaluru International Airport |  | IN | 153 |
| 17 | Chicago O'Hare International Airport |  | US | 147 |
| 18 | Charlotte/Douglas International Airport |  | US | 142 |
| 19 | Congonhas Airport |  | BR | 139 |
| 20 | Ninoy Aquino International Airport |  | PH | 138 |
| 21 | Madrid Barajas International Airport |  | ES | 138 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 23 | Netaji Subhash Chandra Bose International Airport |  | IN | 131 |
| 24 | Kuala Lumpur International Airport |  | MY | 128 |
| 25 | Tenerife Norte Airport |  | ES | 126 |
| 26 | Reno/Tahoe International Airport |  | US | 122 |
| 27 | Daniel K Inouye International Airport |  | US | 121 |
| 28 | Salt Lake City International Airport |  | US | 121 |
| 29 | Malpensa International Airport |  | IT | 120 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 119 |
| 31 | Charles de Gaulle International Airport |  | FR | 116 |
| 32 | Vitoria/Foronda Airport |  | ES | 113 |
| 33 | Barcelona International Airport |  | ES | 106 |
| 34 | Pune Airport |  | IN | 104 |
| 35 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 36 | Austin-Bergstrom International Airport |  | US | 103 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 103 |
| 38 | Gimpo International Airport |  | KR | 101 |
| 39 | Seattle-Tacoma International Airport |  | US | 98 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 48 | 31m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 46 | 1h 26m | 910 km | 721.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 45 | 1h 46m | 1,156 km | 897.7 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 38 | 16m | 206 km | 135.1 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 12 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 36 | 27m | 152 km | 94.1 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 35 | 28m | 275 km | 165.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 17 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 34 | 53m | 556 km | 325.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 29 | 1h 42m | 1,423 km | 711.7 t |
| 21 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 28 | 23m | 252 km | 121.6 t |
| 22 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 27 | 11m | 127 km | 59.1 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 26 | 20m | 147 km | 65.8 t |
| 26 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 24 | 13m | 99 km | 41.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 23 | 53m | 493 km | 195.7 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 30 | Melbourne International Airport (YMML) | Long Hill Airport (YLHL) | 22 | 34m | 431 km | 163.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N926TP |  | SC40 (SC40) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-04-04 12:08 UTC | 2026-04-04 12:46 UTC | 37m |
| HBXBO | HBX | Muenster Aero Airport (LSPU) | Reichenbach Air Base (LSGR) | 2026-04-04 11:54 UTC | 2026-04-04 12:42 UTC | 48m |
| AUA21C | Austrian Airlines | Vienna International Airport (LOWW) | Frankfurt am Main International Airport (EDDF) | 2026-04-04 11:31 UTC | 2026-04-04 12:40 UTC | 1h 8m |
| N9886K |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-04 12:31 UTC | 2026-04-04 12:38 UTC | 6m |
| CXK141 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-04 12:13 UTC | 2026-04-04 12:37 UTC | 24m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-04-04 12:09 UTC | 2026-04-04 12:34 UTC | 24m |
| TGVOY | TGV | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-04 11:52 UTC | 2026-04-04 12:31 UTC | 39m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Courchevel Airport (LFLJ) | 2026-04-04 11:45 UTC | 2026-04-04 12:30 UTC | 45m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-04-04 12:02 UTC | 2026-04-04 12:29 UTC | 26m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Raron Airport (LSTA) | 2026-04-04 11:35 UTC | 2026-04-04 12:28 UTC | 52m |
| IFJ39S | IFJ | Cascais Airport (LPCS) | Cascais Airport (LPCS) | 2026-04-04 12:00 UTC | 2026-04-04 12:26 UTC | 26m |
| DLH3LC | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-04 11:46 UTC | 2026-04-04 12:24 UTC | 37m |
| FHSKJ | FHS | Grenoble-Isere Airport (LFLS) | Meribel Airport (LFKX) | 2026-04-04 12:05 UTC | 2026-04-04 12:21 UTC | 15m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-04 12:10 UTC | 2026-04-04 12:20 UTC | 10m |
| WWI82 | WWI | Daniel K Inouye International Airport (PHNL) | Van Nuys Airport (KVNY) | 2026-04-04 07:42 UTC | 2026-04-04 12:18 UTC | 4h 35m |
| DFIRE | DFI | Innsbruck Airport (LOWI) | Frankfurt-Egelsbach Airport (EDFE) | 2026-04-04 11:13 UTC | 2026-04-04 12:15 UTC | 1h 1m |
| AWA477 | AWA | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-04-04 11:33 UTC | 2026-04-04 12:11 UTC | 38m |
| BBC395 | BBC | VGZR (VGZR) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-04 11:26 UTC | 2026-04-04 12:10 UTC | 43m |
| DLH9YY | Lufthansa | Frankfurt am Main International Airport (EDDF) | Celle-Arloh Airport (EDVC) | 2026-04-04 11:12 UTC | 2026-04-04 12:07 UTC | 54m |
| BEL7LF | Brussels Airlines | Brussels Airport (EBBR) | Nordlingen Airport (EDNO) | 2026-04-04 11:03 UTC | 2026-04-04 12:07 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
