# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_12:52:20_UTC-green)

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

**Latest saved flight:** 2026-05-14 12:52:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 12:52:20 UTC

- **81,571** saved flights
- **29,559** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,571** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,005,139.5 tonnes** estimated CO2 emissions
- **58,268,958 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3501 |
| 2 | SkyWest Airlines | 3020 |
| 3 | IndiGo | 1795 |
| 4 | EJA | 1525 |
| 5 | American Airlines | 1255 |
| 6 | Southwest Airlines | 1190 |
| 7 | Lufthansa | 1060 |
| 8 | ENY | 1019 |
| 9 | Delta Air Lines | 894 |
| 10 | Vueling | 776 |
| 11 | AXM | 746 |
| 12 | LATAM Airlines | 742 |
| 13 | WIF | 708 |
| 14 | All Nippon Airways | 646 |
| 15 | AZU | 640 |
| 16 | Swiss International | 639 |
| 17 | QLK | 608 |
| 18 | LXJ | 592 |
| 19 | Alaska Airlines | 578 |
| 20 | easyJet | 543 |
| 21 | EJU | 526 |
| 22 | AEE | 521 |
| 23 | Cathay Pacific | 510 |
| 24 | VIV | 483 |
| 25 | Air France | 482 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 440 |
| 28 | CXK | 423 |
| 29 | AIQ | 407 |
| 30 | United Airlines | 403 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66360 |
| 2 | 🇪🇸 ES | 5802 |
| 3 | 🇮🇳 IN | 5606 |
| 4 | 🇦🇺 AU | 5260 |
| 5 | 🇩🇪 DE | 4593 |
| 6 | 🇮🇹 IT | 4515 |
| 7 | 🇧🇷 BR | 4496 |
| 8 | 🇯🇵 JP | 4171 |
| 9 | 🇨🇦 CA | 4057 |
| 10 | 🇬🇧 GB | 3493 |
| 11 | 🇫🇷 FR | 3252 |
| 12 | 🇨🇴 CO | 2722 |
| 13 | 🇲🇽 MX | 2454 |
| 14 | 🇬🇷 GR | 2382 |
| 15 | 🇳🇴 NO | 2281 |
| 16 | 🇨🇭 CH | 2196 |
| 17 | 🇲🇾 MY | 1873 |
| 18 | 🇿🇦 ZA | 1544 |
| 19 | 🇹🇷 TR | 1451 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1436 |
| 22 | 🇵🇱 PL | 1359 |
| 23 | 🇵🇭 PH | 1301 |
| 24 | 🇰🇷 KR | 1251 |
| 25 | 🇬🇹 GT | 1244 |
| 26 | 🇲🇦 MA | 955 |
| 27 | 🇲🇴 MO | 937 |
| 28 | 🇲🇪 ME | 876 |
| 29 | 🇳🇱 NL | 843 |
| 30 | 🇭🇷 HR | 723 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1785 |
| 2 | Tokyo International Airport |  | JP | 1398 |
| 3 | Denver International Airport |  | US | 1367 |
| 4 | Indira Gandhi International Airport |  | IN | 1189 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1166 |
| 6 | Frankfurt am Main International Airport |  | DE | 1072 |
| 7 | Harry Reid International Airport |  | US | 1013 |
| 8 | Zurich Airport |  | CH | 977 |
| 9 | La Aurora Airport |  | GT | 939 |
| 10 | Macau International Airport |  | MO | 937 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 919 |
| 12 | Guaymaral Airport |  | CO | 914 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 791 |
| 16 | Madrid Barajas International Airport |  | ES | 748 |
| 17 | Kuala Lumpur International Airport |  | MY | 747 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 711 |
| 19 | Malpensa International Airport |  | IT | 691 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 21 | Bengaluru International Airport |  | IN | 688 |
| 22 | Salt Lake City International Airport |  | US | 673 |
| 23 | Capua Airport |  | IT | 665 |
| 24 | Charles de Gaulle International Airport |  | FR | 641 |
| 25 | Congonhas Airport |  | BR | 636 |
| 26 | Charlotte/Douglas International Airport |  | US | 634 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Ninoy Aquino International Airport |  | PH | 595 |
| 29 | Daniel K Inouye International Airport |  | US | 590 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 587 |
| 31 | Barcelona International Airport |  | ES | 547 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 546 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 542 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 528 |
| 35 | Don Mueang International Airport |  | TH | 517 |
| 36 | Vitoria/Foronda Airport |  | ES | 513 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 510 |
| 38 | Amsterdam Airport Schiphol |  | NL | 507 |
| 39 | O. R. Tambo International Airport |  | ZA | 489 |
| 40 | Calgary International Airport |  | CA | 481 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 294 | 21m | 244 km | 1,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 220 | 1h 26m | 910 km | 3,452.3 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 208 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 195 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 188 | 19m | 165 km | 534.8 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 186 | 1h 11m | 770 km | 2,470.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 121 | 27m | 215 km | 448.1 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 120 | 20m | 147 km | 303.7 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 118 | 14m | 154 km | 312.7 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 102 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MFX7530 | MFX | Indira Gandhi International Airport (VIDP) | Hissar Airport (VIHR) | 2026-05-14 12:34 UTC | 2026-05-14 12:52 UTC | 17m |
| VTEJZ | VTE | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-05-14 12:19 UTC | 2026-05-14 12:52 UTC | 32m |
| N7900T |  | SOLAG - Sol e Lua Aviacao Agricola Airport (SICO) | SOLAG - Sol e Lua Aviacao Agricola Airport (SICO) | 2026-05-14 11:43 UTC | 2026-05-14 12:48 UTC | 1h 4m |
| CCA117 | Air China | Quanzhou Airport (ZSQZ) | Macau International Airport (VMMC) | 2026-05-13 12:56 UTC | 2026-05-14 12:34 UTC | 23h 37m |
| N410RW |  | New Century Aircenter Airport (KIXD) | Newton-City-County Airport (KEWK) | 2026-05-14 11:47 UTC | 2026-05-14 12:33 UTC | 46m |
| N813MR |  | Palatka Municipal/Lt Kay Larkin Field (K28J) | Palatka Municipal/Lt Kay Larkin Field (K28J) | 2026-05-14 12:28 UTC | 2026-05-14 12:29 UTC | 0m |
| N3899Q |  | Mid-Carolina Regional Airport (KRUQ) | Mid-Carolina Regional Airport (KRUQ) | 2026-05-14 12:29 UTC | 2026-05-14 12:29 UTC | 0m |
| FLC76 | FLC | Reno/Tahoe International Airport (KRNO) | Yerington Municipal Airport (KO43) | 2026-05-14 12:15 UTC | 2026-05-14 12:26 UTC | 10m |
| ETD7BR | Etihad Airways | Frankfurt am Main International Airport (EDDF) | Queen Alia International Airport (OJAI) | 2026-05-14 09:18 UTC | 2026-05-14 12:23 UTC | 3h 5m |
| ZSSNN | ZSS | Fisantekraal Airport (FAFK) | Paarl East Airport (FAPU) | 2026-05-14 11:54 UTC | 2026-05-14 12:16 UTC | 21m |
| N301MT |  | Lovell Field (KCHA) | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | 2026-05-14 11:24 UTC | 2026-05-14 12:16 UTC | 52m |
| ETD8JZ | Etihad Airways | Václav Havel Airport (LKPR) | Queen Alia International Airport (OJAI) | 2026-05-14 09:21 UTC | 2026-05-14 12:15 UTC | 2h 53m |
| N3899Q |  | Concord-Padgett Regional Airport (KJQF) | Bradley Field (NC29) | 2026-05-14 11:57 UTC | 2026-05-14 12:09 UTC | 12m |
| N109EJ |  | Clarke County Airport (K23M) | Clarke County Airport (K23M) | 2026-05-14 11:58 UTC | 2026-05-14 12:05 UTC | 7m |
| FDB574 | flydubai | Tribhuvan International Airport (VNKT) | Queen Alia International Airport (OJAI) | 2026-05-13 17:52 UTC | 2026-05-14 12:04 UTC | 18h 12m |
| HFA853 | HFA | Haifa International Airport (LLHA) | Queen Alia International Airport (OJAI) | 2026-05-14 11:40 UTC | 2026-05-14 12:03 UTC | 22m |
| ZSHIE | ZSH | Ysterplaat Air Force Base (FAYP) | Fisantekraal Airport (FAFK) | 2026-05-14 11:04 UTC | 2026-05-14 12:00 UTC | 56m |
| AUB1747 | AUB | Auburn University Regional Airport (KAUO) | Auburn University Regional Airport (KAUO) | 2026-05-14 11:37 UTC | 2026-05-14 11:59 UTC | 21m |
| SWR5HX | Swiss International | Zurich Airport (LSZH) | Václav Havel Airport (LKPR) | 2026-05-14 11:04 UTC | 2026-05-14 11:57 UTC | 53m |
| FYG46YN | FYG | Munster Osnabruck Airport (EDDG) | Rotterdam Airport (EHRD) | 2026-05-14 11:18 UTC | 2026-05-14 11:55 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
