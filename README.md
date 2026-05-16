# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_11:05:06_UTC-green)

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

**Latest saved flight:** 2026-05-16 11:05:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 11:05:06 UTC

- **84,531** saved flights
- **30,432** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,531** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,042,829.5 tonnes** estimated CO2 emissions
- **60,453,884 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3618 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1828 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1300 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1072 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 922 |
| 10 | Vueling | 798 |
| 11 | AXM | 768 |
| 12 | LATAM Airlines | 765 |
| 13 | WIF | 731 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 659 |
| 16 | Swiss International | 657 |
| 17 | QLK | 620 |
| 18 | LXJ | 619 |
| 19 | Alaska Airlines | 599 |
| 20 | easyJet | 557 |
| 21 | EJU | 537 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 532 |
| 24 | VIV | 505 |
| 25 | Air France | 497 |
| 26 | Japan Airlines | 474 |
| 27 | AXB | 448 |
| 28 | CXK | 446 |
| 29 | MXY | 420 |
| 30 | United Airlines | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69210 |
| 2 | 🇪🇸 ES | 5970 |
| 3 | 🇮🇳 IN | 5720 |
| 4 | 🇦🇺 AU | 5410 |
| 5 | 🇩🇪 DE | 4700 |
| 6 | 🇮🇹 IT | 4658 |
| 7 | 🇧🇷 BR | 4645 |
| 8 | 🇯🇵 JP | 4258 |
| 9 | 🇨🇦 CA | 4205 |
| 10 | 🇬🇧 GB | 3607 |
| 11 | 🇫🇷 FR | 3358 |
| 12 | 🇨🇴 CO | 2821 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2457 |
| 15 | 🇳🇴 NO | 2356 |
| 16 | 🇨🇭 CH | 2230 |
| 17 | 🇲🇾 MY | 1926 |
| 18 | 🇿🇦 ZA | 1596 |
| 19 | 🇹🇷 TR | 1507 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1470 |
| 22 | 🇵🇱 PL | 1404 |
| 23 | 🇵🇭 PH | 1328 |
| 24 | 🇰🇷 KR | 1312 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 980 |
| 27 | 🇲🇴 MO | 980 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 861 |
| 30 | 🇭🇷 HR | 755 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1849 |
| 2 | Tokyo International Airport |  | JP | 1423 |
| 3 | Denver International Airport |  | US | 1419 |
| 4 | Indira Gandhi International Airport |  | IN | 1220 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1186 |
| 6 | Frankfurt am Main International Airport |  | DE | 1088 |
| 7 | Harry Reid International Airport |  | US | 1062 |
| 8 | Zurich Airport |  | CH | 1005 |
| 9 | Macau International Airport |  | MO | 980 |
| 10 | La Aurora Airport |  | GT | 965 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 770 |
| 17 | Kuala Lumpur International Airport |  | MY | 765 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 706 |
| 20 | Malpensa International Airport |  | IT | 705 |
| 21 | Salt Lake City International Airport |  | US | 704 |
| 22 | Bengaluru International Airport |  | IN | 698 |
| 23 | Capua Airport |  | IT | 690 |
| 24 | Charles de Gaulle International Airport |  | FR | 662 |
| 25 | Congonhas Airport |  | BR | 657 |
| 26 | Charlotte/Douglas International Airport |  | US | 656 |
| 27 | Daniel K Inouye International Airport |  | US | 616 |
| 28 | Tenerife Norte Airport |  | ES | 612 |
| 29 | Ninoy Aquino International Airport |  | PH | 608 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 565 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 563 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 544 |
| 35 | Vitoria/Foronda Airport |  | ES | 534 |
| 36 | Don Mueang International Airport |  | TH | 532 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 530 |
| 38 | Amsterdam Airport Schiphol |  | NL | 522 |
| 39 | O. R. Tambo International Airport |  | ZA | 503 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 312 | 21m | 244 km | 1,313.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 217 | 14m | 114 km | 425.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 191 | 19m | 165 km | 543.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 177 | 26m | 275 km | 838.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 119 | 20m | 250 km | 514.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 107 | 18m | 144 km | 266.2 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAG76 | DRA | Le Havre Octeville Airport (LFOH) | Caen-Carpiquet Airport (LFRK) | 2026-05-16 10:53 UTC | 2026-05-16 11:05 UTC | 11m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-15 19:45 UTC | 2026-05-16 11:03 UTC | 15h 18m |
| N247RU |  | Burlington/Alamance Regional Airport (KBUY) | St Pete-Clearwater International Airport (KPIE) | 2026-05-16 09:35 UTC | 2026-05-16 11:00 UTC | 1h 25m |
| N847MH |  | Harry Reid International Airport (KLAS) | Nellis Afb Airport (KLSV) | 2026-05-16 10:44 UTC | 2026-05-16 10:51 UTC | 7m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-16 10:30 UTC | 2026-05-16 10:43 UTC | 12m |
| LOT7CR | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Gjader Air Base (LAGJ) | 2026-05-16 08:58 UTC | 2026-05-16 10:41 UTC | 1h 43m |
| N252EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-16 08:35 UTC | 2026-05-16 10:39 UTC | 2h 4m |
| N243EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-16 08:36 UTC | 2026-05-16 10:32 UTC | 1h 55m |
| WMT7868 | WMT | Memmingen Allgau Airport (EDJA) | LRPV (LRPV) | 2026-05-16 08:42 UTC | 2026-05-16 10:31 UTC | 1h 48m |
| UPS1014 | UPS | Louisville Muhammad Ali International Airport (KSDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-16 08:44 UTC | 2026-05-16 10:27 UTC | 1h 42m |
| RYR88DM | Ryanair | London Stansted Airport (EGSS) | Le Blanc Airport (LFEL) | 2026-05-16 09:27 UTC | 2026-05-16 10:25 UTC | 57m |
| DEDBQ | DED | Bonn-Hangelar Airport (EDKB) | Siegerland Airport (EDGS) | 2026-05-16 09:52 UTC | 2026-05-16 10:22 UTC | 30m |
| FDX1502 | FDX | Frederick W Smith International Airport (KMEM) | Huntington Municipal Airport (KHHG) | 2026-05-16 09:24 UTC | 2026-05-16 10:19 UTC | 54m |
| RYR35CB | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Visoko Sport Airfield (LQVI) | 2026-05-16 09:01 UTC | 2026-05-16 10:17 UTC | 1h 16m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-16 10:05 UTC | 2026-05-16 10:16 UTC | 10m |
| DRK401 | DRK | Tribhuvan International Airport (VNKT) | Yongphulla Airport (VQ10) | 2026-05-16 07:54 UTC | 2026-05-16 10:16 UTC | 2h 22m |
| REH50 | REH | Mc Clellan Airfield (KMCC) | Trinity Center Airport (KO86) | 2026-05-16 09:28 UTC | 2026-05-16 10:15 UTC | 47m |
| TKJ6AN | TKJ | Sivas Airport (LTAR) | Erzincan Airport (LTCD) | 2026-05-16 09:54 UTC | 2026-05-16 10:12 UTC | 17m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-16 09:58 UTC | 2026-05-16 10:10 UTC | 11m |
| RYR674 | Ryanair | Vienna International Airport (LOWW) | Trstenik Airport (LYTR) | 2026-05-16 09:09 UTC | 2026-05-16 10:10 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
