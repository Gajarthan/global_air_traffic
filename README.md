# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_17:35:14_UTC-green)

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

**Latest saved flight:** 2026-04-22 17:35:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 17:35:14 UTC

- **48,411** saved flights
- **19,664** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **48,411** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **580,678.4 tonnes** estimated CO2 emissions
- **33,662,519 km** total distance flown
- **836 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2057 |
| 2 | SkyWest Airlines | 1863 |
| 3 | IndiGo | 1138 |
| 4 | EJA | 834 |
| 5 | American Airlines | 798 |
| 6 | Southwest Airlines | 686 |
| 7 | ENY | 627 |
| 8 | Lufthansa | 545 |
| 9 | Vueling | 484 |
| 10 | AXM | 481 |
| 11 | LATAM Airlines | 473 |
| 12 | All Nippon Airways | 437 |
| 13 | AZU | 413 |
| 14 | Delta Air Lines | 399 |
| 15 | WIF | 398 |
| 16 | QLK | 386 |
| 17 | LXJ | 372 |
| 18 | Swiss International | 369 |
| 19 | AEE | 331 |
| 20 | Alaska Airlines | 324 |
| 21 | EJU | 318 |
| 22 | easyJet | 309 |
| 23 | VIV | 307 |
| 24 | Japan Airlines | 290 |
| 25 | Air France | 275 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 258 |
| 28 | JetBlue | 255 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 244 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 38413 |
| 2 | 🇮🇳 IN | 3551 |
| 3 | 🇪🇸 ES | 3516 |
| 4 | 🇦🇺 AU | 3315 |
| 5 | 🇧🇷 BR | 2825 |
| 6 | 🇯🇵 JP | 2646 |
| 7 | 🇮🇹 IT | 2622 |
| 8 | 🇩🇪 DE | 2548 |
| 9 | 🇨🇦 CA | 2391 |
| 10 | 🇨🇴 CO | 2254 |
| 11 | 🇬🇧 GB | 2003 |
| 12 | 🇫🇷 FR | 1851 |
| 13 | 🇲🇽 MX | 1495 |
| 14 | 🇬🇷 GR | 1488 |
| 15 | 🇨🇭 CH | 1324 |
| 16 | 🇳🇴 NO | 1274 |
| 17 | 🇲🇾 MY | 1176 |
| 18 | 🇿🇦 ZA | 1000 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 872 |
| 21 | 🇹🇷 TR | 855 |
| 22 | 🇵🇭 PH | 843 |
| 23 | 🇰🇷 KR | 792 |
| 24 | 🇵🇱 PL | 770 |
| 25 | 🇬🇹 GT | 753 |
| 26 | 🇲🇦 MA | 594 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 496 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 434 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1131 |
| 2 | Tokyo International Airport |  | JP | 899 |
| 3 | Denver International Airport |  | US | 805 |
| 4 | El Dorado International Airport |  | CO | 775 |
| 5 | Indira Gandhi International Airport |  | IN | 752 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 736 |
| 7 | Guaymaral Airport |  | CO | 649 |
| 8 | Harry Reid International Airport |  | US | 629 |
| 9 | Zurich Airport |  | CH | 573 |
| 10 | La Aurora Airport |  | GT | 560 |
| 11 | Frankfurt am Main International Airport |  | DE | 519 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 480 |
| 13 | Chicago O'Hare International Airport |  | US | 474 |
| 14 | Kuala Lumpur International Airport |  | MY | 472 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 457 |
| 16 | Macau International Airport |  | MO | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Madrid Barajas International Airport |  | ES | 436 |
| 19 | Bengaluru International Airport |  | IN | 430 |
| 20 | Charlotte/Douglas International Airport |  | US | 413 |
| 21 | Congonhas Airport |  | BR | 407 |
| 22 | Malpensa International Airport |  | IT | 403 |
| 23 | Tenerife Norte Airport |  | ES | 403 |
| 24 | Ninoy Aquino International Airport |  | PH | 390 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 369 |
| 26 | Salt Lake City International Airport |  | US | 363 |
| 27 | Charles de Gaulle International Airport |  | FR | 360 |
| 28 | Daniel K Inouye International Airport |  | US | 357 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 354 |
| 30 | Capua Airport |  | IT | 352 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 331 |
| 32 | Reno/Tahoe International Airport |  | US | 329 |
| 33 | Vitoria/Foronda Airport |  | ES | 329 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 328 |
| 35 | O. R. Tambo International Airport |  | ZA | 322 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 320 |
| 37 | Barcelona International Airport |  | ES | 320 |
| 38 | Don Mueang International Airport |  | TH | 295 |
| 39 | Calgary International Airport |  | CA | 288 |
| 40 | Viracopos International Airport |  | BR | 286 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 261 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 228 | 1h 7m | 706 km | 2,775.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 184 | 14m | 114 km | 360.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 143 | 28m | 304 km | 749.6 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 141 | 21m | 244 km | 593.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 139 | 1h 27m | 910 km | 2,181.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 128 | 19m | 165 km | 364.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 117 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 113 | 26m | 275 km | 535.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 99 | 44m | 452 km | 771.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 83 | 31m | 369 km | 528.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 69 | 1h 42m | 1,156 km | 1,376.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 68 | 1h 0m | 695 km | 815.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ABK300 | ABK | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-04-22 17:13 UTC | 2026-04-22 17:35 UTC | 22m |
| ARSON02 | ARS | Dave Eby Field (4XA5) | 2OK5 (2OK5) | 2026-04-22 17:16 UTC | 2026-04-22 17:26 UTC | 10m |
| N99FF |  | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-04-22 16:59 UTC | 2026-04-22 17:23 UTC | 23m |
| HYDRA31 | HYD | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-04-22 16:59 UTC | 2026-04-22 17:21 UTC | 21m |
| RNGR870 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-04-22 16:49 UTC | 2026-04-22 17:18 UTC | 28m |
| N116HR |  | Ohio State University Airport (KOSU) | Madison County Airport (KUYF) | 2026-04-22 16:48 UTC | 2026-04-22 17:17 UTC | 28m |
| N399GB |  | Grand Junction Regional Airport (KGJT) | Grand Junction Regional Airport (KGJT) | 2026-04-22 17:06 UTC | 2026-04-22 17:12 UTC | 6m |
| N13262 |  | Deland Municipal-Sidney H Taylor Field (KDED) | North Exuma Airport (85FA) | 2026-04-22 16:45 UTC | 2026-04-22 17:12 UTC | 27m |
| BOE157 | BOE | Boeing Field/King County International Airport (KBFI) | Ephrata Municipal Airport (KEPH) | 2026-04-22 16:49 UTC | 2026-04-22 17:10 UTC | 20m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-22 16:53 UTC | 2026-04-22 17:06 UTC | 13m |
| RAIDR36 | RAI | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 8CL0 (8CL0) | 2026-04-22 16:32 UTC | 2026-04-22 17:03 UTC | 31m |
| NIT288 | NIT | Macon Downtown Airport (KMAC) | Macon Downtown Airport (KMAC) | 2026-04-22 16:41 UTC | 2026-04-22 17:03 UTC | 21m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-22 16:51 UTC | 2026-04-22 17:01 UTC | 10m |
| N612W |  | Addison Airport (KADS) | Square Air Airport (TS63) | 2026-04-22 16:44 UTC | 2026-04-22 17:01 UTC | 16m |
| N37242 |  | Kalkaska City Airport (KY89) | Ernie's Field (1MI4) | 2026-04-22 14:17 UTC | 2026-04-22 16:58 UTC | 2h 40m |
| ERU316 | ERU | Ormond Beach Municipal Airport (KOMN) | KXFL (KXFL) | 2026-04-22 16:53 UTC | 2026-04-22 16:58 UTC | 4m |
| N734SE |  | Murfreesboro Municipal Airport (KMBT) | Murfreesboro Municipal Airport (KMBT) | 2026-04-22 16:46 UTC | 2026-04-22 16:57 UTC | 10m |
| N700GW |  | Centennial Airport (KAPA) | Williams Ranch Airport (1CO2) | 2026-04-22 15:20 UTC | 2026-04-22 16:56 UTC | 1h 35m |
| N716BB |  | Teterboro Airport (KTEB) | Odell Williamson Municipal Airport (K60J) | 2026-04-22 15:50 UTC | 2026-04-22 16:55 UTC | 1h 5m |
| N331US |  | Victoria International Airport (CYYJ) | Boeing Field/King County International Airport (KBFI) | 2026-04-22 16:30 UTC | 2026-04-22 16:51 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
