# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_15:56:45_UTC-green)

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

**Latest saved flight:** 2026-04-16 15:56:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 15:56:45 UTC

- **37,513** saved flights
- **16,232** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,513** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **453,375.8 tonnes** estimated CO2 emissions
- **26,282,654 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1589 |
| 2 | SkyWest Airlines | 1465 |
| 3 | IndiGo | 930 |
| 4 | EJA | 635 |
| 5 | American Airlines | 626 |
| 6 | Southwest Airlines | 518 |
| 7 | ENY | 488 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | LATAM Airlines | 380 |
| 11 | Vueling | 376 |
| 12 | All Nippon Airways | 337 |
| 13 | AZU | 333 |
| 14 | Delta Air Lines | 319 |
| 15 | QLK | 313 |
| 16 | LXJ | 298 |
| 17 | Swiss International | 282 |
| 18 | WIF | 282 |
| 19 | AEE | 251 |
| 20 | Alaska Airlines | 247 |
| 21 | EJU | 246 |
| 22 | easyJet | 246 |
| 23 | VIV | 236 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 213 |
| 26 | United Airlines | 208 |
| 27 | EDV | 206 |
| 28 | AIQ | 198 |
| 29 | GLO | 198 |
| 30 | Avianca | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29376 |
| 2 | 🇮🇳 IN | 2842 |
| 3 | 🇪🇸 ES | 2788 |
| 4 | 🇦🇺 AU | 2652 |
| 5 | 🇧🇷 BR | 2210 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 1988 |
| 8 | 🇩🇪 DE | 1931 |
| 9 | 🇨🇴 CO | 1843 |
| 10 | 🇨🇦 CA | 1825 |
| 11 | 🇬🇧 GB | 1549 |
| 12 | 🇫🇷 FR | 1427 |
| 13 | 🇲🇽 MX | 1179 |
| 14 | 🇬🇷 GR | 1140 |
| 15 | 🇨🇭 CH | 1033 |
| 16 | 🇲🇾 MY | 962 |
| 17 | 🇳🇴 NO | 911 |
| 18 | 🇿🇦 ZA | 799 |
| 19 | 🇳🇿 NZ | 789 |
| 20 | 🇵🇭 PH | 702 |
| 21 | 🇹🇭 TH | 689 |
| 22 | 🇹🇷 TR | 678 |
| 23 | 🇬🇹 GT | 644 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 590 |
| 26 | 🇲🇦 MA | 471 |
| 27 | 🇳🇱 NL | 377 |
| 28 | 🇲🇪 ME | 371 |
| 29 | 🇧🇸 BS | 365 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 875 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 654 |
| 4 | Denver International Airport |  | US | 625 |
| 5 | Indira Gandhi International Airport |  | IN | 613 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 563 |
| 7 | Harry Reid International Airport |  | US | 488 |
| 8 | La Aurora Airport |  | GT | 474 |
| 9 | Guaymaral Airport |  | CO | 470 |
| 10 | Zurich Airport |  | CH | 454 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 374 |
| 12 | Kuala Lumpur International Airport |  | MY | 374 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 371 |
| 14 | Chicago O'Hare International Airport |  | US | 363 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Frankfurt am Main International Airport |  | DE | 345 |
| 17 | Madrid Barajas International Airport |  | ES | 342 |
| 18 | Macau International Airport |  | MO | 341 |
| 19 | Tenerife Norte Airport |  | ES | 332 |
| 20 | Charlotte/Douglas International Airport |  | US | 331 |
| 21 | Bengaluru International Airport |  | IN | 328 |
| 22 | Congonhas Airport |  | BR | 327 |
| 23 | Ninoy Aquino International Airport |  | PH | 325 |
| 24 | Malpensa International Airport |  | IT | 307 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 289 |
| 26 | Salt Lake City International Airport |  | US | 282 |
| 27 | Daniel K Inouye International Airport |  | US | 279 |
| 28 | Charles de Gaulle International Airport |  | FR | 278 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 267 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 266 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | O. R. Tambo International Airport |  | ZA | 256 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 256 |
| 34 | Reno/Tahoe International Airport |  | US | 255 |
| 35 | Vitoria/Foronda Airport |  | ES | 250 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 244 |
| 37 | Barcelona International Airport |  | ES | 240 |
| 38 | Don Mueang International Airport |  | TH | 235 |
| 39 | Viracopos International Airport |  | BR | 232 |
| 40 | Seattle-Tacoma International Airport |  | US | 229 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 185 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 94 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 90 | 21m | 244 km | 379.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 84 | 27m | 275 km | 398.0 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 81 | 21m | 99 km | 138.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 56 | 1h 41m | 1,423 km | 1,374.3 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 27 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 54 | 26m | 215 km | 200.0 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HTY238 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-16 15:31 UTC | 2026-04-16 15:56 UTC | 25m |
| N419PH |  | K1J6 (K1J6) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-16 14:54 UTC | 2026-04-16 15:49 UTC | 54m |
| N67490 |  | Sanctuary Ranch Airport (7TS4) | Tightwaad Air Ranch Airport (XA16) | 2026-04-16 15:34 UTC | 2026-04-16 15:47 UTC | 12m |
| N64017 |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-04-16 15:15 UTC | 2026-04-16 15:45 UTC | 30m |
| BOX738 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-16 01:40 UTC | 2026-04-16 15:43 UTC | 14h 3m |
| TCF637 | TCF | Melbourne Orlando International Airport (KMLB) | New Smyrna Beach Municipal (Jack Bolt Field) Airport (KEVB) | 2026-04-16 14:54 UTC | 2026-04-16 15:42 UTC | 48m |
| SRB501 | SRB | Batajnica Air Base (LYBT) | Batajnica Air Base (LYBT) | 2026-04-16 14:29 UTC | 2026-04-16 15:37 UTC | 1h 8m |
| N111JM |  | Montgomery-Gibbs Executive Airport (KMYF) | Jacqueline Cochran Regional Airport (KTRM) | 2026-04-16 15:21 UTC | 2026-04-16 15:36 UTC | 15m |
| N58LC |  | Mc Clellan-Palomar Airport (KCRQ) | Buchanan Field (KCCR) | 2026-04-16 14:26 UTC | 2026-04-16 15:35 UTC | 1h 8m |
| SHERPA2 | SHE | Coolidge Municipal Airport (KP08) | Coolidge Municipal Airport (KP08) | 2026-04-16 15:05 UTC | 2026-04-16 15:33 UTC | 28m |
| N223MG |  | Perot Field/Fort Worth Alliance Airport (KAFW) | 5TS4 (5TS4) | 2026-04-16 15:05 UTC | 2026-04-16 15:33 UTC | 27m |
| N426SH |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-16 15:09 UTC | 2026-04-16 15:30 UTC | 20m |
| N254SB |  | Antiquers Aerodrome (FD08) | Tweed/New Haven Airport (KHVN) | 2026-04-16 12:51 UTC | 2026-04-16 15:30 UTC | 2h 38m |
| DSU91 | DSU | Cleveland Municipal Airport (KRNV) | Cleveland Municipal Airport (KRNV) | 2026-04-16 14:35 UTC | 2026-04-16 15:29 UTC | 54m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-16 15:14 UTC | 2026-04-16 15:29 UTC | 14m |
| SCU10 | SCU | Jirik Field (OL23) | 19OK (19OK) | 2026-04-16 13:55 UTC | 2026-04-16 15:29 UTC | 1h 34m |
| SYS131 | SYS | RAF Ternhill (EGOE) | RAF Ternhill (EGOE) | 2026-04-16 15:28 UTC | 2026-04-16 15:29 UTC | 1m |
| ARK401D | ARK | Sabadell Airport (LELL) | Girona Airport (LEGE) | 2026-04-16 15:05 UTC | 2026-04-16 15:28 UTC | 23m |
| QTR8408 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-16 08:20 UTC | 2026-04-16 15:28 UTC | 7h 7m |
| RYR200T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-16 14:36 UTC | 2026-04-16 15:25 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
