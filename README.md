# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_21:40:31_UTC-green)

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

**Latest saved flight:** 2026-05-14 21:40:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 21:40:31 UTC

- **82,378** saved flights
- **29,842** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **82,378** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,013,880.2 tonnes** estimated CO2 emissions
- **58,775,663 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3531 |
| 2 | SkyWest Airlines | 3055 |
| 3 | IndiGo | 1800 |
| 4 | EJA | 1544 |
| 5 | American Airlines | 1272 |
| 6 | Southwest Airlines | 1205 |
| 7 | Lufthansa | 1062 |
| 8 | ENY | 1028 |
| 9 | Delta Air Lines | 900 |
| 10 | Vueling | 780 |
| 11 | AXM | 746 |
| 12 | LATAM Airlines | 746 |
| 13 | WIF | 716 |
| 14 | AZU | 649 |
| 15 | All Nippon Airways | 646 |
| 16 | Swiss International | 641 |
| 17 | QLK | 608 |
| 18 | LXJ | 598 |
| 19 | Alaska Airlines | 582 |
| 20 | easyJet | 546 |
| 21 | EJU | 529 |
| 22 | AEE | 524 |
| 23 | Cathay Pacific | 512 |
| 24 | VIV | 492 |
| 25 | Air France | 484 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 442 |
| 28 | CXK | 431 |
| 29 | MXY | 409 |
| 30 | United Airlines | 408 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 67299 |
| 2 | 🇪🇸 ES | 5836 |
| 3 | 🇮🇳 IN | 5625 |
| 4 | 🇦🇺 AU | 5265 |
| 5 | 🇩🇪 DE | 4615 |
| 6 | 🇮🇹 IT | 4554 |
| 7 | 🇧🇷 BR | 4552 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4106 |
| 10 | 🇬🇧 GB | 3516 |
| 11 | 🇫🇷 FR | 3274 |
| 12 | 🇨🇴 CO | 2738 |
| 13 | 🇲🇽 MX | 2498 |
| 14 | 🇬🇷 GR | 2398 |
| 15 | 🇳🇴 NO | 2308 |
| 16 | 🇨🇭 CH | 2202 |
| 17 | 🇲🇾 MY | 1874 |
| 18 | 🇿🇦 ZA | 1550 |
| 19 | 🇹🇷 TR | 1464 |
| 20 | 🇳🇿 NZ | 1442 |
| 21 | 🇹🇭 TH | 1438 |
| 22 | 🇵🇱 PL | 1372 |
| 23 | 🇵🇭 PH | 1302 |
| 24 | 🇬🇹 GT | 1256 |
| 25 | 🇰🇷 KR | 1252 |
| 26 | 🇲🇦 MA | 960 |
| 27 | 🇲🇴 MO | 943 |
| 28 | 🇲🇪 ME | 878 |
| 29 | 🇳🇱 NL | 847 |
| 30 | 🇭🇷 HR | 735 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1809 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1383 |
| 4 | Indira Gandhi International Airport |  | IN | 1193 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1172 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1024 |
| 8 | Zurich Airport |  | CH | 980 |
| 9 | La Aurora Airport |  | GT | 951 |
| 10 | Macau International Airport |  | MO | 943 |
| 11 | Guaymaral Airport |  | CO | 924 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 923 |
| 13 | El Dorado International Airport |  | CO | 881 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 827 |
| 15 | Chicago O'Hare International Airport |  | US | 798 |
| 16 | Madrid Barajas International Airport |  | ES | 753 |
| 17 | Kuala Lumpur International Airport |  | MY | 748 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 717 |
| 19 | Malpensa International Airport |  | IT | 694 |
| 20 | Bengaluru International Airport |  | IN | 691 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 22 | Salt Lake City International Airport |  | US | 679 |
| 23 | Capua Airport |  | IT | 673 |
| 24 | Charles de Gaulle International Airport |  | FR | 646 |
| 25 | Charlotte/Douglas International Airport |  | US | 642 |
| 26 | Congonhas Airport |  | BR | 639 |
| 27 | Tenerife Norte Airport |  | ES | 600 |
| 28 | Ninoy Aquino International Airport |  | PH | 596 |
| 29 | Daniel K Inouye International Airport |  | US | 596 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 552 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 552 |
| 33 | Barcelona International Airport |  | ES | 552 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 533 |
| 35 | Don Mueang International Airport |  | TH | 518 |
| 36 | Vitoria/Foronda Airport |  | ES | 517 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 517 |
| 38 | Amsterdam Airport Schiphol |  | NL | 511 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 484 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 385 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 297 | 21m | 244 km | 1,250.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 211 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 196 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 172 | 26m | 275 km | 815.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 124 | 27m | 152 km | 324.1 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 123 | 27m | 215 km | 455.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 121 | 20m | 147 km | 306.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 113 | 23m | 55 km | 107.4 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 112 | 1h 2m | 695 km | 1,342.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 104 | 13m | - | - |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 104 | 18m | 144 km | 258.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SAS2744 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | Palanga International Airport (EYPA) | 2026-05-14 21:05 UTC | 2026-05-14 21:40 UTC | 34m |
| TKR136 | TKR | Grand Junction Regional Airport (KGJT) | Sanpete County Regional Airport (K41U) | 2026-05-14 20:58 UTC | 2026-05-14 21:33 UTC | 34m |
| SLH385 | SLH | Naples Municipal Airport (KAPF) | Lincoln Airport (KLNK) | 2026-05-14 18:08 UTC | 2026-05-14 21:29 UTC | 3h 21m |
| URSA12 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-14 20:41 UTC | 2026-05-14 21:28 UTC | 47m |
| N55928 |  | Modesto City-County-Harry Sham Field (KMOD) | Modesto City-County-Harry Sham Field (KMOD) | 2026-05-14 21:24 UTC | 2026-05-14 21:26 UTC | 2m |
| XAJDM | XAJ | William P Hobby Airport (KHOU) | General Mariano Escobedo International Airport (MMMY) | 2026-05-14 20:19 UTC | 2026-05-14 21:25 UTC | 1h 5m |
| HIGH63 | HIG | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-05-14 20:28 UTC | 2026-05-14 21:19 UTC | 51m |
| N158NS |  | Pittsburgh International Airport (KPIT) | Witham Field (KSUA) | 2026-05-14 19:26 UTC | 2026-05-14 21:18 UTC | 1h 52m |
| N540M |  | Allegheny County Airport (KAGC) | Akron-Canton Regional Airport (KCAK) | 2026-05-14 20:56 UTC | 2026-05-14 21:17 UTC | 20m |
| XSR324 | XSR | Dallas Love Field (KDAL) | Colonel James Jabara Airport (KAAO) | 2026-05-14 20:19 UTC | 2026-05-14 21:13 UTC | 53m |
| N155SH |  | John C Tune Airport (KJWN) | Lebanon Municipal Airport (KM54) | 2026-05-14 20:52 UTC | 2026-05-14 21:12 UTC | 20m |
| N54KW |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-05-14 21:07 UTC | 2026-05-14 21:10 UTC | 2m |
| TKR137 | TKR | Grand Junction Regional Airport (KGJT) | K43U (K43U) | 2026-05-14 20:49 UTC | 2026-05-14 21:09 UTC | 20m |
| 00NIKE40 |  | NM28 (NM28) | Stallion Army Air Field (K95E) | 2026-05-14 20:55 UTC | 2026-05-14 21:09 UTC | 13m |
| POL25 | POL | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-05-14 20:26 UTC | 2026-05-14 21:07 UTC | 41m |
| N493LG |  | Usaf Academy Davis Airfield (KAFF) | Fremont County Airport (K1V6) | 2026-05-14 20:39 UTC | 2026-05-14 21:05 UTC | 26m |
| N595DL |  | KM33 (KM33) | KM33 (KM33) | 2026-05-14 20:31 UTC | 2026-05-14 21:05 UTC | 34m |
| N445B |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-05-14 20:29 UTC | 2026-05-14 21:05 UTC | 35m |
| ETD2NPA | Etihad Airways | Manchester Airport (EGCC) | Queen Alia International Airport (OJAI) | 2026-05-14 17:01 UTC | 2026-05-14 21:03 UTC | 4h 2m |
| MWH1 | MWH | Bellingham International Airport (KBLI) | Rainbow Ranch Airport (ID87) | 2026-05-14 19:34 UTC | 2026-05-14 21:01 UTC | 1h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
