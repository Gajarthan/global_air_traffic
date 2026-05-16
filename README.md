# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_21:06:43_UTC-green)

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

**Latest saved flight:** 2026-05-16 21:06:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 21:06:43 UTC

- **85,320** saved flights
- **30,662** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,320** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,052,170.3 tonnes** estimated CO2 emissions
- **60,995,377 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3660 |
| 2 | SkyWest Airlines | 3153 |
| 3 | IndiGo | 1836 |
| 4 | EJA | 1608 |
| 5 | American Airlines | 1308 |
| 6 | Southwest Airlines | 1243 |
| 7 | Lufthansa | 1083 |
| 8 | ENY | 1061 |
| 9 | Delta Air Lines | 931 |
| 10 | Vueling | 808 |
| 11 | LATAM Airlines | 773 |
| 12 | AXM | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | Swiss International | 662 |
| 16 | All Nippon Airways | 660 |
| 17 | LXJ | 627 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 604 |
| 20 | easyJet | 563 |
| 21 | EJU | 540 |
| 22 | AEE | 536 |
| 23 | Cathay Pacific | 534 |
| 24 | VIV | 512 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | CXK | 453 |
| 28 | AXB | 450 |
| 29 | MXY | 426 |
| 30 | United Airlines | 419 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69976 |
| 2 | 🇪🇸 ES | 6029 |
| 3 | 🇮🇳 IN | 5750 |
| 4 | 🇦🇺 AU | 5418 |
| 5 | 🇩🇪 DE | 4750 |
| 6 | 🇧🇷 BR | 4698 |
| 7 | 🇮🇹 IT | 4695 |
| 8 | 🇯🇵 JP | 4260 |
| 9 | 🇨🇦 CA | 4235 |
| 10 | 🇬🇧 GB | 3633 |
| 11 | 🇫🇷 FR | 3390 |
| 12 | 🇨🇴 CO | 2865 |
| 13 | 🇲🇽 MX | 2624 |
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
| 27 | 🇲🇴 MO | 985 |
| 28 | 🇲🇪 ME | 888 |
| 29 | 🇳🇱 NL | 866 |
| 30 | 🇭🇷 HR | 762 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1865 |
| 2 | Denver International Airport |  | US | 1431 |
| 3 | Tokyo International Airport |  | JP | 1424 |
| 4 | Indira Gandhi International Airport |  | IN | 1231 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1189 |
| 6 | Frankfurt am Main International Airport |  | DE | 1094 |
| 7 | Harry Reid International Airport |  | US | 1075 |
| 8 | Zurich Airport |  | CH | 1013 |
| 9 | Macau International Airport |  | MO | 985 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 942 |
| 13 | El Dorado International Airport |  | CO | 919 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 859 |
| 15 | Chicago O'Hare International Airport |  | US | 826 |
| 16 | Madrid Barajas International Airport |  | ES | 777 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 736 |
| 19 | Malpensa International Airport |  | IT | 709 |
| 20 | Salt Lake City International Airport |  | US | 708 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 697 |
| 24 | Charles de Gaulle International Airport |  | FR | 664 |
| 25 | Charlotte/Douglas International Airport |  | US | 661 |
| 26 | Congonhas Airport |  | BR | 659 |
| 27 | Daniel K Inouye International Airport |  | US | 622 |
| 28 | Tenerife Norte Airport |  | ES | 619 |
| 29 | Ninoy Aquino International Airport |  | PH | 611 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 579 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 570 |
| 33 | Barcelona International Airport |  | ES | 569 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 540 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 537 |
| 37 | Don Mueang International Airport |  | TH | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 526 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 498 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 315 | 21m | 244 km | 1,326.4 t |
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
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 103 | 1h 41m | 1,156 km | 2,054.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU821 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-05-16 20:05 UTC | 2026-05-16 21:06 UTC | 1h 1m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 20:44 UTC | 2026-05-16 21:00 UTC | 15m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-16 20:05 UTC | 2026-05-16 20:54 UTC | 49m |
| N737WR |  | Jacksonville Executive At Craig Airport (KCRG) | Cecil Airport (KVQQ) | 2026-05-16 20:31 UTC | 2026-05-16 20:54 UTC | 22m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-16 06:10 UTC | 2026-05-16 20:50 UTC | 14h 39m |
| CAP2869 | CAP | 70NH (70NH) | Concord Municipal Airport (KCON) | 2026-05-16 19:30 UTC | 2026-05-16 20:47 UTC | 1h 17m |
| N150RJ |  | William P Hobby Airport (KHOU) | Lea County/Jal Airport (KE26) | 2026-05-16 19:32 UTC | 2026-05-16 20:44 UTC | 1h 12m |
| N732ZY |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-05-16 20:11 UTC | 2026-05-16 20:42 UTC | 30m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-05-16 20:28 UTC | 2026-05-16 20:37 UTC | 9m |
| N880PC |  | 91IS (91IS) | Hoblit Farms Airport (IL94) | 2026-05-16 20:26 UTC | 2026-05-16 20:37 UTC | 11m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-16 20:13 UTC | 2026-05-16 20:36 UTC | 22m |
|  |  | Cape Fear Regional Jetport/Howie Franklin Field (KSUT) | Cape Fear Regional Jetport/Howie Franklin Field (KSUT) | 2026-05-16 20:32 UTC | 2026-05-16 20:36 UTC | 3m |
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-05-16 19:50 UTC | 2026-05-16 20:34 UTC | 43m |
| CSI502 | CSI | Albuquerque International Sunport Airport (KABQ) | Sacaton Airport (NM16) | 2026-05-16 20:06 UTC | 2026-05-16 20:33 UTC | 27m |
| N694DA |  | 3WI1 (3WI1) | 3WI1 (3WI1) | 2026-05-16 20:19 UTC | 2026-05-16 20:31 UTC | 12m |
| N414TB |  | Beech Factory Airport (KBEC) | Salina Regional Airport (KSLN) | 2026-05-16 19:43 UTC | 2026-05-16 20:31 UTC | 47m |
| RYR1TW | Ryanair | Dublin Airport (EIDW) | Ampuriabrava Airport (LEAP) | 2026-05-16 18:40 UTC | 2026-05-16 20:29 UTC | 1h 48m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-16 20:12 UTC | 2026-05-16 20:27 UTC | 15m |
| LXJ394 | LXJ | Livermore Municipal Airport (KLVK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-16 20:09 UTC | 2026-05-16 20:27 UTC | 17m |
| ANA968 | All Nippon Airways | Nagasaki Airport (RJFU) | Tokyo International Airport (RJTT) | 2026-05-16 19:06 UTC | 2026-05-16 20:27 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
