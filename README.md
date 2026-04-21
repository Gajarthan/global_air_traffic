# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_14:32:26_UTC-green)

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

**Latest saved flight:** 2026-04-21 14:32:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 14:32:26 UTC

- **46,751** saved flights
- **19,154** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,751** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **562,884.2 tonnes** estimated CO2 emissions
- **32,630,966 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1989 |
| 2 | SkyWest Airlines | 1801 |
| 3 | IndiGo | 1102 |
| 4 | EJA | 801 |
| 5 | American Airlines | 772 |
| 6 | Southwest Airlines | 670 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 499 |
| 9 | Vueling | 474 |
| 10 | AXM | 469 |
| 11 | LATAM Airlines | 463 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 399 |
| 14 | Delta Air Lines | 390 |
| 15 | QLK | 376 |
| 16 | WIF | 371 |
| 17 | LXJ | 362 |
| 18 | Swiss International | 358 |
| 19 | AEE | 318 |
| 20 | Alaska Airlines | 318 |
| 21 | EJU | 313 |
| 22 | VIV | 300 |
| 23 | easyJet | 298 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 250 |
| 27 | JetBlue | 249 |
| 28 | AXB | 246 |
| 29 | United Airlines | 246 |
| 30 | GLO | 237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37030 |
| 2 | 🇮🇳 IN | 3428 |
| 3 | 🇪🇸 ES | 3423 |
| 4 | 🇦🇺 AU | 3231 |
| 5 | 🇧🇷 BR | 2738 |
| 6 | 🇯🇵 JP | 2567 |
| 7 | 🇮🇹 IT | 2543 |
| 8 | 🇩🇪 DE | 2423 |
| 9 | 🇨🇦 CA | 2279 |
| 10 | 🇨🇴 CO | 2170 |
| 11 | 🇬🇧 GB | 1915 |
| 12 | 🇫🇷 FR | 1788 |
| 13 | 🇲🇽 MX | 1451 |
| 14 | 🇬🇷 GR | 1425 |
| 15 | 🇨🇭 CH | 1285 |
| 16 | 🇳🇴 NO | 1186 |
| 17 | 🇲🇾 MY | 1145 |
| 18 | 🇿🇦 ZA | 970 |
| 19 | 🇳🇿 NZ | 911 |
| 20 | 🇹🇭 TH | 846 |
| 21 | 🇵🇭 PH | 831 |
| 22 | 🇹🇷 TR | 825 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 739 |
| 25 | 🇬🇹 GT | 739 |
| 26 | 🇲🇦 MA | 581 |
| 27 | 🇲🇪 ME | 496 |
| 28 | 🇳🇱 NL | 479 |
| 29 | 🇲🇴 MO | 440 |
| 30 | 🇧🇸 BS | 421 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1097 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 776 |
| 4 | El Dorado International Airport |  | CO | 757 |
| 5 | Indira Gandhi International Airport |  | IN | 736 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 707 |
| 7 | Harry Reid International Airport |  | US | 604 |
| 8 | Guaymaral Airport |  | CO | 598 |
| 9 | Zurich Airport |  | CH | 553 |
| 10 | La Aurora Airport |  | GT | 547 |
| 11 | Frankfurt am Main International Airport |  | DE | 471 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 13 | Chicago O'Hare International Airport |  | US | 459 |
| 14 | Kuala Lumpur International Airport |  | MY | 458 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 448 |
| 16 | Macau International Airport |  | MO | 440 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 418 |
| 19 | Bengaluru International Airport |  | IN | 412 |
| 20 | Charlotte/Douglas International Airport |  | US | 401 |
| 21 | Malpensa International Airport |  | IT | 400 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 390 |
| 24 | Ninoy Aquino International Airport |  | PH | 384 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 356 |
| 26 | Charles de Gaulle International Airport |  | FR | 349 |
| 27 | Daniel K Inouye International Airport |  | US | 348 |
| 28 | Salt Lake City International Airport |  | US | 347 |
| 29 | Capua Airport |  | IT | 347 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 344 |
| 31 | Reno/Tahoe International Airport |  | US | 323 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 323 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 319 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | O. R. Tambo International Airport |  | ZA | 312 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 37 | Barcelona International Airport |  | ES | 311 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 280 |
| 40 | Viracopos International Airport |  | BR | 279 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 240 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 177 | 14m | 114 km | 347.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 136 | 21m | 244 km | 572.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 124 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 112 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 75 | 52m | 556 km | 718.9 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 0m | 695 km | 779.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-04-21 13:47 UTC | 2026-04-21 14:32 UTC | 44m |
| PAIN12 | PAI | Flysooner Field (OK50) | Henderson Farm Airport (35OL) | 2026-04-21 14:03 UTC | 2026-04-21 14:31 UTC | 28m |
| HK5178G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-21 14:10 UTC | 2026-04-21 14:31 UTC | 21m |
| CTM1291 | CTM | Joigny Airport (LFGK) | Lyon-Bron Airport (LFLY) | 2026-04-21 13:46 UTC | 2026-04-21 14:28 UTC | 42m |
| N619BL |  | 14MI (14MI) | Cherry Capital Airport (KTVC) | 2026-04-21 12:36 UTC | 2026-04-21 14:23 UTC | 1h 46m |
| RNGR713 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-04-21 13:57 UTC | 2026-04-21 14:23 UTC | 25m |
| CXK105 | CXK | Gwinnett County/Briscoe Field (KLZU) | Aiken Field (85GA) | 2026-04-21 13:15 UTC | 2026-04-21 14:20 UTC | 1h 5m |
| N4381L |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-04-21 13:35 UTC | 2026-04-21 14:18 UTC | 43m |
| TSTR64 | TST | Patuxent River Nas (Trapnell Field) Airport (KNHK) | Patuxent River Nas (Trapnell Field) Airport (KNHK) | 2026-04-21 13:05 UTC | 2026-04-21 14:18 UTC | 1h 12m |
| BOMR804 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Ingleside Regional Airport (KTFP) | 2026-04-21 13:35 UTC | 2026-04-21 14:14 UTC | 39m |
| N70075 |  | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-04-21 13:52 UTC | 2026-04-21 14:14 UTC | 21m |
| N384CA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-04-21 13:51 UTC | 2026-04-21 14:12 UTC | 20m |
| CXK345 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-04-21 13:05 UTC | 2026-04-21 14:10 UTC | 1h 5m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-04-21 13:34 UTC | 2026-04-21 14:10 UTC | 35m |
| OOENE | OOE | Aix-en-Provence (BA 114) Airport (LFMA) | Avignon-Caumont Airport (LFMV) | 2026-04-21 13:31 UTC | 2026-04-21 14:08 UTC | 37m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-21 13:39 UTC | 2026-04-21 14:08 UTC | 29m |
| N96403 |  | Hector International Airport (KFAR) | Sky Manor Aero Estates Airport (MN86) | 2026-04-21 13:30 UTC | 2026-04-21 14:06 UTC | 36m |
| N345B |  | Doylestown Airport (KDYL) | Lancaster Airport (KLNS) | 2026-04-21 13:26 UTC | 2026-04-21 14:04 UTC | 38m |
| CXK1121 | CXK | Conroe/North Houston Regional Airport (KCXO) | Conroe/North Houston Regional Airport (KCXO) | 2026-04-21 14:01 UTC | 2026-04-21 14:02 UTC | 1m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-04-21 13:23 UTC | 2026-04-21 14:01 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
