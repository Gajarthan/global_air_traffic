# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_18:42:20_UTC-green)

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

**Latest saved flight:** 2026-05-04 18:42:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 18:42:20 UTC

- **68,123** saved flights
- **25,590** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,123** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **836,678.1 tonnes** estimated CO2 emissions
- **48,503,079 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2929 |
| 2 | SkyWest Airlines | 2508 |
| 3 | IndiGo | 1581 |
| 4 | EJA | 1218 |
| 5 | American Airlines | 1052 |
| 6 | Southwest Airlines | 958 |
| 7 | Lufthansa | 874 |
| 8 | ENY | 834 |
| 9 | Vueling | 670 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 633 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 574 |
| 14 | Delta Air Lines | 567 |
| 15 | AZU | 551 |
| 16 | Swiss International | 528 |
| 17 | QLK | 523 |
| 18 | LXJ | 492 |
| 19 | Alaska Airlines | 461 |
| 20 | easyJet | 453 |
| 21 | AEE | 451 |
| 22 | EJU | 444 |
| 23 | VIV | 423 |
| 24 | Cathay Pacific | 410 |
| 25 | Air France | 404 |
| 26 | Japan Airlines | 399 |
| 27 | AXB | 386 |
| 28 | AIQ | 346 |
| 29 | CXK | 346 |
| 30 | GLO | 331 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53809 |
| 2 | 🇪🇸 ES | 4987 |
| 3 | 🇮🇳 IN | 4977 |
| 4 | 🇦🇺 AU | 4497 |
| 5 | 🇧🇷 BR | 3829 |
| 6 | 🇩🇪 DE | 3819 |
| 7 | 🇮🇹 IT | 3745 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3352 |
| 10 | 🇬🇧 GB | 2963 |
| 11 | 🇫🇷 FR | 2718 |
| 12 | 🇨🇴 CO | 2655 |
| 13 | 🇲🇽 MX | 2161 |
| 14 | 🇬🇷 GR | 2056 |
| 15 | 🇨🇭 CH | 1900 |
| 16 | 🇳🇴 NO | 1858 |
| 17 | 🇲🇾 MY | 1635 |
| 18 | 🇿🇦 ZA | 1371 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1222 |
| 22 | 🇵🇭 PH | 1137 |
| 23 | 🇵🇱 PL | 1119 |
| 24 | 🇬🇹 GT | 1106 |
| 25 | 🇰🇷 KR | 1089 |
| 26 | 🇲🇦 MA | 831 |
| 27 | 🇲🇴 MO | 769 |
| 28 | 🇲🇪 ME | 739 |
| 29 | 🇳🇱 NL | 713 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1490 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1115 |
| 4 | Indira Gandhi International Airport |  | IN | 1041 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1003 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 877 |
| 8 | Guaymaral Airport |  | CO | 850 |
| 9 | Harry Reid International Airport |  | US | 844 |
| 10 | La Aurora Airport |  | GT | 822 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 769 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 668 |
| 14 | Kuala Lumpur International Airport |  | MY | 656 |
| 15 | Chicago O'Hare International Airport |  | US | 654 |
| 16 | Madrid Barajas International Airport |  | ES | 650 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 604 |
| 18 | Bengaluru International Airport |  | IN | 603 |
| 19 | Malpensa International Airport |  | IT | 597 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 21 | Congonhas Airport |  | BR | 549 |
| 22 | Salt Lake City International Airport |  | US | 540 |
| 23 | Charles de Gaulle International Airport |  | FR | 538 |
| 24 | Tenerife Norte Airport |  | ES | 537 |
| 25 | Charlotte/Douglas International Airport |  | US | 536 |
| 26 | Capua Airport |  | IT | 525 |
| 27 | Ninoy Aquino International Airport |  | PH | 517 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 502 |
| 29 | Daniel K Inouye International Airport |  | US | 494 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 479 |
| 31 | Barcelona International Airport |  | ES | 472 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 459 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 454 |
| 34 | Vitoria/Foronda Airport |  | ES | 451 |
| 35 | O. R. Tambo International Airport |  | ZA | 434 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 426 |
| 38 | Amsterdam Airport Schiphol |  | NL | 420 |
| 39 | Reno/Tahoe International Airport |  | US | 407 |
| 40 | Calgary International Airport |  | CA | 403 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 351 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 232 | 21m | 244 km | 976.9 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 170 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 152 | 26m | 275 km | 720.3 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 130 | 21m | 99 km | 222.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 114 | 27m | 152 km | 297.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 113 | 31m | 369 km | 719.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 96 | 14m | 154 km | 254.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 94 | 1h 2m | 695 km | 1,126.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 53m | 1,304 km | 2,069.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N61577 |  | 16PA (16PA) | Allegheny County Airport (KAGC) | 2026-05-04 18:19 UTC | 2026-05-04 18:42 UTC | 22m |
| ATG7720 | ATG | Budapest Ferenc Liszt International Airport (LHBP) | Macau International Airport (VMMC) | 2026-05-04 08:35 UTC | 2026-05-04 18:39 UTC | 10h 4m |
| CTX62 | CTX | Dekalb-Peachtree Airport (KPDK) | Cy Nunnally Memorial Airport (KD73) | 2026-05-04 18:18 UTC | 2026-05-04 18:39 UTC | 20m |
| N444CM |  | Columbia Metro Airport (KCAE) | Nassau Airport (83FL) | 2026-05-04 17:42 UTC | 2026-05-04 18:35 UTC | 52m |
| N478DS |  | Crosswinds-Wilson Pvt Airport (SC37) | 6SC1 (6SC1) | 2026-05-04 18:18 UTC | 2026-05-04 18:29 UTC | 10m |
| POE205 | POE | Toronto Pearson International Airport (CYYZ) | Halifax Robert L. Stanfield International Airport (CYHZ) | 2026-05-04 16:43 UTC | 2026-05-04 18:25 UTC | 1h 42m |
| N20AH |  | Grand Prairie Municipal Airport (KGPM) | Grand Prairie Municipal Airport (KGPM) | 2026-05-04 18:09 UTC | 2026-05-04 18:23 UTC | 14m |
| DRACO51 | DRA | OK79 (OK79) | Perkins Airport (5OK8) | 2026-05-04 17:51 UTC | 2026-05-04 18:23 UTC | 31m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-05-04 17:53 UTC | 2026-05-04 18:19 UTC | 26m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-04 18:07 UTC | 2026-05-04 18:18 UTC | 10m |
| N122NH |  | Mifflin County Airport (KRVL) | Drillmore Acres Airport (0PN7) | 2026-05-04 17:50 UTC | 2026-05-04 18:17 UTC | 26m |
| N557PC |  | San Bernardino International Airport (KSBD) | Meadows Field (KBFL) | 2026-05-04 17:35 UTC | 2026-05-04 18:14 UTC | 38m |
| N411BN |  | John Wayne/Orange County Airport (KSNA) | San Bernardino International Airport (KSBD) | 2026-05-04 17:44 UTC | 2026-05-04 18:11 UTC | 26m |
| N956TX |  | San Antonio International Airport (KSAT) | Austin-Bergstrom International Airport (KAUS) | 2026-05-04 17:42 UTC | 2026-05-04 18:10 UTC | 27m |
| N234CR |  | Falcon Field (KFFZ) | Montezuma Airport (19AZ) | 2026-05-04 17:29 UTC | 2026-05-04 18:08 UTC | 39m |
| C2703 |  | Monterey Regional Airport (KMRY) | 8CL9 (8CL9) | 2026-05-04 17:19 UTC | 2026-05-04 18:07 UTC | 48m |
| N82AU |  | Collier Airpark (2AL1) | Bay Minette Municipal Airport (K1R8) | 2026-05-04 17:57 UTC | 2026-05-04 18:07 UTC | 10m |
| N122PA |  | Boca Raton Airport (KBCT) | 5TX8 (5TX8) | 2026-05-04 14:56 UTC | 2026-05-04 18:06 UTC | 3h 9m |
| WSN8 | WSN | Albuquerque International Sunport Airport (KABQ) | Grant County Airport (KSVC) | 2026-05-04 17:22 UTC | 2026-05-04 18:06 UTC | 43m |
| N417FP |  | Malad City Airport (KMLD) | Malad City Airport (KMLD) | 2026-05-04 17:54 UTC | 2026-05-04 18:05 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
