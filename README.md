# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_01:41:26_UTC-green)

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

**Latest saved flight:** 2026-08-15 01:41:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 01:41:26 UTC

- **197,303** saved flights
- **61,888** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,355,594.0 tonnes** estimated CO2 emissions
- **136,556,172 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7836 |
| 2 | SkyWest Airlines | 7111 |
| 3 | EJA | 3894 |
| 4 | IndiGo | 3388 |
| 5 | Southwest Airlines | 3062 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2444 |
| 8 | Delta Air Lines | 2341 |
| 9 | LATAM Airlines | 1856 |
| 10 | AZU | 1789 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1568 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1280 |
| 18 | EJU | 1222 |
| 19 | QLK | 1212 |
| 20 | All Nippon Airways | 1188 |
| 21 | Alaska Airlines | 1169 |
| 22 | VIV | 1088 |
| 23 | GLO | 1069 |
| 24 | Air France | 1034 |
| 25 | PGT | 1026 |
| 26 | AEE | 1012 |
| 27 | United Airlines | 1007 |
| 28 | CXK | 1005 |
| 29 | WMT | 986 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 167982 |
| 2 | 🇪🇸 ES | 12718 |
| 3 | 🇧🇷 BR | 11376 |
| 4 | 🇦🇺 AU | 11047 |
| 5 | 🇨🇦 CA | 10820 |
| 6 | 🇮🇳 IN | 10594 |
| 7 | 🇮🇹 IT | 10271 |
| 8 | 🇩🇪 DE | 9773 |
| 9 | 🇬🇧 GB | 9252 |
| 10 | 🇯🇵 JP | 8004 |
| 11 | 🇫🇷 FR | 7845 |
| 12 | 🇨🇴 CO | 7786 |
| 13 | 🇬🇷 GR | 5787 |
| 14 | 🇲🇽 MX | 5589 |
| 15 | 🇹🇷 TR | 5376 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5042 |
| 18 | 🇲🇾 MY | 3348 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3252 |
| 21 | 🇹🇭 TH | 3036 |
| 22 | 🇳🇿 NZ | 2752 |
| 23 | 🇵🇭 PH | 2597 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2390 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1591 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4116 |
| 2 | Denver International Airport |  | US | 3216 |
| 3 | Tokyo International Airport |  | JP | 2455 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2393 |
| 6 | Harry Reid International Airport |  | US | 2267 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2079 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1809 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1757 |
| 14 | Chicago O'Hare International Airport |  | US | 1735 |
| 15 | Congonhas Airport |  | BR | 1665 |
| 16 | Frankfurt am Main International Airport |  | DE | 1663 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1506 |
| 20 | Capua Airport |  | IT | 1506 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1457 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1370 |
| 24 | Malpensa International Airport |  | IT | 1369 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1248 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1233 |
| 30 | Ninoy Aquino International Airport |  | PH | 1228 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1207 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1150 |
| 34 | Seattle-Tacoma International Airport |  | US | 1137 |
| 35 | Calgary International Airport |  | CA | 1124 |
| 36 | Reno/Tahoe International Airport |  | US | 1115 |
| 37 | Oslo Gardermoen Airport |  | NO | 1111 |
| 38 | Daniel K Inouye International Airport |  | US | 1097 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 724 | 21m | 244 km | 3,048.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 475 | 1h 7m | 770 km | 6,310.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 455 | 24m | 225 km | 1,765.2 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 337 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 284 | 1h 49m | 1,423 km | 6,969.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 281 | 22m | 55 km | 267.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 233 | 1h 38m | 1,156 km | 4,648.3 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 223 | 31m | 369 km | 1,419.5 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 48m | 1,304 km | 4,814.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CARGO39 | CAR | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Dothan Regional Airport (KDHN) | 2026-08-15 01:18 UTC | 2026-08-15 01:41 UTC | 23m |
| N415PW |  | Watsonville Municipal Airport (KWVI) | San Carlos Airport (KSQL) | 2026-08-15 01:23 UTC | 2026-08-15 01:40 UTC | 16m |
| N42148 |  | Chino Airport (KCNO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-15 00:22 UTC | 2026-08-15 01:38 UTC | 1h 15m |
| MAFFS6 | MAF | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-15 01:17 UTC | 2026-08-15 01:27 UTC | 10m |
| N149TH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-15 00:47 UTC | 2026-08-15 01:21 UTC | 33m |
| N94JA |  | Page Field (KFMY) | Punta Gorda Airport (KPGD) | 2026-08-15 00:56 UTC | 2026-08-15 01:20 UTC | 24m |
| N822F |  | Daniel K Inouye International Airport (PHNL) | Wheeler Army Air Field (PHHI) | 2026-08-15 00:59 UTC | 2026-08-15 01:16 UTC | 17m |
| XC6 |  | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-08-15 00:34 UTC | 2026-08-15 01:11 UTC | 36m |
| MNL99 | MNL | Palo Alto Airport (KPAO) | Gnoss Field (KDVO) | 2026-08-15 00:55 UTC | 2026-08-15 01:10 UTC | 15m |
| N56735 |  | Ohio State University Airport (KOSU) | Pigeon Airport (II16) | 2026-08-15 00:01 UTC | 2026-08-15 01:05 UTC | 1h 3m |
| N450PD |  | Roberts Field/Redmond Municipal Airport (KRDM) | Tracy Ranch Airport (ID88) | 2026-08-15 00:24 UTC | 2026-08-15 01:03 UTC | 39m |
| N501KT |  | Nashville International Airport (KBNA) | Auburn University Regional Airport (KAUO) | 2026-08-15 00:21 UTC | 2026-08-15 01:00 UTC | 39m |
| N2714F |  | Homer Airport (PAHO) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-14 23:49 UTC | 2026-08-15 01:00 UTC | 1h 11m |
| EPI243 | EPI | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-15 00:38 UTC | 2026-08-15 00:59 UTC | 21m |
| N25914 |  | Long Beach (Daugherty Field) Airport (KLGB) | San Gabriel Valley Airport (KEMT) | 2026-08-15 00:41 UTC | 2026-08-15 00:58 UTC | 16m |
| ZHH | ZHH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-08-15 00:28 UTC | 2026-08-15 00:53 UTC | 24m |
| SKW5978 | SkyWest Airlines | Denver International Airport (KDEN) | Harris River Ranch Airport (9CA7) | 2026-08-14 23:02 UTC | 2026-08-15 00:52 UTC | 1h 49m |
| UAE441 | Emirates | Adelaide International Airport (YPAD) | Fujairah International Airport (OMFJ) | 2026-08-14 12:28 UTC | 2026-08-15 00:46 UTC | 12h 17m |
| VOI3482 | VOI | Cancun International Airport (MMUN) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-08-14 22:58 UTC | 2026-08-15 00:44 UTC | 1h 46m |
| AVA9554 | Avianca | El Dorado International Airport (SKBO) | Fundacion Airport (SKFU) | 2026-08-14 23:43 UTC | 2026-08-15 00:42 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
