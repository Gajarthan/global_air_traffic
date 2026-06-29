# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_01:32:10_UTC-green)

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

**Latest saved flight:** 2026-06-29 01:32:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-29 01:32:10 UTC

- **123,686** saved flights
- **42,403** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **123,686** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,495,400.1 tonnes** estimated CO2 emissions
- **86,689,864 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5051 |
| 2 | SkyWest Airlines | 4580 |
| 3 | EJA | 2418 |
| 4 | IndiGo | 2362 |
| 5 | American Airlines | 1912 |
| 6 | Southwest Airlines | 1855 |
| 7 | ENY | 1554 |
| 8 | Delta Air Lines | 1470 |
| 9 | Lufthansa | 1330 |
| 10 | LATAM Airlines | 1113 |
| 11 | Vueling | 1099 |
| 12 | WIF | 1092 |
| 13 | AZU | 1041 |
| 14 | AXM | 988 |
| 15 | LXJ | 960 |
| 16 | Swiss International | 870 |
| 17 | All Nippon Airways | 833 |
| 18 | Alaska Airlines | 812 |
| 19 | easyJet | 789 |
| 20 | QLK | 779 |
| 21 | EJU | 774 |
| 22 | Cathay Pacific | 693 |
| 23 | AEE | 683 |
| 24 | Air France | 675 |
| 25 | VIV | 674 |
| 26 | United Airlines | 662 |
| 27 | CXK | 653 |
| 28 | MXY | 646 |
| 29 | JetBlue | 626 |
| 30 | GLO | 619 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 105327 |
| 2 | 🇪🇸 ES | 8307 |
| 3 | 🇮🇳 IN | 7404 |
| 4 | 🇦🇺 AU | 7225 |
| 5 | 🇧🇷 BR | 6876 |
| 6 | 🇩🇪 DE | 6579 |
| 7 | 🇮🇹 IT | 6563 |
| 8 | 🇨🇦 CA | 6485 |
| 9 | 🇬🇧 GB | 5445 |
| 10 | 🇯🇵 JP | 5444 |
| 11 | 🇫🇷 FR | 4906 |
| 12 | 🇨🇴 CO | 4031 |
| 13 | 🇲🇽 MX | 3600 |
| 14 | 🇬🇷 GR | 3524 |
| 15 | 🇳🇴 NO | 3401 |
| 16 | 🇨🇭 CH | 3174 |
| 17 | 🇹🇷 TR | 2594 |
| 18 | 🇲🇾 MY | 2557 |
| 19 | 🇿🇦 ZA | 2043 |
| 20 | 🇵🇱 PL | 2029 |
| 21 | 🇳🇿 NZ | 1998 |
| 22 | 🇹🇭 TH | 1932 |
| 23 | 🇰🇷 KR | 1929 |
| 24 | 🇵🇭 PH | 1762 |
| 25 | 🇬🇹 GT | 1710 |
| 26 | 🇲🇦 MA | 1322 |
| 27 | 🇲🇪 ME | 1231 |
| 28 | 🇲🇴 MO | 1177 |
| 29 | 🇳🇱 NL | 1175 |
| 30 | 🇧🇸 BS | 1075 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2603 |
| 2 | Denver International Airport |  | US | 2077 |
| 3 | Tokyo International Airport |  | JP | 1800 |
| 4 | Indira Gandhi International Airport |  | IN | 1632 |
| 5 | Harry Reid International Airport |  | US | 1544 |
| 6 | Guaymaral Airport |  | CO | 1519 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1486 |
| 8 | Zurich Airport |  | CH | 1374 |
| 9 | La Aurora Airport |  | GT | 1321 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1319 |
| 11 | Frankfurt am Main International Airport |  | DE | 1285 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1217 |
| 13 | Chicago O'Hare International Airport |  | US | 1199 |
| 14 | Macau International Airport |  | MO | 1177 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1085 |
| 17 | Capua Airport |  | IT | 1057 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1032 |
| 19 | Madrid Barajas International Airport |  | ES | 1029 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 985 |
| 22 | Congonhas Airport |  | BR | 965 |
| 23 | Charlotte/Douglas International Airport |  | US | 934 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 910 |
| 25 | Charles de Gaulle International Airport |  | FR | 904 |
| 26 | Bengaluru International Airport |  | IN | 889 |
| 27 | Malpensa International Airport |  | IT | 856 |
| 28 | Ninoy Aquino International Airport |  | PH | 817 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 816 |
| 30 | Daniel K Inouye International Airport |  | US | 793 |
| 31 | Barcelona International Airport |  | ES | 771 |
| 32 | Tenerife Norte Airport |  | ES | 764 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 754 |
| 34 | Calgary International Airport |  | CA | 726 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 718 |
| 36 | Vitoria/Foronda Airport |  | ES | 717 |
| 37 | Seattle-Tacoma International Airport |  | US | 713 |
| 38 | Amsterdam Airport Schiphol |  | NL | 712 |
| 39 | Scottsdale Airport |  | US | 711 |
| 40 | Viracopos International Airport |  | BR | 701 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 450 | 21m | 244 km | 1,894.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 322 | 24m | 225 km | 1,249.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 311 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 296 | 1h 25m | 910 km | 4,644.9 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 180 | 22m | 55 km | 171.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 178 | 26m | 215 km | 659.2 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 175 | 20m | 99 km | 299.8 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 172 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 170 | 44m | 241 km | 706.1 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 168 | 27m | 152 km | 439.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 158 | 1h 44m | 1,423 km | 3,877.6 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 155 | 18m | 144 km | 385.6 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 144 | 1h 38m | 1,156 km | 2,872.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 142 | 1h 1m | 695 km | 1,702.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 141 | 1h 17m | 961 km | 2,337.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 139 | 30m | 49 km | 117.5 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 139 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NMA301 | NMA | Malpensa International Airport (LIMC) | HE12 (HE12) | 2026-06-28 22:13 UTC | 2026-06-29 01:32 UTC | 3h 18m |
| XSN40 | XSN | Truckee-Tahoe Airport (KTRK) | Gnoss Field (KDVO) | 2026-06-29 00:52 UTC | 2026-06-29 01:23 UTC | 31m |
| TKR102 | TKR | Animas Air Park (K00C) | CD82 (CD82) | 2026-06-29 00:51 UTC | 2026-06-29 01:15 UTC | 24m |
| VAR405 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-06-28 23:59 UTC | 2026-06-29 01:13 UTC | 1h 14m |
| N2904 |  | Salt Lake City International Airport (KSLC) | Cottonwood Airport (KP52) | 2026-06-28 23:50 UTC | 2026-06-29 01:08 UTC | 1h 17m |
| N1KD |  | Des Moines International Airport (KDSM) | Spencer Municipal Airport (KSPW) | 2026-06-29 00:42 UTC | 2026-06-29 01:05 UTC | 23m |
| N350RX |  | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-06-29 00:41 UTC | 2026-06-29 01:03 UTC | 22m |
| QLK35D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 2026-06-28 23:54 UTC | 2026-06-29 01:03 UTC | 1h 8m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-06-29 00:26 UTC | 2026-06-29 01:03 UTC | 36m |
| N96TJ |  | Chino Airport (KCNO) | Big Bear City Airport (KL35) | 2026-06-29 00:19 UTC | 2026-06-29 00:58 UTC | 39m |
| N565TA |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-28 23:59 UTC | 2026-06-29 00:54 UTC | 55m |
| THY726 | Turkish Airlines | Istanbul Airport (LTFM) | Simara Airport (VNSI) | 2026-06-28 18:30 UTC | 2026-06-29 00:53 UTC | 6h 23m |
| XAAVS | XAA | Del Norte International Airport (MMAN) | Del Norte International Airport (MMAN) | 2026-06-29 00:48 UTC | 2026-06-29 00:49 UTC | 0m |
| ENY3634 | ENY | Chicago O'Hare International Airport (KORD) | Dvoracek Field (23MI) | 2026-06-29 00:11 UTC | 2026-06-29 00:47 UTC | 35m |
| N2YV |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-29 00:00 UTC | 2026-06-29 00:47 UTC | 46m |
| EXU | EXU | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-28 23:58 UTC | 2026-06-29 00:46 UTC | 47m |
| FRLD15 | FRL | Grand Junction Regional Airport (KGJT) | 27CO (27CO) | 2026-06-29 00:33 UTC | 2026-06-29 00:44 UTC | 10m |
| ENY3705 | ENY | Dallas-Fort Worth International Airport (KDFW) | Cisco Municipal Airport (K3F2) | 2026-06-29 00:23 UTC | 2026-06-29 00:44 UTC | 20m |
| SWA191 | Southwest Airlines | Harry Reid International Airport (KLAS) | Twentynine Palms Airport (KTNP) | 2026-06-29 00:18 UTC | 2026-06-29 00:40 UTC | 22m |
| EJA469 | EJA | Boeing Field/King County International Airport (KBFI) | 3WA1 (3WA1) | 2026-06-29 00:24 UTC | 2026-06-29 00:37 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
