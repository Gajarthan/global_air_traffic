# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_20:25:26_UTC-green)

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

**Latest saved flight:** 2026-04-28 20:25:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-28 20:25:26 UTC

- **58,472** saved flights
- **22,760** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,472** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **710,312.6 tonnes** estimated CO2 emissions
- **41,177,542 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2487 |
| 2 | SkyWest Airlines | 2197 |
| 3 | IndiGo | 1337 |
| 4 | EJA | 1035 |
| 5 | American Airlines | 920 |
| 6 | Southwest Airlines | 836 |
| 7 | Lufthansa | 742 |
| 8 | ENY | 730 |
| 9 | Vueling | 582 |
| 10 | AXM | 570 |
| 11 | LATAM Airlines | 555 |
| 12 | All Nippon Airways | 517 |
| 13 | WIF | 489 |
| 14 | AZU | 484 |
| 15 | Delta Air Lines | 480 |
| 16 | Swiss International | 464 |
| 17 | QLK | 456 |
| 18 | LXJ | 415 |
| 19 | Alaska Airlines | 398 |
| 20 | AEE | 388 |
| 21 | easyJet | 384 |
| 22 | EJU | 379 |
| 23 | VIV | 371 |
| 24 | Air France | 342 |
| 25 | Cathay Pacific | 338 |
| 26 | Japan Airlines | 338 |
| 27 | AXB | 319 |
| 28 | AIQ | 295 |
| 29 | United Airlines | 295 |
| 30 | JetBlue | 294 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46268 |
| 2 | 🇪🇸 ES | 4258 |
| 3 | 🇮🇳 IN | 4206 |
| 4 | 🇦🇺 AU | 3959 |
| 5 | 🇧🇷 BR | 3316 |
| 6 | 🇩🇪 DE | 3230 |
| 7 | 🇮🇹 IT | 3201 |
| 8 | 🇯🇵 JP | 3157 |
| 9 | 🇨🇦 CA | 2896 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2480 |
| 12 | 🇫🇷 FR | 2316 |
| 13 | 🇲🇽 MX | 1845 |
| 14 | 🇬🇷 GR | 1741 |
| 15 | 🇨🇭 CH | 1642 |
| 16 | 🇳🇴 NO | 1591 |
| 17 | 🇲🇾 MY | 1382 |
| 18 | 🇿🇦 ZA | 1192 |
| 19 | 🇳🇿 NZ | 1094 |
| 20 | 🇹🇷 TR | 1061 |
| 21 | 🇹🇭 TH | 1057 |
| 22 | 🇵🇭 PH | 984 |
| 23 | 🇵🇱 PL | 943 |
| 24 | 🇰🇷 KR | 926 |
| 25 | 🇬🇹 GT | 858 |
| 26 | 🇲🇦 MA | 740 |
| 27 | 🇲🇪 ME | 635 |
| 28 | 🇲🇴 MO | 628 |
| 29 | 🇳🇱 NL | 611 |
| 30 | 🇮🇩 ID | 502 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1318 |
| 2 | Tokyo International Airport |  | JP | 1073 |
| 3 | Denver International Airport |  | US | 976 |
| 4 | Indira Gandhi International Airport |  | IN | 885 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 857 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 742 |
| 9 | Frankfurt am Main International Airport |  | DE | 732 |
| 10 | Zurich Airport |  | CH | 706 |
| 11 | La Aurora Airport |  | GT | 648 |
| 12 | Macau International Airport |  | MO | 628 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 580 |
| 14 | Chicago O'Hare International Airport |  | US | 558 |
| 15 | Madrid Barajas International Airport |  | ES | 545 |
| 16 | Kuala Lumpur International Airport |  | MY | 545 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 539 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 513 |
| 19 | Malpensa International Airport |  | IT | 506 |
| 20 | Bengaluru International Airport |  | IN | 504 |
| 21 | Congonhas Airport |  | BR | 478 |
| 22 | Charlotte/Douglas International Airport |  | US | 464 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 453 |
| 25 | Charles de Gaulle International Airport |  | FR | 452 |
| 26 | Salt Lake City International Airport |  | US | 451 |
| 27 | Capua Airport |  | IT | 444 |
| 28 | Daniel K Inouye International Airport |  | US | 431 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 427 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 419 |
| 31 | Barcelona International Airport |  | ES | 396 |
| 32 | Vitoria/Foronda Airport |  | ES | 395 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 389 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 386 |
| 35 | O. R. Tambo International Airport |  | ZA | 380 |
| 36 | Reno/Tahoe International Airport |  | US | 375 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 371 |
| 38 | Don Mueang International Airport |  | TH | 359 |
| 39 | Amsterdam Airport Schiphol |  | NL | 354 |
| 40 | Calgary International Airport |  | CA | 346 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 189 | 21m | 244 km | 795.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 183 | 24m | 225 km | 710.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 171 | 1h 27m | 910 km | 2,683.4 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 164 | 28m | 304 km | 859.7 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 120 | 1h 12m | 770 km | 1,594.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 110 | 44m | 452 km | 857.3 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 100 | 20m | 99 km | 171.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 94 | 20m | 250 km | 406.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 80 | 1h 53m | 1,304 km | 1,799.8 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4769L |  | Bloomsburg Municipal Airport (KN13) | Bloomsburg Municipal Airport (KN13) | 2026-04-28 19:59 UTC | 2026-04-28 20:25 UTC | 25m |
| N510KF |  | Joe Foss Field (KFSD) | Mitchell Municipal Airport (KMHE) | 2026-04-28 19:34 UTC | 2026-04-28 20:19 UTC | 44m |
| N265PS |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-28 19:14 UTC | 2026-04-28 20:17 UTC | 1h 3m |
| GIZMO11 | GIZ | 6OK6 (6OK6) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-04-28 19:50 UTC | 2026-04-28 20:13 UTC | 22m |
| N1424V |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-04-28 20:10 UTC | 2026-04-28 20:12 UTC | 1m |
| SEH7RT | SEH | Diagoras Airport (LGRP) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-28 19:22 UTC | 2026-04-28 20:08 UTC | 46m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-04-28 19:39 UTC | 2026-04-28 20:07 UTC | 28m |
| TAUNT11 | TAU | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Nelson High Point Airport (8OK7) | 2026-04-28 19:28 UTC | 2026-04-28 20:00 UTC | 32m |
| N183TS |  | Keesler Afb Airport (KBIX) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-28 18:59 UTC | 2026-04-28 19:59 UTC | 59m |
| N4333J |  | Willow Run Airport (KYIP) | Willow Run Airport (KYIP) | 2026-04-28 19:54 UTC | 2026-04-28 19:59 UTC | 5m |
| BOE339 | BOE | Renton Municipal Airport (KRNT) | Warden Airport (K2S4) | 2026-04-28 17:58 UTC | 2026-04-28 19:59 UTC | 2h 0m |
| GPD202 | GPD | Deck Airport (K9D4) | Teterboro Airport (KTEB) | 2026-04-28 19:27 UTC | 2026-04-28 19:59 UTC | 31m |
| N931T |  | KNKL (KNKL) | Mobile International Airport (KBFM) | 2026-04-28 19:38 UTC | 2026-04-28 19:57 UTC | 18m |
| LXJ339 | LXJ | Hilton Head Airport (KHXD) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-28 19:08 UTC | 2026-04-28 19:56 UTC | 48m |
| XAAVS | XAA | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-04-28 19:45 UTC | 2026-04-28 19:54 UTC | 8m |
| TGDLV | TGD | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-28 19:47 UTC | 2026-04-28 19:54 UTC | 6m |
| FAF6515 | FAF | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | Limoges Airport (LFBL) | 2026-04-28 19:38 UTC | 2026-04-28 19:52 UTC | 14m |
| CGPCW | CGP | Vancouver International Airport (CYVR) | Princeton Airport (CYDC) | 2026-04-28 19:14 UTC | 2026-04-28 19:52 UTC | 38m |
| N821FR |  | Santa Monica Municipal Airport (KSMO) | Santa Monica Municipal Airport (KSMO) | 2026-04-28 19:04 UTC | 2026-04-28 19:52 UTC | 47m |
| FOXX377 | FOX | Colle Field (34MS) | Bear Pen Airport (NC43) | 2026-04-28 17:42 UTC | 2026-04-28 19:52 UTC | 2h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
