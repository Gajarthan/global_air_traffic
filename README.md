# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_16:33:27_UTC-green)

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

**Latest saved flight:** 2026-04-27 16:33:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 16:33:27 UTC

- **56,867** saved flights
- **22,258** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,867** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **690,840.7 tonnes** estimated CO2 emissions
- **40,048,733 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2419 |
| 2 | SkyWest Airlines | 2142 |
| 3 | IndiGo | 1296 |
| 4 | EJA | 1016 |
| 5 | American Airlines | 900 |
| 6 | Southwest Airlines | 809 |
| 7 | ENY | 715 |
| 8 | Lufthansa | 703 |
| 9 | Vueling | 571 |
| 10 | AXM | 553 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 501 |
| 13 | AZU | 476 |
| 14 | WIF | 473 |
| 15 | Delta Air Lines | 471 |
| 16 | Swiss International | 447 |
| 17 | QLK | 439 |
| 18 | LXJ | 408 |
| 19 | Alaska Airlines | 380 |
| 20 | AEE | 374 |
| 21 | EJU | 368 |
| 22 | easyJet | 364 |
| 23 | VIV | 363 |
| 24 | Air France | 332 |
| 25 | Cathay Pacific | 328 |
| 26 | Japan Airlines | 327 |
| 27 | AXB | 311 |
| 28 | JetBlue | 290 |
| 29 | GLO | 287 |
| 30 | AIQ | 286 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45008 |
| 2 | 🇪🇸 ES | 4156 |
| 3 | 🇮🇳 IN | 4088 |
| 4 | 🇦🇺 AU | 3810 |
| 5 | 🇧🇷 BR | 3272 |
| 6 | 🇩🇪 DE | 3116 |
| 7 | 🇮🇹 IT | 3110 |
| 8 | 🇯🇵 JP | 3048 |
| 9 | 🇨🇦 CA | 2810 |
| 10 | 🇨🇴 CO | 2574 |
| 11 | 🇬🇧 GB | 2400 |
| 12 | 🇫🇷 FR | 2244 |
| 13 | 🇲🇽 MX | 1809 |
| 14 | 🇬🇷 GR | 1684 |
| 15 | 🇨🇭 CH | 1602 |
| 16 | 🇳🇴 NO | 1535 |
| 17 | 🇲🇾 MY | 1343 |
| 18 | 🇿🇦 ZA | 1161 |
| 19 | 🇳🇿 NZ | 1072 |
| 20 | 🇹🇷 TR | 1039 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 964 |
| 23 | 🇵🇱 PL | 920 |
| 24 | 🇰🇷 KR | 904 |
| 25 | 🇬🇹 GT | 845 |
| 26 | 🇲🇦 MA | 721 |
| 27 | 🇲🇪 ME | 618 |
| 28 | 🇲🇴 MO | 605 |
| 29 | 🇳🇱 NL | 595 |
| 30 | 🇮🇩 ID | 488 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1288 |
| 2 | Tokyo International Airport |  | JP | 1034 |
| 3 | Denver International Airport |  | US | 944 |
| 4 | El Dorado International Airport |  | CO | 867 |
| 5 | Indira Gandhi International Airport |  | IN | 866 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 831 |
| 7 | Guaymaral Airport |  | CO | 789 |
| 8 | Harry Reid International Airport |  | US | 725 |
| 9 | Frankfurt am Main International Airport |  | DE | 691 |
| 10 | Zurich Airport |  | CH | 683 |
| 11 | La Aurora Airport |  | GT | 636 |
| 12 | Macau International Airport |  | MO | 605 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 564 |
| 14 | Chicago O'Hare International Airport |  | US | 551 |
| 15 | Madrid Barajas International Airport |  | ES | 532 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 530 |
| 17 | Kuala Lumpur International Airport |  | MY | 529 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 501 |
| 19 | Malpensa International Airport |  | IT | 494 |
| 20 | Bengaluru International Airport |  | IN | 490 |
| 21 | Congonhas Airport |  | BR | 471 |
| 22 | Charlotte/Douglas International Airport |  | US | 457 |
| 23 | Tenerife Norte Airport |  | ES | 455 |
| 24 | Ninoy Aquino International Airport |  | PH | 443 |
| 25 | Salt Lake City International Airport |  | US | 439 |
| 26 | Charles de Gaulle International Airport |  | FR | 439 |
| 27 | Capua Airport |  | IT | 428 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 421 |
| 29 | Daniel K Inouye International Airport |  | US | 418 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 408 |
| 31 | Barcelona International Airport |  | ES | 389 |
| 32 | Vitoria/Foronda Airport |  | ES | 387 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 384 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 378 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 36 | O. R. Tambo International Airport |  | ZA | 365 |
| 37 | Reno/Tahoe International Airport |  | US | 365 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 340 |
| 40 | Calgary International Airport |  | CA | 339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 322 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 209 | 14m | 114 km | 409.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 182 | 21m | 244 km | 766.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 163 | 1h 27m | 910 km | 2,557.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 137 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 111 | 1h 12m | 770 km | 1,474.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 109 | 44m | 452 km | 849.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 96 | 31m | 369 km | 611.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 85 | 52m | 556 km | 814.8 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 53m | 1,304 km | 1,732.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 72 | 1h 42m | 1,423 km | 1,767.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N481MR |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-27 16:09 UTC | 2026-04-27 16:33 UTC | 24m |
| FAG707 | FAG | La Aurora Airport (MGGT) | La America Airport (MHEI) | 2026-04-27 15:31 UTC | 2026-04-27 16:29 UTC | 57m |
| LXJ339 | LXJ | Carson City Airport (KCXP) | Van Nuys Airport (KVNY) | 2026-04-27 15:29 UTC | 2026-04-27 16:26 UTC | 56m |
| GIZMO21 | GIZ | Enid Woodring Regional Airport (KWDG) | Flying E Ranch Airport (OK16) | 2026-04-27 16:06 UTC | 2026-04-27 16:23 UTC | 17m |
| VIRAL75 | Virgin Atlantic | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-04-27 16:08 UTC | 2026-04-27 16:20 UTC | 12m |
| N444TH |  | Peter O Knight Airport (KTPF) | Wauchula Municipal Airport (KCHN) | 2026-04-27 15:32 UTC | 2026-04-27 16:20 UTC | 47m |
| N7873N |  | City Of Colorado Springs Municipal Airport (KCOS) | Lone Tree Ranch Airport (35CO) | 2026-04-27 15:52 UTC | 2026-04-27 16:20 UTC | 28m |
| ABY530 | ABY | Sharjah International Airport (OMSJ) | Simara Airport (VNSI) | 2026-04-27 12:22 UTC | 2026-04-27 16:13 UTC | 3h 51m |
| SWA3885 | Southwest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Salt Lake City International Airport (KSLC) | 2026-04-27 15:05 UTC | 2026-04-27 16:12 UTC | 1h 7m |
| N231AV |  | Nampa Municipal Airport (KMAN) | Skinner Ranch Airport (12OR) | 2026-04-27 15:39 UTC | 2026-04-27 16:09 UTC | 30m |
| ROT273L | ROT | Henri Coanda International Airport (LROP) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-27 14:54 UTC | 2026-04-27 16:08 UTC | 1h 14m |
| BOX722 | BOX | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-27 08:45 UTC | 2026-04-27 16:08 UTC | 7h 22m |
| JSX8002 | JSX | John Wayne/Orange County Airport (KSNA) | Seven Springs Airport (16TA) | 2026-04-27 14:32 UTC | 2026-04-27 16:06 UTC | 1h 34m |
| MAS114 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Simara Airport (VNSI) | 2026-04-27 11:35 UTC | 2026-04-27 16:06 UTC | 4h 31m |
| LXJ556 | LXJ | K36U (K36U) | Telluride Regional Airport (KTEX) | 2026-04-27 15:26 UTC | 2026-04-27 16:06 UTC | 39m |
| SKW5495 | SkyWest Airlines | Santa Fe Regional Airport (KSAF) | Denver International Airport (KDEN) | 2026-04-27 15:15 UTC | 2026-04-27 16:05 UTC | 49m |
| EJA895 | EJA | Dallas Love Field (KDAL) | Scottsdale Airport (KSDL) | 2026-04-27 13:46 UTC | 2026-04-27 16:04 UTC | 2h 17m |
| BUZZ31 | BUZ | Frontier Airport (55XS) | Laughlin Afb Aux Nr 1 Airport (KT70) | 2026-04-27 15:59 UTC | 2026-04-27 16:03 UTC | 3m |
| ENSA47 | ENS | Fazenda Entre Rios Airport (SDEO) | Mirassol Airport (SDMH) | 2026-04-27 15:49 UTC | 2026-04-27 16:01 UTC | 11m |
| OAL8NJ | OAL | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-27 15:37 UTC | 2026-04-27 16:01 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
