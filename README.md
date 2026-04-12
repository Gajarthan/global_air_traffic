# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_13:47:34_UTC-green)

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

**Latest saved flight:** 2026-04-12 13:47:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 13:47:34 UTC

- **30,489** saved flights
- **13,918** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,489** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **373,634.6 tonnes** estimated CO2 emissions
- **21,659,974 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1267 |
| 2 | SkyWest Airlines | 1230 |
| 3 | IndiGo | 800 |
| 4 | American Airlines | 524 |
| 5 | EJA | 524 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 364 |
| 9 | AXM | 334 |
| 10 | Vueling | 315 |
| 11 | LATAM Airlines | 301 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 265 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 247 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 225 |
| 18 | Alaska Airlines | 201 |
| 19 | EJU | 201 |
| 20 | easyJet | 201 |
| 21 | Japan Airlines | 197 |
| 22 | VIV | 196 |
| 23 | WIF | 194 |
| 24 | AEE | 193 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | Air France | 163 |
| 29 | AIQ | 162 |
| 30 | GLO | 162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23888 |
| 2 | 🇮🇳 IN | 2451 |
| 3 | 🇪🇸 ES | 2263 |
| 4 | 🇦🇺 AU | 2170 |
| 5 | 🇧🇷 BR | 1757 |
| 6 | 🇯🇵 JP | 1710 |
| 7 | 🇮🇹 IT | 1587 |
| 8 | 🇩🇪 DE | 1537 |
| 9 | 🇨🇴 CO | 1528 |
| 10 | 🇨🇦 CA | 1478 |
| 11 | 🇬🇧 GB | 1232 |
| 12 | 🇫🇷 FR | 1126 |
| 13 | 🇲🇽 MX | 975 |
| 14 | 🇬🇷 GR | 874 |
| 15 | 🇨🇭 CH | 857 |
| 16 | 🇲🇾 MY | 804 |
| 17 | 🇳🇿 NZ | 665 |
| 18 | 🇳🇴 NO | 654 |
| 19 | 🇿🇦 ZA | 630 |
| 20 | 🇵🇭 PH | 573 |
| 21 | 🇹🇭 TH | 567 |
| 22 | 🇹🇷 TR | 555 |
| 23 | 🇬🇹 GT | 553 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 462 |
| 26 | 🇲🇦 MA | 393 |
| 27 | 🇧🇸 BS | 319 |
| 28 | 🇲🇪 ME | 308 |
| 29 | 🇮🇩 ID | 296 |
| 30 | 🇳🇱 NL | 293 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 722 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 545 |
| 4 | Indira Gandhi International Airport |  | IN | 514 |
| 5 | Denver International Airport |  | US | 512 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 428 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 392 |
| 9 | Zurich Airport |  | CH | 370 |
| 10 | Guaymaral Airport |  | CO | 362 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 308 |
| 15 | Kuala Lumpur International Airport |  | MY | 305 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 301 |
| 17 | Macau International Airport |  | MO | 289 |
| 18 | Bengaluru International Airport |  | IN | 277 |
| 19 | Charlotte/Douglas International Airport |  | US | 271 |
| 20 | Tenerife Norte Airport |  | ES | 268 |
| 21 | Madrid Barajas International Airport |  | ES | 266 |
| 22 | Ninoy Aquino International Airport |  | PH | 263 |
| 23 | Congonhas Airport |  | BR | 257 |
| 24 | Malpensa International Airport |  | IT | 247 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 232 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 221 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 213 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 212 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 209 |
| 33 | Capua Airport |  | IT | 209 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 204 |
| 35 | Miami International Airport |  | US | 203 |
| 36 | O. R. Tambo International Airport |  | ZA | 202 |
| 37 | Vitoria/Foronda Airport |  | ES | 200 |
| 38 | Barcelona International Airport |  | ES | 194 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 191 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 140 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 127 | 14m | 114 km | 249.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 80 | 19m | 165 km | 227.6 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 14 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 64 | 27m | 275 km | 303.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 55 | 21m | 244 km | 231.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 51 | 20m | 250 km | 220.3 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 43 | 1h 21m | 961 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N66VM |  | Dayton/Wright Brothers Airport (KMGY) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-12 13:20 UTC | 2026-04-12 13:47 UTC | 27m |
| FJO66L | FJO | London City Airport (EGLC) | Zurich Airport (LSZH) | 2026-04-12 12:18 UTC | 2026-04-12 13:44 UTC | 1h 25m |
| N21725 |  | 6PA6 (6PA6) | 1NK0 (1NK0) | 2026-04-12 12:10 UTC | 2026-04-12 13:42 UTC | 1h 31m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-04-12 12:49 UTC | 2026-04-12 13:38 UTC | 48m |
| DFEEL | DFE | Nuremberg Airport (EDDN) | Siegerland Airport (EDGS) | 2026-04-12 12:29 UTC | 2026-04-12 13:36 UTC | 1h 6m |
| N487ER |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-12 13:10 UTC | 2026-04-12 13:35 UTC | 24m |
| N55VY |  | Sugar Loaf Shores Airport (7FA1) | Witham Field (KSUA) | 2026-04-12 12:58 UTC | 2026-04-12 13:33 UTC | 35m |
| N183TS |  | Columbus Airport (KCSG) | Nashville International Airport (KBNA) | 2026-04-12 12:39 UTC | 2026-04-12 13:32 UTC | 52m |
| UAE380 | Emirates | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-04-12 07:11 UTC | 2026-04-12 13:30 UTC | 6h 19m |
| N65329 |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-04-12 13:25 UTC | 2026-04-12 13:28 UTC | 3m |
| N710CA |  | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-04-12 13:01 UTC | 2026-04-12 13:22 UTC | 20m |
| ERU483 | ERU | KXFL (KXFL) | Skinners Wholesale Nursery Airport (16FD) | 2026-04-12 13:13 UTC | 2026-04-12 13:16 UTC | 3m |
| N5253A |  | Sidney Municipal Airport (KN23) | 1NK0 (1NK0) | 2026-04-12 12:57 UTC | 2026-04-12 13:13 UTC | 16m |
| RYR11QJ | Ryanair | Madrid Barajas International Airport (LEMD) | Malpensa International Airport (LIMC) | 2026-04-12 11:33 UTC | 2026-04-12 13:13 UTC | 1h 39m |
| N584S |  | Fort Meade Executive Airport (KFME) | Cambridge-Dorchester Regional Airport (KCGE) | 2026-04-12 12:50 UTC | 2026-04-12 13:13 UTC | 22m |
|  |  | Dallas-Fort Worth International Airport (KDFW) | Dallas-Fort Worth International Airport (KDFW) | 2026-04-12 13:09 UTC | 2026-04-12 13:12 UTC | 2m |
| N683TM |  | West Memphis Municipal Airport (KAWM) | Jonesboro Municipal Airport (KJBR) | 2026-04-12 12:46 UTC | 2026-04-12 13:08 UTC | 22m |
| N55458 |  | Groton-New London Airport (KGON) | RI20 (RI20) | 2026-04-12 12:33 UTC | 2026-04-12 13:08 UTC | 35m |
| N970MB |  | Boulder Municipal Airport (KBDU) | Athanasiou Valley Airport (CO07) | 2026-04-12 12:50 UTC | 2026-04-12 13:07 UTC | 17m |
| N916PC |  | Tampa International Airport (KTPA) | Mobile International Airport (KBFM) | 2026-04-12 12:08 UTC | 2026-04-12 13:05 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
