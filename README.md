# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_19:21:59_UTC-green)

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

**Latest saved flight:** 2026-08-18 19:21:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 19:21:59 UTC

- **213,157** saved flights
- **67,461** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,157** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,563,070.2 tonnes** estimated CO2 emissions
- **148,583,780 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8457 |
| 2 | SkyWest Airlines | 7638 |
| 3 | EJA | 4151 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3557 |
| 6 | Southwest Airlines | 3401 |
| 7 | Delta Air Lines | 2749 |
| 8 | ENY | 2647 |
| 9 | LATAM Airlines | 2007 |
| 10 | AZU | 1944 |
| 11 | Lufthansa | 1784 |
| 12 | Vueling | 1781 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1681 |
| 15 | easyJet | 1480 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1347 |
| 19 | QLK | 1320 |
| 20 | EJU | 1314 |
| 21 | Alaska Airlines | 1306 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1175 |
| 24 | GLO | 1156 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1098 |
| 28 | JetBlue | 1086 |
| 29 | AEE | 1078 |
| 30 | Wizz Air | 1064 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180102 |
| 2 | 🇪🇸 ES | 13648 |
| 3 | 🇧🇷 BR | 12250 |
| 4 | 🇦🇺 AU | 11966 |
| 5 | 🇨🇦 CA | 11764 |
| 6 | 🇮🇳 IN | 11356 |
| 7 | 🇮🇹 IT | 11235 |
| 8 | 🇩🇪 DE | 10534 |
| 9 | 🇬🇧 GB | 9943 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8639 |
| 12 | 🇫🇷 FR | 8475 |
| 13 | 🇬🇷 GR | 6248 |
| 14 | 🇹🇷 TR | 6118 |
| 15 | 🇲🇽 MX | 5979 |
| 16 | 🇨🇭 CH | 5651 |
| 17 | 🇳🇴 NO | 5308 |
| 18 | 🇲🇾 MY | 3675 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3518 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2947 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2724 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2321 |
| 27 | 🇲🇦 MA | 2150 |
| 28 | 🇳🇱 NL | 1902 |
| 29 | 🇲🇪 ME | 1842 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4481 |
| 2 | Denver International Airport |  | US | 3475 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2554 |
| 6 | Harry Reid International Airport |  | US | 2382 |
| 7 | Zurich Airport |  | CH | 2221 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2197 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2196 |
| 10 | La Aurora Airport |  | GT | 2071 |
| 11 | Chicago O'Hare International Airport |  | US | 1969 |
| 12 | El Dorado International Airport |  | CO | 1968 |
| 13 | Salt Lake City International Airport |  | US | 1886 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1879 |
| 15 | Congonhas Airport |  | BR | 1784 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Capua Airport |  | IT | 1612 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1610 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1602 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1558 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1485 |
| 25 | Charles de Gaulle International Airport |  | FR | 1470 |
| 26 | Charlotte/Douglas International Airport |  | US | 1437 |
| 27 | Kuala Lumpur International Airport |  | MY | 1356 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1313 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1293 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1264 |
| 34 | Viracopos International Airport |  | BR | 1244 |
| 35 | Calgary International Airport |  | CA | 1204 |
| 36 | Oslo Gardermoen Airport |  | NO | 1181 |
| 37 | Vitoria/Foronda Airport |  | ES | 1175 |
| 38 | Reno/Tahoe International Airport |  | US | 1158 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1151 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1045 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 758 | 21m | 244 km | 3,191.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 450 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 312 | 44m | 241 km | 1,296.0 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 281 | 21m | 250 km | 1,213.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 252 | 1h 14m | 961 km | 4,177.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 250 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 229 | 1h 49m | 1,304 km | 5,151.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA3295 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-08-18 04:32 UTC | 2026-08-18 19:21 UTC | 14h 49m |
| N456RR |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-08-18 18:46 UTC | 2026-08-18 19:21 UTC | 35m |
| N733PN |  | Northeast Philadelphia Airport (KPNE) | Wings Field (KLOM) | 2026-08-18 18:37 UTC | 2026-08-18 19:21 UTC | 44m |
| XBKMJ | XBK | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | General Mariano Matamoros Airport (MMCB) | 2026-08-18 19:00 UTC | 2026-08-18 19:12 UTC | 11m |
| N840FA |  | Aurora State Airport (KUAO) | Portland-Hillsboro Airport (KHIO) | 2026-08-18 18:56 UTC | 2026-08-18 19:10 UTC | 14m |
| N137AL |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Joplin Regional Airport (KJLN) | 2026-08-18 18:36 UTC | 2026-08-18 19:10 UTC | 33m |
| N1NP |  | Kearney Regional Airport (KEAR) | Lincoln Airport (KLNK) | 2026-08-18 18:45 UTC | 2026-08-18 19:09 UTC | 24m |
| N234FF |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-18 18:37 UTC | 2026-08-18 19:08 UTC | 31m |
| ASI670 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-08-18 18:32 UTC | 2026-08-18 19:07 UTC | 35m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-08-18 18:46 UTC | 2026-08-18 19:00 UTC | 14m |
| N1544E |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-18 18:35 UTC | 2026-08-18 18:59 UTC | 24m |
| ES803 |  | Johnsen Airport (4CA7) | Sacramento Mather Airport (KMHR) | 2026-08-18 17:56 UTC | 2026-08-18 18:58 UTC | 1h 2m |
| N8397L |  | UT99 (UT99) | Wendover Airport (KENV) | 2026-08-18 17:54 UTC | 2026-08-18 18:57 UTC | 1h 3m |
| N98485 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Palo Alto Airport (KPAO) | 2026-08-18 18:43 UTC | 2026-08-18 18:57 UTC | 14m |
| HK3773 |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-08-18 18:38 UTC | 2026-08-18 18:56 UTC | 18m |
| MAKO44 | MAK | Baker & Hall Airport (77CL) | Baker & Hall Airport (77CL) | 2026-08-18 18:42 UTC | 2026-08-18 18:55 UTC | 13m |
| FTO381 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-18 18:28 UTC | 2026-08-18 18:54 UTC | 26m |
| N171EX |  | Flagstaff Pulliam Airport (KFLG) | Cedar City Regional Airport (KCDC) | 2026-08-18 18:20 UTC | 2026-08-18 18:53 UTC | 33m |
| N510PK |  | Lake Havasu City Airport (KHII) | Kingman Airport (KIGM) | 2026-08-18 18:43 UTC | 2026-08-18 18:52 UTC | 8m |
| N732FJ |  | South Jersey Regional Airport (KVAY) | Central Jersey Regional Airport (K47N) | 2026-08-18 18:34 UTC | 2026-08-18 18:51 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
