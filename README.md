# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_17:54:00_UTC-green)

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

**Latest saved flight:** 2026-09-05 17:54:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 17:54:00 UTC

- **248,603** saved flights
- **74,839** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,603** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,990,722.2 tonnes** estimated CO2 emissions
- **173,375,199 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9954 |
| 2 | SkyWest Airlines | 8679 |
| 3 | EJA | 4797 |
| 4 | IndiGo | 4153 |
| 5 | American Airlines | 3977 |
| 6 | Southwest Airlines | 3698 |
| 7 | Delta Air Lines | 3155 |
| 8 | ENY | 2972 |
| 9 | LATAM Airlines | 2399 |
| 10 | AZU | 2314 |
| 11 | Vueling | 2122 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1974 |
| 14 | LXJ | 1929 |
| 15 | easyJet | 1716 |
| 16 | Swiss International | 1668 |
| 17 | AXM | 1627 |
| 18 | EJU | 1603 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1559 |
| 21 | Alaska Airlines | 1483 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1408 |
| 24 | GLO | 1388 |
| 25 | VIV | 1366 |
| 26 | PGT | 1362 |
| 27 | Air France | 1358 |
| 28 | Wizz Air | 1341 |
| 29 | JetBlue | 1224 |
| 30 | AEE | 1223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206194 |
| 2 | 🇪🇸 ES | 15917 |
| 3 | 🇧🇷 BR | 14535 |
| 4 | 🇦🇺 AU | 14105 |
| 5 | 🇨🇦 CA | 13814 |
| 6 | 🇮🇹 IT | 13620 |
| 7 | 🇮🇳 IN | 12950 |
| 8 | 🇩🇪 DE | 12218 |
| 9 | 🇬🇧 GB | 11675 |
| 10 | 🇨🇴 CO | 10869 |
| 11 | 🇫🇷 FR | 10021 |
| 12 | 🇯🇵 JP | 9815 |
| 13 | 🇹🇷 TR | 7405 |
| 14 | 🇬🇷 GR | 7327 |
| 15 | 🇲🇽 MX | 6883 |
| 16 | 🇨🇭 CH | 6706 |
| 17 | 🇳🇴 NO | 6156 |
| 18 | 🇹🇭 TH | 4491 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4158 |
| 22 | 🇳🇿 NZ | 3397 |
| 23 | 🇵🇭 PH | 3383 |
| 24 | 🇬🇹 GT | 3115 |
| 25 | 🇰🇷 KR | 2886 |
| 26 | 🇭🇷 HR | 2858 |
| 27 | 🇲🇦 MA | 2513 |
| 28 | 🇲🇪 ME | 2326 |
| 29 | 🇳🇱 NL | 2237 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5118 |
| 2 | Denver International Airport |  | US | 4011 |
| 3 | Indira Gandhi International Airport |  | IN | 3026 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2724 |
| 6 | Harry Reid International Airport |  | US | 2650 |
| 7 | Zurich Airport |  | CH | 2602 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2525 |
| 9 | El Dorado International Airport |  | CO | 2493 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2471 |
| 11 | La Aurora Airport |  | GT | 2373 |
| 12 | Salt Lake City International Airport |  | US | 2204 |
| 13 | Chicago O'Hare International Airport |  | US | 2178 |
| 14 | Congonhas Airport |  | BR | 2138 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2048 |
| 16 | Capua Airport |  | IT | 1957 |
| 17 | Madrid Barajas International Airport |  | ES | 1951 |
| 18 | Frankfurt am Main International Airport |  | DE | 1945 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1868 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1789 |
| 22 | Charles de Gaulle International Airport |  | FR | 1746 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1728 |
| 25 | Ninoy Aquino International Airport |  | PH | 1647 |
| 26 | Macau International Airport |  | MO | 1638 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1634 |
| 28 | Charlotte/Douglas International Airport |  | US | 1575 |
| 29 | Barcelona International Airport |  | ES | 1574 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1525 |
| 32 | Viracopos International Airport |  | BR | 1483 |
| 33 | Seattle-Tacoma International Airport |  | US | 1462 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1446 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1431 |
| 37 | Bengaluru International Airport |  | IN | 1429 |
| 38 | Oslo Gardermoen Airport |  | NO | 1398 |
| 39 | Vancouver International Airport |  | CA | 1390 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1348 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 923 | 21m | 244 km | 3,886.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 656 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 629 | 24m | 225 km | 2,440.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 558 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 409 | 27m | 275 km | 1,938.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 370 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 333 | 23m | 55 km | 316.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 295 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 287 | 1h 14m | 961 km | 4,757.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 284 | 19m | 144 km | 706.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N49285 |  | Fullerton Municipal Airport (KFUL) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-05 17:04 UTC | 2026-09-05 17:54 UTC | 49m |
| N307SW |  | Gillespie Field (KSEE) | Van Nuys Airport (KVNY) | 2026-09-05 16:12 UTC | 2026-09-05 17:53 UTC | 1h 41m |
| SWR9TC | Swiss International | Zurich Airport (LSZH) | Manchester Airport (EGCC) | 2026-09-05 15:29 UTC | 2026-09-05 17:51 UTC | 2h 22m |
| N6409E |  | Chehalis-Centralia Airport (KCLS) | Olympia Regional Airport (KOLM) | 2026-09-05 17:32 UTC | 2026-09-05 17:49 UTC | 16m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-05 17:19 UTC | 2026-09-05 17:42 UTC | 23m |
| N44836 |  | Dillant/Hopkins Airport (KEEN) | Dillant/Hopkins Airport (KEEN) | 2026-09-05 17:29 UTC | 2026-09-05 17:35 UTC | 5m |
| N4920P |  | Porter County Regional Airport (KVPZ) | Purdue University Airport (KLAF) | 2026-09-05 17:01 UTC | 2026-09-05 17:32 UTC | 30m |
| N321FS |  | Brigham City Regional Airport (KBMC) | Preston Airport (KU10) | 2026-09-05 17:08 UTC | 2026-09-05 17:27 UTC | 19m |
| N99832 |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-09-05 16:33 UTC | 2026-09-05 17:26 UTC | 53m |
| HK5445 |  | Santiago Vila Airport (SKGI) | Santiago Vila Airport (SKGI) | 2026-09-05 17:04 UTC | 2026-09-05 17:23 UTC | 19m |
| N106PA |  | La Aurora Airport (MGGT) | El Palmer Airport (MSSA) | 2026-09-05 17:06 UTC | 2026-09-05 17:21 UTC | 15m |
| TKR02 | TKR | TX20 (TX20) | Silverton Municipal Airport (79XS) | 2026-09-05 17:01 UTC | 2026-09-05 17:20 UTC | 19m |
| N181LT |  | Caldwell Executive Airport (KEUL) | Bald Mountain Airport (OG45) | 2026-09-05 17:00 UTC | 2026-09-05 17:18 UTC | 18m |
| TKR41 | TKR | TX20 (TX20) | Silverton Municipal Airport (79XS) | 2026-09-05 16:59 UTC | 2026-09-05 17:18 UTC | 19m |
| N18NY |  | Van Nuys Airport (KVNY) | Mesawood Airport (6CO2) | 2026-09-05 16:12 UTC | 2026-09-05 17:17 UTC | 1h 5m |
| N805FA |  | Palo Alto Airport (KPAO) | Santa Ynez/Kunkle Field (KIZA) | 2026-09-05 16:17 UTC | 2026-09-05 17:15 UTC | 58m |
| N447RM |  | Billings Logan International Airport (KBIL) | Cottonwood Airport (0MT5) | 2026-09-05 17:00 UTC | 2026-09-05 17:15 UTC | 14m |
| N692CK |  | Burke Lakefront Airport (KBKL) | Burke Lakefront Airport (KBKL) | 2026-09-05 17:08 UTC | 2026-09-05 17:15 UTC | 7m |
| N2QW |  | Lake County Airport (KLXV) | Athanasiou Valley Airport (CO07) | 2026-09-05 15:15 UTC | 2026-09-05 17:13 UTC | 1h 57m |
| N56BA |  | Tazewell County Airport (KJFZ) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-09-05 16:35 UTC | 2026-09-05 17:11 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
