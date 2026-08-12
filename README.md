# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_19:34:56_UTC-green)

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

**Latest saved flight:** 2026-08-12 19:34:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 19:34:56 UTC

- **190,485** saved flights
- **60,142** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,485** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,279,981.7 tonnes** estimated CO2 emissions
- **132,172,853 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7554 |
| 2 | SkyWest Airlines | 6896 |
| 3 | EJA | 3758 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2974 |
| 6 | American Airlines | 2952 |
| 7 | ENY | 2358 |
| 8 | Delta Air Lines | 2236 |
| 9 | LATAM Airlines | 1786 |
| 10 | AZU | 1717 |
| 11 | Lufthansa | 1658 |
| 12 | WIF | 1583 |
| 13 | Vueling | 1582 |
| 14 | LXJ | 1491 |
| 15 | easyJet | 1314 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1178 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1135 |
| 22 | VIV | 1051 |
| 23 | GLO | 1027 |
| 24 | Air France | 994 |
| 25 | PGT | 983 |
| 26 | AEE | 975 |
| 27 | CXK | 975 |
| 28 | United Airlines | 974 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 946 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162330 |
| 2 | 🇪🇸 ES | 12288 |
| 3 | 🇧🇷 BR | 10949 |
| 4 | 🇦🇺 AU | 10660 |
| 5 | 🇨🇦 CA | 10438 |
| 6 | 🇮🇳 IN | 10368 |
| 7 | 🇮🇹 IT | 9889 |
| 8 | 🇩🇪 DE | 9420 |
| 9 | 🇬🇧 GB | 8873 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7628 |
| 12 | 🇨🇴 CO | 7315 |
| 13 | 🇬🇷 GR | 5574 |
| 14 | 🇲🇽 MX | 5403 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5074 |
| 17 | 🇳🇴 NO | 4909 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3211 |
| 20 | 🇵🇱 PL | 3152 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2410 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1957 |
| 27 | 🇲🇦 MA | 1930 |
| 28 | 🇳🇱 NL | 1700 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3949 |
| 2 | Denver International Airport |  | US | 3128 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2355 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2221 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2016 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1969 |
| 10 | La Aurora Airport |  | GT | 1853 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1723 |
| 12 | El Dorado International Airport |  | CO | 1718 |
| 13 | Salt Lake City International Airport |  | US | 1691 |
| 14 | Chicago O'Hare International Airport |  | US | 1665 |
| 15 | Frankfurt am Main International Airport |  | DE | 1626 |
| 16 | Congonhas Airport |  | BR | 1591 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1504 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1476 |
| 20 | Capua Airport |  | IT | 1476 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1405 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1368 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1315 |
| 25 | Charles de Gaulle International Airport |  | FR | 1305 |
| 26 | Charlotte/Douglas International Airport |  | US | 1275 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1192 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1168 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1104 |
| 34 | Reno/Tahoe International Airport |  | US | 1097 |
| 35 | Seattle-Tacoma International Airport |  | US | 1095 |
| 36 | Calgary International Airport |  | CA | 1086 |
| 37 | Daniel K Inouye International Airport |  | US | 1070 |
| 38 | Oslo Gardermoen Airport |  | NO | 1066 |
| 39 | Tenerife Norte Airport |  | ES | 1044 |
| 40 | Vitoria/Foronda Airport |  | ES | 1034 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 973 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 698 | 21m | 244 km | 2,939.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 443 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 320 | 27m | 275 km | 1,516.3 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 300 | 8m | - | - |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 227 | 19m | 144 km | 564.7 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N484LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-12 17:22 UTC | 2026-08-12 19:34 UTC | 2h 12m |
| CXK444 | CXK | Hartford-Brainard Airport (KHFD) | Hartford-Brainard Airport (KHFD) | 2026-08-12 19:15 UTC | 2026-08-12 19:33 UTC | 17m |
| N542JJ |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-12 18:39 UTC | 2026-08-12 19:30 UTC | 51m |
| N3641R |  | Somerset Airport (KSMQ) | Central Jersey Regional Airport (K47N) | 2026-08-12 18:57 UTC | 2026-08-12 19:27 UTC | 30m |
| N88765 |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-12 18:57 UTC | 2026-08-12 19:25 UTC | 28m |
| N911TG |  | St Pete-Clearwater International Airport (KPIE) | Peter O Knight Airport (KTPF) | 2026-08-12 19:14 UTC | 2026-08-12 19:23 UTC | 9m |
| N727MZ |  | Oakland County International Airport (KPTK) | 69MI (69MI) | 2026-08-12 18:51 UTC | 2026-08-12 19:16 UTC | 24m |
| N5QD |  | 0PA0 (0PA0) | Gunden Airport (PS54) | 2026-08-12 19:14 UTC | 2026-08-12 19:14 UTC | 0m |
| N975GV |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-08-12 18:01 UTC | 2026-08-12 19:10 UTC | 1h 8m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-12 19:05 UTC | 2026-08-12 19:09 UTC | 3m |
| N271HP |  | Fort Worth Meacham International Airport (KFTW) | Kenneth Copeland Airport (K4T2) | 2026-08-12 18:23 UTC | 2026-08-12 19:07 UTC | 44m |
| N993CB |  | Chico Regional Airport (KCIC) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-12 18:28 UTC | 2026-08-12 19:07 UTC | 38m |
| GFD50 | GFD | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-08-12 18:36 UTC | 2026-08-12 19:06 UTC | 29m |
| N899NH |  | La Aurora Airport (MGGT) | Bananera Airport (MGBN) | 2026-08-12 18:45 UTC | 2026-08-12 19:05 UTC | 19m |
| TKR210 | TKR | Hill Afb Airport (KHIF) | Skypark Airport (KBTF) | 2026-08-12 19:01 UTC | 2026-08-12 19:04 UTC | 3m |
| AWH48K | AWH | Hannover Airport (EDDV) | London Biggin Hill Airport (EGKB) | 2026-08-12 17:52 UTC | 2026-08-12 19:01 UTC | 1h 8m |
| N135CK |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-08-12 18:49 UTC | 2026-08-12 19:00 UTC | 11m |
| HALCONES | Hawaiian Airlines | El Bosque Airport (SCBQ) | Estero Seco Airport (SCZE) | 2026-08-12 18:22 UTC | 2026-08-12 19:00 UTC | 38m |
| JRT59 | JRT | Mc Ghee Tyson Airport (KTYS) | Monmouth Executive Airport (KBLM) | 2026-08-12 17:30 UTC | 2026-08-12 18:59 UTC | 1h 28m |
| BCS5709 | BCS | Henri Coanda International Airport (LROP) | Malpensa International Airport (LIMC) | 2026-08-12 17:04 UTC | 2026-08-12 18:58 UTC | 1h 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
