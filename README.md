# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_17:40:41_UTC-green)

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

**Latest saved flight:** 2026-05-15 17:40:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 17:40:41 UTC

- **83,248** saved flights
- **30,107** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,248** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,024,502.3 tonnes** estimated CO2 emissions
- **59,391,435 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3564 |
| 2 | SkyWest Airlines | 3076 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1563 |
| 5 | American Airlines | 1280 |
| 6 | Southwest Airlines | 1217 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1035 |
| 9 | Delta Air Lines | 911 |
| 10 | Vueling | 788 |
| 11 | LATAM Airlines | 753 |
| 12 | AXM | 751 |
| 13 | WIF | 723 |
| 14 | AZU | 655 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 647 |
| 17 | QLK | 615 |
| 18 | LXJ | 608 |
| 19 | Alaska Airlines | 587 |
| 20 | easyJet | 547 |
| 21 | EJU | 534 |
| 22 | AEE | 528 |
| 23 | Cathay Pacific | 518 |
| 24 | VIV | 498 |
| 25 | Air France | 489 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 443 |
| 28 | CXK | 440 |
| 29 | MXY | 413 |
| 30 | AIQ | 410 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68042 |
| 2 | 🇪🇸 ES | 5905 |
| 3 | 🇮🇳 IN | 5654 |
| 4 | 🇦🇺 AU | 5322 |
| 5 | 🇩🇪 DE | 4662 |
| 6 | 🇮🇹 IT | 4602 |
| 7 | 🇧🇷 BR | 4601 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4147 |
| 10 | 🇬🇧 GB | 3552 |
| 11 | 🇫🇷 FR | 3313 |
| 12 | 🇨🇴 CO | 2770 |
| 13 | 🇲🇽 MX | 2524 |
| 14 | 🇬🇷 GR | 2419 |
| 15 | 🇳🇴 NO | 2325 |
| 16 | 🇨🇭 CH | 2215 |
| 17 | 🇲🇾 MY | 1889 |
| 18 | 🇿🇦 ZA | 1572 |
| 19 | 🇹🇷 TR | 1480 |
| 20 | 🇳🇿 NZ | 1463 |
| 21 | 🇹🇭 TH | 1452 |
| 22 | 🇵🇱 PL | 1386 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1257 |
| 26 | 🇲🇦 MA | 968 |
| 27 | 🇲🇴 MO | 952 |
| 28 | 🇲🇪 ME | 883 |
| 29 | 🇳🇱 NL | 858 |
| 30 | 🇭🇷 HR | 745 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1824 |
| 2 | Tokyo International Airport |  | JP | 1406 |
| 3 | Denver International Airport |  | US | 1392 |
| 4 | Indira Gandhi International Airport |  | IN | 1201 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1177 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1036 |
| 8 | Zurich Airport |  | CH | 991 |
| 9 | La Aurora Airport |  | GT | 952 |
| 10 | Macau International Airport |  | MO | 952 |
| 11 | Guaymaral Airport |  | CO | 935 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 926 |
| 13 | El Dorado International Airport |  | CO | 891 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 832 |
| 15 | Chicago O'Hare International Airport |  | US | 804 |
| 16 | Madrid Barajas International Airport |  | ES | 758 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 722 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 20 | Malpensa International Airport |  | IT | 696 |
| 21 | Bengaluru International Airport |  | IN | 694 |
| 22 | Salt Lake City International Airport |  | US | 690 |
| 23 | Capua Airport |  | IT | 675 |
| 24 | Charles de Gaulle International Airport |  | FR | 652 |
| 25 | Charlotte/Douglas International Airport |  | US | 649 |
| 26 | Congonhas Airport |  | BR | 648 |
| 27 | Tenerife Norte Airport |  | ES | 605 |
| 28 | Daniel K Inouye International Airport |  | US | 601 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 558 |
| 32 | Barcelona International Airport |  | ES | 558 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 556 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 538 |
| 35 | Vitoria/Foronda Airport |  | ES | 528 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 520 |
| 38 | Amsterdam Airport Schiphol |  | NL | 519 |
| 39 | O. R. Tambo International Airport |  | ZA | 493 |
| 40 | Calgary International Airport |  | CA | 488 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 390 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 299 | 21m | 244 km | 1,259.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 212 | 14m | 114 km | 415.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 173 | 26m | 275 km | 819.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 125 | 27m | 152 km | 326.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 122 | 20m | 147 km | 308.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 117 | 23m | 55 km | 111.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 117 | 20m | 250 km | 505.4 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 106 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 105 | 18m | 144 km | 261.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 100 | 1h 18m | 961 km | 1,657.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RNGR873 | RNG | Ingleside Regional Airport (KTFP) | Ingleside Regional Airport (KTFP) | 2026-05-15 17:10 UTC | 2026-05-15 17:40 UTC | 30m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-15 17:26 UTC | 2026-05-15 17:39 UTC | 12m |
| LXJ437 | LXJ | Scottsdale Airport (KSDL) | Moffett Federal Airfield (KNUQ) | 2026-05-15 16:03 UTC | 2026-05-15 17:37 UTC | 1h 34m |
| N698JA |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-05-15 17:15 UTC | 2026-05-15 17:37 UTC | 22m |
| BOE867 | BOE | Boeing Field/King County International Airport (KBFI) | Grant County International Airport (KMWH) | 2026-05-15 16:28 UTC | 2026-05-15 17:35 UTC | 1h 7m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-15 17:11 UTC | 2026-05-15 17:34 UTC | 22m |
| NASA501 | NAS | Newport News/Williamsburg International Airport (KPHF) | Newport News/Williamsburg International Airport (KPHF) | 2026-05-15 17:28 UTC | 2026-05-15 17:29 UTC | 0m |
| N6458B |  | Double Eagle Ii Airport (KAEG) | Los Alamos Airport (KLAM) | 2026-05-15 16:47 UTC | 2026-05-15 17:26 UTC | 39m |
| N990AM |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-05-15 16:58 UTC | 2026-05-15 17:26 UTC | 27m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-05-15 15:36 UTC | 2026-05-15 17:26 UTC | 1h 50m |
| AXY387M | AXY | Morante Airport (LETE) | Istanbul Hezarfen Airfield (LTBW) | 2026-05-15 14:04 UTC | 2026-05-15 17:25 UTC | 3h 21m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-05-15 17:12 UTC | 2026-05-15 17:25 UTC | 12m |
| CODE21 | COD | 75OK (75OK) | Sopwith Ldg Airport (OK56) | 2026-05-15 17:05 UTC | 2026-05-15 17:19 UTC | 14m |
| SLH560 | SLH | Indianapolis International Airport (KIND) | Lincoln Airport (KLNK) | 2026-05-15 15:50 UTC | 2026-05-15 17:17 UTC | 1h 27m |
| N1450U |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-15 15:51 UTC | 2026-05-15 17:15 UTC | 1h 23m |
| C2703 |  | Mc Clellan Airfield (KMCC) | Longbell Ranch Airport (2CL3) | 2026-05-15 16:20 UTC | 2026-05-15 17:14 UTC | 54m |
| N717TF |  | Harry Reid International Airport (KLAS) | Henderson Executive Airport (KHND) | 2026-05-15 16:53 UTC | 2026-05-15 17:14 UTC | 20m |
| N550WW |  | Colorado City Municipal Airport (KAZC) | Twentynine Palms Airport (KTNP) | 2026-05-15 16:45 UTC | 2026-05-15 17:14 UTC | 28m |
| AWH25H | AWH | Saarbrucken Airport (EDDR) | Leipzig Halle Airport (EDDP) | 2026-05-15 16:28 UTC | 2026-05-15 17:11 UTC | 43m |
| DREAD81 | DRE | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | AL78 (AL78) | 2026-05-15 16:34 UTC | 2026-05-15 17:11 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
