# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_16:35:16_UTC-green)

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

**Latest saved flight:** 2026-08-16 16:35:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 16:35:16 UTC

- **205,174** saved flights
- **65,510** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,174** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,466,433.3 tonnes** estimated CO2 emissions
- **142,981,641 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8085 |
| 2 | SkyWest Airlines | 7362 |
| 3 | EJA | 3968 |
| 4 | IndiGo | 3513 |
| 5 | American Airlines | 3407 |
| 6 | Southwest Airlines | 3309 |
| 7 | Delta Air Lines | 2626 |
| 8 | ENY | 2553 |
| 9 | LATAM Airlines | 1924 |
| 10 | AZU | 1854 |
| 11 | Lufthansa | 1746 |
| 12 | Vueling | 1700 |
| 13 | WIF | 1653 |
| 14 | LXJ | 1614 |
| 15 | easyJet | 1419 |
| 16 | Swiss International | 1371 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1293 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1256 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1126 |
| 24 | GLO | 1103 |
| 25 | Air France | 1097 |
| 26 | PGT | 1095 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1049 |
| 29 | WMT | 1032 |
| 30 | CXK | 1014 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174233 |
| 2 | 🇪🇸 ES | 13131 |
| 3 | 🇧🇷 BR | 11733 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11310 |
| 6 | 🇮🇳 IN | 10964 |
| 7 | 🇮🇹 IT | 10685 |
| 8 | 🇩🇪 DE | 10159 |
| 9 | 🇬🇧 GB | 9583 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇫🇷 FR | 8133 |
| 12 | 🇨🇴 CO | 8106 |
| 13 | 🇬🇷 GR | 6047 |
| 14 | 🇹🇷 TR | 5800 |
| 15 | 🇲🇽 MX | 5756 |
| 16 | 🇨🇭 CH | 5495 |
| 17 | 🇳🇴 NO | 5121 |
| 18 | 🇲🇾 MY | 3528 |
| 19 | 🇿🇦 ZA | 3448 |
| 20 | 🇵🇱 PL | 3387 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2577 |
| 25 | 🇰🇷 KR | 2504 |
| 26 | 🇭🇷 HR | 2195 |
| 27 | 🇲🇦 MA | 2068 |
| 28 | 🇳🇱 NL | 1835 |
| 29 | 🇲🇪 ME | 1721 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4297 |
| 2 | Denver International Airport |  | US | 3344 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Guaymaral Airport |  | CO | 2486 |
| 5 | Indira Gandhi International Airport |  | IN | 2485 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2146 |
| 8 | Zurich Airport |  | CH | 2144 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2127 |
| 10 | La Aurora Airport |  | GT | 1970 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1870 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1828 |
| 14 | Salt Lake City International Airport |  | US | 1811 |
| 15 | Congonhas Airport |  | BR | 1709 |
| 16 | Frankfurt am Main International Airport |  | DE | 1702 |
| 17 | Madrid Barajas International Airport |  | ES | 1610 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1567 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1558 |
| 20 | Capua Airport |  | IT | 1556 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1483 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1413 |
| 25 | Charles de Gaulle International Airport |  | FR | 1406 |
| 26 | Charlotte/Douglas International Airport |  | US | 1395 |
| 27 | Kuala Lumpur International Airport |  | MY | 1308 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1275 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1260 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1233 |
| 32 | Barcelona International Airport |  | ES | 1225 |
| 33 | Seattle-Tacoma International Airport |  | US | 1216 |
| 34 | Viracopos International Airport |  | BR | 1188 |
| 35 | Calgary International Airport |  | CA | 1159 |
| 36 | Reno/Tahoe International Airport |  | US | 1136 |
| 37 | Oslo Gardermoen Airport |  | NO | 1135 |
| 38 | Vitoria/Foronda Airport |  | ES | 1133 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1023 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 388 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 256 | 24m | 218 km | 964.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 246 | 19m | 99 km | 421.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 241 | 1h 37m | 1,156 km | 4,807.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 221 | 1h 49m | 1,304 km | 4,971.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 218 | 28m | 152 km | 569.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N689EE |  | Dekalb-Peachtree Airport (KPDK) | Smith Field (GE27) | 2026-08-16 16:07 UTC | 2026-08-16 16:35 UTC | 27m |
| N169BA |  | Songbird Ranch Airport (91TS) | Bb Airpark (TE88) | 2026-08-16 15:54 UTC | 2026-08-16 16:33 UTC | 38m |
| N998RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Oswego County Airport (KFZY) | 2026-08-16 15:52 UTC | 2026-08-16 16:30 UTC | 38m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-16 16:12 UTC | 2026-08-16 16:29 UTC | 16m |
| LDX11C | LDX | Barcelona International Airport (LEBL) | Zurich Airport (LSZH) | 2026-08-16 14:56 UTC | 2026-08-16 16:23 UTC | 1h 27m |
| N4928E |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-16 15:55 UTC | 2026-08-16 16:15 UTC | 20m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-16 15:49 UTC | 2026-08-16 16:08 UTC | 18m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-16 15:52 UTC | 2026-08-16 16:07 UTC | 14m |
| N719KS |  | Rocky Mountain Metro Airport (KBJC) | 1CO7 (1CO7) | 2026-08-16 14:26 UTC | 2026-08-16 16:05 UTC | 1h 39m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-16 15:41 UTC | 2026-08-16 16:05 UTC | 23m |
| APJ808 | APJ | Incheon International Airport (RKSI) | Tokyo International Airport (RJTT) | 2026-08-16 14:22 UTC | 2026-08-16 16:04 UTC | 1h 42m |
| N135RF |  | Daulton Airport (77CA) | Lee Vining Airport (KO24) | 2026-08-16 15:34 UTC | 2026-08-16 16:03 UTC | 28m |
| TCERB | TCE | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-08-16 15:11 UTC | 2026-08-16 16:00 UTC | 49m |
| N54HA |  | Chicago Executive Airport (KPWK) | Dreamcatcher Airport (2MN2) | 2026-08-16 15:00 UTC | 2026-08-16 15:58 UTC | 57m |
| ENSAIO63 | ENS | Professor Urbano Ernesto Stumpf Airport (SBSJ) | Helibras Airport (SIYS) | 2026-08-16 14:31 UTC | 2026-08-16 15:58 UTC | 1h 26m |
| CXK426 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-16 15:03 UTC | 2026-08-16 15:57 UTC | 54m |
| N75HF |  | Willow Run Airport (KYIP) | Lonesome Pine Airport (KLNP) | 2026-08-16 15:08 UTC | 2026-08-16 15:57 UTC | 49m |
| TGRWC | TGR | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-16 15:35 UTC | 2026-08-16 15:57 UTC | 21m |
| N444XT |  | Dayton/Wright Brothers Airport (KMGY) | London/Corbin/Magee Airport (KLOZ) | 2026-08-16 15:29 UTC | 2026-08-16 15:56 UTC | 27m |
| N68SL |  | Fort Worth Meacham International Airport (KFTW) | Spokane International Airport (KGEG) | 2026-08-16 12:47 UTC | 2026-08-16 15:53 UTC | 3h 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
