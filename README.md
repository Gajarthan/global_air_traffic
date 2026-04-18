# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_16:12:18_UTC-green)

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

**Latest saved flight:** 2026-04-18 16:12:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 16:12:18 UTC

- **41,420** saved flights
- **17,501** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,420** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **497,894.3 tonnes** estimated CO2 emissions
- **28,863,435 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1742 |
| 2 | SkyWest Airlines | 1594 |
| 3 | IndiGo | 1026 |
| 4 | EJA | 716 |
| 5 | American Airlines | 685 |
| 6 | Southwest Airlines | 580 |
| 7 | ENY | 524 |
| 8 | AXM | 434 |
| 9 | Vueling | 414 |
| 10 | LATAM Airlines | 411 |
| 11 | Lufthansa | 405 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 368 |
| 14 | Delta Air Lines | 348 |
| 15 | QLK | 341 |
| 16 | LXJ | 326 |
| 17 | WIF | 324 |
| 18 | Swiss International | 319 |
| 19 | AEE | 280 |
| 20 | Alaska Airlines | 278 |
| 21 | EJU | 272 |
| 22 | easyJet | 269 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 235 |
| 26 | United Airlines | 223 |
| 27 | JetBlue | 222 |
| 28 | AXB | 219 |
| 29 | GLO | 218 |
| 30 | EDV | 216 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32549 |
| 2 | 🇮🇳 IN | 3133 |
| 3 | 🇪🇸 ES | 3059 |
| 4 | 🇦🇺 AU | 2918 |
| 5 | 🇧🇷 BR | 2474 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2151 |
| 8 | 🇩🇪 DE | 2105 |
| 9 | 🇨🇦 CA | 2018 |
| 10 | 🇨🇴 CO | 1957 |
| 11 | 🇬🇧 GB | 1687 |
| 12 | 🇫🇷 FR | 1599 |
| 13 | 🇲🇽 MX | 1295 |
| 14 | 🇬🇷 GR | 1261 |
| 15 | 🇨🇭 CH | 1166 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1030 |
| 18 | 🇿🇦 ZA | 867 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 740 |
| 22 | 🇹🇷 TR | 724 |
| 23 | 🇬🇹 GT | 698 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 659 |
| 26 | 🇲🇦 MA | 509 |
| 27 | 🇳🇱 NL | 425 |
| 28 | 🇲🇪 ME | 424 |
| 29 | 🇧🇸 BS | 391 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 950 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 679 |
| 5 | Indira Gandhi International Airport |  | IN | 674 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 627 |
| 7 | Harry Reid International Airport |  | US | 531 |
| 8 | Guaymaral Airport |  | CO | 521 |
| 9 | La Aurora Airport |  | GT | 514 |
| 10 | Zurich Airport |  | CH | 501 |
| 11 | Kuala Lumpur International Airport |  | MY | 415 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 405 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 394 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 394 |
| 16 | Macau International Airport |  | MO | 377 |
| 17 | Madrid Barajas International Airport |  | ES | 377 |
| 18 | Frankfurt am Main International Airport |  | DE | 374 |
| 19 | Bengaluru International Airport |  | IN | 370 |
| 20 | Tenerife Norte Airport |  | ES | 362 |
| 21 | Charlotte/Douglas International Airport |  | US | 361 |
| 22 | Congonhas Airport |  | BR | 360 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 334 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 314 |
| 27 | Daniel K Inouye International Airport |  | US | 307 |
| 28 | Charles de Gaulle International Airport |  | FR | 304 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 303 |
| 30 | Vitoria/Foronda Airport |  | ES | 293 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 288 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 285 |
| 33 | O. R. Tambo International Airport |  | ZA | 281 |
| 34 | Reno/Tahoe International Airport |  | US | 281 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 280 |
| 36 | Capua Airport |  | IT | 274 |
| 37 | Barcelona International Airport |  | ES | 265 |
| 38 | Viracopos International Airport |  | BR | 254 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Don Mueang International Airport |  | TH | 246 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 208 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 110 | 21m | 244 km | 463.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 104 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 69 | 20m | 250 km | 298.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 62 | 16m | 162 km | 173.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASA183 | Alaska Airlines | Portland International Airport (KPDX) | Bermuda Dunes Airport (KUDD) | 2026-04-18 14:17 UTC | 2026-04-18 16:12 UTC | 1h 54m |
| N10BB |  | Chester Catawba Regional Airport (KDCM) | Chester Catawba Regional Airport (KDCM) | 2026-04-18 15:24 UTC | 2026-04-18 16:11 UTC | 47m |
| N61GA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-18 15:45 UTC | 2026-04-18 16:07 UTC | 22m |
| N497PJ |  | Rio Vista Municipal Airport (KO88) | Rio Vista Municipal Airport (KO88) | 2026-04-18 15:32 UTC | 2026-04-18 16:06 UTC | 34m |
| N208JP |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-04-18 15:12 UTC | 2026-04-18 16:01 UTC | 49m |
| N13715 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-18 15:43 UTC | 2026-04-18 15:58 UTC | 15m |
| N32300 |  | Cecil Airport (KVQQ) | Thrifts Airport (FL11) | 2026-04-18 15:45 UTC | 2026-04-18 15:57 UTC | 12m |
| VAR476 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-18 15:42 UTC | 2026-04-18 15:49 UTC | 6m |
| CXK657 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-18 15:27 UTC | 2026-04-18 15:48 UTC | 21m |
| ERU460 | ERU | Daytona Beach International Airport (KDAB) | Skinners Wholesale Nursery Airport (16FD) | 2026-04-18 15:22 UTC | 2026-04-18 15:48 UTC | 26m |
| BOX738 | BOX | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-04-18 02:00 UTC | 2026-04-18 15:47 UTC | 13h 46m |
| XBSCZ | XBS | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-04-18 13:51 UTC | 2026-04-18 15:46 UTC | 1h 54m |
| FJIRZ | FJI | Toulouse-Lasbordes Airport (LFCL) | Toulouse-Lasbordes Airport (LFCL) | 2026-04-18 15:14 UTC | 2026-04-18 15:45 UTC | 31m |
| CXK329 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-18 15:13 UTC | 2026-04-18 15:43 UTC | 30m |
| N735CF |  | Rocky Mountain Metro Airport (KBJC) | Central Colorado Regional Airport (KAEJ) | 2026-04-18 15:01 UTC | 2026-04-18 15:43 UTC | 42m |
| CFSCF | CFS | Peterborough Airport (CYPQ) | Peterborough Airport (CYPQ) | 2026-04-18 15:21 UTC | 2026-04-18 15:42 UTC | 21m |
| EJA412 | EJA | Palm Beach International Airport (KPBI) | Lincoln Airport (KLNK) | 2026-04-18 12:00 UTC | 2026-04-18 15:42 UTC | 3h 42m |
| OKDUD62 | OKD | Jicin Airport (LKJC) | Horice Airport (LKHC) | 2026-04-18 15:28 UTC | 2026-04-18 15:42 UTC | 13m |
| CXK219 | CXK | Concord-Padgett Regional Airport (KJQF) | Mid-Carolina Regional Airport (KRUQ) | 2026-04-18 15:14 UTC | 2026-04-18 15:41 UTC | 27m |
| FFL1242 | FFL | John Wayne/Orange County Airport (KSNA) | AZ86 (AZ86) | 2026-04-18 14:28 UTC | 2026-04-18 15:41 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
