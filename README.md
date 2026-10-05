# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_23:53:29_UTC-green)

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

**Latest saved flight:** 2026-10-04 23:53:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-04 23:53:29 UTC

- **276,625** saved flights
- **80,481** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **276,625** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,349,987.0 tonnes** estimated CO2 emissions
- **194,202,143 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10841 |
| 2 | SkyWest Airlines | 9617 |
| 3 | EJA | 5428 |
| 4 | IndiGo | 4611 |
| 5 | American Airlines | 4279 |
| 6 | Southwest Airlines | 4061 |
| 7 | Delta Air Lines | 3441 |
| 8 | ENY | 3229 |
| 9 | LATAM Airlines | 2681 |
| 10 | AZU | 2603 |
| 11 | Vueling | 2290 |
| 12 | WIF | 2250 |
| 13 | LXJ | 2191 |
| 14 | Lufthansa | 2077 |
| 15 | easyJet | 1834 |
| 16 | Swiss International | 1806 |
| 17 | QLK | 1784 |
| 18 | EJU | 1720 |
| 19 | AXM | 1694 |
| 20 | United Airlines | 1684 |
| 21 | Alaska Airlines | 1632 |
| 22 | All Nippon Airways | 1579 |
| 23 | PGT | 1555 |
| 24 | GLO | 1544 |
| 25 | WMT | 1536 |
| 26 | Air France | 1522 |
| 27 | VIV | 1517 |
| 28 | Wizz Air | 1498 |
| 29 | CXK | 1366 |
| 30 | AEE | 1314 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230893 |
| 2 | 🇪🇸 ES | 17289 |
| 3 | 🇧🇷 BR | 16253 |
| 4 | 🇦🇺 AU | 15951 |
| 5 | 🇨🇦 CA | 15408 |
| 6 | 🇮🇹 IT | 14915 |
| 7 | 🇮🇳 IN | 14590 |
| 8 | 🇩🇪 DE | 13202 |
| 9 | 🇨🇴 CO | 12852 |
| 10 | 🇬🇧 GB | 12734 |
| 11 | 🇫🇷 FR | 10930 |
| 12 | 🇯🇵 JP | 10527 |
| 13 | 🇹🇷 TR | 8347 |
| 14 | 🇬🇷 GR | 7921 |
| 15 | 🇲🇽 MX | 7643 |
| 16 | 🇨🇭 CH | 7338 |
| 17 | 🇳🇴 NO | 6819 |
| 18 | 🇹🇭 TH | 4958 |
| 19 | 🇲🇾 MY | 4588 |
| 20 | 🇿🇦 ZA | 4576 |
| 21 | 🇵🇱 PL | 4521 |
| 22 | 🇳🇿 NZ | 3938 |
| 23 | 🇵🇭 PH | 3660 |
| 24 | 🇬🇹 GT | 3467 |
| 25 | 🇭🇷 HR | 3143 |
| 26 | 🇰🇷 KR | 3108 |
| 27 | 🇲🇦 MA | 2729 |
| 28 | 🇲🇪 ME | 2594 |
| 29 | 🇳🇱 NL | 2465 |
| 30 | 🇮🇩 ID | 2283 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5607 |
| 2 | Denver International Airport |  | US | 4513 |
| 3 | Indira Gandhi International Airport |  | IN | 3293 |
| 4 | Tokyo International Airport |  | JP | 3158 |
| 5 | El Dorado International Airport |  | CO | 3080 |
| 6 | Harry Reid International Airport |  | US | 2980 |
| 7 | Zurich Airport |  | CH | 2869 |
| 8 | Guaymaral Airport |  | CO | 2855 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2765 |
| 10 | La Aurora Airport |  | GT | 2637 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2635 |
| 12 | Salt Lake City International Airport |  | US | 2463 |
| 13 | Congonhas Airport |  | BR | 2365 |
| 14 | Chicago O'Hare International Airport |  | US | 2329 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2269 |
| 16 | Capua Airport |  | IT | 2151 |
| 17 | Madrid Barajas International Airport |  | ES | 2130 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2112 |
| 19 | Frankfurt am Main International Airport |  | DE | 2078 |
| 20 | Charles de Gaulle International Airport |  | FR | 1962 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1961 |
| 22 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 23 | Malpensa International Airport |  | IT | 1953 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1935 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1844 |
| 26 | Macau International Airport |  | MO | 1805 |
| 27 | Ninoy Aquino International Airport |  | PH | 1801 |
| 28 | Charlotte/Douglas International Airport |  | US | 1725 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1720 |
| 30 | Barcelona International Airport |  | ES | 1704 |
| 31 | Viracopos International Airport |  | BR | 1658 |
| 32 | Kuala Lumpur International Airport |  | MY | 1645 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1628 |
| 34 | Seattle-Tacoma International Airport |  | US | 1627 |
| 35 | Calgary International Airport |  | CA | 1572 |
| 36 | Don Mueang International Airport |  | TH | 1562 |
| 37 | Oslo Gardermoen Airport |  | NO | 1550 |
| 38 | Vancouver International Airport |  | CA | 1549 |
| 39 | Bengaluru International Airport |  | IN | 1543 |
| 40 | Reno/Tahoe International Airport |  | US | 1505 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1043 | 21m | 244 km | 4,391.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 700 | 24m | 225 km | 2,715.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 698 | 1h 6m | 770 km | 9,272.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 461 | 44m | 555 km | 4,414.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 437 | 1h 50m | 1,423 km | 10,724.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 425 | 44m | 241 km | 1,765.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 371 | 21m | 250 km | 1,602.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 357 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 348 | 1h 6m | 706 km | 4,236.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 343 | 26m | 215 km | 1,270.3 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 337 | 1h 40m | 1,156 km | 6,723.0 t |
| 21 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 324 | 19m | 14 km | 81.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 322 | 19m | 144 km | 801.0 t |
| 23 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 312 | 42m | 535 km | 2,881.5 t |
| 24 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 287 | 28m | 152 km | 750.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 275 | 44m | 431 km | 2,046.5 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 275 | 51m | 556 km | 2,636.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-10-04 12:23 UTC | 2026-10-04 23:53 UTC | 11h 29m |
| BRG682 | BRG | Kivalina Airport (PAVL) | Noatak Airport (PAWN) | 2026-10-04 23:38 UTC | 2026-10-04 23:50 UTC | 12m |
| N42SH |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-10-04 22:54 UTC | 2026-10-04 23:50 UTC | 56m |
| N786TX |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-10-04 22:24 UTC | 2026-10-04 23:43 UTC | 1h 19m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-10-04 22:08 UTC | 2026-10-04 23:39 UTC | 1h 30m |
| IMM | IMM | Puckapunyal (Military) Airport (YPKL) | Melbourne Essendon Airport (YMEN) | 2026-10-04 23:02 UTC | 2026-10-04 23:36 UTC | 34m |
| N194TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-10-04 23:18 UTC | 2026-10-04 23:36 UTC | 17m |
| MNN | MNN | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-10-04 23:16 UTC | 2026-10-04 23:28 UTC | 12m |
| CGPPV | CGP | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-10-04 23:12 UTC | 2026-10-04 23:27 UTC | 15m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-10-04 12:43 UTC | 2026-10-04 23:25 UTC | 10h 42m |
| CPA318 | Cathay Pacific | Barcelona International Airport (LEBL) | Macau International Airport (VMMC) | 2026-10-04 12:02 UTC | 2026-10-04 23:22 UTC | 11h 19m |
| CGPCR | CGP | Vancouver International Airport (CYVR) | Alert Bay Airport (CYAL) | 2026-10-04 22:38 UTC | 2026-10-04 23:22 UTC | 43m |
| N371RM |  | Columbus Airport (KCSG) | Gregory M Simmons Memorial Airport (KGZN) | 2026-10-04 21:00 UTC | 2026-10-04 23:20 UTC | 2h 19m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-10-04 22:59 UTC | 2026-10-04 23:19 UTC | 20m |
| ZKLTE | ZKL | Hood Airport (NZMS) | Hood Airport (NZMS) | 2026-10-04 22:12 UTC | 2026-10-04 23:18 UTC | 1h 5m |
| N318DC |  | London Luton Airport (EGGW) | Bangor International Airport (KBGR) | 2026-10-04 16:32 UTC | 2026-10-04 23:15 UTC | 6h 43m |
| RNA415 | RNA | Tribhuvan International Airport (VNKT) | Naypyidaw Airport (VYEL) | 2026-10-04 21:39 UTC | 2026-10-04 23:15 UTC | 1h 35m |
| N404FR |  | Centennial Airport (KAPA) | Laramie Regional Airport (KLAR) | 2026-10-04 22:05 UTC | 2026-10-04 23:12 UTC | 1h 6m |
| N291DV |  | Spaulding Airport (K1Q2) | Palm Springs International Airport (KPSP) | 2026-10-04 21:54 UTC | 2026-10-04 23:11 UTC | 1h 16m |
| UAE9848 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-10-04 16:12 UTC | 2026-10-04 23:09 UTC | 6h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
