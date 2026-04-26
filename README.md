# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_10:10:14_UTC-green)

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

**Latest saved flight:** 2026-04-26 10:10:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 10:10:14 UTC

- **54,986** saved flights
- **21,679** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,986** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **663,717.4 tonnes** estimated CO2 emissions
- **38,476,373 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2321 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1246 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 663 |
| 9 | Vueling | 552 |
| 10 | AXM | 535 |
| 11 | LATAM Airlines | 526 |
| 12 | All Nippon Airways | 491 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 453 |
| 15 | WIF | 451 |
| 16 | QLK | 428 |
| 17 | Swiss International | 427 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 366 |
| 21 | EJU | 355 |
| 22 | easyJet | 352 |
| 23 | VIV | 352 |
| 24 | Japan Airlines | 320 |
| 25 | Air France | 317 |
| 26 | Cathay Pacific | 309 |
| 27 | AXB | 293 |
| 28 | AIQ | 282 |
| 29 | JetBlue | 280 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43682 |
| 2 | 🇪🇸 ES | 3998 |
| 3 | 🇮🇳 IN | 3942 |
| 4 | 🇦🇺 AU | 3720 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2975 |
| 7 | 🇯🇵 JP | 2970 |
| 8 | 🇩🇪 DE | 2967 |
| 9 | 🇨🇦 CA | 2728 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2301 |
| 12 | 🇫🇷 FR | 2155 |
| 13 | 🇲🇽 MX | 1721 |
| 14 | 🇬🇷 GR | 1638 |
| 15 | 🇨🇭 CH | 1555 |
| 16 | 🇳🇴 NO | 1462 |
| 17 | 🇲🇾 MY | 1303 |
| 18 | 🇿🇦 ZA | 1133 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 999 |
| 21 | 🇹🇭 TH | 997 |
| 22 | 🇵🇭 PH | 940 |
| 23 | 🇰🇷 KR | 887 |
| 24 | 🇵🇱 PL | 884 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 696 |
| 27 | 🇲🇪 ME | 600 |
| 28 | 🇳🇱 NL | 569 |
| 29 | 🇲🇴 MO | 563 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1248 |
| 2 | Tokyo International Airport |  | JP | 1012 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 837 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 808 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Zurich Airport |  | CH | 658 |
| 10 | Frankfurt am Main International Airport |  | DE | 648 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 563 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Kuala Lumpur International Airport |  | MY | 516 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 17 | Madrid Barajas International Airport |  | ES | 508 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 489 |
| 19 | Malpensa International Airport |  | IT | 472 |
| 20 | Bengaluru International Airport |  | IN | 469 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 438 |
| 24 | Ninoy Aquino International Airport |  | PH | 433 |
| 25 | Charles de Gaulle International Airport |  | FR | 419 |
| 26 | Salt Lake City International Airport |  | US | 415 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 401 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 393 |
| 31 | Vitoria/Foronda Airport |  | ES | 378 |
| 32 | Barcelona International Airport |  | ES | 373 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 364 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 37 | O. R. Tambo International Airport |  | ZA | 354 |
| 38 | Don Mueang International Airport |  | TH | 339 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 251 | 1h 7m | 706 km | 3,055.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 159 | 1h 27m | 910 km | 2,495.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 158 | 28m | 304 km | 828.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 134 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 127 | 26m | 275 km | 601.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 107 | 1h 12m | 770 km | 1,421.4 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 94 | 31m | 369 km | 598.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 90 | 27m | 215 km | 333.3 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 72 | 58m | 493 km | 612.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-25 20:04 UTC | 2026-04-26 10:10 UTC | 14h 5m |
| SWR3HY | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-04-26 09:24 UTC | 2026-04-26 09:58 UTC | 34m |
| RYR6MF | Ryanair | Eindhoven Airport (EHEH) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-26 08:07 UTC | 2026-04-26 09:40 UTC | 1h 33m |
| ZSTKH | ZST | Fraaiuitzicht Airport (FAFU) | Rand Airport (FAGM) | 2026-04-26 09:19 UTC | 2026-04-26 09:39 UTC | 19m |
| ABY385 | ABY | Sharjah International Airport (OMSJ) | Queen Alia International Airport (OJAI) | 2026-04-26 04:28 UTC | 2026-04-26 09:38 UTC | 5h 9m |
| SWR97Q | Swiss International | Bologna / Borgo Panigale Airport (LIPE) | Zurich Airport (LSZH) | 2026-04-26 08:42 UTC | 2026-04-26 09:30 UTC | 47m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Kristiansund Airport Kvernberget (ENKB) | 2026-04-26 08:48 UTC | 2026-04-26 09:28 UTC | 39m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-26 08:55 UTC | 2026-04-26 09:28 UTC | 32m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Oyen Municipal Airport (CED3) | 2026-04-26 08:58 UTC | 2026-04-26 09:27 UTC | 29m |
| FSMT1T | FSM | Cuatro Vientos Airport (LECU) | E. Castellanos-Villacastin Airport (LEEV) | 2026-04-26 08:53 UTC | 2026-04-26 09:27 UTC | 33m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-25 21:53 UTC | 2026-04-26 09:26 UTC | 11h 33m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-26 08:57 UTC | 2026-04-26 09:23 UTC | 26m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-04-26 08:48 UTC | 2026-04-26 09:22 UTC | 33m |
| DEKLP | DEK | Husum-Schwesing Airport (EDXJ) | Husum-Schwesing Airport (EDXJ) | 2026-04-26 08:29 UTC | 2026-04-26 09:21 UTC | 52m |
| SHA943 | SHA | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-04-26 09:02 UTC | 2026-04-26 09:20 UTC | 17m |
|  |  | Ile d'Yeu Airport (LFEY) | Ile d'Yeu Airport (LFEY) | 2026-04-26 09:18 UTC | 2026-04-26 09:18 UTC | 0m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-25 22:06 UTC | 2026-04-26 09:17 UTC | 11h 10m |
| IBB55LF | IBB | Tenerife Norte Airport (GCXO) | Federico Garcia Lorca Airport (LEGR) | 2026-04-26 07:22 UTC | 2026-04-26 09:15 UTC | 1h 52m |
| VOE1ZP | VOE | Alicante International Airport (LEAL) | La Morgal Airport (LEMR) | 2026-04-26 08:04 UTC | 2026-04-26 09:10 UTC | 1h 6m |
| AEE253 | AEE | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-26 08:17 UTC | 2026-04-26 09:10 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
