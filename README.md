# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_15:32:21_UTC-green)

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

**Latest saved flight:** 2026-04-19 15:32:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 15:32:21 UTC

- **43,178** saved flights
- **18,032** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,178** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **520,086.3 tonnes** estimated CO2 emissions
- **30,149,928 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1816 |
| 2 | SkyWest Airlines | 1655 |
| 3 | IndiGo | 1068 |
| 4 | EJA | 737 |
| 5 | American Airlines | 708 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 557 |
| 8 | AXM | 446 |
| 9 | LATAM Airlines | 434 |
| 10 | Lufthansa | 432 |
| 11 | Vueling | 430 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 382 |
| 14 | Delta Air Lines | 364 |
| 15 | QLK | 354 |
| 16 | Swiss International | 337 |
| 17 | LXJ | 335 |
| 18 | WIF | 335 |
| 19 | AEE | 293 |
| 20 | Alaska Airlines | 290 |
| 21 | EJU | 285 |
| 22 | easyJet | 277 |
| 23 | VIV | 272 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 244 |
| 26 | AXB | 230 |
| 27 | United Airlines | 230 |
| 28 | JetBlue | 229 |
| 29 | GLO | 226 |
| 30 | AIQ | 222 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33867 |
| 2 | 🇮🇳 IN | 3285 |
| 3 | 🇪🇸 ES | 3186 |
| 4 | 🇦🇺 AU | 3029 |
| 5 | 🇧🇷 BR | 2590 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2267 |
| 8 | 🇩🇪 DE | 2199 |
| 9 | 🇨🇦 CA | 2089 |
| 10 | 🇨🇴 CO | 1990 |
| 11 | 🇬🇧 GB | 1757 |
| 12 | 🇫🇷 FR | 1664 |
| 13 | 🇲🇽 MX | 1338 |
| 14 | 🇬🇷 GR | 1333 |
| 15 | 🇨🇭 CH | 1200 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1069 |
| 18 | 🇿🇦 ZA | 907 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 764 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 711 |
| 25 | 🇵🇱 PL | 691 |
| 26 | 🇲🇦 MA | 538 |
| 27 | 🇲🇪 ME | 452 |
| 28 | 🇳🇱 NL | 446 |
| 29 | 🇧🇸 BS | 400 |
| 30 | 🇮🇩 ID | 400 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 998 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Indira Gandhi International Airport |  | IN | 707 |
| 4 | Denver International Airport |  | US | 705 |
| 5 | El Dorado International Airport |  | CO | 696 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 663 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 539 |
| 9 | La Aurora Airport |  | GT | 524 |
| 10 | Zurich Airport |  | CH | 524 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 415 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 412 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 403 |
| 17 | Macau International Airport |  | MO | 399 |
| 18 | Madrid Barajas International Airport |  | ES | 388 |
| 19 | Bengaluru International Airport |  | IN | 388 |
| 20 | Tenerife Norte Airport |  | ES | 379 |
| 21 | Charlotte/Douglas International Airport |  | US | 373 |
| 22 | Congonhas Airport |  | BR | 372 |
| 23 | Ninoy Aquino International Airport |  | PH | 366 |
| 24 | Malpensa International Airport |  | IT | 355 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 27 | Salt Lake City International Airport |  | US | 325 |
| 28 | Daniel K Inouye International Airport |  | US | 319 |
| 29 | Charles de Gaulle International Airport |  | FR | 319 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 302 |
| 31 | Vitoria/Foronda Airport |  | ES | 301 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 294 |
| 33 | Reno/Tahoe International Airport |  | US | 294 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 292 |
| 35 | O. R. Tambo International Airport |  | ZA | 290 |
| 36 | Capua Airport |  | IT | 290 |
| 37 | Barcelona International Airport |  | ES | 279 |
| 38 | Viracopos International Airport |  | BR | 265 |
| 39 | Don Mueang International Airport |  | TH | 265 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 217 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 164 | 14m | 114 km | 321.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 118 | 21m | 244 km | 496.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 100 | 26m | 275 km | 473.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 71 | 20m | 147 km | 179.7 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 66 | 26m | 215 km | 244.4 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 61 | 13m | - | - |
| 27 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 59 | 1h 21m | 961 km | 978.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRF1 | TRF | Addison Airport (KADS) | Indianhead Ranch Airport (1TS9) | 2026-04-19 15:13 UTC | 2026-04-19 15:32 UTC | 18m |
| SD1 |  | Tri-County Aerodrome (48TX) | 52TA (52TA) | 2026-04-19 14:32 UTC | 2026-04-19 15:32 UTC | 59m |
| N164AS |  | Skywest Inc Airport (K7T7) | Midland International Air And Space Port Airport (KMAF) | 2026-04-19 15:19 UTC | 2026-04-19 15:30 UTC | 11m |
| QTR8082 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-19 08:27 UTC | 2026-04-19 15:29 UTC | 7h 1m |
| N4347R |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-04-19 14:45 UTC | 2026-04-19 15:24 UTC | 38m |
| N3892Q |  | Windsoar Airport (1MO2) | Johnson County Executive Airport (KOJC) | 2026-04-19 15:00 UTC | 2026-04-19 15:20 UTC | 19m |
| N544BH |  | Beaufort Executive Airport (KARW) | SC28 (SC28) | 2026-04-19 14:55 UTC | 2026-04-19 15:18 UTC | 22m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-19 14:26 UTC | 2026-04-19 15:16 UTC | 50m |
| N115JR |  | Hicks Airfield (KT67) | Decatur Municipal Airport (KLUD) | 2026-04-19 15:03 UTC | 2026-04-19 15:15 UTC | 12m |
| N167CS |  | K00V (K00V) | Telluride Regional Airport (KTEX) | 2026-04-19 13:24 UTC | 2026-04-19 15:05 UTC | 1h 41m |
| N654DT |  | Ranchaero Grand Vista Airport (47FL) | FL61 (FL61) | 2026-04-19 14:47 UTC | 2026-04-19 15:04 UTC | 16m |
| N491LG |  | Tall Timber Airport (CD28) | La Garita Creek Ranch Airport (5CO6) | 2026-04-19 14:53 UTC | 2026-04-19 15:03 UTC | 9m |
| N39VF |  | Henderson Executive Airport (KHND) | Grand Canyon West Airport (K1G4) | 2026-04-19 14:15 UTC | 2026-04-19 15:00 UTC | 44m |
| N900JW |  | Fort Smith Regional Airport (KFSM) | Wilson Ranch Airport (79OK) | 2026-04-19 14:35 UTC | 2026-04-19 14:59 UTC | 23m |
| N88810 |  | Lakeland Linder International Airport (KLAL) | Zephyrhills Municipal Airport (KZPH) | 2026-04-19 14:47 UTC | 2026-04-19 14:59 UTC | 11m |
| GCLYJ | GCL | Fife Airport (EGPJ) | Fife Airport (EGPJ) | 2026-04-19 14:32 UTC | 2026-04-19 14:57 UTC | 25m |
| N46CK |  | Savannah/Hilton Head International Airport (KSAV) | Demopolis Regional Airport (KDYA) | 2026-04-19 13:47 UTC | 2026-04-19 14:53 UTC | 1h 5m |
| N866P |  | St George Regional Airport (KSGU) | NV54 (NV54) | 2026-04-19 14:13 UTC | 2026-04-19 14:53 UTC | 39m |
| CPA337 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-19 07:15 UTC | 2026-04-19 14:52 UTC | 7h 37m |
| N5473R |  | Caddo Mills Municipal Airport (K7F3) | Jones Field (KF00) | 2026-04-19 14:18 UTC | 2026-04-19 14:52 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
