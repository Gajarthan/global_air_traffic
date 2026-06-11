# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_06:05:26_UTC-green)

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

**Latest saved flight:** 2026-06-11 06:05:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-11 06:05:26 UTC

- **107,811** saved flights
- **37,765** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **107,811** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,318,027.3 tonnes** estimated CO2 emissions
- **76,407,381 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4438 |
| 2 | SkyWest Airlines | 4046 |
| 3 | IndiGo | 2137 |
| 4 | EJA | 2080 |
| 5 | American Airlines | 1715 |
| 6 | Southwest Airlines | 1621 |
| 7 | ENY | 1347 |
| 8 | Delta Air Lines | 1279 |
| 9 | Lufthansa | 1230 |
| 10 | Vueling | 986 |
| 11 | LATAM Airlines | 957 |
| 12 | WIF | 946 |
| 13 | AXM | 915 |
| 14 | AZU | 877 |
| 15 | LXJ | 813 |
| 16 | Swiss International | 784 |
| 17 | All Nippon Airways | 749 |
| 18 | Alaska Airlines | 740 |
| 19 | QLK | 717 |
| 20 | easyJet | 696 |
| 21 | EJU | 686 |
| 22 | Cathay Pacific | 648 |
| 23 | AEE | 615 |
| 24 | VIV | 614 |
| 25 | Air France | 608 |
| 26 | United Airlines | 594 |
| 27 | MXY | 580 |
| 28 | CXK | 569 |
| 29 | AXB | 531 |
| 30 | Japan Airlines | 531 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 90723 |
| 2 | 🇪🇸 ES | 7391 |
| 3 | 🇮🇳 IN | 6733 |
| 4 | 🇦🇺 AU | 6465 |
| 5 | 🇧🇷 BR | 5939 |
| 6 | 🇩🇪 DE | 5784 |
| 7 | 🇮🇹 IT | 5771 |
| 8 | 🇨🇦 CA | 5652 |
| 9 | 🇯🇵 JP | 4908 |
| 10 | 🇬🇧 GB | 4578 |
| 11 | 🇫🇷 FR | 4282 |
| 12 | 🇨🇴 CO | 3734 |
| 13 | 🇲🇽 MX | 3224 |
| 14 | 🇬🇷 GR | 3059 |
| 15 | 🇳🇴 NO | 2979 |
| 16 | 🇨🇭 CH | 2741 |
| 17 | 🇲🇾 MY | 2347 |
| 18 | 🇹🇷 TR | 2095 |
| 19 | 🇿🇦 ZA | 1845 |
| 20 | 🇳🇿 NZ | 1792 |
| 21 | 🇰🇷 KR | 1790 |
| 22 | 🇹🇭 TH | 1772 |
| 23 | 🇵🇱 PL | 1760 |
| 24 | 🇵🇭 PH | 1578 |
| 25 | 🇬🇹 GT | 1550 |
| 26 | 🇲🇦 MA | 1190 |
| 27 | 🇲🇴 MO | 1132 |
| 28 | 🇳🇱 NL | 1057 |
| 29 | 🇲🇪 ME | 1040 |
| 30 | 🇭🇷 HR | 940 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2328 |
| 2 | Denver International Airport |  | US | 1829 |
| 3 | Tokyo International Airport |  | JP | 1627 |
| 4 | Indira Gandhi International Airport |  | IN | 1464 |
| 5 | Harry Reid International Airport |  | US | 1374 |
| 6 | Guaymaral Airport |  | CO | 1373 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1351 |
| 8 | Zurich Airport |  | CH | 1222 |
| 9 | Frankfurt am Main International Airport |  | DE | 1213 |
| 10 | La Aurora Airport |  | GT | 1192 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1161 |
| 12 | El Dorado International Airport |  | CO | 1132 |
| 13 | Macau International Airport |  | MO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1081 |
| 15 | Chicago O'Hare International Airport |  | US | 1075 |
| 16 | Madrid Barajas International Airport |  | ES | 938 |
| 17 | Capua Airport |  | IT | 924 |
| 18 | Kuala Lumpur International Airport |  | MY | 920 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 918 |
| 20 | Salt Lake City International Airport |  | US | 915 |
| 21 | Charlotte/Douglas International Airport |  | US | 833 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 823 |
| 23 | Congonhas Airport |  | BR | 822 |
| 24 | Charles de Gaulle International Airport |  | FR | 813 |
| 25 | Bengaluru International Airport |  | IN | 813 |
| 26 | Malpensa International Airport |  | IT | 798 |
| 27 | Daniel K Inouye International Airport |  | US | 728 |
| 28 | Ninoy Aquino International Airport |  | PH | 724 |
| 29 | Tenerife Norte Airport |  | ES | 721 |
| 30 | Barcelona International Airport |  | ES | 704 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 700 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 698 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 698 |
| 34 | Amsterdam Airport Schiphol |  | NL | 653 |
| 35 | Don Mueang International Airport |  | TH | 648 |
| 36 | Vitoria/Foronda Airport |  | ES | 643 |
| 37 | Calgary International Airport |  | CA | 636 |
| 38 | Seattle-Tacoma International Airport |  | US | 621 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 619 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 610 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 568 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 396 | 21m | 244 km | 1,667.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 288 | 24m | 225 km | 1,117.3 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 279 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 262 | 1h 25m | 910 km | 4,111.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 249 | 1h 10m | 770 km | 3,307.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 216 | 26m | 275 km | 1,023.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 158 | 22m | 55 km | 150.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 157 | 27m | 215 km | 581.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 151 | 14m | 154 km | 400.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 149 | 27m | 152 km | 389.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 148 | 13m | - | - |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 131 | 1h 1m | 695 km | 1,570.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 129 | 44m | 241 km | 535.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 122 | 1h 18m | 961 km | 2,022.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ANA28 | All Nippon Airways | Osaka International Airport (RJOO) | Tokyo International Airport (RJTT) | 2026-06-11 05:16 UTC | 2026-06-11 06:05 UTC | 49m |
| N911TG |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Peter O Knight Airport (KTPF) | 2026-06-11 05:25 UTC | 2026-06-11 05:46 UTC | 20m |
| EXV | EXV | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-11 05:27 UTC | 2026-06-11 05:40 UTC | 12m |
| DEHMF | DEH | Mannheim-City Airport (EDFM) | Oberschleisheim Airfield (EDNX) | 2026-06-11 04:32 UTC | 2026-06-11 05:35 UTC | 1h 3m |
| GFA012 | Gulf Air | Bahrain International Airport (OBBI) | Chkalovskiy Airport (UUMU) | 2026-06-10 23:18 UTC | 2026-06-11 05:35 UTC | 6h 16m |
| AAL1271 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-11 03:27 UTC | 2026-06-11 05:33 UTC | 2h 5m |
| LLR873 | LLR | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-06-11 04:57 UTC | 2026-06-11 05:31 UTC | 34m |
| N340EA |  | K00V (K00V) | Cuchara Ranch Airport (CD48) | 2026-06-11 04:36 UTC | 2026-06-11 05:29 UTC | 52m |
| EWG72D | EWG | Salzburg Airport (LOWS) | Hamburg Airport (EDDH) | 2026-06-11 04:22 UTC | 2026-06-11 05:27 UTC | 1h 4m |
| AAO57 | AAO | Václav Havel Airport (LKPR) | Berlin Brandenburg Airport (EDDB) | 2026-06-11 04:41 UTC | 2026-06-11 05:22 UTC | 41m |
| JST516 | JST | Melbourne International Airport (YMML) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-11 04:09 UTC | 2026-06-11 05:21 UTC | 1h 11m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-06-11 04:38 UTC | 2026-06-11 05:20 UTC | 41m |
| SWR12K | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-06-11 04:21 UTC | 2026-06-11 05:17 UTC | 56m |
| OAL048 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiros Airport (LGSY) | 2026-06-11 04:50 UTC | 2026-06-11 05:14 UTC | 24m |
| AIQ3209 | AIQ | Don Mueang International Airport (VTBD) | VLXL (VLXL) | 2026-06-11 04:21 UTC | 2026-06-11 05:12 UTC | 50m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-06-11 04:42 UTC | 2026-06-11 05:10 UTC | 28m |
| AE921 |  | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-06-11 04:45 UTC | 2026-06-11 05:08 UTC | 23m |
| SNJ15 | SNJ | Tokyo International Airport (RJTT) | Oita Airport (RJFO) | 2026-06-11 03:54 UTC | 2026-06-11 05:05 UTC | 1h 11m |
| DAG | DAG | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-06-11 04:20 UTC | 2026-06-11 05:05 UTC | 45m |
| O794SC |  | San Bernardino International Airport (KSBD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-11 04:06 UTC | 2026-06-11 05:03 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
