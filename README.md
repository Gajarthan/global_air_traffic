# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_10:52:23_UTC-green)

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

**Latest saved flight:** 2026-05-02 10:52:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 10:52:23 UTC

- **63,895** saved flights
- **24,358** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,895** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **783,344.9 tonnes** estimated CO2 emissions
- **45,411,301 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2687 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1469 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 991 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 819 |
| 8 | ENY | 784 |
| 9 | Vueling | 629 |
| 10 | AXM | 622 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 564 |
| 13 | WIF | 536 |
| 14 | Delta Air Lines | 531 |
| 15 | AZU | 517 |
| 16 | QLK | 502 |
| 17 | Swiss International | 493 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 418 |
| 21 | AEE | 413 |
| 22 | EJU | 409 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 388 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 370 |
| 27 | AXB | 354 |
| 28 | AIQ | 328 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50531 |
| 2 | 🇪🇸 ES | 4640 |
| 3 | 🇮🇳 IN | 4633 |
| 4 | 🇦🇺 AU | 4339 |
| 5 | 🇧🇷 BR | 3594 |
| 6 | 🇩🇪 DE | 3560 |
| 7 | 🇯🇵 JP | 3506 |
| 8 | 🇮🇹 IT | 3468 |
| 9 | 🇨🇦 CA | 3137 |
| 10 | 🇬🇧 GB | 2733 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2520 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1906 |
| 15 | 🇨🇭 CH | 1781 |
| 16 | 🇳🇴 NO | 1752 |
| 17 | 🇲🇾 MY | 1524 |
| 18 | 🇿🇦 ZA | 1298 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1167 |
| 21 | 🇹🇷 TR | 1129 |
| 22 | 🇵🇭 PH | 1085 |
| 23 | 🇰🇷 KR | 1045 |
| 24 | 🇵🇱 PL | 1040 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 780 |
| 27 | 🇲🇴 MO | 723 |
| 28 | 🇲🇪 ME | 689 |
| 29 | 🇳🇱 NL | 669 |
| 30 | 🇮🇩 ID | 539 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1181 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 973 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 929 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 822 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 760 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 723 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Chicago O'Hare International Airport |  | US | 607 |
| 15 | Kuala Lumpur International Airport |  | MY | 603 |
| 16 | Madrid Barajas International Airport |  | ES | 602 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 560 |
| 20 | Malpensa International Airport |  | IT | 548 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 502 |
| 24 | Tenerife Norte Airport |  | ES | 502 |
| 25 | Charles de Gaulle International Airport |  | FR | 498 |
| 26 | Ninoy Aquino International Airport |  | PH | 493 |
| 27 | Daniel K Inouye International Airport |  | US | 473 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 469 |
| 29 | Capua Airport |  | IT | 468 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 432 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 422 |
| 34 | Vitoria/Foronda Airport |  | ES | 421 |
| 35 | O. R. Tambo International Airport |  | ZA | 411 |
| 36 | Don Mueang International Airport |  | TH | 403 |
| 37 | Amsterdam Airport Schiphol |  | NL | 398 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 217 | 21m | 244 km | 913.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 188 | 1h 27m | 910 km | 2,950.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 187 | 28m | 304 km | 980.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 142 | 26m | 275 km | 672.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 139 | 1h 11m | 770 km | 1,846.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 118 | 44m | 452 km | 919.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 108 | 31m | 369 km | 687.4 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 96 | 20m | 147 km | 242.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 88 | 57m | 493 km | 748.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 87 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SAMU38 | SAM | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-05-02 10:40 UTC | 2026-05-02 10:52 UTC | 12m |
| AZG9602 | AZG | Oslo Gardermoen Airport (ENGM) | Zhuhai Airport (ZGSD) | 2026-05-01 19:34 UTC | 2026-05-02 10:44 UTC | 15h 9m |
| DFPOL | DFP | Munster Osnabruck Airport (EDDG) | Dortmund Airport (EDLW) | 2026-05-02 10:06 UTC | 2026-05-02 10:40 UTC | 33m |
| BLVF | BLV | Shek Kong Air Base (VHSK) | Chek Lap Kok International Airport (VHHH) | 2026-05-02 10:28 UTC | 2026-05-02 10:36 UTC | 7m |
| LSI143 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-01 23:22 UTC | 2026-05-02 10:30 UTC | 11h 8m |
| IGO172 | IndiGo | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-02 08:18 UTC | 2026-05-02 10:25 UTC | 2h 7m |
| CCA115 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-05-02 07:38 UTC | 2026-05-02 10:25 UTC | 2h 46m |
| DKPET | DKP | Bad Worishofen-Nord Airport (EDNH) | Langkampfen Airport (LOIK) | 2026-05-02 08:37 UTC | 2026-05-02 10:25 UTC | 1h 47m |
| GGNHL | GGN | Dunkeswell Airport (EGTU) | Dunkeswell Airport (EGTU) | 2026-05-02 10:20 UTC | 2026-05-02 10:20 UTC | 0m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-01 20:05 UTC | 2026-05-02 10:20 UTC | 14h 15m |
| SPMOC | SPM | Nowy Targ Airport (EPNT) | Pobiednik Wielki Airport (EPKP) | 2026-05-02 09:08 UTC | 2026-05-02 10:20 UTC | 1h 11m |
| HB1777 |  | Gruyeres Airport (LSGT) | Saanen Airport (LSGK) | 2026-05-02 09:23 UTC | 2026-05-02 10:16 UTC | 53m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-05-02 09:15 UTC | 2026-05-02 10:11 UTC | 55m |
| CUCO322 | CUC | Armilla Airport (LEGA) | Armilla Airport (LEGA) | 2026-05-02 10:00 UTC | 2026-05-02 10:05 UTC | 4m |
| HAF701 | HAF | Syros Airport (LGSO) | Syros Airport (LGSO) | 2026-05-02 09:57 UTC | 2026-05-02 10:03 UTC | 6m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Reykholar Airport (BIRE) | 2026-05-02 09:40 UTC | 2026-05-02 10:02 UTC | 21m |
| CNF419S | CNF | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-05-02 09:52 UTC | 2026-05-02 10:02 UTC | 9m |
| AIQ3207 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-02 09:08 UTC | 2026-05-02 09:58 UTC | 50m |
| CHX87 | CHX | Dachau-Grobenried Airport (EDMD) | Hoefen Airport (LOIR) | 2026-05-02 09:30 UTC | 2026-05-02 09:58 UTC | 28m |
| RYR1963 | Ryanair | Memmingen Allgau Airport (EDJA) | Sepurine Training Base (LD57) | 2026-05-02 09:10 UTC | 2026-05-02 09:56 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
