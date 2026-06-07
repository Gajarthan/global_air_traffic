# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_11:56:12_UTC-green)

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

**Latest saved flight:** 2026-06-07 11:56:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 11:56:12 UTC

- **105,242** saved flights
- **37,034** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,242** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,287,851.4 tonnes** estimated CO2 emissions
- **74,658,052 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4330 |
| 2 | SkyWest Airlines | 3961 |
| 3 | IndiGo | 2097 |
| 4 | EJA | 2009 |
| 5 | American Airlines | 1691 |
| 6 | Southwest Airlines | 1591 |
| 7 | ENY | 1320 |
| 8 | Delta Air Lines | 1244 |
| 9 | Lufthansa | 1209 |
| 10 | Vueling | 970 |
| 11 | LATAM Airlines | 929 |
| 12 | WIF | 920 |
| 13 | AXM | 906 |
| 14 | AZU | 842 |
| 15 | LXJ | 792 |
| 16 | Swiss International | 763 |
| 17 | All Nippon Airways | 737 |
| 18 | Alaska Airlines | 730 |
| 19 | QLK | 708 |
| 20 | easyJet | 684 |
| 21 | EJU | 665 |
| 22 | Cathay Pacific | 629 |
| 23 | AEE | 608 |
| 24 | Air France | 603 |
| 25 | VIV | 603 |
| 26 | United Airlines | 585 |
| 27 | MXY | 571 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 525 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88469 |
| 2 | 🇪🇸 ES | 7248 |
| 3 | 🇮🇳 IN | 6610 |
| 4 | 🇦🇺 AU | 6353 |
| 5 | 🇧🇷 BR | 5727 |
| 6 | 🇩🇪 DE | 5655 |
| 7 | 🇮🇹 IT | 5607 |
| 8 | 🇨🇦 CA | 5473 |
| 9 | 🇯🇵 JP | 4850 |
| 10 | 🇬🇧 GB | 4450 |
| 11 | 🇫🇷 FR | 4185 |
| 12 | 🇨🇴 CO | 3634 |
| 13 | 🇲🇽 MX | 3148 |
| 14 | 🇬🇷 GR | 2998 |
| 15 | 🇳🇴 NO | 2915 |
| 16 | 🇨🇭 CH | 2697 |
| 17 | 🇲🇾 MY | 2324 |
| 18 | 🇹🇷 TR | 2026 |
| 19 | 🇿🇦 ZA | 1816 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1754 |
| 22 | 🇹🇭 TH | 1746 |
| 23 | 🇵🇱 PL | 1713 |
| 24 | 🇵🇭 PH | 1557 |
| 25 | 🇬🇹 GT | 1526 |
| 26 | 🇲🇦 MA | 1165 |
| 27 | 🇲🇴 MO | 1104 |
| 28 | 🇳🇱 NL | 1033 |
| 29 | 🇲🇪 ME | 1006 |
| 30 | 🇭🇷 HR | 917 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2285 |
| 2 | Denver International Airport |  | US | 1801 |
| 3 | Tokyo International Airport |  | JP | 1606 |
| 4 | Indira Gandhi International Airport |  | IN | 1437 |
| 5 | Harry Reid International Airport |  | US | 1346 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1333 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1201 |
| 9 | Zurich Airport |  | CH | 1194 |
| 10 | La Aurora Airport |  | GT | 1174 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1133 |
| 12 | El Dorado International Airport |  | CO | 1108 |
| 13 | Macau International Airport |  | MO | 1104 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1065 |
| 15 | Chicago O'Hare International Airport |  | US | 1059 |
| 16 | Madrid Barajas International Airport |  | ES | 921 |
| 17 | Kuala Lumpur International Airport |  | MY | 911 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 899 |
| 19 | Salt Lake City International Airport |  | US | 898 |
| 20 | Capua Airport |  | IT | 889 |
| 21 | Charlotte/Douglas International Airport |  | US | 816 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 810 |
| 23 | Charles de Gaulle International Airport |  | FR | 801 |
| 24 | Congonhas Airport |  | BR | 795 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 787 |
| 27 | Daniel K Inouye International Airport |  | US | 719 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 713 |
| 30 | Barcelona International Airport |  | ES | 692 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 679 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 675 |
| 34 | Amsterdam Airport Schiphol |  | NL | 641 |
| 35 | Don Mueang International Airport |  | TH | 639 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 604 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 601 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 387 | 21m | 244 km | 1,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 259 | 1h 25m | 910 km | 4,064.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 243 | 1h 10m | 770 km | 3,228.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 219 | 19m | 165 km | 623.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 153 | 27m | 215 km | 566.6 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 149 | 14m | 154 km | 394.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 141 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 137 | 18m | 144 km | 340.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 121 | 44m | 241 km | 502.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGIJO | CGI | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-06-07 11:38 UTC | 2026-06-07 11:56 UTC | 17m |
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-07 11:01 UTC | 2026-06-07 11:48 UTC | 46m |
| HKC9488 | HKC | Istanbul Airport (LTFM) | Zhuhai Airport (ZGSD) | 2026-06-06 23:39 UTC | 2026-06-07 11:47 UTC | 12h 7m |
| HBTDZ | HBT | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-06-07 11:06 UTC | 2026-06-07 11:44 UTC | 37m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-06-06 21:37 UTC | 2026-06-07 11:44 UTC | 14h 7m |
| CXK594 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-07 11:01 UTC | 2026-06-07 11:30 UTC | 28m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-06-07 10:41 UTC | 2026-06-07 11:20 UTC | 39m |
| HWS02 | HWS | Trollhattan-Vanersborg Airport (ESGT) | Trollhattan-Vanersborg Airport (ESGT) | 2026-06-07 11:15 UTC | 2026-06-07 11:16 UTC | 1m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-07 10:29 UTC | 2026-06-07 11:12 UTC | 42m |
| CXK549 | CXK | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-07 10:00 UTC | 2026-06-07 11:08 UTC | 1h 8m |
| D9720 |  | Schanis Airport (LSZX) | Schanis Airport (LSZX) | 2026-06-07 09:52 UTC | 2026-06-07 11:05 UTC | 1h 13m |
| LYBAY | LYB | Klaipeda Airport (EYKL) | Klaipeda Airport (EYKL) | 2026-06-07 11:02 UTC | 2026-06-07 11:03 UTC | 1m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-07 10:51 UTC | 2026-06-07 11:03 UTC | 12m |
| THA136 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-06-07 10:10 UTC | 2026-06-07 11:03 UTC | 52m |
| WIF8HK | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-07 10:45 UTC | 2026-06-07 11:01 UTC | 15m |
| DTR69V | DTR | Pantelleria Airport (LICG) | LICL (LICL) | 2026-06-07 10:24 UTC | 2026-06-07 11:00 UTC | 36m |
| CXK282 | CXK | Hampton Roads Executive Airport (KPVG) | Chesapeake Regional Airport (KCPK) | 2026-06-07 10:28 UTC | 2026-06-07 10:58 UTC | 30m |
| MAS1276 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-06-07 10:46 UTC | 2026-06-07 10:58 UTC | 11m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-06-07 10:09 UTC | 2026-06-07 10:56 UTC | 47m |
| LOT513 | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Iasi Airport (LRIA) | 2026-06-07 09:37 UTC | 2026-06-07 10:51 UTC | 1h 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
