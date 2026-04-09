# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_21:15:34_UTC-green)

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

**Latest saved flight:** 2026-04-09 21:15:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-09 21:15:34 UTC

- **25,903** saved flights
- **12,384** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **25,903** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **319,123.0 tonnes** estimated CO2 emissions
- **18,499,882 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1071 |
| 2 | SkyWest Airlines | 1063 |
| 3 | IndiGo | 702 |
| 4 | American Airlines | 463 |
| 5 | EJA | 463 |
| 6 | Southwest Airlines | 372 |
| 7 | Lufthansa | 338 |
| 8 | ENY | 338 |
| 9 | Vueling | 266 |
| 10 | AXM | 260 |
| 11 | LATAM Airlines | 256 |
| 12 | All Nippon Airways | 231 |
| 13 | QLK | 230 |
| 14 | Delta Air Lines | 215 |
| 15 | LXJ | 207 |
| 16 | AZU | 205 |
| 17 | Swiss International | 181 |
| 18 | Alaska Airlines | 177 |
| 19 | VIV | 173 |
| 20 | Japan Airlines | 171 |
| 21 | EJU | 169 |
| 22 | easyJet | 169 |
| 23 | WIF | 165 |
| 24 | AEE | 164 |
| 25 | United Airlines | 156 |
| 26 | EDV | 150 |
| 27 | Avianca | 149 |
| 28 | AXB | 144 |
| 29 | PGT | 135 |
| 30 | BRC | 134 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20402 |
| 2 | 🇮🇳 IN | 2152 |
| 3 | 🇪🇸 ES | 1941 |
| 4 | 🇦🇺 AU | 1882 |
| 5 | 🇧🇷 BR | 1458 |
| 6 | 🇯🇵 JP | 1434 |
| 7 | 🇩🇪 DE | 1341 |
| 8 | 🇮🇹 IT | 1326 |
| 9 | 🇨🇴 CO | 1306 |
| 10 | 🇨🇦 CA | 1207 |
| 11 | 🇬🇧 GB | 1043 |
| 12 | 🇫🇷 FR | 962 |
| 13 | 🇲🇽 MX | 836 |
| 14 | 🇬🇷 GR | 743 |
| 15 | 🇨🇭 CH | 715 |
| 16 | 🇲🇾 MY | 624 |
| 17 | 🇳🇴 NO | 557 |
| 18 | 🇳🇿 NZ | 554 |
| 19 | 🇿🇦 ZA | 532 |
| 20 | 🇹🇷 TR | 492 |
| 21 | 🇬🇹 GT | 488 |
| 22 | 🇵🇭 PH | 478 |
| 23 | 🇰🇷 KR | 447 |
| 24 | 🇹🇭 TH | 433 |
| 25 | 🇵🇱 PL | 385 |
| 26 | 🇲🇦 MA | 320 |
| 27 | 🇧🇸 BS | 270 |
| 28 | 🇲🇪 ME | 259 |
| 29 | 🇮🇩 ID | 258 |
| 30 | 🇳🇱 NL | 256 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 608 |
| 2 | El Dorado International Airport |  | CO | 484 |
| 3 | Tokyo International Airport |  | JP | 480 |
| 4 | Indira Gandhi International Airport |  | IN | 444 |
| 5 | Denver International Airport |  | US | 440 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 361 |
| 7 | La Aurora Airport |  | GT | 338 |
| 8 | Harry Reid International Airport |  | US | 334 |
| 9 | Zurich Airport |  | CH | 305 |
| 10 | Frankfurt am Main International Airport |  | DE | 283 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 269 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 264 |
| 14 | Chicago O'Hare International Airport |  | US | 263 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 256 |
| 16 | Macau International Airport |  | MO | 253 |
| 17 | Charlotte/Douglas International Airport |  | US | 238 |
| 18 | Bengaluru International Airport |  | IN | 235 |
| 19 | Kuala Lumpur International Airport |  | MY | 231 |
| 20 | Tenerife Norte Airport |  | ES | 228 |
| 21 | Ninoy Aquino International Airport |  | PH | 222 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 206 |
| 24 | Malpensa International Airport |  | IT | 205 |
| 25 | Congonhas Airport |  | BR | 204 |
| 26 | Salt Lake City International Airport |  | US | 201 |
| 27 | Daniel K Inouye International Airport |  | US | 197 |
| 28 | Reno/Tahoe International Airport |  | US | 193 |
| 29 | Charles de Gaulle International Airport |  | FR | 185 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 180 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 180 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 170 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 35 | O. R. Tambo International Airport |  | ZA | 168 |
| 36 | Barcelona International Airport |  | ES | 167 |
| 37 | Seattle-Tacoma International Airport |  | US | 165 |
| 38 | Vitoria/Foronda Airport |  | ES | 163 |
| 39 | Capua Airport |  | IT | 161 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 122 | 1h 8m | 706 km | 1,485.4 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 106 | 14m | 114 km | 207.9 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
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
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 50 | 31m | 369 km | 318.3 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 46 | 20m | 250 km | 198.7 t |
| 21 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 24 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 42 | 13m | 99 km | 72.0 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4308P |  | Old Bridge Airport (K3N6) | 8NJ0 (8NJ0) | 2026-04-09 20:42 UTC | 2026-04-09 21:15 UTC | 33m |
| N971MB |  | Curtis Municipal Airport (K47V) | Rocky Mountain Metro Airport (KBJC) | 2026-04-09 20:20 UTC | 2026-04-09 21:14 UTC | 53m |
| JOK | JOK | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-09 20:34 UTC | 2026-04-09 21:13 UTC | 38m |
| N2087E |  | Hemet-Ryan Airport (KHMT) | Riverside Airport (KRAL) | 2026-04-09 20:29 UTC | 2026-04-09 21:12 UTC | 43m |
| N345B |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-04-09 20:48 UTC | 2026-04-09 21:12 UTC | 23m |
| N1679H |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-04-09 20:56 UTC | 2026-04-09 21:11 UTC | 15m |
| N9678W |  | Paulding Northwest Atlanta Airport (KPUJ) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-04-09 20:41 UTC | 2026-04-09 21:11 UTC | 29m |
| N35408 |  | Elmendorf Afb Airport (PAED) | Talkeetna Airport (PATK) | 2026-04-09 20:22 UTC | 2026-04-09 21:11 UTC | 48m |
| N38316 |  | Meriden Markham Municipal Airport (KMMK) | Windham Airport (KIJD) | 2026-04-09 20:23 UTC | 2026-04-09 21:07 UTC | 44m |
| N89433 |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 2026-04-09 20:29 UTC | 2026-04-09 21:07 UTC | 37m |
| N9106Y |  | Porter County Regional Airport (KVPZ) | Purdue University Airport (KLAF) | 2026-04-09 20:17 UTC | 2026-04-09 21:05 UTC | 47m |
| NWX251 | NWX | Aero Valley Airport (K52F) | Eugene's Dream Airport (6XS7) | 2026-04-09 20:33 UTC | 2026-04-09 21:05 UTC | 31m |
| N2SY |  | Tampa International Airport (KTPA) | Mid-Way Regional Airport (KJWY) | 2026-04-09 18:25 UTC | 2026-04-09 21:00 UTC | 2h 34m |
| N9917E |  | Salt Lake City International Airport (KSLC) | K36U (K36U) | 2026-04-09 20:47 UTC | 2026-04-09 20:58 UTC | 11m |
| N194TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-09 20:29 UTC | 2026-04-09 20:57 UTC | 28m |
| N793US |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-04-09 20:09 UTC | 2026-04-09 20:56 UTC | 47m |
| N739TS |  | Mckinney Ntl Airport (KTKI) | Flying T Ranch Airport (41TS) | 2026-04-09 20:25 UTC | 2026-04-09 20:55 UTC | 30m |
| ZKIOJ | ZKI | Dunedin Airport (NZDN) | Dunedin Airport (NZDN) | 2026-04-09 20:31 UTC | 2026-04-09 20:54 UTC | 22m |
| N438H |  | Westover Arb/Metro Airport (KCEF) | Laguardia Airport (KLGA) | 2026-04-09 19:59 UTC | 2026-04-09 20:53 UTC | 53m |
| N510LG |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-04-09 20:35 UTC | 2026-04-09 20:49 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
