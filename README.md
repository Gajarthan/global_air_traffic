# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_21:45:57_UTC-green)

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

**Latest saved flight:** 2026-08-09 21:45:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 21:45:57 UTC

- **182,771** saved flights
- **58,350** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,771** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,197,174.5 tonnes** estimated CO2 emissions
- **127,372,433 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7259 |
| 2 | SkyWest Airlines | 6653 |
| 3 | EJA | 3614 |
| 4 | IndiGo | 3195 |
| 5 | Southwest Airlines | 2867 |
| 6 | American Airlines | 2856 |
| 7 | ENY | 2278 |
| 8 | Delta Air Lines | 2165 |
| 9 | LATAM Airlines | 1707 |
| 10 | AZU | 1638 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1508 |
| 14 | LXJ | 1445 |
| 15 | easyJet | 1254 |
| 16 | Swiss International | 1252 |
| 17 | AXM | 1226 |
| 18 | EJU | 1123 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1099 |
| 22 | VIV | 1006 |
| 23 | GLO | 981 |
| 24 | AEE | 954 |
| 25 | CXK | 952 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 925 |
| 30 | MXY | 914 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156419 |
| 2 | 🇪🇸 ES | 11750 |
| 3 | 🇧🇷 BR | 10496 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10009 |
| 6 | 🇨🇦 CA | 9950 |
| 7 | 🇮🇹 IT | 9468 |
| 8 | 🇩🇪 DE | 9053 |
| 9 | 🇬🇧 GB | 8478 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7283 |
| 12 | 🇨🇴 CO | 6832 |
| 13 | 🇬🇷 GR | 5360 |
| 14 | 🇲🇽 MX | 5220 |
| 15 | 🇨🇭 CH | 4879 |
| 16 | 🇹🇷 TR | 4746 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3064 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2343 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1850 |
| 27 | 🇭🇷 HR | 1827 |
| 28 | 🇲🇪 ME | 1650 |
| 29 | 🇳🇱 NL | 1643 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3790 |
| 2 | Denver International Airport |  | US | 3023 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2235 |
| 6 | Harry Reid International Airport |  | US | 2140 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1962 |
| 8 | Zurich Airport |  | CH | 1953 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1900 |
| 10 | La Aurora Airport |  | GT | 1798 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1667 |
| 12 | El Dorado International Airport |  | CO | 1639 |
| 13 | Chicago O'Hare International Airport |  | US | 1635 |
| 14 | Salt Lake City International Airport |  | US | 1633 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1523 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1447 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1434 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1365 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1306 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1263 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1240 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1140 |
| 30 | Ninoy Aquino International Airport |  | PH | 1135 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1119 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Viracopos International Airport |  | BR | 1050 |
| 34 | Reno/Tahoe International Airport |  | US | 1049 |
| 35 | Seattle-Tacoma International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1043 |
| 37 | Calgary International Airport |  | CA | 1040 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 999 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 671 | 21m | 244 km | 2,825.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 425 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 251 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 225 | 19m | 99 km | 385.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 223 | 1h 15m | 961 km | 3,696.3 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 221 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 199 | 1h 1m | 695 km | 2,385.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFG4105 | CFG | Frankfurt am Main International Airport (EDDF) | HE42 (HE42) | 2026-08-09 18:23 UTC | 2026-08-09 21:45 UTC | 3h 22m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-09 20:21 UTC | 2026-08-09 21:35 UTC | 1h 13m |
| EZY8364 | easyJet | L'Aquila / Preturo Airport (LIAP) | London Gatwick Airport (EGKK) | 2026-08-09 19:10 UTC | 2026-08-09 21:33 UTC | 2h 23m |
| N3563Q |  | Schaumburg Regional Airport (K06C) | IS63 (IS63) | 2026-08-09 20:45 UTC | 2026-08-09 21:29 UTC | 43m |
| CXK419 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-08-09 21:11 UTC | 2026-08-09 21:28 UTC | 17m |
| N1241U |  | Pensacola International Airport (KPNS) | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | 2026-08-09 21:09 UTC | 2026-08-09 21:22 UTC | 12m |
| N1308T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-09 17:27 UTC | 2026-08-09 21:21 UTC | 3h 53m |
| N232TB |  | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-09 21:17 UTC | 2026-08-09 21:18 UTC | 1m |
| TGGMP | TGG | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-08-09 20:59 UTC | 2026-08-09 21:18 UTC | 18m |
| N1028S |  | Lykes Silver Lake Airport (FL36) | Lykes Silver Lake Airport (FL36) | 2026-08-09 20:56 UTC | 2026-08-09 21:13 UTC | 16m |
| N330VA |  | Ann Arbor Municipal Airport (KARB) | Lenawee County Airport (KADG) | 2026-08-09 19:50 UTC | 2026-08-09 21:10 UTC | 1h 19m |
| N515TC |  | Des Moines International Airport (KDSM) | Jesse Viertel Memorial Airport (KVER) | 2026-08-09 20:41 UTC | 2026-08-09 21:05 UTC | 23m |
| MSR931 | EgyptAir | Buraimi Airport (OOBR) | HE13 (HE13) | 2026-08-09 18:13 UTC | 2026-08-09 21:02 UTC | 2h 48m |
| EZY65PM | easyJet | London Gatwick Airport (EGKK) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-09 19:29 UTC | 2026-08-09 21:00 UTC | 1h 31m |
| N901ST |  | Hendrickson Flying Service Airport (IL93) | Rochelle Municipal/Koritz Field (KRPJ) | 2026-08-09 19:50 UTC | 2026-08-09 21:00 UTC | 1h 10m |
| N680DJ |  | Weaver Airport (MT54) | Centennial Airport (KAPA) | 2026-08-09 19:18 UTC | 2026-08-09 21:00 UTC | 1h 42m |
| N500RG |  | 80TX (80TX) | Austin-Bergstrom International Airport (KAUS) | 2026-08-09 20:14 UTC | 2026-08-09 20:59 UTC | 45m |
| N410GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-08-09 20:35 UTC | 2026-08-09 20:58 UTC | 22m |
| EJA511 | EJA | Rochester International Airport (KRST) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-09 17:04 UTC | 2026-08-09 20:57 UTC | 3h 52m |
| N237GR |  | James M Cox Dayton International Airport (KDAY) | Boyne Mountain Airport (KBFA) | 2026-08-09 20:09 UTC | 2026-08-09 20:57 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
