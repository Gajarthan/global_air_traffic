# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_11:01:18_UTC-green)

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

**Latest saved flight:** 2026-08-21 11:01:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 11:01:18 UTC

- **221,774** saved flights
- **69,441** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **221,774** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,669,845.4 tonnes** estimated CO2 emissions
- **154,773,647 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8885 |
| 2 | SkyWest Airlines | 7891 |
| 3 | EJA | 4289 |
| 4 | IndiGo | 3765 |
| 5 | American Airlines | 3671 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2852 |
| 8 | ENY | 2724 |
| 9 | LATAM Airlines | 2104 |
| 10 | AZU | 2032 |
| 11 | Vueling | 1867 |
| 12 | Lufthansa | 1834 |
| 13 | WIF | 1774 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1532 |
| 16 | Swiss International | 1474 |
| 17 | AXM | 1465 |
| 18 | QLK | 1405 |
| 19 | United Airlines | 1390 |
| 20 | EJU | 1386 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | GLO | 1211 |
| 24 | PGT | 1210 |
| 25 | VIV | 1206 |
| 26 | Air France | 1203 |
| 27 | WMT | 1178 |
| 28 | Wizz Air | 1134 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1108 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186309 |
| 2 | 🇪🇸 ES | 14213 |
| 3 | 🇧🇷 BR | 12792 |
| 4 | 🇦🇺 AU | 12645 |
| 5 | 🇨🇦 CA | 12248 |
| 6 | 🇮🇹 IT | 11801 |
| 7 | 🇮🇳 IN | 11737 |
| 8 | 🇩🇪 DE | 10941 |
| 9 | 🇬🇧 GB | 10398 |
| 10 | 🇨🇴 CO | 9104 |
| 11 | 🇯🇵 JP | 9041 |
| 12 | 🇫🇷 FR | 8826 |
| 13 | 🇬🇷 GR | 6474 |
| 14 | 🇹🇷 TR | 6404 |
| 15 | 🇲🇽 MX | 6157 |
| 16 | 🇨🇭 CH | 5848 |
| 17 | 🇳🇴 NO | 5518 |
| 18 | 🇲🇾 MY | 3881 |
| 19 | 🇿🇦 ZA | 3801 |
| 20 | 🇹🇭 TH | 3740 |
| 21 | 🇵🇱 PL | 3675 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3015 |
| 24 | 🇬🇹 GT | 2793 |
| 25 | 🇰🇷 KR | 2655 |
| 26 | 🇭🇷 HR | 2466 |
| 27 | 🇲🇦 MA | 2226 |
| 28 | 🇳🇱 NL | 1968 |
| 29 | 🇲🇪 ME | 1965 |
| 30 | 🇮🇩 ID | 1898 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4649 |
| 2 | Denver International Airport |  | US | 3615 |
| 3 | Tokyo International Airport |  | JP | 2710 |
| 4 | Indira Gandhi International Airport |  | IN | 2696 |
| 5 | Guaymaral Airport |  | CO | 2606 |
| 6 | Harry Reid International Airport |  | US | 2443 |
| 7 | Zurich Airport |  | CH | 2296 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2252 |
| 10 | La Aurora Airport |  | GT | 2128 |
| 11 | El Dorado International Airport |  | CO | 2073 |
| 12 | Chicago O'Hare International Airport |  | US | 2025 |
| 13 | Salt Lake City International Airport |  | US | 1948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1909 |
| 15 | Congonhas Airport |  | BR | 1869 |
| 16 | Frankfurt am Main International Airport |  | DE | 1798 |
| 17 | Madrid Barajas International Airport |  | ES | 1738 |
| 18 | Capua Airport |  | IT | 1694 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1661 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1630 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1586 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1553 |
| 25 | Charles de Gaulle International Airport |  | FR | 1528 |
| 26 | Charlotte/Douglas International Airport |  | US | 1471 |
| 27 | Ninoy Aquino International Airport |  | PH | 1435 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1362 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1346 |
| 31 | Bengaluru International Airport |  | IN | 1330 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1315 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1299 |
| 35 | Calgary International Airport |  | CA | 1256 |
| 36 | Oslo Gardermoen Airport |  | NO | 1236 |
| 37 | Enrique Olaya Herrera Airport |  | CO | 1235 |
| 38 | Vitoria/Foronda Airport |  | ES | 1231 |
| 39 | Don Mueang International Airport |  | TH | 1230 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1191 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1064 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 800 | 21m | 244 km | 3,368.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 553 | 1h 7m | 770 km | 7,346.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 499 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 499 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 374 | 27m | 275 km | 1,772.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 329 | 1h 50m | 1,423 km | 8,074.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 293 | 21m | 250 km | 1,265.6 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 277 | 1h 38m | 1,156 km | 5,526.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 276 | 24m | 218 km | 1,039.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 273 | 27m | 215 km | 1,011.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 269 | 44m | 555 km | 2,575.8 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 261 | 1h 14m | 961 km | 4,326.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 252 | 19m | 144 km | 626.8 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 239 | 1h 49m | 1,304 km | 5,376.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXHGG | SXH | Eleftherios Venizelos International Airport (LGAV) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-21 10:47 UTC | 2026-08-21 11:01 UTC | 13m |
| WZZ53 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Stuttgart Airport (EDDS) | 2026-08-21 09:05 UTC | 2026-08-21 10:21 UTC | 1h 15m |
| WNG17E | WNG | Treasure Coast International Airport (KFPR) | Baggett Airport (FD57) | 2026-08-21 09:54 UTC | 2026-08-21 10:21 UTC | 26m |
| AAL208 | American Airlines | Chicago O'Hare International Airport (KORD) | Dublin Airport (EIDW) | 2026-08-21 03:43 UTC | 2026-08-21 10:21 UTC | 6h 37m |
| LLR853 | LLR | Hissar Airport (VIHR) | Ambala Air Force Station (VIAM) | 2026-08-21 09:40 UTC | 2026-08-21 10:19 UTC | 38m |
| LHX3VJ | LHX | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-08-21 09:25 UTC | 2026-08-21 10:12 UTC | 46m |
| N562JL |  | Long Beach (Daugherty Field) Airport (KLGB) | San Francisco International Airport (KSFO) | 2026-08-21 09:12 UTC | 2026-08-21 10:08 UTC | 55m |
| SYS06 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-08-21 08:26 UTC | 2026-08-21 10:06 UTC | 1h 39m |
| SHY04 | SHY | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-08-21 09:32 UTC | 2026-08-21 10:04 UTC | 31m |
| SWR97Q | Swiss International | Bologna / Borgo Panigale Airport (LIPE) | Zurich Airport (LSZH) | 2026-08-21 08:50 UTC | 2026-08-21 10:04 UTC | 1h 13m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | G 605 Airport (RK6O) | 2026-08-21 09:27 UTC | 2026-08-21 10:03 UTC | 36m |
| CSZ662 | CSZ | Kansai International Airport (RJBB) | Guangzhou Baiyun International Airport (ZGGG) | 2026-08-21 06:39 UTC | 2026-08-21 09:57 UTC | 3h 18m |
| AUA63N | Austrian Airlines | Budapest Ferenc Liszt International Airport (LHBP) | Vienna International Airport (LOWW) | 2026-08-21 09:18 UTC | 2026-08-21 09:56 UTC | 37m |
| AEA7157 | AEA | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-08-21 09:30 UTC | 2026-08-21 09:55 UTC | 25m |
| TCNYK | TCN | Antalya International Airport (LTAI) | Corte Airport (LFKT) | 2026-08-21 07:19 UTC | 2026-08-21 09:54 UTC | 2h 35m |
| DLH3HX | Lufthansa | Munich International Airport (EDDM) | Sibiu International Airport (LRSB) | 2026-08-21 08:52 UTC | 2026-08-21 09:53 UTC | 1h 1m |
| HVN431 | HVN | Incheon International Airport (RKSI) | Noi Bai International Airport (VVNB) | 2026-08-21 03:04 UTC | 2026-08-21 09:52 UTC | 6h 48m |
| SWR9MH | Swiss International | Stuttgart Airport (EDDS) | Zurich Airport (LSZH) | 2026-08-21 08:50 UTC | 2026-08-21 09:52 UTC | 1h 1m |
| RYR39DE | Ryanair | Dublin Airport (EIDW) | Kenitra Airport (GMMY) | 2026-08-21 07:09 UTC | 2026-08-21 09:49 UTC | 2h 40m |
| RTG7100 | RTG | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-08-21 09:09 UTC | 2026-08-21 09:48 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
