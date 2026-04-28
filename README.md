# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_11:03:48_UTC-green)

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

**Latest saved flight:** 2026-04-28 11:03:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 11:03:48 UTC

- **58,003** saved flights
- **22,605** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,003** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **705,846.4 tonnes** estimated CO2 emissions
- **40,918,635 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2465 |
| 2 | SkyWest Airlines | 2190 |
| 3 | IndiGo | 1326 |
| 4 | EJA | 1031 |
| 5 | American Airlines | 917 |
| 6 | Southwest Airlines | 831 |
| 7 | Lufthansa | 727 |
| 8 | ENY | 726 |
| 9 | Vueling | 577 |
| 10 | AXM | 566 |
| 11 | LATAM Airlines | 552 |
| 12 | All Nippon Airways | 516 |
| 13 | WIF | 485 |
| 14 | AZU | 482 |
| 15 | Delta Air Lines | 475 |
| 16 | Swiss International | 458 |
| 17 | QLK | 456 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 396 |
| 20 | AEE | 386 |
| 21 | easyJet | 383 |
| 22 | EJU | 374 |
| 23 | VIV | 369 |
| 24 | Air France | 339 |
| 25 | Cathay Pacific | 336 |
| 26 | Japan Airlines | 336 |
| 27 | AXB | 316 |
| 28 | JetBlue | 294 |
| 29 | AIQ | 293 |
| 30 | United Airlines | 290 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45888 |
| 2 | 🇪🇸 ES | 4222 |
| 3 | 🇮🇳 IN | 4173 |
| 4 | 🇦🇺 AU | 3953 |
| 5 | 🇧🇷 BR | 3296 |
| 6 | 🇩🇪 DE | 3187 |
| 7 | 🇮🇹 IT | 3172 |
| 8 | 🇯🇵 JP | 3142 |
| 9 | 🇨🇦 CA | 2862 |
| 10 | 🇨🇴 CO | 2604 |
| 11 | 🇬🇧 GB | 2460 |
| 12 | 🇫🇷 FR | 2280 |
| 13 | 🇲🇽 MX | 1829 |
| 14 | 🇬🇷 GR | 1730 |
| 15 | 🇨🇭 CH | 1629 |
| 16 | 🇳🇴 NO | 1572 |
| 17 | 🇲🇾 MY | 1374 |
| 18 | 🇿🇦 ZA | 1178 |
| 19 | 🇳🇿 NZ | 1092 |
| 20 | 🇹🇷 TR | 1057 |
| 21 | 🇹🇭 TH | 1049 |
| 22 | 🇵🇭 PH | 980 |
| 23 | 🇵🇱 PL | 934 |
| 24 | 🇰🇷 KR | 925 |
| 25 | 🇬🇹 GT | 849 |
| 26 | 🇲🇦 MA | 731 |
| 27 | 🇲🇪 ME | 629 |
| 28 | 🇲🇴 MO | 624 |
| 29 | 🇳🇱 NL | 601 |
| 30 | 🇮🇩 ID | 502 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1311 |
| 2 | Tokyo International Airport |  | JP | 1066 |
| 3 | Denver International Airport |  | US | 969 |
| 4 | Indira Gandhi International Airport |  | IN | 881 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 851 |
| 7 | Guaymaral Airport |  | CO | 800 |
| 8 | Harry Reid International Airport |  | US | 738 |
| 9 | Frankfurt am Main International Airport |  | DE | 715 |
| 10 | Zurich Airport |  | CH | 696 |
| 11 | La Aurora Airport |  | GT | 639 |
| 12 | Macau International Airport |  | MO | 624 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 575 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Madrid Barajas International Airport |  | ES | 541 |
| 16 | Kuala Lumpur International Airport |  | MY | 541 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 512 |
| 19 | Malpensa International Airport |  | IT | 502 |
| 20 | Bengaluru International Airport |  | IN | 498 |
| 21 | Congonhas Airport |  | BR | 475 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 459 |
| 24 | Ninoy Aquino International Airport |  | PH | 451 |
| 25 | Salt Lake City International Airport |  | US | 449 |
| 26 | Charles de Gaulle International Airport |  | FR | 448 |
| 27 | Capua Airport |  | IT | 440 |
| 28 | Daniel K Inouye International Airport |  | US | 429 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 424 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 416 |
| 31 | Barcelona International Airport |  | ES | 394 |
| 32 | Vitoria/Foronda Airport |  | ES | 392 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 383 |
| 35 | O. R. Tambo International Airport |  | ZA | 374 |
| 36 | Reno/Tahoe International Airport |  | US | 374 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 38 | Don Mueang International Airport |  | TH | 357 |
| 39 | Amsterdam Airport Schiphol |  | NL | 345 |
| 40 | Calgary International Airport |  | CA | 341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 188 | 21m | 244 km | 791.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 183 | 24m | 225 km | 710.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 169 | 1h 27m | 910 km | 2,652.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 144 | 19m | 165 km | 409.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 132 | 26m | 275 km | 625.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 119 | 1h 12m | 770 km | 1,580.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 91 | 20m | 250 km | 393.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 79 | 58m | 493 km | 672.1 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 75 | 1h 42m | 1,423 km | 1,840.6 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DSCO02 | DSC | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-28 10:11 UTC | 2026-04-28 11:03 UTC | 51m |
| HSORJ3 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-28 10:22 UTC | 2026-04-28 11:00 UTC | 37m |
| PANTR01 | PAN | Ovar Airport (LPOV) | Espinho Airport (LPIN) | 2026-04-28 10:37 UTC | 2026-04-28 11:00 UTC | 22m |
|  |  | Gullknapp Flpl Airport (ENGK) | Kristiansand Airport (ENCN) | 2026-04-28 09:08 UTC | 2026-04-28 10:54 UTC | 1h 45m |
| ZSSWR | ZSS | O. R. Tambo International Airport (FAOR) | Hartebeespoortdam Airport (FAHB) | 2026-04-28 10:18 UTC | 2026-04-28 10:47 UTC | 29m |
| CHX3 | CHX | Leverkusen Airport (EDKL) | Cologne Bonn Airport (EDDK) | 2026-04-28 10:34 UTC | 2026-04-28 10:44 UTC | 9m |
| SKQ78 | SKQ | Burlington/Alamance Regional Airport (KBUY) | West Virginia International Yeager Airport (KCRW) | 2026-04-28 09:42 UTC | 2026-04-28 10:32 UTC | 49m |
| N455LF |  | Reed Airport (WT24) | Ox Meadows Airport (04WA) | 2026-04-28 10:23 UTC | 2026-04-28 10:28 UTC | 5m |
| EZS25BW | EZS | Geneva Cointrin International Airport (LSGG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-04-28 09:23 UTC | 2026-04-28 10:27 UTC | 1h 3m |
| HKC393 | HKC | Budapest Ferenc Liszt International Airport (LHBP) | Zhuhai Airport (ZGSD) | 2026-04-28 00:06 UTC | 2026-04-28 10:26 UTC | 10h 20m |
| IBX65 | IBX | Matsumoto Airport (RJAF) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-28 09:44 UTC | 2026-04-28 10:25 UTC | 40m |
| DLH8VK | Lufthansa | Munich International Airport (EDDM) | Bekescsaba Glider Airport (LHBC) | 2026-04-28 09:28 UTC | 2026-04-28 10:25 UTC | 56m |
| RYR8MV | Ryanair | Ciampino Airport (LIRA) | Coventry Airport (EGBE) | 2026-04-28 07:50 UTC | 2026-04-28 10:19 UTC | 2h 28m |
| NJZ196 | NJZ | Cecil Ranch Airport (37CN) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-28 09:51 UTC | 2026-04-28 10:19 UTC | 27m |
| ROT603W | ROT | Henri Coanda International Airport (LROP) | Caransebes Airport (LRCS) | 2026-04-28 09:43 UTC | 2026-04-28 10:15 UTC | 32m |
| SXBDZ | SXB | Megara Airport (LGMG) | Tripolis Airport (LGTP) | 2026-04-28 09:51 UTC | 2026-04-28 10:14 UTC | 22m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-04-28 06:27 UTC | 2026-04-28 10:12 UTC | 3h 44m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-27 19:06 UTC | 2026-04-28 10:11 UTC | 15h 4m |
| PANTR01 | PAN | Ovar Airport (LPOV) | Ovar Airport (LPOV) | 2026-04-28 09:54 UTC | 2026-04-28 10:10 UTC | 15m |
| LOT2AT | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-28 07:51 UTC | 2026-04-28 10:07 UTC | 2h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
