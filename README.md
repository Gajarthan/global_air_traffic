# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_22:56:58_UTC-green)

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

**Latest saved flight:** 2026-05-05 22:56:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 22:56:58 UTC

- **69,965** saved flights
- **26,128** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **69,965** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **861,637.4 tonnes** estimated CO2 emissions
- **49,949,995 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3007 |
| 2 | SkyWest Airlines | 2618 |
| 3 | IndiGo | 1599 |
| 4 | EJA | 1275 |
| 5 | American Airlines | 1094 |
| 6 | Southwest Airlines | 1008 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 868 |
| 9 | Vueling | 690 |
| 10 | AXM | 667 |
| 11 | LATAM Airlines | 653 |
| 12 | WIF | 596 |
| 13 | Delta Air Lines | 592 |
| 14 | All Nippon Airways | 585 |
| 15 | AZU | 570 |
| 16 | Swiss International | 539 |
| 17 | QLK | 537 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 487 |
| 20 | easyJet | 468 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 439 |
| 24 | Cathay Pacific | 426 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55676 |
| 2 | 🇪🇸 ES | 5104 |
| 3 | 🇮🇳 IN | 5029 |
| 4 | 🇦🇺 AU | 4613 |
| 5 | 🇧🇷 BR | 3943 |
| 6 | 🇩🇪 DE | 3900 |
| 7 | 🇮🇹 IT | 3832 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3458 |
| 10 | 🇬🇧 GB | 3037 |
| 11 | 🇫🇷 FR | 2768 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2224 |
| 14 | 🇬🇷 GR | 2086 |
| 15 | 🇨🇭 CH | 1923 |
| 16 | 🇳🇴 NO | 1913 |
| 17 | 🇲🇾 MY | 1664 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1294 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1259 |
| 22 | 🇵🇭 PH | 1160 |
| 23 | 🇵🇱 PL | 1151 |
| 24 | 🇬🇹 GT | 1127 |
| 25 | 🇰🇷 KR | 1111 |
| 26 | 🇲🇦 MA | 843 |
| 27 | 🇲🇴 MO | 800 |
| 28 | 🇲🇪 ME | 755 |
| 29 | 🇳🇱 NL | 728 |
| 30 | 🇮🇩 ID | 588 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1562 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1160 |
| 4 | Indira Gandhi International Airport |  | IN | 1056 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1021 |
| 6 | Frankfurt am Main International Airport |  | DE | 895 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 873 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 837 |
| 11 | Zurich Airport |  | CH | 827 |
| 12 | Macau International Airport |  | MO | 800 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 700 |
| 14 | Chicago O'Hare International Airport |  | US | 671 |
| 15 | Kuala Lumpur International Airport |  | MY | 668 |
| 16 | Madrid Barajas International Airport |  | ES | 666 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 628 |
| 18 | Malpensa International Airport |  | IT | 609 |
| 19 | Bengaluru International Airport |  | IN | 605 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 603 |
| 21 | Salt Lake City International Airport |  | US | 568 |
| 22 | Congonhas Airport |  | BR | 559 |
| 23 | Charlotte/Douglas International Airport |  | US | 552 |
| 24 | Charles de Gaulle International Airport |  | FR | 550 |
| 25 | Tenerife Norte Airport |  | ES | 544 |
| 26 | Capua Airport |  | IT | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Daniel K Inouye International Airport |  | US | 511 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 510 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 494 |
| 31 | Barcelona International Airport |  | ES | 486 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 474 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 441 |
| 37 | O. R. Tambo International Airport |  | ZA | 438 |
| 38 | Amsterdam Airport Schiphol |  | NL | 430 |
| 39 | Reno/Tahoe International Airport |  | US | 416 |
| 40 | Calgary International Airport |  | CA | 415 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 241 | 21m | 244 km | 1,014.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 174 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
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
| ES807 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-05 22:32 UTC | 2026-05-05 22:56 UTC | 24m |
| XIH | XIH | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-05-05 22:06 UTC | 2026-05-05 22:53 UTC | 47m |
| R21236 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-05 20:12 UTC | 2026-05-05 22:49 UTC | 2h 37m |
| URSA26 | URS | Fairbanks International Airport (PAFA) | Ladd Army Air Field (PAFB) | 2026-05-05 22:08 UTC | 2026-05-05 22:46 UTC | 38m |
| ARCAS44 | ARC | Wichita Valley Airport (KF14) | TX02 (TX02) | 2026-05-05 22:26 UTC | 2026-05-05 22:44 UTC | 17m |
| CPA395 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-05-05 20:08 UTC | 2026-05-05 22:43 UTC | 2h 35m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 22:29 UTC | 2026-05-05 22:43 UTC | 13m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-05-05 11:57 UTC | 2026-05-05 22:40 UTC | 10h 42m |
| THY170 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-05 13:37 UTC | 2026-05-05 22:39 UTC | 9h 1m |
| N604D |  | Pensacola International Airport (KPNS) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-05 21:44 UTC | 2026-05-05 22:34 UTC | 50m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-05-05 12:05 UTC | 2026-05-05 22:34 UTC | 10h 28m |
| N722KP |  | Juneau International Airport (PAJN) | Mule Creek Airport (CBS4) | 2026-05-05 22:10 UTC | 2026-05-05 22:34 UTC | 23m |
| N169ES |  | Van Nuys Airport (KVNY) | Santa Monica Municipal Airport (KSMO) | 2026-05-05 22:25 UTC | 2026-05-05 22:33 UTC | 7m |
| XE1191 |  | Scottsdale Airport (KSDL) | Santa Monica Municipal Airport (KSMO) | 2026-05-05 21:08 UTC | 2026-05-05 22:30 UTC | 1h 22m |
| N540M |  | Tri-State/Milton J Ferguson Field (KHTS) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-05 22:03 UTC | 2026-05-05 22:28 UTC | 25m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-05-05 10:42 UTC | 2026-05-05 22:28 UTC | 11h 45m |
| FDY158 | FDY | Pittsburgh International Airport (KPIT) | Lancaster Airport (KLNS) | 2026-05-05 21:15 UTC | 2026-05-05 22:27 UTC | 1h 12m |
| N6045F |  | Conroe/North Houston Regional Airport (KCXO) | Navasota Municipal Airport (K60R) | 2026-05-05 21:36 UTC | 2026-05-05 22:27 UTC | 50m |
| VOZ630 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Collector Airport (YCLT) | 2026-05-05 21:52 UTC | 2026-05-05 22:20 UTC | 28m |
| STAG01 | STA | Wichita Valley Airport (KF14) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-05-05 22:02 UTC | 2026-05-05 22:20 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
