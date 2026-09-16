# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_14:21:47_UTC-green)

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

**Latest saved flight:** 2026-09-16 14:21:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 14:21:47 UTC

- **260,212** saved flights
- **77,170** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **260,212** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,152,267.5 tonnes** estimated CO2 emissions
- **182,740,147 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10298 |
| 2 | SkyWest Airlines | 9065 |
| 3 | EJA | 5045 |
| 4 | IndiGo | 4370 |
| 5 | American Airlines | 4097 |
| 6 | Southwest Airlines | 3822 |
| 7 | Delta Air Lines | 3251 |
| 8 | ENY | 3078 |
| 9 | LATAM Airlines | 2506 |
| 10 | AZU | 2444 |
| 11 | Vueling | 2195 |
| 12 | WIF | 2093 |
| 13 | LXJ | 2034 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1768 |
| 16 | Swiss International | 1732 |
| 17 | QLK | 1681 |
| 18 | AXM | 1649 |
| 19 | EJU | 1646 |
| 20 | United Airlines | 1602 |
| 21 | Alaska Airlines | 1546 |
| 22 | All Nippon Airways | 1511 |
| 23 | WMT | 1468 |
| 24 | GLO | 1450 |
| 25 | PGT | 1449 |
| 26 | VIV | 1426 |
| 27 | Air France | 1424 |
| 28 | Wizz Air | 1414 |
| 29 | TKR | 1260 |
| 30 | AEE | 1259 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216024 |
| 2 | 🇪🇸 ES | 16466 |
| 3 | 🇧🇷 BR | 15219 |
| 4 | 🇦🇺 AU | 14879 |
| 5 | 🇨🇦 CA | 14477 |
| 6 | 🇮🇹 IT | 14151 |
| 7 | 🇮🇳 IN | 13765 |
| 8 | 🇩🇪 DE | 12631 |
| 9 | 🇬🇧 GB | 12110 |
| 10 | 🇨🇴 CO | 11708 |
| 11 | 🇫🇷 FR | 10435 |
| 12 | 🇯🇵 JP | 10125 |
| 13 | 🇹🇷 TR | 7851 |
| 14 | 🇬🇷 GR | 7564 |
| 15 | 🇲🇽 MX | 7175 |
| 16 | 🇨🇭 CH | 6981 |
| 17 | 🇳🇴 NO | 6427 |
| 18 | 🇹🇭 TH | 4679 |
| 19 | 🇲🇾 MY | 4442 |
| 20 | 🇿🇦 ZA | 4402 |
| 21 | 🇵🇱 PL | 4295 |
| 22 | 🇳🇿 NZ | 3609 |
| 23 | 🇵🇭 PH | 3487 |
| 24 | 🇬🇹 GT | 3325 |
| 25 | 🇭🇷 HR | 2977 |
| 26 | 🇰🇷 KR | 2969 |
| 27 | 🇲🇦 MA | 2609 |
| 28 | 🇲🇪 ME | 2448 |
| 29 | 🇳🇱 NL | 2330 |
| 30 | 🇮🇩 ID | 2199 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5327 |
| 2 | Denver International Airport |  | US | 4212 |
| 3 | Indira Gandhi International Airport |  | IN | 3139 |
| 4 | Tokyo International Airport |  | JP | 3021 |
| 5 | Guaymaral Airport |  | CO | 2769 |
| 6 | Harry Reid International Airport |  | US | 2762 |
| 7 | El Dorado International Airport |  | CO | 2731 |
| 8 | Zurich Airport |  | CH | 2723 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2616 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2533 |
| 11 | La Aurora Airport |  | GT | 2522 |
| 12 | Salt Lake City International Airport |  | US | 2295 |
| 13 | Chicago O'Hare International Airport |  | US | 2255 |
| 14 | Congonhas Airport |  | BR | 2224 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2127 |
| 16 | Capua Airport |  | IT | 2030 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1958 |
| 20 | Malpensa International Airport |  | IT | 1872 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1871 |
| 22 | Charles de Gaulle International Airport |  | FR | 1836 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1835 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1792 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1773 |
| 26 | Macau International Airport |  | MO | 1723 |
| 27 | Ninoy Aquino International Airport |  | PH | 1711 |
| 28 | Barcelona International Airport |  | ES | 1626 |
| 29 | Charlotte/Douglas International Airport |  | US | 1624 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1601 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1577 |
| 33 | Seattle-Tacoma International Airport |  | US | 1528 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1514 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1486 |
| 37 | Bengaluru International Airport |  | IN | 1478 |
| 38 | Oslo Gardermoen Airport |  | NO | 1464 |
| 39 | Vancouver International Airport |  | CA | 1456 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1398 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 970 | 21m | 244 km | 4,084.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 703 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 653 | 1h 6m | 770 km | 8,674.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 650 | 24m | 225 km | 2,521.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 583 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 395 | 44m | 241 km | 1,640.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 366 | 24m | 218 km | 1,378.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 358 | 21m | 250 km | 1,546.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 327 | 1h 6m | 706 km | 3,981.2 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 324 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 316 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 300 | 1h 14m | 961 km | 4,972.7 t |
| 23 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 27 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 277 | 42m | 535 km | 2,558.3 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N562X |  | MD09 (MD09) | MD09 (MD09) | 2026-09-16 14:08 UTC | 2026-09-16 14:21 UTC | 13m |
| N871ST |  | Reading Regional/Carl A Spaatz Field (KRDG) | Capital City Airport (KCXY) | 2026-09-16 13:54 UTC | 2026-09-16 14:16 UTC | 21m |
| N6640H |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-09-16 13:35 UTC | 2026-09-16 14:16 UTC | 41m |
| SMILER1 | SMI | Randolph Afb Airport (KRND) | Flying L Airport (TE90) | 2026-09-16 13:56 UTC | 2026-09-16 14:15 UTC | 19m |
| N6964H |  | Montgomery County Airpark (KGAI) | Montgomery County Airpark (KGAI) | 2026-09-16 11:32 UTC | 2026-09-16 14:13 UTC | 2h 41m |
| N800FV |  | Newport Regional Airport (KM19) | Newport Regional Airport (KM19) | 2026-09-16 14:00 UTC | 2026-09-16 14:12 UTC | 12m |
| OXF42 | OXF | Oxford (Kidlington) Airport (EGTK) | Turweston Airport (EGBT) | 2026-09-16 12:55 UTC | 2026-09-16 14:11 UTC | 1h 15m |
| N4583R |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-09-16 13:55 UTC | 2026-09-16 14:10 UTC | 14m |
| N439H |  | Westover Arb/Metro Airport (KCEF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-16 13:40 UTC | 2026-09-16 14:09 UTC | 29m |
| N4768E |  | Ryan Field (KRYN) | Ryan Field (KRYN) | 2026-09-16 13:54 UTC | 2026-09-16 14:09 UTC | 14m |
| N727GH |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-09-16 13:37 UTC | 2026-09-16 14:09 UTC | 31m |
| N733ZB |  | Owosso Community Airport (KRNP) | Owosso Community Airport (KRNP) | 2026-09-16 13:33 UTC | 2026-09-16 14:07 UTC | 33m |
| N509AM |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-16 13:35 UTC | 2026-09-16 14:03 UTC | 28m |
| CXK335 | CXK | Long Island Mac Arthur Airport (KISP) | Elizabeth Field (K0B8) | 2026-09-16 13:25 UTC | 2026-09-16 14:03 UTC | 38m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Medina River Ranch Airport (XS43) | 2026-09-16 13:17 UTC | 2026-09-16 14:01 UTC | 44m |
| YRZEF | YRZ | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-09-16 13:11 UTC | 2026-09-16 13:56 UTC | 45m |
| EJM713 | EJM | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-16 13:42 UTC | 2026-09-16 13:55 UTC | 13m |
| N804FA |  | Dyersburg Regional Airport (KDYR) | Dyersburg Regional Airport (KDYR) | 2026-09-16 13:01 UTC | 2026-09-16 13:54 UTC | 52m |
| IGO697H | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-16 09:43 UTC | 2026-09-16 13:53 UTC | 4h 10m |
| N5444F |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-09-16 13:44 UTC | 2026-09-16 13:46 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
