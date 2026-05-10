# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_14:31:30_UTC-green)

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

**Latest saved flight:** 2026-05-10 14:31:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 14:31:30 UTC

- **77,039** saved flights
- **28,171** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **77,039** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **954,943.0 tonnes** estimated CO2 emissions
- **55,359,014 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3304 |
| 2 | SkyWest Airlines | 2853 |
| 3 | IndiGo | 1720 |
| 4 | EJA | 1412 |
| 5 | American Airlines | 1203 |
| 6 | Southwest Airlines | 1125 |
| 7 | Lufthansa | 1009 |
| 8 | ENY | 962 |
| 9 | Delta Air Lines | 802 |
| 10 | Vueling | 740 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 661 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 613 |
| 16 | QLK | 591 |
| 17 | Swiss International | 585 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 541 |
| 20 | easyJet | 516 |
| 21 | Cathay Pacific | 498 |
| 22 | AEE | 497 |
| 23 | EJU | 497 |
| 24 | VIV | 460 |
| 25 | Air France | 453 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 428 |
| 28 | CXK | 394 |
| 29 | AIQ | 386 |
| 30 | MXY | 378 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 62031 |
| 2 | 🇪🇸 ES | 5519 |
| 3 | 🇮🇳 IN | 5396 |
| 4 | 🇦🇺 AU | 5028 |
| 5 | 🇩🇪 DE | 4360 |
| 6 | 🇧🇷 BR | 4289 |
| 7 | 🇮🇹 IT | 4244 |
| 8 | 🇯🇵 JP | 4017 |
| 9 | 🇨🇦 CA | 3821 |
| 10 | 🇬🇧 GB | 3320 |
| 11 | 🇫🇷 FR | 3060 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2361 |
| 14 | 🇬🇷 GR | 2280 |
| 15 | 🇳🇴 NO | 2115 |
| 16 | 🇨🇭 CH | 2084 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1478 |
| 19 | 🇳🇿 NZ | 1391 |
| 20 | 🇹🇷 TR | 1386 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1285 |
| 23 | 🇵🇭 PH | 1242 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1199 |
| 26 | 🇲🇴 MO | 911 |
| 27 | 🇲🇦 MA | 910 |
| 28 | 🇲🇪 ME | 823 |
| 29 | 🇳🇱 NL | 805 |
| 30 | 🇭🇷 HR | 669 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1708 |
| 2 | Tokyo International Airport |  | JP | 1348 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1140 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1118 |
| 6 | Frankfurt am Main International Airport |  | DE | 1008 |
| 7 | Harry Reid International Airport |  | US | 955 |
| 8 | Macau International Airport |  | MO | 911 |
| 9 | Zurich Airport |  | CH | 911 |
| 10 | La Aurora Airport |  | GT | 900 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 770 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 15 | Chicago O'Hare International Airport |  | US | 753 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 716 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 671 |
| 20 | Malpensa International Airport |  | IT | 668 |
| 21 | Bengaluru International Airport |  | IN | 668 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Capua Airport |  | IT | 608 |
| 24 | Charlotte/Douglas International Airport |  | US | 607 |
| 25 | Congonhas Airport |  | BR | 606 |
| 26 | Charles de Gaulle International Airport |  | FR | 605 |
| 27 | Tenerife Norte Airport |  | ES | 572 |
| 28 | Ninoy Aquino International Airport |  | PH | 565 |
| 29 | Daniel K Inouye International Airport |  | US | 560 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 555 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 524 |
| 32 | Barcelona International Airport |  | ES | 522 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 518 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 504 |
| 35 | Don Mueang International Airport |  | TH | 490 |
| 36 | Vitoria/Foronda Airport |  | ES | 488 |
| 37 | Amsterdam Airport Schiphol |  | NL | 485 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 39 | O. R. Tambo International Airport |  | ZA | 464 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 275 | 21m | 244 km | 1,157.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 184 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 165 | 26m | 275 km | 781.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 117 | 27m | 215 km | 433.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 96 | 1h 2m | - | - |
| 29 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 96 | 18m | 144 km | 238.8 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DMWUE | DMW | Wurzburg-Schenkenturm Airport (EDFW) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-05-10 13:17 UTC | 2026-05-10 14:31 UTC | 1h 13m |
| CGFDE | CGF | Montréal / St-Hubert Airport (CYHU) | Drummondville Airport (CSC3) | 2026-05-10 14:01 UTC | 2026-05-10 14:30 UTC | 29m |
| VAR403 | VAR | Bishop Airfield (1AZ0) | Bishop Airfield (1AZ0) | 2026-05-10 14:16 UTC | 2026-05-10 14:28 UTC | 11m |
| VAR856 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-05-10 13:54 UTC | 2026-05-10 14:26 UTC | 31m |
| CXK535 | CXK | Concord-Padgett Regional Airport (KJQF) | Concord-Padgett Regional Airport (KJQF) | 2026-05-10 14:06 UTC | 2026-05-10 14:25 UTC | 19m |
| ELY348 | ELY | Zurich Airport (LSZH) | Herzliya Airport (LLHZ) | 2026-05-10 10:58 UTC | 2026-05-10 14:24 UTC | 3h 26m |
| SCX8778 | SCX | St Louis Downtown Airport (KCPS) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 13:14 UTC | 2026-05-10 14:24 UTC | 1h 9m |
| N422US |  | La Belle Municipal Airport (KX14) | La Belle Municipal Airport (KX14) | 2026-05-10 13:59 UTC | 2026-05-10 14:15 UTC | 15m |
| N316ML |  | Donegal Springs Airpark (KN71) | Donegal Springs Airpark (KN71) | 2026-05-10 13:48 UTC | 2026-05-10 14:13 UTC | 25m |
| CXK397 | CXK | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-05-10 13:52 UTC | 2026-05-10 14:13 UTC | 20m |
| N19650 |  | Dupage Airport (KDPA) | Bolingbrook's Clow International Airport (K1C5) | 2026-05-10 13:26 UTC | 2026-05-10 14:09 UTC | 42m |
| N702SS |  | Van Nuys Airport (KVNY) | Scottsdale Airport (KSDL) | 2026-05-10 13:05 UTC | 2026-05-10 14:05 UTC | 1h 0m |
| VAR403 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-05-10 13:45 UTC | 2026-05-10 14:04 UTC | 19m |
| 7TVIW |  | Mostaganem Airport (DA14) | Mostaganem Airport (DA14) | 2026-05-10 13:44 UTC | 2026-05-10 14:04 UTC | 19m |
| N92WG |  | Addison Airport (KADS) | Silverton Municipal Airport (79XS) | 2026-05-10 13:10 UTC | 2026-05-10 13:59 UTC | 48m |
| KLM636 | KLM Royal Dutch | Harry Reid International Airport (KLAS) | Amsterdam Airport Schiphol (EHAM) | 2026-05-10 04:25 UTC | 2026-05-10 13:57 UTC | 9h 31m |
| EWG2WJ | EWG | Hamburg Airport (EDDH) | Stuttgart Airport (EDDS) | 2026-05-10 12:55 UTC | 2026-05-10 13:56 UTC | 1h 1m |
| OMM090 | OMM | LZRY (LZRY) | LZRY (LZRY) | 2026-05-10 13:33 UTC | 2026-05-10 13:56 UTC | 23m |
| SWA2126 | Southwest Airlines | Chicago Midway International Airport (KMDW) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 12:50 UTC | 2026-05-10 13:54 UTC | 1h 4m |
| EZY24RT | easyJet | Belfast International Airport (EGAA) | Amsterdam Airport Schiphol (EHAM) | 2026-05-10 12:43 UTC | 2026-05-10 13:52 UTC | 1h 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
