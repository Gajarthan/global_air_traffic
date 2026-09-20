# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_00:58:04_UTC-green)

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

**Latest saved flight:** 2026-09-20 00:58:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-20 00:58:04 UTC

- **264,132** saved flights
- **77,982** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **264,132** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,200,829.7 tonnes** estimated CO2 emissions
- **185,555,344 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10444 |
| 2 | SkyWest Airlines | 9187 |
| 3 | EJA | 5136 |
| 4 | IndiGo | 4437 |
| 5 | American Airlines | 4132 |
| 6 | Southwest Airlines | 3887 |
| 7 | Delta Air Lines | 3290 |
| 8 | ENY | 3114 |
| 9 | LATAM Airlines | 2551 |
| 10 | AZU | 2485 |
| 11 | Vueling | 2216 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2070 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1742 |
| 17 | QLK | 1705 |
| 18 | EJU | 1665 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1619 |
| 21 | Alaska Airlines | 1567 |
| 22 | All Nippon Airways | 1523 |
| 23 | PGT | 1486 |
| 24 | WMT | 1484 |
| 25 | GLO | 1471 |
| 26 | Air France | 1445 |
| 27 | VIV | 1444 |
| 28 | Wizz Air | 1431 |
| 29 | CXK | 1279 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219520 |
| 2 | 🇪🇸 ES | 16634 |
| 3 | 🇧🇷 BR | 15468 |
| 4 | 🇦🇺 AU | 15122 |
| 5 | 🇨🇦 CA | 14712 |
| 6 | 🇮🇹 IT | 14357 |
| 7 | 🇮🇳 IN | 14025 |
| 8 | 🇩🇪 DE | 12749 |
| 9 | 🇬🇧 GB | 12252 |
| 10 | 🇨🇴 CO | 11995 |
| 11 | 🇫🇷 FR | 10550 |
| 12 | 🇯🇵 JP | 10216 |
| 13 | 🇹🇷 TR | 8002 |
| 14 | 🇬🇷 GR | 7657 |
| 15 | 🇲🇽 MX | 7270 |
| 16 | 🇨🇭 CH | 7048 |
| 17 | 🇳🇴 NO | 6516 |
| 18 | 🇹🇭 TH | 4732 |
| 19 | 🇲🇾 MY | 4473 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4350 |
| 22 | 🇳🇿 NZ | 3665 |
| 23 | 🇵🇭 PH | 3513 |
| 24 | 🇬🇹 GT | 3364 |
| 25 | 🇭🇷 HR | 3010 |
| 26 | 🇰🇷 KR | 2992 |
| 27 | 🇲🇦 MA | 2645 |
| 28 | 🇲🇪 ME | 2474 |
| 29 | 🇳🇱 NL | 2367 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5399 |
| 2 | Denver International Airport |  | US | 4275 |
| 3 | Indira Gandhi International Airport |  | IN | 3171 |
| 4 | Tokyo International Airport |  | JP | 3051 |
| 5 | El Dorado International Airport |  | CO | 2811 |
| 6 | Harry Reid International Airport |  | US | 2811 |
| 7 | Guaymaral Airport |  | CO | 2785 |
| 8 | Zurich Airport |  | CH | 2747 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2654 |
| 10 | La Aurora Airport |  | GT | 2556 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2555 |
| 12 | Salt Lake City International Airport |  | US | 2330 |
| 13 | Chicago O'Hare International Airport |  | US | 2270 |
| 14 | Congonhas Airport |  | BR | 2255 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2158 |
| 16 | Capua Airport |  | IT | 2065 |
| 17 | Madrid Barajas International Airport |  | ES | 2039 |
| 18 | Frankfurt am Main International Airport |  | DE | 2015 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1996 |
| 20 | Malpensa International Airport |  | IT | 1902 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1891 |
| 22 | Charles de Gaulle International Airport |  | FR | 1865 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1860 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1836 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1804 |
| 26 | Macau International Airport |  | MO | 1758 |
| 27 | Ninoy Aquino International Airport |  | PH | 1725 |
| 28 | Barcelona International Airport |  | ES | 1647 |
| 29 | Charlotte/Douglas International Airport |  | US | 1646 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1625 |
| 31 | Viracopos International Airport |  | BR | 1603 |
| 32 | Kuala Lumpur International Airport |  | MY | 1603 |
| 33 | Seattle-Tacoma International Airport |  | US | 1552 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1541 |
| 35 | Calgary International Airport |  | CA | 1507 |
| 36 | Don Mueang International Airport |  | TH | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1498 |
| 38 | Oslo Gardermoen Airport |  | NO | 1486 |
| 39 | Vancouver International Airport |  | CA | 1479 |
| 40 | Antalya International Airport |  | TR | 1416 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 989 | 21m | 244 km | 4,164.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 725 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 664 | 1h 6m | 770 km | 8,820.7 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 658 | 24m | 225 km | 2,552.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 417 | 1h 50m | 1,423 km | 10,233.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 377 | 24m | 218 km | 1,420.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 338 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 286 | 1h 50m | 1,304 km | 6,434.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 283 | 42m | 535 km | 2,613.7 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 266 | 18m | 14 km | 66.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N32WS |  | Lee Vining Airport (KO24) | 6CL4 (6CL4) | 2026-09-20 00:47 UTC | 2026-09-20 00:58 UTC | 10m |
| N965LB |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-09-20 00:16 UTC | 2026-09-20 00:57 UTC | 41m |
| N8325C |  | 11CL (11CL) | Big Bear City Airport (KL35) | 2026-09-20 00:31 UTC | 2026-09-20 00:50 UTC | 19m |
| N736JA |  | Watsonville Municipal Airport (KWVI) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-09-20 00:14 UTC | 2026-09-20 00:46 UTC | 31m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-20 00:28 UTC | 2026-09-20 00:44 UTC | 15m |
| FDX10 | FDX | Charles de Gaulle International Airport (LFPG) | Burgas Airport (LBBG) | 2026-09-19 22:26 UTC | 2026-09-20 00:43 UTC | 2h 17m |
| N1625U |  | Monterey Regional Airport (KMRY) | Hayward Executive Airport (KHWD) | 2026-09-20 00:12 UTC | 2026-09-20 00:40 UTC | 27m |
| AHY5830 | AHY | Sibay Airport (UWUA) | Bezymyanka Airfield (UWWG) | 2026-09-19 19:23 UTC | 2026-09-20 00:35 UTC | 5h 11m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-09-20 00:17 UTC | 2026-09-20 00:34 UTC | 17m |
| 83C |  | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-09-19 23:49 UTC | 2026-09-20 00:33 UTC | 43m |
| CPA694 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-19 20:03 UTC | 2026-09-20 00:33 UTC | 4h 29m |
| TMN3 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-19 21:32 UTC | 2026-09-20 00:32 UTC | 3h 0m |
| N11179 |  | Auburn Municipal Airport (KAUN) | Lake Tahoe Airport (KTVL) | 2026-09-20 00:04 UTC | 2026-09-20 00:29 UTC | 25m |
| UPS5848 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Salt Lake City International Airport (KSLC) | 2026-09-19 21:15 UTC | 2026-09-20 00:23 UTC | 3h 8m |
| VAR497 | VAR | Phoenix Goodyear Airport (KGYR) | Lake Havasu City Airport (KHII) | 2026-09-19 22:48 UTC | 2026-09-20 00:14 UTC | 1h 26m |
| SKW4310 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | UT49 (UT49) | 2026-09-19 23:51 UTC | 2026-09-20 00:08 UTC | 17m |
| N816MS |  | Chino Airport (KCNO) | Big Bear City Airport (KL35) | 2026-09-19 23:39 UTC | 2026-09-20 00:08 UTC | 28m |
| KAI42 | KAI | Oakland San Francisco Bay Airport (KOAK) | Bangor International Airport (KBGR) | 2026-09-19 19:10 UTC | 2026-09-20 00:07 UTC | 4h 57m |
| ASA1062 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-09-19 23:42 UTC | 2026-09-20 00:04 UTC | 21m |
| ANZ028M | ANZ | Napier Airport (NZNR) | Mercer1 PDZ Airport (NZME) | 2026-09-19 23:18 UTC | 2026-09-20 00:03 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
