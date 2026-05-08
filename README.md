# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_05:42:36_UTC-green)

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

**Latest saved flight:** 2026-05-08 05:42:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 05:42:36 UTC

- **72,732** saved flights
- **27,004** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,732** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **896,626.6 tonnes** estimated CO2 emissions
- **51,978,352 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3127 |
| 2 | SkyWest Airlines | 2714 |
| 3 | IndiGo | 1641 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 929 |
| 8 | ENY | 915 |
| 9 | Vueling | 707 |
| 10 | AXM | 689 |
| 11 | LATAM Airlines | 677 |
| 12 | WIF | 624 |
| 13 | Delta Air Lines | 613 |
| 14 | All Nippon Airways | 601 |
| 15 | AZU | 585 |
| 16 | QLK | 558 |
| 17 | Swiss International | 555 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 512 |
| 20 | easyJet | 480 |
| 21 | EJU | 468 |
| 22 | AEE | 467 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 428 |
| 26 | Air France | 423 |
| 27 | AXB | 401 |
| 28 | CXK | 368 |
| 29 | AIQ | 360 |
| 30 | United Airlines | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58386 |
| 2 | 🇪🇸 ES | 5249 |
| 3 | 🇮🇳 IN | 5149 |
| 4 | 🇦🇺 AU | 4833 |
| 5 | 🇧🇷 BR | 4074 |
| 6 | 🇩🇪 DE | 4030 |
| 7 | 🇮🇹 IT | 3976 |
| 8 | 🇯🇵 JP | 3839 |
| 9 | 🇨🇦 CA | 3635 |
| 10 | 🇬🇧 GB | 3120 |
| 11 | 🇫🇷 FR | 2855 |
| 12 | 🇨🇴 CO | 2679 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2151 |
| 15 | 🇳🇴 NO | 2019 |
| 16 | 🇨🇭 CH | 1968 |
| 17 | 🇲🇾 MY | 1721 |
| 18 | 🇿🇦 ZA | 1427 |
| 19 | 🇳🇿 NZ | 1322 |
| 20 | 🇹🇷 TR | 1306 |
| 21 | 🇹🇭 TH | 1296 |
| 22 | 🇵🇱 PL | 1210 |
| 23 | 🇵🇭 PH | 1182 |
| 24 | 🇬🇹 GT | 1147 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 863 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 772 |
| 29 | 🇳🇱 NL | 754 |
| 30 | 🇧🇸 BS | 611 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1290 |
| 3 | Denver International Airport |  | US | 1218 |
| 4 | Indira Gandhi International Airport |  | IN | 1089 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1052 |
| 6 | Frankfurt am Main International Airport |  | DE | 926 |
| 7 | Harry Reid International Airport |  | US | 910 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 874 |
| 10 | Zurich Airport |  | CH | 858 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 732 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 690 |
| 16 | Madrid Barajas International Airport |  | ES | 681 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 633 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 628 |
| 20 | Bengaluru International Airport |  | IN | 627 |
| 21 | Salt Lake City International Airport |  | US | 595 |
| 22 | Congonhas Airport |  | BR | 575 |
| 23 | Charlotte/Douglas International Airport |  | US | 574 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 566 |
| 26 | Tenerife Norte Airport |  | ES | 550 |
| 27 | Ninoy Aquino International Airport |  | PH | 538 |
| 28 | Daniel K Inouye International Airport |  | US | 533 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 522 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 500 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 494 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 486 |
| 34 | Vitoria/Foronda Airport |  | ES | 476 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 458 |
| 36 | Don Mueang International Airport |  | TH | 455 |
| 37 | Amsterdam Airport Schiphol |  | NL | 449 |
| 38 | O. R. Tambo International Airport |  | ZA | 448 |
| 39 | Calgary International Airport |  | CA | 435 |
| 40 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 433 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 363 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 266 | 1h 7m | 706 km | 3,238.6 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 256 | 21m | 244 km | 1,077.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 213 | 24m | 225 km | 826.3 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 161 | 26m | 275 km | 762.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 106 | 14m | 154 km | 280.9 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 97 | 1h 43m | 1,423 km | 2,380.5 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 93 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AWT | AWT | Nowra Airport (YSNW) | Sydney Bankstown Airport (YSBK) | 2026-05-08 05:13 UTC | 2026-05-08 05:42 UTC | 29m |
| NV131 |  | Mount Gambier Airport (YMTG) | Melbourne Essendon Airport (YMEN) | 2026-05-08 04:57 UTC | 2026-05-08 05:32 UTC | 34m |
| UAE9852 | Emirates | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-05-07 14:43 UTC | 2026-05-08 05:31 UTC | 14h 48m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-05-08 04:35 UTC | 2026-05-08 05:31 UTC | 56m |
| VAR425 | VAR | Phoenix Goodyear Airport (KGYR) | Glendale Regional Airport (KGEU) | 2026-05-08 05:01 UTC | 2026-05-08 05:20 UTC | 18m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-08 01:01 UTC | 2026-05-08 05:16 UTC | 4h 15m |
| UAL946 | United Airlines | Washington Dulles International Airport (KIAD) | Amsterdam Airport Schiphol (EHAM) | 2026-05-07 22:09 UTC | 2026-05-08 05:12 UTC | 7h 3m |
| TAG10 | TAG | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-05-07 18:33 UTC | 2026-05-08 05:08 UTC | 10h 35m |
| AE930 |  | Canberra International Airport (YSCB) | Tumut Airport (YTMU) | 2026-05-08 04:52 UTC | 2026-05-08 05:05 UTC | 13m |
| ACH4 | ACH | Sechelt-Gibsons Airport (CAP3) | Vancouver International Airport (CYVR) | 2026-05-08 04:45 UTC | 2026-05-08 05:01 UTC | 15m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-08 04:28 UTC | 2026-05-08 05:01 UTC | 32m |
| DAL2673 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 00:58 UTC | 2026-05-08 05:00 UTC | 4h 1m |
| N374AW |  | Yokota Air Base (RJTY) | Yokota Air Base (RJTY) | 2026-05-08 04:46 UTC | 2026-05-08 04:55 UTC | 8m |
| FD291 |  | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-05-08 04:14 UTC | 2026-05-08 04:54 UTC | 39m |
| N543CW |  | 74WT (74WT) | Renton Municipal Airport (KRNT) | 2026-05-08 04:04 UTC | 2026-05-08 04:51 UTC | 46m |
| RYR23WP | Ryanair | Marseille Provence Airport (LFML) | Menorca Airport (LEMH) | 2026-05-08 04:10 UTC | 2026-05-08 04:49 UTC | 38m |
| 00000000 |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 04:34 UTC | 2026-05-08 04:44 UTC | 10m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-05-08 04:24 UTC | 2026-05-08 04:42 UTC | 18m |
| N493LG |  | CO54 (CO54) | Usaf Academy Davis Airfield (KAFF) | 2026-05-08 04:28 UTC | 2026-05-08 04:40 UTC | 12m |
| RYR4FL | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Foggia / Gino Lisa Airport (LIBF) | 2026-05-08 04:15 UTC | 2026-05-08 04:38 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
