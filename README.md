# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_11:07:02_UTC-green)

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

**Latest saved flight:** 2026-04-19 11:07:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 11:07:02 UTC

- **42,781** saved flights
- **17,902** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **42,781** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **514,934.4 tonnes** estimated CO2 emissions
- **29,851,270 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1796 |
| 2 | SkyWest Airlines | 1653 |
| 3 | IndiGo | 1054 |
| 4 | EJA | 733 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 441 |
| 9 | Vueling | 427 |
| 10 | LATAM Airlines | 425 |
| 11 | Lufthansa | 423 |
| 12 | All Nippon Airways | 396 |
| 13 | AZU | 378 |
| 14 | Delta Air Lines | 363 |
| 15 | QLK | 354 |
| 16 | LXJ | 333 |
| 17 | Swiss International | 330 |
| 18 | WIF | 327 |
| 19 | Alaska Airlines | 290 |
| 20 | AEE | 287 |
| 21 | EJU | 281 |
| 22 | easyJet | 274 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 268 |
| 25 | Air France | 241 |
| 26 | United Airlines | 230 |
| 27 | JetBlue | 228 |
| 28 | AXB | 226 |
| 29 | GLO | 225 |
| 30 | EDV | 219 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33690 |
| 2 | 🇮🇳 IN | 3232 |
| 3 | 🇪🇸 ES | 3138 |
| 4 | 🇦🇺 AU | 3024 |
| 5 | 🇧🇷 BR | 2549 |
| 6 | 🇯🇵 JP | 2406 |
| 7 | 🇮🇹 IT | 2223 |
| 8 | 🇩🇪 DE | 2167 |
| 9 | 🇨🇦 CA | 2084 |
| 10 | 🇨🇴 CO | 1973 |
| 11 | 🇬🇧 GB | 1732 |
| 12 | 🇫🇷 FR | 1646 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1309 |
| 15 | 🇨🇭 CH | 1189 |
| 16 | 🇲🇾 MY | 1078 |
| 17 | 🇳🇴 NO | 1043 |
| 18 | 🇿🇦 ZA | 889 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 765 |
| 22 | 🇹🇷 TR | 757 |
| 23 | 🇰🇷 KR | 719 |
| 24 | 🇬🇹 GT | 707 |
| 25 | 🇵🇱 PL | 676 |
| 26 | 🇲🇦 MA | 531 |
| 27 | 🇲🇪 ME | 444 |
| 28 | 🇳🇱 NL | 437 |
| 29 | 🇮🇩 ID | 398 |
| 30 | 🇧🇸 BS | 397 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 994 |
| 2 | Tokyo International Airport |  | JP | 823 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | Indira Gandhi International Airport |  | IN | 696 |
| 5 | El Dorado International Airport |  | CO | 691 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 650 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 522 |
| 10 | Zurich Airport |  | CH | 515 |
| 11 | Kuala Lumpur International Airport |  | MY | 426 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 414 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 410 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 394 |
| 17 | Macau International Airport |  | MO | 391 |
| 18 | Madrid Barajas International Airport |  | ES | 381 |
| 19 | Bengaluru International Airport |  | IN | 381 |
| 20 | Tenerife Norte Airport |  | ES | 373 |
| 21 | Charlotte/Douglas International Airport |  | US | 371 |
| 22 | Ninoy Aquino International Airport |  | PH | 366 |
| 23 | Congonhas Airport |  | BR | 366 |
| 24 | Malpensa International Airport |  | IT | 350 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Salt Lake City International Airport |  | US | 324 |
| 27 | Netaji Subhash Chandra Bose International Airport |  | IN | 319 |
| 28 | Daniel K Inouye International Airport |  | US | 318 |
| 29 | Charles de Gaulle International Airport |  | FR | 314 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 298 |
| 32 | Reno/Tahoe International Airport |  | US | 294 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 34 | O. R. Tambo International Airport |  | ZA | 286 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 286 |
| 36 | Capua Airport |  | IT | 284 |
| 37 | Barcelona International Airport |  | ES | 274 |
| 38 | Viracopos International Airport |  | BR | 261 |
| 39 | Don Mueang International Airport |  | TH | 259 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 131 | 28m | 304 km | 686.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 117 | 21m | 244 km | 492.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 116 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 116 | 19m | 165 km | 330.0 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 94 | 54m | 546 km | 885.0 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 71 | 20m | 250 km | 306.7 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 67 | 20m | 147 km | 169.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 60 | 57m | 493 km | 510.5 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 60 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 30 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BHA406 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-04-19 11:01 UTC | 2026-04-19 11:07 UTC | 5m |
| IGT1211 | IGT | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-04-19 03:07 UTC | 2026-04-19 10:56 UTC | 7h 49m |
| ALK181 | ALK | Suvarnabhumi Airport (VTBS) | Langtang Airport (VNLT) | 2026-04-19 00:51 UTC | 2026-04-19 10:52 UTC | 10h 0m |
| RYR4PN | Ryanair | Trieste / Ronchi Dei Legionari (LIPQ) | Palermo / Bocca Di Falco Airport (LICP) | 2026-04-19 09:28 UTC | 2026-04-19 10:34 UTC | 1h 5m |
| HYS226 | HYS | Paris Beauvais Tille Airport (LFOB) | Satu Mare Airport (LRSM) | 2026-04-19 08:44 UTC | 2026-04-19 10:33 UTC | 1h 48m |
| GTI8229 | GTI | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-04-18 20:28 UTC | 2026-04-19 10:32 UTC | 14h 3m |
| AXM6032 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-04-19 10:06 UTC | 2026-04-19 10:27 UTC | 20m |
| OAL043 | OAL | Kithira Airport (LGKC) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-19 09:50 UTC | 2026-04-19 10:26 UTC | 35m |
| ANA860 | All Nippon Airways | Chek Lap Kok International Airport (VHHH) | Tokyo International Airport (RJTT) | 2026-04-19 06:53 UTC | 2026-04-19 10:26 UTC | 3h 32m |
| RSC22SD | RSC | Tenerife Norte Airport (GCXO) | Gran Canaria Airport (GCLP) | 2026-04-19 10:08 UTC | 2026-04-19 10:24 UTC | 15m |
| GCFVR | GCF | Carlisle Airport (EGNC) | Carlisle Airport (EGNC) | 2026-04-19 10:18 UTC | 2026-04-19 10:23 UTC | 4m |
|  |  | Langtang Airport (VNLT) | Tribhuvan International Airport (VNKT) | 2026-04-19 10:02 UTC | 2026-04-19 10:22 UTC | 19m |
| CPA987 | Cathay Pacific | Macau International Airport (VMMC) | Chek Lap Kok International Airport (VHHH) | 2026-04-19 10:14 UTC | 2026-04-19 10:20 UTC | 5m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-19 09:58 UTC | 2026-04-19 10:20 UTC | 22m |
| GVANN | GVA | Carlisle Airport (EGNC) | Carlisle Airport (EGNC) | 2026-04-19 10:12 UTC | 2026-04-19 10:19 UTC | 6m |
| N502XL |  | Malaga Airport (LEMG) | Liverpool John Lennon Airport (EGGP) | 2026-04-19 07:34 UTC | 2026-04-19 10:19 UTC | 2h 44m |
| RSC8LL | RSC | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-04-19 10:01 UTC | 2026-04-19 10:19 UTC | 17m |
| MAC338C | MAC | Montpellier-Mediterranee Airport (LFMT) | Saiss Airport (GMFF) | 2026-04-19 08:35 UTC | 2026-04-19 10:18 UTC | 1h 42m |
| FYS10AK | FYS | Cuatro Vientos Airport (LECU) | E. Castellanos-Villacastin Airport (LEEV) | 2026-04-19 09:42 UTC | 2026-04-19 10:18 UTC | 35m |
| FGXBJ | FGX | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | 2026-04-19 10:17 UTC | 2026-04-19 10:17 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
