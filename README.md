# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_14:02:06_UTC-green)

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

**Latest saved flight:** 2026-05-08 14:02:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 14:02:06 UTC

- **73,215** saved flights
- **27,127** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **73,215** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **902,274.4 tonnes** estimated CO2 emissions
- **52,305,764 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3154 |
| 2 | SkyWest Airlines | 2715 |
| 3 | IndiGo | 1656 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 947 |
| 8 | ENY | 915 |
| 9 | Vueling | 715 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 678 |
| 12 | WIF | 636 |
| 13 | Delta Air Lines | 625 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 589 |
| 16 | QLK | 573 |
| 17 | Swiss International | 562 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 485 |
| 21 | EJU | 471 |
| 22 | AEE | 469 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 434 |
| 26 | Air France | 426 |
| 27 | AXB | 407 |
| 28 | CXK | 372 |
| 29 | AIQ | 366 |
| 30 | United Airlines | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58515 |
| 2 | 🇪🇸 ES | 5304 |
| 3 | 🇮🇳 IN | 5203 |
| 4 | 🇦🇺 AU | 4901 |
| 5 | 🇩🇪 DE | 4095 |
| 6 | 🇧🇷 BR | 4093 |
| 7 | 🇮🇹 IT | 4019 |
| 8 | 🇯🇵 JP | 3874 |
| 9 | 🇨🇦 CA | 3643 |
| 10 | 🇬🇧 GB | 3156 |
| 11 | 🇫🇷 FR | 2896 |
| 12 | 🇨🇴 CO | 2681 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2168 |
| 15 | 🇳🇴 NO | 2045 |
| 16 | 🇨🇭 CH | 2001 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1435 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1317 |
| 21 | 🇹🇭 TH | 1314 |
| 22 | 🇵🇱 PL | 1227 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇰🇷 KR | 1151 |
| 25 | 🇬🇹 GT | 1149 |
| 26 | 🇲🇦 MA | 872 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 785 |
| 29 | 🇳🇱 NL | 767 |
| 30 | 🇧🇸 BS | 614 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1302 |
| 3 | Denver International Airport |  | US | 1219 |
| 4 | Indira Gandhi International Airport |  | IN | 1097 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1062 |
| 6 | Frankfurt am Main International Airport |  | DE | 944 |
| 7 | Harry Reid International Airport |  | US | 911 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 876 |
| 10 | Zurich Airport |  | CH | 867 |
| 11 | La Aurora Airport |  | GT | 856 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 734 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 696 |
| 16 | Madrid Barajas International Airport |  | ES | 685 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 639 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 20 | Bengaluru International Airport |  | IN | 635 |
| 21 | Salt Lake City International Airport |  | US | 596 |
| 22 | Charlotte/Douglas International Airport |  | US | 575 |
| 23 | Congonhas Airport |  | BR | 575 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 570 |
| 26 | Tenerife Norte Airport |  | ES | 556 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 535 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 529 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 505 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 495 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 491 |
| 34 | Vitoria/Foronda Airport |  | ES | 478 |
| 35 | Don Mueang International Airport |  | TH | 462 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 461 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 460 |
| 38 | Amsterdam Airport Schiphol |  | NL | 459 |
| 39 | O. R. Tambo International Airport |  | ZA | 450 |
| 40 | Calgary International Airport |  | CA | 435 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 364 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 257 | 21m | 244 km | 1,082.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 181 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 162 | 26m | 275 km | 767.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 111 | 27m | 215 km | 411.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 109 | 20m | 147 km | 275.8 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 98 | 1h 43m | 1,423 km | 2,405.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 91 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DENIZ | DEN | Dortmund Airport (EDLW) | Munster-Telgte Airport (EDLT) | 2026-05-08 13:27 UTC | 2026-05-08 14:02 UTC | 34m |
| SCA35 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-05-08 13:21 UTC | 2026-05-08 14:01 UTC | 40m |
| N5011K |  | TX91 (TX91) | Lancaster Regional Airport (KLNC) | 2026-05-08 13:34 UTC | 2026-05-08 13:59 UTC | 25m |
| N3739W |  | Lincoln Regional/Karl Harder Field (KLHM) | Sacramento Mather Airport (KMHR) | 2026-05-08 13:40 UTC | 2026-05-08 13:57 UTC | 17m |
| PDU66 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-05-08 13:36 UTC | 2026-05-08 13:54 UTC | 18m |
| CES5014 | China Eastern | Malpensa International Airport (LIMC) | Pskov Airport (ULOO) | 2026-05-08 11:48 UTC | 2026-05-08 13:52 UTC | 2h 4m |
| SWR2PA | Swiss International | Nice-Cote d'Azur Airport (LFMN) | Zurich Airport (LSZH) | 2026-05-08 12:53 UTC | 2026-05-08 13:46 UTC | 52m |
| N900HS |  | Clearwater Executive Airport (KCLW) | Peter O Knight Airport (KTPF) | 2026-05-08 13:25 UTC | 2026-05-08 13:37 UTC | 12m |
| N551LX |  | Frederick Municipal Airport (KFDK) | PS25 (PS25) | 2026-05-08 13:26 UTC | 2026-05-08 13:36 UTC | 10m |
| DFBOX | DFB | Coburg-Brandensteinsebene Airport (EDQC) | Oelde Bergeler Airport (EDLU) | 2026-05-08 12:52 UTC | 2026-05-08 13:36 UTC | 44m |
| HBMGB | HBM | St Gallen Altenrhein Airport (LSZR) | Bad Ragaz Airport (LSZE) | 2026-05-08 13:25 UTC | 2026-05-08 13:35 UTC | 10m |
| WIRE31 | WIR | Sopwith Ldg Airport (OK56) | Sopwith Ldg Airport (OK56) | 2026-05-08 13:08 UTC | 2026-05-08 13:26 UTC | 18m |
| N695SU |  | Miller-Herrold Airport (28MI) | Shangrila Airport (WS25) | 2026-05-08 12:39 UTC | 2026-05-08 13:26 UTC | 46m |
| DAL2717 | Delta Air Lines | San Antonio International Airport (KSAT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 11:15 UTC | 2026-05-08 13:26 UTC | 2h 10m |
| BABOON6 | BAB | KF31 (KF31) | KF31 (KF31) | 2026-05-08 13:25 UTC | 2026-05-08 13:26 UTC | 0m |
| N102JS |  | Pocono Mountains Regional Airport (KMPO) | Lancaster Airport (KLNS) | 2026-05-08 12:51 UTC | 2026-05-08 13:25 UTC | 34m |
| N202AB |  | Eifling Field (39AR) | Thunder Ridge Ranch Airport (45AR) | 2026-05-08 13:10 UTC | 2026-05-08 13:25 UTC | 14m |
| IGO9287 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Naypyidaw Airport (VYEL) | 2026-05-08 12:21 UTC | 2026-05-08 13:24 UTC | 1h 3m |
| N183TS |  | Columbus Airport (KCSG) | Austin-Bergstrom International Airport (KAUS) | 2026-05-08 11:18 UTC | 2026-05-08 13:24 UTC | 2h 5m |
| N350WC |  | 5TA2 (5TA2) | XS10 (XS10) | 2026-05-08 12:47 UTC | 2026-05-08 13:24 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
