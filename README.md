# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_18:37:32_UTC-green)

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

**Latest saved flight:** 2026-05-08 18:37:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 18:37:32 UTC

- **73,909** saved flights
- **27,351** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **73,909** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **908,915.3 tonnes** estimated CO2 emissions
- **52,690,742 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3180 |
| 2 | SkyWest Airlines | 2732 |
| 3 | IndiGo | 1664 |
| 4 | EJA | 1353 |
| 5 | American Airlines | 1149 |
| 6 | Southwest Airlines | 1070 |
| 7 | Lufthansa | 961 |
| 8 | ENY | 926 |
| 9 | Vueling | 722 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 685 |
| 12 | Delta Air Lines | 650 |
| 13 | WIF | 645 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 594 |
| 16 | QLK | 573 |
| 17 | Swiss International | 564 |
| 18 | LXJ | 546 |
| 19 | Alaska Airlines | 516 |
| 20 | easyJet | 487 |
| 21 | EJU | 477 |
| 22 | AEE | 473 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 451 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 430 |
| 27 | AXB | 411 |
| 28 | CXK | 376 |
| 29 | AIQ | 366 |
| 30 | MXY | 357 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 59254 |
| 2 | 🇪🇸 ES | 5348 |
| 3 | 🇮🇳 IN | 5227 |
| 4 | 🇦🇺 AU | 4907 |
| 5 | 🇩🇪 DE | 4157 |
| 6 | 🇧🇷 BR | 4135 |
| 7 | 🇮🇹 IT | 4047 |
| 8 | 🇯🇵 JP | 3877 |
| 9 | 🇨🇦 CA | 3679 |
| 10 | 🇬🇧 GB | 3179 |
| 11 | 🇫🇷 FR | 2932 |
| 12 | 🇨🇴 CO | 2686 |
| 13 | 🇲🇽 MX | 2298 |
| 14 | 🇬🇷 GR | 2188 |
| 15 | 🇳🇴 NO | 2067 |
| 16 | 🇨🇭 CH | 2012 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1325 |
| 21 | 🇹🇭 TH | 1317 |
| 22 | 🇵🇱 PL | 1240 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1164 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 880 |
| 27 | 🇲🇴 MO | 853 |
| 28 | 🇲🇪 ME | 793 |
| 29 | 🇳🇱 NL | 774 |
| 30 | 🇧🇸 BS | 623 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1635 |
| 2 | Tokyo International Airport |  | JP | 1303 |
| 3 | Denver International Airport |  | US | 1229 |
| 4 | Indira Gandhi International Airport |  | IN | 1103 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1072 |
| 6 | Frankfurt am Main International Airport |  | DE | 956 |
| 7 | Harry Reid International Airport |  | US | 917 |
| 8 | Guaymaral Airport |  | CO | 881 |
| 9 | El Dorado International Airport |  | CO | 878 |
| 10 | Zurich Airport |  | CH | 874 |
| 11 | La Aurora Airport |  | GT | 869 |
| 12 | Macau International Airport |  | MO | 853 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 743 |
| 14 | Chicago O'Hare International Airport |  | US | 714 |
| 15 | Kuala Lumpur International Airport |  | MY | 696 |
| 16 | Madrid Barajas International Airport |  | ES | 693 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 654 |
| 18 | Malpensa International Airport |  | IT | 641 |
| 19 | Bengaluru International Airport |  | IN | 641 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 599 |
| 22 | Congonhas Airport |  | BR | 585 |
| 23 | Charlotte/Douglas International Airport |  | US | 582 |
| 24 | Charles de Gaulle International Airport |  | FR | 574 |
| 25 | Capua Airport |  | IT | 574 |
| 26 | Tenerife Norte Airport |  | ES | 559 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 539 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 531 |
| 30 | Barcelona International Airport |  | ES | 509 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 508 |
| 32 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 500 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 500 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Amsterdam Airport Schiphol |  | NL | 466 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 464 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 440 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 366 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 260 | 21m | 244 km | 1,094.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 186 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 136 | 21m | 99 km | 233.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 101 | 1h 2m | 695 km | 1,210.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 100 | 1h 42m | 1,423 km | 2,454.2 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 97 | 23m | 55 km | 92.2 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 91 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N24KK |  | Smyrna Airport (KMQY) | 2KY3 (2KY3) | 2026-05-08 18:07 UTC | 2026-05-08 18:37 UTC | 29m |
| CXK395 | CXK | Morristown Municipal Airport (KMMU) | Lancaster Airport (KLNS) | 2026-05-08 17:29 UTC | 2026-05-08 18:35 UTC | 1h 6m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-08 18:18 UTC | 2026-05-08 18:34 UTC | 16m |
| N54PV |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-05-08 18:14 UTC | 2026-05-08 18:32 UTC | 18m |
| AUB153 | AUB | Auburn University Regional Airport (KAUO) | Columbus Airport (KCSG) | 2026-05-08 17:32 UTC | 2026-05-08 18:32 UTC | 59m |
| N2291C |  | NV13 (NV13) | Carson City Airport (KCXP) | 2026-05-08 18:18 UTC | 2026-05-08 18:31 UTC | 13m |
| N2252Z |  | Heritage Field (KPTW) | Lancaster Airport (KLNS) | 2026-05-08 18:05 UTC | 2026-05-08 18:28 UTC | 22m |
| AIC5VC | Air India | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-08 16:41 UTC | 2026-05-08 18:24 UTC | 1h 42m |
| BOX722 | BOX | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-08 14:18 UTC | 2026-05-08 18:22 UTC | 4h 4m |
| RTY131 | RTY | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-05-08 17:41 UTC | 2026-05-08 18:19 UTC | 38m |
| N5086R |  | Pierce County/Thun Field (KPLU) | Pierce County/Thun Field (KPLU) | 2026-05-08 17:52 UTC | 2026-05-08 18:16 UTC | 23m |
| DAL120 | Delta Air Lines | Tokyo International Airport (RJTT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 07:56 UTC | 2026-05-08 18:15 UTC | 10h 19m |
| N225MV |  | Montgomery-Gibbs Executive Airport (KMYF) | Jacqueline Cochran Regional Airport (KTRM) | 2026-05-08 17:57 UTC | 2026-05-08 18:13 UTC | 16m |
| DAL1641 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 18:00 UTC | 2026-05-08 18:13 UTC | 12m |
| N721JD |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-05-08 17:03 UTC | 2026-05-08 18:13 UTC | 1h 9m |
| N3957A |  | Beggs Ranch/Aledo/ Airport (TX15) | Addington Field (4TX8) | 2026-05-08 17:55 UTC | 2026-05-08 18:11 UTC | 15m |
| N6141T |  | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-05-08 17:58 UTC | 2026-05-08 18:11 UTC | 13m |
| PGT380U | PGT | Dusseldorf International Airport (EDDL) | Istanbul Airport (LTFM) | 2026-05-08 15:39 UTC | 2026-05-08 18:11 UTC | 2h 31m |
| DAL171 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 17:41 UTC | 2026-05-08 18:10 UTC | 28m |
| SKW3801 | SkyWest Airlines | Indianapolis International Airport (KIND) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 16:42 UTC | 2026-05-08 18:07 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
