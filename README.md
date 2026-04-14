# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_19:30:38_UTC-green)

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

**Latest saved flight:** 2026-04-14 19:30:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 19:30:38 UTC

- **34,600** saved flights
- **15,322** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **34,600** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **423,249.7 tonnes** estimated CO2 emissions
- **24,536,212 km** total distance flown
- **846 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1486 |
| 2 | SkyWest Airlines | 1382 |
| 3 | IndiGo | 870 |
| 4 | EJA | 594 |
| 5 | American Airlines | 593 |
| 6 | Southwest Airlines | 493 |
| 7 | ENY | 454 |
| 8 | Lufthansa | 381 |
| 9 | AXM | 363 |
| 10 | Vueling | 351 |
| 11 | LATAM Airlines | 344 |
| 12 | All Nippon Airways | 310 |
| 13 | AZU | 307 |
| 14 | Delta Air Lines | 292 |
| 15 | QLK | 289 |
| 16 | LXJ | 275 |
| 17 | Swiss International | 264 |
| 18 | WIF | 254 |
| 19 | easyJet | 233 |
| 20 | AEE | 232 |
| 21 | Alaska Airlines | 231 |
| 22 | EJU | 230 |
| 23 | VIV | 224 |
| 24 | Japan Airlines | 216 |
| 25 | EDV | 197 |
| 26 | United Airlines | 194 |
| 27 | Air France | 193 |
| 28 | GLO | 187 |
| 29 | JetBlue | 183 |
| 30 | Avianca | 182 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27123 |
| 2 | 🇮🇳 IN | 2660 |
| 3 | 🇪🇸 ES | 2601 |
| 4 | 🇦🇺 AU | 2416 |
| 5 | 🇧🇷 BR | 2034 |
| 6 | 🇯🇵 JP | 1873 |
| 7 | 🇮🇹 IT | 1864 |
| 8 | 🇩🇪 DE | 1776 |
| 9 | 🇨🇴 CO | 1724 |
| 10 | 🇨🇦 CA | 1676 |
| 11 | 🇬🇧 GB | 1432 |
| 12 | 🇫🇷 FR | 1298 |
| 13 | 🇲🇽 MX | 1105 |
| 14 | 🇬🇷 GR | 1032 |
| 15 | 🇨🇭 CH | 958 |
| 16 | 🇲🇾 MY | 877 |
| 17 | 🇳🇴 NO | 821 |
| 18 | 🇿🇦 ZA | 726 |
| 19 | 🇳🇿 NZ | 726 |
| 20 | 🇵🇭 PH | 652 |
| 21 | 🇹🇷 TR | 637 |
| 22 | 🇹🇭 TH | 625 |
| 23 | 🇬🇹 GT | 609 |
| 24 | 🇰🇷 KR | 585 |
| 25 | 🇵🇱 PL | 548 |
| 26 | 🇲🇦 MA | 437 |
| 27 | 🇧🇸 BS | 345 |
| 28 | 🇳🇱 NL | 345 |
| 29 | 🇲🇪 ME | 340 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 819 |
| 2 | Tokyo International Airport |  | JP | 640 |
| 3 | El Dorado International Airport |  | CO | 613 |
| 4 | Denver International Airport |  | US | 577 |
| 5 | Indira Gandhi International Airport |  | IN | 564 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 507 |
| 7 | Harry Reid International Airport |  | US | 456 |
| 8 | La Aurora Airport |  | GT | 445 |
| 9 | Zurich Airport |  | CH | 431 |
| 10 | Guaymaral Airport |  | CO | 429 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 350 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 348 |
| 13 | Chicago O'Hare International Airport |  | US | 344 |
| 14 | Kuala Lumpur International Airport |  | MY | 337 |
| 15 | Frankfurt am Main International Airport |  | DE | 334 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 314 |
| 19 | Charlotte/Douglas International Airport |  | US | 309 |
| 20 | Bengaluru International Airport |  | IN | 307 |
| 21 | Tenerife Norte Airport |  | ES | 304 |
| 22 | Ninoy Aquino International Airport |  | PH | 301 |
| 23 | Congonhas Airport |  | BR | 301 |
| 24 | Malpensa International Airport |  | IT | 282 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 269 |
| 26 | Salt Lake City International Airport |  | US | 263 |
| 27 | Daniel K Inouye International Airport |  | US | 262 |
| 28 | Capua Airport |  | IT | 259 |
| 29 | Charles de Gaulle International Airport |  | FR | 257 |
| 30 | Reno/Tahoe International Airport |  | US | 245 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 241 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 241 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 238 |
| 34 | O. R. Tambo International Airport |  | ZA | 235 |
| 35 | Vitoria/Foronda Airport |  | ES | 231 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 230 |
| 37 | Barcelona International Airport |  | ES | 224 |
| 38 | Seattle-Tacoma International Airport |  | US | 216 |
| 39 | Miami International Airport |  | US | 215 |
| 40 | Viracopos International Airport |  | BR | 213 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 167 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 161 | 1h 8m | 706 km | 1,960.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 142 | 14m | 114 km | 278.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 100 | 1h 27m | 910 km | 1,569.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 84 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 79 | 21m | 244 km | 332.6 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 75 | 27m | 275 km | 355.4 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 73 | 1h 12m | 770 km | 969.7 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 57 | 20m | 147 km | 144.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 53 | 13m | 99 km | 90.9 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 49 | 26m | 215 km | 181.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 49 | 14m | 154 km | 129.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 48 | 1h 20m | 961 km | 795.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N46168 |  | Southerly Airport (58FD) | Winter Haven Regional Airport (KGIF) | 2026-04-14 19:13 UTC | 2026-04-14 19:30 UTC | 17m |
| N70CZ |  | East Side Airport (3TS0) | Mc Alester Regional Airport (KMLC) | 2026-04-14 18:08 UTC | 2026-04-14 19:30 UTC | 1h 22m |
| RNGR736 | RNG | Mellon Ranch Airport (XS59) | Ingleside Regional Airport (KTFP) | 2026-04-14 18:58 UTC | 2026-04-14 19:24 UTC | 26m |
| N30JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-04-14 19:11 UTC | 2026-04-14 19:24 UTC | 12m |
| N407FA |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-14 19:07 UTC | 2026-04-14 19:22 UTC | 14m |
| N690AC |  | Louisville Muhammad Ali International Airport (KSDF) | Mobile International Airport (KBFM) | 2026-04-14 17:59 UTC | 2026-04-14 19:18 UTC | 1h 19m |
| N491TC |  | 52OR (52OR) | Portland-Hillsboro Airport (KHIO) | 2026-04-14 18:49 UTC | 2026-04-14 19:18 UTC | 29m |
| N9552A |  | Addison Airport (KADS) | Pritchard Airport (99TE) | 2026-04-14 18:47 UTC | 2026-04-14 19:17 UTC | 30m |
| N523PC |  | Gnoss Field (KDVO) | Gnoss Field (KDVO) | 2026-04-14 18:35 UTC | 2026-04-14 19:14 UTC | 39m |
| XBPHW | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-04-14 18:32 UTC | 2026-04-14 19:12 UTC | 40m |
| N453LP |  | KFTG (KFTG) | Chaparral Airport (CO18) | 2026-04-14 18:55 UTC | 2026-04-14 19:11 UTC | 16m |
| N945G |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-14 18:38 UTC | 2026-04-14 19:11 UTC | 32m |
| FHBVE | FHB | Dax Seyresse Airport (LFBY) | Dax Seyresse Airport (LFBY) | 2026-04-14 19:05 UTC | 2026-04-14 19:06 UTC | 1m |
| N729EL |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-04-14 17:36 UTC | 2026-04-14 18:59 UTC | 1h 23m |
| EJA162 | EJA | Salt Lake City International Airport (KSLC) | Elko Regional Airport (KEKO) | 2026-04-14 18:30 UTC | 2026-04-14 18:57 UTC | 26m |
| N22LT |  | Prineville Airport (KS39) | Prineville Airport (KS39) | 2026-04-14 18:53 UTC | 2026-04-14 18:57 UTC | 3m |
| N407FA |  | Wilkes-Barre/Scranton International Airport (KAVP) | Lancaster Airport (KLNS) | 2026-04-14 17:58 UTC | 2026-04-14 18:56 UTC | 57m |
| N112FS |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-04-14 18:14 UTC | 2026-04-14 18:54 UTC | 40m |
| AJAY51 | AJA | Danaher Airport (7TX0) | 2XA0 (2XA0) | 2026-04-14 18:44 UTC | 2026-04-14 18:53 UTC | 9m |
| SPADE16 | SPA | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-04-14 18:29 UTC | 2026-04-14 18:52 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
