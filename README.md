# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_04:36:10_UTC-green)

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

**Latest saved flight:** 2026-05-07 04:36:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 04:36:10 UTC

- **71,715** saved flights
- **26,652** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,715** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **883,939.2 tonnes** estimated CO2 emissions
- **51,242,855 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3081 |
| 2 | SkyWest Airlines | 2671 |
| 3 | IndiGo | 1622 |
| 4 | EJA | 1314 |
| 5 | American Airlines | 1124 |
| 6 | Southwest Airlines | 1045 |
| 7 | Lufthansa | 922 |
| 8 | ENY | 900 |
| 9 | Vueling | 702 |
| 10 | AXM | 685 |
| 11 | LATAM Airlines | 668 |
| 12 | WIF | 611 |
| 13 | Delta Air Lines | 601 |
| 14 | All Nippon Airways | 596 |
| 15 | AZU | 580 |
| 16 | QLK | 554 |
| 17 | Swiss International | 551 |
| 18 | LXJ | 521 |
| 19 | Alaska Airlines | 507 |
| 20 | easyJet | 476 |
| 21 | AEE | 461 |
| 22 | EJU | 459 |
| 23 | Cathay Pacific | 446 |
| 24 | VIV | 445 |
| 25 | Japan Airlines | 424 |
| 26 | Air France | 418 |
| 27 | AXB | 399 |
| 28 | AIQ | 358 |
| 29 | CXK | 357 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57368 |
| 2 | 🇪🇸 ES | 5204 |
| 3 | 🇮🇳 IN | 5101 |
| 4 | 🇦🇺 AU | 4789 |
| 5 | 🇧🇷 BR | 4020 |
| 6 | 🇩🇪 DE | 3987 |
| 7 | 🇮🇹 IT | 3921 |
| 8 | 🇯🇵 JP | 3813 |
| 9 | 🇨🇦 CA | 3565 |
| 10 | 🇬🇧 GB | 3087 |
| 11 | 🇫🇷 FR | 2816 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2264 |
| 14 | 🇬🇷 GR | 2128 |
| 15 | 🇳🇴 NO | 1964 |
| 16 | 🇨🇭 CH | 1951 |
| 17 | 🇲🇾 MY | 1708 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1318 |
| 20 | 🇹🇭 TH | 1291 |
| 21 | 🇹🇷 TR | 1287 |
| 22 | 🇵🇱 PL | 1189 |
| 23 | 🇵🇭 PH | 1172 |
| 24 | 🇬🇹 GT | 1140 |
| 25 | 🇰🇷 KR | 1133 |
| 26 | 🇲🇦 MA | 853 |
| 27 | 🇲🇴 MO | 834 |
| 28 | 🇲🇪 ME | 767 |
| 29 | 🇳🇱 NL | 744 |
| 30 | 🇧🇸 BS | 605 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1602 |
| 2 | Tokyo International Airport |  | JP | 1285 |
| 3 | Denver International Airport |  | US | 1200 |
| 4 | Indira Gandhi International Airport |  | IN | 1076 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1040 |
| 6 | Frankfurt am Main International Airport |  | DE | 916 |
| 7 | Harry Reid International Airport |  | US | 898 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | La Aurora Airport |  | GT | 849 |
| 11 | Zurich Airport |  | CH | 849 |
| 12 | Macau International Airport |  | MO | 834 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 724 |
| 14 | Chicago O'Hare International Airport |  | US | 699 |
| 15 | Kuala Lumpur International Airport |  | MY | 685 |
| 16 | Madrid Barajas International Airport |  | ES | 678 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 641 |
| 18 | Malpensa International Airport |  | IT | 625 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 20 | Bengaluru International Airport |  | IN | 618 |
| 21 | Salt Lake City International Airport |  | US | 582 |
| 22 | Congonhas Airport |  | BR | 570 |
| 23 | Charlotte/Douglas International Airport |  | US | 565 |
| 24 | Capua Airport |  | IT | 562 |
| 25 | Charles de Gaulle International Airport |  | FR | 560 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 533 |
| 28 | Daniel K Inouye International Airport |  | US | 530 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 518 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 491 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 480 |
| 34 | Vitoria/Foronda Airport |  | ES | 472 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 452 |
| 37 | Amsterdam Airport Schiphol |  | NL | 444 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Calgary International Airport |  | CA | 431 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 253 | 21m | 244 km | 1,065.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 179 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 175 | 20m | 165 km | 497.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 134 | 21m | 99 km | 229.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 103 | 14m | 154 km | 272.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-06 14:06 UTC | 2026-05-07 04:36 UTC | 14h 30m |
| QFA443 | Qantas | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-05-07 03:16 UTC | 2026-05-07 04:25 UTC | 1h 9m |
| N327CH |  | IS43 (IS43) | Frasca Field (KC16) | 2026-05-07 04:05 UTC | 2026-05-07 04:13 UTC | 7m |
| UBG121 | UBG | VGZR (VGZR) | Jessore Airport (VGJR) | 2026-05-07 03:40 UTC | 2026-05-07 04:08 UTC | 28m |
| AAL2890 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Sacramento International Airport (KSMF) | 2026-05-06 23:00 UTC | 2026-05-07 04:06 UTC | 5h 6m |
| BKBD06 | BKB | Khok Kathiam Airport (VTBL) | Khok Kathiam Airport (VTBL) | 2026-05-07 03:46 UTC | 2026-05-07 04:03 UTC | 17m |
| THNDR21 | THN | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-05-07 03:43 UTC | 2026-05-07 04:03 UTC | 19m |
| AEE594 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Syros Airport (LGSO) | 2026-05-07 03:00 UTC | 2026-05-07 03:50 UTC | 49m |
| GRIT82 | GRI | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-05-07 03:44 UTC | 2026-05-07 03:49 UTC | 5m |
| GRIT17 | GRI | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-05-07 03:44 UTC | 2026-05-07 03:49 UTC | 5m |
| IGO1151 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-05-07 02:36 UTC | 2026-05-07 03:45 UTC | 1h 9m |
| N916SP |  | Watts-Woodland Airport (KO41) | Mc Clellan Airfield (KMCC) | 2026-05-07 03:26 UTC | 2026-05-07 03:45 UTC | 18m |
| HMO | HMO | Albury Airport (YMAY) | Corowa Airport (YCOR) | 2026-05-07 03:33 UTC | 2026-05-07 03:44 UTC | 11m |
| N999PR |  | Scottsdale Airport (KSDL) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-07 02:06 UTC | 2026-05-07 03:39 UTC | 1h 33m |
| N9769F |  | Las Cruces International Airport (KLRU) | Deming Municipal Airport (KDMN) | 2026-05-07 03:00 UTC | 2026-05-07 03:39 UTC | 38m |
| SPTN885 | SPT | Sacramento Mather Airport (KMHR) | Van Vleck Airport (57CN) | 2026-05-07 02:42 UTC | 2026-05-07 03:38 UTC | 56m |
| JAL553 | Japan Airlines | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-05-07 02:31 UTC | 2026-05-07 03:38 UTC | 1h 6m |
| ZKHQQ | ZKH | North Shore Aerodrome (NZNE) | North Shore Aerodrome (NZNE) | 2026-05-07 03:17 UTC | 2026-05-07 03:36 UTC | 19m |
| RFS730 | RFS | Portland-Hillsboro Airport (KHIO) | WA69 (WA69) | 2026-05-07 02:00 UTC | 2026-05-07 03:35 UTC | 1h 34m |
| ASA1123 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Lihue Airport (PHLI) | 2026-05-07 03:20 UTC | 2026-05-07 03:35 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
