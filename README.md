# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_16:16:52_UTC-green)

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

**Latest saved flight:** 2026-05-07 16:16:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 16:16:52 UTC

- **72,030** saved flights
- **26,748** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,030** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **887,747.6 tonnes** estimated CO2 emissions
- **51,463,630 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3103 |
| 2 | SkyWest Airlines | 2677 |
| 3 | IndiGo | 1632 |
| 4 | EJA | 1319 |
| 5 | American Airlines | 1128 |
| 6 | Southwest Airlines | 1047 |
| 7 | Lufthansa | 925 |
| 8 | ENY | 905 |
| 9 | Vueling | 703 |
| 10 | AXM | 688 |
| 11 | LATAM Airlines | 669 |
| 12 | WIF | 617 |
| 13 | Delta Air Lines | 603 |
| 14 | All Nippon Airways | 599 |
| 15 | AZU | 581 |
| 16 | QLK | 554 |
| 17 | Swiss International | 554 |
| 18 | LXJ | 523 |
| 19 | Alaska Airlines | 507 |
| 20 | easyJet | 478 |
| 21 | AEE | 463 |
| 22 | EJU | 463 |
| 23 | Cathay Pacific | 448 |
| 24 | VIV | 445 |
| 25 | Japan Airlines | 426 |
| 26 | Air France | 422 |
| 27 | AXB | 401 |
| 28 | CXK | 361 |
| 29 | AIQ | 359 |
| 30 | JetBlue | 345 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57582 |
| 2 | 🇪🇸 ES | 5222 |
| 3 | 🇮🇳 IN | 5127 |
| 4 | 🇦🇺 AU | 4799 |
| 5 | 🇧🇷 BR | 4031 |
| 6 | 🇩🇪 DE | 4007 |
| 7 | 🇮🇹 IT | 3953 |
| 8 | 🇯🇵 JP | 3829 |
| 9 | 🇨🇦 CA | 3585 |
| 10 | 🇬🇧 GB | 3103 |
| 11 | 🇫🇷 FR | 2836 |
| 12 | 🇨🇴 CO | 2675 |
| 13 | 🇲🇽 MX | 2266 |
| 14 | 🇬🇷 GR | 2136 |
| 15 | 🇳🇴 NO | 1985 |
| 16 | 🇨🇭 CH | 1964 |
| 17 | 🇲🇾 MY | 1715 |
| 18 | 🇿🇦 ZA | 1422 |
| 19 | 🇳🇿 NZ | 1320 |
| 20 | 🇹🇭 TH | 1294 |
| 21 | 🇹🇷 TR | 1293 |
| 22 | 🇵🇱 PL | 1200 |
| 23 | 🇵🇭 PH | 1174 |
| 24 | 🇬🇹 GT | 1144 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 855 |
| 27 | 🇲🇴 MO | 842 |
| 28 | 🇲🇪 ME | 769 |
| 29 | 🇳🇱 NL | 749 |
| 30 | 🇧🇸 BS | 607 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1606 |
| 2 | Tokyo International Airport |  | JP | 1287 |
| 3 | Denver International Airport |  | US | 1202 |
| 4 | Indira Gandhi International Airport |  | IN | 1080 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1044 |
| 6 | Frankfurt am Main International Airport |  | DE | 918 |
| 7 | Harry Reid International Airport |  | US | 900 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 870 |
| 10 | Zurich Airport |  | CH | 855 |
| 11 | La Aurora Airport |  | GT | 851 |
| 12 | Macau International Airport |  | MO | 842 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 726 |
| 14 | Chicago O'Hare International Airport |  | US | 700 |
| 15 | Kuala Lumpur International Airport |  | MY | 689 |
| 16 | Madrid Barajas International Airport |  | ES | 680 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 642 |
| 18 | Malpensa International Airport |  | IT | 628 |
| 19 | Bengaluru International Airport |  | IN | 625 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 21 | Salt Lake City International Airport |  | US | 583 |
| 22 | Congonhas Airport |  | BR | 571 |
| 23 | Charlotte/Douglas International Airport |  | US | 567 |
| 24 | Capua Airport |  | IT | 567 |
| 25 | Charles de Gaulle International Airport |  | FR | 564 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 534 |
| 28 | Daniel K Inouye International Airport |  | US | 531 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 520 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 492 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 482 |
| 34 | Vitoria/Foronda Airport |  | ES | 473 |
| 35 | Don Mueang International Airport |  | TH | 454 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 453 |
| 37 | O. R. Tambo International Airport |  | ZA | 445 |
| 38 | Amsterdam Airport Schiphol |  | NL | 445 |
| 39 | Calgary International Airport |  | CA | 433 |
| 40 | Reno/Tahoe International Airport |  | US | 423 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 361 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 254 | 21m | 244 km | 1,069.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 211 | 24m | 225 km | 818.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 179 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 105 | 14m | 154 km | 278.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SHINR20 | SHI | Austin-Bergstrom International Airport (KAUS) | Fayette Regional Air Center Airport (K3T5) | 2026-05-07 15:36 UTC | 2026-05-07 16:16 UTC | 40m |
| HYDRA31 | HYD | 75OK (75OK) | Lariat Ranch Airport (OK42) | 2026-05-07 15:48 UTC | 2026-05-07 16:14 UTC | 26m |
| OXF6514 | OXF | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-05-07 15:04 UTC | 2026-05-07 16:13 UTC | 1h 9m |
| N168SP |  | French Valley Airport (KF70) | Santa Barbara Municipal Airport (KSBA) | 2026-05-07 15:18 UTC | 2026-05-07 16:13 UTC | 55m |
| RVP953 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-05-07 15:34 UTC | 2026-05-07 16:12 UTC | 37m |
| PAG983T | PAG | Thunder Bay Airport (CYQT) | Thunder Bay Airport (CYQT) | 2026-05-07 14:12 UTC | 2026-05-07 16:09 UTC | 1h 57m |
| UAL542 | United Airlines | Detroit Metro Wayne County Airport (KDTW) | Denver International Airport (KDEN) | 2026-05-07 13:21 UTC | 2026-05-07 16:07 UTC | 2h 45m |
| N192MA |  | Aurora Municipal Airport (KARR) | 2LL9 (2LL9) | 2026-05-07 15:43 UTC | 2026-05-07 16:05 UTC | 22m |
| N377RT |  | Pinyon Airport (CO43) | Crawford Airport (K99V) | 2026-05-07 15:49 UTC | 2026-05-07 16:05 UTC | 16m |
| AXEL10 | AXE | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Provo Municipal Airport (KPVU) | 2026-05-07 14:29 UTC | 2026-05-07 16:05 UTC | 1h 35m |
| N439H |  | Rhode Island Tf Green International Airport (KPVD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-07 15:41 UTC | 2026-05-07 16:02 UTC | 20m |
| N172YA |  | Essex County Airport (KCDW) | Blairstown Airport (K1N7) | 2026-05-07 15:31 UTC | 2026-05-07 16:01 UTC | 30m |
| SLICK19 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-05-07 15:36 UTC | 2026-05-07 16:01 UTC | 24m |
| LFA321 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-05-07 15:39 UTC | 2026-05-07 16:01 UTC | 21m |
| PTXHP | PTX | Fazenda Santa Ines Airport (SDJR) | Fazenda Campo Vitoria Airport (SDVA) | 2026-05-07 15:22 UTC | 2026-05-07 15:58 UTC | 35m |
| N685ST |  | 9CL5 (9CL5) | San Luis Obispo County Regional Airport (KSBP) | 2026-05-07 15:35 UTC | 2026-05-07 15:55 UTC | 20m |
| N529AB |  | Knutson Airport (4ND1) | 19ND (19ND) | 2026-05-07 12:32 UTC | 2026-05-07 15:55 UTC | 3h 22m |
| HTY238 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-05-07 15:24 UTC | 2026-05-07 15:51 UTC | 26m |
| N284PC |  | Dekalb-Peachtree Airport (KPDK) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-05-07 14:54 UTC | 2026-05-07 15:48 UTC | 53m |
| N393BW |  | Modesto City-County-Harry Sham Field (KMOD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-07 15:32 UTC | 2026-05-07 15:48 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
