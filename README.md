# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_08:25:15_UTC-green)

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

**Latest saved flight:** 2026-05-14 08:25:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 08:25:15 UTC

- **81,365** saved flights
- **29,504** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,365** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,002,288.2 tonnes** estimated CO2 emissions
- **58,103,663 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3485 |
| 2 | SkyWest Airlines | 3020 |
| 3 | IndiGo | 1786 |
| 4 | EJA | 1525 |
| 5 | American Airlines | 1255 |
| 6 | Southwest Airlines | 1190 |
| 7 | Lufthansa | 1056 |
| 8 | ENY | 1019 |
| 9 | Delta Air Lines | 894 |
| 10 | Vueling | 773 |
| 11 | AXM | 742 |
| 12 | LATAM Airlines | 741 |
| 13 | WIF | 702 |
| 14 | All Nippon Airways | 645 |
| 15 | AZU | 640 |
| 16 | Swiss International | 632 |
| 17 | QLK | 608 |
| 18 | LXJ | 592 |
| 19 | Alaska Airlines | 578 |
| 20 | easyJet | 540 |
| 21 | EJU | 523 |
| 22 | AEE | 519 |
| 23 | Cathay Pacific | 509 |
| 24 | VIV | 483 |
| 25 | Air France | 479 |
| 26 | Japan Airlines | 462 |
| 27 | AXB | 439 |
| 28 | CXK | 423 |
| 29 | AIQ | 405 |
| 30 | United Airlines | 403 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66305 |
| 2 | 🇪🇸 ES | 5776 |
| 3 | 🇮🇳 IN | 5580 |
| 4 | 🇦🇺 AU | 5248 |
| 5 | 🇩🇪 DE | 4572 |
| 6 | 🇮🇹 IT | 4494 |
| 7 | 🇧🇷 BR | 4488 |
| 8 | 🇯🇵 JP | 4156 |
| 9 | 🇨🇦 CA | 4049 |
| 10 | 🇬🇧 GB | 3478 |
| 11 | 🇫🇷 FR | 3236 |
| 12 | 🇨🇴 CO | 2721 |
| 13 | 🇲🇽 MX | 2454 |
| 14 | 🇬🇷 GR | 2372 |
| 15 | 🇳🇴 NO | 2265 |
| 16 | 🇨🇭 CH | 2185 |
| 17 | 🇲🇾 MY | 1860 |
| 18 | 🇿🇦 ZA | 1534 |
| 19 | 🇹🇷 TR | 1448 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1432 |
| 22 | 🇵🇱 PL | 1351 |
| 23 | 🇵🇭 PH | 1294 |
| 24 | 🇰🇷 KR | 1245 |
| 25 | 🇬🇹 GT | 1244 |
| 26 | 🇲🇦 MA | 951 |
| 27 | 🇲🇴 MO | 934 |
| 28 | 🇲🇪 ME | 869 |
| 29 | 🇳🇱 NL | 837 |
| 30 | 🇭🇷 HR | 719 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1785 |
| 2 | Tokyo International Airport |  | JP | 1391 |
| 3 | Denver International Airport |  | US | 1367 |
| 4 | Indira Gandhi International Airport |  | IN | 1181 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1162 |
| 6 | Frankfurt am Main International Airport |  | DE | 1067 |
| 7 | Harry Reid International Airport |  | US | 1011 |
| 8 | Zurich Airport |  | CH | 969 |
| 9 | La Aurora Airport |  | GT | 939 |
| 10 | Macau International Airport |  | MO | 934 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 919 |
| 12 | Guaymaral Airport |  | CO | 913 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 791 |
| 16 | Madrid Barajas International Airport |  | ES | 745 |
| 17 | Kuala Lumpur International Airport |  | MY | 742 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 711 |
| 19 | Malpensa International Airport |  | IT | 689 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 688 |
| 21 | Bengaluru International Airport |  | IN | 687 |
| 22 | Salt Lake City International Airport |  | US | 673 |
| 23 | Capua Airport |  | IT | 662 |
| 24 | Charles de Gaulle International Airport |  | FR | 637 |
| 25 | Charlotte/Douglas International Airport |  | US | 634 |
| 26 | Congonhas Airport |  | BR | 633 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Ninoy Aquino International Airport |  | PH | 591 |
| 29 | Daniel K Inouye International Airport |  | US | 590 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 583 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 545 |
| 32 | Barcelona International Airport |  | ES | 544 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 542 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 526 |
| 35 | Don Mueang International Airport |  | TH | 515 |
| 36 | Vitoria/Foronda Airport |  | ES | 513 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 510 |
| 38 | Amsterdam Airport Schiphol |  | NL | 506 |
| 39 | O. R. Tambo International Airport |  | ZA | 487 |
| 40 | Calgary International Airport |  | CA | 480 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 294 | 21m | 244 km | 1,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 272 | 1h 8m | 706 km | 3,311.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 218 | 28m | 304 km | 1,142.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 218 | 1h 27m | 910 km | 3,420.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 208 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 194 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 187 | 19m | 165 km | 531.9 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 184 | 1h 11m | 770 km | 2,444.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 120 | 27m | 215 km | 444.4 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 118 | 20m | 147 km | 298.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 116 | 14m | 154 km | 307.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 101 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HGB309 | HGB | Fukuoka Airport (RJFF) | Chek Lap Kok International Airport (VHHH) | 2026-05-14 05:17 UTC | 2026-05-14 08:25 UTC | 3h 7m |
| CONDR11 | CON | Getafe Air Base (LEGT) | Vigo Airport (LEVX) | 2026-05-14 07:09 UTC | 2026-05-14 08:06 UTC | 57m |
| ZSOKA | ZSO | O. R. Tambo International Airport (FAOR) | Hartebeespoortdam Airport (FAHB) | 2026-05-14 07:33 UTC | 2026-05-14 08:03 UTC | 30m |
| FJKZH | FJK | Saint-Cyr-l'Ecole Airport (LFPZ) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-05-14 07:59 UTC | 2026-05-14 08:02 UTC | 3m |
| BML | BML | Corowa Airport (YCOR) | Albury Airport (YMAY) | 2026-05-14 07:38 UTC | 2026-05-14 07:56 UTC | 18m |
| HTY204 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-05-14 07:27 UTC | 2026-05-14 07:54 UTC | 26m |
| BBC371 | BBC | VGZR (VGZR) | Tribhuvan International Airport (VNKT) | 2026-05-14 06:41 UTC | 2026-05-14 07:53 UTC | 1h 12m |
| N490LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-14 05:15 UTC | 2026-05-14 07:53 UTC | 2h 37m |
| OEFAF | OEF | Linz Airport (LOWL) | Mayerhofen Airport (LOKM) | 2026-05-14 07:35 UTC | 2026-05-14 07:52 UTC | 16m |
| BASIC11 | BAS | Pardubice Airport (LKPD) | Nove Mesto Airport (LKNM) | 2026-05-14 07:18 UTC | 2026-05-14 07:46 UTC | 28m |
| RYR59WU | Ryanair | Dublin Airport (EIDW) | London Luton Airport (EGGW) | 2026-05-14 06:57 UTC | 2026-05-14 07:44 UTC | 46m |
| ANE74KE | ANE | Madrid Barajas International Airport (LEMD) | Garray Airport (LEGY) | 2026-05-14 07:18 UTC | 2026-05-14 07:43 UTC | 25m |
| NOZ7TE | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-05-14 06:22 UTC | 2026-05-14 07:40 UTC | 1h 17m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-05-14 07:14 UTC | 2026-05-14 07:38 UTC | 24m |
| NWK2772 | NWK | Perth International Airport (YPPH) | Kalgoorlie-Boulder Airport (YPKG) | 2026-05-14 06:52 UTC | 2026-05-14 07:38 UTC | 45m |
| AIZ807 | AIZ | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-05-14 07:15 UTC | 2026-05-14 07:37 UTC | 21m |
| ELY5114 | ELY | Batumi International Airport (UGSB) | Queen Alia International Airport (OJAI) | 2026-05-14 05:44 UTC | 2026-05-14 07:36 UTC | 1h 52m |
| MNE301 | MNE | Frankfurt am Main International Airport (EDDF) | Dubrovnik Airport (LDDU) | 2026-05-14 06:10 UTC | 2026-05-14 07:35 UTC | 1h 24m |
| ANZ625 | ANZ | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-05-14 06:19 UTC | 2026-05-14 07:35 UTC | 1h 15m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-14 07:16 UTC | 2026-05-14 07:33 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
