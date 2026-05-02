# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_17:51:50_UTC-green)

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

**Latest saved flight:** 2026-05-02 17:51:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 17:51:50 UTC

- **64,657** saved flights
- **24,583** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **64,657** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **792,829.7 tonnes** estimated CO2 emissions
- **45,961,141 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2744 |
| 2 | SkyWest Airlines | 2378 |
| 3 | IndiGo | 1493 |
| 4 | EJA | 1152 |
| 5 | American Airlines | 999 |
| 6 | Southwest Airlines | 911 |
| 7 | Lufthansa | 833 |
| 8 | ENY | 791 |
| 9 | Vueling | 638 |
| 10 | AXM | 631 |
| 11 | LATAM Airlines | 600 |
| 12 | All Nippon Airways | 566 |
| 13 | WIF | 539 |
| 14 | Delta Air Lines | 535 |
| 15 | AZU | 525 |
| 16 | QLK | 502 |
| 17 | Swiss International | 498 |
| 18 | LXJ | 463 |
| 19 | Alaska Airlines | 442 |
| 20 | easyJet | 422 |
| 21 | AEE | 419 |
| 22 | EJU | 415 |
| 23 | VIV | 404 |
| 24 | Cathay Pacific | 389 |
| 25 | Japan Airlines | 379 |
| 26 | Air France | 377 |
| 27 | AXB | 363 |
| 28 | AIQ | 330 |
| 29 | CXK | 329 |
| 30 | GLO | 316 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51044 |
| 2 | 🇪🇸 ES | 4732 |
| 3 | 🇮🇳 IN | 4705 |
| 4 | 🇦🇺 AU | 4343 |
| 5 | 🇧🇷 BR | 3647 |
| 6 | 🇩🇪 DE | 3630 |
| 7 | 🇯🇵 JP | 3527 |
| 8 | 🇮🇹 IT | 3511 |
| 9 | 🇨🇦 CA | 3170 |
| 10 | 🇬🇧 GB | 2778 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2561 |
| 13 | 🇲🇽 MX | 2037 |
| 14 | 🇬🇷 GR | 1937 |
| 15 | 🇨🇭 CH | 1817 |
| 16 | 🇳🇴 NO | 1764 |
| 17 | 🇲🇾 MY | 1546 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1178 |
| 21 | 🇹🇷 TR | 1160 |
| 22 | 🇵🇭 PH | 1087 |
| 23 | 🇵🇱 PL | 1060 |
| 24 | 🇰🇷 KR | 1056 |
| 25 | 🇬🇹 GT | 998 |
| 26 | 🇲🇦 MA | 795 |
| 27 | 🇲🇴 MO | 728 |
| 28 | 🇲🇪 ME | 698 |
| 29 | 🇳🇱 NL | 682 |
| 30 | 🇮🇩 ID | 544 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1413 |
| 2 | Tokyo International Airport |  | JP | 1189 |
| 3 | Denver International Airport |  | US | 1056 |
| 4 | Indira Gandhi International Airport |  | IN | 987 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 943 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 833 |
| 9 | Harry Reid International Airport |  | US | 810 |
| 10 | Zurich Airport |  | CH | 767 |
| 11 | La Aurora Airport |  | GT | 748 |
| 12 | Macau International Airport |  | MO | 728 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 633 |
| 14 | Kuala Lumpur International Airport |  | MY | 614 |
| 15 | Madrid Barajas International Airport |  | ES | 613 |
| 16 | Chicago O'Hare International Airport |  | US | 612 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 578 |
| 18 | Bengaluru International Airport |  | IN | 570 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 20 | Malpensa International Airport |  | IT | 557 |
| 21 | Congonhas Airport |  | BR | 526 |
| 22 | Tenerife Norte Airport |  | ES | 515 |
| 23 | Charlotte/Douglas International Airport |  | US | 510 |
| 24 | Salt Lake City International Airport |  | US | 508 |
| 25 | Charles de Gaulle International Airport |  | FR | 505 |
| 26 | Ninoy Aquino International Airport |  | PH | 494 |
| 27 | Daniel K Inouye International Airport |  | US | 476 |
| 28 | Capua Airport |  | IT | 474 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 474 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 461 |
| 31 | Barcelona International Airport |  | ES | 441 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 431 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 430 |
| 34 | Vitoria/Foronda Airport |  | ES | 429 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 407 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 403 |
| 38 | Amsterdam Airport Schiphol |  | NL | 400 |
| 39 | Reno/Tahoe International Airport |  | US | 396 |
| 40 | Calgary International Airport |  | CA | 381 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 259 | 1h 7m | 706 km | 3,153.3 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 219 | 21m | 244 km | 922.1 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 201 | 24m | 225 km | 779.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 189 | 1h 27m | 910 km | 2,965.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 188 | 28m | 304 km | 985.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 159 | 20m | 165 km | 452.3 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 159 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 152 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 145 | 26m | 275 km | 687.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 119 | 44m | 452 km | 927.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 109 | 31m | 369 km | 693.8 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 86 | 23m | 55 km | 81.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N121NG |  | Cedar Crest Field (1TN0) | KM33 (KM33) | 2026-05-02 17:38 UTC | 2026-05-02 17:51 UTC | 13m |
| N834LA |  | Dupage Airport (KDPA) | Wade Airport (56LL) | 2026-05-02 17:36 UTC | 2026-05-02 17:47 UTC | 11m |
| N7425T |  | Bend Municipal Airport (KBDN) | Sisters Eagle Air Airport (K6K5) | 2026-05-02 17:25 UTC | 2026-05-02 17:43 UTC | 18m |
| CXK253 | CXK | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-05-02 16:35 UTC | 2026-05-02 17:34 UTC | 58m |
| AGV08 | AGV | Meiringen Airport (LSMM) | Muenster Aero Airport (LSPU) | 2026-05-02 17:24 UTC | 2026-05-02 17:30 UTC | 5m |
| N738C |  | Sky Ranch At Carefree Airport (18AZ) | Cottonwood Airport (KP52) | 2026-05-02 16:56 UTC | 2026-05-02 17:28 UTC | 32m |
| CGTRH | CGT | Vernon Airport (CYVK) | Kelowna Airport (CYLW) | 2026-05-02 17:27 UTC | 2026-05-02 17:28 UTC | 1m |
| N10580 |  | Vance Brand Airport (KLMO) | Laramie Regional Airport (KLAR) | 2026-05-02 16:59 UTC | 2026-05-02 17:24 UTC | 24m |
| N2888C |  | River View Field (72IN) | River View Field (72IN) | 2026-05-02 17:10 UTC | 2026-05-02 17:21 UTC | 10m |
| N65JA |  | Aurora Municipal Airport (KARR) | Walnut Creek Airport (49IL) | 2026-05-02 16:59 UTC | 2026-05-02 17:21 UTC | 21m |
| N8126X |  | Flying W Airport (KN14) | Trenton-Robbinsville Airport (KN87) | 2026-05-02 16:44 UTC | 2026-05-02 17:20 UTC | 36m |
| N64301 |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-05-02 17:07 UTC | 2026-05-02 17:14 UTC | 7m |
| N36BG |  | City Of Slaton/Larry T Neal Memorial Airport (KF49) | 0TE3 (0TE3) | 2026-05-02 16:53 UTC | 2026-05-02 17:13 UTC | 20m |
| N26KX |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Sugar Creek Airport (58AR) | 2026-05-02 17:04 UTC | 2026-05-02 17:13 UTC | 8m |
| XBMNG | XBM | Hermanos Serdan International Airport (MMPB) | Tlaxcala Airport (MMTA) | 2026-05-02 16:58 UTC | 2026-05-02 17:13 UTC | 14m |
| N5629S |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-02 16:58 UTC | 2026-05-02 17:09 UTC | 10m |
| N23PR |  | Robert F Swinnie Airport (KPHH) | Hilton Head Airport (KHXD) | 2026-05-02 16:37 UTC | 2026-05-02 17:09 UTC | 31m |
| PROHB | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-05-02 17:01 UTC | 2026-05-02 17:08 UTC | 7m |
| XBHGM | XBH | General Mariano Matamoros Airport (MMCB) | MM62 (MM62) | 2026-05-02 15:42 UTC | 2026-05-02 17:08 UTC | 1h 26m |
| N774AW |  | Stellar Airpark (KP19) | Montezuma Airport (19AZ) | 2026-05-02 16:46 UTC | 2026-05-02 17:07 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
