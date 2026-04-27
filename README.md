# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_08:55:05_UTC-green)

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

**Latest saved flight:** 2026-04-27 08:55:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 08:55:05 UTC

- **56,534** saved flights
- **22,176** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **56,534** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **686,091.8 tonnes** estimated CO2 emissions
- **39,773,440 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2399 |
| 2 | SkyWest Airlines | 2134 |
| 3 | IndiGo | 1288 |
| 4 | EJA | 1012 |
| 5 | American Airlines | 900 |
| 6 | Southwest Airlines | 804 |
| 7 | ENY | 714 |
| 8 | Lufthansa | 693 |
| 9 | Vueling | 566 |
| 10 | AXM | 551 |
| 11 | LATAM Airlines | 547 |
| 12 | All Nippon Airways | 499 |
| 13 | AZU | 475 |
| 14 | WIF | 469 |
| 15 | Delta Air Lines | 466 |
| 16 | Swiss International | 445 |
| 17 | QLK | 438 |
| 18 | LXJ | 404 |
| 19 | Alaska Airlines | 380 |
| 20 | AEE | 371 |
| 21 | EJU | 365 |
| 22 | VIV | 361 |
| 23 | easyJet | 360 |
| 24 | Air France | 329 |
| 25 | Japan Airlines | 326 |
| 26 | Cathay Pacific | 324 |
| 27 | AXB | 310 |
| 28 | JetBlue | 289 |
| 29 | GLO | 285 |
| 30 | United Airlines | 285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44813 |
| 2 | 🇪🇸 ES | 4129 |
| 3 | 🇮🇳 IN | 4066 |
| 4 | 🇦🇺 AU | 3802 |
| 5 | 🇧🇷 BR | 3257 |
| 6 | 🇩🇪 DE | 3086 |
| 7 | 🇮🇹 IT | 3085 |
| 8 | 🇯🇵 JP | 3032 |
| 9 | 🇨🇦 CA | 2789 |
| 10 | 🇨🇴 CO | 2558 |
| 11 | 🇬🇧 GB | 2371 |
| 12 | 🇫🇷 FR | 2219 |
| 13 | 🇲🇽 MX | 1799 |
| 14 | 🇬🇷 GR | 1671 |
| 15 | 🇨🇭 CH | 1597 |
| 16 | 🇳🇴 NO | 1516 |
| 17 | 🇲🇾 MY | 1336 |
| 18 | 🇿🇦 ZA | 1153 |
| 19 | 🇳🇿 NZ | 1072 |
| 20 | 🇹🇷 TR | 1031 |
| 21 | 🇹🇭 TH | 1012 |
| 22 | 🇵🇭 PH | 962 |
| 23 | 🇵🇱 PL | 910 |
| 24 | 🇰🇷 KR | 901 |
| 25 | 🇬🇹 GT | 842 |
| 26 | 🇲🇦 MA | 715 |
| 27 | 🇲🇪 ME | 615 |
| 28 | 🇲🇴 MO | 596 |
| 29 | 🇳🇱 NL | 591 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1284 |
| 2 | Tokyo International Airport |  | JP | 1030 |
| 3 | Denver International Airport |  | US | 939 |
| 4 | El Dorado International Airport |  | CO | 864 |
| 5 | Indira Gandhi International Airport |  | IN | 858 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 823 |
| 7 | Guaymaral Airport |  | CO | 778 |
| 8 | Harry Reid International Airport |  | US | 720 |
| 9 | Zurich Airport |  | CH | 681 |
| 10 | Frankfurt am Main International Airport |  | DE | 680 |
| 11 | La Aurora Airport |  | GT | 633 |
| 12 | Macau International Airport |  | MO | 596 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 562 |
| 14 | Chicago O'Hare International Airport |  | US | 551 |
| 15 | Madrid Barajas International Airport |  | ES | 530 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 526 |
| 17 | Kuala Lumpur International Airport |  | MY | 526 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 500 |
| 19 | Malpensa International Airport |  | IT | 491 |
| 20 | Bengaluru International Airport |  | IN | 487 |
| 21 | Congonhas Airport |  | BR | 468 |
| 22 | Charlotte/Douglas International Airport |  | US | 456 |
| 23 | Tenerife Norte Airport |  | ES | 452 |
| 24 | Ninoy Aquino International Airport |  | PH | 442 |
| 25 | Charles de Gaulle International Airport |  | FR | 435 |
| 26 | Salt Lake City International Airport |  | US | 433 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 419 |
| 28 | Capua Airport |  | IT | 419 |
| 29 | Daniel K Inouye International Airport |  | US | 416 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 407 |
| 31 | Barcelona International Airport |  | ES | 387 |
| 32 | Vitoria/Foronda Airport |  | ES | 385 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 382 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 373 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 368 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 361 |
| 38 | Don Mueang International Airport |  | TH | 345 |
| 39 | Amsterdam Airport Schiphol |  | NL | 338 |
| 40 | Calgary International Airport |  | CA | 337 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 317 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 208 | 14m | 114 km | 408.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 180 | 21m | 244 km | 757.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 162 | 1h 27m | 910 km | 2,542.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 139 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 136 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 110 | 1h 12m | 770 km | 1,461.3 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 109 | 44m | 452 km | 849.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 1m | 695 km | 970.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 53m | 1,304 km | 1,732.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 74 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 71 | 1h 42m | 1,423 km | 1,742.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRPR52 | TRP | Oakey Airport (YBOK) | Toowoomba Airport (YTWB) | 2026-04-27 08:28 UTC | 2026-04-27 08:55 UTC | 26m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-27 01:19 UTC | 2026-04-27 08:48 UTC | 7h 28m |
| AXM189 | AXM | Kuala Lumpur International Airport (WMKK) | Benta Airport (WMAC) | 2026-04-27 01:00 UTC | 2026-04-27 08:44 UTC | 7h 44m |
| LSI191 | LSI | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-26 21:33 UTC | 2026-04-27 08:36 UTC | 11h 2m |
| CLX4327 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-26 21:37 UTC | 2026-04-27 08:33 UTC | 10h 55m |
| TLM220 | TLM | Don Mueang International Airport (VTBD) | Tribhuvan International Airport (VNKT) | 2026-04-27 05:07 UTC | 2026-04-27 08:29 UTC | 3h 22m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-27 08:22 UTC | 2026-04-27 08:29 UTC | 7m |
| UAE9840 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-27 01:50 UTC | 2026-04-27 08:27 UTC | 6h 37m |
| AFL1886 | AFL | Sheremetyevo International Airport (UUEE) | Bezymyanka Airfield (UWWG) | 2026-04-27 07:30 UTC | 2026-04-27 08:25 UTC | 54m |
| STW001 | STW | Antalya International Airport (LTAI) | Sheremetyevo International Airport (UUEE) | 2026-04-27 04:20 UTC | 2026-04-27 08:23 UTC | 4h 3m |
| THY70 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-04-26 22:58 UTC | 2026-04-27 08:23 UTC | 9h 25m |
| IAM2855 | IAM | Pratica Di Mare Airport (LIRE) | Bari / Palese International Airport (LIBD) | 2026-04-27 07:11 UTC | 2026-04-27 08:21 UTC | 1h 9m |
| CPA008 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-26 21:09 UTC | 2026-04-27 08:21 UTC | 11h 11m |
| KLM1787 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Hannover Airport (EDDV) | 2026-04-27 07:33 UTC | 2026-04-27 08:15 UTC | 41m |
| CABBY81 | CAB | Kbely Air Base (LKKB) | Pardubice Airport (LKPD) | 2026-04-27 07:19 UTC | 2026-04-27 08:10 UTC | 50m |
| EJU38RH | EJU | Alicante International Airport (LEAL) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-27 05:11 UTC | 2026-04-27 08:06 UTC | 2h 55m |
| SEH2JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-27 07:42 UTC | 2026-04-27 08:05 UTC | 22m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-04-27 07:39 UTC | 2026-04-27 08:03 UTC | 24m |
| JBU608 | JetBlue | Harry Reid International Airport (KLAS) | Gallup Municipal Airport (KGUP) | 2026-04-27 07:22 UTC | 2026-04-27 08:02 UTC | 40m |
| N340EA |  | K00V (K00V) | Pinon Canyon Airport (0CD5) | 2026-04-27 07:10 UTC | 2026-04-27 07:59 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
