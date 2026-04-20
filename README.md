# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_08:06:52_UTC-green)

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

**Latest saved flight:** 2026-04-20 08:06:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 08:06:52 UTC

- **44,662** saved flights
- **18,509** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,662** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **538,500.6 tonnes** estimated CO2 emissions
- **31,217,428 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1879 |
| 2 | SkyWest Airlines | 1741 |
| 3 | IndiGo | 1077 |
| 4 | EJA | 779 |
| 5 | American Airlines | 741 |
| 6 | Southwest Airlines | 642 |
| 7 | ENY | 584 |
| 8 | AXM | 447 |
| 9 | Vueling | 447 |
| 10 | LATAM Airlines | 446 |
| 11 | Lufthansa | 444 |
| 12 | All Nippon Airways | 402 |
| 13 | AZU | 389 |
| 14 | Delta Air Lines | 381 |
| 15 | QLK | 364 |
| 16 | LXJ | 354 |
| 17 | WIF | 348 |
| 18 | Swiss International | 343 |
| 19 | Alaska Airlines | 308 |
| 20 | AEE | 303 |
| 21 | EJU | 293 |
| 22 | VIV | 285 |
| 23 | easyJet | 284 |
| 24 | Japan Airlines | 273 |
| 25 | Air France | 251 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 237 |
| 28 | AXB | 234 |
| 29 | GLO | 234 |
| 30 | Cathay Pacific | 228 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35421 |
| 2 | 🇮🇳 IN | 3327 |
| 3 | 🇪🇸 ES | 3273 |
| 4 | 🇦🇺 AU | 3112 |
| 5 | 🇧🇷 BR | 2664 |
| 6 | 🇯🇵 JP | 2454 |
| 7 | 🇮🇹 IT | 2370 |
| 8 | 🇩🇪 DE | 2257 |
| 9 | 🇨🇦 CA | 2175 |
| 10 | 🇨🇴 CO | 2057 |
| 11 | 🇬🇧 GB | 1802 |
| 12 | 🇫🇷 FR | 1688 |
| 13 | 🇲🇽 MX | 1398 |
| 14 | 🇬🇷 GR | 1375 |
| 15 | 🇨🇭 CH | 1210 |
| 16 | 🇳🇴 NO | 1106 |
| 17 | 🇲🇾 MY | 1097 |
| 18 | 🇿🇦 ZA | 921 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇵🇭 PH | 805 |
| 21 | 🇹🇭 TH | 799 |
| 22 | 🇹🇷 TR | 787 |
| 23 | 🇰🇷 KR | 738 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 707 |
| 26 | 🇲🇦 MA | 551 |
| 27 | 🇲🇪 ME | 471 |
| 28 | 🇳🇱 NL | 454 |
| 29 | 🇲🇴 MO | 413 |
| 30 | 🇧🇸 BS | 411 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1051 |
| 2 | Tokyo International Airport |  | JP | 837 |
| 3 | Denver International Airport |  | US | 751 |
| 4 | El Dorado International Airport |  | CO | 719 |
| 5 | Indira Gandhi International Airport |  | IN | 719 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 683 |
| 7 | Harry Reid International Airport |  | US | 580 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 541 |
| 10 | Zurich Airport |  | CH | 532 |
| 11 | Chicago O'Hare International Airport |  | US | 442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 441 |
| 13 | Kuala Lumpur International Airport |  | MY | 436 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 433 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 420 |
| 16 | Frankfurt am Main International Airport |  | DE | 416 |
| 17 | Macau International Airport |  | MO | 413 |
| 18 | Madrid Barajas International Airport |  | ES | 397 |
| 19 | Bengaluru International Airport |  | IN | 395 |
| 20 | Tenerife Norte Airport |  | ES | 391 |
| 21 | Charlotte/Douglas International Airport |  | US | 388 |
| 22 | Congonhas Airport |  | BR | 381 |
| 23 | Malpensa International Airport |  | IT | 377 |
| 24 | Ninoy Aquino International Airport |  | PH | 373 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 338 |
| 26 | Salt Lake City International Airport |  | US | 338 |
| 27 | Daniel K Inouye International Airport |  | US | 333 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 331 |
| 29 | Charles de Gaulle International Airport |  | FR | 326 |
| 30 | Reno/Tahoe International Airport |  | US | 311 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 311 |
| 32 | Capua Airport |  | IT | 309 |
| 33 | Vitoria/Foronda Airport |  | ES | 307 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 302 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 297 |
| 36 | O. R. Tambo International Airport |  | ZA | 296 |
| 37 | Barcelona International Airport |  | ES | 289 |
| 38 | Calgary International Airport |  | CA | 273 |
| 39 | Viracopos International Airport |  | BR | 270 |
| 40 | Don Mueang International Airport |  | TH | 270 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 209 | 1h 7m | 706 km | 2,544.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 135 | 28m | 304 km | 707.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 127 | 21m | 244 km | 534.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 120 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 119 | 19m | 165 km | 338.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 97 | 54m | 546 km | 913.3 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 92 | 44m | 452 km | 717.0 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 73 | 20m | 250 km | 315.3 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 72 | 52m | 556 km | 690.2 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 69 | 26m | 215 km | 255.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 63 | 13m | 99 km | 108.0 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 62 | 57m | 493 km | 527.5 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 61 | 1h 0m | 695 km | 731.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ANA185 | All Nippon Airways | Daniel K Inouye International Airport (PHNL) | Tokyo International Airport (RJTT) | 2026-04-19 23:37 UTC | 2026-04-20 08:06 UTC | 8h 29m |
| DLH1YN | Lufthansa | Munich International Airport (EDDM) | Václav Havel Airport (LKPR) | 2026-04-20 06:35 UTC | 2026-04-20 08:00 UTC | 1h 24m |
| ESPKY | ESP | Tallinn Airport (EETN) | Johvi Airfield (EEJI) | 2026-04-20 07:28 UTC | 2026-04-20 07:56 UTC | 27m |
| LSI191 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-19 20:54 UTC | 2026-04-20 07:56 UTC | 11h 1m |
| ATG7619 | ATG | Henri Coanda International Airport (LROP) | Zhuhai Airport (ZGSD) | 2026-04-19 20:03 UTC | 2026-04-20 07:54 UTC | 11h 51m |
| CLX4327 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-19 20:59 UTC | 2026-04-20 07:54 UTC | 10h 54m |
| PBD466 | PBD | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-20 07:49 UTC | 2026-04-20 07:52 UTC | 3m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-04-19 20:20 UTC | 2026-04-20 07:51 UTC | 11h 30m |
| LTR742 | LTR | Svalbard Airport Longyear (ENSB) | Ny-Ålesund Airport Hamnerabben (ENAS) | 2026-04-20 07:38 UTC | 2026-04-20 07:50 UTC | 11m |
| HBZUR | HBZ | Ambri Airport (LSPM) | LSMF (LSMF) | 2026-04-20 07:06 UTC | 2026-04-20 07:46 UTC | 40m |
| FHRSJ | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-20 07:24 UTC | 2026-04-20 07:43 UTC | 19m |
| RUK7NA | RUK | Belfast International Airport (EGAA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-20 04:58 UTC | 2026-04-20 07:30 UTC | 2h 31m |
| RYR2LT | Ryanair | Poznań-Ławica Airport (EPPO) | Poznań-Ławica Airport (EPPO) | 2026-04-20 04:14 UTC | 2026-04-20 07:25 UTC | 3h 11m |
| N429CF |  | Dallas Executive Airport (KRBD) | Mid-Way Regional Airport (KJWY) | 2026-04-20 07:12 UTC | 2026-04-20 07:24 UTC | 12m |
| EWG8M | EWG | Stuttgart Airport (EDDS) | Hamburg Airport (EDDH) | 2026-04-20 06:25 UTC | 2026-04-20 07:20 UTC | 54m |
| ECC282 | ECC | Antwerp International Airport (Deurne) (EBAW) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-04-20 06:07 UTC | 2026-04-20 07:19 UTC | 1h 11m |
| SWR42B | Swiss International | Zurich Airport (LSZH) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-20 06:24 UTC | 2026-04-20 07:18 UTC | 54m |
| AUA271 | Austrian Airlines | Vienna International Airport (LOWW) | Hannover Airport (EDDV) | 2026-04-20 06:12 UTC | 2026-04-20 07:18 UTC | 1h 6m |
| OAL063 | OAL | Paros Airport (LGPA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-20 06:41 UTC | 2026-04-20 07:16 UTC | 35m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-20 07:02 UTC | 2026-04-20 07:15 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
