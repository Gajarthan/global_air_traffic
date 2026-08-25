# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_09:05:39_UTC-green)

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

**Latest saved flight:** 2026-08-25 09:05:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 09:05:39 UTC

- **234,556** saved flights
- **71,868** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,556** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,825,738.0 tonnes** estimated CO2 emissions
- **163,810,897 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9402 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3964 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2253 |
| 10 | AZU | 2184 |
| 11 | Vueling | 2007 |
| 12 | Lufthansa | 1906 |
| 13 | WIF | 1863 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1633 |
| 16 | Swiss International | 1570 |
| 17 | AXM | 1569 |
| 18 | EJU | 1499 |
| 19 | QLK | 1496 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1397 |
| 23 | GLO | 1306 |
| 24 | WMT | 1301 |
| 25 | VIV | 1294 |
| 26 | PGT | 1279 |
| 27 | Air France | 1271 |
| 28 | Wizz Air | 1241 |
| 29 | AEE | 1165 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195102 |
| 2 | 🇪🇸 ES | 15064 |
| 3 | 🇧🇷 BR | 13686 |
| 4 | 🇦🇺 AU | 13312 |
| 5 | 🇨🇦 CA | 12980 |
| 6 | 🇮🇹 IT | 12739 |
| 7 | 🇮🇳 IN | 12342 |
| 8 | 🇩🇪 DE | 11549 |
| 9 | 🇬🇧 GB | 11029 |
| 10 | 🇨🇴 CO | 9854 |
| 11 | 🇯🇵 JP | 9518 |
| 12 | 🇫🇷 FR | 9375 |
| 13 | 🇹🇷 TR | 6947 |
| 14 | 🇬🇷 GR | 6896 |
| 15 | 🇲🇽 MX | 6527 |
| 16 | 🇨🇭 CH | 6249 |
| 17 | 🇳🇴 NO | 5787 |
| 18 | 🇲🇾 MY | 4195 |
| 19 | 🇹🇭 TH | 4173 |
| 20 | 🇿🇦 ZA | 4091 |
| 21 | 🇵🇱 PL | 3910 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3230 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2747 |
| 26 | 🇭🇷 HR | 2691 |
| 27 | 🇲🇦 MA | 2378 |
| 28 | 🇲🇪 ME | 2165 |
| 29 | 🇳🇱 NL | 2100 |
| 30 | 🇮🇩 ID | 2051 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2858 |
| 4 | Tokyo International Airport |  | JP | 2832 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2517 |
| 7 | Zurich Airport |  | CH | 2450 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2348 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2197 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1868 |
| 17 | Capua Airport |  | IT | 1847 |
| 18 | Madrid Barajas International Airport |  | ES | 1844 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1765 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1678 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1627 |
| 25 | Macau International Airport |  | MO | 1607 |
| 26 | Ninoy Aquino International Airport |  | PH | 1559 |
| 27 | Kuala Lumpur International Airport |  | MY | 1518 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1480 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Seattle-Tacoma International Airport |  | US | 1378 |
| 34 | Bengaluru International Airport |  | IN | 1378 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1358 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1310 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | O. R. Tambo International Airport |  | ZA | 1271 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 594 | 24m | 225 km | 2,304.4 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 593 | 1h 6m | 770 km | 7,877.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 386 | 27m | 275 km | 1,829.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 362 | 1h 50m | 1,423 km | 8,884.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 339 | 44m | 555 km | 3,246.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 328 | 21m | 250 km | 1,416.8 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 312 | 24m | 218 km | 1,175.4 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 307 | 1h 40m | 1,156 km | 6,124.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 287 | 27m | 215 km | 1,062.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 259 | 15m | 154 km | 686.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HGB341 | HGB | Kansai International Airport (RJBB) | Chek Lap Kok International Airport (VHHH) | 2026-08-25 05:45 UTC | 2026-08-25 09:05 UTC | 3h 20m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-25 08:46 UTC | 2026-08-25 09:04 UTC | 17m |
| GCICC | GCI | Denham Aerodrome (EGLD) | Denham Aerodrome (EGLD) | 2026-08-25 08:46 UTC | 2026-08-25 08:56 UTC | 10m |
| SYERTN4 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-08-25 08:50 UTC | 2026-08-25 08:54 UTC | 3m |
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-25 08:39 UTC | 2026-08-25 08:52 UTC | 12m |
| AWH91C | AWH | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-08-25 08:06 UTC | 2026-08-25 08:46 UTC | 40m |
| LXC60 | LXC | Lapalisse - Perigny Airport (LFHX) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-25 07:21 UTC | 2026-08-25 08:46 UTC | 1h 24m |
| OKCZE | OKC | Kunovice Airport (LKKU) | Kunovice Airport (LKKU) | 2026-08-25 08:21 UTC | 2026-08-25 08:45 UTC | 23m |
| MABSU | MAB | London Stansted Airport (EGSS) | Newquay Cornwall Airport (EGHQ) | 2026-08-25 07:21 UTC | 2026-08-25 08:36 UTC | 1h 15m |
| EIN26M | Aer Lingus | Birmingham International Airport (EGBB) | Dublin Airport (EIDW) | 2026-08-25 07:32 UTC | 2026-08-25 08:33 UTC | 1h 0m |
| FHNHD | FHN | Tours-Val-de-Loire Airport (LFOT) | Blois-Le Breuil Airport (LFOQ) | 2026-08-25 06:36 UTC | 2026-08-25 08:31 UTC | 1h 54m |
| RYS7051 | RYS | Katowice International Airport (EPKT) | Araxos Airport (LGRX) | 2026-08-25 06:31 UTC | 2026-08-25 08:31 UTC | 1h 59m |
| N660LF |  | Renton Municipal Airport (KRNT) | Christensen Field (8WA6) | 2026-08-25 07:58 UTC | 2026-08-25 08:30 UTC | 32m |
| EFC65F | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-08-25 07:24 UTC | 2026-08-25 08:24 UTC | 59m |
| IBIS2 | IBI | Frankfurt-Egelsbach Airport (EDFE) | Lauterbach Airport (EDFT) | 2026-08-25 07:27 UTC | 2026-08-25 08:22 UTC | 55m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-08-25 05:59 UTC | 2026-08-25 08:21 UTC | 2h 21m |
| AIC3RK | Air India | Indira Gandhi International Airport (VIDP) | Shimla Airport (VISM) | 2026-08-25 07:48 UTC | 2026-08-25 08:17 UTC | 29m |
| 5YCPL |  | Nairobi Wilson Airport (HKNW) | Naivasha Airport (HKNV) | 2026-08-25 07:59 UTC | 2026-08-25 08:16 UTC | 17m |
| SFJ83 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-25 07:10 UTC | 2026-08-25 08:12 UTC | 1h 2m |
| RGA06 | RGA | Locarno Airport (LSZL) | Muenster Aero Airport (LSPU) | 2026-08-25 08:01 UTC | 2026-08-25 08:11 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
