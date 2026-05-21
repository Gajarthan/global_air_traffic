# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_20:53:48_UTC-green)

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

**Latest saved flight:** 2026-05-21 20:53:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 20:53:48 UTC

- **90,687** saved flights
- **32,283** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **90,687** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,119,553.7 tonnes** estimated CO2 emissions
- **64,901,664 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3875 |
| 2 | SkyWest Airlines | 3357 |
| 3 | IndiGo | 1901 |
| 4 | EJA | 1718 |
| 5 | American Airlines | 1379 |
| 6 | Southwest Airlines | 1314 |
| 7 | Lufthansa | 1119 |
| 8 | ENY | 1119 |
| 9 | Delta Air Lines | 993 |
| 10 | Vueling | 863 |
| 11 | LATAM Airlines | 816 |
| 12 | AXM | 800 |
| 13 | WIF | 794 |
| 14 | AZU | 720 |
| 15 | Swiss International | 690 |
| 16 | LXJ | 683 |
| 17 | All Nippon Airways | 679 |
| 18 | Alaska Airlines | 641 |
| 19 | QLK | 639 |
| 20 | easyJet | 592 |
| 21 | EJU | 583 |
| 22 | Cathay Pacific | 579 |
| 23 | AEE | 556 |
| 24 | VIV | 537 |
| 25 | Air France | 532 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 478 |
| 28 | MXY | 467 |
| 29 | AXB | 463 |
| 30 | AIQ | 438 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 74772 |
| 2 | 🇪🇸 ES | 6430 |
| 3 | 🇮🇳 IN | 5980 |
| 4 | 🇦🇺 AU | 5618 |
| 5 | 🇩🇪 DE | 5001 |
| 6 | 🇮🇹 IT | 4980 |
| 7 | 🇧🇷 BR | 4972 |
| 8 | 🇨🇦 CA | 4546 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3877 |
| 11 | 🇫🇷 FR | 3643 |
| 12 | 🇨🇴 CO | 3127 |
| 13 | 🇲🇽 MX | 2798 |
| 14 | 🇬🇷 GR | 2608 |
| 15 | 🇳🇴 NO | 2537 |
| 16 | 🇨🇭 CH | 2384 |
| 17 | 🇲🇾 MY | 2011 |
| 18 | 🇹🇷 TR | 1654 |
| 19 | 🇿🇦 ZA | 1647 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1538 |
| 22 | 🇵🇱 PL | 1489 |
| 23 | 🇰🇷 KR | 1417 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1353 |
| 26 | 🇲🇦 MA | 1047 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 920 |
| 29 | 🇳🇱 NL | 919 |
| 30 | 🇭🇷 HR | 823 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1979 |
| 2 | Denver International Airport |  | US | 1523 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1297 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1226 |
| 6 | Harry Reid International Airport |  | US | 1161 |
| 7 | Frankfurt am Main International Airport |  | DE | 1128 |
| 8 | Guaymaral Airport |  | CO | 1083 |
| 9 | Zurich Airport |  | CH | 1073 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1033 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 997 |
| 13 | El Dorado International Airport |  | CO | 987 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 918 |
| 15 | Chicago O'Hare International Airport |  | US | 875 |
| 16 | Madrid Barajas International Airport |  | ES | 824 |
| 17 | Kuala Lumpur International Airport |  | MY | 796 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 774 |
| 19 | Salt Lake City International Airport |  | US | 762 |
| 20 | Capua Airport |  | IT | 761 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 733 |
| 22 | Malpensa International Airport |  | IT | 730 |
| 23 | Bengaluru International Airport |  | IN | 718 |
| 24 | Charles de Gaulle International Airport |  | FR | 709 |
| 25 | Charlotte/Douglas International Airport |  | US | 699 |
| 26 | Congonhas Airport |  | BR | 694 |
| 27 | Tenerife Norte Airport |  | ES | 662 |
| 28 | Daniel K Inouye International Airport |  | US | 661 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 611 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 602 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 593 |
| 34 | Vitoria/Foronda Airport |  | ES | 574 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 573 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 565 |
| 38 | Amsterdam Airport Schiphol |  | NL | 564 |
| 39 | Calgary International Airport |  | CA | 537 |
| 40 | O. R. Tambo International Airport |  | ZA | 521 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 443 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 336 | 21m | 244 km | 1,414.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 234 | 9m | - | - |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 133 | 27m | 152 km | 347.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 117 | 18m | 144 km | 291.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRIBE61 | TRI | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Jeremiah Denton Airport (K4R9) | 2026-05-21 20:29 UTC | 2026-05-21 20:53 UTC | 24m |
| CXK401 | CXK | Rowland Dusters Airport (75XS) | Castroville Municipal Airport (KCVB) | 2026-05-21 20:21 UTC | 2026-05-21 20:52 UTC | 31m |
| G26561 |  | KEDG (KEDG) | KEDG (KEDG) | 2026-05-21 19:43 UTC | 2026-05-21 20:50 UTC | 1h 6m |
| N912PF |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-21 20:31 UTC | 2026-05-21 20:49 UTC | 18m |
| N680EA |  | KHTO (KHTO) | Auburn University Regional Airport (KAUO) | 2026-05-21 18:39 UTC | 2026-05-21 20:49 UTC | 2h 9m |
| 504HW |  | Riego Flight Strip (38CL) | Riego Flight Strip (38CL) | 2026-05-21 18:51 UTC | 2026-05-21 20:48 UTC | 1h 56m |
| BULET42 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-21 19:21 UTC | 2026-05-21 20:46 UTC | 1h 24m |
| N402WD |  | Rabb Dusting Inc Airport (XS66) | Rabb Dusting Inc Airport (XS66) | 2026-05-21 20:18 UTC | 2026-05-21 20:44 UTC | 25m |
| N856MB |  | Athanasiou Valley Airport (CO07) | Elk Park Ranch Airport (34CD) | 2026-05-21 20:20 UTC | 2026-05-21 20:43 UTC | 22m |
| N149AH |  | Ormond Beach Municipal Airport (KOMN) | Orlando Executive Airport (KORL) | 2026-05-21 20:04 UTC | 2026-05-21 20:33 UTC | 28m |
| ATAC21 | ATA | Luke Afb Airport (KLUF) | Sells Airport (KE78) | 2026-05-21 20:11 UTC | 2026-05-21 20:31 UTC | 20m |
| JOLLY71 | JOL | Davidson Strip (45AA) | Sixmile Lake Airport (AA06) | 2026-05-21 19:55 UTC | 2026-05-21 20:30 UTC | 35m |
| N609MW |  | Carson City Airport (KCXP) | Rosaschi Air Park (KN59) | 2026-05-21 20:18 UTC | 2026-05-21 20:30 UTC | 11m |
| N923JK |  | Waukesha County Airport (KUES) | Miller-Herrold Airport (28MI) | 2026-05-21 19:52 UTC | 2026-05-21 20:25 UTC | 32m |
| N93FS |  | Lima Allen County Airport (KAOH) | Roscommon County/Blodgett Memorial Airport (KHTL) | 2026-05-21 19:43 UTC | 2026-05-21 20:19 UTC | 36m |
| 0  YP |  | Whidbey Island Nas (Ault Field) Airport (KNUW) | Chiloquin State Airport (K2S7) | 2026-05-21 19:25 UTC | 2026-05-21 20:18 UTC | 52m |
| N690LA |  | Mobile Regional Airport (KMOB) | Akron-Canton Regional Airport (KCAK) | 2026-05-21 18:33 UTC | 2026-05-21 20:18 UTC | 1h 44m |
| BNOB | BNO | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-05-21 19:44 UTC | 2026-05-21 20:18 UTC | 34m |
| DRAGO64 | DRA | Pau Pyrenees Airport (LFBP) | Tarbes-Lourdes-Pyrenees Airport (LFBT) | 2026-05-21 19:56 UTC | 2026-05-21 20:16 UTC | 19m |
| N8526P |  | Corona Municipal Airport (KAJO) | Hemet-Ryan Airport (KHMT) | 2026-05-21 19:44 UTC | 2026-05-21 20:13 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
