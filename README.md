# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_16:54:40_UTC-green)

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

**Latest saved flight:** 2026-05-02 16:54:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 16:54:40 UTC

- **64,519** saved flights
- **24,535** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,519** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **791,013.1 tonnes** estimated CO2 emissions
- **45,855,830 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2736 |
| 2 | SkyWest Airlines | 2371 |
| 3 | IndiGo | 1492 |
| 4 | EJA | 1151 |
| 5 | American Airlines | 994 |
| 6 | Southwest Airlines | 909 |
| 7 | Lufthansa | 831 |
| 8 | ENY | 790 |
| 9 | Vueling | 636 |
| 10 | AXM | 630 |
| 11 | LATAM Airlines | 600 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 535 |
| 15 | AZU | 523 |
| 16 | QLK | 502 |
| 17 | Swiss International | 498 |
| 18 | LXJ | 460 |
| 19 | Alaska Airlines | 441 |
| 20 | easyJet | 421 |
| 21 | AEE | 417 |
| 22 | EJU | 413 |
| 23 | VIV | 403 |
| 24 | Cathay Pacific | 389 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 376 |
| 27 | AXB | 362 |
| 28 | AIQ | 330 |
| 29 | CXK | 328 |
| 30 | GLO | 316 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50920 |
| 2 | 🇪🇸 ES | 4717 |
| 3 | 🇮🇳 IN | 4700 |
| 4 | 🇦🇺 AU | 4343 |
| 5 | 🇧🇷 BR | 3643 |
| 6 | 🇩🇪 DE | 3618 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3500 |
| 9 | 🇨🇦 CA | 3155 |
| 10 | 🇬🇧 GB | 2772 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2553 |
| 13 | 🇲🇽 MX | 2033 |
| 14 | 🇬🇷 GR | 1930 |
| 15 | 🇨🇭 CH | 1814 |
| 16 | 🇳🇴 NO | 1762 |
| 17 | 🇲🇾 MY | 1545 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1158 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇰🇷 KR | 1056 |
| 24 | 🇵🇱 PL | 1055 |
| 25 | 🇬🇹 GT | 998 |
| 26 | 🇲🇦 MA | 792 |
| 27 | 🇲🇴 MO | 728 |
| 28 | 🇲🇪 ME | 698 |
| 29 | 🇳🇱 NL | 682 |
| 30 | 🇮🇩 ID | 544 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1412 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1052 |
| 4 | Indira Gandhi International Airport |  | IN | 984 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 940 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 830 |
| 9 | Harry Reid International Airport |  | US | 809 |
| 10 | Zurich Airport |  | CH | 767 |
| 11 | La Aurora Airport |  | GT | 748 |
| 12 | Macau International Airport |  | MO | 728 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 631 |
| 14 | Kuala Lumpur International Airport |  | MY | 613 |
| 15 | Madrid Barajas International Airport |  | ES | 612 |
| 16 | Chicago O'Hare International Airport |  | US | 611 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 578 |
| 18 | Bengaluru International Airport |  | IN | 570 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 557 |
| 21 | Congonhas Airport |  | BR | 526 |
| 22 | Tenerife Norte Airport |  | ES | 513 |
| 23 | Salt Lake City International Airport |  | US | 508 |
| 24 | Charlotte/Douglas International Airport |  | US | 506 |
| 25 | Charles de Gaulle International Airport |  | FR | 503 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 475 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 474 |
| 29 | Capua Airport |  | IT | 469 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 461 |
| 31 | Barcelona International Airport |  | ES | 439 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 429 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 429 |
| 34 | Vitoria/Foronda Airport |  | ES | 428 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 403 |
| 38 | Amsterdam Airport Schiphol |  | NL | 400 |
| 39 | Reno/Tahoe International Airport |  | US | 395 |
| 40 | Calgary International Airport |  | CA | 380 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 219 | 21m | 244 km | 922.1 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 159 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 145 | 26m | 275 km | 687.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 90 | 1h 42m | 1,156 km | 1,795.5 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 86 | 23m | 55 km | 81.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 84 | 1h 42m | 1,423 km | 2,061.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1914V |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-05-02 16:42 UTC | 2026-05-02 16:54 UTC | 12m |
| N3799T |  | Pompano Beach Airpark (KPMP) | Immokalee Regional Airport (KIMM) | 2026-05-02 15:42 UTC | 2026-05-02 16:52 UTC | 1h 10m |
| NSZ5352 | NSZ | Alicante International Airport (LEAL) | Stockholm-Arlanda Airport (ESSA) | 2026-05-02 13:20 UTC | 2026-05-02 16:49 UTC | 3h 29m |
| N988LB |  | Eugene's Dream Airport (6XS7) | Perot Field/Fort Worth Alliance Airport (KAFW) | 2026-05-02 16:36 UTC | 2026-05-02 16:48 UTC | 11m |
| N96836 |  | Delano Municipal Airport (KDLO) | Meadows Field (KBFL) | 2026-05-02 16:31 UTC | 2026-05-02 16:45 UTC | 14m |
| N756UJ |  | Skydive Iowa Airport (09IA) | Skydive Iowa Airport (09IA) | 2026-05-02 16:17 UTC | 2026-05-02 16:43 UTC | 25m |
| N992AK |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-05-02 16:37 UTC | 2026-05-02 16:37 UTC | 0m |
| N82WC |  | K61B (K61B) | X Bar 1 Ranch (Lower) Airport (AZ97) | 2026-05-02 15:57 UTC | 2026-05-02 16:35 UTC | 38m |
| N1914V |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-05-02 16:19 UTC | 2026-05-02 16:32 UTC | 12m |
| N432AT |  | Okc Will Rogers International Airport (KOKC) | Rocky Mountain Metro Airport (KBJC) | 2026-05-02 14:49 UTC | 2026-05-02 16:31 UTC | 1h 41m |
| SCU48 | SCU | Double W Airport (3OK7) | 19OK (19OK) | 2026-05-02 16:00 UTC | 2026-05-02 16:31 UTC | 31m |
| N434BZ |  | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-05-02 16:16 UTC | 2026-05-02 16:30 UTC | 14m |
| OMFRI | OMF | Kosice Airport (LZKZ) | Spisska Nova Glider Airport (LZSV) | 2026-05-02 16:19 UTC | 2026-05-02 16:29 UTC | 10m |
| EJA463 | EJA | Gleim Field (FD81) | Lancaster Airport (KLNS) | 2026-05-02 14:39 UTC | 2026-05-02 16:23 UTC | 1h 43m |
| DHXCF | DHX | Regensburg-Oberhub Airport (EDNR) | Straubing Airport (EDMS) | 2026-05-02 16:11 UTC | 2026-05-02 16:21 UTC | 10m |
| N218HP |  | Space Coast Regional Airport (KTIX) | Virgil I Grissom Municipal Airport (KBFR) | 2026-05-02 13:56 UTC | 2026-05-02 16:21 UTC | 2h 24m |
| N225J |  | Preston Airport (KU10) | Preston Airport (KU10) | 2026-05-02 15:46 UTC | 2026-05-02 16:15 UTC | 28m |
| N1743L |  | Allegheny County Airport (KAGC) | Rostraver Airport (KFWQ) | 2026-05-02 14:54 UTC | 2026-05-02 16:15 UTC | 1h 20m |
| N92824 |  | Mallory Airport (WV12) | Kurt's Field (27WV) | 2026-05-02 15:52 UTC | 2026-05-02 16:09 UTC | 17m |
| N120AM |  | NM79 (NM79) | Las Cruces International Airport (KLRU) | 2026-05-02 16:00 UTC | 2026-05-02 16:07 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
