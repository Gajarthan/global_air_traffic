# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_18:08:08_UTC-green)

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

**Latest saved flight:** 2026-04-29 18:08:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 18:08:08 UTC

- **59,415** saved flights
- **23,017** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **59,415** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **721,063.1 tonnes** estimated CO2 emissions
- **41,800,761 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2528 |
| 2 | SkyWest Airlines | 2225 |
| 3 | IndiGo | 1362 |
| 4 | EJA | 1055 |
| 5 | American Airlines | 929 |
| 6 | Southwest Airlines | 844 |
| 7 | Lufthansa | 758 |
| 8 | ENY | 740 |
| 9 | Vueling | 594 |
| 10 | AXM | 580 |
| 11 | LATAM Airlines | 563 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 500 |
| 14 | Delta Air Lines | 494 |
| 15 | AZU | 488 |
| 16 | Swiss International | 471 |
| 17 | QLK | 463 |
| 18 | LXJ | 422 |
| 19 | Alaska Airlines | 405 |
| 20 | AEE | 397 |
| 21 | easyJet | 391 |
| 22 | EJU | 387 |
| 23 | VIV | 373 |
| 24 | Air France | 353 |
| 25 | Japan Airlines | 346 |
| 26 | Cathay Pacific | 340 |
| 27 | AXB | 327 |
| 28 | AIQ | 300 |
| 29 | JetBlue | 299 |
| 30 | CXK | 296 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46946 |
| 2 | 🇪🇸 ES | 4320 |
| 3 | 🇮🇳 IN | 4309 |
| 4 | 🇦🇺 AU | 4025 |
| 5 | 🇧🇷 BR | 3356 |
| 6 | 🇩🇪 DE | 3308 |
| 7 | 🇮🇹 IT | 3274 |
| 8 | 🇯🇵 JP | 3225 |
| 9 | 🇨🇦 CA | 2938 |
| 10 | 🇨🇴 CO | 2611 |
| 11 | 🇬🇧 GB | 2519 |
| 12 | 🇫🇷 FR | 2361 |
| 13 | 🇲🇽 MX | 1864 |
| 14 | 🇬🇷 GR | 1783 |
| 15 | 🇨🇭 CH | 1660 |
| 16 | 🇳🇴 NO | 1633 |
| 17 | 🇲🇾 MY | 1409 |
| 18 | 🇿🇦 ZA | 1210 |
| 19 | 🇳🇿 NZ | 1108 |
| 20 | 🇹🇭 TH | 1073 |
| 21 | 🇹🇷 TR | 1072 |
| 22 | 🇵🇭 PH | 1003 |
| 23 | 🇵🇱 PL | 964 |
| 24 | 🇰🇷 KR | 952 |
| 25 | 🇬🇹 GT | 867 |
| 26 | 🇲🇦 MA | 745 |
| 27 | 🇲🇪 ME | 644 |
| 28 | 🇲🇴 MO | 637 |
| 29 | 🇳🇱 NL | 629 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1327 |
| 2 | Tokyo International Airport |  | JP | 1096 |
| 3 | Denver International Airport |  | US | 991 |
| 4 | Indira Gandhi International Airport |  | IN | 906 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 879 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 807 |
| 8 | Harry Reid International Airport |  | US | 754 |
| 9 | Frankfurt am Main International Airport |  | DE | 748 |
| 10 | Zurich Airport |  | CH | 718 |
| 11 | La Aurora Airport |  | GT | 654 |
| 12 | Macau International Airport |  | MO | 637 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 586 |
| 14 | Chicago O'Hare International Airport |  | US | 566 |
| 15 | Kuala Lumpur International Airport |  | MY | 555 |
| 16 | Madrid Barajas International Airport |  | ES | 551 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 548 |
| 18 | Malpensa International Airport |  | IT | 519 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 20 | Bengaluru International Airport |  | IN | 515 |
| 21 | Congonhas Airport |  | BR | 483 |
| 22 | Charlotte/Douglas International Airport |  | US | 471 |
| 23 | Capua Airport |  | IT | 466 |
| 24 | Charles de Gaulle International Airport |  | FR | 465 |
| 25 | Tenerife Norte Airport |  | ES | 463 |
| 26 | Salt Lake City International Airport |  | US | 461 |
| 27 | Ninoy Aquino International Airport |  | PH | 460 |
| 28 | Daniel K Inouye International Airport |  | US | 446 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 430 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 31 | Barcelona International Airport |  | ES | 406 |
| 32 | Vitoria/Foronda Airport |  | ES | 398 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 397 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 391 |
| 35 | O. R. Tambo International Airport |  | ZA | 388 |
| 36 | Reno/Tahoe International Airport |  | US | 379 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 377 |
| 38 | Amsterdam Airport Schiphol |  | NL | 367 |
| 39 | Don Mueang International Airport |  | TH | 366 |
| 40 | Calgary International Airport |  | CA | 353 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 330 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 198 | 21m | 244 km | 833.7 t |
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
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 79 | 23m | 55 km | 75.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 78 | 1h 43m | 1,423 km | 1,914.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 77 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 75 | 14m | 154 km | 198.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BB028 |  | Stennis International Airport (KHSA) | Skywest Airpark (62AL) | 2026-04-29 17:41 UTC | 2026-04-29 18:08 UTC | 26m |
| N492DS |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-29 17:51 UTC | 2026-04-29 18:04 UTC | 13m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-29 17:47 UTC | 2026-04-29 18:03 UTC | 15m |
| N645PV |  | Redstone Army Air Field (KHUA) | Huntsville Executive Tom Sharp Jr Field (KMDQ) | 2026-04-29 17:11 UTC | 2026-04-29 17:57 UTC | 45m |
| JEDI41 | JED | Lakehurst Maxfield Field (KNEL) | Lakehurst Maxfield Field (KNEL) | 2026-04-29 17:38 UTC | 2026-04-29 17:48 UTC | 10m |
| RYR9658 | Ryanair | Reggio Calabria Airport (LICR) | Malpensa International Airport (LIMC) | 2026-04-29 16:15 UTC | 2026-04-29 17:46 UTC | 1h 31m |
| HTY254 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-29 17:16 UTC | 2026-04-29 17:46 UTC | 29m |
| CFYUL | CFY | Penticton Airport (CYYF) | Bow Island Airport (CEF3) | 2026-04-29 16:54 UTC | 2026-04-29 17:42 UTC | 47m |
| EAX7G | EAX | Sabadell Airport (LELL) | Sabadell Airport (LELL) | 2026-04-29 16:55 UTC | 2026-04-29 17:40 UTC | 45m |
| CXK397 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-29 17:07 UTC | 2026-04-29 17:40 UTC | 33m |
| DNC1JG | DNC | La Axarquia-Leoni Benabu Airport (LEAX) | Jayena Airport (LE84) | 2026-04-29 17:31 UTC | 2026-04-29 17:39 UTC | 7m |
| N615LF |  | Belle Plaine Municipal Airport (KTZT) | Iowa City Municipal Airport (KIOW) | 2026-04-29 17:22 UTC | 2026-04-29 17:39 UTC | 17m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-29 16:24 UTC | 2026-04-29 17:36 UTC | 1h 12m |
| N25995 |  | Addington Field (4TX8) | Lazy 9 Ranch Airport (TX64) | 2026-04-29 17:18 UTC | 2026-04-29 17:35 UTC | 17m |
| KING54 | KIN | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-04-29 17:01 UTC | 2026-04-29 17:35 UTC | 33m |
| PFA312 | PFA | Vero Beach Regional Airport (KVRB) | Marco Island Executive Airport (KMKY) | 2026-04-29 15:52 UTC | 2026-04-29 17:33 UTC | 1h 41m |
| CXK171 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-04-29 17:14 UTC | 2026-04-29 17:33 UTC | 18m |
| N965MS |  | Brackett Field (KPOC) | General Wm J Fox Airfield (KWJF) | 2026-04-29 16:54 UTC | 2026-04-29 17:33 UTC | 39m |
| EJA939 | EJA | John Wayne/Orange County Airport (KSNA) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-29 16:31 UTC | 2026-04-29 17:32 UTC | 1h 1m |
| THY6164 | Turkish Airlines | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-29 12:48 UTC | 2026-04-29 17:31 UTC | 4h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
