# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_11:24:40_UTC-green)

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

**Latest saved flight:** 2026-05-17 11:24:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 11:24:40 UTC

- **85,829** saved flights
- **30,781** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,829** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,061,745.3 tonnes** estimated CO2 emissions
- **61,550,451 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3674 |
| 2 | SkyWest Airlines | 3172 |
| 3 | IndiGo | 1852 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1318 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1089 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 936 |
| 10 | Vueling | 812 |
| 11 | AXM | 780 |
| 12 | LATAM Airlines | 778 |
| 13 | WIF | 734 |
| 14 | AZU | 671 |
| 15 | All Nippon Airways | 666 |
| 16 | Swiss International | 666 |
| 17 | LXJ | 628 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 566 |
| 21 | Cathay Pacific | 546 |
| 22 | EJU | 545 |
| 23 | AEE | 539 |
| 24 | VIV | 515 |
| 25 | Air France | 501 |
| 26 | Japan Airlines | 477 |
| 27 | CXK | 453 |
| 28 | AXB | 452 |
| 29 | MXY | 427 |
| 30 | AIQ | 422 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70223 |
| 2 | 🇪🇸 ES | 6064 |
| 3 | 🇮🇳 IN | 5794 |
| 4 | 🇦🇺 AU | 5471 |
| 5 | 🇩🇪 DE | 4784 |
| 6 | 🇮🇹 IT | 4736 |
| 7 | 🇧🇷 BR | 4717 |
| 8 | 🇯🇵 JP | 4312 |
| 9 | 🇨🇦 CA | 4257 |
| 10 | 🇬🇧 GB | 3661 |
| 11 | 🇫🇷 FR | 3414 |
| 12 | 🇨🇴 CO | 2878 |
| 13 | 🇲🇽 MX | 2642 |
| 14 | 🇬🇷 GR | 2491 |
| 15 | 🇳🇴 NO | 2377 |
| 16 | 🇨🇭 CH | 2274 |
| 17 | 🇲🇾 MY | 1957 |
| 18 | 🇿🇦 ZA | 1611 |
| 19 | 🇹🇷 TR | 1541 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1495 |
| 22 | 🇵🇱 PL | 1421 |
| 23 | 🇵🇭 PH | 1350 |
| 24 | 🇰🇷 KR | 1342 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇴 MO | 1003 |
| 27 | 🇲🇦 MA | 996 |
| 28 | 🇲🇪 ME | 896 |
| 29 | 🇳🇱 NL | 873 |
| 30 | 🇭🇷 HR | 767 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Denver International Airport |  | US | 1442 |
| 3 | Tokyo International Airport |  | JP | 1439 |
| 4 | Indira Gandhi International Airport |  | IN | 1243 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1194 |
| 6 | Frankfurt am Main International Airport |  | DE | 1099 |
| 7 | Harry Reid International Airport |  | US | 1084 |
| 8 | Zurich Airport |  | CH | 1024 |
| 9 | Macau International Airport |  | MO | 1003 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 926 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 864 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 783 |
| 17 | Kuala Lumpur International Airport |  | MY | 778 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 20 | Malpensa International Airport |  | IT | 712 |
| 21 | Salt Lake City International Airport |  | US | 711 |
| 22 | Capua Airport |  | IT | 705 |
| 23 | Bengaluru International Airport |  | IN | 702 |
| 24 | Charles de Gaulle International Airport |  | FR | 668 |
| 25 | Charlotte/Douglas International Airport |  | US | 665 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 630 |
| 28 | Tenerife Norte Airport |  | ES | 625 |
| 29 | Ninoy Aquino International Airport |  | PH | 618 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 583 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 572 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 552 |
| 35 | Vitoria/Foronda Airport |  | ES | 544 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 541 |
| 37 | Don Mueang International Airport |  | TH | 540 |
| 38 | Amsterdam Airport Schiphol |  | NL | 531 |
| 39 | O. R. Tambo International Airport |  | ZA | 507 |
| 40 | Calgary International Airport |  | CA | 501 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 319 | 21m | 244 km | 1,343.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 228 | 1h 26m | 910 km | 3,577.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 226 | 28m | 304 km | 1,184.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 198 | 1h 10m | 770 km | 2,630.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 180 | 26m | 275 km | 852.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 134 | 31m | 369 km | 852.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 109 | 18m | 144 km | 271.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 105 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR8454 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-16 23:13 UTC | 2026-05-17 11:24 UTC | 12h 11m |
| GTI8522 | GTI | Narita International Airport (RJAA) | Macau International Airport (VMMC) | 2026-05-17 01:25 UTC | 2026-05-17 11:07 UTC | 9h 41m |
| IGO1157D | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Langtang Airport (VNLT) | 2026-05-17 10:31 UTC | 2026-05-17 11:07 UTC | 36m |
| FYG35YN | FYG | Toulon-Hyeres Airport (LFTH) | Rotterdam Airport (EHRD) | 2026-05-17 09:31 UTC | 2026-05-17 10:59 UTC | 1h 27m |
| FJO646 | FJO | Parma Airport (LIMP) | Raron Airport (LSTA) | 2026-05-17 10:24 UTC | 2026-05-17 10:57 UTC | 33m |
| GRFRV | GRF | Henstridge Airfield (EGHS) | Henstridge Airfield (EGHS) | 2026-05-17 10:30 UTC | 2026-05-17 10:53 UTC | 23m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-05-17 09:17 UTC | 2026-05-17 10:50 UTC | 1h 32m |
| MMO151P | MMO | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-05-17 10:46 UTC | 2026-05-17 10:46 UTC | 0m |
| SWU1909 | SWU | Sigonella Airport (LICZ) | Trento / Mattarello Airport (LIDT) | 2026-05-17 09:00 UTC | 2026-05-17 10:42 UTC | 1h 42m |
| EJU573R | EJU | Malpensa International Airport (LIMC) | Pantelleria Airport (LICG) | 2026-05-17 09:27 UTC | 2026-05-17 10:36 UTC | 1h 9m |
| MNE311 | MNE | Zurich Airport (LSZH) | Dubrovnik Airport (LDDU) | 2026-05-17 09:21 UTC | 2026-05-17 10:35 UTC | 1h 13m |
| JFA46Y | JFA | Megeve Airport (LFHM) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-17 09:34 UTC | 2026-05-17 10:33 UTC | 59m |
| DMS | DMS | Adelaide International Airport (YPAD) | Sydney Bankstown Airport (YSBK) | 2026-05-17 08:50 UTC | 2026-05-17 10:29 UTC | 1h 38m |
| EJU705T | EJU | Malpensa International Airport (LIMC) | L'Aquila / Preturo Airport (LIAP) | 2026-05-17 09:25 UTC | 2026-05-17 10:28 UTC | 1h 2m |
| TCADO | TCA | Antalya International Airport (LTAI) | Nice-Cote d'Azur Airport (LFMN) | 2026-05-17 06:38 UTC | 2026-05-17 10:27 UTC | 3h 49m |
| ANE1099 | ANE | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-05-17 10:02 UTC | 2026-05-17 10:27 UTC | 24m |
| AZU2476 | AZU | Viracopos International Airport (SBKP) | Teixeira de Freitas Airport (SNTF) | 2026-05-17 09:14 UTC | 2026-05-17 10:25 UTC | 1h 11m |
| LNK651R | LNK | Cape Town International Airport (FACT) | Barberton Airport (FABR) | 2026-05-17 08:37 UTC | 2026-05-17 10:25 UTC | 1h 48m |
| DRAG38 | DRA | L'alpe D'huez Airport (LFHU) | Grenoble Le Versoud Airport (LFLG) | 2026-05-17 10:14 UTC | 2026-05-17 10:23 UTC | 8m |
| RYR60ED | Ryanair | Edinburgh Airport (EGPH) | Cork Airport (EICK) | 2026-05-17 09:27 UTC | 2026-05-17 10:23 UTC | 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
