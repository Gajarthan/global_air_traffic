# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_00:33:13_UTC-green)

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

**Latest saved flight:** 2026-09-28 00:33:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-28 00:33:13 UTC

- **271,465** saved flights
- **79,443** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **271,465** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,291,653.5 tonnes** estimated CO2 emissions
- **190,820,495 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10679 |
| 2 | SkyWest Airlines | 9459 |
| 3 | EJA | 5317 |
| 4 | IndiGo | 4537 |
| 5 | American Airlines | 4217 |
| 6 | Southwest Airlines | 4001 |
| 7 | Delta Air Lines | 3373 |
| 8 | ENY | 3192 |
| 9 | LATAM Airlines | 2610 |
| 10 | AZU | 2547 |
| 11 | Vueling | 2257 |
| 12 | WIF | 2205 |
| 13 | LXJ | 2141 |
| 14 | Lufthansa | 2058 |
| 15 | easyJet | 1814 |
| 16 | Swiss International | 1778 |
| 17 | QLK | 1748 |
| 18 | EJU | 1698 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1659 |
| 21 | Alaska Airlines | 1603 |
| 22 | All Nippon Airways | 1559 |
| 23 | PGT | 1531 |
| 24 | GLO | 1515 |
| 25 | WMT | 1515 |
| 26 | Air France | 1492 |
| 27 | VIV | 1486 |
| 28 | Wizz Air | 1473 |
| 29 | CXK | 1335 |
| 30 | AEE | 1298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226261 |
| 2 | 🇪🇸 ES | 16986 |
| 3 | 🇧🇷 BR | 15893 |
| 4 | 🇦🇺 AU | 15603 |
| 5 | 🇨🇦 CA | 15136 |
| 6 | 🇮🇹 IT | 14666 |
| 7 | 🇮🇳 IN | 14356 |
| 8 | 🇩🇪 DE | 13013 |
| 9 | 🇬🇧 GB | 12550 |
| 10 | 🇨🇴 CO | 12475 |
| 11 | 🇫🇷 FR | 10782 |
| 12 | 🇯🇵 JP | 10406 |
| 13 | 🇹🇷 TR | 8218 |
| 14 | 🇬🇷 GR | 7818 |
| 15 | 🇲🇽 MX | 7492 |
| 16 | 🇨🇭 CH | 7214 |
| 17 | 🇳🇴 NO | 6701 |
| 18 | 🇹🇭 TH | 4847 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4524 |
| 21 | 🇵🇱 PL | 4452 |
| 22 | 🇳🇿 NZ | 3816 |
| 23 | 🇵🇭 PH | 3587 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3093 |
| 26 | 🇰🇷 KR | 3066 |
| 27 | 🇲🇦 MA | 2691 |
| 28 | 🇲🇪 ME | 2547 |
| 29 | 🇳🇱 NL | 2439 |
| 30 | 🇮🇩 ID | 2258 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5532 |
| 2 | Denver International Airport |  | US | 4426 |
| 3 | Indira Gandhi International Airport |  | IN | 3243 |
| 4 | Tokyo International Airport |  | JP | 3116 |
| 5 | El Dorado International Airport |  | CO | 2963 |
| 6 | Harry Reid International Airport |  | US | 2916 |
| 7 | Guaymaral Airport |  | CO | 2826 |
| 8 | Zurich Airport |  | CH | 2811 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2720 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2401 |
| 13 | Chicago O'Hare International Airport |  | US | 2315 |
| 14 | Congonhas Airport |  | BR | 2313 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2223 |
| 16 | Capua Airport |  | IT | 2096 |
| 17 | Madrid Barajas International Airport |  | ES | 2091 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2052 |
| 19 | Frankfurt am Main International Airport |  | DE | 2052 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1931 |
| 21 | Malpensa International Airport |  | IT | 1931 |
| 22 | Charles de Gaulle International Airport |  | FR | 1928 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1910 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1900 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1761 |
| 28 | Charlotte/Douglas International Airport |  | US | 1697 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1692 |
| 30 | Barcelona International Airport |  | ES | 1683 |
| 31 | Viracopos International Airport |  | BR | 1633 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1594 |
| 34 | Seattle-Tacoma International Airport |  | US | 1591 |
| 35 | Calgary International Airport |  | CA | 1545 |
| 36 | Don Mueang International Airport |  | TH | 1533 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1521 |
| 39 | Vancouver International Airport |  | CA | 1520 |
| 40 | Reno/Tahoe International Airport |  | US | 1451 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1018 | 21m | 244 km | 4,286.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 751 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 451 | 44m | 555 km | 4,318.5 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 436 | 27m | 275 km | 2,066.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 428 | 1h 50m | 1,423 km | 10,503.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 415 | 44m | 241 km | 1,723.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 346 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 315 | 19m | 144 km | 783.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 307 | 1h 14m | 961 km | 5,088.7 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 300 | 42m | 535 km | 2,770.7 t |
| 25 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 299 | 18m | 14 km | 74.8 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 294 | 1h 50m | 1,304 km | 6,614.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKFTD | ZKF | Rangiora Airfield (NZRT) | West Melton Aerodrome (NZWL) | 2026-09-28 00:18 UTC | 2026-09-28 00:33 UTC | 14m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-28 00:00 UTC | 2026-09-28 00:19 UTC | 19m |
| N554VR |  | Cleveland-Hopkins International Airport (KCLE) | Berkeley County Airport (KMKS) | 2026-09-27 22:07 UTC | 2026-09-28 00:05 UTC | 1h 58m |
| N376AE |  | El Peco Ranch Airport (49CL) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-27 23:34 UTC | 2026-09-28 00:05 UTC | 30m |
| EJA134 | EJA | Syracuse Hancock International Airport (KSYR) | Rochester International Airport (KRST) | 2026-09-27 22:20 UTC | 2026-09-28 00:03 UTC | 1h 42m |
| N118FS |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Vowers Ranch Airport (WY29) | 2026-09-27 23:52 UTC | 2026-09-28 00:03 UTC | 10m |
| NPF | NPF | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-27 23:26 UTC | 2026-09-27 23:58 UTC | 32m |
| N339SP |  | Zamperini Field (KTOA) | Big Bear City Airport (KL35) | 2026-09-27 23:05 UTC | 2026-09-27 23:47 UTC | 42m |
| N900KE |  | Dallas Love Field (KDAL) | Melby Ranch Airstrip (33CO) | 2026-09-27 22:24 UTC | 2026-09-27 23:47 UTC | 1h 23m |
| CFFJK | CFF | Chilliwack Airport (CYCW) | Pitt Meadows Airport (CYPK) | 2026-09-27 23:24 UTC | 2026-09-27 23:47 UTC | 23m |
| N95HT |  | Orlando International Airport (KMCO) | Orlando International Airport (KMCO) | 2026-09-27 23:33 UTC | 2026-09-27 23:44 UTC | 11m |
| OAI | OAI | Barwon Heads Airport (YBRS) | Barwon Heads Airport (YBRS) | 2026-09-27 23:23 UTC | 2026-09-27 23:43 UTC | 20m |
| N237JT |  | Lovell Field (KCHA) | North Pickens Airport (K3M8) | 2026-09-27 23:16 UTC | 2026-09-27 23:43 UTC | 26m |
| LR453 |  | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-09-27 23:07 UTC | 2026-09-27 23:41 UTC | 34m |
| N691DK |  | Vancouver International Airport (CYVR) | Squamish Airport (CYSE) | 2026-09-27 23:27 UTC | 2026-09-27 23:40 UTC | 13m |
| ENY3425 | ENY | Chicago O'Hare International Airport (KORD) | 8II3 (8II3) | 2026-09-27 23:05 UTC | 2026-09-27 23:39 UTC | 33m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-09-27 23:31 UTC | 2026-09-27 23:37 UTC | 6m |
| ENY4192 | ENY | Phoenix Sky Harbor International Airport (KPHX) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-09-27 23:14 UTC | 2026-09-27 23:36 UTC | 22m |
| WSK155 | WSK | Perth International Airport (YPPH) | Hyden Airport (YHYD) | 2026-09-27 23:02 UTC | 2026-09-27 23:35 UTC | 32m |
| SKW3164 | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-09-27 22:32 UTC | 2026-09-27 23:31 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
