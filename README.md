# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_01:21:29_UTC-green)

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

**Latest saved flight:** 2026-05-13 01:21:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 01:21:29 UTC

- **79,840** saved flights
- **29,039** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,840** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **985,583.9 tonnes** estimated CO2 emissions
- **57,135,299 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3435 |
| 2 | SkyWest Airlines | 2967 |
| 3 | IndiGo | 1761 |
| 4 | EJA | 1481 |
| 5 | American Airlines | 1239 |
| 6 | Southwest Airlines | 1169 |
| 7 | Lufthansa | 1048 |
| 8 | ENY | 996 |
| 9 | Delta Air Lines | 875 |
| 10 | Vueling | 764 |
| 11 | AXM | 732 |
| 12 | LATAM Airlines | 726 |
| 13 | WIF | 690 |
| 14 | All Nippon Airways | 638 |
| 15 | AZU | 628 |
| 16 | Swiss International | 617 |
| 17 | QLK | 596 |
| 18 | LXJ | 579 |
| 19 | Alaska Airlines | 562 |
| 20 | easyJet | 533 |
| 21 | EJU | 515 |
| 22 | AEE | 514 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 474 |
| 25 | Air France | 470 |
| 26 | Japan Airlines | 455 |
| 27 | AXB | 438 |
| 28 | CXK | 414 |
| 29 | AIQ | 397 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64858 |
| 2 | 🇪🇸 ES | 5688 |
| 3 | 🇮🇳 IN | 5512 |
| 4 | 🇦🇺 AU | 5131 |
| 5 | 🇩🇪 DE | 4513 |
| 6 | 🇮🇹 IT | 4424 |
| 7 | 🇧🇷 BR | 4411 |
| 8 | 🇯🇵 JP | 4095 |
| 9 | 🇨🇦 CA | 3986 |
| 10 | 🇬🇧 GB | 3428 |
| 11 | 🇫🇷 FR | 3169 |
| 12 | 🇨🇴 CO | 2709 |
| 13 | 🇲🇽 MX | 2407 |
| 14 | 🇬🇷 GR | 2347 |
| 15 | 🇳🇴 NO | 2211 |
| 16 | 🇨🇭 CH | 2150 |
| 17 | 🇲🇾 MY | 1833 |
| 18 | 🇿🇦 ZA | 1510 |
| 19 | 🇹🇷 TR | 1437 |
| 20 | 🇳🇿 NZ | 1414 |
| 21 | 🇹🇭 TH | 1408 |
| 22 | 🇵🇱 PL | 1329 |
| 23 | 🇵🇭 PH | 1266 |
| 24 | 🇰🇷 KR | 1230 |
| 25 | 🇬🇹 GT | 1224 |
| 26 | 🇲🇦 MA | 938 |
| 27 | 🇲🇴 MO | 925 |
| 28 | 🇲🇪 ME | 854 |
| 29 | 🇳🇱 NL | 827 |
| 30 | 🇭🇷 HR | 703 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1757 |
| 2 | Tokyo International Airport |  | JP | 1377 |
| 3 | Denver International Airport |  | US | 1339 |
| 4 | Indira Gandhi International Airport |  | IN | 1166 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1151 |
| 6 | Frankfurt am Main International Airport |  | DE | 1051 |
| 7 | Harry Reid International Airport |  | US | 992 |
| 8 | Zurich Airport |  | CH | 948 |
| 9 | Macau International Airport |  | MO | 925 |
| 10 | La Aurora Airport |  | GT | 922 |
| 11 | Guaymaral Airport |  | CO | 901 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 897 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 810 |
| 15 | Chicago O'Hare International Airport |  | US | 779 |
| 16 | Kuala Lumpur International Airport |  | MY | 733 |
| 17 | Madrid Barajas International Airport |  | ES | 732 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 705 |
| 19 | Malpensa International Airport |  | IT | 684 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 21 | Bengaluru International Airport |  | IN | 679 |
| 22 | Salt Lake City International Airport |  | US | 655 |
| 23 | Capua Airport |  | IT | 650 |
| 24 | Charlotte/Douglas International Airport |  | US | 628 |
| 25 | Charles de Gaulle International Airport |  | FR | 624 |
| 26 | Congonhas Airport |  | BR | 623 |
| 27 | Tenerife Norte Airport |  | ES | 592 |
| 28 | Daniel K Inouye International Airport |  | US | 580 |
| 29 | Ninoy Aquino International Airport |  | PH | 577 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 570 |
| 31 | Barcelona International Airport |  | ES | 537 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 535 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 531 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 522 |
| 35 | Vitoria/Foronda Airport |  | ES | 507 |
| 36 | Don Mueang International Airport |  | TH | 504 |
| 37 | Amsterdam Airport Schiphol |  | NL | 500 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 495 |
| 39 | O. R. Tambo International Airport |  | ZA | 477 |
| 40 | Calgary International Airport |  | CA | 471 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 375 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 287 | 21m | 244 km | 1,208.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 214 | 1h 27m | 910 km | 3,358.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 203 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 180 | 1h 11m | 770 km | 2,391.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 117 | 20m | 147 km | 296.1 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 115 | 20m | 250 km | 496.7 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
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
| BOSOX45 | BOS | Cape Cod Coast Guard Air Station (KFMH) | Cape Cod Coast Guard Air Station (KFMH) | 2026-05-13 00:39 UTC | 2026-05-13 01:21 UTC | 41m |
| N7874N |  | City Of Colorado Springs Municipal Airport (KCOS) | Mann Ranch Airport (95CO) | 2026-05-13 00:30 UTC | 2026-05-13 01:06 UTC | 35m |
| BLITZ56 | BLI | Indiana County/Jimmy Stewart Field (KIDI) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-05-13 00:47 UTC | 2026-05-13 01:00 UTC | 12m |
| UAL2651 | United Airlines | Palm Springs International Airport (KPSP) | Denver International Airport (KDEN) | 2026-05-12 23:19 UTC | 2026-05-13 00:59 UTC | 1h 40m |
| CXK340 | CXK | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-13 00:46 UTC | 2026-05-13 00:56 UTC | 10m |
| BRG622 | BRG | Kobuk Airport (PAOB) | Ambler Airport (PAFM) | 2026-05-13 00:42 UTC | 2026-05-13 00:55 UTC | 12m |
| QLK35D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 2026-05-12 23:40 UTC | 2026-05-13 00:51 UTC | 1h 11m |
| HMF003 | HMF | Gothenburg City Airport (ESGP) | Gothenburg City Airport (ESGP) | 2026-05-13 00:34 UTC | 2026-05-13 00:51 UTC | 16m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Elk Park Ranch Airport (34CD) | 2026-05-13 00:31 UTC | 2026-05-13 00:42 UTC | 11m |
| JGR3055 | JGR | Amakusa Airport (RJDA) | Amakusa Airport (RJDA) | 2026-05-13 00:41 UTC | 2026-05-13 00:42 UTC | 1m |
| CFEWO | CFE | Three Hills Airport (CEN3) | Calgary / Springbank Airport (CYBW) | 2026-05-12 23:50 UTC | 2026-05-13 00:42 UTC | 51m |
| N245FR |  | 95CA (95CA) | Meadows Field (KBFL) | 2026-05-12 23:56 UTC | 2026-05-13 00:41 UTC | 45m |
| N955JS |  | Mc Clellan Airfield (KMCC) | Henderson Executive Airport (KHND) | 2026-05-12 23:30 UTC | 2026-05-13 00:36 UTC | 1h 5m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-05-12 23:39 UTC | 2026-05-13 00:34 UTC | 55m |
| PCM7703 | PCM | 66CL (66CL) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-13 00:02 UTC | 2026-05-13 00:33 UTC | 30m |
| N78US |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-05-12 23:53 UTC | 2026-05-13 00:31 UTC | 37m |
| SWA4262 | Southwest Airlines | Norman Y Mineta San Jose International Airport (KSJC) | Palm Springs International Airport (KPSP) | 2026-05-12 23:27 UTC | 2026-05-13 00:27 UTC | 59m |
| N753C |  | Rocky Mountain Metro Airport (KBJC) | 51CA (51CA) | 2026-05-12 21:40 UTC | 2026-05-13 00:25 UTC | 2h 44m |
| JANET15 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-05-13 00:14 UTC | 2026-05-13 00:25 UTC | 11m |
| JAL373 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-12 23:19 UTC | 2026-05-13 00:24 UTC | 1h 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
