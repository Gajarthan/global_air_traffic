# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_14:25:33_UTC-green)

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

**Latest saved flight:** 2026-05-29 14:25:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-29 14:25:33 UTC

- **96,528** saved flights
- **33,943** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,528** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,182,166.1 tonnes** estimated CO2 emissions
- **68,531,366 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4056 |
| 2 | SkyWest Airlines | 3582 |
| 3 | IndiGo | 1997 |
| 4 | EJA | 1824 |
| 5 | American Airlines | 1457 |
| 6 | Southwest Airlines | 1402 |
| 7 | ENY | 1186 |
| 8 | Lufthansa | 1153 |
| 9 | Delta Air Lines | 1055 |
| 10 | Vueling | 912 |
| 11 | LATAM Airlines | 865 |
| 12 | WIF | 855 |
| 13 | AXM | 854 |
| 14 | AZU | 779 |
| 15 | LXJ | 734 |
| 16 | Swiss International | 719 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 672 |
| 19 | QLK | 669 |
| 20 | easyJet | 632 |
| 21 | EJU | 614 |
| 22 | Cathay Pacific | 583 |
| 23 | AEE | 581 |
| 24 | VIV | 570 |
| 25 | Air France | 567 |
| 26 | CXK | 517 |
| 27 | MXY | 510 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 488 |
| 30 | AIQ | 465 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79729 |
| 2 | 🇪🇸 ES | 6742 |
| 3 | 🇮🇳 IN | 6308 |
| 4 | 🇦🇺 AU | 5922 |
| 5 | 🇧🇷 BR | 5314 |
| 6 | 🇩🇪 DE | 5295 |
| 7 | 🇮🇹 IT | 5217 |
| 8 | 🇨🇦 CA | 4909 |
| 9 | 🇯🇵 JP | 4599 |
| 10 | 🇬🇧 GB | 4140 |
| 11 | 🇫🇷 FR | 3923 |
| 12 | 🇨🇴 CO | 3345 |
| 13 | 🇲🇽 MX | 2965 |
| 14 | 🇬🇷 GR | 2784 |
| 15 | 🇳🇴 NO | 2715 |
| 16 | 🇨🇭 CH | 2540 |
| 17 | 🇲🇾 MY | 2170 |
| 18 | 🇹🇷 TR | 1791 |
| 19 | 🇿🇦 ZA | 1727 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1639 |
| 22 | 🇰🇷 KR | 1589 |
| 23 | 🇵🇱 PL | 1579 |
| 24 | 🇵🇭 PH | 1455 |
| 25 | 🇬🇹 GT | 1442 |
| 26 | 🇲🇦 MA | 1093 |
| 27 | 🇲🇴 MO | 1040 |
| 28 | 🇳🇱 NL | 971 |
| 29 | 🇲🇪 ME | 948 |
| 30 | 🇭🇷 HR | 876 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2087 |
| 2 | Denver International Airport |  | US | 1632 |
| 3 | Tokyo International Airport |  | JP | 1524 |
| 4 | Indira Gandhi International Airport |  | IN | 1366 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1275 |
| 6 | Harry Reid International Airport |  | US | 1241 |
| 7 | Guaymaral Airport |  | CO | 1186 |
| 8 | Frankfurt am Main International Airport |  | DE | 1162 |
| 9 | Zurich Airport |  | CH | 1127 |
| 10 | La Aurora Airport |  | GT | 1105 |
| 11 | El Dorado International Airport |  | CO | 1041 |
| 12 | Macau International Airport |  | MO | 1040 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1039 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 966 |
| 15 | Chicago O'Hare International Airport |  | US | 926 |
| 16 | Kuala Lumpur International Airport |  | MY | 858 |
| 17 | Madrid Barajas International Airport |  | ES | 854 |
| 18 | Salt Lake City International Airport |  | US | 811 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 809 |
| 20 | Capua Airport |  | IT | 801 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Bengaluru International Airport |  | IN | 755 |
| 23 | Malpensa International Airport |  | IT | 754 |
| 24 | Charles de Gaulle International Airport |  | FR | 749 |
| 25 | Congonhas Airport |  | BR | 735 |
| 26 | Charlotte/Douglas International Airport |  | US | 730 |
| 27 | Daniel K Inouye International Airport |  | US | 686 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 646 |
| 31 | Barcelona International Airport |  | ES | 645 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 623 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 617 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 35 | Don Mueang International Airport |  | TH | 600 |
| 36 | Amsterdam Airport Schiphol |  | NL | 599 |
| 37 | Vitoria/Foronda Airport |  | ES | 595 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 571 |
| 39 | Calgary International Airport |  | CA | 568 |
| 40 | O. R. Tambo International Airport |  | ZA | 550 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 488 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 356 | 21m | 244 km | 1,499.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 256 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 245 | 14m | 114 km | 480.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 139 | 27m | 152 km | 363.3 t |
| 19 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 131 | 20m | 250 km | 565.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 126 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 123 | 1h 39m | 1,156 km | 2,453.8 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N286LH |  | Chester County G O Carlson Airport (KMQS) | Chester County G O Carlson Airport (KMQS) | 2026-05-29 13:35 UTC | 2026-05-29 14:25 UTC | 49m |
| SPSMW | SPS | Poznań-Ławica Airport (EPPO) | Pila Airport (EPPI) | 2026-05-29 13:34 UTC | 2026-05-29 14:22 UTC | 47m |
| FHOKE | FHO | Lille/Marcq-en-Baroeul Airport (LFQO) | Lille/Marcq-en-Baroeul Airport (LFQO) | 2026-05-29 14:03 UTC | 2026-05-29 14:18 UTC | 14m |
| N426RB |  | Double W Airport (3OK7) | Barcus Field (95OK) | 2026-05-29 13:53 UTC | 2026-05-29 14:16 UTC | 22m |
| N255FD |  | Kissimmee Gateway Airport (KISM) | Orlando Executive Airport (KORL) | 2026-05-29 13:18 UTC | 2026-05-29 14:15 UTC | 56m |
| N20BQ |  | Dupage Airport (KDPA) | Jack W Watson Airport (0IL9) | 2026-05-29 13:57 UTC | 2026-05-29 14:14 UTC | 16m |
| N803PT |  | Oakland County International Airport (KPTK) | Oakland County International Airport (KPTK) | 2026-05-29 13:26 UTC | 2026-05-29 14:12 UTC | 46m |
| N506RP |  | Nashville International Airport (KBNA) | Coleman A Young Municipal Airport (KDET) | 2026-05-29 12:58 UTC | 2026-05-29 14:09 UTC | 1h 10m |
| CFYBG | CFY | Barrie-Orillia (Lake Simcoe Regional Airport) (CYLS) | Brampton Airport (CNC3) | 2026-05-29 13:51 UTC | 2026-05-29 14:07 UTC | 16m |
| BB021 |  | Collier/Pine Barren Airpark (FD89) | KNQB (KNQB) | 2026-05-29 13:51 UTC | 2026-05-29 14:04 UTC | 13m |
| N544SF |  | Skypark Airport (KBTF) | Nephi Municipal Airport (KU14) | 2026-05-29 13:14 UTC | 2026-05-29 14:01 UTC | 46m |
| N916NT |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-05-29 13:21 UTC | 2026-05-29 14:01 UTC | 39m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-29 13:50 UTC | 2026-05-29 14:00 UTC | 9m |
| N264MA |  | Hinaman Acres Airport (1PA0) | Sunbury Airport (K71N) | 2026-05-29 13:46 UTC | 2026-05-29 13:59 UTC | 13m |
| RFD9000 | RFD | General Mariano Escobedo International Airport (MMMY) | Plan De Guadalupe International Airport (MMIO) | 2026-05-29 13:12 UTC | 2026-05-29 13:58 UTC | 45m |
| DMMWK | DMM | Werdohl-Kuntrop Airport (EDKW) | Werdohl-Kuntrop Airport (EDKW) | 2026-05-29 13:52 UTC | 2026-05-29 13:57 UTC | 4m |
| FAD3080 | FAD | Maria Montez International Airport (MDBH) | Maria Montez International Airport (MDBH) | 2026-05-29 13:51 UTC | 2026-05-29 13:56 UTC | 5m |
| HOWLR62 | HOW | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-05-29 13:38 UTC | 2026-05-29 13:53 UTC | 15m |
| N342GR |  | Miami Homestead General Aviation Airport (KX51) | Miami Homestead General Aviation Airport (KX51) | 2026-05-29 13:36 UTC | 2026-05-29 13:52 UTC | 16m |
| SMASH51 | SMA | Tularosa Airport (TA31) | Tularosa Airport (TA31) | 2026-05-29 13:49 UTC | 2026-05-29 13:49 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
