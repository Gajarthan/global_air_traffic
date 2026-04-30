# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_06:24:27_UTC-green)

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

**Latest saved flight:** 2026-04-30 06:24:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 06:24:27 UTC

- **60,143** saved flights
- **23,230** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,143** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **731,592.5 tonnes** estimated CO2 emissions
- **42,411,162 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2552 |
| 2 | SkyWest Airlines | 2253 |
| 3 | IndiGo | 1380 |
| 4 | EJA | 1082 |
| 5 | American Airlines | 941 |
| 6 | Southwest Airlines | 854 |
| 7 | Lufthansa | 761 |
| 8 | ENY | 748 |
| 9 | Vueling | 598 |
| 10 | AXM | 585 |
| 11 | LATAM Airlines | 575 |
| 12 | All Nippon Airways | 532 |
| 13 | WIF | 504 |
| 14 | Delta Air Lines | 503 |
| 15 | AZU | 493 |
| 16 | QLK | 476 |
| 17 | Swiss International | 473 |
| 18 | LXJ | 428 |
| 19 | Alaska Airlines | 415 |
| 20 | AEE | 400 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 379 |
| 24 | Cathay Pacific | 360 |
| 25 | Air France | 353 |
| 26 | Japan Airlines | 352 |
| 27 | AXB | 330 |
| 28 | AIQ | 304 |
| 29 | JetBlue | 300 |
| 30 | CXK | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47645 |
| 2 | 🇮🇳 IN | 4363 |
| 3 | 🇪🇸 ES | 4344 |
| 4 | 🇦🇺 AU | 4128 |
| 5 | 🇧🇷 BR | 3404 |
| 6 | 🇩🇪 DE | 3328 |
| 7 | 🇮🇹 IT | 3296 |
| 8 | 🇯🇵 JP | 3279 |
| 9 | 🇨🇦 CA | 2982 |
| 10 | 🇨🇴 CO | 2613 |
| 11 | 🇬🇧 GB | 2525 |
| 12 | 🇫🇷 FR | 2369 |
| 13 | 🇲🇽 MX | 1886 |
| 14 | 🇬🇷 GR | 1798 |
| 15 | 🇨🇭 CH | 1665 |
| 16 | 🇳🇴 NO | 1642 |
| 17 | 🇲🇾 MY | 1424 |
| 18 | 🇿🇦 ZA | 1212 |
| 19 | 🇳🇿 NZ | 1136 |
| 20 | 🇹🇭 TH | 1085 |
| 21 | 🇹🇷 TR | 1075 |
| 22 | 🇵🇭 PH | 1015 |
| 23 | 🇵🇱 PL | 970 |
| 24 | 🇰🇷 KR | 968 |
| 25 | 🇬🇹 GT | 876 |
| 26 | 🇲🇦 MA | 749 |
| 27 | 🇲🇴 MO | 666 |
| 28 | 🇲🇪 ME | 656 |
| 29 | 🇳🇱 NL | 630 |
| 30 | 🇮🇩 ID | 509 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1339 |
| 2 | Tokyo International Airport |  | JP | 1108 |
| 3 | Denver International Airport |  | US | 1005 |
| 4 | Indira Gandhi International Airport |  | IN | 920 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 886 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 808 |
| 8 | Harry Reid International Airport |  | US | 765 |
| 9 | Frankfurt am Main International Airport |  | DE | 754 |
| 10 | Zurich Airport |  | CH | 721 |
| 11 | Macau International Airport |  | MO | 666 |
| 12 | La Aurora Airport |  | GT | 660 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 598 |
| 14 | Chicago O'Hare International Airport |  | US | 572 |
| 15 | Kuala Lumpur International Airport |  | MY | 561 |
| 16 | Madrid Barajas International Airport |  | ES | 556 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 554 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 534 |
| 19 | Bengaluru International Airport |  | IN | 523 |
| 20 | Malpensa International Airport |  | IT | 521 |
| 21 | Congonhas Airport |  | BR | 491 |
| 22 | Charlotte/Douglas International Airport |  | US | 478 |
| 23 | Salt Lake City International Airport |  | US | 468 |
| 24 | Capua Airport |  | IT | 467 |
| 25 | Charles de Gaulle International Airport |  | FR | 466 |
| 26 | Ninoy Aquino International Airport |  | PH | 465 |
| 27 | Tenerife Norte Airport |  | ES | 463 |
| 28 | Daniel K Inouye International Airport |  | US | 453 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 436 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 434 |
| 31 | Barcelona International Airport |  | ES | 410 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 403 |
| 33 | Vitoria/Foronda Airport |  | ES | 400 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 395 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 383 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 383 |
| 38 | Don Mueang International Airport |  | TH | 372 |
| 39 | Amsterdam Airport Schiphol |  | NL | 368 |
| 40 | Calgary International Airport |  | CA | 357 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 178 | 1h 27m | 910 km | 2,793.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 172 | 28m | 304 km | 901.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 147 | 19m | 165 km | 418.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 143 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 143 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 127 | 1h 12m | 770 km | 1,687.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 112 | 44m | 452 km | 872.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 101 | 31m | 369 km | 642.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 91 | 20m | 147 km | 230.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 90 | 28m | 152 km | 235.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 84 | 1h 42m | 1,156 km | 1,675.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 28 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 77 | 14m | 154 km | 204.0 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Langtang Airport (VNLT) | 2026-04-30 03:25 UTC | 2026-04-30 06:24 UTC | 2h 59m |
| GEC8460 | GEC | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-29 19:27 UTC | 2026-04-30 06:17 UTC | 10h 49m |
| LOT4YP | LOT Polish Airlines | Stockholm-Arlanda Airport (ESSA) | Khrabrovo Airport (UMKK) | 2026-04-30 05:45 UTC | 2026-04-30 06:16 UTC | 30m |
| HKC9486 | HKC | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-04-29 18:52 UTC | 2026-04-30 06:14 UTC | 11h 21m |
| ZJO | ZJO | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-04-30 05:33 UTC | 2026-04-30 06:11 UTC | 37m |
| YHU | YHU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-30 05:39 UTC | 2026-04-30 06:06 UTC | 27m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-04-30 05:16 UTC | 2026-04-30 05:49 UTC | 33m |
| FGEFJ | FGE | Montpellier Candillargues Airport (LFNG) | Montpellier Candillargues Airport (LFNG) | 2026-04-30 05:34 UTC | 2026-04-30 05:47 UTC | 13m |
| WIF7GT | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-04-30 05:28 UTC | 2026-04-30 05:46 UTC | 18m |
| AM345 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-04-30 05:16 UTC | 2026-04-30 05:43 UTC | 26m |
| BBC371 | BBC | VGZR (VGZR) | Langtang Airport (VNLT) | 2026-04-30 04:29 UTC | 2026-04-30 05:38 UTC | 1h 9m |
| AIQ3524 | AIQ | Don Mueang International Airport (VTBD) | Nakhon Ratchasima Airport (VTUQ) | 2026-04-30 05:14 UTC | 2026-04-30 05:35 UTC | 20m |
| VLG8RK | Vueling | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-04-30 05:01 UTC | 2026-04-30 05:32 UTC | 31m |
| N135DT |  | Nephi Municipal Airport (KU14) | KU42 (KU42) | 2026-04-30 05:13 UTC | 2026-04-30 05:31 UTC | 18m |
| AEE241 | AEE | Samos Airport (LGSM) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-30 04:50 UTC | 2026-04-30 05:31 UTC | 41m |
| ITY1278 | ITY | Napoli / Capodichino International Airport (LIRN) | Linate Airport (LIML) | 2026-04-30 04:29 UTC | 2026-04-30 05:30 UTC | 1h 0m |
| EWG7060 | EWG | Hamburg Airport (EDDH) | Dusseldorf International Airport (EDDL) | 2026-04-30 04:49 UTC | 2026-04-30 05:29 UTC | 40m |
| N6166U |  | Phoenix Goodyear Airport (KGYR) | AZ86 (AZ86) | 2026-04-30 04:46 UTC | 2026-04-30 05:29 UTC | 43m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-04-29 18:44 UTC | 2026-04-30 05:28 UTC | 10h 43m |
| AEE372 | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-30 04:52 UTC | 2026-04-30 05:24 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
