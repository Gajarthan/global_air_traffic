# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_16:32:19_UTC-green)

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

**Latest saved flight:** 2026-08-19 16:32:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 16:32:19 UTC

- **216,352** saved flights
- **68,327** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **216,352** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,602,886.4 tonnes** estimated CO2 emissions
- **150,891,967 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8651 |
| 2 | SkyWest Airlines | 7720 |
| 3 | EJA | 4197 |
| 4 | IndiGo | 3685 |
| 5 | American Airlines | 3603 |
| 6 | Southwest Airlines | 3438 |
| 7 | Delta Air Lines | 2796 |
| 8 | ENY | 2668 |
| 9 | LATAM Airlines | 2048 |
| 10 | AZU | 1974 |
| 11 | Vueling | 1820 |
| 12 | Lufthansa | 1810 |
| 13 | WIF | 1731 |
| 14 | LXJ | 1702 |
| 15 | easyJet | 1501 |
| 16 | Swiss International | 1445 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1367 |
| 19 | EJU | 1349 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1324 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1185 |
| 24 | PGT | 1175 |
| 25 | Air France | 1174 |
| 26 | GLO | 1172 |
| 27 | WMT | 1132 |
| 28 | JetBlue | 1102 |
| 29 | Wizz Air | 1100 |
| 30 | AEE | 1087 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 182224 |
| 2 | 🇪🇸 ES | 13894 |
| 3 | 🇧🇷 BR | 12447 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11906 |
| 6 | 🇮🇳 IN | 11478 |
| 7 | 🇮🇹 IT | 11475 |
| 8 | 🇩🇪 DE | 10733 |
| 9 | 🇬🇧 GB | 10163 |
| 10 | 🇯🇵 JP | 8870 |
| 11 | 🇨🇴 CO | 8839 |
| 12 | 🇫🇷 FR | 8645 |
| 13 | 🇬🇷 GR | 6332 |
| 14 | 🇹🇷 TR | 6218 |
| 15 | 🇲🇽 MX | 6040 |
| 16 | 🇨🇭 CH | 5757 |
| 17 | 🇳🇴 NO | 5383 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3679 |
| 20 | 🇵🇱 PL | 3583 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 2998 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2749 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2370 |
| 27 | 🇲🇦 MA | 2177 |
| 28 | 🇳🇱 NL | 1934 |
| 29 | 🇲🇪 ME | 1885 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4531 |
| 2 | Denver International Airport |  | US | 3518 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2622 |
| 5 | Guaymaral Airport |  | CO | 2581 |
| 6 | Harry Reid International Airport |  | US | 2402 |
| 7 | Zurich Airport |  | CH | 2251 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2218 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2209 |
| 10 | La Aurora Airport |  | GT | 2090 |
| 11 | El Dorado International Airport |  | CO | 2017 |
| 12 | Chicago O'Hare International Airport |  | US | 1985 |
| 13 | Salt Lake City International Airport |  | US | 1903 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1891 |
| 15 | Congonhas Airport |  | BR | 1815 |
| 16 | Frankfurt am Main International Airport |  | DE | 1771 |
| 17 | Madrid Barajas International Airport |  | ES | 1695 |
| 18 | Capua Airport |  | IT | 1646 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1630 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1611 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1589 |
| 22 | Macau International Airport |  | MO | 1562 |
| 23 | Malpensa International Airport |  | IT | 1520 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1488 |
| 26 | Charlotte/Douglas International Airport |  | US | 1452 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1328 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1320 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1290 |
| 33 | Seattle-Tacoma International Airport |  | US | 1282 |
| 34 | Viracopos International Airport |  | BR | 1261 |
| 35 | Calgary International Airport |  | CA | 1218 |
| 36 | Oslo Gardermoen Airport |  | NO | 1199 |
| 37 | Vitoria/Foronda Airport |  | ES | 1197 |
| 38 | Amsterdam Airport Schiphol |  | NL | 1170 |
| 39 | Don Mueang International Airport |  | TH | 1167 |
| 40 | Enrique Olaya Herrera Airport |  | CO | 1166 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1056 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 771 | 21m | 244 km | 3,246.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 487 | 13m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 469 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 361 | 27m | 275 km | 1,710.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 317 | 1h 49m | 1,423 km | 7,779.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 315 | 44m | 241 km | 1,308.4 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 266 | 27m | 215 km | 985.2 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 255 | 1h 14m | 961 km | 4,226.8 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 254 | 13m | - | - |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 246 | 19m | 144 km | 611.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 243 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 232 | 1h 49m | 1,304 km | 5,219.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HGB8236 | HGB | Palau International Airport (PTRO) | Chek Lap Kok International Airport (VHHH) | 2026-08-19 13:07 UTC | 2026-08-19 16:32 UTC | 3h 24m |
| AHK205 | AHK | Kansai International Airport (RJBB) | Chek Lap Kok International Airport (VHHH) | 2026-08-19 13:14 UTC | 2026-08-19 16:25 UTC | 3h 10m |
| N737GS |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-19 16:13 UTC | 2026-08-19 16:24 UTC | 11m |
| N9802Z |  | Williams Ranch Airport (1CO2) | Telluride Regional Airport (KTEX) | 2026-08-19 16:13 UTC | 2026-08-19 16:24 UTC | 10m |
| N71HH |  | Tib Field (40ME) | Sanford Seacoast Regional Airport (KSFM) | 2026-08-19 15:53 UTC | 2026-08-19 16:23 UTC | 30m |
| N618MM |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-19 15:08 UTC | 2026-08-19 16:22 UTC | 1h 14m |
| FDB3PR | flydubai | Sofia Airport (LBSF) | Queen Alia International Airport (OJAI) | 2026-08-19 15:05 UTC | 2026-08-19 16:22 UTC | 1h 17m |
| FJO67M | FJO | Torino / Caselle International Airport (LIMF) | Torino / Caselle International Airport (LIMF) | 2026-08-19 15:58 UTC | 2026-08-19 16:18 UTC | 20m |
| BRW149 | BRW | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-08-19 15:40 UTC | 2026-08-19 16:18 UTC | 37m |
| GCKGK | GCK | RAF Halton (EGWN) | RAF Halton (EGWN) | 2026-08-19 16:15 UTC | 2026-08-19 16:16 UTC | 0m |
| N519PR |  | Buchanan Field (KCCR) | Hayward Executive Airport (KHWD) | 2026-08-19 15:43 UTC | 2026-08-19 16:10 UTC | 27m |
| WIF5H | WIF | Bergen Airport Flesland (ENBR) | Trondheim Airport Vaernes (ENVA) | 2026-08-19 15:20 UTC | 2026-08-19 16:09 UTC | 49m |
| LXJ329 | LXJ | Des Moines International Airport (KDSM) | Telluride Regional Airport (KTEX) | 2026-08-19 13:52 UTC | 2026-08-19 16:09 UTC | 2h 17m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-19 15:21 UTC | 2026-08-19 16:08 UTC | 47m |
| AEE926 | AEE | Eleftherios Venizelos International Airport (LGAV) | Queen Alia International Airport (OJAI) | 2026-08-19 14:47 UTC | 2026-08-19 16:08 UTC | 1h 21m |
| EVC05 | EVC | Patuxent River Nas (Trapnell Field) Airport (KNHK) | Richmond Executive/Chesterfield County Airport (KFCI) | 2026-08-19 15:41 UTC | 2026-08-19 16:05 UTC | 24m |
| N49AW |  | Johnson Airport (3AK4) | Trading Bay Production Airport (5AK0) | 2026-08-19 15:49 UTC | 2026-08-19 16:03 UTC | 13m |
| LS16 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-19 15:41 UTC | 2026-08-19 16:03 UTC | 21m |
| N22XZ |  | Keflavik International Airport (BIKF) | Bangor International Airport (KBGR) | 2026-08-19 11:13 UTC | 2026-08-19 16:01 UTC | 4h 48m |
| N5NJ |  | Teterboro Airport (KTEB) | Linden Airport (KLDJ) | 2026-08-19 15:48 UTC | 2026-08-19 16:00 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
