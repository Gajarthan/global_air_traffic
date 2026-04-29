# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_04:32:51_UTC-green)

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

**Latest saved flight:** 2026-04-29 04:32:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 04:32:51 UTC

- **58,674** saved flights
- **22,824** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,674** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **712,640.7 tonnes** estimated CO2 emissions
- **41,312,506 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2487 |
| 2 | SkyWest Airlines | 2204 |
| 3 | IndiGo | 1339 |
| 4 | EJA | 1039 |
| 5 | American Airlines | 924 |
| 6 | Southwest Airlines | 839 |
| 7 | Lufthansa | 742 |
| 8 | ENY | 732 |
| 9 | Vueling | 582 |
| 10 | AXM | 574 |
| 11 | LATAM Airlines | 556 |
| 12 | All Nippon Airways | 521 |
| 13 | WIF | 489 |
| 14 | Delta Air Lines | 487 |
| 15 | AZU | 486 |
| 16 | Swiss International | 464 |
| 17 | QLK | 460 |
| 18 | LXJ | 416 |
| 19 | Alaska Airlines | 401 |
| 20 | AEE | 388 |
| 21 | easyJet | 384 |
| 22 | EJU | 379 |
| 23 | VIV | 372 |
| 24 | Air France | 342 |
| 25 | Japan Airlines | 340 |
| 26 | Cathay Pacific | 339 |
| 27 | AXB | 321 |
| 28 | AIQ | 296 |
| 29 | JetBlue | 295 |
| 30 | United Airlines | 295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46496 |
| 2 | 🇪🇸 ES | 4259 |
| 3 | 🇮🇳 IN | 4219 |
| 4 | 🇦🇺 AU | 3987 |
| 5 | 🇧🇷 BR | 3323 |
| 6 | 🇩🇪 DE | 3234 |
| 7 | 🇮🇹 IT | 3201 |
| 8 | 🇯🇵 JP | 3174 |
| 9 | 🇨🇦 CA | 2904 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2480 |
| 12 | 🇫🇷 FR | 2317 |
| 13 | 🇲🇽 MX | 1854 |
| 14 | 🇬🇷 GR | 1741 |
| 15 | 🇨🇭 CH | 1642 |
| 16 | 🇳🇴 NO | 1592 |
| 17 | 🇲🇾 MY | 1391 |
| 18 | 🇿🇦 ZA | 1192 |
| 19 | 🇳🇿 NZ | 1106 |
| 20 | 🇹🇷 TR | 1063 |
| 21 | 🇹🇭 TH | 1058 |
| 22 | 🇵🇭 PH | 990 |
| 23 | 🇵🇱 PL | 943 |
| 24 | 🇰🇷 KR | 929 |
| 25 | 🇬🇹 GT | 860 |
| 26 | 🇲🇦 MA | 740 |
| 27 | 🇲🇪 ME | 635 |
| 28 | 🇲🇴 MO | 631 |
| 29 | 🇳🇱 NL | 611 |
| 30 | 🇮🇩 ID | 503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1321 |
| 2 | Tokyo International Airport |  | JP | 1079 |
| 3 | Denver International Airport |  | US | 982 |
| 4 | Indira Gandhi International Airport |  | IN | 886 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 857 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 748 |
| 9 | Frankfurt am Main International Airport |  | DE | 733 |
| 10 | Zurich Airport |  | CH | 706 |
| 11 | La Aurora Airport |  | GT | 649 |
| 12 | Macau International Airport |  | MO | 631 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 581 |
| 14 | Chicago O'Hare International Airport |  | US | 560 |
| 15 | Kuala Lumpur International Airport |  | MY | 548 |
| 16 | Madrid Barajas International Airport |  | ES | 545 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 543 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 517 |
| 19 | Bengaluru International Airport |  | IN | 507 |
| 20 | Malpensa International Airport |  | IT | 506 |
| 21 | Congonhas Airport |  | BR | 479 |
| 22 | Charlotte/Douglas International Airport |  | US | 468 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 456 |
| 25 | Salt Lake City International Airport |  | US | 454 |
| 26 | Charles de Gaulle International Airport |  | FR | 453 |
| 27 | Capua Airport |  | IT | 444 |
| 28 | Daniel K Inouye International Airport |  | US | 438 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 421 |
| 31 | Barcelona International Airport |  | ES | 396 |
| 32 | Vitoria/Foronda Airport |  | ES | 396 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 390 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 386 |
| 35 | O. R. Tambo International Airport |  | ZA | 380 |
| 36 | Reno/Tahoe International Airport |  | US | 376 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 372 |
| 38 | Don Mueang International Airport |  | TH | 360 |
| 39 | Amsterdam Airport Schiphol |  | NL | 354 |
| 40 | Calgary International Airport |  | CA | 347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 192 | 21m | 244 km | 808.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 185 | 24m | 225 km | 717.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 172 | 1h 27m | 910 km | 2,699.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 121 | 1h 12m | 770 km | 1,607.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 94 | 20m | 250 km | 406.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N54715 |  | Blue Ribbon Airport (WN29) | William R Fairchild International Airport (KCLM) | 2026-04-29 04:21 UTC | 2026-04-29 04:32 UTC | 11m |
| TAY401 | TAY | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-28 12:06 UTC | 2026-04-29 04:27 UTC | 16h 21m |
| ELY2371 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-04-29 03:50 UTC | 2026-04-29 04:23 UTC | 32m |
| VAIL51 | VAI | Harrington Ranch Airport (CO02) | Buckley Space Force Base Airport (KBKF) | 2026-04-29 04:08 UTC | 2026-04-29 04:19 UTC | 11m |
| LBQ865 | LBQ | Tallahassee International Airport (KTLH) | Tampa Executive Airport (KVDF) | 2026-04-29 03:33 UTC | 2026-04-29 04:17 UTC | 44m |
| MAZER62 | MAZ | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-29 02:30 UTC | 2026-04-29 04:17 UTC | 1h 47m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-29 03:45 UTC | 2026-04-29 04:17 UTC | 31m |
| MAZER61 | MAZ | City Of Colorado Springs Municipal Airport (KCOS) | Perry Park Airport (CO93) | 2026-04-29 03:43 UTC | 2026-04-29 03:57 UTC | 13m |
| TEX05 | TEX | Tauranga Airport (NZTG) | Feilding Airport (NZFI) | 2026-04-29 02:41 UTC | 2026-04-29 03:54 UTC | 1h 12m |
|  |  | South Haven Area Regional Airport (KLWA) | South Haven Area Regional Airport (KLWA) | 2026-04-29 03:42 UTC | 2026-04-29 03:53 UTC | 10m |
| N586FD |  | Kissimmee Gateway Airport (KISM) | Marksville Municipal Airport (KMKV) | 2026-04-29 02:00 UTC | 2026-04-29 03:51 UTC | 1h 50m |
| N8GU |  | Daniel Field (KDNL) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-29 03:20 UTC | 2026-04-29 03:48 UTC | 27m |
| AAL1275 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Albuquerque International Sunport Airport (KABQ) | 2026-04-29 00:04 UTC | 2026-04-29 03:45 UTC | 3h 40m |
| N856MB |  | Sanctuary Ranch Airport (7TS4) | XA10 (XA10) | 2026-04-29 03:41 UTC | 2026-04-29 03:43 UTC | 1m |
| ANA535 | All Nippon Airways | Tokyo International Airport (RJTT) | Takamatsu Airport (RJOT) | 2026-04-29 02:53 UTC | 2026-04-29 03:42 UTC | 49m |
| UPS921 | UPS | San Diego International Airport (KSAN) | Willow Valley Airport (45AZ) | 2026-04-29 02:49 UTC | 2026-04-29 03:41 UTC | 52m |
| N863MH |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-04-29 03:31 UTC | 2026-04-29 03:39 UTC | 8m |
| QLK1504 | QLK | Cape Barren Island Airport (YCBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-29 02:26 UTC | 2026-04-29 03:36 UTC | 1h 9m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-29 03:10 UTC | 2026-04-29 03:35 UTC | 24m |
| N139HN |  | Logan County Airport (K6L4) | West Virginia International Yeager Airport (KCRW) | 2026-04-29 03:13 UTC | 2026-04-29 03:32 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
