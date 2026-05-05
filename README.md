# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_06:03:06_UTC-green)

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

**Latest saved flight:** 2026-05-05 06:03:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 06:03:06 UTC

- **68,884** saved flights
- **25,815** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,884** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **847,005.3 tonnes** estimated CO2 emissions
- **49,101,758 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2953 |
| 2 | SkyWest Airlines | 2557 |
| 3 | IndiGo | 1587 |
| 4 | EJA | 1242 |
| 5 | American Airlines | 1071 |
| 6 | Southwest Airlines | 978 |
| 7 | Lufthansa | 886 |
| 8 | ENY | 851 |
| 9 | Vueling | 675 |
| 10 | AXM | 660 |
| 11 | LATAM Airlines | 640 |
| 12 | All Nippon Airways | 581 |
| 13 | Delta Air Lines | 580 |
| 14 | WIF | 580 |
| 15 | AZU | 559 |
| 16 | QLK | 532 |
| 17 | Swiss International | 529 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 473 |
| 20 | easyJet | 456 |
| 21 | AEE | 451 |
| 22 | EJU | 447 |
| 23 | VIV | 430 |
| 24 | Cathay Pacific | 416 |
| 25 | Japan Airlines | 405 |
| 26 | Air France | 404 |
| 27 | AXB | 388 |
| 28 | AIQ | 348 |
| 29 | CXK | 348 |
| 30 | MXY | 337 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54643 |
| 2 | 🇪🇸 ES | 5028 |
| 3 | 🇮🇳 IN | 4995 |
| 4 | 🇦🇺 AU | 4581 |
| 5 | 🇧🇷 BR | 3864 |
| 6 | 🇩🇪 DE | 3847 |
| 7 | 🇮🇹 IT | 3772 |
| 8 | 🇯🇵 JP | 3697 |
| 9 | 🇨🇦 CA | 3396 |
| 10 | 🇬🇧 GB | 2981 |
| 11 | 🇫🇷 FR | 2724 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2193 |
| 14 | 🇬🇷 GR | 2065 |
| 15 | 🇨🇭 CH | 1903 |
| 16 | 🇳🇴 NO | 1872 |
| 17 | 🇲🇾 MY | 1642 |
| 18 | 🇿🇦 ZA | 1377 |
| 19 | 🇳🇿 NZ | 1286 |
| 20 | 🇹🇭 TH | 1245 |
| 21 | 🇹🇷 TR | 1229 |
| 22 | 🇵🇭 PH | 1153 |
| 23 | 🇵🇱 PL | 1127 |
| 24 | 🇬🇹 GT | 1113 |
| 25 | 🇰🇷 KR | 1100 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 783 |
| 28 | 🇲🇪 ME | 744 |
| 29 | 🇳🇱 NL | 718 |
| 30 | 🇮🇩 ID | 585 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1524 |
| 2 | Tokyo International Airport |  | JP | 1246 |
| 3 | Denver International Airport |  | US | 1131 |
| 4 | Indira Gandhi International Airport |  | IN | 1046 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1008 |
| 6 | Frankfurt am Main International Airport |  | DE | 882 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 859 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 828 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 783 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 681 |
| 14 | Chicago O'Hare International Airport |  | US | 660 |
| 15 | Kuala Lumpur International Airport |  | MY | 658 |
| 16 | Madrid Barajas International Airport |  | ES | 655 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 617 |
| 18 | Bengaluru International Airport |  | IN | 604 |
| 19 | Malpensa International Airport |  | IT | 600 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 598 |
| 21 | Salt Lake City International Airport |  | US | 552 |
| 22 | Congonhas Airport |  | BR | 552 |
| 23 | Charlotte/Douglas International Airport |  | US | 543 |
| 24 | Tenerife Norte Airport |  | ES | 540 |
| 25 | Charles de Gaulle International Airport |  | FR | 539 |
| 26 | Capua Airport |  | IT | 529 |
| 27 | Ninoy Aquino International Airport |  | PH | 524 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 504 |
| 29 | Daniel K Inouye International Airport |  | US | 502 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 487 |
| 31 | Barcelona International Airport |  | ES | 478 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 458 |
| 34 | Vitoria/Foronda Airport |  | ES | 456 |
| 35 | Don Mueang International Airport |  | TH | 437 |
| 36 | O. R. Tambo International Airport |  | ZA | 436 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 430 |
| 38 | Amsterdam Airport Schiphol |  | NL | 422 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 408 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 236 | 21m | 244 km | 993.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 166 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 155 | 26m | 275 km | 734.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 153 | 1h 12m | 770 km | 2,032.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 131 | 21m | 99 km | 224.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 125 | 44m | 452 km | 974.2 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 116 | 31m | 369 km | 738.4 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 109 | 20m | 250 km | 470.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 97 | 14m | 154 km | 257.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 96 | 1h 2m | 695 km | 1,150.8 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AAE121 | AAE | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-05-04 18:44 UTC | 2026-05-05 06:03 UTC | 11h 18m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-05-05 05:35 UTC | 2026-05-05 06:01 UTC | 25m |
| CLX4971 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-04 19:02 UTC | 2026-05-05 05:58 UTC | 10h 55m |
| NIU | NIU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-05-05 05:28 UTC | 2026-05-05 05:54 UTC | 25m |
| EWG8M | EWG | Hamburg Airport (EDDH) | Walldurn Airport (EDEW) | 2026-05-05 04:37 UTC | 2026-05-05 05:49 UTC | 1h 11m |
| FD618 |  | Perth Jandakot Airport (YPJT) | Kellerberrin Airport (YKEB) | 2026-05-05 05:14 UTC | 2026-05-05 05:43 UTC | 28m |
| RYR2TY | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-05-05 04:35 UTC | 2026-05-05 05:42 UTC | 1h 7m |
| NKD | NKD | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-05-05 05:13 UTC | 2026-05-05 05:42 UTC | 28m |
| DEPAA | DEP | Dimokritos Airport (LGAL) | Plovdiv International Airport (LBPD) | 2026-05-05 04:36 UTC | 2026-05-05 05:40 UTC | 1h 4m |
| ZEF | ZEF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-05 05:20 UTC | 2026-05-05 05:39 UTC | 19m |
| UPS2 | UPS | Cologne Bonn Airport (EDDK) | Macau International Airport (VMMC) | 2026-05-04 18:40 UTC | 2026-05-05 05:38 UTC | 10h 58m |
| DLH821 | Lufthansa | Gothenburg-Landvetter Airport (ESGG) | Lauterbach Airport (EDFT) | 2026-05-05 04:09 UTC | 2026-05-05 05:34 UTC | 1h 25m |
| DLH403 | Lufthansa | Newark Liberty International Airport (KEWR) | Anspach/Taunus Airport (EDFA) | 2026-05-04 22:19 UTC | 2026-05-05 05:32 UTC | 7h 13m |
| DLH9YA | Lufthansa | Poznań-Ławica Airport (EPPO) | Wasserkuppe Airport (EDER) | 2026-05-05 04:26 UTC | 2026-05-05 05:32 UTC | 1h 6m |
| JA02NA |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-05-05 05:24 UTC | 2026-05-05 05:32 UTC | 8m |
| IGO6HC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Thamkharka Airport (VNTH) | 2026-05-05 04:40 UTC | 2026-05-05 05:24 UTC | 44m |
| AWA473 | AWA | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-05-05 04:40 UTC | 2026-05-05 05:23 UTC | 43m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-05-05 04:34 UTC | 2026-05-05 05:23 UTC | 48m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-05 04:56 UTC | 2026-05-05 05:22 UTC | 25m |
| EZY825P | easyJet | Glasgow International Airport (EGPF) | Belfast International Airport (EGAA) | 2026-05-05 04:59 UTC | 2026-05-05 05:22 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
