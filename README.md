# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_09:21:56_UTC-green)

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

**Latest saved flight:** 2026-04-26 09:21:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 09:21:56 UTC

- **54,899** saved flights
- **21,662** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,899** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **662,146.4 tonnes** estimated CO2 emissions
- **38,385,298 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2317 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1243 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 659 |
| 9 | Vueling | 551 |
| 10 | AXM | 533 |
| 11 | LATAM Airlines | 526 |
| 12 | All Nippon Airways | 489 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 453 |
| 15 | WIF | 448 |
| 16 | QLK | 426 |
| 17 | Swiss International | 424 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 365 |
| 21 | easyJet | 352 |
| 22 | VIV | 352 |
| 23 | EJU | 351 |
| 24 | Japan Airlines | 319 |
| 25 | Air France | 316 |
| 26 | Cathay Pacific | 308 |
| 27 | AXB | 291 |
| 28 | AIQ | 281 |
| 29 | JetBlue | 280 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43680 |
| 2 | 🇪🇸 ES | 3982 |
| 3 | 🇮🇳 IN | 3926 |
| 4 | 🇦🇺 AU | 3714 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2970 |
| 7 | 🇩🇪 DE | 2960 |
| 8 | 🇯🇵 JP | 2956 |
| 9 | 🇨🇦 CA | 2723 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2294 |
| 12 | 🇫🇷 FR | 2144 |
| 13 | 🇲🇽 MX | 1720 |
| 14 | 🇬🇷 GR | 1633 |
| 15 | 🇨🇭 CH | 1549 |
| 16 | 🇳🇴 NO | 1458 |
| 17 | 🇲🇾 MY | 1297 |
| 18 | 🇿🇦 ZA | 1123 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 996 |
| 21 | 🇹🇭 TH | 992 |
| 22 | 🇵🇭 PH | 940 |
| 23 | 🇰🇷 KR | 885 |
| 24 | 🇵🇱 PL | 880 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 692 |
| 27 | 🇲🇪 ME | 598 |
| 28 | 🇳🇱 NL | 564 |
| 29 | 🇲🇴 MO | 560 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1248 |
| 2 | Tokyo International Airport |  | JP | 1007 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 830 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 806 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Zurich Airport |  | CH | 653 |
| 10 | Frankfurt am Main International Airport |  | DE | 643 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 560 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 514 |
| 17 | Madrid Barajas International Airport |  | ES | 507 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 489 |
| 19 | Malpensa International Airport |  | IT | 471 |
| 20 | Bengaluru International Airport |  | IN | 468 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 437 |
| 24 | Ninoy Aquino International Airport |  | PH | 433 |
| 25 | Charles de Gaulle International Airport |  | FR | 417 |
| 26 | Salt Lake City International Airport |  | US | 415 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 400 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 393 |
| 31 | Vitoria/Foronda Airport |  | ES | 376 |
| 32 | Barcelona International Airport |  | ES | 373 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 361 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 37 | O. R. Tambo International Airport |  | ZA | 353 |
| 38 | Don Mueang International Airport |  | TH | 338 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 251 | 1h 7m | 706 km | 3,055.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 159 | 1h 27m | 910 km | 2,495.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 157 | 28m | 304 km | 823.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 133 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 127 | 26m | 275 km | 601.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 106 | 1h 12m | 770 km | 1,408.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 94 | 31m | 369 km | 598.3 t |
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
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 72 | 58m | 493 km | 612.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEKLP | DEK | Husum-Schwesing Airport (EDXJ) | Husum-Schwesing Airport (EDXJ) | 2026-04-26 08:29 UTC | 2026-04-26 09:21 UTC | 52m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-25 22:06 UTC | 2026-04-26 09:17 UTC | 11h 10m |
| KLM1303 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-04-26 07:55 UTC | 2026-04-26 09:06 UTC | 1h 11m |
| HBXCL | HBX | St Stephan Airport (LSTS) | Megeve Airport (LFHM) | 2026-04-26 08:08 UTC | 2026-04-26 09:05 UTC | 57m |
| HBXTP | HBX | Dubendorf Airport (LSMD) | St Gallen Altenrhein Airport (LSZR) | 2026-04-26 08:41 UTC | 2026-04-26 09:01 UTC | 19m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-25 21:43 UTC | 2026-04-26 08:49 UTC | 11h 5m |
| ATG7780 | ATG | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-25 19:29 UTC | 2026-04-26 08:45 UTC | 13h 15m |
| PH4V2 |  | De Kooy Airport (EHKD) | Texel Airport (EHTX) | 2026-04-26 07:57 UTC | 2026-04-26 08:41 UTC | 43m |
| RXA2131 | RXA | Perth International Airport (YPPH) | Manjimup Airport (YMJM) | 2026-04-26 07:54 UTC | 2026-04-26 08:41 UTC | 46m |
| FGRUB | FGR | Maubeuge-Elesmes Airport (LFQJ) | Maubeuge-Elesmes Airport (LFQJ) | 2026-04-26 07:58 UTC | 2026-04-26 08:41 UTC | 42m |
| NSZ2632 | NSZ | Stockholm-Arlanda Airport (ESSA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-26 07:03 UTC | 2026-04-26 08:34 UTC | 1h 30m |
| VOE6XC | VOE | Menorca Airport (LEMH) | La Morgal Airport (LEMR) | 2026-04-26 07:09 UTC | 2026-04-26 08:34 UTC | 1h 24m |
| GTI8138 | GTI | Suvarnabhumi Airport (VTBS) | Macau International Airport (VMMC) | 2026-04-26 03:21 UTC | 2026-04-26 08:32 UTC | 5h 10m |
| GTI9445 | GTI | RAF Fairford (EGVA) | Macau International Airport (VMMC) | 2026-04-25 20:49 UTC | 2026-04-26 08:28 UTC | 11h 39m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Ambala Air Force Station (VIAM) | 2026-04-26 06:29 UTC | 2026-04-26 08:26 UTC | 1h 56m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-26 07:07 UTC | 2026-04-26 08:26 UTC | 1h 18m |
| RYR4EY | Ryanair | Brussels South Charleroi Airport (EBCI) | Angads Airport (GMFO) | 2026-04-26 05:57 UTC | 2026-04-26 08:24 UTC | 2h 26m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-26 08:04 UTC | 2026-04-26 08:22 UTC | 18m |
| ANA785 | All Nippon Airways | Osaka International Airport (RJOO) | Saga Airport (RJFS) | 2026-04-26 07:25 UTC | 2026-04-26 08:22 UTC | 57m |
| FHSNO | FHS | Meribel Airport (LFKX) | Meribel Airport (LFKX) | 2026-04-26 07:28 UTC | 2026-04-26 08:20 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
