# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_04:05:52_UTC-green)

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

**Latest saved flight:** 2026-05-17 04:05:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 04:05:52 UTC

- **85,555** saved flights
- **30,719** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,555** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,056,349.2 tonnes** estimated CO2 emissions
- **61,237,638 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3663 |
| 2 | SkyWest Airlines | 3171 |
| 3 | IndiGo | 1839 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1317 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1083 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 936 |
| 10 | Vueling | 809 |
| 11 | LATAM Airlines | 778 |
| 12 | AXM | 772 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | All Nippon Airways | 663 |
| 16 | Swiss International | 662 |
| 17 | LXJ | 628 |
| 18 | QLK | 622 |
| 19 | Alaska Airlines | 609 |
| 20 | easyJet | 563 |
| 21 | Cathay Pacific | 543 |
| 22 | EJU | 540 |
| 23 | AEE | 537 |
| 24 | VIV | 515 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 476 |
| 27 | CXK | 453 |
| 28 | AXB | 451 |
| 29 | MXY | 427 |
| 30 | United Airlines | 420 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70189 |
| 2 | 🇪🇸 ES | 6036 |
| 3 | 🇮🇳 IN | 5763 |
| 4 | 🇦🇺 AU | 5435 |
| 5 | 🇩🇪 DE | 4754 |
| 6 | 🇧🇷 BR | 4711 |
| 7 | 🇮🇹 IT | 4698 |
| 8 | 🇯🇵 JP | 4281 |
| 9 | 🇨🇦 CA | 4252 |
| 10 | 🇬🇧 GB | 3639 |
| 11 | 🇫🇷 FR | 3390 |
| 12 | 🇨🇴 CO | 2876 |
| 13 | 🇲🇽 MX | 2641 |
| 14 | 🇬🇷 GR | 2479 |
| 15 | 🇳🇴 NO | 2374 |
| 16 | 🇨🇭 CH | 2245 |
| 17 | 🇲🇾 MY | 1935 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1528 |
| 20 | 🇳🇿 NZ | 1503 |
| 21 | 🇹🇭 TH | 1482 |
| 22 | 🇵🇱 PL | 1416 |
| 23 | 🇵🇭 PH | 1340 |
| 24 | 🇰🇷 KR | 1321 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇦 MA | 993 |
| 27 | 🇲🇴 MO | 992 |
| 28 | 🇲🇪 ME | 890 |
| 29 | 🇳🇱 NL | 866 |
| 30 | 🇭🇷 HR | 763 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Denver International Airport |  | US | 1441 |
| 3 | Tokyo International Airport |  | JP | 1431 |
| 4 | Indira Gandhi International Airport |  | IN | 1235 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1190 |
| 6 | Frankfurt am Main International Airport |  | DE | 1095 |
| 7 | Harry Reid International Airport |  | US | 1079 |
| 8 | Zurich Airport |  | CH | 1014 |
| 9 | Macau International Airport |  | MO | 992 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 925 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 863 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 777 |
| 17 | Kuala Lumpur International Airport |  | MY | 768 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Salt Lake City International Airport |  | US | 711 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 710 |
| 21 | Malpensa International Airport |  | IT | 709 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 697 |
| 24 | Charlotte/Douglas International Airport |  | US | 664 |
| 25 | Charles de Gaulle International Airport |  | FR | 664 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 628 |
| 28 | Tenerife Norte Airport |  | ES | 621 |
| 29 | Ninoy Aquino International Airport |  | PH | 614 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 582 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 571 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 541 |
| 36 | Vitoria/Foronda Airport |  | ES | 540 |
| 37 | Don Mueang International Airport |  | TH | 536 |
| 38 | Amsterdam Airport Schiphol |  | NL | 526 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 500 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 318 | 21m | 244 km | 1,339.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 241 | 24m | 225 km | 935.0 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 226 | 1h 26m | 910 km | 3,546.5 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 225 | 28m | 304 km | 1,179.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 195 | 1h 11m | 770 km | 2,590.4 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 178 | 26m | 275 km | 843.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 134 | 31m | 369 km | 852.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SKW5345 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Bermuda Dunes Airport (KUDD) | 2026-05-17 03:44 UTC | 2026-05-17 04:05 UTC | 21m |
| IGO1151 | IndiGo | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-05-17 02:42 UTC | 2026-05-17 04:02 UTC | 1h 19m |
| CDG1151 | CDG | Singapore Changi International Airport (WSSS) | Macau International Airport (VMMC) | 2026-05-16 17:24 UTC | 2026-05-17 03:53 UTC | 10h 29m |
| ICL857 | ICL | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-05-16 16:10 UTC | 2026-05-17 03:52 UTC | 11h 42m |
| HSDZT | HSD | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-05-17 03:40 UTC | 2026-05-17 03:47 UTC | 7m |
| N856MH |  | Harry Reid International Airport (KLAS) | Nellis Afb Airport (KLSV) | 2026-05-17 03:35 UTC | 2026-05-17 03:44 UTC | 9m |
| TAM3690 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Fazenda Canaa Airport (SIBN) | 2026-05-17 03:05 UTC | 2026-05-17 03:37 UTC | 31m |
| HKC9492 | HKC | Istanbul Hezarfen Airfield (LTBW) | Macau International Airport (VMMC) | 2026-05-16 14:56 UTC | 2026-05-17 03:29 UTC | 12h 32m |
| JST890 | JST | Sydney Kingsford Smith International Airport (YSSY) | Hervey Bay Airport (YHBA) | 2026-05-17 02:08 UTC | 2026-05-17 03:21 UTC | 1h 13m |
| ANA375 | All Nippon Airways | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-05-17 02:03 UTC | 2026-05-17 03:20 UTC | 1h 16m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Annette Island Airport (PANT) | 2026-05-17 01:44 UTC | 2026-05-17 03:17 UTC | 1h 33m |
| QFA185 | Qantas | Brisbane International Airport (YBBN) | Glenorchy Airport (NZGY) | 2026-05-17 00:12 UTC | 2026-05-17 03:09 UTC | 2h 57m |
| N207NX |  | High Lonesome Airport (NM91) | Flagstaff Pulliam Airport (KFLG) | 2026-05-17 02:40 UTC | 2026-05-17 03:09 UTC | 29m |
| CSI532 | CSI | Albuquerque International Sunport Airport (KABQ) | Jicarilla Apache Nation Airport (K24N) | 2026-05-17 02:41 UTC | 2026-05-17 03:08 UTC | 27m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-05-17 02:45 UTC | 2026-05-17 03:05 UTC | 19m |
| N87ME |  | Ronald Reagan Washington Ntl Airport (KDCA) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-05-17 02:59 UTC | 2026-05-17 03:03 UTC | 3m |
| IGO421W | IndiGo | Barrackpore Air Force Station (VEPI) | Suketar Airport (VNTJ) | 2026-05-17 02:32 UTC | 2026-05-17 03:03 UTC | 30m |
| NOK572 | NOK | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-05-17 02:29 UTC | 2026-05-17 03:03 UTC | 33m |
| N301BF |  | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-05-17 02:47 UTC | 2026-05-17 03:01 UTC | 13m |
| N885GT |  | Dekalb-Peachtree Airport (KPDK) | Blue Ridge Skyport Airport (57GA) | 2026-05-17 02:27 UTC | 2026-05-17 02:59 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
