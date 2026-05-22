# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_05:18:43_UTC-green)

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

**Latest saved flight:** 2026-05-22 05:18:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 05:18:43 UTC

- **91,037** saved flights
- **32,374** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,037** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,122,600.7 tonnes** estimated CO2 emissions
- **65,078,300 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3875 |
| 2 | SkyWest Airlines | 3374 |
| 3 | IndiGo | 1905 |
| 4 | EJA | 1726 |
| 5 | American Airlines | 1388 |
| 6 | Southwest Airlines | 1321 |
| 7 | ENY | 1123 |
| 8 | Lufthansa | 1119 |
| 9 | Delta Air Lines | 997 |
| 10 | Vueling | 863 |
| 11 | LATAM Airlines | 817 |
| 12 | AXM | 803 |
| 13 | WIF | 795 |
| 14 | AZU | 721 |
| 15 | Swiss International | 690 |
| 16 | LXJ | 685 |
| 17 | All Nippon Airways | 683 |
| 18 | Alaska Airlines | 644 |
| 19 | QLK | 644 |
| 20 | easyJet | 592 |
| 21 | EJU | 583 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 557 |
| 24 | VIV | 540 |
| 25 | Air France | 532 |
| 26 | Japan Airlines | 483 |
| 27 | CXK | 479 |
| 28 | MXY | 469 |
| 29 | AXB | 463 |
| 30 | AIQ | 440 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 75139 |
| 2 | 🇪🇸 ES | 6432 |
| 3 | 🇮🇳 IN | 5990 |
| 4 | 🇦🇺 AU | 5684 |
| 5 | 🇩🇪 DE | 5004 |
| 6 | 🇧🇷 BR | 4981 |
| 7 | 🇮🇹 IT | 4980 |
| 8 | 🇨🇦 CA | 4584 |
| 9 | 🇯🇵 JP | 4430 |
| 10 | 🇬🇧 GB | 3877 |
| 11 | 🇫🇷 FR | 3644 |
| 12 | 🇨🇴 CO | 3139 |
| 13 | 🇲🇽 MX | 2806 |
| 14 | 🇬🇷 GR | 2610 |
| 15 | 🇳🇴 NO | 2538 |
| 16 | 🇨🇭 CH | 2384 |
| 17 | 🇲🇾 MY | 2022 |
| 18 | 🇹🇷 TR | 1657 |
| 19 | 🇿🇦 ZA | 1647 |
| 20 | 🇳🇿 NZ | 1571 |
| 21 | 🇹🇭 TH | 1543 |
| 22 | 🇵🇱 PL | 1489 |
| 23 | 🇰🇷 KR | 1444 |
| 24 | 🇵🇭 PH | 1395 |
| 25 | 🇬🇹 GT | 1361 |
| 26 | 🇲🇦 MA | 1048 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 920 |
| 29 | 🇳🇱 NL | 919 |
| 30 | 🇭🇷 HR | 824 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1986 |
| 2 | Denver International Airport |  | US | 1527 |
| 3 | Tokyo International Airport |  | JP | 1477 |
| 4 | Indira Gandhi International Airport |  | IN | 1299 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1227 |
| 6 | Harry Reid International Airport |  | US | 1167 |
| 7 | Frankfurt am Main International Airport |  | DE | 1129 |
| 8 | Guaymaral Airport |  | CO | 1083 |
| 9 | Zurich Airport |  | CH | 1073 |
| 10 | La Aurora Airport |  | GT | 1040 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1000 |
| 13 | El Dorado International Airport |  | CO | 993 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 921 |
| 15 | Chicago O'Hare International Airport |  | US | 876 |
| 16 | Madrid Barajas International Airport |  | ES | 824 |
| 17 | Kuala Lumpur International Airport |  | MY | 800 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 774 |
| 19 | Salt Lake City International Airport |  | US | 766 |
| 20 | Capua Airport |  | IT | 761 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 739 |
| 22 | Malpensa International Airport |  | IT | 730 |
| 23 | Bengaluru International Airport |  | IN | 719 |
| 24 | Charles de Gaulle International Airport |  | FR | 709 |
| 25 | Charlotte/Douglas International Airport |  | US | 702 |
| 26 | Congonhas Airport |  | BR | 695 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 662 |
| 29 | Ninoy Aquino International Airport |  | PH | 639 |
| 30 | Barcelona International Airport |  | ES | 611 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 603 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 596 |
| 34 | Vitoria/Foronda Airport |  | ES | 574 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 574 |
| 36 | Don Mueang International Airport |  | TH | 567 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 38 | Amsterdam Airport Schiphol |  | NL | 564 |
| 39 | Calgary International Airport |  | CA | 543 |
| 40 | O. R. Tambo International Airport |  | ZA | 521 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 443 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 237 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 234 | 1h 26m | 910 km | 3,672.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 210 | 1h 10m | 770 km | 2,789.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 197 | 19m | 165 km | 560.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 149 | 21m | 99 km | 255.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 133 | 27m | 152 km | 347.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 131 | 14m | 154 km | 347.1 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 117 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 117 | 18m | 144 km | 291.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 9HFAE |  | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-05-22 04:36 UTC | 2026-05-22 05:18 UTC | 42m |
| CPA509 | Cathay Pacific | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-05-22 01:02 UTC | 2026-05-22 05:18 UTC | 4h 15m |
| N774LK |  | El Paso International Airport (KELP) | Casas Adobes Airpark (NM69) | 2026-05-22 04:46 UTC | 2026-05-22 05:15 UTC | 29m |
| JYRJK | JYR | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-05-22 04:53 UTC | 2026-05-22 05:10 UTC | 17m |
| IGO017 | IndiGo | Juhu Aerodrome (VAJJ) | Queen Alia International Airport (OJAI) | 2026-05-21 21:31 UTC | 2026-05-22 05:08 UTC | 7h 36m |
| KF52 |  | Seoul Air Base (RKSM) | G 417 Airport (RK34) | 2026-05-22 04:51 UTC | 2026-05-22 05:06 UTC | 15m |
| N108RF |  | 7FL3 (7FL3) | 7FL3 (7FL3) | 2026-05-22 04:59 UTC | 2026-05-22 05:02 UTC | 2m |
| FHVYC | FHV | Valenciennes-Denain Airport (LFAV) | Brussels Airport (EBBR) | 2026-05-22 04:41 UTC | 2026-05-22 04:59 UTC | 17m |
| ZJA | ZJA | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-05-22 04:18 UTC | 2026-05-22 04:47 UTC | 29m |
| TGW550 | TGW | Singapore Changi International Airport (WSSS) | Wattay International Airport (VLVT) | 2026-05-22 02:19 UTC | 2026-05-22 04:47 UTC | 2h 27m |
| AIQ3923 | AIQ | Don Mueang International Airport (VTBD) | Tak Airport (VTPT) | 2026-05-22 04:14 UTC | 2026-05-22 04:45 UTC | 31m |
| WIF6PC | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-22 04:32 UTC | 2026-05-22 04:42 UTC | 10m |
| UBG105 | UBG | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-05-22 04:16 UTC | 2026-05-22 04:41 UTC | 25m |
| TGZ723 | TGZ | Tbilisi International Airport (UGTB) | Gyumri Shirak Airport (UDSG) | 2026-05-22 04:25 UTC | 2026-05-22 04:41 UTC | 16m |
| RJA408 | Royal Jordanian | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-22 04:35 UTC | 2026-05-22 04:41 UTC | 6m |
| AEE352 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-05-22 04:21 UTC | 2026-05-22 04:41 UTC | 19m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-05-22 04:17 UTC | 2026-05-22 04:36 UTC | 19m |
| OCN4EK | OCN | Frankfurt am Main International Airport (EDDF) | Zemunik Airport (LDZD) | 2026-05-22 03:30 UTC | 2026-05-22 04:34 UTC | 1h 3m |
| AXM6016 | AXM | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 2026-05-22 04:18 UTC | 2026-05-22 04:32 UTC | 14m |
| APG6229 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-22 04:08 UTC | 2026-05-22 04:32 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
