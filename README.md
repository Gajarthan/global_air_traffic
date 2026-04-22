# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_10:48:51_UTC-green)

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

**Latest saved flight:** 2026-04-22 10:48:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 10:48:51 UTC

- **47,729** saved flights
- **19,447** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,729** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **573,951.9 tonnes** estimated CO2 emissions
- **33,272,572 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2027 |
| 2 | SkyWest Airlines | 1846 |
| 3 | IndiGo | 1126 |
| 4 | EJA | 819 |
| 5 | American Airlines | 790 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 620 |
| 8 | Lufthansa | 518 |
| 9 | AXM | 480 |
| 10 | Vueling | 476 |
| 11 | LATAM Airlines | 467 |
| 12 | All Nippon Airways | 435 |
| 13 | AZU | 408 |
| 14 | Delta Air Lines | 396 |
| 15 | QLK | 386 |
| 16 | WIF | 383 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 364 |
| 19 | AEE | 323 |
| 20 | Alaska Airlines | 323 |
| 21 | EJU | 316 |
| 22 | easyJet | 304 |
| 23 | VIV | 304 |
| 24 | Japan Airlines | 288 |
| 25 | Air France | 269 |
| 26 | Cathay Pacific | 259 |
| 27 | AXB | 252 |
| 28 | JetBlue | 252 |
| 29 | United Airlines | 251 |
| 30 | AIQ | 241 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37905 |
| 2 | 🇮🇳 IN | 3501 |
| 3 | 🇪🇸 ES | 3456 |
| 4 | 🇦🇺 AU | 3311 |
| 5 | 🇧🇷 BR | 2793 |
| 6 | 🇯🇵 JP | 2629 |
| 7 | 🇮🇹 IT | 2593 |
| 8 | 🇩🇪 DE | 2486 |
| 9 | 🇨🇦 CA | 2339 |
| 10 | 🇨🇴 CO | 2210 |
| 11 | 🇬🇧 GB | 1950 |
| 12 | 🇫🇷 FR | 1818 |
| 13 | 🇲🇽 MX | 1479 |
| 14 | 🇬🇷 GR | 1458 |
| 15 | 🇨🇭 CH | 1306 |
| 16 | 🇳🇴 NO | 1230 |
| 17 | 🇲🇾 MY | 1169 |
| 18 | 🇿🇦 ZA | 984 |
| 19 | 🇳🇿 NZ | 922 |
| 20 | 🇹🇭 TH | 858 |
| 21 | 🇵🇭 PH | 839 |
| 22 | 🇹🇷 TR | 836 |
| 23 | 🇰🇷 KR | 782 |
| 24 | 🇵🇱 PL | 752 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 589 |
| 27 | 🇲🇪 ME | 511 |
| 28 | 🇳🇱 NL | 487 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1123 |
| 2 | Tokyo International Airport |  | JP | 894 |
| 3 | Denver International Airport |  | US | 795 |
| 4 | El Dorado International Airport |  | CO | 769 |
| 5 | Indira Gandhi International Airport |  | IN | 743 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 723 |
| 7 | Guaymaral Airport |  | CO | 618 |
| 8 | Harry Reid International Airport |  | US | 618 |
| 9 | Zurich Airport |  | CH | 563 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 491 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Kuala Lumpur International Airport |  | MY | 468 |
| 14 | Chicago O'Hare International Airport |  | US | 467 |
| 15 | Macau International Airport |  | MO | 454 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 439 |
| 18 | Bengaluru International Airport |  | IN | 423 |
| 19 | Madrid Barajas International Airport |  | ES | 421 |
| 20 | Charlotte/Douglas International Airport |  | US | 408 |
| 21 | Malpensa International Airport |  | IT | 402 |
| 22 | Tenerife Norte Airport |  | ES | 399 |
| 23 | Congonhas Airport |  | BR | 399 |
| 24 | Ninoy Aquino International Airport |  | PH | 388 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 362 |
| 26 | Salt Lake City International Airport |  | US | 359 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 354 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 350 |
| 31 | Reno/Tahoe International Airport |  | US | 329 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 328 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 324 |
| 34 | Vitoria/Foronda Airport |  | ES | 321 |
| 35 | O. R. Tambo International Airport |  | ZA | 318 |
| 36 | Barcelona International Airport |  | ES | 316 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 313 |
| 38 | Don Mueang International Airport |  | TH | 289 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 283 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 247 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 226 | 1h 7m | 706 km | 2,751.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 182 | 14m | 114 km | 357.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 142 | 28m | 304 km | 744.4 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 138 | 1h 27m | 910 km | 2,165.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 127 | 19m | 165 km | 361.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 98 | 44m | 452 km | 763.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 80 | 20m | 250 km | 345.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 77 | 20m | 147 km | 194.9 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 74 | 26m | 215 km | 274.1 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 67 | 1h 0m | 695 km | 803.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UPS844 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Salt Lake City International Airport (KSLC) | 2026-04-22 07:49 UTC | 2026-04-22 10:48 UTC | 2h 59m |
| VALK | VAL | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-04-22 08:53 UTC | 2026-04-22 10:42 UTC | 1h 49m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-22 07:50 UTC | 2026-04-22 10:39 UTC | 2h 48m |
| EWG1GC | EWG | Francisco de Sá Carneiro Airport (LPPR) | Hamburg Airport (EDDH) | 2026-04-22 07:59 UTC | 2026-04-22 10:37 UTC | 2h 37m |
| ZKIWD | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-22 10:12 UTC | 2026-04-22 10:26 UTC | 13m |
| RNA434 | RNA | Narita International Airport (RJAA) | Simara Airport (VNSI) | 2026-04-22 02:11 UTC | 2026-04-22 10:23 UTC | 8h 11m |
| UFX64 | UFX | RAF Woodvale (EGOW) | Blackpool International Airport (EGNH) | 2026-04-22 10:09 UTC | 2026-04-22 10:21 UTC | 11m |
| SKQ78 | SKQ | Burlington/Alamance Regional Airport (KBUY) | West Virginia International Yeager Airport (KCRW) | 2026-04-22 09:29 UTC | 2026-04-22 10:17 UTC | 48m |
| FHADE | FHA | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Megeve Airport (LFHM) | 2026-04-22 10:05 UTC | 2026-04-22 10:13 UTC | 7m |
| IGO7126 | IndiGo | Chhatrapati Shivaji International Airport (VABB) | Mysore Airport (VOMY) | 2026-04-22 05:11 UTC | 2026-04-22 10:04 UTC | 4h 53m |
| DLH1KK | Lufthansa | Munich International Airport (EDDM) | Napoli / Capodichino International Airport (LIRN) | 2026-04-22 08:47 UTC | 2026-04-22 09:59 UTC | 1h 12m |
| NOZ372 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-04-22 08:27 UTC | 2026-04-22 09:58 UTC | 1h 31m |
| AIQ3207 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-04-22 09:02 UTC | 2026-04-22 09:53 UTC | 50m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-22 09:31 UTC | 2026-04-22 09:53 UTC | 21m |
| DLH053 | Lufthansa | Bremen Airport (EDDW) | Frankfurt am Main International Airport (EDDF) | 2026-04-22 09:03 UTC | 2026-04-22 09:49 UTC | 46m |
| UPS1468 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Bowlin Airport (IN85) | 2026-04-22 09:16 UTC | 2026-04-22 09:47 UTC | 31m |
| AXM5194 | AXM | Kuala Lumpur International Airport (WMKK) | Telupid Airport (WBKE) | 2026-04-22 07:35 UTC | 2026-04-22 09:45 UTC | 2h 10m |
| RYR798V | Ryanair | Munster Osnabruck Airport (EDDG) | Palma De Mallorca Airport (LEPA) | 2026-04-22 07:47 UTC | 2026-04-22 09:45 UTC | 1h 58m |
| AZU2797 | AZU | Viracopos International Airport (SBKP) | Ubatuba Airport (SDUB) | 2026-04-22 09:24 UTC | 2026-04-22 09:44 UTC | 20m |
| IGO273W | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lengpui Airport (VELP) | 2026-04-22 08:56 UTC | 2026-04-22 09:44 UTC | 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
