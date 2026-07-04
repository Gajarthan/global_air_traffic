# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_20:51:14_UTC-green)

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

**Latest saved flight:** 2026-07-04 20:51:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 20:51:14 UTC

- **129,252** saved flights
- **43,976** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,252** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,561,160.7 tonnes** estimated CO2 emissions
- **90,502,070 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5253 |
| 2 | SkyWest Airlines | 4796 |
| 3 | EJA | 2528 |
| 4 | IndiGo | 2426 |
| 5 | American Airlines | 1996 |
| 6 | Southwest Airlines | 1948 |
| 7 | ENY | 1623 |
| 8 | Delta Air Lines | 1545 |
| 9 | Lufthansa | 1360 |
| 10 | LATAM Airlines | 1176 |
| 11 | Vueling | 1147 |
| 12 | WIF | 1133 |
| 13 | AZU | 1098 |
| 14 | AXM | 1003 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 899 |
| 17 | All Nippon Airways | 858 |
| 18 | Alaska Airlines | 833 |
| 19 | easyJet | 828 |
| 20 | QLK | 808 |
| 21 | EJU | 801 |
| 22 | VIV | 715 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 706 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 689 |
| 28 | MXY | 677 |
| 29 | JetBlue | 672 |
| 30 | GLO | 657 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110638 |
| 2 | 🇪🇸 ES | 8616 |
| 3 | 🇮🇳 IN | 7608 |
| 4 | 🇦🇺 AU | 7482 |
| 5 | 🇧🇷 BR | 7254 |
| 6 | 🇨🇦 CA | 6812 |
| 7 | 🇩🇪 DE | 6794 |
| 8 | 🇮🇹 IT | 6767 |
| 9 | 🇬🇧 GB | 5736 |
| 10 | 🇯🇵 JP | 5609 |
| 11 | 🇫🇷 FR | 5127 |
| 12 | 🇨🇴 CO | 4086 |
| 13 | 🇲🇽 MX | 3770 |
| 14 | 🇬🇷 GR | 3684 |
| 15 | 🇳🇴 NO | 3522 |
| 16 | 🇨🇭 CH | 3308 |
| 17 | 🇹🇷 TR | 2815 |
| 18 | 🇲🇾 MY | 2603 |
| 19 | 🇿🇦 ZA | 2137 |
| 20 | 🇵🇱 PL | 2122 |
| 21 | 🇳🇿 NZ | 2071 |
| 22 | 🇹🇭 TH | 2001 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1808 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1385 |
| 27 | 🇲🇪 ME | 1285 |
| 28 | 🇳🇱 NL | 1214 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1130 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2698 |
| 2 | Denver International Airport |  | US | 2201 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1677 |
| 5 | Harry Reid International Airport |  | US | 1612 |
| 6 | Guaymaral Airport |  | CO | 1573 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1531 |
| 8 | Zurich Airport |  | CH | 1421 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1376 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1316 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1241 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1150 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1084 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1062 |
| 20 | Madrid Barajas International Airport |  | ES | 1060 |
| 21 | Congonhas Airport |  | BR | 1021 |
| 22 | Kuala Lumpur International Airport |  | MY | 1013 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 941 |
| 25 | Charles de Gaulle International Airport |  | FR | 939 |
| 26 | Bengaluru International Airport |  | IN | 920 |
| 27 | Malpensa International Airport |  | IT | 878 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 873 |
| 29 | Ninoy Aquino International Airport |  | PH | 838 |
| 30 | Daniel K Inouye International Airport |  | US | 814 |
| 31 | Barcelona International Airport |  | ES | 804 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 790 |
| 33 | Tenerife Norte Airport |  | ES | 784 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 753 |
| 36 | Vitoria/Foronda Airport |  | ES | 748 |
| 37 | Seattle-Tacoma International Airport |  | US | 747 |
| 38 | Scottsdale Airport |  | US | 744 |
| 39 | Viracopos International Airport |  | BR | 739 |
| 40 | Amsterdam Airport Schiphol |  | NL | 731 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 659 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 467 | 21m | 244 km | 1,966.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 237 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 159 | 18m | 144 km | 395.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 153 | 1h 1m | 695 km | 1,834.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 148 | 54m | 136 km | 347.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N252SP |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-07-04 20:13 UTC | 2026-07-04 20:51 UTC | 37m |
| N366EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-04 19:52 UTC | 2026-07-04 20:48 UTC | 56m |
| TKR910 | TKR | Mesa Gateway Airport (KIWA) | Rimrock Airport (48AZ) | 2026-07-04 20:25 UTC | 2026-07-04 20:41 UTC | 16m |
| TKR107 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-07-04 20:27 UTC | 2026-07-04 20:41 UTC | 14m |
| N33HF |  | Alice International Airport (KALI) | Cabaniss Field Nolf Airport (KNGW) | 2026-07-04 20:17 UTC | 2026-07-04 20:36 UTC | 19m |
| TKR184 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-07-04 20:14 UTC | 2026-07-04 20:32 UTC | 18m |
| N493LG |  | CO54 (CO54) | Desiderata Ranch Airport (30CO) | 2026-07-04 20:17 UTC | 2026-07-04 20:32 UTC | 15m |
| THY170 | Turkish Airlines | Istanbul Airport (LTFM) | VYNT (VYNT) | 2026-07-04 13:14 UTC | 2026-07-04 20:32 UTC | 7h 17m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Lashio Airport (VYLS) | 2026-07-04 15:30 UTC | 2026-07-04 20:32 UTC | 5h 1m |
| STY90 | STY | Philadelphia International Airport (KPHL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 19:42 UTC | 2026-07-04 20:29 UTC | 46m |
| N135CK |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-07-04 19:33 UTC | 2026-07-04 20:28 UTC | 55m |
| TMN125 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-07-04 11:16 UTC | 2026-07-04 20:28 UTC | 9h 11m |
| TKR140 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-07-04 20:06 UTC | 2026-07-04 20:26 UTC | 19m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-07-04 06:14 UTC | 2026-07-04 20:26 UTC | 14h 11m |
| TKR41 | TKR | Animas Air Park (K00C) | Blanding Municipal Airport (KBDG) | 2026-07-04 20:05 UTC | 2026-07-04 20:21 UTC | 15m |
| DAL675 | Delta Air Lines | Kansas City International Airport (KMCI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 17:50 UTC | 2026-07-04 20:18 UTC | 2h 27m |
| DAL113 | Delta Air Lines | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 11:39 UTC | 2026-07-04 20:15 UTC | 8h 35m |
| DHK896 | DHK | Abqaiq Airport (OEBQ) | Zhuhai Airport (ZGSD) | 2026-07-04 12:24 UTC | 2026-07-04 20:12 UTC | 7h 47m |
| EJA888 | EJA | Yucca Valley Airport (KL22) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-04 19:14 UTC | 2026-07-04 20:11 UTC | 57m |
| N80BM |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-07-04 19:43 UTC | 2026-07-04 20:10 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
