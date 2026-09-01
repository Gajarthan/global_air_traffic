# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_02:52:24_UTC-green)

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

**Latest saved flight:** 2026-09-01 02:52:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 02:52:24 UTC

- **243,243** saved flights
- **73,717** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **243,243** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,928,626.6 tonnes** estimated CO2 emissions
- **169,775,457 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9765 |
| 2 | SkyWest Airlines | 8529 |
| 3 | EJA | 4703 |
| 4 | IndiGo | 4086 |
| 5 | American Airlines | 3917 |
| 6 | Southwest Airlines | 3656 |
| 7 | Delta Air Lines | 3102 |
| 8 | ENY | 2931 |
| 9 | LATAM Airlines | 2333 |
| 10 | AZU | 2263 |
| 11 | Vueling | 2083 |
| 12 | Lufthansa | 1951 |
| 13 | WIF | 1930 |
| 14 | LXJ | 1883 |
| 15 | easyJet | 1696 |
| 16 | Swiss International | 1638 |
| 17 | AXM | 1603 |
| 18 | EJU | 1561 |
| 19 | QLK | 1553 |
| 20 | United Airlines | 1531 |
| 21 | Alaska Airlines | 1455 |
| 22 | All Nippon Airways | 1437 |
| 23 | WMT | 1369 |
| 24 | GLO | 1361 |
| 25 | VIV | 1333 |
| 26 | PGT | 1330 |
| 27 | Air France | 1326 |
| 28 | Wizz Air | 1317 |
| 29 | JetBlue | 1204 |
| 30 | AEE | 1201 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 201577 |
| 2 | 🇪🇸 ES | 15623 |
| 3 | 🇧🇷 BR | 14187 |
| 4 | 🇦🇺 AU | 13820 |
| 5 | 🇨🇦 CA | 13544 |
| 6 | 🇮🇹 IT | 13317 |
| 7 | 🇮🇳 IN | 12724 |
| 8 | 🇩🇪 DE | 11994 |
| 9 | 🇬🇧 GB | 11483 |
| 10 | 🇨🇴 CO | 10504 |
| 11 | 🇫🇷 FR | 9801 |
| 12 | 🇯🇵 JP | 9729 |
| 13 | 🇹🇷 TR | 7233 |
| 14 | 🇬🇷 GR | 7169 |
| 15 | 🇲🇽 MX | 6714 |
| 16 | 🇨🇭 CH | 6542 |
| 17 | 🇳🇴 NO | 6010 |
| 18 | 🇹🇭 TH | 4397 |
| 19 | 🇲🇾 MY | 4301 |
| 20 | 🇿🇦 ZA | 4233 |
| 21 | 🇵🇱 PL | 4090 |
| 22 | 🇳🇿 NZ | 3345 |
| 23 | 🇵🇭 PH | 3328 |
| 24 | 🇬🇹 GT | 3060 |
| 25 | 🇰🇷 KR | 2862 |
| 26 | 🇭🇷 HR | 2805 |
| 27 | 🇲🇦 MA | 2462 |
| 28 | 🇲🇪 ME | 2270 |
| 29 | 🇳🇱 NL | 2199 |
| 30 | 🇮🇩 ID | 2121 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5019 |
| 2 | Denver International Airport |  | US | 3918 |
| 3 | Indira Gandhi International Airport |  | IN | 2964 |
| 4 | Tokyo International Airport |  | JP | 2897 |
| 5 | Guaymaral Airport |  | CO | 2707 |
| 6 | Harry Reid International Airport |  | US | 2588 |
| 7 | Zurich Airport |  | CH | 2553 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2484 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2426 |
| 10 | El Dorado International Airport |  | CO | 2385 |
| 11 | La Aurora Airport |  | GT | 2329 |
| 12 | Salt Lake City International Airport |  | US | 2152 |
| 13 | Chicago O'Hare International Airport |  | US | 2151 |
| 14 | Congonhas Airport |  | BR | 2077 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2017 |
| 16 | Frankfurt am Main International Airport |  | DE | 1921 |
| 17 | Capua Airport |  | IT | 1914 |
| 18 | Madrid Barajas International Airport |  | ES | 1909 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1826 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1790 |
| 21 | Malpensa International Airport |  | IT | 1736 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1720 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1706 |
| 24 | Charles de Gaulle International Airport |  | FR | 1702 |
| 25 | Macau International Airport |  | MO | 1621 |
| 26 | Ninoy Aquino International Airport |  | PH | 1618 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1558 |
| 28 | Charlotte/Douglas International Airport |  | US | 1555 |
| 29 | Kuala Lumpur International Airport |  | MY | 1550 |
| 30 | Barcelona International Airport |  | ES | 1544 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1471 |
| 32 | Viracopos International Airport |  | BR | 1445 |
| 33 | Seattle-Tacoma International Airport |  | US | 1425 |
| 34 | Don Mueang International Airport |  | TH | 1416 |
| 35 | Bengaluru International Airport |  | IN | 1411 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 1410 |
| 37 | Calgary International Airport |  | CA | 1397 |
| 38 | Oslo Gardermoen Airport |  | NO | 1366 |
| 39 | Vancouver International Airport |  | CA | 1354 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1328 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1097 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 897 | 21m | 244 km | 3,777.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 628 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 618 | 24m | 225 km | 2,397.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 400 | 27m | 275 km | 1,895.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 383 | 1h 50m | 1,423 km | 9,399.4 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 371 | 44m | 555 km | 3,552.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 354 | 44m | 241 km | 1,470.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 334 | 24m | 218 km | 1,258.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 324 | 1h 39m | 1,156 km | 6,463.7 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 322 | 22m | 55 km | 306.1 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 321 | 1h 7m | 706 km | 3,908.2 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 302 | 19m | 99 km | 517.3 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 296 | 26m | 215 km | 1,096.3 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 287 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 282 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 279 | 1h 14m | 961 km | 4,624.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 275 | 19m | 144 km | 684.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 265 | 15m | 154 km | 702.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DEVIL41 | DEV | Dunbar Ranch Airport (0XS8) | Dunbar Ranch Airport (0XS8) | 2026-09-01 02:41 UTC | 2026-09-01 02:52 UTC | 11m |
| N79CB |  | Albuquerque International Sunport Airport (KABQ) | Phoenix Deer Valley Airport (KDVT) | 2026-09-01 01:52 UTC | 2026-09-01 02:47 UTC | 55m |
| LBQ792 | LBQ | Syracuse Hancock International Airport (KSYR) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-09-01 02:23 UTC | 2026-09-01 02:44 UTC | 21m |
| OUA38 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Tulsa International Airport (KTUL) | 2026-09-01 01:55 UTC | 2026-09-01 02:43 UTC | 47m |
| CPA345 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-08-31 23:42 UTC | 2026-09-01 02:18 UTC | 2h 36m |
| ASA7098 | Alaska Airlines | Ted Stevens Anchorage International Airport (PANC) | Johnstone Point Airport (2AK5) | 2026-09-01 01:55 UTC | 2026-09-01 02:16 UTC | 20m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-09-01 01:52 UTC | 2026-09-01 02:12 UTC | 20m |
| PFR | PFR | Albury Airport (YMAY) | Holbrook Airport (YHBK) | 2026-09-01 02:02 UTC | 2026-09-01 02:12 UTC | 10m |
| UTY3116 | UTY | Adelaide International Airport (YPAD) | Blinman Airport (YBLM) | 2026-09-01 01:24 UTC | 2026-09-01 02:07 UTC | 43m |
| AAR8703 | AAR | Gimpo International Airport (RKSS) | G 710 Airport (RK6D) | 2026-09-01 01:39 UTC | 2026-09-01 02:07 UTC | 27m |
| ALFT5 | ALF | Anacortes Airport (K74S) | Bellingham International Airport (KBLI) | 2026-09-01 01:55 UTC | 2026-09-01 02:06 UTC | 10m |
| CFBFY | CFB | Pitt Meadows Airport (CYPK) | Chilliwack Airport (CYCW) | 2026-09-01 01:41 UTC | 2026-09-01 02:05 UTC | 24m |
| SFJ75 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-01 01:01 UTC | 2026-09-01 02:04 UTC | 1h 3m |
| G21122 |  | KU42 (KU42) | Cedar Valley Airport (UT10) | 2026-09-01 01:36 UTC | 2026-09-01 02:04 UTC | 28m |
| PUL107 | PUL | Sudbury Airport (CYSB) | Elk Lake Airport (CPE3) | 2026-09-01 01:45 UTC | 2026-09-01 02:03 UTC | 18m |
| BHA951 | BHA | Tribhuvan International Airport (VNKT) | Bhojpur Airport (VNBJ) | 2026-09-01 01:32 UTC | 2026-09-01 01:59 UTC | 27m |
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Zhuhai Airport (ZGSD) | 2026-08-31 18:58 UTC | 2026-09-01 01:58 UTC | 7h 0m |
| N515MJ |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-09-01 01:43 UTC | 2026-09-01 01:57 UTC | 14m |
| VT552 |  | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-09-01 01:01 UTC | 2026-09-01 01:54 UTC | 52m |
| IGO7193 | IndiGo | Chennai International Airport (VOMM) | Kovilpatti Airport (VO26) | 2026-09-01 00:47 UTC | 2026-09-01 01:53 UTC | 1h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
