# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_10:24:57_UTC-green)

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

**Latest saved flight:** 2026-08-23 10:24:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 10:24:57 UTC

- **228,108** saved flights
- **70,640** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,108** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,750,865.9 tonnes** estimated CO2 emissions
- **159,470,485 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9155 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3859 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1935 |
| 12 | Lufthansa | 1866 |
| 13 | WIF | 1798 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1588 |
| 16 | Swiss International | 1520 |
| 17 | AXM | 1514 |
| 18 | QLK | 1447 |
| 19 | EJU | 1444 |
| 20 | United Airlines | 1444 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1370 |
| 23 | GLO | 1264 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | WMT | 1241 |
| 27 | Air France | 1238 |
| 28 | Wizz Air | 1183 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190648 |
| 2 | 🇪🇸 ES | 14630 |
| 3 | 🇧🇷 BR | 13293 |
| 4 | 🇦🇺 AU | 12945 |
| 5 | 🇨🇦 CA | 12620 |
| 6 | 🇮🇹 IT | 12284 |
| 7 | 🇮🇳 IN | 12025 |
| 8 | 🇩🇪 DE | 11218 |
| 9 | 🇬🇧 GB | 10716 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9296 |
| 12 | 🇫🇷 FR | 9118 |
| 13 | 🇹🇷 TR | 6705 |
| 14 | 🇬🇷 GR | 6697 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6028 |
| 17 | 🇳🇴 NO | 5604 |
| 18 | 🇲🇾 MY | 4040 |
| 19 | 🇹🇭 TH | 3958 |
| 20 | 🇿🇦 ZA | 3953 |
| 21 | 🇵🇱 PL | 3790 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3131 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2703 |
| 26 | 🇭🇷 HR | 2591 |
| 27 | 🇲🇦 MA | 2303 |
| 28 | 🇲🇪 ME | 2067 |
| 29 | 🇳🇱 NL | 2037 |
| 30 | 🇮🇩 ID | 1971 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2778 |
| 4 | Tokyo International Airport |  | JP | 2774 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2473 |
| 7 | Zurich Airport |  | CH | 2371 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2332 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2303 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2009 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1829 |
| 17 | Madrid Barajas International Airport |  | ES | 1779 |
| 18 | Capua Airport |  | IT | 1772 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1648 |
| 22 | Malpensa International Airport |  | IT | 1624 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1610 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1576 |
| 26 | Ninoy Aquino International Airport |  | PH | 1500 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1464 |
| 29 | Barcelona International Airport |  | ES | 1423 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1352 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Calgary International Airport |  | CA | 1299 |
| 37 | Don Mueang International Airport |  | TH | 1297 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1232 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 572 | 1h 6m | 770 km | 7,598.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 347 | 1h 50m | 1,423 km | 8,515.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 312 | 21m | 250 km | 1,347.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 303 | 44m | 555 km | 2,901.4 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 260 | 19m | 144 km | 646.7 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 240 | 15m | 154 km | 635.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PH876 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-23 08:51 UTC | 2026-08-23 10:24 UTC | 1h 33m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-23 10:02 UTC | 2026-08-23 10:18 UTC | 16m |
| RGA17 | RGA | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-23 09:54 UTC | 2026-08-23 10:06 UTC | 11m |
| OKUUR14 | OKU | Zamberk Airport (LKZM) | Zamberk Airport (LKZM) | 2026-08-23 10:01 UTC | 2026-08-23 10:03 UTC | 1m |
| ELY027 | ELY | Ben Gurion International Airport (LLBG) | Newark Liberty International Airport (KEWR) | 2026-08-22 22:47 UTC | 2026-08-23 09:57 UTC | 11h 10m |
| PH1551 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-23 09:19 UTC | 2026-08-23 09:54 UTC | 35m |
| EAI31M | EAI | Southampton Airport (EGHI) | Dublin Airport (EIDW) | 2026-08-23 08:35 UTC | 2026-08-23 09:49 UTC | 1h 14m |
| UPS64 | UPS | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 07:45 UTC | 2026-08-23 09:46 UTC | 2h 1m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Muenster Aero Airport (LSPU) | 2026-08-23 09:29 UTC | 2026-08-23 09:44 UTC | 14m |
| AWA475 | AWA | VGZR (VGZR) | Saidpur Airport (VGSD) | 2026-08-23 08:55 UTC | 2026-08-23 09:32 UTC | 36m |
| SAS1048 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Gallivare Airport (ESNG) | 2026-08-23 08:20 UTC | 2026-08-23 09:31 UTC | 1h 10m |
| FDA397 | FDA | Nagoya Airport (RJNA) | Okadama Airport (RJCO) | 2026-08-23 08:03 UTC | 2026-08-23 09:27 UTC | 1h 24m |
| AEE4579 | AEE | Kuopio Airport (EFKU) | Barysiai Airport (EYSB) | 2026-08-23 08:26 UTC | 2026-08-23 09:26 UTC | 1h 0m |
| GBWUH | GBW | RNAS Lee-On-Solent (EGHF) | RNAS Lee-On-Solent (EGHF) | 2026-08-23 08:55 UTC | 2026-08-23 09:26 UTC | 31m |
| CTV992 | CTV | Soekarno-Hatta International Airport (WIII) | WIAT (WIAT) | 2026-08-23 09:03 UTC | 2026-08-23 09:24 UTC | 21m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Reykjanes Airport (BIRS) | 2026-08-23 08:59 UTC | 2026-08-23 09:24 UTC | 24m |
| WIF9VK | WIF | Bergen Airport Flesland (ENBR) | Molde Airport (ENML) | 2026-08-23 08:49 UTC | 2026-08-23 09:23 UTC | 33m |
| IGO4EP | IndiGo | Chennai International Airport (VOMM) | Salem Airport (VOSM) | 2026-08-23 08:40 UTC | 2026-08-23 09:22 UTC | 42m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-23 09:10 UTC | 2026-08-23 09:21 UTC | 10m |
| PH1635 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-23 09:14 UTC | 2026-08-23 09:20 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
