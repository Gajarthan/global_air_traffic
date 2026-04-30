# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_20:04:49_UTC-green)

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

**Latest saved flight:** 2026-04-30 20:04:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-30 20:04:49 UTC

- **60,954** saved flights
- **23,475** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **60,954** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **742,062.2 tonnes** estimated CO2 emissions
- **43,018,098 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2574 |
| 2 | SkyWest Airlines | 2271 |
| 3 | IndiGo | 1399 |
| 4 | EJA | 1092 |
| 5 | American Airlines | 951 |
| 6 | Southwest Airlines | 859 |
| 7 | Lufthansa | 779 |
| 8 | ENY | 751 |
| 9 | Vueling | 605 |
| 10 | AXM | 595 |
| 11 | LATAM Airlines | 579 |
| 12 | All Nippon Airways | 537 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 508 |
| 15 | AZU | 496 |
| 16 | Swiss International | 479 |
| 17 | QLK | 478 |
| 18 | LXJ | 434 |
| 19 | Alaska Airlines | 416 |
| 20 | AEE | 402 |
| 21 | easyJet | 400 |
| 22 | EJU | 391 |
| 23 | VIV | 383 |
| 24 | Cathay Pacific | 362 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 334 |
| 28 | AIQ | 311 |
| 29 | United Airlines | 302 |
| 30 | CXK | 300 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48154 |
| 2 | 🇪🇸 ES | 4422 |
| 3 | 🇮🇳 IN | 4416 |
| 4 | 🇦🇺 AU | 4149 |
| 5 | 🇧🇷 BR | 3457 |
| 6 | 🇩🇪 DE | 3398 |
| 7 | 🇮🇹 IT | 3337 |
| 8 | 🇯🇵 JP | 3315 |
| 9 | 🇨🇦 CA | 3004 |
| 10 | 🇨🇴 CO | 2623 |
| 11 | 🇬🇧 GB | 2594 |
| 12 | 🇫🇷 FR | 2407 |
| 13 | 🇲🇽 MX | 1908 |
| 14 | 🇬🇷 GR | 1815 |
| 15 | 🇨🇭 CH | 1710 |
| 16 | 🇳🇴 NO | 1696 |
| 17 | 🇲🇾 MY | 1447 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1139 |
| 20 | 🇹🇭 TH | 1103 |
| 21 | 🇹🇷 TR | 1085 |
| 22 | 🇵🇭 PH | 1023 |
| 23 | 🇵🇱 PL | 988 |
| 24 | 🇰🇷 KR | 985 |
| 25 | 🇬🇹 GT | 899 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 675 |
| 28 | 🇲🇪 ME | 668 |
| 29 | 🇳🇱 NL | 640 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1348 |
| 2 | Tokyo International Airport |  | JP | 1119 |
| 3 | Denver International Airport |  | US | 1012 |
| 4 | Indira Gandhi International Airport |  | IN | 931 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 893 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 818 |
| 8 | Frankfurt am Main International Airport |  | DE | 774 |
| 9 | Harry Reid International Airport |  | US | 772 |
| 10 | Zurich Airport |  | CH | 734 |
| 11 | Macau International Airport |  | MO | 675 |
| 12 | La Aurora Airport |  | GT | 675 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 603 |
| 14 | Chicago O'Hare International Airport |  | US | 576 |
| 15 | Madrid Barajas International Airport |  | ES | 571 |
| 16 | Kuala Lumpur International Airport |  | MY | 570 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 555 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 535 |
| 19 | Malpensa International Airport |  | IT | 530 |
| 20 | Bengaluru International Airport |  | IN | 530 |
| 21 | Congonhas Airport |  | BR | 499 |
| 22 | Charlotte/Douglas International Airport |  | US | 486 |
| 23 | Tenerife Norte Airport |  | ES | 474 |
| 24 | Charles de Gaulle International Airport |  | FR | 474 |
| 25 | Salt Lake City International Airport |  | US | 473 |
| 26 | Ninoy Aquino International Airport |  | PH | 468 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 454 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 443 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 436 |
| 31 | Barcelona International Airport |  | ES | 413 |
| 32 | Vitoria/Foronda Airport |  | ES | 410 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 406 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 401 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 385 |
| 37 | Reno/Tahoe International Airport |  | US | 384 |
| 38 | Don Mueang International Airport |  | TH | 379 |
| 39 | Amsterdam Airport Schiphol |  | NL | 375 |
| 40 | Calgary International Airport |  | CA | 358 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 335 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 203 | 21m | 244 km | 854.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 190 | 24m | 225 km | 737.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 179 | 1h 27m | 910 km | 2,808.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 150 | 19m | 165 km | 426.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 146 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 128 | 1h 12m | 770 km | 1,700.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 105 | 20m | 99 km | 179.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 102 | 31m | 369 km | 649.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 91 | 28m | 152 km | 237.8 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 85 | 1h 42m | 1,156 km | 1,695.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 1m | 695 km | 1,006.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 53m | 1,304 km | 1,844.8 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 81 | 23m | 55 km | 77.0 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 29 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 78 | 14m | 154 km | 206.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-04-30 19:52 UTC | 2026-04-30 20:04 UTC | 11m |
| N25221 |  | Roberts Field (KRDM) | Madras Municipal Airport (KS33) | 2026-04-30 19:26 UTC | 2026-04-30 20:02 UTC | 36m |
| N24336 |  | Felts Field (KSFF) | Felts Field (KSFF) | 2026-04-30 19:38 UTC | 2026-04-30 19:49 UTC | 10m |
| N39688 |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-04-30 18:52 UTC | 2026-04-30 19:48 UTC | 55m |
| BOE342 | BOE | Renton Municipal Airport (KRNT) | Odessa Municipal Airport (K43D) | 2026-04-30 18:11 UTC | 2026-04-30 19:46 UTC | 1h 35m |
| KING98 | KIN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-04-30 18:54 UTC | 2026-04-30 19:46 UTC | 52m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-30 19:27 UTC | 2026-04-30 19:45 UTC | 17m |
| OSU51 | OSU | Bolton Field (KTZR) | Ohio State University Airport (KOSU) | 2026-04-30 19:06 UTC | 2026-04-30 19:45 UTC | 39m |
| N64317 |  | Merrill Field (PAMR) | Skwentna Airport (PASW) | 2026-04-30 19:04 UTC | 2026-04-30 19:45 UTC | 40m |
| N425KD |  | Grand Junction Regional Airport (KGJT) | Santa Fe Regional Airport (KSAF) | 2026-04-30 18:42 UTC | 2026-04-30 19:43 UTC | 1h 1m |
| C6034 |  | Kodiak Airport (PADQ) | Kodiak Airport (PADQ) | 2026-04-30 18:32 UTC | 2026-04-30 19:43 UTC | 1h 11m |
| N4353L |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Kansas City/Lee's Summit Regional Airport (KLXT) | 2026-04-30 18:27 UTC | 2026-04-30 19:41 UTC | 1h 14m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-30 19:18 UTC | 2026-04-30 19:40 UTC | 22m |
| N359FA |  | New Castle Airport (KILG) | Paramount Air Airport (JY04) | 2026-04-30 19:11 UTC | 2026-04-30 19:40 UTC | 28m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-04-30 19:19 UTC | 2026-04-30 19:32 UTC | 13m |
| N497PJ |  | Tracy Municipal Airport (KTCY) | Byron Airport (KC83) | 2026-04-30 19:14 UTC | 2026-04-30 19:32 UTC | 17m |
| N38809 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-04-30 19:18 UTC | 2026-04-30 19:28 UTC | 10m |
| TGFSS | TGF | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-30 19:15 UTC | 2026-04-30 19:27 UTC | 11m |
| LTA905 | LTA | Tri-L Acres Airpark (1AL2) | Tri-L Acres Airpark (1AL2) | 2026-04-30 19:12 UTC | 2026-04-30 19:26 UTC | 13m |
| SNBD1 | SNB | Comox Airport (CYQQ) | Comox Airport (CYQQ) | 2026-04-30 19:09 UTC | 2026-04-30 19:24 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
