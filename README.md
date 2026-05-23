# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_17:29:56_UTC-green)

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

**Latest saved flight:** 2026-05-23 17:29:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 17:29:56 UTC

- **92,831** saved flights
- **32,892** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,831** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,141,502.0 tonnes** estimated CO2 emissions
- **66,174,029 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3926 |
| 2 | SkyWest Airlines | 3438 |
| 3 | IndiGo | 1935 |
| 4 | EJA | 1761 |
| 5 | American Airlines | 1405 |
| 6 | Southwest Airlines | 1337 |
| 7 | ENY | 1146 |
| 8 | Lufthansa | 1128 |
| 9 | Delta Air Lines | 1016 |
| 10 | Vueling | 883 |
| 11 | LATAM Airlines | 825 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 741 |
| 15 | LXJ | 702 |
| 16 | Swiss International | 694 |
| 17 | All Nippon Airways | 689 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 606 |
| 21 | EJU | 592 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 563 |
| 24 | VIV | 550 |
| 25 | Air France | 545 |
| 26 | CXK | 492 |
| 27 | Japan Airlines | 487 |
| 28 | MXY | 487 |
| 29 | AXB | 471 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76715 |
| 2 | 🇪🇸 ES | 6523 |
| 3 | 🇮🇳 IN | 6097 |
| 4 | 🇦🇺 AU | 5730 |
| 5 | 🇩🇪 DE | 5101 |
| 6 | 🇧🇷 BR | 5080 |
| 7 | 🇮🇹 IT | 5051 |
| 8 | 🇨🇦 CA | 4699 |
| 9 | 🇯🇵 JP | 4476 |
| 10 | 🇬🇧 GB | 3952 |
| 11 | 🇫🇷 FR | 3744 |
| 12 | 🇨🇴 CO | 3225 |
| 13 | 🇲🇽 MX | 2854 |
| 14 | 🇬🇷 GR | 2659 |
| 15 | 🇳🇴 NO | 2580 |
| 16 | 🇨🇭 CH | 2429 |
| 17 | 🇲🇾 MY | 2065 |
| 18 | 🇹🇷 TR | 1700 |
| 19 | 🇿🇦 ZA | 1683 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1571 |
| 22 | 🇵🇱 PL | 1519 |
| 23 | 🇰🇷 KR | 1475 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1399 |
| 26 | 🇲🇦 MA | 1064 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 932 |
| 29 | 🇲🇪 ME | 929 |
| 30 | 🇭🇷 HR | 841 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2010 |
| 2 | Denver International Airport |  | US | 1556 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1328 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1238 |
| 6 | Harry Reid International Airport |  | US | 1195 |
| 7 | Frankfurt am Main International Airport |  | DE | 1138 |
| 8 | Guaymaral Airport |  | CO | 1120 |
| 9 | Zurich Airport |  | CH | 1085 |
| 10 | La Aurora Airport |  | GT | 1068 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1017 |
| 13 | El Dorado International Airport |  | CO | 1015 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 931 |
| 15 | Chicago O'Hare International Airport |  | US | 885 |
| 16 | Madrid Barajas International Airport |  | ES | 833 |
| 17 | Kuala Lumpur International Airport |  | MY | 815 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 781 |
| 19 | Salt Lake City International Airport |  | US | 779 |
| 20 | Capua Airport |  | IT | 772 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 738 |
| 23 | Bengaluru International Airport |  | IN | 733 |
| 24 | Charles de Gaulle International Airport |  | FR | 725 |
| 25 | Charlotte/Douglas International Airport |  | US | 710 |
| 26 | Congonhas Airport |  | BR | 707 |
| 27 | Daniel K Inouye International Airport |  | US | 670 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 623 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 615 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 605 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 598 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 584 |
| 35 | Vitoria/Foronda Airport |  | ES | 583 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 572 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 550 |
| 40 | O. R. Tambo International Airport |  | ZA | 533 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 460 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 342 | 21m | 244 km | 1,440.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 245 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 201 | 19m | 165 km | 571.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 138 | 27m | 215 km | 511.1 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 113 | 1h 40m | 1,156 km | 2,254.3 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | Nevada County Airport (KGOO) | Truckee-Tahoe Airport (KTRK) | 2026-05-23 16:59 UTC | 2026-05-23 17:29 UTC | 30m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 17:02 UTC | 2026-05-23 17:23 UTC | 20m |
| N154RV |  | K00V (K00V) | Central Colorado Regional Airport (KAEJ) | 2026-05-23 16:50 UTC | 2026-05-23 17:22 UTC | 32m |
| CFKSF | CFK | Campbell River Airport (CYBL) | Pitt Meadows Airport (CYPK) | 2026-05-23 16:43 UTC | 2026-05-23 17:18 UTC | 35m |
| N98MN |  | Hartford-Brainard Airport (KHFD) | Worcester Regional Airport (KORH) | 2026-05-23 17:06 UTC | 2026-05-23 17:18 UTC | 12m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 16:57 UTC | 2026-05-23 17:18 UTC | 20m |
| N733HK |  | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-05-23 16:30 UTC | 2026-05-23 17:17 UTC | 47m |
| N12648 |  | Portland-Troutdale Airport (KTTD) | Brown's Cape Horn Airport (4WA1) | 2026-05-23 17:06 UTC | 2026-05-23 17:14 UTC | 8m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-23 17:00 UTC | 2026-05-23 17:13 UTC | 13m |
| N335F |  | Austin-Bergstrom International Airport (KAUS) | Jicarilla Apache Nation Airport (K24N) | 2026-05-23 15:36 UTC | 2026-05-23 17:12 UTC | 1h 35m |
| N475RC |  | Wisky Ranch/Chevlon Airport (6AZ2) | Payson Airport (KPAN) | 2026-05-23 17:01 UTC | 2026-05-23 17:12 UTC | 10m |
| N326LH |  | KFTG (KFTG) | Spring Canyon Airport (CO94) | 2026-05-23 16:48 UTC | 2026-05-23 17:09 UTC | 21m |
| N78183 |  | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-05-23 17:03 UTC | 2026-05-23 17:05 UTC | 2m |
| N411UH |  | Hill Afb Airport (KHIF) | Salt Lake City International Airport (KSLC) | 2026-05-23 16:48 UTC | 2026-05-23 17:02 UTC | 14m |
| BYF30 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-05-23 16:29 UTC | 2026-05-23 16:54 UTC | 24m |
| XBNYR | XBN | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-05-23 16:36 UTC | 2026-05-23 16:54 UTC | 17m |
| N456JB |  | French Valley Airport (KF70) | Riverside Airport (KRAL) | 2026-05-23 16:18 UTC | 2026-05-23 16:53 UTC | 35m |
| N350RX |  | CL36 (CL36) | Truckee-Tahoe Airport (KTRK) | 2026-05-23 16:31 UTC | 2026-05-23 16:53 UTC | 22m |
| N251SF |  | Dupage Airport (KDPA) | Hendrickson Flying Service Airport (IL93) | 2026-05-23 16:36 UTC | 2026-05-23 16:51 UTC | 15m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-05-23 16:20 UTC | 2026-05-23 16:48 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
