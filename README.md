# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_10:39:02_UTC-green)

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

**Latest saved flight:** 2026-05-24 10:39:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-24 10:39:02 UTC

- **93,571** saved flights
- **33,082** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,571** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,150,865.6 tonnes** estimated CO2 emissions
- **66,716,845 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3948 |
| 2 | SkyWest Airlines | 3474 |
| 3 | IndiGo | 1946 |
| 4 | EJA | 1771 |
| 5 | American Airlines | 1423 |
| 6 | Southwest Airlines | 1357 |
| 7 | ENY | 1159 |
| 8 | Lufthansa | 1132 |
| 9 | Delta Air Lines | 1026 |
| 10 | Vueling | 888 |
| 11 | LATAM Airlines | 835 |
| 12 | AXM | 824 |
| 13 | WIF | 812 |
| 14 | AZU | 742 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 698 |
| 17 | All Nippon Airways | 696 |
| 18 | Alaska Airlines | 653 |
| 19 | QLK | 649 |
| 20 | easyJet | 611 |
| 21 | EJU | 600 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 566 |
| 24 | VIV | 555 |
| 25 | Air France | 551 |
| 26 | CXK | 501 |
| 27 | MXY | 495 |
| 28 | Japan Airlines | 488 |
| 29 | AXB | 476 |
| 30 | AIQ | 453 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77375 |
| 2 | 🇪🇸 ES | 6561 |
| 3 | 🇮🇳 IN | 6144 |
| 4 | 🇦🇺 AU | 5743 |
| 5 | 🇩🇪 DE | 5134 |
| 6 | 🇧🇷 BR | 5115 |
| 7 | 🇮🇹 IT | 5075 |
| 8 | 🇨🇦 CA | 4736 |
| 9 | 🇯🇵 JP | 4509 |
| 10 | 🇬🇧 GB | 3986 |
| 11 | 🇫🇷 FR | 3776 |
| 12 | 🇨🇴 CO | 3250 |
| 13 | 🇲🇽 MX | 2877 |
| 14 | 🇬🇷 GR | 2685 |
| 15 | 🇳🇴 NO | 2597 |
| 16 | 🇨🇭 CH | 2447 |
| 17 | 🇲🇾 MY | 2081 |
| 18 | 🇹🇷 TR | 1724 |
| 19 | 🇿🇦 ZA | 1691 |
| 20 | 🇳🇿 NZ | 1594 |
| 21 | 🇹🇭 TH | 1587 |
| 22 | 🇵🇱 PL | 1530 |
| 23 | 🇰🇷 KR | 1504 |
| 24 | 🇵🇭 PH | 1419 |
| 25 | 🇬🇹 GT | 1409 |
| 26 | 🇲🇦 MA | 1073 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 938 |
| 29 | 🇲🇪 ME | 932 |
| 30 | 🇭🇷 HR | 847 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2030 |
| 2 | Denver International Airport |  | US | 1579 |
| 3 | Tokyo International Airport |  | JP | 1501 |
| 4 | Indira Gandhi International Airport |  | IN | 1339 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1241 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1143 |
| 8 | Guaymaral Airport |  | CO | 1133 |
| 9 | Zurich Airport |  | CH | 1090 |
| 10 | La Aurora Airport |  | GT | 1077 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1023 |
| 13 | El Dorado International Airport |  | CO | 1021 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 936 |
| 15 | Chicago O'Hare International Airport |  | US | 893 |
| 16 | Madrid Barajas International Airport |  | ES | 837 |
| 17 | Kuala Lumpur International Airport |  | MY | 822 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 789 |
| 19 | Salt Lake City International Airport |  | US | 787 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 746 |
| 22 | Malpensa International Airport |  | IT | 741 |
| 23 | Bengaluru International Airport |  | IN | 737 |
| 24 | Charles de Gaulle International Airport |  | FR | 732 |
| 25 | Charlotte/Douglas International Airport |  | US | 713 |
| 26 | Congonhas Airport |  | BR | 709 |
| 27 | Daniel K Inouye International Airport |  | US | 673 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 648 |
| 30 | Barcelona International Airport |  | ES | 629 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 625 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 610 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 594 |
| 35 | Vitoria/Foronda Airport |  | ES | 584 |
| 36 | Don Mueang International Airport |  | TH | 581 |
| 37 | Amsterdam Airport Schiphol |  | NL | 578 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 536 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 465 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 249 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 240 | 1h 26m | 910 km | 3,766.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 237 | 28m | 304 km | 1,242.4 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 215 | 1h 10m | 770 km | 2,856.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 139 | 27m | 215 km | 514.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 136 | 14m | 154 km | 360.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 120 | 1h 1m | 695 km | 1,438.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 115 | 1h 40m | 1,156 km | 2,294.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-05-24 10:28 UTC | 2026-05-24 10:39 UTC | 10m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-24 10:04 UTC | 2026-05-24 10:36 UTC | 32m |
| HBFAN | HBF | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-05-24 10:06 UTC | 2026-05-24 10:34 UTC | 28m |
| QLK26D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-05-24 09:22 UTC | 2026-05-24 10:05 UTC | 42m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-05-24 08:58 UTC | 2026-05-24 09:58 UTC | 1h 0m |
| JJA1406 | JJA | Fukuoka Airport (RJFF) | Incheon International Airport (RKSI) | 2026-05-24 08:59 UTC | 2026-05-24 09:55 UTC | 56m |
| PHPNX | PHP | Alcantarilla Airport (LERI) | Alcantarilla Airport (LERI) | 2026-05-24 08:17 UTC | 2026-05-24 09:54 UTC | 1h 36m |
| AFR68LX | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-05-24 08:52 UTC | 2026-05-24 09:49 UTC | 56m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-05-24 09:35 UTC | 2026-05-24 09:49 UTC | 13m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-24 08:56 UTC | 2026-05-24 09:47 UTC | 51m |
| ANA667 | All Nippon Airways | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-05-24 08:21 UTC | 2026-05-24 09:43 UTC | 1h 21m |
| SFJ85 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-24 08:35 UTC | 2026-05-24 09:43 UTC | 1h 8m |
| ADO87 | ADO | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-05-24 08:32 UTC | 2026-05-24 09:42 UTC | 1h 9m |
| EJU307A | EJU | Paris-Orly Airport (LFPO) | Toulouse-Blagnac Airport (LFBO) | 2026-05-24 08:41 UTC | 2026-05-24 09:41 UTC | 1h 0m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-05-24 08:59 UTC | 2026-05-24 09:40 UTC | 40m |
| VOE50KV | VOE | Toulouse-Blagnac Airport (LFBO) | Sinj Glider Airport (LDSS) | 2026-05-24 08:00 UTC | 2026-05-24 09:40 UTC | 1h 39m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-05-24 07:25 UTC | 2026-05-24 09:38 UTC | 2h 12m |
| SWR9YD | Swiss International | Budapest Ferenc Liszt International Airport (LHBP) | Zurich Airport (LSZH) | 2026-05-24 08:16 UTC | 2026-05-24 09:37 UTC | 1h 20m |
| AUA823H | Austrian Airlines | Vienna International Airport (LOWW) | Thessaloniki Macedonia International Airport (LGTS) | 2026-05-24 08:12 UTC | 2026-05-24 09:36 UTC | 1h 23m |
| AFR89YP | Air France | Charles de Gaulle International Airport (LFPG) | Otocac Airport (LDRO) | 2026-05-24 08:05 UTC | 2026-05-24 09:35 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
