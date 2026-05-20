# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_22:51:03_UTC-green)

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

**Latest saved flight:** 2026-05-20 22:51:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-20 22:51:03 UTC

- **89,503** saved flights
- **31,931** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **89,503** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,107,774.7 tonnes** estimated CO2 emissions
- **64,218,822 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3839 |
| 2 | SkyWest Airlines | 3325 |
| 3 | IndiGo | 1887 |
| 4 | EJA | 1692 |
| 5 | American Airlines | 1366 |
| 6 | Southwest Airlines | 1297 |
| 7 | Lufthansa | 1116 |
| 8 | ENY | 1105 |
| 9 | Delta Air Lines | 980 |
| 10 | Vueling | 853 |
| 11 | LATAM Airlines | 806 |
| 12 | AXM | 790 |
| 13 | WIF | 776 |
| 14 | AZU | 712 |
| 15 | Swiss International | 688 |
| 16 | All Nippon Airways | 671 |
| 17 | LXJ | 667 |
| 18 | Alaska Airlines | 635 |
| 19 | QLK | 633 |
| 20 | easyJet | 589 |
| 21 | Cathay Pacific | 578 |
| 22 | EJU | 576 |
| 23 | AEE | 552 |
| 24 | VIV | 535 |
| 25 | Air France | 524 |
| 26 | Japan Airlines | 480 |
| 27 | CXK | 469 |
| 28 | AXB | 459 |
| 29 | MXY | 455 |
| 30 | AIQ | 433 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 73676 |
| 2 | 🇪🇸 ES | 6349 |
| 3 | 🇮🇳 IN | 5916 |
| 4 | 🇦🇺 AU | 5557 |
| 5 | 🇩🇪 DE | 4955 |
| 6 | 🇮🇹 IT | 4955 |
| 7 | 🇧🇷 BR | 4917 |
| 8 | 🇨🇦 CA | 4488 |
| 9 | 🇯🇵 JP | 4367 |
| 10 | 🇬🇧 GB | 3819 |
| 11 | 🇫🇷 FR | 3592 |
| 12 | 🇨🇴 CO | 3075 |
| 13 | 🇲🇽 MX | 2774 |
| 14 | 🇬🇷 GR | 2582 |
| 15 | 🇳🇴 NO | 2487 |
| 16 | 🇨🇭 CH | 2355 |
| 17 | 🇲🇾 MY | 1984 |
| 18 | 🇿🇦 ZA | 1641 |
| 19 | 🇹🇷 TR | 1628 |
| 20 | 🇳🇿 NZ | 1544 |
| 21 | 🇹🇭 TH | 1523 |
| 22 | 🇵🇱 PL | 1480 |
| 23 | 🇰🇷 KR | 1384 |
| 24 | 🇵🇭 PH | 1372 |
| 25 | 🇬🇹 GT | 1339 |
| 26 | 🇲🇴 MO | 1034 |
| 27 | 🇲🇦 MA | 1032 |
| 28 | 🇲🇪 ME | 917 |
| 29 | 🇳🇱 NL | 907 |
| 30 | 🇭🇷 HR | 808 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1960 |
| 2 | Denver International Airport |  | US | 1502 |
| 3 | Tokyo International Airport |  | JP | 1456 |
| 4 | Indira Gandhi International Airport |  | IN | 1279 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1216 |
| 6 | Harry Reid International Airport |  | US | 1140 |
| 7 | Frankfurt am Main International Airport |  | DE | 1125 |
| 8 | Zurich Airport |  | CH | 1066 |
| 9 | Guaymaral Airport |  | CO | 1049 |
| 10 | Macau International Airport |  | MO | 1034 |
| 11 | La Aurora Airport |  | GT | 1019 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 992 |
| 13 | El Dorado International Airport |  | CO | 978 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 911 |
| 15 | Chicago O'Hare International Airport |  | US | 864 |
| 16 | Madrid Barajas International Airport |  | ES | 814 |
| 17 | Kuala Lumpur International Airport |  | MY | 786 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 767 |
| 19 | Capua Airport |  | IT | 761 |
| 20 | Salt Lake City International Airport |  | US | 750 |
| 21 | Malpensa International Airport |  | IT | 727 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 723 |
| 23 | Bengaluru International Airport |  | IN | 712 |
| 24 | Charles de Gaulle International Airport |  | FR | 698 |
| 25 | Congonhas Airport |  | BR | 689 |
| 26 | Charlotte/Douglas International Airport |  | US | 688 |
| 27 | Daniel K Inouye International Airport |  | US | 656 |
| 28 | Tenerife Norte Airport |  | ES | 653 |
| 29 | Ninoy Aquino International Airport |  | PH | 630 |
| 30 | Barcelona International Airport |  | ES | 602 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 599 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 588 |
| 34 | Vitoria/Foronda Airport |  | ES | 568 |
| 35 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 567 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 37 | Amsterdam Airport Schiphol |  | NL | 557 |
| 38 | Don Mueang International Airport |  | TH | 555 |
| 39 | Calgary International Airport |  | CA | 533 |
| 40 | O. R. Tambo International Airport |  | ZA | 519 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 429 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 333 | 21m | 244 km | 1,402.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 244 | 24m | 225 km | 946.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 234 | 14m | 114 km | 459.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 229 | 9m | - | - |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 228 | 28m | 304 km | 1,195.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 204 | 1h 10m | 770 km | 2,710.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 185 | 26m | 275 km | 876.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 137 | 31m | 369 km | 872.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 131 | 27m | 215 km | 485.2 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 131 | 22m | 55 km | 124.5 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 126 | 14m | 154 km | 333.8 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 116 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 116 | 18m | 144 km | 288.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 109 | 1h 18m | 961 km | 1,806.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 109 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 107 | 1h 41m | 1,156 km | 2,134.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N296AE |  | John Edwin Jones Sr Field/Metter Municipal Airport (KMHP) | Daniel Field (KDNL) | 2026-05-20 22:11 UTC | 2026-05-20 22:51 UTC | 39m |
| N317GW |  | 9FD7 (9FD7) | Weedon Field (KEUF) | 2026-05-20 21:46 UTC | 2026-05-20 22:45 UTC | 58m |
| ARRIS69 | ARR | California City Municipal Airport (KL71) | Trona Airport (KL72) | 2026-05-20 20:42 UTC | 2026-05-20 22:32 UTC | 1h 49m |
| RTY775 | RTY | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-05-20 21:48 UTC | 2026-05-20 22:27 UTC | 39m |
| N200KS |  | Sanderson Field (KSHN) | Sanderson Field (KSHN) | 2026-05-20 22:02 UTC | 2026-05-20 22:24 UTC | 21m |
| RMRNR53 | RMR | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-20 22:22 UTC | 2026-05-20 22:24 UTC | 1m |
| LXJ406 | LXJ | Harry Reid International Airport (KLAS) | Montréal / St-Hubert Airport (CYHU) | 2026-05-20 18:17 UTC | 2026-05-20 22:21 UTC | 4h 4m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-05-20 10:58 UTC | 2026-05-20 22:20 UTC | 11h 21m |
| N63UD |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-05-20 21:14 UTC | 2026-05-20 22:19 UTC | 1h 4m |
| HKC9490 | HKC | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-05-20 10:27 UTC | 2026-05-20 22:13 UTC | 11h 46m |
| N5280F |  | 8TX7 (8TX7) | 8TX7 (8TX7) | 2026-05-20 21:40 UTC | 2026-05-20 22:13 UTC | 32m |
| N500JJ |  | Miami-Opa Locka Executive Airport (KOPF) | Gunnison-Crested Butte Regional Airport (KGUC) | 2026-05-20 18:24 UTC | 2026-05-20 22:10 UTC | 3h 45m |
| N3466K |  | Camp Bullis Als (Cals) Airport (9TX5) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-05-20 21:57 UTC | 2026-05-20 22:07 UTC | 9m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Macau International Airport (VMMC) | 2026-05-20 11:32 UTC | 2026-05-20 22:05 UTC | 10h 32m |
| TCN80 | TCN | Monterey Regional Airport (KMRY) | Deitch Airport (41PA) | 2026-05-20 17:08 UTC | 2026-05-20 22:04 UTC | 4h 55m |
| GLR2747 | GLR | Saskatoon John G. Diefenbaker International Airport (CYXE) | Regina Beach Airport (CKL9) | 2026-05-20 21:34 UTC | 2026-05-20 22:04 UTC | 29m |
| N133PE |  | Cobb County International/Mccollum Field (KRYY) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-20 20:59 UTC | 2026-05-20 22:01 UTC | 1h 2m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-05-20 10:46 UTC | 2026-05-20 22:01 UTC | 11h 15m |
| N604SG |  | Mefford Field (KTLR) | Henderson Executive Airport (KHND) | 2026-05-20 21:09 UTC | 2026-05-20 22:01 UTC | 52m |
| SKW5212 | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-05-20 20:56 UTC | 2026-05-20 21:57 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
