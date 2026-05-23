# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_18:30:09_UTC-green)

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

**Latest saved flight:** 2026-05-23 18:30:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 18:30:09 UTC

- **92,991** saved flights
- **32,943** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,991** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,143,589.7 tonnes** estimated CO2 emissions
- **66,295,054 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3931 |
| 2 | SkyWest Airlines | 3444 |
| 3 | IndiGo | 1935 |
| 4 | EJA | 1763 |
| 5 | American Airlines | 1408 |
| 6 | Southwest Airlines | 1345 |
| 7 | ENY | 1150 |
| 8 | Lufthansa | 1129 |
| 9 | Delta Air Lines | 1019 |
| 10 | Vueling | 885 |
| 11 | LATAM Airlines | 827 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 742 |
| 15 | LXJ | 704 |
| 16 | Swiss International | 695 |
| 17 | All Nippon Airways | 689 |
| 18 | Alaska Airlines | 648 |
| 19 | QLK | 648 |
| 20 | easyJet | 608 |
| 21 | EJU | 596 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 564 |
| 24 | VIV | 552 |
| 25 | Air France | 546 |
| 26 | CXK | 495 |
| 27 | MXY | 488 |
| 28 | Japan Airlines | 487 |
| 29 | AXB | 472 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76876 |
| 2 | 🇪🇸 ES | 6535 |
| 3 | 🇮🇳 IN | 6099 |
| 4 | 🇦🇺 AU | 5730 |
| 5 | 🇩🇪 DE | 5110 |
| 6 | 🇧🇷 BR | 5090 |
| 7 | 🇮🇹 IT | 5059 |
| 8 | 🇨🇦 CA | 4711 |
| 9 | 🇯🇵 JP | 4476 |
| 10 | 🇬🇧 GB | 3962 |
| 11 | 🇫🇷 FR | 3751 |
| 12 | 🇨🇴 CO | 3229 |
| 13 | 🇲🇽 MX | 2862 |
| 14 | 🇬🇷 GR | 2668 |
| 15 | 🇳🇴 NO | 2583 |
| 16 | 🇨🇭 CH | 2432 |
| 17 | 🇲🇾 MY | 2065 |
| 18 | 🇹🇷 TR | 1709 |
| 19 | 🇿🇦 ZA | 1683 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1571 |
| 22 | 🇵🇱 PL | 1520 |
| 23 | 🇰🇷 KR | 1475 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1401 |
| 26 | 🇲🇦 MA | 1065 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 933 |
| 29 | 🇲🇪 ME | 929 |
| 30 | 🇭🇷 HR | 841 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2015 |
| 2 | Denver International Airport |  | US | 1560 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1328 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1239 |
| 6 | Harry Reid International Airport |  | US | 1198 |
| 7 | Frankfurt am Main International Airport |  | DE | 1139 |
| 8 | Guaymaral Airport |  | CO | 1123 |
| 9 | Zurich Airport |  | CH | 1086 |
| 10 | La Aurora Airport |  | GT | 1069 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1019 |
| 13 | El Dorado International Airport |  | CO | 1015 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 931 |
| 15 | Chicago O'Hare International Airport |  | US | 886 |
| 16 | Madrid Barajas International Airport |  | ES | 834 |
| 17 | Kuala Lumpur International Airport |  | MY | 815 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 786 |
| 19 | Salt Lake City International Airport |  | US | 780 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 738 |
| 23 | Bengaluru International Airport |  | IN | 734 |
| 24 | Charles de Gaulle International Airport |  | FR | 727 |
| 25 | Charlotte/Douglas International Airport |  | US | 710 |
| 26 | Congonhas Airport |  | BR | 707 |
| 27 | Daniel K Inouye International Airport |  | US | 672 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 626 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 619 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 605 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 598 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 586 |
| 35 | Vitoria/Foronda Airport |  | ES | 583 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 573 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 551 |
| 40 | O. R. Tambo International Airport |  | ZA | 533 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 461 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 344 | 21m | 244 km | 1,448.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 245 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 113 | 1h 40m | 1,156 km | 2,254.3 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N506KB |  | City Of Colorado Springs Municipal Airport (KCOS) | Pinon Canyon Airport (0CD5) | 2026-05-23 17:52 UTC | 2026-05-23 18:30 UTC | 38m |
| N353CT |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-05-23 17:37 UTC | 2026-05-23 18:28 UTC | 50m |
| CHX29 | CHX | Hamburg-Finkenwerder Airport (EDHI) | Hamburg Airport (EDDH) | 2026-05-23 18:06 UTC | 2026-05-23 18:27 UTC | 20m |
| N475RC |  | Wisky Ranch/Chevlon Airport (6AZ2) | Wisky Ranch/Chevlon Airport (6AZ2) | 2026-05-23 18:03 UTC | 2026-05-23 18:25 UTC | 21m |
| N235MT |  | Cape Cod Gateway Airport (KHYA) | Provincetown Municipal Airport (KPVC) | 2026-05-23 18:10 UTC | 2026-05-23 18:23 UTC | 13m |
| N253EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-23 17:21 UTC | 2026-05-23 18:22 UTC | 1h 0m |
| N4928E |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-23 17:42 UTC | 2026-05-23 18:20 UTC | 38m |
| JUMP16 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-05-23 18:03 UTC | 2026-05-23 18:18 UTC | 15m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-05-23 18:09 UTC | 2026-05-23 18:10 UTC | 0m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-23 17:51 UTC | 2026-05-23 18:07 UTC | 16m |
| N38HF |  | Northampton Airport (K7B2) | KHTO (KHTO) | 2026-05-23 17:28 UTC | 2026-05-23 18:05 UTC | 36m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-05-23 17:21 UTC | 2026-05-23 18:02 UTC | 40m |
| N424KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 17:35 UTC | 2026-05-23 18:01 UTC | 25m |
| N4087H |  | Portland-Hillsboro Airport (KHIO) | Newport Municipal Airport (KONP) | 2026-05-23 17:08 UTC | 2026-05-23 18:00 UTC | 52m |
| N738UY |  | Aero Valley Airport (K52F) | Bridgeport Municipal Airport (KXBP) | 2026-05-23 17:26 UTC | 2026-05-23 17:57 UTC | 30m |
| XSR732 | XSR | Monterey Regional Airport (KMRY) | Rocky Mountain Metro Airport (KBJC) | 2026-05-23 15:53 UTC | 2026-05-23 17:56 UTC | 2h 2m |
| CXK613 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-05-23 16:30 UTC | 2026-05-23 17:55 UTC | 1h 25m |
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-05-23 17:42 UTC | 2026-05-23 17:52 UTC | 10m |
| XBHNL | XBH | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-23 17:51 UTC | 2026-05-23 17:52 UTC | 0m |
| N351PC |  | Millard Airport (KMLE) | Ida Grove Municipal Airport (KIDG) | 2026-05-23 17:34 UTC | 2026-05-23 17:52 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
