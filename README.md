# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_15:13:05_UTC-green)

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

**Latest saved flight:** 2026-05-02 15:13:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 15:13:05 UTC

- **64,340** saved flights
- **24,480** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,340** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **788,855.6 tonnes** estimated CO2 emissions
- **45,730,760 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2726 |
| 2 | SkyWest Airlines | 2366 |
| 3 | IndiGo | 1489 |
| 4 | EJA | 1146 |
| 5 | American Airlines | 993 |
| 6 | Southwest Airlines | 905 |
| 7 | Lufthansa | 828 |
| 8 | ENY | 787 |
| 9 | Vueling | 634 |
| 10 | AXM | 630 |
| 11 | LATAM Airlines | 599 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 532 |
| 15 | AZU | 523 |
| 16 | QLK | 502 |
| 17 | Swiss International | 497 |
| 18 | LXJ | 456 |
| 19 | Alaska Airlines | 440 |
| 20 | easyJet | 421 |
| 21 | AEE | 417 |
| 22 | EJU | 411 |
| 23 | VIV | 402 |
| 24 | Cathay Pacific | 389 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 375 |
| 27 | AXB | 362 |
| 28 | AIQ | 330 |
| 29 | CXK | 325 |
| 30 | GLO | 314 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50732 |
| 2 | 🇪🇸 ES | 4693 |
| 3 | 🇮🇳 IN | 4692 |
| 4 | 🇦🇺 AU | 4343 |
| 5 | 🇧🇷 BR | 3638 |
| 6 | 🇩🇪 DE | 3602 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3494 |
| 9 | 🇨🇦 CA | 3147 |
| 10 | 🇬🇧 GB | 2767 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2543 |
| 13 | 🇲🇽 MX | 2025 |
| 14 | 🇬🇷 GR | 1926 |
| 15 | 🇨🇭 CH | 1809 |
| 16 | 🇳🇴 NO | 1762 |
| 17 | 🇲🇾 MY | 1543 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1149 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇰🇷 KR | 1056 |
| 24 | 🇵🇱 PL | 1054 |
| 25 | 🇬🇹 GT | 996 |
| 26 | 🇲🇦 MA | 790 |
| 27 | 🇲🇴 MO | 727 |
| 28 | 🇲🇪 ME | 696 |
| 29 | 🇳🇱 NL | 680 |
| 30 | 🇮🇩 ID | 544 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1409 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1051 |
| 4 | Indira Gandhi International Airport |  | IN | 983 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 938 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 829 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 766 |
| 11 | La Aurora Airport |  | GT | 746 |
| 12 | Macau International Airport |  | MO | 727 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Kuala Lumpur International Airport |  | MY | 612 |
| 15 | Madrid Barajas International Airport |  | ES | 609 |
| 16 | Chicago O'Hare International Airport |  | US | 608 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 576 |
| 18 | Bengaluru International Airport |  | IN | 569 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 553 |
| 21 | Congonhas Airport |  | BR | 525 |
| 22 | Tenerife Norte Airport |  | ES | 511 |
| 23 | Charlotte/Douglas International Airport |  | US | 504 |
| 24 | Salt Lake City International Airport |  | US | 504 |
| 25 | Charles de Gaulle International Airport |  | FR | 501 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 474 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 473 |
| 29 | Capua Airport |  | IT | 468 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 460 |
| 31 | Barcelona International Airport |  | ES | 437 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 429 |
| 33 | Vitoria/Foronda Airport |  | ES | 426 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 401 |
| 38 | Amsterdam Airport Schiphol |  | NL | 399 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 218 | 21m | 244 km | 917.9 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 158 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 144 | 26m | 275 km | 682.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 90 | 1h 42m | 1,156 km | 1,795.5 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 2m | 695 km | 1,066.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 83 | 1h 43m | 1,423 km | 2,037.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 83 | 1h 19m | 961 km | 1,375.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-05-02 14:53 UTC | 2026-05-02 15:13 UTC | 19m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-02 14:58 UTC | 2026-05-02 15:09 UTC | 10m |
| N714FL |  | Willow Run Airport (KYIP) | Willow Run Airport (KYIP) | 2026-05-02 14:55 UTC | 2026-05-02 15:08 UTC | 13m |
| EXM94 | EXM | Gloucestershire Airport (EGBJ) | Oxford (Kidlington) Airport (EGTK) | 2026-05-02 14:36 UTC | 2026-05-02 15:08 UTC | 31m |
| C6506 |  | Atlantic City International Airport (KACY) | NJ58 (NJ58) | 2026-05-02 14:12 UTC | 2026-05-02 15:04 UTC | 51m |
| N182HB |  | Green Castle Airport (IA24) | Iowa City Municipal Airport (KIOW) | 2026-05-02 14:14 UTC | 2026-05-02 15:03 UTC | 48m |
| N504AF |  | Addison Airport (KADS) | Majors Airport (KGVT) | 2026-05-02 14:35 UTC | 2026-05-02 15:01 UTC | 26m |
| HB3395 |  | Bad Ragaz Airport (LSZE) | Bad Ragaz Airport (LSZE) | 2026-05-02 13:35 UTC | 2026-05-02 15:00 UTC | 1h 24m |
| N1732V |  | Boerne Stage Airfield (K5C1) | Castroville Municipal Airport (KCVB) | 2026-05-02 14:45 UTC | 2026-05-02 14:59 UTC | 13m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-05-02 14:14 UTC | 2026-05-02 14:57 UTC | 42m |
| SCU57 | SCU | 19OK (19OK) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-05-02 14:32 UTC | 2026-05-02 14:57 UTC | 24m |
| N608FA |  | Lazy J Ranch Airport (PS82) | Lancaster Airport (KLNS) | 2026-05-02 14:12 UTC | 2026-05-02 14:57 UTC | 44m |
| N735VH |  | Grand Junction Regional Airport (KGJT) | Phylcon Ranch Airport (9CO9) | 2026-05-02 14:45 UTC | 2026-05-02 14:55 UTC | 10m |
|  |  | Karlindo Airport (3PN2) | Karlindo Airport (3PN2) | 2026-05-02 14:46 UTC | 2026-05-02 14:46 UTC | 0m |
| LHX9TY | LHX | Munich International Airport (EDDM) | Napoli / Capodichino International Airport (LIRN) | 2026-05-02 13:33 UTC | 2026-05-02 14:46 UTC | 1h 13m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-02 14:28 UTC | 2026-05-02 14:45 UTC | 17m |
| N6152H |  | Aero Valley Airport (K52F) | Decatur Municipal Airport (KLUD) | 2026-05-02 14:11 UTC | 2026-05-02 14:44 UTC | 33m |
| N218DS |  | Capital City Airport (KCXY) | Capital City Airport (KCXY) | 2026-05-02 13:37 UTC | 2026-05-02 14:44 UTC | 1h 7m |
| N21469 |  | Inyokern Airport (KIYK) | 91CL (91CL) | 2026-05-02 14:26 UTC | 2026-05-02 14:41 UTC | 15m |
| N7487G |  | Fort Worth Meacham International Airport (KFTW) | Decatur Municipal Airport (KLUD) | 2026-05-02 14:14 UTC | 2026-05-02 14:40 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
