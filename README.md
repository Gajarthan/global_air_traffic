# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_07:18:42_UTC-green)

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

**Latest saved flight:** 2026-05-01 07:18:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 07:18:42 UTC

- **61,754** saved flights
- **23,733** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,754** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **753,402.0 tonnes** estimated CO2 emissions
- **43,675,480 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2585 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1412 |
| 4 | EJA | 1117 |
| 5 | American Airlines | 964 |
| 6 | Southwest Airlines | 877 |
| 7 | Lufthansa | 783 |
| 8 | ENY | 765 |
| 9 | Vueling | 608 |
| 10 | AXM | 602 |
| 11 | LATAM Airlines | 585 |
| 12 | All Nippon Airways | 545 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 502 |
| 16 | QLK | 497 |
| 17 | Swiss International | 479 |
| 18 | LXJ | 439 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 403 |
| 21 | easyJet | 400 |
| 22 | EJU | 395 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 377 |
| 25 | Japan Airlines | 360 |
| 26 | Air France | 358 |
| 27 | AXB | 339 |
| 28 | AIQ | 316 |
| 29 | CXK | 306 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48944 |
| 2 | 🇮🇳 IN | 4457 |
| 3 | 🇪🇸 ES | 4439 |
| 4 | 🇦🇺 AU | 4275 |
| 5 | 🇧🇷 BR | 3493 |
| 6 | 🇩🇪 DE | 3413 |
| 7 | 🇯🇵 JP | 3362 |
| 8 | 🇮🇹 IT | 3352 |
| 9 | 🇨🇦 CA | 3056 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2606 |
| 12 | 🇫🇷 FR | 2415 |
| 13 | 🇲🇽 MX | 1948 |
| 14 | 🇬🇷 GR | 1822 |
| 15 | 🇨🇭 CH | 1715 |
| 16 | 🇳🇴 NO | 1698 |
| 17 | 🇲🇾 MY | 1468 |
| 18 | 🇿🇦 ZA | 1253 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1116 |
| 21 | 🇹🇷 TR | 1091 |
| 22 | 🇵🇭 PH | 1056 |
| 23 | 🇰🇷 KR | 999 |
| 24 | 🇵🇱 PL | 990 |
| 25 | 🇬🇹 GT | 922 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 696 |
| 28 | 🇲🇪 ME | 671 |
| 29 | 🇳🇱 NL | 646 |
| 30 | 🇮🇩 ID | 527 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1370 |
| 2 | Tokyo International Airport |  | JP | 1137 |
| 3 | Denver International Airport |  | US | 1025 |
| 4 | Indira Gandhi International Airport |  | IN | 939 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 896 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 790 |
| 9 | Frankfurt am Main International Airport |  | DE | 779 |
| 10 | Zurich Airport |  | CH | 735 |
| 11 | Macau International Airport |  | MO | 696 |
| 12 | La Aurora Airport |  | GT | 691 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Chicago O'Hare International Airport |  | US | 583 |
| 15 | Kuala Lumpur International Airport |  | MY | 580 |
| 16 | Madrid Barajas International Airport |  | ES | 574 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 563 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 557 |
| 19 | Bengaluru International Airport |  | IN | 536 |
| 20 | Malpensa International Airport |  | IT | 534 |
| 21 | Congonhas Airport |  | BR | 504 |
| 22 | Charlotte/Douglas International Airport |  | US | 491 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Ninoy Aquino International Airport |  | PH | 479 |
| 25 | Charles de Gaulle International Airport |  | FR | 476 |
| 26 | Tenerife Norte Airport |  | ES | 474 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 460 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 448 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 446 |
| 31 | Barcelona International Airport |  | ES | 414 |
| 32 | Vitoria/Foronda Airport |  | ES | 411 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 409 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 402 |
| 35 | O. R. Tambo International Airport |  | ZA | 394 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 389 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 384 |
| 39 | Amsterdam Airport Schiphol |  | NL | 381 |
| 40 | Calgary International Airport |  | CA | 366 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 337 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 207 | 21m | 244 km | 871.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 182 | 1h 27m | 910 km | 2,856.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 177 | 28m | 304 km | 927.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 152 | 19m | 165 km | 432.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 148 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 131 | 1h 12m | 770 km | 1,740.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 104 | 31m | 369 km | 662.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 82 | 14m | 154 km | 217.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR818 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-01 00:27 UTC | 2026-05-01 07:18 UTC | 6h 51m |
| DH07A |  | Suwon Airport (RKSW) | G 501 Airport (RK52) | 2026-05-01 06:56 UTC | 2026-05-01 07:08 UTC | 11m |
| IGO246F | IndiGo | Juhu Aerodrome (VAJJ) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-01 05:01 UTC | 2026-05-01 07:04 UTC | 2h 2m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-04-30 20:02 UTC | 2026-05-01 07:00 UTC | 10h 58m |
| CPA335 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-30 23:31 UTC | 2026-05-01 06:58 UTC | 7h 26m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-30 20:04 UTC | 2026-05-01 06:53 UTC | 10h 49m |
| DCSEB | DCS | Strasbourg Airport (LFST) | Trento / Mattarello Airport (LIDT) | 2026-05-01 06:11 UTC | 2026-05-01 06:53 UTC | 42m |
| ZUMGL | ZUM | Delta 200 Airstrip (FADX) | Stellenbosch Airport (FASH) | 2026-05-01 06:28 UTC | 2026-05-01 06:48 UTC | 19m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-30 18:53 UTC | 2026-05-01 06:47 UTC | 11h 54m |
| N54DD |  | K4SD (K4SD) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-01 06:09 UTC | 2026-05-01 06:45 UTC | 35m |
| UPS913 | UPS | John Wayne/Orange County Airport (KSNA) | Double Eagle Ii Airport (KAEG) | 2026-05-01 05:34 UTC | 2026-05-01 06:45 UTC | 1h 10m |
| IUB | IUB | Warrnambool Airport (YWBL) | Cape Otway Airport (YCTY) | 2026-05-01 06:16 UTC | 2026-05-01 06:43 UTC | 26m |
| KLM887 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-04-30 19:33 UTC | 2026-05-01 06:43 UTC | 11h 9m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-05-01 06:08 UTC | 2026-05-01 06:37 UTC | 29m |
| EJU828E | EJU | Toulouse-Blagnac Airport (LFBO) | Lyon Saint-Exupery Airport (LFLL) | 2026-05-01 05:53 UTC | 2026-05-01 06:36 UTC | 43m |
| LOG32MW | LOG | Glasgow International Airport (EGPF) | XPLO (XPLO) | 2026-05-01 06:12 UTC | 2026-05-01 06:34 UTC | 21m |
| VOE3544 | VOE | Asturias Airport (LEAS) | Federico Garcia Lorca Airport (LEGR) | 2026-05-01 05:27 UTC | 2026-05-01 06:34 UTC | 1h 6m |
| CT347 |  | Perth International Airport (YPPH) | Kalgoorlie-Boulder Airport (YPKG) | 2026-05-01 05:33 UTC | 2026-05-01 06:34 UTC | 1h 0m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Tribhuvan International Airport (VNKT) | 2026-05-01 03:31 UTC | 2026-05-01 06:30 UTC | 2h 58m |
| FFT3885 | FFT | Dallas-Fort Worth International Airport (KDFW) | Harry Reid International Airport (KLAS) | 2026-05-01 03:59 UTC | 2026-05-01 06:30 UTC | 2h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
