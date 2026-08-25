# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_22:21:05_UTC-green)

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

**Latest saved flight:** 2026-08-25 22:21:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 22:21:05 UTC

- **236,870** saved flights
- **72,285** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,870** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,852,696.1 tonnes** estimated CO2 emissions
- **165,373,686 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9499 |
| 2 | SkyWest Airlines | 8380 |
| 3 | EJA | 4605 |
| 4 | IndiGo | 3986 |
| 5 | American Airlines | 3850 |
| 6 | Southwest Airlines | 3611 |
| 7 | Delta Air Lines | 3020 |
| 8 | ENY | 2875 |
| 9 | LATAM Airlines | 2273 |
| 10 | AZU | 2211 |
| 11 | Vueling | 2028 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1881 |
| 14 | LXJ | 1850 |
| 15 | easyJet | 1656 |
| 16 | Swiss International | 1588 |
| 17 | AXM | 1576 |
| 18 | EJU | 1520 |
| 19 | QLK | 1502 |
| 20 | United Airlines | 1501 |
| 21 | Alaska Airlines | 1423 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1324 |
| 24 | GLO | 1323 |
| 25 | VIV | 1308 |
| 26 | PGT | 1291 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1268 |
| 29 | JetBlue | 1178 |
| 30 | AEE | 1175 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196902 |
| 2 | 🇪🇸 ES | 15214 |
| 3 | 🇧🇷 BR | 13843 |
| 4 | 🇦🇺 AU | 13356 |
| 5 | 🇨🇦 CA | 13115 |
| 6 | 🇮🇹 IT | 12929 |
| 7 | 🇮🇳 IN | 12420 |
| 8 | 🇩🇪 DE | 11661 |
| 9 | 🇬🇧 GB | 11175 |
| 10 | 🇨🇴 CO | 10072 |
| 11 | 🇯🇵 JP | 9546 |
| 12 | 🇫🇷 FR | 9503 |
| 13 | 🇹🇷 TR | 7032 |
| 14 | 🇬🇷 GR | 6978 |
| 15 | 🇲🇽 MX | 6584 |
| 16 | 🇨🇭 CH | 6322 |
| 17 | 🇳🇴 NO | 5862 |
| 18 | 🇲🇾 MY | 4225 |
| 19 | 🇹🇭 TH | 4219 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3944 |
| 22 | 🇳🇿 NZ | 3259 |
| 23 | 🇵🇭 PH | 3243 |
| 24 | 🇬🇹 GT | 2972 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2733 |
| 27 | 🇲🇦 MA | 2395 |
| 28 | 🇲🇪 ME | 2203 |
| 29 | 🇳🇱 NL | 2125 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4922 |
| 2 | Denver International Airport |  | US | 3845 |
| 3 | Indira Gandhi International Airport |  | IN | 2884 |
| 4 | Tokyo International Airport |  | JP | 2843 |
| 5 | Guaymaral Airport |  | CO | 2689 |
| 6 | Harry Reid International Airport |  | US | 2532 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2427 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2369 |
| 10 | La Aurora Airport |  | GT | 2266 |
| 11 | El Dorado International Airport |  | CO | 2259 |
| 12 | Chicago O'Hare International Airport |  | US | 2131 |
| 13 | Salt Lake City International Airport |  | US | 2090 |
| 14 | Congonhas Airport |  | BR | 2018 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1984 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1864 |
| 18 | Madrid Barajas International Airport |  | ES | 1860 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1785 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1748 |
| 21 | Malpensa International Airport |  | IT | 1698 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1679 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1650 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1568 |
| 27 | Charlotte/Douglas International Airport |  | US | 1527 |
| 28 | Kuala Lumpur International Airport |  | MY | 1526 |
| 29 | Barcelona International Airport |  | ES | 1499 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1489 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1437 |
| 32 | Viracopos International Airport |  | BR | 1415 |
| 33 | Seattle-Tacoma International Airport |  | US | 1389 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1388 |
| 35 | Bengaluru International Airport |  | IN | 1384 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1355 |
| 38 | Oslo Gardermoen Airport |  | NO | 1328 |
| 39 | Vancouver International Airport |  | CA | 1295 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1089 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 869 | 21m | 244 km | 3,659.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 603 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 532 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 391 | 27m | 275 km | 1,852.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 343 | 44m | 241 km | 1,424.8 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 318 | 24m | 218 km | 1,198.0 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 315 | 1h 40m | 1,156 km | 6,284.1 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 314 | 22m | 55 km | 298.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 295 | 19m | 99 km | 505.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 273 | 1h 14m | 961 km | 4,525.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 268 | 19m | 144 km | 666.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 254 | 1h 50m | 1,304 km | 5,714.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 247 | 28m | 152 km | 645.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N713PM |  | 5MS2 (5MS2) | 5MS2 (5MS2) | 2026-08-25 21:01 UTC | 2026-08-25 22:21 UTC | 1h 19m |
| N403AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-25 21:44 UTC | 2026-08-25 22:19 UTC | 35m |
| LOT7YE | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Tallinn Airport (EETN) | 2026-08-25 21:19 UTC | 2026-08-25 22:17 UTC | 58m |
| N125MG |  | Roberts Field/Redmond Municipal Airport (KRDM) | Dry Creek Airpark (OG21) | 2026-08-25 21:46 UTC | 2026-08-25 22:15 UTC | 28m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-08-25 11:14 UTC | 2026-08-25 22:13 UTC | 10h 59m |
| N813AM |  | Litchfield Municipal Airport (K3LF) | 1IL1 (1IL1) | 2026-08-25 21:54 UTC | 2026-08-25 22:11 UTC | 16m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-25 21:47 UTC | 2026-08-25 22:11 UTC | 23m |
| N350ZF |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-25 21:48 UTC | 2026-08-25 22:10 UTC | 22m |
| N893AP |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-08-25 21:28 UTC | 2026-08-25 22:08 UTC | 39m |
| N8192U |  | Monmouth Executive Airport (KBLM) | Monmouth Executive Airport (KBLM) | 2026-08-25 21:54 UTC | 2026-08-25 22:07 UTC | 13m |
| EVA003 | EVA Air | Washington Dulles International Airport (KIAD) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-25 06:12 UTC | 2026-08-25 22:07 UTC | 15h 55m |
| TRP7 | TRP | Robinson Airport (MD14) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-25 21:52 UTC | 2026-08-25 22:06 UTC | 13m |
| N80678 |  | Pearson Field (KVUO) | Independence State Airport (K7S5) | 2026-08-25 21:17 UTC | 2026-08-25 22:03 UTC | 45m |
| N407JH |  | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-25 16:20 UTC | 2026-08-25 22:02 UTC | 5h 42m |
| WMU84 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-08-25 21:55 UTC | 2026-08-25 22:02 UTC | 7m |
| BULET46 | BUL | Catalina Airport (KAVX) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-25 21:19 UTC | 2026-08-25 22:00 UTC | 41m |
| N54661 |  | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-08-25 21:13 UTC | 2026-08-25 21:58 UTC | 45m |
| N636EM |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-25 21:54 UTC | 2026-08-25 21:57 UTC | 2m |
| WMT2MK | WMT | Olbia / Costa Smeralda Airport (LIEO) | Malpensa International Airport (LIMC) | 2026-08-25 20:56 UTC | 2026-08-25 21:54 UTC | 57m |
| QLK571D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-25 21:22 UTC | 2026-08-25 21:54 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
