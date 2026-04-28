# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_01:09:48_UTC-green)

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

**Latest saved flight:** 2026-04-28 01:09:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 01:09:48 UTC

- **57,560** saved flights
- **22,504** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,560** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **698,381.5 tonnes** estimated CO2 emissions
- **40,485,882 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2442 |
| 2 | SkyWest Airlines | 2189 |
| 3 | IndiGo | 1298 |
| 4 | EJA | 1030 |
| 5 | American Airlines | 913 |
| 6 | Southwest Airlines | 825 |
| 7 | ENY | 726 |
| 8 | Lufthansa | 710 |
| 9 | Vueling | 574 |
| 10 | AXM | 557 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 504 |
| 13 | AZU | 482 |
| 14 | WIF | 478 |
| 15 | Delta Air Lines | 474 |
| 16 | Swiss International | 450 |
| 17 | QLK | 446 |
| 18 | LXJ | 413 |
| 19 | Alaska Airlines | 393 |
| 20 | AEE | 380 |
| 21 | easyJet | 377 |
| 22 | EJU | 370 |
| 23 | VIV | 369 |
| 24 | Air France | 334 |
| 25 | Japan Airlines | 330 |
| 26 | Cathay Pacific | 329 |
| 27 | AXB | 312 |
| 28 | JetBlue | 294 |
| 29 | United Airlines | 290 |
| 30 | GLO | 288 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45811 |
| 2 | 🇪🇸 ES | 4186 |
| 3 | 🇮🇳 IN | 4094 |
| 4 | 🇦🇺 AU | 3867 |
| 5 | 🇧🇷 BR | 3294 |
| 6 | 🇮🇹 IT | 3140 |
| 7 | 🇩🇪 DE | 3139 |
| 8 | 🇯🇵 JP | 3069 |
| 9 | 🇨🇦 CA | 2854 |
| 10 | 🇨🇴 CO | 2604 |
| 11 | 🇬🇧 GB | 2441 |
| 12 | 🇫🇷 FR | 2256 |
| 13 | 🇲🇽 MX | 1827 |
| 14 | 🇬🇷 GR | 1706 |
| 15 | 🇨🇭 CH | 1606 |
| 16 | 🇳🇴 NO | 1550 |
| 17 | 🇲🇾 MY | 1351 |
| 18 | 🇿🇦 ZA | 1165 |
| 19 | 🇳🇿 NZ | 1088 |
| 20 | 🇹🇷 TR | 1048 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 968 |
| 23 | 🇵🇱 PL | 925 |
| 24 | 🇰🇷 KR | 907 |
| 25 | 🇬🇹 GT | 847 |
| 26 | 🇲🇦 MA | 726 |
| 27 | 🇲🇪 ME | 623 |
| 28 | 🇲🇴 MO | 608 |
| 29 | 🇳🇱 NL | 598 |
| 30 | 🇮🇩 ID | 493 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1308 |
| 2 | Tokyo International Airport |  | JP | 1042 |
| 3 | Denver International Airport |  | US | 966 |
| 4 | El Dorado International Airport |  | CO | 878 |
| 5 | Indira Gandhi International Airport |  | IN | 869 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 841 |
| 7 | Guaymaral Airport |  | CO | 800 |
| 8 | Harry Reid International Airport |  | US | 735 |
| 9 | Frankfurt am Main International Airport |  | DE | 699 |
| 10 | Zurich Airport |  | CH | 687 |
| 11 | La Aurora Airport |  | GT | 638 |
| 12 | Macau International Airport |  | MO | 608 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 574 |
| 14 | Chicago O'Hare International Airport |  | US | 555 |
| 15 | Madrid Barajas International Airport |  | ES | 536 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 17 | Kuala Lumpur International Airport |  | MY | 534 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 507 |
| 19 | Malpensa International Airport |  | IT | 497 |
| 20 | Bengaluru International Airport |  | IN | 490 |
| 21 | Congonhas Airport |  | BR | 474 |
| 22 | Charlotte/Douglas International Airport |  | US | 463 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Salt Lake City International Airport |  | US | 448 |
| 25 | Ninoy Aquino International Airport |  | PH | 445 |
| 26 | Charles de Gaulle International Airport |  | FR | 442 |
| 27 | Capua Airport |  | IT | 437 |
| 28 | Daniel K Inouye International Airport |  | US | 426 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 424 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 409 |
| 31 | Barcelona International Airport |  | ES | 392 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 33 | Vitoria/Foronda Airport |  | ES | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 379 |
| 35 | Reno/Tahoe International Airport |  | US | 374 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 37 | O. R. Tambo International Airport |  | ZA | 367 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 342 |
| 40 | Calgary International Airport |  | CA | 341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 185 | 21m | 244 km | 779.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 164 | 1h 27m | 910 km | 2,573.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 131 | 26m | 275 km | 620.8 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 113 | 1h 12m | 770 km | 1,501.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 73 | 1h 42m | 1,423 km | 1,791.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N309FA |  | Harrisburg International Airport (KMDT) | Lehigh Valley International Airport (KABE) | 2026-04-28 00:32 UTC | 2026-04-28 01:09 UTC | 37m |
| N3386E |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-04-28 00:27 UTC | 2026-04-28 01:07 UTC | 40m |
| N26WR |  | Gnoss Field (KDVO) | Santa Monica Municipal Airport (KSMO) | 2026-04-27 23:49 UTC | 2026-04-28 00:59 UTC | 1h 10m |
| N180JW |  | NY09 (NY09) | Lancaster Airport (KLNS) | 2026-04-27 23:50 UTC | 2026-04-28 00:57 UTC | 1h 7m |
| AERT8 | AER | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-04-27 23:53 UTC | 2026-04-28 00:52 UTC | 58m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-27 20:27 UTC | 2026-04-28 00:50 UTC | 4h 23m |
| N408GG |  | Linden Airport (KLDJ) | Linden Airport (KLDJ) | 2026-04-27 22:51 UTC | 2026-04-28 00:48 UTC | 1h 57m |
| TMN7D | TMN | Auckland International Airport (NZAA) | Melbourne International Airport (YMML) | 2026-04-27 21:21 UTC | 2026-04-28 00:44 UTC | 3h 22m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-04-28 00:27 UTC | 2026-04-28 00:42 UTC | 14m |
| SIL1403 | SIL | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-04-27 23:56 UTC | 2026-04-28 00:38 UTC | 41m |
| SCU36 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-04-28 00:27 UTC | 2026-04-28 00:33 UTC | 5m |
| FD478 |  | Toowoomba Airport (YTWB) | Maryborough Airport (YMYB) | 2026-04-27 23:53 UTC | 2026-04-28 00:26 UTC | 32m |
| PE993 |  | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-27 23:39 UTC | 2026-04-28 00:26 UTC | 47m |
| PLC3 | PLC | Auckland International Airport (NZAA) | Auckland International Airport (NZAA) | 2026-04-27 23:57 UTC | 2026-04-28 00:21 UTC | 23m |
| ETD2NP | Etihad Airways | Manchester Airport (EGCC) | Queen Alia International Airport (OJAI) | 2026-04-27 20:18 UTC | 2026-04-28 00:19 UTC | 4h 0m |
| N761QS |  | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Bermuda Dunes Airport (KUDD) | 2026-04-27 19:26 UTC | 2026-04-28 00:17 UTC | 4h 51m |
| N20225 |  | Dekalb-Peachtree Airport (KPDK) | Richard B Russell Regional - J H Towers Field (KRMG) | 2026-04-27 23:42 UTC | 2026-04-28 00:16 UTC | 34m |
| ZKUSK | ZKU | Feilding Airport (NZFI) | Feilding Airport (NZFI) | 2026-04-27 23:50 UTC | 2026-04-28 00:15 UTC | 24m |
| ZJO | ZJO | Melbourne Essendon Airport (YMEN) | Melbourne Moorabbin Airport (YMMB) | 2026-04-27 22:52 UTC | 2026-04-28 00:13 UTC | 1h 20m |
| N317KC |  | Merrill Field (PAMR) | Tin Creek Airport (PAFL) | 2026-04-27 23:35 UTC | 2026-04-28 00:11 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
