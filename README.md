# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_05:36:27_UTC-green)

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

**Latest saved flight:** 2026-04-13 05:36:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 05:36:27 UTC

- **31,697** saved flights
- **14,345** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,697** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **390,102.6 tonnes** estimated CO2 emissions
- **22,614,643 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1323 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 808 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 464 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 375 |
| 9 | AXM | 338 |
| 10 | LATAM Airlines | 324 |
| 11 | Vueling | 320 |
| 12 | All Nippon Airways | 290 |
| 13 | AZU | 284 |
| 14 | Delta Air Lines | 265 |
| 15 | QLK | 264 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 233 |
| 18 | Alaska Airlines | 215 |
| 19 | easyJet | 211 |
| 20 | WIF | 207 |
| 21 | EJU | 205 |
| 22 | VIV | 204 |
| 23 | AEE | 199 |
| 24 | Japan Airlines | 199 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 173 |
| 28 | Avianca | 171 |
| 29 | Air France | 169 |
| 30 | JetBlue | 168 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25037 |
| 2 | 🇮🇳 IN | 2479 |
| 3 | 🇪🇸 ES | 2345 |
| 4 | 🇦🇺 AU | 2223 |
| 5 | 🇧🇷 BR | 1890 |
| 6 | 🇯🇵 JP | 1730 |
| 7 | 🇮🇹 IT | 1658 |
| 8 | 🇨🇴 CO | 1598 |
| 9 | 🇩🇪 DE | 1595 |
| 10 | 🇨🇦 CA | 1537 |
| 11 | 🇬🇧 GB | 1277 |
| 12 | 🇫🇷 FR | 1159 |
| 13 | 🇲🇽 MX | 1015 |
| 14 | 🇬🇷 GR | 903 |
| 15 | 🇨🇭 CH | 880 |
| 16 | 🇲🇾 MY | 813 |
| 17 | 🇳🇴 NO | 696 |
| 18 | 🇳🇿 NZ | 684 |
| 19 | 🇿🇦 ZA | 646 |
| 20 | 🇵🇭 PH | 591 |
| 21 | 🇬🇹 GT | 587 |
| 22 | 🇹🇷 TR | 581 |
| 23 | 🇹🇭 TH | 577 |
| 24 | 🇰🇷 KR | 542 |
| 25 | 🇵🇱 PL | 478 |
| 26 | 🇲🇦 MA | 407 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 314 |
| 29 | 🇲🇴 MO | 303 |
| 30 | 🇮🇩 ID | 301 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 765 |
| 2 | Tokyo International Airport |  | JP | 583 |
| 3 | El Dorado International Airport |  | CO | 568 |
| 4 | Denver International Airport |  | US | 538 |
| 5 | Indira Gandhi International Airport |  | IN | 525 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 441 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 413 |
| 9 | Guaymaral Airport |  | CO | 388 |
| 10 | Zurich Airport |  | CH | 387 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 12 | Chicago O'Hare International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 320 |
| 15 | Kuala Lumpur International Airport |  | MY | 309 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 307 |
| 17 | Macau International Airport |  | MO | 303 |
| 18 | Charlotte/Douglas International Airport |  | US | 289 |
| 19 | Tenerife Norte Airport |  | ES | 282 |
| 20 | Bengaluru International Airport |  | IN | 282 |
| 21 | Madrid Barajas International Airport |  | ES | 281 |
| 22 | Congonhas Airport |  | BR | 277 |
| 23 | Ninoy Aquino International Airport |  | PH | 272 |
| 24 | Malpensa International Airport |  | IT | 257 |
| 25 | Daniel K Inouye International Airport |  | US | 245 |
| 26 | Salt Lake City International Airport |  | US | 244 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 243 |
| 28 | Reno/Tahoe International Airport |  | US | 242 |
| 29 | Charles de Gaulle International Airport |  | FR | 230 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 229 |
| 31 | John Paul II International Airport Kraków-Balice Airport |  | PL | 217 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 216 |
| 33 | Capua Airport |  | IT | 216 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 216 |
| 35 | Miami International Airport |  | US | 210 |
| 36 | O. R. Tambo International Airport |  | ZA | 209 |
| 37 | Vitoria/Foronda Airport |  | ES | 207 |
| 38 | Seattle-Tacoma International Airport |  | US | 202 |
| 39 | Barcelona International Airport |  | ES | 199 |
| 40 | Viracopos International Airport |  | BR | 196 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 147 | 1h 8m | 706 km | 1,789.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 116 | 24m | 225 km | 450.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 105 | 28m | 304 km | 550.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 91 | 1h 28m | 910 km | 1,428.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 82 | 19m | 165 km | 233.3 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 76 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 71 | 55m | 546 km | 668.5 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 67 | 27m | 275 km | 317.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 66 | 21m | 244 km | 277.9 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 66 | 1h 12m | 770 km | 876.8 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 62 | 31m | 369 km | 394.6 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 19 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 58 | 45m | 452 km | 452.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 54 | 20m | 250 km | 233.2 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 49 | 20m | 147 km | 124.0 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 47 | 16m | 162 km | 131.7 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HGO1782 | HGO | London Stansted Airport (EGSS) | Macau International Airport (VMMC) | 2026-04-12 09:38 UTC | 2026-04-13 05:36 UTC | 19h 58m |
| ETH644 | Ethiopian Airlines | Yaounde Nsimalen International Airport (FKYS) | Macau International Airport (VMMC) | 2026-04-12 14:37 UTC | 2026-04-13 05:34 UTC | 14h 56m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-13 05:19 UTC | 2026-04-13 05:30 UTC | 10m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-12 14:30 UTC | 2026-04-13 05:28 UTC | 14h 57m |
| IGO1721 | IndiGo | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-13 01:02 UTC | 2026-04-13 05:25 UTC | 4h 23m |
| CLX2N | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-04-12 14:06 UTC | 2026-04-13 05:22 UTC | 15h 16m |
| LR455 |  | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-13 04:39 UTC | 2026-04-13 05:11 UTC | 32m |
| RYR7597 | Ryanair | Toulouse-Blagnac Airport (LFBO) | Menorca Airport (LEMH) | 2026-04-13 04:10 UTC | 2026-04-13 04:56 UTC | 46m |
| RYR13KA | Ryanair | Torino / Caselle International Airport (LIMF) | Decimomannu Airport (LIED) | 2026-04-13 04:01 UTC | 2026-04-13 04:54 UTC | 52m |
| ASA1212 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-04-13 04:28 UTC | 2026-04-13 04:50 UTC | 22m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-04-13 04:31 UTC | 2026-04-13 04:50 UTC | 18m |
| WZZ89TS | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Berane Airport (LYBR) | 2026-04-13 04:02 UTC | 2026-04-13 04:47 UTC | 45m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Mae Sariang Airport (VTCS) | 2026-04-13 04:23 UTC | 2026-04-13 04:46 UTC | 23m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-04-13 04:20 UTC | 2026-04-13 04:46 UTC | 26m |
| HLJ | HLJ | Perth International Airport (YPPH) | Kondinin Airport (YKDN) | 2026-04-13 04:08 UTC | 2026-04-13 04:46 UTC | 38m |
| RYR1SR | Ryanair | Barcelona International Airport (LEBL) | Menorca Airport (LEMH) | 2026-04-13 04:10 UTC | 2026-04-13 04:45 UTC | 34m |
| FENEC03 | FEN | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-04-13 04:42 UTC | 2026-04-13 04:43 UTC | 1m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-13 04:10 UTC | 2026-04-13 04:43 UTC | 33m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-04-13 04:24 UTC | 2026-04-13 04:42 UTC | 18m |
| APG221 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-13 04:15 UTC | 2026-04-13 04:40 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
