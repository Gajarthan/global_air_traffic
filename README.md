# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_04:50:36_UTC-green)

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

**Latest saved flight:** 2026-09-05 04:50:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 04:50:36 UTC

- **247,997** saved flights
- **74,728** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **247,997** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,982,772.3 tonnes** estimated CO2 emissions
- **172,914,338 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9932 |
| 2 | SkyWest Airlines | 8670 |
| 3 | EJA | 4792 |
| 4 | IndiGo | 4140 |
| 5 | American Airlines | 3975 |
| 6 | Southwest Airlines | 3694 |
| 7 | Delta Air Lines | 3151 |
| 8 | ENY | 2966 |
| 9 | LATAM Airlines | 2392 |
| 10 | AZU | 2311 |
| 11 | Vueling | 2117 |
| 12 | WIF | 1983 |
| 13 | Lufthansa | 1970 |
| 14 | LXJ | 1927 |
| 15 | easyJet | 1714 |
| 16 | Swiss International | 1662 |
| 17 | AXM | 1622 |
| 18 | EJU | 1591 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1558 |
| 21 | Alaska Airlines | 1482 |
| 22 | All Nippon Airways | 1453 |
| 23 | WMT | 1399 |
| 24 | GLO | 1382 |
| 25 | VIV | 1365 |
| 26 | PGT | 1357 |
| 27 | Air France | 1352 |
| 28 | Wizz Air | 1337 |
| 29 | JetBlue | 1222 |
| 30 | AEE | 1218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 205835 |
| 2 | 🇪🇸 ES | 15869 |
| 3 | 🇧🇷 BR | 14503 |
| 4 | 🇦🇺 AU | 14103 |
| 5 | 🇨🇦 CA | 13792 |
| 6 | 🇮🇹 IT | 13568 |
| 7 | 🇮🇳 IN | 12909 |
| 8 | 🇩🇪 DE | 12178 |
| 9 | 🇬🇧 GB | 11642 |
| 10 | 🇨🇴 CO | 10820 |
| 11 | 🇫🇷 FR | 9978 |
| 12 | 🇯🇵 JP | 9800 |
| 13 | 🇹🇷 TR | 7376 |
| 14 | 🇬🇷 GR | 7291 |
| 15 | 🇲🇽 MX | 6866 |
| 16 | 🇨🇭 CH | 6671 |
| 17 | 🇳🇴 NO | 6147 |
| 18 | 🇹🇭 TH | 4475 |
| 19 | 🇲🇾 MY | 4351 |
| 20 | 🇿🇦 ZA | 4281 |
| 21 | 🇵🇱 PL | 4146 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3377 |
| 24 | 🇬🇹 GT | 3100 |
| 25 | 🇰🇷 KR | 2885 |
| 26 | 🇭🇷 HR | 2845 |
| 27 | 🇲🇦 MA | 2505 |
| 28 | 🇲🇪 ME | 2313 |
| 29 | 🇳🇱 NL | 2234 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5108 |
| 2 | Denver International Airport |  | US | 4008 |
| 3 | Indira Gandhi International Airport |  | IN | 3018 |
| 4 | Tokyo International Airport |  | JP | 2923 |
| 5 | Guaymaral Airport |  | CO | 2723 |
| 6 | Harry Reid International Airport |  | US | 2649 |
| 7 | Zurich Airport |  | CH | 2592 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2523 |
| 9 | El Dorado International Airport |  | CO | 2477 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2461 |
| 11 | La Aurora Airport |  | GT | 2359 |
| 12 | Salt Lake City International Airport |  | US | 2199 |
| 13 | Chicago O'Hare International Airport |  | US | 2175 |
| 14 | Congonhas Airport |  | BR | 2129 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2045 |
| 16 | Capua Airport |  | IT | 1949 |
| 17 | Madrid Barajas International Airport |  | ES | 1944 |
| 18 | Frankfurt am Main International Airport |  | DE | 1941 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1863 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1812 |
| 21 | Malpensa International Airport |  | IT | 1777 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 23 | Charles de Gaulle International Airport |  | FR | 1739 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1645 |
| 26 | Macau International Airport |  | MO | 1634 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1625 |
| 28 | Charlotte/Douglas International Airport |  | US | 1573 |
| 29 | Kuala Lumpur International Airport |  | MY | 1568 |
| 30 | Barcelona International Airport |  | ES | 1567 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1521 |
| 32 | Viracopos International Airport |  | BR | 1481 |
| 33 | Seattle-Tacoma International Airport |  | US | 1461 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1446 |
| 35 | Don Mueang International Airport |  | TH | 1438 |
| 36 | Calgary International Airport |  | CA | 1430 |
| 37 | Bengaluru International Airport |  | IN | 1426 |
| 38 | Oslo Gardermoen Airport |  | NO | 1395 |
| 39 | Vancouver International Airport |  | CA | 1388 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1346 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 921 | 21m | 244 km | 3,878.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 653 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 621 | 1h 6m | 770 km | 8,249.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 554 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 408 | 27m | 275 km | 1,933.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 395 | 1h 50m | 1,423 km | 9,693.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 385 | 44m | 555 km | 3,686.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 368 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 367 | 44m | 241 km | 1,524.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 346 | 24m | 218 km | 1,303.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 286 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 283 | 19m | 144 km | 703.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 255 | 28m | 152 km | 666.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N978TS |  | Hammond Northshore Regional Airport (KHDC) | Auburn University Regional Airport (KAUO) | 2026-09-05 03:38 UTC | 2026-09-05 04:50 UTC | 1h 11m |
| UAL2384 | United Airlines | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | San Francisco International Airport (KSFO) | 2026-09-04 22:58 UTC | 2026-09-05 04:42 UTC | 5h 44m |
| N119UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-05 03:39 UTC | 2026-09-05 04:39 UTC | 59m |
| ANZ623 | ANZ | Auckland International Airport (NZAA) | Glenorchy Airport (NZGY) | 2026-09-05 03:06 UTC | 2026-09-05 04:36 UTC | 1h 30m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-09-05 04:18 UTC | 2026-09-05 04:36 UTC | 17m |
| LS68 |  | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-05 04:06 UTC | 2026-09-05 04:32 UTC | 25m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-09-05 03:45 UTC | 2026-09-05 04:28 UTC | 43m |
| AXM6304 | AXM | Kuala Lumpur International Airport (WMKK) | Penang International Airport (WMKP) | 2026-09-05 04:01 UTC | 2026-09-05 04:28 UTC | 26m |
| N660LF |  | Renton Municipal Airport (KRNT) | Mineral County Airport (K9S4) | 2026-09-05 03:13 UTC | 2026-09-05 04:27 UTC | 1h 14m |
| N2112K |  | Erie Municipal Airport (KEIK) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-09-05 02:40 UTC | 2026-09-05 04:27 UTC | 1h 47m |
| N450GG |  | Spring Creek Field (79TX) | Afton Lincoln County/General Boyd L Eddins Field (KAFO) | 2026-09-05 01:51 UTC | 2026-09-05 04:23 UTC | 2h 31m |
| VUBCF | VUB | Agra Airport (VIAG) | Bareilly Air Force Station (VIBY) | 2026-09-05 03:56 UTC | 2026-09-05 04:22 UTC | 25m |
| FDA353 | FDA | Nagoya Airport (RJNA) | Yamagata Airport (RJSC) | 2026-09-05 03:43 UTC | 2026-09-05 04:21 UTC | 37m |
| THY70A | Turkish Airlines | Istanbul Airport (LTFM) | Zafer Airport (LTBZ) | 2026-09-05 03:57 UTC | 2026-09-05 04:21 UTC | 23m |
| VOZ1117 | Virgin Australia | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-09-05 03:14 UTC | 2026-09-05 04:20 UTC | 1h 5m |
| N2863E |  | Boise Air Trml/Gowen Field (KBOI) | Bald Mountain Airport (OG45) | 2026-09-05 03:30 UTC | 2026-09-05 04:19 UTC | 49m |
| FD626J |  | Perth Jandakot Airport (YPJT) | Turkey Creek Airport (YTKY) | 2026-09-05 01:34 UTC | 2026-09-05 04:14 UTC | 2h 40m |
| IGO531P | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-09-05 03:30 UTC | 2026-09-05 04:14 UTC | 44m |
| AIQ3212 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-09-05 03:31 UTC | 2026-09-05 04:14 UTC | 42m |
|  |  | Pinto Martins International Airport (SBFZ) | SWBE (SWBE) | 2026-09-05 03:48 UTC | 2026-09-05 04:12 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
