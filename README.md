# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_13:46:41_UTC-green)

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

**Latest saved flight:** 2026-04-22 13:46:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 13:46:41 UTC

- **47,933** saved flights
- **19,505** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,933** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **576,100.3 tonnes** estimated CO2 emissions
- **33,397,117 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2037 |
| 2 | SkyWest Airlines | 1846 |
| 3 | IndiGo | 1131 |
| 4 | EJA | 820 |
| 5 | American Airlines | 790 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 621 |
| 8 | Lufthansa | 531 |
| 9 | AXM | 481 |
| 10 | Vueling | 479 |
| 11 | LATAM Airlines | 470 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 409 |
| 14 | Delta Air Lines | 396 |
| 15 | WIF | 389 |
| 16 | QLK | 386 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 365 |
| 19 | AEE | 325 |
| 20 | Alaska Airlines | 323 |
| 21 | EJU | 318 |
| 22 | easyJet | 307 |
| 23 | VIV | 304 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 269 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 256 |
| 28 | JetBlue | 252 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 244 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37993 |
| 2 | 🇮🇳 IN | 3527 |
| 3 | 🇪🇸 ES | 3479 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2803 |
| 6 | 🇯🇵 JP | 2644 |
| 7 | 🇮🇹 IT | 2607 |
| 8 | 🇩🇪 DE | 2516 |
| 9 | 🇨🇦 CA | 2345 |
| 10 | 🇨🇴 CO | 2216 |
| 11 | 🇬🇧 GB | 1972 |
| 12 | 🇫🇷 FR | 1829 |
| 13 | 🇲🇽 MX | 1479 |
| 14 | 🇬🇷 GR | 1466 |
| 15 | 🇨🇭 CH | 1313 |
| 16 | 🇳🇴 NO | 1245 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 994 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 871 |
| 21 | 🇹🇷 TR | 842 |
| 22 | 🇵🇭 PH | 841 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 760 |
| 25 | 🇬🇹 GT | 745 |
| 26 | 🇲🇦 MA | 589 |
| 27 | 🇲🇪 ME | 513 |
| 28 | 🇳🇱 NL | 488 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 425 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1123 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 795 |
| 4 | El Dorado International Airport |  | CO | 771 |
| 5 | Indira Gandhi International Airport |  | IN | 749 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 728 |
| 7 | Harry Reid International Airport |  | US | 621 |
| 8 | Guaymaral Airport |  | CO | 620 |
| 9 | Zurich Airport |  | CH | 565 |
| 10 | La Aurora Airport |  | GT | 552 |
| 11 | Frankfurt am Main International Airport |  | DE | 502 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Kuala Lumpur International Airport |  | MY | 472 |
| 14 | Chicago O'Hare International Airport |  | US | 468 |
| 15 | Macau International Airport |  | MO | 454 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 427 |
| 19 | Bengaluru International Airport |  | IN | 426 |
| 20 | Charlotte/Douglas International Airport |  | US | 409 |
| 21 | Malpensa International Airport |  | IT | 402 |
| 22 | Tenerife Norte Airport |  | ES | 401 |
| 23 | Congonhas Airport |  | BR | 401 |
| 24 | Ninoy Aquino International Airport |  | PH | 389 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 362 |
| 26 | Salt Lake City International Airport |  | US | 359 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 354 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 351 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 330 |
| 32 | Reno/Tahoe International Airport |  | US | 329 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 324 |
| 34 | Vitoria/Foronda Airport |  | ES | 323 |
| 35 | O. R. Tambo International Airport |  | ZA | 319 |
| 36 | Barcelona International Airport |  | ES | 316 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 314 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 284 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 248 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 183 | 14m | 114 km | 358.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 114 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 110 | 26m | 275 km | 521.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 81 | 20m | 250 km | 349.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 78 | 20m | 147 km | 197.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 76 | 26m | 215 km | 281.5 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 67 | 1h 0m | 695 km | 803.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3363E |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-04-22 13:30 UTC | 2026-04-22 13:46 UTC | 16m |
| AXB1056 | AXB | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-22 13:21 UTC | 2026-04-22 13:46 UTC | 25m |
| N531NA |  | Massey Ranch Airpark (KX50) | Arthur Dunn Air Park (KX21) | 2026-04-22 13:16 UTC | 2026-04-22 13:34 UTC | 18m |
| ERU957 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-04-22 13:11 UTC | 2026-04-22 13:32 UTC | 21m |
| CGNQZ | CGN | Thunder Bay Airport (CYQT) | Kakabeka Falls Airport (CKG8) | 2026-04-22 13:15 UTC | 2026-04-22 13:30 UTC | 15m |
| IGO6041 | IndiGo | Ambala Air Force Station (VIAM) | Pantnagar Airport (VIPT) | 2026-04-22 13:05 UTC | 2026-04-22 13:28 UTC | 23m |
| IGO2145 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Shimla Airport (VISM) | 2026-04-22 11:51 UTC | 2026-04-22 13:28 UTC | 1h 36m |
| AXB1527 | AXB | Indira Gandhi International Airport (VIDP) | Bharkot Airport (VI82) | 2026-04-22 13:05 UTC | 2026-04-22 13:28 UTC | 22m |
| N734BH |  | North Perry Airport (KHWO) | North Perry Airport (KHWO) | 2026-04-22 12:35 UTC | 2026-04-22 13:26 UTC | 51m |
| N510BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-04-22 12:22 UTC | 2026-04-22 13:26 UTC | 1h 4m |
| N120FM |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-22 13:14 UTC | 2026-04-22 13:24 UTC | 10m |
| N64LV |  | Mount Moriah Field (02AR) | Yazoo County Airport (K87I) | 2026-04-22 12:56 UTC | 2026-04-22 13:21 UTC | 25m |
| CXK104 | CXK | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-04-22 12:11 UTC | 2026-04-22 13:18 UTC | 1h 7m |
| N86HZ |  | Delaware Airpark (K33N) | DE04 (DE04) | 2026-04-22 13:10 UTC | 2026-04-22 13:17 UTC | 7m |
| N8398L |  | Dupage Airport (KDPA) | Lake In The Hills Airport (K3CK) | 2026-04-22 13:02 UTC | 2026-04-22 13:17 UTC | 14m |
| N5623E |  | Schaumburg Regional Airport (K06C) | IS80 (IS80) | 2026-04-22 12:50 UTC | 2026-04-22 13:16 UTC | 26m |
| SMGLR49 | SMG | Letkov Airport (LKPL) | Kbely Air Base (LKKB) | 2026-04-22 12:25 UTC | 2026-04-22 13:15 UTC | 50m |
| WIF850 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-22 12:58 UTC | 2026-04-22 13:15 UTC | 16m |
| N7866N |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-04-22 12:50 UTC | 2026-04-22 13:14 UTC | 24m |
| EJA958 | EJA | Miami International Airport (KMIA) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-22 11:24 UTC | 2026-04-22 13:14 UTC | 1h 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
