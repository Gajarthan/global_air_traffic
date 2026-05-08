# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_17:03:53_UTC-green)

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

**Latest saved flight:** 2026-05-08 17:03:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 17:03:53 UTC

- **73,640** saved flights
- **27,273** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **73,640** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **906,042.0 tonnes** estimated CO2 emissions
- **52,524,176 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3169 |
| 2 | SkyWest Airlines | 2723 |
| 3 | IndiGo | 1662 |
| 4 | EJA | 1351 |
| 5 | American Airlines | 1142 |
| 6 | Southwest Airlines | 1066 |
| 7 | Lufthansa | 961 |
| 8 | ENY | 920 |
| 9 | Vueling | 719 |
| 10 | AXM | 694 |
| 11 | LATAM Airlines | 683 |
| 12 | WIF | 643 |
| 13 | Delta Air Lines | 639 |
| 14 | All Nippon Airways | 605 |
| 15 | AZU | 592 |
| 16 | QLK | 573 |
| 17 | Swiss International | 563 |
| 18 | LXJ | 542 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 486 |
| 21 | EJU | 475 |
| 22 | AEE | 471 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 451 |
| 25 | Japan Airlines | 435 |
| 26 | Air France | 429 |
| 27 | AXB | 411 |
| 28 | CXK | 373 |
| 29 | AIQ | 366 |
| 30 | MXY | 355 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58936 |
| 2 | 🇪🇸 ES | 5330 |
| 3 | 🇮🇳 IN | 5220 |
| 4 | 🇦🇺 AU | 4907 |
| 5 | 🇩🇪 DE | 4143 |
| 6 | 🇧🇷 BR | 4121 |
| 7 | 🇮🇹 IT | 4034 |
| 8 | 🇯🇵 JP | 3876 |
| 9 | 🇨🇦 CA | 3667 |
| 10 | 🇬🇧 GB | 3170 |
| 11 | 🇫🇷 FR | 2923 |
| 12 | 🇨🇴 CO | 2684 |
| 13 | 🇲🇽 MX | 2291 |
| 14 | 🇬🇷 GR | 2184 |
| 15 | 🇳🇴 NO | 2063 |
| 16 | 🇨🇭 CH | 2009 |
| 17 | 🇲🇾 MY | 1735 |
| 18 | 🇿🇦 ZA | 1443 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1323 |
| 21 | 🇹🇭 TH | 1316 |
| 22 | 🇵🇱 PL | 1237 |
| 23 | 🇵🇭 PH | 1198 |
| 24 | 🇬🇹 GT | 1155 |
| 25 | 🇰🇷 KR | 1151 |
| 26 | 🇲🇦 MA | 874 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 789 |
| 29 | 🇳🇱 NL | 772 |
| 30 | 🇧🇸 BS | 620 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1627 |
| 2 | Tokyo International Airport |  | JP | 1302 |
| 3 | Denver International Airport |  | US | 1226 |
| 4 | Indira Gandhi International Airport |  | IN | 1100 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1069 |
| 6 | Frankfurt am Main International Airport |  | DE | 956 |
| 7 | Harry Reid International Airport |  | US | 914 |
| 8 | Guaymaral Airport |  | CO | 879 |
| 9 | El Dorado International Airport |  | CO | 878 |
| 10 | Zurich Airport |  | CH | 871 |
| 11 | La Aurora Airport |  | GT | 861 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 738 |
| 14 | Chicago O'Hare International Airport |  | US | 709 |
| 15 | Kuala Lumpur International Airport |  | MY | 696 |
| 16 | Madrid Barajas International Airport |  | ES | 690 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 648 |
| 18 | Bengaluru International Airport |  | IN | 640 |
| 19 | Malpensa International Airport |  | IT | 639 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 637 |
| 21 | Salt Lake City International Airport |  | US | 597 |
| 22 | Congonhas Airport |  | BR | 583 |
| 23 | Charlotte/Douglas International Airport |  | US | 579 |
| 24 | Capua Airport |  | IT | 574 |
| 25 | Charles de Gaulle International Airport |  | FR | 573 |
| 26 | Tenerife Norte Airport |  | ES | 558 |
| 27 | Ninoy Aquino International Airport |  | PH | 543 |
| 28 | Daniel K Inouye International Airport |  | US | 536 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 530 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 508 |
| 31 | Barcelona International Airport |  | ES | 508 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 500 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 495 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 481 |
| 35 | Vitoria/Foronda Airport |  | ES | 480 |
| 36 | Amsterdam Airport Schiphol |  | NL | 464 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 463 |
| 38 | Don Mueang International Airport |  | TH | 462 |
| 39 | O. R. Tambo International Airport |  | ZA | 453 |
| 40 | Calgary International Airport |  | CA | 439 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 365 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 268 | 1h 8m | 706 km | 3,262.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 258 | 21m | 244 km | 1,086.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 207 | 28m | 304 km | 1,085.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 203 | 1h 27m | 910 km | 3,185.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 183 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 178 | 20m | 165 km | 506.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 175 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 112 | 27m | 215 km | 414.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 111 | 20m | 147 km | 280.9 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 101 | 1h 2m | 695 km | 1,210.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 99 | 1h 42m | 1,423 km | 2,429.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 95 | 23m | 55 km | 90.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Bodø Airport (ENBO) | ENEN (ENEN) | 91 | 14m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KSF12 | KSF | Kent State University Airport (K1G3) | Portage County Airport (KPOV) | 2026-05-08 16:10 UTC | 2026-05-08 17:03 UTC | 53m |
| DAL161 | Delta Air Lines | Amsterdam Airport Schiphol (EHAM) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 08:10 UTC | 2026-05-08 17:01 UTC | 8h 50m |
| N509JE |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-05-08 16:37 UTC | 2026-05-08 17:00 UTC | 22m |
| CXK434 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-08 16:24 UTC | 2026-05-08 16:59 UTC | 35m |
| DMRRB | DMR | Brandenburg-Muhlenfeld Airport (EDBE) | Brandenburg-Muhlenfeld Airport (EDBE) | 2026-05-08 14:31 UTC | 2026-05-08 16:52 UTC | 2h 20m |
| FLABY51 | FLA | Laughlin Afb Aux Nr 1 Airport (KT70) | 6TA4 (6TA4) | 2026-05-08 16:24 UTC | 2026-05-08 16:48 UTC | 24m |
| N279CG |  | Delaware Airpark (K33N) | Delaware Airpark (K33N) | 2026-05-08 16:22 UTC | 2026-05-08 16:48 UTC | 26m |
| N4841Y |  | Kelly Air Park (CO15) | Kelly Air Park (CO15) | 2026-05-08 16:25 UTC | 2026-05-08 16:44 UTC | 19m |
| N303RH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-05-08 16:17 UTC | 2026-05-08 16:43 UTC | 26m |
| N350WC |  | TE92 (TE92) | Lubbock Executive Airpark (KF82) | 2026-05-08 15:56 UTC | 2026-05-08 16:43 UTC | 47m |
| TWY68 | TWY | Farnborough Airport (EGLF) | Bangor International Airport (KBGR) | 2026-05-08 10:06 UTC | 2026-05-08 16:42 UTC | 6h 35m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-08 16:28 UTC | 2026-05-08 16:40 UTC | 11m |
| DLH3UV | Lufthansa | Munster Osnabruck Airport (EDDG) | Nordlingen Airport (EDNO) | 2026-05-08 15:44 UTC | 2026-05-08 16:35 UTC | 50m |
| DLH8M | Lufthansa | Hamburg Airport (EDDH) | Ingolstadt Manching Airport (ETSI) | 2026-05-08 15:34 UTC | 2026-05-08 16:35 UTC | 1h 1m |
| N10BB |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-05-08 16:26 UTC | 2026-05-08 16:35 UTC | 9m |
| N22265 |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-08 16:07 UTC | 2026-05-08 16:34 UTC | 27m |
| N6098X |  | Carson City Airport (KCXP) | Lee Vining Airport (KO24) | 2026-05-08 15:58 UTC | 2026-05-08 16:33 UTC | 34m |
| N824KC |  | Livermore Municipal Airport (KLVK) | Tracy Municipal Airport (KTCY) | 2026-05-08 16:17 UTC | 2026-05-08 16:32 UTC | 15m |
| N608CA |  | Vance Brand Airport (KLMO) | Laramie Regional Airport (KLAR) | 2026-05-08 16:05 UTC | 2026-05-08 16:32 UTC | 27m |
| SSF342 | SSF | Borisoglebskoye Airport (UWKG) | Talagi Airport (ULAA) | 2026-05-07 20:56 UTC | 2026-05-08 16:29 UTC | 19h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
