# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_10:42:47_UTC-green)

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

**Latest saved flight:** 2026-08-23 10:42:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 10:42:47 UTC

- **228,158** saved flights
- **70,643** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,158** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,751,681.6 tonnes** estimated CO2 emissions
- **159,517,774 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9157 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4393 |
| 4 | IndiGo | 3860 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2919 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2184 |
| 10 | AZU | 2112 |
| 11 | Vueling | 1935 |
| 12 | Lufthansa | 1866 |
| 13 | WIF | 1799 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1589 |
| 16 | Swiss International | 1520 |
| 17 | AXM | 1515 |
| 18 | QLK | 1448 |
| 19 | EJU | 1445 |
| 20 | United Airlines | 1444 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1370 |
| 23 | GLO | 1265 |
| 24 | VIV | 1253 |
| 25 | PGT | 1251 |
| 26 | WMT | 1243 |
| 27 | Air France | 1241 |
| 28 | Wizz Air | 1185 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1138 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190652 |
| 2 | 🇪🇸 ES | 14633 |
| 3 | 🇧🇷 BR | 13294 |
| 4 | 🇦🇺 AU | 12949 |
| 5 | 🇨🇦 CA | 12620 |
| 6 | 🇮🇹 IT | 12289 |
| 7 | 🇮🇳 IN | 12029 |
| 8 | 🇩🇪 DE | 11223 |
| 9 | 🇬🇧 GB | 10722 |
| 10 | 🇨🇴 CO | 9384 |
| 11 | 🇯🇵 JP | 9300 |
| 12 | 🇫🇷 FR | 9121 |
| 13 | 🇹🇷 TR | 6710 |
| 14 | 🇬🇷 GR | 6699 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6030 |
| 17 | 🇳🇴 NO | 5606 |
| 18 | 🇲🇾 MY | 4045 |
| 19 | 🇹🇭 TH | 3962 |
| 20 | 🇿🇦 ZA | 3953 |
| 21 | 🇵🇱 PL | 3790 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3133 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2703 |
| 26 | 🇭🇷 HR | 2592 |
| 27 | 🇲🇦 MA | 2304 |
| 28 | 🇲🇪 ME | 2068 |
| 29 | 🇳🇱 NL | 2037 |
| 30 | 🇮🇩 ID | 1972 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2780 |
| 4 | Tokyo International Airport |  | JP | 2776 |
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
| 17 | Madrid Barajas International Airport |  | ES | 1780 |
| 18 | Capua Airport |  | IT | 1774 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1703 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1698 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1625 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1611 |
| 24 | Macau International Airport |  | MO | 1594 |
| 25 | Charles de Gaulle International Airport |  | FR | 1579 |
| 26 | Ninoy Aquino International Airport |  | PH | 1501 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1466 |
| 29 | Barcelona International Airport |  | ES | 1424 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1352 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 33 | Viracopos International Airport |  | BR | 1348 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1299 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1232 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 832 | 21m | 244 km | 3,503.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 573 | 1h 6m | 770 km | 7,611.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 347 | 1h 50m | 1,423 km | 8,515.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 314 | 1h 7m | 706 km | 3,823.0 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 312 | 21m | 250 km | 1,347.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 304 | 44m | 555 km | 2,910.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 291 | 24m | 218 km | 1,096.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 277 | 27m | 215 km | 1,025.9 t |
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
| EJU3629 | EJU | Malpensa International Airport (LIMC) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-23 09:45 UTC | 2026-08-23 10:42 UTC | 57m |
| HBKNE | HBK | Locarno Airport (LSZL) | Ambri Airport (LSPM) | 2026-08-23 10:23 UTC | 2026-08-23 10:40 UTC | 17m |
| VOZ878 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-08-23 09:02 UTC | 2026-08-23 10:39 UTC | 1h 37m |
| CRK260 | CRK | Chek Lap Kok International Airport (VHHH) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-23 09:04 UTC | 2026-08-23 10:38 UTC | 1h 33m |
| CHX32 | CHX | ETT1 (ETT1) | ETT1 (ETT1) | 2026-08-23 10:26 UTC | 2026-08-23 10:29 UTC | 3m |
| PH876 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-23 08:51 UTC | 2026-08-23 10:24 UTC | 1h 33m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-23 10:02 UTC | 2026-08-23 10:18 UTC | 16m |
| UBG149 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-23 09:31 UTC | 2026-08-23 10:09 UTC | 37m |
| CHX82 | CHX | Berlin Brandenburg Airport (EDDB) | Berlin Brandenburg Airport (EDDB) | 2026-08-23 10:05 UTC | 2026-08-23 10:06 UTC | 1m |
| RGA17 | RGA | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-23 09:54 UTC | 2026-08-23 10:06 UTC | 11m |
| N103GR |  | Westchester County Airport (KHPN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-23 09:35 UTC | 2026-08-23 10:04 UTC | 28m |
| OKUUR14 | OKU | Zamberk Airport (LKZM) | Zamberk Airport (LKZM) | 2026-08-23 10:01 UTC | 2026-08-23 10:03 UTC | 1m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Chandigarh Airport (VICG) | 2026-08-23 09:34 UTC | 2026-08-23 10:00 UTC | 25m |
| ELY027 | ELY | Ben Gurion International Airport (LLBG) | Newark Liberty International Airport (KEWR) | 2026-08-22 22:47 UTC | 2026-08-23 09:57 UTC | 11h 10m |
| RIZ01 | RIZ | Treviso / Sant'Angelo Airport (LIPH) | Klagenfurt Airport (LOWK) | 2026-08-23 09:31 UTC | 2026-08-23 09:57 UTC | 26m |
| AUA707X | Austrian Airlines | Vienna International Airport (LOWW) | Sibiu International Airport (LRSB) | 2026-08-23 09:08 UTC | 2026-08-23 09:55 UTC | 47m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-23 09:27 UTC | 2026-08-23 09:54 UTC | 27m |
| PH1551 |  | EHDB (EHDB) | EHDB (EHDB) | 2026-08-23 09:19 UTC | 2026-08-23 09:54 UTC | 35m |
| EAI31M | EAI | Southampton Airport (EGHI) | Dublin Airport (EIDW) | 2026-08-23 08:35 UTC | 2026-08-23 09:49 UTC | 1h 14m |
| CSZ9125 | CSZ | Shenzhen Bao'an International Airport (ZGSZ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-23 06:54 UTC | 2026-08-23 09:48 UTC | 2h 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
