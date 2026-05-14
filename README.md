# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_01:51:21_UTC-green)

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

**Latest saved flight:** 2026-05-14 01:51:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 01:51:21 UTC

- **81,205** saved flights
- **29,465** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,205** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,000,373.0 tonnes** estimated CO2 emissions
- **57,992,636 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3477 |
| 2 | SkyWest Airlines | 3020 |
| 3 | IndiGo | 1777 |
| 4 | EJA | 1525 |
| 5 | American Airlines | 1255 |
| 6 | Southwest Airlines | 1190 |
| 7 | Lufthansa | 1055 |
| 8 | ENY | 1019 |
| 9 | Delta Air Lines | 894 |
| 10 | Vueling | 771 |
| 11 | LATAM Airlines | 741 |
| 12 | AXM | 735 |
| 13 | WIF | 702 |
| 14 | All Nippon Airways | 643 |
| 15 | AZU | 640 |
| 16 | Swiss International | 630 |
| 17 | QLK | 601 |
| 18 | LXJ | 592 |
| 19 | Alaska Airlines | 577 |
| 20 | easyJet | 538 |
| 21 | EJU | 521 |
| 22 | AEE | 517 |
| 23 | Cathay Pacific | 509 |
| 24 | VIV | 483 |
| 25 | Air France | 476 |
| 26 | Japan Airlines | 461 |
| 27 | AXB | 439 |
| 28 | CXK | 423 |
| 29 | AIQ | 403 |
| 30 | United Airlines | 403 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66274 |
| 2 | 🇪🇸 ES | 5760 |
| 3 | 🇮🇳 IN | 5559 |
| 4 | 🇦🇺 AU | 5203 |
| 5 | 🇩🇪 DE | 4568 |
| 6 | 🇧🇷 BR | 4488 |
| 7 | 🇮🇹 IT | 4481 |
| 8 | 🇯🇵 JP | 4139 |
| 9 | 🇨🇦 CA | 4049 |
| 10 | 🇬🇧 GB | 3472 |
| 11 | 🇫🇷 FR | 3220 |
| 12 | 🇨🇴 CO | 2721 |
| 13 | 🇲🇽 MX | 2453 |
| 14 | 🇬🇷 GR | 2368 |
| 15 | 🇳🇴 NO | 2261 |
| 16 | 🇨🇭 CH | 2183 |
| 17 | 🇲🇾 MY | 1844 |
| 18 | 🇿🇦 ZA | 1530 |
| 19 | 🇹🇷 TR | 1446 |
| 20 | 🇳🇿 NZ | 1428 |
| 21 | 🇹🇭 TH | 1426 |
| 22 | 🇵🇱 PL | 1350 |
| 23 | 🇵🇭 PH | 1280 |
| 24 | 🇬🇹 GT | 1242 |
| 25 | 🇰🇷 KR | 1239 |
| 26 | 🇲🇦 MA | 949 |
| 27 | 🇲🇴 MO | 934 |
| 28 | 🇲🇪 ME | 867 |
| 29 | 🇳🇱 NL | 837 |
| 30 | 🇭🇷 HR | 717 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1785 |
| 2 | Tokyo International Airport |  | JP | 1389 |
| 3 | Denver International Airport |  | US | 1367 |
| 4 | Indira Gandhi International Airport |  | IN | 1178 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1159 |
| 6 | Frankfurt am Main International Airport |  | DE | 1065 |
| 7 | Harry Reid International Airport |  | US | 1009 |
| 8 | Zurich Airport |  | CH | 967 |
| 9 | La Aurora Airport |  | GT | 938 |
| 10 | Macau International Airport |  | MO | 934 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 919 |
| 12 | Guaymaral Airport |  | CO | 913 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 791 |
| 16 | Madrid Barajas International Airport |  | ES | 742 |
| 17 | Kuala Lumpur International Airport |  | MY | 738 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 711 |
| 19 | Malpensa International Airport |  | IT | 689 |
| 20 | Bengaluru International Airport |  | IN | 683 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 682 |
| 22 | Salt Lake City International Airport |  | US | 673 |
| 23 | Capua Airport |  | IT | 660 |
| 24 | Charlotte/Douglas International Airport |  | US | 634 |
| 25 | Charles de Gaulle International Airport |  | FR | 634 |
| 26 | Congonhas Airport |  | BR | 633 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Daniel K Inouye International Airport |  | US | 590 |
| 29 | Ninoy Aquino International Airport |  | PH | 585 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 579 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 544 |
| 32 | Barcelona International Airport |  | ES | 542 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 541 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 526 |
| 35 | Vitoria/Foronda Airport |  | ES | 513 |
| 36 | Don Mueang International Airport |  | TH | 512 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 510 |
| 38 | Amsterdam Airport Schiphol |  | NL | 506 |
| 39 | O. R. Tambo International Airport |  | ZA | 486 |
| 40 | Calgary International Airport |  | CA | 480 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 294 | 21m | 244 km | 1,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 272 | 1h 8m | 706 km | 3,311.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 233 | 24m | 225 km | 903.9 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 218 | 1h 27m | 910 km | 3,420.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 217 | 28m | 304 km | 1,137.6 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 208 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 192 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 186 | 19m | 165 km | 529.1 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 184 | 1h 11m | 770 km | 2,444.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 141 | 20m | 99 km | 241.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 127 | 31m | 369 km | 808.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 118 | 20m | 147 km | 298.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 114 | 14m | 154 km | 302.1 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 23 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 108 | 57m | 493 km | 918.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 101 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PBR750 | PBR | Grand Junction Regional Airport (KGJT) | Vancouver International Airport (CYVR) | 2026-05-13 23:47 UTC | 2026-05-14 01:51 UTC | 2h 4m |
| R8563 |  | Wollongong Airport (YWOL) | Wollongong Airport (YWOL) | 2026-05-14 01:39 UTC | 2026-05-14 01:50 UTC | 11m |
| MONDO14 | MON | Striplin Airfield (AL62) | 5AL8 (5AL8) | 2026-05-14 01:22 UTC | 2026-05-14 01:39 UTC | 16m |
| PPJMJ | PPJ | Araxa Airport (SBAX) | Congonhas Airport (SBSP) | 2026-05-14 00:54 UTC | 2026-05-14 01:30 UTC | 36m |
| N853HL |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-05-14 00:57 UTC | 2026-05-14 01:29 UTC | 32m |
| N734DG |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-14 01:00 UTC | 2026-05-14 01:29 UTC | 29m |
| RCANE43 | RCA | T W Spear Memorial Airport (4AL9) | Northwest Florida Beaches International Airport (KECP) | 2026-05-14 00:41 UTC | 2026-05-14 01:29 UTC | 47m |
| FD629 |  | Perth Jandakot Airport (YPJT) | Wyalkatchem Airport (YWKM) | 2026-05-14 00:57 UTC | 2026-05-14 01:28 UTC | 31m |
| T73 |  | Hemet-Ryan Airport (KHMT) | Krey Field (0CL1) | 2026-05-14 01:09 UTC | 2026-05-14 01:25 UTC | 16m |
| AXEL21 | AXE | Bb Airpark (TE88) | Austin-Bergstrom International Airport (KAUS) | 2026-05-14 00:56 UTC | 2026-05-14 01:25 UTC | 28m |
| NPN | NPN | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-05-14 00:56 UTC | 2026-05-14 01:23 UTC | 26m |
| N540AW |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-05-14 01:15 UTC | 2026-05-14 01:19 UTC | 4m |
| HTC | HTC | Albury Airport (YMAY) | Holbrook Airport (YHBK) | 2026-05-14 01:01 UTC | 2026-05-14 01:16 UTC | 15m |
| FFT3453 | FFT | Laguardia Airport (KLGA) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-05-13 23:22 UTC | 2026-05-14 01:15 UTC | 1h 53m |
| AAL3198 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Okc Will Rogers International Airport (KOKC) | 2026-05-14 00:38 UTC | 2026-05-14 01:15 UTC | 37m |
| FD467 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-14 00:41 UTC | 2026-05-14 01:15 UTC | 34m |
| N464KB |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-05-14 00:43 UTC | 2026-05-14 01:13 UTC | 30m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-05-14 01:00 UTC | 2026-05-14 01:12 UTC | 11m |
| EJA571 | EJA | Salt Lake City International Airport (KSLC) | North Las Vegas Airport (KVGT) | 2026-05-14 00:15 UTC | 2026-05-14 01:12 UTC | 56m |
| ATN3352 | ATN | Seattle-Tacoma International Airport (KSEA) | Denver International Airport (KDEN) | 2026-05-13 23:05 UTC | 2026-05-14 01:11 UTC | 2h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
