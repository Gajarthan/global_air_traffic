# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_04:33:33_UTC-green)

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

**Latest saved flight:** 2026-05-21 04:33:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 04:33:33 UTC

- **89,693** saved flights
- **31,975** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,693** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,109,547.8 tonnes** estimated CO2 emissions
- **64,321,610 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3840 |
| 2 | SkyWest Airlines | 3333 |
| 3 | IndiGo | 1890 |
| 4 | EJA | 1696 |
| 5 | American Airlines | 1368 |
| 6 | Southwest Airlines | 1300 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1106 |
| 9 | Delta Air Lines | 987 |
| 10 | Vueling | 853 |
| 11 | LATAM Airlines | 807 |
| 12 | AXM | 795 |
| 13 | WIF | 776 |
| 14 | AZU | 713 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 675 |
| 17 | LXJ | 668 |
| 18 | Alaska Airlines | 638 |
| 19 | QLK | 635 |
| 20 | easyJet | 589 |
| 21 | Cathay Pacific | 578 |
| 22 | EJU | 576 |
| 23 | AEE | 552 |
| 24 | VIV | 535 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 481 |
| 27 | CXK | 470 |
| 28 | AXB | 460 |
| 29 | MXY | 457 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73889 |
| 2 | 🇪🇸 ES | 6351 |
| 3 | 🇮🇳 IN | 5928 |
| 4 | 🇦🇺 AU | 5597 |
| 5 | 🇩🇪 DE | 4958 |
| 6 | 🇮🇹 IT | 4955 |
| 7 | 🇧🇷 BR | 4920 |
| 8 | 🇨🇦 CA | 4494 |
| 9 | 🇯🇵 JP | 4377 |
| 10 | 🇬🇧 GB | 3820 |
| 11 | 🇫🇷 FR | 3593 |
| 12 | 🇨🇴 CO | 3079 |
| 13 | 🇲🇽 MX | 2778 |
| 14 | 🇬🇷 GR | 2582 |
| 15 | 🇳🇴 NO | 2487 |
| 16 | 🇨🇭 CH | 2355 |
| 17 | 🇲🇾 MY | 1996 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1629 |
| 20 | 🇳🇿 NZ | 1550 |
| 21 | 🇹🇭 TH | 1525 |
| 22 | 🇵🇱 PL | 1480 |
| 23 | 🇰🇷 KR | 1402 |
| 24 | 🇵🇭 PH | 1381 |
| 25 | 🇬🇹 GT | 1339 |
| 26 | 🇲🇴 MO | 1035 |
| 27 | 🇲🇦 MA | 1032 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 907 |
| 30 | 🇭🇷 HR | 808 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1963 |
| 2 | Denver International Airport |  | US | 1507 |
| 3 | Tokyo International Airport |  | JP | 1460 |
| 4 | Indira Gandhi International Airport |  | IN | 1283 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1216 |
| 6 | Harry Reid International Airport |  | US | 1149 |
| 7 | Frankfurt am Main International Airport |  | DE | 1126 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1049 |
| 10 | Macau International Airport |  | MO | 1035 |
| 11 | La Aurora Airport |  | GT | 1019 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 992 |
| 13 | El Dorado International Airport |  | CO | 980 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 913 |
| 15 | Chicago O'Hare International Airport |  | US | 867 |
| 16 | Madrid Barajas International Airport |  | ES | 814 |
| 17 | Kuala Lumpur International Airport |  | MY | 791 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 770 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 756 |
| 21 | Malpensa International Airport |  | IT | 727 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 727 |
| 23 | Bengaluru International Airport |  | IN | 713 |
| 24 | Charles de Gaulle International Airport |  | FR | 699 |
| 25 | Congonhas Airport |  | BR | 690 |
| 26 | Charlotte/Douglas International Airport |  | US | 689 |
| 27 | Daniel K Inouye International Airport |  | US | 657 |
| 28 | Tenerife Norte Airport |  | ES | 654 |
| 29 | Ninoy Aquino International Airport |  | PH | 635 |
| 30 | Barcelona International Airport |  | ES | 602 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 600 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 589 |
| 34 | Vitoria/Foronda Airport |  | ES | 569 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 567 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Amsterdam Airport Schiphol |  | NL | 557 |
| 38 | Don Mueang International Airport |  | TH | 556 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 333 | 21m | 244 km | 1,402.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 248 | 24m | 225 km | 962.1 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 235 | 14m | 114 km | 460.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 229 | 28m | 304 km | 1,200.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 229 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 205 | 1h 10m | 770 km | 2,723.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 195 | 19m | 165 km | 554.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 185 | 26m | 275 km | 876.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 137 | 31m | 369 km | 872.0 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 132 | 22m | 55 km | 125.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 128 | 14m | 154 km | 339.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 04:13 UTC | 2026-05-21 04:33 UTC | 20m |
| VAR853 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 04:10 UTC | 2026-05-21 04:32 UTC | 21m |
| ZJI | ZJI | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-05-21 04:02 UTC | 2026-05-21 04:30 UTC | 27m |
| N677TX |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-21 03:52 UTC | 2026-05-21 04:30 UTC | 37m |
| N352FS |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-05-21 04:04 UTC | 2026-05-21 04:29 UTC | 24m |
| N108UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-05-21 03:23 UTC | 2026-05-21 04:25 UTC | 1h 1m |
| N541SF |  | Skypark Airport (KBTF) | Nephi Municipal Airport (KU14) | 2026-05-21 03:32 UTC | 2026-05-21 04:16 UTC | 43m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-21 03:48 UTC | 2026-05-21 04:14 UTC | 25m |
| NTX | NTX | Melbourne Moorabbin Airport (YMMB) | Echuca Airport (YECH) | 2026-05-21 03:38 UTC | 2026-05-21 04:12 UTC | 33m |
| N205BR |  | Henderson Executive Airport (KHND) | Henderson Executive Airport (KHND) | 2026-05-21 03:45 UTC | 2026-05-21 04:11 UTC | 26m |
| KING67 | KIN | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-05-21 03:27 UTC | 2026-05-21 04:03 UTC | 35m |
| N352FS |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-05-21 03:31 UTC | 2026-05-21 03:54 UTC | 23m |
| VAR448 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 03:15 UTC | 2026-05-21 03:48 UTC | 32m |
| ANA793 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-05-21 02:36 UTC | 2026-05-21 03:44 UTC | 1h 8m |
| VAR425 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 03:24 UTC | 2026-05-21 03:43 UTC | 19m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-21 03:19 UTC | 2026-05-21 03:38 UTC | 18m |
| VAR493 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-21 03:17 UTC | 2026-05-21 03:36 UTC | 19m |
| HL5247 |  | Gimpo International Airport (RKSS) | G 419 Airport (RK48) | 2026-05-21 03:11 UTC | 2026-05-21 03:34 UTC | 22m |
| SWT1810 | SWT | Cologne Bonn Airport (EDDK) | Vitoria/Foronda Airport (LEVT) | 2026-05-21 02:01 UTC | 2026-05-21 03:33 UTC | 1h 32m |
| N279PD |  | Mc Clellan Airfield (KMCC) | Sacramento Executive Airport (KSAC) | 2026-05-21 03:17 UTC | 2026-05-21 03:31 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
