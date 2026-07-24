# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_19:58:44_UTC-green)

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

**Latest saved flight:** 2026-07-24 19:58:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 19:58:44 UTC

- **148,658** saved flights
- **49,614** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **148,658** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,777,203.4 tonnes** estimated CO2 emissions
- **103,026,286 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5999 |
| 2 | SkyWest Airlines | 5439 |
| 3 | EJA | 2943 |
| 4 | IndiGo | 2665 |
| 5 | American Airlines | 2366 |
| 6 | Southwest Airlines | 2248 |
| 7 | ENY | 1851 |
| 8 | Delta Air Lines | 1755 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1367 |
| 11 | AZU | 1285 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1256 |
| 14 | LXJ | 1150 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 957 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 930 |
| 20 | QLK | 922 |
| 21 | EJU | 906 |
| 22 | VIV | 821 |
| 23 | CXK | 797 |
| 24 | AEE | 780 |
| 25 | Air France | 779 |
| 26 | JetBlue | 777 |
| 27 | MXY | 774 |
| 28 | Cathay Pacific | 773 |
| 29 | GLO | 771 |
| 30 | United Airlines | 770 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 128321 |
| 2 | 🇪🇸 ES | 9594 |
| 3 | 🇦🇺 AU | 8459 |
| 4 | 🇧🇷 BR | 8394 |
| 5 | 🇮🇳 IN | 8369 |
| 6 | 🇨🇦 CA | 7960 |
| 7 | 🇮🇹 IT | 7686 |
| 8 | 🇩🇪 DE | 7613 |
| 9 | 🇬🇧 GB | 6790 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5899 |
| 12 | 🇨🇴 CO | 4988 |
| 13 | 🇲🇽 MX | 4309 |
| 14 | 🇬🇷 GR | 4207 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3493 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2506 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1977 |
| 25 | 🇬🇹 GT | 1935 |
| 26 | 🇲🇦 MA | 1520 |
| 27 | 🇲🇪 ME | 1469 |
| 28 | 🇳🇱 NL | 1379 |
| 29 | 🇭🇷 HR | 1348 |
| 30 | 🇲🇴 MO | 1236 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3059 |
| 2 | Denver International Airport |  | US | 2490 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Guaymaral Airport |  | CO | 1859 |
| 5 | Indira Gandhi International Airport |  | IN | 1858 |
| 6 | Harry Reid International Airport |  | US | 1842 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1668 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1566 |
| 10 | La Aurora Airport |  | GT | 1498 |
| 11 | Frankfurt am Main International Airport |  | DE | 1404 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1400 |
| 13 | Chicago O'Hare International Airport |  | US | 1377 |
| 14 | Salt Lake City International Airport |  | US | 1340 |
| 15 | El Dorado International Airport |  | CO | 1332 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1278 |
| 17 | Macau International Airport |  | MO | 1236 |
| 18 | Congonhas Airport |  | BR | 1199 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1179 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1158 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1061 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1043 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1001 |
| 28 | Malpensa International Airport |  | IT | 960 |
| 29 | Ninoy Aquino International Airport |  | PH | 926 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 906 |
| 31 | Barcelona International Airport |  | ES | 895 |
| 32 | Daniel K Inouye International Airport |  | US | 892 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 888 |
| 34 | Calgary International Airport |  | CA | 850 |
| 35 | Seattle-Tacoma International Airport |  | US | 850 |
| 36 | Tenerife Norte Airport |  | ES | 849 |
| 37 | Scottsdale Airport |  | US | 845 |
| 38 | Viracopos International Airport |  | BR | 839 |
| 39 | Amsterdam Airport Schiphol |  | NL | 829 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 785 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 539 | 21m | 244 km | 2,269.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 360 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 266 | 27m | 275 km | 1,260.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 196 | 20m | 99 km | 335.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 183 | 20m | 250 km | 790.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 182 | 27m | 152 km | 475.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 174 | 1h 16m | 961 km | 2,884.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 167 | 1h 39m | 1,156 km | 3,331.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N27M |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-07-24 19:42 UTC | 2026-07-24 19:58 UTC | 15m |
| N217WM |  | Kalifonsky Meadows Airport (0AA7) | Homer Airport (PAHO) | 2026-07-24 19:09 UTC | 2026-07-24 19:54 UTC | 45m |
| ENT4UZ | ENT | Poznań-Ławica Airport (EPPO) | Diagoras Airport (LGRP) | 2026-07-24 17:16 UTC | 2026-07-24 19:50 UTC | 2h 33m |
| XBOWB | XBO | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-24 19:20 UTC | 2026-07-24 19:44 UTC | 24m |
| N115GK |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-07-24 19:08 UTC | 2026-07-24 19:41 UTC | 33m |
| N95TK |  | Poplar Grove Airport (KC77) | IS80 (IS80) | 2026-07-24 18:29 UTC | 2026-07-24 19:39 UTC | 1h 9m |
| ILU45A | ILU | University Of Illinois/Willard Airport (KCMI) | University Of Illinois/Willard Airport (KCMI) | 2026-07-24 18:31 UTC | 2026-07-24 19:38 UTC | 1h 7m |
| TKR162 | TKR | Whiterik Field (51WT) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-24 19:23 UTC | 2026-07-24 19:38 UTC | 15m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-07-24 19:00 UTC | 2026-07-24 19:38 UTC | 37m |
| HK5165G |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-07-24 19:20 UTC | 2026-07-24 19:36 UTC | 16m |
| N75VJ |  | Tracy Municipal Airport (KTCY) | Lake Tahoe Airport (KTVL) | 2026-07-24 18:57 UTC | 2026-07-24 19:33 UTC | 36m |
| RAM997 | Royal Air Maroc | Francisco de Sá Carneiro Airport (LPPR) | Mohammed V International Airport (GMMN) | 2026-07-24 18:14 UTC | 2026-07-24 19:32 UTC | 1h 18m |
| EJA680 | EJA | Akron-Canton Regional Airport (KCAK) | Valhalla Airport (IN91) | 2026-07-24 19:01 UTC | 2026-07-24 19:31 UTC | 30m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-07-24 19:11 UTC | 2026-07-24 19:31 UTC | 20m |
| LXJ375 | LXJ | Black River Ranch Airport (1MI3) | Toronto Pearson International Airport (CYYZ) | 2026-07-24 18:45 UTC | 2026-07-24 19:31 UTC | 45m |
| N29049 |  | Farmville Regional Airport (KFVX) | Farmville Regional Airport (KFVX) | 2026-07-24 19:22 UTC | 2026-07-24 19:30 UTC | 7m |
| N81034 |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-07-24 19:14 UTC | 2026-07-24 19:29 UTC | 14m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-07-24 19:08 UTC | 2026-07-24 19:27 UTC | 19m |
| N405SB |  | Laconia Municipal Airport (KLCI) | Lebanon Municipal Airport (KLEB) | 2026-07-24 18:41 UTC | 2026-07-24 19:27 UTC | 45m |
| N909CS |  | Kalaeloa (John Rodgers Field) Airport (PHJR) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-24 17:34 UTC | 2026-07-24 19:24 UTC | 1h 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
