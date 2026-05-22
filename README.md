# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_16:56:02_UTC-green)

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

**Latest saved flight:** 2026-05-22 16:56:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 16:56:02 UTC

- **91,571** saved flights
- **32,525** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,571** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,127,794.9 tonnes** estimated CO2 emissions
- **65,379,415 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3892 |
| 2 | SkyWest Airlines | 3385 |
| 3 | IndiGo | 1913 |
| 4 | EJA | 1733 |
| 5 | American Airlines | 1390 |
| 6 | Southwest Airlines | 1326 |
| 7 | ENY | 1127 |
| 8 | Lufthansa | 1121 |
| 9 | Delta Air Lines | 1003 |
| 10 | Vueling | 873 |
| 11 | LATAM Airlines | 819 |
| 12 | AXM | 806 |
| 13 | WIF | 804 |
| 14 | AZU | 725 |
| 15 | LXJ | 692 |
| 16 | Swiss International | 691 |
| 17 | All Nippon Airways | 685 |
| 18 | Alaska Airlines | 645 |
| 19 | QLK | 644 |
| 20 | easyJet | 597 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 558 |
| 24 | VIV | 544 |
| 25 | Air France | 539 |
| 26 | Japan Airlines | 484 |
| 27 | CXK | 482 |
| 28 | MXY | 471 |
| 29 | AXB | 466 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 75534 |
| 2 | 🇪🇸 ES | 6470 |
| 3 | 🇮🇳 IN | 6012 |
| 4 | 🇦🇺 AU | 5690 |
| 5 | 🇩🇪 DE | 5038 |
| 6 | 🇧🇷 BR | 5007 |
| 7 | 🇮🇹 IT | 5007 |
| 8 | 🇨🇦 CA | 4608 |
| 9 | 🇯🇵 JP | 4444 |
| 10 | 🇬🇧 GB | 3909 |
| 11 | 🇫🇷 FR | 3695 |
| 12 | 🇨🇴 CO | 3168 |
| 13 | 🇲🇽 MX | 2823 |
| 14 | 🇬🇷 GR | 2623 |
| 15 | 🇳🇴 NO | 2567 |
| 16 | 🇨🇭 CH | 2402 |
| 17 | 🇲🇾 MY | 2033 |
| 18 | 🇹🇷 TR | 1666 |
| 19 | 🇿🇦 ZA | 1665 |
| 20 | 🇳🇿 NZ | 1571 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1500 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1398 |
| 25 | 🇬🇹 GT | 1372 |
| 26 | 🇲🇦 MA | 1051 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇳🇱 NL | 926 |
| 29 | 🇲🇪 ME | 924 |
| 30 | 🇭🇷 HR | 829 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1990 |
| 2 | Denver International Airport |  | US | 1535 |
| 3 | Tokyo International Airport |  | JP | 1480 |
| 4 | Indira Gandhi International Airport |  | IN | 1304 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1230 |
| 6 | Harry Reid International Airport |  | US | 1174 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1101 |
| 9 | Zurich Airport |  | CH | 1077 |
| 10 | La Aurora Airport |  | GT | 1048 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1004 |
| 13 | El Dorado International Airport |  | CO | 998 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 921 |
| 15 | Chicago O'Hare International Airport |  | US | 876 |
| 16 | Madrid Barajas International Airport |  | ES | 828 |
| 17 | Kuala Lumpur International Airport |  | MY | 805 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 776 |
| 19 | Salt Lake City International Airport |  | US | 771 |
| 20 | Capua Airport |  | IT | 766 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 739 |
| 22 | Malpensa International Airport |  | IT | 733 |
| 23 | Bengaluru International Airport |  | IN | 724 |
| 24 | Charles de Gaulle International Airport |  | FR | 717 |
| 25 | Charlotte/Douglas International Airport |  | US | 704 |
| 26 | Congonhas Airport |  | BR | 699 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 641 |
| 30 | Barcelona International Airport |  | ES | 618 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 608 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 597 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 577 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | Amsterdam Airport Schiphol |  | NL | 567 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 545 |
| 40 | O. R. Tambo International Airport |  | ZA | 527 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 451 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 239 | 9m | - | - |
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
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 132 | 14m | 154 km | 349.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 125 | 20m | 250 km | 539.9 t |
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
| N365ES |  | Cable Airport (KCCB) | Riverside Airport (KRAL) | 2026-05-22 16:45 UTC | 2026-05-22 16:56 UTC | 11m |
| SWA3400 | Southwest Airlines | Chicago Midway International Airport (KMDW) | 84OL (84OL) | 2026-05-22 15:28 UTC | 2026-05-22 16:51 UTC | 1h 23m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-05-22 16:44 UTC | 2026-05-22 16:49 UTC | 5m |
| N5331F |  | Sky Manor Airport (KN40) | Jugtown Mountain Airport (2NJ1) | 2026-05-22 16:26 UTC | 2026-05-22 16:46 UTC | 19m |
| 19MF |  | Coleman A Young Municipal Airport (KDET) | K8M8 (K8M8) | 2026-05-22 16:18 UTC | 2026-05-22 16:45 UTC | 27m |
| N5473R |  | Ralph M Hall/Rockwall Municipal Airport (KF46) | Van Zandt County Regional Airport (K76F) | 2026-05-22 16:31 UTC | 2026-05-22 16:44 UTC | 13m |
| TRF542 | TRF | Addison Airport (KADS) | Caddo Mills Municipal Airport (K7F3) | 2026-05-22 15:51 UTC | 2026-05-22 16:44 UTC | 53m |
| ERU96 | ERU | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-05-22 16:14 UTC | 2026-05-22 16:38 UTC | 24m |
| N851TA |  | Fullerton Municipal Airport (KFUL) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-22 16:02 UTC | 2026-05-22 16:38 UTC | 35m |
| AFR53FU | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-05-22 15:54 UTC | 2026-05-22 16:38 UTC | 43m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-22 16:20 UTC | 2026-05-22 16:35 UTC | 15m |
| N327TM |  | Henderson Executive Airport (KHND) | Willow Springs Ranch Airport (1AZ8) | 2026-05-22 16:02 UTC | 2026-05-22 16:35 UTC | 32m |
| VAR448 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-05-22 16:18 UTC | 2026-05-22 16:34 UTC | 15m |
| NGF7510 | NGF | 6CL9 (6CL9) | Palo Alto Airport (KPAO) | 2026-05-22 15:41 UTC | 2026-05-22 16:33 UTC | 52m |
| NSZ8MV | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-05-22 15:37 UTC | 2026-05-22 16:32 UTC | 54m |
| N7293R |  | Concord Municipal Airport (KCON) | Concord Municipal Airport (KCON) | 2026-05-22 16:08 UTC | 2026-05-22 16:29 UTC | 21m |
| OKBLT | OKB | Nymburk Ul Ploch Airport (LKNY) | Nymburk Ul Ploch Airport (LKNY) | 2026-05-22 15:39 UTC | 2026-05-22 16:28 UTC | 49m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-05-22 15:41 UTC | 2026-05-22 16:27 UTC | 45m |
| OKAUI77 | OKA | Zamberk Airport (LKZM) | Jaromer Airport (LKJA) | 2026-05-22 16:14 UTC | 2026-05-22 16:27 UTC | 12m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-05-22 13:02 UTC | 2026-05-22 16:26 UTC | 3h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
