# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_22:20:03_UTC-green)

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

**Latest saved flight:** 2026-04-30 22:20:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 22:20:03 UTC

- **61,269** saved flights
- **23,596** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,269** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **746,195.6 tonnes** estimated CO2 emissions
- **43,257,717 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2582 |
| 2 | SkyWest Airlines | 2286 |
| 3 | IndiGo | 1400 |
| 4 | EJA | 1108 |
| 5 | American Airlines | 957 |
| 6 | Southwest Airlines | 868 |
| 7 | Lufthansa | 779 |
| 8 | ENY | 758 |
| 9 | Vueling | 607 |
| 10 | AXM | 595 |
| 11 | LATAM Airlines | 583 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 511 |
| 15 | AZU | 499 |
| 16 | QLK | 479 |
| 17 | Swiss International | 479 |
| 18 | LXJ | 437 |
| 19 | Alaska Airlines | 418 |
| 20 | AEE | 403 |
| 21 | easyJet | 400 |
| 22 | EJU | 394 |
| 23 | VIV | 387 |
| 24 | Cathay Pacific | 369 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 335 |
| 28 | AIQ | 311 |
| 29 | CXK | 305 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48538 |
| 2 | 🇪🇸 ES | 4430 |
| 3 | 🇮🇳 IN | 4421 |
| 4 | 🇦🇺 AU | 4157 |
| 5 | 🇧🇷 BR | 3479 |
| 6 | 🇩🇪 DE | 3401 |
| 7 | 🇮🇹 IT | 3345 |
| 8 | 🇯🇵 JP | 3317 |
| 9 | 🇨🇦 CA | 3028 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2601 |
| 12 | 🇫🇷 FR | 2410 |
| 13 | 🇲🇽 MX | 1929 |
| 14 | 🇬🇷 GR | 1821 |
| 15 | 🇨🇭 CH | 1711 |
| 16 | 🇳🇴 NO | 1696 |
| 17 | 🇲🇾 MY | 1447 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1153 |
| 20 | 🇹🇭 TH | 1104 |
| 21 | 🇹🇷 TR | 1088 |
| 22 | 🇵🇭 PH | 1029 |
| 23 | 🇵🇱 PL | 989 |
| 24 | 🇰🇷 KR | 986 |
| 25 | 🇬🇹 GT | 917 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 682 |
| 28 | 🇲🇪 ME | 669 |
| 29 | 🇳🇱 NL | 643 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1359 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1021 |
| 4 | Indira Gandhi International Airport |  | IN | 934 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 895 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 779 |
| 9 | Frankfurt am Main International Airport |  | DE | 774 |
| 10 | Zurich Airport |  | CH | 734 |
| 11 | La Aurora Airport |  | GT | 688 |
| 12 | Macau International Airport |  | MO | 682 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 606 |
| 14 | Chicago O'Hare International Airport |  | US | 578 |
| 15 | Madrid Barajas International Airport |  | ES | 572 |
| 16 | Kuala Lumpur International Airport |  | MY | 570 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 557 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Malpensa International Airport |  | IT | 532 |
| 20 | Bengaluru International Airport |  | IN | 530 |
| 21 | Congonhas Airport |  | BR | 502 |
| 22 | Charlotte/Douglas International Airport |  | US | 488 |
| 23 | Salt Lake City International Airport |  | US | 478 |
| 24 | Charles de Gaulle International Airport |  | FR | 476 |
| 25 | Tenerife Norte Airport |  | ES | 474 |
| 26 | Ninoy Aquino International Airport |  | PH | 470 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 455 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 443 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 441 |
| 31 | Barcelona International Airport |  | ES | 413 |
| 32 | Vitoria/Foronda Airport |  | ES | 411 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 406 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 401 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 387 |
| 37 | Reno/Tahoe International Airport |  | US | 386 |
| 38 | Don Mueang International Airport |  | TH | 379 |
| 39 | Amsterdam Airport Schiphol |  | NL | 378 |
| 40 | Calgary International Airport |  | CA | 360 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 337 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 204 | 21m | 244 km | 859.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 179 | 1h 27m | 910 km | 2,808.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 150 | 19m | 165 km | 426.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 148 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 107 | 20m | 99 km | 183.3 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 103 | 31m | 369 km | 655.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 78 | 14m | 154 km | 206.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGR449 | CGR | Fernando Air Base (RPUL) | Calapan Airport (RPUK) | 2026-04-30 21:53 UTC | 2026-04-30 22:20 UTC | 27m |
| N68310 |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-04-30 21:47 UTC | 2026-04-30 22:16 UTC | 28m |
| BLADE20 | BLA | Fairchild Afb Airport (KSKA) | Fairchild Afb Airport (KSKA) | 2026-04-30 22:00 UTC | 2026-04-30 22:13 UTC | 13m |
| N12834 |  | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-04-30 21:56 UTC | 2026-04-30 22:09 UTC | 12m |
| N100MU |  | Tulsa International Airport (KTUL) | Double W Airport (3OK7) | 2026-04-30 21:43 UTC | 2026-04-30 22:07 UTC | 23m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-30 14:22 UTC | 2026-04-30 22:05 UTC | 7h 42m |
| N497PJ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-04-30 21:21 UTC | 2026-04-30 22:04 UTC | 43m |
| CXK482 | CXK | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-30 21:49 UTC | 2026-04-30 22:04 UTC | 14m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-30 10:48 UTC | 2026-04-30 22:01 UTC | 11h 12m |
| LS01 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-30 21:08 UTC | 2026-04-30 22:00 UTC | 51m |
| SCA1 | SCA | Prescott Regional/Ernest A Love Field (KPRC) | 20AZ (20AZ) | 2026-04-30 21:17 UTC | 2026-04-30 21:59 UTC | 41m |
| N65JA |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-04-30 21:37 UTC | 2026-04-30 21:58 UTC | 20m |
| N191VF |  | Trenton Mercer Airport (KTTN) | AL40 (AL40) | 2026-04-30 19:44 UTC | 2026-04-30 21:58 UTC | 2h 13m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-30 10:42 UTC | 2026-04-30 21:53 UTC | 11h 10m |
| N7931N |  | Grayhill Airport (GA98) | Auburn University Regional Airport (KAUO) | 2026-04-30 21:32 UTC | 2026-04-30 21:53 UTC | 21m |
| N404LR |  | St Augustine Airport (KSGJ) | William B Greene Jr Regional Airport (K0A9) | 2026-04-30 20:51 UTC | 2026-04-30 21:52 UTC | 1h 0m |
| N882CT |  | Auburn Municipal Airport (KAUN) | San Carlos Airport (KSQL) | 2026-04-30 21:08 UTC | 2026-04-30 21:51 UTC | 42m |
| SRN6261 | SRN | Mollis Airport (LSZM) | Cologne Bonn Airport (EDDK) | 2026-04-30 20:39 UTC | 2026-04-30 21:49 UTC | 1h 9m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-30 17:37 UTC | 2026-04-30 21:49 UTC | 4h 11m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-30 20:59 UTC | 2026-04-30 21:48 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
