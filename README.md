# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_22:51:36_UTC-green)

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

**Latest saved flight:** 2026-05-22 22:51:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 22:51:36 UTC

- **92,129** saved flights
- **32,714** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,129** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,133,131.2 tonnes** estimated CO2 emissions
- **65,688,767 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3906 |
| 2 | SkyWest Airlines | 3422 |
| 3 | IndiGo | 1913 |
| 4 | EJA | 1750 |
| 5 | American Airlines | 1399 |
| 6 | Southwest Airlines | 1332 |
| 7 | ENY | 1139 |
| 8 | Lufthansa | 1123 |
| 9 | Delta Air Lines | 1012 |
| 10 | Vueling | 877 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 806 |
| 13 | WIF | 806 |
| 14 | AZU | 734 |
| 15 | LXJ | 700 |
| 16 | Swiss International | 691 |
| 17 | All Nippon Airways | 685 |
| 18 | Alaska Airlines | 645 |
| 19 | QLK | 644 |
| 20 | easyJet | 603 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 558 |
| 24 | VIV | 546 |
| 25 | Air France | 540 |
| 26 | CXK | 485 |
| 27 | Japan Airlines | 484 |
| 28 | MXY | 478 |
| 29 | AXB | 466 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76240 |
| 2 | 🇪🇸 ES | 6492 |
| 3 | 🇮🇳 IN | 6014 |
| 4 | 🇦🇺 AU | 5691 |
| 5 | 🇩🇪 DE | 5050 |
| 6 | 🇧🇷 BR | 5049 |
| 7 | 🇮🇹 IT | 5025 |
| 8 | 🇨🇦 CA | 4656 |
| 9 | 🇯🇵 JP | 4446 |
| 10 | 🇬🇧 GB | 3928 |
| 11 | 🇫🇷 FR | 3711 |
| 12 | 🇨🇴 CO | 3190 |
| 13 | 🇲🇽 MX | 2840 |
| 14 | 🇬🇷 GR | 2627 |
| 15 | 🇳🇴 NO | 2572 |
| 16 | 🇨🇭 CH | 2407 |
| 17 | 🇲🇾 MY | 2033 |
| 18 | 🇹🇷 TR | 1673 |
| 19 | 🇿🇦 ZA | 1667 |
| 20 | 🇳🇿 NZ | 1577 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1504 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1400 |
| 25 | 🇬🇹 GT | 1389 |
| 26 | 🇲🇦 MA | 1060 |
| 27 | 🇲🇴 MO | 1036 |
| 28 | 🇳🇱 NL | 927 |
| 29 | 🇲🇪 ME | 925 |
| 30 | 🇭🇷 HR | 830 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2004 |
| 2 | Denver International Airport |  | US | 1553 |
| 3 | Tokyo International Airport |  | JP | 1481 |
| 4 | Indira Gandhi International Airport |  | IN | 1306 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1230 |
| 6 | Harry Reid International Airport |  | US | 1187 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1107 |
| 9 | Zurich Airport |  | CH | 1079 |
| 10 | La Aurora Airport |  | GT | 1062 |
| 11 | Macau International Airport |  | MO | 1036 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1011 |
| 13 | El Dorado International Airport |  | CO | 1004 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 924 |
| 15 | Chicago O'Hare International Airport |  | US | 883 |
| 16 | Madrid Barajas International Airport |  | ES | 830 |
| 17 | Kuala Lumpur International Airport |  | MY | 805 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 768 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 740 |
| 22 | Malpensa International Airport |  | IT | 734 |
| 23 | Bengaluru International Airport |  | IN | 724 |
| 24 | Charles de Gaulle International Airport |  | FR | 718 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 703 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 642 |
| 30 | Barcelona International Airport |  | ES | 621 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 610 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 601 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | Amsterdam Airport Schiphol |  | NL | 568 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 548 |
| 40 | O. R. Tambo International Airport |  | ZA | 528 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 454 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 237 | 14m | 114 km | 464.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 235 | 1h 26m | 910 km | 3,687.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 232 | 28m | 304 km | 1,216.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 212 | 1h 10m | 770 km | 2,816.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 199 | 19m | 165 km | 566.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 151 | 21m | 99 km | 258.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 139 | 31m | 369 km | 884.8 t |
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
| SKW5382 | SkyWest Airlines | Louisville Muhammad Ali International Airport (KSDF) | Chicago O'Hare International Airport (KORD) | 2026-05-22 21:57 UTC | 2026-05-22 22:51 UTC | 54m |
| N893AP |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-05-22 22:15 UTC | 2026-05-22 22:40 UTC | 25m |
| CAP4359 | CAP | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-05-22 22:13 UTC | 2026-05-22 22:34 UTC | 21m |
| N107MW |  | Marshdale Airport (CO52) | Marshdale Airport (CO52) | 2026-05-22 21:19 UTC | 2026-05-22 22:34 UTC | 1h 14m |
| N930MG |  | Buchanan Field (KCCR) | Truckee-Tahoe Airport (KTRK) | 2026-05-22 22:09 UTC | 2026-05-22 22:31 UTC | 22m |
| EJA303 | EJA | Westchester County Airport (KHPN) | New River Mcas (Mccutcheon Field) Airport (KNCA) | 2026-05-22 21:21 UTC | 2026-05-22 22:29 UTC | 1h 8m |
| N124ME |  | Iowa City Municipal Airport (KIOW) | Iowa City Municipal Airport (KIOW) | 2026-05-22 21:34 UTC | 2026-05-22 22:29 UTC | 54m |
| ZKHUP | ZKH | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-05-22 22:12 UTC | 2026-05-22 22:27 UTC | 15m |
| 504HW |  | Van Dyke Strip (25CL) | Riego Flight Strip (38CL) | 2026-05-22 21:23 UTC | 2026-05-22 22:23 UTC | 1h 0m |
| N779RJ |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-05-22 21:48 UTC | 2026-05-22 22:22 UTC | 34m |
| CXK362 | CXK | Mckinney Ntl Airport (KTKI) | Casey Field (TE06) | 2026-05-22 21:02 UTC | 2026-05-22 22:21 UTC | 1h 18m |
| N1266U |  | Fort Worth Meacham International Airport (KFTW) | Bridgeport Municipal Airport (KXBP) | 2026-05-22 21:26 UTC | 2026-05-22 22:20 UTC | 54m |
| N4077D |  | Caldwell Executive Airport (KEUL) | Treasure Gulch Airport (22ID) | 2026-05-22 21:54 UTC | 2026-05-22 22:19 UTC | 25m |
| N1708W |  | Al Divine Airport (65CL) | San Carlos Airport (KSQL) | 2026-05-22 21:25 UTC | 2026-05-22 22:18 UTC | 52m |
| N2087E |  | San Gabriel Valley Airport (KEMT) | Brackett Field (KPOC) | 2026-05-22 21:56 UTC | 2026-05-22 22:17 UTC | 20m |
| BRG2622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-05-22 21:30 UTC | 2026-05-22 22:14 UTC | 44m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | Creech Afb Airport (KINS) | 2026-05-22 22:04 UTC | 2026-05-22 22:14 UTC | 10m |
| TEXDOT1 | TEX | Lubbock Preston Smith International Airport (KLBB) | Austin-Bergstrom International Airport (KAUS) | 2026-05-22 21:10 UTC | 2026-05-22 22:13 UTC | 1h 3m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-22 17:58 UTC | 2026-05-22 22:12 UTC | 4h 14m |
| N15MJ |  | Palo Alto Airport (KPAO) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-22 21:22 UTC | 2026-05-22 22:12 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
