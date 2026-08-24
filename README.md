# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_08:39:52_UTC-green)

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

**Latest saved flight:** 2026-08-24 08:39:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 08:39:52 UTC

- **231,232** saved flights
- **71,234** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,232** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,787,996.4 tonnes** estimated CO2 emissions
- **161,622,982 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9283 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3912 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3574 |
| 7 | Delta Air Lines | 2957 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2224 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1970 |
| 12 | Lufthansa | 1879 |
| 13 | LXJ | 1824 |
| 14 | WIF | 1823 |
| 15 | easyJet | 1613 |
| 16 | Swiss International | 1542 |
| 17 | AXM | 1540 |
| 18 | EJU | 1475 |
| 19 | QLK | 1472 |
| 20 | United Airlines | 1470 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1381 |
| 23 | GLO | 1291 |
| 24 | VIV | 1272 |
| 25 | WMT | 1271 |
| 26 | PGT | 1263 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1214 |
| 29 | AEE | 1152 |
| 30 | JetBlue | 1152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192834 |
| 2 | 🇪🇸 ES | 14826 |
| 3 | 🇧🇷 BR | 13517 |
| 4 | 🇦🇺 AU | 13136 |
| 5 | 🇨🇦 CA | 12761 |
| 6 | 🇮🇹 IT | 12530 |
| 7 | 🇮🇳 IN | 12177 |
| 8 | 🇩🇪 DE | 11357 |
| 9 | 🇬🇧 GB | 10861 |
| 10 | 🇨🇴 CO | 9612 |
| 11 | 🇯🇵 JP | 9414 |
| 12 | 🇫🇷 FR | 9231 |
| 13 | 🇹🇷 TR | 6821 |
| 14 | 🇬🇷 GR | 6805 |
| 15 | 🇲🇽 MX | 6431 |
| 16 | 🇨🇭 CH | 6130 |
| 17 | 🇳🇴 NO | 5683 |
| 18 | 🇲🇾 MY | 4107 |
| 19 | 🇹🇭 TH | 4051 |
| 20 | 🇿🇦 ZA | 4023 |
| 21 | 🇵🇱 PL | 3834 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3177 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2721 |
| 26 | 🇭🇷 HR | 2649 |
| 27 | 🇲🇦 MA | 2341 |
| 28 | 🇲🇪 ME | 2122 |
| 29 | 🇳🇱 NL | 2064 |
| 30 | 🇮🇩 ID | 2005 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2817 |
| 4 | Tokyo International Airport |  | JP | 2809 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2491 |
| 7 | Zurich Airport |  | CH | 2408 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2329 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2148 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1846 |
| 17 | Madrid Barajas International Airport |  | ES | 1814 |
| 18 | Capua Airport |  | IT | 1813 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1738 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1656 |
| 22 | Malpensa International Airport |  | IT | 1654 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Macau International Airport |  | MO | 1602 |
| 25 | Charles de Gaulle International Airport |  | FR | 1598 |
| 26 | Ninoy Aquino International Airport |  | PH | 1528 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1487 |
| 29 | Barcelona International Airport |  | ES | 1452 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Bengaluru International Airport |  | IN | 1366 |
| 34 | Seattle-Tacoma International Airport |  | US | 1363 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1325 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1288 |
| 39 | Vancouver International Airport |  | CA | 1255 |
| 40 | Vitoria/Foronda Airport |  | ES | 1253 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 845 | 21m | 244 km | 3,558.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 583 | 1h 6m | 770 km | 7,744.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 580 | 24m | 225 km | 2,250.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 381 | 27m | 275 km | 1,805.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 356 | 1h 50m | 1,423 km | 8,736.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 335 | 44m | 241 km | 1,391.5 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 319 | 44m | 555 km | 3,054.6 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 304 | 24m | 218 km | 1,145.3 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 300 | 1h 38m | 1,156 km | 5,984.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 266 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 263 | 19m | 144 km | 654.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 245 | 15m | 154 km | 649.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEZMD | DEZ | Aachen-Merzbruck Airport (EDKA) | Aachen-Merzbruck Airport (EDKA) | 2026-08-24 07:43 UTC | 2026-08-24 08:39 UTC | 56m |
| LEONE03 | LEO | Pratica Di Mare Airport (LIRE) | Pratica Di Mare Airport (LIRE) | 2026-08-24 08:17 UTC | 2026-08-24 08:26 UTC | 9m |
| 340 |  | LL1A (LL1A) | LL1A (LL1A) | 2026-08-24 07:31 UTC | 2026-08-24 08:20 UTC | 49m |
| 0000322 |  | Be'er Sheva (Teyman) Airport (LLBS) | LL1A (LL1A) | 2026-08-24 07:27 UTC | 2026-08-24 08:19 UTC | 52m |
| L2B |  | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-24 06:58 UTC | 2026-08-24 08:16 UTC | 1h 18m |
| HNL24A | HNL | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-24 07:45 UTC | 2026-08-24 08:15 UTC | 30m |
| N399LG |  | CO54 (CO54) | CO86 (CO86) | 2026-08-24 07:27 UTC | 2026-08-24 08:14 UTC | 47m |
| A7GHZ |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-24 07:49 UTC | 2026-08-24 08:12 UTC | 23m |
| YOI | YOI | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-24 07:37 UTC | 2026-08-24 08:11 UTC | 33m |
| FD447 |  | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-08-24 07:38 UTC | 2026-08-24 08:10 UTC | 32m |
| EFC68L | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-24 07:56 UTC | 2026-08-24 08:10 UTC | 14m |
| DLH836 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Billund Airport (EKBI) | 2026-08-24 07:08 UTC | 2026-08-24 08:09 UTC | 1h 0m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-24 07:55 UTC | 2026-08-24 08:07 UTC | 11m |
| ZEF | ZEF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-24 07:08 UTC | 2026-08-24 08:06 UTC | 57m |
| QTR9950 | Qatar Airways | Hamad International Airport (OTHH) | Doha International Airport (OTBD) | 2026-08-24 07:33 UTC | 2026-08-24 08:06 UTC | 33m |
| LNX87GL | LNX | London Luton Airport (EGGW) | Dublin Airport (EIDW) | 2026-08-24 06:57 UTC | 2026-08-24 08:05 UTC | 1h 7m |
| THA044 | Thai Airways | Suvarnabhumi Airport (VTBS) | Khon Kaen Airport (VTUK) | 2026-08-24 07:23 UTC | 2026-08-24 07:59 UTC | 36m |
| RUK530X | RUK | London Stansted Airport (EGSS) | Visoko Sport Airfield (LQVI) | 2026-08-24 06:07 UTC | 2026-08-24 07:58 UTC | 1h 50m |
| N53AR |  | Ted Stevens Anchorage International Airport (PANC) | AK04 (AK04) | 2026-08-24 07:22 UTC | 2026-08-24 07:55 UTC | 33m |
| ANE8113 | ANE | Francisco de Sá Carneiro Airport (LPPR) | Almeria International Airport (LEAM) | 2026-08-24 06:53 UTC | 2026-08-24 07:54 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
