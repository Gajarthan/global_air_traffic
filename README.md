# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_19:42:56_UTC-green)

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

**Latest saved flight:** 2026-08-18 19:42:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 19:42:56 UTC

- **213,228** saved flights
- **67,477** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **213,228** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,564,059.5 tonnes** estimated CO2 emissions
- **148,641,130 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8460 |
| 2 | SkyWest Airlines | 7643 |
| 3 | EJA | 4153 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3558 |
| 6 | Southwest Airlines | 3401 |
| 7 | Delta Air Lines | 2751 |
| 8 | ENY | 2648 |
| 9 | LATAM Airlines | 2008 |
| 10 | AZU | 1944 |
| 11 | Lufthansa | 1784 |
| 12 | Vueling | 1782 |
| 13 | WIF | 1712 |
| 14 | LXJ | 1682 |
| 15 | easyJet | 1480 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1349 |
| 19 | QLK | 1320 |
| 20 | EJU | 1314 |
| 21 | Alaska Airlines | 1307 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1175 |
| 24 | GLO | 1156 |
| 25 | PGT | 1154 |
| 26 | Air France | 1153 |
| 27 | WMT | 1099 |
| 28 | JetBlue | 1086 |
| 29 | AEE | 1078 |
| 30 | Wizz Air | 1066 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 180181 |
| 2 | 🇪🇸 ES | 13651 |
| 3 | 🇧🇷 BR | 12254 |
| 4 | 🇦🇺 AU | 11966 |
| 5 | 🇨🇦 CA | 11766 |
| 6 | 🇮🇳 IN | 11356 |
| 7 | 🇮🇹 IT | 11243 |
| 8 | 🇩🇪 DE | 10534 |
| 9 | 🇬🇧 GB | 9946 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8643 |
| 12 | 🇫🇷 FR | 8475 |
| 13 | 🇬🇷 GR | 6252 |
| 14 | 🇹🇷 TR | 6120 |
| 15 | 🇲🇽 MX | 5979 |
| 16 | 🇨🇭 CH | 5653 |
| 17 | 🇳🇴 NO | 5308 |
| 18 | 🇲🇾 MY | 3675 |
| 19 | 🇿🇦 ZA | 3606 |
| 20 | 🇵🇱 PL | 3519 |
| 21 | 🇹🇭 TH | 3450 |
| 22 | 🇳🇿 NZ | 2947 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2724 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2322 |
| 27 | 🇲🇦 MA | 2150 |
| 28 | 🇳🇱 NL | 1902 |
| 29 | 🇲🇪 ME | 1842 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4482 |
| 2 | Denver International Airport |  | US | 3479 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2554 |
| 6 | Harry Reid International Airport |  | US | 2383 |
| 7 | Zurich Airport |  | CH | 2222 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2198 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2197 |
| 10 | La Aurora Airport |  | GT | 2071 |
| 11 | El Dorado International Airport |  | CO | 1969 |
| 12 | Chicago O'Hare International Airport |  | US | 1969 |
| 13 | Salt Lake City International Airport |  | US | 1889 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1880 |
| 15 | Congonhas Airport |  | BR | 1784 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Capua Airport |  | IT | 1614 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1610 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1602 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1559 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1487 |
| 25 | Charles de Gaulle International Airport |  | FR | 1470 |
| 26 | Charlotte/Douglas International Airport |  | US | 1437 |
| 27 | Kuala Lumpur International Airport |  | MY | 1356 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1313 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1294 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1283 |
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
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 759 | 21m | 244 km | 3,195.9 t |
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
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 239 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 229 | 1h 49m | 1,304 km | 5,151.9 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N291HW |  | Republic Airport (KFRG) | Bridgeport/Sikorsky Airport (KBDR) | 2026-08-18 19:15 UTC | 2026-08-18 19:42 UTC | 27m |
| N739ZG |  | Flying Cloud Airport (KFCM) | Hutchinson Municipal/Butler Field (KHCD) | 2026-08-18 18:42 UTC | 2026-08-18 19:41 UTC | 58m |
| WMU74 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Kirsch Municipal Airport (KIRS) | 2026-08-18 19:08 UTC | 2026-08-18 19:41 UTC | 33m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-08-18 19:20 UTC | 2026-08-18 19:36 UTC | 16m |
| THY8CD | Turkish Airlines | Antalya International Airport (LTAI) | Białystok-Krywlany Airport (EPBK) | 2026-08-18 17:04 UTC | 2026-08-18 19:36 UTC | 2h 31m |
| DHX729 | DHX | Bahrain International Airport (OBBI) | Zhuhai Airport (ZGSD) | 2026-08-18 11:19 UTC | 2026-08-18 19:35 UTC | 8h 16m |
| QTR8438 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-18 11:44 UTC | 2026-08-18 19:29 UTC | 7h 45m |
| N62494 |  | Portland-Hillsboro Airport (KHIO) | Chamberlain Airport (OR60) | 2026-08-18 17:28 UTC | 2026-08-18 19:29 UTC | 2h 1m |
| N4438T |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-18 18:57 UTC | 2026-08-18 19:29 UTC | 31m |
| N733MX |  | Medina Municipal Airport (K1G5) | Medina Municipal Airport (K1G5) | 2026-08-18 18:44 UTC | 2026-08-18 19:28 UTC | 44m |
| AEZ839Y | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-18 18:43 UTC | 2026-08-18 19:28 UTC | 45m |
| MSR888 | EgyptAir | HE30 (HE30) | Hulwan (HE15) | 2026-08-18 19:02 UTC | 2026-08-18 19:27 UTC | 25m |
| N733BK |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-18 19:15 UTC | 2026-08-18 19:27 UTC | 12m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-18 18:55 UTC | 2026-08-18 19:26 UTC | 31m |
| N96705 |  | Neversweat Airport (1OK0) | Shawnee Regional Airport (KSNL) | 2026-08-18 18:45 UTC | 2026-08-18 19:26 UTC | 41m |
| TAUNT11 | TAU | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-08-18 19:07 UTC | 2026-08-18 19:23 UTC | 16m |
| CPA3295 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-08-18 04:32 UTC | 2026-08-18 19:21 UTC | 14h 49m |
| N456RR |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-08-18 18:46 UTC | 2026-08-18 19:21 UTC | 35m |
| N733PN |  | Northeast Philadelphia Airport (KPNE) | Wings Field (KLOM) | 2026-08-18 18:37 UTC | 2026-08-18 19:21 UTC | 44m |
| N748CB |  | Trenton Mercer Airport (KTTN) | Mar Bar L Farms Airport (NJ46) | 2026-08-18 19:06 UTC | 2026-08-18 19:18 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
