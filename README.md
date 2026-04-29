# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_20:57:15_UTC-green)

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

**Latest saved flight:** 2026-04-29 20:57:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 20:57:15 UTC

- **59,591** saved flights
- **23,083** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,591** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **723,383.1 tonnes** estimated CO2 emissions
- **41,935,250 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2544 |
| 2 | SkyWest Airlines | 2231 |
| 3 | IndiGo | 1362 |
| 4 | EJA | 1066 |
| 5 | American Airlines | 934 |
| 6 | Southwest Airlines | 847 |
| 7 | Lufthansa | 759 |
| 8 | ENY | 740 |
| 9 | Vueling | 595 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 566 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 500 |
| 14 | Delta Air Lines | 496 |
| 15 | AZU | 489 |
| 16 | Swiss International | 473 |
| 17 | QLK | 463 |
| 18 | LXJ | 425 |
| 19 | Alaska Airlines | 406 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 388 |
| 23 | VIV | 373 |
| 24 | Air France | 353 |
| 25 | Japan Airlines | 346 |
| 26 | Cathay Pacific | 343 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 300 |
| 30 | United Airlines | 298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 47172 |
| 2 | 🇪🇸 ES | 4332 |
| 3 | 🇮🇳 IN | 4311 |
| 4 | 🇦🇺 AU | 4029 |
| 5 | 🇧🇷 BR | 3366 |
| 6 | 🇩🇪 DE | 3311 |
| 7 | 🇮🇹 IT | 3287 |
| 8 | 🇯🇵 JP | 3225 |
| 9 | 🇨🇦 CA | 2951 |
| 10 | 🇨🇴 CO | 2611 |
| 11 | 🇬🇧 GB | 2522 |
| 12 | 🇫🇷 FR | 2365 |
| 13 | 🇲🇽 MX | 1865 |
| 14 | 🇬🇷 GR | 1784 |
| 15 | 🇨🇭 CH | 1664 |
| 16 | 🇳🇴 NO | 1633 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1108 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1072 |
| 22 | 🇵🇭 PH | 1003 |
| 23 | 🇵🇱 PL | 968 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 869 |
| 26 | 🇲🇦 MA | 747 |
| 27 | 🇲🇪 ME | 650 |
| 28 | 🇲🇴 MO | 639 |
| 29 | 🇳🇱 NL | 629 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1328 |
| 2 | Tokyo International Airport |  | JP | 1096 |
| 3 | Denver International Airport |  | US | 997 |
| 4 | Indira Gandhi International Airport |  | IN | 906 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 879 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 807 |
| 8 | Harry Reid International Airport |  | US | 757 |
| 9 | Frankfurt am Main International Airport |  | DE | 749 |
| 10 | Zurich Airport |  | CH | 720 |
| 11 | La Aurora Airport |  | GT | 655 |
| 12 | Macau International Airport |  | MO | 639 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 590 |
| 14 | Chicago O'Hare International Airport |  | US | 567 |
| 15 | Kuala Lumpur International Airport |  | MY | 555 |
| 16 | Madrid Barajas International Airport |  | ES | 553 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 550 |
| 18 | Malpensa International Airport |  | IT | 520 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 484 |
| 22 | Charlotte/Douglas International Airport |  | US | 474 |
| 23 | Capua Airport |  | IT | 466 |
| 24 | Charles de Gaulle International Airport |  | FR | 465 |
| 25 | Tenerife Norte Airport |  | ES | 463 |
| 26 | Salt Lake City International Airport |  | US | 462 |
| 27 | Ninoy Aquino International Airport |  | PH | 460 |
| 28 | Daniel K Inouye International Airport |  | US | 447 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 431 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 31 | Barcelona International Airport |  | ES | 407 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 399 |
| 33 | Vitoria/Foronda Airport |  | ES | 399 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 393 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 382 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 378 |
| 38 | Amsterdam Airport Schiphol |  | NL | 367 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 354 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 199 | 21m | 244 km | 837.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 176 | 1h 27m | 910 km | 2,761.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 168 | 28m | 304 km | 880.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 146 | 19m | 165 km | 415.3 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 142 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 134 | 26m | 275 km | 635.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 126 | 1h 12m | 770 km | 1,673.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 99 | 31m | 369 km | 630.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 98 | 27m | 215 km | 363.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 90 | 20m | 147 km | 227.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 89 | 28m | 152 km | 232.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 83 | 1h 43m | 1,156 km | 1,655.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 83 | 57m | 493 km | 706.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 80 | 23m | 55 km | 76.0 t |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 78 | 1h 43m | 1,423 km | 1,914.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 75 | 14m | 154 km | 198.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| URSA02 | URS | Gold King Creek Airport (PAAN) | Ladd Army Air Field (PAFB) | 2026-04-29 20:33 UTC | 2026-04-29 20:57 UTC | 23m |
| CPA040 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-04-29 16:03 UTC | 2026-04-29 20:52 UTC | 4h 48m |
| ATG7720 | ATG | Budapest Ferenc Liszt International Airport (LHBP) | Zhuhai Airport (ZGSD) | 2026-04-29 08:41 UTC | 2026-04-29 20:49 UTC | 12h 7m |
| N288ME |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-04-29 20:32 UTC | 2026-04-29 20:44 UTC | 12m |
| BPX298 | BPX | KXFL (KXFL) | KXFL (KXFL) | 2026-04-29 20:23 UTC | 2026-04-29 20:43 UTC | 19m |
| PDU66 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-29 19:52 UTC | 2026-04-29 20:43 UTC | 50m |
| EJA675 | EJA | Centennial Airport (KAPA) | Rocky Mountain Metro Airport (KBJC) | 2026-04-29 20:18 UTC | 2026-04-29 20:41 UTC | 23m |
| N151RG |  | K5T6 (K5T6) | Wilkeys Airport (TA50) | 2026-04-29 20:17 UTC | 2026-04-29 20:35 UTC | 18m |
| N567DF |  | Redding Regional Airport (KRDD) | Lake California Air Park (68CA) | 2026-04-29 20:22 UTC | 2026-04-29 20:32 UTC | 10m |
| N460LD |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-29 20:14 UTC | 2026-04-29 20:31 UTC | 16m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-29 06:07 UTC | 2026-04-29 20:29 UTC | 14h 21m |
| N894JH |  | KU42 (KU42) | Northern Colorado Regional Airport (KFNL) | 2026-04-29 19:34 UTC | 2026-04-29 20:29 UTC | 54m |
| N2326B |  | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-29 19:18 UTC | 2026-04-29 20:28 UTC | 1h 9m |
| COS148 | COS | La Esperanza Airport (MNEP) | El Bluff Airport (MNFF) | 2026-04-29 20:16 UTC | 2026-04-29 20:27 UTC | 10m |
| RGA16 | RGA | Zweisimmen Airport (LSTZ) | Zweisimmen Airport (LSTZ) | 2026-04-29 19:40 UTC | 2026-04-29 20:25 UTC | 45m |
| SCU7 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-04-29 20:09 UTC | 2026-04-29 20:25 UTC | 15m |
| N206SG |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-04-29 20:13 UTC | 2026-04-29 20:24 UTC | 11m |
| RYR1HK | Ryanair | Madrid Barajas International Airport (LEMD) | Malpensa International Airport (LIMC) | 2026-04-29 18:38 UTC | 2026-04-29 20:20 UTC | 1h 42m |
| N7165G |  | Ramona Airport (KRNM) | Ramona Airport (KRNM) | 2026-04-29 20:07 UTC | 2026-04-29 20:19 UTC | 11m |
| BUTET46 | BUT | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-29 19:28 UTC | 2026-04-29 20:18 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
