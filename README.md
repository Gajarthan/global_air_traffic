# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_20:51:05_UTC-green)

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

**Latest saved flight:** 2026-04-26 20:51:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 20:51:05 UTC

- **55,994** saved flights
- **22,006** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,994** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **677,082.0 tonnes** estimated CO2 emissions
- **39,251,132 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2386 |
| 2 | SkyWest Airlines | 2113 |
| 3 | IndiGo | 1275 |
| 4 | EJA | 997 |
| 5 | American Airlines | 894 |
| 6 | Southwest Airlines | 792 |
| 7 | ENY | 702 |
| 8 | Lufthansa | 691 |
| 9 | Vueling | 566 |
| 10 | AXM | 545 |
| 11 | LATAM Airlines | 542 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 473 |
| 14 | WIF | 466 |
| 15 | Delta Air Lines | 460 |
| 16 | Swiss International | 439 |
| 17 | QLK | 429 |
| 18 | LXJ | 400 |
| 19 | Alaska Airlines | 371 |
| 20 | AEE | 370 |
| 21 | EJU | 361 |
| 22 | VIV | 357 |
| 23 | easyJet | 356 |
| 24 | Air France | 327 |
| 25 | Japan Airlines | 321 |
| 26 | Cathay Pacific | 315 |
| 27 | AXB | 305 |
| 28 | GLO | 285 |
| 29 | JetBlue | 284 |
| 30 | AIQ | 283 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 44340 |
| 2 | 🇪🇸 ES | 4109 |
| 3 | 🇮🇳 IN | 4024 |
| 4 | 🇦🇺 AU | 3728 |
| 5 | 🇧🇷 BR | 3242 |
| 6 | 🇩🇪 DE | 3066 |
| 7 | 🇮🇹 IT | 3061 |
| 8 | 🇯🇵 JP | 2991 |
| 9 | 🇨🇦 CA | 2772 |
| 10 | 🇨🇴 CO | 2533 |
| 11 | 🇬🇧 GB | 2359 |
| 12 | 🇫🇷 FR | 2211 |
| 13 | 🇲🇽 MX | 1778 |
| 14 | 🇬🇷 GR | 1664 |
| 15 | 🇨🇭 CH | 1586 |
| 16 | 🇳🇴 NO | 1506 |
| 17 | 🇲🇾 MY | 1326 |
| 18 | 🇿🇦 ZA | 1151 |
| 19 | 🇳🇿 NZ | 1043 |
| 20 | 🇹🇷 TR | 1025 |
| 21 | 🇹🇭 TH | 1004 |
| 22 | 🇵🇭 PH | 948 |
| 23 | 🇵🇱 PL | 906 |
| 24 | 🇰🇷 KR | 894 |
| 25 | 🇬🇹 GT | 836 |
| 26 | 🇲🇦 MA | 712 |
| 27 | 🇲🇪 ME | 610 |
| 28 | 🇳🇱 NL | 585 |
| 29 | 🇲🇴 MO | 575 |
| 30 | 🇧🇸 BS | 485 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1271 |
| 2 | Tokyo International Airport |  | JP | 1019 |
| 3 | Denver International Airport |  | US | 928 |
| 4 | El Dorado International Airport |  | CO | 852 |
| 5 | Indira Gandhi International Airport |  | IN | 852 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 818 |
| 7 | Guaymaral Airport |  | CO | 775 |
| 8 | Harry Reid International Airport |  | US | 712 |
| 9 | Frankfurt am Main International Airport |  | DE | 677 |
| 10 | Zurich Airport |  | CH | 673 |
| 11 | La Aurora Airport |  | GT | 628 |
| 12 | Macau International Airport |  | MO | 575 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 559 |
| 14 | Chicago O'Hare International Airport |  | US | 546 |
| 15 | Madrid Barajas International Airport |  | ES | 527 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 523 |
| 17 | Kuala Lumpur International Airport |  | MY | 523 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 492 |
| 19 | Malpensa International Airport |  | IT | 486 |
| 20 | Bengaluru International Airport |  | IN | 479 |
| 21 | Congonhas Airport |  | BR | 467 |
| 22 | Charlotte/Douglas International Airport |  | US | 452 |
| 23 | Tenerife Norte Airport |  | ES | 451 |
| 24 | Ninoy Aquino International Airport |  | PH | 437 |
| 25 | Charles de Gaulle International Airport |  | FR | 431 |
| 26 | Salt Lake City International Airport |  | US | 427 |
| 27 | Capua Airport |  | IT | 417 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 413 |
| 29 | Daniel K Inouye International Airport |  | US | 410 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 402 |
| 31 | Barcelona International Airport |  | ES | 385 |
| 32 | Vitoria/Foronda Airport |  | ES | 384 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 378 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 373 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 365 |
| 36 | Reno/Tahoe International Airport |  | US | 364 |
| 37 | O. R. Tambo International Airport |  | ZA | 360 |
| 38 | Don Mueang International Airport |  | TH | 341 |
| 39 | Calgary International Airport |  | CA | 334 |
| 40 | Amsterdam Airport Schiphol |  | NL | 332 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 316 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 205 | 14m | 114 km | 402.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 177 | 21m | 244 km | 745.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 161 | 1h 27m | 910 km | 2,526.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 134 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 130 | 26m | 275 km | 616.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 109 | 1h 12m | 770 km | 1,448.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 93 | 27m | 215 km | 344.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 85 | 20m | 147 km | 215.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 79 | 1h 40m | 1,156 km | 1,576.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 1m | 695 km | 947.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 77 | 13m | 99 km | 132.0 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 76 | 1h 53m | 1,304 km | 1,709.8 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 74 | 58m | 493 km | 629.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 74 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 70 | 1h 42m | 1,423 km | 1,717.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-26 06:07 UTC | 2026-04-26 20:51 UTC | 14h 43m |
| N739UL |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-04-26 20:31 UTC | 2026-04-26 20:45 UTC | 13m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-26 06:24 UTC | 2026-04-26 20:36 UTC | 14h 11m |
| EJA158 | EJA | Monterey Regional Airport (KMRY) | Eagle Field (CL01) | 2026-04-26 20:05 UTC | 2026-04-26 20:35 UTC | 29m |
| ES801 |  | Sacramento Mather Airport (KMHR) | Cameron Park Airport (KO61) | 2026-04-26 18:48 UTC | 2026-04-26 20:35 UTC | 1h 46m |
| N501SV |  | 48CN (48CN) | Alpine County Airport (KM45) | 2026-04-26 19:55 UTC | 2026-04-26 20:35 UTC | 40m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-26 19:45 UTC | 2026-04-26 20:35 UTC | 49m |
| N500XX |  | Scottsdale Airport (KSDL) | San Martin Airport (KE16) | 2026-04-26 18:50 UTC | 2026-04-26 20:35 UTC | 1h 44m |
| N4983N |  | Aurora Municipal Airport (KARR) | Humm Airport (06IL) | 2026-04-26 20:09 UTC | 2026-04-26 20:22 UTC | 12m |
| EJA485 | EJA | 2OI8 (2OI8) | Lehigh Valley International Airport (KABE) | 2026-04-26 19:27 UTC | 2026-04-26 20:21 UTC | 53m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-04-26 20:04 UTC | 2026-04-26 20:20 UTC | 16m |
| CSZ921 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Zhuhai Airport (ZGSD) | 2026-04-26 20:04 UTC | 2026-04-26 20:19 UTC | 14m |
| N38HL |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-04-26 19:53 UTC | 2026-04-26 20:19 UTC | 26m |
| N630HR |  | Aero Valley Airport (K52F) | Denton Enterprise Airport (KDTO) | 2026-04-26 20:09 UTC | 2026-04-26 20:18 UTC | 9m |
| N550LG |  | Hector International Airport (KFAR) | Dreamcatcher Airport (2MN2) | 2026-04-26 19:50 UTC | 2026-04-26 20:13 UTC | 22m |
| RYR78XT | Ryanair | Palma De Mallorca Airport (LEPA) | Munster Osnabruck Airport (EDDG) | 2026-04-26 17:58 UTC | 2026-04-26 20:10 UTC | 2h 11m |
| N525TK1 |  | Murfreesboro Municipal Airport (KMBT) | Ripley Airport (K25M) | 2026-04-26 19:34 UTC | 2026-04-26 20:05 UTC | 30m |
| EJA578 | EJA | Scottsdale Airport (KSDL) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-26 17:06 UTC | 2026-04-26 20:04 UTC | 2h 57m |
| EJA922 | EJA | Raleigh-Durham International Airport (KRDU) | Auburn University Regional Airport (KAUO) | 2026-04-26 18:52 UTC | 2026-04-26 20:04 UTC | 1h 12m |
| ZKLTL | ZKL | Stratford Airport (NZSD) | New Plymouth Airport (NZNP) | 2026-04-26 19:17 UTC | 2026-04-26 20:04 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
