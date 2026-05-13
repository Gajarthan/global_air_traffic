# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_10:47:54_UTC-green)

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

**Latest saved flight:** 2026-05-13 10:47:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-13 10:47:54 UTC

- **79,942** saved flights
- **29,059** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,942** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **986,626.4 tonnes** estimated CO2 emissions
- **57,195,731 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3441 |
| 2 | SkyWest Airlines | 2967 |
| 3 | IndiGo | 1764 |
| 4 | EJA | 1481 |
| 5 | American Airlines | 1239 |
| 6 | Southwest Airlines | 1169 |
| 7 | Lufthansa | 1048 |
| 8 | ENY | 996 |
| 9 | Delta Air Lines | 875 |
| 10 | Vueling | 764 |
| 11 | AXM | 733 |
| 12 | LATAM Airlines | 726 |
| 13 | WIF | 694 |
| 14 | All Nippon Airways | 641 |
| 15 | AZU | 629 |
| 16 | Swiss International | 621 |
| 17 | QLK | 596 |
| 18 | LXJ | 579 |
| 19 | Alaska Airlines | 562 |
| 20 | easyJet | 533 |
| 21 | EJU | 516 |
| 22 | AEE | 515 |
| 23 | Cathay Pacific | 504 |
| 24 | VIV | 474 |
| 25 | Air France | 473 |
| 26 | Japan Airlines | 456 |
| 27 | AXB | 438 |
| 28 | CXK | 414 |
| 29 | AIQ | 398 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64866 |
| 2 | 🇪🇸 ES | 5699 |
| 3 | 🇮🇳 IN | 5522 |
| 4 | 🇦🇺 AU | 5139 |
| 5 | 🇩🇪 DE | 4530 |
| 6 | 🇮🇹 IT | 4431 |
| 7 | 🇧🇷 BR | 4413 |
| 8 | 🇯🇵 JP | 4113 |
| 9 | 🇨🇦 CA | 3988 |
| 10 | 🇬🇧 GB | 3437 |
| 11 | 🇫🇷 FR | 3177 |
| 12 | 🇨🇴 CO | 2709 |
| 13 | 🇲🇽 MX | 2407 |
| 14 | 🇬🇷 GR | 2349 |
| 15 | 🇳🇴 NO | 2225 |
| 16 | 🇨🇭 CH | 2159 |
| 17 | 🇲🇾 MY | 1836 |
| 18 | 🇿🇦 ZA | 1516 |
| 19 | 🇹🇷 TR | 1437 |
| 20 | 🇹🇭 TH | 1415 |
| 21 | 🇳🇿 NZ | 1414 |
| 22 | 🇵🇱 PL | 1333 |
| 23 | 🇵🇭 PH | 1267 |
| 24 | 🇰🇷 KR | 1234 |
| 25 | 🇬🇹 GT | 1224 |
| 26 | 🇲🇦 MA | 939 |
| 27 | 🇲🇴 MO | 926 |
| 28 | 🇲🇪 ME | 857 |
| 29 | 🇳🇱 NL | 830 |
| 30 | 🇭🇷 HR | 708 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1757 |
| 2 | Tokyo International Airport |  | JP | 1379 |
| 3 | Denver International Airport |  | US | 1339 |
| 4 | Indira Gandhi International Airport |  | IN | 1169 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1152 |
| 6 | Frankfurt am Main International Airport |  | DE | 1053 |
| 7 | Harry Reid International Airport |  | US | 992 |
| 8 | Zurich Airport |  | CH | 953 |
| 9 | Macau International Airport |  | MO | 926 |
| 10 | La Aurora Airport |  | GT | 922 |
| 11 | Guaymaral Airport |  | CO | 901 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 897 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 810 |
| 15 | Chicago O'Hare International Airport |  | US | 779 |
| 16 | Kuala Lumpur International Airport |  | MY | 734 |
| 17 | Madrid Barajas International Airport |  | ES | 733 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 705 |
| 19 | Malpensa International Airport |  | IT | 686 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 680 |
| 21 | Bengaluru International Airport |  | IN | 679 |
| 22 | Salt Lake City International Airport |  | US | 655 |
| 23 | Capua Airport |  | IT | 652 |
| 24 | Charlotte/Douglas International Airport |  | US | 628 |
| 25 | Charles de Gaulle International Airport |  | FR | 628 |
| 26 | Congonhas Airport |  | BR | 624 |
| 27 | Tenerife Norte Airport |  | ES | 593 |
| 28 | Daniel K Inouye International Airport |  | US | 580 |
| 29 | Ninoy Aquino International Airport |  | PH | 578 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 571 |
| 31 | Barcelona International Airport |  | ES | 537 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 535 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 531 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 524 |
| 35 | Vitoria/Foronda Airport |  | ES | 508 |
| 36 | Don Mueang International Airport |  | TH | 507 |
| 37 | Amsterdam Airport Schiphol |  | NL | 502 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 495 |
| 39 | O. R. Tambo International Airport |  | ZA | 480 |
| 40 | Calgary International Airport |  | CA | 471 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 375 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 287 | 21m | 244 km | 1,208.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 230 | 24m | 225 km | 892.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 215 | 1h 27m | 910 km | 3,373.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 203 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 191 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 180 | 1h 11m | 770 km | 2,391.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 117 | 20m | 147 km | 296.1 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 115 | 20m | 250 km | 496.7 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 2m | 695 km | 1,270.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 106 | 57m | 493 km | 901.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 105 | 1h 42m | 1,423 km | 2,576.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 101 | 18m | 144 km | 251.2 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 100 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N34HF |  | Linden Airport (KLDJ) | Millville Municipal Airport (KMIV) | 2026-05-13 09:51 UTC | 2026-05-13 10:47 UTC | 56m |
| IOS224 | IOS | Land's End Airport (EGHC) | Newquay Cornwall Airport (EGHQ) | 2026-05-13 10:15 UTC | 2026-05-13 10:32 UTC | 16m |
| GNS109 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-13 10:25 UTC | 2026-05-13 10:29 UTC | 3m |
| GRZLY12 | GRZ | Melsbroek Air Base (EBMB) | Liege Airport (EBLG) | 2026-05-13 09:12 UTC | 2026-05-13 10:23 UTC | 1h 11m |
| NIVAL05 | NIV | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-05-13 10:05 UTC | 2026-05-13 10:21 UTC | 16m |
| RYR9WQ | Ryanair | Liverpool John Lennon Airport (EGGP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-13 07:59 UTC | 2026-05-13 10:08 UTC | 2h 9m |
| UPS1392 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Kosciusko-Attala County Airport (KOSX) | 2026-05-13 09:16 UTC | 2026-05-13 10:06 UTC | 49m |
| APG092 | APG | Ninoy Aquino International Airport (RPLL) | Macau International Airport (VMMC) | 2026-05-13 08:20 UTC | 2026-05-13 10:05 UTC | 1h 45m |
| HR615 |  | Kisarazu Airport (RJTK) | Kisarazu Airport (RJTK) | 2026-05-13 09:46 UTC | 2026-05-13 09:59 UTC | 13m |
| PHKFU | PHK | Eelde Airport (EHGG) | Borkum Airport (EDWR) | 2026-05-13 09:33 UTC | 2026-05-13 09:56 UTC | 22m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-05-13 09:13 UTC | 2026-05-13 09:53 UTC | 40m |
| CHX89 | CHX | Regensburg-Oberhub Airport (EDNR) | Nittenau-Bruck Airport (EDNM) | 2026-05-13 09:43 UTC | 2026-05-13 09:52 UTC | 9m |
| NOZ372 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Tromsø Airport (ENTC) | 2026-05-13 08:30 UTC | 2026-05-13 09:52 UTC | 1h 21m |
| LOT3HB | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-13 09:04 UTC | 2026-05-13 09:51 UTC | 46m |
| OCN8PF | OCN | Frankfurt am Main International Airport (EDDF) | Otocac Airport (LDRO) | 2026-05-13 08:50 UTC | 2026-05-13 09:49 UTC | 58m |
| AEA7157 | AEA | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-05-13 09:21 UTC | 2026-05-13 09:46 UTC | 25m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-13 09:13 UTC | 2026-05-13 09:45 UTC | 32m |
| A7GQD |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-05-13 09:29 UTC | 2026-05-13 09:45 UTC | 15m |
| REV99 | REV | East Midlands Airport (EGNX) | Alderney Airport (EGJA) | 2026-05-13 08:02 UTC | 2026-05-13 09:44 UTC | 1h 41m |
| AZU6050 | AZU | Congonhas Airport (SBSP) | Ilha dos Porcos Grandes Airport (SILI) | 2026-05-13 09:18 UTC | 2026-05-13 09:42 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
