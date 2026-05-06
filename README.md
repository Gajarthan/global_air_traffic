# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_15:23:40_UTC-green)

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

**Latest saved flight:** 2026-05-06 15:23:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 15:23:40 UTC

- **70,620** saved flights
- **26,297** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,620** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **871,324.6 tonnes** estimated CO2 emissions
- **50,511,569 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3041 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1619 |
| 4 | EJA | 1284 |
| 5 | American Airlines | 1099 |
| 6 | Southwest Airlines | 1019 |
| 7 | Lufthansa | 912 |
| 8 | ENY | 877 |
| 9 | Vueling | 695 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 659 |
| 12 | WIF | 603 |
| 13 | Delta Air Lines | 594 |
| 14 | All Nippon Airways | 590 |
| 15 | AZU | 573 |
| 16 | QLK | 547 |
| 17 | Swiss International | 545 |
| 18 | LXJ | 510 |
| 19 | Alaska Airlines | 494 |
| 20 | easyJet | 474 |
| 21 | AEE | 456 |
| 22 | EJU | 455 |
| 23 | VIV | 442 |
| 24 | Cathay Pacific | 434 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 416 |
| 27 | AXB | 394 |
| 28 | AIQ | 358 |
| 29 | CXK | 350 |
| 30 | GLO | 343 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 56075 |
| 2 | 🇪🇸 ES | 5158 |
| 3 | 🇮🇳 IN | 5083 |
| 4 | 🇦🇺 AU | 4706 |
| 5 | 🇧🇷 BR | 3979 |
| 6 | 🇩🇪 DE | 3946 |
| 7 | 🇮🇹 IT | 3873 |
| 8 | 🇯🇵 JP | 3775 |
| 9 | 🇨🇦 CA | 3488 |
| 10 | 🇬🇧 GB | 3066 |
| 11 | 🇫🇷 FR | 2798 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2235 |
| 14 | 🇬🇷 GR | 2108 |
| 15 | 🇳🇴 NO | 1937 |
| 16 | 🇨🇭 CH | 1936 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1404 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1273 |
| 22 | 🇵🇭 PH | 1171 |
| 23 | 🇵🇱 PL | 1168 |
| 24 | 🇬🇹 GT | 1131 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 847 |
| 27 | 🇲🇴 MO | 821 |
| 28 | 🇲🇪 ME | 758 |
| 29 | 🇳🇱 NL | 738 |
| 30 | 🇮🇩 ID | 596 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1571 |
| 2 | Tokyo International Airport |  | JP | 1274 |
| 3 | Denver International Airport |  | US | 1169 |
| 4 | Indira Gandhi International Airport |  | IN | 1066 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1032 |
| 6 | Frankfurt am Main International Airport |  | DE | 909 |
| 7 | Harry Reid International Airport |  | US | 880 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 841 |
| 11 | Zurich Airport |  | CH | 838 |
| 12 | Macau International Airport |  | MO | 821 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 703 |
| 14 | Kuala Lumpur International Airport |  | MY | 679 |
| 15 | Chicago O'Hare International Airport |  | US | 677 |
| 16 | Madrid Barajas International Airport |  | ES | 673 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Malpensa International Airport |  | IT | 616 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 21 | Salt Lake City International Airport |  | US | 569 |
| 22 | Congonhas Airport |  | BR | 566 |
| 23 | Charlotte/Douglas International Airport |  | US | 557 |
| 24 | Charles de Gaulle International Airport |  | FR | 555 |
| 25 | Capua Airport |  | IT | 551 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 517 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 497 |
| 31 | Barcelona International Airport |  | ES | 490 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 481 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 471 |
| 34 | Vitoria/Foronda Airport |  | ES | 469 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 445 |
| 37 | O. R. Tambo International Airport |  | ZA | 441 |
| 38 | Amsterdam Airport Schiphol |  | NL | 439 |
| 39 | Calgary International Airport |  | CA | 418 |
| 40 | Reno/Tahoe International Airport |  | US | 416 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 245 | 21m | 244 km | 1,031.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 176 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 159 | 26m | 275 km | 753.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 98 | 1h 2m | 695 km | 1,174.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFG6YR | CFG | Munich International Airport (EDDM) | Gunzenhausen-Reutberg Airport (EDMH) | 2026-05-06 14:40 UTC | 2026-05-06 15:23 UTC | 42m |
| DLH459 | Lufthansa | San Francisco International Airport (KSFO) | Niederstetten Airport (ETHN) | 2026-05-06 04:28 UTC | 2026-05-06 15:23 UTC | 10h 54m |
| EWG2GA | EWG | Munich International Airport (EDDM) | Marburg-Schonstadt Airport (EDFN) | 2026-05-06 14:24 UTC | 2026-05-06 15:23 UTC | 59m |
| RYR17PM | Ryanair | Poznań-Ławica Airport (EPPO) | Altena-Hegenscheid Airport (EDKD) | 2026-05-06 14:01 UTC | 2026-05-06 15:23 UTC | 1h 21m |
| N605CA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-06 14:37 UTC | 2026-05-06 15:18 UTC | 40m |
| CXK1023 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Brown Field Municipal Airport (KSDM) | 2026-05-06 14:34 UTC | 2026-05-06 15:18 UTC | 44m |
| N473CA |  | Meadows Field (KBFL) | Santa Barbara Municipal Airport (KSBA) | 2026-05-06 14:28 UTC | 2026-05-06 15:11 UTC | 43m |
| N2060N |  | Molnau Airpark (1MN5) | Molnau Airpark (1MN5) | 2026-05-06 13:11 UTC | 2026-05-06 15:09 UTC | 1h 58m |
| N551AP |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-06 14:43 UTC | 2026-05-06 15:09 UTC | 25m |
| N16534 |  | St Pete-Clearwater International Airport (KPIE) | Clearwater Executive Airport (KCLW) | 2026-05-06 14:49 UTC | 2026-05-06 15:07 UTC | 18m |
| DHK528 | DHK | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-05-06 04:22 UTC | 2026-05-06 15:06 UTC | 10h 44m |
| BOX502 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-06 04:20 UTC | 2026-05-06 15:06 UTC | 10h 45m |
| CPA337 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-06 07:22 UTC | 2026-05-06 15:03 UTC | 7h 40m |
| N502RP |  | Long Beach (Daugherty Field) Airport (KLGB) | Scottsdale Airport (KSDL) | 2026-05-06 14:00 UTC | 2026-05-06 15:02 UTC | 1h 2m |
| FIN5H | Finnair | Helsinki Vantaa Airport (EFHK) | Nida Airport (EYND) | 2026-05-06 13:59 UTC | 2026-05-06 14:57 UTC | 58m |
| OOAAC | OOA | Antwerp International Airport (Deurne) (EBAW) | Antwerp International Airport (Deurne) (EBAW) | 2026-05-06 14:21 UTC | 2026-05-06 14:53 UTC | 32m |
| N138BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-05-06 14:39 UTC | 2026-05-06 14:53 UTC | 13m |
| N509JE |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-05-06 14:34 UTC | 2026-05-06 14:52 UTC | 18m |
| BNI69 | BNI | Łódź Władysław Reymont Airport (EPLL) | Ostrów Airport (EPOM) | 2026-05-06 14:06 UTC | 2026-05-06 14:52 UTC | 46m |
|  |  | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-05-06 14:45 UTC | 2026-05-06 14:49 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
