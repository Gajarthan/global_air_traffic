# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_05:29:23_UTC-green)

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

**Latest saved flight:** 2026-04-21 05:29:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 05:29:23 UTC

- **46,250** saved flights
- **19,028** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,250** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **557,829.6 tonnes** estimated CO2 emissions
- **32,337,947 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1958 |
| 2 | SkyWest Airlines | 1799 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 799 |
| 5 | American Airlines | 769 |
| 6 | Southwest Airlines | 670 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 477 |
| 9 | Vueling | 465 |
| 10 | AXM | 462 |
| 11 | LATAM Airlines | 458 |
| 12 | All Nippon Airways | 412 |
| 13 | AZU | 397 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 371 |
| 16 | WIF | 363 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 355 |
| 19 | Alaska Airlines | 317 |
| 20 | AEE | 314 |
| 21 | EJU | 308 |
| 22 | VIV | 298 |
| 23 | easyJet | 292 |
| 24 | Japan Airlines | 277 |
| 25 | Air France | 263 |
| 26 | Cathay Pacific | 249 |
| 27 | JetBlue | 248 |
| 28 | United Airlines | 246 |
| 29 | AXB | 242 |
| 30 | GLO | 237 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36845 |
| 2 | 🇮🇳 IN | 3386 |
| 3 | 🇪🇸 ES | 3378 |
| 4 | 🇦🇺 AU | 3185 |
| 5 | 🇧🇷 BR | 2716 |
| 6 | 🇯🇵 JP | 2512 |
| 7 | 🇮🇹 IT | 2490 |
| 8 | 🇩🇪 DE | 2366 |
| 9 | 🇨🇦 CA | 2263 |
| 10 | 🇨🇴 CO | 2130 |
| 11 | 🇬🇧 GB | 1891 |
| 12 | 🇫🇷 FR | 1751 |
| 13 | 🇲🇽 MX | 1443 |
| 14 | 🇬🇷 GR | 1407 |
| 15 | 🇨🇭 CH | 1254 |
| 16 | 🇳🇴 NO | 1153 |
| 17 | 🇲🇾 MY | 1130 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 909 |
| 20 | 🇵🇭 PH | 825 |
| 21 | 🇹🇭 TH | 819 |
| 22 | 🇹🇷 TR | 814 |
| 23 | 🇰🇷 KR | 755 |
| 24 | 🇬🇹 GT | 737 |
| 25 | 🇵🇱 PL | 733 |
| 26 | 🇲🇦 MA | 569 |
| 27 | 🇲🇪 ME | 485 |
| 28 | 🇳🇱 NL | 468 |
| 29 | 🇲🇴 MO | 436 |
| 30 | 🇧🇸 BS | 420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1095 |
| 2 | Tokyo International Airport |  | JP | 857 |
| 3 | Denver International Airport |  | US | 774 |
| 4 | El Dorado International Airport |  | CO | 743 |
| 5 | Indira Gandhi International Airport |  | IN | 733 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 700 |
| 7 | Harry Reid International Airport |  | US | 600 |
| 8 | Guaymaral Airport |  | CO | 583 |
| 9 | Zurich Airport |  | CH | 549 |
| 10 | La Aurora Airport |  | GT | 545 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 462 |
| 12 | Chicago O'Hare International Airport |  | US | 459 |
| 13 | Kuala Lumpur International Airport |  | MY | 452 |
| 14 | Frankfurt am Main International Airport |  | DE | 450 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 447 |
| 16 | Macau International Airport |  | MO | 436 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 423 |
| 18 | Madrid Barajas International Airport |  | ES | 412 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 396 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 388 |
| 24 | Ninoy Aquino International Airport |  | PH | 383 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 354 |
| 26 | Daniel K Inouye International Airport |  | US | 346 |
| 27 | Salt Lake City International Airport |  | US | 346 |
| 28 | Charles de Gaulle International Airport |  | FR | 342 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 30 | Capua Airport |  | IT | 334 |
| 31 | Reno/Tahoe International Airport |  | US | 321 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 319 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 318 |
| 34 | Vitoria/Foronda Airport |  | ES | 317 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 311 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 303 |
| 38 | Calgary International Airport |  | CA | 280 |
| 39 | Viracopos International Airport |  | BR | 277 |
| 40 | Don Mueang International Airport |  | TH | 275 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 218 | 1h 7m | 706 km | 2,654.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 174 | 14m | 114 km | 341.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 138 | 28m | 304 km | 723.4 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 134 | 21m | 244 km | 564.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 130 | 1h 27m | 910 km | 2,040.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 111 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 75 | 20m | 147 km | 189.8 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 71 | 26m | 215 km | 263.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 68 | 13m | 99 km | 116.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 52m | 1,304 km | 1,462.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SYE | SYE | Tyabb Airport (YTYA) | Melbourne Essendon Airport (YMEN) | 2026-04-21 05:02 UTC | 2026-04-21 05:29 UTC | 26m |
| WXQ | WXQ | Colac Airport (YOLA) | Melbourne Essendon Airport (YMEN) | 2026-04-21 04:37 UTC | 2026-04-21 05:25 UTC | 47m |
| JNA736 | JNA | Taichung Ching Chuang Kang Airport (RCMQ) | Incheon International Airport (RKSI) | 2026-04-21 03:14 UTC | 2026-04-21 05:12 UTC | 1h 58m |
| AAL1999 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Andrews County Airport (KE11) | 2026-04-21 04:27 UTC | 2026-04-21 05:12 UTC | 45m |
| PJP | PJP | Perth Jandakot Airport (YPJT) | Cunderdin Airport (YCUN) | 2026-04-21 04:45 UTC | 2026-04-21 05:09 UTC | 24m |
| QLK1525 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-21 04:20 UTC | 2026-04-21 05:08 UTC | 48m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-04-21 04:50 UTC | 2026-04-21 05:06 UTC | 15m |
| N136HN |  | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-21 05:03 UTC | 2026-04-21 05:06 UTC | 2m |
| N914DK |  | Rogue Valley International/Medford Airport (KMFR) | Siskiyou County Airport (KSIY) | 2026-04-21 04:49 UTC | 2026-04-21 05:03 UTC | 13m |
| ZKTAE | ZKT | Tauranga Airport (NZTG) | Tauranga Airport (NZTG) | 2026-04-21 04:50 UTC | 2026-04-21 05:00 UTC | 9m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-21 04:35 UTC | 2026-04-21 04:49 UTC | 14m |
| N436CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Apple Valley Airport (KAPV) | 2026-04-21 03:50 UTC | 2026-04-21 04:47 UTC | 56m |
| TQR | TQR | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-04-21 04:11 UTC | 2026-04-21 04:43 UTC | 31m |
| AAL2520 | American Airlines | Tampa International Airport (KTPA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-21 00:34 UTC | 2026-04-21 04:41 UTC | 4h 6m |
| YNH | YNH | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-04-21 04:16 UTC | 2026-04-21 04:37 UTC | 21m |
| N224MT |  | Kielberg Canyon Airport (30AZ) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-21 04:13 UTC | 2026-04-21 04:33 UTC | 20m |
| N617BG |  | Renton Municipal Airport (KRNT) | Quincy Flying Service Airport (WA74) | 2026-04-21 04:06 UTC | 2026-04-21 04:32 UTC | 25m |
| N334CA |  | Tucson International Airport (KTUS) | Bisbee Municipal Airport (KP04) | 2026-04-21 03:11 UTC | 2026-04-21 04:31 UTC | 1h 19m |
| CHILD1 | CHI | Gunnison River Farms Airport (2CO5) | Usaf Academy Davis Airfield (KAFF) | 2026-04-21 04:04 UTC | 2026-04-21 04:28 UTC | 24m |
| ANZ222L | ANZ | Auckland International Airport (NZAA) | Wellsford Airport (NZWJ) | 2026-04-21 04:12 UTC | 2026-04-21 04:28 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
