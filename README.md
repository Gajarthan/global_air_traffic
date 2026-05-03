# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_08:57:42_UTC-green)

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

**Latest saved flight:** 2026-05-03 08:57:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 08:57:42 UTC

- **65,384** saved flights
- **24,792** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,384** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **802,013.0 tonnes** estimated CO2 emissions
- **46,493,507 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2779 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1514 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1011 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 838 |
| 8 | ENY | 806 |
| 9 | Vueling | 644 |
| 10 | AXM | 639 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 570 |
| 13 | Delta Air Lines | 546 |
| 14 | WIF | 539 |
| 15 | AZU | 526 |
| 16 | QLK | 510 |
| 17 | Swiss International | 503 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 433 |
| 21 | AEE | 423 |
| 22 | EJU | 419 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 392 |
| 25 | Japan Airlines | 386 |
| 26 | Air France | 380 |
| 27 | AXB | 366 |
| 28 | AIQ | 334 |
| 29 | CXK | 331 |
| 30 | GLO | 317 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51706 |
| 2 | 🇪🇸 ES | 4781 |
| 3 | 🇮🇳 IN | 4760 |
| 4 | 🇦🇺 AU | 4384 |
| 5 | 🇧🇷 BR | 3673 |
| 6 | 🇩🇪 DE | 3650 |
| 7 | 🇯🇵 JP | 3574 |
| 8 | 🇮🇹 IT | 3556 |
| 9 | 🇨🇦 CA | 3203 |
| 10 | 🇬🇧 GB | 2817 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2584 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1955 |
| 15 | 🇨🇭 CH | 1833 |
| 16 | 🇳🇴 NO | 1770 |
| 17 | 🇲🇾 MY | 1568 |
| 18 | 🇿🇦 ZA | 1326 |
| 19 | 🇳🇿 NZ | 1220 |
| 20 | 🇹🇭 TH | 1193 |
| 21 | 🇹🇷 TR | 1173 |
| 22 | 🇵🇭 PH | 1096 |
| 23 | 🇰🇷 KR | 1069 |
| 24 | 🇵🇱 PL | 1066 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 802 |
| 27 | 🇲🇴 MO | 737 |
| 28 | 🇲🇪 ME | 708 |
| 29 | 🇳🇱 NL | 688 |
| 30 | 🇮🇩 ID | 558 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1203 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 996 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 953 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 838 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 776 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 737 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Chicago O'Hare International Airport |  | US | 623 |
| 15 | Madrid Barajas International Airport |  | ES | 623 |
| 16 | Kuala Lumpur International Airport |  | MY | 623 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 583 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 570 |
| 20 | Malpensa International Airport |  | IT | 563 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 519 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 515 |
| 25 | Charles de Gaulle International Airport |  | FR | 509 |
| 26 | Ninoy Aquino International Airport |  | PH | 499 |
| 27 | Capua Airport |  | IT | 488 |
| 28 | Daniel K Inouye International Airport |  | US | 481 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 480 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 445 |
| 32 | Vitoria/Foronda Airport |  | ES | 438 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 435 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 434 |
| 35 | O. R. Tambo International Airport |  | ZA | 419 |
| 36 | Don Mueang International Airport |  | TH | 415 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 38 | Amsterdam Airport Schiphol |  | NL | 404 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 222 | 21m | 244 km | 934.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 202 | 24m | 225 km | 783.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 161 | 20m | 165 km | 458.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 153 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 145 | 1h 11m | 770 km | 1,926.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 120 | 44m | 452 km | 935.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 106 | 20m | 250 km | 457.9 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 91 | 57m | 493 km | 774.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 87 | 14m | 154 km | 230.5 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-05-02 21:43 UTC | 2026-05-03 08:57 UTC | 11h 14m |
| STM3466 | STM | Antalya International Airport (LTAI) | LRPV (LRPV) | 2026-05-03 07:37 UTC | 2026-05-03 08:53 UTC | 1h 16m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-03 07:07 UTC | 2026-05-03 08:52 UTC | 1h 45m |
| DRAG381 | DRA | Grenoble-Isere Airport (LFLS) | Grenoble Le Versoud Airport (LFLG) | 2026-05-03 08:40 UTC | 2026-05-03 08:51 UTC | 10m |
| GPX7961 | GPX | Helsinki Vantaa Airport (EFHK) | Yelgava Airport (EVEA) | 2026-05-03 08:14 UTC | 2026-05-03 08:49 UTC | 34m |
| CKS9164 | CKS | Ramstein Air Base (ETAR) | Macau International Airport (VMMC) | 2026-05-02 21:11 UTC | 2026-05-03 08:45 UTC | 11h 34m |
| VOE7XB | VOE | Alicante International Airport (LEAL) | Vitoria/Foronda Airport (LEVT) | 2026-05-03 07:53 UTC | 2026-05-03 08:43 UTC | 50m |
| HBZPV | HBZ | Wangen-Lachen Airport (LSPV) | Ambri Airport (LSPM) | 2026-05-03 08:23 UTC | 2026-05-03 08:43 UTC | 20m |
| OAL042 | OAL | Eleftherios Venizelos International Airport (LGAV) | Kithira Airport (LGKC) | 2026-05-03 08:14 UTC | 2026-05-03 08:41 UTC | 27m |
| AIC217 | Air India | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-05-03 07:29 UTC | 2026-05-03 08:37 UTC | 1h 7m |
| IGO236 | IndiGo | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-03 06:36 UTC | 2026-05-03 08:37 UTC | 2h 1m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-05-03 08:04 UTC | 2026-05-03 08:33 UTC | 29m |
| RYR8QH | Ryanair | London Stansted Airport (EGSS) | Celje Glider Airport (LJCL) | 2026-05-03 06:45 UTC | 2026-05-03 08:31 UTC | 1h 46m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-05-03 07:14 UTC | 2026-05-03 08:29 UTC | 1h 15m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Ambala Air Force Station (VIAM) | 2026-05-03 06:34 UTC | 2026-05-03 08:28 UTC | 1h 53m |
| IGO6336 | IndiGo | Bengaluru International Airport (VOBL) | Rajahmundry Airport (VORY) | 2026-05-03 07:27 UTC | 2026-05-03 08:26 UTC | 58m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-03 07:13 UTC | 2026-05-03 08:26 UTC | 1h 12m |
| TVJ132 | TVJ | Suvarnabhumi Airport (VTBS) | VLXL (VLXL) | 2026-05-03 07:28 UTC | 2026-05-03 08:26 UTC | 57m |
| EZY37KJ | easyJet | Manchester Airport (EGCC) | Tivat Airport (LYTV) | 2026-05-03 05:52 UTC | 2026-05-03 08:23 UTC | 2h 31m |
| JL2325 |  | Osaka International Airport (RJOO) | Tajima Airport (RJBT) | 2026-05-03 08:08 UTC | 2026-05-03 08:23 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
