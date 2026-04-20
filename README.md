# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_17:12:45_UTC-green)

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

**Latest saved flight:** 2026-04-20 17:12:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 17:12:45 UTC

- **45,504** saved flights
- **18,778** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **45,504** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **549,422.3 tonnes** estimated CO2 emissions
- **31,850,568 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1937 |
| 2 | SkyWest Airlines | 1758 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 786 |
| 5 | American Airlines | 747 |
| 6 | Southwest Airlines | 651 |
| 7 | ENY | 590 |
| 8 | Lufthansa | 471 |
| 9 | Vueling | 459 |
| 10 | AXM | 458 |
| 11 | LATAM Airlines | 450 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 392 |
| 14 | Delta Air Lines | 384 |
| 15 | QLK | 366 |
| 16 | WIF | 359 |
| 17 | LXJ | 357 |
| 18 | Swiss International | 352 |
| 19 | AEE | 312 |
| 20 | Alaska Airlines | 309 |
| 21 | EJU | 304 |
| 22 | VIV | 292 |
| 23 | easyJet | 290 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 262 |
| 26 | JetBlue | 242 |
| 27 | United Airlines | 241 |
| 28 | AXB | 240 |
| 29 | Cathay Pacific | 236 |
| 30 | GLO | 236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35929 |
| 2 | 🇮🇳 IN | 3383 |
| 3 | 🇪🇸 ES | 3352 |
| 4 | 🇦🇺 AU | 3131 |
| 5 | 🇧🇷 BR | 2686 |
| 6 | 🇯🇵 JP | 2487 |
| 7 | 🇮🇹 IT | 2469 |
| 8 | 🇩🇪 DE | 2356 |
| 9 | 🇨🇦 CA | 2203 |
| 10 | 🇨🇴 CO | 2093 |
| 11 | 🇬🇧 GB | 1875 |
| 12 | 🇫🇷 FR | 1740 |
| 13 | 🇲🇽 MX | 1421 |
| 14 | 🇬🇷 GR | 1400 |
| 15 | 🇨🇭 CH | 1248 |
| 16 | 🇳🇴 NO | 1147 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇵🇭 PH | 811 |
| 22 | 🇹🇷 TR | 808 |
| 23 | 🇰🇷 KR | 747 |
| 24 | 🇬🇹 GT | 733 |
| 25 | 🇵🇱 PL | 728 |
| 26 | 🇲🇦 MA | 565 |
| 27 | 🇲🇪 ME | 482 |
| 28 | 🇳🇱 NL | 464 |
| 29 | 🇲🇴 MO | 424 |
| 30 | 🇧🇸 BS | 417 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1062 |
| 2 | Tokyo International Airport |  | JP | 849 |
| 3 | Denver International Airport |  | US | 754 |
| 4 | El Dorado International Airport |  | CO | 730 |
| 5 | Indira Gandhi International Airport |  | IN | 730 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 695 |
| 7 | Harry Reid International Airport |  | US | 587 |
| 8 | Guaymaral Airport |  | CO | 574 |
| 9 | Zurich Airport |  | CH | 544 |
| 10 | La Aurora Airport |  | GT | 541 |
| 11 | Kuala Lumpur International Airport |  | MY | 449 |
| 12 | Chicago O'Hare International Airport |  | US | 448 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 446 |
| 14 | Frankfurt am Main International Airport |  | DE | 443 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 436 |
| 16 | Macau International Airport |  | MO | 424 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 421 |
| 18 | Madrid Barajas International Airport |  | ES | 407 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 393 |
| 21 | Tenerife Norte Airport |  | ES | 393 |
| 22 | Malpensa International Airport |  | IT | 392 |
| 23 | Congonhas Airport |  | BR | 384 |
| 24 | Ninoy Aquino International Airport |  | PH | 376 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 345 |
| 26 | Salt Lake City International Airport |  | US | 339 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 28 | Charles de Gaulle International Airport |  | FR | 338 |
| 29 | Daniel K Inouye International Airport |  | US | 336 |
| 30 | Capua Airport |  | IT | 328 |
| 31 | Reno/Tahoe International Airport |  | US | 314 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 314 |
| 33 | Vitoria/Foronda Airport |  | ES | 313 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 312 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 308 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 298 |
| 38 | Calgary International Airport |  | CA | 276 |
| 39 | Don Mueang International Airport |  | TH | 275 |
| 40 | Viracopos International Airport |  | BR | 273 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 231 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 168 | 14m | 114 km | 329.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 129 | 21m | 244 km | 543.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 106 | 26m | 275 km | 502.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 80 | 31m | 369 km | 509.2 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 71 | 26m | 215 km | 263.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 67 | 13m | 99 km | 114.9 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 28 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 63 | 1h 52m | 1,304 km | 1,417.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CSZ887 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Jubarkas Airport (EYJB) | 2026-04-20 07:03 UTC | 2026-04-20 17:12 UTC | 10h 9m |
| LXJ428 | LXJ | Huntsville International-Carl T Jones Field (KHSV) | Orlando Executive Airport (KORL) | 2026-04-20 16:03 UTC | 2026-04-20 17:11 UTC | 1h 8m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-20 15:34 UTC | 2026-04-20 17:11 UTC | 1h 37m |
| MLIN30 | MLI | Istres Le Tube/Istres Air Base (BA 125) Airport (LFMI) | Lurcy-Levis Airport (LFJU) | 2026-04-20 16:25 UTC | 2026-04-20 17:06 UTC | 40m |
| N4325R |  | Miami Executive Airport (KTMB) | Richards Field (04FA) | 2026-04-20 17:01 UTC | 2026-04-20 17:06 UTC | 5m |
| EXS9AN | EXS | London Stansted Airport (EGSS) | L'Aquila / Preturo Airport (LIAP) | 2026-04-20 14:32 UTC | 2026-04-20 17:04 UTC | 2h 32m |
| FPO743 | FPO | Lille-Lesquin Airport (LFQQ) | Pratica Di Mare Airport (LIRE) | 2026-04-20 14:46 UTC | 2026-04-20 17:04 UTC | 2h 18m |
| RYR61PH | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Foligno Airport (LIAF) | 2026-04-20 16:00 UTC | 2026-04-20 17:04 UTC | 1h 4m |
| N496SP |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-20 16:43 UTC | 2026-04-20 17:04 UTC | 20m |
| WARBEVR7 | WAR | Borrego Valley Airport (KL08) | Borrego Air Ranch Airport (58CL) | 2026-04-20 16:35 UTC | 2026-04-20 17:03 UTC | 28m |
| IATLS | IAT | Bologna / Borgo Panigale Airport (LIPE) | Bologna / Borgo Panigale Airport (LIPE) | 2026-04-20 16:50 UTC | 2026-04-20 16:59 UTC | 8m |
| N51PG |  | Hutson Airfield (8FL0) | Peter O Knight Airport (KTPF) | 2026-04-20 16:12 UTC | 2026-04-20 16:57 UTC | 45m |
| N702PC |  | KU77 (KU77) | Henderson Executive Airport (KHND) | 2026-04-20 15:32 UTC | 2026-04-20 16:55 UTC | 1h 22m |
| STT40 | STT | Boise Air Trml/Gowen Field (KBOI) | Ontario Municipal Airport (KONO) | 2026-04-20 16:31 UTC | 2026-04-20 16:54 UTC | 23m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-04-20 16:17 UTC | 2026-04-20 16:52 UTC | 34m |
| CFARA | CFA | RAF Brize Norton (EGVN) | Netheravon Airfield (EGDN) | 2026-04-20 16:33 UTC | 2026-04-20 16:50 UTC | 17m |
| RYR6QZ | Ryanair | L'Aquila / Preturo Airport (LIAP) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-20 15:24 UTC | 2026-04-20 16:44 UTC | 1h 19m |
| SHARK45 | SHA | Usaf Academy Davis Airfield (KAFF) | Central Colorado Regional Airport (KAEJ) | 2026-04-20 16:07 UTC | 2026-04-20 16:42 UTC | 35m |
| BALL17 | BAL | 75OK (75OK) | Tulsa International Airport (KTUL) | 2026-04-20 16:03 UTC | 2026-04-20 16:42 UTC | 38m |
| N54GB |  | Carson City Airport (KCXP) | Minden-Tahoe Airport (KMEV) | 2026-04-20 16:32 UTC | 2026-04-20 16:41 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
