# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_00:55:01_UTC-green)

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

**Latest saved flight:** 2026-05-01 00:55:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 00:55:01 UTC

- **61,547** saved flights
- **23,691** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,547** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **749,640.0 tonnes** estimated CO2 emissions
- **43,457,390 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2582 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1401 |
| 4 | EJA | 1117 |
| 5 | American Airlines | 962 |
| 6 | Southwest Airlines | 875 |
| 7 | Lufthansa | 779 |
| 8 | ENY | 765 |
| 9 | Vueling | 607 |
| 10 | AXM | 598 |
| 11 | LATAM Airlines | 585 |
| 12 | All Nippon Airways | 538 |
| 13 | WIF | 518 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 502 |
| 16 | QLK | 487 |
| 17 | Swiss International | 479 |
| 18 | LXJ | 439 |
| 19 | Alaska Airlines | 423 |
| 20 | AEE | 403 |
| 21 | easyJet | 400 |
| 22 | EJU | 394 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 372 |
| 25 | Air France | 358 |
| 26 | Japan Airlines | 355 |
| 27 | AXB | 335 |
| 28 | AIQ | 311 |
| 29 | CXK | 305 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48879 |
| 2 | 🇪🇸 ES | 4430 |
| 3 | 🇮🇳 IN | 4424 |
| 4 | 🇦🇺 AU | 4215 |
| 5 | 🇧🇷 BR | 3493 |
| 6 | 🇩🇪 DE | 3403 |
| 7 | 🇮🇹 IT | 3345 |
| 8 | 🇯🇵 JP | 3330 |
| 9 | 🇨🇦 CA | 3049 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2602 |
| 12 | 🇫🇷 FR | 2410 |
| 13 | 🇲🇽 MX | 1946 |
| 14 | 🇬🇷 GR | 1821 |
| 15 | 🇨🇭 CH | 1711 |
| 16 | 🇳🇴 NO | 1696 |
| 17 | 🇲🇾 MY | 1455 |
| 18 | 🇿🇦 ZA | 1247 |
| 19 | 🇳🇿 NZ | 1165 |
| 20 | 🇹🇭 TH | 1104 |
| 21 | 🇹🇷 TR | 1091 |
| 22 | 🇵🇭 PH | 1037 |
| 23 | 🇵🇱 PL | 989 |
| 24 | 🇰🇷 KR | 987 |
| 25 | 🇬🇹 GT | 922 |
| 26 | 🇲🇦 MA | 758 |
| 27 | 🇲🇴 MO | 687 |
| 28 | 🇲🇪 ME | 670 |
| 29 | 🇳🇱 NL | 644 |
| 30 | 🇮🇩 ID | 518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1367 |
| 2 | Tokyo International Airport |  | JP | 1123 |
| 3 | Denver International Airport |  | US | 1023 |
| 4 | Indira Gandhi International Airport |  | IN | 935 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 895 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 786 |
| 9 | Frankfurt am Main International Airport |  | DE | 774 |
| 10 | Zurich Airport |  | CH | 734 |
| 11 | La Aurora Airport |  | GT | 691 |
| 12 | Macau International Airport |  | MO | 687 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Chicago O'Hare International Airport |  | US | 583 |
| 15 | Kuala Lumpur International Airport |  | MY | 574 |
| 16 | Madrid Barajas International Airport |  | ES | 572 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 563 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 544 |
| 19 | Malpensa International Airport |  | IT | 532 |
| 20 | Bengaluru International Airport |  | IN | 530 |
| 21 | Congonhas Airport |  | BR | 504 |
| 22 | Charlotte/Douglas International Airport |  | US | 491 |
| 23 | Salt Lake City International Airport |  | US | 484 |
| 24 | Charles de Gaulle International Airport |  | FR | 476 |
| 25 | Tenerife Norte Airport |  | ES | 474 |
| 26 | Ninoy Aquino International Airport |  | PH | 473 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 458 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 446 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 444 |
| 31 | Barcelona International Airport |  | ES | 413 |
| 32 | Vitoria/Foronda Airport |  | ES | 411 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 409 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 401 |
| 35 | O. R. Tambo International Airport |  | ZA | 393 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 389 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Amsterdam Airport Schiphol |  | NL | 379 |
| 39 | Don Mueang International Airport |  | TH | 379 |
| 40 | Calgary International Airport |  | CA | 365 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 337 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 206 | 21m | 244 km | 867.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 192 | 24m | 225 km | 744.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 180 | 1h 27m | 910 km | 2,824.6 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 174 | 28m | 304 km | 912.2 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 151 | 19m | 165 km | 429.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 148 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 145 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 138 | 26m | 275 km | 653.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 129 | 1h 12m | 770 km | 1,713.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 114 | 44m | 452 km | 888.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 104 | 31m | 369 km | 662.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 96 | 20m | 250 km | 414.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 80 | 14m | 154 km | 212.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N611MV |  | Redding Regional Airport (KRDD) | Sierraville Dearwater Airport (KO79) | 2026-05-01 00:27 UTC | 2026-05-01 00:55 UTC | 27m |
| CLX4M | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-04-30 09:30 UTC | 2026-05-01 00:51 UTC | 15h 20m |
| N303RH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-30 23:42 UTC | 2026-05-01 00:47 UTC | 1h 5m |
| TAY401 | TAY | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-30 08:30 UTC | 2026-05-01 00:47 UTC | 16h 17m |
| N205NB |  | Thunder Ridge Airpark (UT83) | KU42 (KU42) | 2026-05-01 00:10 UTC | 2026-05-01 00:45 UTC | 35m |
| SFJ21 | SFJ | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-05-01 00:00 UTC | 2026-05-01 00:45 UTC | 45m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-05-01 00:28 UTC | 2026-05-01 00:43 UTC | 15m |
| APJ304 | APJ | Narita International Airport (RJAA) | Kansai International Airport (RJBB) | 2026-04-30 23:52 UTC | 2026-05-01 00:41 UTC | 49m |
| SCA43 | SCA | Chandler Municipal Airport (KCHD) | Payson Airport (KPAN) | 2026-04-30 23:47 UTC | 2026-05-01 00:40 UTC | 53m |
| CGSSC | CGS | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-05-01 00:09 UTC | 2026-05-01 00:39 UTC | 30m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-01 00:19 UTC | 2026-05-01 00:39 UTC | 20m |
| LXJ361 | LXJ | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Hayward Executive Airport (KHWD) | 2026-04-30 23:41 UTC | 2026-05-01 00:38 UTC | 56m |
| MPH9441 | MPH | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-30 13:29 UTC | 2026-05-01 00:35 UTC | 11h 6m |
| LXJ317 | LXJ | Teterboro Airport (KTEB) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-30 22:58 UTC | 2026-05-01 00:32 UTC | 1h 34m |
| N3126E |  | Massengill Airport (7OI9) | Ohio State University Airport (KOSU) | 2026-04-30 23:36 UTC | 2026-05-01 00:31 UTC | 55m |
| SHERPA7 | SHE | Breezy Knoll Airport (0FD5) | Duke Field,(Eglin Af Aux Nr 3) Airport (KEGI) | 2026-05-01 00:18 UTC | 2026-05-01 00:30 UTC | 12m |
| CWA926 | CWA | Edmonton International Airport (CYEG) | Grande Prairie Airport (CYQU) | 2026-04-30 20:02 UTC | 2026-05-01 00:28 UTC | 4h 25m |
| RGY923 | RGY | Scottsdale Airport (KSDL) | Sequoia Field (KD86) | 2026-04-30 23:14 UTC | 2026-05-01 00:27 UTC | 1h 13m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-30 23:52 UTC | 2026-05-01 00:25 UTC | 32m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-01 00:05 UTC | 2026-05-01 00:24 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
