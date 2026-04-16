# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_20:42:22_UTC-green)

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

**Latest saved flight:** 2026-04-16 20:42:22 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 20:42:22 UTC

- **38,048** saved flights
- **16,449** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,048** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **459,846.7 tonnes** estimated CO2 emissions
- **26,657,779 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1606 |
| 2 | SkyWest Airlines | 1491 |
| 3 | IndiGo | 932 |
| 4 | EJA | 655 |
| 5 | American Airlines | 639 |
| 6 | Southwest Airlines | 527 |
| 7 | ENY | 494 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | Vueling | 382 |
| 11 | LATAM Airlines | 381 |
| 12 | AZU | 340 |
| 13 | All Nippon Airways | 337 |
| 14 | Delta Air Lines | 324 |
| 15 | QLK | 313 |
| 16 | LXJ | 306 |
| 17 | WIF | 287 |
| 18 | Swiss International | 283 |
| 19 | AEE | 254 |
| 20 | Alaska Airlines | 251 |
| 21 | easyJet | 250 |
| 22 | EJU | 249 |
| 23 | VIV | 242 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 215 |
| 26 | EDV | 210 |
| 27 | United Airlines | 210 |
| 28 | GLO | 199 |
| 29 | AIQ | 198 |
| 30 | Avianca | 196 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30001 |
| 2 | 🇮🇳 IN | 2854 |
| 3 | 🇪🇸 ES | 2828 |
| 4 | 🇦🇺 AU | 2655 |
| 5 | 🇧🇷 BR | 2241 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 2010 |
| 8 | 🇩🇪 DE | 1945 |
| 9 | 🇨🇴 CO | 1878 |
| 10 | 🇨🇦 CA | 1856 |
| 11 | 🇬🇧 GB | 1571 |
| 12 | 🇫🇷 FR | 1445 |
| 13 | 🇲🇽 MX | 1200 |
| 14 | 🇬🇷 GR | 1149 |
| 15 | 🇨🇭 CH | 1037 |
| 16 | 🇲🇾 MY | 963 |
| 17 | 🇳🇴 NO | 923 |
| 18 | 🇿🇦 ZA | 799 |
| 19 | 🇳🇿 NZ | 789 |
| 20 | 🇵🇭 PH | 704 |
| 21 | 🇹🇭 TH | 690 |
| 22 | 🇹🇷 TR | 682 |
| 23 | 🇬🇹 GT | 651 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 596 |
| 26 | 🇲🇦 MA | 476 |
| 27 | 🇳🇱 NL | 380 |
| 28 | 🇲🇪 ME | 375 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 890 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 662 |
| 4 | Denver International Airport |  | US | 635 |
| 5 | Indira Gandhi International Airport |  | IN | 617 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 568 |
| 7 | Harry Reid International Airport |  | US | 498 |
| 8 | Guaymaral Airport |  | CO | 490 |
| 9 | La Aurora Airport |  | GT | 478 |
| 10 | Zurich Airport |  | CH | 457 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 379 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 377 |
| 13 | Kuala Lumpur International Airport |  | MY | 375 |
| 14 | Chicago O'Hare International Airport |  | US | 370 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Macau International Airport |  | MO | 347 |
| 17 | Madrid Barajas International Airport |  | ES | 346 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 342 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Congonhas Airport |  | BR | 330 |
| 22 | Bengaluru International Airport |  | IN | 328 |
| 23 | Ninoy Aquino International Airport |  | PH | 327 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 295 |
| 26 | Salt Lake City International Airport |  | US | 289 |
| 27 | Daniel K Inouye International Airport |  | US | 283 |
| 28 | Charles de Gaulle International Airport |  | FR | 281 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 269 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 268 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Vitoria/Foronda Airport |  | ES | 258 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 249 |
| 37 | Barcelona International Airport |  | ES | 244 |
| 38 | Don Mueang International Airport |  | TH | 236 |
| 39 | Viracopos International Airport |  | BR | 235 |
| 40 | Seattle-Tacoma International Airport |  | US | 230 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 195 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 154 | 14m | 114 km | 302.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 94 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 93 | 21m | 244 km | 391.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 86 | 26m | 275 km | 407.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 57 | 1h 41m | 1,423 km | 1,398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 56 | 26m | 215 km | 207.4 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 53 | 13m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 53 | 1h 53m | 1,304 km | 1,192.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N124DN |  | Provincetown Municipal Airport (KPVC) | Provincetown Municipal Airport (KPVC) | 2026-04-16 20:31 UTC | 2026-04-16 20:42 UTC | 10m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-16 20:25 UTC | 2026-04-16 20:37 UTC | 12m |
| N72608 |  | Reno/Tahoe International Airport (KRNO) | Reno/Tahoe International Airport (KRNO) | 2026-04-16 20:10 UTC | 2026-04-16 20:35 UTC | 25m |
| N311ZZ |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-16 19:59 UTC | 2026-04-16 20:34 UTC | 34m |
| ERU973 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-04-16 20:12 UTC | 2026-04-16 20:33 UTC | 20m |
| CXK191 | CXK | Delano Municipal Airport (KDLO) | Meadows Field (KBFL) | 2026-04-16 20:13 UTC | 2026-04-16 20:32 UTC | 19m |
| N862TC |  | Palm Beach County Park Airport (KLNA) | Pompano Beach Airpark (KPMP) | 2026-04-16 20:03 UTC | 2026-04-16 20:30 UTC | 26m |
| BOX740 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-16 04:10 UTC | 2026-04-16 20:28 UTC | 16h 17m |
| HKC9458 | HKC | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-16 13:22 UTC | 2026-04-16 20:27 UTC | 7h 4m |
| UAE9842 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-16 13:59 UTC | 2026-04-16 20:24 UTC | 6h 25m |
| CGENW | CGE | Provo Municipal Airport (KPVU) | Citabriair Airport (UT43) | 2026-04-16 19:06 UTC | 2026-04-16 20:24 UTC | 1h 18m |
| N44YA |  | Lafayette Airstrip (OR90) | Mc Minnville Municipal Airport (KMMV) | 2026-04-16 20:19 UTC | 2026-04-16 20:22 UTC | 2m |
| N488AA |  | Denton Enterprise Airport (KDTO) | Richards Airport (TA47) | 2026-04-16 19:36 UTC | 2026-04-16 20:21 UTC | 45m |
| TVR4703 | TVR | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-16 13:45 UTC | 2026-04-16 20:21 UTC | 6h 35m |
| N265LD |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-04-16 19:43 UTC | 2026-04-16 20:18 UTC | 35m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-04-16 05:46 UTC | 2026-04-16 20:18 UTC | 14h 32m |
| CLAW01 | CLA | North Pickens Airport (K3M8) | North Pickens Airport (K3M8) | 2026-04-16 20:04 UTC | 2026-04-16 20:16 UTC | 12m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-04-16 09:00 UTC | 2026-04-16 20:15 UTC | 11h 15m |
| GRZLY39 | GRZ | Las Cruces International Airport (KLRU) | Sedona Airport (KSEZ) | 2026-04-16 19:12 UTC | 2026-04-16 20:13 UTC | 1h 0m |
| N974MM |  | Virginia Tech/Montgomery Executive Airport (KBCB) | VA00 (VA00) | 2026-04-16 19:58 UTC | 2026-04-16 20:11 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
