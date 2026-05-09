# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_23:49:52_UTC-green)

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

**Latest saved flight:** 2026-05-08 23:49:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 23:49:52 UTC

- **74,703** saved flights
- **27,609** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,703** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **919,291.8 tonnes** estimated CO2 emissions
- **53,292,281 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3201 |
| 2 | SkyWest Airlines | 2786 |
| 3 | IndiGo | 1664 |
| 4 | EJA | 1387 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1086 |
| 7 | Lufthansa | 963 |
| 8 | ENY | 937 |
| 9 | Vueling | 725 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 693 |
| 12 | Delta Air Lines | 686 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 601 |
| 16 | QLK | 576 |
| 17 | Swiss International | 566 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 526 |
| 20 | easyJet | 490 |
| 21 | EJU | 479 |
| 22 | AEE | 478 |
| 23 | Cathay Pacific | 469 |
| 24 | VIV | 453 |
| 25 | Japan Airlines | 436 |
| 26 | Air France | 431 |
| 27 | AXB | 411 |
| 28 | CXK | 383 |
| 29 | AIQ | 366 |
| 30 | MXY | 363 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60319 |
| 2 | 🇪🇸 ES | 5376 |
| 3 | 🇮🇳 IN | 5233 |
| 4 | 🇦🇺 AU | 4921 |
| 5 | 🇧🇷 BR | 4195 |
| 6 | 🇩🇪 DE | 4169 |
| 7 | 🇮🇹 IT | 4062 |
| 8 | 🇯🇵 JP | 3881 |
| 9 | 🇨🇦 CA | 3736 |
| 10 | 🇬🇧 GB | 3197 |
| 11 | 🇫🇷 FR | 2940 |
| 12 | 🇨🇴 CO | 2690 |
| 13 | 🇲🇽 MX | 2319 |
| 14 | 🇬🇷 GR | 2198 |
| 15 | 🇳🇴 NO | 2076 |
| 16 | 🇨🇭 CH | 2017 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1350 |
| 20 | 🇹🇷 TR | 1329 |
| 21 | 🇹🇭 TH | 1317 |
| 22 | 🇵🇱 PL | 1244 |
| 23 | 🇵🇭 PH | 1206 |
| 24 | 🇬🇹 GT | 1183 |
| 25 | 🇰🇷 KR | 1159 |
| 26 | 🇲🇦 MA | 885 |
| 27 | 🇲🇴 MO | 861 |
| 28 | 🇲🇪 ME | 796 |
| 29 | 🇳🇱 NL | 775 |
| 30 | 🇧🇸 BS | 627 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1305 |
| 3 | Denver International Airport |  | US | 1256 |
| 4 | Indira Gandhi International Airport |  | IN | 1106 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1077 |
| 6 | Frankfurt am Main International Airport |  | DE | 960 |
| 7 | Harry Reid International Airport |  | US | 931 |
| 8 | La Aurora Airport |  | GT | 887 |
| 9 | Guaymaral Airport |  | CO | 885 |
| 10 | El Dorado International Airport |  | CO | 878 |
| 11 | Zurich Airport |  | CH | 877 |
| 12 | Macau International Airport |  | MO | 861 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 727 |
| 15 | Madrid Barajas International Airport |  | ES | 700 |
| 16 | Kuala Lumpur International Airport |  | MY | 696 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 664 |
| 18 | Malpensa International Airport |  | IT | 644 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 643 |
| 20 | Bengaluru International Airport |  | IN | 641 |
| 21 | Salt Lake City International Airport |  | US | 616 |
| 22 | Congonhas Airport |  | BR | 596 |
| 23 | Charlotte/Douglas International Airport |  | US | 590 |
| 24 | Charles de Gaulle International Airport |  | FR | 577 |
| 25 | Capua Airport |  | IT | 575 |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 560 |
| 27 | Tenerife Norte Airport |  | ES | 559 |
| 28 | Ninoy Aquino International Airport |  | PH | 547 |
| 29 | Daniel K Inouye International Airport |  | US | 545 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 532 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 516 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 503 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 468 |
| 37 | Amsterdam Airport Schiphol |  | NL | 467 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 447 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 269 | 1h 8m | 706 km | 3,275.1 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 264 | 21m | 244 km | 1,111.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 218 | 24m | 225 km | 845.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 208 | 28m | 304 km | 1,090.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 137 | 21m | 99 km | 234.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 101 | 1h 2m | 695 km | 1,210.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 100 | 1h 42m | 1,423 km | 2,454.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL1605 | Delta Air Lines | St Louis Lambert International Airport (KSTL) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 22:40 UTC | 2026-05-08 23:49 UTC | 1h 9m |
| N331DV |  | Northwest Florida Beaches International Airport (KECP) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-05-08 22:51 UTC | 2026-05-08 23:48 UTC | 57m |
| N8170G |  | Van Nuys Airport (KVNY) | Henderson Executive Airport (KHND) | 2026-05-08 22:28 UTC | 2026-05-08 23:45 UTC | 1h 16m |
| N372BH |  | Lewis University Airport (KLOT) | Morris Municipal/James R Washburn Field (KC09) | 2026-05-08 23:10 UTC | 2026-05-08 23:43 UTC | 32m |
| N3126E |  | Ohio State University Airport (KOSU) | Delaware Municipal/Jim Moore Field (KDLZ) | 2026-05-08 23:29 UTC | 2026-05-08 23:39 UTC | 10m |
| TWY188 | TWY | Santa Barbara Municipal Airport (KSBA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 19:11 UTC | 2026-05-08 23:38 UTC | 4h 26m |
| XCPGJ | XCP | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Benito Juarez International Airport (MMMX) | 2026-05-08 23:25 UTC | 2026-05-08 23:34 UTC | 9m |
| N479AK |  | Pilot Point Airport (PAPN) | Kenai Municipal Airport (PAEN) | 2026-05-08 22:20 UTC | 2026-05-08 23:32 UTC | 1h 11m |
| N11019 |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-05-08 23:17 UTC | 2026-05-08 23:31 UTC | 13m |
| TGGMP | TGG | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-08 23:11 UTC | 2026-05-08 23:30 UTC | 19m |
| CXK416 | CXK | Ogden-Hinckley Airport (KOGD) | Nephi Municipal Airport (KU14) | 2026-05-08 22:35 UTC | 2026-05-08 23:28 UTC | 53m |
| BRG682 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-05-08 22:58 UTC | 2026-05-08 23:28 UTC | 29m |
| N128SH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-05-08 22:00 UTC | 2026-05-08 23:27 UTC | 1h 27m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-08 23:03 UTC | 2026-05-08 23:26 UTC | 23m |
| CSI505 | CSI | Albuquerque International Sunport Airport (KABQ) | Mystic Bluffs Airport (NM56) | 2026-05-08 23:03 UTC | 2026-05-08 23:26 UTC | 23m |
| N2441D |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-08 22:43 UTC | 2026-05-08 23:26 UTC | 42m |
| DAL2061 | Delta Air Lines | John Wayne/Orange County Airport (KSNA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 19:59 UTC | 2026-05-08 23:24 UTC | 3h 24m |
| N49FB |  | Reading Regional/Carl A Spaatz Field (KRDG) | Marshall Farms Airport (08IL) | 2026-05-08 20:48 UTC | 2026-05-08 23:24 UTC | 2h 36m |
| MXY808 | MXY | Orlando International Airport (KMCO) | Lancaster Airport (KLNS) | 2026-05-08 21:05 UTC | 2026-05-08 23:22 UTC | 2h 16m |
| SKW330Z | SkyWest Airlines | Chicago O'Hare International Airport (KORD) | James G Whiting Memorial Field (KMEY) | 2026-05-08 22:15 UTC | 2026-05-08 23:21 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
