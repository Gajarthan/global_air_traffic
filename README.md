# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_22:14:44_UTC-green)

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

**Latest saved flight:** 2026-04-27 22:14:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-27 22:14:44 UTC

- **57,423** saved flights
- **22,461** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **57,423** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **696,777.3 tonnes** estimated CO2 emissions
- **40,392,889 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2442 |
| 2 | SkyWest Airlines | 2180 |
| 3 | IndiGo | 1298 |
| 4 | EJA | 1028 |
| 5 | American Airlines | 911 |
| 6 | Southwest Airlines | 822 |
| 7 | ENY | 725 |
| 8 | Lufthansa | 710 |
| 9 | Vueling | 574 |
| 10 | AXM | 553 |
| 11 | LATAM Airlines | 551 |
| 12 | All Nippon Airways | 501 |
| 13 | AZU | 481 |
| 14 | WIF | 478 |
| 15 | Delta Air Lines | 473 |
| 16 | Swiss International | 450 |
| 17 | QLK | 441 |
| 18 | LXJ | 412 |
| 19 | Alaska Airlines | 390 |
| 20 | AEE | 379 |
| 21 | easyJet | 377 |
| 22 | EJU | 370 |
| 23 | VIV | 368 |
| 24 | Air France | 334 |
| 25 | Cathay Pacific | 328 |
| 26 | Japan Airlines | 327 |
| 27 | AXB | 312 |
| 28 | JetBlue | 293 |
| 29 | United Airlines | 289 |
| 30 | GLO | 288 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 45679 |
| 2 | 🇪🇸 ES | 4185 |
| 3 | 🇮🇳 IN | 4093 |
| 4 | 🇦🇺 AU | 3825 |
| 5 | 🇧🇷 BR | 3292 |
| 6 | 🇮🇹 IT | 3140 |
| 7 | 🇩🇪 DE | 3139 |
| 8 | 🇯🇵 JP | 3048 |
| 9 | 🇨🇦 CA | 2843 |
| 10 | 🇨🇴 CO | 2601 |
| 11 | 🇬🇧 GB | 2438 |
| 12 | 🇫🇷 FR | 2255 |
| 13 | 🇲🇽 MX | 1823 |
| 14 | 🇬🇷 GR | 1705 |
| 15 | 🇨🇭 CH | 1605 |
| 16 | 🇳🇴 NO | 1550 |
| 17 | 🇲🇾 MY | 1344 |
| 18 | 🇿🇦 ZA | 1165 |
| 19 | 🇳🇿 NZ | 1078 |
| 20 | 🇹🇷 TR | 1048 |
| 21 | 🇹🇭 TH | 1017 |
| 22 | 🇵🇭 PH | 966 |
| 23 | 🇵🇱 PL | 925 |
| 24 | 🇰🇷 KR | 904 |
| 25 | 🇬🇹 GT | 847 |
| 26 | 🇲🇦 MA | 726 |
| 27 | 🇲🇪 ME | 623 |
| 28 | 🇲🇴 MO | 607 |
| 29 | 🇳🇱 NL | 597 |
| 30 | 🇧🇸 BS | 489 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1303 |
| 2 | Tokyo International Airport |  | JP | 1034 |
| 3 | Denver International Airport |  | US | 961 |
| 4 | El Dorado International Airport |  | CO | 876 |
| 5 | Indira Gandhi International Airport |  | IN | 868 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 840 |
| 7 | Guaymaral Airport |  | CO | 800 |
| 8 | Harry Reid International Airport |  | US | 733 |
| 9 | Frankfurt am Main International Airport |  | DE | 699 |
| 10 | Zurich Airport |  | CH | 686 |
| 11 | La Aurora Airport |  | GT | 638 |
| 12 | Macau International Airport |  | MO | 607 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 572 |
| 14 | Chicago O'Hare International Airport |  | US | 554 |
| 15 | Madrid Barajas International Airport |  | ES | 536 |
| 16 | Hartsfield/Jackson Atlanta International Airport |  | US | 534 |
| 17 | Kuala Lumpur International Airport |  | MY | 530 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 502 |
| 19 | Malpensa International Airport |  | IT | 497 |
| 20 | Bengaluru International Airport |  | IN | 490 |
| 21 | Congonhas Airport |  | BR | 473 |
| 22 | Charlotte/Douglas International Airport |  | US | 462 |
| 23 | Tenerife Norte Airport |  | ES | 458 |
| 24 | Salt Lake City International Airport |  | US | 446 |
| 25 | Ninoy Aquino International Airport |  | PH | 444 |
| 26 | Charles de Gaulle International Airport |  | FR | 441 |
| 27 | Capua Airport |  | IT | 437 |
| 28 | Atizapan De Zaragoza Airport |  | MX | 424 |
| 29 | Daniel K Inouye International Airport |  | US | 424 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 409 |
| 31 | Barcelona International Airport |  | ES | 392 |
| 32 | Vitoria/Foronda Airport |  | ES | 389 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 388 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 379 |
| 35 | Reno/Tahoe International Airport |  | US | 374 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 369 |
| 37 | O. R. Tambo International Airport |  | ZA | 367 |
| 38 | Don Mueang International Airport |  | TH | 347 |
| 39 | Amsterdam Airport Schiphol |  | NL | 341 |
| 40 | Calgary International Airport |  | CA | 339 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 327 | 26m | - | - |
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
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 97 | 31m | 369 km | 617.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 94 | 27m | 215 km | 348.1 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 90 | 20m | 250 km | 388.7 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 87 | 52m | 556 km | 834.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 86 | 20m | 147 km | 217.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 80 | 1h 43m | 1,156 km | 1,596.0 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 79 | 1h 53m | 1,304 km | 1,777.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 77 | 23m | 55 km | 73.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 76 | 58m | 493 km | 646.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 75 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 74 | 1h 19m | 961 km | 1,226.6 t |
| 30 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 73 | 1h 42m | 1,423 km | 1,791.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N48KL |  | Greenville Spartanburg International Airport (KGSP) | Crooked Fence Farm Airport (3SC4) | 2026-04-27 22:04 UTC | 2026-04-27 22:14 UTC | 10m |
| N424W |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-04-27 21:48 UTC | 2026-04-27 22:09 UTC | 21m |
| N787MM |  | Los Angeles International Airport (KLAX) | Harry Reid International Airport (KLAS) | 2026-04-27 21:17 UTC | 2026-04-27 22:09 UTC | 52m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-27 20:32 UTC | 2026-04-27 22:08 UTC | 1h 35m |
| BALL11 | BAL | Enid Woodring Regional Airport (KWDG) | William R Pogue Municipal Airport (KOWP) | 2026-04-27 21:45 UTC | 2026-04-27 22:07 UTC | 21m |
| N248JS |  | Centennial Airport (KAPA) | Northern Colorado Regional Airport (KFNL) | 2026-04-27 21:24 UTC | 2026-04-27 22:06 UTC | 41m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-27 21:45 UTC | 2026-04-27 22:06 UTC | 20m |
| ZKETT | ZKE | North Shore Aerodrome (NZNE) | North Shore Aerodrome (NZNE) | 2026-04-27 22:04 UTC | 2026-04-27 22:05 UTC | 0m |
| N2378T |  | Flying Bk Ranch Airport (AL32) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-04-27 21:31 UTC | 2026-04-27 22:04 UTC | 33m |
| ZKNYF | ZKN | Stratford Airport (NZSD) | New Plymouth Airport (NZNP) | 2026-04-27 21:42 UTC | 2026-04-27 22:01 UTC | 18m |
| AAL2256 | American Airlines | Los Angeles International Airport (KLAX) | Harry Reid International Airport (KLAS) | 2026-04-27 21:11 UTC | 2026-04-27 21:57 UTC | 46m |
| N480LP |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-04-27 20:44 UTC | 2026-04-27 21:56 UTC | 1h 12m |
| RJA017 | Royal Jordanian | Hamburg-Finkenwerder Airport (EDHI) | Queen Alia International Airport (OJAI) | 2026-04-27 17:48 UTC | 2026-04-27 21:56 UTC | 4h 8m |
| N34SJ |  | Crossville Memorial-Whitson Field (KCSV) | Chiriaco Summit Airport (KL77) | 2026-04-27 16:08 UTC | 2026-04-27 21:54 UTC | 5h 45m |
| BOMR732 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Waldron Field Nolf Airport (KNWL) | 2026-04-27 21:35 UTC | 2026-04-27 21:52 UTC | 17m |
| FFL1395 | FFL | Manassas Regional/Harry P Davis Field (KHEF) | Coastal Carolina Regional Airport (KEWN) | 2026-04-27 20:49 UTC | 2026-04-27 21:49 UTC | 59m |
| N8502V |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-27 20:35 UTC | 2026-04-27 21:48 UTC | 1h 12m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-04-27 20:45 UTC | 2026-04-27 21:48 UTC | 1h 2m |
| N2885D |  | Lehigh Valley International Airport (KABE) | Sky Manor Airport (KN40) | 2026-04-27 21:19 UTC | 2026-04-27 21:45 UTC | 26m |
| N280FG |  | Trenton Mercer Airport (KTTN) | Chester County G O Carlson Airport (KMQS) | 2026-04-27 20:57 UTC | 2026-04-27 21:44 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
