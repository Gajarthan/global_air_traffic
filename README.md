# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_13:38:21_UTC-green)

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

**Latest saved flight:** 2026-05-03 13:38:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 13:38:21 UTC

- **65,695** saved flights
- **24,867** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,695** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **806,692.4 tonnes** estimated CO2 emissions
- **46,764,778 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2797 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1527 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1012 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 847 |
| 8 | ENY | 806 |
| 9 | Vueling | 649 |
| 10 | AXM | 645 |
| 11 | LATAM Airlines | 613 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 547 |
| 14 | WIF | 545 |
| 15 | AZU | 528 |
| 16 | QLK | 513 |
| 17 | Swiss International | 504 |
| 18 | LXJ | 471 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 437 |
| 21 | AEE | 429 |
| 22 | EJU | 425 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 395 |
| 25 | Japan Airlines | 388 |
| 26 | Air France | 385 |
| 27 | AXB | 369 |
| 28 | AIQ | 339 |
| 29 | CXK | 334 |
| 30 | GLO | 318 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51770 |
| 2 | 🇪🇸 ES | 4822 |
| 3 | 🇮🇳 IN | 4799 |
| 4 | 🇦🇺 AU | 4406 |
| 5 | 🇧🇷 BR | 3688 |
| 6 | 🇩🇪 DE | 3683 |
| 7 | 🇯🇵 JP | 3595 |
| 8 | 🇮🇹 IT | 3588 |
| 9 | 🇨🇦 CA | 3205 |
| 10 | 🇬🇧 GB | 2842 |
| 11 | 🇨🇴 CO | 2647 |
| 12 | 🇫🇷 FR | 2605 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1975 |
| 15 | 🇨🇭 CH | 1849 |
| 16 | 🇳🇴 NO | 1783 |
| 17 | 🇲🇾 MY | 1588 |
| 18 | 🇿🇦 ZA | 1344 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1211 |
| 21 | 🇹🇷 TR | 1189 |
| 22 | 🇵🇭 PH | 1106 |
| 23 | 🇵🇱 PL | 1079 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1003 |
| 26 | 🇲🇦 MA | 808 |
| 27 | 🇲🇴 MO | 740 |
| 28 | 🇲🇪 ME | 715 |
| 29 | 🇳🇱 NL | 698 |
| 30 | 🇮🇩 ID | 567 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 1001 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 962 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 843 |
| 8 | Guaymaral Airport |  | CO | 842 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 783 |
| 11 | La Aurora Airport |  | GT | 752 |
| 12 | Macau International Airport |  | MO | 740 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Kuala Lumpur International Airport |  | MY | 632 |
| 15 | Madrid Barajas International Airport |  | ES | 626 |
| 16 | Chicago O'Hare International Airport |  | US | 624 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 586 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 567 |
| 21 | Congonhas Airport |  | BR | 530 |
| 22 | Tenerife Norte Airport |  | ES | 526 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Charles de Gaulle International Airport |  | FR | 516 |
| 25 | Salt Lake City International Airport |  | US | 515 |
| 26 | Ninoy Aquino International Airport |  | PH | 503 |
| 27 | Capua Airport |  | IT | 496 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 486 |
| 29 | Daniel K Inouye International Airport |  | US | 482 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 449 |
| 32 | Vitoria/Foronda Airport |  | ES | 440 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 438 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 438 |
| 35 | O. R. Tambo International Airport |  | ZA | 423 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 411 |
| 38 | Amsterdam Airport Schiphol |  | NL | 409 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 347 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 223 | 21m | 244 km | 939.0 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 163 | 20m | 165 km | 463.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 155 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 116 | 21m | 99 km | 198.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 107 | 20m | 250 km | 462.2 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 104 | 28m | 152 km | 271.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 102 | 27m | 215 km | 377.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 99 | 20m | 147 km | 250.5 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 93 | 57m | 493 km | 791.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 90 | 14m | 154 km | 238.5 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 86 | 1h 42m | 1,423 km | 2,110.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKDUD23 | OKD | Bubovice Airport (LKBU) | Bubovice Airport (LKBU) | 2026-05-03 13:28 UTC | 2026-05-03 13:38 UTC | 10m |
| N2108L |  | Dekalb-Peachtree Airport (KPDK) | Barrow County Airport (KWDR) | 2026-05-03 13:12 UTC | 2026-05-03 13:37 UTC | 25m |
|  |  | Langtang Airport (VNLT) | Tribhuvan International Airport (VNKT) | 2026-05-03 13:22 UTC | 2026-05-03 13:22 UTC | 0m |
| N8185R |  | Plant City Airport (KPCM) | Zephyrhills Municipal Airport (KZPH) | 2026-05-03 12:37 UTC | 2026-05-03 13:21 UTC | 44m |
| N406BL |  | Charleston Afb/International Airport (KCHS) | Beaufort Executive Airport (KARW) | 2026-05-03 12:41 UTC | 2026-05-03 13:16 UTC | 35m |
| N510BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-05-03 12:45 UTC | 2026-05-03 13:15 UTC | 29m |
|  |  | Flomaton Airport (0AL5) | Monroe County Aeroplex Airport (KMVC) | 2026-05-03 12:56 UTC | 2026-05-03 13:11 UTC | 15m |
| DEQHS | DEQ | Meschede-Schuren Airport (EDKM) | Meschede-Schuren Airport (EDKM) | 2026-05-03 13:01 UTC | 2026-05-03 13:11 UTC | 9m |
| N955SC |  | Grand Prairie Municipal Airport (KGPM) | C David Campbell Field-Corsicana Municipal Airport (KCRS) | 2026-05-03 12:36 UTC | 2026-05-03 13:07 UTC | 30m |
| C6506 |  | Atlantic City International Airport (KACY) | 8NJ0 (8NJ0) | 2026-05-03 12:51 UTC | 2026-05-03 13:06 UTC | 15m |
| N314LM |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-03 12:39 UTC | 2026-05-03 13:01 UTC | 22m |
| ECODU | ECO | Valencia Airport (LEVC) | A Coruna Airport (LECO) | 2026-05-03 11:40 UTC | 2026-05-03 12:51 UTC | 1h 10m |
| FGJBC | FGJ | Quiberon Airport (LFEQ) | Quiberon Airport (LFEQ) | 2026-05-03 12:41 UTC | 2026-05-03 12:50 UTC | 8m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-03 12:21 UTC | 2026-05-03 12:45 UTC | 24m |
| BAG12 | BAG | Voslau Airport (LOAV) | Frankfurt-Egelsbach Airport (EDFE) | 2026-05-03 11:19 UTC | 2026-05-03 12:45 UTC | 1h 26m |
| RYR6NZ | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Palermo / Bocca Di Falco Airport (LICP) | 2026-05-03 11:48 UTC | 2026-05-03 12:45 UTC | 57m |
| RYR95ND | Ryanair | Barcelona International Airport (LEBL) | London Luton Airport (EGGW) | 2026-05-03 10:54 UTC | 2026-05-03 12:44 UTC | 1h 50m |
| N655EE |  | Arlington Municipal Airport (KGKY) | Abaco I Walker C Airport (MYAW) | 2026-05-03 10:25 UTC | 2026-05-03 12:43 UTC | 2h 17m |
| HAF403 | HAF | Elefsis Airport (LGEL) | Aktion National Airport (LGPZ) | 2026-05-03 12:02 UTC | 2026-05-03 12:42 UTC | 40m |
| N915SH |  | Joe Foss Field (KFSD) | Platte Municipal Airport (K1D3) | 2026-05-03 12:12 UTC | 2026-05-03 12:41 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
