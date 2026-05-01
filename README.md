# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_11:10:57_UTC-green)

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

**Latest saved flight:** 2026-05-01 11:10:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 11:10:57 UTC

- **61,851** saved flights
- **23,759** unique routes
- **124** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,851** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **755,289.7 tonnes** estimated CO2 emissions
- **43,784,910 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2591 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1416 |
| 4 | EJA | 1117 |
| 5 | American Airlines | 965 |
| 6 | Southwest Airlines | 877 |
| 7 | Lufthansa | 788 |
| 8 | ENY | 765 |
| 9 | Vueling | 609 |
| 10 | AXM | 603 |
| 11 | LATAM Airlines | 585 |
| 12 | All Nippon Airways | 548 |
| 13 | WIF | 520 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 502 |
| 16 | QLK | 498 |
| 17 | Swiss International | 480 |
| 18 | LXJ | 439 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 403 |
| 21 | easyJet | 401 |
| 22 | EJU | 395 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 378 |
| 25 | Japan Airlines | 364 |
| 26 | Air France | 359 |
| 27 | AXB | 342 |
| 28 | AIQ | 317 |
| 29 | CXK | 306 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48951 |
| 2 | 🇮🇳 IN | 4472 |
| 3 | 🇪🇸 ES | 4456 |
| 4 | 🇦🇺 AU | 4279 |
| 5 | 🇧🇷 BR | 3493 |
| 6 | 🇩🇪 DE | 3423 |
| 7 | 🇯🇵 JP | 3392 |
| 8 | 🇮🇹 IT | 3355 |
| 9 | 🇨🇦 CA | 3059 |
| 10 | 🇨🇴 CO | 2627 |
| 11 | 🇬🇧 GB | 2626 |
| 12 | 🇫🇷 FR | 2423 |
| 13 | 🇲🇽 MX | 1948 |
| 14 | 🇬🇷 GR | 1827 |
| 15 | 🇨🇭 CH | 1722 |
| 16 | 🇳🇴 NO | 1702 |
| 17 | 🇲🇾 MY | 1469 |
| 18 | 🇿🇦 ZA | 1259 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1120 |
| 21 | 🇹🇷 TR | 1093 |
| 22 | 🇵🇭 PH | 1058 |
| 23 | 🇰🇷 KR | 1004 |
| 24 | 🇵🇱 PL | 993 |
| 25 | 🇬🇹 GT | 922 |
| 26 | 🇲🇦 MA | 759 |
| 27 | 🇲🇴 MO | 697 |
| 28 | 🇲🇪 ME | 674 |
| 29 | 🇳🇱 NL | 646 |
| 30 | 🇮🇩 ID | 527 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1370 |
| 2 | Tokyo International Airport |  | JP | 1144 |
| 3 | Denver International Airport |  | US | 1025 |
| 4 | Indira Gandhi International Airport |  | IN | 942 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 897 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 822 |
| 8 | Harry Reid International Airport |  | US | 790 |
| 9 | Frankfurt am Main International Airport |  | DE | 785 |
| 10 | Zurich Airport |  | CH | 738 |
| 11 | Macau International Airport |  | MO | 697 |
| 12 | La Aurora Airport |  | GT | 691 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Chicago O'Hare International Airport |  | US | 583 |
| 15 | Kuala Lumpur International Airport |  | MY | 580 |
| 16 | Madrid Barajas International Airport |  | ES | 577 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 564 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 537 |
| 20 | Malpensa International Airport |  | IT | 535 |
| 21 | Congonhas Airport |  | BR | 504 |
| 22 | Charlotte/Douglas International Airport |  | US | 492 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Ninoy Aquino International Airport |  | PH | 480 |
| 25 | Tenerife Norte Airport |  | ES | 477 |
| 26 | Charles de Gaulle International Airport |  | FR | 477 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 460 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 448 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 446 |
| 31 | Barcelona International Airport |  | ES | 414 |
| 32 | Vitoria/Foronda Airport |  | ES | 412 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 409 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 402 |
| 35 | O. R. Tambo International Airport |  | ZA | 396 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 389 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 385 |
| 39 | Amsterdam Airport Schiphol |  | NL | 381 |
| 40 | Calgary International Airport |  | CA | 366 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 337 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 207 | 21m | 244 km | 871.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 182 | 1h 27m | 910 km | 2,856.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 178 | 28m | 304 km | 933.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 152 | 19m | 165 km | 432.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 148 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 139 | 26m | 275 km | 658.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 133 | 1h 12m | 770 km | 1,766.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 105 | 31m | 369 km | 668.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 98 | 20m | 250 km | 423.3 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 93 | 20m | 147 km | 235.3 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 82 | 14m | 154 km | 217.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 81 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GKAMY | GKA | RNAS Yeovilton (EGDY) | RNAS Yeovilton (EGDY) | 2026-05-01 11:07 UTC | 2026-05-01 11:10 UTC | 3m |
| EVA667 | EVA Air | Hartsfield/Jackson Atlanta International Airport (KATL) | Akeno Airport (RJOE) | 2026-04-30 21:04 UTC | 2026-05-01 11:05 UTC | 14h 1m |
| IOS224 | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-05-01 10:45 UTC | 2026-05-01 11:05 UTC | 20m |
| RYR97BW | Ryanair | Marseille Provence Airport (LFML) | Sevilla Airport (LEZL) | 2026-05-01 09:24 UTC | 2026-05-01 11:04 UTC | 1h 39m |
| HB2498 |  | Saanen Airport (LSGK) | Raron Airport (LSTA) | 2026-05-01 10:15 UTC | 2026-05-01 10:57 UTC | 41m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-01 10:10 UTC | 2026-05-01 10:56 UTC | 45m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-01 10:41 UTC | 2026-05-01 10:55 UTC | 13m |
| JAL2088 | Japan Airlines | Naha Airport (ROAH) | Yao Airport (RJOY) | 2026-05-01 09:22 UTC | 2026-05-01 10:49 UTC | 1h 26m |
| LOT4NJ | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Szczecin-Goleniow Solidarność Airport (EPSC) | 2026-05-01 10:02 UTC | 2026-05-01 10:46 UTC | 43m |
| HBEFT | HBE | Ambri Airport (LSPM) | Reichenbach Air Base (LSGR) | 2026-05-01 10:03 UTC | 2026-05-01 10:44 UTC | 40m |
| REH7 | REH | Nevada County Airport (KGOO) | Truckee-Tahoe Airport (KTRK) | 2026-05-01 10:22 UTC | 2026-05-01 10:42 UTC | 20m |
| HKS39 | HKS | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-05-01 10:11 UTC | 2026-05-01 10:40 UTC | 28m |
| AE951 |  | Sydney Bankstown Airport (YSBK) | Conargo Airport (YCNO) | 2026-05-01 09:34 UTC | 2026-05-01 10:40 UTC | 1h 5m |
| CHX65 | CHX | Neustadt/Aisch Airport (EDQN) | Herzogenaurach Airport (EDQH) | 2026-05-01 10:32 UTC | 2026-05-01 10:38 UTC | 6m |
| IBE0445 | Iberia | Madrid Barajas International Airport (LEMD) | San Sebastian Airport (LESO) | 2026-05-01 10:08 UTC | 2026-05-01 10:37 UTC | 28m |
| SEH8LH | SEH | Limnos Airport (LGLM) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-01 09:49 UTC | 2026-05-01 10:36 UTC | 47m |
| SKQ78 | SKQ | Burlington/Alamance Regional Airport (KBUY) | West Virginia International Yeager Airport (KCRW) | 2026-05-01 09:46 UTC | 2026-05-01 10:34 UTC | 48m |
| DLH9C | Lufthansa | Zurich Airport (LSZH) | Frankfurt am Main International Airport (EDDF) | 2026-05-01 09:46 UTC | 2026-05-01 10:34 UTC | 47m |
| AXB2053 | AXB | Bengaluru International Airport (VOBL) | Birsa Munda Airport (VERC) | 2026-05-01 08:40 UTC | 2026-05-01 10:32 UTC | 1h 52m |
| EDC869R | EDC | Oxford (Kidlington) Airport (EGTK) | Guernsey Airport (EGJB) | 2026-05-01 09:52 UTC | 2026-05-01 10:31 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
