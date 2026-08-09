# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_03:30:41_UTC-green)

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

**Latest saved flight:** 2026-08-09 03:30:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 03:30:41 UTC

- **180,177** saved flights
- **57,724** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,177** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,165,245.4 tonnes** estimated CO2 emissions
- **125,521,470 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7126 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3554 |
| 4 | IndiGo | 3153 |
| 5 | Southwest Airlines | 2839 |
| 6 | American Airlines | 2816 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1679 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1487 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1229 |
| 16 | Swiss International | 1225 |
| 17 | AXM | 1213 |
| 18 | QLK | 1102 |
| 19 | Alaska Airlines | 1095 |
| 20 | EJU | 1095 |
| 21 | All Nippon Airways | 1092 |
| 22 | VIV | 996 |
| 23 | GLO | 964 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 936 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 904 |
| 30 | PGT | 896 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154678 |
| 2 | 🇪🇸 ES | 11553 |
| 3 | 🇧🇷 BR | 10342 |
| 4 | 🇦🇺 AU | 10114 |
| 5 | 🇮🇳 IN | 9879 |
| 6 | 🇨🇦 CA | 9848 |
| 7 | 🇮🇹 IT | 9285 |
| 8 | 🇩🇪 DE | 8896 |
| 9 | 🇬🇧 GB | 8309 |
| 10 | 🇯🇵 JP | 7265 |
| 11 | 🇫🇷 FR | 7153 |
| 12 | 🇨🇴 CO | 6703 |
| 13 | 🇬🇷 GR | 5244 |
| 14 | 🇲🇽 MX | 5161 |
| 15 | 🇨🇭 CH | 4789 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4585 |
| 18 | 🇲🇾 MY | 3167 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2922 |
| 21 | 🇹🇭 TH | 2725 |
| 22 | 🇳🇿 NZ | 2591 |
| 23 | 🇵🇭 PH | 2380 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2252 |
| 26 | 🇲🇦 MA | 1816 |
| 27 | 🇭🇷 HR | 1793 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1616 |
| 30 | 🇲🇴 MO | 1511 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2255 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2200 |
| 6 | Harry Reid International Airport |  | US | 2126 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1934 |
| 8 | Zurich Airport |  | CH | 1909 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1614 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1511 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1435 |
| 19 | Madrid Barajas International Airport |  | ES | 1409 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1350 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1283 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1259 |
| 24 | Malpensa International Airport |  | IT | 1240 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1216 |
| 27 | Kuala Lumpur International Airport |  | MY | 1193 |
| 28 | Bengaluru International Airport |  | IN | 1177 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1121 |
| 30 | Ninoy Aquino International Airport |  | PH | 1120 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1072 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1037 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1029 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 973 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 666 | 21m | 244 km | 2,804.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 424 | 24m | 225 km | 1,644.9 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 423 | 1h 8m | 770 km | 5,619.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 296 | 1h 7m | 706 km | 3,603.8 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 252 | 1h 48m | 1,423 km | 6,184.5 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 211 | 1h 38m | 1,156 km | 4,209.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 208 | 31m | 369 km | 1,324.0 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N246AM |  | Effingham County Regional Airport (K1H2) | Frasca Field (KC16) | 2026-08-09 03:01 UTC | 2026-08-09 03:30 UTC | 28m |
| ANA964 | All Nippon Airways | Beijing Capital International Airport (ZBAA) | Tokyo International Airport (RJTT) | 2026-08-09 00:32 UTC | 2026-08-09 03:18 UTC | 2h 45m |
| AEA064 | AEA | Cancun International Airport (MMUN) | Marsh Harbour International Airport (MYAM) | 2026-08-09 01:44 UTC | 2026-08-09 03:17 UTC | 1h 33m |
| N177AR |  | Zamperini Field (KTOA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-09 01:59 UTC | 2026-08-09 03:17 UTC | 1h 17m |
| EJM960 | EJM | Daniel K Inouye International Airport (PHNL) | Van Nuys Airport (KVNY) | 2026-08-08 22:31 UTC | 2026-08-09 03:16 UTC | 4h 44m |
| JES3156 | JES | Ministro Pistarini International Airport (SAEZ) | El Dorado Airport (SATD) | 2026-08-09 01:47 UTC | 2026-08-09 03:08 UTC | 1h 21m |
| N424KT |  | Fort Crosby Airport (8AK5) | Nugget Bench Airport (33AK) | 2026-08-09 02:43 UTC | 2026-08-09 03:06 UTC | 22m |
| CRN555 | CRN | Kelowna Airport (CYLW) | Sparwood Elk Valley Airport (CYSW) | 2026-08-09 02:31 UTC | 2026-08-09 03:03 UTC | 31m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bombala Airport (YBOM) | 2026-08-09 02:29 UTC | 2026-08-09 03:02 UTC | 32m |
| N954B |  | Seattle Paine Field International Airport (KPAE) | Arlington Municipal Airport (KAWO) | 2026-08-09 02:41 UTC | 2026-08-09 03:00 UTC | 19m |
| XCN70 | XCN | Spokane International Airport (KGEG) | Omak Airport (KOMK) | 2026-08-09 02:27 UTC | 2026-08-09 02:57 UTC | 29m |
| N336PA |  | Rocky Mountain Metro Airport (KBJC) | Pine Bluffs Municipal Airport (K82V) | 2026-08-09 02:05 UTC | 2026-08-09 02:52 UTC | 46m |
| XUM2593 | XUM | Gimpo International Airport (RKSS) | Sacheon Air Base (RKPS) | 2026-08-09 02:08 UTC | 2026-08-09 02:51 UTC | 43m |
| FFT1469 | FFT | Harry Reid International Airport (KLAS) | San Diego International Airport (KSAN) | 2026-08-09 02:05 UTC | 2026-08-09 02:51 UTC | 45m |
| ZKIDU | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-08-09 01:38 UTC | 2026-08-09 02:50 UTC | 1h 12m |
| N465TX |  | MU13 (MU13) | Dallas Executive Airport (KRBD) | 2026-08-09 00:49 UTC | 2026-08-09 02:50 UTC | 2h 0m |
| ISR047 | ISR | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-08-09 02:27 UTC | 2026-08-09 02:49 UTC | 22m |
| N2YV |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-09 02:17 UTC | 2026-08-09 02:46 UTC | 29m |
| N390SA |  | Mason City Municipal Airport (KMCW) | SD49 (SD49) | 2026-08-09 02:01 UTC | 2026-08-09 02:45 UTC | 43m |
| NJE048R | NJE | Gaziemir Airport (LTBK) | Santorini Airport (LGSR) | 2026-08-09 02:19 UTC | 2026-08-09 02:43 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
