# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_19:07:56_UTC-green)

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

**Latest saved flight:** 2026-05-19 19:07:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 19:07:56 UTC

- **88,351** saved flights
- **31,565** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **88,351** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,093,305.4 tonnes** estimated CO2 emissions
- **63,380,022 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3787 |
| 2 | SkyWest Airlines | 3275 |
| 3 | IndiGo | 1876 |
| 4 | EJA | 1676 |
| 5 | American Airlines | 1354 |
| 6 | Southwest Airlines | 1284 |
| 7 | Lufthansa | 1112 |
| 8 | ENY | 1093 |
| 9 | Delta Air Lines | 968 |
| 10 | Vueling | 845 |
| 11 | LATAM Airlines | 792 |
| 12 | AXM | 786 |
| 13 | WIF | 765 |
| 14 | AZU | 700 |
| 15 | Swiss International | 682 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 647 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 625 |
| 20 | easyJet | 583 |
| 21 | EJU | 568 |
| 22 | Cathay Pacific | 563 |
| 23 | AEE | 547 |
| 24 | VIV | 530 |
| 25 | Air France | 519 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 466 |
| 28 | AXB | 458 |
| 29 | MXY | 451 |
| 30 | AIQ | 431 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72552 |
| 2 | 🇪🇸 ES | 6279 |
| 3 | 🇮🇳 IN | 5880 |
| 4 | 🇦🇺 AU | 5504 |
| 5 | 🇩🇪 DE | 4918 |
| 6 | 🇮🇹 IT | 4900 |
| 7 | 🇧🇷 BR | 4842 |
| 8 | 🇨🇦 CA | 4423 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3768 |
| 11 | 🇫🇷 FR | 3539 |
| 12 | 🇨🇴 CO | 3017 |
| 13 | 🇲🇽 MX | 2745 |
| 14 | 🇬🇷 GR | 2559 |
| 15 | 🇳🇴 NO | 2457 |
| 16 | 🇨🇭 CH | 2334 |
| 17 | 🇲🇾 MY | 1974 |
| 18 | 🇿🇦 ZA | 1637 |
| 19 | 🇹🇷 TR | 1602 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1518 |
| 22 | 🇵🇱 PL | 1469 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1357 |
| 25 | 🇬🇹 GT | 1330 |
| 26 | 🇲🇦 MA | 1022 |
| 27 | 🇲🇴 MO | 1021 |
| 28 | 🇲🇪 ME | 913 |
| 29 | 🇳🇱 NL | 898 |
| 30 | 🇭🇷 HR | 797 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1938 |
| 2 | Denver International Airport |  | US | 1478 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1268 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1210 |
| 6 | Harry Reid International Airport |  | US | 1125 |
| 7 | Frankfurt am Main International Airport |  | DE | 1119 |
| 8 | Zurich Airport |  | CH | 1055 |
| 9 | Guaymaral Airport |  | CO | 1027 |
| 10 | Macau International Airport |  | MO | 1021 |
| 11 | La Aurora Airport |  | GT | 1011 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 978 |
| 13 | El Dorado International Airport |  | CO | 962 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 898 |
| 15 | Chicago O'Hare International Airport |  | US | 856 |
| 16 | Madrid Barajas International Airport |  | ES | 803 |
| 17 | Kuala Lumpur International Airport |  | MY | 784 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 758 |
| 19 | Capua Airport |  | IT | 748 |
| 20 | Salt Lake City International Airport |  | US | 737 |
| 21 | Malpensa International Airport |  | IT | 724 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 708 |
| 24 | Charles de Gaulle International Airport |  | FR | 690 |
| 25 | Charlotte/Douglas International Airport |  | US | 683 |
| 26 | Congonhas Airport |  | BR | 674 |
| 27 | Daniel K Inouye International Airport |  | US | 648 |
| 28 | Tenerife Norte Airport |  | ES | 648 |
| 29 | Ninoy Aquino International Airport |  | PH | 622 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 597 |
| 31 | Barcelona International Airport |  | ES | 597 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 585 |
| 34 | Vitoria/Foronda Airport |  | ES | 567 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 555 |
| 37 | Don Mueang International Airport |  | TH | 552 |
| 38 | Amsterdam Airport Schiphol |  | NL | 550 |
| 39 | Calgary International Airport |  | CA | 525 |
| 40 | O. R. Tambo International Airport |  | ZA | 518 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 421 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 330 | 21m | 244 km | 1,389.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 229 | 14m | 114 km | 449.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 226 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 184 | 26m | 275 km | 871.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 129 | 27m | 215 km | 477.8 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 124 | 23m | 55 km | 117.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 123 | 20m | 250 km | 531.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 114 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DHX729 | DHX | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-05-19 11:45 UTC | 2026-05-19 19:07 UTC | 7h 22m |
| MYSTIC62 | MYS | Dee Jay Airport (8PA1) | Capital City Airport (KCXY) | 2026-05-19 18:29 UTC | 2026-05-19 19:03 UTC | 34m |
| BNOR | BNO | Brønnøysund Airport (ENBN) | Mo i Rana Airport Rossvoll (ENRA) | 2026-05-19 18:40 UTC | 2026-05-19 19:00 UTC | 20m |
| N607FJ |  | Ted Stevens Anchorage International Airport (PANC) | Merle K (Mudhole) Smith Airport (PACV) | 2026-05-19 17:31 UTC | 2026-05-19 18:59 UTC | 1h 27m |
| SWR5PC | Swiss International | London Gatwick Airport (EGKK) | Zurich Airport (LSZH) | 2026-05-19 17:45 UTC | 2026-05-19 18:57 UTC | 1h 12m |
| RAM983 | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Mohammed V International Airport (GMMN) | 2026-05-19 18:07 UTC | 2026-05-19 18:56 UTC | 49m |
| CXK158 | CXK | Sugar Land Regional Airport (KSGR) | Henson Farms Airport (3TS5) | 2026-05-19 18:28 UTC | 2026-05-19 18:52 UTC | 24m |
| OXF2781 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-05-19 17:25 UTC | 2026-05-19 18:51 UTC | 1h 25m |
| N42CU |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-05-19 17:52 UTC | 2026-05-19 18:46 UTC | 54m |
| CGLOX | CGL | Saskatoon John G. Diefenbaker International Airport (CYXE) | Calgary International Airport (CYYC) | 2026-05-19 17:31 UTC | 2026-05-19 18:44 UTC | 1h 13m |
| JAF8GH | JAF | Lille-Lesquin Airport (LFQQ) | Tit Mellil Airport (GMMT) | 2026-05-19 15:59 UTC | 2026-05-19 18:43 UTC | 2h 44m |
| N47698 |  | Denali Airport (AK06) | Summit Airport (PAST) | 2026-05-19 18:24 UTC | 2026-05-19 18:43 UTC | 19m |
| G08815 |  | Selfridge Angb Airport (KMTC) | Selfridge Angb Airport (KMTC) | 2026-05-19 18:28 UTC | 2026-05-19 18:43 UTC | 15m |
| BBC386 | BBC | VGZR (VGZR) | Kuala Lumpur International Airport (WMKK) | 2026-05-19 15:29 UTC | 2026-05-19 18:43 UTC | 3h 14m |
| BULET11 | BUL | Bob Maxwell Memorial Airfield (KOKB) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-19 17:21 UTC | 2026-05-19 18:42 UTC | 1h 20m |
| N124RF |  | Griffiss International Airport (KRME) | KNY2 (KNY2) | 2026-05-19 17:47 UTC | 2026-05-19 18:40 UTC | 53m |
| MSR754 | EgyptAir | Madrid Barajas International Airport (LEMD) | HE32 (HE32) | 2026-05-19 15:01 UTC | 2026-05-19 18:39 UTC | 3h 38m |
| N8339D |  | David Wayne Hooks Memorial Airport (KDWH) | Easterwood Field (KCLL) | 2026-05-19 17:51 UTC | 2026-05-19 18:36 UTC | 45m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-05-19 17:47 UTC | 2026-05-19 18:34 UTC | 47m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-19 18:19 UTC | 2026-05-19 18:33 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
