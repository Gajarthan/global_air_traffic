# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_02:39:48_UTC-green)

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

**Latest saved flight:** 2026-08-15 02:39:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 02:39:48 UTC

- **197,373** saved flights
- **61,900** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,373** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,356,389.0 tonnes** estimated CO2 emissions
- **136,602,261 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7836 |
| 2 | SkyWest Airlines | 7112 |
| 3 | EJA | 3894 |
| 4 | IndiGo | 3388 |
| 5 | Southwest Airlines | 3067 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2341 |
| 9 | LATAM Airlines | 1856 |
| 10 | AZU | 1789 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1569 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1329 |
| 17 | AXM | 1282 |
| 18 | EJU | 1222 |
| 19 | QLK | 1213 |
| 20 | All Nippon Airways | 1190 |
| 21 | Alaska Airlines | 1169 |
| 22 | VIV | 1089 |
| 23 | GLO | 1070 |
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
| 1 | 🇺🇸 US | 168027 |
| 2 | 🇪🇸 ES | 12718 |
| 3 | 🇧🇷 BR | 11378 |
| 4 | 🇦🇺 AU | 11061 |
| 5 | 🇨🇦 CA | 10828 |
| 6 | 🇮🇳 IN | 10599 |
| 7 | 🇮🇹 IT | 10271 |
| 8 | 🇩🇪 DE | 9774 |
| 9 | 🇬🇧 GB | 9252 |
| 10 | 🇯🇵 JP | 8013 |
| 11 | 🇫🇷 FR | 7845 |
| 12 | 🇨🇴 CO | 7792 |
| 13 | 🇬🇷 GR | 5787 |
| 14 | 🇲🇽 MX | 5594 |
| 15 | 🇹🇷 TR | 5378 |
| 16 | 🇨🇭 CH | 5315 |
| 17 | 🇳🇴 NO | 5044 |
| 18 | 🇲🇾 MY | 3352 |
| 19 | 🇿🇦 ZA | 3320 |
| 20 | 🇵🇱 PL | 3253 |
| 21 | 🇹🇭 TH | 3040 |
| 22 | 🇳🇿 NZ | 2754 |
| 23 | 🇵🇭 PH | 2603 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2393 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1993 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1599 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3218 |
| 3 | Tokyo International Airport |  | JP | 2459 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2395 |
| 6 | Harry Reid International Airport |  | US | 2267 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2079 |
| 8 | Zurich Airport |  | CH | 2079 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1812 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1757 |
| 14 | Chicago O'Hare International Airport |  | US | 1735 |
| 15 | Congonhas Airport |  | BR | 1665 |
| 16 | Frankfurt am Main International Airport |  | DE | 1663 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1507 |
| 20 | Capua Airport |  | IT | 1506 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1457 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1370 |
| 24 | Malpensa International Airport |  | IT | 1369 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1250 |
| 28 | Bengaluru International Airport |  | IN | 1244 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1233 |
| 30 | Ninoy Aquino International Airport |  | PH | 1231 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1207 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1150 |
| 34 | Seattle-Tacoma International Airport |  | US | 1138 |
| 35 | Calgary International Airport |  | CA | 1124 |
| 36 | Reno/Tahoe International Airport |  | US | 1115 |
| 37 | Oslo Gardermoen Airport |  | NO | 1112 |
| 38 | Daniel K Inouye International Airport |  | US | 1097 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 724 | 21m | 244 km | 3,048.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 477 | 1h 7m | 770 km | 6,336.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 456 | 24m | 225 km | 1,769.1 t |
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
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 234 | 1h 38m | 1,156 km | 4,668.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 224 | 31m | 369 km | 1,425.8 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 48m | 1,304 km | 4,814.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NJL | NJL | RAAF Williams Point Cook Base (YMPC) | Melbourne Moorabbin Airport (YMMB) | 2026-08-15 02:25 UTC | 2026-08-15 02:39 UTC | 14m |
| SWA1938 | Southwest Airlines | William P Hobby Airport (KHOU) | Baker Airport (K0O2) | 2026-08-14 23:36 UTC | 2026-08-15 02:30 UTC | 2h 53m |
| TIV241 | TIV | Chicago Midway International Airport (KMDW) | Kingston Ranch Airport (04NV) | 2026-08-14 22:55 UTC | 2026-08-15 02:27 UTC | 3h 31m |
| LBQ792 | LBQ | Syracuse Hancock International Airport (KSYR) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-15 02:05 UTC | 2026-08-15 02:23 UTC | 17m |
| VAR413 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 00:50 UTC | 2026-08-15 02:19 UTC | 1h 29m |
| 231166 |  | Bacchus Marsh Airport (YBSS) | Bacchus Marsh Airport (YBSS) | 2026-08-15 01:56 UTC | 2026-08-15 02:19 UTC | 23m |
| NIJ | NIJ | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-15 01:50 UTC | 2026-08-15 02:15 UTC | 25m |
| N567FL |  | 7PA5 (7PA5) | Northeast Philadelphia Airport (KPNE) | 2026-08-15 00:43 UTC | 2026-08-15 02:08 UTC | 1h 25m |
| TRP2 | TRP | Maryland Airport (K2W5) | Joint Base Andrews Airport (KADW) | 2026-08-15 01:54 UTC | 2026-08-15 02:05 UTC | 10m |
| UBG161 | UBG | VGZR (VGZR) | Shah Mokhdum Airport (VGRJ) | 2026-08-15 01:36 UTC | 2026-08-15 02:03 UTC | 26m |
| TKR181 | TKR | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-15 01:48 UTC | 2026-08-15 01:59 UTC | 11m |
| THA241 | Thai Airways | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 2026-08-15 01:05 UTC | 2026-08-15 01:46 UTC | 41m |
| SPIKR20 | SPI | 0TS2 (0TS2) | Albany Municipal Airport (KT23) | 2026-08-15 01:31 UTC | 2026-08-15 01:46 UTC | 15m |
| QLK1253 | QLK | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-08-14 23:36 UTC | 2026-08-15 01:45 UTC | 2h 8m |
| CARGO39 | CAR | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Dothan Regional Airport (KDHN) | 2026-08-15 01:18 UTC | 2026-08-15 01:41 UTC | 23m |
| N145EA |  | Jirik Field (OL23) | Central Colorado Regional Airport (KAEJ) | 2026-08-14 23:43 UTC | 2026-08-15 01:40 UTC | 1h 57m |
| N415PW |  | Watsonville Municipal Airport (KWVI) | San Carlos Airport (KSQL) | 2026-08-15 01:23 UTC | 2026-08-15 01:40 UTC | 16m |
| COOL48 | COO | 0TS2 (0TS2) | Albany Municipal Airport (KT23) | 2026-08-15 01:23 UTC | 2026-08-15 01:39 UTC | 15m |
| VIV9405 | VIV | General Mariano Escobedo International Airport (MMMY) | Santa Lucia Air Force Base (MMSM) | 2026-08-15 00:38 UTC | 2026-08-15 01:39 UTC | 1h 0m |
| N42148 |  | Chino Airport (KCNO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-15 00:22 UTC | 2026-08-15 01:38 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
