# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_15:45:25_UTC-green)

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

**Latest saved flight:** 2026-08-15 15:45:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 15:45:25 UTC

- **198,868** saved flights
- **62,161** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,868** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,375,402.8 tonnes** estimated CO2 emissions
- **137,704,507 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7913 |
| 2 | SkyWest Airlines | 7118 |
| 3 | EJA | 3901 |
| 4 | IndiGo | 3441 |
| 5 | Southwest Airlines | 3074 |
| 6 | American Airlines | 3056 |
| 7 | ENY | 2452 |
| 8 | Delta Air Lines | 2352 |
| 9 | LATAM Airlines | 1870 |
| 10 | AZU | 1807 |
| 11 | Lufthansa | 1702 |
| 12 | Vueling | 1670 |
| 13 | WIF | 1639 |
| 14 | LXJ | 1573 |
| 15 | easyJet | 1366 |
| 16 | Swiss International | 1345 |
| 17 | AXM | 1307 |
| 18 | EJU | 1231 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1096 |
| 23 | GLO | 1081 |
| 24 | Air France | 1053 |
| 25 | PGT | 1048 |
| 26 | AEE | 1024 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1007 |
| 29 | WMT | 1003 |
| 30 | Wizz Air | 984 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168487 |
| 2 | 🇪🇸 ES | 12843 |
| 3 | 🇧🇷 BR | 11474 |
| 4 | 🇦🇺 AU | 11146 |
| 5 | 🇨🇦 CA | 10861 |
| 6 | 🇮🇳 IN | 10749 |
| 7 | 🇮🇹 IT | 10419 |
| 8 | 🇩🇪 DE | 9874 |
| 9 | 🇬🇧 GB | 9354 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7927 |
| 12 | 🇨🇴 CO | 7865 |
| 13 | 🇬🇷 GR | 5867 |
| 14 | 🇲🇽 MX | 5617 |
| 15 | 🇹🇷 TR | 5502 |
| 16 | 🇨🇭 CH | 5397 |
| 17 | 🇳🇴 NO | 5073 |
| 18 | 🇲🇾 MY | 3427 |
| 19 | 🇿🇦 ZA | 3364 |
| 20 | 🇵🇱 PL | 3290 |
| 21 | 🇹🇭 TH | 3129 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2542 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2108 |
| 27 | 🇲🇦 MA | 2015 |
| 28 | 🇳🇱 NL | 1789 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4127 |
| 2 | Denver International Airport |  | US | 3226 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2452 |
| 5 | Indira Gandhi International Airport |  | IN | 2436 |
| 6 | Harry Reid International Airport |  | US | 2270 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2103 |
| 8 | Zurich Airport |  | CH | 2103 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2054 |
| 10 | La Aurora Airport |  | GT | 1948 |
| 11 | El Dorado International Airport |  | CO | 1827 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1766 |
| 13 | Salt Lake City International Airport |  | US | 1762 |
| 14 | Chicago O'Hare International Airport |  | US | 1738 |
| 15 | Congonhas Airport |  | BR | 1679 |
| 16 | Frankfurt am Main International Airport |  | DE | 1675 |
| 17 | Madrid Barajas International Airport |  | ES | 1565 |
| 18 | Macau International Airport |  | MO | 1535 |
| 19 | Capua Airport |  | IT | 1520 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1511 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1461 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1435 |
| 23 | Malpensa International Airport |  | IT | 1385 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 25 | Charles de Gaulle International Airport |  | FR | 1368 |
| 26 | Charlotte/Douglas International Airport |  | US | 1311 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1255 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1241 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1198 |
| 33 | Viracopos International Airport |  | BR | 1161 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1118 |
| 37 | Reno/Tahoe International Airport |  | US | 1117 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1096 |
| 40 | Tenerife Norte Airport |  | ES | 1090 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1010 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 363 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 334 | 27m | 275 km | 1,582.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 290 | 1h 49m | 1,423 km | 7,117.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 283 | 22m | 55 km | 269.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 243 | 19m | 99 km | 416.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 242 | 1h 15m | 961 km | 4,011.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 237 | 1h 38m | 1,156 km | 4,728.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 215 | 1h 3m | 695 km | 2,577.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5229H |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-08-15 15:19 UTC | 2026-08-15 15:45 UTC | 25m |
| N895CA |  | Mesa Gateway Airport (KIWA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-15 15:26 UTC | 2026-08-15 15:42 UTC | 16m |
| N64364 |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-15 15:25 UTC | 2026-08-15 15:42 UTC | 16m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-15 14:48 UTC | 2026-08-15 15:39 UTC | 51m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-15 14:53 UTC | 2026-08-15 15:37 UTC | 44m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-15 15:13 UTC | 2026-08-15 15:35 UTC | 22m |
| N153KD |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-15 14:22 UTC | 2026-08-15 15:33 UTC | 1h 10m |
| IDPCY | IDP | Trieste / Ronchi Dei Legionari (LIPQ) | Udine / Campoformido Air Base (LIPD) | 2026-08-15 15:13 UTC | 2026-08-15 15:29 UTC | 16m |
| N3TY |  | Reno/Tahoe International Airport (KRNO) | NV13 (NV13) | 2026-08-15 15:01 UTC | 2026-08-15 15:23 UTC | 22m |
| N330V |  | Kintail Farm Airport (GA00) | Kintail Farm Airport (GA00) | 2026-08-15 15:09 UTC | 2026-08-15 15:21 UTC | 11m |
| DRAG172 | DRA | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-08-15 14:41 UTC | 2026-08-15 15:17 UTC | 36m |
|  |  | Currituck County Regional Airport (KONX) | Currituck County Regional Airport (KONX) | 2026-08-15 15:16 UTC | 2026-08-15 15:16 UTC | 0m |
| LTA906 | LTA | K41A (K41A) | K41A (K41A) | 2026-08-15 14:41 UTC | 2026-08-15 15:14 UTC | 32m |
| N8454H |  | Old Bridge Airport (K3N6) | Monmouth Executive Airport (KBLM) | 2026-08-15 14:47 UTC | 2026-08-15 15:13 UTC | 26m |
| N212GS |  | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-08-15 15:07 UTC | 2026-08-15 15:12 UTC | 4m |
| 310NR |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-15 15:11 UTC | 2026-08-15 15:11 UTC | 0m |
| N46132 |  | Preston Airport (KU10) | Logan-Cache Airport (KLGU) | 2026-08-15 14:58 UTC | 2026-08-15 15:09 UTC | 10m |
| TGPWO | TGP | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-15 14:45 UTC | 2026-08-15 15:08 UTC | 23m |
| GBFBR | GBF | RNAS Lee-On-Solent (EGHF) | RNAS Lee-On-Solent (EGHF) | 2026-08-15 14:53 UTC | 2026-08-15 15:08 UTC | 14m |
|  |  | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-14 20:44 UTC | 2026-08-15 15:03 UTC | 18h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
