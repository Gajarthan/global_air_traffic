# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_17:35:16_UTC-green)

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

**Latest saved flight:** 2026-04-19 17:35:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 17:35:16 UTC

- **43,538** saved flights
- **18,170** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,538** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **523,786.4 tonnes** estimated CO2 emissions
- **30,364,429 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1837 |
| 2 | SkyWest Airlines | 1677 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 743 |
| 5 | American Airlines | 714 |
| 6 | Southwest Airlines | 608 |
| 7 | ENY | 563 |
| 8 | AXM | 446 |
| 9 | Lufthansa | 438 |
| 10 | Vueling | 437 |
| 11 | LATAM Airlines | 434 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 383 |
| 14 | Delta Air Lines | 368 |
| 15 | QLK | 354 |
| 16 | LXJ | 341 |
| 17 | WIF | 339 |
| 18 | Swiss International | 337 |
| 19 | AEE | 299 |
| 20 | Alaska Airlines | 291 |
| 21 | EJU | 287 |
| 22 | easyJet | 278 |
| 23 | VIV | 274 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | AXB | 232 |
| 27 | United Airlines | 230 |
| 28 | JetBlue | 229 |
| 29 | GLO | 228 |
| 30 | AIQ | 222 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 34221 |
| 2 | 🇮🇳 IN | 3299 |
| 3 | 🇪🇸 ES | 3228 |
| 4 | 🇦🇺 AU | 3033 |
| 5 | 🇧🇷 BR | 2598 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2300 |
| 8 | 🇩🇪 DE | 2224 |
| 9 | 🇨🇦 CA | 2109 |
| 10 | 🇨🇴 CO | 2013 |
| 11 | 🇬🇧 GB | 1772 |
| 12 | 🇫🇷 FR | 1674 |
| 13 | 🇬🇷 GR | 1351 |
| 14 | 🇲🇽 MX | 1349 |
| 15 | 🇨🇭 CH | 1201 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1084 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 772 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 713 |
| 25 | 🇵🇱 PL | 696 |
| 26 | 🇲🇦 MA | 544 |
| 27 | 🇲🇪 ME | 458 |
| 28 | 🇳🇱 NL | 447 |
| 29 | 🇧🇸 BS | 402 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1007 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 716 |
| 4 | Indira Gandhi International Airport |  | IN | 710 |
| 5 | El Dorado International Airport |  | CO | 704 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 672 |
| 7 | Harry Reid International Airport |  | US | 551 |
| 8 | Guaymaral Airport |  | CO | 547 |
| 9 | La Aurora Airport |  | GT | 526 |
| 10 | Zurich Airport |  | CH | 525 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 427 |
| 13 | Chicago O'Hare International Airport |  | US | 423 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 419 |
| 15 | Frankfurt am Main International Airport |  | DE | 411 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Bengaluru International Airport |  | IN | 392 |
| 19 | Madrid Barajas International Airport |  | ES | 390 |
| 20 | Tenerife Norte Airport |  | ES | 386 |
| 21 | Charlotte/Douglas International Airport |  | US | 376 |
| 22 | Congonhas Airport |  | BR | 374 |
| 23 | Ninoy Aquino International Airport |  | PH | 366 |
| 24 | Malpensa International Airport |  | IT | 361 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 330 |
| 26 | Salt Lake City International Airport |  | US | 329 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 28 | Charles de Gaulle International Airport |  | FR | 324 |
| 29 | Daniel K Inouye International Airport |  | US | 321 |
| 30 | Vitoria/Foronda Airport |  | ES | 305 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 302 |
| 32 | Reno/Tahoe International Airport |  | US | 300 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 296 |
| 34 | Capua Airport |  | IT | 296 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 295 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 282 |
| 38 | Viracopos International Airport |  | BR | 266 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 258 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 220 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 164 | 14m | 114 km | 321.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 119 | 21m | 244 km | 501.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 107 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 101 | 26m | 275 km | 478.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 70 | 52m | 556 km | 671.0 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 64 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 60 | 1h 21m | 961 km | 994.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N312WG |  | Chicago Executive Airport (KPWK) | Chicago Executive Airport (KPWK) | 2026-04-19 17:10 UTC | 2026-04-19 17:35 UTC | 25m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-04-19 17:14 UTC | 2026-04-19 17:32 UTC | 18m |
| BRG661 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-19 17:00 UTC | 2026-04-19 17:30 UTC | 29m |
| N42LG |  | Haller Airpark (7FL4) | Bartow Executive Airport (KBOW) | 2026-04-19 16:21 UTC | 2026-04-19 17:20 UTC | 59m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-19 16:59 UTC | 2026-04-19 17:14 UTC | 15m |
| LVS074 | LVS | Mariano Moreno Airport (SADJ) | Mariano Moreno Airport (SADJ) | 2026-04-19 17:05 UTC | 2026-04-19 17:10 UTC | 4m |
| N423FP |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-04-19 16:33 UTC | 2026-04-19 17:08 UTC | 35m |
| GPD952 | GPD | Luis Munoz Marin International Airport (TJSJ) | Cyril E King Airport (TIST) | 2026-04-19 16:55 UTC | 2026-04-19 17:08 UTC | 13m |
| N289ST |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-19 16:34 UTC | 2026-04-19 17:07 UTC | 33m |
| TWY83 | TWY | Santa Barbara Municipal Airport (KSBA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-19 16:30 UTC | 2026-04-19 17:06 UTC | 36m |
| SH247 |  | Macdill Afb Airport (KMCF) | Redtail Airstrip (FA30) | 2026-04-19 16:37 UTC | 2026-04-19 17:05 UTC | 28m |
| N992AK |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-04-19 16:40 UTC | 2026-04-19 17:04 UTC | 23m |
| N987BC |  | Bowie Municipal Airport (K0F2) | 69XA (69XA) | 2026-04-19 16:52 UTC | 2026-04-19 17:04 UTC | 12m |
| LYM5872 | LYM | Hartsfield/Jackson Atlanta International Airport (KATL) | Robert Sibley Airport (KSZY) | 2026-04-19 16:23 UTC | 2026-04-19 17:02 UTC | 39m |
| SAS687 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Malpensa International Airport (LIMC) | 2026-04-19 15:18 UTC | 2026-04-19 17:02 UTC | 1h 43m |
| RA01519 |  | Minsk International Airport (UMMS) | Smolensk North Airport (XUBS) | 2026-04-19 16:46 UTC | 2026-04-19 17:02 UTC | 15m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-19 16:49 UTC | 2026-04-19 17:01 UTC | 12m |
| N912GW |  | Naples Municipal Airport (KAPF) | 68LA (68LA) | 2026-04-19 14:34 UTC | 2026-04-19 17:00 UTC | 2h 26m |
| FFL613 | FFL | Eppley Airfield (KOMA) | 56NE (56NE) | 2026-04-19 15:59 UTC | 2026-04-19 16:58 UTC | 58m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-19 16:45 UTC | 2026-04-19 16:56 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
