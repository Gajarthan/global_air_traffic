# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_08:35:18_UTC-green)

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

**Latest saved flight:** 2026-04-30 08:35:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 08:35:18 UTC

- **60,272** saved flights
- **23,265** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,272** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **734,794.7 tonnes** estimated CO2 emissions
- **42,596,796 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2559 |
| 2 | SkyWest Airlines | 2253 |
| 3 | IndiGo | 1386 |
| 4 | EJA | 1082 |
| 5 | American Airlines | 941 |
| 6 | Southwest Airlines | 854 |
| 7 | Lufthansa | 763 |
| 8 | ENY | 748 |
| 9 | Vueling | 599 |
| 10 | AXM | 588 |
| 11 | LATAM Airlines | 575 |
| 12 | All Nippon Airways | 535 |
| 13 | WIF | 506 |
| 14 | Delta Air Lines | 503 |
| 15 | AZU | 493 |
| 16 | QLK | 477 |
| 17 | Swiss International | 476 |
| 18 | LXJ | 428 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 400 |
| 21 | easyJet | 396 |
| 22 | EJU | 390 |
| 23 | VIV | 379 |
| 24 | Cathay Pacific | 361 |
| 25 | Air France | 355 |
| 26 | Japan Airlines | 354 |
| 27 | AXB | 331 |
| 28 | AIQ | 305 |
| 29 | JetBlue | 300 |
| 30 | United Airlines | 299 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47655 |
| 2 | 🇮🇳 IN | 4381 |
| 3 | 🇪🇸 ES | 4358 |
| 4 | 🇦🇺 AU | 4141 |
| 5 | 🇧🇷 BR | 3404 |
| 6 | 🇩🇪 DE | 3345 |
| 7 | 🇮🇹 IT | 3305 |
| 8 | 🇯🇵 JP | 3298 |
| 9 | 🇨🇦 CA | 2984 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2544 |
| 12 | 🇫🇷 FR | 2374 |
| 13 | 🇲🇽 MX | 1886 |
| 14 | 🇬🇷 GR | 1804 |
| 15 | 🇨🇭 CH | 1679 |
| 16 | 🇳🇴 NO | 1648 |
| 17 | 🇲🇾 MY | 1429 |
| 18 | 🇿🇦 ZA | 1222 |
| 19 | 🇳🇿 NZ | 1137 |
| 20 | 🇹🇭 TH | 1087 |
| 21 | 🇹🇷 TR | 1077 |
| 22 | 🇵🇭 PH | 1019 |
| 23 | 🇰🇷 KR | 975 |
| 24 | 🇵🇱 PL | 972 |
| 25 | 🇬🇹 GT | 876 |
| 26 | 🇲🇦 MA | 750 |
| 27 | 🇲🇴 MO | 671 |
| 28 | 🇲🇪 ME | 658 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇮🇩 ID | 516 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1339 |
| 2 | Tokyo International Airport |  | JP | 1115 |
| 3 | Denver International Airport |  | US | 1005 |
| 4 | Indira Gandhi International Airport |  | IN | 924 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 888 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 765 |
| 9 | Frankfurt am Main International Airport |  | DE | 757 |
| 10 | Zurich Airport |  | CH | 726 |
| 11 | Macau International Airport |  | MO | 671 |
| 12 | La Aurora Airport |  | GT | 660 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 598 |
| 14 | Chicago O'Hare International Airport |  | US | 573 |
| 15 | Kuala Lumpur International Airport |  | MY | 563 |
| 16 | Madrid Barajas International Airport |  | ES | 558 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 534 |
| 19 | Malpensa International Airport |  | IT | 525 |
| 20 | Bengaluru International Airport |  | IN | 525 |
| 21 | Congonhas Airport |  | BR | 491 |
| 22 | Charlotte/Douglas International Airport |  | US | 478 |
| 23 | Salt Lake City International Airport |  | US | 468 |
| 24 | Charles de Gaulle International Airport |  | FR | 468 |
| 25 | Capua Airport |  | IT | 467 |
| 26 | Ninoy Aquino International Airport |  | PH | 466 |
| 27 | Tenerife Norte Airport |  | ES | 463 |
| 28 | Daniel K Inouye International Airport |  | US | 454 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 437 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 31 | Barcelona International Airport |  | ES | 411 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 33 | Vitoria/Foronda Airport |  | ES | 401 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 395 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 383 |
| 38 | Don Mueang International Airport |  | TH | 374 |
| 39 | Amsterdam Airport Schiphol |  | NL | 368 |
| 40 | Calgary International Airport |  | CA | 358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 254 | 1h 7m | 706 km | 3,092.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 178 | 1h 27m | 910 km | 2,793.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 173 | 28m | 304 km | 906.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 148 | 19m | 165 km | 421.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 144 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 143 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 135 | 26m | 275 km | 639.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 127 | 1h 12m | 770 km | 1,687.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 101 | 31m | 369 km | 642.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 92 | 20m | 147 km | 232.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 84 | 1h 42m | 1,156 km | 1,675.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 77 | 14m | 154 km | 204.0 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSN382 | China Southern | Brisbane International Airport (YBBN) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-04-30 00:19 UTC | 2026-04-30 08:35 UTC | 8h 15m |
| DIFLD | DIF | Wangerooge Airport (EDWG) | Wangerooge Airport (EDWG) | 2026-04-30 08:16 UTC | 2026-04-30 08:33 UTC | 17m |
| AFR57GA | Air France | Charles de Gaulle International Airport (LFPG) | Malpensa International Airport (LIMC) | 2026-04-30 07:21 UTC | 2026-04-30 08:32 UTC | 1h 11m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-04-29 21:39 UTC | 2026-04-30 08:32 UTC | 10h 52m |
| HBXCL | HBX | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-04-30 07:58 UTC | 2026-04-30 08:31 UTC | 32m |
| SQF902 | SQF | M. R. Stefanik Airport (LZIB) | Kbely Air Base (LKKB) | 2026-04-30 07:56 UTC | 2026-04-30 08:31 UTC | 35m |
| HSOMR3 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-30 08:03 UTC | 2026-04-30 08:30 UTC | 26m |
| ABB854 | ABB | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-04-29 20:53 UTC | 2026-04-30 08:25 UTC | 11h 31m |
|  |  | HAL Airport (VOBG) | HAL Airport (VOBG) | 2026-04-30 08:24 UTC | 2026-04-30 08:25 UTC | 0m |
| HAF209A | HAF | Elefsis Airport (LGEL) | Ioannina Airport (LGIO) | 2026-04-30 07:12 UTC | 2026-04-30 08:17 UTC | 1h 5m |
| ULC91 | ULC | Megeve Airport (LFHM) | St Stephan Airport (LSTS) | 2026-04-30 07:46 UTC | 2026-04-30 08:15 UTC | 29m |
| THY70 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-04-29 23:12 UTC | 2026-04-30 08:14 UTC | 9h 2m |
| AZG1922 | AZG | Frankfurt-Hahn Airport (EDFH) | Zhuhai Airport (ZGSD) | 2026-04-29 16:53 UTC | 2026-04-30 08:12 UTC | 15h 18m |
| FJW8661 | FJW | Reitz Airport (FARZ) | Heidelburg Airport (FAHG) | 2026-04-30 07:13 UTC | 2026-04-30 08:10 UTC | 56m |
| HSOPK3 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-30 07:35 UTC | 2026-04-30 08:09 UTC | 34m |
| FD619 |  | Perth Jandakot Airport (YPJT) | Wagin Airport (YWGN) | 2026-04-30 07:41 UTC | 2026-04-30 08:09 UTC | 28m |
| LNK071P | LNK | Jomo Kenyatta International Airport (HKJK) | Heidelburg Airport (FAHG) | 2026-04-30 04:06 UTC | 2026-04-30 08:08 UTC | 4h 1m |
| CSN336 | China Southern | Auckland International Airport (NZAA) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-04-29 21:23 UTC | 2026-04-30 08:05 UTC | 10h 41m |
| SFR660 | SFR | Cape Town International Airport (FACT) | Heidelburg Airport (FAHG) | 2026-04-30 04:07 UTC | 2026-04-30 08:03 UTC | 3h 55m |
| GFRGP | GFR | RAF Halton (EGWN) | Netherthorpe Airfield (EGNF) | 2026-04-30 07:32 UTC | 2026-04-30 08:02 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
