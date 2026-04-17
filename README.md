# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_07:36:07_UTC-green)

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

**Latest saved flight:** 2026-04-17 07:36:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 07:36:07 UTC

- **38,574** saved flights
- **16,617** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,574** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **466,071.3 tonnes** estimated CO2 emissions
- **27,018,629 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1616 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 948 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 406 |
| 9 | Vueling | 389 |
| 10 | LATAM Airlines | 386 |
| 11 | Lufthansa | 385 |
| 12 | AZU | 343 |
| 13 | All Nippon Airways | 342 |
| 14 | Delta Air Lines | 326 |
| 15 | QLK | 326 |
| 16 | LXJ | 309 |
| 17 | WIF | 292 |
| 18 | Swiss International | 285 |
| 19 | Alaska Airlines | 258 |
| 20 | AEE | 257 |
| 21 | EJU | 250 |
| 22 | easyJet | 250 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 234 |
| 25 | Air France | 215 |
| 26 | EDV | 212 |
| 27 | United Airlines | 211 |
| 28 | GLO | 200 |
| 29 | AIQ | 199 |
| 30 | JetBlue | 199 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30437 |
| 2 | 🇮🇳 IN | 2901 |
| 3 | 🇪🇸 ES | 2851 |
| 4 | 🇦🇺 AU | 2765 |
| 5 | 🇧🇷 BR | 2263 |
| 6 | 🇯🇵 JP | 2086 |
| 7 | 🇮🇹 IT | 2020 |
| 8 | 🇩🇪 DE | 1954 |
| 9 | 🇨🇦 CA | 1900 |
| 10 | 🇨🇴 CO | 1898 |
| 11 | 🇬🇧 GB | 1575 |
| 12 | 🇫🇷 FR | 1448 |
| 13 | 🇲🇽 MX | 1216 |
| 14 | 🇬🇷 GR | 1159 |
| 15 | 🇨🇭 CH | 1048 |
| 16 | 🇲🇾 MY | 980 |
| 17 | 🇳🇴 NO | 933 |
| 18 | 🇳🇿 NZ | 807 |
| 19 | 🇿🇦 ZA | 799 |
| 20 | 🇵🇭 PH | 716 |
| 21 | 🇹🇭 TH | 706 |
| 22 | 🇹🇷 TR | 688 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 634 |
| 25 | 🇵🇱 PL | 600 |
| 26 | 🇲🇦 MA | 478 |
| 27 | 🇳🇱 NL | 386 |
| 28 | 🇲🇪 ME | 378 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 361 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 710 |
| 3 | El Dorado International Airport |  | CO | 669 |
| 4 | Denver International Airport |  | US | 648 |
| 5 | Indira Gandhi International Airport |  | IN | 627 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 572 |
| 7 | Harry Reid International Airport |  | US | 506 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 462 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 12 | Kuala Lumpur International Airport |  | MY | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 378 |
| 15 | Chicago O'Hare International Airport |  | US | 372 |
| 16 | Macau International Airport |  | MO | 355 |
| 17 | Madrid Barajas International Airport |  | ES | 350 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Bengaluru International Airport |  | IN | 335 |
| 22 | Congonhas Airport |  | BR | 334 |
| 23 | Ninoy Aquino International Airport |  | PH | 333 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 292 |
| 27 | Daniel K Inouye International Airport |  | US | 287 |
| 28 | Charles de Gaulle International Airport |  | FR | 282 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 275 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 31 | Vitoria/Foronda Airport |  | ES | 263 |
| 32 | Capua Airport |  | IT | 262 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 258 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 249 |
| 38 | Don Mueang International Airport |  | TH | 237 |
| 39 | Viracopos International Airport |  | BR | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 178 | 1h 8m | 706 km | 2,167.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 98 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 97 | 21m | 244 km | 408.4 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 88 | 26m | 275 km | 417.0 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 85 | 54m | 546 km | 800.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 78 | 1h 11m | 770 km | 1,036.2 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 74 | 45m | 452 km | 576.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 23 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 58 | 1h 41m | 1,423 km | 1,423.4 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 57 | 26m | 215 km | 211.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 29 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 53 | 1h 21m | 961 km | 878.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KLM835 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Hang Nadim Airport (WIDD) | 2026-04-16 19:27 UTC | 2026-04-17 07:36 UTC | 12h 8m |
| NCG08 | NCG | Midden-Zeeland Airport (EHMZ) | Rotterdam Airport (EHRD) | 2026-04-17 07:15 UTC | 2026-04-17 07:33 UTC | 17m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Sariang Airport (VTCS) | 2026-04-17 07:12 UTC | 2026-04-17 07:27 UTC | 15m |
| SPICY85 | SPI | Niederstetten Airport (ETHN) | Ochsenfurt Airport (EDGJ) | 2026-04-17 06:37 UTC | 2026-04-17 07:21 UTC | 44m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-04-17 06:52 UTC | 2026-04-17 07:17 UTC | 24m |
| 2SALE |  | Blackpool International Airport (EGNH) | Liverpool John Lennon Airport (EGGP) | 2026-04-17 07:00 UTC | 2026-04-17 07:15 UTC | 14m |
| XSN06 | XSN | K61B (K61B) | San Carlos Airport (KSQL) | 2026-04-17 05:28 UTC | 2026-04-17 07:10 UTC | 1h 41m |
| N240HY |  | Merrill Municipal Airport (KRRL) | Wausau Downtown Airport (KAUW) | 2026-04-17 06:56 UTC | 2026-04-17 07:05 UTC | 8m |
| N432LF |  | Port Angeles Cgas Airport (KNOW) | Tacoma Narrows Airport (KTIW) | 2026-04-17 06:28 UTC | 2026-04-17 07:01 UTC | 32m |
| V619 |  | Locarno Airport (LSZL) | Ambri Airport (LSPM) | 2026-04-17 06:46 UTC | 2026-04-17 07:00 UTC | 14m |
| JLK | JLK | Moruya Airport (YMRY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-17 05:38 UTC | 2026-04-17 07:00 UTC | 1h 22m |
| RYR611A | Ryanair | Valencia Airport (LEVC) | Eindhoven Airport (EHEH) | 2026-04-17 04:53 UTC | 2026-04-17 06:58 UTC | 2h 4m |
| LUCKY22 | LUC | Kawaihapai Airfield (PHDH) | Waimea-Kohala Airport (PHMU) | 2026-04-17 06:20 UTC | 2026-04-17 06:55 UTC | 34m |
| R21237 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-17 06:10 UTC | 2026-04-17 06:45 UTC | 35m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-04-17 05:55 UTC | 2026-04-17 06:44 UTC | 49m |
| N911LS |  | Halstead Airport (SN05) | Cessna Acft Field (KCEA) | 2026-04-17 06:26 UTC | 2026-04-17 06:42 UTC | 16m |
| UBG147 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-17 06:09 UTC | 2026-04-17 06:42 UTC | 33m |
| VOZ274 | Virgin Australia | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-17 05:42 UTC | 2026-04-17 06:40 UTC | 58m |
| RYR82LZ | Ryanair | Václav Havel Airport (LKPR) | Diagoras Airport (LGRP) | 2026-04-17 04:04 UTC | 2026-04-17 06:37 UTC | 2h 33m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-04-17 05:23 UTC | 2026-04-17 06:37 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
