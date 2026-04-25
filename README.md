# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_15:41:30_UTC-green)

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

**Latest saved flight:** 2026-04-25 15:41:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 15:41:30 UTC

- **53,654** saved flights
- **21,310** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,654** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **643,171.2 tonnes** estimated CO2 emissions
- **37,285,286 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2261 |
| 2 | SkyWest Airlines | 2009 |
| 3 | IndiGo | 1224 |
| 4 | EJA | 949 |
| 5 | American Airlines | 858 |
| 6 | Southwest Airlines | 756 |
| 7 | ENY | 674 |
| 8 | Lufthansa | 634 |
| 9 | Vueling | 542 |
| 10 | AXM | 522 |
| 11 | LATAM Airlines | 520 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 455 |
| 14 | WIF | 447 |
| 15 | Delta Air Lines | 441 |
| 16 | QLK | 416 |
| 17 | Swiss International | 415 |
| 18 | LXJ | 393 |
| 19 | AEE | 360 |
| 20 | Alaska Airlines | 353 |
| 21 | easyJet | 344 |
| 22 | EJU | 340 |
| 23 | VIV | 340 |
| 24 | Japan Airlines | 313 |
| 25 | Air France | 309 |
| 26 | AXB | 285 |
| 27 | Cathay Pacific | 284 |
| 28 | AIQ | 277 |
| 29 | GLO | 273 |
| 30 | JetBlue | 273 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42599 |
| 2 | 🇪🇸 ES | 3896 |
| 3 | 🇮🇳 IN | 3853 |
| 4 | 🇦🇺 AU | 3622 |
| 5 | 🇧🇷 BR | 3117 |
| 6 | 🇮🇹 IT | 2896 |
| 7 | 🇯🇵 JP | 2889 |
| 8 | 🇩🇪 DE | 2878 |
| 9 | 🇨🇦 CA | 2660 |
| 10 | 🇨🇴 CO | 2457 |
| 11 | 🇬🇧 GB | 2253 |
| 12 | 🇫🇷 FR | 2097 |
| 13 | 🇲🇽 MX | 1653 |
| 14 | 🇬🇷 GR | 1613 |
| 15 | 🇨🇭 CH | 1526 |
| 16 | 🇳🇴 NO | 1450 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1017 |
| 20 | 🇹🇭 TH | 975 |
| 21 | 🇹🇷 TR | 964 |
| 22 | 🇵🇭 PH | 918 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 865 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 671 |
| 27 | 🇲🇪 ME | 578 |
| 28 | 🇳🇱 NL | 547 |
| 29 | 🇲🇴 MO | 529 |
| 30 | 🇧🇸 BS | 467 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1220 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 882 |
| 4 | El Dorado International Airport |  | CO | 833 |
| 5 | Indira Gandhi International Airport |  | IN | 819 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 797 |
| 7 | Guaymaral Airport |  | CO | 738 |
| 8 | Harry Reid International Airport |  | US | 687 |
| 9 | Zurich Airport |  | CH | 639 |
| 10 | La Aurora Airport |  | GT | 617 |
| 11 | Frankfurt am Main International Airport |  | DE | 617 |
| 12 | Macau International Airport |  | MO | 529 |
| 13 | Chicago O'Hare International Airport |  | US | 525 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 523 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 507 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 500 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 458 |
| 20 | Malpensa International Airport |  | IT | 454 |
| 21 | Congonhas Airport |  | BR | 451 |
| 22 | Charlotte/Douglas International Airport |  | US | 437 |
| 23 | Tenerife Norte Airport |  | ES | 426 |
| 24 | Ninoy Aquino International Airport |  | PH | 424 |
| 25 | Charles de Gaulle International Airport |  | FR | 406 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 399 |
| 27 | Salt Lake City International Airport |  | US | 399 |
| 28 | Daniel K Inouye International Airport |  | US | 388 |
| 29 | Capua Airport |  | IT | 387 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 385 |
| 31 | Vitoria/Foronda Airport |  | ES | 368 |
| 32 | Barcelona International Airport |  | ES | 362 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 357 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 357 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 357 |
| 36 | Reno/Tahoe International Airport |  | US | 356 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 317 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 299 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 163 | 21m | 244 km | 686.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 125 | 26m | 275 km | 592.3 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 83 | 52m | 556 km | 795.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 76 | 1h 41m | 1,156 km | 1,516.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 70 | 1h 19m | 961 km | 1,160.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 70 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 70 | 1h 53m | 1,304 km | 1,574.8 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 69 | 24m | 55 km | 65.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N24373 |  | Portland-Hillsboro Airport (KHIO) | Mc Minnville Municipal Airport (KMMV) | 2026-04-25 15:22 UTC | 2026-04-25 15:41 UTC | 18m |
| N331ED |  | Barrow County Airport (KWDR) | Cobb County International/Mccollum Field (KRYY) | 2026-04-25 15:16 UTC | 2026-04-25 15:37 UTC | 20m |
| N411MH |  | Frederick W Smith International Airport (KMEM) | Cleveland Municipal Airport (KRNV) | 2026-04-25 15:13 UTC | 2026-04-25 15:37 UTC | 23m |
| N532HF |  | Marion Airport (KC17) | Marion Airport (KC17) | 2026-04-25 15:06 UTC | 2026-04-25 15:34 UTC | 27m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 15:14 UTC | 2026-04-25 15:29 UTC | 15m |
| N929CH |  | Centennial Airport (KAPA) | Pueblo Memorial Airport (KPUB) | 2026-04-25 14:52 UTC | 2026-04-25 15:27 UTC | 35m |
| N562SD |  | Manchester Boston Regional Airport (KMHT) | Lebanon Municipal Airport (KLEB) | 2026-04-25 14:59 UTC | 2026-04-25 15:26 UTC | 26m |
| N252MX |  | Ryan Field (KRYN) | Ryan Field (KRYN) | 2026-04-25 15:08 UTC | 2026-04-25 15:19 UTC | 10m |
| N9026G |  | Deer Park Airport (KDEW) | Deer Park Airport (KDEW) | 2026-04-25 15:14 UTC | 2026-04-25 15:17 UTC | 3m |
| QTR8040 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-25 08:15 UTC | 2026-04-25 15:16 UTC | 7h 0m |
| N988LL |  | Miami Executive Airport (KTMB) | Summerland Key Cove Airport (FD51) | 2026-04-25 14:31 UTC | 2026-04-25 15:15 UTC | 44m |
| CAP4359 | CAP | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-25 15:01 UTC | 2026-04-25 15:13 UTC | 12m |
| N405SB |  | Laconia Municipal Airport (KLCI) | Lebanon Municipal Airport (KLEB) | 2026-04-25 14:39 UTC | 2026-04-25 15:12 UTC | 33m |
| SCA28 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-25 14:31 UTC | 2026-04-25 15:08 UTC | 37m |
| N517AF |  | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-04-25 14:45 UTC | 2026-04-25 15:06 UTC | 20m |
| N492DS |  | KU77 (KU77) | KU77 (KU77) | 2026-04-25 14:52 UTC | 2026-04-25 15:01 UTC | 9m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 14:46 UTC | 2026-04-25 15:01 UTC | 15m |
| N8068C |  | Crystal Airport (KMIC) | Crystal Airport (KMIC) | 2026-04-25 14:57 UTC | 2026-04-25 15:00 UTC | 3m |
| HBZVS | HBZ | Courchevel Airport (LFLJ) | Raron Airport (LSTA) | 2026-04-25 14:40 UTC | 2026-04-25 14:59 UTC | 19m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-25 14:41 UTC | 2026-04-25 14:59 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
