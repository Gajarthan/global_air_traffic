# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_21:10:26_UTC-green)

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

**Latest saved flight:** 2026-04-21 21:10:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 21:10:26 UTC

- **47,320** saved flights
- **19,337** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,320** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **568,876.4 tonnes** estimated CO2 emissions
- **32,978,340 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2016 |
| 2 | SkyWest Airlines | 1830 |
| 3 | IndiGo | 1107 |
| 4 | EJA | 812 |
| 5 | American Airlines | 784 |
| 6 | Southwest Airlines | 678 |
| 7 | ENY | 615 |
| 8 | Lufthansa | 509 |
| 9 | Vueling | 476 |
| 10 | AXM | 470 |
| 11 | LATAM Airlines | 467 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 404 |
| 14 | Delta Air Lines | 393 |
| 15 | WIF | 380 |
| 16 | QLK | 376 |
| 17 | LXJ | 367 |
| 18 | Swiss International | 364 |
| 19 | AEE | 321 |
| 20 | Alaska Airlines | 321 |
| 21 | EJU | 315 |
| 22 | easyJet | 303 |
| 23 | VIV | 300 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 253 |
| 27 | JetBlue | 252 |
| 28 | AXB | 248 |
| 29 | United Airlines | 248 |
| 30 | GLO | 240 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37660 |
| 2 | 🇮🇳 IN | 3443 |
| 3 | 🇪🇸 ES | 3439 |
| 4 | 🇦🇺 AU | 3235 |
| 5 | 🇧🇷 BR | 2783 |
| 6 | 🇮🇹 IT | 2584 |
| 7 | 🇯🇵 JP | 2571 |
| 8 | 🇩🇪 DE | 2449 |
| 9 | 🇨🇦 CA | 2320 |
| 10 | 🇨🇴 CO | 2200 |
| 11 | 🇬🇧 GB | 1933 |
| 12 | 🇫🇷 FR | 1805 |
| 13 | 🇲🇽 MX | 1463 |
| 14 | 🇬🇷 GR | 1444 |
| 15 | 🇨🇭 CH | 1299 |
| 16 | 🇳🇴 NO | 1211 |
| 17 | 🇲🇾 MY | 1147 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 915 |
| 20 | 🇹🇭 TH | 847 |
| 21 | 🇵🇭 PH | 833 |
| 22 | 🇹🇷 TR | 832 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 745 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 586 |
| 27 | 🇲🇪 ME | 506 |
| 28 | 🇳🇱 NL | 483 |
| 29 | 🇲🇴 MO | 447 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1117 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 785 |
| 4 | El Dorado International Airport |  | CO | 765 |
| 5 | Indira Gandhi International Airport |  | IN | 737 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 715 |
| 7 | Guaymaral Airport |  | CO | 615 |
| 8 | Harry Reid International Airport |  | US | 610 |
| 9 | Zurich Airport |  | CH | 563 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 481 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 474 |
| 13 | Chicago O'Hare International Airport |  | US | 463 |
| 14 | Kuala Lumpur International Airport |  | MY | 460 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 16 | Macau International Airport |  | MO | 447 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 421 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 406 |
| 21 | Malpensa International Airport |  | IT | 401 |
| 22 | Congonhas Airport |  | BR | 397 |
| 23 | Tenerife Norte Airport |  | ES | 395 |
| 24 | Ninoy Aquino International Airport |  | PH | 385 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 357 |
| 26 | Salt Lake City International Airport |  | US | 355 |
| 27 | Daniel K Inouye International Airport |  | US | 353 |
| 28 | Charles de Gaulle International Airport |  | FR | 352 |
| 29 | Capua Airport |  | IT | 351 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 345 |
| 31 | Reno/Tahoe International Airport |  | US | 327 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 327 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 322 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | O. R. Tambo International Airport |  | ZA | 313 |
| 36 | Barcelona International Airport |  | ES | 313 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 282 |
| 40 | Viracopos International Airport |  | BR | 281 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 246 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 180 | 14m | 114 km | 353.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 76 | 20m | 147 km | 192.3 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 75 | 52m | 556 km | 718.9 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 0m | 695 km | 779.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 64 | 16m | 162 km | 179.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 63 | 11m | 15 km | 16.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R43543 |  | Wheeler-Sack Army Air Field (KGTB) | Wheeler-Sack Army Air Field (KGTB) | 2026-04-21 20:58 UTC | 2026-04-21 21:10 UTC | 12m |
| N509AF |  | Morristown Municipal Airport (KMMU) | Sky Manor Airport (KN40) | 2026-04-21 20:03 UTC | 2026-04-21 21:09 UTC | 1h 6m |
| N17FJ |  | Bob Hope Airport (KBUR) | Yucca Valley Airport (KL22) | 2026-04-21 20:48 UTC | 2026-04-21 21:09 UTC | 20m |
| STGRY32 | STG | Corpus Christi Nas (Truax Field) Airport (KNGP) | MS74 (MS74) | 2026-04-21 19:17 UTC | 2026-04-21 21:08 UTC | 1h 50m |
| N225MK |  | St Pete-Clearwater International Airport (KPIE) | Orlando Executive Airport (KORL) | 2026-04-21 20:28 UTC | 2026-04-21 21:06 UTC | 37m |
| URSA23 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-21 20:36 UTC | 2026-04-21 21:06 UTC | 29m |
| N48ZA |  | 8NJ0 (8NJ0) | Laguardia Airport (KLGA) | 2026-04-21 20:15 UTC | 2026-04-21 21:04 UTC | 48m |
| VILLN62 | VIL | Hill Afb Airport (KHIF) | Goshute Airport (UT65) | 2026-04-21 20:32 UTC | 2026-04-21 21:02 UTC | 29m |
| ARES44 | ARE | Ciampino Airport (LIRA) | Urbe Airport (LIRU) | 2026-04-21 20:41 UTC | 2026-04-21 20:53 UTC | 12m |
| N511MP |  | Fort Lauderdale Executive Airport (KFXE) | Immokalee Regional Airport (KIMM) | 2026-04-21 19:51 UTC | 2026-04-21 20:49 UTC | 57m |
| N82HE |  | William B Greene Jr Regional Airport (K0A9) | Raleigh-Durham International Airport (KRDU) | 2026-04-21 20:07 UTC | 2026-04-21 20:44 UTC | 36m |
| N621HS |  | Phyllis Field (6IL2) | 8LL1 (8LL1) | 2026-04-21 20:13 UTC | 2026-04-21 20:44 UTC | 30m |
| ZKPDZ | ZKP | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-04-21 20:31 UTC | 2026-04-21 20:43 UTC | 12m |
| N157PH |  | Cincinnati Municipal/Lunken Field (KLUK) | Scottsdale Airport (KSDL) | 2026-04-21 17:13 UTC | 2026-04-21 20:42 UTC | 3h 29m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-21 20:31 UTC | 2026-04-21 20:42 UTC | 10m |
| VJT809 | VJT | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-21 19:05 UTC | 2026-04-21 20:40 UTC | 1h 34m |
| N99273 |  | Dover Afb Airport (KDOV) | Ocean City Municipal Airport (KOXB) | 2026-04-21 20:05 UTC | 2026-04-21 20:39 UTC | 33m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-04-21 06:23 UTC | 2026-04-21 20:38 UTC | 14h 14m |
| CGHAN | CGH | Vancouver International Airport (CYVR) | Pitt Meadows Airport (CYPK) | 2026-04-21 20:21 UTC | 2026-04-21 20:37 UTC | 16m |
| TWY007 | TWY | Horseshoe Bay Resort Airport (KDZB) | Cavern City Air Trml Airport (KCNM) | 2026-04-21 19:51 UTC | 2026-04-21 20:37 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
