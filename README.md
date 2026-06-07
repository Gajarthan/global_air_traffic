# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_23:36:36_UTC-green)

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

**Latest saved flight:** 2026-06-06 23:36:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-06 23:36:36 UTC

- **104,955** saved flights
- **36,971** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **104,955** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,283,568.9 tonnes** estimated CO2 emissions
- **74,409,791 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4312 |
| 2 | SkyWest Airlines | 3961 |
| 3 | IndiGo | 2089 |
| 4 | EJA | 2008 |
| 5 | American Airlines | 1691 |
| 6 | Southwest Airlines | 1591 |
| 7 | ENY | 1320 |
| 8 | Delta Air Lines | 1244 |
| 9 | Lufthansa | 1202 |
| 10 | Vueling | 965 |
| 11 | LATAM Airlines | 929 |
| 12 | WIF | 914 |
| 13 | AXM | 898 |
| 14 | AZU | 841 |
| 15 | LXJ | 792 |
| 16 | Swiss International | 755 |
| 17 | All Nippon Airways | 734 |
| 18 | Alaska Airlines | 730 |
| 19 | QLK | 699 |
| 20 | easyJet | 682 |
| 21 | EJU | 659 |
| 22 | Cathay Pacific | 628 |
| 23 | AEE | 606 |
| 24 | VIV | 603 |
| 25 | Air France | 602 |
| 26 | United Airlines | 585 |
| 27 | MXY | 571 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 522 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88435 |
| 2 | 🇪🇸 ES | 7219 |
| 3 | 🇮🇳 IN | 6597 |
| 4 | 🇦🇺 AU | 6323 |
| 5 | 🇧🇷 BR | 5724 |
| 6 | 🇩🇪 DE | 5628 |
| 7 | 🇮🇹 IT | 5575 |
| 8 | 🇨🇦 CA | 5470 |
| 9 | 🇯🇵 JP | 4821 |
| 10 | 🇬🇧 GB | 4429 |
| 11 | 🇫🇷 FR | 4154 |
| 12 | 🇨🇴 CO | 3634 |
| 13 | 🇲🇽 MX | 3147 |
| 14 | 🇬🇷 GR | 2987 |
| 15 | 🇳🇴 NO | 2903 |
| 16 | 🇨🇭 CH | 2673 |
| 17 | 🇲🇾 MY | 2298 |
| 18 | 🇹🇷 TR | 2006 |
| 19 | 🇿🇦 ZA | 1804 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1736 |
| 22 | 🇹🇭 TH | 1724 |
| 23 | 🇵🇱 PL | 1695 |
| 24 | 🇵🇭 PH | 1541 |
| 25 | 🇬🇹 GT | 1526 |
| 26 | 🇲🇦 MA | 1160 |
| 27 | 🇲🇴 MO | 1103 |
| 28 | 🇳🇱 NL | 1029 |
| 29 | 🇲🇪 ME | 997 |
| 30 | 🇭🇷 HR | 916 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2285 |
| 2 | Denver International Airport |  | US | 1801 |
| 3 | Tokyo International Airport |  | JP | 1600 |
| 4 | Indira Gandhi International Airport |  | IN | 1433 |
| 5 | Harry Reid International Airport |  | US | 1345 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1330 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1198 |
| 9 | Zurich Airport |  | CH | 1185 |
| 10 | La Aurora Airport |  | GT | 1174 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1133 |
| 12 | El Dorado International Airport |  | CO | 1108 |
| 13 | Macau International Airport |  | MO | 1103 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1065 |
| 15 | Chicago O'Hare International Airport |  | US | 1058 |
| 16 | Madrid Barajas International Airport |  | ES | 917 |
| 17 | Kuala Lumpur International Airport |  | MY | 900 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 899 |
| 19 | Salt Lake City International Airport |  | US | 898 |
| 20 | Capua Airport |  | IT | 883 |
| 21 | Charlotte/Douglas International Airport |  | US | 816 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 803 |
| 23 | Charles de Gaulle International Airport |  | FR | 799 |
| 24 | Congonhas Airport |  | BR | 795 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 786 |
| 27 | Daniel K Inouye International Airport |  | US | 719 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 705 |
| 30 | Barcelona International Airport |  | ES | 687 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 678 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 674 |
| 34 | Amsterdam Airport Schiphol |  | NL | 637 |
| 35 | Don Mueang International Airport |  | TH | 630 |
| 36 | Vitoria/Foronda Airport |  | ES | 630 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 603 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 601 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 387 | 21m | 244 km | 1,629.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 278 | 24m | 225 km | 1,078.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 257 | 28m | 304 km | 1,347.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 257 | 1h 25m | 910 km | 4,032.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 241 | 1h 10m | 770 km | 3,201.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 209 | 26m | 275 km | 990.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 152 | 27m | 215 km | 562.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 145 | 31m | 369 km | 923.0 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 136 | 18m | 144 km | 338.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GTI9498 | GTI | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-06-06 11:26 UTC | 2026-06-06 23:36 UTC | 12h 10m |
| AAR742 | AAR | Suvarnabhumi Airport (VTBS) | Incheon International Airport (RKSI) | 2026-06-06 18:42 UTC | 2026-06-06 23:35 UTC | 4h 52m |
| N157CL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 23:26 UTC | 2026-06-06 23:32 UTC | 6m |
| ZKJMP | ZKJ | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-06-06 23:06 UTC | 2026-06-06 23:24 UTC | 18m |
| N102SW |  | Dekalb-Peachtree Airport (KPDK) | Dekalb-Peachtree Airport (KPDK) | 2026-06-06 22:39 UTC | 2026-06-06 23:20 UTC | 40m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Zhuhai Airport (ZGSD) | 2026-06-06 20:26 UTC | 2026-06-06 23:20 UTC | 2h 53m |
| N857WA |  | Hayward Executive Airport (KHWD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-06 22:51 UTC | 2026-06-06 23:17 UTC | 25m |
| N1926A |  | Witham Field (KSUA) | Laurel Hill Farms Airport (2SC7) | 2026-06-06 21:47 UTC | 2026-06-06 23:17 UTC | 1h 29m |
| N690MF |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-06-06 22:56 UTC | 2026-06-06 23:10 UTC | 14m |
| N511EX |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 23:02 UTC | 2026-06-06 23:07 UTC | 5m |
| N600HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-06-06 23:02 UTC | 2026-06-06 23:05 UTC | 3m |
| N803JF |  | 1AR0 (1AR0) | 1AR0 (1AR0) | 2026-06-06 23:03 UTC | 2026-06-06 23:03 UTC | 0m |
| N998MF |  | Meadows Field (KBFL) | Reno/Tahoe International Airport (KRNO) | 2026-06-06 22:09 UTC | 2026-06-06 23:02 UTC | 53m |
| PDT5814 | PDT | Charlotte/Douglas International Airport (KCLT) | Logan County Airport (K6L4) | 2026-06-06 22:29 UTC | 2026-06-06 23:00 UTC | 31m |
| EJA637 | EJA | Teterboro Airport (KTEB) | Norfolk International Airport (KORF) | 2026-06-06 22:11 UTC | 2026-06-06 23:00 UTC | 49m |
| N157CL |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-06 22:47 UTC | 2026-06-06 22:54 UTC | 6m |
| N320KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-06 21:55 UTC | 2026-06-06 22:54 UTC | 58m |
| SNJ91 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-06-06 21:45 UTC | 2026-06-06 22:53 UTC | 1h 8m |
| N444SE |  | Addison Airport (KADS) | Bird Nest Airport (4MS5) | 2026-06-06 21:52 UTC | 2026-06-06 22:53 UTC | 1h 0m |
| LIFELN1 | LIF | Northern Colorado Regional Airport (KFNL) | Crystal Lakes Airport (25CO) | 2026-06-06 22:37 UTC | 2026-06-06 22:53 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
