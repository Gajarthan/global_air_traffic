# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_16:40:51_UTC-green)

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

**Latest saved flight:** 2026-04-26 16:40:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 16:40:51 UTC

- **55,649** saved flights
- **21,868** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,649** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **672,432.3 tonnes** estimated CO2 emissions
- **38,981,580 km** total distance flown
- **843 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2362 |
| 2 | SkyWest Airlines | 2091 |
| 3 | IndiGo | 1275 |
| 4 | EJA | 980 |
| 5 | American Airlines | 884 |
| 6 | Southwest Airlines | 783 |
| 7 | ENY | 699 |
| 8 | Lufthansa | 689 |
| 9 | Vueling | 562 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 535 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 466 |
| 14 | WIF | 462 |
| 15 | Delta Air Lines | 457 |
| 16 | Swiss International | 437 |
| 17 | QLK | 429 |
| 18 | LXJ | 398 |
| 19 | AEE | 369 |
| 20 | Alaska Airlines | 368 |
| 21 | EJU | 360 |
| 22 | easyJet | 355 |
| 23 | VIV | 355 |
| 24 | Air France | 327 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 313 |
| 27 | AXB | 305 |
| 28 | GLO | 284 |
| 29 | AIQ | 283 |
| 30 | JetBlue | 283 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43970 |
| 2 | 🇪🇸 ES | 4077 |
| 3 | 🇮🇳 IN | 4024 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3211 |
| 6 | 🇩🇪 DE | 3053 |
| 7 | 🇮🇹 IT | 3041 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2745 |
| 10 | 🇨🇴 CO | 2517 |
| 11 | 🇬🇧 GB | 2344 |
| 12 | 🇫🇷 FR | 2206 |
| 13 | 🇲🇽 MX | 1754 |
| 14 | 🇬🇷 GR | 1661 |
| 15 | 🇨🇭 CH | 1581 |
| 16 | 🇳🇴 NO | 1496 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1149 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1017 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 899 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 829 |
| 26 | 🇲🇦 MA | 709 |
| 27 | 🇲🇪 ME | 608 |
| 28 | 🇳🇱 NL | 581 |
| 29 | 🇲🇴 MO | 571 |
| 30 | 🇧🇸 BS | 482 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1259 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 918 |
| 4 | Indira Gandhi International Airport |  | IN | 852 |
| 5 | El Dorado International Airport |  | CO | 847 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 818 |
| 7 | Guaymaral Airport |  | CO | 766 |
| 8 | Harry Reid International Airport |  | US | 707 |
| 9 | Frankfurt am Main International Airport |  | DE | 672 |
| 10 | Zurich Airport |  | CH | 669 |
| 11 | La Aurora Airport |  | GT | 622 |
| 12 | Macau International Airport |  | MO | 571 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 550 |
| 14 | Chicago O'Hare International Airport |  | US | 541 |
| 15 | Madrid Barajas International Airport |  | ES | 523 |
| 16 | Kuala Lumpur International Airport |  | MY | 523 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 519 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 480 |
| 20 | Bengaluru International Airport |  | IN | 479 |
| 21 | Congonhas Airport |  | BR | 463 |
| 22 | Charlotte/Douglas International Airport |  | US | 448 |
| 23 | Tenerife Norte Airport |  | ES | 445 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 431 |
| 26 | Salt Lake City International Airport |  | US | 420 |
| 27 | Capua Airport |  | IT | 414 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 410 |
| 29 | Daniel K Inouye International Airport |  | US | 408 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 402 |
| 31 | Vitoria/Foronda Airport |  | ES | 384 |
| 32 | Barcelona International Airport |  | ES | 381 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 373 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 372 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 363 |
| 37 | O. R. Tambo International Airport |  | ZA | 359 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 331 |
| 40 | Amsterdam Airport Schiphol |  | NL | 330 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 312 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 203 | 14m | 114 km | 398.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 175 | 21m | 244 km | 736.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 87 | 27m | 152 km | 227.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 78 | 1h 1m | 695 km | 935.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-26 15:18 UTC | 2026-04-26 16:40 UTC | 1h 22m |
| N543WB |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-04-26 15:51 UTC | 2026-04-26 16:40 UTC | 49m |
| UAL755 | United Airlines | Youngberg Ranch Airport (NV17) | San Francisco International Airport (KSFO) | 2026-04-26 15:55 UTC | 2026-04-26 16:40 UTC | 44m |
| OKCPB | OKC | Cannes-Mandelieu Airport (LFMD) | Milano / Bresso Airport (LIMB) | 2026-04-26 15:30 UTC | 2026-04-26 16:39 UTC | 1h 9m |
| PNC0610 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-26 16:17 UTC | 2026-04-26 16:31 UTC | 14m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-26 16:18 UTC | 2026-04-26 16:30 UTC | 11m |
| N275WA |  | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-04-26 16:29 UTC | 2026-04-26 16:29 UTC | 0m |
| PSBTJ | PSB | SBMM (SBMM) | SBMM (SBMM) | 2026-04-26 16:12 UTC | 2026-04-26 16:25 UTC | 13m |
| N11540 |  | Villa Char Mar Airport (1FA9) | Wauchula Municipal Airport (KCHN) | 2026-04-26 15:45 UTC | 2026-04-26 16:24 UTC | 38m |
| S5DTJ |  | Cerklje Airport (LJCE) | Cerklje Airport (LJCE) | 2026-04-26 16:16 UTC | 2026-04-26 16:19 UTC | 2m |
| N616RM |  | Valkaria Airport (KX59) | Fellsmere Airport (4FL3) | 2026-04-26 15:32 UTC | 2026-04-26 16:17 UTC | 44m |
| QTR78X | Qatar Airways | Henri Coanda International Airport (LROP) | Queen Alia International Airport (OJAI) | 2026-04-26 14:24 UTC | 2026-04-26 16:15 UTC | 1h 51m |
| CPA3348 | Cathay Pacific | Soekarno-Hatta International Airport (WIII) | Macau International Airport (VMMC) | 2026-04-26 08:44 UTC | 2026-04-26 16:15 UTC | 7h 31m |
| SXS8VB | SXS | Hamburg Airport (EDDH) | Adnan Menderes International Airport (LTBJ) | 2026-04-26 13:28 UTC | 2026-04-26 16:11 UTC | 2h 42m |
| WIF74D | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-04-26 15:51 UTC | 2026-04-26 16:08 UTC | 17m |
| RYR65CN | Ryanair | Manchester Airport (EGCC) | Malpensa International Airport (LIMC) | 2026-04-26 14:20 UTC | 2026-04-26 16:05 UTC | 1h 45m |
| RYR26HH | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Crotone Airport (LIBC) | 2026-04-26 14:48 UTC | 2026-04-26 16:03 UTC | 1h 14m |
| CGFHA | CGF | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-04-26 15:35 UTC | 2026-04-26 16:03 UTC | 27m |
| PH1348 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-04-26 15:32 UTC | 2026-04-26 16:01 UTC | 29m |
| N3944Q |  | Merritt Island Airport (KCOI) | Merritt Island Airport (KCOI) | 2026-04-26 15:34 UTC | 2026-04-26 16:00 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
