# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_05:35:22_UTC-green)

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

**Latest saved flight:** 2026-05-02 05:35:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 05:35:22 UTC

- **63,499** saved flights
- **24,268** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,499** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **775,710.8 tonnes** estimated CO2 emissions
- **44,968,744 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2656 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1449 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 989 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 811 |
| 8 | ENY | 784 |
| 9 | Vueling | 616 |
| 10 | AXM | 615 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 558 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 529 |
| 15 | AZU | 517 |
| 16 | QLK | 500 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 439 |
| 20 | easyJet | 411 |
| 21 | AEE | 410 |
| 22 | EJU | 403 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 385 |
| 25 | Japan Airlines | 370 |
| 26 | Air France | 364 |
| 27 | AXB | 351 |
| 28 | AIQ | 323 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50506 |
| 2 | 🇮🇳 IN | 4567 |
| 3 | 🇪🇸 ES | 4563 |
| 4 | 🇦🇺 AU | 4327 |
| 5 | 🇧🇷 BR | 3593 |
| 6 | 🇩🇪 DE | 3510 |
| 7 | 🇯🇵 JP | 3454 |
| 8 | 🇮🇹 IT | 3432 |
| 9 | 🇨🇦 CA | 3132 |
| 10 | 🇬🇧 GB | 2691 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2480 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1880 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1508 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1146 |
| 21 | 🇹🇷 TR | 1112 |
| 22 | 🇵🇭 PH | 1073 |
| 23 | 🇵🇱 PL | 1022 |
| 24 | 🇰🇷 KR | 1022 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 774 |
| 27 | 🇲🇴 MO | 713 |
| 28 | 🇲🇪 ME | 685 |
| 29 | 🇳🇱 NL | 661 |
| 30 | 🇮🇩 ID | 537 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1167 |
| 3 | Denver International Airport |  | US | 1046 |
| 4 | Indira Gandhi International Airport |  | IN | 961 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 917 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 811 |
| 9 | Harry Reid International Airport |  | US | 806 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 713 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 625 |
| 14 | Chicago O'Hare International Airport |  | US | 606 |
| 15 | Kuala Lumpur International Airport |  | MY | 599 |
| 16 | Madrid Barajas International Airport |  | ES | 595 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 561 |
| 19 | Bengaluru International Airport |  | IN | 552 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 502 |
| 24 | Charles de Gaulle International Airport |  | FR | 489 |
| 25 | Ninoy Aquino International Airport |  | PH | 488 |
| 26 | Tenerife Norte Airport |  | ES | 488 |
| 27 | Daniel K Inouye International Airport |  | US | 472 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 461 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 32 | Barcelona International Airport |  | ES | 425 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 414 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 37 | Don Mueang International Airport |  | TH | 395 |
| 38 | Reno/Tahoe International Airport |  | US | 394 |
| 39 | Amsterdam Airport Schiphol |  | NL | 392 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 257 | 1h 7m | 706 km | 3,129.0 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 216 | 21m | 244 km | 909.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 198 | 24m | 225 km | 768.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 187 | 1h 27m | 910 km | 2,934.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 181 | 28m | 304 km | 948.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 148 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 135 | 1h 12m | 770 km | 1,793.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 117 | 44m | 452 km | 911.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 96 | 20m | 147 km | 242.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 85 | 14m | 154 km | 225.2 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CATS09 | CAT | Kadena Air Base (RODN) | A 511 Airport (RKSG) | 2026-05-02 03:00 UTC | 2026-05-02 05:35 UTC | 2h 34m |
| BBC371 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-05-02 04:17 UTC | 2026-05-02 05:25 UTC | 1h 7m |
| QTR8472 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-01 22:23 UTC | 2026-05-02 05:21 UTC | 6h 57m |
| EW585SL |  | Borovaya Airfield (UMMB) | Borovaya Airfield (UMMB) | 2026-05-02 05:08 UTC | 2026-05-02 05:13 UTC | 5m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-02 00:52 UTC | 2026-05-02 05:12 UTC | 4h 20m |
| ZKHUP | ZKH | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-05-02 05:00 UTC | 2026-05-02 05:10 UTC | 9m |
| SEH1AM | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-05-02 04:38 UTC | 2026-05-02 05:02 UTC | 24m |
| CCA964 | Air China | Brussels Airport (EBBR) | Macau International Airport (VMMC) | 2026-05-01 11:04 UTC | 2026-05-02 04:53 UTC | 17h 49m |
| FIN8PN | Finnair | Helsinki Vantaa Airport (EFHK) | Ranua Airport (EFRU) | 2026-05-02 04:03 UTC | 2026-05-02 04:53 UTC | 49m |
| N808ET |  | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-05-02 03:40 UTC | 2026-05-02 04:46 UTC | 1h 6m |
| SKW5195 | SkyWest Airlines | Denver International Airport (KDEN) | Chapman Field (CD10) | 2026-05-02 04:16 UTC | 2026-05-02 04:41 UTC | 25m |
| JST884 | JST | Melbourne International Airport (YMML) | Hervey Bay Airport (YHBA) | 2026-05-02 02:46 UTC | 2026-05-02 04:39 UTC | 1h 52m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-02 03:45 UTC | 2026-05-02 04:36 UTC | 50m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-05-02 04:12 UTC | 2026-05-02 04:30 UTC | 17m |
| DAL1299 | Delta Air Lines | George Bush Intcntl/Houston Airport (KIAH) | Salt Lake City International Airport (KSLC) | 2026-05-02 01:41 UTC | 2026-05-02 04:28 UTC | 2h 46m |
| RQM | RQM | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-02 03:49 UTC | 2026-05-02 04:26 UTC | 36m |
| JST293 | JST | Auckland International Airport (NZAA) | Wanaka Airport (NZWF) | 2026-05-02 03:02 UTC | 2026-05-02 04:23 UTC | 1h 21m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-05-02 02:38 UTC | 2026-05-02 04:21 UTC | 1h 43m |
| ANZ623 | ANZ | Auckland International Airport (NZAA) | Wanaka Airport (NZWF) | 2026-05-02 02:53 UTC | 2026-05-02 04:20 UTC | 1h 26m |
| IGO531P | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Yongphulla Airport (VQ10) | 2026-05-02 03:38 UTC | 2026-05-02 04:18 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
