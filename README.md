# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_15:13:13_UTC-green)

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

**Latest saved flight:** 2026-05-01 15:13:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 15:13:13 UTC

- **62,277** saved flights
- **23,885** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **62,277** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **760,223.2 tonnes** estimated CO2 emissions
- **44,070,913 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2616 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1424 |
| 4 | EJA | 1119 |
| 5 | American Airlines | 969 |
| 6 | Southwest Airlines | 880 |
| 7 | Lufthansa | 802 |
| 8 | ENY | 765 |
| 9 | Vueling | 611 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 588 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 528 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 510 |
| 16 | QLK | 498 |
| 17 | Swiss International | 481 |
| 18 | LXJ | 442 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 407 |
| 21 | easyJet | 404 |
| 22 | EJU | 399 |
| 23 | VIV | 390 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 361 |
| 27 | AXB | 346 |
| 28 | AIQ | 319 |
| 29 | CXK | 308 |
| 30 | MXY | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49196 |
| 2 | 🇪🇸 ES | 4501 |
| 3 | 🇮🇳 IN | 4500 |
| 4 | 🇦🇺 AU | 4287 |
| 5 | 🇧🇷 BR | 3534 |
| 6 | 🇩🇪 DE | 3463 |
| 7 | 🇯🇵 JP | 3409 |
| 8 | 🇮🇹 IT | 3384 |
| 9 | 🇨🇦 CA | 3061 |
| 10 | 🇬🇧 GB | 2654 |
| 11 | 🇨🇴 CO | 2635 |
| 12 | 🇫🇷 FR | 2454 |
| 13 | 🇲🇽 MX | 1954 |
| 14 | 🇬🇷 GR | 1852 |
| 15 | 🇨🇭 CH | 1744 |
| 16 | 🇳🇴 NO | 1725 |
| 17 | 🇲🇾 MY | 1489 |
| 18 | 🇿🇦 ZA | 1269 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1127 |
| 21 | 🇹🇷 TR | 1100 |
| 22 | 🇵🇭 PH | 1062 |
| 23 | 🇰🇷 KR | 1008 |
| 24 | 🇵🇱 PL | 1005 |
| 25 | 🇬🇹 GT | 945 |
| 26 | 🇲🇦 MA | 764 |
| 27 | 🇲🇴 MO | 701 |
| 28 | 🇲🇪 ME | 678 |
| 29 | 🇳🇱 NL | 648 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1373 |
| 2 | Tokyo International Airport |  | JP | 1152 |
| 3 | Denver International Airport |  | US | 1027 |
| 4 | Indira Gandhi International Airport |  | IN | 948 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 907 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 830 |
| 8 | Frankfurt am Main International Airport |  | DE | 800 |
| 9 | Harry Reid International Airport |  | US | 792 |
| 10 | Zurich Airport |  | CH | 740 |
| 11 | La Aurora Airport |  | GT | 707 |
| 12 | Macau International Airport |  | MO | 701 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Kuala Lumpur International Airport |  | MY | 590 |
| 15 | Chicago O'Hare International Airport |  | US | 585 |
| 16 | Madrid Barajas International Airport |  | ES | 582 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 565 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 541 |
| 20 | Malpensa International Airport |  | IT | 537 |
| 21 | Congonhas Airport |  | BR | 509 |
| 22 | Charlotte/Douglas International Airport |  | US | 495 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Tenerife Norte Airport |  | ES | 485 |
| 25 | Charles de Gaulle International Airport |  | FR | 483 |
| 26 | Ninoy Aquino International Airport |  | PH | 482 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 461 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 452 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 448 |
| 31 | Barcelona International Airport |  | ES | 417 |
| 32 | Vitoria/Foronda Airport |  | ES | 416 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 410 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 406 |
| 35 | O. R. Tambo International Airport |  | ZA | 400 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 393 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 387 |
| 39 | Amsterdam Airport Schiphol |  | NL | 382 |
| 40 | Calgary International Airport |  | CA | 367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 341 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 208 | 21m | 244 km | 875.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 151 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 140 | 26m | 275 km | 663.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 110 | 20m | 99 km | 188.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 101 | 20m | 250 km | 436.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 95 | 28m | 152 km | 248.3 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 94 | 20m | 147 km | 237.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 86 | 1h 1m | 695 km | 1,030.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 80 | 1h 43m | 1,423 km | 1,963.3 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XBPHW | XBP | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-05-01 13:53 UTC | 2026-05-01 15:13 UTC | 1h 19m |
| N6042Z |  | Sarasota/Bradenton International Airport (KSRQ) | Wauchula Municipal Airport (KCHN) | 2026-05-01 14:40 UTC | 2026-05-01 15:13 UTC | 32m |
| N627AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-01 14:35 UTC | 2026-05-01 15:11 UTC | 36m |
| N271SH |  | 0TS2 (0TS2) | Perot Field/Fort Worth Alliance Airport (KAFW) | 2026-05-01 14:33 UTC | 2026-05-01 15:10 UTC | 36m |
| N262BC |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-05-01 14:45 UTC | 2026-05-01 15:07 UTC | 22m |
| N616ML |  | Logan-Cache Airport (KLGU) | Malad City Airport (KMLD) | 2026-05-01 14:27 UTC | 2026-05-01 15:05 UTC | 38m |
| CXK448 | CXK | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-01 14:48 UTC | 2026-05-01 15:03 UTC | 15m |
| N649GC |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-01 14:39 UTC | 2026-05-01 15:02 UTC | 23m |
| GPJCN | GPJ | Norwich International Airport (EGSH) | EGYO (EGYO) | 2026-05-01 14:29 UTC | 2026-05-01 14:58 UTC | 28m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-01 14:27 UTC | 2026-05-01 14:54 UTC | 26m |
| GFRGP | GFR | Coventry Airport (EGBE) | Netherthorpe Airfield (EGNF) | 2026-05-01 14:32 UTC | 2026-05-01 14:54 UTC | 21m |
| OST39 | OST | Stillwater Regional Airport (KSWO) | Hilltop Airport (40OK) | 2026-05-01 14:38 UTC | 2026-05-01 14:53 UTC | 15m |
| N73424 |  | Cedar Creek Airport (MO74) | Mexico Memorial Airport (KMYJ) | 2026-05-01 14:39 UTC | 2026-05-01 14:52 UTC | 13m |
| N429NA |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-05-01 13:41 UTC | 2026-05-01 14:48 UTC | 1h 7m |
| N528SV |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-05-01 14:22 UTC | 2026-05-01 14:47 UTC | 25m |
| N80790 |  | Dupage Airport (KDPA) | Lake In The Hills Airport (K3CK) | 2026-05-01 14:32 UTC | 2026-05-01 14:45 UTC | 12m |
| SCA5 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-05-01 14:19 UTC | 2026-05-01 14:44 UTC | 24m |
| N945TE |  | Lebanon Municipal Airport (KM54) | Lebanon Municipal Airport (KM54) | 2026-05-01 14:42 UTC | 2026-05-01 14:44 UTC | 2m |
| BOX502 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-01 04:05 UTC | 2026-05-01 14:43 UTC | 10h 38m |
| N40XJ |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 14:15 UTC | 2026-05-01 14:41 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
