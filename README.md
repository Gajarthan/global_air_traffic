# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_21:39:30_UTC-green)

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

**Latest saved flight:** 2026-04-26 21:39:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 21:39:30 UTC

- **56,107** saved flights
- **22,053** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,107** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **678,844.0 tonnes** estimated CO2 emissions
- **39,353,277 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2389 |
| 2 | SkyWest Airlines | 2122 |
| 3 | IndiGo | 1275 |
| 4 | EJA | 1007 |
| 5 | American Airlines | 896 |
| 6 | Southwest Airlines | 798 |
| 7 | ENY | 706 |
| 8 | Lufthansa | 691 |
| 9 | Vueling | 566 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 544 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 473 |
| 14 | WIF | 466 |
| 15 | Delta Air Lines | 461 |
| 16 | Swiss International | 439 |
| 17 | QLK | 430 |
| 18 | LXJ | 400 |
| 19 | Alaska Airlines | 374 |
| 20 | AEE | 371 |
| 21 | EJU | 361 |
| 22 | VIV | 358 |
| 23 | easyJet | 357 |
| 24 | Air France | 327 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 318 |
| 27 | AXB | 305 |
| 28 | JetBlue | 286 |
| 29 | GLO | 285 |
| 30 | United Airlines | 284 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44498 |
| 2 | 🇪🇸 ES | 4113 |
| 3 | 🇮🇳 IN | 4025 |
| 4 | 🇦🇺 AU | 3730 |
| 5 | 🇧🇷 BR | 3245 |
| 6 | 🇩🇪 DE | 3066 |
| 7 | 🇮🇹 IT | 3063 |
| 8 | 🇯🇵 JP | 2993 |
| 9 | 🇨🇦 CA | 2775 |
| 10 | 🇨🇴 CO | 2535 |
| 11 | 🇬🇧 GB | 2362 |
| 12 | 🇫🇷 FR | 2211 |
| 13 | 🇲🇽 MX | 1781 |
| 14 | 🇬🇷 GR | 1666 |
| 15 | 🇨🇭 CH | 1586 |
| 16 | 🇳🇴 NO | 1506 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1151 |
| 19 | 🇳🇿 NZ | 1047 |
| 20 | 🇹🇷 TR | 1027 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 907 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 836 |
| 26 | 🇲🇦 MA | 713 |
| 27 | 🇲🇪 ME | 610 |
| 28 | 🇳🇱 NL | 587 |
| 29 | 🇲🇴 MO | 578 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1276 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 932 |
| 4 | El Dorado International Airport |  | CO | 853 |
| 5 | Indira Gandhi International Airport |  | IN | 853 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 820 |
| 7 | Guaymaral Airport |  | CO | 775 |
| 8 | Harry Reid International Airport |  | US | 714 |
| 9 | Frankfurt am Main International Airport |  | DE | 677 |
| 10 | Zurich Airport |  | CH | 673 |
| 11 | La Aurora Airport |  | GT | 628 |
| 12 | Macau International Airport |  | MO | 578 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 559 |
| 14 | Chicago O'Hare International Airport |  | US | 546 |
| 15 | Madrid Barajas International Airport |  | ES | 527 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 523 |
| 17 | Kuala Lumpur International Airport |  | MY | 523 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 486 |
| 20 | Bengaluru International Airport |  | IN | 479 |
| 21 | Congonhas Airport |  | BR | 467 |
| 22 | Charlotte/Douglas International Airport |  | US | 453 |
| 23 | Tenerife Norte Airport |  | ES | 451 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 431 |
| 26 | Salt Lake City International Airport |  | US | 428 |
| 27 | Capua Airport |  | IT | 417 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 414 |
| 29 | Daniel K Inouye International Airport |  | US | 412 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 402 |
| 31 | Barcelona International Airport |  | ES | 386 |
| 32 | Vitoria/Foronda Airport |  | ES | 384 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 379 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 373 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 367 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 360 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 334 |
| 40 | Amsterdam Airport Schiphol |  | NL | 334 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 316 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 206 | 14m | 114 km | 404.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 178 | 21m | 244 km | 749.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 134 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 80 | 1h 1m | 695 km | 959.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 53m | 1,304 km | 1,709.8 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 74 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA875 | Cathay Pacific | Dallas-Fort Worth International Airport (KDFW) | Macau International Airport (VMMC) | 2026-04-26 06:32 UTC | 2026-04-26 21:39 UTC | 15h 6m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-26 17:12 UTC | 2026-04-26 21:38 UTC | 4h 26m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-04-26 10:37 UTC | 2026-04-26 21:35 UTC | 10h 58m |
| CAP416 | CAP | Riverside Airport (KRAL) | Hemet-Ryan Airport (KHMT) | 2026-04-26 20:52 UTC | 2026-04-26 21:31 UTC | 39m |
| AJD013X | AJD | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-04-26 10:11 UTC | 2026-04-26 21:24 UTC | 11h 12m |
| CPA640 | Cathay Pacific | Langtang Airport (VNLT) | Macau International Airport (VMMC) | 2026-04-26 17:58 UTC | 2026-04-26 21:23 UTC | 3h 24m |
| N3946M |  | Candy Lake Estate Airport (98OK) | Tulsa International Airport (KTUL) | 2026-04-26 21:04 UTC | 2026-04-26 21:20 UTC | 16m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-04-26 20:55 UTC | 2026-04-26 21:18 UTC | 22m |
| EJA567 | EJA | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-04-26 20:20 UTC | 2026-04-26 21:08 UTC | 48m |
| N411FA |  | Fullerton Municipal Airport (KFUL) | Fullerton Municipal Airport (KFUL) | 2026-04-26 20:56 UTC | 2026-04-26 21:07 UTC | 11m |
| N7334F |  | Georgetown-Scott County Regional Airport (K27K) | Capital City Airport (KFFT) | 2026-04-26 20:29 UTC | 2026-04-26 21:04 UTC | 35m |
| N686MJ |  | Pike County/Hatcher Field (KPBX) | 57KY (57KY) | 2026-04-26 20:49 UTC | 2026-04-26 21:02 UTC | 12m |
| N553RA |  | 5TS4 (5TS4) | Decatur Municipal Airport (KLUD) | 2026-04-26 20:59 UTC | 2026-04-26 21:01 UTC | 1m |
| N99FD |  | Boise Air Trml/Gowen Field (KBOI) | High Valley Airport (ID35) | 2026-04-26 20:43 UTC | 2026-04-26 20:58 UTC | 14m |
| N73910 |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-04-26 20:54 UTC | 2026-04-26 20:57 UTC | 3m |
| N107PT |  | Napa County Airport (KAPC) | Lake Tahoe Airport (KTVL) | 2026-04-26 20:11 UTC | 2026-04-26 20:54 UTC | 43m |
| N9452B |  | CA54 (CA54) | CA54 (CA54) | 2026-04-26 20:21 UTC | 2026-04-26 20:54 UTC | 33m |
| SWA456 | Southwest Airlines | Long Beach (Daugherty Field) Airport (KLGB) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-26 19:52 UTC | 2026-04-26 20:54 UTC | 1h 1m |
| EJA865 | EJA | Rassawek Airstrip (78VA) | Los Banos Municipal Airport (KLSN) | 2026-04-26 15:42 UTC | 2026-04-26 20:52 UTC | 5h 10m |
| N3312G |  | Richland Airport (KRLD) | Sunnyside Municipal Airport (K1S5) | 2026-04-26 20:11 UTC | 2026-04-26 20:52 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
