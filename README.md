# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_01:37:04_UTC-green)

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

**Latest saved flight:** 2026-04-26 01:37:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 01:37:04 UTC

- **54,581** saved flights
- **21,585** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,581** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **657,388.9 tonnes** estimated CO2 emissions
- **38,109,504 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2297 |
| 2 | SkyWest Airlines | 2071 |
| 3 | IndiGo | 1230 |
| 4 | EJA | 967 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 779 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 642 |
| 9 | Vueling | 547 |
| 10 | LATAM Airlines | 526 |
| 11 | AXM | 524 |
| 12 | All Nippon Airways | 480 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | Swiss International | 419 |
| 17 | QLK | 416 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 364 |
| 20 | AEE | 362 |
| 21 | VIV | 352 |
| 22 | EJU | 349 |
| 23 | easyJet | 349 |
| 24 | Japan Airlines | 315 |
| 25 | Air France | 313 |
| 26 | Cathay Pacific | 306 |
| 27 | AXB | 286 |
| 28 | AIQ | 279 |
| 29 | GLO | 279 |
| 30 | JetBlue | 278 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43625 |
| 2 | 🇪🇸 ES | 3952 |
| 3 | 🇮🇳 IN | 3871 |
| 4 | 🇦🇺 AU | 3642 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2945 |
| 7 | 🇩🇪 DE | 2912 |
| 8 | 🇯🇵 JP | 2908 |
| 9 | 🇨🇦 CA | 2717 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2282 |
| 12 | 🇫🇷 FR | 2124 |
| 13 | 🇲🇽 MX | 1716 |
| 14 | 🇬🇷 GR | 1624 |
| 15 | 🇨🇭 CH | 1537 |
| 16 | 🇳🇴 NO | 1455 |
| 17 | 🇲🇾 MY | 1273 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1036 |
| 20 | 🇹🇷 TR | 984 |
| 21 | 🇹🇭 TH | 979 |
| 22 | 🇵🇭 PH | 924 |
| 23 | 🇰🇷 KR | 880 |
| 24 | 🇵🇱 PL | 874 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 685 |
| 27 | 🇲🇪 ME | 589 |
| 28 | 🇳🇱 NL | 553 |
| 29 | 🇲🇴 MO | 552 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1247 |
| 2 | Tokyo International Airport |  | JP | 988 |
| 3 | Denver International Airport |  | US | 910 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 823 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 801 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 703 |
| 9 | Zurich Airport |  | CH | 646 |
| 10 | Frankfurt am Main International Airport |  | DE | 628 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 552 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 542 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 507 |
| 17 | Madrid Barajas International Airport |  | ES | 504 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 475 |
| 19 | Malpensa International Airport |  | IT | 468 |
| 20 | Bengaluru International Airport |  | IN | 461 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 427 |
| 25 | Salt Lake City International Airport |  | US | 414 |
| 26 | Charles de Gaulle International Airport |  | FR | 413 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 401 |
| 29 | Capua Airport |  | IT | 398 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 386 |
| 31 | Vitoria/Foronda Airport |  | ES | 372 |
| 32 | Barcelona International Airport |  | ES | 369 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 364 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 358 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 334 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 248 | 1h 7m | 706 km | 3,019.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 177 | 24m | 225 km | 686.7 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 172 | 21m | 244 km | 724.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 155 | 1h 27m | 910 km | 2,432.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 126 | 26m | 275 km | 597.1 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 101 | 1h 11m | 770 km | 1,341.7 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 93 | 31m | 369 km | 592.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N442BG |  | Wood County Airport (K1G0) | Wood County Airport (K1G0) | 2026-04-26 01:19 UTC | 2026-04-26 01:37 UTC | 17m |
| CHX88 | CHX | Nuremberg Airport (EDDN) | Rosenthal-Field Plossen Airport (EDQP) | 2026-04-26 01:01 UTC | 2026-04-26 01:26 UTC | 25m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-25 23:41 UTC | 2026-04-26 01:15 UTC | 1h 34m |
| STA621D | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-04-26 00:55 UTC | 2026-04-26 01:11 UTC | 16m |
| THY84U | Turkish Airlines | Chicago O'Hare International Airport (KORD) | EPSJ (EPSJ) | 2026-04-25 17:03 UTC | 2026-04-26 01:10 UTC | 8h 7m |
| N3181Q |  | Fulton County Executive/Charlie Brown Field (KFTY) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-25 23:13 UTC | 2026-04-26 00:56 UTC | 1h 43m |
| N900EY |  | Salt Lake City International Airport (KSLC) | Music Mountain Air Ranch Airport (68AZ) | 2026-04-25 23:35 UTC | 2026-04-26 00:56 UTC | 1h 20m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-26 00:33 UTC | 2026-04-26 00:54 UTC | 21m |
| N224JA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-26 00:32 UTC | 2026-04-26 00:52 UTC | 19m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-26 00:48 UTC | 2026-04-26 00:51 UTC | 3m |
| QTR814 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-25 18:00 UTC | 2026-04-26 00:47 UTC | 6h 47m |
| N377LM |  | 2TS6 (2TS6) | Mid-Way Regional Airport (KJWY) | 2026-04-26 00:30 UTC | 2026-04-26 00:45 UTC | 15m |
| N110UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-04-25 23:44 UTC | 2026-04-26 00:44 UTC | 59m |
| CXK477 | CXK | B & C Airport (IL99) | 1IS5 (1IS5) | 2026-04-26 00:39 UTC | 2026-04-26 00:44 UTC | 4m |
| N51883 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-04-26 00:00 UTC | 2026-04-26 00:42 UTC | 42m |
| AFL212 | AFL | Sheremetyevo International Airport (UUEE) | Macau International Airport (VMMC) | 2026-04-25 16:25 UTC | 2026-04-26 00:42 UTC | 8h 16m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-04-26 00:27 UTC | 2026-04-26 00:42 UTC | 14m |
| TVR4703 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-25 18:03 UTC | 2026-04-26 00:41 UTC | 6h 37m |
| N600AT |  | Floyd W Jones Lebanon Airport (KLBO) | 11MU (11MU) | 2026-04-26 00:28 UTC | 2026-04-26 00:40 UTC | 11m |
| AIQ3522 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Ratchasima Airport (VTUQ) | 2026-04-26 00:13 UTC | 2026-04-26 00:39 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
