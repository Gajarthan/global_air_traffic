# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_23:29:21_UTC-green)

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

**Latest saved flight:** 2026-09-13 23:29:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 23:29:21 UTC

- **257,978** saved flights
- **76,751** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,978** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,122,770.9 tonnes** estimated CO2 emissions
- **181,030,199 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10250 |
| 2 | SkyWest Airlines | 8987 |
| 3 | EJA | 5004 |
| 4 | IndiGo | 4330 |
| 5 | American Airlines | 4078 |
| 6 | Southwest Airlines | 3796 |
| 7 | Delta Air Lines | 3230 |
| 8 | ENY | 3058 |
| 9 | LATAM Airlines | 2482 |
| 10 | AZU | 2414 |
| 11 | Vueling | 2183 |
| 12 | WIF | 2070 |
| 13 | LXJ | 2018 |
| 14 | Lufthansa | 2016 |
| 15 | easyJet | 1761 |
| 16 | Swiss International | 1724 |
| 17 | QLK | 1661 |
| 18 | AXM | 1646 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1596 |
| 21 | Alaska Airlines | 1530 |
| 22 | All Nippon Airways | 1497 |
| 23 | WMT | 1456 |
| 24 | GLO | 1439 |
| 25 | PGT | 1432 |
| 26 | Air France | 1409 |
| 27 | VIV | 1409 |
| 28 | Wizz Air | 1402 |
| 29 | JetBlue | 1248 |
| 30 | TKR | 1248 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 214187 |
| 2 | 🇪🇸 ES | 16369 |
| 3 | 🇧🇷 BR | 15076 |
| 4 | 🇦🇺 AU | 14681 |
| 5 | 🇨🇦 CA | 14366 |
| 6 | 🇮🇹 IT | 14068 |
| 7 | 🇮🇳 IN | 13595 |
| 8 | 🇩🇪 DE | 12561 |
| 9 | 🇬🇧 GB | 12028 |
| 10 | 🇨🇴 CO | 11580 |
| 11 | 🇫🇷 FR | 10367 |
| 12 | 🇯🇵 JP | 10042 |
| 13 | 🇹🇷 TR | 7764 |
| 14 | 🇬🇷 GR | 7516 |
| 15 | 🇲🇽 MX | 7114 |
| 16 | 🇨🇭 CH | 6919 |
| 17 | 🇳🇴 NO | 6375 |
| 18 | 🇹🇭 TH | 4640 |
| 19 | 🇲🇾 MY | 4425 |
| 20 | 🇿🇦 ZA | 4388 |
| 21 | 🇵🇱 PL | 4275 |
| 22 | 🇳🇿 NZ | 3562 |
| 23 | 🇵🇭 PH | 3466 |
| 24 | 🇬🇹 GT | 3263 |
| 25 | 🇭🇷 HR | 2963 |
| 26 | 🇰🇷 KR | 2948 |
| 27 | 🇲🇦 MA | 2592 |
| 28 | 🇲🇪 ME | 2427 |
| 29 | 🇳🇱 NL | 2322 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5291 |
| 2 | Denver International Airport |  | US | 4172 |
| 3 | Indira Gandhi International Airport |  | IN | 3118 |
| 4 | Tokyo International Airport |  | JP | 2997 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2734 |
| 7 | Zurich Airport |  | CH | 2702 |
| 8 | El Dorado International Airport |  | CO | 2695 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2601 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2518 |
| 11 | La Aurora Airport |  | GT | 2479 |
| 12 | Salt Lake City International Airport |  | US | 2273 |
| 13 | Chicago O'Hare International Airport |  | US | 2244 |
| 14 | Congonhas Airport |  | BR | 2211 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2108 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2011 |
| 18 | Frankfurt am Main International Airport |  | DE | 1989 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1937 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1862 |
| 21 | Malpensa International Airport |  | IT | 1856 |
| 22 | Charles de Gaulle International Airport |  | FR | 1819 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1810 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1784 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1751 |
| 26 | Macau International Airport |  | MO | 1710 |
| 27 | Ninoy Aquino International Airport |  | PH | 1697 |
| 28 | Barcelona International Airport |  | ES | 1620 |
| 29 | Charlotte/Douglas International Airport |  | US | 1616 |
| 30 | Kuala Lumpur International Airport |  | MY | 1592 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1582 |
| 32 | Viracopos International Airport |  | BR | 1554 |
| 33 | Seattle-Tacoma International Airport |  | US | 1514 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1506 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1476 |
| 37 | Bengaluru International Airport |  | IN | 1464 |
| 38 | Oslo Gardermoen Airport |  | NO | 1455 |
| 39 | Vancouver International Airport |  | CA | 1448 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1391 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 695 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 577 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 390 | 44m | 241 km | 1,620.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 361 | 24m | 218 km | 1,360.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 356 | 21m | 250 km | 1,537.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 319 | 26m | 215 km | 1,181.4 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 312 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 308 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 297 | 1h 14m | 961 km | 4,922.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1202 | IndiGo | Bahrain International Airport (OBBI) | Pune Airport (VAPO) | 2026-09-13 20:19 UTC | 2026-09-13 23:29 UTC | 3h 9m |
| N353MV |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-09-13 22:54 UTC | 2026-09-13 23:25 UTC | 30m |
| N8154J |  | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-09-13 22:42 UTC | 2026-09-13 23:16 UTC | 34m |
| UAL941 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-09-13 15:16 UTC | 2026-09-13 23:15 UTC | 7h 59m |
| PRDRV | PRD | Tres Marias Airport (SDWL) | Congonhas Airport (SBSP) | 2026-09-13 22:57 UTC | 2026-09-13 23:09 UTC | 12m |
| CFTOM | CFT | Edmonton International Airport (CYEG) | Fairmont Hot Springs Airport (CYCZ) | 2026-09-13 22:30 UTC | 2026-09-13 23:03 UTC | 33m |
| N719ND |  | Hillsboro Municipal Airport (K3H4) | Hillsboro Municipal Airport (K3H4) | 2026-09-13 22:58 UTC | 2026-09-13 23:03 UTC | 4m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-09-13 12:01 UTC | 2026-09-13 23:01 UTC | 10h 59m |
| VKG469 | VKG | Diagoras Airport (LGRP) | Zielona Góra-Babimost Airport (EPZG) | 2026-09-13 20:18 UTC | 2026-09-13 23:01 UTC | 2h 42m |
| N1671W |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-13 22:37 UTC | 2026-09-13 23:01 UTC | 23m |
| N620ME |  | Allegheny County Airport (KAGC) | Allegheny County Airport (KAGC) | 2026-09-13 22:54 UTC | 2026-09-13 22:58 UTC | 3m |
| N350TL |  | Talaheim Airport (1AK8) | Talaheim Airport (1AK8) | 2026-09-13 22:52 UTC | 2026-09-13 22:55 UTC | 3m |
| EJA134 | EJA | Allegheny County Airport (KAGC) | Nashville International Airport (KBNA) | 2026-09-13 21:45 UTC | 2026-09-13 22:52 UTC | 1h 6m |
| N208HF |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-09-13 22:30 UTC | 2026-09-13 22:51 UTC | 21m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-09-13 21:50 UTC | 2026-09-13 22:51 UTC | 1h 0m |
| N99341 |  | Mesquite Metro Airport (KHQZ) | Square Air Airport (TS63) | 2026-09-13 22:18 UTC | 2026-09-13 22:48 UTC | 29m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-09-13 18:13 UTC | 2026-09-13 22:45 UTC | 4h 31m |
| XKV | XKV | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-13 21:54 UTC | 2026-09-13 22:45 UTC | 50m |
| TKR107 | TKR | Throckmorton Municipal Airport (K72F) | Joseph Of Cupertino Stolport Airport (TS20) | 2026-09-13 21:53 UTC | 2026-09-13 22:44 UTC | 51m |
| CAP433 | CAP | Riverside Airport (KRAL) | Big Bear City Airport (KL35) | 2026-09-13 22:08 UTC | 2026-09-13 22:43 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
