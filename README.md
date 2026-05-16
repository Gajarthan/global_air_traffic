# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_21:53:41_UTC-green)

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

**Latest saved flight:** 2026-05-16 21:53:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 21:53:41 UTC

- **85,382** saved flights
- **30,682** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,382** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,053,082.6 tonnes** estimated CO2 emissions
- **61,048,266 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3663 |
| 2 | SkyWest Airlines | 3165 |
| 3 | IndiGo | 1836 |
| 4 | EJA | 1609 |
| 5 | American Airlines | 1312 |
| 6 | Southwest Airlines | 1245 |
| 7 | Lufthansa | 1083 |
| 8 | ENY | 1061 |
| 9 | Delta Air Lines | 932 |
| 10 | Vueling | 809 |
| 11 | LATAM Airlines | 775 |
| 12 | AXM | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | Swiss International | 662 |
| 16 | All Nippon Airways | 660 |
| 17 | LXJ | 628 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 606 |
| 20 | easyJet | 563 |
| 21 | EJU | 540 |
| 22 | AEE | 536 |
| 23 | Cathay Pacific | 536 |
| 24 | VIV | 514 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | CXK | 453 |
| 28 | AXB | 450 |
| 29 | MXY | 426 |
| 30 | United Airlines | 420 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70042 |
| 2 | 🇪🇸 ES | 6034 |
| 3 | 🇮🇳 IN | 5753 |
| 4 | 🇦🇺 AU | 5418 |
| 5 | 🇩🇪 DE | 4752 |
| 6 | 🇧🇷 BR | 4702 |
| 7 | 🇮🇹 IT | 4698 |
| 8 | 🇯🇵 JP | 4260 |
| 9 | 🇨🇦 CA | 4243 |
| 10 | 🇬🇧 GB | 3634 |
| 11 | 🇫🇷 FR | 3390 |
| 12 | 🇨🇴 CO | 2869 |
| 13 | 🇲🇽 MX | 2632 |
| 14 | 🇬🇷 GR | 2478 |
| 15 | 🇳🇴 NO | 2374 |
| 16 | 🇨🇭 CH | 2244 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1521 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1475 |
| 22 | 🇵🇱 PL | 1415 |
| 23 | 🇵🇭 PH | 1334 |
| 24 | 🇰🇷 KR | 1313 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇦 MA | 993 |
| 27 | 🇲🇴 MO | 987 |
| 28 | 🇲🇪 ME | 889 |
| 29 | 🇳🇱 NL | 866 |
| 30 | 🇭🇷 HR | 762 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1870 |
| 2 | Denver International Airport |  | US | 1436 |
| 3 | Tokyo International Airport |  | JP | 1424 |
| 4 | Indira Gandhi International Airport |  | IN | 1233 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1189 |
| 6 | Frankfurt am Main International Airport |  | DE | 1094 |
| 7 | Harry Reid International Airport |  | US | 1076 |
| 8 | Zurich Airport |  | CH | 1013 |
| 9 | Macau International Airport |  | MO | 987 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 944 |
| 13 | El Dorado International Airport |  | CO | 921 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 861 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 777 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 738 |
| 19 | Salt Lake City International Airport |  | US | 710 |
| 20 | Malpensa International Airport |  | IT | 709 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 697 |
| 24 | Charles de Gaulle International Airport |  | FR | 664 |
| 25 | Charlotte/Douglas International Airport |  | US | 661 |
| 26 | Congonhas Airport |  | BR | 660 |
| 27 | Daniel K Inouye International Airport |  | US | 625 |
| 28 | Tenerife Norte Airport |  | ES | 620 |
| 29 | Ninoy Aquino International Airport |  | PH | 611 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 581 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 570 |
| 33 | Barcelona International Airport |  | ES | 570 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 540 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 538 |
| 37 | Don Mueang International Airport |  | TH | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 526 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 499 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 316 | 21m | 244 km | 1,330.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 219 | 14m | 114 km | 429.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 178 | 26m | 275 km | 843.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6089F |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-05-16 20:32 UTC | 2026-05-16 21:53 UTC | 1h 21m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-16 07:26 UTC | 2026-05-16 21:52 UTC | 14h 25m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-16 21:27 UTC | 2026-05-16 21:49 UTC | 22m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-16 17:32 UTC | 2026-05-16 21:43 UTC | 4h 11m |
| EXS5DV | EXS | Jerez Airport (LEJR) | Manchester Airport (EGCC) | 2026-05-16 18:59 UTC | 2026-05-16 21:38 UTC | 2h 38m |
| FFT2524 | FFT | Phoenix Sky Harbor International Airport (KPHX) | Salt Lake City International Airport (KSLC) | 2026-05-16 20:21 UTC | 2026-05-16 21:30 UTC | 1h 9m |
| CGPEV | CGP | Billy Bishop Toronto City Airport (CYTZ) | Billy Bishop Toronto City Airport (CYTZ) | 2026-05-16 20:30 UTC | 2026-05-16 21:28 UTC | 57m |
| N6317D |  | Murfreesboro Municipal Airport (KMBT) | Murfreesboro Municipal Airport (KMBT) | 2026-05-16 20:42 UTC | 2026-05-16 21:28 UTC | 45m |
| BAW142 | British Airways | Indira Gandhi International Airport (VIDP) | Jammu Airport (VIJU) | 2026-05-16 20:53 UTC | 2026-05-16 21:27 UTC | 33m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 21:13 UTC | 2026-05-16 21:27 UTC | 13m |
| N90DT |  | Aero Country Airport (KT31) | Indianhead Ranch Airport (1TS9) | 2026-05-16 21:15 UTC | 2026-05-16 21:21 UTC | 5m |
| N529AB |  | Grand Forks Afb Airport (KRDR) | 19ND (19ND) | 2026-05-16 20:15 UTC | 2026-05-16 21:21 UTC | 1h 5m |
| N63BF |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-05-16 21:07 UTC | 2026-05-16 21:19 UTC | 12m |
| N27TJ |  | 98ME (98ME) | Lebanon Municipal Airport (KLEB) | 2026-05-16 20:19 UTC | 2026-05-16 21:13 UTC | 53m |
| RYR2GQ | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Sofia Airport (LBSF) | 2026-05-16 19:51 UTC | 2026-05-16 21:12 UTC | 1h 21m |
| STT5026 | STT | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-05-16 20:31 UTC | 2026-05-16 21:11 UTC | 39m |
| WJA228 | WJA | Calgary International Airport (CYYC) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-05-16 19:22 UTC | 2026-05-16 21:08 UTC | 1h 45m |
| ERU821 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-05-16 20:05 UTC | 2026-05-16 21:06 UTC | 1h 1m |
| N907KW |  | Cantwell Airport (PATW) | Songlo Vista Airport (3AK3) | 2026-05-16 20:26 UTC | 2026-05-16 21:03 UTC | 37m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 20:44 UTC | 2026-05-16 21:00 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
