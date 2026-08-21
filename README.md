# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_05:26:04_UTC-green)

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

**Latest saved flight:** 2026-08-21 05:26:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 05:26:04 UTC

- **221,231** saved flights
- **69,351** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,231** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,662,495.8 tonnes** estimated CO2 emissions
- **154,347,580 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8848 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3745 |
| 5 | American Airlines | 3669 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2850 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2102 |
| 10 | AZU | 2031 |
| 11 | Vueling | 1858 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1764 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1530 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1455 |
| 18 | United Airlines | 1390 |
| 19 | QLK | 1389 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1350 |
| 22 | All Nippon Airways | 1326 |
| 23 | GLO | 1210 |
| 24 | VIV | 1206 |
| 25 | PGT | 1204 |
| 26 | Air France | 1197 |
| 27 | WMT | 1166 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1106 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186254 |
| 2 | 🇪🇸 ES | 14142 |
| 3 | 🇧🇷 BR | 12784 |
| 4 | 🇦🇺 AU | 12563 |
| 5 | 🇨🇦 CA | 12231 |
| 6 | 🇮🇹 IT | 11742 |
| 7 | 🇮🇳 IN | 11676 |
| 8 | 🇩🇪 DE | 10901 |
| 9 | 🇬🇧 GB | 10365 |
| 10 | 🇨🇴 CO | 9101 |
| 11 | 🇯🇵 JP | 8997 |
| 12 | 🇫🇷 FR | 8786 |
| 13 | 🇬🇷 GR | 6446 |
| 14 | 🇹🇷 TR | 6370 |
| 15 | 🇲🇽 MX | 6156 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5483 |
| 18 | 🇲🇾 MY | 3849 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇹🇭 TH | 3691 |
| 21 | 🇵🇱 PL | 3665 |
| 22 | 🇳🇿 NZ | 3083 |
| 23 | 🇵🇭 PH | 2993 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2641 |
| 26 | 🇭🇷 HR | 2447 |
| 27 | 🇲🇦 MA | 2220 |
| 28 | 🇳🇱 NL | 1962 |
| 29 | 🇲🇪 ME | 1950 |
| 30 | 🇮🇩 ID | 1888 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3614 |
| 3 | Tokyo International Airport |  | JP | 2701 |
| 4 | Indira Gandhi International Airport |  | IN | 2683 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2243 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2072 |
| 12 | Chicago O'Hare International Airport |  | US | 2024 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1685 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1629 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1561 |
| 24 | Malpensa International Airport |  | IT | 1548 |
| 25 | Charles de Gaulle International Airport |  | FR | 1519 |
| 26 | Charlotte/Douglas International Airport |  | US | 1470 |
| 27 | Ninoy Aquino International Airport |  | PH | 1425 |
| 28 | Kuala Lumpur International Airport |  | MY | 1409 |
| 29 | Barcelona International Airport |  | ES | 1356 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1345 |
| 31 | Bengaluru International Airport |  | IN | 1326 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1312 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1255 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 37 | Vitoria/Foronda Airport |  | ES | 1225 |
| 38 | Oslo Gardermoen Airport |  | NO | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1215 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1186 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 797 | 21m | 244 km | 3,355.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 548 | 1h 7m | 770 km | 7,279.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 532 | 24m | 225 km | 2,063.9 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 328 | 1h 50m | 1,423 km | 8,049.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 276 | 1h 38m | 1,156 km | 5,506.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 275 | 24m | 218 km | 1,036.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 24 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 258 | 44m | 555 km | 2,470.5 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N26WR |  | Santa Ynez/Kunkle Field (KIZA) | Santa Monica Municipal Airport (KSMO) | 2026-08-21 04:59 UTC | 2026-08-21 05:26 UTC | 26m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-20 15:06 UTC | 2026-08-21 05:24 UTC | 14h 18m |
| YTK | YTK | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-21 03:53 UTC | 2026-08-21 05:18 UTC | 1h 24m |
| G72234 |  | Rancho Blanco Airport (TE32) | Laredo International Airport (KLRD) | 2026-08-21 03:00 UTC | 2026-08-21 05:15 UTC | 2h 15m |
| CARGO38 | CAR | Dothan Regional Airport (KDHN) | Hidden Springs Airpark (36AL) | 2026-08-21 04:27 UTC | 2026-08-21 05:13 UTC | 45m |
| FIN311 | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-08-21 04:21 UTC | 2026-08-21 05:09 UTC | 47m |
| AMPED22 | AMP | Butts Army Air Field (Fort Carson) Airport (KFCS) | Butts Army Air Field (Fort Carson) Airport (KFCS) | 2026-08-21 03:55 UTC | 2026-08-21 05:08 UTC | 1h 12m |
| NSZ2602 | NSZ | Helsinki Vantaa Airport (EFHK) | Stockholm-Arlanda Airport (ESSA) | 2026-08-21 04:11 UTC | 2026-08-21 04:58 UTC | 47m |
| N862YB |  | Los Alamos Airport (KLAM) | NM74 (NM74) | 2026-08-21 04:18 UTC | 2026-08-21 04:57 UTC | 38m |
|  |  | Albury Airport (YMAY) | Albury Airport (YMAY) | 2026-08-21 04:56 UTC | 2026-08-21 04:56 UTC | 0m |
| AEE352 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-21 04:26 UTC | 2026-08-21 04:48 UTC | 22m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Kerikeri Airport (NZKK) | 2026-08-21 04:18 UTC | 2026-08-21 04:47 UTC | 28m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-21 04:08 UTC | 2026-08-21 04:45 UTC | 36m |
| OKCTP | OKC | Katowice International Airport (EPKT) | Belgrade Nikola Tesla Airport (LYBE) | 2026-08-21 03:42 UTC | 2026-08-21 04:44 UTC | 1h 1m |
| AZU4411 | AZU | Viracopos International Airport (SBKP) | Benedito Mutran Airport (SIBD) | 2026-08-20 16:21 UTC | 2026-08-21 04:40 UTC | 12h 19m |
| N227TW |  | Marana Regional Airport (KAVQ) | Glendale Regional Airport (KGEU) | 2026-08-21 03:36 UTC | 2026-08-21 04:40 UTC | 1h 4m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-08-21 04:18 UTC | 2026-08-21 04:35 UTC | 16m |
| WMT1VF | WMT | Timisoara Traian Vuia Airport (LRTR) | Memmingen Allgau Airport (EDJA) | 2026-08-21 03:11 UTC | 2026-08-21 04:33 UTC | 1h 22m |
| TCKIP | TCK | Milas Bodrum International Airport (LTFE) | Mikonos Airport (LGMK) | 2026-08-21 04:03 UTC | 2026-08-21 04:32 UTC | 29m |
| WIF7GT | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-08-21 04:15 UTC | 2026-08-21 04:32 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
