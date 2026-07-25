# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_21:48:34_UTC-green)

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

**Latest saved flight:** 2026-07-25 21:48:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 21:48:34 UTC

- **151,255** saved flights
- **50,277** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,255** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,809,514.3 tonnes** estimated CO2 emissions
- **104,899,378 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6105 |
| 2 | SkyWest Airlines | 5537 |
| 3 | EJA | 2996 |
| 4 | IndiGo | 2694 |
| 5 | American Airlines | 2401 |
| 6 | Southwest Airlines | 2301 |
| 7 | ENY | 1888 |
| 8 | Delta Air Lines | 1777 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1399 |
| 11 | AZU | 1312 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1271 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 987 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 942 |
| 20 | QLK | 931 |
| 21 | EJU | 926 |
| 22 | VIV | 834 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 793 |
| 26 | Air France | 788 |
| 27 | GLO | 788 |
| 28 | JetBlue | 788 |
| 29 | United Airlines | 782 |
| 30 | Cathay Pacific | 781 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130534 |
| 2 | 🇪🇸 ES | 9786 |
| 3 | 🇧🇷 BR | 8570 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8481 |
| 6 | 🇨🇦 CA | 8074 |
| 7 | 🇮🇹 IT | 7833 |
| 8 | 🇩🇪 DE | 7754 |
| 9 | 🇬🇧 GB | 6941 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5985 |
| 12 | 🇨🇴 CO | 5149 |
| 13 | 🇲🇽 MX | 4366 |
| 14 | 🇬🇷 GR | 4297 |
| 15 | 🇳🇴 NO | 4002 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3586 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2569 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2271 |
| 22 | 🇹🇭 TH | 2193 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1539 |
| 27 | 🇲🇪 ME | 1481 |
| 28 | 🇳🇱 NL | 1395 |
| 29 | 🇭🇷 HR | 1384 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3113 |
| 2 | Denver International Airport |  | US | 2543 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1904 |
| 5 | Indira Gandhi International Airport |  | IN | 1882 |
| 6 | Harry Reid International Airport |  | US | 1868 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1695 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1583 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1430 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1415 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | Salt Lake City International Airport |  | US | 1362 |
| 15 | El Dorado International Airport |  | CO | 1362 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1292 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1228 |
| 19 | Madrid Barajas International Airport |  | ES | 1208 |
| 20 | Capua Airport |  | IT | 1205 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1172 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1076 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1066 |
| 26 | Charles de Gaulle International Airport |  | FR | 1038 |
| 27 | Bengaluru International Airport |  | IN | 1012 |
| 28 | Malpensa International Airport |  | IT | 990 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 917 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 906 |
| 32 | Barcelona International Airport |  | ES | 906 |
| 33 | Daniel K Inouye International Airport |  | US | 904 |
| 34 | Tenerife Norte Airport |  | ES | 871 |
| 35 | Seattle-Tacoma International Airport |  | US | 866 |
| 36 | Calgary International Airport |  | CA | 858 |
| 37 | Scottsdale Airport |  | US | 854 |
| 38 | Viracopos International Airport |  | BR | 853 |
| 39 | Amsterdam Airport Schiphol |  | NL | 838 |
| 40 | Oslo Gardermoen Airport |  | NO | 830 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 803 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 548 | 21m | 244 km | 2,307.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 179 | 30m | 49 km | 151.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 177 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 165 | 51m | 556 km | 1,581.7 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N71PM |  | Camp Bullis Als (Cals) Airport (9TX5) | Kestrel Airpark (K1T7) | 2026-07-25 21:34 UTC | 2026-07-25 21:48 UTC | 13m |
| AAL2672 | American Airlines | John Wayne/Orange County Airport (KSNA) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-25 19:04 UTC | 2026-07-25 21:42 UTC | 2h 38m |
| TKR140 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-25 21:29 UTC | 2026-07-25 21:42 UTC | 12m |
| N80616 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-25 20:42 UTC | 2026-07-25 21:40 UTC | 58m |
| N29EF |  | Princeton Airport (K39N) | Lancaster Airport (KLNS) | 2026-07-25 20:56 UTC | 2026-07-25 21:38 UTC | 41m |
| N4230H |  | Daniel K Inouye International Airport (PHNL) | Daniel K Inouye International Airport (PHNL) | 2026-07-25 21:34 UTC | 2026-07-25 21:36 UTC | 1m |
| N9424E |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-25 20:45 UTC | 2026-07-25 21:34 UTC | 49m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-07-25 21:18 UTC | 2026-07-25 21:31 UTC | 12m |
| TKR183 | TKR | Boise Air Trml/Gowen Field (KBOI) | Crowley Ranch Airstrip (78OR) | 2026-07-25 21:17 UTC | 2026-07-25 21:30 UTC | 13m |
| N9737V |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-25 20:38 UTC | 2026-07-25 21:24 UTC | 45m |
| N884WE |  | Santa Barbara Municipal Airport (KSBA) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-25 16:19 UTC | 2026-07-25 21:22 UTC | 5h 3m |
| UAL967 | United Airlines | Napoli / Capodichino International Airport (LIRN) | Newark Liberty International Airport (KEWR) | 2026-07-25 12:34 UTC | 2026-07-25 21:19 UTC | 8h 45m |
| N206WX |  | Henry County Airport (K7W5) | Nietz Airport (6OH7) | 2026-07-25 21:02 UTC | 2026-07-25 21:15 UTC | 13m |
| FTO381 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-07-25 20:42 UTC | 2026-07-25 21:13 UTC | 30m |
| N3NJ |  | Morristown Municipal Airport (KMMU) | Morristown Municipal Airport (KMMU) | 2026-07-25 21:07 UTC | 2026-07-25 21:12 UTC | 5m |
| N36HF |  | Morehaven Airport (MA43) | KHTO (KHTO) | 2026-07-25 20:42 UTC | 2026-07-25 21:09 UTC | 26m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-25 20:50 UTC | 2026-07-25 21:07 UTC | 16m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-25 20:05 UTC | 2026-07-25 21:06 UTC | 1h 1m |
| TKR01 | TKR | Boise Air Trml/Gowen Field (KBOI) | Payette Municipal Airport (KS75) | 2026-07-25 20:57 UTC | 2026-07-25 21:05 UTC | 7m |
| N42BG |  | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-07-25 20:27 UTC | 2026-07-25 21:05 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
