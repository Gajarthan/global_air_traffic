# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_15:25:52_UTC-green)

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

**Latest saved flight:** 2026-04-24 15:25:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 15:25:52 UTC

- **51,417** saved flights
- **20,579** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **51,417** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **615,520.6 tonnes** estimated CO2 emissions
- **35,682,353 km** total distance flown
- **834 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2170 |
| 2 | SkyWest Airlines | 1941 |
| 3 | IndiGo | 1193 |
| 4 | EJA | 884 |
| 5 | American Airlines | 824 |
| 6 | Southwest Airlines | 725 |
| 7 | ENY | 653 |
| 8 | Lufthansa | 602 |
| 9 | Vueling | 516 |
| 10 | AXM | 507 |
| 11 | LATAM Airlines | 497 |
| 12 | All Nippon Airways | 465 |
| 13 | AZU | 435 |
| 14 | WIF | 428 |
| 15 | Delta Air Lines | 420 |
| 16 | QLK | 412 |
| 17 | Swiss International | 394 |
| 18 | LXJ | 386 |
| 19 | AEE | 347 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 329 |
| 22 | easyJet | 325 |
| 23 | VIV | 323 |
| 24 | Japan Airlines | 304 |
| 25 | Air France | 294 |
| 26 | AXB | 279 |
| 27 | Cathay Pacific | 272 |
| 28 | JetBlue | 265 |
| 29 | AIQ | 264 |
| 30 | United Airlines | 263 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40651 |
| 2 | 🇮🇳 IN | 3757 |
| 3 | 🇪🇸 ES | 3726 |
| 4 | 🇦🇺 AU | 3568 |
| 5 | 🇧🇷 BR | 2962 |
| 6 | 🇯🇵 JP | 2809 |
| 7 | 🇩🇪 DE | 2760 |
| 8 | 🇮🇹 IT | 2758 |
| 9 | 🇨🇦 CA | 2550 |
| 10 | 🇨🇴 CO | 2374 |
| 11 | 🇬🇧 GB | 2142 |
| 12 | 🇫🇷 FR | 1987 |
| 13 | 🇲🇽 MX | 1576 |
| 14 | 🇬🇷 GR | 1560 |
| 15 | 🇨🇭 CH | 1456 |
| 16 | 🇳🇴 NO | 1391 |
| 17 | 🇲🇾 MY | 1238 |
| 18 | 🇿🇦 ZA | 1069 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 943 |
| 21 | 🇹🇷 TR | 923 |
| 22 | 🇵🇭 PH | 897 |
| 23 | 🇰🇷 KR | 858 |
| 24 | 🇵🇱 PL | 827 |
| 25 | 🇬🇹 GT | 785 |
| 26 | 🇲🇦 MA | 631 |
| 27 | 🇲🇪 ME | 551 |
| 28 | 🇳🇱 NL | 523 |
| 29 | 🇲🇴 MO | 496 |
| 30 | 🇧🇸 BS | 448 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1180 |
| 2 | Tokyo International Airport |  | JP | 955 |
| 3 | Denver International Airport |  | US | 845 |
| 4 | El Dorado International Airport |  | CO | 811 |
| 5 | Indira Gandhi International Airport |  | IN | 801 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 772 |
| 7 | Guaymaral Airport |  | CO | 699 |
| 8 | Harry Reid International Airport |  | US | 668 |
| 9 | Zurich Airport |  | CH | 607 |
| 10 | Frankfurt am Main International Airport |  | DE | 588 |
| 11 | La Aurora Airport |  | GT | 585 |
| 12 | Chicago O'Hare International Airport |  | US | 504 |
| 13 | Macau International Airport |  | MO | 496 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 15 | Kuala Lumpur International Airport |  | MY | 491 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 483 |
| 17 | Madrid Barajas International Airport |  | ES | 469 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 465 |
| 19 | Bengaluru International Airport |  | IN | 446 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 425 |
| 22 | Malpensa International Airport |  | IT | 421 |
| 23 | Ninoy Aquino International Airport |  | PH | 414 |
| 24 | Tenerife Norte Airport |  | ES | 410 |
| 25 | Charles de Gaulle International Airport |  | FR | 386 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 384 |
| 27 | Salt Lake City International Airport |  | US | 377 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 377 |
| 29 | Daniel K Inouye International Airport |  | US | 375 |
| 30 | Capua Airport |  | IT | 355 |
| 31 | Vitoria/Foronda Airport |  | ES | 350 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 346 |
| 33 | Barcelona International Airport |  | ES | 346 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 344 |
| 35 | Reno/Tahoe International Airport |  | US | 343 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 343 |
| 37 | O. R. Tambo International Airport |  | ZA | 342 |
| 38 | Don Mueang International Airport |  | TH | 319 |
| 39 | Calgary International Airport |  | CA | 310 |
| 40 | Viracopos International Airport |  | BR | 302 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 283 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 241 | 1h 7m | 706 km | 2,934.2 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 197 | 14m | 114 km | 386.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 154 | 21m | 244 km | 648.5 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 153 | 28m | 304 km | 802.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 147 | 1h 27m | 910 km | 2,306.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 136 | 19m | 165 km | 386.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 129 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 125 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 120 | 26m | 275 km | 568.6 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 105 | 44m | 452 km | 818.3 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 92 | 1h 12m | 770 km | 1,222.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 88 | 31m | 369 km | 560.1 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 88 | 20m | 250 km | 380.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 84 | 27m | 215 km | 311.1 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 82 | 20m | 147 km | 207.5 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 78 | 27m | 152 km | 203.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 74 | 1h 41m | 1,156 km | 1,476.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 67 | 16m | 162 km | 187.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-04-24 15:04 UTC | 2026-04-24 15:25 UTC | 21m |
| HCX43 | HCX | Palanga International Airport (EYPA) | Tallinn Airport (EETN) | 2026-04-24 14:36 UTC | 2026-04-24 15:22 UTC | 45m |
| TIGER33 | TIG | Sandy Creek Airport (73TX) | Dunbar Ranch Airport (0XS8) | 2026-04-24 14:50 UTC | 2026-04-24 15:21 UTC | 31m |
| N70JA |  | Witham Field (KSUA) | Indiantown Airport (KX58) | 2026-04-24 15:04 UTC | 2026-04-24 15:19 UTC | 15m |
| N6189Q |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-24 14:36 UTC | 2026-04-24 15:15 UTC | 39m |
| N4334X |  | Waterbury-Oxford Airport (KOXC) | Westmoreland Airport (49NY) | 2026-04-24 14:53 UTC | 2026-04-24 15:15 UTC | 22m |
| N484MF |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-24 14:19 UTC | 2026-04-24 15:12 UTC | 53m |
| N555BH |  | Tusquittee Landing Airport (NC08) | Tusquittee Landing Airport (NC08) | 2026-04-24 14:06 UTC | 2026-04-24 15:09 UTC | 1h 2m |
| ZUISN | ZUI | Malmesbury Airport (FAMY) | Ysterplaat Air Force Base (FAYP) | 2026-04-24 14:49 UTC | 2026-04-24 15:09 UTC | 19m |
| N169PM |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-04-24 14:52 UTC | 2026-04-24 15:08 UTC | 15m |
| N71F |  | Indianapolis International Airport (KIND) | 16KY (16KY) | 2026-04-24 14:31 UTC | 2026-04-24 15:08 UTC | 36m |
| QTR8436 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-24 08:27 UTC | 2026-04-24 15:07 UTC | 6h 40m |
| N5623E |  | Schaumburg Regional Airport (K06C) | Ruder Airport (59IL) | 2026-04-24 14:47 UTC | 2026-04-24 15:04 UTC | 17m |
| GGRUN | GGR | Newcastle Airport (EGNT) | White Waltham Airfield (EGLM) | 2026-04-24 13:26 UTC | 2026-04-24 15:03 UTC | 1h 37m |
| N349ME |  | Norwood Memorial Airport (KOWD) | Cape Cod Gateway Airport (KHYA) | 2026-04-24 14:36 UTC | 2026-04-24 15:02 UTC | 25m |
| QTR8402 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-24 08:16 UTC | 2026-04-24 15:02 UTC | 6h 46m |
| NOAA43 | NOA | Lakeland Linder International Airport (KLAL) | Patrick Space Force Base Airport (KCOF) | 2026-04-24 13:39 UTC | 2026-04-24 15:02 UTC | 1h 22m |
| HK5271G |  | Guaymaral Airport (SKGY) | Madrid Air Base (SKMA) | 2026-04-24 14:31 UTC | 2026-04-24 14:59 UTC | 28m |
| CPA392 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-24 07:01 UTC | 2026-04-24 14:59 UTC | 7h 57m |
| N172RR |  | Groton-New London Airport (KGON) | Worcester Regional Airport (KORH) | 2026-04-24 14:14 UTC | 2026-04-24 14:58 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
