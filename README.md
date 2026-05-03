# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_14:17:03_UTC-green)

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

**Latest saved flight:** 2026-05-03 14:17:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 14:17:03 UTC

- **65,802** saved flights
- **24,896** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,802** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **807,840.3 tonnes** estimated CO2 emissions
- **46,831,322 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2804 |
| 2 | SkyWest Airlines | 2420 |
| 3 | IndiGo | 1532 |
| 4 | EJA | 1161 |
| 5 | American Airlines | 1012 |
| 6 | Southwest Airlines | 921 |
| 7 | Lufthansa | 847 |
| 8 | ENY | 807 |
| 9 | Vueling | 652 |
| 10 | AXM | 648 |
| 11 | LATAM Airlines | 613 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 551 |
| 14 | WIF | 546 |
| 15 | AZU | 532 |
| 16 | QLK | 513 |
| 17 | Swiss International | 504 |
| 18 | LXJ | 471 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 438 |
| 21 | AEE | 429 |
| 22 | EJU | 427 |
| 23 | VIV | 411 |
| 24 | Cathay Pacific | 395 |
| 25 | Japan Airlines | 388 |
| 26 | Air France | 386 |
| 27 | AXB | 369 |
| 28 | AIQ | 339 |
| 29 | CXK | 335 |
| 30 | GLO | 320 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51825 |
| 2 | 🇪🇸 ES | 4836 |
| 3 | 🇮🇳 IN | 4812 |
| 4 | 🇦🇺 AU | 4406 |
| 5 | 🇧🇷 BR | 3703 |
| 6 | 🇩🇪 DE | 3686 |
| 7 | 🇮🇹 IT | 3598 |
| 8 | 🇯🇵 JP | 3595 |
| 9 | 🇨🇦 CA | 3209 |
| 10 | 🇬🇧 GB | 2845 |
| 11 | 🇨🇴 CO | 2649 |
| 12 | 🇫🇷 FR | 2611 |
| 13 | 🇲🇽 MX | 2079 |
| 14 | 🇬🇷 GR | 1977 |
| 15 | 🇨🇭 CH | 1851 |
| 16 | 🇳🇴 NO | 1787 |
| 17 | 🇲🇾 MY | 1594 |
| 18 | 🇿🇦 ZA | 1348 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1212 |
| 21 | 🇹🇷 TR | 1190 |
| 22 | 🇵🇭 PH | 1106 |
| 23 | 🇵🇱 PL | 1084 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1011 |
| 26 | 🇲🇦 MA | 810 |
| 27 | 🇲🇴 MO | 740 |
| 28 | 🇲🇪 ME | 717 |
| 29 | 🇳🇱 NL | 699 |
| 30 | 🇮🇩 ID | 567 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1436 |
| 2 | Tokyo International Airport |  | JP | 1212 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 1003 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 962 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 844 |
| 8 | Frankfurt am Main International Airport |  | DE | 844 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 783 |
| 11 | La Aurora Airport |  | GT | 757 |
| 12 | Macau International Airport |  | MO | 740 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Kuala Lumpur International Airport |  | MY | 635 |
| 15 | Madrid Barajas International Airport |  | ES | 627 |
| 16 | Chicago O'Hare International Airport |  | US | 625 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 590 |
| 18 | Bengaluru International Airport |  | IN | 587 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 568 |
| 21 | Congonhas Airport |  | BR | 532 |
| 22 | Tenerife Norte Airport |  | ES | 527 |
| 23 | Charlotte/Douglas International Airport |  | US | 518 |
| 24 | Charles de Gaulle International Airport |  | FR | 517 |
| 25 | Salt Lake City International Airport |  | US | 516 |
| 26 | Ninoy Aquino International Airport |  | PH | 503 |
| 27 | Capua Airport |  | IT | 497 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 486 |
| 29 | Daniel K Inouye International Airport |  | US | 482 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 467 |
| 31 | Barcelona International Airport |  | ES | 450 |
| 32 | Vitoria/Foronda Airport |  | ES | 441 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 440 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 439 |
| 35 | O. R. Tambo International Airport |  | ZA | 425 |
| 36 | Don Mueang International Airport |  | TH | 423 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 411 |
| 38 | Amsterdam Airport Schiphol |  | NL | 410 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 348 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 223 | 21m | 244 km | 939.0 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 165 | 20m | 165 km | 469.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 161 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 156 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 147 | 1h 11m | 770 km | 1,952.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 118 | 21m | 99 km | 202.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 107 | 20m | 250 km | 462.2 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 104 | 28m | 152 km | 271.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 102 | 27m | 215 km | 377.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 99 | 20m | 147 km | 250.5 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 93 | 57m | 493 km | 791.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 91 | 14m | 154 km | 241.1 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 2m | 695 km | 1,090.8 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 53m | 1,304 km | 2,024.8 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 86 | 1h 42m | 1,423 km | 2,110.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 85 | 1h 19m | 961 km | 1,408.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC211 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-05-03 13:13 UTC | 2026-05-03 14:17 UTC | 1h 3m |
| N899AA |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-05-03 13:54 UTC | 2026-05-03 14:14 UTC | 19m |
| CXK300 | CXK | Denton Enterprise Airport (KDTO) | Lazy 9 Ranch Airport (TX64) | 2026-05-03 12:49 UTC | 2026-05-03 14:06 UTC | 1h 17m |
| N503SP |  | RI20 (RI20) | Quonset State Airport (KOQU) | 2026-05-03 12:45 UTC | 2026-05-03 14:01 UTC | 1h 16m |
| N775MC |  | Skywest Inc Airport (K7T7) | 7TX5 (7TX5) | 2026-05-03 11:51 UTC | 2026-05-03 13:58 UTC | 2h 6m |
| SPOZTB | SPO | John Paul II International Airport Kraków-Balice Airport (EPKK) | Pobiednik Wielki Airport (EPKP) | 2026-05-03 13:44 UTC | 2026-05-03 13:55 UTC | 11m |
| PVL852 | PVL | Québec City Jean Lesage International Airport (CYQB) | Gaspe (Michel-Pouliot) Airport (CYGP) | 2026-05-03 12:58 UTC | 2026-05-03 13:52 UTC | 54m |
| N836CM |  | Thomaston-Upson County Airport (KOPN) | Barkley Regional Airport (KPAH) | 2026-05-03 12:52 UTC | 2026-05-03 13:51 UTC | 58m |
| CCA897 | Air China | Beijing Capital International Airport (ZBAA) | Tunoshna Airport (UUDL) | 2026-05-03 07:16 UTC | 2026-05-03 13:51 UTC | 6h 34m |
| IGO1161 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-05-03 12:31 UTC | 2026-05-03 13:49 UTC | 1h 18m |
| AUA11Q | Austrian Airlines | Vienna International Airport (LOWW) | Graz Airport (LOWG) | 2026-05-03 13:23 UTC | 2026-05-03 13:48 UTC | 24m |
| N916LF |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-05-03 13:09 UTC | 2026-05-03 13:45 UTC | 35m |
| N239DS |  | Trump Airport (16OI) | Ohio State University Airport (KOSU) | 2026-05-03 13:10 UTC | 2026-05-03 13:40 UTC | 30m |
| N510BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-05-03 13:25 UTC | 2026-05-03 13:40 UTC | 15m |
| AXM6038 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-03 13:16 UTC | 2026-05-03 13:38 UTC | 21m |
| OKDUD23 | OKD | Bubovice Airport (LKBU) | Bubovice Airport (LKBU) | 2026-05-03 13:28 UTC | 2026-05-03 13:38 UTC | 10m |
| N2108L |  | Dekalb-Peachtree Airport (KPDK) | Barrow County Airport (KWDR) | 2026-05-03 13:12 UTC | 2026-05-03 13:37 UTC | 25m |
| N141WP |  | Blue Grass Airport (KLEX) | Albany Municipal Airport (KK19) | 2026-05-03 11:24 UTC | 2026-05-03 13:36 UTC | 2h 11m |
| N150RJ |  | Lubbock Preston Smith International Airport (KLBB) | 3TE7 (3TE7) | 2026-05-03 13:08 UTC | 2026-05-03 13:34 UTC | 26m |
| RYR7588 | Ryanair | Copernicus Wrocław Airport (EPWR) | Chania International Airport (LGSA) | 2026-05-03 11:16 UTC | 2026-05-03 13:31 UTC | 2h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
