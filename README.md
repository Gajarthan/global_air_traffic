# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_14:15:41_UTC-green)

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

**Latest saved flight:** 2026-04-30 14:15:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 14:15:41 UTC

- **60,554** saved flights
- **23,334** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,554** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **738,461.2 tonnes** estimated CO2 emissions
- **42,809,346 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2568 |
| 2 | SkyWest Airlines | 2254 |
| 3 | IndiGo | 1395 |
| 4 | EJA | 1082 |
| 5 | American Airlines | 943 |
| 6 | Southwest Airlines | 855 |
| 7 | Lufthansa | 771 |
| 8 | ENY | 748 |
| 9 | Vueling | 604 |
| 10 | AXM | 595 |
| 11 | LATAM Airlines | 578 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 514 |
| 14 | Delta Air Lines | 503 |
| 15 | AZU | 495 |
| 16 | QLK | 478 |
| 17 | Swiss International | 478 |
| 18 | LXJ | 428 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 401 |
| 21 | easyJet | 399 |
| 22 | EJU | 390 |
| 23 | VIV | 379 |
| 24 | Cathay Pacific | 362 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 332 |
| 28 | AIQ | 309 |
| 29 | JetBlue | 300 |
| 30 | CXK | 299 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47729 |
| 2 | 🇪🇸 ES | 4404 |
| 3 | 🇮🇳 IN | 4401 |
| 4 | 🇦🇺 AU | 4149 |
| 5 | 🇧🇷 BR | 3429 |
| 6 | 🇩🇪 DE | 3374 |
| 7 | 🇯🇵 JP | 3315 |
| 8 | 🇮🇹 IT | 3312 |
| 9 | 🇨🇦 CA | 2994 |
| 10 | 🇨🇴 CO | 2617 |
| 11 | 🇬🇧 GB | 2571 |
| 12 | 🇫🇷 FR | 2393 |
| 13 | 🇲🇽 MX | 1887 |
| 14 | 🇬🇷 GR | 1809 |
| 15 | 🇨🇭 CH | 1703 |
| 16 | 🇳🇴 NO | 1684 |
| 17 | 🇲🇾 MY | 1447 |
| 18 | 🇿🇦 ZA | 1241 |
| 19 | 🇳🇿 NZ | 1139 |
| 20 | 🇹🇭 TH | 1097 |
| 21 | 🇹🇷 TR | 1078 |
| 22 | 🇵🇭 PH | 1023 |
| 23 | 🇰🇷 KR | 985 |
| 24 | 🇵🇱 PL | 982 |
| 25 | 🇬🇹 GT | 884 |
| 26 | 🇲🇦 MA | 755 |
| 27 | 🇲🇴 MO | 674 |
| 28 | 🇲🇪 ME | 665 |
| 29 | 🇳🇱 NL | 636 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1339 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1005 |
| 4 | Indira Gandhi International Airport |  | IN | 929 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 889 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 812 |
| 8 | Harry Reid International Airport |  | US | 768 |
| 9 | Frankfurt am Main International Airport |  | DE | 766 |
| 10 | Zurich Airport |  | CH | 730 |
| 11 | Macau International Airport |  | MO | 674 |
| 12 | La Aurora Airport |  | GT | 665 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 599 |
| 14 | Chicago O'Hare International Airport |  | US | 573 |
| 15 | Kuala Lumpur International Airport |  | MY | 570 |
| 16 | Madrid Barajas International Airport |  | ES | 565 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Malpensa International Airport |  | IT | 527 |
| 20 | Bengaluru International Airport |  | IN | 527 |
| 21 | Congonhas Airport |  | BR | 494 |
| 22 | Charlotte/Douglas International Airport |  | US | 481 |
| 23 | Charles de Gaulle International Airport |  | FR | 473 |
| 24 | Tenerife Norte Airport |  | ES | 472 |
| 25 | Salt Lake City International Airport |  | US | 468 |
| 26 | Ninoy Aquino International Airport |  | PH | 468 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 454 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 31 | Barcelona International Airport |  | ES | 412 |
| 32 | Vitoria/Foronda Airport |  | ES | 409 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 398 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 384 |
| 37 | Reno/Tahoe International Airport |  | US | 383 |
| 38 | Don Mueang International Airport |  | TH | 378 |
| 39 | Amsterdam Airport Schiphol |  | NL | 372 |
| 40 | Calgary International Airport |  | CA | 358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 332 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 179 | 1h 27m | 910 km | 2,808.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 150 | 19m | 165 km | 426.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 144 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 137 | 26m | 275 km | 649.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 102 | 31m | 369 km | 649.3 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 102 | 20m | 99 km | 174.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 84 | 1h 42m | 1,156 km | 1,675.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 80 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 78 | 14m | 154 km | 206.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-04-30 14:02 UTC | 2026-04-30 14:15 UTC | 13m |
| N6243C |  | Leesburg International Airport (KLEE) | Leesburg International Airport (KLEE) | 2026-04-30 13:29 UTC | 2026-04-30 14:10 UTC | 41m |
| BURNY17 | BUR | Wildlife/Stroud Airport (TS80) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-04-30 13:49 UTC | 2026-04-30 14:07 UTC | 17m |
| UAE4DU | Emirates | Dubai International Airport (OMDB) | Heidelburg Airport (FAHG) | 2026-04-30 06:26 UTC | 2026-04-30 14:05 UTC | 7h 39m |
| ERU17 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-04-30 13:35 UTC | 2026-04-30 14:03 UTC | 27m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-30 12:46 UTC | 2026-04-30 14:02 UTC | 1h 15m |
| N457MT |  | Stonewall Airpark (41TN) | John C Tune Airport (KJWN) | 2026-04-30 13:35 UTC | 2026-04-30 13:57 UTC | 21m |
| IGO1161 | IndiGo | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-30 12:43 UTC | 2026-04-30 13:55 UTC | 1h 11m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-04-30 13:10 UTC | 2026-04-30 13:49 UTC | 38m |
| SRG336 | SRG | Caernarfon Airport (EGCK) | Caernarfon Airport (EGCK) | 2026-04-30 13:16 UTC | 2026-04-30 13:47 UTC | 31m |
|  |  | Ny-Ålesund Airport Hamnerabben (ENAS) | Ny-Ålesund Airport Hamnerabben (ENAS) | 2026-04-30 13:36 UTC | 2026-04-30 13:46 UTC | 10m |
| PCH60T | PCH | Buochs Airport (LSZC) | Dubendorf Airport (LSMD) | 2026-04-30 13:35 UTC | 2026-04-30 13:46 UTC | 10m |
| CXA826 | CXA | Charles de Gaulle International Airport (LFPG) | Staroselye Airport (UUBK) | 2026-04-30 10:33 UTC | 2026-04-30 13:46 UTC | 3h 12m |
| CHH470 | CHH | Brussels Airport (EBBR) | Tunoshna Airport (UUDL) | 2026-04-30 10:26 UTC | 2026-04-30 13:44 UTC | 3h 17m |
| N583CT |  | Sarasota/Bradenton International Airport (KSRQ) | Bald Eagle Airfield- Myakka Head Airport (67FL) | 2026-04-30 12:58 UTC | 2026-04-30 13:41 UTC | 42m |
| HBZYW | HBZ | Wangen-Lachen Airport (LSPV) | Buochs Airport (LSZC) | 2026-04-30 13:25 UTC | 2026-04-30 13:40 UTC | 14m |
| N314LM |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-04-30 13:15 UTC | 2026-04-30 13:37 UTC | 22m |
| N426RB |  | Tulsa Riverside Airport (KRVS) | Haskell Airport (K2K9) | 2026-04-30 13:12 UTC | 2026-04-30 13:36 UTC | 23m |
| N624B |  | Lovell Field (KCHA) | Pratermill Flight Park Airport (GA72) | 2026-04-30 13:17 UTC | 2026-04-30 13:35 UTC | 17m |
| N458G |  | Mc Clellan Airfield (KMCC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-30 12:56 UTC | 2026-04-30 13:33 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
