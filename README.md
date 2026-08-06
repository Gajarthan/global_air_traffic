# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_23:57:15_UTC-green)

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

**Latest saved flight:** 2026-08-05 23:57:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 23:57:15 UTC

- **173,507** saved flights
- **56,265** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,507** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,089,748.8 tonnes** estimated CO2 emissions
- **121,144,860 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6886 |
| 2 | SkyWest Airlines | 6369 |
| 3 | EJA | 3450 |
| 4 | IndiGo | 3031 |
| 5 | Southwest Airlines | 2741 |
| 6 | American Airlines | 2731 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2060 |
| 9 | LATAM Airlines | 1605 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1533 |
| 12 | WIF | 1448 |
| 13 | Vueling | 1428 |
| 14 | LXJ | 1361 |
| 15 | AXM | 1185 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1175 |
| 18 | EJU | 1059 |
| 19 | QLK | 1057 |
| 20 | Alaska Airlines | 1056 |
| 21 | All Nippon Airways | 1046 |
| 22 | VIV | 953 |
| 23 | Cathay Pacific | 938 |
| 24 | CXK | 924 |
| 25 | GLO | 914 |
| 26 | United Airlines | 904 |
| 27 | AEE | 903 |
| 28 | Air France | 888 |
| 29 | MXY | 880 |
| 30 | JetBlue | 867 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149694 |
| 2 | 🇪🇸 ES | 11093 |
| 3 | 🇧🇷 BR | 9883 |
| 4 | 🇦🇺 AU | 9675 |
| 5 | 🇮🇳 IN | 9509 |
| 6 | 🇨🇦 CA | 9506 |
| 7 | 🇮🇹 IT | 8946 |
| 8 | 🇩🇪 DE | 8585 |
| 9 | 🇬🇧 GB | 8029 |
| 10 | 🇯🇵 JP | 6948 |
| 11 | 🇫🇷 FR | 6869 |
| 12 | 🇨🇴 CO | 6399 |
| 13 | 🇬🇷 GR | 5030 |
| 14 | 🇲🇽 MX | 4967 |
| 15 | 🇨🇭 CH | 4566 |
| 16 | 🇳🇴 NO | 4507 |
| 17 | 🇹🇷 TR | 4247 |
| 18 | 🇲🇾 MY | 3083 |
| 19 | 🇵🇱 PL | 2896 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2532 |
| 22 | 🇳🇿 NZ | 2508 |
| 23 | 🇵🇭 PH | 2284 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2175 |
| 26 | 🇲🇦 MA | 1742 |
| 27 | 🇭🇷 HR | 1673 |
| 28 | 🇲🇪 ME | 1586 |
| 29 | 🇳🇱 NL | 1564 |
| 30 | 🇲🇴 MO | 1499 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2880 |
| 3 | Tokyo International Airport |  | JP | 2174 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2119 |
| 6 | Harry Reid International Airport |  | US | 2077 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1883 |
| 8 | Zurich Airport |  | CH | 1832 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1824 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1580 |
| 13 | Chicago O'Hare International Airport |  | US | 1572 |
| 14 | Salt Lake City International Airport |  | US | 1559 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1499 |
| 17 | Congonhas Airport |  | BR | 1430 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1419 |
| 19 | Capua Airport |  | IT | 1351 |
| 20 | Madrid Barajas International Airport |  | ES | 1349 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1221 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1206 |
| 24 | Charlotte/Douglas International Airport |  | US | 1199 |
| 25 | Charles de Gaulle International Airport |  | FR | 1175 |
| 26 | Malpensa International Airport |  | IT | 1174 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1076 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1070 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Seattle-Tacoma International Airport |  | US | 1003 |
| 34 | Daniel K Inouye International Airport |  | US | 1001 |
| 35 | Reno/Tahoe International Airport |  | US | 987 |
| 36 | Calgary International Airport |  | CA | 987 |
| 37 | Viracopos International Airport |  | BR | 985 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 945 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 633 | 21m | 244 km | 2,665.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 393 | 1h 8m | 770 km | 5,220.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 260 | 22m | 55 km | 247.1 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 201 | 1h 38m | 1,156 km | 4,009.9 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 201 | 31m | 369 km | 1,279.4 t |
| 27 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 200 | 8m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZHJ | ZHJ | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-05 23:35 UTC | 2026-08-05 23:57 UTC | 21m |
| TSR | TSR | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-05 23:40 UTC | 2026-08-05 23:55 UTC | 14m |
| SYH1410 | SYH | Laurence G Hanscom Field (KBED) | Bangor International Airport (KBGR) | 2026-08-05 22:38 UTC | 2026-08-05 23:50 UTC | 1h 11m |
| N737EE |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-05 23:18 UTC | 2026-08-05 23:48 UTC | 30m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-08-05 12:48 UTC | 2026-08-05 23:47 UTC | 10h 59m |
| N62RJ |  | Bowman Field (KLOU) | Madison Regional Airport (KIMS) | 2026-08-05 23:08 UTC | 2026-08-05 23:40 UTC | 32m |
| ZKBJM | ZKB | Nelson Airport (NZNS) | Nelson Airport (NZNS) | 2026-08-05 23:06 UTC | 2026-08-05 23:39 UTC | 33m |
| NJM1933 | NJM | Salt Lake City International Airport (KSLC) | Mud Lake/West Jefferson County Airport (K1U2) | 2026-08-05 23:07 UTC | 2026-08-05 23:36 UTC | 29m |
| N792SP |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-08-05 23:21 UTC | 2026-08-05 23:36 UTC | 14m |
| CFR230 | CFR | Nevada County Airport (KGOO) | Truckee-Tahoe Airport (KTRK) | 2026-08-05 23:22 UTC | 2026-08-05 23:34 UTC | 11m |
| N1218Z |  | Schroon Lake Airport (K4B7) | Holmes County Airport (K10G) | 2026-08-05 20:25 UTC | 2026-08-05 23:27 UTC | 3h 2m |
| GEC8290 | GEC | Ben Gurion International Airport (LLBG) | HE12 (HE12) | 2026-08-05 22:39 UTC | 2026-08-05 23:26 UTC | 47m |
| TKR210 | TKR | Ohkay Owingeh Airport (KE14) | Jicarilla Apache Nation Airport (K24N) | 2026-08-05 23:14 UTC | 2026-08-05 23:25 UTC | 11m |
| FFL8109 | FFL | Raleigh-Durham International Airport (KRDU) | Sapelo Island Airport (08GA) | 2026-08-05 22:31 UTC | 2026-08-05 23:22 UTC | 51m |
| N3868U |  | Patrick Leahy Burlington International Airport (KBTV) | Franklin County State Airport (KFSO) | 2026-08-05 22:30 UTC | 2026-08-05 23:21 UTC | 50m |
| N990MF |  | Delaware Municipal/Jim Moore Field (KDLZ) | Lakes Of The North Airport (K4Y4) | 2026-08-05 22:32 UTC | 2026-08-05 23:18 UTC | 46m |
| ZHH | ZHH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-05 22:55 UTC | 2026-08-05 23:15 UTC | 20m |
| CRN911 | CRN | Vancouver International Airport (CYVR) | Banff Airport (CYBA) | 2026-08-05 22:18 UTC | 2026-08-05 23:15 UTC | 56m |
| N1SK |  | Nampa Municipal Airport (KMAN) | Mountain Home Municipal Airport (KU76) | 2026-08-05 22:54 UTC | 2026-08-05 23:14 UTC | 20m |
| ZFB | ZFB | Redcliffe Airport (YRED) | Brisbane Archerfield Airport (YBAF) | 2026-08-05 22:57 UTC | 2026-08-05 23:12 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
