# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_13:19:09_UTC-green)

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

**Latest saved flight:** 2026-04-26 13:19:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 13:19:09 UTC

- **55,200** saved flights
- **21,730** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,200** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **667,239.3 tonnes** estimated CO2 emissions
- **38,680,540 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2339 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1256 |
| 4 | EJA | 968 |
| 5 | American Airlines | 880 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 674 |
| 9 | Vueling | 557 |
| 10 | AXM | 543 |
| 11 | LATAM Airlines | 531 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 464 |
| 14 | Delta Air Lines | 453 |
| 15 | WIF | 453 |
| 16 | Swiss International | 432 |
| 17 | QLK | 429 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 367 |
| 21 | EJU | 358 |
| 22 | easyJet | 355 |
| 23 | VIV | 352 |
| 24 | Japan Airlines | 321 |
| 25 | Air France | 319 |
| 26 | Cathay Pacific | 312 |
| 27 | AXB | 297 |
| 28 | AIQ | 282 |
| 29 | JetBlue | 281 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43708 |
| 2 | 🇪🇸 ES | 4021 |
| 3 | 🇮🇳 IN | 3972 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3177 |
| 6 | 🇮🇹 IT | 3002 |
| 7 | 🇩🇪 DE | 3000 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2729 |
| 10 | 🇨🇴 CO | 2485 |
| 11 | 🇬🇧 GB | 2315 |
| 12 | 🇫🇷 FR | 2180 |
| 13 | 🇲🇽 MX | 1721 |
| 14 | 🇬🇷 GR | 1646 |
| 15 | 🇨🇭 CH | 1568 |
| 16 | 🇳🇴 NO | 1469 |
| 17 | 🇲🇾 MY | 1322 |
| 18 | 🇿🇦 ZA | 1139 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1004 |
| 21 | 🇹🇭 TH | 1000 |
| 22 | 🇵🇭 PH | 944 |
| 23 | 🇰🇷 KR | 894 |
| 24 | 🇵🇱 PL | 889 |
| 25 | 🇬🇹 GT | 825 |
| 26 | 🇲🇦 MA | 703 |
| 27 | 🇲🇪 ME | 605 |
| 28 | 🇳🇱 NL | 570 |
| 29 | 🇲🇴 MO | 568 |
| 30 | 🇮🇩 ID | 476 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1249 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | Indira Gandhi International Airport |  | IN | 841 |
| 5 | El Dorado International Airport |  | CO | 840 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 812 |
| 7 | Guaymaral Airport |  | CO | 751 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Zurich Airport |  | CH | 664 |
| 10 | Frankfurt am Main International Airport |  | DE | 658 |
| 11 | La Aurora Airport |  | GT | 618 |
| 12 | Macau International Airport |  | MO | 568 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 536 |
| 15 | Kuala Lumpur International Airport |  | MY | 521 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 17 | Madrid Barajas International Airport |  | ES | 511 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 475 |
| 20 | Bengaluru International Airport |  | IN | 471 |
| 21 | Congonhas Airport |  | BR | 456 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 441 |
| 24 | Ninoy Aquino International Airport |  | PH | 435 |
| 25 | Charles de Gaulle International Airport |  | FR | 423 |
| 26 | Salt Lake City International Airport |  | US | 415 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 407 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 397 |
| 31 | Vitoria/Foronda Airport |  | ES | 380 |
| 32 | Barcelona International Airport |  | ES | 375 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 368 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 366 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 362 |
| 37 | O. R. Tambo International Airport |  | ZA | 355 |
| 38 | Don Mueang International Airport |  | TH | 339 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Viracopos International Airport |  | BR | 323 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 305 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 201 | 14m | 114 km | 394.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 141 | 19m | 165 km | 401.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 128 | 26m | 275 km | 606.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 90 | 27m | 215 km | 333.3 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 83 | 27m | 152 km | 216.9 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 73 | 58m | 493 km | 621.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9042H |  | Albert Whitted Airport (KSPG) | Winter Haven Regional Airport (KGIF) | 2026-04-26 12:44 UTC | 2026-04-26 13:19 UTC | 35m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-26 06:29 UTC | 2026-04-26 12:57 UTC | 6h 28m |
| GBKIJ | GBK | Fowlmere Airfield (EGMA) | Fowlmere Airfield (EGMA) | 2026-04-26 12:30 UTC | 2026-04-26 12:55 UTC | 24m |
| FJLEM | FJL | Saint-Cyr-l'Ecole Airport (LFPZ) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-04-26 12:17 UTC | 2026-04-26 12:48 UTC | 30m |
| RYR8V | Ryanair | Sandefjord Airport Torp (ENTO) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-26 11:07 UTC | 2026-04-26 12:45 UTC | 1h 37m |
| N608EA |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-04-26 12:38 UTC | 2026-04-26 12:44 UTC | 6m |
| KAP747 | KAP | Cape Cod Gateway Airport (KHYA) | KNHZ (KNHZ) | 2026-04-26 11:59 UTC | 2026-04-26 12:41 UTC | 42m |
| WIF1FY | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-26 12:30 UTC | 2026-04-26 12:41 UTC | 11m |
| SXHNY | SXH | Eleftherios Venizelos International Airport (LGAV) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-26 12:28 UTC | 2026-04-26 12:38 UTC | 10m |
| S5DOT |  | Novo Mesto Airport (LJNM) | Novo Mesto Airport (LJNM) | 2026-04-26 12:20 UTC | 2026-04-26 12:37 UTC | 16m |
| FJKZH | FJK | Saint-Cyr-l'Ecole Airport (LFPZ) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-04-26 12:21 UTC | 2026-04-26 12:34 UTC | 13m |
| RYR51DD | Ryanair | Comiso Airport Vincenzo Magliocco (LICB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-26 10:28 UTC | 2026-04-26 12:33 UTC | 2h 4m |
| TVJ134 | TVJ | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-04-26 11:24 UTC | 2026-04-26 12:31 UTC | 1h 7m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-26 12:07 UTC | 2026-04-26 12:30 UTC | 22m |
| GBMOF | GBM | EG32 (EG32) | EG32 (EG32) | 2026-04-26 12:11 UTC | 2026-04-26 12:27 UTC | 15m |
| WIF170 | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-04-26 11:59 UTC | 2026-04-26 12:27 UTC | 27m |
| HK3544G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-26 12:07 UTC | 2026-04-26 12:25 UTC | 17m |
| JBU550 | JetBlue | Savannah/Hilton Head International Airport (KSAV) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-26 10:27 UTC | 2026-04-26 12:24 UTC | 1h 56m |
| VLG1SE | Vueling | Firenze / Peretola Airport (LIRQ) | Paris-Orly Airport (LFPO) | 2026-04-26 11:02 UTC | 2026-04-26 12:22 UTC | 1h 20m |
| RYR2WY | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Neumarkt/Obf. Airport (EDPO) | 2026-04-26 11:14 UTC | 2026-04-26 12:22 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
