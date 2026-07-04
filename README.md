# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_12:30:35_UTC-green)

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

**Latest saved flight:** 2026-07-04 12:30:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 12:30:35 UTC

- **128,667** saved flights
- **43,829** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,667** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,552,738.0 tonnes** estimated CO2 emissions
- **90,013,799 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5231 |
| 2 | SkyWest Airlines | 4769 |
| 3 | EJA | 2522 |
| 4 | IndiGo | 2421 |
| 5 | American Airlines | 1983 |
| 6 | Southwest Airlines | 1934 |
| 7 | ENY | 1612 |
| 8 | Delta Air Lines | 1532 |
| 9 | Lufthansa | 1355 |
| 10 | LATAM Airlines | 1170 |
| 11 | Vueling | 1139 |
| 12 | WIF | 1132 |
| 13 | AZU | 1091 |
| 14 | AXM | 1003 |
| 15 | LXJ | 997 |
| 16 | Swiss International | 894 |
| 17 | All Nippon Airways | 858 |
| 18 | Alaska Airlines | 831 |
| 19 | easyJet | 820 |
| 20 | QLK | 808 |
| 21 | EJU | 796 |
| 22 | Cathay Pacific | 710 |
| 23 | VIV | 710 |
| 24 | AEE | 703 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 685 |
| 28 | MXY | 672 |
| 29 | JetBlue | 663 |
| 30 | GLO | 649 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110126 |
| 2 | 🇪🇸 ES | 8566 |
| 3 | 🇮🇳 IN | 7593 |
| 4 | 🇦🇺 AU | 7479 |
| 5 | 🇧🇷 BR | 7201 |
| 6 | 🇨🇦 CA | 6775 |
| 7 | 🇩🇪 DE | 6764 |
| 8 | 🇮🇹 IT | 6747 |
| 9 | 🇬🇧 GB | 5701 |
| 10 | 🇯🇵 JP | 5607 |
| 11 | 🇫🇷 FR | 5105 |
| 12 | 🇨🇴 CO | 4072 |
| 13 | 🇲🇽 MX | 3750 |
| 14 | 🇬🇷 GR | 3660 |
| 15 | 🇳🇴 NO | 3512 |
| 16 | 🇨🇭 CH | 3289 |
| 17 | 🇹🇷 TR | 2764 |
| 18 | 🇲🇾 MY | 2602 |
| 19 | 🇿🇦 ZA | 2132 |
| 20 | 🇵🇱 PL | 2108 |
| 21 | 🇳🇿 NZ | 2069 |
| 22 | 🇹🇭 TH | 2001 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1808 |
| 25 | 🇬🇹 GT | 1763 |
| 26 | 🇲🇦 MA | 1376 |
| 27 | 🇲🇪 ME | 1277 |
| 28 | 🇳🇱 NL | 1210 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇭🇷 HR | 1115 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2681 |
| 2 | Denver International Airport |  | US | 2182 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1675 |
| 5 | Harry Reid International Airport |  | US | 1606 |
| 6 | Guaymaral Airport |  | CO | 1559 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1525 |
| 8 | Zurich Airport |  | CH | 1413 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1369 |
| 10 | La Aurora Airport |  | GT | 1363 |
| 11 | Frankfurt am Main International Airport |  | DE | 1313 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1256 |
| 13 | Chicago O'Hare International Airport |  | US | 1236 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1147 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1069 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 20 | Madrid Barajas International Airport |  | ES | 1053 |
| 21 | Congonhas Airport |  | BR | 1012 |
| 22 | Kuala Lumpur International Airport |  | MY | 1012 |
| 23 | Charlotte/Douglas International Airport |  | US | 968 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 939 |
| 25 | Charles de Gaulle International Airport |  | FR | 937 |
| 26 | Bengaluru International Airport |  | IN | 917 |
| 27 | Malpensa International Airport |  | IT | 875 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 865 |
| 29 | Ninoy Aquino International Airport |  | PH | 838 |
| 30 | Daniel K Inouye International Airport |  | US | 813 |
| 31 | Barcelona International Airport |  | ES | 800 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 786 |
| 33 | Tenerife Norte Airport |  | ES | 783 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 758 |
| 35 | Calgary International Airport |  | CA | 752 |
| 36 | Seattle-Tacoma International Airport |  | US | 743 |
| 37 | Vitoria/Foronda Airport |  | ES | 743 |
| 38 | Scottsdale Airport |  | US | 742 |
| 39 | Viracopos International Airport |  | BR | 735 |
| 40 | Amsterdam Airport Schiphol |  | NL | 728 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 652 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 466 | 21m | 244 km | 1,962.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 324 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 245 | 26m | 275 km | 1,161.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 237 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 167 | 1h 45m | 1,423 km | 4,098.4 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 158 | 20m | 250 km | 682.5 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 152 | 1h 1m | 695 km | 1,822.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 143 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HB2414 |  | Zweisimmen Airport (LSTZ) | Saanen Airport (LSGK) | 2026-07-04 11:25 UTC | 2026-07-04 12:30 UTC | 1h 5m |
| N6148J |  | Cleburne Regional Airport (KCPT) | Jim Sears Airport (3TA7) | 2026-07-04 11:51 UTC | 2026-07-04 12:26 UTC | 35m |
| N18728 |  | Peter O Knight Airport (KTPF) | Plant City Airport (KPCM) | 2026-07-04 11:41 UTC | 2026-07-04 12:26 UTC | 44m |
| OM1010 |  | Samedan Airport (LSZS) | LIVD (LIVD) | 2026-07-04 12:10 UTC | 2026-07-04 12:24 UTC | 14m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-07-03 21:37 UTC | 2026-07-04 12:10 UTC | 14h 33m |
| RGA18 | RGA | Bex Airport (LSGB) | Zweisimmen Airport (LSTZ) | 2026-07-04 11:31 UTC | 2026-07-04 12:09 UTC | 37m |
| N4002S |  | Easton/Valley View Airport (K11V) | Easton/Valley View Airport (K11V) | 2026-07-04 11:29 UTC | 2026-07-04 12:08 UTC | 38m |
| N79005 |  | Ituverava Airport (SDIV) | Ituverava Airport (SDIV) | 2026-07-04 11:56 UTC | 2026-07-04 11:57 UTC | 0m |
| AIC8RR | Air India | Juhu Aerodrome (VAJJ) | Indira Gandhi International Airport (VIDP) | 2026-07-04 09:59 UTC | 2026-07-04 11:55 UTC | 1h 55m |
| OKSEE | OKS | Mnichovo Hradiste Airport (LKMH) | Mnichovo Hradiste Airport (LKMH) | 2026-07-04 11:37 UTC | 2026-07-04 11:54 UTC | 17m |
| STY90 | STY | KNY2 (KNY2) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 11:03 UTC | 2026-07-04 11:45 UTC | 42m |
| AXB1050 | AXB | Juhu Aerodrome (VAJJ) | Indira Gandhi International Airport (VIDP) | 2026-07-04 09:52 UTC | 2026-07-04 11:40 UTC | 1h 47m |
| AEE6DS | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-07-04 11:20 UTC | 2026-07-04 11:40 UTC | 20m |
| RYR7FV | Ryanair | Ciampino Airport (LIRA) | Sochaczew Airport (EPSO) | 2026-07-04 09:38 UTC | 2026-07-04 11:39 UTC | 2h 0m |
| OKYUA95 | OKY | Jaromer Airport (LKJA) | Hradec Kralove Airport (LKHK) | 2026-07-04 11:28 UTC | 2026-07-04 11:35 UTC | 7m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-07-04 11:27 UTC | 2026-07-04 11:34 UTC | 7m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-07-04 11:03 UTC | 2026-07-04 11:32 UTC | 29m |
| HBZNP | HBZ | Buochs Airport (LSZC) | LSMF (LSMF) | 2026-07-04 11:14 UTC | 2026-07-04 11:29 UTC | 14m |
| DFROH | DFR | Casale Monferrato Airport (LILM) | Casale Monferrato Airport (LILM) | 2026-07-04 09:46 UTC | 2026-07-04 11:26 UTC | 1h 40m |
| JBU134 | JetBlue | San Francisco International Airport (KSFO) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 05:54 UTC | 2026-07-04 11:25 UTC | 5h 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
