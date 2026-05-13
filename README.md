# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_13:08:56_UTC-green)

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

**Latest saved flight:** 2026-05-13 13:08:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 13:08:56 UTC

- **80,060** saved flights
- **29,105** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **80,060** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **988,180.2 tonnes** estimated CO2 emissions
- **57,285,808 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3447 |
| 2 | SkyWest Airlines | 2967 |
| 3 | IndiGo | 1771 |
| 4 | EJA | 1481 |
| 5 | American Airlines | 1239 |
| 6 | Southwest Airlines | 1170 |
| 7 | Lufthansa | 1051 |
| 8 | ENY | 996 |
| 9 | Delta Air Lines | 876 |
| 10 | Vueling | 766 |
| 11 | AXM | 734 |
| 12 | LATAM Airlines | 727 |
| 13 | WIF | 694 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 629 |
| 16 | Swiss International | 623 |
| 17 | QLK | 596 |
| 18 | LXJ | 580 |
| 19 | Alaska Airlines | 562 |
| 20 | easyJet | 534 |
| 21 | AEE | 516 |
| 22 | EJU | 516 |
| 23 | Cathay Pacific | 504 |
| 24 | Air France | 474 |
| 25 | VIV | 474 |
| 26 | Japan Airlines | 457 |
| 27 | AXB | 438 |
| 28 | CXK | 417 |
| 29 | AIQ | 399 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64925 |
| 2 | 🇪🇸 ES | 5720 |
| 3 | 🇮🇳 IN | 5537 |
| 4 | 🇦🇺 AU | 5139 |
| 5 | 🇩🇪 DE | 4541 |
| 6 | 🇮🇹 IT | 4440 |
| 7 | 🇧🇷 BR | 4421 |
| 8 | 🇯🇵 JP | 4123 |
| 9 | 🇨🇦 CA | 3988 |
| 10 | 🇬🇧 GB | 3444 |
| 11 | 🇫🇷 FR | 3188 |
| 12 | 🇨🇴 CO | 2712 |
| 13 | 🇲🇽 MX | 2407 |
| 14 | 🇬🇷 GR | 2357 |
| 15 | 🇳🇴 NO | 2228 |
| 16 | 🇨🇭 CH | 2164 |
| 17 | 🇲🇾 MY | 1838 |
| 18 | 🇿🇦 ZA | 1524 |
| 19 | 🇹🇷 TR | 1437 |
| 20 | 🇹🇭 TH | 1419 |
| 21 | 🇳🇿 NZ | 1414 |
| 22 | 🇵🇱 PL | 1333 |
| 23 | 🇵🇭 PH | 1267 |
| 24 | 🇰🇷 KR | 1235 |
| 25 | 🇬🇹 GT | 1224 |
| 26 | 🇲🇦 MA | 941 |
| 27 | 🇲🇴 MO | 928 |
| 28 | 🇲🇪 ME | 857 |
| 29 | 🇳🇱 NL | 830 |
| 30 | 🇭🇷 HR | 708 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1757 |
| 2 | Tokyo International Airport |  | JP | 1383 |
| 3 | Denver International Airport |  | US | 1339 |
| 4 | Indira Gandhi International Airport |  | IN | 1171 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1155 |
| 6 | Frankfurt am Main International Airport |  | DE | 1056 |
| 7 | Harry Reid International Airport |  | US | 993 |
| 8 | Zurich Airport |  | CH | 957 |
| 9 | Macau International Airport |  | MO | 928 |
| 10 | La Aurora Airport |  | GT | 922 |
| 11 | Guaymaral Airport |  | CO | 904 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 898 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 810 |
| 15 | Chicago O'Hare International Airport |  | US | 779 |
| 16 | Madrid Barajas International Airport |  | ES | 736 |
| 17 | Kuala Lumpur International Airport |  | MY | 735 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 705 |
| 19 | Malpensa International Airport |  | IT | 687 |
| 20 | Bengaluru International Airport |  | IN | 681 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 22 | Salt Lake City International Airport |  | US | 655 |
| 23 | Capua Airport |  | IT | 652 |
| 24 | Charles de Gaulle International Airport |  | FR | 629 |
| 25 | Charlotte/Douglas International Airport |  | US | 628 |
| 26 | Congonhas Airport |  | BR | 624 |
| 27 | Tenerife Norte Airport |  | ES | 595 |
| 28 | Daniel K Inouye International Airport |  | US | 581 |
| 29 | Ninoy Aquino International Airport |  | PH | 578 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 574 |
| 31 | Barcelona International Airport |  | ES | 538 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 536 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 531 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 524 |
| 35 | Vitoria/Foronda Airport |  | ES | 510 |
| 36 | Don Mueang International Airport |  | TH | 508 |
| 37 | Amsterdam Airport Schiphol |  | NL | 502 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 496 |
| 39 | O. R. Tambo International Airport |  | ZA | 483 |
| 40 | Calgary International Airport |  | CA | 471 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 376 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 288 | 21m | 244 km | 1,212.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 216 | 1h 27m | 910 km | 3,389.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 203 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 192 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 182 | 1h 11m | 770 km | 2,417.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 117 | 20m | 147 km | 296.1 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 107 | 57m | 493 km | 910.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 2m | 695 km | 1,270.6 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 102 | 18m | 144 km | 253.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 101 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N541LA |  | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | Ferguson Airport (81VA) | 2026-05-13 12:32 UTC | 2026-05-13 13:08 UTC | 36m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-13 12:51 UTC | 2026-05-13 13:05 UTC | 14m |
| OKIMC | OKI | Holic Airport (LZHL) | Mlada Boleslav Airport (LKMB) | 2026-05-13 12:00 UTC | 2026-05-13 13:00 UTC | 1h 0m |
| N486BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-05-13 12:35 UTC | 2026-05-13 12:59 UTC | 24m |
| EZY9 | easyJet | Durham Tees Valley Airport (EGNV) | Durham Tees Valley Airport (EGNV) | 2026-05-13 12:37 UTC | 2026-05-13 12:59 UTC | 21m |
| 00000000 |  | Dothan Regional Airport (KDHN) | Mid-Way Regional Airport (KJWY) | 2026-05-13 11:11 UTC | 2026-05-13 12:53 UTC | 1h 41m |
| N842KP |  | Lewis University Airport (KLOT) | Neiner Airport (19LL) | 2026-05-13 12:04 UTC | 2026-05-13 12:45 UTC | 40m |
| N428S |  | Erie-Ottawa International Airport (KPCW) | Erie-Ottawa International Airport (KPCW) | 2026-05-13 12:42 UTC | 2026-05-13 12:44 UTC | 1m |
| CXK549 | CXK | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-05-13 11:55 UTC | 2026-05-13 12:37 UTC | 41m |
| C18 |  | LHFP (LHFP) | Vienna International Airport (LOWW) | 2026-05-13 12:24 UTC | 2026-05-13 12:36 UTC | 11m |
| CXK461 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-13 12:10 UTC | 2026-05-13 12:33 UTC | 23m |
| ZSPLL | ZSP | O. R. Tambo International Airport (FAOR) | Krugersdorp Airport (FAKR) | 2026-05-13 12:05 UTC | 2026-05-13 12:32 UTC | 27m |
| N682SA |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-13 12:15 UTC | 2026-05-13 12:30 UTC | 15m |
| N905NY |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-05-13 12:14 UTC | 2026-05-13 12:29 UTC | 14m |
| N350PR |  | Baton Rouge Metro, Ryan Field (KBTR) | LA31 (LA31) | 2026-05-13 12:07 UTC | 2026-05-13 12:23 UTC | 16m |
| AGV01 | AGV | Courchevel Airport (LFLJ) | Aosta Airport (LIMW) | 2026-05-13 12:04 UTC | 2026-05-13 12:23 UTC | 19m |
| DLH6CN | Lufthansa | Frankfurt am Main International Airport (EDDF) | Herzogenaurach Airport (EDQH) | 2026-05-13 11:50 UTC | 2026-05-13 12:22 UTC | 31m |
| HB2505 |  | Nikolsdorf Airport (LOKL) | Nikolsdorf Airport (LOKL) | 2026-05-13 12:00 UTC | 2026-05-13 12:18 UTC | 17m |
| IOS240 | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-05-13 11:54 UTC | 2026-05-13 12:17 UTC | 22m |
| AAH56 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-05-13 11:54 UTC | 2026-05-13 12:16 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
