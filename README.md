# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_22:30:44_UTC-green)

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

**Latest saved flight:** 2026-05-12 22:30:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 22:30:44 UTC

- **79,629** saved flights
- **28,967** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,629** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **983,733.2 tonnes** estimated CO2 emissions
- **57,028,011 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3433 |
| 2 | SkyWest Airlines | 2961 |
| 3 | IndiGo | 1761 |
| 4 | EJA | 1470 |
| 5 | American Airlines | 1238 |
| 6 | Southwest Airlines | 1164 |
| 7 | Lufthansa | 1048 |
| 8 | ENY | 991 |
| 9 | Delta Air Lines | 870 |
| 10 | Vueling | 764 |
| 11 | AXM | 729 |
| 12 | LATAM Airlines | 723 |
| 13 | WIF | 690 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 625 |
| 16 | Swiss International | 617 |
| 17 | QLK | 592 |
| 18 | LXJ | 578 |
| 19 | Alaska Airlines | 558 |
| 20 | easyJet | 533 |
| 21 | EJU | 515 |
| 22 | AEE | 513 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 473 |
| 25 | Air France | 470 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 438 |
| 28 | CXK | 411 |
| 29 | AIQ | 397 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64601 |
| 2 | 🇪🇸 ES | 5687 |
| 3 | 🇮🇳 IN | 5512 |
| 4 | 🇦🇺 AU | 5095 |
| 5 | 🇩🇪 DE | 4512 |
| 6 | 🇮🇹 IT | 4424 |
| 7 | 🇧🇷 BR | 4395 |
| 8 | 🇯🇵 JP | 4073 |
| 9 | 🇨🇦 CA | 3973 |
| 10 | 🇬🇧 GB | 3427 |
| 11 | 🇫🇷 FR | 3169 |
| 12 | 🇨🇴 CO | 2709 |
| 13 | 🇲🇽 MX | 2405 |
| 14 | 🇬🇷 GR | 2343 |
| 15 | 🇳🇴 NO | 2211 |
| 16 | 🇨🇭 CH | 2150 |
| 17 | 🇲🇾 MY | 1828 |
| 18 | 🇿🇦 ZA | 1510 |
| 19 | 🇹🇷 TR | 1436 |
| 20 | 🇹🇭 TH | 1408 |
| 21 | 🇳🇿 NZ | 1406 |
| 22 | 🇵🇱 PL | 1329 |
| 23 | 🇵🇭 PH | 1260 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1222 |
| 26 | 🇲🇦 MA | 938 |
| 27 | 🇲🇴 MO | 925 |
| 28 | 🇲🇪 ME | 854 |
| 29 | 🇳🇱 NL | 827 |
| 30 | 🇭🇷 HR | 703 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1749 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1335 |
| 4 | Indira Gandhi International Airport |  | IN | 1166 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1149 |
| 6 | Frankfurt am Main International Airport |  | DE | 1051 |
| 7 | Harry Reid International Airport |  | US | 985 |
| 8 | Zurich Airport |  | CH | 948 |
| 9 | Macau International Airport |  | MO | 925 |
| 10 | La Aurora Airport |  | GT | 920 |
| 11 | Guaymaral Airport |  | CO | 901 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 892 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 807 |
| 15 | Chicago O'Hare International Airport |  | US | 775 |
| 16 | Madrid Barajas International Airport |  | ES | 732 |
| 17 | Kuala Lumpur International Airport |  | MY | 730 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 701 |
| 19 | Malpensa International Airport |  | IT | 684 |
| 20 | Bengaluru International Airport |  | IN | 679 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 22 | Salt Lake City International Airport |  | US | 650 |
| 23 | Capua Airport |  | IT | 650 |
| 24 | Charlotte/Douglas International Airport |  | US | 628 |
| 25 | Charles de Gaulle International Airport |  | FR | 624 |
| 26 | Congonhas Airport |  | BR | 620 |
| 27 | Tenerife Norte Airport |  | ES | 592 |
| 28 | Daniel K Inouye International Airport |  | US | 578 |
| 29 | Ninoy Aquino International Airport |  | PH | 574 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 570 |
| 31 | Barcelona International Airport |  | ES | 536 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 535 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 530 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 522 |
| 35 | Vitoria/Foronda Airport |  | ES | 507 |
| 36 | Don Mueang International Airport |  | TH | 504 |
| 37 | Amsterdam Airport Schiphol |  | NL | 500 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 494 |
| 39 | O. R. Tambo International Airport |  | ZA | 477 |
| 40 | Calgary International Airport |  | CA | 469 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 375 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 285 | 21m | 244 km | 1,200.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 202 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 117 | 20m | 147 km | 296.1 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 115 | 20m | 250 km | 496.7 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 2m | 695 km | 1,270.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 106 | 57m | 493 km | 901.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 105 | 1h 42m | 1,423 km | 2,576.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 101 | 18m | 144 km | 251.2 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 100 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| STMPD19 | STM | Cones Field (2CA2) | Holiday Ranch Airport (27CA) | 2026-05-12 22:18 UTC | 2026-05-12 22:30 UTC | 12m |
| AL4 |  | Wallacia Airport (YWLX) | Wallacia Airport (YWLX) | 2026-05-12 21:39 UTC | 2026-05-12 22:29 UTC | 50m |
| N2477F |  | Buchanan Field (KCCR) | Mc Clellan Airfield (KMCC) | 2026-05-12 21:43 UTC | 2026-05-12 22:29 UTC | 45m |
| N82RF |  | Spokane International Airport (KGEG) | Flying R Airport (11UT) | 2026-05-12 17:34 UTC | 2026-05-12 22:21 UTC | 4h 46m |
| ERU11 | ERU | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-05-12 22:05 UTC | 2026-05-12 22:18 UTC | 12m |
| N323CL |  | Brookhaven Airport (KHWV) | Westmoreland Airport (49NY) | 2026-05-12 22:04 UTC | 2026-05-12 22:15 UTC | 11m |
| N716AT |  | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-05-12 21:56 UTC | 2026-05-12 22:13 UTC | 16m |
| HAWK268 | HAW | Kingsville Nas Airport (KNQI) | Orange Grove Nalf Airport (KNOG) | 2026-05-12 21:39 UTC | 2026-05-12 22:13 UTC | 34m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-05-12 10:17 UTC | 2026-05-12 22:10 UTC | 11h 52m |
| N7190C |  | Chandler Municipal Airport (KCHD) | Pegasus Airpark (5AZ3) | 2026-05-12 21:51 UTC | 2026-05-12 22:10 UTC | 19m |
| WAH | WAH | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-05-12 22:01 UTC | 2026-05-12 22:09 UTC | 8m |
| N3055N |  | Mc Minnville Municipal Airport (KMMV) | Mc Minnville Municipal Airport (KMMV) | 2026-05-12 22:02 UTC | 2026-05-12 22:05 UTC | 2m |
| N955LA |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-05-12 21:02 UTC | 2026-05-12 22:04 UTC | 1h 1m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-05-12 20:19 UTC | 2026-05-12 22:01 UTC | 1h 42m |
| N327CH |  | 2LL5 (2LL5) | Frasca Field (KC16) | 2026-05-12 21:56 UTC | 2026-05-12 22:01 UTC | 5m |
| TRP2 | TRP | Deale Airport (MD22) | Joint Base Andrews Airport (KADW) | 2026-05-12 21:51 UTC | 2026-05-12 22:00 UTC | 8m |
| N42742 |  | Stoney Point Field (6GA0) | Pickens County Airport (KJZP) | 2026-05-12 21:21 UTC | 2026-05-12 21:58 UTC | 36m |
| N439H |  | Westover Arb/Metro Airport (KCEF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-12 21:28 UTC | 2026-05-12 21:57 UTC | 29m |
| N40798 |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-05-12 21:15 UTC | 2026-05-12 21:57 UTC | 41m |
| N29BB |  | Buchanan Field (KCCR) | Truckee-Tahoe Airport (KTRK) | 2026-05-12 21:24 UTC | 2026-05-12 21:56 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
