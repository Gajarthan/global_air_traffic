# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_20:25:01_UTC-green)

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

**Latest saved flight:** 2026-05-06 20:25:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 20:25:01 UTC

- **71,205** saved flights
- **26,497** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,205** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **877,501.0 tonnes** estimated CO2 emissions
- **50,869,623 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3073 |
| 2 | SkyWest Airlines | 2651 |
| 3 | IndiGo | 1621 |
| 4 | EJA | 1299 |
| 5 | American Airlines | 1115 |
| 6 | Southwest Airlines | 1032 |
| 7 | Lufthansa | 922 |
| 8 | ENY | 889 |
| 9 | Vueling | 701 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 661 |
| 12 | WIF | 610 |
| 13 | Delta Air Lines | 598 |
| 14 | All Nippon Airways | 591 |
| 15 | AZU | 578 |
| 16 | Swiss International | 551 |
| 17 | QLK | 547 |
| 18 | LXJ | 516 |
| 19 | Alaska Airlines | 498 |
| 20 | easyJet | 476 |
| 21 | AEE | 460 |
| 22 | EJU | 459 |
| 23 | VIV | 445 |
| 24 | Cathay Pacific | 435 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 418 |
| 27 | AXB | 395 |
| 28 | AIQ | 358 |
| 29 | CXK | 353 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 56753 |
| 2 | 🇪🇸 ES | 5196 |
| 3 | 🇮🇳 IN | 5089 |
| 4 | 🇦🇺 AU | 4706 |
| 5 | 🇧🇷 BR | 4002 |
| 6 | 🇩🇪 DE | 3976 |
| 7 | 🇮🇹 IT | 3911 |
| 8 | 🇯🇵 JP | 3777 |
| 9 | 🇨🇦 CA | 3529 |
| 10 | 🇬🇧 GB | 3084 |
| 11 | 🇫🇷 FR | 2814 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2254 |
| 14 | 🇬🇷 GR | 2124 |
| 15 | 🇳🇴 NO | 1962 |
| 16 | 🇨🇭 CH | 1950 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1283 |
| 22 | 🇵🇱 PL | 1185 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1135 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 853 |
| 27 | 🇲🇴 MO | 825 |
| 28 | 🇲🇪 ME | 766 |
| 29 | 🇳🇱 NL | 743 |
| 30 | 🇧🇸 BS | 600 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1591 |
| 2 | Tokyo International Airport |  | JP | 1275 |
| 3 | Denver International Airport |  | US | 1184 |
| 4 | Indira Gandhi International Airport |  | IN | 1070 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1038 |
| 6 | Frankfurt am Main International Airport |  | DE | 915 |
| 7 | Harry Reid International Airport |  | US | 890 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | Zurich Airport |  | CH | 848 |
| 11 | La Aurora Airport |  | GT | 845 |
| 12 | Macau International Airport |  | MO | 825 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 716 |
| 14 | Chicago O'Hare International Airport |  | US | 693 |
| 15 | Kuala Lumpur International Airport |  | MY | 679 |
| 16 | Madrid Barajas International Airport |  | ES | 677 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 638 |
| 18 | Malpensa International Airport |  | IT | 621 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 21 | Salt Lake City International Airport |  | US | 575 |
| 22 | Congonhas Airport |  | BR | 569 |
| 23 | Capua Airport |  | IT | 562 |
| 24 | Charlotte/Douglas International Airport |  | US | 560 |
| 25 | Charles de Gaulle International Airport |  | FR | 558 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 523 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 500 |
| 31 | Barcelona International Airport |  | ES | 497 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 485 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 477 |
| 34 | Vitoria/Foronda Airport |  | ES | 471 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 446 |
| 37 | Amsterdam Airport Schiphol |  | NL | 443 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Calgary International Airport |  | CA | 423 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 248 | 21m | 244 km | 1,044.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 178 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 95 | 1h 43m | 1,423 km | 2,331.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 89 | 23m | 55 km | 84.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ANA968 | All Nippon Airways | Nagasaki Airport (RJFU) | Tokyo International Airport (RJTT) | 2026-05-06 19:08 UTC | 2026-05-06 20:25 UTC | 1h 16m |
| N488BL |  | Johnston Regional Airport (KJNX) | Wayne Executive Jetport Airport (KGWW) | 2026-05-06 20:00 UTC | 2026-05-06 20:17 UTC | 16m |
| N605FF |  | Riverside Airport (KRAL) | Santa Barbara Municipal Airport (KSBA) | 2026-05-06 19:04 UTC | 2026-05-06 20:17 UTC | 1h 12m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-06 19:40 UTC | 2026-05-06 20:15 UTC | 35m |
| N7063Q |  | Tampa North Aero Park Airport (KX39) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-05-06 20:03 UTC | 2026-05-06 20:15 UTC | 11m |
| HAWK222 | HAW | Kingsville Nas Airport (KNQI) | Duval County Ranch Company Airport (28TA) | 2026-05-06 20:00 UTC | 2026-05-06 20:14 UTC | 13m |
| N460LD |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-06 19:21 UTC | 2026-05-06 20:12 UTC | 50m |
| N293DC |  | Sacramento Executive Airport (KSAC) | Sacramento Mather Airport (KMHR) | 2026-05-06 19:59 UTC | 2026-05-06 20:12 UTC | 12m |
| HOOK43 | HOO | Good Life Ranch Airport (17OK) | Tulsa International Airport (KTUL) | 2026-05-06 19:38 UTC | 2026-05-06 20:11 UTC | 32m |
| SWR5BW | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-05-06 19:57 UTC | 2026-05-06 20:10 UTC | 12m |
| N71PW |  | Eagle Field (15ME) | Presque Isle International Airport (KPQI) | 2026-05-06 19:24 UTC | 2026-05-06 20:08 UTC | 44m |
| CHP14 | CHP | Bodad Airport (CA11) | Weed Airport (KO46) | 2026-05-06 19:47 UTC | 2026-05-06 20:05 UTC | 18m |
| N36PJ |  | Monterey Regional Airport (KMRY) | Santa Ynez/Kunkle Field (KIZA) | 2026-05-06 19:23 UTC | 2026-05-06 20:05 UTC | 42m |
| N48JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-05-06 19:24 UTC | 2026-05-06 20:03 UTC | 38m |
| N665GR |  | Willow Airport (PAUO) | Ted Stevens Anchorage International Airport (PANC) | 2026-05-06 19:36 UTC | 2026-05-06 20:03 UTC | 26m |
| N9476X |  | 8II1 (8II1) | Purdue University Airport (KLAF) | 2026-05-06 19:22 UTC | 2026-05-06 20:01 UTC | 39m |
| N7012N |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Rush City Regional Airport (KROS) | 2026-05-06 19:17 UTC | 2026-05-06 20:00 UTC | 43m |
| EVIL06 | EVI | Good Life Ranch Airport (17OK) | Tulsa International Airport (KTUL) | 2026-05-06 19:29 UTC | 2026-05-06 19:59 UTC | 29m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-06 05:55 UTC | 2026-05-06 19:58 UTC | 14h 2m |
| EJM518 | EJM | Van Nuys Airport (KVNY) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-06 19:02 UTC | 2026-05-06 19:56 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
