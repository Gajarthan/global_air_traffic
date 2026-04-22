# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_00:51:38_UTC-green)

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

**Latest saved flight:** 2026-04-22 00:51:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 00:51:38 UTC

- **47,530** saved flights
- **19,401** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,530** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **571,281.8 tonnes** estimated CO2 emissions
- **33,117,785 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2019 |
| 2 | SkyWest Airlines | 1846 |
| 3 | IndiGo | 1109 |
| 4 | EJA | 819 |
| 5 | American Airlines | 790 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 620 |
| 8 | Lufthansa | 509 |
| 9 | Vueling | 476 |
| 10 | AXM | 473 |
| 11 | LATAM Airlines | 467 |
| 12 | All Nippon Airways | 429 |
| 13 | AZU | 406 |
| 14 | Delta Air Lines | 396 |
| 15 | QLK | 385 |
| 16 | WIF | 380 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 364 |
| 19 | Alaska Airlines | 323 |
| 20 | AEE | 321 |
| 21 | EJU | 315 |
| 22 | VIV | 304 |
| 23 | easyJet | 303 |
| 24 | Japan Airlines | 286 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 259 |
| 27 | JetBlue | 252 |
| 28 | United Airlines | 251 |
| 29 | AXB | 248 |
| 30 | GLO | 241 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37886 |
| 2 | 🇮🇳 IN | 3447 |
| 3 | 🇪🇸 ES | 3440 |
| 4 | 🇦🇺 AU | 3282 |
| 5 | 🇧🇷 BR | 2789 |
| 6 | 🇯🇵 JP | 2602 |
| 7 | 🇮🇹 IT | 2586 |
| 8 | 🇩🇪 DE | 2451 |
| 9 | 🇨🇦 CA | 2337 |
| 10 | 🇨🇴 CO | 2210 |
| 11 | 🇬🇧 GB | 1938 |
| 12 | 🇫🇷 FR | 1805 |
| 13 | 🇲🇽 MX | 1477 |
| 14 | 🇬🇷 GR | 1444 |
| 15 | 🇨🇭 CH | 1299 |
| 16 | 🇳🇴 NO | 1211 |
| 17 | 🇲🇾 MY | 1153 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 919 |
| 20 | 🇹🇭 TH | 847 |
| 21 | 🇵🇭 PH | 835 |
| 22 | 🇹🇷 TR | 833 |
| 23 | 🇰🇷 KR | 776 |
| 24 | 🇵🇱 PL | 745 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 586 |
| 27 | 🇲🇪 ME | 506 |
| 28 | 🇳🇱 NL | 484 |
| 29 | 🇲🇴 MO | 452 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1123 |
| 2 | Tokyo International Airport |  | JP | 885 |
| 3 | Denver International Airport |  | US | 795 |
| 4 | El Dorado International Airport |  | CO | 769 |
| 5 | Indira Gandhi International Airport |  | IN | 737 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 715 |
| 7 | Guaymaral Airport |  | CO | 618 |
| 8 | Harry Reid International Airport |  | US | 618 |
| 9 | Zurich Airport |  | CH | 563 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 482 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Chicago O'Hare International Airport |  | US | 467 |
| 14 | Kuala Lumpur International Airport |  | MY | 462 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 16 | Macau International Airport |  | MO | 452 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 438 |
| 18 | Madrid Barajas International Airport |  | ES | 421 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 408 |
| 21 | Malpensa International Airport |  | IT | 401 |
| 22 | Congonhas Airport |  | BR | 398 |
| 23 | Tenerife Norte Airport |  | ES | 395 |
| 24 | Ninoy Aquino International Airport |  | PH | 386 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 361 |
| 26 | Salt Lake City International Airport |  | US | 358 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 352 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 345 |
| 31 | Reno/Tahoe International Airport |  | US | 329 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 328 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 324 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | Barcelona International Airport |  | ES | 314 |
| 36 | O. R. Tambo International Airport |  | ZA | 313 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 282 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 247 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 222 | 1h 7m | 706 km | 2,702.9 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 182 | 14m | 114 km | 357.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 136 | 1h 27m | 910 km | 2,134.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 96 | 44m | 452 km | 748.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 76 | 20m | 147 km | 192.3 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 67 | 1h 0m | 695 km | 803.1 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 64 | 16m | 162 km | 179.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SKW3691 | SkyWest Airlines | Los Angeles International Airport (KLAX) | Denver International Airport (KDEN) | 2026-04-21 23:01 UTC | 2026-04-22 00:51 UTC | 1h 50m |
| N3049Q |  | Las Cruces International Airport (KLRU) | Truth Or Consequences Municipal Airport (KTCS) | 2026-04-22 00:14 UTC | 2026-04-22 00:50 UTC | 35m |
| MZT | MZT | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-22 00:10 UTC | 2026-04-22 00:48 UTC | 37m |
| N20G |  | Akron-Canton Regional Airport (KCAK) | Akron-Canton Regional Airport (KCAK) | 2026-04-22 00:24 UTC | 2026-04-22 00:45 UTC | 20m |
| N500FT |  | Rainelle Airport (WV30) | Summersville Airport (KSXL) | 2026-04-22 00:32 UTC | 2026-04-22 00:43 UTC | 11m |
| CPA3144 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-21 13:21 UTC | 2026-04-22 00:41 UTC | 11h 19m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-04-22 00:19 UTC | 2026-04-22 00:38 UTC | 19m |
| N7QN |  | Double Eagle Ii Airport (KAEG) | Manzano Mtn Air Ranch Airport (NM89) | 2026-04-22 00:20 UTC | 2026-04-22 00:38 UTC | 18m |
| AM341 |  | Melbourne Essendon Airport (YMEN) | Albury Airport (YMAY) | 2026-04-21 23:58 UTC | 2026-04-22 00:37 UTC | 39m |
| N9957M |  | Homer Airport (PAHO) | Seldovia Airport (PASO) | 2026-04-22 00:23 UTC | 2026-04-22 00:35 UTC | 12m |
| PNC0600 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-21 23:43 UTC | 2026-04-22 00:31 UTC | 47m |
| URSA23 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-21 22:52 UTC | 2026-04-22 00:30 UTC | 1h 38m |
| MAZER61 | MAZ | Fremont County Airport (K1V6) | Fremont County Airport (K1V6) | 2026-04-21 23:23 UTC | 2026-04-22 00:26 UTC | 1h 2m |
| CPA632 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-21 12:56 UTC | 2026-04-22 00:19 UTC | 11h 22m |
| N992VT |  | Patrick Leahy Burlington International Airport (KBTV) | Auburn/Lewiston Municipal Airport (KLEW) | 2026-04-21 23:16 UTC | 2026-04-22 00:18 UTC | 1h 1m |
| N36PJ |  | Scottsdale Airport (KSDL) | Henderson Executive Airport (KHND) | 2026-04-21 23:16 UTC | 2026-04-22 00:17 UTC | 1h 1m |
| JL2323 |  | Osaka International Airport (RJOO) | Okayama Airport (RJOB) | 2026-04-22 00:04 UTC | 2026-04-22 00:15 UTC | 11m |
| LR453 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-04-21 23:42 UTC | 2026-04-22 00:14 UTC | 32m |
| ZJO | ZJO | Mangalore Airport (YMNG) | Bacchus Marsh Airport (YBSS) | 2026-04-21 23:34 UTC | 2026-04-22 00:11 UTC | 37m |
| N8258P |  | Phoenix Deer Valley Airport (KDVT) | 42AZ (42AZ) | 2026-04-21 23:49 UTC | 2026-04-22 00:08 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
