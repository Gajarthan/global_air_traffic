# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_15:11:02_UTC-green)

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

**Latest saved flight:** 2026-04-08 15:11:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 15:11:02 UTC

- **23,528** saved flights
- **11,433** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,528** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **291,707.7 tonnes** estimated CO2 emissions
- **16,910,590 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 976 |
| 2 | Ryanair | 974 |
| 3 | IndiGo | 661 |
| 4 | American Airlines | 427 |
| 5 | EJA | 422 |
| 6 | Southwest Airlines | 331 |
| 7 | Lufthansa | 307 |
| 8 | ENY | 304 |
| 9 | Vueling | 246 |
| 10 | AXM | 243 |
| 11 | LATAM Airlines | 232 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 201 |
| 15 | LXJ | 193 |
| 16 | AZU | 184 |
| 17 | Swiss International | 173 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 158 |
| 22 | EJU | 154 |
| 23 | WIF | 149 |
| 24 | AEE | 148 |
| 25 | United Airlines | 147 |
| 26 | Avianca | 141 |
| 27 | AXB | 136 |
| 28 | EDV | 136 |
| 29 | Air France | 125 |
| 30 | Wizz Air | 121 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18238 |
| 2 | 🇮🇳 IN | 2015 |
| 3 | 🇪🇸 ES | 1814 |
| 4 | 🇦🇺 AU | 1748 |
| 5 | 🇯🇵 JP | 1349 |
| 6 | 🇧🇷 BR | 1304 |
| 7 | 🇩🇪 DE | 1217 |
| 8 | 🇮🇹 IT | 1207 |
| 9 | 🇨🇴 CO | 1203 |
| 10 | 🇨🇦 CA | 1051 |
| 11 | 🇬🇧 GB | 965 |
| 12 | 🇫🇷 FR | 878 |
| 13 | 🇲🇽 MX | 751 |
| 14 | 🇬🇷 GR | 680 |
| 15 | 🇨🇭 CH | 662 |
| 16 | 🇲🇾 MY | 576 |
| 17 | 🇿🇦 ZA | 516 |
| 18 | 🇳🇴 NO | 508 |
| 19 | 🇳🇿 NZ | 499 |
| 20 | 🇬🇹 GT | 474 |
| 21 | 🇹🇷 TR | 455 |
| 22 | 🇵🇭 PH | 447 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 389 |
| 25 | 🇵🇱 PL | 349 |
| 26 | 🇲🇦 MA | 289 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇧🇸 BS | 246 |
| 29 | 🇲🇪 ME | 243 |
| 30 | 🇳🇱 NL | 238 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 555 |
| 2 | El Dorado International Airport |  | CO | 448 |
| 3 | Tokyo International Airport |  | JP | 448 |
| 4 | Indira Gandhi International Airport |  | IN | 414 |
| 5 | Denver International Airport |  | US | 410 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 330 |
| 7 | La Aurora Airport |  | GT | 327 |
| 8 | Harry Reid International Airport |  | US | 311 |
| 9 | Zurich Airport |  | CH | 286 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Guaymaral Airport |  | CO | 246 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 243 |
| 13 | Chicago O'Hare International Airport |  | US | 243 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 16 | Macau International Airport |  | MO | 226 |
| 17 | Bengaluru International Airport |  | IN | 226 |
| 18 | Charlotte/Douglas International Airport |  | US | 221 |
| 19 | Kuala Lumpur International Airport |  | MY | 210 |
| 20 | Madrid Barajas International Airport |  | ES | 209 |
| 21 | Tenerife Norte Airport |  | ES | 207 |
| 22 | Ninoy Aquino International Airport |  | PH | 206 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 195 |
| 24 | Malpensa International Airport |  | IT | 192 |
| 25 | Congonhas Airport |  | BR | 188 |
| 26 | Salt Lake City International Airport |  | US | 183 |
| 27 | Daniel K Inouye International Airport |  | US | 178 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Charles de Gaulle International Airport |  | FR | 173 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 163 |
| 32 | O. R. Tambo International Airport |  | ZA | 161 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 157 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 156 |
| 35 | Miami International Airport |  | US | 156 |
| 36 | Pune Airport |  | IN | 154 |
| 37 | Vitoria/Foronda Airport |  | ES | 153 |
| 38 | Barcelona International Airport |  | ES | 151 |
| 39 | Seattle-Tacoma International Airport |  | US | 150 |
| 40 | Gimpo International Airport |  | KR | 141 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 97 | 14m | 114 km | 190.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 91 | 26m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 64 | 1h 42m | 1,156 km | 1,276.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 40 | 1h 43m | 1,423 km | 981.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 35 | 12m | 15 km | 9.2 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3558E |  | Mefford Field (KTLR) | Meadows Field (KBFL) | 2026-04-08 14:47 UTC | 2026-04-08 15:11 UTC | 23m |
| N33ZG |  | Animas Air Park (K00C) | North Las Vegas Airport (KVGT) | 2026-04-08 11:12 UTC | 2026-04-08 15:01 UTC | 3h 49m |
| FHGTM | FHG | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-04-08 14:37 UTC | 2026-04-08 15:01 UTC | 23m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-04-08 14:33 UTC | 2026-04-08 14:53 UTC | 19m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-08 14:05 UTC | 2026-04-08 14:50 UTC | 44m |
| N6196P |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-08 14:15 UTC | 2026-04-08 14:48 UTC | 32m |
| CH021141 |  | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | 2026-04-08 14:39 UTC | 2026-04-08 14:47 UTC | 8m |
| BRCAT03 | BRC | Roswell Air Center Airport (KROW) | Roswell Air Center Airport (KROW) | 2026-04-08 14:21 UTC | 2026-04-08 14:46 UTC | 24m |
| AIB74TN | AIB | Toulouse-Blagnac Airport (LFBO) | Toulouse-Blagnac Airport (LFBO) | 2026-04-08 14:22 UTC | 2026-04-08 14:44 UTC | 22m |
| RN260Z |  | Brewton Municipal Airport (K12J) | Brewton Municipal Airport (K12J) | 2026-04-08 14:13 UTC | 2026-04-08 14:44 UTC | 30m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-08 13:53 UTC | 2026-04-08 14:40 UTC | 47m |
| GCMLY | GCM | Henstridge Airfield (EGHS) | Henstridge Airfield (EGHS) | 2026-04-08 14:30 UTC | 2026-04-08 14:39 UTC | 9m |
| JUMP9 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-04-08 14:27 UTC | 2026-04-08 14:39 UTC | 11m |
| N11DT |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-08 14:11 UTC | 2026-04-08 14:33 UTC | 21m |
| N86BJ |  | Denton Enterprise Airport (KDTO) | Tightwaad Air Ranch Airport (XA16) | 2026-04-08 14:08 UTC | 2026-04-08 14:33 UTC | 25m |
| N407LG |  | Fort Worth Meacham International Airport (KFTW) | 2TS0 (2TS0) | 2026-04-08 13:27 UTC | 2026-04-08 14:32 UTC | 1h 4m |
| SH124 |  | Whiting Field Nas North Airport (KNSE) | Brewton Municipal Airport (K12J) | 2026-04-08 13:47 UTC | 2026-04-08 14:30 UTC | 43m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-04-08 14:07 UTC | 2026-04-08 14:29 UTC | 22m |
| RYR89YN | Ryanair | Stockholm-Arlanda Airport (ESSA) | Jastarnia Airport (EPJA) | 2026-04-08 13:38 UTC | 2026-04-08 14:28 UTC | 50m |
| N62KW |  | Muscatine Municipal Airport (KMUT) | Crawford County Airport (KRSV) | 2026-04-08 13:55 UTC | 2026-04-08 14:27 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
