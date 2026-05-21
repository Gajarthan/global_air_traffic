# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_23:29:35_UTC-green)

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

**Latest saved flight:** 2026-05-21 23:29:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-21 23:29:35 UTC

- **90,837** saved flights
- **32,332** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **90,837** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,120,952.9 tonnes** estimated CO2 emissions
- **64,982,777 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3875 |
| 2 | SkyWest Airlines | 3366 |
| 3 | IndiGo | 1902 |
| 4 | EJA | 1724 |
| 5 | American Airlines | 1385 |
| 6 | Southwest Airlines | 1316 |
| 7 | ENY | 1121 |
| 8 | Lufthansa | 1119 |
| 9 | Delta Air Lines | 996 |
| 10 | Vueling | 863 |
| 11 | LATAM Airlines | 817 |
| 12 | AXM | 800 |
| 13 | WIF | 794 |
| 14 | AZU | 721 |
| 15 | Swiss International | 690 |
| 16 | LXJ | 685 |
| 17 | All Nippon Airways | 679 |
| 18 | Alaska Airlines | 643 |
| 19 | QLK | 641 |
| 20 | easyJet | 592 |
| 21 | EJU | 583 |
| 22 | Cathay Pacific | 579 |
| 23 | AEE | 556 |
| 24 | VIV | 539 |
| 25 | Air France | 532 |
| 26 | Japan Airlines | 482 |
| 27 | CXK | 479 |
| 28 | MXY | 469 |
| 29 | AXB | 463 |
| 30 | AIQ | 438 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 74969 |
| 2 | 🇪🇸 ES | 6430 |
| 3 | 🇮🇳 IN | 5983 |
| 4 | 🇦🇺 AU | 5628 |
| 5 | 🇩🇪 DE | 5002 |
| 6 | 🇧🇷 BR | 4981 |
| 7 | 🇮🇹 IT | 4980 |
| 8 | 🇨🇦 CA | 4571 |
| 9 | 🇯🇵 JP | 4400 |
| 10 | 🇬🇧 GB | 3877 |
| 11 | 🇫🇷 FR | 3643 |
| 12 | 🇨🇴 CO | 3135 |
| 13 | 🇲🇽 MX | 2804 |
| 14 | 🇬🇷 GR | 2608 |
| 15 | 🇳🇴 NO | 2537 |
| 16 | 🇨🇭 CH | 2384 |
| 17 | 🇲🇾 MY | 2011 |
| 18 | 🇹🇷 TR | 1654 |
| 19 | 🇿🇦 ZA | 1647 |
| 20 | 🇳🇿 NZ | 1555 |
| 21 | 🇹🇭 TH | 1538 |
| 22 | 🇵🇱 PL | 1489 |
| 23 | 🇰🇷 KR | 1425 |
| 24 | 🇵🇭 PH | 1387 |
| 25 | 🇬🇹 GT | 1359 |
| 26 | 🇲🇦 MA | 1047 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇲🇪 ME | 920 |
| 29 | 🇳🇱 NL | 919 |
| 30 | 🇭🇷 HR | 823 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1983 |
| 2 | Denver International Airport |  | US | 1524 |
| 3 | Tokyo International Airport |  | JP | 1468 |
| 4 | Indira Gandhi International Airport |  | IN | 1297 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1226 |
| 6 | Harry Reid International Airport |  | US | 1164 |
| 7 | Frankfurt am Main International Airport |  | DE | 1128 |
| 8 | Guaymaral Airport |  | CO | 1083 |
| 9 | Zurich Airport |  | CH | 1073 |
| 10 | La Aurora Airport |  | GT | 1039 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1000 |
| 13 | El Dorado International Airport |  | CO | 991 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 920 |
| 15 | Chicago O'Hare International Airport |  | US | 876 |
| 16 | Madrid Barajas International Airport |  | ES | 824 |
| 17 | Kuala Lumpur International Airport |  | MY | 796 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 774 |
| 19 | Salt Lake City International Airport |  | US | 762 |
| 20 | Capua Airport |  | IT | 761 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 734 |
| 22 | Malpensa International Airport |  | IT | 730 |
| 23 | Bengaluru International Airport |  | IN | 718 |
| 24 | Charles de Gaulle International Airport |  | FR | 709 |
| 25 | Charlotte/Douglas International Airport |  | US | 701 |
| 26 | Congonhas Airport |  | BR | 695 |
| 27 | Daniel K Inouye International Airport |  | US | 663 |
| 28 | Tenerife Norte Airport |  | ES | 662 |
| 29 | Ninoy Aquino International Airport |  | PH | 637 |
| 30 | Barcelona International Airport |  | ES | 611 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 602 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 593 |
| 34 | Vitoria/Foronda Airport |  | ES | 574 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 574 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Don Mueang International Airport |  | TH | 565 |
| 38 | Amsterdam Airport Schiphol |  | NL | 564 |
| 39 | Calgary International Airport |  | CA | 541 |
| 40 | O. R. Tambo International Airport |  | ZA | 521 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 443 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 337 | 21m | 244 km | 1,419.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 249 | 24m | 225 km | 966.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 237 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 232 | 1h 26m | 910 km | 3,640.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 231 | 28m | 304 km | 1,211.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 208 | 1h 10m | 770 km | 2,763.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 196 | 19m | 165 km | 557.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 133 | 27m | 152 km | 347.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 129 | 14m | 154 km | 341.8 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 117 | 18m | 144 km | 291.0 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFTOW | CFT | Viking Airport (CEE8) | Calgary International Airport (CYYC) | 2026-05-21 22:49 UTC | 2026-05-21 23:29 UTC | 40m |
| N865PC |  | Asheville Regional Airport (KAVL) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-05-21 21:55 UTC | 2026-05-21 23:23 UTC | 1h 28m |
| N478DC |  | Oakland County International Airport (KPTK) | Dupont/Lapeer Airport (KD95) | 2026-05-21 22:09 UTC | 2026-05-21 23:23 UTC | 1h 13m |
| N96KS |  | Nevada County Airport (KGOO) | Rogers Field (KO05) | 2026-05-21 22:53 UTC | 2026-05-21 23:19 UTC | 25m |
| N5407F |  | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-05-21 22:44 UTC | 2026-05-21 23:13 UTC | 28m |
| N534Y |  | Cameron Park Airport (KO61) | Cameron Park Airport (KO61) | 2026-05-21 23:09 UTC | 2026-05-21 23:11 UTC | 2m |
| N642RG |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-21 22:01 UTC | 2026-05-21 23:10 UTC | 1h 8m |
| YTU | YTU | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-05-21 21:51 UTC | 2026-05-21 23:03 UTC | 1h 12m |
| N526SH |  | Cotulla-La Salle County Airport (KCOT) | Laredo International Airport (KLRD) | 2026-05-21 22:04 UTC | 2026-05-21 22:59 UTC | 54m |
| N362Q |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-21 21:46 UTC | 2026-05-21 22:57 UTC | 1h 10m |
| PDU57 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-05-21 21:42 UTC | 2026-05-21 22:57 UTC | 1h 15m |
| N175U |  | Easton/Newnam Field (KESN) | St Pete-Clearwater International Airport (KPIE) | 2026-05-21 20:44 UTC | 2026-05-21 22:55 UTC | 2h 10m |
| N977DM |  | Teterboro Airport (KTEB) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-21 22:06 UTC | 2026-05-21 22:54 UTC | 47m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-21 22:32 UTC | 2026-05-21 22:54 UTC | 21m |
| N9425H |  | Dupage Airport (KDPA) | Jack W Watson Airport (0IL9) | 2026-05-21 22:32 UTC | 2026-05-21 22:47 UTC | 15m |
| EDG471 | EDG | Des Moines International Airport (KDSM) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-21 19:33 UTC | 2026-05-21 22:46 UTC | 3h 13m |
| FXC33 | FXC | Laguardia Airport (KLGA) | Francis S Gabreski Airport (KFOK) | 2026-05-21 22:14 UTC | 2026-05-21 22:44 UTC | 30m |
| QLK1790 | QLK | Adelaide International Airport (YPAD) | Melbourne International Airport (YMML) | 2026-05-21 21:43 UTC | 2026-05-21 22:41 UTC | 58m |
| N27DX |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-05-21 22:07 UTC | 2026-05-21 22:40 UTC | 32m |
| N5411A |  | Soldotna Airport (PASX) | Sparrevohn Lrrs Airport (PASV) | 2026-05-21 21:55 UTC | 2026-05-21 22:39 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
