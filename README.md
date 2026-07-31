# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_11:56:02_UTC-green)

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

**Latest saved flight:** 2026-07-31 11:56:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 11:56:02 UTC

- **162,237** saved flights
- **53,486** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **162,237** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,947,190.4 tonnes** estimated CO2 emissions
- **112,880,603 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6481 |
| 2 | SkyWest Airlines | 5910 |
| 3 | EJA | 3210 |
| 4 | IndiGo | 2845 |
| 5 | American Airlines | 2562 |
| 6 | Southwest Airlines | 2539 |
| 7 | ENY | 2018 |
| 8 | Delta Air Lines | 1925 |
| 9 | Lufthansa | 1528 |
| 10 | LATAM Airlines | 1524 |
| 11 | AZU | 1425 |
| 12 | WIF | 1371 |
| 13 | Vueling | 1346 |
| 14 | LXJ | 1261 |
| 15 | AXM | 1129 |
| 16 | Swiss International | 1117 |
| 17 | easyJet | 1068 |
| 18 | Alaska Airlines | 1007 |
| 19 | QLK | 1003 |
| 20 | EJU | 1000 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 892 |
| 23 | CXK | 866 |
| 24 | Cathay Pacific | 856 |
| 25 | United Airlines | 855 |
| 26 | GLO | 851 |
| 27 | AEE | 850 |
| 28 | Air France | 841 |
| 29 | MXY | 840 |
| 30 | JetBlue | 827 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140026 |
| 2 | 🇪🇸 ES | 10401 |
| 3 | 🇧🇷 BR | 9265 |
| 4 | 🇦🇺 AU | 9200 |
| 5 | 🇮🇳 IN | 8951 |
| 6 | 🇨🇦 CA | 8817 |
| 7 | 🇮🇹 IT | 8360 |
| 8 | 🇩🇪 DE | 8175 |
| 9 | 🇬🇧 GB | 7447 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6421 |
| 12 | 🇨🇴 CO | 5758 |
| 13 | 🇬🇷 GR | 4660 |
| 14 | 🇲🇽 MX | 4651 |
| 15 | 🇳🇴 NO | 4283 |
| 16 | 🇨🇭 CH | 4267 |
| 17 | 🇹🇷 TR | 3872 |
| 18 | 🇲🇾 MY | 2933 |
| 19 | 🇵🇱 PL | 2759 |
| 20 | 🇿🇦 ZA | 2635 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2308 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2077 |
| 26 | 🇲🇦 MA | 1635 |
| 27 | 🇲🇪 ME | 1530 |
| 28 | 🇭🇷 HR | 1518 |
| 29 | 🇳🇱 NL | 1483 |
| 30 | 🇲🇴 MO | 1357 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3312 |
| 2 | Denver International Airport |  | US | 2694 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2035 |
| 5 | Indira Gandhi International Airport |  | IN | 1991 |
| 6 | Harry Reid International Airport |  | US | 1968 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1791 |
| 8 | Zurich Airport |  | CH | 1733 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1703 |
| 10 | La Aurora Airport |  | GT | 1613 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1507 |
| 12 | El Dorado International Airport |  | CO | 1483 |
| 13 | Frankfurt am Main International Airport |  | DE | 1478 |
| 14 | Chicago O'Hare International Airport |  | US | 1468 |
| 15 | Salt Lake City International Airport |  | US | 1458 |
| 16 | Macau International Airport |  | MO | 1357 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1353 |
| 18 | Congonhas Airport |  | BR | 1346 |
| 19 | Madrid Barajas International Airport |  | ES | 1282 |
| 20 | Capua Airport |  | IT | 1274 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1238 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1151 |
| 24 | Charlotte/Douglas International Airport |  | US | 1140 |
| 25 | Kuala Lumpur International Airport |  | MY | 1116 |
| 26 | Charles de Gaulle International Airport |  | FR | 1108 |
| 27 | Malpensa International Airport |  | IT | 1073 |
| 28 | Bengaluru International Airport |  | IN | 1062 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 991 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 984 |
| 32 | Barcelona International Airport |  | ES | 962 |
| 33 | Daniel K Inouye International Airport |  | US | 953 |
| 34 | Seattle-Tacoma International Airport |  | US | 942 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 923 |
| 37 | Tenerife Norte Airport |  | ES | 909 |
| 38 | Scottsdale Airport |  | US | 908 |
| 39 | Oslo Gardermoen Airport |  | NO | 905 |
| 40 | Reno/Tahoe International Airport |  | US | 889 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 853 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 591 | 21m | 244 km | 2,488.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 387 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 298 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 239 | 19m | 165 km | 679.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 239 | 22m | 55 km | 227.2 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 235 | 44m | 241 km | 976.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 222 | 1h 47m | 1,423 km | 5,448.2 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 206 | 20m | 250 km | 889.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 204 | 20m | 99 km | 349.4 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 198 | 30m | 49 km | 167.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 193 | 1h 15m | 961 km | 3,199.1 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 193 | 28m | 152 km | 504.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 191 | 18m | 144 km | 475.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 180 | 1h 1m | 695 km | 2,157.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 49m | 1,304 km | 3,892.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EZY52GC | easyJet | Montpellier-Mediterranee Airport (LFMT) | Manchester Airport (EGCC) | 2026-07-31 10:13 UTC | 2026-07-31 11:56 UTC | 1h 42m |
| LVJUQ | LVJ | Larnaca International Airport (LCLK) | RAF Akrotiri (LCRA) | 2026-07-31 11:19 UTC | 2026-07-31 11:45 UTC | 26m |
| CCDNS | CCD | Larnaca International Airport (LCLK) | RAF Akrotiri (LCRA) | 2026-07-31 11:18 UTC | 2026-07-31 11:44 UTC | 26m |
| N710FM |  | Jack W Watson Airport (0IL9) | Gord Airport (0LL6) | 2026-07-31 11:27 UTC | 2026-07-31 11:39 UTC | 11m |
| CXK139 | CXK | Greenville Downtown Airport (KGMU) | Greenville Downtown Airport (KGMU) | 2026-07-31 11:38 UTC | 2026-07-31 11:38 UTC | 0m |
| IMX401 | IMX | Ostend-Bruges International Airport (EBOS) | Nice-Cote d'Azur Airport (LFMN) | 2026-07-31 09:19 UTC | 2026-07-31 11:31 UTC | 2h 12m |
|  |  | Gilze Rijen Air Base (EHGR) | Gilze Rijen Air Base (EHGR) | 2026-07-31 11:23 UTC | 2026-07-31 11:23 UTC | 0m |
| N479LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-31 10:16 UTC | 2026-07-31 11:22 UTC | 1h 5m |
| N3700K |  | Village Airport (0TN2) | Mc Ghee Tyson Airport (KTYS) | 2026-07-31 11:15 UTC | 2026-07-31 11:22 UTC | 7m |
| H2UPB |  | Larnaca International Airport (LCLK) | Larnaca International Airport (LCLK) | 2026-07-31 11:04 UTC | 2026-07-31 11:18 UTC | 14m |
| VOE4UW | VOE | Toulouse-Blagnac Airport (LFBO) | Figari Sud-Corse Airport (LFKF) | 2026-07-31 10:14 UTC | 2026-07-31 11:16 UTC | 1h 1m |
| DEZHA | DEZ | Westerland Sylt Airport (EDXW) | Hamburg Airport (EDDH) | 2026-07-31 10:29 UTC | 2026-07-31 11:15 UTC | 45m |
| FDR967 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-07-31 10:41 UTC | 2026-07-31 11:12 UTC | 31m |
| EAI55SK | EAI | Edinburgh Airport (EGPH) | Dublin Airport (EIDW) | 2026-07-31 10:12 UTC | 2026-07-31 11:11 UTC | 59m |
| HK4854 |  | Enrique Olaya Herrera Airport (SKMD) | Amalfi Airport (SKAM) | 2026-07-31 11:00 UTC | 2026-07-31 11:11 UTC | 11m |
|  |  | DCAE Cosford Airport (EGWC) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-07-31 10:43 UTC | 2026-07-31 11:11 UTC | 27m |
| LVJUQ | LVJ | RAF Akrotiri (LCRA) | Larnaca International Airport (LCLK) | 2026-07-31 10:42 UTC | 2026-07-31 11:08 UTC | 25m |
| CCDNS | CCD | RAF Akrotiri (LCRA) | Larnaca International Airport (LCLK) | 2026-07-31 10:42 UTC | 2026-07-31 11:08 UTC | 25m |
| LAS1 | LAS | Zurich Airport (LSZH) | Dubendorf Airport (LSMD) | 2026-07-31 11:00 UTC | 2026-07-31 11:06 UTC | 6m |
| JES3150 | JES | Ministro Pistarini International Airport (SAEZ) | Dionisio Cerqueira Airport (SSDC) | 2026-07-31 09:37 UTC | 2026-07-31 11:06 UTC | 1h 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
