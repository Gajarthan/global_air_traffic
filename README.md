# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_21:17:46_UTC-green)

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

**Latest saved flight:** 2026-04-30 21:17:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 21:17:46 UTC

- **61,128** saved flights
- **23,542** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,128** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **744,397.1 tonnes** estimated CO2 emissions
- **43,153,453 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2581 |
| 2 | SkyWest Airlines | 2279 |
| 3 | IndiGo | 1400 |
| 4 | EJA | 1104 |
| 5 | American Airlines | 954 |
| 6 | Southwest Airlines | 867 |
| 7 | Lufthansa | 779 |
| 8 | ENY | 757 |
| 9 | Vueling | 607 |
| 10 | AXM | 595 |
| 11 | LATAM Airlines | 583 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 509 |
| 15 | AZU | 499 |
| 16 | Swiss International | 479 |
| 17 | QLK | 478 |
| 18 | LXJ | 435 |
| 19 | Alaska Airlines | 418 |
| 20 | AEE | 403 |
| 21 | easyJet | 400 |
| 22 | EJU | 393 |
| 23 | VIV | 384 |
| 24 | Cathay Pacific | 363 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 335 |
| 28 | AIQ | 311 |
| 29 | CXK | 302 |
| 30 | United Airlines | 302 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48363 |
| 2 | 🇪🇸 ES | 4429 |
| 3 | 🇮🇳 IN | 4420 |
| 4 | 🇦🇺 AU | 4149 |
| 5 | 🇧🇷 BR | 3477 |
| 6 | 🇩🇪 DE | 3399 |
| 7 | 🇮🇹 IT | 3342 |
| 8 | 🇯🇵 JP | 3315 |
| 9 | 🇨🇦 CA | 3016 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2600 |
| 12 | 🇫🇷 FR | 2409 |
| 13 | 🇲🇽 MX | 1918 |
| 14 | 🇬🇷 GR | 1820 |
| 15 | 🇨🇭 CH | 1710 |
| 16 | 🇳🇴 NO | 1696 |
| 17 | 🇲🇾 MY | 1447 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1141 |
| 20 | 🇹🇭 TH | 1104 |
| 21 | 🇹🇷 TR | 1087 |
| 22 | 🇵🇭 PH | 1025 |
| 23 | 🇵🇱 PL | 989 |
| 24 | 🇰🇷 KR | 985 |
| 25 | 🇬🇹 GT | 908 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 677 |
| 28 | 🇲🇪 ME | 669 |
| 29 | 🇳🇱 NL | 642 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1354 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1018 |
| 4 | Indira Gandhi International Airport |  | IN | 933 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 895 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 775 |
| 9 | Frankfurt am Main International Airport |  | DE | 774 |
| 10 | Zurich Airport |  | CH | 734 |
| 11 | La Aurora Airport |  | GT | 681 |
| 12 | Macau International Airport |  | MO | 677 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 605 |
| 14 | Chicago O'Hare International Airport |  | US | 577 |
| 15 | Madrid Barajas International Airport |  | ES | 571 |
| 16 | Kuala Lumpur International Airport |  | MY | 570 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 556 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Malpensa International Airport |  | IT | 531 |
| 20 | Bengaluru International Airport |  | IN | 530 |
| 21 | Congonhas Airport |  | BR | 502 |
| 22 | Charlotte/Douglas International Airport |  | US | 488 |
| 23 | Salt Lake City International Airport |  | US | 475 |
| 24 | Charles de Gaulle International Airport |  | FR | 475 |
| 25 | Tenerife Norte Airport |  | ES | 474 |
| 26 | Ninoy Aquino International Airport |  | PH | 469 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 455 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 443 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 438 |
| 31 | Barcelona International Airport |  | ES | 413 |
| 32 | Vitoria/Foronda Airport |  | ES | 411 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 406 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 401 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 387 |
| 37 | Reno/Tahoe International Airport |  | US | 386 |
| 38 | Don Mueang International Airport |  | TH | 379 |
| 39 | Amsterdam Airport Schiphol |  | NL | 377 |
| 40 | Calgary International Airport |  | CA | 359 |

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
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 146 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 107 | 20m | 99 km | 183.3 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 102 | 31m | 369 km | 649.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 91 | 28m | 152 km | 237.8 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 53m | 1,304 km | 1,844.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 78 | 14m | 154 km | 206.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-30 10:06 UTC | 2026-04-30 21:17 UTC | 11h 10m |
| N6411J |  | Angwin-Parrett Field (K2O3) | Angwin-Parrett Field (K2O3) | 2026-04-30 20:56 UTC | 2026-04-30 21:17 UTC | 20m |
| CXK700 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-30 20:32 UTC | 2026-04-30 21:16 UTC | 44m |
| N2087E |  | San Gabriel Valley Airport (KEMT) | Brackett Field (KPOC) | 2026-04-30 20:53 UTC | 2026-04-30 21:04 UTC | 10m |
| N497PJ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-04-30 20:46 UTC | 2026-04-30 21:03 UTC | 17m |
| N490LP |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-30 19:49 UTC | 2026-04-30 20:58 UTC | 1h 8m |
| N506DS |  | Auburn Municipal Airport (KAUN) | Lincoln Regional/Karl Harder Field (KLHM) | 2026-04-30 19:50 UTC | 2026-04-30 20:58 UTC | 1h 8m |
| N482EC |  | Porter County Regional Airport (KVPZ) | Auburn University Regional Airport (KAUO) | 2026-04-30 19:33 UTC | 2026-04-30 20:55 UTC | 1h 22m |
| N160RW |  | CA13 (CA13) | Lake Tahoe Airport (KTVL) | 2026-04-30 20:18 UTC | 2026-04-30 20:51 UTC | 33m |
| N171FR |  | Westchester County Airport (KHPN) | Lancaster Airport (KLNS) | 2026-04-30 19:55 UTC | 2026-04-30 20:51 UTC | 56m |
| N5125B |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-30 20:18 UTC | 2026-04-30 20:47 UTC | 29m |
| N446BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-04-30 20:22 UTC | 2026-04-30 20:46 UTC | 24m |
| N282MM |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-30 20:37 UTC | 2026-04-30 20:45 UTC | 8m |
| N3515S |  | Corona Municipal Airport (KAJO) | Riverside Airport (KRAL) | 2026-04-30 20:18 UTC | 2026-04-30 20:43 UTC | 25m |
| N605VA |  | K4A7 (K4A7) | K4A7 (K4A7) | 2026-04-30 20:07 UTC | 2026-04-30 20:42 UTC | 35m |
| NUS531 | NUS | Glendale Regional Airport (KGEU) | Robert Sibley Airport (KSZY) | 2026-04-30 18:16 UTC | 2026-04-30 20:42 UTC | 2h 25m |
| AFL1195 | AFL | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-30 20:42 UTC | 2026-04-30 20:42 UTC | 0m |
| SYS114 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-04-30 20:23 UTC | 2026-04-30 20:41 UTC | 17m |
| N871DG |  | Modesto City-County-Harry Sham Field (KMOD) | Palo Alto Airport (KPAO) | 2026-04-30 20:19 UTC | 2026-04-30 20:40 UTC | 20m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-30 20:28 UTC | 2026-04-30 20:38 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
