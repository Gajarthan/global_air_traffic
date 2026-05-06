# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_12:55:29_UTC-green)

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

**Latest saved flight:** 2026-05-06 12:55:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 12:55:29 UTC

- **70,438** saved flights
- **26,243** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,438** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **869,207.4 tonnes** estimated CO2 emissions
- **50,388,833 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3032 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1616 |
| 4 | EJA | 1282 |
| 5 | American Airlines | 1096 |
| 6 | Southwest Airlines | 1019 |
| 7 | Lufthansa | 905 |
| 8 | ENY | 876 |
| 9 | Vueling | 694 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 658 |
| 12 | WIF | 599 |
| 13 | Delta Air Lines | 594 |
| 14 | All Nippon Airways | 590 |
| 15 | AZU | 570 |
| 16 | QLK | 547 |
| 17 | Swiss International | 543 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 494 |
| 20 | easyJet | 473 |
| 21 | EJU | 455 |
| 22 | AEE | 454 |
| 23 | VIV | 441 |
| 24 | Cathay Pacific | 433 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 414 |
| 27 | AXB | 393 |
| 28 | AIQ | 358 |
| 29 | CXK | 349 |
| 30 | GLO | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55931 |
| 2 | 🇪🇸 ES | 5143 |
| 3 | 🇮🇳 IN | 5078 |
| 4 | 🇦🇺 AU | 4706 |
| 5 | 🇧🇷 BR | 3965 |
| 6 | 🇩🇪 DE | 3924 |
| 7 | 🇮🇹 IT | 3859 |
| 8 | 🇯🇵 JP | 3775 |
| 9 | 🇨🇦 CA | 3475 |
| 10 | 🇬🇧 GB | 3055 |
| 11 | 🇫🇷 FR | 2788 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2228 |
| 14 | 🇬🇷 GR | 2100 |
| 15 | 🇨🇭 CH | 1932 |
| 16 | 🇳🇴 NO | 1925 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1400 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1267 |
| 22 | 🇵🇭 PH | 1171 |
| 23 | 🇵🇱 PL | 1161 |
| 24 | 🇰🇷 KR | 1130 |
| 25 | 🇬🇹 GT | 1129 |
| 26 | 🇲🇦 MA | 845 |
| 27 | 🇲🇴 MO | 818 |
| 28 | 🇲🇪 ME | 757 |
| 29 | 🇳🇱 NL | 733 |
| 30 | 🇮🇩 ID | 596 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1570 |
| 2 | Tokyo International Airport |  | JP | 1274 |
| 3 | Denver International Airport |  | US | 1167 |
| 4 | Indira Gandhi International Airport |  | IN | 1066 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1028 |
| 6 | Frankfurt am Main International Airport |  | DE | 903 |
| 7 | Harry Reid International Airport |  | US | 880 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 839 |
| 11 | Zurich Airport |  | CH | 834 |
| 12 | Macau International Airport |  | MO | 818 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 703 |
| 14 | Kuala Lumpur International Airport |  | MY | 679 |
| 15 | Chicago O'Hare International Airport |  | US | 676 |
| 16 | Madrid Barajas International Airport |  | ES | 672 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Malpensa International Airport |  | IT | 613 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 20 | Bengaluru International Airport |  | IN | 613 |
| 21 | Salt Lake City International Airport |  | US | 569 |
| 22 | Congonhas Airport |  | BR | 563 |
| 23 | Charlotte/Douglas International Airport |  | US | 555 |
| 24 | Charles de Gaulle International Airport |  | FR | 553 |
| 25 | Capua Airport |  | IT | 550 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 517 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 495 |
| 31 | Barcelona International Airport |  | ES | 490 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 478 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 468 |
| 34 | Vitoria/Foronda Airport |  | ES | 466 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 444 |
| 37 | O. R. Tambo International Airport |  | ZA | 440 |
| 38 | Amsterdam Airport Schiphol |  | NL | 435 |
| 39 | Calgary International Airport |  | CA | 417 |
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
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 175 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 158 | 26m | 275 km | 748.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 106 | 20m | 147 km | 268.2 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 97 | 1h 2m | 695 km | 1,162.7 t |
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
| ERU963 | ERU | Daytona Beach International Airport (KDAB) | Ormond Beach Municipal Airport (KOMN) | 2026-05-06 12:42 UTC | 2026-05-06 12:55 UTC | 13m |
| N603DW |  | Joe Foss Field (KFSD) | Dubuque Regional Airport (KDBQ) | 2026-05-06 11:45 UTC | 2026-05-06 12:33 UTC | 47m |
| CTM1245 | CTM | Orleans-Bricy (BA 123) Air Base (LFOJ) | La Roche-sur-Yon Airport (LFRI) | 2026-05-06 12:03 UTC | 2026-05-06 12:32 UTC | 29m |
| DBVHA | DBV | Hamburg Airport (EDDH) | Oberpfaffenhofen Airport (EDMO) | 2026-05-06 11:28 UTC | 2026-05-06 12:28 UTC | 1h 0m |
| N1674E |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-05-06 12:08 UTC | 2026-05-06 12:23 UTC | 14m |
| N247LT |  | Central Wisconsin Airport (KCWA) | Dane County Regional/Truax Field (KMSN) | 2026-05-06 11:51 UTC | 2026-05-06 12:12 UTC | 20m |
| CO76 |  | Pirassununga Airport (SDPY) | Pirassununga Airport (SDPY) | 2026-05-06 11:39 UTC | 2026-05-06 12:10 UTC | 30m |
| N32AC |  | Blue Grass Airport (KLEX) | II45 (II45) | 2026-05-06 11:39 UTC | 2026-05-06 12:09 UTC | 30m |
| WMT7JJ | WMT | Catania / Fontanarossa Airport (LICC) | Malpensa International Airport (LIMC) | 2026-05-06 10:22 UTC | 2026-05-06 12:06 UTC | 1h 44m |
| N320HB |  | Shady International Airport (FA49) | Abaco I Walker C Airport (MYAW) | 2026-05-06 11:33 UTC | 2026-05-06 12:05 UTC | 31m |
| VLG66VP | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-05-06 11:22 UTC | 2026-05-06 12:03 UTC | 40m |
| AUA3U | Austrian Airlines | Vienna International Airport (LOWW) | Suceava Stefan cel Mare Airport (LRSV) | 2026-05-06 11:01 UTC | 2026-05-06 12:01 UTC | 1h 0m |
| AAH52 | AAH | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-05-06 11:39 UTC | 2026-05-06 12:01 UTC | 21m |
| CNS13 | CNS | Portsmouth International At Pease Airport (KPSM) | Tweed/New Haven Airport (KHVN) | 2026-05-06 11:11 UTC | 2026-05-06 12:00 UTC | 48m |
| N3008U |  | Naper Aero Club Airport (LL10) | Curanda Airport (LL39) | 2026-05-06 11:40 UTC | 2026-05-06 11:59 UTC | 18m |
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-05-06 11:11 UTC | 2026-05-06 11:58 UTC | 46m |
| N377MD |  | Flying Cloud Airport (KFCM) | Joe Foss Field (KFSD) | 2026-05-06 11:24 UTC | 2026-05-06 11:57 UTC | 33m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-05-05 21:35 UTC | 2026-05-06 11:57 UTC | 14h 21m |
| RPA5687 | Republic Airways | General Edward Lawrence Logan International Airport (KBOS) | Deale Airport (MD22) | 2026-05-06 10:21 UTC | 2026-05-06 11:53 UTC | 1h 31m |
| SWA1944 | Southwest Airlines | Rhode Island Tf Green International Airport (KPVD) | Magennis Farm Airport (7MD1) | 2026-05-06 10:39 UTC | 2026-05-06 11:53 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
