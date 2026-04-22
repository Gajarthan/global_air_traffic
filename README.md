# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_09:27:13_UTC-green)

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

**Latest saved flight:** 2026-04-22 09:27:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-22 09:27:13 UTC

- **47,632** saved flights
- **19,425** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,632** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **572,612.1 tonnes** estimated CO2 emissions
- **33,194,905 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2024 |
| 2 | SkyWest Airlines | 1846 |
| 3 | IndiGo | 1118 |
| 4 | EJA | 819 |
| 5 | American Airlines | 790 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 620 |
| 8 | Lufthansa | 510 |
| 9 | Vueling | 476 |
| 10 | AXM | 475 |
| 11 | LATAM Airlines | 467 |
| 12 | All Nippon Airways | 434 |
| 13 | AZU | 406 |
| 14 | Delta Air Lines | 396 |
| 15 | QLK | 386 |
| 16 | WIF | 381 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 364 |
| 19 | Alaska Airlines | 323 |
| 20 | AEE | 322 |
| 21 | EJU | 316 |
| 22 | easyJet | 304 |
| 23 | VIV | 304 |
| 24 | Japan Airlines | 287 |
| 25 | Air France | 269 |
| 26 | Cathay Pacific | 259 |
| 27 | JetBlue | 252 |
| 28 | United Airlines | 251 |
| 29 | AXB | 250 |
| 30 | GLO | 241 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37894 |
| 2 | 🇮🇳 IN | 3472 |
| 3 | 🇪🇸 ES | 3446 |
| 4 | 🇦🇺 AU | 3298 |
| 5 | 🇧🇷 BR | 2789 |
| 6 | 🇯🇵 JP | 2617 |
| 7 | 🇮🇹 IT | 2591 |
| 8 | 🇩🇪 DE | 2465 |
| 9 | 🇨🇦 CA | 2337 |
| 10 | 🇨🇴 CO | 2210 |
| 11 | 🇬🇧 GB | 1947 |
| 12 | 🇫🇷 FR | 1814 |
| 13 | 🇲🇽 MX | 1479 |
| 14 | 🇬🇷 GR | 1453 |
| 15 | 🇨🇭 CH | 1306 |
| 16 | 🇳🇴 NO | 1220 |
| 17 | 🇲🇾 MY | 1156 |
| 18 | 🇿🇦 ZA | 980 |
| 19 | 🇳🇿 NZ | 919 |
| 20 | 🇹🇭 TH | 857 |
| 21 | 🇵🇭 PH | 837 |
| 22 | 🇹🇷 TR | 835 |
| 23 | 🇰🇷 KR | 779 |
| 24 | 🇵🇱 PL | 750 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 588 |
| 27 | 🇲🇪 ME | 508 |
| 28 | 🇳🇱 NL | 485 |
| 29 | 🇲🇴 MO | 454 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1123 |
| 2 | Tokyo International Airport |  | JP | 891 |
| 3 | Denver International Airport |  | US | 795 |
| 4 | El Dorado International Airport |  | CO | 769 |
| 5 | Indira Gandhi International Airport |  | IN | 737 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 720 |
| 7 | Guaymaral Airport |  | CO | 618 |
| 8 | Harry Reid International Airport |  | US | 618 |
| 9 | Zurich Airport |  | CH | 563 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 484 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 477 |
| 13 | Chicago O'Hare International Airport |  | US | 467 |
| 14 | Kuala Lumpur International Airport |  | MY | 462 |
| 15 | Macau International Airport |  | MO | 454 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 438 |
| 18 | Bengaluru International Airport |  | IN | 422 |
| 19 | Madrid Barajas International Airport |  | ES | 421 |
| 20 | Charlotte/Douglas International Airport |  | US | 408 |
| 21 | Malpensa International Airport |  | IT | 402 |
| 22 | Congonhas Airport |  | BR | 398 |
| 23 | Tenerife Norte Airport |  | ES | 395 |
| 24 | Ninoy Aquino International Airport |  | PH | 387 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 362 |
| 26 | Salt Lake City International Airport |  | US | 358 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 354 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 348 |
| 31 | Reno/Tahoe International Airport |  | US | 329 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 328 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 324 |
| 34 | Vitoria/Foronda Airport |  | ES | 320 |
| 35 | O. R. Tambo International Airport |  | ZA | 316 |
| 36 | Barcelona International Airport |  | ES | 316 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 38 | Don Mueang International Airport |  | TH | 288 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 282 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 247 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 225 | 1h 7m | 706 km | 2,739.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 182 | 14m | 114 km | 357.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 167 | 24m | 225 km | 647.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 137 | 1h 27m | 910 km | 2,149.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 100 | 54m | 546 km | 941.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 97 | 44m | 452 km | 756.0 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 80 | 20m | 250 km | 345.6 t |
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
| UFX64 | UFX | RAF Woodvale (EGOW) | Blackpool International Airport (EGNH) | 2026-04-22 09:16 UTC | 2026-04-22 09:27 UTC | 11m |
| HSOMR3 | HSO | Husum-Schwesing Airport (EDXJ) | Helgoland-Dune Airport (EDXH) | 2026-04-22 08:54 UTC | 2026-04-22 09:20 UTC | 26m |
| FDX1404 | FDX | MS00 (MS00) | NM76 (NM76) | 2026-04-22 07:38 UTC | 2026-04-22 09:13 UTC | 1h 34m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-04-22 08:28 UTC | 2026-04-22 09:09 UTC | 41m |
| HBZYJ | HBZ | Saanen Airport (LSGK) | Sion Airport (LSGS) | 2026-04-22 08:25 UTC | 2026-04-22 09:00 UTC | 35m |
| RDF9 | RDF | Ingolstadt Manching Airport (ETSI) | Ingolstadt Manching Airport (ETSI) | 2026-04-22 08:40 UTC | 2026-04-22 08:58 UTC | 17m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-22 08:19 UTC | 2026-04-22 08:55 UTC | 36m |
| BOE8BX | BOE | Monte Prieto Ranch Airport (57NM) | Stallion Army Air Field (K95E) | 2026-04-22 08:03 UTC | 2026-04-22 08:55 UTC | 51m |
| I2315 |  | Pratica Di Mare Airport (LIRE) | Gioia Del Colle Airport (LIBV) | 2026-04-22 07:15 UTC | 2026-04-22 08:54 UTC | 1h 39m |
| GAF153 | GAF | Wunstorf Airport (ETNW) | Vilnius International Airport (EYVI) | 2026-04-22 07:00 UTC | 2026-04-22 08:54 UTC | 1h 54m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-22 08:23 UTC | 2026-04-22 08:52 UTC | 29m |
| AEE272 | AEE | Eleftherios Venizelos International Airport (LGAV) | Olimboi Airport (LG56) | 2026-04-22 08:27 UTC | 2026-04-22 08:50 UTC | 23m |
| EJU41ZW | EJU | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-04-22 07:33 UTC | 2026-04-22 08:49 UTC | 1h 16m |
| SPHOR | SPH | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-04-22 08:48 UTC | 2026-04-22 08:48 UTC | 0m |
| SEH400 | SEH | Eleftherios Venizelos International Airport (LGAV) | Naxos Airport (LGNX) | 2026-04-22 08:26 UTC | 2026-04-22 08:47 UTC | 20m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-22 08:32 UTC | 2026-04-22 08:46 UTC | 14m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-22 08:14 UTC | 2026-04-22 08:42 UTC | 27m |
| NAK729 | NAK | Saint-Yan Airport (LFLN) | Lyon-Bron Airport (LFLY) | 2026-04-22 08:05 UTC | 2026-04-22 08:41 UTC | 35m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Ambala Air Force Station (VIAM) | 2026-04-22 06:36 UTC | 2026-04-22 08:39 UTC | 2h 2m |
| SPHOR | SPH | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-04-22 07:48 UTC | 2026-04-22 08:37 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
