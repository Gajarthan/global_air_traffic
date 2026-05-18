# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_18:55:42_UTC-green)

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

**Latest saved flight:** 2026-05-18 18:55:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-18 18:55:42 UTC

- **87,448** saved flights
- **31,292** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,448** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,082,608.2 tonnes** estimated CO2 emissions
- **62,759,894 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3745 |
| 2 | SkyWest Airlines | 3239 |
| 3 | IndiGo | 1868 |
| 4 | EJA | 1658 |
| 5 | American Airlines | 1342 |
| 6 | Southwest Airlines | 1277 |
| 7 | Lufthansa | 1102 |
| 8 | ENY | 1086 |
| 9 | Delta Air Lines | 960 |
| 10 | Vueling | 832 |
| 11 | LATAM Airlines | 790 |
| 12 | AXM | 782 |
| 13 | WIF | 749 |
| 14 | AZU | 692 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 642 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 623 |
| 20 | easyJet | 575 |
| 21 | EJU | 565 |
| 22 | Cathay Pacific | 555 |
| 23 | AEE | 546 |
| 24 | VIV | 525 |
| 25 | Air France | 511 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 460 |
| 28 | AXB | 456 |
| 29 | MXY | 444 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71709 |
| 2 | 🇪🇸 ES | 6196 |
| 3 | 🇮🇳 IN | 5848 |
| 4 | 🇦🇺 AU | 5486 |
| 5 | 🇩🇪 DE | 4867 |
| 6 | 🇮🇹 IT | 4852 |
| 7 | 🇧🇷 BR | 4812 |
| 8 | 🇨🇦 CA | 4361 |
| 9 | 🇯🇵 JP | 4323 |
| 10 | 🇬🇧 GB | 3730 |
| 11 | 🇫🇷 FR | 3495 |
| 12 | 🇨🇴 CO | 2965 |
| 13 | 🇲🇽 MX | 2723 |
| 14 | 🇬🇷 GR | 2543 |
| 15 | 🇳🇴 NO | 2420 |
| 16 | 🇨🇭 CH | 2315 |
| 17 | 🇲🇾 MY | 1965 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1588 |
| 20 | 🇳🇿 NZ | 1519 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1452 |
| 23 | 🇰🇷 KR | 1360 |
| 24 | 🇵🇭 PH | 1354 |
| 25 | 🇬🇹 GT | 1319 |
| 26 | 🇲🇴 MO | 1016 |
| 27 | 🇲🇦 MA | 1014 |
| 28 | 🇲🇪 ME | 906 |
| 29 | 🇳🇱 NL | 892 |
| 30 | 🇭🇷 HR | 787 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1922 |
| 2 | Denver International Airport |  | US | 1465 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1257 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1207 |
| 6 | Harry Reid International Airport |  | US | 1113 |
| 7 | Frankfurt am Main International Airport |  | DE | 1113 |
| 8 | Zurich Airport |  | CH | 1043 |
| 9 | Macau International Airport |  | MO | 1016 |
| 10 | Guaymaral Airport |  | CO | 1005 |
| 11 | La Aurora Airport |  | GT | 1002 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 969 |
| 13 | El Dorado International Airport |  | CO | 948 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 884 |
| 15 | Chicago O'Hare International Airport |  | US | 844 |
| 16 | Madrid Barajas International Airport |  | ES | 794 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 752 |
| 19 | Capua Airport |  | IT | 740 |
| 20 | Salt Lake City International Airport |  | US | 730 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 22 | Malpensa International Airport |  | IT | 716 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 680 |
| 25 | Charlotte/Douglas International Airport |  | US | 678 |
| 26 | Congonhas Airport |  | BR | 673 |
| 27 | Daniel K Inouye International Airport |  | US | 642 |
| 28 | Tenerife Norte Airport |  | ES | 641 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 589 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 581 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 561 |
| 35 | Vitoria/Foronda Airport |  | ES | 558 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 552 |
| 37 | Amsterdam Airport Schiphol |  | NL | 546 |
| 38 | Don Mueang International Airport |  | TH | 545 |
| 39 | Calgary International Airport |  | CA | 514 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 412 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 326 | 21m | 244 km | 1,372.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 225 | 14m | 114 km | 441.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 223 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 147 | 21m | 99 km | 251.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 127 | 20m | 147 km | 321.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 112 | 18m | 144 km | 278.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 106 | 1h 52m | 1,304 km | 2,384.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFAB123 | FFA | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-05-18 18:32 UTC | 2026-05-18 18:55 UTC | 23m |
| N9134Q |  | Chatham Municipal Airport (KCQX) | Provincetown Municipal Airport (KPVC) | 2026-05-18 17:13 UTC | 2026-05-18 18:46 UTC | 1h 32m |
| LNG12 | LNG | Fort Worth Nas Jrb (Carswell Field) Airport (KNFW) | Flying Oaks Airport (2TE2) | 2026-05-18 18:16 UTC | 2026-05-18 18:39 UTC | 23m |
| G20300 |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-05-18 18:19 UTC | 2026-05-18 18:39 UTC | 19m |
| N7040Q |  | Mount Pleasant Landing Strip (67NJ) | Blairstown Airport (K1N7) | 2026-05-18 18:08 UTC | 2026-05-18 18:37 UTC | 29m |
| N751SP |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-05-18 17:39 UTC | 2026-05-18 18:31 UTC | 52m |
| ASP864 | ASP | Edmonton International Airport (CYEG) | Harry Reid International Airport (KLAS) | 2026-05-18 15:34 UTC | 2026-05-18 18:28 UTC | 2h 54m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-05-18 16:55 UTC | 2026-05-18 18:28 UTC | 1h 32m |
| ERU842 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-05-18 17:39 UTC | 2026-05-18 18:26 UTC | 47m |
| N30JA |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-18 17:57 UTC | 2026-05-18 18:25 UTC | 28m |
| UAL991 | United Airlines | Barcelona International Airport (LEBL) | Washington Dulles International Airport (KIAD) | 2026-05-18 09:59 UTC | 2026-05-18 18:25 UTC | 8h 25m |
| C2701 |  | Mc Clellan Airfield (KMCC) | Boeing Field/King County International Airport (KBFI) | 2026-05-18 16:08 UTC | 2026-05-18 18:24 UTC | 2h 16m |
| N54RJ |  | Perry-Houston County Airport (KPXE) | Southwest Georgia Regional Airport (KABY) | 2026-05-18 18:08 UTC | 2026-05-18 18:23 UTC | 14m |
| ETD937 | Etihad Airways | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-17 16:07 UTC | 2026-05-18 18:22 UTC | 26h 14m |
| N8125L |  | Roberts Field (KRDM) | Dry Creek Airpark (OG21) | 2026-05-18 18:04 UTC | 2026-05-18 18:17 UTC | 13m |
| LD501 |  | Comandante Espora Airport (SAZB) | SA14 (SA14) | 2026-05-18 17:46 UTC | 2026-05-18 18:16 UTC | 30m |
| FFAB123 | FFA | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-05-18 17:34 UTC | 2026-05-18 18:15 UTC | 41m |
| GSTDR31 | GST | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-05-18 16:32 UTC | 2026-05-18 18:15 UTC | 1h 43m |
| N8710U |  | Savannah/Hilton Head International Airport (KSAV) | Hilton Head Airport (KHXD) | 2026-05-18 17:16 UTC | 2026-05-18 18:12 UTC | 55m |
| N398PF |  | St Louis Regional Airport (KALN) | St Paul Downtown Holman Field (KSTP) | 2026-05-18 16:58 UTC | 2026-05-18 18:09 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
