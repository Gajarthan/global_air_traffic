# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_21:59:21_UTC-green)

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

**Latest saved flight:** 2026-08-24 21:59:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 21:59:21 UTC

- **233,558** saved flights
- **71,721** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,558** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,814,925.1 tonnes** estimated CO2 emissions
- **163,184,067 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9379 |
| 2 | SkyWest Airlines | 8275 |
| 3 | EJA | 4542 |
| 4 | IndiGo | 3943 |
| 5 | American Airlines | 3812 |
| 6 | Southwest Airlines | 3591 |
| 7 | Delta Air Lines | 2982 |
| 8 | ENY | 2846 |
| 9 | LATAM Airlines | 2245 |
| 10 | AZU | 2176 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1842 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1551 |
| 18 | EJU | 1495 |
| 19 | United Airlines | 1481 |
| 20 | QLK | 1475 |
| 21 | Alaska Airlines | 1405 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1302 |
| 24 | WMT | 1297 |
| 25 | VIV | 1285 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1161 |
| 30 | JetBlue | 1161 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194539 |
| 2 | 🇪🇸 ES | 15001 |
| 3 | 🇧🇷 BR | 13648 |
| 4 | 🇦🇺 AU | 13168 |
| 5 | 🇨🇦 CA | 12902 |
| 6 | 🇮🇹 IT | 12704 |
| 7 | 🇮🇳 IN | 12281 |
| 8 | 🇩🇪 DE | 11507 |
| 9 | 🇬🇧 GB | 11008 |
| 10 | 🇨🇴 CO | 9798 |
| 11 | 🇯🇵 JP | 9448 |
| 12 | 🇫🇷 FR | 9342 |
| 13 | 🇹🇷 TR | 6920 |
| 14 | 🇬🇷 GR | 6870 |
| 15 | 🇲🇽 MX | 6486 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4144 |
| 19 | 🇹🇭 TH | 4108 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3891 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3187 |
| 24 | 🇬🇹 GT | 2929 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2371 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4862 |
| 2 | Denver International Airport |  | US | 3790 |
| 3 | Indira Gandhi International Airport |  | IN | 2844 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2507 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2389 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2342 |
| 10 | La Aurora Airport |  | GT | 2232 |
| 11 | El Dorado International Airport |  | CO | 2181 |
| 12 | Chicago O'Hare International Airport |  | US | 2113 |
| 13 | Salt Lake City International Airport |  | US | 2060 |
| 14 | Congonhas Airport |  | BR | 1993 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1968 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1756 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1728 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1663 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1621 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1536 |
| 27 | Charlotte/Douglas International Airport |  | US | 1514 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1437 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1412 |
| 32 | Viracopos International Airport |  | BR | 1390 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1373 |
| 34 | Bengaluru International Airport |  | IN | 1372 |
| 35 | Seattle-Tacoma International Airport |  | US | 1369 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1333 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1271 |
| 40 | Vitoria/Foronda Airport |  | ES | 1266 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 852 | 21m | 244 km | 3,587.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 582 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 522 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 309 | 24m | 218 km | 1,164.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 306 | 1h 38m | 1,156 km | 6,104.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 250 | 1h 50m | 1,304 km | 5,624.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3921Q |  | Fletcher Field (2MO0) | Miami County Airport (KK81) | 2026-08-24 21:29 UTC | 2026-08-24 21:59 UTC | 29m |
| N945RF |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-24 21:38 UTC | 2026-08-24 21:50 UTC | 12m |
| 1881 |  | Cildir Airport (LTBD) | Cildir Airport (LTBD) | 2026-08-24 20:43 UTC | 2026-08-24 21:43 UTC | 1h 0m |
| TKR106 | TKR | Hill Afb Airport (KHIF) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 21:23 UTC | 2026-08-24 21:37 UTC | 14m |
| N2476Y |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-08-24 21:33 UTC | 2026-08-24 21:36 UTC | 2m |
| N1507X |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-08-24 20:51 UTC | 2026-08-24 21:32 UTC | 40m |
| LXJ435 | LXJ | Santa Barbara Municipal Airport (KSBA) | San Francisco International Airport (KSFO) | 2026-08-24 20:48 UTC | 2026-08-24 21:31 UTC | 42m |
| N980CT |  | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-08-24 21:30 UTC | 2026-08-24 21:30 UTC | 0m |
| N945RF |  | Essex County Airport (KCDW) | Newark Liberty International Airport (KEWR) | 2026-08-24 20:58 UTC | 2026-08-24 21:27 UTC | 29m |
| BT614 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-24 21:04 UTC | 2026-08-24 21:25 UTC | 21m |
| CXK651 | CXK | Camarillo Airport (KCMA) | Lompoc Airport (KLPC) | 2026-08-24 20:34 UTC | 2026-08-24 21:25 UTC | 51m |
| SFE2 | SFE | Danz Ranch Airport (XA02) | Bud Dryden Airport (TX05) | 2026-08-24 21:07 UTC | 2026-08-24 21:24 UTC | 16m |
| N522EE |  | Van Nuys Airport (KVNY) | Sacramento Mather Airport (KMHR) | 2026-08-24 20:35 UTC | 2026-08-24 21:22 UTC | 46m |
| N22TE |  | WN36 (WN36) | Shaniko Ranch Airport (9OR1) | 2026-08-24 19:12 UTC | 2026-08-24 21:21 UTC | 2h 9m |
| N968L |  | Lewis University Airport (KLOT) | Neiner Airport (19LL) | 2026-08-24 20:38 UTC | 2026-08-24 21:20 UTC | 41m |
| AATK309 | AAT | UT99 (UT99) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 20:47 UTC | 2026-08-24 21:19 UTC | 31m |
| N21585 |  | Harford County Airport (K0W3) | Millville Municipal Airport (KMIV) | 2026-08-24 20:45 UTC | 2026-08-24 21:18 UTC | 32m |
| N991AK |  | Merrill Field (PAMR) | Big Mountain Airport (PABM) | 2026-08-24 20:34 UTC | 2026-08-24 21:14 UTC | 39m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 21:02 UTC | 2026-08-24 21:11 UTC | 9m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-24 21:02 UTC | 2026-08-24 21:11 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
