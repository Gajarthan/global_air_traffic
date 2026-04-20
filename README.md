# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_21:08:45_UTC-green)

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

**Latest saved flight:** 2026-04-20 21:08:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 21:08:45 UTC

- **45,946** saved flights
- **18,942** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **45,946** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **553,911.5 tonnes** estimated CO2 emissions
- **32,110,810 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1957 |
| 2 | SkyWest Airlines | 1784 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 798 |
| 5 | American Airlines | 762 |
| 6 | Southwest Airlines | 662 |
| 7 | ENY | 599 |
| 8 | Lufthansa | 477 |
| 9 | Vueling | 465 |
| 10 | AXM | 458 |
| 11 | LATAM Airlines | 454 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 395 |
| 14 | Delta Air Lines | 387 |
| 15 | QLK | 366 |
| 16 | WIF | 362 |
| 17 | LXJ | 358 |
| 18 | Swiss International | 355 |
| 19 | Alaska Airlines | 314 |
| 20 | AEE | 313 |
| 21 | EJU | 308 |
| 22 | VIV | 296 |
| 23 | easyJet | 292 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 263 |
| 26 | JetBlue | 247 |
| 27 | United Airlines | 244 |
| 28 | AXB | 240 |
| 29 | Cathay Pacific | 236 |
| 30 | GLO | 236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36518 |
| 2 | 🇮🇳 IN | 3383 |
| 3 | 🇪🇸 ES | 3378 |
| 4 | 🇦🇺 AU | 3131 |
| 5 | 🇧🇷 BR | 2702 |
| 6 | 🇯🇵 JP | 2489 |
| 7 | 🇮🇹 IT | 2488 |
| 8 | 🇩🇪 DE | 2366 |
| 9 | 🇨🇦 CA | 2229 |
| 10 | 🇨🇴 CO | 2118 |
| 11 | 🇬🇧 GB | 1887 |
| 12 | 🇫🇷 FR | 1748 |
| 13 | 🇲🇽 MX | 1434 |
| 14 | 🇬🇷 GR | 1403 |
| 15 | 🇨🇭 CH | 1253 |
| 16 | 🇳🇴 NO | 1152 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 897 |
| 20 | 🇹🇭 TH | 817 |
| 21 | 🇹🇷 TR | 813 |
| 22 | 🇵🇭 PH | 811 |
| 23 | 🇰🇷 KR | 747 |
| 24 | 🇬🇹 GT | 734 |
| 25 | 🇵🇱 PL | 732 |
| 26 | 🇲🇦 MA | 569 |
| 27 | 🇲🇪 ME | 484 |
| 28 | 🇳🇱 NL | 467 |
| 29 | 🇲🇴 MO | 426 |
| 30 | 🇧🇸 BS | 419 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1082 |
| 2 | Tokyo International Airport |  | JP | 849 |
| 3 | Denver International Airport |  | US | 765 |
| 4 | El Dorado International Airport |  | CO | 738 |
| 5 | Indira Gandhi International Airport |  | IN | 730 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 698 |
| 7 | Harry Reid International Airport |  | US | 590 |
| 8 | Guaymaral Airport |  | CO | 582 |
| 9 | Zurich Airport |  | CH | 548 |
| 10 | La Aurora Airport |  | GT | 542 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 457 |
| 12 | Chicago O'Hare International Airport |  | US | 455 |
| 13 | Frankfurt am Main International Airport |  | DE | 450 |
| 14 | Kuala Lumpur International Airport |  | MY | 449 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 444 |
| 16 | Macau International Airport |  | MO | 426 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 421 |
| 18 | Madrid Barajas International Airport |  | ES | 412 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 398 |
| 21 | Malpensa International Airport |  | IT | 395 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 385 |
| 24 | Ninoy Aquino International Airport |  | PH | 376 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 350 |
| 26 | Daniel K Inouye International Airport |  | US | 342 |
| 27 | Salt Lake City International Airport |  | US | 342 |
| 28 | Charles de Gaulle International Airport |  | FR | 340 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 30 | Capua Airport |  | IT | 334 |
| 31 | Reno/Tahoe International Airport |  | US | 319 |
| 32 | Vitoria/Foronda Airport |  | ES | 317 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 317 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 316 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 311 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 303 |
| 38 | Calgary International Airport |  | CA | 277 |
| 39 | Viracopos International Airport |  | BR | 276 |
| 40 | Don Mueang International Airport |  | TH | 275 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 213 | 1h 7m | 706 km | 2,593.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 171 | 14m | 114 km | 335.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 163 | 24m | 225 km | 632.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 132 | 21m | 244 km | 555.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 110 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
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
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 52m | 1,304 km | 1,439.8 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG2652 | BRG | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-20 20:41 UTC | 2026-04-20 21:08 UTC | 26m |
| TRF559 | TRF | North Texas Regional/Perrin Field (KGYI) | Rocket Ranch Airport (OK90) | 2026-04-20 20:12 UTC | 2026-04-20 21:04 UTC | 51m |
| N722WD |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-20 20:33 UTC | 2026-04-20 20:56 UTC | 23m |
| N24GM |  | Conroe/North Houston Regional Airport (KCXO) | Grand Rock Airport (XA52) | 2026-04-20 20:20 UTC | 2026-04-20 20:55 UTC | 34m |
| N739LD |  | Quast Airport (MN62) | Hutchinson Municipal/Butler Field (KHCD) | 2026-04-20 20:49 UTC | 2026-04-20 20:54 UTC | 5m |
| SLG1 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-04-20 19:27 UTC | 2026-04-20 20:52 UTC | 1h 25m |
| QTR69J | Qatar Airways | Berlin Brandenburg Airport (EDDB) | Hamad International Airport (OTHH) | 2026-04-20 15:17 UTC | 2026-04-20 20:50 UTC | 5h 33m |
| N352BG |  | Wood County Airport (K1G0) | Donald P Miller Airport (KFZI) | 2026-04-20 19:52 UTC | 2026-04-20 20:46 UTC | 53m |
| UAE9414 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-20 14:11 UTC | 2026-04-20 20:45 UTC | 6h 34m |
| SCA14 | SCA | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-20 20:10 UTC | 2026-04-20 20:44 UTC | 34m |
| N457TS |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-04-20 20:01 UTC | 2026-04-20 20:43 UTC | 41m |
| N716AT |  | Ralph Wien Memorial Airport (PAOT) | Selawik Airport (PASK) | 2026-04-20 20:15 UTC | 2026-04-20 20:41 UTC | 25m |
| WUP668 | WUP | Saline County Regional Airport (KSUZ) | Austin-Bergstrom International Airport (KAUS) | 2026-04-20 19:20 UTC | 2026-04-20 20:41 UTC | 1h 21m |
| SWA4410 | Southwest Airlines | John Wayne/Orange County Airport (KSNA) | Sacramento International Airport (KSMF) | 2026-04-20 19:35 UTC | 2026-04-20 20:41 UTC | 1h 5m |
| N9305N |  | French Valley Airport (KF70) | Hemet-Ryan Airport (KHMT) | 2026-04-20 20:15 UTC | 2026-04-20 20:41 UTC | 26m |
| N330JE |  | Addington Field (4TX8) | Lazy 9 Ranch Airport (TX64) | 2026-04-20 19:53 UTC | 2026-04-20 20:38 UTC | 44m |
| REEF32 | REE | Hasting Airpark (MS80) | Water Valley Municipal Airport (K33M) | 2026-04-20 20:18 UTC | 2026-04-20 20:34 UTC | 15m |
| CFR89 | CFR | Sequoia Ranch Airport (CA44) | Porter Ranch Airport (68CN) | 2026-04-20 20:26 UTC | 2026-04-20 20:32 UTC | 6m |
| CXK1073 | CXK | Ogden-Hinckley Airport (KOGD) | Downey/Hyde Memorial/ Airport (KU58) | 2026-04-20 19:40 UTC | 2026-04-20 20:32 UTC | 51m |
| N329TX |  | Baylie Airport (66XS) | Square Air Airport (TS63) | 2026-04-20 20:25 UTC | 2026-04-20 20:29 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
