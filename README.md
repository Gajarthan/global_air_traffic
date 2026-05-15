# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_23:53:16_UTC-green)

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

**Latest saved flight:** 2026-05-14 23:53:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 23:53:16 UTC

- **82,635** saved flights
- **29,929** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,635** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,017,170.7 tonnes** estimated CO2 emissions
- **58,966,416 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3532 |
| 2 | SkyWest Airlines | 3066 |
| 3 | IndiGo | 1800 |
| 4 | EJA | 1554 |
| 5 | American Airlines | 1276 |
| 6 | Southwest Airlines | 1211 |
| 7 | Lufthansa | 1062 |
| 8 | ENY | 1034 |
| 9 | Delta Air Lines | 906 |
| 10 | Vueling | 781 |
| 11 | LATAM Airlines | 751 |
| 12 | AXM | 747 |
| 13 | WIF | 716 |
| 14 | AZU | 653 |
| 15 | All Nippon Airways | 647 |
| 16 | Swiss International | 641 |
| 17 | QLK | 610 |
| 18 | LXJ | 601 |
| 19 | Alaska Airlines | 585 |
| 20 | easyJet | 546 |
| 21 | EJU | 529 |
| 22 | AEE | 524 |
| 23 | Cathay Pacific | 517 |
| 24 | VIV | 494 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 442 |
| 28 | CXK | 432 |
| 29 | MXY | 410 |
| 30 | United Airlines | 408 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67629 |
| 2 | 🇪🇸 ES | 5841 |
| 3 | 🇮🇳 IN | 5625 |
| 4 | 🇦🇺 AU | 5284 |
| 5 | 🇩🇪 DE | 4619 |
| 6 | 🇧🇷 BR | 4578 |
| 7 | 🇮🇹 IT | 4556 |
| 8 | 🇯🇵 JP | 4173 |
| 9 | 🇨🇦 CA | 4116 |
| 10 | 🇬🇧 GB | 3518 |
| 11 | 🇫🇷 FR | 3274 |
| 12 | 🇨🇴 CO | 2756 |
| 13 | 🇲🇽 MX | 2506 |
| 14 | 🇬🇷 GR | 2399 |
| 15 | 🇳🇴 NO | 2308 |
| 16 | 🇨🇭 CH | 2203 |
| 17 | 🇲🇾 MY | 1876 |
| 18 | 🇿🇦 ZA | 1550 |
| 19 | 🇹🇷 TR | 1465 |
| 20 | 🇳🇿 NZ | 1457 |
| 21 | 🇹🇭 TH | 1438 |
| 22 | 🇵🇱 PL | 1372 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇰🇷 KR | 1264 |
| 25 | 🇬🇹 GT | 1256 |
| 26 | 🇲🇦 MA | 960 |
| 27 | 🇲🇴 MO | 943 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 849 |
| 30 | 🇭🇷 HR | 735 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1821 |
| 2 | Tokyo International Airport |  | JP | 1399 |
| 3 | Denver International Airport |  | US | 1388 |
| 4 | Indira Gandhi International Airport |  | IN | 1193 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1172 |
| 6 | Frankfurt am Main International Airport |  | DE | 1073 |
| 7 | Harry Reid International Airport |  | US | 1033 |
| 8 | Zurich Airport |  | CH | 981 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 943 |
| 11 | Guaymaral Airport |  | CO | 925 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 923 |
| 13 | El Dorado International Airport |  | CO | 889 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 829 |
| 15 | Chicago O'Hare International Airport |  | US | 803 |
| 16 | Madrid Barajas International Airport |  | ES | 753 |
| 17 | Kuala Lumpur International Airport |  | MY | 748 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 720 |
| 19 | Malpensa International Airport |  | IT | 694 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 691 |
| 21 | Bengaluru International Airport |  | IN | 691 |
| 22 | Salt Lake City International Airport |  | US | 684 |
| 23 | Capua Airport |  | IT | 673 |
| 24 | Charles de Gaulle International Airport |  | FR | 646 |
| 25 | Charlotte/Douglas International Airport |  | US | 645 |
| 26 | Congonhas Airport |  | BR | 643 |
| 27 | Tenerife Norte Airport |  | ES | 600 |
| 28 | Daniel K Inouye International Airport |  | US | 599 |
| 29 | Ninoy Aquino International Airport |  | PH | 596 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 555 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 554 |
| 33 | Barcelona International Airport |  | ES | 553 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 533 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 519 |
| 36 | Don Mueang International Airport |  | TH | 518 |
| 37 | Vitoria/Foronda Airport |  | ES | 518 |
| 38 | Amsterdam Airport Schiphol |  | NL | 512 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 485 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 298 | 21m | 244 km | 1,254.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 138 | 44m | 452 km | 1,075.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 115 | 23m | 55 km | 109.3 t |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 2m | 695 km | 1,354.5 t |
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
| ERU2 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-05-14 23:28 UTC | 2026-05-14 23:53 UTC | 24m |
| N5JH |  | Buchanan Field (KCCR) | Sacramento Mather Airport (KMHR) | 2026-05-14 23:32 UTC | 2026-05-14 23:50 UTC | 18m |
| N938BS |  | Portland-Troutdale Airport (KTTD) | Nervino Airport (KO02) | 2026-05-14 21:58 UTC | 2026-05-14 23:48 UTC | 1h 49m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Hope Airport (KBUR) | 2026-05-14 23:08 UTC | 2026-05-14 23:47 UTC | 39m |
| N168BL |  | Johnston Regional Airport (KJNX) | Wayne Executive Jetport Airport (KGWW) | 2026-05-14 23:26 UTC | 2026-05-14 23:46 UTC | 20m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-05-14 22:53 UTC | 2026-05-14 23:38 UTC | 45m |
| N760GP |  | John Wayne/Orange County Airport (KSNA) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-05-14 23:23 UTC | 2026-05-14 23:37 UTC | 14m |
| CXK168 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-05-14 22:20 UTC | 2026-05-14 23:36 UTC | 1h 16m |
| N75615 |  | West Georgia Regional/O V Gray Field (KCTJ) | Columbus Airport (KCSG) | 2026-05-14 22:56 UTC | 2026-05-14 23:35 UTC | 39m |
| TKR12 | TKR | Grand Junction Regional Airport (KGJT) | K43U (K43U) | 2026-05-14 23:05 UTC | 2026-05-14 23:32 UTC | 26m |
| N298MC |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-05-14 23:14 UTC | 2026-05-14 23:28 UTC | 14m |
| CATS02 | CAT | Osan Air Base (RKSO) | G 712 Airport (RK60) | 2026-05-14 22:59 UTC | 2026-05-14 23:28 UTC | 28m |
| TKR136 | TKR | Sanpete County Regional Airport (K41U) | Sanpete County Regional Airport (K41U) | 2026-05-14 21:49 UTC | 2026-05-14 23:26 UTC | 1h 37m |
| VTE3552 | VTE | Dallas-Fort Worth International Airport (KDFW) | Matzie Airport (30MO) | 2026-05-14 22:25 UTC | 2026-05-14 23:24 UTC | 58m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-14 21:42 UTC | 2026-05-14 23:24 UTC | 1h 41m |
| TKR16 | TKR | Sanpete County Regional Airport (K41U) | K43U (K43U) | 2026-05-14 22:01 UTC | 2026-05-14 23:24 UTC | 1h 23m |
| N513CS |  | Boeing Field/King County International Airport (KBFI) | San Francisco International Airport (KSFO) | 2026-05-14 21:30 UTC | 2026-05-14 23:23 UTC | 1h 52m |
| CKS273 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-05-14 14:10 UTC | 2026-05-14 23:22 UTC | 9h 12m |
| N887CE |  | Eppley Airfield (KOMA) | NV13 (NV13) | 2026-05-14 20:35 UTC | 2026-05-14 23:20 UTC | 2h 44m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-05-14 11:40 UTC | 2026-05-14 23:19 UTC | 11h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
