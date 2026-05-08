# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_21:58:08_UTC-green)

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

**Latest saved flight:** 2026-05-08 21:58:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 21:58:08 UTC

- **74,448** saved flights
- **27,548** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **74,448** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **915,490.4 tonnes** estimated CO2 emissions
- **53,071,907 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3200 |
| 2 | SkyWest Airlines | 2766 |
| 3 | IndiGo | 1664 |
| 4 | EJA | 1378 |
| 5 | American Airlines | 1161 |
| 6 | Southwest Airlines | 1081 |
| 7 | Lufthansa | 963 |
| 8 | ENY | 930 |
| 9 | Vueling | 725 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 691 |
| 12 | Delta Air Lines | 668 |
| 13 | WIF | 649 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 598 |
| 16 | QLK | 573 |
| 17 | Swiss International | 566 |
| 18 | LXJ | 553 |
| 19 | Alaska Airlines | 523 |
| 20 | easyJet | 490 |
| 21 | EJU | 479 |
| 22 | AEE | 478 |
| 23 | Cathay Pacific | 462 |
| 24 | VIV | 453 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 430 |
| 27 | AXB | 411 |
| 28 | CXK | 382 |
| 29 | AIQ | 366 |
| 30 | United Airlines | 361 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 59975 |
| 2 | 🇪🇸 ES | 5374 |
| 3 | 🇮🇳 IN | 5233 |
| 4 | 🇦🇺 AU | 4909 |
| 5 | 🇧🇷 BR | 4177 |
| 6 | 🇩🇪 DE | 4166 |
| 7 | 🇮🇹 IT | 4061 |
| 8 | 🇯🇵 JP | 3877 |
| 9 | 🇨🇦 CA | 3714 |
| 10 | 🇬🇧 GB | 3193 |
| 11 | 🇫🇷 FR | 2939 |
| 12 | 🇨🇴 CO | 2690 |
| 13 | 🇲🇽 MX | 2307 |
| 14 | 🇬🇷 GR | 2198 |
| 15 | 🇳🇴 NO | 2076 |
| 16 | 🇨🇭 CH | 2016 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1338 |
| 20 | 🇹🇷 TR | 1328 |
| 21 | 🇹🇭 TH | 1317 |
| 22 | 🇵🇱 PL | 1244 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1177 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 885 |
| 27 | 🇲🇴 MO | 855 |
| 28 | 🇲🇪 ME | 796 |
| 29 | 🇳🇱 NL | 774 |
| 30 | 🇧🇸 BS | 626 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1649 |
| 2 | Tokyo International Airport |  | JP | 1303 |
| 3 | Denver International Airport |  | US | 1249 |
| 4 | Indira Gandhi International Airport |  | IN | 1106 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1077 |
| 6 | Frankfurt am Main International Airport |  | DE | 959 |
| 7 | Harry Reid International Airport |  | US | 929 |
| 8 | Guaymaral Airport |  | CO | 885 |
| 9 | La Aurora Airport |  | GT | 882 |
| 10 | El Dorado International Airport |  | CO | 878 |
| 11 | Zurich Airport |  | CH | 876 |
| 12 | Macau International Airport |  | MO | 855 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 751 |
| 14 | Chicago O'Hare International Airport |  | US | 721 |
| 15 | Madrid Barajas International Airport |  | ES | 699 |
| 16 | Kuala Lumpur International Airport |  | MY | 696 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 661 |
| 18 | Malpensa International Airport |  | IT | 643 |
| 19 | Bengaluru International Airport |  | IN | 641 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 609 |
| 22 | Congonhas Airport |  | BR | 591 |
| 23 | Charlotte/Douglas International Airport |  | US | 587 |
| 24 | Charles de Gaulle International Airport |  | FR | 576 |
| 25 | Capua Airport |  | IT | 575 |
| 26 | Tenerife Norte Airport |  | ES | 559 |
| 27 | Daniel K Inouye International Airport |  | US | 543 |
| 28 | Ninoy Aquino International Airport |  | PH | 543 |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 532 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 532 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 513 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 501 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 497 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 467 |
| 37 | Amsterdam Airport Schiphol |  | NL | 466 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 443 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
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
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA683 | LFA | Jacksonville Executive At Craig Airport (KCRG) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-08 20:43 UTC | 2026-05-08 21:58 UTC | 1h 14m |
| PDU57 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-05-08 21:18 UTC | 2026-05-08 21:56 UTC | 38m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-08 11:04 UTC | 2026-05-08 21:52 UTC | 10h 47m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-08 17:44 UTC | 2026-05-08 21:48 UTC | 4h 3m |
| N50PE |  | Harrisburg International Airport (KMDT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-08 20:56 UTC | 2026-05-08 21:48 UTC | 51m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-08 10:42 UTC | 2026-05-08 21:44 UTC | 11h 2m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-08 21:25 UTC | 2026-05-08 21:42 UTC | 17m |
| N66DV |  | Crazy Horse Airport (12WV) | West Virginia International Yeager Airport (KCRW) | 2026-05-08 21:20 UTC | 2026-05-08 21:40 UTC | 20m |
| N5276P |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-08 21:18 UTC | 2026-05-08 21:40 UTC | 22m |
| N164YF |  | Harvey's Acres Airport (OR28) | Green Acres Air Park (7OR6) | 2026-05-08 20:52 UTC | 2026-05-08 21:39 UTC | 46m |
| N912BL |  | Winter Haven Regional Airport (KGIF) | Lake Wales Municipal Airport (KX07) | 2026-05-08 21:25 UTC | 2026-05-08 21:36 UTC | 10m |
| CONGO64 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-05-08 20:24 UTC | 2026-05-08 21:34 UTC | 1h 9m |
| N26793 |  | Dekalb-Peachtree Airport (KPDK) | Pickens County Airport (KJZP) | 2026-05-08 21:08 UTC | 2026-05-08 21:29 UTC | 20m |
| JINX31 | JIN | Circle P Ranch Airport (82XS) | Kenedy Regional Airport (K2R9) | 2026-05-08 21:12 UTC | 2026-05-08 21:28 UTC | 16m |
| NCR549 | NCR | Netaji Subhash Chandra Bose International Airport (VECC) | Zhuhai Airport (ZGSD) | 2026-05-08 18:30 UTC | 2026-05-08 21:27 UTC | 2h 57m |
| N522CP |  | French Valley Airport (KF70) | Lake Havasu City Airport (KHII) | 2026-05-08 20:30 UTC | 2026-05-08 21:27 UTC | 57m |
| N905XX |  | City Of Colorado Springs Municipal Airport (KCOS) | Pinon Canyon Airport (0CD5) | 2026-05-08 19:56 UTC | 2026-05-08 21:26 UTC | 1h 29m |
| N329MH |  | Phoenix Deer Valley Airport (KDVT) | Parsons Field (4AZ6) | 2026-05-08 20:59 UTC | 2026-05-08 21:24 UTC | 25m |
| CFC0540 | CFC | Denver International Airport (KDEN) | Brandon Municipal Airport (CYBR) | 2026-05-08 15:01 UTC | 2026-05-08 21:22 UTC | 6h 20m |
| CXK606 | CXK | Fort Worth Meacham International Airport (KFTW) | Jim Sears Airport (3TA7) | 2026-05-08 20:36 UTC | 2026-05-08 21:21 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
