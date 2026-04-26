# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_08:22:34_UTC-green)

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

**Latest saved flight:** 2026-04-26 08:22:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 08:22:34 UTC

- **54,816** saved flights
- **21,644** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **54,816** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **660,329.3 tonnes** estimated CO2 emissions
- **38,279,959 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2313 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1238 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 652 |
| 9 | Vueling | 550 |
| 10 | AXM | 530 |
| 11 | LATAM Airlines | 526 |
| 12 | All Nippon Airways | 485 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 452 |
| 15 | WIF | 448 |
| 16 | QLK | 426 |
| 17 | Swiss International | 423 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 365 |
| 21 | VIV | 352 |
| 22 | EJU | 350 |
| 23 | easyJet | 350 |
| 24 | Japan Airlines | 318 |
| 25 | Air France | 313 |
| 26 | Cathay Pacific | 308 |
| 27 | AXB | 288 |
| 28 | AIQ | 280 |
| 29 | JetBlue | 280 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43676 |
| 2 | 🇪🇸 ES | 3968 |
| 3 | 🇮🇳 IN | 3905 |
| 4 | 🇦🇺 AU | 3712 |
| 5 | 🇧🇷 BR | 3161 |
| 6 | 🇮🇹 IT | 2963 |
| 7 | 🇯🇵 JP | 2944 |
| 8 | 🇩🇪 DE | 2941 |
| 9 | 🇨🇦 CA | 2723 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2287 |
| 12 | 🇫🇷 FR | 2133 |
| 13 | 🇲🇽 MX | 1720 |
| 14 | 🇬🇷 GR | 1631 |
| 15 | 🇨🇭 CH | 1543 |
| 16 | 🇳🇴 NO | 1458 |
| 17 | 🇲🇾 MY | 1291 |
| 18 | 🇿🇦 ZA | 1121 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 991 |
| 21 | 🇹🇭 TH | 990 |
| 22 | 🇵🇭 PH | 938 |
| 23 | 🇰🇷 KR | 882 |
| 24 | 🇵🇱 PL | 877 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 688 |
| 27 | 🇲🇪 ME | 596 |
| 28 | 🇳🇱 NL | 559 |
| 29 | 🇲🇴 MO | 554 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1247 |
| 2 | Tokyo International Airport |  | JP | 1002 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | El Dorado International Airport |  | CO | 839 |
| 5 | Indira Gandhi International Airport |  | IN | 827 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 805 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 703 |
| 9 | Zurich Airport |  | CH | 650 |
| 10 | Frankfurt am Main International Airport |  | DE | 637 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 554 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 16 | Kuala Lumpur International Airport |  | MY | 513 |
| 17 | Madrid Barajas International Airport |  | ES | 506 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 489 |
| 19 | Malpensa International Airport |  | IT | 469 |
| 20 | Bengaluru International Airport |  | IN | 465 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 435 |
| 24 | Ninoy Aquino International Airport |  | PH | 433 |
| 25 | Salt Lake City International Airport |  | US | 415 |
| 26 | Charles de Gaulle International Airport |  | FR | 414 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 400 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 391 |
| 31 | Vitoria/Foronda Airport |  | ES | 374 |
| 32 | Barcelona International Airport |  | ES | 372 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | Reno/Tahoe International Airport |  | US | 364 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 359 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 37 | O. R. Tambo International Airport |  | ZA | 352 |
| 38 | Don Mueang International Airport |  | TH | 337 |
| 39 | Calgary International Airport |  | CA | 327 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 249 | 1h 7m | 706 km | 3,031.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 158 | 1h 27m | 910 km | 2,479.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 133 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 127 | 26m | 275 km | 601.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 104 | 1h 11m | 770 km | 1,381.6 t |
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
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-26 08:04 UTC | 2026-04-26 08:22 UTC | 18m |
|  |  | Lamezia Terme Airport (LICA) | Crotone Airport (LIBC) | 2026-04-26 07:38 UTC | 2026-04-26 07:58 UTC | 20m |
| FHPIA | FHP | Pont Sur Yonne Airport (LFGO) | Pont Sur Yonne Airport (LFGO) | 2026-04-26 07:49 UTC | 2026-04-26 07:50 UTC | 0m |
| JDL2787 | JDL | Shenzhen Bao'an International Airport (ZGSZ) | VGZR (VGZR) | 2026-04-25 21:25 UTC | 2026-04-26 07:43 UTC | 10h 17m |
| RFS718 | RFS | Auburn Municipal Airport (KS50) | Portland-Hillsboro Airport (KHIO) | 2026-04-26 06:24 UTC | 2026-04-26 07:30 UTC | 1h 6m |
| VOE1664 | VOE | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Paris-Orly Airport (LFPO) | 2026-04-26 06:21 UTC | 2026-04-26 07:30 UTC | 1h 8m |
| VOE3931 | VOE | Francisco de Sá Carneiro Airport (LPPR) | La Morgal Airport (LEMR) | 2026-04-26 06:50 UTC | 2026-04-26 07:30 UTC | 39m |
| VOR12 | VOR | Schleswig Airport (ETNS) | Sonderborg Airport (EKSB) | 2026-04-26 05:50 UTC | 2026-04-26 07:28 UTC | 1h 37m |
| KST2612 | KST | Chiang Mai International Airport (VTCC) | Lamphun Airport (VTCO) | 2026-04-26 07:00 UTC | 2026-04-26 07:26 UTC | 26m |
| MNE101 | MNE | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 2026-04-26 07:04 UTC | 2026-04-26 07:25 UTC | 21m |
| WZZ139 | Wizz Air | Oslo Gardermoen Airport (ENGM) | Oksywie Military Air Base (EPOK) | 2026-04-26 06:32 UTC | 2026-04-26 07:22 UTC | 49m |
| EIN63N | Aer Lingus | Dublin Airport (EIDW) | Brussels Airport (EBBR) | 2026-04-26 06:12 UTC | 2026-04-26 07:21 UTC | 1h 8m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Chiang Rai Airport (VTCR) | 2026-04-26 07:02 UTC | 2026-04-26 07:18 UTC | 15m |
| DLH9XK | Lufthansa | Frankfurt am Main International Airport (EDDF) | Dinkelsbuhl-Sinbronn Airport (EDND) | 2026-04-26 06:38 UTC | 2026-04-26 07:17 UTC | 39m |
| RYR537E | Ryanair | Sepurine Training Base (LD57) | Ceske Budejovice Airport (LKCS) | 2026-04-26 06:12 UTC | 2026-04-26 07:17 UTC | 1h 5m |
| FJO71P | FJO | Paris-Le Bourget Airport (LFPB) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-26 06:06 UTC | 2026-04-26 07:16 UTC | 1h 10m |
| WUK712 | WUK | London Gatwick Airport (EGKK) | Dubrovnik Airport (LDDU) | 2026-04-26 05:09 UTC | 2026-04-26 07:15 UTC | 2h 5m |
| EZY24HL | easyJet | London Luton Airport (EGGW) | Livno Brda Bosni Airport (LQLV) | 2026-04-26 05:20 UTC | 2026-04-26 07:13 UTC | 1h 53m |
| OECOG | OEC | Stockerau Airport (LOAU) | Znojmo Airport (LKZN) | 2026-04-26 07:00 UTC | 2026-04-26 07:13 UTC | 13m |
| AIC4CJ | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-04-26 06:55 UTC | 2026-04-26 07:13 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
