# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_06:53:54_UTC-green)

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

**Latest saved flight:** 2026-08-18 06:53:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 06:53:54 UTC

- **211,029** saved flights
- **67,057** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,029** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,536,746.4 tonnes** estimated CO2 emissions
- **147,057,763 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8343 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3594 |
| 5 | American Airlines | 3533 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1912 |
| 11 | Lufthansa | 1771 |
| 12 | Vueling | 1754 |
| 13 | WIF | 1694 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1406 |
| 17 | AXM | 1374 |
| 18 | United Airlines | 1340 |
| 19 | QLK | 1315 |
| 20 | Alaska Airlines | 1301 |
| 21 | EJU | 1287 |
| 22 | All Nippon Airways | 1281 |
| 23 | VIV | 1164 |
| 24 | GLO | 1139 |
| 25 | Air France | 1133 |
| 26 | PGT | 1128 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1071 |
| 29 | AEE | 1069 |
| 30 | Wizz Air | 1045 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178865 |
| 2 | 🇪🇸 ES | 13467 |
| 3 | 🇧🇷 BR | 12095 |
| 4 | 🇦🇺 AU | 11906 |
| 5 | 🇨🇦 CA | 11686 |
| 6 | 🇮🇳 IN | 11215 |
| 7 | 🇮🇹 IT | 11021 |
| 8 | 🇩🇪 DE | 10391 |
| 9 | 🇬🇧 GB | 9816 |
| 10 | 🇯🇵 JP | 8738 |
| 11 | 🇨🇴 CO | 8483 |
| 12 | 🇫🇷 FR | 8360 |
| 13 | 🇬🇷 GR | 6188 |
| 14 | 🇹🇷 TR | 6008 |
| 15 | 🇲🇽 MX | 5929 |
| 16 | 🇨🇭 CH | 5591 |
| 17 | 🇳🇴 NO | 5244 |
| 18 | 🇲🇾 MY | 3622 |
| 19 | 🇿🇦 ZA | 3533 |
| 20 | 🇵🇱 PL | 3484 |
| 21 | 🇹🇭 TH | 3383 |
| 22 | 🇳🇿 NZ | 2941 |
| 23 | 🇵🇭 PH | 2801 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2571 |
| 26 | 🇭🇷 HR | 2264 |
| 27 | 🇲🇦 MA | 2123 |
| 28 | 🇳🇱 NL | 1875 |
| 29 | 🇲🇪 ME | 1795 |
| 30 | 🇮🇩 ID | 1748 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4447 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2622 |
| 4 | Indira Gandhi International Airport |  | IN | 2557 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2373 |
| 7 | Zurich Airport |  | CH | 2194 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1938 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1725 |
| 17 | Madrid Barajas International Airport |  | ES | 1647 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1587 |
| 21 | Macau International Airport |  | MO | 1548 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1486 |
| 24 | Malpensa International Airport |  | IT | 1459 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1339 |
| 28 | Ninoy Aquino International Airport |  | PH | 1327 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1294 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1267 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1162 |
| 37 | Vitoria/Foronda Airport |  | ES | 1161 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1135 |
| 40 | Daniel K Inouye International Airport |  | US | 1124 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 750 | 21m | 244 km | 3,158.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 519 | 1h 7m | 770 km | 6,894.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 490 | 24m | 225 km | 1,901.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 351 | 27m | 275 km | 1,663.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 347 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 310 | 1h 49m | 1,423 km | 7,607.9 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 253 | 1h 37m | 1,156 km | 5,047.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 241 | 31m | 369 km | 1,534.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R21200 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-18 05:48 UTC | 2026-08-18 06:53 UTC | 1h 5m |
| CFG6AL | CFG | Hamburg Airport (EDDH) | Frankfurt am Main International Airport (EDDF) | 2026-08-18 06:00 UTC | 2026-08-18 06:44 UTC | 44m |
| DKAGX | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-08-18 06:15 UTC | 2026-08-18 06:42 UTC | 26m |
| BPO312 | BPO | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-08-18 06:24 UTC | 2026-08-18 06:41 UTC | 16m |
| BBC388 | BBC | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-18 05:34 UTC | 2026-08-18 06:21 UTC | 46m |
| AUA26K | Austrian Airlines | Vienna International Airport (LOWW) | Stuttgart Airport (EDDS) | 2026-08-18 05:13 UTC | 2026-08-18 06:11 UTC | 58m |
| XCN70 | XCN | Ephrata Municipal Airport (KEPH) | Ross Airport (32WA) | 2026-08-18 05:04 UTC | 2026-08-18 06:08 UTC | 1h 3m |
| LAN809 | LAN | Comodoro Arturo Merino Benitez International Airport (SCEL) | Palo Alto Airport (SCAO) | 2026-08-18 05:52 UTC | 2026-08-18 06:06 UTC | 14m |
| QLK106D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Nambucca Heads Airport (YNHS) | 2026-08-18 05:22 UTC | 2026-08-18 06:04 UTC | 41m |
| AIQ1040 | AIQ | Don Mueang International Airport (VTBD) | Xieng Khouang Airport (VLXK) | 2026-08-18 05:21 UTC | 2026-08-18 06:04 UTC | 42m |
| RYR7273 | Ryanair | John Paul II International Airport Kraków-Balice Airport (EPKK) | Otocac Airport (LDRO) | 2026-08-18 05:12 UTC | 2026-08-18 06:04 UTC | 51m |
| RYR7FM | Ryanair | Brussels South Charleroi Airport (EBCI) | Figari Sud-Corse Airport (LFKF) | 2026-08-18 04:43 UTC | 2026-08-18 06:03 UTC | 1h 20m |
| ZSMFS | ZSM | Rand Airport (FAGM) | Rooiberg Airport (FARO) | 2026-08-18 05:29 UTC | 2026-08-18 06:02 UTC | 33m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-08-18 05:20 UTC | 2026-08-18 06:00 UTC | 40m |
| WIF8HM | WIF | Bergen Airport Flesland (ENBR) | Ålesund Airport (ENAL) | 2026-08-18 05:30 UTC | 2026-08-18 06:00 UTC | 30m |
| RXA6436 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Nambucca Heads Airport (YNHS) | 2026-08-18 05:04 UTC | 2026-08-18 05:57 UTC | 53m |
| QLK380D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-18 05:31 UTC | 2026-08-18 05:56 UTC | 24m |
| RYR205A | Ryanair | Vienna International Airport (LOWW) | Barcelona International Airport (LEBL) | 2026-08-18 03:56 UTC | 2026-08-18 05:54 UTC | 1h 58m |
| WIF5DB | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-08-18 05:33 UTC | 2026-08-18 05:54 UTC | 20m |
| APG227 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-18 05:29 UTC | 2026-08-18 05:54 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
