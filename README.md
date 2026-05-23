# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_08:39:55_UTC-green)

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

**Latest saved flight:** 2026-05-23 08:39:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-23 08:39:55 UTC

- **92,397** saved flights
- **32,768** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **92,397** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,136,471.8 tonnes** estimated CO2 emissions
- **65,882,420 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3918 |
| 2 | SkyWest Airlines | 3425 |
| 3 | IndiGo | 1927 |
| 4 | EJA | 1750 |
| 5 | American Airlines | 1400 |
| 6 | Southwest Airlines | 1333 |
| 7 | ENY | 1139 |
| 8 | Lufthansa | 1125 |
| 9 | Delta Air Lines | 1012 |
| 10 | Vueling | 878 |
| 11 | LATAM Airlines | 824 |
| 12 | AXM | 815 |
| 13 | WIF | 807 |
| 14 | AZU | 734 |
| 15 | LXJ | 700 |
| 16 | Swiss International | 693 |
| 17 | All Nippon Airways | 689 |
| 18 | QLK | 648 |
| 19 | Alaska Airlines | 647 |
| 20 | easyJet | 605 |
| 21 | EJU | 589 |
| 22 | Cathay Pacific | 581 |
| 23 | AEE | 560 |
| 24 | VIV | 547 |
| 25 | Air France | 542 |
| 26 | Japan Airlines | 487 |
| 27 | CXK | 486 |
| 28 | MXY | 479 |
| 29 | AXB | 470 |
| 30 | AIQ | 448 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 76329 |
| 2 | 🇪🇸 ES | 6502 |
| 3 | 🇮🇳 IN | 6067 |
| 4 | 🇦🇺 AU | 5726 |
| 5 | 🇩🇪 DE | 5072 |
| 6 | 🇧🇷 BR | 5052 |
| 7 | 🇮🇹 IT | 5034 |
| 8 | 🇨🇦 CA | 4672 |
| 9 | 🇯🇵 JP | 4474 |
| 10 | 🇬🇧 GB | 3935 |
| 11 | 🇫🇷 FR | 3721 |
| 12 | 🇨🇴 CO | 3196 |
| 13 | 🇲🇽 MX | 2846 |
| 14 | 🇬🇷 GR | 2641 |
| 15 | 🇳🇴 NO | 2574 |
| 16 | 🇨🇭 CH | 2416 |
| 17 | 🇲🇾 MY | 2057 |
| 18 | 🇹🇷 TR | 1684 |
| 19 | 🇿🇦 ZA | 1673 |
| 20 | 🇳🇿 NZ | 1586 |
| 21 | 🇹🇭 TH | 1568 |
| 22 | 🇵🇱 PL | 1506 |
| 23 | 🇰🇷 KR | 1475 |
| 24 | 🇵🇭 PH | 1413 |
| 25 | 🇬🇹 GT | 1389 |
| 26 | 🇲🇦 MA | 1060 |
| 27 | 🇲🇴 MO | 1037 |
| 28 | 🇳🇱 NL | 929 |
| 29 | 🇲🇪 ME | 928 |
| 30 | 🇭🇷 HR | 835 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2006 |
| 2 | Denver International Airport |  | US | 1553 |
| 3 | Tokyo International Airport |  | JP | 1490 |
| 4 | Indira Gandhi International Airport |  | IN | 1322 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1233 |
| 6 | Harry Reid International Airport |  | US | 1191 |
| 7 | Frankfurt am Main International Airport |  | DE | 1133 |
| 8 | Guaymaral Airport |  | CO | 1107 |
| 9 | Zurich Airport |  | CH | 1083 |
| 10 | La Aurora Airport |  | GT | 1062 |
| 11 | Macau International Airport |  | MO | 1037 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1012 |
| 13 | El Dorado International Airport |  | CO | 1007 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 925 |
| 15 | Chicago O'Hare International Airport |  | US | 883 |
| 16 | Madrid Barajas International Airport |  | ES | 832 |
| 17 | Kuala Lumpur International Airport |  | MY | 812 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 779 |
| 19 | Salt Lake City International Airport |  | US | 776 |
| 20 | Capua Airport |  | IT | 769 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 743 |
| 22 | Malpensa International Airport |  | IT | 736 |
| 23 | Bengaluru International Airport |  | IN | 729 |
| 24 | Charles de Gaulle International Airport |  | FR | 721 |
| 25 | Charlotte/Douglas International Airport |  | US | 707 |
| 26 | Congonhas Airport |  | BR | 703 |
| 27 | Daniel K Inouye International Airport |  | US | 668 |
| 28 | Tenerife Norte Airport |  | ES | 663 |
| 29 | Ninoy Aquino International Airport |  | PH | 647 |
| 30 | Barcelona International Airport |  | ES | 623 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 612 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 601 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 598 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 583 |
| 35 | Vitoria/Foronda Airport |  | ES | 576 |
| 36 | Don Mueang International Airport |  | TH | 575 |
| 37 | Amsterdam Airport Schiphol |  | NL | 570 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 39 | Calgary International Airport |  | CA | 549 |
| 40 | O. R. Tambo International Airport |  | ZA | 529 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 454 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 340 | 21m | 244 km | 1,431.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 253 | 24m | 225 km | 981.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 244 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 239 | 14m | 114 km | 468.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 238 | 1h 26m | 910 km | 3,734.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 234 | 28m | 304 km | 1,226.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 213 | 1h 10m | 770 km | 2,829.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 200 | 19m | 165 km | 568.9 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 151 | 21m | 99 km | 258.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 137 | 27m | 215 km | 507.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 136 | 22m | 55 km | 129.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 134 | 14m | 154 km | 355.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 127 | 20m | 250 km | 548.6 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 119 | 1h 1m | 695 km | 1,426.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 119 | 18m | 144 km | 296.0 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 113 | 1h 42m | 1,423 km | 2,773.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SXS7VF | SXS | Gaziemir Airport (LTBK) | Radomir Dolni Rakovets Airfield (LB13) | 2026-05-23 07:52 UTC | 2026-05-23 08:39 UTC | 47m |
| DEGGL | DEG | Hildesheim Airport (EDVM) | Uetersen/Heist Airport (EDHE) | 2026-05-23 07:47 UTC | 2026-05-23 08:39 UTC | 51m |
| ISR169 | ISR | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-05-23 08:02 UTC | 2026-05-23 08:22 UTC | 20m |
| DIFLD | DIF | Harle Airport (EDXP) | Wangerooge Airport (EDWG) | 2026-05-23 08:03 UTC | 2026-05-23 08:06 UTC | 3m |
| YOX | YOX | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-23 07:24 UTC | 2026-05-23 08:06 UTC | 41m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-05-23 07:02 UTC | 2026-05-23 07:59 UTC | 56m |
| DHFCB | DHF | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-05-23 07:57 UTC | 2026-05-23 07:57 UTC | 0m |
| THY9MV | Turkish Airlines | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-05-23 07:40 UTC | 2026-05-23 07:57 UTC | 17m |
| TVJ132 | TVJ | Suvarnabhumi Airport (VTBS) | Kengtung Airport (VYKG) | 2026-05-23 07:02 UTC | 2026-05-23 07:56 UTC | 54m |
| OAL082 | OAL | Thessaloniki Macedonia International Airport (LGTS) | Ikaria Airport (LGIK) | 2026-05-23 06:49 UTC | 2026-05-23 07:53 UTC | 1h 3m |
| TCSKO | TCS | Ataturk International Airport (LTBA) | Isparta Airport (LTBM) | 2026-05-23 07:14 UTC | 2026-05-23 07:52 UTC | 38m |
| RYR74SV | Ryanair | Luqa Airport (LMML) | Otocac Airport (LDRO) | 2026-05-23 06:19 UTC | 2026-05-23 07:50 UTC | 1h 30m |
| CFG8EP | CFG | Palma De Mallorca Airport (LEPA) | Frankfurt am Main International Airport (EDDF) | 2026-05-23 05:58 UTC | 2026-05-23 07:49 UTC | 1h 51m |
| RYR161N | Ryanair | Barcelona International Airport (LEBL) | Malpensa International Airport (LIMC) | 2026-05-23 06:34 UTC | 2026-05-23 07:49 UTC | 1h 15m |
| RYR84UF | Ryanair | Bristol International Airport (EGGD) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-05-23 05:58 UTC | 2026-05-23 07:44 UTC | 1h 46m |
| FPYHY | FPY | Grenoble Le Versoud Airport (LFLG) | L'alpe D'huez Airport (LFHU) | 2026-05-23 07:06 UTC | 2026-05-23 07:43 UTC | 37m |
| HBXPY | HBX | Fricktal-Schupfart Airport (LSZI) | Buttwil Airport (LSZU) | 2026-05-23 07:20 UTC | 2026-05-23 07:43 UTC | 23m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Hosur Airport (VO95) | 2026-05-23 07:08 UTC | 2026-05-23 07:42 UTC | 34m |
| CMA574 | CMA | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-05-22 20:20 UTC | 2026-05-23 07:42 UTC | 11h 22m |
| RYR1DA | Ryanair | Sepurine Training Base (LD57) | Karlsruhe Baden-Baden Airport (EDSB) | 2026-05-23 06:30 UTC | 2026-05-23 07:39 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
