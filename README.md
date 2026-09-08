# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_00:50:26_UTC-green)

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

**Latest saved flight:** 2026-09-08 00:50:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 00:50:26 UTC

- **251,172** saved flights
- **75,360** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,172** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,024,077.8 tonnes** estimated CO2 emissions
- **175,308,858 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10049 |
| 2 | SkyWest Airlines | 8786 |
| 3 | EJA | 4855 |
| 4 | IndiGo | 4199 |
| 5 | American Airlines | 4018 |
| 6 | Southwest Airlines | 3723 |
| 7 | Delta Air Lines | 3182 |
| 8 | ENY | 3001 |
| 9 | LATAM Airlines | 2419 |
| 10 | AZU | 2333 |
| 11 | Vueling | 2142 |
| 12 | WIF | 2011 |
| 13 | Lufthansa | 1987 |
| 14 | LXJ | 1962 |
| 15 | easyJet | 1728 |
| 16 | Swiss International | 1686 |
| 17 | AXM | 1628 |
| 18 | QLK | 1616 |
| 19 | EJU | 1613 |
| 20 | United Airlines | 1570 |
| 21 | Alaska Airlines | 1501 |
| 22 | All Nippon Airways | 1471 |
| 23 | WMT | 1423 |
| 24 | GLO | 1395 |
| 25 | PGT | 1379 |
| 26 | VIV | 1376 |
| 27 | Wizz Air | 1366 |
| 28 | Air France | 1365 |
| 29 | AEE | 1230 |
| 30 | JetBlue | 1230 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208421 |
| 2 | 🇪🇸 ES | 16053 |
| 3 | 🇧🇷 BR | 14639 |
| 4 | 🇦🇺 AU | 14279 |
| 5 | 🇨🇦 CA | 13940 |
| 6 | 🇮🇹 IT | 13754 |
| 7 | 🇮🇳 IN | 13105 |
| 8 | 🇩🇪 DE | 12329 |
| 9 | 🇬🇧 GB | 11770 |
| 10 | 🇨🇴 CO | 11061 |
| 11 | 🇫🇷 FR | 10105 |
| 12 | 🇯🇵 JP | 9888 |
| 13 | 🇹🇷 TR | 7506 |
| 14 | 🇬🇷 GR | 7377 |
| 15 | 🇲🇽 MX | 6941 |
| 16 | 🇨🇭 CH | 6764 |
| 17 | 🇳🇴 NO | 6218 |
| 18 | 🇹🇭 TH | 4512 |
| 19 | 🇲🇾 MY | 4372 |
| 20 | 🇿🇦 ZA | 4313 |
| 21 | 🇵🇱 PL | 4191 |
| 22 | 🇳🇿 NZ | 3426 |
| 23 | 🇵🇭 PH | 3408 |
| 24 | 🇬🇹 GT | 3137 |
| 25 | 🇰🇷 KR | 2902 |
| 26 | 🇭🇷 HR | 2885 |
| 27 | 🇲🇦 MA | 2537 |
| 28 | 🇲🇪 ME | 2363 |
| 29 | 🇳🇱 NL | 2267 |
| 30 | 🇮🇩 ID | 2147 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5189 |
| 2 | Denver International Airport |  | US | 4073 |
| 3 | Indira Gandhi International Airport |  | IN | 3053 |
| 4 | Tokyo International Airport |  | JP | 2952 |
| 5 | Guaymaral Airport |  | CO | 2740 |
| 6 | Harry Reid International Airport |  | US | 2672 |
| 7 | Zurich Airport |  | CH | 2628 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2550 |
| 9 | El Dorado International Airport |  | CO | 2550 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2483 |
| 11 | La Aurora Airport |  | GT | 2392 |
| 12 | Salt Lake City International Airport |  | US | 2225 |
| 13 | Chicago O'Hare International Airport |  | US | 2191 |
| 14 | Congonhas Airport |  | BR | 2150 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2070 |
| 16 | Capua Airport |  | IT | 1982 |
| 17 | Madrid Barajas International Airport |  | ES | 1976 |
| 18 | Frankfurt am Main International Airport |  | DE | 1957 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1882 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1829 |
| 21 | Malpensa International Airport |  | IT | 1804 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1766 |
| 23 | Charles de Gaulle International Airport |  | FR | 1757 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1748 |
| 25 | Ninoy Aquino International Airport |  | PH | 1663 |
| 26 | Enrique Olaya Herrera Airport |  | CO | 1660 |
| 27 | Macau International Airport |  | MO | 1651 |
| 28 | Barcelona International Airport |  | ES | 1587 |
| 29 | Charlotte/Douglas International Airport |  | US | 1586 |
| 30 | Kuala Lumpur International Airport |  | MY | 1574 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1540 |
| 32 | Viracopos International Airport |  | BR | 1500 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1459 |
| 35 | Don Mueang International Airport |  | TH | 1446 |
| 36 | Calgary International Airport |  | CA | 1445 |
| 37 | Bengaluru International Airport |  | IN | 1434 |
| 38 | Oslo Gardermoen Airport |  | NO | 1414 |
| 39 | Vancouver International Airport |  | CA | 1402 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1361 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 933 | 21m | 244 km | 3,928.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 665 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 630 | 1h 6m | 770 km | 8,369.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 564 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 412 | 27m | 275 km | 1,952.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 400 | 1h 50m | 1,423 km | 9,816.6 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 391 | 44m | 555 km | 3,744.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 374 | 44m | 241 km | 1,553.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 349 | 24m | 218 km | 1,314.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 335 | 23m | 55 km | 318.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 310 | 26m | 215 km | 1,148.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 291 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 272 | 1h 50m | 1,304 km | 6,119.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 257 | 41m | 535 km | 2,373.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NIA322 | NIA | Bergamo / Orio Al Serio Airport (LIME) | HE42 (HE42) | 2026-09-07 21:51 UTC | 2026-09-08 00:50 UTC | 2h 58m |
| NJL | NJL | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-08 00:15 UTC | 2026-09-08 00:49 UTC | 34m |
| N411ST |  | Gulf Shores International/Jack Edwards Field (KJKA) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-08 00:11 UTC | 2026-09-08 00:43 UTC | 32m |
| MNL14 | MNL | Truckee-Tahoe Airport (KTRK) | Buchanan Field (KCCR) | 2026-09-08 00:13 UTC | 2026-09-08 00:39 UTC | 26m |
| N125TN |  | Tyler Pounds Regional Airport (KTYR) | Austin-Bergstrom International Airport (KAUS) | 2026-09-08 00:04 UTC | 2026-09-08 00:39 UTC | 34m |
| AAL933P | American Airlines | Miami International Airport (KMIA) | Islas Malvinas Airport (SAAR) | 2026-09-07 16:47 UTC | 2026-09-08 00:27 UTC | 7h 39m |
| N36PJ |  | San Luis Obispo County Regional Airport (KSBP) | Henderson Executive Airport (KHND) | 2026-09-07 22:58 UTC | 2026-09-08 00:17 UTC | 1h 18m |
| NQT | NQT | Perth Jandakot Airport (YPJT) | Dalwallinu Airport (YDWU) | 2026-09-07 23:31 UTC | 2026-09-08 00:16 UTC | 44m |
| CGENW | CGE | Calgary International Airport (CYYC) | Gospel Ranch Airport (MN52) | 2026-09-07 22:23 UTC | 2026-09-08 00:15 UTC | 1h 51m |
| N908GF |  | Alderman Farm Airport (XS47) | San Antonio International Airport (KSAT) | 2026-09-08 00:01 UTC | 2026-09-08 00:13 UTC | 12m |
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-07 17:37 UTC | 2026-09-08 00:13 UTC | 6h 35m |
| ERU813 | ERU | Daytona Beach International Airport (KDAB) | Gainesville Regional Airport (KGNV) | 2026-09-07 23:07 UTC | 2026-09-08 00:12 UTC | 1h 4m |
| RXA6117 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-09-07 23:23 UTC | 2026-09-08 00:06 UTC | 43m |
| N744DA |  | Fairbanks International Airport (PAFA) | Ruby Airport (PARY) | 2026-09-07 23:11 UTC | 2026-09-08 00:04 UTC | 53m |
| EVANS25 | EVA Air | Fremont County Airport (K1V6) | Geary Ranch Airport (CO65) | 2026-09-07 23:32 UTC | 2026-09-08 00:03 UTC | 31m |
| N984SB |  | Harry Reid International Airport (KLAS) | Twentynine Palms Airport (KTNP) | 2026-09-07 23:33 UTC | 2026-09-08 00:03 UTC | 30m |
| N144AL |  | William P Hobby Airport (KHOU) | Valley Vista Airport (6CA5) | 2026-09-07 21:05 UTC | 2026-09-08 00:00 UTC | 2h 55m |
| N8RS |  | Flying Bj Airport (3NC5) | Southern West Virginia Regional Airport (KEBD) | 2026-09-07 23:30 UTC | 2026-09-07 23:59 UTC | 29m |
| CNS370 | CNS | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-09-07 23:19 UTC | 2026-09-07 23:56 UTC | 37m |
| N915MR |  | Albuquerque International Sunport Airport (KABQ) | Crownpoint Airport (K0E8) | 2026-09-07 23:36 UTC | 2026-09-07 23:56 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
