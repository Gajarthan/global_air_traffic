# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_07:43:12_UTC-green)

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

**Latest saved flight:** 2026-04-18 07:43:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 07:43:12 UTC

- **40,722** saved flights
- **17,308** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,722** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **490,430.6 tonnes** estimated CO2 emissions
- **28,430,757 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1702 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 996 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 422 |
| 9 | Vueling | 405 |
| 10 | LATAM Airlines | 400 |
| 11 | Lufthansa | 390 |
| 12 | All Nippon Airways | 362 |
| 13 | AZU | 361 |
| 14 | Delta Air Lines | 347 |
| 15 | QLK | 341 |
| 16 | LXJ | 325 |
| 17 | WIF | 316 |
| 18 | Swiss International | 307 |
| 19 | Alaska Airlines | 276 |
| 20 | AEE | 270 |
| 21 | EJU | 266 |
| 22 | easyJet | 265 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 252 |
| 25 | Air France | 228 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 208 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32291 |
| 2 | 🇮🇳 IN | 3036 |
| 3 | 🇪🇸 ES | 2997 |
| 4 | 🇦🇺 AU | 2896 |
| 5 | 🇧🇷 BR | 2409 |
| 6 | 🇯🇵 JP | 2215 |
| 7 | 🇮🇹 IT | 2110 |
| 8 | 🇩🇪 DE | 2034 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1643 |
| 12 | 🇫🇷 FR | 1543 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1221 |
| 15 | 🇨🇭 CH | 1105 |
| 16 | 🇲🇾 MY | 1026 |
| 17 | 🇳🇴 NO | 1005 |
| 18 | 🇳🇿 NZ | 844 |
| 19 | 🇿🇦 ZA | 831 |
| 20 | 🇵🇭 PH | 744 |
| 21 | 🇹🇭 TH | 723 |
| 22 | 🇹🇷 TR | 707 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 662 |
| 25 | 🇵🇱 PL | 626 |
| 26 | 🇲🇦 MA | 501 |
| 27 | 🇳🇱 NL | 411 |
| 28 | 🇲🇪 ME | 406 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 375 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 756 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 677 |
| 5 | Indira Gandhi International Airport |  | IN | 653 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 607 |
| 7 | Harry Reid International Airport |  | US | 529 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 486 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 12 | Kuala Lumpur International Airport |  | MY | 402 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 391 |
| 16 | Macau International Airport |  | MO | 372 |
| 17 | Madrid Barajas International Airport |  | ES | 369 |
| 18 | Bengaluru International Airport |  | IN | 359 |
| 19 | Charlotte/Douglas International Airport |  | US | 358 |
| 20 | Tenerife Norte Airport |  | ES | 358 |
| 21 | Frankfurt am Main International Airport |  | DE | 355 |
| 22 | Congonhas Airport |  | BR | 353 |
| 23 | Ninoy Aquino International Airport |  | PH | 346 |
| 24 | Malpensa International Airport |  | IT | 328 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 306 |
| 28 | Charles de Gaulle International Airport |  | FR | 297 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 292 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Vitoria/Foronda Airport |  | ES | 282 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 281 |
| 33 | Reno/Tahoe International Airport |  | US | 280 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 268 |
| 36 | O. R. Tambo International Airport |  | ZA | 267 |
| 37 | Barcelona International Airport |  | ES | 258 |
| 38 | Calgary International Airport |  | CA | 247 |
| 39 | Viracopos International Airport |  | BR | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 190 | 1h 7m | 706 km | 2,313.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 148 | 24m | 225 km | 574.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 119 | 28m | 304 km | 623.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 117 | 1h 27m | 910 km | 1,836.0 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 109 | 21m | 244 km | 459.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 108 | 19m | 165 km | 307.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 107 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 96 | 26m | 275 km | 454.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 88 | 54m | 546 km | 828.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 82 | 44m | 452 km | 639.1 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 74 | 31m | 369 km | 471.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 64 | 20m | 147 km | 162.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 63 | 20m | 250 km | 272.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 62 | 1h 41m | 1,423 km | 1,521.6 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 57 | 59m | 695 km | 683.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-18 07:27 UTC | 2026-04-18 07:43 UTC | 15m |
| POK | POK | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-18 07:22 UTC | 2026-04-18 07:37 UTC | 14m |
| BRU783 | BRU | Minsk International Airport (UMMS) | Beslan Airport (URMO) | 2026-04-18 04:24 UTC | 2026-04-18 07:29 UTC | 3h 5m |
| DMYLF | DMY | Griesau Airport (EDPG) | Griesau Airport (EDPG) | 2026-04-18 07:17 UTC | 2026-04-18 07:27 UTC | 10m |
|  |  | Megeve Airport (LFHM) | Bex Airport (LSGB) | 2026-04-18 07:27 UTC | 2026-04-18 07:27 UTC | 0m |
| IGO1153 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-04-18 06:00 UTC | 2026-04-18 07:17 UTC | 1h 17m |
| EZY48TH | easyJet | London Gatwick Airport (EGKK) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-18 05:35 UTC | 2026-04-18 07:12 UTC | 1h 37m |
| SEH470 | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-18 06:46 UTC | 2026-04-18 07:05 UTC | 18m |
| RYR6406 | Ryanair | Alghero / Fertilia Airport (LIEA) | Decimomannu Airport (LIED) | 2026-04-18 06:49 UTC | 2026-04-18 07:03 UTC | 13m |
| SIS49 | SIS | Van Nuys Airport (KVNY) | Fairbanks International Airport (PAFA) | 2026-04-18 02:12 UTC | 2026-04-18 06:59 UTC | 4h 46m |
| HBZPA | HBZ | LSMF (LSMF) | Sion Airport (LSGS) | 2026-04-18 06:05 UTC | 2026-04-18 06:58 UTC | 53m |
| PXT578 | PXT | San Luis Obispo County Regional Airport (KSBP) | Reno/Tahoe International Airport (KRNO) | 2026-04-18 06:12 UTC | 2026-04-18 06:58 UTC | 46m |
| QTR818 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-18 00:14 UTC | 2026-04-18 06:55 UTC | 6h 41m |
| OAL2MS | OAL | Eleftherios Venizelos International Airport (LGAV) | Milos Airport (LGML) | 2026-04-18 06:35 UTC | 2026-04-18 06:52 UTC | 17m |
| T7ACA |  | Niksic Airport (LYNK) | Hvar Private Airport (LDSH) | 2026-04-18 06:33 UTC | 2026-04-18 06:51 UTC | 18m |
| AM324 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-04-18 06:25 UTC | 2026-04-18 06:47 UTC | 22m |
| N232LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-04-18 06:19 UTC | 2026-04-18 06:46 UTC | 27m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-18 06:11 UTC | 2026-04-18 06:43 UTC | 32m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Langtang Airport (VNLT) | 2026-04-18 03:34 UTC | 2026-04-18 06:43 UTC | 3h 8m |
| TRA97X | TRA | Rotterdam Airport (EHRD) | Otocac Airport (LDRO) | 2026-04-18 05:16 UTC | 2026-04-18 06:43 UTC | 1h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
