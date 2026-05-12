# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_09:01:31_UTC-green)

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

**Latest saved flight:** 2026-05-12 09:01:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 09:01:31 UTC

- **78,602** saved flights
- **28,648** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,602** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **972,800.2 tonnes** estimated CO2 emissions
- **56,394,215 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3388 |
| 2 | SkyWest Airlines | 2924 |
| 3 | IndiGo | 1739 |
| 4 | EJA | 1450 |
| 5 | American Airlines | 1226 |
| 6 | Southwest Airlines | 1154 |
| 7 | Lufthansa | 1032 |
| 8 | ENY | 980 |
| 9 | Delta Air Lines | 858 |
| 10 | Vueling | 754 |
| 11 | AXM | 725 |
| 12 | LATAM Airlines | 714 |
| 13 | WIF | 678 |
| 14 | All Nippon Airways | 633 |
| 15 | AZU | 621 |
| 16 | Swiss International | 602 |
| 17 | QLK | 592 |
| 18 | LXJ | 571 |
| 19 | Alaska Airlines | 553 |
| 20 | easyJet | 526 |
| 21 | AEE | 510 |
| 22 | EJU | 510 |
| 23 | Cathay Pacific | 500 |
| 24 | VIV | 467 |
| 25 | Air France | 465 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 437 |
| 28 | CXK | 402 |
| 29 | MXY | 394 |
| 30 | AIQ | 391 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63609 |
| 2 | 🇪🇸 ES | 5633 |
| 3 | 🇮🇳 IN | 5459 |
| 4 | 🇦🇺 AU | 5079 |
| 5 | 🇩🇪 DE | 4460 |
| 6 | 🇮🇹 IT | 4363 |
| 7 | 🇧🇷 BR | 4347 |
| 8 | 🇯🇵 JP | 4056 |
| 9 | 🇨🇦 CA | 3887 |
| 10 | 🇬🇧 GB | 3378 |
| 11 | 🇫🇷 FR | 3119 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2388 |
| 14 | 🇬🇷 GR | 2318 |
| 15 | 🇳🇴 NO | 2159 |
| 16 | 🇨🇭 CH | 2117 |
| 17 | 🇲🇾 MY | 1818 |
| 18 | 🇿🇦 ZA | 1490 |
| 19 | 🇹🇷 TR | 1424 |
| 20 | 🇳🇿 NZ | 1402 |
| 21 | 🇹🇭 TH | 1396 |
| 22 | 🇵🇱 PL | 1310 |
| 23 | 🇵🇭 PH | 1254 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 927 |
| 27 | 🇲🇴 MO | 916 |
| 28 | 🇲🇪 ME | 844 |
| 29 | 🇳🇱 NL | 819 |
| 30 | 🇭🇷 HR | 682 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1731 |
| 2 | Tokyo International Airport |  | JP | 1365 |
| 3 | Denver International Airport |  | US | 1316 |
| 4 | Indira Gandhi International Airport |  | IN | 1154 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1137 |
| 6 | Frankfurt am Main International Airport |  | DE | 1036 |
| 7 | Harry Reid International Airport |  | US | 974 |
| 8 | Zurich Airport |  | CH | 930 |
| 9 | Macau International Airport |  | MO | 916 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 872 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 797 |
| 15 | Chicago O'Hare International Airport |  | US | 765 |
| 16 | Madrid Barajas International Airport |  | ES | 727 |
| 17 | Kuala Lumpur International Airport |  | MY | 727 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 696 |
| 19 | Malpensa International Airport |  | IT | 681 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 21 | Bengaluru International Airport |  | IN | 675 |
| 22 | Salt Lake City International Airport |  | US | 644 |
| 23 | Capua Airport |  | IT | 635 |
| 24 | Charlotte/Douglas International Airport |  | US | 621 |
| 25 | Charles de Gaulle International Airport |  | FR | 618 |
| 26 | Congonhas Airport |  | BR | 614 |
| 27 | Tenerife Norte Airport |  | ES | 586 |
| 28 | Daniel K Inouye International Airport |  | US | 571 |
| 29 | Ninoy Aquino International Airport |  | PH | 571 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 560 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 531 |
| 32 | Barcelona International Airport |  | ES | 531 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 527 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 515 |
| 35 | Vitoria/Foronda Airport |  | ES | 501 |
| 36 | Don Mueang International Airport |  | TH | 498 |
| 37 | Amsterdam Airport Schiphol |  | NL | 494 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 486 |
| 39 | O. R. Tambo International Airport |  | ZA | 469 |
| 40 | Calgary International Airport |  | CA | 464 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 283 | 21m | 244 km | 1,191.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 211 | 1h 27m | 910 km | 3,311.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 188 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 175 | 1h 12m | 770 km | 2,324.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 168 | 26m | 275 km | 796.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 112 | 14m | 154 km | 296.8 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 103 | 23m | 55 km | 97.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 99 | 12m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 99 | 18m | 144 km | 246.3 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-12 08:49 UTC | 2026-05-12 09:01 UTC | 11m |
| AFM01O | AFM | Valence-Chabeuil Airport (LFLU) | Mende-Brenoux Airport (LFNB) | 2026-05-12 08:14 UTC | 2026-05-12 08:57 UTC | 42m |
| YRCAA | YRC | Baneasa International Airport (LRBS) | Mihail Kogalniceanu International Airport (LRCK) | 2026-05-12 08:14 UTC | 2026-05-12 08:39 UTC | 25m |
| PGT4UY | PGT | Gaziemir Airport (LTBK) | Yalova Airport (LTBP) | 2026-05-12 08:09 UTC | 2026-05-12 08:38 UTC | 29m |
| XPP | XPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-05-12 08:21 UTC | 2026-05-12 08:38 UTC | 16m |
| ZAM34 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-12 07:57 UTC | 2026-05-12 08:38 UTC | 40m |
| JHH | JHH | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-05-12 08:12 UTC | 2026-05-12 08:34 UTC | 21m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Forsaeti Airport (BIFZ) | 2026-05-12 08:21 UTC | 2026-05-12 08:32 UTC | 11m |
| PGT72Q | PGT | Eleftherios Venizelos International Airport (LGAV) | Yalova Airport (LTBP) | 2026-05-12 07:50 UTC | 2026-05-12 08:32 UTC | 42m |
| WGTL10 | WGT | RAAF Base Amberley (YAMB) | RAAF Base Richmond (YSRI) | 2026-05-12 07:24 UTC | 2026-05-12 08:29 UTC | 1h 5m |
| FDX1426 | FDX | Frederick W Smith International Airport (KMEM) | Austin-Bergstrom International Airport (KAUS) | 2026-05-12 07:16 UTC | 2026-05-12 08:29 UTC | 1h 12m |
| ZAM38 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-05-12 08:23 UTC | 2026-05-12 08:27 UTC | 3m |
| JMA8621 | JMA | Naivasha Airport (HKNV) | Nairobi Wilson Airport (HKNW) | 2026-05-12 08:25 UTC | 2026-05-12 08:26 UTC | 1m |
| ATLAS20 | ATL | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-05-12 08:20 UTC | 2026-05-12 08:24 UTC | 3m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-05-12 07:05 UTC | 2026-05-12 08:21 UTC | 1h 16m |
| AAL2571 | American Airlines | Palm Springs International Airport (KPSP) | Columbus Municipal Airport (0NM0) | 2026-05-12 07:10 UTC | 2026-05-12 08:21 UTC | 1h 10m |
| PNC2597 | PNC | Jekabpils Airport (EVKA) | Birzai Airport (EYBI) | 2026-05-12 07:07 UTC | 2026-05-12 08:18 UTC | 1h 10m |
| ANA319 | All Nippon Airways | Tokyo International Airport (RJTT) | Toyama Airport (RJNT) | 2026-05-12 07:51 UTC | 2026-05-12 08:18 UTC | 26m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-12 07:16 UTC | 2026-05-12 08:17 UTC | 1h 0m |
| EWG1VH | EWG | Salzburg Airport (LOWS) | Hamburg Airport (EDDH) | 2026-05-12 07:08 UTC | 2026-05-12 08:16 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
