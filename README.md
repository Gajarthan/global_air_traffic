# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_23:34:33_UTC-green)

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

**Latest saved flight:** 2026-09-05 23:34:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-05 23:34:33 UTC

- **248,988** saved flights
- **74,919** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **248,988** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,996,838.6 tonnes** estimated CO2 emissions
- **173,729,775 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9965 |
| 2 | SkyWest Airlines | 8703 |
| 3 | EJA | 4811 |
| 4 | IndiGo | 4154 |
| 5 | American Airlines | 3987 |
| 6 | Southwest Airlines | 3703 |
| 7 | Delta Air Lines | 3159 |
| 8 | ENY | 2983 |
| 9 | LATAM Airlines | 2404 |
| 10 | AZU | 2318 |
| 11 | Vueling | 2122 |
| 12 | WIF | 1986 |
| 13 | Lufthansa | 1975 |
| 14 | LXJ | 1936 |
| 15 | easyJet | 1719 |
| 16 | Swiss International | 1669 |
| 17 | AXM | 1627 |
| 18 | EJU | 1603 |
| 19 | QLK | 1591 |
| 20 | United Airlines | 1565 |
| 21 | Alaska Airlines | 1488 |
| 22 | All Nippon Airways | 1455 |
| 23 | WMT | 1409 |
| 24 | GLO | 1391 |
| 25 | VIV | 1367 |
| 26 | PGT | 1364 |
| 27 | Air France | 1359 |
| 28 | Wizz Air | 1343 |
| 29 | JetBlue | 1226 |
| 30 | AEE | 1223 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 206623 |
| 2 | 🇪🇸 ES | 15928 |
| 3 | 🇧🇷 BR | 14561 |
| 4 | 🇦🇺 AU | 14109 |
| 5 | 🇨🇦 CA | 13840 |
| 6 | 🇮🇹 IT | 13639 |
| 7 | 🇮🇳 IN | 12956 |
| 8 | 🇩🇪 DE | 12223 |
| 9 | 🇬🇧 GB | 11686 |
| 10 | 🇨🇴 CO | 10914 |
| 11 | 🇫🇷 FR | 10027 |
| 12 | 🇯🇵 JP | 9815 |
| 13 | 🇹🇷 TR | 7415 |
| 14 | 🇬🇷 GR | 7330 |
| 15 | 🇲🇽 MX | 6891 |
| 16 | 🇨🇭 CH | 6709 |
| 17 | 🇳🇴 NO | 6156 |
| 18 | 🇹🇭 TH | 4491 |
| 19 | 🇲🇾 MY | 4362 |
| 20 | 🇿🇦 ZA | 4291 |
| 21 | 🇵🇱 PL | 4162 |
| 22 | 🇳🇿 NZ | 3399 |
| 23 | 🇵🇭 PH | 3385 |
| 24 | 🇬🇹 GT | 3123 |
| 25 | 🇰🇷 KR | 2888 |
| 26 | 🇭🇷 HR | 2860 |
| 27 | 🇲🇦 MA | 2515 |
| 28 | 🇲🇪 ME | 2331 |
| 29 | 🇳🇱 NL | 2243 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5138 |
| 2 | Denver International Airport |  | US | 4028 |
| 3 | Indira Gandhi International Airport |  | IN | 3027 |
| 4 | Tokyo International Airport |  | JP | 2928 |
| 5 | Guaymaral Airport |  | CO | 2730 |
| 6 | Harry Reid International Airport |  | US | 2652 |
| 7 | Zurich Airport |  | CH | 2604 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2530 |
| 9 | El Dorado International Airport |  | CO | 2507 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2471 |
| 11 | La Aurora Airport |  | GT | 2380 |
| 12 | Salt Lake City International Airport |  | US | 2208 |
| 13 | Chicago O'Hare International Airport |  | US | 2181 |
| 14 | Congonhas Airport |  | BR | 2140 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2054 |
| 16 | Capua Airport |  | IT | 1960 |
| 17 | Madrid Barajas International Airport |  | ES | 1956 |
| 18 | Frankfurt am Main International Airport |  | DE | 1945 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1872 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1816 |
| 21 | Malpensa International Airport |  | IT | 1790 |
| 22 | Charles de Gaulle International Airport |  | FR | 1748 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1742 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1731 |
| 25 | Ninoy Aquino International Airport |  | PH | 1648 |
| 26 | Macau International Airport |  | MO | 1641 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1639 |
| 28 | Charlotte/Douglas International Airport |  | US | 1575 |
| 29 | Barcelona International Airport |  | ES | 1574 |
| 30 | Kuala Lumpur International Airport |  | MY | 1570 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1527 |
| 32 | Viracopos International Airport |  | BR | 1488 |
| 33 | Seattle-Tacoma International Airport |  | US | 1465 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1449 |
| 35 | Don Mueang International Airport |  | TH | 1440 |
| 36 | Calgary International Airport |  | CA | 1432 |
| 37 | Bengaluru International Airport |  | IN | 1429 |
| 38 | Oslo Gardermoen Airport |  | NO | 1398 |
| 39 | Vancouver International Airport |  | CA | 1394 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1352 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1103 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 925 | 21m | 244 km | 3,894.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 657 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 630 | 24m | 225 km | 2,444.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 624 | 1h 6m | 770 km | 8,289.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 561 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 410 | 27m | 275 km | 1,942.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 397 | 1h 50m | 1,423 km | 9,743.0 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 387 | 44m | 555 km | 3,705.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 370 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 368 | 44m | 241 km | 1,528.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 351 | 21m | 250 km | 1,516.1 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 348 | 24m | 218 km | 1,311.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 334 | 23m | 55 km | 317.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 332 | 1h 39m | 1,156 km | 6,623.3 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 306 | 26m | 215 km | 1,133.3 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 288 | 1h 14m | 961 km | 4,773.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 287 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 285 | 19m | 144 km | 708.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 270 | 1h 50m | 1,304 km | 6,074.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 256 | 28m | 152 km | 669.0 t |
| 30 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 254 | 41m | 535 km | 2,345.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTZ | YTZ | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-09-05 22:48 UTC | 2026-09-05 23:34 UTC | 46m |
| N114NS |  | True Grit South Airport (CO95) | True Grit South Airport (CO95) | 2026-09-05 23:16 UTC | 2026-09-05 23:31 UTC | 15m |
| N6455N |  | Montgomery-Gibbs Executive Airport (KMYF) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-05 23:09 UTC | 2026-09-05 23:25 UTC | 16m |
| LXJ612 | LXJ | Monroe County Airport (KBMG) | Metz Airport (3CA7) | 2026-09-05 18:58 UTC | 2026-09-05 23:13 UTC | 4h 15m |
| N424RP |  | Falcon Field (KFFZ) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-05 21:00 UTC | 2026-09-05 23:13 UTC | 2h 13m |
| N228KS |  | Odessa-Schlemeyer Field (KODO) | Boyd Airport (TX36) | 2026-09-05 22:38 UTC | 2026-09-05 23:13 UTC | 35m |
| XSN06 | XSN | North Las Vegas Airport (KVGT) | Lake Tahoe Airport (KTVL) | 2026-09-05 21:53 UTC | 2026-09-05 23:11 UTC | 1h 17m |
| DLH586 | Lufthansa | Munich International Airport (EDDM) | Giza Embaba Airport (HEEM) | 2026-09-05 20:09 UTC | 2026-09-05 23:10 UTC | 3h 0m |
| CAL5686 | CAL | Amsterdam Airport Schiphol (EHAM) | Pune Airport (VAPO) | 2026-09-05 15:16 UTC | 2026-09-05 23:08 UTC | 7h 52m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-05 15:44 UTC | 2026-09-05 23:02 UTC | 7h 18m |
| N228SB |  | Lincoln Airport (KLNK) | Mc Elroy Airfield (K20V) | 2026-09-05 21:47 UTC | 2026-09-05 23:01 UTC | 1h 13m |
| EJA667 | EJA | KHTO (KHTO) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-05 19:47 UTC | 2026-09-05 23:00 UTC | 3h 13m |
|  |  | Vancouver International Airport (CYVR) | Grand Forks Airport (CZGF) | 2026-09-05 21:58 UTC | 2026-09-05 22:59 UTC | 1h 1m |
| N251CT |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Santa Barbara Municipal Airport (KSBA) | 2026-09-05 22:11 UTC | 2026-09-05 22:59 UTC | 47m |
| LFA332 | LFA | Jacksonville Executive At Craig Airport (KCRG) | K55J (K55J) | 2026-09-05 22:14 UTC | 2026-09-05 22:58 UTC | 43m |
| N3466K |  | TX09 (TX09) | New Braunfels Ntl Airport (KBAZ) | 2026-09-05 22:55 UTC | 2026-09-05 22:56 UTC | 1m |
| EJA950 | EJA | John Wayne/Orange County Airport (KSNA) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-05 21:52 UTC | 2026-09-05 22:52 UTC | 59m |
| SAMU44 | SAM | Chateaubriant Pouance Airport (LFTQ) | Nantes Atlantique Airport (LFRS) | 2026-09-05 22:35 UTC | 2026-09-05 22:52 UTC | 16m |
| ASL18F | ASL | Frankfurt-Hahn Airport (EDFH) | Nis Airport (LYNI) | 2026-09-05 21:14 UTC | 2026-09-05 22:50 UTC | 1h 36m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-05 22:25 UTC | 2026-09-05 22:48 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
