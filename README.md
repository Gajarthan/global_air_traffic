# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_14:07:57_UTC-green)

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

**Latest saved flight:** 2026-05-23 14:07:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 14:07:57 UTC

- **92,522** saved flights
- **32,801** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,522** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,138,023.5 tonnes** estimated CO2 emissions
- **65,972,379 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3919 |
| 2 | SkyWest Airlines | 3425 |
| 3 | IndiGo | 1928 |
| 4 | EJA | 1753 |
| 5 | American Airlines | 1401 |
| 6 | Southwest Airlines | 1334 |
| 7 | ENY | 1139 |
| 8 | Lufthansa | 1125 |
| 9 | Delta Air Lines | 1012 |
| 10 | Vueling | 881 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 738 |
| 15 | LXJ | 700 |
| 16 | Swiss International | 694 |
| 17 | All Nippon Airways | 689 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 605 |
| 21 | EJU | 589 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 560 |
| 24 | VIV | 549 |
| 25 | Air France | 542 |
| 26 | CXK | 488 |
| 27 | Japan Airlines | 487 |
| 28 | MXY | 483 |
| 29 | AXB | 471 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76378 |
| 2 | 🇪🇸 ES | 6510 |
| 3 | 🇮🇳 IN | 6074 |
| 4 | 🇦🇺 AU | 5726 |
| 5 | 🇩🇪 DE | 5082 |
| 6 | 🇧🇷 BR | 5064 |
| 7 | 🇮🇹 IT | 5039 |
| 8 | 🇨🇦 CA | 4676 |
| 9 | 🇯🇵 JP | 4474 |
| 10 | 🇬🇧 GB | 3942 |
| 11 | 🇫🇷 FR | 3735 |
| 12 | 🇨🇴 CO | 3213 |
| 13 | 🇲🇽 MX | 2850 |
| 14 | 🇬🇷 GR | 2644 |
| 15 | 🇳🇴 NO | 2580 |
| 16 | 🇨🇭 CH | 2424 |
| 17 | 🇲🇾 MY | 2065 |
| 18 | 🇹🇷 TR | 1694 |
| 19 | 🇿🇦 ZA | 1679 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1571 |
| 22 | 🇵🇱 PL | 1513 |
| 23 | 🇰🇷 KR | 1475 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1393 |
| 26 | 🇲🇦 MA | 1060 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 931 |
| 29 | 🇲🇪 ME | 929 |
| 30 | 🇭🇷 HR | 837 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2006 |
| 2 | Denver International Airport |  | US | 1553 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1323 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1233 |
| 6 | Harry Reid International Airport |  | US | 1191 |
| 7 | Frankfurt am Main International Airport |  | DE | 1134 |
| 8 | Guaymaral Airport |  | CO | 1117 |
| 9 | Zurich Airport |  | CH | 1085 |
| 10 | La Aurora Airport |  | GT | 1064 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1012 |
| 13 | El Dorado International Airport |  | CO | 1010 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 926 |
| 15 | Chicago O'Hare International Airport |  | US | 883 |
| 16 | Madrid Barajas International Airport |  | ES | 832 |
| 17 | Kuala Lumpur International Airport |  | MY | 815 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 769 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 738 |
| 23 | Bengaluru International Airport |  | IN | 731 |
| 24 | Charles de Gaulle International Airport |  | FR | 722 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 704 |
| 27 | Daniel K Inouye International Airport |  | US | 669 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 623 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 614 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 603 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 598 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 579 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 571 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 549 |
| 40 | O. R. Tambo International Airport |  | ZA | 531 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 459 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 341 | 21m | 244 km | 1,435.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 127 | 20m | 250 km | 548.6 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK284 | CXK | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-23 12:34 UTC | 2026-05-23 14:07 UTC | 1h 33m |
| ERU854 | ERU | Daytona Beach International Airport (KDAB) | FL47 (FL47) | 2026-05-23 13:28 UTC | 2026-05-23 14:05 UTC | 37m |
| SPTIR | SPT | Babice Airport (EPBC) | Babice Airport (EPBC) | 2026-05-23 12:39 UTC | 2026-05-23 14:02 UTC | 1h 22m |
| GFA018 | Gulf Air | Charles de Gaulle International Airport (LFPG) | Queen Alia International Airport (OJAI) | 2026-05-23 10:04 UTC | 2026-05-23 14:01 UTC | 3h 56m |
| PJZ600 | PJZ | Friedrichshafen Airport (EDNY) | Friedrichshafen Airport (EDNY) | 2026-05-23 13:10 UTC | 2026-05-23 13:44 UTC | 33m |
| QTR88E | Qatar Airways | Mikonos Airport (LGMK) | Queen Alia International Airport (OJAI) | 2026-05-23 12:19 UTC | 2026-05-23 13:43 UTC | 1h 24m |
| EJA960 | EJA | Destin Executive Airport (KDTS) | Auburn University Regional Airport (KAUO) | 2026-05-23 13:02 UTC | 2026-05-23 13:40 UTC | 37m |
|  |  | 3IS7 (3IS7) | 3IS7 (3IS7) | 2026-05-23 13:40 UTC | 2026-05-23 13:40 UTC | 0m |
| CGXWM | CGX | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-05-23 13:15 UTC | 2026-05-23 13:39 UTC | 24m |
| N1286C |  | Falcon Field (KFFZ) | San Carlos Apache Airport (KP13) | 2026-05-23 13:12 UTC | 2026-05-23 13:34 UTC | 21m |
| ZUMTS | ZUM | Grand Central Airport (FAGC) | Grand Central Airport (FAGC) | 2026-05-23 13:06 UTC | 2026-05-23 13:32 UTC | 26m |
| N250CR |  | XA65 (XA65) | Tilghman Airport (97XS) | 2026-05-23 13:11 UTC | 2026-05-23 13:28 UTC | 16m |
| SPSAKP | SPS | Warsaw Chopin Airport (EPWA) | Warsaw Chopin Airport (EPWA) | 2026-05-23 12:59 UTC | 2026-05-23 13:27 UTC | 28m |
| GRAZE | GRA | White Waltham Airfield (EGLM) | White Waltham Airfield (EGLM) | 2026-05-23 12:41 UTC | 2026-05-23 13:26 UTC | 44m |
| HK2078G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-23 12:49 UTC | 2026-05-23 13:25 UTC | 35m |
| MGSIR | MGS | Linate Airport (LIML) | Cardak Airport (LTAY) | 2026-05-23 11:02 UTC | 2026-05-23 13:22 UTC | 2h 20m |
| DNC7AC | DNC | La Axarquia-Leoni Benabu Airport (LEAX) | La Axarquia-Leoni Benabu Airport (LEAX) | 2026-05-23 13:18 UTC | 2026-05-23 13:22 UTC | 3m |
| N476SP |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-05-23 13:20 UTC | 2026-05-23 13:21 UTC | 1m |
| N1180M |  | Deep Forest Airport (FD48) | Deep Forest Airport (FD48) | 2026-05-23 13:06 UTC | 2026-05-23 13:19 UTC | 13m |
| FDB746 | flydubai | Tirana International Airport Mother Teresa (LATI) | Queen Alia International Airport (OJAI) | 2026-05-23 11:10 UTC | 2026-05-23 13:19 UTC | 2h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
