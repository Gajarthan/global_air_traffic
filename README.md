# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_21:42:20_UTC-green)

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

**Latest saved flight:** 2026-06-01 21:42:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-01 21:42:20 UTC

- **100,434** saved flights
- **35,669** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,434** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,230,259.0 tonnes** estimated CO2 emissions
- **71,319,363 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4157 |
| 2 | SkyWest Airlines | 3766 |
| 3 | IndiGo | 2027 |
| 4 | EJA | 1920 |
| 5 | American Airlines | 1627 |
| 6 | Southwest Airlines | 1518 |
| 7 | ENY | 1252 |
| 8 | Delta Air Lines | 1180 |
| 9 | Lufthansa | 1176 |
| 10 | Vueling | 941 |
| 11 | LATAM Airlines | 893 |
| 12 | WIF | 879 |
| 13 | AXM | 864 |
| 14 | AZU | 809 |
| 15 | LXJ | 761 |
| 16 | Swiss International | 732 |
| 17 | All Nippon Airways | 714 |
| 18 | Alaska Airlines | 702 |
| 19 | QLK | 676 |
| 20 | easyJet | 655 |
| 21 | EJU | 633 |
| 22 | Cathay Pacific | 600 |
| 23 | AEE | 588 |
| 24 | VIV | 581 |
| 25 | Air France | 580 |
| 26 | United Airlines | 564 |
| 27 | CXK | 541 |
| 28 | MXY | 536 |
| 29 | Japan Airlines | 506 |
| 30 | AXB | 497 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 84127 |
| 2 | 🇪🇸 ES | 6961 |
| 3 | 🇮🇳 IN | 6397 |
| 4 | 🇦🇺 AU | 6060 |
| 5 | 🇧🇷 BR | 5490 |
| 6 | 🇩🇪 DE | 5445 |
| 7 | 🇮🇹 IT | 5361 |
| 8 | 🇨🇦 CA | 5168 |
| 9 | 🇯🇵 JP | 4663 |
| 10 | 🇬🇧 GB | 4277 |
| 11 | 🇫🇷 FR | 4016 |
| 12 | 🇨🇴 CO | 3493 |
| 13 | 🇲🇽 MX | 3047 |
| 14 | 🇬🇷 GR | 2870 |
| 15 | 🇳🇴 NO | 2784 |
| 16 | 🇨🇭 CH | 2597 |
| 17 | 🇲🇾 MY | 2198 |
| 18 | 🇹🇷 TR | 1908 |
| 19 | 🇿🇦 ZA | 1753 |
| 20 | 🇳🇿 NZ | 1681 |
| 21 | 🇹🇭 TH | 1665 |
| 22 | 🇰🇷 KR | 1621 |
| 23 | 🇵🇱 PL | 1612 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1465 |
| 26 | 🇲🇦 MA | 1128 |
| 27 | 🇲🇴 MO | 1062 |
| 28 | 🇳🇱 NL | 1003 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 889 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2193 |
| 2 | Denver International Airport |  | US | 1723 |
| 3 | Tokyo International Airport |  | JP | 1546 |
| 4 | Indira Gandhi International Airport |  | IN | 1391 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1294 |
| 6 | Harry Reid International Airport |  | US | 1280 |
| 7 | Guaymaral Airport |  | CO | 1260 |
| 8 | Frankfurt am Main International Airport |  | DE | 1180 |
| 9 | Zurich Airport |  | CH | 1151 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1086 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1062 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1020 |
| 15 | Chicago O'Hare International Airport |  | US | 1008 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 869 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 865 |
| 19 | Salt Lake City International Airport |  | US | 849 |
| 20 | Capua Airport |  | IT | 832 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 781 |
| 22 | Charlotte/Douglas International Airport |  | US | 781 |
| 23 | Charles de Gaulle International Airport |  | FR | 770 |
| 24 | Bengaluru International Airport |  | IN | 767 |
| 25 | Malpensa International Airport |  | IT | 766 |
| 26 | Congonhas Airport |  | BR | 764 |
| 27 | Daniel K Inouye International Airport |  | US | 695 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 669 |
| 30 | Barcelona International Airport |  | ES | 665 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 655 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 640 |
| 34 | Amsterdam Airport Schiphol |  | NL | 619 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 609 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 587 |
| 39 | Seattle-Tacoma International Airport |  | US | 576 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 519 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 365 | 21m | 244 km | 1,536.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 264 | 24m | 225 km | 1,024.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 246 | 1h 26m | 910 km | 3,860.3 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 229 | 1h 10m | 770 km | 3,042.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 144 | 22m | 55 km | 136.9 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 132 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N479DS |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-06-01 21:29 UTC | 2026-06-01 21:42 UTC | 12m |
| N642PF |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-06-01 20:59 UTC | 2026-06-01 21:40 UTC | 40m |
| N1NP |  | Columbus Municipal Airport (KOLU) | Lincoln Airport (KLNK) | 2026-06-01 21:20 UTC | 2026-06-01 21:37 UTC | 16m |
| N88765 |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-01 21:13 UTC | 2026-06-01 21:35 UTC | 21m |
| UAL877 | United Airlines | San Francisco International Airport (KSFO) | Macau International Airport (VMMC) | 2026-06-01 08:54 UTC | 2026-06-01 21:31 UTC | 12h 36m |
| N80945 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-01 21:07 UTC | 2026-06-01 21:29 UTC | 22m |
| KING99 | KIN | Elmendorf Afb Airport (PAED) | Eielson Afb Airport (PAEI) | 2026-06-01 20:26 UTC | 2026-06-01 21:27 UTC | 1h 1m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-01 21:11 UTC | 2026-06-01 21:24 UTC | 13m |
| N103UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-06-01 21:05 UTC | 2026-06-01 21:23 UTC | 17m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-06-01 17:39 UTC | 2026-06-01 21:21 UTC | 3h 42m |
| FFL1728 | FFL | Red Hawk Airport (80LA) | Gregory M Simmons Memorial Airport (KGZN) | 2026-06-01 20:16 UTC | 2026-06-01 21:21 UTC | 1h 5m |
| N616PC |  | Bolton Field (KTZR) | Pickaway County Memorial Airport (KCYO) | 2026-06-01 20:57 UTC | 2026-06-01 21:15 UTC | 18m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-06-01 20:58 UTC | 2026-06-01 21:14 UTC | 15m |
| N716AT |  | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-06-01 20:57 UTC | 2026-06-01 21:11 UTC | 14m |
| N15CV |  | Logan-Cache Airport (KLGU) | Portland-Hillsboro Airport (KHIO) | 2026-06-01 19:47 UTC | 2026-06-01 21:10 UTC | 1h 22m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-06-01 06:39 UTC | 2026-06-01 21:09 UTC | 14h 29m |
| N35KS |  | Mountain Valley Airport (KL94) | 91CL (91CL) | 2026-06-01 19:54 UTC | 2026-06-01 21:09 UTC | 1h 14m |
| BOE892 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-06-01 19:53 UTC | 2026-06-01 21:06 UTC | 1h 13m |
| N133HN |  | Lincoln Airport (KLNK) | Pester Airport (NE59) | 2026-06-01 20:54 UTC | 2026-06-01 20:59 UTC | 5m |
| N107UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-06-01 20:42 UTC | 2026-06-01 20:59 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
