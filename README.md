# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_10:22:32_UTC-green)

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

**Latest saved flight:** 2026-05-09 10:22:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 10:22:32 UTC

- **75,066** saved flights
- **27,683** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,066** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **925,400.4 tonnes** estimated CO2 emissions
- **53,646,399 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3213 |
| 2 | SkyWest Airlines | 2787 |
| 3 | IndiGo | 1685 |
| 4 | EJA | 1387 |
| 5 | American Airlines | 1169 |
| 6 | Southwest Airlines | 1088 |
| 7 | Lufthansa | 970 |
| 8 | ENY | 937 |
| 9 | Vueling | 726 |
| 10 | AXM | 706 |
| 11 | Delta Air Lines | 705 |
| 12 | LATAM Airlines | 693 |
| 13 | WIF | 652 |
| 14 | All Nippon Airways | 613 |
| 15 | AZU | 603 |
| 16 | QLK | 579 |
| 17 | Swiss International | 572 |
| 18 | LXJ | 554 |
| 19 | Alaska Airlines | 530 |
| 20 | easyJet | 495 |
| 21 | AEE | 481 |
| 22 | EJU | 481 |
| 23 | Cathay Pacific | 473 |
| 24 | VIV | 454 |
| 25 | Japan Airlines | 441 |
| 26 | Air France | 434 |
| 27 | AXB | 415 |
| 28 | CXK | 384 |
| 29 | AIQ | 372 |
| 30 | MXY | 363 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 60441 |
| 2 | 🇪🇸 ES | 5388 |
| 3 | 🇮🇳 IN | 5285 |
| 4 | 🇦🇺 AU | 4950 |
| 5 | 🇩🇪 DE | 4205 |
| 6 | 🇧🇷 BR | 4202 |
| 7 | 🇮🇹 IT | 4091 |
| 8 | 🇯🇵 JP | 3935 |
| 9 | 🇨🇦 CA | 3744 |
| 10 | 🇬🇧 GB | 3226 |
| 11 | 🇫🇷 FR | 2970 |
| 12 | 🇨🇴 CO | 2691 |
| 13 | 🇲🇽 MX | 2325 |
| 14 | 🇬🇷 GR | 2213 |
| 15 | 🇳🇴 NO | 2087 |
| 16 | 🇨🇭 CH | 2031 |
| 17 | 🇲🇾 MY | 1761 |
| 18 | 🇿🇦 ZA | 1457 |
| 19 | 🇳🇿 NZ | 1364 |
| 20 | 🇹🇷 TR | 1337 |
| 21 | 🇹🇭 TH | 1330 |
| 22 | 🇵🇱 PL | 1249 |
| 23 | 🇵🇭 PH | 1214 |
| 24 | 🇬🇹 GT | 1184 |
| 25 | 🇰🇷 KR | 1176 |
| 26 | 🇲🇦 MA | 886 |
| 27 | 🇲🇴 MO | 869 |
| 28 | 🇲🇪 ME | 802 |
| 29 | 🇳🇱 NL | 777 |
| 30 | 🇧🇸 BS | 627 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1664 |
| 2 | Tokyo International Airport |  | JP | 1320 |
| 3 | Denver International Airport |  | US | 1258 |
| 4 | Indira Gandhi International Airport |  | IN | 1111 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1085 |
| 6 | Frankfurt am Main International Airport |  | DE | 971 |
| 7 | Harry Reid International Airport |  | US | 934 |
| 8 | La Aurora Airport |  | GT | 888 |
| 9 | Guaymaral Airport |  | CO | 885 |
| 10 | Zurich Airport |  | CH | 884 |
| 11 | El Dorado International Airport |  | CO | 879 |
| 12 | Macau International Airport |  | MO | 869 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 753 |
| 14 | Chicago O'Hare International Airport |  | US | 729 |
| 15 | Kuala Lumpur International Airport |  | MY | 706 |
| 16 | Madrid Barajas International Airport |  | ES | 701 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 664 |
| 18 | Bengaluru International Airport |  | IN | 653 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 650 |
| 20 | Malpensa International Airport |  | IT | 644 |
| 21 | Salt Lake City International Airport |  | US | 617 |
| 22 | Congonhas Airport |  | BR | 596 |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 595 |
| 24 | Charlotte/Douglas International Airport |  | US | 590 |
| 25 | Charles de Gaulle International Airport |  | FR | 582 |
| 26 | Capua Airport |  | IT | 576 |
| 27 | Tenerife Norte Airport |  | ES | 560 |
| 28 | Ninoy Aquino International Airport |  | PH | 550 |
| 29 | Daniel K Inouye International Airport |  | US | 549 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 538 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 518 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 503 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 499 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 471 |
| 37 | Don Mueang International Airport |  | TH | 470 |
| 38 | Amsterdam Airport Schiphol |  | NL | 469 |
| 39 | O. R. Tambo International Airport |  | ZA | 457 |
| 40 | Calgary International Airport |  | CA | 448 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 368 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 266 | 21m | 244 km | 1,120.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 205 | 1h 27m | 910 km | 3,216.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 192 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 181 | 19m | 165 km | 514.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 177 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 164 | 1h 12m | 770 km | 2,178.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 137 | 21m | 99 km | 234.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 117 | 27m | 152 km | 305.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 113 | 27m | 215 km | 418.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 112 | 20m | 147 km | 283.4 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 112 | 20m | 250 km | 483.8 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 102 | 1h 2m | 695 km | 1,222.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 100 | 58m | 493 km | 850.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 99 | 23m | 55 km | 94.1 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 93 | 52m | 556 km | 891.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 92 | 1h 19m | 961 km | 1,524.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-05-09 09:00 UTC | 2026-05-09 10:22 UTC | 1h 21m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Macau International Airport (VMMC) | 2026-05-08 19:56 UTC | 2026-05-09 10:21 UTC | 14h 24m |
| DLH6RK | Lufthansa | Frankfurt am Main International Airport (EDDF) | Napoli / Capodichino International Airport (LIRN) | 2026-05-09 08:51 UTC | 2026-05-09 10:19 UTC | 1h 27m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-08 19:22 UTC | 2026-05-09 10:10 UTC | 14h 47m |
| SXBDZ | SXB | Megara Airport (LGMG) | Sparti Airport (LGSP) | 2026-05-09 09:14 UTC | 2026-05-09 09:52 UTC | 38m |
| DAL2963 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 09:32 UTC | 2026-05-09 09:51 UTC | 19m |
| 4XCXT |  | Be'er Sheva (Teyman) Airport (LLBS) | Be'er Sheva (Teyman) Airport (LLBS) | 2026-05-09 09:41 UTC | 2026-05-09 09:47 UTC | 5m |
| RYR35CB | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Visoko Sport Airfield (LQVI) | 2026-05-09 08:37 UTC | 2026-05-09 09:47 UTC | 1h 10m |
| GIA2221 | Garuda Indonesia | Soekarno-Hatta International Airport (WIII) | Achmad Yani Airport (WARS) | 2026-05-09 09:10 UTC | 2026-05-09 09:46 UTC | 35m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 08:48 UTC | 2026-05-09 09:46 UTC | 57m |
| JST635 | JST | Brisbane International Airport (YBBN) | Avalon Airport (YMAV) | 2026-05-09 07:45 UTC | 2026-05-09 09:45 UTC | 2h 0m |
| FNK1 | FNK | Itzehoe/Hungriger Wolf Airport (EDHF) | Itzehoe/Hungriger Wolf Airport (EDHF) | 2026-05-09 09:23 UTC | 2026-05-09 09:40 UTC | 17m |
| NHZ22 | NHZ | Norwich International Airport (EGSH) | Beccles Airport (EGSM) | 2026-05-09 09:09 UTC | 2026-05-09 09:39 UTC | 29m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Kristiansund Airport Kvernberget (ENKB) | 2026-05-09 08:54 UTC | 2026-05-09 09:38 UTC | 44m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Bakki Airport (BIBA) | 2026-05-09 09:22 UTC | 2026-05-09 09:38 UTC | 16m |
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-05-09 09:21 UTC | 2026-05-09 09:38 UTC | 17m |
| DAL2245 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 08:32 UTC | 2026-05-09 09:36 UTC | 1h 4m |
| WZZ442V | Wizz Air | Katowice International Airport (EPKT) | Dortmund Airport (EDLW) | 2026-05-09 08:15 UTC | 2026-05-09 09:34 UTC | 1h 18m |
| IGO881 | IndiGo | VEVZ (VEVZ) | Hosur Airport (VO95) | 2026-05-09 06:51 UTC | 2026-05-09 09:33 UTC | 2h 41m |
| WIF1WL | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-05-09 09:04 UTC | 2026-05-09 09:30 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
