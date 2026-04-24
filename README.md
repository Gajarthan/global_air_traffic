# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_21:57:43_UTC-green)

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

**Latest saved flight:** 2026-04-24 21:57:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 21:57:43 UTC

- **52,717** saved flights
- **21,051** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **52,717** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **629,925.7 tonnes** estimated CO2 emissions
- **36,517,431 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2216 |
| 2 | SkyWest Airlines | 1994 |
| 3 | IndiGo | 1196 |
| 4 | EJA | 935 |
| 5 | American Airlines | 852 |
| 6 | Southwest Airlines | 751 |
| 7 | ENY | 668 |
| 8 | Lufthansa | 614 |
| 9 | Vueling | 529 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 506 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 446 |
| 14 | WIF | 437 |
| 15 | Delta Air Lines | 436 |
| 16 | QLK | 412 |
| 17 | Swiss International | 402 |
| 18 | LXJ | 392 |
| 19 | AEE | 355 |
| 20 | Alaska Airlines | 348 |
| 21 | VIV | 335 |
| 22 | easyJet | 333 |
| 23 | EJU | 332 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 303 |
| 26 | AXB | 280 |
| 27 | Cathay Pacific | 278 |
| 28 | JetBlue | 272 |
| 29 | United Airlines | 272 |
| 30 | GLO | 267 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42117 |
| 2 | 🇪🇸 ES | 3806 |
| 3 | 🇮🇳 IN | 3770 |
| 4 | 🇦🇺 AU | 3571 |
| 5 | 🇧🇷 BR | 3045 |
| 6 | 🇮🇹 IT | 2826 |
| 7 | 🇯🇵 JP | 2809 |
| 8 | 🇩🇪 DE | 2800 |
| 9 | 🇨🇦 CA | 2634 |
| 10 | 🇨🇴 CO | 2433 |
| 11 | 🇬🇧 GB | 2189 |
| 12 | 🇫🇷 FR | 2045 |
| 13 | 🇲🇽 MX | 1627 |
| 14 | 🇬🇷 GR | 1587 |
| 15 | 🇨🇭 CH | 1474 |
| 16 | 🇳🇴 NO | 1420 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1087 |
| 19 | 🇳🇿 NZ | 990 |
| 20 | 🇹🇷 TR | 948 |
| 21 | 🇹🇭 TH | 943 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 839 |
| 25 | 🇬🇹 GT | 814 |
| 26 | 🇲🇦 MA | 651 |
| 27 | 🇲🇪 ME | 561 |
| 28 | 🇳🇱 NL | 533 |
| 29 | 🇲🇴 MO | 506 |
| 30 | 🇧🇸 BS | 462 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1208 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 876 |
| 4 | El Dorado International Airport |  | CO | 826 |
| 5 | Indira Gandhi International Airport |  | IN | 805 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 788 |
| 7 | Guaymaral Airport |  | CO | 726 |
| 8 | Harry Reid International Airport |  | US | 681 |
| 9 | Zurich Airport |  | CH | 618 |
| 10 | La Aurora Airport |  | GT | 608 |
| 11 | Frankfurt am Main International Airport |  | DE | 601 |
| 12 | Chicago O'Hare International Airport |  | US | 521 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 518 |
| 14 | Macau International Airport |  | MO | 506 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 503 |
| 16 | Kuala Lumpur International Airport |  | MY | 491 |
| 17 | Madrid Barajas International Airport |  | ES | 488 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 449 |
| 20 | Congonhas Airport |  | BR | 440 |
| 21 | Malpensa International Airport |  | IT | 439 |
| 22 | Charlotte/Douglas International Airport |  | US | 431 |
| 23 | Tenerife Norte Airport |  | ES | 415 |
| 24 | Ninoy Aquino International Airport |  | PH | 414 |
| 25 | Charles de Gaulle International Airport |  | FR | 399 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 395 |
| 27 | Salt Lake City International Airport |  | US | 391 |
| 28 | Daniel K Inouye International Airport |  | US | 382 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 378 |
| 30 | Capua Airport |  | IT | 369 |
| 31 | Vitoria/Foronda Airport |  | ES | 358 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 33 | Reno/Tahoe International Airport |  | US | 355 |
| 34 | Barcelona International Airport |  | ES | 354 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 350 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 349 |
| 37 | O. R. Tambo International Airport |  | ZA | 343 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 318 |
| 40 | Viracopos International Airport |  | BR | 309 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 293 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 158 | 21m | 244 km | 665.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 131 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 123 | 26m | 275 km | 582.8 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 87 | 27m | 215 km | 322.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 83 | 20m | 147 km | 210.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 81 | 27m | 152 km | 211.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 75 | 1h 41m | 1,156 km | 1,496.2 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 0m | 695 km | 899.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 73 | 13m | 99 km | 125.2 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 53m | 1,304 km | 1,552.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 68 | 24m | 55 km | 64.6 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 67 | 1h 20m | 961 km | 1,110.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N30626 |  | San Marcos Regional Airport (KHYI) | Roger M Dreyer Memorial Airport (KT20) | 2026-04-24 21:22 UTC | 2026-04-24 21:57 UTC | 34m |
| N62AZ |  | Marina Municipal Airport (KOAR) | Sacramento Executive Airport (KSAC) | 2026-04-24 21:07 UTC | 2026-04-24 21:55 UTC | 48m |
| THY6216 | Turkish Airlines | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-23 18:39 UTC | 2026-04-24 21:49 UTC | 27h 10m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-04-24 11:13 UTC | 2026-04-24 21:47 UTC | 10h 34m |
| N851MH |  | Long Beach (Daugherty Field) Airport (KLGB) | Catalina Airport (KAVX) | 2026-04-24 21:33 UTC | 2026-04-24 21:46 UTC | 13m |
| LXJ339 | LXJ | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-04-24 21:44 UTC | 2026-04-24 21:45 UTC | 1m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-24 10:37 UTC | 2026-04-24 21:44 UTC | 11h 6m |
| N29WN |  | Peter O Knight Airport (KTPF) | Peter O Knight Airport (KTPF) | 2026-04-24 21:03 UTC | 2026-04-24 21:42 UTC | 39m |
| CRK081 | CRK | Vancouver International Airport (CYVR) | Macau International Airport (VMMC) | 2026-04-24 08:51 UTC | 2026-04-24 21:41 UTC | 12h 49m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-24 20:48 UTC | 2026-04-24 21:35 UTC | 47m |
| CPA085 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-24 07:10 UTC | 2026-04-24 21:35 UTC | 14h 24m |
| CXK477 | CXK | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-04-24 20:48 UTC | 2026-04-24 21:30 UTC | 41m |
| VAL791 | VAL | Pokemouche Airport (CDA4) | Boston Brook Airport (CCJ3) | 2026-04-24 21:03 UTC | 2026-04-24 21:28 UTC | 25m |
| ARZ685 | ARZ | Mid-Way Regional Airport (KJWY) | Boyd Airport (TX36) | 2026-04-24 20:45 UTC | 2026-04-24 21:27 UTC | 41m |
| ZKLTL | ZKL | New Plymouth Airport (NZNP) | New Plymouth Airport (NZNP) | 2026-04-24 19:33 UTC | 2026-04-24 21:26 UTC | 1h 53m |
| N8502V |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-24 20:42 UTC | 2026-04-24 21:26 UTC | 43m |
| N239J |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Santa Monica Municipal Airport (KSMO) | 2026-04-24 21:09 UTC | 2026-04-24 21:25 UTC | 16m |
| TMN31 | TMN | Melbourne International Airport (YMML) | Chek Lap Kok International Airport (VHHH) | 2026-04-24 12:35 UTC | 2026-04-24 21:24 UTC | 8h 48m |
| N4347R |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-24 20:44 UTC | 2026-04-24 21:20 UTC | 35m |
| DOC42 | DOC | Trondheim Airport Vaernes (ENVA) | Trondheim Airport Vaernes (ENVA) | 2026-04-24 21:14 UTC | 2026-04-24 21:18 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
