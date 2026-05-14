# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_18:57:41_UTC-green)

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

**Latest saved flight:** 2026-05-14 18:57:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 18:57:41 UTC

- **82,182** saved flights
- **29,778** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,182** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,011,179.1 tonnes** estimated CO2 emissions
- **58,619,076 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3528 |
| 2 | SkyWest Airlines | 3040 |
| 3 | IndiGo | 1800 |
| 4 | EJA | 1540 |
| 5 | American Airlines | 1265 |
| 6 | Southwest Airlines | 1201 |
| 7 | Lufthansa | 1062 |
| 8 | ENY | 1027 |
| 9 | Delta Air Lines | 899 |
| 10 | Vueling | 777 |
| 11 | AXM | 746 |
| 12 | LATAM Airlines | 743 |
| 13 | WIF | 716 |
| 14 | All Nippon Airways | 646 |
| 15 | AZU | 646 |
| 16 | Swiss International | 641 |
| 17 | QLK | 608 |
| 18 | LXJ | 596 |
| 19 | Alaska Airlines | 579 |
| 20 | easyJet | 546 |
| 21 | EJU | 528 |
| 22 | AEE | 524 |
| 23 | Cathay Pacific | 510 |
| 24 | VIV | 488 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 442 |
| 28 | CXK | 430 |
| 29 | MXY | 408 |
| 30 | United Airlines | 408 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67033 |
| 2 | 🇪🇸 ES | 5828 |
| 3 | 🇮🇳 IN | 5625 |
| 4 | 🇦🇺 AU | 5263 |
| 5 | 🇩🇪 DE | 4615 |
| 6 | 🇮🇹 IT | 4550 |
| 7 | 🇧🇷 BR | 4536 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4087 |
| 10 | 🇬🇧 GB | 3513 |
| 11 | 🇫🇷 FR | 3273 |
| 12 | 🇨🇴 CO | 2738 |
| 13 | 🇲🇽 MX | 2487 |
| 14 | 🇬🇷 GR | 2397 |
| 15 | 🇳🇴 NO | 2308 |
| 16 | 🇨🇭 CH | 2202 |
| 17 | 🇲🇾 MY | 1874 |
| 18 | 🇿🇦 ZA | 1550 |
| 19 | 🇹🇷 TR | 1461 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1438 |
| 22 | 🇵🇱 PL | 1371 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇬🇹 GT | 1256 |
| 25 | 🇰🇷 KR | 1252 |
| 26 | 🇲🇦 MA | 960 |
| 27 | 🇲🇴 MO | 940 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 847 |
| 30 | 🇭🇷 HR | 735 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1801 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1377 |
| 4 | Indira Gandhi International Airport |  | IN | 1193 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1172 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1021 |
| 8 | Zurich Airport |  | CH | 980 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 940 |
| 11 | Guaymaral Airport |  | CO | 924 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 920 |
| 13 | El Dorado International Airport |  | CO | 881 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 825 |
| 15 | Chicago O'Hare International Airport |  | US | 796 |
| 16 | Madrid Barajas International Airport |  | ES | 753 |
| 17 | Kuala Lumpur International Airport |  | MY | 748 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 717 |
| 19 | Malpensa International Airport |  | IT | 693 |
| 20 | Bengaluru International Airport |  | IN | 691 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 22 | Salt Lake City International Airport |  | US | 675 |
| 23 | Capua Airport |  | IT | 672 |
| 24 | Charles de Gaulle International Airport |  | FR | 645 |
| 25 | Charlotte/Douglas International Airport |  | US | 640 |
| 26 | Congonhas Airport |  | BR | 638 |
| 27 | Tenerife Norte Airport |  | ES | 600 |
| 28 | Ninoy Aquino International Airport |  | PH | 596 |
| 29 | Daniel K Inouye International Airport |  | US | 595 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 551 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 550 |
| 33 | Barcelona International Airport |  | ES | 550 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 532 |
| 35 | Don Mueang International Airport |  | TH | 518 |
| 36 | Vitoria/Foronda Airport |  | ES | 516 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 514 |
| 38 | Amsterdam Airport Schiphol |  | NL | 511 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 482 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 297 | 21m | 244 km | 1,250.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 112 | 23m | 55 km | 106.5 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 111 | 1h 2m | 695 km | 1,330.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 104 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFTHS | CFT | Montréal / St-Hubert Airport (CYHU) | Montréal / St-Hubert Airport (CYHU) | 2026-05-14 17:59 UTC | 2026-05-14 18:57 UTC | 58m |
| N820AB |  | Deland Municipal-Sidney H Taylor Field (KDED) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-05-14 18:08 UTC | 2026-05-14 18:50 UTC | 41m |
| TORA81 | TOR | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-05-14 18:30 UTC | 2026-05-14 18:47 UTC | 17m |
| N869SF |  | Cleveland Regional Jetport Airport (KRZR) | Cleveland Regional Jetport Airport (KRZR) | 2026-05-14 18:37 UTC | 2026-05-14 18:44 UTC | 7m |
| N630FB |  | Phoenix Deer Valley Airport (KDVT) | Payson Airport (KPAN) | 2026-05-14 18:17 UTC | 2026-05-14 18:40 UTC | 23m |
| MS3 |  | Skylark Airport (CA89) | Skylark Airport (CA89) | 2026-05-14 18:26 UTC | 2026-05-14 18:39 UTC | 12m |
| TNKR140 | TNK | Grand Junction Regional Airport (KGJT) | Sanpete County Regional Airport (K41U) | 2026-05-14 18:02 UTC | 2026-05-14 18:37 UTC | 35m |
| ACA7116 | Air Canada | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-05-14 18:32 UTC | 2026-05-14 18:36 UTC | 4m |
| CGHHA | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-05-14 18:18 UTC | 2026-05-14 18:36 UTC | 18m |
| N189PC |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-05-14 18:25 UTC | 2026-05-14 18:36 UTC | 10m |
| N730EL |  | Cottonwood Airport (KP52) | Cottonwood Airport (KP52) | 2026-05-14 18:23 UTC | 2026-05-14 18:34 UTC | 10m |
| N900ML |  | California City Municipal Airport (KL71) | Kelso Valley Airport (CN37) | 2026-05-14 18:09 UTC | 2026-05-14 18:33 UTC | 23m |
| KQA109 | KQA | London Gatwick Airport (EGKK) | Nairobi Wilson Airport (HKNW) | 2026-05-14 10:33 UTC | 2026-05-14 18:31 UTC | 7h 57m |
| N8306D |  | Centennial Airport (KAPA) | Limon Municipal Airport (KLIC) | 2026-05-14 18:04 UTC | 2026-05-14 18:31 UTC | 26m |
| N415XT |  | Charles M Schulz/Sonoma County Airport (KSTS) | Salina Regional Airport (KSLN) | 2026-05-14 14:09 UTC | 2026-05-14 18:30 UTC | 4h 21m |
| N698FL |  | Falcon Field (KFFZ) | 42AZ (42AZ) | 2026-05-14 17:51 UTC | 2026-05-14 18:29 UTC | 37m |
| JJ71 |  | Pensacola International Airport (KPNS) | K4R4 (K4R4) | 2026-05-14 17:58 UTC | 2026-05-14 18:27 UTC | 28m |
| N784CA |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-05-14 18:03 UTC | 2026-05-14 18:26 UTC | 23m |
| SIS49 | SIS | Van Nuys Airport (KVNY) | Meadows Field (KBFL) | 2026-05-14 18:06 UTC | 2026-05-14 18:26 UTC | 20m |
| N350TF |  | Lake Havasu City Airport (KHII) | H A Clark Memorial Field (KCMR) | 2026-05-14 18:01 UTC | 2026-05-14 18:26 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
