# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_01:51:32_UTC-green)

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

**Latest saved flight:** 2026-08-18 01:51:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 01:51:32 UTC

- **210,630** saved flights
- **67,000** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **210,630** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,532,334.8 tonnes** estimated CO2 emissions
- **146,802,018 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8328 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3577 |
| 5 | American Airlines | 3528 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2727 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1911 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1751 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1403 |
| 17 | AXM | 1365 |
| 18 | United Airlines | 1338 |
| 19 | QLK | 1300 |
| 20 | Alaska Airlines | 1296 |
| 21 | EJU | 1285 |
| 22 | All Nippon Airways | 1269 |
| 23 | VIV | 1162 |
| 24 | GLO | 1139 |
| 25 | Air France | 1133 |
| 26 | PGT | 1126 |
| 27 | JetBlue | 1078 |
| 28 | AEE | 1069 |
| 29 | WMT | 1067 |
| 30 | Wizz Air | 1044 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178701 |
| 2 | 🇪🇸 ES | 13454 |
| 3 | 🇧🇷 BR | 12093 |
| 4 | 🇦🇺 AU | 11809 |
| 5 | 🇨🇦 CA | 11674 |
| 6 | 🇮🇳 IN | 11162 |
| 7 | 🇮🇹 IT | 11001 |
| 8 | 🇩🇪 DE | 10377 |
| 9 | 🇬🇧 GB | 9816 |
| 10 | 🇯🇵 JP | 8669 |
| 11 | 🇨🇴 CO | 8466 |
| 12 | 🇫🇷 FR | 8352 |
| 13 | 🇬🇷 GR | 6182 |
| 14 | 🇹🇷 TR | 5997 |
| 15 | 🇲🇽 MX | 5917 |
| 16 | 🇨🇭 CH | 5585 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3601 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3476 |
| 21 | 🇹🇭 TH | 3364 |
| 22 | 🇳🇿 NZ | 2914 |
| 23 | 🇵🇭 PH | 2790 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2561 |
| 26 | 🇭🇷 HR | 2262 |
| 27 | 🇲🇦 MA | 2122 |
| 28 | 🇳🇱 NL | 1874 |
| 29 | 🇲🇪 ME | 1791 |
| 30 | 🇮🇩 ID | 1729 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4444 |
| 2 | Denver International Airport |  | US | 3456 |
| 3 | Tokyo International Airport |  | JP | 2604 |
| 4 | Indira Gandhi International Airport |  | IN | 2540 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2371 |
| 7 | Zurich Airport |  | CH | 2190 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1955 |
| 12 | El Dorado International Airport |  | CO | 1932 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1871 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1723 |
| 17 | Madrid Barajas International Airport |  | ES | 1644 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1598 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1593 |
| 20 | Capua Airport |  | IT | 1584 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1476 |
| 24 | Malpensa International Airport |  | IT | 1456 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1425 |
| 27 | Kuala Lumpur International Airport |  | MY | 1329 |
| 28 | Ninoy Aquino International Airport |  | PH | 1322 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1303 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1280 |
| 32 | Barcelona International Airport |  | ES | 1262 |
| 33 | Seattle-Tacoma International Airport |  | US | 1258 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1198 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1134 |
| 40 | Daniel K Inouye International Airport |  | US | 1119 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 745 | 21m | 244 km | 3,137.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 516 | 1h 7m | 770 km | 6,854.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 488 | 24m | 225 km | 1,893.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 251 | 1h 37m | 1,156 km | 5,007.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 240 | 31m | 369 km | 1,527.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1018B |  | Drift River Airport (3AK5) | Johnson Airport (3AK4) | 2026-08-18 01:25 UTC | 2026-08-18 01:51 UTC | 25m |
| N1078U |  | Pittsburgh/Butler Regional Airport (KBTP) | Lorain County Regional Airport (KLPR) | 2026-08-18 00:58 UTC | 2026-08-18 01:49 UTC | 51m |
| N111WH |  | Lafayette Regional/Paul Fournet Field (KLFT) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-18 01:26 UTC | 2026-08-18 01:46 UTC | 20m |
| N546SL |  | San Rafael Airport (CA35) | Truckee-Tahoe Airport (KTRK) | 2026-08-18 00:54 UTC | 2026-08-18 01:25 UTC | 30m |
| IY25 |  | Cheongju International Airport (RKTU) | G 419 Airport (RK48) | 2026-08-18 00:53 UTC | 2026-08-18 01:20 UTC | 26m |
| N40ER |  | Savannah/Hilton Head International Airport (KSAV) | 9GA2 (9GA2) | 2026-08-18 00:56 UTC | 2026-08-18 01:17 UTC | 21m |
| TKR16 | TKR | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-08-18 01:08 UTC | 2026-08-18 01:15 UTC | 7m |
| CLX1081 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-08-17 14:33 UTC | 2026-08-18 01:13 UTC | 10h 40m |
| N3744Y |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-18 00:32 UTC | 2026-08-18 01:11 UTC | 39m |
| N95HT |  | Orlando International Airport (KMCO) | Orlando International Airport (KMCO) | 2026-08-18 00:29 UTC | 2026-08-18 01:07 UTC | 38m |
| TKR105 | TKR | NV17 (NV17) | Samsarg Field (KN58) | 2026-08-18 00:59 UTC | 2026-08-18 01:05 UTC | 6m |
| UAV16 | UAV | CL13 (CL13) | CL13 (CL13) | 2026-08-18 00:53 UTC | 2026-08-18 01:05 UTC | 11m |
| UAL921 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-08-17 17:18 UTC | 2026-08-18 01:04 UTC | 7h 46m |
| TKR912 | TKR | Albuquerque International Sunport Airport (KABQ) | Runway Bay Airport (NM61) | 2026-08-18 00:55 UTC | 2026-08-18 01:01 UTC | 5m |
| N989PA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-18 00:41 UTC | 2026-08-18 01:00 UTC | 19m |
| TRP1 | TRP | Phillips Army Air Field (Aberdeen Proving Ground) Airport (KAPG) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-08-18 00:28 UTC | 2026-08-18 00:59 UTC | 31m |
| ORS | ORS | Canberra International Airport (YSCB) | Canberra International Airport (YSCB) | 2026-08-18 00:46 UTC | 2026-08-18 00:58 UTC | 11m |
| AIQ3070 | AIQ | Chiang Mai International Airport (VTCC) | Surat Thani Airport (VTSB) | 2026-08-17 23:36 UTC | 2026-08-18 00:56 UTC | 1h 20m |
| N71MB |  | San Francisco International Airport (KSFO) | Rocky Mountain Metro Airport (KBJC) | 2026-08-17 22:43 UTC | 2026-08-18 00:56 UTC | 2h 12m |
| N5620B |  | Minden-Tahoe Airport (KMEV) | Minden-Tahoe Airport (KMEV) | 2026-08-18 00:34 UTC | 2026-08-18 00:55 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
