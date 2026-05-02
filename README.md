# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_09:54:21_UTC-green)

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

**Latest saved flight:** 2026-05-02 09:54:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 09:54:21 UTC

- **63,785** saved flights
- **24,335** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,785** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **780,936.7 tonnes** estimated CO2 emissions
- **45,271,693 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2681 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1461 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 991 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 817 |
| 8 | ENY | 784 |
| 9 | Vueling | 627 |
| 10 | AXM | 620 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 563 |
| 13 | WIF | 535 |
| 14 | Delta Air Lines | 531 |
| 15 | AZU | 517 |
| 16 | QLK | 502 |
| 17 | Swiss International | 488 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 416 |
| 21 | AEE | 411 |
| 22 | EJU | 409 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 386 |
| 25 | Japan Airlines | 376 |
| 26 | Air France | 368 |
| 27 | AXB | 353 |
| 28 | AIQ | 326 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50530 |
| 2 | 🇪🇸 ES | 4616 |
| 3 | 🇮🇳 IN | 4612 |
| 4 | 🇦🇺 AU | 4337 |
| 5 | 🇧🇷 BR | 3594 |
| 6 | 🇩🇪 DE | 3543 |
| 7 | 🇯🇵 JP | 3496 |
| 8 | 🇮🇹 IT | 3464 |
| 9 | 🇨🇦 CA | 3136 |
| 10 | 🇬🇧 GB | 2713 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2505 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1898 |
| 15 | 🇨🇭 CH | 1772 |
| 16 | 🇳🇴 NO | 1747 |
| 17 | 🇲🇾 MY | 1520 |
| 18 | 🇿🇦 ZA | 1294 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1162 |
| 21 | 🇹🇷 TR | 1124 |
| 22 | 🇵🇭 PH | 1083 |
| 23 | 🇰🇷 KR | 1041 |
| 24 | 🇵🇱 PL | 1034 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 778 |
| 27 | 🇲🇴 MO | 720 |
| 28 | 🇲🇪 ME | 688 |
| 29 | 🇳🇱 NL | 667 |
| 30 | 🇮🇩 ID | 539 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1179 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 968 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 926 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 820 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 755 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 720 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Chicago O'Hare International Airport |  | US | 607 |
| 15 | Kuala Lumpur International Airport |  | MY | 602 |
| 16 | Madrid Barajas International Airport |  | ES | 601 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 558 |
| 20 | Malpensa International Airport |  | IT | 546 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 502 |
| 24 | Charles de Gaulle International Airport |  | FR | 495 |
| 25 | Ninoy Aquino International Airport |  | PH | 492 |
| 26 | Tenerife Norte Airport |  | ES | 491 |
| 27 | Daniel K Inouye International Airport |  | US | 473 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 465 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 432 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 420 |
| 34 | Vitoria/Foronda Airport |  | ES | 419 |
| 35 | O. R. Tambo International Airport |  | ZA | 409 |
| 36 | Don Mueang International Airport |  | TH | 400 |
| 37 | Amsterdam Airport Schiphol |  | NL | 396 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 258 | 1h 7m | 706 km | 3,141.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 217 | 21m | 244 km | 913.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 188 | 1h 27m | 910 km | 2,950.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 186 | 28m | 304 km | 975.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 139 | 1h 11m | 770 km | 1,846.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 118 | 44m | 452 km | 919.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 107 | 31m | 369 km | 681.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 96 | 20m | 147 km | 242.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 87 | 57m | 493 km | 740.2 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 84 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEA42ZC | AEA | Madrid Barajas International Airport (LEMD) | Palma De Mallorca Airport (LEPA) | 2026-05-02 09:01 UTC | 2026-05-02 09:54 UTC | 52m |
| DMYIH | DMY | EDJG (EDJG) | EDJG (EDJG) | 2026-05-02 09:22 UTC | 2026-05-02 09:51 UTC | 29m |
| MEECLBM | MEE | Jayena Airport (LE84) | Jayena Airport (LE84) | 2026-05-02 09:16 UTC | 2026-05-02 09:42 UTC | 25m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-05-02 06:09 UTC | 2026-05-02 09:39 UTC | 3h 30m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-02 02:34 UTC | 2026-05-02 09:37 UTC | 7h 2m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-05-02 09:13 UTC | 2026-05-02 09:30 UTC | 17m |
| CRK398 | CRK | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-02 02:12 UTC | 2026-05-02 09:27 UTC | 7h 15m |
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-05-02 08:14 UTC | 2026-05-02 09:24 UTC | 1h 9m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-02 09:11 UTC | 2026-05-02 09:18 UTC | 7m |
| RYR27BA | Ryanair | London Stansted Airport (EGSS) | Mauterndorf Airport (LOSM) | 2026-05-02 07:34 UTC | 2026-05-02 09:14 UTC | 1h 40m |
| 4XHSF |  | LL59 (LL59) | LL59 (LL59) | 2026-05-02 09:13 UTC | 2026-05-02 09:13 UTC | 0m |
| WIF3T | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-05-02 09:00 UTC | 2026-05-02 09:12 UTC | 12m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-02 07:10 UTC | 2026-05-02 09:11 UTC | 2h 1m |
| HLC276 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-05-02 09:02 UTC | 2026-05-02 09:11 UTC | 8m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-05-01 22:04 UTC | 2026-05-02 09:08 UTC | 11h 4m |
| CTK08 | CTK | East Midlands Airport (EGNX) | RAF Ternhill (EGOE) | 2026-05-02 08:49 UTC | 2026-05-02 09:07 UTC | 18m |
| RYR4957 | Ryanair | Valencia Airport (LEVC) | Ifrane Airport (GMFI) | 2026-05-02 07:58 UTC | 2026-05-02 09:06 UTC | 1h 7m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-05-02 08:47 UTC | 2026-05-02 09:01 UTC | 13m |
| RYR1133 | Ryanair | Sigonella Airport (LICZ) | Malpensa International Airport (LIMC) | 2026-05-02 07:30 UTC | 2026-05-02 09:00 UTC | 1h 30m |
| N54DD |  | Riverside Airport (KRAL) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-02 08:02 UTC | 2026-05-02 09:00 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
