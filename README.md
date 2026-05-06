# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_06:17:25_UTC-green)

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

**Latest saved flight:** 2026-05-06 06:17:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 06:17:25 UTC

- **70,220** saved flights
- **26,182** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,220** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **865,388.6 tonnes** estimated CO2 emissions
- **50,167,456 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3009 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1605 |
| 4 | EJA | 1282 |
| 5 | American Airlines | 1096 |
| 6 | Southwest Airlines | 1018 |
| 7 | Lufthansa | 900 |
| 8 | ENY | 876 |
| 9 | Vueling | 691 |
| 10 | AXM | 674 |
| 11 | LATAM Airlines | 656 |
| 12 | WIF | 597 |
| 13 | Delta Air Lines | 594 |
| 14 | All Nippon Airways | 589 |
| 15 | AZU | 570 |
| 16 | QLK | 545 |
| 17 | Swiss International | 540 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 493 |
| 20 | easyJet | 468 |
| 21 | AEE | 453 |
| 22 | EJU | 453 |
| 23 | VIV | 441 |
| 24 | Cathay Pacific | 430 |
| 25 | Japan Airlines | 416 |
| 26 | Air France | 411 |
| 27 | AXB | 391 |
| 28 | AIQ | 357 |
| 29 | CXK | 349 |
| 30 | GLO | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55878 |
| 2 | 🇪🇸 ES | 5107 |
| 3 | 🇮🇳 IN | 5055 |
| 4 | 🇦🇺 AU | 4690 |
| 5 | 🇧🇷 BR | 3957 |
| 6 | 🇩🇪 DE | 3904 |
| 7 | 🇮🇹 IT | 3837 |
| 8 | 🇯🇵 JP | 3752 |
| 9 | 🇨🇦 CA | 3471 |
| 10 | 🇬🇧 GB | 3039 |
| 11 | 🇫🇷 FR | 2769 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2228 |
| 14 | 🇬🇷 GR | 2091 |
| 15 | 🇨🇭 CH | 1925 |
| 16 | 🇳🇴 NO | 1914 |
| 17 | 🇲🇾 MY | 1680 |
| 18 | 🇿🇦 ZA | 1392 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1275 |
| 21 | 🇹🇷 TR | 1261 |
| 22 | 🇵🇭 PH | 1164 |
| 23 | 🇵🇱 PL | 1151 |
| 24 | 🇬🇹 GT | 1129 |
| 25 | 🇰🇷 KR | 1120 |
| 26 | 🇲🇦 MA | 843 |
| 27 | 🇲🇴 MO | 811 |
| 28 | 🇲🇪 ME | 756 |
| 29 | 🇳🇱 NL | 729 |
| 30 | 🇮🇩 ID | 592 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1570 |
| 2 | Tokyo International Airport |  | JP | 1266 |
| 3 | Denver International Airport |  | US | 1167 |
| 4 | Indira Gandhi International Airport |  | IN | 1062 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1024 |
| 6 | Frankfurt am Main International Airport |  | DE | 897 |
| 7 | Harry Reid International Airport |  | US | 879 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 839 |
| 11 | Zurich Airport |  | CH | 828 |
| 12 | Macau International Airport |  | MO | 811 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 703 |
| 14 | Chicago O'Hare International Airport |  | US | 675 |
| 15 | Kuala Lumpur International Airport |  | MY | 673 |
| 16 | Madrid Barajas International Airport |  | ES | 667 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 19 | Malpensa International Airport |  | IT | 610 |
| 20 | Bengaluru International Airport |  | IN | 608 |
| 21 | Salt Lake City International Airport |  | US | 569 |
| 22 | Congonhas Airport |  | BR | 562 |
| 23 | Charlotte/Douglas International Airport |  | US | 555 |
| 24 | Charles de Gaulle International Airport |  | FR | 550 |
| 25 | Capua Airport |  | IT | 545 |
| 26 | Tenerife Norte Airport |  | ES | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 529 |
| 28 | Daniel K Inouye International Airport |  | US | 515 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 513 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 495 |
| 31 | Barcelona International Airport |  | ES | 487 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 477 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 450 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 443 |
| 37 | O. R. Tambo International Airport |  | ZA | 438 |
| 38 | Amsterdam Airport Schiphol |  | NL | 431 |
| 39 | Reno/Tahoe International Airport |  | US | 416 |
| 40 | Calgary International Airport |  | CA | 416 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 244 | 21m | 244 km | 1,027.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 197 | 28m | 304 km | 1,032.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 196 | 1h 27m | 910 km | 3,075.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 175 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 173 | 20m | 165 km | 492.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 171 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 130 | 44m | 452 km | 1,013.2 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 100 | 14m | 154 km | 265.0 t |
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
| C6524 |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Daniel K Inouye International Airport (PHNL) | 2026-05-06 05:56 UTC | 2026-05-06 06:17 UTC | 21m |
| ASA549 | Alaska Airlines | Dallas-Fort Worth International Airport (KDFW) | Boeing Field/King County International Airport (KBFI) | 2026-05-06 02:06 UTC | 2026-05-06 06:08 UTC | 4h 1m |
| JUST11 | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-05-06 05:16 UTC | 2026-05-06 06:07 UTC | 51m |
| ETH644 | Ethiopian Airlines | Cape Town International Airport (FACT) | Zhuhai Airport (ZGSD) | 2026-05-05 12:25 UTC | 2026-05-06 06:06 UTC | 17h 40m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-06 01:38 UTC | 2026-05-06 06:00 UTC | 4h 21m |
| LGL691M | LGL | Luxembourg-Findel International Airport (ELLX) | Malpensa International Airport (LIMC) | 2026-05-06 04:24 UTC | 2026-05-06 05:41 UTC | 1h 16m |
| DLH1MM | Lufthansa | Frankfurt am Main International Airport (EDDF) | Stuttgart Airport (EDDS) | 2026-05-06 05:13 UTC | 2026-05-06 05:38 UTC | 25m |
| AWA443 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-05-06 05:00 UTC | 2026-05-06 05:32 UTC | 32m |
| VLG1DP | Vueling | Barcelona International Airport (LEBL) | Pamplona Airport (LEPP) | 2026-05-06 04:48 UTC | 2026-05-06 05:27 UTC | 39m |
| TNU080 | TNU | Yalgoo Airport (YYAL) | Perth International Airport (YPPH) | 2026-05-06 04:45 UTC | 2026-05-06 05:27 UTC | 41m |
| RYR421P | Ryanair | Madrid Barajas International Airport (LEMD) | Francisco de Sá Carneiro Airport (LPPR) | 2026-05-06 04:36 UTC | 2026-05-06 05:24 UTC | 47m |
| N912MN |  | Joe Foss Field (KFSD) | Winner Regional Airport (KICR) | 2026-05-06 04:40 UTC | 2026-05-06 05:21 UTC | 40m |
| SEH6SF | SEH | Eleftherios Venizelos International Airport (LGAV) | Ihtiman Airport (LBHT) | 2026-05-06 04:08 UTC | 2026-05-06 05:19 UTC | 1h 11m |
| AEE105 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-06 04:39 UTC | 2026-05-06 05:18 UTC | 38m |
| SHIELD | SHI | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-06 04:28 UTC | 2026-05-06 05:16 UTC | 48m |
| KLM70B | KLM Royal Dutch | Václav Havel Airport (LKPR) | Amsterdam Airport Schiphol (EHAM) | 2026-05-06 04:10 UTC | 2026-05-06 05:16 UTC | 1h 5m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-05-06 04:28 UTC | 2026-05-06 05:15 UTC | 47m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-06 04:43 UTC | 2026-05-06 05:14 UTC | 31m |
| AIQ3209 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-06 04:24 UTC | 2026-05-06 05:14 UTC | 50m |
| ITY1285 | ITY | Linate Airport (LIML) | Capua Airport (LIAU) | 2026-05-06 04:15 UTC | 2026-05-06 05:11 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
