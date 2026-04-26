# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_11:02:11_UTC-green)

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

**Latest saved flight:** 2026-04-26 11:02:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-26 11:02:11 UTC

- **55,096** saved flights
- **21,704** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **55,096** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **665,735.7 tonnes** estimated CO2 emissions
- **38,593,376 km** total distance flown
- **844 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2327 |
| 2 | SkyWest Airlines | 2074 |
| 3 | IndiGo | 1253 |
| 4 | EJA | 968 |
| 5 | American Airlines | 879 |
| 6 | Southwest Airlines | 780 |
| 7 | ENY | 693 |
| 8 | Lufthansa | 673 |
| 9 | Vueling | 552 |
| 10 | AXM | 538 |
| 11 | LATAM Airlines | 527 |
| 12 | All Nippon Airways | 494 |
| 13 | AZU | 463 |
| 14 | Delta Air Lines | 453 |
| 15 | WIF | 451 |
| 16 | Swiss International | 430 |
| 17 | QLK | 429 |
| 18 | LXJ | 397 |
| 19 | Alaska Airlines | 368 |
| 20 | AEE | 366 |
| 21 | EJU | 357 |
| 22 | easyJet | 355 |
| 23 | VIV | 352 |
| 24 | Japan Airlines | 321 |
| 25 | Air France | 317 |
| 26 | Cathay Pacific | 311 |
| 27 | AXB | 295 |
| 28 | AIQ | 282 |
| 29 | JetBlue | 280 |
| 30 | GLO | 279 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 43685 |
| 2 | 🇪🇸 ES | 4011 |
| 3 | 🇮🇳 IN | 3962 |
| 4 | 🇦🇺 AU | 3726 |
| 5 | 🇧🇷 BR | 3163 |
| 6 | 🇩🇪 DE | 2992 |
| 7 | 🇯🇵 JP | 2987 |
| 8 | 🇮🇹 IT | 2986 |
| 9 | 🇨🇦 CA | 2729 |
| 10 | 🇨🇴 CO | 2478 |
| 11 | 🇬🇧 GB | 2311 |
| 12 | 🇫🇷 FR | 2165 |
| 13 | 🇲🇽 MX | 1721 |
| 14 | 🇬🇷 GR | 1642 |
| 15 | 🇨🇭 CH | 1560 |
| 16 | 🇳🇴 NO | 1463 |
| 17 | 🇲🇾 MY | 1311 |
| 18 | 🇿🇦 ZA | 1135 |
| 19 | 🇳🇿 NZ | 1039 |
| 20 | 🇹🇷 TR | 1001 |
| 21 | 🇹🇭 TH | 999 |
| 22 | 🇵🇭 PH | 944 |
| 23 | 🇰🇷 KR | 894 |
| 24 | 🇵🇱 PL | 886 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 699 |
| 27 | 🇲🇪 ME | 602 |
| 28 | 🇳🇱 NL | 570 |
| 29 | 🇲🇴 MO | 566 |
| 30 | 🇧🇸 BS | 472 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1248 |
| 2 | Tokyo International Airport |  | JP | 1017 |
| 3 | Denver International Airport |  | US | 911 |
| 4 | Indira Gandhi International Airport |  | IN | 840 |
| 5 | El Dorado International Airport |  | CO | 839 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 809 |
| 7 | Guaymaral Airport |  | CO | 747 |
| 8 | Harry Reid International Airport |  | US | 704 |
| 9 | Zurich Airport |  | CH | 661 |
| 10 | Frankfurt am Main International Airport |  | DE | 658 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 566 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 545 |
| 14 | Chicago O'Hare International Airport |  | US | 535 |
| 15 | Kuala Lumpur International Airport |  | MY | 518 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 515 |
| 17 | Madrid Barajas International Airport |  | ES | 510 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 491 |
| 19 | Malpensa International Airport |  | IT | 472 |
| 20 | Bengaluru International Airport |  | IN | 470 |
| 21 | Congonhas Airport |  | BR | 455 |
| 22 | Charlotte/Douglas International Airport |  | US | 446 |
| 23 | Tenerife Norte Airport |  | ES | 441 |
| 24 | Ninoy Aquino International Airport |  | PH | 435 |
| 25 | Charles de Gaulle International Airport |  | FR | 420 |
| 26 | Salt Lake City International Airport |  | US | 415 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 409 |
| 28 | Daniel K Inouye International Airport |  | US | 407 |
| 29 | Capua Airport |  | IT | 403 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 396 |
| 31 | Vitoria/Foronda Airport |  | ES | 379 |
| 32 | Barcelona International Airport |  | ES | 374 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 365 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 364 |
| 35 | Reno/Tahoe International Airport |  | US | 364 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 359 |
| 37 | O. R. Tambo International Airport |  | ZA | 355 |
| 38 | Don Mueang International Airport |  | TH | 339 |
| 39 | Calgary International Airport |  | CA | 328 |
| 40 | Viracopos International Airport |  | BR | 322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 303 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 179 | 24m | 225 km | 694.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 174 | 21m | 244 km | 732.7 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 160 | 1h 27m | 910 km | 2,510.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 140 | 19m | 165 km | 398.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 136 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 128 | 26m | 275 km | 606.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 108 | 1h 12m | 770 km | 1,434.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 95 | 31m | 369 km | 604.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 90 | 27m | 215 km | 333.3 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 77 | 1h 41m | 1,156 km | 1,536.1 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 75 | 1h 53m | 1,304 km | 1,687.3 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 73 | 58m | 493 km | 621.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 72 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 71 | 1h 19m | 961 km | 1,176.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-04-26 10:51 UTC | 2026-04-26 11:02 UTC | 10m |
| SXARI | SXA | Milos Airport (LGML) | Syros Airport (LGSO) | 2026-04-26 10:20 UTC | 2026-04-26 10:51 UTC | 31m |
| GTI8481 | GTI | Madrid Barajas International Airport (LEMD) | Macau International Airport (VMMC) | 2026-04-25 19:58 UTC | 2026-04-26 10:51 UTC | 14h 52m |
| SRG387 | SRG | MOD St. Athan (EGDX) | MOD St. Athan (EGDX) | 2026-04-26 10:44 UTC | 2026-04-26 10:47 UTC | 2m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-04-25 20:25 UTC | 2026-04-26 10:34 UTC | 14h 8m |
| SRG387 | SRG | Shobdon Aerodrome (EGBS) | MOD St. Athan (EGDX) | 2026-04-26 09:40 UTC | 2026-04-26 10:32 UTC | 51m |
| N911MN |  | Pierre Regional Airport (KPIR) | Murdo Municipal Airport (K8F6) | 2026-04-26 10:07 UTC | 2026-04-26 10:23 UTC | 15m |
| LHX3VJ | LHX | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-04-26 09:27 UTC | 2026-04-26 10:16 UTC | 49m |
| RYR6GM | Ryanair | Memmingen Allgau Airport (EDJA) | Visoko Sport Airfield (LQVI) | 2026-04-26 09:15 UTC | 2026-04-26 10:13 UTC | 57m |
| IBEPP | Iberia | Biella / Cerrione Airport (LILE) | Biella / Cerrione Airport (LILE) | 2026-04-26 10:10 UTC | 2026-04-26 10:13 UTC | 3m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-25 19:14 UTC | 2026-04-26 10:13 UTC | 14h 58m |
| EZY38KQ | easyJet | Nantes Atlantique Airport (LFRS) | London Gatwick Airport (EGKK) | 2026-04-26 09:18 UTC | 2026-04-26 10:11 UTC | 52m |
| SWR5ZM | Swiss International | Zurich Airport (LSZH) | Stockholm-Arlanda Airport (ESSA) | 2026-04-26 07:58 UTC | 2026-04-26 10:10 UTC | 2h 12m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-25 20:04 UTC | 2026-04-26 10:10 UTC | 14h 5m |
| LOT577 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Visoko Sport Airfield (LQVI) | 2026-04-26 08:57 UTC | 2026-04-26 10:07 UTC | 1h 9m |
| RUK1711 | RUK | Manchester Airport (EGCC) | Bassatine Airport (GMFM) | 2026-04-26 07:24 UTC | 2026-04-26 10:06 UTC | 2h 42m |
| EZY74AJ | easyJet | London Gatwick Airport (EGKK) | Bari / Palese International Airport (LIBD) | 2026-04-26 07:38 UTC | 2026-04-26 10:06 UTC | 2h 27m |
| AUA62J | Austrian Airlines | Vienna International Airport (LOWW) | Dubrovnik Airport (LDDU) | 2026-04-26 09:08 UTC | 2026-04-26 10:04 UTC | 55m |
| RYR6UD | Ryanair | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Tivat Airport (LYTV) | 2026-04-26 09:08 UTC | 2026-04-26 10:03 UTC | 54m |
| DLH6RK | Lufthansa | Frankfurt am Main International Airport (EDDF) | Napoli / Capodichino International Airport (LIRN) | 2026-04-26 08:33 UTC | 2026-04-26 10:03 UTC | 1h 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
