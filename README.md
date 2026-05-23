# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_22:50:36_UTC-green)

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

**Latest saved flight:** 2026-05-23 22:50:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 22:50:36 UTC

- **93,303** saved flights
- **33,030** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **93,303** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,147,639.7 tonnes** estimated CO2 emissions
- **66,529,837 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3938 |
| 2 | SkyWest Airlines | 3470 |
| 3 | IndiGo | 1936 |
| 4 | EJA | 1770 |
| 5 | American Airlines | 1421 |
| 6 | Southwest Airlines | 1355 |
| 7 | ENY | 1156 |
| 8 | Lufthansa | 1130 |
| 9 | Delta Air Lines | 1024 |
| 10 | Vueling | 886 |
| 11 | LATAM Airlines | 833 |
| 12 | AXM | 818 |
| 13 | WIF | 809 |
| 14 | AZU | 742 |
| 15 | LXJ | 707 |
| 16 | Swiss International | 695 |
| 17 | All Nippon Airways | 689 |
| 18 | Alaska Airlines | 652 |
| 19 | QLK | 648 |
| 20 | easyJet | 610 |
| 21 | EJU | 598 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 566 |
| 24 | VIV | 554 |
| 25 | Air France | 546 |
| 26 | CXK | 498 |
| 27 | MXY | 493 |
| 28 | Japan Airlines | 487 |
| 29 | AXB | 473 |
| 30 | AIQ | 449 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 77269 |
| 2 | 🇪🇸 ES | 6541 |
| 3 | 🇮🇳 IN | 6106 |
| 4 | 🇦🇺 AU | 5733 |
| 5 | 🇩🇪 DE | 5114 |
| 6 | 🇧🇷 BR | 5110 |
| 7 | 🇮🇹 IT | 5065 |
| 8 | 🇨🇦 CA | 4731 |
| 9 | 🇯🇵 JP | 4476 |
| 10 | 🇬🇧 GB | 3974 |
| 11 | 🇫🇷 FR | 3755 |
| 12 | 🇨🇴 CO | 3246 |
| 13 | 🇲🇽 MX | 2875 |
| 14 | 🇬🇷 GR | 2680 |
| 15 | 🇳🇴 NO | 2585 |
| 16 | 🇨🇭 CH | 2432 |
| 17 | 🇲🇾 MY | 2066 |
| 18 | 🇹🇷 TR | 1714 |
| 19 | 🇿🇦 ZA | 1683 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1572 |
| 22 | 🇵🇱 PL | 1521 |
| 23 | 🇰🇷 KR | 1476 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1407 |
| 26 | 🇲🇦 MA | 1068 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 935 |
| 29 | 🇲🇪 ME | 930 |
| 30 | 🇭🇷 HR | 842 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2028 |
| 2 | Denver International Airport |  | US | 1577 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1330 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1241 |
| 6 | Harry Reid International Airport |  | US | 1203 |
| 7 | Frankfurt am Main International Airport |  | DE | 1141 |
| 8 | Guaymaral Airport |  | CO | 1132 |
| 9 | Zurich Airport |  | CH | 1086 |
| 10 | La Aurora Airport |  | GT | 1075 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1022 |
| 13 | El Dorado International Airport |  | CO | 1019 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 934 |
| 15 | Chicago O'Hare International Airport |  | US | 891 |
| 16 | Madrid Barajas International Airport |  | ES | 836 |
| 17 | Kuala Lumpur International Airport |  | MY | 816 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 788 |
| 19 | Salt Lake City International Airport |  | US | 785 |
| 20 | Capua Airport |  | IT | 776 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 744 |
| 22 | Malpensa International Airport |  | IT | 740 |
| 23 | Bengaluru International Airport |  | IN | 734 |
| 24 | Charles de Gaulle International Airport |  | FR | 727 |
| 25 | Charlotte/Douglas International Airport |  | US | 712 |
| 26 | Congonhas Airport |  | BR | 708 |
| 27 | Daniel K Inouye International Airport |  | US | 673 |
| 28 | Tenerife Norte Airport |  | ES | 664 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 627 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 624 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 609 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 599 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 593 |
| 35 | Vitoria/Foronda Airport |  | ES | 583 |
| 36 | Don Mueang International Airport |  | TH | 576 |
| 37 | Amsterdam Airport Schiphol |  | NL | 575 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 567 |
| 39 | Calgary International Airport |  | CA | 555 |
| 40 | O. R. Tambo International Airport |  | ZA | 533 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 465 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 345 | 21m | 244 km | 1,452.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 248 | 9m | - | - |
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
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 120 | 18m | 144 km | 298.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 115 | 1h 40m | 1,156 km | 2,294.2 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 112 | 1h 18m | 961 km | 1,856.5 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-23 22:04 UTC | 2026-05-23 22:50 UTC | 45m |
| N884HB |  | Crystal Springs Ranch Airport (UT54) | K36U (K36U) | 2026-05-23 21:44 UTC | 2026-05-23 22:34 UTC | 50m |
| N413GG |  | Raleigh-Durham International Airport (KRDU) | NC20 (NC20) | 2026-05-23 22:15 UTC | 2026-05-23 22:32 UTC | 16m |
| VAR854 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-05-23 20:38 UTC | 2026-05-23 22:23 UTC | 1h 44m |
| N280CM |  | Redlands Municipal Airport (KREI) | 4CL4 (4CL4) | 2026-05-23 22:08 UTC | 2026-05-23 22:21 UTC | 12m |
| N32AW |  | Kissimmee Gateway Airport (KISM) | Kissimmee Gateway Airport (KISM) | 2026-05-23 22:06 UTC | 2026-05-23 22:16 UTC | 10m |
| N570JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-05-23 22:06 UTC | 2026-05-23 22:14 UTC | 8m |
| N88EJ |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | K36U (K36U) | 2026-05-23 20:52 UTC | 2026-05-23 22:10 UTC | 1h 18m |
| N4789E |  | Montgomery-Gibbs Executive Airport (KMYF) | General Wm J Fox Airfield (KWJF) | 2026-05-23 20:51 UTC | 2026-05-23 22:05 UTC | 1h 13m |
| RFD9000 | RFD | General Mariano Escobedo International Airport (MMMY) | Plan De Guadalupe International Airport (MMIO) | 2026-05-23 21:04 UTC | 2026-05-23 22:04 UTC | 59m |
| WZZ1469 | Wizz Air | Gothenburg-Landvetter Airport (ESGG) | Jorge Chavez International Airport (SPJC) | 2026-05-23 20:53 UTC | 2026-05-23 22:03 UTC | 1h 9m |
| ZMV | ZMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-05-23 21:45 UTC | 2026-05-23 22:02 UTC | 16m |
| MXY2854 | MXY | Raleigh-Durham International Airport (KRDU) | Bangor International Airport (KBGR) | 2026-05-23 20:17 UTC | 2026-05-23 22:01 UTC | 1h 43m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-23 21:29 UTC | 2026-05-23 21:57 UTC | 28m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-05-23 21:00 UTC | 2026-05-23 21:56 UTC | 56m |
| JBU1042 | JetBlue | Buffalo Niagara International Airport (KBUF) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-23 21:37 UTC | 2026-05-23 21:55 UTC | 18m |
| N132TS |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-23 21:49 UTC | 2026-05-23 21:55 UTC | 6m |
| N125PM |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-05-23 14:49 UTC | 2026-05-23 21:55 UTC | 7h 5m |
| N118JK |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-05-23 20:48 UTC | 2026-05-23 21:55 UTC | 1h 7m |
| N5765B |  | Reek Ranch Airport (ID63) | Reek Ranch Airport (ID63) | 2026-05-23 21:35 UTC | 2026-05-23 21:54 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
