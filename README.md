# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_18:48:11_UTC-green)

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

**Latest saved flight:** 2026-05-22 18:48:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 18:48:11 UTC

- **91,824** saved flights
- **32,612** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,824** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,130,117.9 tonnes** estimated CO2 emissions
- **65,514,082 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3899 |
| 2 | SkyWest Airlines | 3395 |
| 3 | IndiGo | 1913 |
| 4 | EJA | 1740 |
| 5 | American Airlines | 1393 |
| 6 | Southwest Airlines | 1327 |
| 7 | ENY | 1132 |
| 8 | Lufthansa | 1123 |
| 9 | Delta Air Lines | 1005 |
| 10 | Vueling | 876 |
| 11 | LATAM Airlines | 820 |
| 12 | AXM | 806 |
| 13 | WIF | 806 |
| 14 | AZU | 729 |
| 15 | LXJ | 696 |
| 16 | Swiss International | 691 |
| 17 | All Nippon Airways | 685 |
| 18 | Alaska Airlines | 645 |
| 19 | QLK | 644 |
| 20 | easyJet | 599 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 558 |
| 24 | VIV | 545 |
| 25 | Air France | 539 |
| 26 | Japan Airlines | 484 |
| 27 | CXK | 483 |
| 28 | MXY | 474 |
| 29 | AXB | 466 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 75852 |
| 2 | 🇪🇸 ES | 6485 |
| 3 | 🇮🇳 IN | 6013 |
| 4 | 🇦🇺 AU | 5690 |
| 5 | 🇩🇪 DE | 5047 |
| 6 | 🇧🇷 BR | 5021 |
| 7 | 🇮🇹 IT | 5017 |
| 8 | 🇨🇦 CA | 4627 |
| 9 | 🇯🇵 JP | 4444 |
| 10 | 🇬🇧 GB | 3920 |
| 11 | 🇫🇷 FR | 3709 |
| 12 | 🇨🇴 CO | 3170 |
| 13 | 🇲🇽 MX | 2833 |
| 14 | 🇬🇷 GR | 2624 |
| 15 | 🇳🇴 NO | 2572 |
| 16 | 🇨🇭 CH | 2405 |
| 17 | 🇲🇾 MY | 2033 |
| 18 | 🇹🇷 TR | 1670 |
| 19 | 🇿🇦 ZA | 1667 |
| 20 | 🇳🇿 NZ | 1571 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1503 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1398 |
| 25 | 🇬🇹 GT | 1377 |
| 26 | 🇲🇦 MA | 1057 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇳🇱 NL | 927 |
| 29 | 🇲🇪 ME | 924 |
| 30 | 🇭🇷 HR | 830 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1995 |
| 2 | Denver International Airport |  | US | 1539 |
| 3 | Tokyo International Airport |  | JP | 1480 |
| 4 | Indira Gandhi International Airport |  | IN | 1305 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1230 |
| 6 | Harry Reid International Airport |  | US | 1177 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1103 |
| 9 | Zurich Airport |  | CH | 1078 |
| 10 | La Aurora Airport |  | GT | 1052 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1006 |
| 13 | El Dorado International Airport |  | CO | 998 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 921 |
| 15 | Chicago O'Hare International Airport |  | US | 880 |
| 16 | Madrid Barajas International Airport |  | ES | 830 |
| 17 | Kuala Lumpur International Airport |  | MY | 805 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 771 |
| 20 | Capua Airport |  | IT | 768 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 739 |
| 22 | Malpensa International Airport |  | IT | 734 |
| 23 | Bengaluru International Airport |  | IN | 724 |
| 24 | Charles de Gaulle International Airport |  | FR | 717 |
| 25 | Charlotte/Douglas International Airport |  | US | 704 |
| 26 | Congonhas Airport |  | BR | 701 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 641 |
| 30 | Barcelona International Airport |  | ES | 620 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 609 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 599 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 577 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | Amsterdam Airport Schiphol |  | NL | 568 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 546 |
| 40 | O. R. Tambo International Airport |  | ZA | 528 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 452 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 240 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 235 | 1h 26m | 910 km | 3,687.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 232 | 28m | 304 km | 1,216.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 211 | 1h 10m | 770 km | 2,803.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 199 | 19m | 165 km | 566.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 150 | 21m | 99 km | 256.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 137 | 27m | 215 km | 507.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 132 | 14m | 154 km | 349.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 126 | 20m | 250 km | 544.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 118 | 1h 1m | 695 km | 1,414.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK613 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-05-22 17:21 UTC | 2026-05-22 18:48 UTC | 1h 26m |
| N66266 |  | Penn Yan/Yates County Airport (KPEO) | Penn Yan/Yates County Airport (KPEO) | 2026-05-22 18:32 UTC | 2026-05-22 18:42 UTC | 10m |
| CFOCS | CFO | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-05-22 18:05 UTC | 2026-05-22 18:42 UTC | 36m |
| N331RF |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Leoville Airport (CJT9) | 2026-05-22 17:34 UTC | 2026-05-22 18:42 UTC | 1h 7m |
| LXJ448 | LXJ | Miami-Opa Locka Executive Airport (KOPF) | Toronto Pearson International Airport (CYYZ) | 2026-05-22 15:47 UTC | 2026-05-22 18:41 UTC | 2h 53m |
| BOE422 | BOE | Boeing Field/King County International Airport (KBFI) | Hoverhawk Ranch Airport (WN17) | 2026-05-22 18:23 UTC | 2026-05-22 18:39 UTC | 16m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-22 18:01 UTC | 2026-05-22 18:37 UTC | 36m |
| N53402 |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-05-22 18:27 UTC | 2026-05-22 18:37 UTC | 10m |
| N544SP |  | Caldwell Executive Airport (KEUL) | High Valley Airport (ID35) | 2026-05-22 18:08 UTC | 2026-05-22 18:37 UTC | 29m |
| HNW900 | HNW | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-05-22 17:47 UTC | 2026-05-22 18:34 UTC | 47m |
| ERU41 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-05-22 18:06 UTC | 2026-05-22 18:31 UTC | 25m |
| N253EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-22 17:37 UTC | 2026-05-22 18:31 UTC | 53m |
| CGDOQ | CGD | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-05-22 18:03 UTC | 2026-05-22 18:30 UTC | 26m |
| N251SF |  | Dupage Airport (KDPA) | Jack W Watson Airport (0IL9) | 2026-05-22 18:16 UTC | 2026-05-22 18:30 UTC | 13m |
| CGTVB | CGT | Victoria International Airport (CYYJ) | Alert Bay Airport (CYAL) | 2026-05-22 17:21 UTC | 2026-05-22 18:26 UTC | 1h 4m |
| N5283K |  | Harvey's Acres Airport (OR28) | Cottage Grove State Airport (K61S) | 2026-05-22 17:20 UTC | 2026-05-22 18:24 UTC | 1h 4m |
| FTO115 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-05-22 17:47 UTC | 2026-05-22 18:19 UTC | 32m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-05-22 17:31 UTC | 2026-05-22 18:18 UTC | 47m |
| N64RU |  | San Rafael Airport (CA35) | Yolo County Airport (KDWA) | 2026-05-22 17:32 UTC | 2026-05-22 18:17 UTC | 45m |
| N96LS |  | Sky Ranch At Carefree Airport (18AZ) | Payson Airport (KPAN) | 2026-05-22 17:55 UTC | 2026-05-22 18:16 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
