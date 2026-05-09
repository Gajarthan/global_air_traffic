# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_21:48:08_UTC-green)

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

**Latest saved flight:** 2026-05-09 21:48:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 21:48:08 UTC

- **76,206** saved flights
- **27,984** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,206** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **939,952.7 tonnes** estimated CO2 emissions
- **54,490,012 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3267 |
| 2 | SkyWest Airlines | 2837 |
| 3 | IndiGo | 1696 |
| 4 | EJA | 1408 |
| 5 | American Airlines | 1192 |
| 6 | Southwest Airlines | 1116 |
| 7 | Lufthansa | 994 |
| 8 | ENY | 954 |
| 9 | Delta Air Lines | 763 |
| 10 | Vueling | 734 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 705 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 610 |
| 16 | QLK | 579 |
| 17 | Swiss International | 578 |
| 18 | LXJ | 562 |
| 19 | Alaska Airlines | 535 |
| 20 | easyJet | 503 |
| 21 | AEE | 491 |
| 22 | EJU | 489 |
| 23 | Cathay Pacific | 480 |
| 24 | VIV | 458 |
| 25 | Air France | 443 |
| 26 | Japan Airlines | 443 |
| 27 | AXB | 419 |
| 28 | CXK | 391 |
| 29 | AIQ | 377 |
| 30 | United Airlines | 373 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61584 |
| 2 | 🇪🇸 ES | 5456 |
| 3 | 🇮🇳 IN | 5317 |
| 4 | 🇦🇺 AU | 4956 |
| 5 | 🇩🇪 DE | 4286 |
| 6 | 🇧🇷 BR | 4264 |
| 7 | 🇮🇹 IT | 4180 |
| 8 | 🇯🇵 JP | 3960 |
| 9 | 🇨🇦 CA | 3802 |
| 10 | 🇬🇧 GB | 3267 |
| 11 | 🇫🇷 FR | 3018 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2352 |
| 14 | 🇬🇷 GR | 2243 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2069 |
| 17 | 🇲🇾 MY | 1773 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1370 |
| 20 | 🇹🇷 TR | 1364 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1273 |
| 23 | 🇵🇭 PH | 1216 |
| 24 | 🇬🇹 GT | 1197 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 900 |
| 27 | 🇲🇴 MO | 883 |
| 28 | 🇲🇪 ME | 809 |
| 29 | 🇳🇱 NL | 796 |
| 30 | 🇭🇷 HR | 655 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1692 |
| 2 | Tokyo International Airport |  | JP | 1330 |
| 3 | Denver International Airport |  | US | 1284 |
| 4 | Indira Gandhi International Airport |  | IN | 1118 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1100 |
| 6 | Frankfurt am Main International Airport |  | DE | 991 |
| 7 | Harry Reid International Airport |  | US | 948 |
| 8 | Zurich Airport |  | CH | 899 |
| 9 | La Aurora Airport |  | GT | 898 |
| 10 | Guaymaral Airport |  | CO | 890 |
| 11 | Macau International Airport |  | MO | 883 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 767 |
| 14 | Chicago O'Hare International Airport |  | US | 745 |
| 15 | Kuala Lumpur International Airport |  | MY | 713 |
| 16 | Madrid Barajas International Airport |  | ES | 711 |
| 17 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 698 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 677 |
| 19 | Bengaluru International Airport |  | IN | 660 |
| 20 | Malpensa International Airport |  | IT | 657 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 651 |
| 22 | Salt Lake City International Airport |  | US | 627 |
| 23 | Congonhas Airport |  | BR | 603 |
| 24 | Charlotte/Douglas International Airport |  | US | 600 |
| 25 | Capua Airport |  | IT | 594 |
| 26 | Charles de Gaulle International Airport |  | FR | 593 |
| 27 | Tenerife Norte Airport |  | ES | 568 |
| 28 | Daniel K Inouye International Airport |  | US | 556 |
| 29 | Ninoy Aquino International Airport |  | PH | 551 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 541 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 515 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 513 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 502 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 479 |
| 37 | Amsterdam Airport Schiphol |  | NL | 478 |
| 38 | Don Mueang International Airport |  | TH | 475 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 455 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 272 | 21m | 244 km | 1,145.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 194 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 94 | 52m | 556 km | 901.1 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N691DK |  | Truckee-Tahoe Airport (KTRK) | Gnoss Field (KDVO) | 2026-05-09 21:15 UTC | 2026-05-09 21:48 UTC | 32m |
| N219AL |  | Mc Gregor Executive Airport (KPWG) | Stephenville Clark Regional Airport (KSEP) | 2026-05-09 20:58 UTC | 2026-05-09 21:43 UTC | 45m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-09 17:37 UTC | 2026-05-09 21:42 UTC | 4h 5m |
| N50247 |  | Wimauma Air Park (FD77) | Gyro Town Usa Airport (23FL) | 2026-05-09 21:29 UTC | 2026-05-09 21:41 UTC | 12m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-05-09 11:21 UTC | 2026-05-09 21:40 UTC | 10h 19m |
| CGKMH | CGK | Calgary / Springbank Airport (CYBW) | Calgary / Springbank Airport (CYBW) | 2026-05-09 21:11 UTC | 2026-05-09 21:38 UTC | 27m |
| N700DF |  | San Antonio International Airport (KSAT) | TA89 (TA89) | 2026-05-09 20:51 UTC | 2026-05-09 21:24 UTC | 32m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-09 20:40 UTC | 2026-05-09 21:21 UTC | 41m |
| VJT827 | VJT | Henri Coanda International Airport (LROP) | Istanbul Hezarfen Airfield (LTBW) | 2026-05-09 20:43 UTC | 2026-05-09 21:20 UTC | 37m |
| N734VE |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-09 20:52 UTC | 2026-05-09 21:20 UTC | 27m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-09 21:05 UTC | 2026-05-09 21:20 UTC | 15m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-09 21:00 UTC | 2026-05-09 21:19 UTC | 19m |
| STT90 | STT | Boise Air Trml/Gowen Field (KBOI) | Cottonwood Creek Ranch Airport (OG50) | 2026-05-09 20:59 UTC | 2026-05-09 21:19 UTC | 19m |
| N733JW |  | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-05-09 20:08 UTC | 2026-05-09 21:17 UTC | 1h 8m |
| N214RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-09 21:10 UTC | 2026-05-09 21:14 UTC | 4m |
| BRW151 | BRW | Flying Cloud Airport (KFCM) | Hay Shakers Airport (MY46) | 2026-05-09 20:44 UTC | 2026-05-09 21:11 UTC | 26m |
| N734TE |  | Mc Clellan-Palomar Airport (KCRQ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-05-09 20:12 UTC | 2026-05-09 21:07 UTC | 55m |
| DAL2819 | Delta Air Lines | Charlotte/Douglas International Airport (KCLT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:44 UTC | 2026-05-09 21:07 UTC | 2h 23m |
| BRG2550 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-05-09 20:39 UTC | 2026-05-09 21:03 UTC | 24m |
| N73910 |  | Mckinney Ntl Airport (KTKI) | Fly-N-Ski Airport (31XS) | 2026-05-09 20:41 UTC | 2026-05-09 21:03 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
