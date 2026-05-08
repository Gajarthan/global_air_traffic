# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_08:47:24_UTC-green)

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

**Latest saved flight:** 2026-05-08 08:47:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 08:47:24 UTC

- **72,943** saved flights
- **27,041** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,943** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **899,264.2 tonnes** estimated CO2 emissions
- **52,131,258 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3135 |
| 2 | SkyWest Airlines | 2714 |
| 3 | IndiGo | 1648 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 940 |
| 8 | ENY | 915 |
| 9 | Vueling | 713 |
| 10 | AXM | 692 |
| 11 | LATAM Airlines | 677 |
| 12 | WIF | 627 |
| 13 | Delta Air Lines | 619 |
| 14 | All Nippon Airways | 602 |
| 15 | AZU | 585 |
| 16 | QLK | 570 |
| 17 | Swiss International | 556 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 484 |
| 21 | EJU | 470 |
| 22 | AEE | 467 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 433 |
| 26 | Air France | 424 |
| 27 | AXB | 406 |
| 28 | CXK | 368 |
| 29 | AIQ | 364 |
| 30 | United Airlines | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58420 |
| 2 | 🇪🇸 ES | 5286 |
| 3 | 🇮🇳 IN | 5179 |
| 4 | 🇦🇺 AU | 4887 |
| 5 | 🇧🇷 BR | 4074 |
| 6 | 🇩🇪 DE | 4057 |
| 7 | 🇮🇹 IT | 3997 |
| 8 | 🇯🇵 JP | 3863 |
| 9 | 🇨🇦 CA | 3639 |
| 10 | 🇬🇧 GB | 3132 |
| 11 | 🇫🇷 FR | 2872 |
| 12 | 🇨🇴 CO | 2679 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2154 |
| 15 | 🇳🇴 NO | 2025 |
| 16 | 🇨🇭 CH | 1982 |
| 17 | 🇲🇾 MY | 1729 |
| 18 | 🇿🇦 ZA | 1427 |
| 19 | 🇳🇿 NZ | 1328 |
| 20 | 🇹🇷 TR | 1307 |
| 21 | 🇹🇭 TH | 1305 |
| 22 | 🇵🇱 PL | 1214 |
| 23 | 🇵🇭 PH | 1196 |
| 24 | 🇬🇹 GT | 1147 |
| 25 | 🇰🇷 KR | 1143 |
| 26 | 🇲🇦 MA | 868 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 776 |
| 29 | 🇳🇱 NL | 759 |
| 30 | 🇧🇸 BS | 611 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1298 |
| 3 | Denver International Airport |  | US | 1218 |
| 4 | Indira Gandhi International Airport |  | IN | 1093 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1054 |
| 6 | Frankfurt am Main International Airport |  | DE | 938 |
| 7 | Harry Reid International Airport |  | US | 910 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 874 |
| 10 | Zurich Airport |  | CH | 861 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 734 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 693 |
| 16 | Madrid Barajas International Airport |  | ES | 685 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 636 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 634 |
| 20 | Bengaluru International Airport |  | IN | 633 |
| 21 | Salt Lake City International Airport |  | US | 595 |
| 22 | Congonhas Airport |  | BR | 575 |
| 23 | Charlotte/Douglas International Airport |  | US | 574 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 568 |
| 26 | Tenerife Norte Airport |  | ES | 554 |
| 27 | Ninoy Aquino International Airport |  | PH | 542 |
| 28 | Daniel K Inouye International Airport |  | US | 534 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 526 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 504 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 495 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 486 |
| 34 | Vitoria/Foronda Airport |  | ES | 478 |
| 35 | Don Mueang International Airport |  | TH | 460 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 458 |
| 37 | Amsterdam Airport Schiphol |  | NL | 452 |
| 38 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 450 |
| 39 | O. R. Tambo International Airport |  | ZA | 448 |
| 40 | Calgary International Airport |  | CA | 435 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 363 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 267 | 1h 7m | 706 km | 3,250.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 257 | 21m | 244 km | 1,082.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 217 | 24m | 225 km | 841.9 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 205 | 28m | 304 km | 1,074.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 202 | 1h 27m | 910 km | 3,169.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 174 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 162 | 26m | 275 km | 767.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 162 | 1h 12m | 770 km | 2,152.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 99 | 58m | 493 km | 842.3 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 98 | 1h 43m | 1,423 km | 2,405.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 95 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GFBPS | GFB | EG32 (EG32) | EG32 (EG32) | 2026-05-08 08:26 UTC | 2026-05-08 08:47 UTC | 20m |
| ICL984 | ICL | John F Kennedy International Airport (KJFK) | Herzliya Airport (LLHZ) | 2026-05-07 23:04 UTC | 2026-05-08 08:35 UTC | 9h 31m |
| ODSY02 | ODS | RAAF Base Richmond (YSRI) | RAAF Base Richmond (YSRI) | 2026-05-08 08:09 UTC | 2026-05-08 08:26 UTC | 17m |
| SWT7882 | SWT | Palma De Mallorca Airport (LEPA) | Menorca Airport (LEMH) | 2026-05-08 08:06 UTC | 2026-05-08 08:20 UTC | 13m |
| LR5184 |  | Coffs Harbour Airport (YSCH) | Wollomombi Airport (YWMM) | 2026-05-08 07:55 UTC | 2026-05-08 08:11 UTC | 15m |
| IGO612Y | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-05-08 06:18 UTC | 2026-05-08 08:11 UTC | 1h 53m |
| SFJ83 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-08 06:53 UTC | 2026-05-08 08:10 UTC | 1h 16m |
| 4XCBD |  | Megiddo Airport (LLMG) | Queen Alia International Airport (OJAI) | 2026-05-08 05:50 UTC | 2026-05-08 08:04 UTC | 2h 14m |
| AIQ3203 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-08 07:11 UTC | 2026-05-08 08:00 UTC | 49m |
| RYR7SY | Ryanair | Poznań-Ławica Airport (EPPO) | Otocac Airport (LDRO) | 2026-05-08 06:50 UTC | 2026-05-08 08:00 UTC | 1h 9m |
| DLH1100 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Burgos Airport (LEBG) | 2026-05-08 06:19 UTC | 2026-05-08 07:58 UTC | 1h 38m |
| VLG63LZ | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-05-08 07:14 UTC | 2026-05-08 07:56 UTC | 42m |
| AE930 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-05-08 07:36 UTC | 2026-05-08 07:56 UTC | 19m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Long Semado Airport (WBGD) | 2026-05-08 07:32 UTC | 2026-05-08 07:54 UTC | 22m |
| TVF46VR | TVF | Paris-Orly Airport (LFPO) | Ifrane Airport (GMFI) | 2026-05-08 05:27 UTC | 2026-05-08 07:54 UTC | 2h 27m |
| NAF298B | NAF | Gilze Rijen Air Base (EHGR) | Beverlo Air Base (EBLE) | 2026-05-08 07:36 UTC | 2026-05-08 07:54 UTC | 17m |
| IGO6375 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Ambala Air Force Station (VIAM) | 2026-05-08 03:42 UTC | 2026-05-08 07:53 UTC | 4h 10m |
| RJA109 | Royal Jordanian | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-08 07:42 UTC | 2026-05-08 07:52 UTC | 10m |
| FD515 |  | Adelaide International Airport (YPAD) | Hubert Wilkins Airstrip (YJST) | 2026-05-08 07:27 UTC | 2026-05-08 07:52 UTC | 24m |
| N581EA |  | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Casas Adobes Airpark (NM69) | 2026-05-08 07:28 UTC | 2026-05-08 07:52 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
