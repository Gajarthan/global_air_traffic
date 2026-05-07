# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_19:42:40_UTC-green)

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

**Latest saved flight:** 2026-05-07 19:42:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 19:42:40 UTC

- **72,485** saved flights
- **26,912** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,485** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **892,569.0 tonnes** estimated CO2 emissions
- **51,743,132 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3122 |
| 2 | SkyWest Airlines | 2703 |
| 3 | IndiGo | 1638 |
| 4 | EJA | 1333 |
| 5 | American Airlines | 1135 |
| 6 | Southwest Airlines | 1054 |
| 7 | Lufthansa | 929 |
| 8 | ENY | 913 |
| 9 | Vueling | 707 |
| 10 | AXM | 688 |
| 11 | LATAM Airlines | 674 |
| 12 | WIF | 622 |
| 13 | Delta Air Lines | 607 |
| 14 | All Nippon Airways | 599 |
| 15 | AZU | 582 |
| 16 | Swiss International | 555 |
| 17 | QLK | 554 |
| 18 | LXJ | 528 |
| 19 | Alaska Airlines | 509 |
| 20 | easyJet | 480 |
| 21 | EJU | 468 |
| 22 | AEE | 467 |
| 23 | Cathay Pacific | 449 |
| 24 | VIV | 447 |
| 25 | Japan Airlines | 426 |
| 26 | Air France | 422 |
| 27 | AXB | 401 |
| 28 | CXK | 365 |
| 29 | AIQ | 360 |
| 30 | MXY | 349 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58081 |
| 2 | 🇪🇸 ES | 5246 |
| 3 | 🇮🇳 IN | 5141 |
| 4 | 🇦🇺 AU | 4801 |
| 5 | 🇧🇷 BR | 4060 |
| 6 | 🇩🇪 DE | 4027 |
| 7 | 🇮🇹 IT | 3970 |
| 8 | 🇯🇵 JP | 3829 |
| 9 | 🇨🇦 CA | 3619 |
| 10 | 🇬🇧 GB | 3118 |
| 11 | 🇫🇷 FR | 2853 |
| 12 | 🇨🇴 CO | 2677 |
| 13 | 🇲🇽 MX | 2277 |
| 14 | 🇬🇷 GR | 2151 |
| 15 | 🇳🇴 NO | 2016 |
| 16 | 🇨🇭 CH | 1967 |
| 17 | 🇲🇾 MY | 1715 |
| 18 | 🇿🇦 ZA | 1426 |
| 19 | 🇳🇿 NZ | 1320 |
| 20 | 🇹🇷 TR | 1303 |
| 21 | 🇹🇭 TH | 1295 |
| 22 | 🇵🇱 PL | 1209 |
| 23 | 🇵🇭 PH | 1174 |
| 24 | 🇬🇹 GT | 1147 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 862 |
| 27 | 🇲🇴 MO | 843 |
| 28 | 🇲🇪 ME | 771 |
| 29 | 🇳🇱 NL | 752 |
| 30 | 🇧🇸 BS | 610 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1616 |
| 2 | Tokyo International Airport |  | JP | 1287 |
| 3 | Denver International Airport |  | US | 1211 |
| 4 | Indira Gandhi International Airport |  | IN | 1084 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1052 |
| 6 | Frankfurt am Main International Airport |  | DE | 923 |
| 7 | Harry Reid International Airport |  | US | 906 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 872 |
| 10 | Zurich Airport |  | CH | 857 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 843 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 730 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 689 |
| 16 | Madrid Barajas International Airport |  | ES | 681 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 646 |
| 18 | Malpensa International Airport |  | IT | 631 |
| 19 | Bengaluru International Airport |  | IN | 627 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 21 | Salt Lake City International Airport |  | US | 592 |
| 22 | Charlotte/Douglas International Airport |  | US | 572 |
| 23 | Capua Airport |  | IT | 572 |
| 24 | Congonhas Airport |  | BR | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 565 |
| 26 | Tenerife Norte Airport |  | ES | 550 |
| 27 | Ninoy Aquino International Airport |  | PH | 534 |
| 28 | Daniel K Inouye International Airport |  | US | 533 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 521 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 500 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 492 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 486 |
| 34 | Vitoria/Foronda Airport |  | ES | 476 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 457 |
| 36 | Don Mueang International Airport |  | TH | 455 |
| 37 | O. R. Tambo International Airport |  | ZA | 447 |
| 38 | Amsterdam Airport Schiphol |  | NL | 447 |
| 39 | Calgary International Airport |  | CA | 435 |
| 40 | Reno/Tahoe International Airport |  | US | 425 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 362 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 256 | 21m | 244 km | 1,077.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 211 | 24m | 225 km | 818.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 161 | 26m | 275 km | 762.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 105 | 14m | 154 km | 278.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 93 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 91 | 23m | 55 km | 86.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N703AC |  | Middleton Municipal/Morey Field (KC29) | Dubuque Regional Airport (KDBQ) | 2026-05-07 19:03 UTC | 2026-05-07 19:42 UTC | 38m |
| ES800 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-05-07 19:00 UTC | 2026-05-07 19:37 UTC | 37m |
| RTY592 | RTY | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-07 18:51 UTC | 2026-05-07 19:33 UTC | 41m |
| N6268D |  | Cricket Field (4WA2) | Wissler's Airport (65WA) | 2026-05-07 19:04 UTC | 2026-05-07 19:31 UTC | 27m |
| BOX712 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-05-07 04:22 UTC | 2026-05-07 19:29 UTC | 15h 6m |
| MXY882 | MXY | Orlando International Airport (KMCO) | Zoltak Landing Airport (50FL) | 2026-05-07 18:02 UTC | 2026-05-07 19:28 UTC | 1h 26m |
| KSF18 | KSF | Kent State University Airport (K1G3) | Jetway Airport (61OH) | 2026-05-07 19:18 UTC | 2026-05-07 19:27 UTC | 9m |
| HRD30 | HRD | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-05-07 18:43 UTC | 2026-05-07 19:27 UTC | 44m |
| UAL2185 | United Airlines | Denver International Airport (KDEN) | 93FD (93FD) | 2026-05-07 17:08 UTC | 2026-05-07 19:24 UTC | 2h 16m |
| FLC91 | FLC | Santa Fe Regional Airport (KSAF) | Clifford Field (1CO4) | 2026-05-07 18:12 UTC | 2026-05-07 19:21 UTC | 1h 9m |
| N7EA |  | Mesa Gateway Airport (KIWA) | Montezuma Airport (19AZ) | 2026-05-07 19:01 UTC | 2026-05-07 19:21 UTC | 19m |
| PAT087 | PAT | Wheeler Army Air Field (PHHI) | Hi 23 Airstrip (HI46) | 2026-05-07 19:01 UTC | 2026-05-07 19:20 UTC | 19m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-07 18:56 UTC | 2026-05-07 19:19 UTC | 22m |
| N851AA |  | North Palm Beach County General Aviation Airport (KF45) | North Palm Beach County General Aviation Airport (KF45) | 2026-05-07 19:16 UTC | 2026-05-07 19:18 UTC | 2m |
| SFY556 | SFY | Broocke Air Patch Airport (FL95) | Space Coast Regional Airport (KTIX) | 2026-05-07 18:44 UTC | 2026-05-07 19:17 UTC | 32m |
| N956PP |  | Fulton County Executive/Charlie Brown Field (KFTY) | Raleigh-Durham International Airport (KRDU) | 2026-05-07 18:22 UTC | 2026-05-07 19:16 UTC | 54m |
| SKW4023 | SkyWest Airlines | Portland International Airport (KPDX) | Boeing Field/King County International Airport (KBFI) | 2026-05-07 18:46 UTC | 2026-05-07 19:16 UTC | 30m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-07 18:27 UTC | 2026-05-07 19:14 UTC | 46m |
| N377MD |  | Dekalb-Peachtree Airport (KPDK) | Akron-Canton Regional Airport (KCAK) | 2026-05-07 18:07 UTC | 2026-05-07 19:12 UTC | 1h 4m |
| N5253X |  | Dupage Airport (KDPA) | Aero Lake Estates Airport (30IS) | 2026-05-07 18:43 UTC | 2026-05-07 19:12 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
