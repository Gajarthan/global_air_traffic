# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_07:16:22_UTC-green)

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

**Latest saved flight:** 2026-08-23 07:16:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 07:16:22 UTC

- **227,802** saved flights
- **70,592** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,802** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,746,147.8 tonnes** estimated CO2 emissions
- **159,196,973 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9136 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3853 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1926 |
| 12 | Lufthansa | 1862 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1516 |
| 17 | AXM | 1506 |
| 18 | QLK | 1444 |
| 19 | United Airlines | 1444 |
| 20 | EJU | 1438 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1367 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | Air France | 1235 |
| 27 | WMT | 1231 |
| 28 | Wizz Air | 1181 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1132 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190640 |
| 2 | 🇪🇸 ES | 14583 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12917 |
| 5 | 🇨🇦 CA | 12614 |
| 6 | 🇮🇹 IT | 12239 |
| 7 | 🇮🇳 IN | 11997 |
| 8 | 🇩🇪 DE | 11196 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9267 |
| 12 | 🇫🇷 FR | 9102 |
| 13 | 🇹🇷 TR | 6690 |
| 14 | 🇬🇷 GR | 6666 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6002 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 4023 |
| 19 | 🇹🇭 TH | 3931 |
| 20 | 🇿🇦 ZA | 3927 |
| 21 | 🇵🇱 PL | 3783 |
| 22 | 🇳🇿 NZ | 3165 |
| 23 | 🇵🇭 PH | 3115 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2698 |
| 26 | 🇭🇷 HR | 2575 |
| 27 | 🇲🇦 MA | 2297 |
| 28 | 🇲🇪 ME | 2057 |
| 29 | 🇳🇱 NL | 2028 |
| 30 | 🇮🇩 ID | 1970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Tokyo International Airport |  | JP | 2771 |
| 4 | Indira Gandhi International Airport |  | IN | 2768 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2365 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2298 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1937 |
| 16 | Frankfurt am Main International Airport |  | DE | 1825 |
| 17 | Madrid Barajas International Airport |  | ES | 1774 |
| 18 | Capua Airport |  | IT | 1769 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1617 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1606 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1492 |
| 27 | Ninoy Aquino International Airport |  | PH | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1459 |
| 29 | Barcelona International Airport |  | ES | 1414 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Bengaluru International Airport |  | IN | 1349 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1287 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 571 | 1h 6m | 770 km | 7,585.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 563 | 24m | 225 km | 2,184.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 346 | 1h 50m | 1,423 km | 8,491.4 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 308 | 21m | 250 km | 1,330.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 299 | 44m | 555 km | 2,863.1 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 292 | 1h 38m | 1,156 km | 5,825.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 289 | 24m | 218 km | 1,088.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 238 | 15m | 154 km | 630.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XCN70 | XCN | Wilson Creek Airport (K5W1) | Fowler Field (02WN) | 2026-08-23 06:37 UTC | 2026-08-23 07:16 UTC | 38m |
| QLK575D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-08-23 06:42 UTC | 2026-08-23 07:12 UTC | 30m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-23 05:59 UTC | 2026-08-23 06:51 UTC | 51m |
| RMB1 | RMB | Ibiza Airport (LEIB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 05:53 UTC | 2026-08-23 06:50 UTC | 57m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-08-23 05:39 UTC | 2026-08-23 06:47 UTC | 1h 7m |
| JTE742 | JTE | Adelaide International Airport (YPAD) | Mount Gunson Airport (YMGN) | 2026-08-23 06:00 UTC | 2026-08-23 06:45 UTC | 45m |
| N555DF |  | Ben Gurion International Airport (LLBG) | Mikonos Airport (LGMK) | 2026-08-23 05:17 UTC | 2026-08-23 06:43 UTC | 1h 26m |
| BEL6JW | Brussels Airlines | Brussels Airport (EBBR) | Ibiza Airport (LEIB) | 2026-08-23 04:40 UTC | 2026-08-23 06:42 UTC | 2h 2m |
| HLC238 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-08-23 06:06 UTC | 2026-08-23 06:42 UTC | 35m |
| ANE82BX | ANE | Madrid Barajas International Airport (LEMD) | Bilbao Airport (LEBB) | 2026-08-23 06:09 UTC | 2026-08-23 06:40 UTC | 30m |
| EWG59H | EWG | Dusseldorf International Airport (EDDL) | Ibiza Airport (LEIB) | 2026-08-23 04:21 UTC | 2026-08-23 06:38 UTC | 2h 16m |
| FGAHV | FGA | Chambery-Challes-les-Eaux Airport (LFLE) | Albertville Airport (LFKA) | 2026-08-23 06:26 UTC | 2026-08-23 06:37 UTC | 10m |
| RYR325 | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Paphos International Airport (LCPH) | 2026-08-23 05:28 UTC | 2026-08-23 06:36 UTC | 1h 7m |
| BTI3TP | BTI | Vilnius International Airport (EYVI) | Dusseldorf International Airport (EDDL) | 2026-08-23 04:35 UTC | 2026-08-23 06:32 UTC | 1h 57m |
| TVF40JP | TVF | Perouges - Meximieux Airport (LFHC) | Santorini Airport (LGSR) | 2026-08-23 04:09 UTC | 2026-08-23 06:31 UTC | 2h 22m |
| TRA6259 | TRA | Rotterdam Airport (EHRD) | Sinj Glider Airport (LDSS) | 2026-08-23 05:00 UTC | 2026-08-23 06:30 UTC | 1h 29m |
| AUA887R | Austrian Airlines | Vienna International Airport (LOWW) | Karain Airport (LTXE) | 2026-08-23 04:18 UTC | 2026-08-23 06:29 UTC | 2h 10m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Khowai Airport (VEKW) | 2026-08-23 04:24 UTC | 2026-08-23 06:27 UTC | 2h 3m |
| RYR1ST | Ryanair | Brussels South Charleroi Airport (EBCI) | Bilbao Airport (LEBB) | 2026-08-23 04:56 UTC | 2026-08-23 06:26 UTC | 1h 30m |
| N302TP |  | 84OL (84OL) | Tulsa International Airport (KTUL) | 2026-08-23 05:57 UTC | 2026-08-23 06:24 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
