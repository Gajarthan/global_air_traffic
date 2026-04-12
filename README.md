# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_15:23:14_UTC-green)

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

**Latest saved flight:** 2026-04-12 15:23:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 15:23:14 UTC

- **30,670** saved flights
- **13,982** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,670** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **376,230.0 tonnes** estimated CO2 emissions
- **21,810,433 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1279 |
| 2 | SkyWest Airlines | 1233 |
| 3 | IndiGo | 802 |
| 4 | American Airlines | 527 |
| 5 | EJA | 524 |
| 6 | Southwest Airlines | 437 |
| 7 | ENY | 411 |
| 8 | Lufthansa | 365 |
| 9 | AXM | 335 |
| 10 | Vueling | 318 |
| 11 | LATAM Airlines | 304 |
| 12 | All Nippon Airways | 286 |
| 13 | AZU | 268 |
| 14 | QLK | 260 |
| 15 | Delta Air Lines | 249 |
| 16 | LXJ | 242 |
| 17 | Swiss International | 228 |
| 18 | easyJet | 202 |
| 19 | Alaska Airlines | 201 |
| 20 | EJU | 201 |
| 21 | VIV | 198 |
| 22 | Japan Airlines | 197 |
| 23 | WIF | 197 |
| 24 | AEE | 193 |
| 25 | EDV | 180 |
| 26 | United Airlines | 179 |
| 27 | Avianca | 167 |
| 28 | GLO | 165 |
| 29 | Air France | 164 |
| 30 | AIQ | 163 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 24010 |
| 2 | 🇮🇳 IN | 2464 |
| 3 | 🇪🇸 ES | 2287 |
| 4 | 🇦🇺 AU | 2172 |
| 5 | 🇧🇷 BR | 1785 |
| 6 | 🇯🇵 JP | 1711 |
| 7 | 🇮🇹 IT | 1601 |
| 8 | 🇩🇪 DE | 1547 |
| 9 | 🇨🇴 CO | 1536 |
| 10 | 🇨🇦 CA | 1483 |
| 11 | 🇬🇧 GB | 1240 |
| 12 | 🇫🇷 FR | 1132 |
| 13 | 🇲🇽 MX | 979 |
| 14 | 🇬🇷 GR | 879 |
| 15 | 🇨🇭 CH | 866 |
| 16 | 🇲🇾 MY | 807 |
| 17 | 🇳🇴 NO | 666 |
| 18 | 🇳🇿 NZ | 665 |
| 19 | 🇿🇦 ZA | 640 |
| 20 | 🇵🇭 PH | 575 |
| 21 | 🇹🇭 TH | 569 |
| 22 | 🇹🇷 TR | 559 |
| 23 | 🇬🇹 GT | 558 |
| 24 | 🇰🇷 KR | 531 |
| 25 | 🇵🇱 PL | 469 |
| 26 | 🇲🇦 MA | 395 |
| 27 | 🇧🇸 BS | 324 |
| 28 | 🇲🇪 ME | 309 |
| 29 | 🇮🇩 ID | 296 |
| 30 | 🇳🇱 NL | 295 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 726 |
| 2 | Tokyo International Airport |  | JP | 575 |
| 3 | El Dorado International Airport |  | CO | 545 |
| 4 | Indira Gandhi International Airport |  | IN | 518 |
| 5 | Denver International Airport |  | US | 513 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 430 |
| 7 | La Aurora Airport |  | GT | 399 |
| 8 | Harry Reid International Airport |  | US | 392 |
| 9 | Zurich Airport |  | CH | 376 |
| 10 | Guaymaral Airport |  | CO | 368 |
| 11 | Chicago O'Hare International Airport |  | US | 316 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 315 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 14 | Frankfurt am Main International Airport |  | DE | 310 |
| 15 | Kuala Lumpur International Airport |  | MY | 306 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 302 |
| 17 | Macau International Airport |  | MO | 290 |
| 18 | Bengaluru International Airport |  | IN | 280 |
| 19 | Charlotte/Douglas International Airport |  | US | 274 |
| 20 | Tenerife Norte Airport |  | ES | 273 |
| 21 | Madrid Barajas International Airport |  | ES | 271 |
| 22 | Ninoy Aquino International Airport |  | PH | 264 |
| 23 | Congonhas Airport |  | BR | 260 |
| 24 | Malpensa International Airport |  | IT | 249 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 235 |
| 26 | Daniel K Inouye International Airport |  | US | 232 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 222 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 216 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 215 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 214 |
| 33 | Capua Airport |  | IT | 209 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 207 |
| 35 | O. R. Tambo International Airport |  | ZA | 206 |
| 36 | Miami International Airport |  | US | 204 |
| 37 | Vitoria/Foronda Airport |  | ES | 203 |
| 38 | Barcelona International Airport |  | ES | 196 |
| 39 | Seattle-Tacoma International Airport |  | US | 192 |
| 40 | Don Mueang International Airport |  | TH | 192 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 145 | 1h 8m | 706 km | 1,765.4 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 143 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 127 | 14m | 114 km | 249.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 104 | 28m | 304 km | 545.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 81 | 19m | 165 km | 230.4 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 75 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 70 | 55m | 546 km | 659.1 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 67 | 9m | - | - |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 66 | 27m | 275 km | 312.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 60 | 31m | 369 km | 381.9 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 55 | 21m | 244 km | 231.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 52 | 20m | 250 km | 224.6 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 48 | 20m | 147 km | 121.5 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 43 | 14m | 154 km | 113.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 42 | 12m | 15 km | 11.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N230WA |  | Richmond Executive/Chesterfield County Airport (KFCI) | Richmond Executive/Chesterfield County Airport (KFCI) | 2026-04-12 14:41 UTC | 2026-04-12 15:23 UTC | 41m |
| N8EF |  | Northwest Alabama Regional Airport (KMSL) | Auburn University Regional Airport (KAUO) | 2026-04-12 14:37 UTC | 2026-04-12 15:18 UTC | 41m |
| N336BG |  | Wood County Airport (K1G0) | James M Cox Dayton International Airport (KDAY) | 2026-04-12 14:07 UTC | 2026-04-12 15:16 UTC | 1h 8m |
| N56578 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-04-12 14:49 UTC | 2026-04-12 15:13 UTC | 24m |
| CXK126 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-12 14:34 UTC | 2026-04-12 15:12 UTC | 37m |
| DEXCC | DEX | Juist Airport (EDWJ) | Wilhelmshaven-Mariensiel Airport (EDWI) | 2026-04-12 14:40 UTC | 2026-04-12 15:10 UTC | 29m |
| N480LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-12 14:23 UTC | 2026-04-12 15:09 UTC | 46m |
| N224TB |  | St Pete-Clearwater International Airport (KPIE) | Southwest Florida International Airport (KRSW) | 2026-04-12 13:48 UTC | 2026-04-12 15:08 UTC | 1h 19m |
| SWA4597 | Southwest Airlines | Tucson International Airport (KTUS) | Denver International Airport (KDEN) | 2026-04-12 13:44 UTC | 2026-04-12 15:07 UTC | 1h 23m |
| CLX4806 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-04-12 04:05 UTC | 2026-04-12 15:04 UTC | 10h 59m |
| N12064 |  | Clermont County Airport (KI69) | Clermont County Airport (KI69) | 2026-04-12 14:26 UTC | 2026-04-12 15:02 UTC | 36m |
| RYR4PJ | Ryanair | Eleftherios Venizelos International Airport (LGAV) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 12:45 UTC | 2026-04-12 14:55 UTC | 2h 10m |
| LAP1304 | LAP | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Rosario Airport (SGRO) | 2026-04-12 13:22 UTC | 2026-04-12 14:55 UTC | 1h 33m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-12 14:30 UTC | 2026-04-12 14:52 UTC | 21m |
| LXJ406 | LXJ | Boca Raton Airport (KBCT) | Teterboro Airport (KTEB) | 2026-04-12 12:12 UTC | 2026-04-12 14:51 UTC | 2h 38m |
| N146DM |  | Eulogio Sanchez Airport (SCTB) | Chicureo Airport (SCHC) | 2026-04-12 14:31 UTC | 2026-04-12 14:50 UTC | 18m |
| N930RD |  | K8A0 (K8A0) | Branhams Airport (K6J7) | 2026-04-12 13:47 UTC | 2026-04-12 14:49 UTC | 1h 1m |
| N357EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-12 14:01 UTC | 2026-04-12 14:48 UTC | 47m |
| N69P |  | Montgomery-Gibbs Executive Airport (KMYF) | Ohkay Owingeh Airport (KE14) | 2026-04-12 12:40 UTC | 2026-04-12 14:41 UTC | 2h 0m |
| N6018F |  | Morristown Municipal Airport (KMMU) | Morristown Municipal Airport (KMMU) | 2026-04-12 14:32 UTC | 2026-04-12 14:38 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
