# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_07:46:01_UTC-green)

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

**Latest saved flight:** 2026-05-03 07:46:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 07:46:01 UTC

- **65,295** saved flights
- **24,771** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,295** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **800,294.6 tonnes** estimated CO2 emissions
- **46,393,887 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2770 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1504 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1011 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 836 |
| 8 | ENY | 806 |
| 9 | Vueling | 643 |
| 10 | AXM | 636 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 567 |
| 13 | Delta Air Lines | 546 |
| 14 | WIF | 539 |
| 15 | AZU | 526 |
| 16 | QLK | 510 |
| 17 | Swiss International | 503 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 427 |
| 21 | AEE | 422 |
| 22 | EJU | 419 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 392 |
| 25 | Japan Airlines | 386 |
| 26 | Air France | 378 |
| 27 | AXB | 365 |
| 28 | AIQ | 331 |
| 29 | CXK | 331 |
| 30 | GLO | 317 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51706 |
| 2 | 🇪🇸 ES | 4771 |
| 3 | 🇮🇳 IN | 4735 |
| 4 | 🇦🇺 AU | 4382 |
| 5 | 🇧🇷 BR | 3673 |
| 6 | 🇩🇪 DE | 3644 |
| 7 | 🇯🇵 JP | 3562 |
| 8 | 🇮🇹 IT | 3543 |
| 9 | 🇨🇦 CA | 3203 |
| 10 | 🇬🇧 GB | 2801 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2579 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1948 |
| 15 | 🇨🇭 CH | 1827 |
| 16 | 🇳🇴 NO | 1766 |
| 17 | 🇲🇾 MY | 1564 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1220 |
| 20 | 🇹🇭 TH | 1185 |
| 21 | 🇹🇷 TR | 1165 |
| 22 | 🇵🇭 PH | 1094 |
| 23 | 🇰🇷 KR | 1067 |
| 24 | 🇵🇱 PL | 1062 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 801 |
| 27 | 🇲🇴 MO | 736 |
| 28 | 🇲🇪 ME | 705 |
| 29 | 🇳🇱 NL | 687 |
| 30 | 🇮🇩 ID | 554 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1200 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 995 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 949 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 835 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 774 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 736 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Chicago O'Hare International Airport |  | US | 623 |
| 15 | Madrid Barajas International Airport |  | ES | 622 |
| 16 | Kuala Lumpur International Airport |  | MY | 621 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 574 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 570 |
| 20 | Malpensa International Airport |  | IT | 562 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 518 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 515 |
| 25 | Charles de Gaulle International Airport |  | FR | 507 |
| 26 | Ninoy Aquino International Airport |  | PH | 498 |
| 27 | Capua Airport |  | IT | 484 |
| 28 | Daniel K Inouye International Airport |  | US | 481 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 477 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 444 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 435 |
| 33 | Vitoria/Foronda Airport |  | ES | 435 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 431 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 412 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 38 | Amsterdam Airport Schiphol |  | NL | 403 |
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
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 191 | 1h 27m | 910 km | 2,997.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 190 | 28m | 304 km | 996.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 161 | 20m | 165 km | 458.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 153 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 143 | 1h 11m | 770 km | 1,899.6 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 120 | 44m | 452 km | 935.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
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
| EJU78LQ | EJU | Lyon Saint-Exupery Airport (LFLL) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-03 05:23 UTC | 2026-05-03 07:46 UTC | 2h 22m |
| CMA576 | CMA | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-02 20:20 UTC | 2026-05-03 07:41 UTC | 11h 21m |
| TWB408 | TWB | Barcelona International Airport (LEBL) | Incheon International Airport (RKSI) | 2026-05-02 19:32 UTC | 2026-05-03 07:34 UTC | 12h 1m |
| TRP7 | TRP | Chesapeake Ranch Airport (MD50) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-05-03 06:59 UTC | 2026-05-03 07:24 UTC | 24m |
| VOE1664 | VOE | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Paris-Orly Airport (LFPO) | 2026-05-03 06:14 UTC | 2026-05-03 07:19 UTC | 1h 5m |
| IGO364F | IndiGo | Bengaluru International Airport (VOBL) | Meghauli Airport (VNMG) | 2026-05-03 03:46 UTC | 2026-05-03 07:15 UTC | 3h 29m |
| DLH1WN | Lufthansa | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-05-03 06:35 UTC | 2026-05-03 07:12 UTC | 37m |
| JLK | JLK | Moruya Airport (YMRY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-03 06:05 UTC | 2026-05-03 07:11 UTC | 1h 6m |
| QLK11D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-05-03 06:50 UTC | 2026-05-03 07:11 UTC | 20m |
| S5PGI |  | Maribor Airport (LJMB) | Maribor Airport (LJMB) | 2026-05-03 06:56 UTC | 2026-05-03 07:11 UTC | 15m |
| AEE151 | AEE | Alexander the Great International Airport (LGKV) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-03 06:11 UTC | 2026-05-03 07:10 UTC | 59m |
| RYR3603 | Ryanair | Treviso / Sant'Angelo Airport (LIPH) | Bilbao Airport (LEBB) | 2026-05-03 05:22 UTC | 2026-05-03 07:08 UTC | 1h 45m |
| IGO127 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-05-03 06:26 UTC | 2026-05-03 07:07 UTC | 41m |
| AXM6419 | AXM | Ulu Bernam Airport (WMBF) | Batu Pahat Airport (WMAB) | 2026-05-03 06:42 UTC | 2026-05-03 07:05 UTC | 22m |
| EZY24HL | easyJet | London Luton Airport (EGGW) | Zemunik Airport (LDZD) | 2026-05-03 05:10 UTC | 2026-05-03 07:04 UTC | 1h 54m |
| RYR170F | Ryanair | L'Aquila / Preturo Airport (LIAP) | Stanke Dimitrov Highway Strip (LB37) | 2026-05-03 05:59 UTC | 2026-05-03 07:02 UTC | 1h 2m |
| EXS18RK | EXS | London Stansted Airport (EGSS) | Igualada/Odena Airport (LEIG) | 2026-05-03 05:09 UTC | 2026-05-03 07:02 UTC | 1h 53m |
| PAG08 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Brandon Municipal Airport (CYBR) | 2026-05-03 06:27 UTC | 2026-05-03 07:01 UTC | 33m |
| THY9SD | Turkish Airlines | Batumi International Airport (UGSB) | Celje Glider Airport (LJCL) | 2026-05-02 18:47 UTC | 2026-05-03 07:01 UTC | 12h 13m |
| EZY95PL | easyJet | London Gatwick Airport (EGKK) | Malpensa International Airport (LIMC) | 2026-05-03 05:26 UTC | 2026-05-03 06:59 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
