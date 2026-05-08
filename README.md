# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_21:01:28_UTC-green)

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

**Latest saved flight:** 2026-05-08 21:01:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 21:01:28 UTC

- **74,311** saved flights
- **27,502** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,311** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **913,832.9 tonnes** estimated CO2 emissions
- **52,975,823 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3195 |
| 2 | SkyWest Airlines | 2755 |
| 3 | IndiGo | 1664 |
| 4 | EJA | 1373 |
| 5 | American Airlines | 1158 |
| 6 | Southwest Airlines | 1078 |
| 7 | Lufthansa | 963 |
| 8 | ENY | 929 |
| 9 | Vueling | 724 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 688 |
| 12 | Delta Air Lines | 663 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 597 |
| 16 | QLK | 573 |
| 17 | Swiss International | 566 |
| 18 | LXJ | 551 |
| 19 | Alaska Airlines | 522 |
| 20 | easyJet | 490 |
| 21 | AEE | 478 |
| 22 | EJU | 478 |
| 23 | Cathay Pacific | 458 |
| 24 | VIV | 452 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 430 |
| 27 | AXB | 411 |
| 28 | CXK | 380 |
| 29 | AIQ | 366 |
| 30 | MXY | 360 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 59800 |
| 2 | 🇪🇸 ES | 5369 |
| 3 | 🇮🇳 IN | 5229 |
| 4 | 🇦🇺 AU | 4909 |
| 5 | 🇧🇷 BR | 4167 |
| 6 | 🇩🇪 DE | 4165 |
| 7 | 🇮🇹 IT | 4058 |
| 8 | 🇯🇵 JP | 3877 |
| 9 | 🇨🇦 CA | 3704 |
| 10 | 🇬🇧 GB | 3192 |
| 11 | 🇫🇷 FR | 2937 |
| 12 | 🇨🇴 CO | 2688 |
| 13 | 🇲🇽 MX | 2304 |
| 14 | 🇬🇷 GR | 2198 |
| 15 | 🇳🇴 NO | 2076 |
| 16 | 🇨🇭 CH | 2016 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1330 |
| 20 | 🇹🇷 TR | 1328 |
| 21 | 🇹🇭 TH | 1317 |
| 22 | 🇵🇱 PL | 1244 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1175 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 883 |
| 27 | 🇲🇴 MO | 853 |
| 28 | 🇲🇪 ME | 796 |
| 29 | 🇳🇱 NL | 774 |
| 30 | 🇧🇸 BS | 624 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1644 |
| 2 | Tokyo International Airport |  | JP | 1303 |
| 3 | Denver International Airport |  | US | 1243 |
| 4 | Indira Gandhi International Airport |  | IN | 1104 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1077 |
| 6 | Frankfurt am Main International Airport |  | DE | 959 |
| 7 | Harry Reid International Airport |  | US | 924 |
| 8 | Guaymaral Airport |  | CO | 883 |
| 9 | La Aurora Airport |  | GT | 880 |
| 10 | El Dorado International Airport |  | CO | 878 |
| 11 | Zurich Airport |  | CH | 876 |
| 12 | Macau International Airport |  | MO | 853 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 749 |
| 14 | Chicago O'Hare International Airport |  | US | 720 |
| 15 | Madrid Barajas International Airport |  | ES | 697 |
| 16 | Kuala Lumpur International Airport |  | MY | 696 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 658 |
| 18 | Malpensa International Airport |  | IT | 642 |
| 19 | Bengaluru International Airport |  | IN | 641 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 607 |
| 22 | Congonhas Airport |  | BR | 589 |
| 23 | Charlotte/Douglas International Airport |  | US | 585 |
| 24 | Charles de Gaulle International Airport |  | FR | 575 |
| 25 | Capua Airport |  | IT | 575 |
| 26 | Tenerife Norte Airport |  | ES | 559 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 542 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 531 |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 523 |
| 31 | Barcelona International Airport |  | ES | 512 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 511 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 501 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Amsterdam Airport Schiphol |  | NL | 466 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 465 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 443 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 367 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 262 | 21m | 244 km | 1,103.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 190 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 136 | 21m | 99 km | 233.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
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
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 98 | 23m | 55 km | 93.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 91 | 1h 19m | 961 km | 1,508.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N65439 |  | Statesville Regional Airport (KSVH) | Statesville Regional Airport (KSVH) | 2026-05-08 20:41 UTC | 2026-05-08 21:01 UTC | 20m |
| N503MA |  | Akron Fulton International Airport (KAKR) | Wheeling Ohio County Airport (KHLG) | 2026-05-08 20:16 UTC | 2026-05-08 20:57 UTC | 41m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-05-08 20:41 UTC | 2026-05-08 20:54 UTC | 12m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-05-08 06:14 UTC | 2026-05-08 20:47 UTC | 14h 32m |
| N629RP |  | Mckinney Ntl Airport (KTKI) | Boerne Stage Airfield (K5C1) | 2026-05-08 19:26 UTC | 2026-05-08 20:43 UTC | 1h 17m |
| N1193M |  | Hinaman Acres Airport (1PA0) | Lake Airport (19PA) | 2026-05-08 20:26 UTC | 2026-05-08 20:39 UTC | 12m |
| CCK70 | CCK | Phoenix Deer Valley Airport (KDVT) | Cottonwood Airport (KP52) | 2026-05-08 20:10 UTC | 2026-05-08 20:36 UTC | 25m |
| N457TS |  | Santa Barbara Municipal Airport (KSBA) | Henderson Executive Airport (KHND) | 2026-05-08 18:38 UTC | 2026-05-08 20:36 UTC | 1h 57m |
| DAL1471 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 20:23 UTC | 2026-05-08 20:35 UTC | 12m |
| CFYUL | CFY | Calgary International Airport (CYYC) | Del Bonita / Whetstone International Airport (CEQ4) | 2026-05-08 20:16 UTC | 2026-05-08 20:35 UTC | 18m |
| N828WW |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-08 20:05 UTC | 2026-05-08 20:34 UTC | 28m |
| N244LJ |  | Fort Lauderdale Executive Airport (KFXE) | West End Airport (MYGW) | 2026-05-08 20:17 UTC | 2026-05-08 20:33 UTC | 16m |
| N979CC |  | Cuyahoga County Airport (KCGF) | Burke Lakefront Airport (KBKL) | 2026-05-08 20:25 UTC | 2026-05-08 20:32 UTC | 6m |
| SRY | SRY | Tyabb Airport (YTYA) | Ballarat Airport (YBLT) | 2026-05-08 20:02 UTC | 2026-05-08 20:32 UTC | 29m |
| N555BH |  | Tusquittee Landing Airport (NC08) | Tusquittee Landing Airport (NC08) | 2026-05-08 19:47 UTC | 2026-05-08 20:31 UTC | 43m |
| N58060 |  | Christensen Ranch Airport (9CL2) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-08 20:10 UTC | 2026-05-08 20:27 UTC | 16m |
|  |  | Valdez Pioneer Field (PAVD) | King Salmon Airport (PAKN) | 2026-05-08 18:48 UTC | 2026-05-08 20:26 UTC | 1h 38m |
| N5197R |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-05-08 20:15 UTC | 2026-05-08 20:26 UTC | 11m |
| LXJ605 | LXJ | Harry Reid International Airport (KLAS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-08 19:18 UTC | 2026-05-08 20:26 UTC | 1h 8m |
| N584RH |  | Rocky Mountain Metro Airport (KBJC) | Platte Valley Airpark (K18V) | 2026-05-08 19:27 UTC | 2026-05-08 20:25 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
