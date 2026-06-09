# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_17:23:10_UTC-green)

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

**Latest saved flight:** 2026-06-09 17:23:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-09 17:23:10 UTC

- **107,123** saved flights
- **37,586** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,123** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,309,508.6 tonnes** estimated CO2 emissions
- **75,913,542 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4405 |
| 2 | SkyWest Airlines | 4028 |
| 3 | IndiGo | 2122 |
| 4 | EJA | 2068 |
| 5 | American Airlines | 1711 |
| 6 | Southwest Airlines | 1614 |
| 7 | ENY | 1341 |
| 8 | Delta Air Lines | 1274 |
| 9 | Lufthansa | 1223 |
| 10 | Vueling | 983 |
| 11 | LATAM Airlines | 952 |
| 12 | WIF | 939 |
| 13 | AXM | 910 |
| 14 | AZU | 874 |
| 15 | LXJ | 808 |
| 16 | Swiss International | 779 |
| 17 | All Nippon Airways | 741 |
| 18 | Alaska Airlines | 738 |
| 19 | QLK | 711 |
| 20 | easyJet | 692 |
| 21 | EJU | 682 |
| 22 | Cathay Pacific | 643 |
| 23 | AEE | 613 |
| 24 | VIV | 613 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 579 |
| 28 | CXK | 565 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 523 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90202 |
| 2 | 🇪🇸 ES | 7354 |
| 3 | 🇮🇳 IN | 6682 |
| 4 | 🇦🇺 AU | 6403 |
| 5 | 🇧🇷 BR | 5909 |
| 6 | 🇩🇪 DE | 5743 |
| 7 | 🇮🇹 IT | 5739 |
| 8 | 🇨🇦 CA | 5608 |
| 9 | 🇯🇵 JP | 4874 |
| 10 | 🇬🇧 GB | 4550 |
| 11 | 🇫🇷 FR | 4259 |
| 12 | 🇨🇴 CO | 3713 |
| 13 | 🇲🇽 MX | 3209 |
| 14 | 🇬🇷 GR | 3045 |
| 15 | 🇳🇴 NO | 2964 |
| 16 | 🇨🇭 CH | 2734 |
| 17 | 🇲🇾 MY | 2336 |
| 18 | 🇹🇷 TR | 2072 |
| 19 | 🇿🇦 ZA | 1840 |
| 20 | 🇰🇷 KR | 1779 |
| 21 | 🇳🇿 NZ | 1776 |
| 22 | 🇹🇭 TH | 1759 |
| 23 | 🇵🇱 PL | 1745 |
| 24 | 🇵🇭 PH | 1567 |
| 25 | 🇬🇹 GT | 1548 |
| 26 | 🇲🇦 MA | 1182 |
| 27 | 🇲🇴 MO | 1118 |
| 28 | 🇳🇱 NL | 1049 |
| 29 | 🇲🇪 ME | 1026 |
| 30 | 🇭🇷 HR | 929 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2319 |
| 2 | Denver International Airport |  | US | 1822 |
| 3 | Tokyo International Airport |  | JP | 1613 |
| 4 | Indira Gandhi International Airport |  | IN | 1453 |
| 5 | Harry Reid International Airport |  | US | 1367 |
| 6 | Guaymaral Airport |  | CO | 1360 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1345 |
| 8 | Zurich Airport |  | CH | 1216 |
| 9 | Frankfurt am Main International Airport |  | DE | 1210 |
| 10 | La Aurora Airport |  | GT | 1191 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1159 |
| 12 | El Dorado International Airport |  | CO | 1128 |
| 13 | Macau International Airport |  | MO | 1118 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1079 |
| 15 | Chicago O'Hare International Airport |  | US | 1072 |
| 16 | Madrid Barajas International Airport |  | ES | 932 |
| 17 | Capua Airport |  | IT | 915 |
| 18 | Kuala Lumpur International Airport |  | MY | 915 |
| 19 | Salt Lake City International Airport |  | US | 913 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 913 |
| 21 | Charlotte/Douglas International Airport |  | US | 832 |
| 22 | Congonhas Airport |  | BR | 816 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 814 |
| 24 | Charles de Gaulle International Airport |  | FR | 812 |
| 25 | Bengaluru International Airport |  | IN | 803 |
| 26 | Malpensa International Airport |  | IT | 797 |
| 27 | Daniel K Inouye International Airport |  | US | 725 |
| 28 | Ninoy Aquino International Airport |  | PH | 718 |
| 29 | Tenerife Norte Airport |  | ES | 718 |
| 30 | Barcelona International Airport |  | ES | 701 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 697 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 696 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 696 |
| 34 | Amsterdam Airport Schiphol |  | NL | 649 |
| 35 | Don Mueang International Airport |  | TH | 643 |
| 36 | Vitoria/Foronda Airport |  | ES | 640 |
| 37 | Calgary International Airport |  | CA | 632 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 616 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 607 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 563 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 393 | 21m | 244 km | 1,654.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 245 | 1h 10m | 770 km | 3,254.6 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 214 | 26m | 275 km | 1,014.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 205 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 145 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 126 | 44m | 241 km | 523.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 125 | 1h 43m | 1,423 km | 3,067.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 121 | 1h 18m | 961 km | 2,005.6 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MSR848 | EgyptAir | Mohammed V International Airport (GMMN) | HE12 (HE12) | 2026-06-09 12:49 UTC | 2026-06-09 17:23 UTC | 4h 33m |
| DRAG55 | DRA | Boron Airstrip (57CL) | Edwards Af Aux North Base Airport (K9L2) | 2026-06-09 17:03 UTC | 2026-06-09 17:19 UTC | 15m |
| N972TH |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-06-09 16:57 UTC | 2026-06-09 17:16 UTC | 18m |
| GRIT17 | GRI | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-06-09 16:40 UTC | 2026-06-09 17:13 UTC | 32m |
| N331CH |  | Platte Valley Airpark (K18V) | Platte Valley Airpark (K18V) | 2026-06-09 16:54 UTC | 2026-06-09 17:13 UTC | 18m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-06-09 16:42 UTC | 2026-06-09 17:11 UTC | 29m |
| LYPPL | LYP | Paluknys Airport (EYVP) | Rudiskes Airport (EYRD) | 2026-06-09 16:04 UTC | 2026-06-09 17:11 UTC | 1h 6m |
| AS36 |  | 29TA (29TA) | TX20 (TX20) | 2026-06-09 16:47 UTC | 2026-06-09 17:04 UTC | 16m |
| N296CB |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-06-09 16:54 UTC | 2026-06-09 17:04 UTC | 10m |
| N216SR |  | Camp Bullis Als (Cals) Airport (9TX5) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-06-09 16:29 UTC | 2026-06-09 17:04 UTC | 34m |
| N5726B |  | Mariposa-Yosemite Airport (KMPI) | Mariposa-Yosemite Airport (KMPI) | 2026-06-09 16:56 UTC | 2026-06-09 16:59 UTC | 3m |
| N169TS |  | Beryl Junction Airport (UT82) | KXTA (KXTA) | 2026-06-09 15:28 UTC | 2026-06-09 16:56 UTC | 1h 27m |
| N733JH |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-06-09 16:32 UTC | 2026-06-09 16:55 UTC | 23m |
| BOE123 | BOE | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-06-09 14:38 UTC | 2026-06-09 16:55 UTC | 2h 17m |
| KMI525 | KMI | Gia Lam Air Base (VVGL) | Zhuhai Airport (ZGSD) | 2026-06-09 15:50 UTC | 2026-06-09 16:55 UTC | 1h 5m |
| UAL957 | United Airlines | Geneva Cointrin International Airport (LSGG) | Newark Liberty International Airport (KEWR) | 2026-06-09 08:36 UTC | 2026-06-09 16:52 UTC | 8h 15m |
| N19819 |  | Bangor International Airport (KBGR) | Bangor International Airport (KBGR) | 2026-06-09 16:38 UTC | 2026-06-09 16:50 UTC | 12m |
| RNGR805 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-06-09 14:39 UTC | 2026-06-09 16:50 UTC | 2h 10m |
| N308GT |  | Meadows Field (KBFL) | Reno/Tahoe International Airport (KRNO) | 2026-06-09 16:01 UTC | 2026-06-09 16:46 UTC | 45m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-09 16:16 UTC | 2026-06-09 16:43 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
