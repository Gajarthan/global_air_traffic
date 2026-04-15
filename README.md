# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_22:41:29_UTC-green)

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

**Latest saved flight:** 2026-04-15 22:41:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 22:41:29 UTC

- **36,713** saved flights
- **15,992** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **36,713** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **445,479.0 tonnes** estimated CO2 emissions
- **25,824,867 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1561 |
| 2 | SkyWest Airlines | 1454 |
| 3 | IndiGo | 906 |
| 4 | EJA | 628 |
| 5 | American Airlines | 620 |
| 6 | Southwest Airlines | 516 |
| 7 | ENY | 484 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 383 |
| 10 | LATAM Airlines | 374 |
| 11 | Vueling | 370 |
| 12 | AZU | 327 |
| 13 | All Nippon Airways | 321 |
| 14 | Delta Air Lines | 313 |
| 15 | QLK | 302 |
| 16 | LXJ | 292 |
| 17 | Swiss International | 277 |
| 18 | WIF | 272 |
| 19 | AEE | 247 |
| 20 | Alaska Airlines | 244 |
| 21 | easyJet | 242 |
| 22 | EJU | 238 |
| 23 | VIV | 233 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 208 |
| 26 | EDV | 206 |
| 27 | United Airlines | 205 |
| 28 | GLO | 196 |
| 29 | JetBlue | 193 |
| 30 | AIQ | 191 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 28916 |
| 2 | 🇮🇳 IN | 2775 |
| 3 | 🇪🇸 ES | 2731 |
| 4 | 🇦🇺 AU | 2563 |
| 5 | 🇧🇷 BR | 2170 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1951 |
| 8 | 🇩🇪 DE | 1881 |
| 9 | 🇨🇦 CA | 1812 |
| 10 | 🇨🇴 CO | 1810 |
| 11 | 🇬🇧 GB | 1511 |
| 12 | 🇫🇷 FR | 1387 |
| 13 | 🇲🇽 MX | 1153 |
| 14 | 🇬🇷 GR | 1108 |
| 15 | 🇨🇭 CH | 1004 |
| 16 | 🇲🇾 MY | 930 |
| 17 | 🇳🇴 NO | 884 |
| 18 | 🇳🇿 NZ | 778 |
| 19 | 🇿🇦 ZA | 770 |
| 20 | 🇵🇭 PH | 689 |
| 21 | 🇹🇭 TH | 669 |
| 22 | 🇹🇷 TR | 664 |
| 23 | 🇬🇹 GT | 626 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 573 |
| 26 | 🇲🇦 MA | 465 |
| 27 | 🇳🇱 NL | 364 |
| 28 | 🇧🇸 BS | 356 |
| 29 | 🇲🇪 ME | 355 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 870 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 644 |
| 4 | Denver International Airport |  | US | 623 |
| 5 | Indira Gandhi International Airport |  | IN | 593 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 545 |
| 7 | Harry Reid International Airport |  | US | 482 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 369 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 369 |
| 13 | Chicago O'Hare International Airport |  | US | 361 |
| 14 | Kuala Lumpur International Airport |  | MY | 361 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 340 |
| 17 | Madrid Barajas International Airport |  | ES | 333 |
| 18 | Macau International Airport |  | MO | 332 |
| 19 | Charlotte/Douglas International Airport |  | US | 329 |
| 20 | Tenerife Norte Airport |  | ES | 325 |
| 21 | Bengaluru International Airport |  | IN | 323 |
| 22 | Congonhas Airport |  | BR | 322 |
| 23 | Ninoy Aquino International Airport |  | PH | 319 |
| 24 | Malpensa International Airport |  | IT | 299 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 286 |
| 26 | Salt Lake City International Airport |  | US | 277 |
| 27 | Daniel K Inouye International Airport |  | US | 276 |
| 28 | Charles de Gaulle International Airport |  | FR | 273 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 261 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 255 |
| 32 | Reno/Tahoe International Airport |  | US | 253 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 249 |
| 34 | O. R. Tambo International Airport |  | ZA | 248 |
| 35 | Vitoria/Foronda Airport |  | ES | 241 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 240 |
| 37 | Barcelona International Airport |  | ES | 238 |
| 38 | Viracopos International Airport |  | BR | 230 |
| 39 | Seattle-Tacoma International Airport |  | US | 227 |
| 40 | Don Mueang International Airport |  | TH | 226 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 150 | 14m | 114 km | 294.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 88 | 21m | 244 km | 370.5 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 80 | 27m | 275 km | 379.1 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 70 | 31m | 369 km | 445.6 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 52 | 26m | 215 km | 192.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-15 11:34 UTC | 2026-04-15 22:41 UTC | 11h 6m |
| N70846 |  | Ramona Airport (KRNM) | Desert Wings Sky Ranch Airport (04CL) | 2026-04-15 22:18 UTC | 2026-04-15 22:40 UTC | 22m |
| KDI | KDI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-15 21:39 UTC | 2026-04-15 22:40 UTC | 1h 1m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-04-15 10:46 UTC | 2026-04-15 22:39 UTC | 11h 53m |
| N1239T |  | Cobb County International/Mccollum Field (KRYY) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-04-15 21:47 UTC | 2026-04-15 22:34 UTC | 46m |
| N65956 |  | Addison Airport (KADS) | Commerce Municipal Airport (K2F7) | 2026-04-15 21:10 UTC | 2026-04-15 22:29 UTC | 1h 19m |
| N502RP |  | 6CL6 (6CL6) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-15 22:03 UTC | 2026-04-15 22:27 UTC | 24m |
| VADER11 | VAD | Iraan Municipal Airport (K2F0) | Iraan Municipal Airport (K2F0) | 2026-04-15 22:05 UTC | 2026-04-15 22:26 UTC | 20m |
| KLW | KLW | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-04-15 22:14 UTC | 2026-04-15 22:25 UTC | 11m |
| YBV | YBV | Toowoomba Wellcamp Airport (YBWW) | Toowoomba Wellcamp Airport (YBWW) | 2026-04-15 22:01 UTC | 2026-04-15 22:24 UTC | 23m |
| ASA9421 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Okc Will Rogers International Airport (KOKC) | 2026-04-15 19:00 UTC | 2026-04-15 22:17 UTC | 3h 17m |
| N76PW |  | Norman Y Mineta San Jose International Airport (KSJC) | Centennial Airport (KAPA) | 2026-04-15 20:23 UTC | 2026-04-15 22:14 UTC | 1h 51m |
| N422CB |  | Republic Airport (KFRG) | Francis S Gabreski Airport (KFOK) | 2026-04-15 21:42 UTC | 2026-04-15 22:13 UTC | 30m |
| N5275S |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-15 21:53 UTC | 2026-04-15 22:12 UTC | 19m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-15 21:55 UTC | 2026-04-15 22:12 UTC | 16m |
| N41912 |  | Colby Airport (99KY) | Samuels Field (KBRY) | 2026-04-15 21:46 UTC | 2026-04-15 22:09 UTC | 22m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-04-15 21:29 UTC | 2026-04-15 22:09 UTC | 39m |
| EJA966 | EJA | Mc Clellan-Palomar Airport (KCRQ) | Scottsdale Airport (KSDL) | 2026-04-15 21:14 UTC | 2026-04-15 22:07 UTC | 53m |
| N7882N |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-15 21:33 UTC | 2026-04-15 22:05 UTC | 31m |
| UAE9422 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-15 15:44 UTC | 2026-04-15 22:05 UTC | 6h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
