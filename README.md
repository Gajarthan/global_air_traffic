# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_23:28:20_UTC-green)

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

**Latest saved flight:** 2026-04-28 23:28:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 23:28:20 UTC

- **58,595** saved flights
- **22,805** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,595** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **711,602.4 tonnes** estimated CO2 emissions
- **41,252,316 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2487 |
| 2 | SkyWest Airlines | 2204 |
| 3 | IndiGo | 1337 |
| 4 | EJA | 1038 |
| 5 | American Airlines | 923 |
| 6 | Southwest Airlines | 839 |
| 7 | Lufthansa | 742 |
| 8 | ENY | 732 |
| 9 | Vueling | 582 |
| 10 | AXM | 570 |
| 11 | LATAM Airlines | 556 |
| 12 | All Nippon Airways | 517 |
| 13 | WIF | 489 |
| 14 | AZU | 486 |
| 15 | Delta Air Lines | 486 |
| 16 | Swiss International | 464 |
| 17 | QLK | 456 |
| 18 | LXJ | 416 |
| 19 | Alaska Airlines | 399 |
| 20 | AEE | 388 |
| 21 | easyJet | 384 |
| 22 | EJU | 379 |
| 23 | VIV | 372 |
| 24 | Air France | 342 |
| 25 | Cathay Pacific | 339 |
| 26 | Japan Airlines | 338 |
| 27 | AXB | 319 |
| 28 | AIQ | 295 |
| 29 | JetBlue | 295 |
| 30 | United Airlines | 295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46440 |
| 2 | 🇪🇸 ES | 4258 |
| 3 | 🇮🇳 IN | 4207 |
| 4 | 🇦🇺 AU | 3967 |
| 5 | 🇧🇷 BR | 3323 |
| 6 | 🇩🇪 DE | 3233 |
| 7 | 🇮🇹 IT | 3201 |
| 8 | 🇯🇵 JP | 3157 |
| 9 | 🇨🇦 CA | 2903 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2480 |
| 12 | 🇫🇷 FR | 2317 |
| 13 | 🇲🇽 MX | 1850 |
| 14 | 🇬🇷 GR | 1741 |
| 15 | 🇨🇭 CH | 1642 |
| 16 | 🇳🇴 NO | 1591 |
| 17 | 🇲🇾 MY | 1382 |
| 18 | 🇿🇦 ZA | 1192 |
| 19 | 🇳🇿 NZ | 1100 |
| 20 | 🇹🇷 TR | 1061 |
| 21 | 🇹🇭 TH | 1057 |
| 22 | 🇵🇭 PH | 986 |
| 23 | 🇵🇱 PL | 943 |
| 24 | 🇰🇷 KR | 928 |
| 25 | 🇬🇹 GT | 858 |
| 26 | 🇲🇦 MA | 740 |
| 27 | 🇲🇪 ME | 635 |
| 28 | 🇲🇴 MO | 630 |
| 29 | 🇳🇱 NL | 611 |
| 30 | 🇮🇩 ID | 502 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1321 |
| 2 | Tokyo International Airport |  | JP | 1073 |
| 3 | Denver International Airport |  | US | 981 |
| 4 | Indira Gandhi International Airport |  | IN | 885 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 857 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 746 |
| 9 | Frankfurt am Main International Airport |  | DE | 733 |
| 10 | Zurich Airport |  | CH | 706 |
| 11 | La Aurora Airport |  | GT | 648 |
| 12 | Macau International Airport |  | MO | 630 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 581 |
| 14 | Chicago O'Hare International Airport |  | US | 560 |
| 15 | Madrid Barajas International Airport |  | ES | 545 |
| 16 | Kuala Lumpur International Airport |  | MY | 545 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 541 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 514 |
| 19 | Malpensa International Airport |  | IT | 506 |
| 20 | Bengaluru International Airport |  | IN | 504 |
| 21 | Congonhas Airport |  | BR | 479 |
| 22 | Charlotte/Douglas International Airport |  | US | 467 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Salt Lake City International Airport |  | US | 454 |
| 25 | Ninoy Aquino International Airport |  | PH | 454 |
| 26 | Charles de Gaulle International Airport |  | FR | 453 |
| 27 | Capua Airport |  | IT | 444 |
| 28 | Daniel K Inouye International Airport |  | US | 436 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 428 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 419 |
| 31 | Barcelona International Airport |  | ES | 396 |
| 32 | Vitoria/Foronda Airport |  | ES | 395 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 390 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 386 |
| 35 | O. R. Tambo International Airport |  | ZA | 380 |
| 36 | Reno/Tahoe International Airport |  | US | 376 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 372 |
| 38 | Don Mueang International Airport |  | TH | 359 |
| 39 | Amsterdam Airport Schiphol |  | NL | 354 |
| 40 | Calgary International Airport |  | CA | 347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 191 | 21m | 244 km | 804.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 184 | 24m | 225 km | 713.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 171 | 1h 27m | 910 km | 2,683.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 120 | 1h 12m | 770 km | 1,594.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
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
| N271MA |  | Dodge County Airport (KUNU) | Watertown Municipal Airport (KRYV) | 2026-04-28 23:16 UTC | 2026-04-28 23:28 UTC | 11m |
| ZDO | ZDO | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-04-28 22:53 UTC | 2026-04-28 23:14 UTC | 21m |
| N331NG |  | Dekalb-Peachtree Airport (KPDK) | Capital City Airport (KCXY) | 2026-04-28 21:02 UTC | 2026-04-28 23:13 UTC | 2h 11m |
| FRG2 | FRG | General Mitchell International Airport (KMKE) | Sheboygan County Memorial International Airport (KSBM) | 2026-04-28 22:16 UTC | 2026-04-28 23:12 UTC | 55m |
| N8738A |  | Pierce County/Thun Field (KPLU) | Auburn Municipal Airport (KS50) | 2026-04-28 22:59 UTC | 2026-04-28 23:09 UTC | 10m |
| WAH | WAH | Beluga Airport (PABG) | Trading Bay Production Airport (5AK0) | 2026-04-28 22:47 UTC | 2026-04-28 23:06 UTC | 19m |
| VAIL51 | VAI | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-04-28 22:11 UTC | 2026-04-28 23:04 UTC | 52m |
| N20143 |  | Fairfield County Airport (KLHQ) | Rall Field (32OH) | 2026-04-28 22:28 UTC | 2026-04-28 23:04 UTC | 35m |
| N56066 |  | Daniel K Inouye International Airport (PHNL) | Daniel K Inouye International Airport (PHNL) | 2026-04-28 23:00 UTC | 2026-04-28 23:00 UTC | 0m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-04-28 12:10 UTC | 2026-04-28 22:58 UTC | 10h 48m |
| MNB179 | MNB | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-04-28 14:50 UTC | 2026-04-28 22:55 UTC | 8h 4m |
| CSI502 | CSI | Albuquerque International Sunport Airport (KABQ) | NM39 (NM39) | 2026-04-28 22:24 UTC | 2026-04-28 22:52 UTC | 28m |
| N3864M |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-04-28 21:54 UTC | 2026-04-28 22:43 UTC | 49m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-04-28 22:20 UTC | 2026-04-28 22:40 UTC | 20m |
| N29282 |  | Beverly Regional Airport (KBVY) | Orange Municipal Airport (KORE) | 2026-04-28 22:10 UTC | 2026-04-28 22:39 UTC | 29m |
| N605WM |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-28 22:04 UTC | 2026-04-28 22:39 UTC | 34m |
| SKW3388 | SkyWest Airlines | San Diego International Airport (KSAN) | Sequoia Field (KD86) | 2026-04-28 21:52 UTC | 2026-04-28 22:33 UTC | 40m |
|  |  | Skeeter Landing Airport (II97) | IN19 (IN19) | 2026-04-28 22:25 UTC | 2026-04-28 22:32 UTC | 6m |
| EJA807 | EJA | Naples Municipal Airport (KAPF) | Austin-Bergstrom International Airport (KAUS) | 2026-04-28 20:04 UTC | 2026-04-28 22:29 UTC | 2h 25m |
| N418FP |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-04-28 21:34 UTC | 2026-04-28 22:26 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
