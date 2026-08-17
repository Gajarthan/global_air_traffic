# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_09:41:13_UTC-green)

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

**Latest saved flight:** 2026-08-17 09:41:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 09:41:13 UTC

- **207,490** saved flights
- **66,008** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,490** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,495,204.4 tonnes** estimated CO2 emissions
- **144,649,530 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8186 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3547 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2667 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1757 |
| 12 | Vueling | 1720 |
| 13 | WIF | 1667 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1433 |
| 16 | Swiss International | 1381 |
| 17 | AXM | 1357 |
| 18 | United Airlines | 1305 |
| 19 | QLK | 1291 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1265 |
| 22 | All Nippon Airways | 1262 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | PGT | 1110 |
| 26 | Air France | 1106 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1059 |
| 29 | WMT | 1048 |
| 30 | Wizz Air | 1020 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176062 |
| 2 | 🇪🇸 ES | 13240 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11712 |
| 5 | 🇨🇦 CA | 11459 |
| 6 | 🇮🇳 IN | 11060 |
| 7 | 🇮🇹 IT | 10825 |
| 8 | 🇩🇪 DE | 10244 |
| 9 | 🇬🇧 GB | 9648 |
| 10 | 🇯🇵 JP | 8595 |
| 11 | 🇨🇴 CO | 8246 |
| 12 | 🇫🇷 FR | 8197 |
| 13 | 🇬🇷 GR | 6107 |
| 14 | 🇹🇷 TR | 5882 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5532 |
| 17 | 🇳🇴 NO | 5165 |
| 18 | 🇲🇾 MY | 3577 |
| 19 | 🇿🇦 ZA | 3470 |
| 20 | 🇵🇱 PL | 3414 |
| 21 | 🇹🇭 TH | 3310 |
| 22 | 🇳🇿 NZ | 2890 |
| 23 | 🇵🇭 PH | 2765 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2533 |
| 26 | 🇭🇷 HR | 2221 |
| 27 | 🇲🇦 MA | 2089 |
| 28 | 🇳🇱 NL | 1842 |
| 29 | 🇲🇪 ME | 1755 |
| 30 | 🇮🇩 ID | 1718 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2586 |
| 4 | Indira Gandhi International Airport |  | IN | 2511 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2163 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2163 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1921 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1856 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1711 |
| 17 | Madrid Barajas International Airport |  | ES | 1626 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1572 |
| 21 | Macau International Airport |  | MO | 1544 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1465 |
| 24 | Malpensa International Airport |  | IT | 1435 |
| 25 | Charles de Gaulle International Airport |  | FR | 1418 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1322 |
| 28 | Ninoy Aquino International Airport |  | PH | 1310 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1283 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1237 |
| 33 | Barcelona International Airport |  | ES | 1236 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Oslo Gardermoen Airport |  | NO | 1146 |
| 37 | Reno/Tahoe International Airport |  | US | 1143 |
| 38 | Vitoria/Foronda Airport |  | ES | 1143 |
| 39 | Daniel K Inouye International Airport |  | US | 1110 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1109 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 510 | 1h 7m | 770 km | 6,775.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 346 | 27m | 275 km | 1,639.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 304 | 44m | 241 km | 1,262.8 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 301 | 1h 49m | 1,423 km | 7,387.0 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 269 | 21m | 250 km | 1,161.9 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 261 | 24m | 218 km | 983.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 252 | 27m | 215 km | 933.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 246 | 1h 37m | 1,156 km | 4,907.6 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHOTH | FHO | Dreux Vernouillet Airport (LFON) | St Andre De L'eure Airport (LFFD) | 2026-08-17 08:46 UTC | 2026-08-17 09:41 UTC | 54m |
| BOMBERS1 | BOM | Son Bonet Airport (LESB) | Son Bonet Airport (LESB) | 2026-08-17 09:13 UTC | 2026-08-17 09:37 UTC | 23m |
| RMY7864 | RMY | Kuala Lumpur International Airport (WMKK) | Kota Kinabalu International Airport (WBKK) | 2026-08-17 07:14 UTC | 2026-08-17 09:23 UTC | 2h 8m |
| GDKSK | GDK | Deanland Lewes Airport (EGKL) | Bembridge Airport (EGHJ) | 2026-08-17 08:51 UTC | 2026-08-17 09:22 UTC | 31m |
| FHVDB | FHV | Nantes Atlantique Airport (LFRS) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-17 08:50 UTC | 2026-08-17 09:19 UTC | 28m |
| WMY | WMY | Tamworth Airport (YSTW) | Navarre Airport (YNVE) | 2026-08-17 07:43 UTC | 2026-08-17 09:15 UTC | 1h 31m |
| UAL980 | United Airlines | Chicago O'Hare International Airport (KORD) | Dublin Airport (EIDW) | 2026-08-17 02:18 UTC | 2026-08-17 09:01 UTC | 6h 43m |
| JUNO75 | JUN | Oakey Airport (YBOK) | Oakey Airport (YBOK) | 2026-08-17 08:59 UTC | 2026-08-17 09:00 UTC | 0m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-17 08:20 UTC | 2026-08-17 08:59 UTC | 38m |
| EFC69D | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 08:40 UTC | 2026-08-17 08:54 UTC | 14m |
| UBG218 | UBG | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-08-17 08:00 UTC | 2026-08-17 08:50 UTC | 49m |
| CYP4RD | CYP | Larnaca International Airport (LCLK) | Diagoras Airport (LGRP) | 2026-08-17 07:48 UTC | 2026-08-17 08:47 UTC | 58m |
| 5YZBJ |  | Kitui Airport (HKKU) | Narok Airport (HKNO) | 2026-08-17 07:12 UTC | 2026-08-17 08:46 UTC | 1h 34m |
| EAI21HA | EAI | Glasgow International Airport (EGPF) | Dublin Airport (EIDW) | 2026-08-17 07:48 UTC | 2026-08-17 08:46 UTC | 57m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-17 08:22 UTC | 2026-08-17 08:43 UTC | 21m |
| AWA445 | AWA | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-08-17 08:04 UTC | 2026-08-17 08:43 UTC | 38m |
| RYR59GQ | Ryanair | Torino / Caselle International Airport (LIMF) | Brac Airport (LDSB) | 2026-08-17 07:39 UTC | 2026-08-17 08:43 UTC | 1h 3m |
| N31 |  | Tampere-Pirkkala Airport (EFTP) | EFML (EFML) | 2026-08-17 07:33 UTC | 2026-08-17 08:42 UTC | 1h 9m |
| AXM6082 | AXM | Senai International Airport (WMKJ) | Jendarata Airport (WMAJ) | 2026-08-17 08:07 UTC | 2026-08-17 08:41 UTC | 34m |
| PGT1863 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-08-17 07:46 UTC | 2026-08-17 08:38 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
