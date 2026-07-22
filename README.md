# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_23:53:35_UTC-green)

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

**Latest saved flight:** 2026-07-21 23:53:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-21 23:53:35 UTC

- **143,531** saved flights
- **48,084** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,531** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,721,912.0 tonnes** estimated CO2 emissions
- **99,820,988 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5835 |
| 2 | SkyWest Airlines | 5253 |
| 3 | EJA | 2827 |
| 4 | IndiGo | 2611 |
| 5 | American Airlines | 2301 |
| 6 | Southwest Airlines | 2164 |
| 7 | ENY | 1783 |
| 8 | Delta Air Lines | 1704 |
| 9 | Lufthansa | 1439 |
| 10 | LATAM Airlines | 1324 |
| 11 | Vueling | 1233 |
| 12 | AZU | 1232 |
| 13 | WIF | 1225 |
| 14 | LXJ | 1102 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1021 |
| 17 | easyJet | 939 |
| 18 | All Nippon Airways | 921 |
| 19 | Alaska Airlines | 909 |
| 20 | QLK | 906 |
| 21 | EJU | 880 |
| 22 | VIV | 799 |
| 23 | CXK | 766 |
| 24 | AEE | 763 |
| 25 | Air France | 761 |
| 26 | JetBlue | 761 |
| 27 | MXY | 746 |
| 28 | Cathay Pacific | 745 |
| 29 | United Airlines | 745 |
| 30 | GLO | 732 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123519 |
| 2 | 🇪🇸 ES | 9342 |
| 3 | 🇦🇺 AU | 8240 |
| 4 | 🇮🇳 IN | 8183 |
| 5 | 🇧🇷 BR | 8096 |
| 6 | 🇨🇦 CA | 7572 |
| 7 | 🇮🇹 IT | 7476 |
| 8 | 🇩🇪 DE | 7416 |
| 9 | 🇬🇧 GB | 6565 |
| 10 | 🇯🇵 JP | 6034 |
| 11 | 🇫🇷 FR | 5694 |
| 12 | 🇨🇴 CO | 4607 |
| 13 | 🇲🇽 MX | 4177 |
| 14 | 🇬🇷 GR | 4076 |
| 15 | 🇳🇴 NO | 3834 |
| 16 | 🇨🇭 CH | 3718 |
| 17 | 🇹🇷 TR | 3383 |
| 18 | 🇲🇾 MY | 2773 |
| 19 | 🇵🇱 PL | 2416 |
| 20 | 🇿🇦 ZA | 2338 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2129 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1883 |
| 26 | 🇲🇦 MA | 1496 |
| 27 | 🇲🇪 ME | 1422 |
| 28 | 🇳🇱 NL | 1347 |
| 29 | 🇭🇷 HR | 1305 |
| 30 | 🇲🇴 MO | 1203 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2964 |
| 2 | Denver International Airport |  | US | 2411 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1815 |
| 5 | Harry Reid International Airport |  | US | 1802 |
| 6 | Guaymaral Airport |  | CO | 1745 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1638 |
| 8 | Zurich Airport |  | CH | 1591 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1507 |
| 10 | La Aurora Airport |  | GT | 1458 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1356 |
| 13 | Chicago O'Hare International Airport |  | US | 1338 |
| 14 | Salt Lake City International Airport |  | US | 1287 |
| 15 | El Dorado International Airport |  | CO | 1269 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1258 |
| 17 | Macau International Airport |  | MO | 1203 |
| 18 | Capua Airport |  | IT | 1167 |
| 19 | Congonhas Airport |  | BR | 1151 |
| 20 | Madrid Barajas International Airport |  | ES | 1149 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1133 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1035 |
| 25 | Charles de Gaulle International Airport |  | FR | 1006 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1004 |
| 27 | Bengaluru International Airport |  | IN | 977 |
| 28 | Malpensa International Airport |  | IT | 923 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 880 |
| 31 | Daniel K Inouye International Airport |  | US | 874 |
| 32 | Barcelona International Airport |  | ES | 874 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 855 |
| 34 | Tenerife Norte Airport |  | ES | 826 |
| 35 | Seattle-Tacoma International Airport |  | US | 821 |
| 36 | Calgary International Airport |  | CA | 817 |
| 37 | Viracopos International Airport |  | BR | 812 |
| 38 | Amsterdam Airport Schiphol |  | NL | 809 |
| 39 | Scottsdale Airport |  | US | 809 |
| 40 | Vitoria/Foronda Airport |  | ES | 787 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 735 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 523 | 21m | 244 km | 2,202.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 349 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 213 | 22m | 55 km | 202.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 193 | 26m | 215 km | 714.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 178 | 20m | 250 km | 768.9 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 167 | 1h 16m | 961 km | 2,768.1 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N401GH |  | Whippet Field (OR34) | Whippet Field (OR34) | 2026-07-21 23:38 UTC | 2026-07-21 23:53 UTC | 15m |
| N72NG |  | Los Angeles International Airport (KLAX) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-07-21 23:26 UTC | 2026-07-21 23:38 UTC | 11m |
| AAL2669 | American Airlines | John Wayne/Orange County Airport (KSNA) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-21 20:59 UTC | 2026-07-21 23:37 UTC | 2h 38m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-07-21 22:56 UTC | 2026-07-21 23:36 UTC | 40m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-07-21 23:03 UTC | 2026-07-21 23:34 UTC | 30m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-07-21 23:14 UTC | 2026-07-21 23:30 UTC | 16m |
| N121GX |  | Aurora Municipal Airport (KARR) | 72IS (72IS) | 2026-07-21 22:56 UTC | 2026-07-21 23:25 UTC | 28m |
| CFR610 | CFR | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-07-21 23:12 UTC | 2026-07-21 23:22 UTC | 9m |
| STT5690 | STT | Bradshaw Army Airfield (PHSF) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-21 22:59 UTC | 2026-07-21 23:19 UTC | 19m |
| WCC3 | WCC | Gillespie Field (KSEE) | Apple Valley Airport (KAPV) | 2026-07-21 22:53 UTC | 2026-07-21 23:18 UTC | 25m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-07-21 13:05 UTC | 2026-07-21 23:18 UTC | 10h 12m |
| AAL2576 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-21 21:50 UTC | 2026-07-21 23:15 UTC | 1h 25m |
| CFRT71 | CFR | Ramona Airport (KRNM) | Hemet-Ryan Airport (KHMT) | 2026-07-21 22:13 UTC | 2026-07-21 23:05 UTC | 52m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-07-21 22:48 UTC | 2026-07-21 23:01 UTC | 12m |
| DRAG382 | DRA | L'alpe D'huez Airport (LFHU) | L'alpe D'huez Airport (LFHU) | 2026-07-21 22:42 UTC | 2026-07-21 22:59 UTC | 17m |
| LTA367 | LTA | Seafood Warehouse Park Airport (XS77) | Hawthorne Field (K45R) | 2026-07-21 22:31 UTC | 2026-07-21 22:56 UTC | 25m |
| DAL1342 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Sacramento International Airport (KSMF) | 2026-07-21 21:40 UTC | 2026-07-21 22:56 UTC | 1h 15m |
| SCU24 | SCU | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-07-21 22:52 UTC | 2026-07-21 22:56 UTC | 3m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-07-21 08:36 UTC | 2026-07-21 22:56 UTC | 14h 20m |
| EJA16 | EJA | Houston Executive Airport (KTME) | Bowling Green-Warren County Regional Airport (KBWG) | 2026-07-21 20:54 UTC | 2026-07-21 22:54 UTC | 2h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
