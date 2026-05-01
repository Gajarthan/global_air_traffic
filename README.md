# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_17:22:40_UTC-green)

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

**Latest saved flight:** 2026-05-01 17:22:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 17:22:40 UTC

- **62,642** saved flights
- **23,994** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **62,642** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **764,336.8 tonnes** estimated CO2 emissions
- **44,309,382 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2627 |
| 2 | SkyWest Airlines | 2318 |
| 3 | IndiGo | 1434 |
| 4 | EJA | 1128 |
| 5 | American Airlines | 973 |
| 6 | Southwest Airlines | 887 |
| 7 | Lufthansa | 808 |
| 8 | ENY | 770 |
| 9 | Vueling | 614 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 589 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 531 |
| 14 | Delta Air Lines | 519 |
| 15 | AZU | 511 |
| 16 | QLK | 498 |
| 17 | Swiss International | 484 |
| 18 | LXJ | 445 |
| 19 | Alaska Airlines | 428 |
| 20 | AEE | 409 |
| 21 | easyJet | 407 |
| 22 | EJU | 402 |
| 23 | VIV | 393 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 363 |
| 27 | AXB | 347 |
| 28 | AIQ | 319 |
| 29 | CXK | 314 |
| 30 | GLO | 305 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49544 |
| 2 | 🇪🇸 ES | 4529 |
| 3 | 🇮🇳 IN | 4523 |
| 4 | 🇦🇺 AU | 4288 |
| 5 | 🇧🇷 BR | 3550 |
| 6 | 🇩🇪 DE | 3499 |
| 7 | 🇯🇵 JP | 3409 |
| 8 | 🇮🇹 IT | 3402 |
| 9 | 🇨🇦 CA | 3076 |
| 10 | 🇬🇧 GB | 2663 |
| 11 | 🇨🇴 CO | 2639 |
| 12 | 🇫🇷 FR | 2471 |
| 13 | 🇲🇽 MX | 1976 |
| 14 | 🇬🇷 GR | 1867 |
| 15 | 🇨🇭 CH | 1753 |
| 16 | 🇳🇴 NO | 1736 |
| 17 | 🇲🇾 MY | 1489 |
| 18 | 🇿🇦 ZA | 1283 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1127 |
| 21 | 🇹🇷 TR | 1106 |
| 22 | 🇵🇭 PH | 1062 |
| 23 | 🇵🇱 PL | 1013 |
| 24 | 🇰🇷 KR | 1008 |
| 25 | 🇬🇹 GT | 973 |
| 26 | 🇲🇦 MA | 767 |
| 27 | 🇲🇴 MO | 704 |
| 28 | 🇲🇪 ME | 679 |
| 29 | 🇳🇱 NL | 655 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1382 |
| 2 | Tokyo International Airport |  | JP | 1152 |
| 3 | Denver International Airport |  | US | 1032 |
| 4 | Indira Gandhi International Airport |  | IN | 950 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 912 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 834 |
| 8 | Frankfurt am Main International Airport |  | DE | 807 |
| 9 | Harry Reid International Airport |  | US | 796 |
| 10 | Zurich Airport |  | CH | 744 |
| 11 | La Aurora Airport |  | GT | 726 |
| 12 | Macau International Airport |  | MO | 704 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 617 |
| 14 | Kuala Lumpur International Airport |  | MY | 590 |
| 15 | Chicago O'Hare International Airport |  | US | 588 |
| 16 | Madrid Barajas International Airport |  | ES | 588 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 567 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 544 |
| 20 | Malpensa International Airport |  | IT | 539 |
| 21 | Congonhas Airport |  | BR | 513 |
| 22 | Charlotte/Douglas International Airport |  | US | 496 |
| 23 | Salt Lake City International Airport |  | US | 489 |
| 24 | Tenerife Norte Airport |  | ES | 486 |
| 25 | Charles de Gaulle International Airport |  | FR | 486 |
| 26 | Ninoy Aquino International Airport |  | PH | 482 |
| 27 | Capua Airport |  | IT | 468 |
| 28 | Daniel K Inouye International Airport |  | US | 463 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 456 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 450 |
| 31 | Barcelona International Airport |  | ES | 422 |
| 32 | Vitoria/Foronda Airport |  | ES | 418 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 413 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 409 |
| 35 | O. R. Tambo International Airport |  | ZA | 405 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 393 |
| 37 | Reno/Tahoe International Airport |  | US | 390 |
| 38 | Amsterdam Airport Schiphol |  | NL | 388 |
| 39 | Don Mueang International Airport |  | TH | 387 |
| 40 | Calgary International Airport |  | CA | 370 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 343 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 209 | 21m | 244 km | 880.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 155 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 113 | 21m | 99 km | 193.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 104 | 20m | 250 km | 449.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 97 | 28m | 152 km | 253.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 1m | 695 km | 1,042.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 84 | 23m | 55 km | 79.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 80 | 1h 43m | 1,423 km | 1,963.3 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EJU62XU | EJU | Capua Airport (LIAU) | Malpensa International Airport (LIMC) | 2026-05-01 16:17 UTC | 2026-05-01 17:22 UTC | 1h 5m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-01 17:04 UTC | 2026-05-01 17:19 UTC | 15m |
| OKAED | OKA | S. Darius and S. Girenas Airport (EYKS) | S. Darius and S. Girenas Airport (EYKS) | 2026-05-01 16:40 UTC | 2026-05-01 17:15 UTC | 35m |
| N456ER |  | Phyllis Field (6IL2) | Lake In The Hills Airport (K3CK) | 2026-05-01 16:38 UTC | 2026-05-01 17:14 UTC | 36m |
| N21056 |  | Chester County G O Carlson Airport (KMQS) | Harrisburg International Airport (KMDT) | 2026-05-01 16:47 UTC | 2026-05-01 17:14 UTC | 26m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-01 16:31 UTC | 2026-05-01 17:13 UTC | 41m |
| N969TT |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-05-01 16:31 UTC | 2026-05-01 17:11 UTC | 40m |
| N613LG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-01 16:17 UTC | 2026-05-01 17:08 UTC | 50m |
| N786FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-01 16:22 UTC | 2026-05-01 17:07 UTC | 45m |
| CXK468 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-05-01 15:53 UTC | 2026-05-01 17:06 UTC | 1h 13m |
| N508CP |  | KU77 (KU77) | Carbon County Regional/Buck Davis Field (KPUC) | 2026-05-01 16:53 UTC | 2026-05-01 17:05 UTC | 12m |
| N702LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Brookneal/Campbell County Airport (K0V4) | 2026-05-01 16:52 UTC | 2026-05-01 17:03 UTC | 10m |
|  |  | Mc Clellan Airfield (KMCC) | Lake Tahoe Airport (KTVL) | 2026-05-01 16:14 UTC | 2026-05-01 17:02 UTC | 48m |
| N24XZ |  | Piedmont Triad International Airport (KGSO) | Washington-Warren Airport (KOCW) | 2026-05-01 16:30 UTC | 2026-05-01 17:00 UTC | 30m |
| WAH | WAH | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-05-01 16:51 UTC | 2026-05-01 17:00 UTC | 8m |
| N28222 |  | Grand Junction Regional Airport (KGJT) | Westwater Airport (UT42) | 2026-05-01 16:24 UTC | 2026-05-01 16:59 UTC | 35m |
| N554CN |  | Durant Regional/Eaker Field (KDUA) | Mc Alester Regional Airport (KMLC) | 2026-05-01 16:41 UTC | 2026-05-01 16:55 UTC | 13m |
| CGPCW | CGP | Vancouver International Airport (CYVR) | Penticton Airport (CYYF) | 2026-05-01 16:05 UTC | 2026-05-01 16:55 UTC | 49m |
| CXK204 | CXK | Ogden-Hinckley Airport (KOGD) | Savage Field (KU01) | 2026-05-01 16:00 UTC | 2026-05-01 16:52 UTC | 52m |
| LOT3JK | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Hamburg Airport (EDDH) | 2026-05-01 15:45 UTC | 2026-05-01 16:52 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
