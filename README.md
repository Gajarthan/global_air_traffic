# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_23:39:33_UTC-green)

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

**Latest saved flight:** 2026-08-17 23:39:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 23:39:33 UTC

- **210,428** saved flights
- **66,959** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **210,428** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,529,903.6 tonnes** estimated CO2 emissions
- **146,661,079 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8328 |
| 2 | SkyWest Airlines | 7586 |
| 3 | EJA | 4108 |
| 4 | IndiGo | 3577 |
| 5 | American Airlines | 3523 |
| 6 | Southwest Airlines | 3381 |
| 7 | Delta Air Lines | 2723 |
| 8 | ENY | 2623 |
| 9 | LATAM Airlines | 1986 |
| 10 | AZU | 1911 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1751 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1667 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1403 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1336 |
| 19 | QLK | 1295 |
| 20 | Alaska Airlines | 1294 |
| 21 | EJU | 1285 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1160 |
| 24 | GLO | 1139 |
| 25 | Air France | 1133 |
| 26 | PGT | 1124 |
| 27 | JetBlue | 1077 |
| 28 | AEE | 1069 |
| 29 | WMT | 1067 |
| 30 | Wizz Air | 1044 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178489 |
| 2 | 🇪🇸 ES | 13454 |
| 3 | 🇧🇷 BR | 12090 |
| 4 | 🇦🇺 AU | 11773 |
| 5 | 🇨🇦 CA | 11648 |
| 6 | 🇮🇳 IN | 11162 |
| 7 | 🇮🇹 IT | 11001 |
| 8 | 🇩🇪 DE | 10377 |
| 9 | 🇬🇧 GB | 9814 |
| 10 | 🇯🇵 JP | 8647 |
| 11 | 🇨🇴 CO | 8457 |
| 12 | 🇫🇷 FR | 8352 |
| 13 | 🇬🇷 GR | 6181 |
| 14 | 🇹🇷 TR | 5993 |
| 15 | 🇲🇽 MX | 5914 |
| 16 | 🇨🇭 CH | 5585 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3476 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2909 |
| 23 | 🇵🇭 PH | 2784 |
| 24 | 🇬🇹 GT | 2701 |
| 25 | 🇰🇷 KR | 2548 |
| 26 | 🇭🇷 HR | 2262 |
| 27 | 🇲🇦 MA | 2122 |
| 28 | 🇳🇱 NL | 1873 |
| 29 | 🇲🇪 ME | 1791 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4437 |
| 2 | Denver International Airport |  | US | 3445 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2540 |
| 5 | Guaymaral Airport |  | CO | 2530 |
| 6 | Harry Reid International Airport |  | US | 2368 |
| 7 | Zurich Airport |  | CH | 2190 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2182 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 10 | La Aurora Airport |  | GT | 2055 |
| 11 | Chicago O'Hare International Airport |  | US | 1954 |
| 12 | El Dorado International Airport |  | CO | 1928 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1873 |
| 14 | Salt Lake City International Airport |  | US | 1867 |
| 15 | Congonhas Airport |  | BR | 1758 |
| 16 | Frankfurt am Main International Airport |  | DE | 1723 |
| 17 | Madrid Barajas International Airport |  | ES | 1644 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1597 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1592 |
| 20 | Capua Airport |  | IT | 1584 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1470 |
| 24 | Malpensa International Airport |  | IT | 1456 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1425 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1319 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1302 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1278 |
| 32 | Barcelona International Airport |  | ES | 1262 |
| 33 | Seattle-Tacoma International Airport |  | US | 1255 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1195 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1149 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1133 |
| 40 | Daniel K Inouye International Airport |  | US | 1117 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 743 | 21m | 244 km | 3,128.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
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
| N108SC |  | Charles M Schulz/Sonoma County Airport (KSTS) | CA57 (CA57) | 2026-08-17 23:18 UTC | 2026-08-17 23:39 UTC | 21m |
| N7614Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-17 22:56 UTC | 2026-08-17 23:36 UTC | 39m |
| TEX08 | TEX | RNZAF Base Ohakea (NZOH) | RNZAF Base Ohakea (NZOH) | 2026-08-17 22:46 UTC | 2026-08-17 23:30 UTC | 44m |
| N719KF |  | Old Aerodrome (9CL7) | Sacramento International Airport (KSMF) | 2026-08-17 22:51 UTC | 2026-08-17 23:19 UTC | 28m |
| N9176H |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-17 22:22 UTC | 2026-08-17 23:16 UTC | 54m |
| AAL1482 | American Airlines | Harry Reid International Airport (KLAS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-17 21:04 UTC | 2026-08-17 23:13 UTC | 2h 9m |
| EPI271 | EPI | Nuggs Flying M Airport (TE68) | 11TX (11TX) | 2026-08-17 22:47 UTC | 2026-08-17 23:12 UTC | 25m |
| N4958A |  | Montgomery-Gibbs Executive Airport (KMYF) | Santa Monica Municipal Airport (KSMO) | 2026-08-17 21:58 UTC | 2026-08-17 23:11 UTC | 1h 13m |
| SPTN978 | SPT | CA53 (CA53) | Redding Regional Airport (KRDD) | 2026-08-17 22:58 UTC | 2026-08-17 23:10 UTC | 11m |
| N7288W |  | Independence State Airport (K7S5) | Independence State Airport (K7S5) | 2026-08-17 22:43 UTC | 2026-08-17 23:10 UTC | 26m |
| WGTL04 | WGT | Newcastle Airport (YWLM) | Hervey Bay Airport (YHBA) | 2026-08-17 21:58 UTC | 2026-08-17 23:08 UTC | 1h 10m |
| N5050M |  | Boca Raton Airport (KBCT) | Orlando Executive Airport (KORL) | 2026-08-17 21:59 UTC | 2026-08-17 23:06 UTC | 1h 6m |
| JCY504 | JCY | Roche Harbor Airport (WA09) | Boeing Field/King County International Airport (KBFI) | 2026-08-17 22:39 UTC | 2026-08-17 23:04 UTC | 25m |
| N9250C |  | Lansing Municipal Airport (KIGQ) | Lansing Municipal Airport (KIGQ) | 2026-08-17 23:01 UTC | 2026-08-17 23:02 UTC | 0m |
| N9182M |  | Rogue Valley International/Medford Airport (KMFR) | Ashland Municipal/Sumner Parker Field (KS03) | 2026-08-17 22:44 UTC | 2026-08-17 23:01 UTC | 17m |
| N315ME |  | Toledo Executive Airport (KTDZ) | Toledo Executive Airport (KTDZ) | 2026-08-17 22:43 UTC | 2026-08-17 22:58 UTC | 14m |
| ARCAS03 | ARC | Danaher Airport (7TX0) | Rafter P Airport (TA00) | 2026-08-17 22:34 UTC | 2026-08-17 22:57 UTC | 22m |
| CNS47 | CNS | Sierraville Dearwater Airport (KO79) | San Francisco International Airport (KSFO) | 2026-08-17 22:09 UTC | 2026-08-17 22:57 UTC | 47m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-17 22:19 UTC | 2026-08-17 22:57 UTC | 37m |
|  |  | Vancouver International Airport (CYVR) | Alert Bay Airport (CYAL) | 2026-08-17 22:15 UTC | 2026-08-17 22:56 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
