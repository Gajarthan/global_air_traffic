# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_17:34:30_UTC-green)

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

**Latest saved flight:** 2026-05-05 17:34:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 17:34:30 UTC

- **69,274** saved flights
- **25,910** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,274** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **851,653.4 tonnes** estimated CO2 emissions
- **49,371,214 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2977 |
| 2 | SkyWest Airlines | 2566 |
| 3 | IndiGo | 1597 |
| 4 | EJA | 1245 |
| 5 | American Airlines | 1074 |
| 6 | Southwest Airlines | 984 |
| 7 | Lufthansa | 897 |
| 8 | ENY | 854 |
| 9 | Vueling | 681 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 643 |
| 12 | WIF | 591 |
| 13 | All Nippon Airways | 585 |
| 14 | Delta Air Lines | 580 |
| 15 | AZU | 562 |
| 16 | QLK | 534 |
| 17 | Swiss International | 534 |
| 18 | LXJ | 496 |
| 19 | Alaska Airlines | 474 |
| 20 | easyJet | 464 |
| 21 | AEE | 452 |
| 22 | EJU | 450 |
| 23 | VIV | 431 |
| 24 | Cathay Pacific | 417 |
| 25 | Air France | 409 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 338 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54823 |
| 2 | 🇪🇸 ES | 5064 |
| 3 | 🇮🇳 IN | 5024 |
| 4 | 🇦🇺 AU | 4599 |
| 5 | 🇩🇪 DE | 3885 |
| 6 | 🇧🇷 BR | 3883 |
| 7 | 🇮🇹 IT | 3803 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3418 |
| 10 | 🇬🇧 GB | 3017 |
| 11 | 🇫🇷 FR | 2756 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2197 |
| 14 | 🇬🇷 GR | 2076 |
| 15 | 🇨🇭 CH | 1912 |
| 16 | 🇳🇴 NO | 1899 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1389 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1254 |
| 22 | 🇵🇭 PH | 1158 |
| 23 | 🇵🇱 PL | 1141 |
| 24 | 🇬🇹 GT | 1117 |
| 25 | 🇰🇷 KR | 1110 |
| 26 | 🇲🇦 MA | 836 |
| 27 | 🇲🇴 MO | 787 |
| 28 | 🇲🇪 ME | 747 |
| 29 | 🇳🇱 NL | 726 |
| 30 | 🇮🇩 ID | 587 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1526 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1135 |
| 4 | Indira Gandhi International Airport |  | IN | 1052 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1014 |
| 6 | Frankfurt am Main International Airport |  | DE | 892 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 863 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 831 |
| 11 | Zurich Airport |  | CH | 820 |
| 12 | Macau International Airport |  | MO | 787 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 687 |
| 14 | Kuala Lumpur International Airport |  | MY | 668 |
| 15 | Chicago O'Hare International Airport |  | US | 661 |
| 16 | Madrid Barajas International Airport |  | ES | 660 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 617 |
| 18 | Bengaluru International Airport |  | IN | 605 |
| 19 | Malpensa International Airport |  | IT | 604 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 601 |
| 21 | Congonhas Airport |  | BR | 555 |
| 22 | Salt Lake City International Airport |  | US | 554 |
| 23 | Charles de Gaulle International Airport |  | FR | 545 |
| 24 | Charlotte/Douglas International Airport |  | US | 544 |
| 25 | Tenerife Norte Airport |  | ES | 542 |
| 26 | Capua Airport |  | IT | 535 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 509 |
| 29 | Daniel K Inouye International Airport |  | US | 502 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 488 |
| 31 | Barcelona International Airport |  | ES | 480 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 462 |
| 34 | Vitoria/Foronda Airport |  | ES | 461 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | O. R. Tambo International Airport |  | ZA | 438 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 431 |
| 38 | Amsterdam Airport Schiphol |  | NL | 428 |
| 39 | Reno/Tahoe International Airport |  | US | 411 |
| 40 | Calgary International Airport |  | CA | 410 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 236 | 21m | 244 km | 993.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 172 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 156 | 26m | 275 km | 739.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 132 | 21m | 99 km | 226.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSR48 | CSR | Montpellier Candillargues Airport (LFNG) | Nimes-Arles-Camargue Airport (LFTW) | 2026-05-05 17:11 UTC | 2026-05-05 17:34 UTC | 22m |
| N127CA |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-05-05 16:30 UTC | 2026-05-05 17:28 UTC | 58m |
| N26CF |  | Trading Bay Production Airport (5AK0) | Johnson Airport (3AK4) | 2026-05-05 17:15 UTC | 2026-05-05 17:27 UTC | 12m |
| N874BU |  | Geraci Airpark (FL35) | Peter O Knight Airport (KTPF) | 2026-05-05 17:14 UTC | 2026-05-05 17:26 UTC | 12m |
| N361LU |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-05-05 16:36 UTC | 2026-05-05 17:22 UTC | 46m |
| N52606 |  | Sarasota/Bradenton International Airport (KSRQ) | Bartow Executive Airport (KBOW) | 2026-05-05 16:48 UTC | 2026-05-05 17:22 UTC | 33m |
| N804MS |  | Harry Reid International Airport (KLAS) | 1CA4 (1CA4) | 2026-05-05 16:55 UTC | 2026-05-05 17:20 UTC | 24m |
| CPA048 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-05-05 12:16 UTC | 2026-05-05 17:19 UTC | 5h 2m |
| EJM989 | EJM | Teterboro Airport (KTEB) | Rocky Mountain Metro Airport (KBJC) | 2026-05-05 13:28 UTC | 2026-05-05 17:15 UTC | 3h 46m |
| PSBSZ | PSB | Fazenda Boa Vista Airport (SWQM) | Porto dos Gauchos Airport (SWPG) | 2026-05-05 16:10 UTC | 2026-05-05 17:07 UTC | 56m |
| N13683 |  | Mesquite Metro Airport (KHQZ) | 31TS (31TS) | 2026-05-05 13:22 UTC | 2026-05-05 17:06 UTC | 3h 43m |
| EJM23 | EJM | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-05-05 16:48 UTC | 2026-05-05 17:05 UTC | 16m |
| N84CW |  | Chippewa Valley Regional Airport (KEAU) | Green Bay/Austin Straubel International Airport (KGRB) | 2026-05-05 16:37 UTC | 2026-05-05 17:04 UTC | 26m |
| N815SS |  | Trading Bay Production Airport (5AK0) | Mcgahan Industrial Airpark (AK73) | 2026-05-05 16:48 UTC | 2026-05-05 17:04 UTC | 16m |
| N26CF |  | Johnson Airport (3AK4) | Trading Bay Production Airport (5AK0) | 2026-05-05 16:51 UTC | 2026-05-05 17:04 UTC | 12m |
| N894MA |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-05-05 16:37 UTC | 2026-05-05 17:03 UTC | 25m |
| FIN519 | Finnair | Helsinki Vantaa Airport (EFHK) | Ranua Airport (EFRU) | 2026-05-05 15:45 UTC | 2026-05-05 16:59 UTC | 1h 13m |
| WMU79 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | C V Airport (II43) | 2026-05-05 16:30 UTC | 2026-05-05 16:58 UTC | 28m |
| N582T |  | Telluride Regional Airport (KTEX) | CD82 (CD82) | 2026-05-05 14:35 UTC | 2026-05-05 16:57 UTC | 2h 22m |
| LFA543 | LFA | Orlando Sanford International Airport (KSFB) | Space Coast Regional Airport (KTIX) | 2026-05-05 16:08 UTC | 2026-05-05 16:57 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
