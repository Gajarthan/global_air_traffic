# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_19:45:54_UTC-green)

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

**Latest saved flight:** 2026-08-30 19:45:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-30 19:45:54 UTC

- **242,117** saved flights
- **73,384** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **242,117** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,914,428.5 tonnes** estimated CO2 emissions
- **168,952,379 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9714 |
| 2 | SkyWest Airlines | 8493 |
| 3 | EJA | 4679 |
| 4 | IndiGo | 4076 |
| 5 | American Airlines | 3898 |
| 6 | Southwest Airlines | 3637 |
| 7 | Delta Air Lines | 3086 |
| 8 | ENY | 2918 |
| 9 | LATAM Airlines | 2317 |
| 10 | AZU | 2246 |
| 11 | Vueling | 2080 |
| 12 | Lufthansa | 1947 |
| 13 | WIF | 1921 |
| 14 | LXJ | 1875 |
| 15 | easyJet | 1689 |
| 16 | Swiss International | 1636 |
| 17 | AXM | 1599 |
| 18 | EJU | 1550 |
| 19 | QLK | 1544 |
| 20 | United Airlines | 1522 |
| 21 | Alaska Airlines | 1445 |
| 22 | All Nippon Airways | 1431 |
| 23 | WMT | 1364 |
| 24 | GLO | 1350 |
| 25 | VIV | 1327 |
| 26 | PGT | 1325 |
| 27 | Air France | 1323 |
| 28 | Wizz Air | 1311 |
| 29 | AEE | 1198 |
| 30 | JetBlue | 1197 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 200615 |
| 2 | 🇪🇸 ES | 15576 |
| 3 | 🇧🇷 BR | 14095 |
| 4 | 🇦🇺 AU | 13712 |
| 5 | 🇨🇦 CA | 13462 |
| 6 | 🇮🇹 IT | 13259 |
| 7 | 🇮🇳 IN | 12690 |
| 8 | 🇩🇪 DE | 11953 |
| 9 | 🇬🇧 GB | 11430 |
| 10 | 🇨🇴 CO | 10433 |
| 11 | 🇫🇷 FR | 9762 |
| 12 | 🇯🇵 JP | 9702 |
| 13 | 🇹🇷 TR | 7185 |
| 14 | 🇬🇷 GR | 7140 |
| 15 | 🇲🇽 MX | 6685 |
| 16 | 🇨🇭 CH | 6514 |
| 17 | 🇳🇴 NO | 5988 |
| 18 | 🇹🇭 TH | 4390 |
| 19 | 🇲🇾 MY | 4285 |
| 20 | 🇿🇦 ZA | 4225 |
| 21 | 🇵🇱 PL | 4066 |
| 22 | 🇳🇿 NZ | 3328 |
| 23 | 🇵🇭 PH | 3317 |
| 24 | 🇬🇹 GT | 3042 |
| 25 | 🇰🇷 KR | 2856 |
| 26 | 🇭🇷 HR | 2796 |
| 27 | 🇲🇦 MA | 2450 |
| 28 | 🇲🇪 ME | 2264 |
| 29 | 🇳🇱 NL | 2192 |
| 30 | 🇮🇩 ID | 2115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5001 |
| 2 | Denver International Airport |  | US | 3907 |
| 3 | Indira Gandhi International Airport |  | IN | 2956 |
| 4 | Tokyo International Airport |  | JP | 2889 |
| 5 | Guaymaral Airport |  | CO | 2705 |
| 6 | Harry Reid International Airport |  | US | 2571 |
| 7 | Zurich Airport |  | CH | 2548 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2477 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2413 |
| 10 | El Dorado International Airport |  | CO | 2362 |
| 11 | La Aurora Airport |  | GT | 2317 |
| 12 | Chicago O'Hare International Airport |  | US | 2149 |
| 13 | Salt Lake City International Airport |  | US | 2135 |
| 14 | Congonhas Airport |  | BR | 2060 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2004 |
| 16 | Frankfurt am Main International Airport |  | DE | 1918 |
| 17 | Capua Airport |  | IT | 1911 |
| 18 | Madrid Barajas International Airport |  | ES | 1905 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1816 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1782 |
| 21 | Malpensa International Airport |  | IT | 1732 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1710 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1697 |
| 24 | Charles de Gaulle International Airport |  | FR | 1694 |
| 25 | Macau International Airport |  | MO | 1616 |
| 26 | Ninoy Aquino International Airport |  | PH | 1611 |
| 27 | Charlotte/Douglas International Airport |  | US | 1549 |
| 28 | Kuala Lumpur International Airport |  | MY | 1546 |
| 29 | Enrique Olaya Herrera Airport |  | CO | 1545 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1465 |
| 32 | Viracopos International Airport |  | BR | 1437 |
| 33 | Seattle-Tacoma International Airport |  | US | 1414 |
| 34 | Don Mueang International Airport |  | TH | 1413 |
| 35 | Bengaluru International Airport |  | IN | 1408 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1405 |
| 37 | Calgary International Airport |  | CA | 1389 |
| 38 | Oslo Gardermoen Airport |  | NO | 1364 |
| 39 | Vancouver International Airport |  | CA | 1339 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1322 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1096 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 892 | 21m | 244 km | 3,756.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 624 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 615 | 24m | 225 km | 2,385.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 614 | 1h 6m | 770 km | 8,156.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 546 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 399 | 27m | 275 km | 1,890.7 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 382 | 1h 50m | 1,423 km | 9,374.9 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 370 | 44m | 555 km | 3,542.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 366 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 346 | 21m | 250 km | 1,494.5 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 332 | 24m | 218 km | 1,250.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 322 | 1h 40m | 1,156 km | 6,423.8 t |
| 15 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 320 | 22m | 55 km | 304.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 301 | 19m | 99 km | 515.6 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 295 | 26m | 215 km | 1,092.6 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 284 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 280 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 276 | 1h 14m | 961 km | 4,574.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 274 | 19m | 144 km | 681.6 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 264 | 15m | 154 km | 699.5 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 260 | 1h 50m | 1,304 km | 5,849.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 249 | 28m | 152 km | 650.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2231E |  | Sioux Gateway/Brig General Bud Day Field (KSUX) | Sioux Gateway/Brig General Bud Day Field (KSUX) | 2026-08-30 19:31 UTC | 2026-08-30 19:45 UTC | 14m |
| XSN06 | XSN | Montgomery-Gibbs Executive Airport (KMYF) | San Carlos Airport (KSQL) | 2026-08-30 18:10 UTC | 2026-08-30 19:43 UTC | 1h 32m |
| SWR42V | Swiss International | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-08-30 18:38 UTC | 2026-08-30 19:43 UTC | 1h 4m |
| HKC9632 | HKC | Chhatrapati Shivaji International Airport (VABB) | Zhuhai Airport (ZGSD) | 2026-08-30 14:20 UTC | 2026-08-30 19:40 UTC | 5h 20m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-30 17:50 UTC | 2026-08-30 19:40 UTC | 1h 49m |
| TKR804 | TKR | El Coyote Ranch Airport (2TA8) | Alice International Airport (KALI) | 2026-08-30 19:17 UTC | 2026-08-30 19:38 UTC | 21m |
| N690FD |  | Grand Canyon West Airport (K1G4) | Grand Canyon West Airport (K1G4) | 2026-08-30 19:10 UTC | 2026-08-30 19:34 UTC | 23m |
| N92SD |  | Ted Stevens Anchorage International Airport (PANC) | Carpentiers Strip (64AK) | 2026-08-30 18:30 UTC | 2026-08-30 19:26 UTC | 56m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-30 18:32 UTC | 2026-08-30 19:25 UTC | 52m |
| CAP2384 | CAP | Spirit Of St Louis Airport (KSUS) | KMO6 (KMO6) | 2026-08-30 18:34 UTC | 2026-08-30 19:21 UTC | 47m |
| SWR90A | Swiss International | Westerland Sylt Airport (EDXW) | Zurich Airport (LSZH) | 2026-08-30 17:56 UTC | 2026-08-30 19:19 UTC | 1h 22m |
| N120JW |  | Chicago Midway International Airport (KMDW) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-30 18:34 UTC | 2026-08-30 19:18 UTC | 44m |
| N555YS |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-30 18:43 UTC | 2026-08-30 19:16 UTC | 33m |
| N124RF |  | Portland-Hillsboro Airport (KHIO) | Crescent Lake State Airport (K5S2) | 2026-08-30 16:10 UTC | 2026-08-30 19:14 UTC | 3h 3m |
| N492LP |  | 99AZ (99AZ) | Glendale Regional Airport (KGEU) | 2026-08-30 18:11 UTC | 2026-08-30 19:14 UTC | 1h 2m |
| N6112V |  | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | Old Bridge Airport (K3N6) | 2026-08-30 14:34 UTC | 2026-08-30 19:14 UTC | 4h 40m |
| N413CK |  | Coyote Ridge Airport (17ID) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-30 17:50 UTC | 2026-08-30 19:11 UTC | 1h 21m |
| RJB201 | RJB | Paris-Le Bourget Airport (LFPB) | Liverpool John Lennon Airport (EGGP) | 2026-08-30 17:57 UTC | 2026-08-30 19:09 UTC | 1h 12m |
| N113RF |  | Coyote Ridge Airport (17ID) | Coyote Ridge Airport (17ID) | 2026-08-30 18:49 UTC | 2026-08-30 19:09 UTC | 19m |
| N2725N |  | Dane County Regional/Truax Field (KMSN) | Springstead Airport (WS06) | 2026-08-30 18:26 UTC | 2026-08-30 19:08 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
