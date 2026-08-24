# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_01:31:00_UTC-green)

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

**Latest saved flight:** 2026-08-24 01:31:00 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 01:31:00 UTC

- **230,652** saved flights
- **71,161** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **230,652** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,781,032.4 tonnes** estimated CO2 emissions
- **161,219,268 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9252 |
| 2 | SkyWest Airlines | 8200 |
| 3 | EJA | 4471 |
| 4 | IndiGo | 3884 |
| 5 | American Airlines | 3783 |
| 6 | Southwest Airlines | 3569 |
| 7 | Delta Air Lines | 2953 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2223 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1958 |
| 12 | Lufthansa | 1874 |
| 13 | LXJ | 1823 |
| 14 | WIF | 1813 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1538 |
| 17 | AXM | 1523 |
| 18 | EJU | 1470 |
| 19 | United Airlines | 1469 |
| 20 | QLK | 1454 |
| 21 | Alaska Airlines | 1390 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1289 |
| 24 | VIV | 1269 |
| 25 | WMT | 1262 |
| 26 | PGT | 1259 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1212 |
| 29 | JetBlue | 1149 |
| 30 | AEE | 1147 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192673 |
| 2 | 🇪🇸 ES | 14784 |
| 3 | 🇧🇷 BR | 13512 |
| 4 | 🇦🇺 AU | 13019 |
| 5 | 🇨🇦 CA | 12737 |
| 6 | 🇮🇹 IT | 12477 |
| 7 | 🇮🇳 IN | 12105 |
| 8 | 🇩🇪 DE | 11330 |
| 9 | 🇬🇧 GB | 10847 |
| 10 | 🇨🇴 CO | 9596 |
| 11 | 🇯🇵 JP | 9333 |
| 12 | 🇫🇷 FR | 9220 |
| 13 | 🇹🇷 TR | 6804 |
| 14 | 🇬🇷 GR | 6771 |
| 15 | 🇲🇽 MX | 6421 |
| 16 | 🇨🇭 CH | 6116 |
| 17 | 🇳🇴 NO | 5659 |
| 18 | 🇲🇾 MY | 4069 |
| 19 | 🇿🇦 ZA | 4015 |
| 20 | 🇹🇭 TH | 4001 |
| 21 | 🇵🇱 PL | 3827 |
| 22 | 🇳🇿 NZ | 3193 |
| 23 | 🇵🇭 PH | 3156 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2708 |
| 26 | 🇭🇷 HR | 2638 |
| 27 | 🇲🇦 MA | 2338 |
| 28 | 🇲🇪 ME | 2112 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 1984 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3756 |
| 3 | Indira Gandhi International Airport |  | IN | 2802 |
| 4 | Tokyo International Airport |  | JP | 2787 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2489 |
| 7 | Zurich Airport |  | CH | 2403 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2362 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2318 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2141 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2032 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1956 |
| 16 | Frankfurt am Main International Airport |  | DE | 1843 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1806 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1736 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1717 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1655 |
| 22 | Malpensa International Airport |  | IT | 1649 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1618 |
| 24 | Charles de Gaulle International Airport |  | FR | 1598 |
| 25 | Macau International Airport |  | MO | 1597 |
| 26 | Ninoy Aquino International Airport |  | PH | 1516 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1475 |
| 29 | Barcelona International Airport |  | ES | 1442 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1399 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Seattle-Tacoma International Airport |  | US | 1360 |
| 34 | Bengaluru International Airport |  | IN | 1358 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1355 |
| 36 | Calgary International Airport |  | CA | 1314 |
| 37 | Don Mueang International Airport |  | TH | 1308 |
| 38 | Oslo Gardermoen Airport |  | NO | 1283 |
| 39 | Vitoria/Foronda Airport |  | ES | 1252 |
| 40 | O. R. Tambo International Airport |  | ZA | 1250 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 840 | 21m | 244 km | 3,537.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 578 | 1h 6m | 770 km | 7,678.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 571 | 24m | 225 km | 2,215.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 353 | 1h 50m | 1,423 km | 8,663.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 298 | 24m | 218 km | 1,122.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 298 | 1h 38m | 1,156 km | 5,945.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 273 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 242 | 15m | 154 km | 641.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RAM799 | Royal Air Maroc | Bordeaux-Merignac (BA 106) Airport (LFBD) | Blaise Diagne International Airport (GOBD) | 2026-08-23 18:13 UTC | 2026-08-24 01:31 UTC | 7h 17m |
| N979AM |  | Artesia Municipal Airport (KATS) | Artesia Municipal Airport (KATS) | 2026-08-24 01:22 UTC | 2026-08-24 01:24 UTC | 2m |
| N54102 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-08-24 01:02 UTC | 2026-08-24 01:24 UTC | 22m |
| N1377M |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-24 00:50 UTC | 2026-08-24 01:20 UTC | 29m |
| N102AE |  | Antlers Municipal Airport (K80F) | Tinker Afb Airport (KTIK) | 2026-08-24 00:21 UTC | 2026-08-24 01:17 UTC | 56m |
| N320KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-24 00:16 UTC | 2026-08-24 01:12 UTC | 55m |
| ACA268 | Air Canada | Winnipeg James Armstrong Richardson International Airport (CYWG) | Toronto Pearson International Airport (CYYZ) | 2026-08-23 23:13 UTC | 2026-08-24 01:12 UTC | 1h 58m |
| N579WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-08-24 00:37 UTC | 2026-08-24 01:03 UTC | 25m |
| N968SR |  | Van Nuys Airport (KVNY) | San Francisco International Airport (KSFO) | 2026-08-24 00:08 UTC | 2026-08-24 01:00 UTC | 51m |
| MAFFS2 | MAF | Boise Air Trml/Gowen Field (KBOI) | Weiser Municipal Airport (KS87) | 2026-08-24 00:44 UTC | 2026-08-24 00:58 UTC | 14m |
| N671PC |  | Las Cruces International Airport (KLRU) | Grant County Airport (KSVC) | 2026-08-24 00:40 UTC | 2026-08-24 00:57 UTC | 17m |
| TKR910 | TKR | Quail Field (OG42) | Slinkard Airfield (WN31) | 2026-08-24 00:45 UTC | 2026-08-24 00:57 UTC | 11m |
| SXI | SXI | Cessnock Airport (YCNK) | Cessnock Airport (YCNK) | 2026-08-24 00:51 UTC | 2026-08-24 00:56 UTC | 4m |
| N213AN |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | San Martin Airport (KE16) | 2026-08-24 00:21 UTC | 2026-08-24 00:54 UTC | 32m |
| N677TX |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-24 00:19 UTC | 2026-08-24 00:53 UTC | 34m |
| N8467B |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-24 00:48 UTC | 2026-08-24 00:50 UTC | 2m |
| TRP1 | TRP | Martin State Airport (KMTN) | Kent Fort Manor Airport (7MD8) | 2026-08-24 00:33 UTC | 2026-08-24 00:44 UTC | 10m |
| N953LF |  | Des Moines International Airport (KDSM) | Iowa City Municipal Airport (KIOW) | 2026-08-24 00:01 UTC | 2026-08-24 00:44 UTC | 42m |
| N681DC |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-24 00:07 UTC | 2026-08-24 00:43 UTC | 36m |
| N184SF |  | Talladega Municipal Airport (KASN) | Anniston Regional Airport (KANB) | 2026-08-24 00:35 UTC | 2026-08-24 00:42 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
