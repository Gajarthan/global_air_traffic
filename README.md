# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_23:09:46_UTC-green)

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

**Latest saved flight:** 2026-04-26 23:09:46 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 23:09:46 UTC

- **56,233** saved flights
- **22,100** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,233** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **680,899.9 tonnes** estimated CO2 emissions
- **39,472,459 km** total distance flown
- **845 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2390 |
| 2 | SkyWest Airlines | 2128 |
| 3 | IndiGo | 1275 |
| 4 | EJA | 1009 |
| 5 | American Airlines | 897 |
| 6 | Southwest Airlines | 800 |
| 7 | ENY | 713 |
| 8 | Lufthansa | 691 |
| 9 | Vueling | 566 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 545 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 474 |
| 14 | WIF | 466 |
| 15 | Delta Air Lines | 464 |
| 16 | Swiss International | 439 |
| 17 | QLK | 431 |
| 18 | LXJ | 401 |
| 19 | Alaska Airlines | 375 |
| 20 | AEE | 371 |
| 21 | EJU | 361 |
| 22 | VIV | 359 |
| 23 | easyJet | 358 |
| 24 | Air France | 327 |
| 25 | Cathay Pacific | 321 |
| 26 | Japan Airlines | 321 |
| 27 | AXB | 305 |
| 28 | JetBlue | 288 |
| 29 | GLO | 285 |
| 30 | United Airlines | 285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44665 |
| 2 | 🇪🇸 ES | 4114 |
| 3 | 🇮🇳 IN | 4025 |
| 4 | 🇦🇺 AU | 3740 |
| 5 | 🇧🇷 BR | 3251 |
| 6 | 🇩🇪 DE | 3068 |
| 7 | 🇮🇹 IT | 3065 |
| 8 | 🇯🇵 JP | 2993 |
| 9 | 🇨🇦 CA | 2786 |
| 10 | 🇨🇴 CO | 2540 |
| 11 | 🇬🇧 GB | 2363 |
| 12 | 🇫🇷 FR | 2213 |
| 13 | 🇲🇽 MX | 1786 |
| 14 | 🇬🇷 GR | 1666 |
| 15 | 🇨🇭 CH | 1587 |
| 16 | 🇳🇴 NO | 1506 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1151 |
| 19 | 🇳🇿 NZ | 1053 |
| 20 | 🇹🇷 TR | 1027 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 907 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 838 |
| 26 | 🇲🇦 MA | 713 |
| 27 | 🇲🇪 ME | 610 |
| 28 | 🇳🇱 NL | 587 |
| 29 | 🇲🇴 MO | 582 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1282 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 935 |
| 4 | El Dorado International Airport |  | CO | 855 |
| 5 | Indira Gandhi International Airport |  | IN | 853 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 820 |
| 7 | Guaymaral Airport |  | CO | 776 |
| 8 | Harry Reid International Airport |  | US | 716 |
| 9 | Frankfurt am Main International Airport |  | DE | 677 |
| 10 | Zurich Airport |  | CH | 674 |
| 11 | La Aurora Airport |  | GT | 630 |
| 12 | Macau International Airport |  | MO | 582 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 561 |
| 14 | Chicago O'Hare International Airport |  | US | 549 |
| 15 | Madrid Barajas International Airport |  | ES | 528 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 525 |
| 17 | Kuala Lumpur International Airport |  | MY | 523 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 493 |
| 19 | Malpensa International Airport |  | IT | 486 |
| 20 | Bengaluru International Airport |  | IN | 479 |
| 21 | Congonhas Airport |  | BR | 467 |
| 22 | Charlotte/Douglas International Airport |  | US | 454 |
| 23 | Tenerife Norte Airport |  | ES | 451 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 432 |
| 26 | Salt Lake City International Airport |  | US | 431 |
| 27 | Capua Airport |  | IT | 417 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 414 |
| 29 | Daniel K Inouye International Airport |  | US | 413 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 402 |
| 31 | Barcelona International Airport |  | ES | 386 |
| 32 | Vitoria/Foronda Airport |  | ES | 384 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 381 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 373 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 368 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 360 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 337 |
| 40 | Amsterdam Airport Schiphol |  | NL | 334 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 316 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 206 | 14m | 114 km | 404.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 178 | 21m | 244 km | 749.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 135 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 80 | 1h 1m | 695 km | 959.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 53m | 1,304 km | 1,709.8 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 74 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-26 21:38 UTC | 2026-04-26 23:09 UTC | 1h 30m |
| N248SG |  | KN37 (KN37) | Lehigh Valley International Airport (KABE) | 2026-04-26 22:35 UTC | 2026-04-26 23:03 UTC | 27m |
| RGY937 | RGY | Monterey Regional Airport (KMRY) | Scottsdale Airport (KSDL) | 2026-04-26 21:35 UTC | 2026-04-26 22:58 UTC | 1h 22m |
| TVR4703 | TVR | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-26 16:12 UTC | 2026-04-26 22:56 UTC | 6h 43m |
| MFX676 | MFX | Ben Gurion International Airport (LLBG) | Tbilisi International Airport (UGTB) | 2026-04-26 20:37 UTC | 2026-04-26 22:55 UTC | 2h 18m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-26 22:25 UTC | 2026-04-26 22:54 UTC | 29m |
| VIV7066 | VIV | Santa Lucia Air Force Base (MMSM) | Chilpancingo Airport (MMCH) | 2026-04-26 22:30 UTC | 2026-04-26 22:54 UTC | 24m |
| UPS5842 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Salt Lake City International Airport (KSLC) | 2026-04-26 19:30 UTC | 2026-04-26 22:54 UTC | 3h 23m |
| N5278R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-04-26 22:25 UTC | 2026-04-26 22:52 UTC | 27m |
| N950LA |  | Long Beach (Daugherty Field) Airport (KLGB) | Van Nuys Airport (KVNY) | 2026-04-26 22:07 UTC | 2026-04-26 22:51 UTC | 44m |
| YMV | YMV | Wollongong Airport (YWOL) | Aeropelican Airport (YPEC) | 2026-04-26 21:38 UTC | 2026-04-26 22:46 UTC | 1h 8m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-26 22:22 UTC | 2026-04-26 22:41 UTC | 18m |
| N912MN |  | Joe Foss Field (KFSD) | Sibley Municipal Airport (KISB) | 2026-04-26 22:26 UTC | 2026-04-26 22:41 UTC | 14m |
| N378AC |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-04-26 21:48 UTC | 2026-04-26 22:38 UTC | 50m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-26 10:45 UTC | 2026-04-26 22:36 UTC | 11h 50m |
| NHC47 | NHC | Wilhelmshaven-Mariensiel Airport (EDWI) | Wilhelmshaven-Mariensiel Airport (EDWI) | 2026-04-26 21:26 UTC | 2026-04-26 22:35 UTC | 1h 9m |
| N78RK |  | Tucson International Airport (KTUS) | Yampa Valley Airport (KHDN) | 2026-04-26 21:03 UTC | 2026-04-26 22:35 UTC | 1h 31m |
| N2231E |  | Flyers Airport (10IA) | Flyers Airport (10IA) | 2026-04-26 22:27 UTC | 2026-04-26 22:34 UTC | 6m |
| N752CH |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-04-26 21:31 UTC | 2026-04-26 22:31 UTC | 1h 0m |
| AM318 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-04-26 22:03 UTC | 2026-04-26 22:28 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
