# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_13:07:36_UTC-green)

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

**Latest saved flight:** 2026-05-02 13:07:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 13:07:36 UTC

- **64,085** saved flights
- **24,405** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,085** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **785,957.6 tonnes** estimated CO2 emissions
- **45,562,758 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2704 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1477 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 992 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 823 |
| 8 | ENY | 784 |
| 9 | Vueling | 631 |
| 10 | AXM | 628 |
| 11 | LATAM Airlines | 597 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 531 |
| 15 | AZU | 518 |
| 16 | QLK | 502 |
| 17 | Swiss International | 494 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 420 |
| 21 | AEE | 416 |
| 22 | EJU | 410 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 389 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 372 |
| 27 | AXB | 358 |
| 28 | AIQ | 329 |
| 29 | CXK | 321 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50569 |
| 2 | 🇪🇸 ES | 4661 |
| 3 | 🇮🇳 IN | 4657 |
| 4 | 🇦🇺 AU | 4339 |
| 5 | 🇧🇷 BR | 3606 |
| 6 | 🇩🇪 DE | 3581 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3481 |
| 9 | 🇨🇦 CA | 3137 |
| 10 | 🇬🇧 GB | 2748 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2536 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1916 |
| 15 | 🇨🇭 CH | 1790 |
| 16 | 🇳🇴 NO | 1758 |
| 17 | 🇲🇾 MY | 1539 |
| 18 | 🇿🇦 ZA | 1316 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1176 |
| 21 | 🇹🇷 TR | 1139 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇰🇷 KR | 1056 |
| 24 | 🇵🇱 PL | 1045 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 786 |
| 27 | 🇲🇴 MO | 727 |
| 28 | 🇲🇪 ME | 694 |
| 29 | 🇳🇱 NL | 677 |
| 30 | 🇮🇩 ID | 544 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 979 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 933 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 826 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 762 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 727 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Kuala Lumpur International Airport |  | MY | 610 |
| 15 | Chicago O'Hare International Airport |  | US | 608 |
| 16 | Madrid Barajas International Airport |  | ES | 604 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 560 |
| 20 | Malpensa International Airport |  | IT | 551 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Tenerife Norte Airport |  | ES | 506 |
| 23 | Charlotte/Douglas International Airport |  | US | 502 |
| 24 | Salt Lake City International Airport |  | US | 502 |
| 25 | Charles de Gaulle International Airport |  | FR | 499 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 474 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 472 |
| 29 | Capua Airport |  | IT | 468 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 434 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 425 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 34 | Vitoria/Foronda Airport |  | ES | 422 |
| 35 | O. R. Tambo International Airport |  | ZA | 414 |
| 36 | Don Mueang International Airport |  | TH | 406 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 399 |
| 38 | Amsterdam Airport Schiphol |  | NL | 398 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 218 | 21m | 244 km | 917.9 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 158 | 20m | 165 km | 449.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 142 | 26m | 275 km | 672.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 88 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 83 | 1h 43m | 1,423 km | 2,037.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY6199 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-05-01 22:48 UTC | 2026-05-02 13:07 UTC | 14h 19m |
| PH1521 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-05-02 12:03 UTC | 2026-05-02 12:59 UTC | 55m |
| N476SP |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-05-02 12:57 UTC | 2026-05-02 12:59 UTC | 1m |
| ANA868 | All Nippon Airways | Gimpo International Airport (RKSS) | Tokyo International Airport (RJTT) | 2026-05-02 11:10 UTC | 2026-05-02 12:58 UTC | 1h 47m |
| PH957 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-05-02 12:33 UTC | 2026-05-02 12:55 UTC | 22m |
| HBZUZ | HBZ | Courchevel Airport (LFLJ) | Raron Airport (LSTA) | 2026-05-02 12:03 UTC | 2026-05-02 12:49 UTC | 45m |
| NWX580 | NWX | Aero Valley Airport (K52F) | Graham Municipal Airport (KRPH) | 2026-05-02 12:04 UTC | 2026-05-02 12:42 UTC | 38m |
| N11DT |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-05-02 12:24 UTC | 2026-05-02 12:37 UTC | 12m |
| FGXBJ | FGX | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | 2026-05-02 12:14 UTC | 2026-05-02 12:34 UTC | 20m |
| ERU810 | ERU | Daytona Beach International Airport (KDAB) | Arthur Dunn Air Park (KX21) | 2026-05-02 11:44 UTC | 2026-05-02 12:33 UTC | 49m |
| AIP1522 | AIP | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Kinsley Municipal Airport (K33K) | 2026-05-02 12:05 UTC | 2026-05-02 12:33 UTC | 28m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-05-02 12:13 UTC | 2026-05-02 12:33 UTC | 19m |
| SVA847 | Saudia | Suvarnabhumi Airport (VTBS) | Diu Airport (VA1P) | 2026-05-02 08:40 UTC | 2026-05-02 12:32 UTC | 3h 51m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-05-01 21:59 UTC | 2026-05-02 12:31 UTC | 14h 31m |
| N901KS |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-05-02 10:56 UTC | 2026-05-02 12:28 UTC | 1h 31m |
| DCDSO | DCD | Luxembourg-Findel International Airport (ELLX) | EDPR (EDPR) | 2026-05-02 11:28 UTC | 2026-05-02 12:24 UTC | 56m |
| AUA13D | Austrian Airlines | Vienna International Airport (LOWW) | Binningen Airport (EDSI) | 2026-05-02 11:15 UTC | 2026-05-02 12:23 UTC | 1h 8m |
| RYR57ME | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-05-02 11:19 UTC | 2026-05-02 12:21 UTC | 1h 2m |
| DLH6CN | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hettstadt Airport (EDGH) | 2026-05-02 11:51 UTC | 2026-05-02 12:20 UTC | 28m |
| 3AMTT |  | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-02 11:28 UTC | 2026-05-02 12:18 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
