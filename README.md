# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_18:17:16_UTC-green)

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

**Latest saved flight:** 2026-04-24 18:17:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 18:17:16 UTC

- **52,018** saved flights
- **20,795** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,018** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **621,441.2 tonnes** estimated CO2 emissions
- **36,025,576 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2192 |
| 2 | SkyWest Airlines | 1961 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 904 |
| 5 | American Airlines | 832 |
| 6 | Southwest Airlines | 738 |
| 7 | ENY | 659 |
| 8 | Lufthansa | 609 |
| 9 | Vueling | 523 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 498 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 439 |
| 14 | WIF | 432 |
| 15 | Delta Air Lines | 428 |
| 16 | QLK | 412 |
| 17 | Swiss International | 399 |
| 18 | LXJ | 387 |
| 19 | AEE | 353 |
| 20 | Alaska Airlines | 341 |
| 21 | EJU | 332 |
| 22 | easyJet | 330 |
| 23 | VIV | 327 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 272 |
| 28 | JetBlue | 268 |
| 29 | United Airlines | 265 |
| 30 | AIQ | 264 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 41260 |
| 2 | 🇮🇳 IN | 3769 |
| 3 | 🇪🇸 ES | 3768 |
| 4 | 🇦🇺 AU | 3570 |
| 5 | 🇧🇷 BR | 2996 |
| 6 | 🇯🇵 JP | 2809 |
| 7 | 🇮🇹 IT | 2803 |
| 8 | 🇩🇪 DE | 2788 |
| 9 | 🇨🇦 CA | 2592 |
| 10 | 🇨🇴 CO | 2398 |
| 11 | 🇬🇧 GB | 2165 |
| 12 | 🇫🇷 FR | 2022 |
| 13 | 🇲🇽 MX | 1601 |
| 14 | 🇬🇷 GR | 1579 |
| 15 | 🇨🇭 CH | 1468 |
| 16 | 🇳🇴 NO | 1407 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1081 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 938 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 833 |
| 25 | 🇬🇹 GT | 800 |
| 26 | 🇲🇦 MA | 641 |
| 27 | 🇲🇪 ME | 554 |
| 28 | 🇳🇱 NL | 529 |
| 29 | 🇲🇴 MO | 497 |
| 30 | 🇧🇸 BS | 456 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1188 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 859 |
| 4 | El Dorado International Airport |  | CO | 817 |
| 5 | Indira Gandhi International Airport |  | IN | 804 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 782 |
| 7 | Guaymaral Airport |  | CO | 710 |
| 8 | Harry Reid International Airport |  | US | 671 |
| 9 | Zurich Airport |  | CH | 615 |
| 10 | La Aurora Airport |  | GT | 597 |
| 11 | Frankfurt am Main International Airport |  | DE | 595 |
| 12 | Chicago O'Hare International Airport |  | US | 511 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 505 |
| 14 | Macau International Airport |  | MO | 497 |
| 15 | Kuala Lumpur International Airport |  | MY | 491 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 490 |
| 17 | Madrid Barajas International Airport |  | ES | 478 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 435 |
| 21 | Malpensa International Airport |  | IT | 432 |
| 22 | Charlotte/Douglas International Airport |  | US | 430 |
| 23 | Tenerife Norte Airport |  | ES | 415 |
| 24 | Ninoy Aquino International Airport |  | PH | 414 |
| 25 | Charles de Gaulle International Airport |  | FR | 396 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 387 |
| 27 | Salt Lake City International Airport |  | US | 381 |
| 28 | Daniel K Inouye International Airport |  | US | 378 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 364 |
| 31 | Vitoria/Foronda Airport |  | ES | 356 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 353 |
| 33 | Barcelona International Airport |  | ES | 349 |
| 34 | Reno/Tahoe International Airport |  | US | 348 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 347 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 344 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 313 |
| 40 | Viracopos International Airport |  | BR | 303 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 288 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 198 | 14m | 114 km | 388.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 157 | 21m | 244 km | 661.1 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 129 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 121 | 26m | 275 km | 573.4 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 95 | 20m | 99 km | 162.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 86 | 26m | 215 km | 318.5 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 81 | 52m | 556 km | 776.5 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 79 | 27m | 152 km | 206.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 74 | 1h 0m | 695 km | 887.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 67 | 13m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 66 | 1h 20m | 961 km | 1,094.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU897 | ERU | Daytona Beach International Airport (KDAB) | Arthur Dunn Air Park (KX21) | 2026-04-24 17:44 UTC | 2026-04-24 18:17 UTC | 32m |
| N360FA |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-04-24 17:35 UTC | 2026-04-24 18:08 UTC | 33m |
| CXK408 | CXK | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-04-24 17:34 UTC | 2026-04-24 18:08 UTC | 33m |
| QTR61K | Qatar Airways | Copenhagen Kastrup Airport (EKCH) | Queen Alia International Airport (OJAI) | 2026-04-24 14:44 UTC | 2026-04-24 18:05 UTC | 3h 21m |
| N629DC |  | Beaver County Airport (KBVI) | Youngstown Elser Metro Airport (K4G4) | 2026-04-24 17:51 UTC | 2026-04-24 18:05 UTC | 13m |
| TGCCA | TGC | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-24 17:52 UTC | 2026-04-24 18:00 UTC | 7m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-04-24 17:57 UTC | 2026-04-24 17:59 UTC | 2m |
| RAVEN51 | RAV | OK79 (OK79) | 7OK0 (7OK0) | 2026-04-24 17:29 UTC | 2026-04-24 17:56 UTC | 26m |
| N43375 |  | Sids Airport (MA52) | Fitchburg Municipal Airport (KFIT) | 2026-04-24 17:38 UTC | 2026-04-24 17:55 UTC | 17m |
| CXK581 | CXK | Sugar Land Regional Airport (KSGR) | Sugar Land Regional Airport (KSGR) | 2026-04-24 17:38 UTC | 2026-04-24 17:55 UTC | 16m |
| N8973V |  | Ocean County Airport (KMJX) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-24 16:51 UTC | 2026-04-24 17:53 UTC | 1h 2m |
| CXK258 | CXK | Morristown Municipal Airport (KMMU) | Lancaster Airport (KLNS) | 2026-04-24 16:49 UTC | 2026-04-24 17:52 UTC | 1h 2m |
| N6501W |  | 2OH9 (2OH9) | Wilmington Air Park (KILN) | 2026-04-24 17:39 UTC | 2026-04-24 17:51 UTC | 12m |
| C6056 |  | San Diego International Airport (KSAN) | San Diego International Airport (KSAN) | 2026-04-24 16:58 UTC | 2026-04-24 17:51 UTC | 52m |
| N134BF |  | KU77 (KU77) | KU77 (KU77) | 2026-04-24 17:20 UTC | 2026-04-24 17:51 UTC | 30m |
| N900VP |  | Wilkes-Barre/Scranton International Airport (KAVP) | Lehigh Valley International Airport (KABE) | 2026-04-24 17:34 UTC | 2026-04-24 17:49 UTC | 15m |
| EJA130 | EJA | John Glenn Columbus International Airport (KCMH) | Southwest Florida International Airport (KRSW) | 2026-04-24 15:47 UTC | 2026-04-24 17:45 UTC | 1h 58m |
| DCM2771 | DCM | Wilcox Airport (1MT9) | Dothan Regional Airport (KDHN) | 2026-04-24 13:16 UTC | 2026-04-24 17:45 UTC | 4h 29m |
| RYR5KN | Ryanair | Sandefjord Airport Torp (ENTO) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-24 16:11 UTC | 2026-04-24 17:44 UTC | 1h 33m |
| N565DS |  | Centennial Airport (KAPA) | 07CO (07CO) | 2026-04-24 17:29 UTC | 2026-04-24 17:44 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
