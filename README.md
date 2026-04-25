# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_21:28:20_UTC-green)

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

**Latest saved flight:** 2026-04-25 21:28:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 21:28:20 UTC

- **54,353** saved flights
- **21,521** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,353** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **652,832.7 tonnes** estimated CO2 emissions
- **37,845,376 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2294 |
| 2 | SkyWest Airlines | 2059 |
| 3 | IndiGo | 1228 |
| 4 | EJA | 965 |
| 5 | American Airlines | 874 |
| 6 | Southwest Airlines | 776 |
| 7 | ENY | 687 |
| 8 | Lufthansa | 642 |
| 9 | Vueling | 547 |
| 10 | LATAM Airlines | 524 |
| 11 | AXM | 522 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 462 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | Swiss International | 419 |
| 17 | QLK | 416 |
| 18 | LXJ | 397 |
| 19 | AEE | 362 |
| 20 | Alaska Airlines | 359 |
| 21 | easyJet | 349 |
| 22 | EJU | 348 |
| 23 | VIV | 348 |
| 24 | Air France | 313 |
| 25 | Japan Airlines | 313 |
| 26 | Cathay Pacific | 291 |
| 27 | AXB | 286 |
| 28 | GLO | 279 |
| 29 | AIQ | 277 |
| 30 | JetBlue | 277 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43387 |
| 2 | 🇪🇸 ES | 3949 |
| 3 | 🇮🇳 IN | 3864 |
| 4 | 🇦🇺 AU | 3625 |
| 5 | 🇧🇷 BR | 3155 |
| 6 | 🇮🇹 IT | 2938 |
| 7 | 🇩🇪 DE | 2907 |
| 8 | 🇯🇵 JP | 2889 |
| 9 | 🇨🇦 CA | 2699 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2279 |
| 12 | 🇫🇷 FR | 2120 |
| 13 | 🇲🇽 MX | 1701 |
| 14 | 🇬🇷 GR | 1624 |
| 15 | 🇨🇭 CH | 1536 |
| 16 | 🇳🇴 NO | 1455 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1019 |
| 20 | 🇹🇷 TR | 980 |
| 21 | 🇹🇭 TH | 975 |
| 22 | 🇵🇭 PH | 918 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 872 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 685 |
| 27 | 🇲🇪 ME | 588 |
| 28 | 🇳🇱 NL | 552 |
| 29 | 🇲🇴 MO | 536 |
| 30 | 🇧🇸 BS | 471 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1239 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 906 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 822 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 801 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 701 |
| 9 | Zurich Airport |  | CH | 645 |
| 10 | Frankfurt am Main International Airport |  | DE | 627 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 538 |
| 13 | Macau International Airport |  | MO | 536 |
| 14 | Chicago O'Hare International Airport |  | US | 531 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 514 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 504 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 472 |
| 19 | Malpensa International Airport |  | IT | 466 |
| 20 | Bengaluru International Airport |  | IN | 461 |
| 21 | Congonhas Airport |  | BR | 454 |
| 22 | Charlotte/Douglas International Airport |  | US | 445 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 424 |
| 25 | Salt Lake City International Airport |  | US | 412 |
| 26 | Charles de Gaulle International Airport |  | FR | 411 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 405 |
| 28 | Capua Airport |  | IT | 398 |
| 29 | Daniel K Inouye International Airport |  | US | 395 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 385 |
| 31 | Vitoria/Foronda Airport |  | ES | 372 |
| 32 | Barcelona International Airport |  | ES | 367 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 364 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 358 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 324 |
| 40 | Viracopos International Airport |  | BR | 321 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 168 | 21m | 244 km | 707.4 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 126 | 26m | 275 km | 597.1 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 74 | 23m | 55 km | 70.3 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 73 | 1h 53m | 1,304 km | 1,642.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 70 | 1h 19m | 961 km | 1,160.3 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-25 20:42 UTC | 2026-04-25 21:28 UTC | 45m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-04-25 18:03 UTC | 2026-04-25 21:27 UTC | 3h 23m |
| CPA873 | Cathay Pacific | San Francisco International Airport (KSFO) | Macau International Airport (VMMC) | 2026-04-25 07:38 UTC | 2026-04-25 21:17 UTC | 13h 39m |
| N181SD |  | John Wayne/Orange County Airport (KSNA) | Mc Conville Airstrip (CA42) | 2026-04-25 21:04 UTC | 2026-04-25 21:15 UTC | 10m |
| TKR16 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | 6CO3 (6CO3) | 2026-04-25 20:55 UTC | 2026-04-25 21:13 UTC | 18m |
| SRD375 | SRD | RNAS Lee-On-Solent (EGHF) | RNAS Lee-On-Solent (EGHF) | 2026-04-25 19:22 UTC | 2026-04-25 21:09 UTC | 1h 46m |
| N5380L |  | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-04-25 20:48 UTC | 2026-04-25 21:03 UTC | 14m |
| N828SK |  | Stout Airport (FD83) | Rocky Mountain Metro Airport (KBJC) | 2026-04-25 17:20 UTC | 2026-04-25 21:02 UTC | 3h 42m |
| N6389B |  | Dayton/Wright Brothers Airport (KMGY) | Dayton/Wright Brothers Airport (KMGY) | 2026-04-25 20:36 UTC | 2026-04-25 21:01 UTC | 25m |
| CHX76 | CHX | Varrelbusch Airport (EDWU) | Meppe Airport (ETWM) | 2026-04-25 20:49 UTC | 2026-04-25 21:01 UTC | 11m |
| N3049Q |  | Las Cruces International Airport (KLRU) | Casas Adobes Airpark (NM69) | 2026-04-25 20:15 UTC | 2026-04-25 21:00 UTC | 45m |
| N7669G |  | De Kalb Taylor Municipal Airport (KDKB) | Wade Airport (56LL) | 2026-04-25 20:28 UTC | 2026-04-25 20:57 UTC | 29m |
| N125PM |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-04-25 18:55 UTC | 2026-04-25 20:55 UTC | 2h 0m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-25 20:44 UTC | 2026-04-25 20:55 UTC | 10m |
| N118UV |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-04-25 20:27 UTC | 2026-04-25 20:54 UTC | 26m |
| N9448Z |  | North Palm Beach County General Aviation Airport (KF45) | North Palm Beach County General Aviation Airport (KF45) | 2026-04-25 20:52 UTC | 2026-04-25 20:53 UTC | 0m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-25 20:25 UTC | 2026-04-25 20:50 UTC | 24m |
| ACA7 | Air Canada | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-04-25 07:58 UTC | 2026-04-25 20:48 UTC | 12h 49m |
| N9830V |  | Bend Municipal Airport (KBDN) | Juniper Air Park (5OR5) | 2026-04-25 20:38 UTC | 2026-04-25 20:45 UTC | 6m |
| N267WG |  | Sarasota/Bradenton International Airport (KSRQ) | TX11 (TX11) | 2026-04-25 17:59 UTC | 2026-04-25 20:44 UTC | 2h 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
