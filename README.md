# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_10:48:40_UTC-green)

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

**Latest saved flight:** 2026-05-10 10:48:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 10:48:40 UTC

- **76,884** saved flights
- **28,120** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,884** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **953,210.6 tonnes** estimated CO2 emissions
- **55,258,586 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3299 |
| 2 | SkyWest Airlines | 2847 |
| 3 | IndiGo | 1715 |
| 4 | EJA | 1410 |
| 5 | American Airlines | 1201 |
| 6 | Southwest Airlines | 1118 |
| 7 | Lufthansa | 1004 |
| 8 | ENY | 961 |
| 9 | Delta Air Lines | 797 |
| 10 | Vueling | 739 |
| 11 | AXM | 720 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 657 |
| 14 | All Nippon Airways | 625 |
| 15 | AZU | 611 |
| 16 | QLK | 591 |
| 17 | Swiss International | 584 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 541 |
| 20 | easyJet | 512 |
| 21 | Cathay Pacific | 498 |
| 22 | AEE | 497 |
| 23 | EJU | 495 |
| 24 | VIV | 458 |
| 25 | Air France | 451 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 427 |
| 28 | CXK | 391 |
| 29 | AIQ | 386 |
| 30 | MXY | 376 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61913 |
| 2 | 🇪🇸 ES | 5506 |
| 3 | 🇮🇳 IN | 5383 |
| 4 | 🇦🇺 AU | 5028 |
| 5 | 🇩🇪 DE | 4341 |
| 6 | 🇧🇷 BR | 4281 |
| 7 | 🇮🇹 IT | 4236 |
| 8 | 🇯🇵 JP | 4017 |
| 9 | 🇨🇦 CA | 3815 |
| 10 | 🇬🇧 GB | 3313 |
| 11 | 🇫🇷 FR | 3050 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2357 |
| 14 | 🇬🇷 GR | 2277 |
| 15 | 🇳🇴 NO | 2108 |
| 16 | 🇨🇭 CH | 2079 |
| 17 | 🇲🇾 MY | 1800 |
| 18 | 🇿🇦 ZA | 1476 |
| 19 | 🇳🇿 NZ | 1391 |
| 20 | 🇹🇷 TR | 1385 |
| 21 | 🇹🇭 TH | 1379 |
| 22 | 🇵🇱 PL | 1283 |
| 23 | 🇵🇭 PH | 1240 |
| 24 | 🇰🇷 KR | 1214 |
| 25 | 🇬🇹 GT | 1199 |
| 26 | 🇲🇴 MO | 911 |
| 27 | 🇲🇦 MA | 908 |
| 28 | 🇲🇪 ME | 822 |
| 29 | 🇳🇱 NL | 803 |
| 30 | 🇭🇷 HR | 668 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1707 |
| 2 | Tokyo International Airport |  | JP | 1348 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1136 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1117 |
| 6 | Frankfurt am Main International Airport |  | DE | 1004 |
| 7 | Harry Reid International Airport |  | US | 953 |
| 8 | Macau International Airport |  | MO | 911 |
| 9 | Zurich Airport |  | CH | 907 |
| 10 | La Aurora Airport |  | GT | 900 |
| 11 | Guaymaral Airport |  | CO | 890 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 14 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 756 |
| 15 | Chicago O'Hare International Airport |  | US | 751 |
| 16 | Kuala Lumpur International Airport |  | MY | 722 |
| 17 | Madrid Barajas International Airport |  | ES | 716 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 671 |
| 20 | Malpensa International Airport |  | IT | 667 |
| 21 | Bengaluru International Airport |  | IN | 666 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Charlotte/Douglas International Airport |  | US | 604 |
| 24 | Capua Airport |  | IT | 604 |
| 25 | Congonhas Airport |  | BR | 604 |
| 26 | Charles de Gaulle International Airport |  | FR | 602 |
| 27 | Tenerife Norte Airport |  | ES | 572 |
| 28 | Ninoy Aquino International Airport |  | PH | 564 |
| 29 | Daniel K Inouye International Airport |  | US | 560 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 554 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 521 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 517 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 504 |
| 35 | Don Mueang International Airport |  | TH | 490 |
| 36 | Vitoria/Foronda Airport |  | ES | 486 |
| 37 | Amsterdam Airport Schiphol |  | NL | 483 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 39 | O. R. Tambo International Airport |  | ZA | 463 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 275 | 21m | 244 km | 1,157.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 183 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 172 | 1h 12m | 770 km | 2,284.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 165 | 26m | 275 km | 781.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 123 | 31m | 369 km | 782.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 115 | 27m | 215 km | 425.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 110 | 14m | 154 km | 291.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 95 | 1h 2m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEE339 | AEE | Chania International Airport (LGSA) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-10 10:12 UTC | 2026-05-10 10:48 UTC | 35m |
| GBOHJ | GBO | Leicester Airport (EGBG) | Bruntingthorpe Airport (EG74) | 2026-05-10 10:07 UTC | 2026-05-10 10:29 UTC | 22m |
| GBSLT | GBS | Perth/Scone Airport (EGPT) | Perth/Scone Airport (EGPT) | 2026-05-10 10:07 UTC | 2026-05-10 10:26 UTC | 19m |
| SEH311 | SEH | Mikonos Airport (LGMK) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-10 09:59 UTC | 2026-05-10 10:26 UTC | 26m |
| AIC219 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-05-10 09:11 UTC | 2026-05-10 10:21 UTC | 1h 10m |
|  |  | Zell Am See Airport (LOWZ) | Zell Am See Airport (LOWZ) | 2026-05-10 10:06 UTC | 2026-05-10 10:17 UTC | 11m |
| N353SF |  | Washington Dulles International Airport (KIAD) | John F Kennedy International Airport (KJFK) | 2026-05-10 09:30 UTC | 2026-05-10 10:17 UTC | 46m |
| 2SALE |  | Gloucestershire Airport (EGBJ) | Liverpool John Lennon Airport (EGGP) | 2026-05-10 09:33 UTC | 2026-05-10 10:10 UTC | 37m |
| IGO1631 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Naypyidaw Airport (VYEL) | 2026-05-10 09:03 UTC | 2026-05-10 10:00 UTC | 57m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-05-10 09:40 UTC | 2026-05-10 10:00 UTC | 19m |
| HWS08 | HWS | Malmen Air Base (ESCF) | Malmen Air Base (ESCF) | 2026-05-10 09:57 UTC | 2026-05-10 10:00 UTC | 3m |
| GCJBH | GCJ | Bagby Thirsk Prv Airport (EGNG) | Bagby Thirsk Prv Airport (EGNG) | 2026-05-10 09:23 UTC | 2026-05-10 09:55 UTC | 31m |
| AFR68LX | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-05-10 08:56 UTC | 2026-05-10 09:55 UTC | 59m |
| SNJ97 | SNJ | Tokyo International Airport (RJTT) | Hiroshima Airport (RJOA) | 2026-05-10 08:45 UTC | 2026-05-10 09:54 UTC | 1h 8m |
| N456V |  | CA38 (CA38) | Silver Creek Ranch Airport (41CA) | 2026-05-10 09:15 UTC | 2026-05-10 09:51 UTC | 35m |
| APG715 | APG | Ninoy Aquino International Airport (RPLL) | Romblon Airport (RPVU) | 2026-05-10 09:25 UTC | 2026-05-10 09:50 UTC | 24m |
| DLH6YY | Lufthansa | Dusseldorf International Airport (EDDL) | Frankfurt am Main International Airport (EDDF) | 2026-05-10 09:24 UTC | 2026-05-10 09:50 UTC | 26m |
| UBG109 | UBG | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-05-10 09:14 UTC | 2026-05-10 09:49 UTC | 35m |
| EXS31DR | EXS | London Stansted Airport (EGSS) | Ibiza Airport (LEIB) | 2026-05-10 07:32 UTC | 2026-05-10 09:47 UTC | 2h 15m |
| N7413B |  | Teterboro Airport (KTEB) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-10 04:24 UTC | 2026-05-10 09:45 UTC | 5h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
