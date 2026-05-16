# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_22:54:59_UTC-green)

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

**Latest saved flight:** 2026-05-16 22:54:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 22:54:59 UTC

- **85,489** saved flights
- **30,711** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,489** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,055,478.9 tonnes** estimated CO2 emissions
- **61,187,184 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3663 |
| 2 | SkyWest Airlines | 3169 |
| 3 | IndiGo | 1837 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1317 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1083 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 935 |
| 10 | Vueling | 809 |
| 11 | LATAM Airlines | 777 |
| 12 | AXM | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | Swiss International | 662 |
| 16 | All Nippon Airways | 660 |
| 17 | LXJ | 628 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 607 |
| 20 | easyJet | 563 |
| 21 | Cathay Pacific | 543 |
| 22 | EJU | 540 |
| 23 | AEE | 537 |
| 24 | VIV | 514 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | CXK | 453 |
| 28 | AXB | 450 |
| 29 | MXY | 427 |
| 30 | United Airlines | 420 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70156 |
| 2 | 🇪🇸 ES | 6036 |
| 3 | 🇮🇳 IN | 5756 |
| 4 | 🇦🇺 AU | 5426 |
| 5 | 🇩🇪 DE | 4754 |
| 6 | 🇧🇷 BR | 4709 |
| 7 | 🇮🇹 IT | 4698 |
| 8 | 🇯🇵 JP | 4262 |
| 9 | 🇨🇦 CA | 4250 |
| 10 | 🇬🇧 GB | 3639 |
| 11 | 🇫🇷 FR | 3390 |
| 12 | 🇨🇴 CO | 2876 |
| 13 | 🇲🇽 MX | 2637 |
| 14 | 🇬🇷 GR | 2479 |
| 15 | 🇳🇴 NO | 2374 |
| 16 | 🇨🇭 CH | 2245 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1525 |
| 20 | 🇳🇿 NZ | 1498 |
| 21 | 🇹🇭 TH | 1475 |
| 22 | 🇵🇱 PL | 1416 |
| 23 | 🇵🇭 PH | 1336 |
| 24 | 🇰🇷 KR | 1314 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇦 MA | 993 |
| 27 | 🇲🇴 MO | 990 |
| 28 | 🇲🇪 ME | 890 |
| 29 | 🇳🇱 NL | 866 |
| 30 | 🇭🇷 HR | 763 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Denver International Airport |  | US | 1440 |
| 3 | Tokyo International Airport |  | JP | 1425 |
| 4 | Indira Gandhi International Airport |  | IN | 1233 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1190 |
| 6 | Frankfurt am Main International Airport |  | DE | 1095 |
| 7 | Harry Reid International Airport |  | US | 1078 |
| 8 | Zurich Airport |  | CH | 1014 |
| 9 | Macau International Airport |  | MO | 990 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 925 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 863 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 777 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Salt Lake City International Airport |  | US | 710 |
| 20 | Malpensa International Airport |  | IT | 709 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 697 |
| 24 | Charlotte/Douglas International Airport |  | US | 664 |
| 25 | Charles de Gaulle International Airport |  | FR | 664 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 626 |
| 28 | Tenerife Norte Airport |  | ES | 621 |
| 29 | Ninoy Aquino International Airport |  | PH | 612 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 582 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 571 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 540 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 540 |
| 37 | Don Mueang International Airport |  | TH | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 526 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 500 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 316 | 21m | 244 km | 1,330.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 194 | 1h 11m | 770 km | 2,577.1 t |
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
| VKG415 | VKG | Antalya International Airport (LTAI) | Powidz Military Air Base (EPPW) | 2026-05-16 20:13 UTC | 2026-05-16 22:54 UTC | 2h 41m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-05-16 11:54 UTC | 2026-05-16 22:44 UTC | 10h 49m |
| DMS | DMS | Cessnock Airport (YCNK) | Sydney Bankstown Airport (YSBK) | 2026-05-16 22:19 UTC | 2026-05-16 22:41 UTC | 22m |
| FLC89 | FLC | Ted Stevens Anchorage International Airport (PANC) | Ladd Army Air Field (PAFB) | 2026-05-16 18:34 UTC | 2026-05-16 22:40 UTC | 4h 5m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-05-16 12:08 UTC | 2026-05-16 22:40 UTC | 10h 31m |
| TOM9JB | TOM | Cardak Airport (LTAY) | London Gatwick Airport (EGKK) | 2026-05-16 18:41 UTC | 2026-05-16 22:38 UTC | 3h 57m |
| N787MM |  | Chicago Midway International Airport (KMDW) | Harry Reid International Airport (KLAS) | 2026-05-16 19:05 UTC | 2026-05-16 22:37 UTC | 3h 32m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Zhuhai Airport (ZGSD) | 2026-05-16 11:32 UTC | 2026-05-16 22:37 UTC | 11h 5m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-16 22:16 UTC | 2026-05-16 22:36 UTC | 20m |
| AIH953 | AIH | Incheon International Airport (RKSI) | Zhuhai Airport (ZGSD) | 2026-05-16 14:54 UTC | 2026-05-16 22:34 UTC | 7h 39m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-16 22:13 UTC | 2026-05-16 22:30 UTC | 16m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Zhuhai Airport (ZGSD) | 2026-05-16 11:20 UTC | 2026-05-16 22:25 UTC | 11h 4m |
| N621PA |  | Denton Enterprise Airport (KDTO) | Flying D Ranch Airport (TX94) | 2026-05-16 21:50 UTC | 2026-05-16 22:23 UTC | 33m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-05-16 10:24 UTC | 2026-05-16 22:23 UTC | 11h 58m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-05-16 20:16 UTC | 2026-05-16 22:21 UTC | 2h 4m |
| N200MR |  | Centennial Airport (KAPA) | Telluride Regional Airport (KTEX) | 2026-05-16 21:22 UTC | 2026-05-16 22:20 UTC | 58m |
| N301BF |  | KU77 (KU77) | Provo Municipal Airport (KPVU) | 2026-05-16 22:10 UTC | 2026-05-16 22:19 UTC | 9m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-16 21:49 UTC | 2026-05-16 22:19 UTC | 30m |
| SCU20 | SCU | Henryetta Municipal Airport (KF10) | Mc Alester Regional Airport (KMLC) | 2026-05-16 21:50 UTC | 2026-05-16 22:16 UTC | 25m |
| CPA095 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-16 07:25 UTC | 2026-05-16 22:13 UTC | 14h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
