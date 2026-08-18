# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_17:04:27_UTC-green)

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

**Latest saved flight:** 2026-08-18 17:04:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 17:04:27 UTC

- **212,614** saved flights
- **67,343** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **212,614** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,555,644.9 tonnes** estimated CO2 emissions
- **148,153,328 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8431 |
| 2 | SkyWest Airlines | 7619 |
| 3 | EJA | 4133 |
| 4 | IndiGo | 3639 |
| 5 | American Airlines | 3544 |
| 6 | Southwest Airlines | 3390 |
| 7 | Delta Air Lines | 2740 |
| 8 | ENY | 2636 |
| 9 | LATAM Airlines | 2006 |
| 10 | AZU | 1932 |
| 11 | Lufthansa | 1783 |
| 12 | Vueling | 1778 |
| 13 | WIF | 1709 |
| 14 | LXJ | 1677 |
| 15 | easyJet | 1475 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1390 |
| 18 | United Airlines | 1343 |
| 19 | QLK | 1320 |
| 20 | EJU | 1305 |
| 21 | Alaska Airlines | 1304 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1170 |
| 24 | GLO | 1152 |
| 25 | PGT | 1150 |
| 26 | Air France | 1148 |
| 27 | WMT | 1093 |
| 28 | JetBlue | 1081 |
| 29 | AEE | 1072 |
| 30 | Wizz Air | 1059 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179569 |
| 2 | 🇪🇸 ES | 13625 |
| 3 | 🇧🇷 BR | 12211 |
| 4 | 🇦🇺 AU | 11962 |
| 5 | 🇨🇦 CA | 11745 |
| 6 | 🇮🇳 IN | 11345 |
| 7 | 🇮🇹 IT | 11189 |
| 8 | 🇩🇪 DE | 10514 |
| 9 | 🇬🇧 GB | 9921 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8590 |
| 12 | 🇫🇷 FR | 8453 |
| 13 | 🇬🇷 GR | 6224 |
| 14 | 🇹🇷 TR | 6098 |
| 15 | 🇲🇽 MX | 5955 |
| 16 | 🇨🇭 CH | 5646 |
| 17 | 🇳🇴 NO | 5297 |
| 18 | 🇲🇾 MY | 3673 |
| 19 | 🇿🇦 ZA | 3596 |
| 20 | 🇵🇱 PL | 3510 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2721 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2312 |
| 27 | 🇲🇦 MA | 2142 |
| 28 | 🇳🇱 NL | 1898 |
| 29 | 🇲🇪 ME | 1831 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4465 |
| 2 | Denver International Airport |  | US | 3467 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2590 |
| 5 | Guaymaral Airport |  | CO | 2543 |
| 6 | Harry Reid International Airport |  | US | 2380 |
| 7 | Zurich Airport |  | CH | 2219 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2190 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2189 |
| 10 | La Aurora Airport |  | GT | 2068 |
| 11 | El Dorado International Airport |  | CO | 1964 |
| 12 | Chicago O'Hare International Airport |  | US | 1963 |
| 13 | Salt Lake City International Airport |  | US | 1877 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1876 |
| 15 | Congonhas Airport |  | BR | 1780 |
| 16 | Frankfurt am Main International Airport |  | DE | 1737 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1604 |
| 19 | Capua Airport |  | IT | 1601 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1599 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1556 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1476 |
| 25 | Charles de Gaulle International Airport |  | FR | 1464 |
| 26 | Charlotte/Douglas International Airport |  | US | 1431 |
| 27 | Kuala Lumpur International Airport |  | MY | 1354 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1309 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1288 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1235 |
| 35 | Calgary International Airport |  | CA | 1203 |
| 36 | Oslo Gardermoen Airport |  | NO | 1177 |
| 37 | Vitoria/Foronda Airport |  | ES | 1172 |
| 38 | Reno/Tahoe International Airport |  | US | 1155 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1148 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1041 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 755 | 21m | 244 km | 3,179.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 444 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 312 | 1h 49m | 1,423 km | 7,657.0 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 311 | 44m | 241 km | 1,291.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 279 | 21m | 250 km | 1,205.1 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 252 | 1h 14m | 961 km | 4,177.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 228 | 1h 49m | 1,304 km | 5,129.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N445DH |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-18 16:37 UTC | 2026-08-18 17:04 UTC | 26m |
| N432ER |  | Lake In The Hills Airport (K3CK) | Lake In The Hills Airport (K3CK) | 2026-08-18 15:34 UTC | 2026-08-18 17:04 UTC | 1h 30m |
| N28PK |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-08-18 16:38 UTC | 2026-08-18 16:58 UTC | 20m |
| N733BK |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-08-18 16:37 UTC | 2026-08-18 16:51 UTC | 14m |
| N748CB |  | Trenton Mercer Airport (KTTN) | Mar Bar L Farms Airport (NJ46) | 2026-08-18 16:21 UTC | 2026-08-18 16:44 UTC | 23m |
| N36800 |  | Baggett Airport (FD57) | Space Coast Regional Airport (KTIX) | 2026-08-18 15:51 UTC | 2026-08-18 16:44 UTC | 52m |
| FIRE04 | FIR | Vila Real Airport (LPVR) | Viseu Airport (LPVZ) | 2026-08-18 16:29 UTC | 2026-08-18 16:42 UTC | 13m |
| UAE112 | Emirates | Budapest Ferenc Liszt International Airport (LHBP) | Queen Alia International Airport (OJAI) | 2026-08-18 14:00 UTC | 2026-08-18 16:41 UTC | 2h 40m |
| N122JM |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-18 16:02 UTC | 2026-08-18 16:40 UTC | 38m |
| 4XCBD |  | Megiddo Airport (LLMG) | Ein Shemer Airfield (LLES) | 2026-08-18 16:05 UTC | 2026-08-18 16:37 UTC | 32m |
| LXJ429 | LXJ | General Edward Lawrence Logan International Airport (KBOS) | Orlando Executive Airport (KORL) | 2026-08-18 13:51 UTC | 2026-08-18 16:30 UTC | 2h 38m |
| BHL200B | BHL | Aberdeen Dyce Airport (EGPD) | Aberdeen Dyce Airport (EGPD) | 2026-08-18 15:48 UTC | 2026-08-18 16:29 UTC | 41m |
|  |  | Hanover County Municipal Airport (KOFP) | Hanover County Municipal Airport (KOFP) | 2026-08-18 16:29 UTC | 2026-08-18 16:29 UTC | 0m |
| N8365W |  | Donald P Miller Airport (KFZI) | Henry County Airport (K7W5) | 2026-08-18 16:06 UTC | 2026-08-18 16:29 UTC | 22m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-08-18 16:19 UTC | 2026-08-18 16:28 UTC | 8m |
| THNDR12 | THN | Camp Davis Mcolf Airport (14NC) | Camp Davis Mcolf Airport (14NC) | 2026-08-18 16:22 UTC | 2026-08-18 16:28 UTC | 5m |
| CFJKX | CFJ | Calgary / Springbank Airport (CYBW) | Arkayla Springs Airport (CKY8) | 2026-08-18 16:21 UTC | 2026-08-18 16:28 UTC | 6m |
| N310BF |  | Tacoma Narrows Airport (KTIW) | Bellingham International Airport (KBLI) | 2026-08-18 15:44 UTC | 2026-08-18 16:25 UTC | 41m |
| N511CR |  | Henderson Executive Airport (KHND) | Riverside Airport (KRAL) | 2026-08-18 15:39 UTC | 2026-08-18 16:25 UTC | 45m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-08-18 07:16 UTC | 2026-08-18 16:23 UTC | 9h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
