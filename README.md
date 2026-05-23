# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_06:12:19_UTC-green)

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

**Latest saved flight:** 2026-05-23 06:12:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 06:12:19 UTC

- **92,298** saved flights
- **32,739** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,298** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,134,966.2 tonnes** estimated CO2 emissions
- **65,795,144 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3912 |
| 2 | SkyWest Airlines | 3425 |
| 3 | IndiGo | 1921 |
| 4 | EJA | 1750 |
| 5 | American Airlines | 1400 |
| 6 | Southwest Airlines | 1333 |
| 7 | ENY | 1139 |
| 8 | Lufthansa | 1124 |
| 9 | Delta Air Lines | 1012 |
| 10 | Vueling | 877 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 813 |
| 13 | WIF | 806 |
| 14 | AZU | 734 |
| 15 | LXJ | 700 |
| 16 | Swiss International | 693 |
| 17 | All Nippon Airways | 688 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 603 |
| 21 | EJU | 585 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 560 |
| 24 | VIV | 547 |
| 25 | Air France | 540 |
| 26 | Japan Airlines | 487 |
| 27 | CXK | 486 |
| 28 | MXY | 479 |
| 29 | AXB | 469 |
| 30 | AIQ | 445 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76327 |
| 2 | 🇪🇸 ES | 6496 |
| 3 | 🇮🇳 IN | 6040 |
| 4 | 🇦🇺 AU | 5722 |
| 5 | 🇩🇪 DE | 5056 |
| 6 | 🇧🇷 BR | 5052 |
| 7 | 🇮🇹 IT | 5031 |
| 8 | 🇨🇦 CA | 4664 |
| 9 | 🇯🇵 JP | 4469 |
| 10 | 🇬🇧 GB | 3929 |
| 11 | 🇫🇷 FR | 3712 |
| 12 | 🇨🇴 CO | 3196 |
| 13 | 🇲🇽 MX | 2846 |
| 14 | 🇬🇷 GR | 2634 |
| 15 | 🇳🇴 NO | 2572 |
| 16 | 🇨🇭 CH | 2410 |
| 17 | 🇲🇾 MY | 2050 |
| 18 | 🇹🇷 TR | 1673 |
| 19 | 🇿🇦 ZA | 1669 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1560 |
| 22 | 🇵🇱 PL | 1506 |
| 23 | 🇰🇷 KR | 1467 |
| 24 | 🇵🇭 PH | 1407 |
| 25 | 🇬🇹 GT | 1389 |
| 26 | 🇲🇦 MA | 1060 |
| 27 | 🇲🇴 MO | 1036 |
| 28 | 🇳🇱 NL | 927 |
| 29 | 🇲🇪 ME | 927 |
| 30 | 🇭🇷 HR | 831 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2006 |
| 2 | Denver International Airport |  | US | 1553 |
| 3 | Tokyo International Airport |  | JP | 1489 |
| 4 | Indira Gandhi International Airport |  | IN | 1314 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1233 |
| 6 | Harry Reid International Airport |  | US | 1191 |
| 7 | Frankfurt am Main International Airport |  | DE | 1132 |
| 8 | Guaymaral Airport |  | CO | 1107 |
| 9 | Zurich Airport |  | CH | 1081 |
| 10 | La Aurora Airport |  | GT | 1062 |
| 11 | Macau International Airport |  | MO | 1036 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1012 |
| 13 | El Dorado International Airport |  | CO | 1007 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 925 |
| 15 | Chicago O'Hare International Airport |  | US | 883 |
| 16 | Madrid Barajas International Airport |  | ES | 832 |
| 17 | Kuala Lumpur International Airport |  | MY | 811 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 769 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 735 |
| 23 | Bengaluru International Airport |  | IN | 728 |
| 24 | Charles de Gaulle International Airport |  | FR | 718 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 703 |
| 27 | Daniel K Inouye International Airport |  | US | 668 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 645 |
| 30 | Barcelona International Airport |  | ES | 621 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 612 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 601 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 572 |
| 37 | Amsterdam Airport Schiphol |  | NL | 568 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 549 |
| 40 | O. R. Tambo International Airport |  | ZA | 528 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 454 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 340 | 21m | 244 km | 1,431.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 252 | 24m | 225 km | 977.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 233 | 28m | 304 km | 1,221.5 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 200 | 19m | 165 km | 568.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 151 | 21m | 99 km | 258.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 139 | 31m | 369 km | 884.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 137 | 27m | 215 km | 507.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 126 | 20m | 250 km | 544.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N492LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-23 05:14 UTC | 2026-05-23 06:12 UTC | 58m |
| N272BG |  | Spring Creek Field (79TX) | Moffett Federal Airfield (KNUQ) | 2026-05-23 02:52 UTC | 2026-05-23 06:09 UTC | 3h 16m |
| N32BR |  | Santa Barbara Municipal Airport (KSBA) | Scottsdale Airport (KSDL) | 2026-05-23 04:49 UTC | 2026-05-23 05:58 UTC | 1h 9m |
| THA132 | Thai Airways | Suvarnabhumi Airport (VTBS) | VLXL (VLXL) | 2026-05-23 04:51 UTC | 2026-05-23 05:45 UTC | 53m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-05-23 05:20 UTC | 2026-05-23 05:41 UTC | 20m |
| AM343 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-05-23 05:12 UTC | 2026-05-23 05:37 UTC | 25m |
| STA603D | STA | Tribhuvan International Airport (VNKT) | Phaplu Airport (VNPL) | 2026-05-23 05:20 UTC | 2026-05-23 05:36 UTC | 16m |
| ITY1278 | ITY | Capua Airport (LIAU) | Linate Airport (LIML) | 2026-05-23 04:34 UTC | 2026-05-23 05:31 UTC | 57m |
| RYR196A | Ryanair | Luqa Airport (LMML) | Stanke Dimitrov Highway Strip (LB37) | 2026-05-23 04:03 UTC | 2026-05-23 05:30 UTC | 1h 27m |
| DLH9YA | Lufthansa | Poznań-Ławica Airport (EPPO) | Frankfurt am Main International Airport (EDDF) | 2026-05-23 04:25 UTC | 2026-05-23 05:30 UTC | 1h 5m |
| URK | URK | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-05-23 04:42 UTC | 2026-05-23 05:29 UTC | 46m |
| RYR67FC | Ryanair | Paris Beauvais Tille Airport (LFOB) | Treviso / Sant'Angelo Airport (LIPH) | 2026-05-23 04:16 UTC | 2026-05-23 05:27 UTC | 1h 11m |
| RYR5GE | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Otocac Airport (LDRO) | 2026-05-23 04:28 UTC | 2026-05-23 05:24 UTC | 56m |
| WZZ6082 | Wizz Air | M. R. Stefanik Airport (LZIB) | Dortmund Airport (EDLW) | 2026-05-23 04:01 UTC | 2026-05-23 05:23 UTC | 1h 21m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-05-23 04:40 UTC | 2026-05-23 05:22 UTC | 42m |
| THA570 | Thai Airways | Suvarnabhumi Airport (VTBS) | Wattay International Airport (VLVT) | 2026-05-23 04:37 UTC | 2026-05-23 05:22 UTC | 45m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-23 04:17 UTC | 2026-05-23 05:22 UTC | 1h 4m |
| AIQ3239 | AIQ | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-05-23 04:46 UTC | 2026-05-23 05:19 UTC | 32m |
| BHA703 | BHA | Tribhuvan International Airport (VNKT) | Rajbiraj Airport (VNRB) | 2026-05-23 04:52 UTC | 2026-05-23 05:19 UTC | 26m |
| JAL609 | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-05-23 04:01 UTC | 2026-05-23 05:19 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
