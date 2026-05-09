# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_14:58:10_UTC-green)

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

**Latest saved flight:** 2026-05-09 14:58:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 14:58:10 UTC

- **75,441** saved flights
- **27,777** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,441** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **930,376.0 tonnes** estimated CO2 emissions
- **53,934,839 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3228 |
| 2 | SkyWest Airlines | 2793 |
| 3 | IndiGo | 1693 |
| 4 | EJA | 1388 |
| 5 | American Airlines | 1172 |
| 6 | Southwest Airlines | 1092 |
| 7 | Lufthansa | 981 |
| 8 | ENY | 938 |
| 9 | Vueling | 728 |
| 10 | Delta Air Lines | 716 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 699 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 606 |
| 16 | QLK | 579 |
| 17 | Swiss International | 576 |
| 18 | LXJ | 555 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 499 |
| 21 | AEE | 487 |
| 22 | EJU | 483 |
| 23 | Cathay Pacific | 475 |
| 24 | VIV | 455 |
| 25 | Japan Airlines | 443 |
| 26 | Air France | 439 |
| 27 | AXB | 419 |
| 28 | CXK | 388 |
| 29 | AIQ | 377 |
| 30 | MXY | 365 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60637 |
| 2 | 🇪🇸 ES | 5406 |
| 3 | 🇮🇳 IN | 5306 |
| 4 | 🇦🇺 AU | 4952 |
| 5 | 🇩🇪 DE | 4248 |
| 6 | 🇧🇷 BR | 4230 |
| 7 | 🇮🇹 IT | 4119 |
| 8 | 🇯🇵 JP | 3959 |
| 9 | 🇨🇦 CA | 3757 |
| 10 | 🇬🇧 GB | 3248 |
| 11 | 🇫🇷 FR | 2998 |
| 12 | 🇨🇴 CO | 2694 |
| 13 | 🇲🇽 MX | 2330 |
| 14 | 🇬🇷 GR | 2229 |
| 15 | 🇳🇴 NO | 2096 |
| 16 | 🇨🇭 CH | 2055 |
| 17 | 🇲🇾 MY | 1772 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1366 |
| 20 | 🇹🇷 TR | 1358 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1263 |
| 23 | 🇵🇭 PH | 1216 |
| 24 | 🇬🇹 GT | 1191 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 890 |
| 27 | 🇲🇴 MO | 875 |
| 28 | 🇲🇪 ME | 804 |
| 29 | 🇳🇱 NL | 784 |
| 30 | 🇭🇷 HR | 637 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1666 |
| 2 | Tokyo International Airport |  | JP | 1329 |
| 3 | Denver International Airport |  | US | 1262 |
| 4 | Indira Gandhi International Airport |  | IN | 1115 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1095 |
| 6 | Frankfurt am Main International Airport |  | DE | 980 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | La Aurora Airport |  | GT | 894 |
| 9 | Zurich Airport |  | CH | 891 |
| 10 | Guaymaral Airport |  | CO | 888 |
| 11 | El Dorado International Airport |  | CO | 879 |
| 12 | Macau International Airport |  | MO | 875 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 732 |
| 15 | Kuala Lumpur International Airport |  | MY | 712 |
| 16 | Madrid Barajas International Airport |  | ES | 703 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 666 |
| 18 | Bengaluru International Airport |  | IN | 658 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 650 |
| 20 | Malpensa International Airport |  | IT | 647 |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 621 |
| 22 | Salt Lake City International Airport |  | US | 617 |
| 23 | Congonhas Airport |  | BR | 598 |
| 24 | Charlotte/Douglas International Airport |  | US | 593 |
| 25 | Charles de Gaulle International Airport |  | FR | 587 |
| 26 | Capua Airport |  | IT | 582 |
| 27 | Tenerife Norte Airport |  | ES | 562 |
| 28 | Ninoy Aquino International Airport |  | PH | 551 |
| 29 | Daniel K Inouye International Airport |  | US | 550 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 540 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 519 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 506 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 501 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Don Mueang International Airport |  | TH | 475 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 474 |
| 38 | Amsterdam Airport Schiphol |  | NL | 471 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 369 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 267 | 21m | 244 km | 1,124.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 194 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 138 | 20m | 99 km | 236.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 113 | 20m | 147 km | 286.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 93 | 1h 19m | 961 km | 1,541.5 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DMEFP | DME | Eggenfelden Airport (EDME) | Dingolfing Airport (EDPD) | 2026-05-09 14:45 UTC | 2026-05-09 14:58 UTC | 12m |
| BOX500 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-09 04:14 UTC | 2026-05-09 14:54 UTC | 10h 39m |
| FGAHA | FGA | Lognes Emerainville Airport (LFPL) | Melun-Villaroche Air Base (LFPM) | 2026-05-09 14:37 UTC | 2026-05-09 14:49 UTC | 12m |
| UAL1414 | United Airlines | Chicago O'Hare International Airport (KORD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 13:41 UTC | 2026-05-09 14:47 UTC | 1h 6m |
| N821TN |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Button Airport (SN67) | 2026-05-09 14:21 UTC | 2026-05-09 14:40 UTC | 18m |
| N993Q |  | KE80 (KE80) | NM74 (NM74) | 2026-05-09 14:17 UTC | 2026-05-09 14:37 UTC | 19m |
| N182SC |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Anoka County/Blaine (Janes Field) Airport (KANE) | 2026-05-09 14:14 UTC | 2026-05-09 14:34 UTC | 20m |
| N904VU |  | Rattlesnake Ridge Airport (TN81) | John C Tune Airport (KJWN) | 2026-05-09 14:23 UTC | 2026-05-09 14:32 UTC | 9m |
| CXK204 | CXK | Ogden-Hinckley Airport (KOGD) | UT49 (UT49) | 2026-05-09 13:32 UTC | 2026-05-09 14:28 UTC | 56m |
| N3584S |  | Shafter-Minter Field (KMIT) | Shafter-Minter Field (KMIT) | 2026-05-09 13:37 UTC | 2026-05-09 14:28 UTC | 50m |
| DAL1493 | Delta Air Lines | Ronald Reagan Washington Ntl Airport (KDCA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 12:00 UTC | 2026-05-09 14:25 UTC | 2h 24m |
| N172TG |  | Sanford Seacoast Regional Airport (KSFM) | Back Acres Airport (ME46) | 2026-05-09 14:15 UTC | 2026-05-09 14:24 UTC | 9m |
| DAL2263 | Delta Air Lines | Tampa International Airport (KTPA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 11:07 UTC | 2026-05-09 14:23 UTC | 3h 16m |
| N467AA |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-09 14:21 UTC | 2026-05-09 14:23 UTC | 2m |
| N733TL |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-05-09 14:11 UTC | 2026-05-09 14:23 UTC | 12m |
| ASI532 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-05-09 14:02 UTC | 2026-05-09 14:22 UTC | 20m |
| N621FJ |  | Rocky Mountain Metro Airport (KBJC) | Vance Brand Airport (KLMO) | 2026-05-09 13:45 UTC | 2026-05-09 14:21 UTC | 36m |
| HGB932 | HGB | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-09 07:24 UTC | 2026-05-09 14:21 UTC | 6h 56m |
| CXK648 | CXK | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-05-09 14:10 UTC | 2026-05-09 14:20 UTC | 10m |
| N26BQ |  | B & C Airport (IL99) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-09 13:43 UTC | 2026-05-09 14:19 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
