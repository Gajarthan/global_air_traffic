# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_03:45:37_UTC-green)

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

**Latest saved flight:** 2026-05-04 03:45:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 03:45:37 UTC

- **67,109** saved flights
- **25,302** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,109** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **824,144.4 tonnes** estimated CO2 emissions
- **47,776,485 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2857 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1553 |
| 4 | EJA | 1202 |
| 5 | American Airlines | 1039 |
| 6 | Southwest Airlines | 946 |
| 7 | Lufthansa | 857 |
| 8 | ENY | 829 |
| 9 | Vueling | 661 |
| 10 | AXM | 652 |
| 11 | LATAM Airlines | 625 |
| 12 | All Nippon Airways | 576 |
| 13 | Delta Air Lines | 564 |
| 14 | WIF | 559 |
| 15 | AZU | 542 |
| 16 | QLK | 519 |
| 17 | Swiss International | 514 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 455 |
| 20 | easyJet | 444 |
| 21 | AEE | 437 |
| 22 | EJU | 432 |
| 23 | VIV | 419 |
| 24 | Cathay Pacific | 405 |
| 25 | Japan Airlines | 392 |
| 26 | Air France | 390 |
| 27 | AXB | 376 |
| 28 | CXK | 342 |
| 29 | AIQ | 340 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53155 |
| 2 | 🇪🇸 ES | 4910 |
| 3 | 🇮🇳 IN | 4882 |
| 4 | 🇦🇺 AU | 4450 |
| 5 | 🇧🇷 BR | 3768 |
| 6 | 🇩🇪 DE | 3742 |
| 7 | 🇮🇹 IT | 3656 |
| 8 | 🇯🇵 JP | 3615 |
| 9 | 🇨🇦 CA | 3294 |
| 10 | 🇬🇧 GB | 2892 |
| 11 | 🇫🇷 FR | 2654 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2137 |
| 14 | 🇬🇷 GR | 2001 |
| 15 | 🇨🇭 CH | 1869 |
| 16 | 🇳🇴 NO | 1816 |
| 17 | 🇲🇾 MY | 1614 |
| 18 | 🇿🇦 ZA | 1354 |
| 19 | 🇳🇿 NZ | 1254 |
| 20 | 🇹🇭 TH | 1217 |
| 21 | 🇹🇷 TR | 1206 |
| 22 | 🇵🇭 PH | 1120 |
| 23 | 🇵🇱 PL | 1099 |
| 24 | 🇬🇹 GT | 1091 |
| 25 | 🇰🇷 KR | 1080 |
| 26 | 🇲🇦 MA | 821 |
| 27 | 🇲🇴 MO | 757 |
| 28 | 🇲🇪 ME | 724 |
| 29 | 🇳🇱 NL | 708 |
| 30 | 🇮🇩 ID | 571 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1482 |
| 2 | Tokyo International Airport |  | JP | 1219 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1021 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 975 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 863 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 836 |
| 10 | La Aurora Airport |  | GT | 810 |
| 11 | Zurich Airport |  | CH | 793 |
| 12 | Macau International Airport |  | MO | 757 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 662 |
| 14 | Kuala Lumpur International Airport |  | MY | 646 |
| 15 | Chicago O'Hare International Airport |  | US | 642 |
| 16 | Madrid Barajas International Airport |  | ES | 640 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 596 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 586 |
| 20 | Malpensa International Airport |  | IT | 577 |
| 21 | Congonhas Airport |  | BR | 541 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 533 |
| 24 | Charlotte/Douglas International Airport |  | US | 529 |
| 25 | Charles de Gaulle International Airport |  | FR | 524 |
| 26 | Ninoy Aquino International Airport |  | PH | 509 |
| 27 | Capua Airport |  | IT | 505 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 491 |
| 29 | Daniel K Inouye International Airport |  | US | 488 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 473 |
| 31 | Barcelona International Airport |  | ES | 460 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 453 |
| 33 | Vitoria/Foronda Airport |  | ES | 445 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 444 |
| 35 | O. R. Tambo International Airport |  | ZA | 426 |
| 36 | Don Mueang International Airport |  | TH | 425 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 421 |
| 38 | Amsterdam Airport Schiphol |  | NL | 416 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 228 | 21m | 244 km | 960.0 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 204 | 24m | 225 km | 791.4 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 193 | 28m | 304 km | 1,011.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 193 | 1h 27m | 910 km | 3,028.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 168 | 20m | 165 km | 477.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 157 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 148 | 1h 12m | 770 km | 1,966.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 112 | 27m | 152 km | 292.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 111 | 31m | 369 km | 706.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 94 | 14m | 154 km | 249.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 2m | 695 km | 1,102.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 90 | 1h 43m | 1,423 km | 2,208.7 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MCA | MCA | Sunshine Coast Airport (YBMC) | Caloundra Airport (YCDR) | 2026-05-04 02:45 UTC | 2026-05-04 03:45 UTC | 1h 0m |
| IGO1151 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-05-04 02:21 UTC | 2026-05-04 03:41 UTC | 1h 20m |
| CES5015 | China Eastern | Singapore Changi International Airport (WSSS) | Macau International Airport (VMMC) | 2026-05-03 17:02 UTC | 2026-05-04 03:38 UTC | 10h 36m |
| ZJI | ZJI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-04 03:13 UTC | 2026-05-04 03:35 UTC | 21m |
| AIC8ES | Air India | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-05-04 01:27 UTC | 2026-05-04 03:25 UTC | 1h 57m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-04 03:12 UTC | 2026-05-04 03:24 UTC | 12m |
| ENY3804 | ENY | Dallas-Fort Worth International Airport (KDFW) | Grand Junction Regional Airport (KGJT) | 2026-05-04 01:34 UTC | 2026-05-04 03:23 UTC | 1h 48m |
| FD257 |  | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-05-04 02:25 UTC | 2026-05-04 03:06 UTC | 40m |
| AM341 |  | Melbourne Essendon Airport (YMEN) | Dadswells Bridge Airport (YCFF) | 2026-05-04 02:23 UTC | 2026-05-04 03:01 UTC | 38m |
| N617BG |  | Renton Municipal Airport (KRNT) | Thompson Falls Airport (KTHM) | 2026-05-04 01:46 UTC | 2026-05-04 03:01 UTC | 1h 14m |
| QLK623D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-05-04 02:22 UTC | 2026-05-04 02:59 UTC | 37m |
| N7660U |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-05-04 02:52 UTC | 2026-05-04 02:58 UTC | 5m |
| AIQ3201 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-04 02:05 UTC | 2026-05-04 02:54 UTC | 48m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-04 02:40 UTC | 2026-05-04 02:52 UTC | 11m |
| QLK223D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Adaminaby Airport (YADI) | 2026-05-04 02:15 UTC | 2026-05-04 02:52 UTC | 36m |
| JAL2823 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-05-04 01:55 UTC | 2026-05-04 02:47 UTC | 52m |
|  |  | Atlantic City International Airport (KACY) | Atlantic City International Airport (KACY) | 2026-05-04 02:35 UTC | 2026-05-04 02:45 UTC | 10m |
| APG711 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-05-04 02:17 UTC | 2026-05-04 02:45 UTC | 28m |
| ROLR23 | ROL | Mount Hotham Airport (YHOT) | Yarram Airport (YYRM) | 2026-05-04 02:31 UTC | 2026-05-04 02:43 UTC | 12m |
| NOK100 | NOK | Don Mueang International Airport (VTBD) | Chiang Rai Airport (VTCR) | 2026-05-04 01:53 UTC | 2026-05-04 02:43 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
