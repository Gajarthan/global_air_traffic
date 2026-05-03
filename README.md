# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_23:34:20_UTC-green)

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

**Latest saved flight:** 2026-05-02 23:34:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 23:34:20 UTC

- **65,144** saved flights
- **24,745** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,144** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **798,321.1 tonnes** estimated CO2 emissions
- **46,279,485 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2763 |
| 2 | SkyWest Airlines | 2418 |
| 3 | IndiGo | 1495 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1010 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 834 |
| 8 | ENY | 806 |
| 9 | Vueling | 640 |
| 10 | AXM | 631 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 566 |
| 13 | Delta Air Lines | 546 |
| 14 | WIF | 539 |
| 15 | AZU | 526 |
| 16 | QLK | 502 |
| 17 | Swiss International | 499 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 446 |
| 20 | easyJet | 425 |
| 21 | AEE | 420 |
| 22 | EJU | 416 |
| 23 | VIV | 408 |
| 24 | Cathay Pacific | 392 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 377 |
| 27 | AXB | 363 |
| 28 | CXK | 331 |
| 29 | AIQ | 330 |
| 30 | GLO | 317 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51675 |
| 2 | 🇪🇸 ES | 4756 |
| 3 | 🇮🇳 IN | 4707 |
| 4 | 🇦🇺 AU | 4349 |
| 5 | 🇧🇷 BR | 3673 |
| 6 | 🇩🇪 DE | 3637 |
| 7 | 🇮🇹 IT | 3529 |
| 8 | 🇯🇵 JP | 3529 |
| 9 | 🇨🇦 CA | 3197 |
| 10 | 🇬🇧 GB | 2797 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2571 |
| 13 | 🇲🇽 MX | 2071 |
| 14 | 🇬🇷 GR | 1943 |
| 15 | 🇨🇭 CH | 1820 |
| 16 | 🇳🇴 NO | 1766 |
| 17 | 🇲🇾 MY | 1546 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1211 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1165 |
| 22 | 🇵🇭 PH | 1093 |
| 23 | 🇵🇱 PL | 1061 |
| 24 | 🇰🇷 KR | 1060 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 800 |
| 27 | 🇲🇴 MO | 734 |
| 28 | 🇲🇪 ME | 701 |
| 29 | 🇳🇱 NL | 686 |
| 30 | 🇮🇩 ID | 545 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1190 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 988 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 945 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 834 |
| 9 | Harry Reid International Airport |  | US | 819 |
| 10 | Zurich Airport |  | CH | 769 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 734 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 641 |
| 14 | Chicago O'Hare International Airport |  | US | 623 |
| 15 | Madrid Barajas International Airport |  | ES | 619 |
| 16 | Kuala Lumpur International Airport |  | MY | 614 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 570 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 560 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 518 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 514 |
| 25 | Charles de Gaulle International Airport |  | FR | 505 |
| 26 | Ninoy Aquino International Airport |  | PH | 497 |
| 27 | Daniel K Inouye International Airport |  | US | 480 |
| 28 | Capua Airport |  | IT | 480 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 474 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 442 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 435 |
| 33 | Vitoria/Foronda Airport |  | ES | 432 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 430 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 38 | Amsterdam Airport Schiphol |  | NL | 403 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 222 | 21m | 244 km | 934.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 202 | 24m | 225 km | 783.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 148 | 26m | 275 km | 701.3 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-02 11:50 UTC | 2026-05-02 23:34 UTC | 11h 44m |
| DAL1764 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-05-02 13:53 UTC | 2026-05-02 23:25 UTC | 9h 31m |
| FFT2198 | FFT | Chicago O'Hare International Airport (KORD) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-05-02 22:04 UTC | 2026-05-02 23:24 UTC | 1h 20m |
| DAL2843 | Delta Air Lines | Nashville International Airport (KBNA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-02 21:34 UTC | 2026-05-02 23:21 UTC | 1h 46m |
| N723AJ |  | KU42 (KU42) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-02 22:08 UTC | 2026-05-02 23:11 UTC | 1h 2m |
| SCU35 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-05-02 22:47 UTC | 2026-05-02 23:03 UTC | 16m |
| EJA877 | EJA | Eppley Airfield (KOMA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-02 20:35 UTC | 2026-05-02 23:02 UTC | 2h 26m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-05-02 22:35 UTC | 2026-05-02 23:01 UTC | 25m |
| OSU14 | OSU | Ohio State University Airport (KOSU) | Madison County Airport (KUYF) | 2026-05-02 22:29 UTC | 2026-05-02 22:56 UTC | 26m |
| DAL2910 | Delta Air Lines | Indianapolis International Airport (KIND) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-02 21:33 UTC | 2026-05-02 22:55 UTC | 1h 22m |
| SNJ91 | SNJ | Tokyo International Airport (RJTT) | Hiroshima Airport (RJOA) | 2026-05-02 21:46 UTC | 2026-05-02 22:54 UTC | 1h 7m |
| N2545G |  | Pru Field (K33S) | Pru Field (K33S) | 2026-05-02 22:43 UTC | 2026-05-02 22:49 UTC | 6m |
| N325HL |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-05-02 22:16 UTC | 2026-05-02 22:47 UTC | 30m |
| JBU266 | JetBlue | Southwest Florida International Airport (KRSW) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-02 20:03 UTC | 2026-05-02 22:46 UTC | 2h 43m |
| N7153W |  | Reservoir Airport (MD95) | Donegal Springs Airpark (KN71) | 2026-05-02 22:20 UTC | 2026-05-02 22:46 UTC | 26m |
| EJA310 | EJA | Dekalb-Peachtree Airport (KPDK) | Dekalb-Peachtree Airport (KPDK) | 2026-05-02 22:42 UTC | 2026-05-02 22:46 UTC | 3m |
| SAVER70 | SAV | Bomoen Airport (ENBM) | Bergen Airport Flesland (ENBR) | 2026-05-02 22:29 UTC | 2026-05-02 22:45 UTC | 15m |
| ENY3598 | ENY | Chicago O'Hare International Airport (KORD) | 7II7 (7II7) | 2026-05-02 22:23 UTC | 2026-05-02 22:44 UTC | 21m |
| VIV7434 | VIV | Abraham Gonzalez International Airport (MMCS) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-02 20:53 UTC | 2026-05-02 22:44 UTC | 1h 50m |
| JZA192 | JZA | Vancouver International Airport (CYVR) | Moose Jaw Air Vice Marshal C. M. McEwen Airport (CYMJ) | 2026-05-02 21:09 UTC | 2026-05-02 22:43 UTC | 1h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
