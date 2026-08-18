# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_23:09:56_UTC-green)

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

**Latest saved flight:** 2026-08-18 23:09:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 23:09:56 UTC

- **213,845** saved flights
- **67,613** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,845** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,571,464.8 tonnes** estimated CO2 emissions
- **149,070,424 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8487 |
| 2 | SkyWest Airlines | 7682 |
| 3 | EJA | 4176 |
| 4 | IndiGo | 3644 |
| 5 | American Airlines | 3574 |
| 6 | Southwest Airlines | 3420 |
| 7 | Delta Air Lines | 2757 |
| 8 | ENY | 2658 |
| 9 | LATAM Airlines | 2021 |
| 10 | AZU | 1956 |
| 11 | Vueling | 1791 |
| 12 | Lufthansa | 1784 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1689 |
| 15 | easyJet | 1483 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1359 |
| 19 | QLK | 1322 |
| 20 | EJU | 1316 |
| 21 | Alaska Airlines | 1311 |
| 22 | All Nippon Airways | 1287 |
| 23 | VIV | 1179 |
| 24 | GLO | 1161 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1103 |
| 28 | JetBlue | 1090 |
| 29 | AEE | 1080 |
| 30 | Wizz Air | 1068 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180869 |
| 2 | 🇪🇸 ES | 13681 |
| 3 | 🇧🇷 BR | 12313 |
| 4 | 🇦🇺 AU | 11976 |
| 5 | 🇨🇦 CA | 11821 |
| 6 | 🇮🇳 IN | 11360 |
| 7 | 🇮🇹 IT | 11267 |
| 8 | 🇩🇪 DE | 10539 |
| 9 | 🇬🇧 GB | 9970 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8699 |
| 12 | 🇫🇷 FR | 8488 |
| 13 | 🇬🇷 GR | 6263 |
| 14 | 🇹🇷 TR | 6129 |
| 15 | 🇲🇽 MX | 6003 |
| 16 | 🇨🇭 CH | 5656 |
| 17 | 🇳🇴 NO | 5310 |
| 18 | 🇲🇾 MY | 3676 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3526 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2955 |
| 23 | 🇵🇭 PH | 2839 |
| 24 | 🇬🇹 GT | 2728 |
| 25 | 🇰🇷 KR | 2585 |
| 26 | 🇭🇷 HR | 2326 |
| 27 | 🇲🇦 MA | 2154 |
| 28 | 🇳🇱 NL | 1903 |
| 29 | 🇲🇪 ME | 1849 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4506 |
| 2 | Denver International Airport |  | US | 3503 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2594 |
| 5 | Guaymaral Airport |  | CO | 2559 |
| 6 | Harry Reid International Airport |  | US | 2390 |
| 7 | Zurich Airport |  | CH | 2223 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2207 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2200 |
| 10 | La Aurora Airport |  | GT | 2074 |
| 11 | El Dorado International Airport |  | CO | 1980 |
| 12 | Chicago O'Hare International Airport |  | US | 1976 |
| 13 | Salt Lake City International Airport |  | US | 1890 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1887 |
| 15 | Congonhas Airport |  | BR | 1793 |
| 16 | Frankfurt am Main International Airport |  | DE | 1741 |
| 17 | Madrid Barajas International Airport |  | ES | 1667 |
| 18 | Capua Airport |  | IT | 1617 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1616 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1605 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1569 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Malpensa International Airport |  | IT | 1491 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 25 | Charles de Gaulle International Airport |  | FR | 1472 |
| 26 | Charlotte/Douglas International Airport |  | US | 1439 |
| 27 | Kuala Lumpur International Airport |  | MY | 1357 |
| 28 | Ninoy Aquino International Airport |  | PH | 1346 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1317 |
| 30 | Barcelona International Airport |  | ES | 1304 |
| 31 | Bengaluru International Airport |  | IN | 1304 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1285 |
| 33 | Seattle-Tacoma International Airport |  | US | 1270 |
| 34 | Viracopos International Airport |  | BR | 1250 |
| 35 | Calgary International Airport |  | CA | 1214 |
| 36 | Oslo Gardermoen Airport |  | NO | 1182 |
| 37 | Vitoria/Foronda Airport |  | ES | 1176 |
| 38 | Reno/Tahoe International Airport |  | US | 1161 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1152 |
| 40 | Enrique Olaya Herrera Airport |  | CO | 1139 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1046 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 760 | 21m | 244 km | 3,200.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 482 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 458 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 266 | 19m | 99 km | 455.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 265 | 1h 38m | 1,156 km | 5,286.7 t |
| 19 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 254 | 1h 14m | 961 km | 4,210.2 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 246 | 31m | 369 km | 1,565.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 241 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 230 | 1h 49m | 1,304 km | 5,174.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CARD44 | CAR | Seoul Air Base (RKSM) | RKRS (RKRS) | 2026-08-18 22:57 UTC | 2026-08-18 23:09 UTC | 12m |
| CARD43 | CAR | Seoul Air Base (RKSM) | RKRS (RKRS) | 2026-08-18 22:57 UTC | 2026-08-18 23:08 UTC | 11m |
| ICY76 | ICY | Yentna Bend Strip (0AK2) | Jewell Airport (AK72) | 2026-08-18 22:39 UTC | 2026-08-18 23:08 UTC | 28m |
| RYR5ST | Ryanair | Bournemouth Airport (EGHH) | Saint-Affrique-Belmont Airport (LFIF) | 2026-08-18 21:28 UTC | 2026-08-18 23:07 UTC | 1h 38m |
| FTO383 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-18 22:36 UTC | 2026-08-18 23:06 UTC | 30m |
| N6946F |  | Somerset Airport (KSMQ) | Sky Manor Airport (KN40) | 2026-08-18 22:25 UTC | 2026-08-18 23:04 UTC | 39m |
| N714ER |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-18 22:34 UTC | 2026-08-18 22:55 UTC | 21m |
| URSA19 | URS | Gold King Creek Airport (PAAN) | Ladd Army Air Field (PAFB) | 2026-08-18 21:29 UTC | 2026-08-18 22:55 UTC | 1h 26m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-18 22:02 UTC | 2026-08-18 22:47 UTC | 44m |
| N321AP |  | Montréal / St-Hubert Airport (CYHU) | Bangor International Airport (KBGR) | 2026-08-18 22:09 UTC | 2026-08-18 22:46 UTC | 37m |
| IN613 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-18 21:50 UTC | 2026-08-18 22:41 UTC | 51m |
| N149UD |  | Chicago Executive Airport (KPWK) | Chicago Executive Airport (KPWK) | 2026-08-18 21:47 UTC | 2026-08-18 22:40 UTC | 53m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-18 21:55 UTC | 2026-08-18 22:40 UTC | 45m |
| EDGE92 | EDG | 4XA5 (4XA5) | Ksa Orchards Airport (OK11) | 2026-08-18 22:05 UTC | 2026-08-18 22:40 UTC | 34m |
| N671PC |  | Las Cruces International Airport (KLRU) | Grant County Airport (KSVC) | 2026-08-18 22:20 UTC | 2026-08-18 22:36 UTC | 16m |
| N54P |  | Washington Dulles International Airport (KIAD) | Flying Cloud Airport (KFCM) | 2026-08-18 20:16 UTC | 2026-08-18 22:34 UTC | 2h 18m |
| CPA696 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-08-18 17:25 UTC | 2026-08-18 22:34 UTC | 5h 9m |
| N7237Q |  | Lincoln County Regional Airport (KIPJ) | Lincoln County Regional Airport (KIPJ) | 2026-08-18 21:40 UTC | 2026-08-18 22:33 UTC | 52m |
| N992CE |  | Page Field (KFMY) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-18 20:21 UTC | 2026-08-18 22:33 UTC | 2h 11m |
| TKR912 | TKR | Albuquerque International Sunport Airport (KABQ) | Sandia Airpark Estates East Airport (K1N1) | 2026-08-18 22:27 UTC | 2026-08-18 22:32 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
