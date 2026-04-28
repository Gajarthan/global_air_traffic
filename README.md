# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_15:28:49_UTC-green)

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

**Latest saved flight:** 2026-04-28 15:28:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 15:28:49 UTC

- **58,300** saved flights
- **22,691** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,300** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **708,851.6 tonnes** estimated CO2 emissions
- **41,092,846 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2482 |
| 2 | SkyWest Airlines | 2191 |
| 3 | IndiGo | 1337 |
| 4 | EJA | 1032 |
| 5 | American Airlines | 918 |
| 6 | Southwest Airlines | 833 |
| 7 | Lufthansa | 737 |
| 8 | ENY | 728 |
| 9 | Vueling | 580 |
| 10 | AXM | 570 |
| 11 | LATAM Airlines | 555 |
| 12 | All Nippon Airways | 517 |
| 13 | WIF | 487 |
| 14 | AZU | 483 |
| 15 | Delta Air Lines | 476 |
| 16 | Swiss International | 464 |
| 17 | QLK | 456 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 396 |
| 20 | AEE | 388 |
| 21 | easyJet | 383 |
| 22 | EJU | 378 |
| 23 | VIV | 369 |
| 24 | Air France | 342 |
| 25 | Cathay Pacific | 338 |
| 26 | Japan Airlines | 338 |
| 27 | AXB | 319 |
| 28 | AIQ | 295 |
| 29 | JetBlue | 294 |
| 30 | United Airlines | 291 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46057 |
| 2 | 🇪🇸 ES | 4244 |
| 3 | 🇮🇳 IN | 4205 |
| 4 | 🇦🇺 AU | 3959 |
| 5 | 🇧🇷 BR | 3310 |
| 6 | 🇩🇪 DE | 3223 |
| 7 | 🇮🇹 IT | 3197 |
| 8 | 🇯🇵 JP | 3157 |
| 9 | 🇨🇦 CA | 2882 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2474 |
| 12 | 🇫🇷 FR | 2312 |
| 13 | 🇲🇽 MX | 1837 |
| 14 | 🇬🇷 GR | 1738 |
| 15 | 🇨🇭 CH | 1641 |
| 16 | 🇳🇴 NO | 1582 |
| 17 | 🇲🇾 MY | 1382 |
| 18 | 🇿🇦 ZA | 1190 |
| 19 | 🇳🇿 NZ | 1092 |
| 20 | 🇹🇷 TR | 1061 |
| 21 | 🇹🇭 TH | 1056 |
| 22 | 🇵🇭 PH | 984 |
| 23 | 🇵🇱 PL | 943 |
| 24 | 🇰🇷 KR | 926 |
| 25 | 🇬🇹 GT | 856 |
| 26 | 🇲🇦 MA | 739 |
| 27 | 🇲🇪 ME | 633 |
| 28 | 🇲🇴 MO | 628 |
| 29 | 🇳🇱 NL | 609 |
| 30 | 🇮🇩 ID | 502 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1315 |
| 2 | Tokyo International Airport |  | JP | 1073 |
| 3 | Denver International Airport |  | US | 973 |
| 4 | Indira Gandhi International Airport |  | IN | 885 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 855 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 741 |
| 9 | Frankfurt am Main International Airport |  | DE | 727 |
| 10 | Zurich Airport |  | CH | 705 |
| 11 | La Aurora Airport |  | GT | 646 |
| 12 | Macau International Airport |  | MO | 628 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 575 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Kuala Lumpur International Airport |  | MY | 545 |
| 16 | Madrid Barajas International Airport |  | ES | 542 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 535 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 513 |
| 19 | Malpensa International Airport |  | IT | 505 |
| 20 | Bengaluru International Airport |  | IN | 504 |
| 21 | Congonhas Airport |  | BR | 478 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 453 |
| 25 | Charles de Gaulle International Airport |  | FR | 451 |
| 26 | Salt Lake City International Airport |  | US | 449 |
| 27 | Capua Airport |  | IT | 443 |
| 28 | Daniel K Inouye International Airport |  | US | 429 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 425 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 418 |
| 31 | Barcelona International Airport |  | ES | 396 |
| 32 | Vitoria/Foronda Airport |  | ES | 394 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 386 |
| 35 | O. R. Tambo International Airport |  | ZA | 379 |
| 36 | Reno/Tahoe International Airport |  | US | 374 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 371 |
| 38 | Don Mueang International Airport |  | TH | 359 |
| 39 | Amsterdam Airport Schiphol |  | NL | 353 |
| 40 | Calgary International Airport |  | CA | 344 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 188 | 21m | 244 km | 791.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 183 | 24m | 225 km | 710.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 171 | 1h 27m | 910 km | 2,683.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 141 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 132 | 26m | 275 km | 625.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 120 | 1h 12m | 770 km | 1,594.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 93 | 20m | 250 km | 401.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL1607 | United Airlines | Indianapolis International Airport (KIND) | Denver International Airport (KDEN) | 2026-04-28 13:03 UTC | 2026-04-28 15:28 UTC | 2h 25m |
| WZZ907 | Wizz Air | Tallinn Airport (EETN) | Giżycko-Mazury Residence (EPGM) | 2026-04-28 14:37 UTC | 2026-04-28 15:27 UTC | 50m |
| N738WC |  | Treasure Coast Airpark (FL37) | Immokalee Regional Airport (KIMM) | 2026-04-28 14:38 UTC | 2026-04-28 15:23 UTC | 44m |
|  |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-04-28 15:00 UTC | 2026-04-28 15:19 UTC | 18m |
| XBSKT | XBS | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-04-28 14:50 UTC | 2026-04-28 15:18 UTC | 27m |
| N458AM |  | 4IS1 (4IS1) | Frasca Field (KC16) | 2026-04-28 15:03 UTC | 2026-04-28 15:17 UTC | 13m |
| N742CF |  | Mc Clellan-Palomar Airport (KCRQ) | Big Bear City Airport (KL35) | 2026-04-28 14:50 UTC | 2026-04-28 15:16 UTC | 26m |
| ERU64 | ERU | 42AZ (42AZ) | 42AZ (42AZ) | 2026-04-28 15:02 UTC | 2026-04-28 15:12 UTC | 10m |
| DILIA | DIL | Rostock-Laage Airport (ETNL) | Siegerland Airport (EDGS) | 2026-04-28 14:18 UTC | 2026-04-28 15:11 UTC | 53m |
| CGHAP | CGH | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-04-28 14:39 UTC | 2026-04-28 15:10 UTC | 30m |
| N428MG |  | Middle Georgia Regional Airport (KMCN) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-28 14:14 UTC | 2026-04-28 15:07 UTC | 53m |
| N24BQ |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-28 14:48 UTC | 2026-04-28 15:06 UTC | 18m |
| CXK416 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-04-28 14:34 UTC | 2026-04-28 15:05 UTC | 30m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Trenton-Robbinsville Airport (KN87) | 2026-04-28 14:40 UTC | 2026-04-28 15:04 UTC | 24m |
| SAMU42 | SAM | Roanne-Renaison Airport (LFLO) | Saint-Etienne-Boutheon Airport (LFMH) | 2026-04-28 14:48 UTC | 2026-04-28 15:03 UTC | 14m |
| 166514 |  | Pinon Canyon Airport (0CD5) | Pinon Canyon Airport (0CD5) | 2026-04-28 14:25 UTC | 2026-04-28 15:02 UTC | 36m |
| N997DJ |  | Ted Stevens Anchorage International Airport (PANC) | Bear Creek 1 Airport (AK02) | 2026-04-28 13:38 UTC | 2026-04-28 15:01 UTC | 1h 23m |
| N150RC |  | Barrow County Airport (KWDR) | Pensacola International Airport (KPNS) | 2026-04-28 14:04 UTC | 2026-04-28 14:59 UTC | 55m |
| EJM790 | EJM | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-28 14:43 UTC | 2026-04-28 14:58 UTC | 14m |
| BPX291 | BPX | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-28 14:20 UTC | 2026-04-28 14:57 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
