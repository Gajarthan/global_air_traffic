# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_11:10:24_UTC-green)

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

**Latest saved flight:** 2026-05-12 11:10:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 11:10:24 UTC

- **78,735** saved flights
- **28,673** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,735** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **974,662.9 tonnes** estimated CO2 emissions
- **56,502,200 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3398 |
| 2 | SkyWest Airlines | 2924 |
| 3 | IndiGo | 1746 |
| 4 | EJA | 1450 |
| 5 | American Airlines | 1226 |
| 6 | Southwest Airlines | 1154 |
| 7 | Lufthansa | 1043 |
| 8 | ENY | 980 |
| 9 | Delta Air Lines | 858 |
| 10 | Vueling | 759 |
| 11 | AXM | 728 |
| 12 | LATAM Airlines | 715 |
| 13 | WIF | 680 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 622 |
| 16 | Swiss International | 607 |
| 17 | QLK | 592 |
| 18 | LXJ | 571 |
| 19 | Alaska Airlines | 553 |
| 20 | easyJet | 526 |
| 21 | EJU | 512 |
| 22 | AEE | 510 |
| 23 | Cathay Pacific | 501 |
| 24 | Air France | 467 |
| 25 | VIV | 467 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 437 |
| 28 | CXK | 403 |
| 29 | AIQ | 394 |
| 30 | MXY | 394 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63619 |
| 2 | 🇪🇸 ES | 5655 |
| 3 | 🇮🇳 IN | 5476 |
| 4 | 🇦🇺 AU | 5087 |
| 5 | 🇩🇪 DE | 4483 |
| 6 | 🇮🇹 IT | 4385 |
| 7 | 🇧🇷 BR | 4351 |
| 8 | 🇯🇵 JP | 4072 |
| 9 | 🇨🇦 CA | 3892 |
| 10 | 🇬🇧 GB | 3390 |
| 11 | 🇫🇷 FR | 3137 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2388 |
| 14 | 🇬🇷 GR | 2318 |
| 15 | 🇳🇴 NO | 2168 |
| 16 | 🇨🇭 CH | 2121 |
| 17 | 🇲🇾 MY | 1826 |
| 18 | 🇿🇦 ZA | 1498 |
| 19 | 🇹🇷 TR | 1425 |
| 20 | 🇳🇿 NZ | 1402 |
| 21 | 🇹🇭 TH | 1401 |
| 22 | 🇵🇱 PL | 1317 |
| 23 | 🇵🇭 PH | 1258 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 927 |
| 27 | 🇲🇴 MO | 919 |
| 28 | 🇲🇪 ME | 847 |
| 29 | 🇳🇱 NL | 822 |
| 30 | 🇭🇷 HR | 685 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1731 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1316 |
| 4 | Indira Gandhi International Airport |  | IN | 1157 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1137 |
| 6 | Frankfurt am Main International Airport |  | DE | 1045 |
| 7 | Harry Reid International Airport |  | US | 975 |
| 8 | Zurich Airport |  | CH | 934 |
| 9 | Macau International Airport |  | MO | 919 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 872 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 797 |
| 15 | Chicago O'Hare International Airport |  | US | 765 |
| 16 | Madrid Barajas International Airport |  | ES | 730 |
| 17 | Kuala Lumpur International Airport |  | MY | 729 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 696 |
| 19 | Malpensa International Airport |  | IT | 682 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 21 | Bengaluru International Airport |  | IN | 675 |
| 22 | Salt Lake City International Airport |  | US | 644 |
| 23 | Capua Airport |  | IT | 639 |
| 24 | Charlotte/Douglas International Airport |  | US | 621 |
| 25 | Charles de Gaulle International Airport |  | FR | 620 |
| 26 | Congonhas Airport |  | BR | 615 |
| 27 | Tenerife Norte Airport |  | ES | 588 |
| 28 | Ninoy Aquino International Airport |  | PH | 573 |
| 29 | Daniel K Inouye International Airport |  | US | 571 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 563 |
| 31 | Barcelona International Airport |  | ES | 532 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 531 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 518 |
| 35 | Vitoria/Foronda Airport |  | ES | 502 |
| 36 | Don Mueang International Airport |  | TH | 501 |
| 37 | Amsterdam Airport Schiphol |  | NL | 496 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 486 |
| 39 | O. R. Tambo International Airport |  | ZA | 473 |
| 40 | Calgary International Airport |  | CA | 464 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 283 | 21m | 244 km | 1,191.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 189 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 104 | 57m | 493 km | 884.8 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 103 | 23m | 55 km | 97.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 99 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 99 | 18m | 144 km | 246.3 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-05-12 10:58 UTC | 2026-05-12 11:10 UTC | 11m |
| ANA266 | All Nippon Airways | Fukuoka Airport (RJFF) | Tokyo International Airport (RJTT) | 2026-05-12 09:46 UTC | 2026-05-12 11:06 UTC | 1h 19m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-11 20:20 UTC | 2026-05-12 11:05 UTC | 14h 45m |
| N656W |  | Holmes County Airport (K10G) | Indiana County/Jimmy Stewart Field (KIDI) | 2026-05-12 10:28 UTC | 2026-05-12 11:04 UTC | 35m |
| FKH8062 | FKH | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-11 08:25 UTC | 2026-05-12 11:02 UTC | 26h 36m |
| EXS1 | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-05-12 09:55 UTC | 2026-05-12 10:53 UTC | 58m |
| RYR877 | Ryanair | Torino / Caselle International Airport (LIMF) | Crotone Airport (LIBC) | 2026-05-12 09:26 UTC | 2026-05-12 10:53 UTC | 1h 26m |
| AGUST51 | AGU | Vergiate Airport (LILG) | Varese / Venegono Airport (LILN) | 2026-05-12 10:01 UTC | 2026-05-12 10:52 UTC | 50m |
| SVA982 | Saudia | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-05-11 17:41 UTC | 2026-05-12 10:50 UTC | 17h 8m |
| GRZLY12 | GRZ | Liege Airport (EBLG) | Beauvechain Air Base (EBBE) | 2026-05-12 09:35 UTC | 2026-05-12 10:44 UTC | 1h 9m |
| GRZLY11 | GRZ | Liege Airport (EBLG) | Beauvechain Air Base (EBBE) | 2026-05-12 09:33 UTC | 2026-05-12 10:44 UTC | 1h 11m |
| JUST | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-05-12 08:57 UTC | 2026-05-12 10:42 UTC | 1h 44m |
| AEA1903 | AEA | Madrid Barajas International Airport (LEMD) | Logrono-Agoncillo Airport (LELO) | 2026-05-12 10:15 UTC | 2026-05-12 10:40 UTC | 24m |
| CXK506 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-12 10:33 UTC | 2026-05-12 10:39 UTC | 5m |
| DHTAF | DHT | Frankfurt-Egelsbach Airport (EDFE) | Frankfurt-Egelsbach Airport (EDFE) | 2026-05-12 09:24 UTC | 2026-05-12 10:36 UTC | 1h 12m |
| MFX7626 | MFX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-05-11 18:16 UTC | 2026-05-12 10:33 UTC | 16h 17m |
| CXH | CXH | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-12 09:57 UTC | 2026-05-12 10:32 UTC | 34m |
| BUDDY51 | BUD | Pardubice Airport (LKPD) | Kbely Air Base (LKKB) | 2026-05-12 10:03 UTC | 2026-05-12 10:27 UTC | 24m |
| RYR86JB | Ryanair | Vienna International Airport (LOWW) | Sigonella Airport (LICZ) | 2026-05-12 08:38 UTC | 2026-05-12 10:22 UTC | 1h 44m |
| KEM980 | KEM | O. R. Tambo International Airport (FAOR) | Lydenburg Airport (FALL) | 2026-05-12 09:53 UTC | 2026-05-12 10:17 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
