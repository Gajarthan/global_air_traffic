# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_18:36:36_UTC-green)

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

**Latest saved flight:** 2026-05-06 18:36:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 18:36:36 UTC

- **70,994** saved flights
- **26,416** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,994** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **875,101.7 tonnes** estimated CO2 emissions
- **50,730,535 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3059 |
| 2 | SkyWest Airlines | 2640 |
| 3 | IndiGo | 1621 |
| 4 | EJA | 1293 |
| 5 | American Airlines | 1108 |
| 6 | Southwest Airlines | 1028 |
| 7 | Lufthansa | 917 |
| 8 | ENY | 885 |
| 9 | Vueling | 701 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 661 |
| 12 | WIF | 608 |
| 13 | Delta Air Lines | 596 |
| 14 | All Nippon Airways | 590 |
| 15 | AZU | 577 |
| 16 | Swiss International | 548 |
| 17 | QLK | 547 |
| 18 | LXJ | 513 |
| 19 | Alaska Airlines | 497 |
| 20 | easyJet | 475 |
| 21 | AEE | 459 |
| 22 | EJU | 458 |
| 23 | VIV | 445 |
| 24 | Cathay Pacific | 434 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 418 |
| 27 | AXB | 395 |
| 28 | AIQ | 358 |
| 29 | CXK | 352 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 56487 |
| 2 | 🇪🇸 ES | 5186 |
| 3 | 🇮🇳 IN | 5089 |
| 4 | 🇦🇺 AU | 4706 |
| 5 | 🇧🇷 BR | 3998 |
| 6 | 🇩🇪 DE | 3968 |
| 7 | 🇮🇹 IT | 3897 |
| 8 | 🇯🇵 JP | 3775 |
| 9 | 🇨🇦 CA | 3509 |
| 10 | 🇬🇧 GB | 3079 |
| 11 | 🇫🇷 FR | 2808 |
| 12 | 🇨🇴 CO | 2667 |
| 13 | 🇲🇽 MX | 2251 |
| 14 | 🇬🇷 GR | 2121 |
| 15 | 🇳🇴 NO | 1955 |
| 16 | 🇨🇭 CH | 1946 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1301 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1282 |
| 22 | 🇵🇱 PL | 1177 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1135 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 850 |
| 27 | 🇲🇴 MO | 824 |
| 28 | 🇲🇪 ME | 762 |
| 29 | 🇳🇱 NL | 743 |
| 30 | 🇮🇩 ID | 596 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1584 |
| 2 | Tokyo International Airport |  | JP | 1274 |
| 3 | Denver International Airport |  | US | 1176 |
| 4 | Indira Gandhi International Airport |  | IN | 1070 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1037 |
| 6 | Frankfurt am Main International Airport |  | DE | 912 |
| 7 | Harry Reid International Airport |  | US | 885 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 862 |
| 10 | La Aurora Airport |  | GT | 845 |
| 11 | Zurich Airport |  | CH | 844 |
| 12 | Macau International Airport |  | MO | 824 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 713 |
| 14 | Chicago O'Hare International Airport |  | US | 688 |
| 15 | Kuala Lumpur International Airport |  | MY | 679 |
| 16 | Madrid Barajas International Airport |  | ES | 675 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 635 |
| 18 | Malpensa International Airport |  | IT | 618 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 21 | Salt Lake City International Airport |  | US | 573 |
| 22 | Congonhas Airport |  | BR | 569 |
| 23 | Capua Airport |  | IT | 559 |
| 24 | Charlotte/Douglas International Airport |  | US | 557 |
| 25 | Charles de Gaulle International Airport |  | FR | 557 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 522 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 500 |
| 31 | Barcelona International Airport |  | ES | 497 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 483 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 474 |
| 34 | Vitoria/Foronda Airport |  | ES | 470 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 446 |
| 37 | Amsterdam Airport Schiphol |  | NL | 443 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Reno/Tahoe International Airport |  | US | 422 |
| 40 | Calgary International Airport |  | CA | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 357 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 247 | 21m | 244 km | 1,040.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 178 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 159 | 26m | 275 km | 753.4 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 95 | 1h 43m | 1,423 km | 2,331.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 89 | 23m | 55 km | 84.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3853J |  | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-05-06 18:14 UTC | 2026-05-06 18:36 UTC | 22m |
| CFR604 | CFR | Longbell Ranch Airport (2CL3) | Bodad Airport (CA11) | 2026-05-06 18:20 UTC | 2026-05-06 18:35 UTC | 15m |
| N152SB |  | Melbourne Orlando International Airport (KMLB) | Peter O Knight Airport (KTPF) | 2026-05-06 17:55 UTC | 2026-05-06 18:34 UTC | 39m |
| PAT454 | PAT | Truckee-Tahoe Airport (KTRK) | Sacramento Mather Airport (KMHR) | 2026-05-06 17:27 UTC | 2026-05-06 18:31 UTC | 1h 4m |
| SLEEP81 | SLE | Flying E Ranch Airport (OK16) | Mooreland Municipal Airport (KMDF) | 2026-05-06 17:57 UTC | 2026-05-06 18:30 UTC | 33m |
| CMD7 | CMD | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 0CA3 (0CA3) | 2026-05-06 18:08 UTC | 2026-05-06 18:25 UTC | 16m |
| N2676 |  | Fulton County Executive/Charlie Brown Field (KFTY) | 5MD8 (5MD8) | 2026-05-06 17:04 UTC | 2026-05-06 18:23 UTC | 1h 18m |
| BOX722 | BOX | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-06 14:11 UTC | 2026-05-06 18:19 UTC | 4h 7m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-06 17:59 UTC | 2026-05-06 18:17 UTC | 17m |
| ADN64E | ADN | Dusseldorf International Airport (EDDL) | Burg Feuerstein Airport (EDQE) | 2026-05-06 17:29 UTC | 2026-05-06 18:16 UTC | 46m |
| AUA217N | Austrian Airlines | Vienna International Airport (LOWW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-05-06 17:12 UTC | 2026-05-06 18:16 UTC | 1h 3m |
| DLH5XV | Lufthansa | Glasgow International Airport (EGPF) | Ober-Morlen Airport (EDFP) | 2026-05-06 16:38 UTC | 2026-05-06 18:16 UTC | 1h 37m |
| AER121 | AER | Fairbanks International Airport (PAFA) | PAFV (PAFV) | 2026-05-06 17:50 UTC | 2026-05-06 18:15 UTC | 24m |
| N833MK |  | Morristown Municipal Airport (KMMU) | Newark Liberty International Airport (KEWR) | 2026-05-06 17:16 UTC | 2026-05-06 18:14 UTC | 57m |
|  |  | Crystal Lake Airpark (0GE1) | Crystal Lake Airpark (0GE1) | 2026-05-06 18:09 UTC | 2026-05-06 18:10 UTC | 0m |
| RYR3BU | Ryanair | Leeds Bradford Airport (EGNM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-06 15:59 UTC | 2026-05-06 18:06 UTC | 2h 6m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Burris Ranch Airport (2TE6) | 2026-05-06 17:36 UTC | 2026-05-06 18:06 UTC | 30m |
| SMGLR33 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-05-06 16:22 UTC | 2026-05-06 18:03 UTC | 1h 40m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-06 17:10 UTC | 2026-05-06 18:03 UTC | 53m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-06 17:15 UTC | 2026-05-06 18:03 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
