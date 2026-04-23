# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_05:31:52_UTC-green)

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

**Latest saved flight:** 2026-04-23 05:31:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 05:31:52 UTC

- **49,170** saved flights
- **19,923** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,170** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **587,445.5 tonnes** estimated CO2 emissions
- **34,054,812 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2073 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1143 |
| 4 | EJA | 852 |
| 5 | American Airlines | 810 |
| 6 | Southwest Airlines | 703 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 550 |
| 9 | Vueling | 487 |
| 10 | AXM | 486 |
| 11 | LATAM Airlines | 481 |
| 12 | All Nippon Airways | 443 |
| 13 | AZU | 421 |
| 14 | Delta Air Lines | 405 |
| 15 | WIF | 404 |
| 16 | QLK | 395 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 371 |
| 19 | AEE | 333 |
| 20 | Alaska Airlines | 329 |
| 21 | EJU | 318 |
| 22 | easyJet | 312 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 292 |
| 25 | Air France | 277 |
| 26 | AXB | 260 |
| 27 | Cathay Pacific | 259 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | AIQ | 249 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39212 |
| 2 | 🇮🇳 IN | 3575 |
| 3 | 🇪🇸 ES | 3535 |
| 4 | 🇦🇺 AU | 3414 |
| 5 | 🇧🇷 BR | 2870 |
| 6 | 🇯🇵 JP | 2679 |
| 7 | 🇮🇹 IT | 2639 |
| 8 | 🇩🇪 DE | 2568 |
| 9 | 🇨🇦 CA | 2446 |
| 10 | 🇨🇴 CO | 2289 |
| 11 | 🇬🇧 GB | 2020 |
| 12 | 🇫🇷 FR | 1860 |
| 13 | 🇲🇽 MX | 1528 |
| 14 | 🇬🇷 GR | 1496 |
| 15 | 🇨🇭 CH | 1333 |
| 16 | 🇳🇴 NO | 1288 |
| 17 | 🇲🇾 MY | 1186 |
| 18 | 🇿🇦 ZA | 1002 |
| 19 | 🇳🇿 NZ | 953 |
| 20 | 🇹🇭 TH | 883 |
| 21 | 🇹🇷 TR | 863 |
| 22 | 🇵🇭 PH | 857 |
| 23 | 🇰🇷 KR | 807 |
| 24 | 🇵🇱 PL | 778 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 598 |
| 27 | 🇲🇪 ME | 519 |
| 28 | 🇳🇱 NL | 497 |
| 29 | 🇲🇴 MO | 455 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 910 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 787 |
| 5 | Indira Gandhi International Airport |  | IN | 758 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 739 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 642 |
| 9 | Zurich Airport |  | CH | 577 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 526 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 487 |
| 14 | Kuala Lumpur International Airport |  | MY | 476 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 465 |
| 16 | Macau International Airport |  | MO | 455 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 450 |
| 18 | Madrid Barajas International Airport |  | ES | 440 |
| 19 | Bengaluru International Airport |  | IN | 432 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 413 |
| 22 | Tenerife Norte Airport |  | ES | 405 |
| 23 | Malpensa International Airport |  | IT | 404 |
| 24 | Ninoy Aquino International Airport |  | PH | 396 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 377 |
| 26 | Salt Lake City International Airport |  | US | 369 |
| 27 | Daniel K Inouye International Airport |  | US | 365 |
| 28 | Charles de Gaulle International Airport |  | FR | 364 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 356 |
| 30 | Capua Airport |  | IT | 353 |
| 31 | Vitoria/Foronda Airport |  | ES | 335 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 335 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 325 |
| 36 | O. R. Tambo International Airport |  | ZA | 323 |
| 37 | Barcelona International Airport |  | ES | 321 |
| 38 | Don Mueang International Airport |  | TH | 300 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 293 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 231 | 1h 7m | 706 km | 2,812.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 189 | 14m | 114 km | 370.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 170 | 24m | 225 km | 659.5 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 147 | 21m | 244 km | 619.0 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 145 | 28m | 304 km | 760.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 140 | 1h 27m | 910 km | 2,196.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 130 | 19m | 165 km | 369.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 115 | 26m | 275 km | 544.9 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 101 | 44m | 452 km | 787.1 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 84 | 31m | 369 km | 534.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 82 | 20m | 250 km | 354.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 78 | 26m | 215 km | 288.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 71 | 1h 41m | 1,156 km | 1,416.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-23 04:27 UTC | 2026-04-23 05:31 UTC | 1h 4m |
| JUST71 | JUS | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-23 02:58 UTC | 2026-04-23 05:28 UTC | 2h 29m |
| R20539 |  | Gray Army Air Field (Joint Base Lewis-Mcchord) Airport (KGRF) | KZ10 (KZ10) | 2026-04-23 05:10 UTC | 2026-04-23 05:18 UTC | 7m |
| FIN4J | Finnair | Helsinki Vantaa Airport (EFHK) | Pyhoselka Airport (EFPH) | 2026-04-23 03:49 UTC | 2026-04-23 04:58 UTC | 1h 9m |
| EJA417 | EJA | Santa Barbara Municipal Airport (KSBA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-23 04:15 UTC | 2026-04-23 04:54 UTC | 38m |
| ZKHWD | ZKH | Christchurch International Airport (NZCH) | Christchurch International Airport (NZCH) | 2026-04-23 04:32 UTC | 2026-04-23 04:48 UTC | 15m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Kaikohe Airport (NZKO) | 2026-04-23 04:21 UTC | 2026-04-23 04:46 UTC | 24m |
| VOZ1690 | Virgin Australia | Gold Coast Airport (YBCG) | Canberra International Airport (YSCB) | 2026-04-23 03:35 UTC | 2026-04-23 04:46 UTC | 1h 11m |
| WIF6PC | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-23 04:32 UTC | 2026-04-23 04:43 UTC | 10m |
| IGO5268 | IndiGo | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-04-23 03:02 UTC | 2026-04-23 04:39 UTC | 1h 36m |
| IGO214J | IndiGo | Indira Gandhi International Airport (VIDP) | Gaya Airport (VEGY) | 2026-04-22 09:36 UTC | 2026-04-23 04:38 UTC | 19h 2m |
| TAM4522 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Morro do Chapeu Airport (SNOC) | 2026-04-23 02:40 UTC | 2026-04-23 04:38 UTC | 1h 57m |
| MATTI | MAT | Ostrava Leos Janacek Airport (LKMT) | Václav Havel Airport (LKPR) | 2026-04-23 03:57 UTC | 2026-04-23 04:35 UTC | 38m |
| SAS41T | Scandinavian Airlines | Vilnius International Airport (EYVI) | Nida Airport (EYND) | 2026-04-23 03:56 UTC | 2026-04-23 04:33 UTC | 37m |
| AIQ3374 | AIQ | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-04-23 03:59 UTC | 2026-04-23 04:33 UTC | 34m |
|  |  | Bergen Airport Flesland (ENBR) | Stavanger Airport Sola (ENZV) | 2026-04-23 04:14 UTC | 2026-04-23 04:32 UTC | 17m |
| BTN772 | BTN | Tribhuvan International Airport (VNKT) | Paro Airport (VQPR) | 2026-04-23 03:54 UTC | 2026-04-23 04:31 UTC | 37m |
| FD244 |  | Tamworth Airport (YSTW) | Walgett Airport (YWLG) | 2026-04-23 03:52 UTC | 2026-04-23 04:27 UTC | 34m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-23 04:10 UTC | 2026-04-23 04:26 UTC | 16m |
| N63JT |  | Salt Lake City International Airport (KSLC) | Faries Field (79MO) | 2026-04-23 01:43 UTC | 2026-04-23 04:23 UTC | 2h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
