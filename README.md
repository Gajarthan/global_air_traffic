# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_13:57:57_UTC-green)

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

**Latest saved flight:** 2026-04-19 13:57:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 13:57:57 UTC

- **43,025** saved flights
- **17,972** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **43,025** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **518,310.4 tonnes** estimated CO2 emissions
- **30,046,981 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1810 |
| 2 | SkyWest Airlines | 1654 |
| 3 | IndiGo | 1063 |
| 4 | EJA | 734 |
| 5 | American Airlines | 706 |
| 6 | Southwest Airlines | 599 |
| 7 | ENY | 556 |
| 8 | AXM | 446 |
| 9 | Vueling | 430 |
| 10 | LATAM Airlines | 429 |
| 11 | Lufthansa | 427 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 381 |
| 14 | Delta Air Lines | 364 |
| 15 | QLK | 354 |
| 16 | LXJ | 334 |
| 17 | Swiss International | 334 |
| 18 | WIF | 333 |
| 19 | AEE | 291 |
| 20 | Alaska Airlines | 290 |
| 21 | EJU | 284 |
| 22 | easyJet | 277 |
| 23 | VIV | 271 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 244 |
| 26 | United Airlines | 230 |
| 27 | AXB | 228 |
| 28 | JetBlue | 228 |
| 29 | GLO | 225 |
| 30 | AIQ | 222 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33753 |
| 2 | 🇮🇳 IN | 3272 |
| 3 | 🇪🇸 ES | 3165 |
| 4 | 🇦🇺 AU | 3025 |
| 5 | 🇧🇷 BR | 2576 |
| 6 | 🇯🇵 JP | 2411 |
| 7 | 🇮🇹 IT | 2252 |
| 8 | 🇩🇪 DE | 2185 |
| 9 | 🇨🇦 CA | 2086 |
| 10 | 🇨🇴 CO | 1980 |
| 11 | 🇬🇧 GB | 1751 |
| 12 | 🇫🇷 FR | 1660 |
| 13 | 🇲🇽 MX | 1335 |
| 14 | 🇬🇷 GR | 1323 |
| 15 | 🇨🇭 CH | 1195 |
| 16 | 🇲🇾 MY | 1090 |
| 17 | 🇳🇴 NO | 1059 |
| 18 | 🇿🇦 ZA | 905 |
| 19 | 🇳🇿 NZ | 875 |
| 20 | 🇵🇭 PH | 791 |
| 21 | 🇹🇭 TH | 780 |
| 22 | 🇹🇷 TR | 763 |
| 23 | 🇰🇷 KR | 728 |
| 24 | 🇬🇹 GT | 709 |
| 25 | 🇵🇱 PL | 687 |
| 26 | 🇲🇦 MA | 538 |
| 27 | 🇲🇪 ME | 451 |
| 28 | 🇳🇱 NL | 441 |
| 29 | 🇮🇩 ID | 400 |
| 30 | 🇧🇸 BS | 399 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 995 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 705 |
| 4 | Indira Gandhi International Airport |  | IN | 705 |
| 5 | El Dorado International Airport |  | CO | 694 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 657 |
| 7 | Harry Reid International Airport |  | US | 548 |
| 8 | Guaymaral Airport |  | CO | 533 |
| 9 | La Aurora Airport |  | GT | 523 |
| 10 | Zurich Airport |  | CH | 521 |
| 11 | Kuala Lumpur International Airport |  | MY | 432 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 422 |
| 13 | Chicago O'Hare International Airport |  | US | 415 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 412 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 407 |
| 16 | Frankfurt am Main International Airport |  | DE | 398 |
| 17 | Macau International Airport |  | MO | 397 |
| 18 | Madrid Barajas International Airport |  | ES | 385 |
| 19 | Bengaluru International Airport |  | IN | 385 |
| 20 | Tenerife Norte Airport |  | ES | 375 |
| 21 | Charlotte/Douglas International Airport |  | US | 371 |
| 22 | Congonhas Airport |  | BR | 368 |
| 23 | Ninoy Aquino International Airport |  | PH | 366 |
| 24 | Malpensa International Airport |  | IT | 353 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 329 |
| 26 | Netaji Subhash Chandra Bose International Airport |  | IN | 326 |
| 27 | Salt Lake City International Airport |  | US | 325 |
| 28 | Daniel K Inouye International Airport |  | US | 319 |
| 29 | Charles de Gaulle International Airport |  | FR | 319 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 302 |
| 31 | Vitoria/Foronda Airport |  | ES | 300 |
| 32 | Reno/Tahoe International Airport |  | US | 294 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 293 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 290 |
| 35 | O. R. Tambo International Airport |  | ZA | 289 |
| 36 | Capua Airport |  | IT | 288 |
| 37 | Barcelona International Airport |  | ES | 277 |
| 38 | Don Mueang International Airport |  | TH | 265 |
| 39 | Viracopos International Airport |  | BR | 264 |
| 40 | Calgary International Airport |  | CA | 256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 214 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 162 | 14m | 114 km | 317.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 118 | 21m | 244 km | 496.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 106 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 89 | 21m | 99 km | 152.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 77 | 31m | 369 km | 490.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 69 | 20m | 147 km | 174.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 69 | 52m | 556 km | 661.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 66 | 26m | 215 km | 244.4 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 60 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 53m | 1,304 km | 1,349.8 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 0m | 695 km | 707.2 t |
| 30 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N985AA |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-04-19 13:19 UTC | 2026-04-19 13:57 UTC | 38m |
| AIC4MC | Air India | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-19 13:39 UTC | 2026-04-19 13:52 UTC | 12m |
| N876SC |  | Grand Prairie Municipal Airport (KGPM) | Waco Regional Airport (KACT) | 2026-04-19 13:14 UTC | 2026-04-19 13:50 UTC | 36m |
| ERU450 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-19 12:09 UTC | 2026-04-19 13:50 UTC | 1h 41m |
| CPA393 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-19 06:10 UTC | 2026-04-19 13:36 UTC | 7h 25m |
| AZG1647 | AZG | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-04-19 07:10 UTC | 2026-04-19 13:36 UTC | 6h 26m |
| N264SA |  | Sundance Airport (KHSD) | Neversweat Airport (1OK0) | 2026-04-19 12:51 UTC | 2026-04-19 13:35 UTC | 43m |
| CSN356 | China Southern | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-19 06:04 UTC | 2026-04-19 13:32 UTC | 7h 28m |
| LXJ405 | LXJ | Palm Beach International Airport (KPBI) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-19 12:03 UTC | 2026-04-19 13:31 UTC | 1h 28m |
| N2382R |  | Tampa Executive Airport (KVDF) | Tampa Executive Airport (KVDF) | 2026-04-19 12:08 UTC | 2026-04-19 13:20 UTC | 1h 12m |
| N179PF |  | Des Moines International Airport (KDSM) | St Paul Downtown Holman Field (KSTP) | 2026-04-19 12:34 UTC | 2026-04-19 13:19 UTC | 44m |
| N249EB |  | Gainesville Municipal Airport (KGLE) | Tightwaad Air Ranch Airport (XA16) | 2026-04-19 12:51 UTC | 2026-04-19 13:13 UTC | 21m |
| RYR5XB | Ryanair | Dublin Airport (EIDW) | Newquay Cornwall Airport (EGHQ) | 2026-04-19 12:29 UTC | 2026-04-19 13:07 UTC | 38m |
| ANE72UZ | ANE | Madrid Barajas International Airport (LEMD) | Torino / Caselle International Airport (LIMF) | 2026-04-19 11:24 UTC | 2026-04-19 13:06 UTC | 1h 41m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-19 12:39 UTC | 2026-04-19 13:06 UTC | 26m |
| N6694G |  | Ann Arbor Municipal Airport (KARB) | Lenawee County Airport (KADG) | 2026-04-19 12:39 UTC | 2026-04-19 13:05 UTC | 25m |
| WIF66D | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-04-19 12:47 UTC | 2026-04-19 13:03 UTC | 16m |
| ANS900 | ANS | El Boldal Airport (SCBD) | Chicureo Airport (SCHC) | 2026-04-19 12:48 UTC | 2026-04-19 13:02 UTC | 13m |
| N134AM |  | Villa Char Mar Airport (1FA9) | Villa Char Mar Airport (1FA9) | 2026-04-19 13:02 UTC | 2026-04-19 13:02 UTC | 0m |
| PDT5800 | PDT | Philadelphia International Airport (KPHL) | Harrisburg International Airport (KMDT) | 2026-04-19 12:43 UTC | 2026-04-19 13:02 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
