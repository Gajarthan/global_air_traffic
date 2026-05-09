# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_11:20:39_UTC-green)

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

**Latest saved flight:** 2026-05-09 11:20:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 11:20:39 UTC

- **75,171** saved flights
- **27,704** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,171** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **926,987.9 tonnes** estimated CO2 emissions
- **53,738,427 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3218 |
| 2 | SkyWest Airlines | 2787 |
| 3 | IndiGo | 1689 |
| 4 | EJA | 1387 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1089 |
| 7 | Lufthansa | 971 |
| 8 | ENY | 937 |
| 9 | Vueling | 727 |
| 10 | AXM | 709 |
| 11 | Delta Air Lines | 705 |
| 12 | LATAM Airlines | 694 |
| 13 | WIF | 653 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 603 |
| 16 | QLK | 579 |
| 17 | Swiss International | 574 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 498 |
| 21 | EJU | 482 |
| 22 | AEE | 481 |
| 23 | Cathay Pacific | 474 |
| 24 | VIV | 454 |
| 25 | Japan Airlines | 443 |
| 26 | Air France | 436 |
| 27 | AXB | 417 |
| 28 | CXK | 384 |
| 29 | AIQ | 376 |
| 30 | MXY | 363 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60449 |
| 2 | 🇪🇸 ES | 5396 |
| 3 | 🇮🇳 IN | 5297 |
| 4 | 🇦🇺 AU | 4952 |
| 5 | 🇩🇪 DE | 4221 |
| 6 | 🇧🇷 BR | 4204 |
| 7 | 🇮🇹 IT | 4102 |
| 8 | 🇯🇵 JP | 3959 |
| 9 | 🇨🇦 CA | 3744 |
| 10 | 🇬🇧 GB | 3230 |
| 11 | 🇫🇷 FR | 2977 |
| 12 | 🇨🇴 CO | 2691 |
| 13 | 🇲🇽 MX | 2326 |
| 14 | 🇬🇷 GR | 2213 |
| 15 | 🇳🇴 NO | 2091 |
| 16 | 🇨🇭 CH | 2042 |
| 17 | 🇲🇾 MY | 1766 |
| 18 | 🇿🇦 ZA | 1461 |
| 19 | 🇳🇿 NZ | 1364 |
| 20 | 🇹🇷 TR | 1340 |
| 21 | 🇹🇭 TH | 1338 |
| 22 | 🇵🇱 PL | 1255 |
| 23 | 🇵🇭 PH | 1214 |
| 24 | 🇬🇹 GT | 1184 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 888 |
| 27 | 🇲🇴 MO | 870 |
| 28 | 🇲🇪 ME | 803 |
| 29 | 🇳🇱 NL | 779 |
| 30 | 🇭🇷 HR | 632 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1329 |
| 3 | Denver International Airport |  | US | 1258 |
| 4 | Indira Gandhi International Airport |  | IN | 1113 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1085 |
| 6 | Frankfurt am Main International Airport |  | DE | 973 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | La Aurora Airport |  | GT | 888 |
| 9 | Zurich Airport |  | CH | 888 |
| 10 | Guaymaral Airport |  | CO | 885 |
| 11 | El Dorado International Airport |  | CO | 879 |
| 12 | Macau International Airport |  | MO | 870 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 729 |
| 15 | Kuala Lumpur International Airport |  | MY | 709 |
| 16 | Madrid Barajas International Airport |  | ES | 701 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 664 |
| 18 | Bengaluru International Airport |  | IN | 655 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 650 |
| 20 | Malpensa International Airport |  | IT | 645 |
| 21 | Salt Lake City International Airport |  | US | 617 |
| 22 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 597 |
| 23 | Congonhas Airport |  | BR | 596 |
| 24 | Charlotte/Douglas International Airport |  | US | 590 |
| 25 | Charles de Gaulle International Airport |  | FR | 584 |
| 26 | Capua Airport |  | IT | 579 |
| 27 | Tenerife Norte Airport |  | ES | 562 |
| 28 | Ninoy Aquino International Airport |  | PH | 550 |
| 29 | Daniel K Inouye International Airport |  | US | 549 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 539 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 518 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 503 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 500 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Don Mueang International Airport |  | TH | 473 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 471 |
| 38 | Amsterdam Airport Schiphol |  | NL | 470 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 266 | 21m | 244 km | 1,120.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 181 | 19m | 165 km | 514.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 177 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 137 | 21m | 99 km | 234.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 113 | 27m | 215 km | 418.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 112 | 20m | 147 km | 283.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 102 | 1h 2m | 695 km | 1,222.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 100 | 58m | 493 km | 850.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N678PP |  | UT99 (UT99) | Provo Municipal Airport (KPVU) | 2026-05-09 11:05 UTC | 2026-05-09 11:20 UTC | 15m |
| HKC6652 | HKC | VGZR (VGZR) | Zhuhai Airport (ZGSD) | 2026-05-09 08:31 UTC | 2026-05-09 11:16 UTC | 2h 44m |
| HB1673 |  | Winterthur Airport (LSPH) | Winterthur Airport (LSPH) | 2026-05-09 10:37 UTC | 2026-05-09 10:57 UTC | 19m |
| SWA1523 | Southwest Airlines | Gerald R Ford International Airport (KGRR) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-05-09 09:37 UTC | 2026-05-09 10:52 UTC | 1h 14m |
| DEBFT | DEB | Gunzburg-Donauried Airport (EDMG) | Mengen-Hohentengen Airport (EDTM) | 2026-05-09 09:47 UTC | 2026-05-09 10:50 UTC | 1h 3m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 10:33 UTC | 2026-05-09 10:50 UTC | 16m |
| LSI143 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-08 23:43 UTC | 2026-05-09 10:47 UTC | 11h 4m |
|  |  | Zell Am See Airport (LOWZ) | Zell Am See Airport (LOWZ) | 2026-05-09 10:28 UTC | 2026-05-09 10:41 UTC | 13m |
| YV221T |  | General Manuel Carlos Piar International Airport (SVPR) | Bocon Airport (SVBN) | 2026-05-09 10:12 UTC | 2026-05-09 10:38 UTC | 26m |
| EZY18FP | easyJet | Berlin Brandenburg Airport (EDDB) | London Gatwick Airport (EGKK) | 2026-05-09 09:03 UTC | 2026-05-09 10:36 UTC | 1h 32m |
| IGO6413 | IndiGo | Agartala Airport (VEAT) | Shillong Airport (VEBI) | 2026-05-09 10:13 UTC | 2026-05-09 10:29 UTC | 15m |
| AEA18QC | AEA | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-05-09 09:35 UTC | 2026-05-09 10:28 UTC | 52m |
| SAS2301 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Vinnu Airport (ENSU) | 2026-05-09 09:52 UTC | 2026-05-09 10:24 UTC | 31m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-05-09 09:00 UTC | 2026-05-09 10:22 UTC | 1h 21m |
| BEL5KF | Brussels Airlines | Brussels Airport (EBBR) | Faro Airport (LPFR) | 2026-05-09 07:39 UTC | 2026-05-09 10:22 UTC | 2h 42m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-08 19:56 UTC | 2026-05-09 10:21 UTC | 14h 24m |
| DLH6RK | Lufthansa | Frankfurt am Main International Airport (EDDF) | Napoli / Capodichino International Airport (LIRN) | 2026-05-09 08:51 UTC | 2026-05-09 10:19 UTC | 1h 27m |
| N500FE |  | Flying Cloud Airport (KFCM) | Philip Airport (KPHP) | 2026-05-09 08:26 UTC | 2026-05-09 10:16 UTC | 1h 49m |
| RYR4749 | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Palermo / Bocca Di Falco Airport (LICP) | 2026-05-09 08:45 UTC | 2026-05-09 10:16 UTC | 1h 31m |
| AXB2819 | AXB | Bengaluru International Airport (VOBL) | VEVZ (VEVZ) | 2026-05-09 07:32 UTC | 2026-05-09 10:15 UTC | 2h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
