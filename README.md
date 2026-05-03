# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_23:45:35_UTC-green)

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

**Latest saved flight:** 2026-05-03 23:45:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 23:45:35 UTC

- **67,023** saved flights
- **25,287** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,023** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **822,864.6 tonnes** estimated CO2 emissions
- **47,702,294 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2857 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1546 |
| 4 | EJA | 1200 |
| 5 | American Airlines | 1039 |
| 6 | Southwest Airlines | 944 |
| 7 | Lufthansa | 857 |
| 8 | ENY | 828 |
| 9 | Vueling | 661 |
| 10 | AXM | 649 |
| 11 | LATAM Airlines | 625 |
| 12 | All Nippon Airways | 575 |
| 13 | Delta Air Lines | 562 |
| 14 | WIF | 559 |
| 15 | AZU | 542 |
| 16 | QLK | 517 |
| 17 | Swiss International | 514 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 454 |
| 20 | easyJet | 444 |
| 21 | AEE | 436 |
| 22 | EJU | 432 |
| 23 | VIV | 418 |
| 24 | Cathay Pacific | 403 |
| 25 | Air France | 390 |
| 26 | Japan Airlines | 388 |
| 27 | AXB | 376 |
| 28 | CXK | 342 |
| 29 | AIQ | 339 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53118 |
| 2 | 🇪🇸 ES | 4909 |
| 3 | 🇮🇳 IN | 4859 |
| 4 | 🇦🇺 AU | 4435 |
| 5 | 🇧🇷 BR | 3768 |
| 6 | 🇩🇪 DE | 3742 |
| 7 | 🇮🇹 IT | 3656 |
| 8 | 🇯🇵 JP | 3597 |
| 9 | 🇨🇦 CA | 3290 |
| 10 | 🇬🇧 GB | 2892 |
| 11 | 🇫🇷 FR | 2654 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2133 |
| 14 | 🇬🇷 GR | 2000 |
| 15 | 🇨🇭 CH | 1869 |
| 16 | 🇳🇴 NO | 1816 |
| 17 | 🇲🇾 MY | 1601 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1246 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1205 |
| 22 | 🇵🇭 PH | 1114 |
| 23 | 🇵🇱 PL | 1099 |
| 24 | 🇬🇹 GT | 1091 |
| 25 | 🇰🇷 KR | 1076 |
| 26 | 🇲🇦 MA | 821 |
| 27 | 🇲🇴 MO | 755 |
| 28 | 🇲🇪 ME | 724 |
| 29 | 🇳🇱 NL | 708 |
| 30 | 🇮🇩 ID | 569 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1481 |
| 2 | Tokyo International Airport |  | JP | 1213 |
| 3 | Denver International Airport |  | US | 1107 |
| 4 | Indira Gandhi International Airport |  | IN | 1015 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 974 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 863 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 835 |
| 10 | La Aurora Airport |  | GT | 810 |
| 11 | Zurich Airport |  | CH | 793 |
| 12 | Macau International Airport |  | MO | 755 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 661 |
| 14 | Chicago O'Hare International Airport |  | US | 642 |
| 15 | Madrid Barajas International Airport |  | ES | 640 |
| 16 | Kuala Lumpur International Airport |  | MY | 639 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 594 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 584 |
| 20 | Malpensa International Airport |  | IT | 577 |
| 21 | Congonhas Airport |  | BR | 541 |
| 22 | Salt Lake City International Airport |  | US | 534 |
| 23 | Tenerife Norte Airport |  | ES | 533 |
| 24 | Charlotte/Douglas International Airport |  | US | 529 |
| 25 | Charles de Gaulle International Airport |  | FR | 524 |
| 26 | Ninoy Aquino International Airport |  | PH | 507 |
| 27 | Capua Airport |  | IT | 505 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 488 |
| 29 | Daniel K Inouye International Airport |  | US | 487 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 472 |
| 31 | Barcelona International Airport |  | ES | 459 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 453 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 444 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 421 |
| 38 | Amsterdam Airport Schiphol |  | NL | 416 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 227 | 21m | 244 km | 955.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 204 | 24m | 225 km | 791.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 167 | 20m | 165 km | 475.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 112 | 27m | 152 km | 292.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 111 | 31m | 369 km | 706.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 96 | 1h 41m | 1,156 km | 1,915.2 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 89 | 1h 42m | 1,423 km | 2,184.2 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N690MF |  | Fentress Airpark (XS90) | Fentress Airpark (XS90) | 2026-05-03 22:49 UTC | 2026-05-03 23:45 UTC | 55m |
| ERU42 | ERU | 42AZ (42AZ) | 42AZ (42AZ) | 2026-05-03 23:35 UTC | 2026-05-03 23:45 UTC | 10m |
| UAE9848 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-05-03 17:17 UTC | 2026-05-03 23:36 UTC | 6h 19m |
| UPS5852 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-03 20:14 UTC | 2026-05-03 23:36 UTC | 3h 21m |
| TVR4703 | TVR | Sharjah International Airport (OMSJ) | Macau International Airport (VMMC) | 2026-05-03 16:58 UTC | 2026-05-03 23:29 UTC | 6h 31m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 23:15 UTC | 2026-05-03 23:26 UTC | 11m |
| N921RA |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-03 22:54 UTC | 2026-05-03 23:25 UTC | 30m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-03 19:18 UTC | 2026-05-03 23:24 UTC | 4h 5m |
| N560ML |  | Centennial Airport (KAPA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-03 21:38 UTC | 2026-05-03 23:21 UTC | 1h 42m |
| N606LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-03 22:41 UTC | 2026-05-03 23:20 UTC | 39m |
| N |  | Texada Gillies Bay Airport (CYGB) | Vancouver International Airport (CYVR) | 2026-05-03 23:00 UTC | 2026-05-03 23:20 UTC | 19m |
| N331SK |  | Mc Ghee Tyson Airport (KTYS) | Okc Will Rogers International Airport (KOKC) | 2026-05-03 21:24 UTC | 2026-05-03 23:20 UTC | 1h 55m |
| MXY808 | MXY | Orlando International Airport (KMCO) | Lancaster Airport (KLNS) | 2026-05-03 21:20 UTC | 2026-05-03 23:19 UTC | 1h 59m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-05-03 22:49 UTC | 2026-05-03 23:12 UTC | 23m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 23:01 UTC | 2026-05-03 23:12 UTC | 11m |
| VT698 |  | Moorea Airport (NTTM) | Tikehau Airport (NTGC) | 2026-05-03 20:57 UTC | 2026-05-03 23:11 UTC | 2h 14m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-03 22:54 UTC | 2026-05-03 23:10 UTC | 16m |
| QLK581D | QLK | Adelaide International Airport (YPAD) | Port Lincoln Airport (YPLC) | 2026-05-03 22:35 UTC | 2026-05-03 23:10 UTC | 34m |
| ZJF | ZJF | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-05-03 22:45 UTC | 2026-05-03 23:09 UTC | 23m |
| N169BA |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-05-03 22:59 UTC | 2026-05-03 23:02 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
