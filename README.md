# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_19:34:38_UTC-green)

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

**Latest saved flight:** 2026-04-27 19:34:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 19:34:38 UTC

- **57,271** saved flights
- **22,407** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,271** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **695,333.2 tonnes** estimated CO2 emissions
- **40,309,171 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2437 |
| 2 | SkyWest Airlines | 2168 |
| 3 | IndiGo | 1298 |
| 4 | EJA | 1026 |
| 5 | American Airlines | 908 |
| 6 | Southwest Airlines | 821 |
| 7 | ENY | 722 |
| 8 | Lufthansa | 710 |
| 9 | Vueling | 574 |
| 10 | AXM | 553 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 501 |
| 13 | AZU | 480 |
| 14 | WIF | 478 |
| 15 | Delta Air Lines | 471 |
| 16 | Swiss International | 450 |
| 17 | QLK | 439 |
| 18 | LXJ | 411 |
| 19 | Alaska Airlines | 388 |
| 20 | AEE | 379 |
| 21 | easyJet | 377 |
| 22 | EJU | 370 |
| 23 | VIV | 366 |
| 24 | Air France | 334 |
| 25 | Cathay Pacific | 328 |
| 26 | Japan Airlines | 327 |
| 27 | AXB | 312 |
| 28 | JetBlue | 292 |
| 29 | United Airlines | 288 |
| 30 | GLO | 287 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45468 |
| 2 | 🇪🇸 ES | 4182 |
| 3 | 🇮🇳 IN | 4092 |
| 4 | 🇦🇺 AU | 3813 |
| 5 | 🇧🇷 BR | 3288 |
| 6 | 🇮🇹 IT | 3139 |
| 7 | 🇩🇪 DE | 3137 |
| 8 | 🇯🇵 JP | 3048 |
| 9 | 🇨🇦 CA | 2831 |
| 10 | 🇨🇴 CO | 2593 |
| 11 | 🇬🇧 GB | 2434 |
| 12 | 🇫🇷 FR | 2253 |
| 13 | 🇲🇽 MX | 1815 |
| 14 | 🇬🇷 GR | 1705 |
| 15 | 🇨🇭 CH | 1605 |
| 16 | 🇳🇴 NO | 1550 |
| 17 | 🇲🇾 MY | 1343 |
| 18 | 🇿🇦 ZA | 1165 |
| 19 | 🇳🇿 NZ | 1072 |
| 20 | 🇹🇷 TR | 1048 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 964 |
| 23 | 🇵🇱 PL | 925 |
| 24 | 🇰🇷 KR | 904 |
| 25 | 🇬🇹 GT | 847 |
| 26 | 🇲🇦 MA | 724 |
| 27 | 🇲🇪 ME | 623 |
| 28 | 🇲🇴 MO | 607 |
| 29 | 🇳🇱 NL | 597 |
| 30 | 🇧🇸 BS | 488 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1297 |
| 2 | Tokyo International Airport |  | JP | 1034 |
| 3 | Denver International Airport |  | US | 952 |
| 4 | El Dorado International Airport |  | CO | 873 |
| 5 | Indira Gandhi International Airport |  | IN | 868 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 840 |
| 7 | Guaymaral Airport |  | CO | 798 |
| 8 | Harry Reid International Airport |  | US | 727 |
| 9 | Frankfurt am Main International Airport |  | DE | 699 |
| 10 | Zurich Airport |  | CH | 686 |
| 11 | La Aurora Airport |  | GT | 638 |
| 12 | Macau International Airport |  | MO | 607 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 571 |
| 14 | Chicago O'Hare International Airport |  | US | 553 |
| 15 | Madrid Barajas International Airport |  | ES | 536 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 532 |
| 17 | Kuala Lumpur International Airport |  | MY | 529 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 502 |
| 19 | Malpensa International Airport |  | IT | 497 |
| 20 | Bengaluru International Airport |  | IN | 490 |
| 21 | Congonhas Airport |  | BR | 472 |
| 22 | Charlotte/Douglas International Airport |  | US | 462 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Salt Lake City International Airport |  | US | 444 |
| 25 | Ninoy Aquino International Airport |  | PH | 443 |
| 26 | Charles de Gaulle International Airport |  | FR | 441 |
| 27 | Capua Airport |  | IT | 437 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 423 |
| 29 | Daniel K Inouye International Airport |  | US | 423 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 409 |
| 31 | Barcelona International Airport |  | ES | 391 |
| 32 | Vitoria/Foronda Airport |  | ES | 389 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 386 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 379 |
| 35 | Reno/Tahoe International Airport |  | US | 372 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 37 | O. R. Tambo International Airport |  | ZA | 367 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 341 |
| 40 | Calgary International Airport |  | CA | 339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 326 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 252 | 1h 7m | 706 km | 3,068.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 209 | 14m | 114 km | 409.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 185 | 21m | 244 km | 779.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 181 | 24m | 225 km | 702.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 163 | 1h 27m | 910 km | 2,557.8 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 160 | 28m | 304 km | 838.8 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 142 | 19m | 165 km | 403.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 138 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 131 | 26m | 275 km | 620.8 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 111 | 1h 12m | 770 km | 1,474.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 109 | 44m | 452 km | 849.5 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 99 | 20m | 99 km | 169.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 96 | 31m | 369 km | 611.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 86 | 52m | 556 km | 824.4 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 78 | 13m | 99 km | 133.7 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 73 | 1h 42m | 1,423 km | 1,791.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 73 | 1h 19m | 961 km | 1,210.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-04-27 18:37 UTC | 2026-04-27 19:34 UTC | 57m |
| N2373M |  | Trenton Mercer Airport (KTTN) | Chester County G O Carlson Airport (KMQS) | 2026-04-27 18:28 UTC | 2026-04-27 19:29 UTC | 1h 0m |
| PRWSG | PRW | Eurico de Aguiar Salles Airport (SBVT) | Guarapari Airport (SNGA) | 2026-04-27 18:55 UTC | 2026-04-27 19:27 UTC | 32m |
| N904RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-04-27 17:38 UTC | 2026-04-27 19:25 UTC | 1h 47m |
| QTR340 | Qatar Airways | Sheremetyevo International Airport (UUEE) | Queen Alia International Airport (OJAI) | 2026-04-27 15:29 UTC | 2026-04-27 19:25 UTC | 3h 55m |
| ROCK81 | ROC | 2TX3 (2TX3) | Chaparrosa Ranch Airport (72TE) | 2026-04-27 19:01 UTC | 2026-04-27 19:23 UTC | 21m |
| DADDY11 | DAD | RAF Mildenhall (EGUN) | RAF Mildenhall (EGUN) | 2026-04-27 18:09 UTC | 2026-04-27 19:20 UTC | 1h 11m |
| N17598 |  | Seattle Paine Field International Airport (KPAE) | Boeing Field/King County International Airport (KBFI) | 2026-04-27 18:07 UTC | 2026-04-27 19:17 UTC | 1h 10m |
| LXJ421 | LXJ | John Wayne/Orange County Airport (KSNA) | Harry Reid International Airport (KLAS) | 2026-04-27 18:35 UTC | 2026-04-27 19:17 UTC | 41m |
| RNGR843 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-04-27 18:45 UTC | 2026-04-27 19:16 UTC | 31m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-27 19:05 UTC | 2026-04-27 19:15 UTC | 10m |
| C6056 |  | San Diego International Airport (KSAN) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-27 19:10 UTC | 2026-04-27 19:14 UTC | 3m |
| N200EK |  | Flying Cloud Airport (KFCM) | Joe Foss Field (KFSD) | 2026-04-27 18:20 UTC | 2026-04-27 19:13 UTC | 53m |
| N6346A |  | Airy-Acres Airport (6NY3) | Airy-Acres Airport (6NY3) | 2026-04-27 18:52 UTC | 2026-04-27 19:13 UTC | 21m |
| CXK517 | CXK | Lawrence Municipal Airport (KLWM) | Lawrence Municipal Airport (KLWM) | 2026-04-27 17:47 UTC | 2026-04-27 19:12 UTC | 1h 25m |
| CXK171 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-04-27 18:47 UTC | 2026-04-27 19:03 UTC | 16m |
| N8318Q |  | Quakertown Airport (KUKT) | Lancaster Airport (KLNS) | 2026-04-27 18:26 UTC | 2026-04-27 19:01 UTC | 34m |
| N84UC |  | Cincinnati Municipal/Lunken Field (KLUK) | My Place Airport (3OH7) | 2026-04-27 18:47 UTC | 2026-04-27 18:59 UTC | 12m |
| EJA983 | EJA | Reading Regional/Carl A Spaatz Field (KRDG) | Rocky Mountain Metro Airport (KBJC) | 2026-04-27 15:00 UTC | 2026-04-27 18:59 UTC | 3h 58m |
| XBPZE | XBP | Plan De Guadalupe International Airport (MMIO) | Rnk Ranch Airport (8TS8) | 2026-04-27 18:06 UTC | 2026-04-27 18:57 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
