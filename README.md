# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_04:01:40_UTC-green)

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

**Latest saved flight:** 2026-08-11 04:01:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 04:01:40 UTC

- **185,835** saved flights
- **59,012** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,835** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,229,765.1 tonnes** estimated CO2 emissions
- **129,261,744 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7354 |
| 2 | SkyWest Airlines | 6784 |
| 3 | EJA | 3675 |
| 4 | IndiGo | 3240 |
| 5 | Southwest Airlines | 2923 |
| 6 | American Airlines | 2901 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2191 |
| 9 | LATAM Airlines | 1739 |
| 10 | AZU | 1671 |
| 11 | Lufthansa | 1628 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1459 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1241 |
| 18 | EJU | 1146 |
| 19 | QLK | 1143 |
| 20 | All Nippon Airways | 1133 |
| 21 | Alaska Airlines | 1114 |
| 22 | VIV | 1026 |
| 23 | GLO | 997 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | United Airlines | 950 |
| 28 | Cathay Pacific | 947 |
| 29 | PGT | 947 |
| 30 | MXY | 922 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159002 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10675 |
| 4 | 🇦🇺 AU | 10368 |
| 5 | 🇨🇦 CA | 10161 |
| 6 | 🇮🇳 IN | 10160 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9154 |
| 9 | 🇬🇧 GB | 8608 |
| 10 | 🇯🇵 JP | 7557 |
| 11 | 🇫🇷 FR | 7406 |
| 12 | 🇨🇴 CO | 7026 |
| 13 | 🇬🇷 GR | 5439 |
| 14 | 🇲🇽 MX | 5311 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4872 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3236 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3092 |
| 21 | 🇹🇭 TH | 2872 |
| 22 | 🇳🇿 NZ | 2647 |
| 23 | 🇵🇭 PH | 2452 |
| 24 | 🇬🇹 GT | 2373 |
| 25 | 🇰🇷 KR | 2302 |
| 26 | 🇲🇦 MA | 1878 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3864 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2341 |
| 4 | Indira Gandhi International Airport |  | IN | 2283 |
| 5 | Guaymaral Airport |  | CO | 2273 |
| 6 | Harry Reid International Airport |  | US | 2181 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1931 |
| 10 | La Aurora Airport |  | GT | 1821 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1672 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1597 |
| 16 | Congonhas Airport |  | BR | 1553 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1329 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1295 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1266 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1212 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1163 |
| 30 | Ninoy Aquino International Airport |  | PH | 1157 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1142 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Reno/Tahoe International Airport |  | US | 1072 |
| 34 | Seattle-Tacoma International Airport |  | US | 1071 |
| 35 | Viracopos International Airport |  | BR | 1070 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1056 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 684 | 21m | 244 km | 2,880.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 448 | 1h 7m | 770 km | 5,951.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 431 | 24m | 225 km | 1,672.1 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 263 | 1h 49m | 1,423 km | 6,454.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 221 | 1h 38m | 1,156 km | 4,408.9 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 217 | 31m | 369 km | 1,381.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EFC13C | EFC | Al Saqr Field (OMRS) | Ras Al Khaimah International Airport (OMRK) | 2026-08-11 03:48 UTC | 2026-08-11 04:01 UTC | 13m |
| N291CB |  | Riverside Airport (KRAL) | Whiteman Airport (KWHP) | 2026-08-11 03:08 UTC | 2026-08-11 03:43 UTC | 35m |
| N739TS |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-08-11 03:13 UTC | 2026-08-11 03:43 UTC | 29m |
| ANA247 | All Nippon Airways | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-11 02:39 UTC | 2026-08-11 03:42 UTC | 1h 3m |
| HRCLS63 | HRC | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-11 03:04 UTC | 2026-08-11 03:41 UTC | 36m |
| ELY5461 | ELY | Ben Gurion International Airport (LLBG) | Diagoras Airport (LGRP) | 2026-08-11 02:23 UTC | 2026-08-11 03:34 UTC | 1h 10m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-11 03:04 UTC | 2026-08-11 03:30 UTC | 26m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-11 02:10 UTC | 2026-08-11 03:20 UTC | 1h 10m |
| OXK | OXK | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-11 03:10 UTC | 2026-08-11 03:20 UTC | 10m |
| AAL3159 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-11 01:26 UTC | 2026-08-11 03:18 UTC | 1h 51m |
| N727KT |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-11 02:53 UTC | 2026-08-11 03:17 UTC | 24m |
| JAL2791 | Japan Airlines | Hakodate Airport (RJCH) | Aomori Airport (RJSA) | 2026-08-11 03:05 UTC | 2026-08-11 03:17 UTC | 11m |
| SCU19 | SCU | William R Pogue Municipal Airport (KOWP) | Tulsa International Airport (KTUL) | 2026-08-11 02:51 UTC | 2026-08-11 03:14 UTC | 23m |
| BLINR17 | BLI | Travis Afb Airport (KSUU) | Travis Afb Airport (KSUU) | 2026-08-11 02:23 UTC | 2026-08-11 03:13 UTC | 50m |
| 8L8 |  | Sydney Bankstown Airport (YSBK) | Walgett Airport (YWLG) | 2026-08-11 02:06 UTC | 2026-08-11 03:12 UTC | 1h 5m |
| 8QMBE |  | Dharavandhoo Airport (VRMD) | Dharavandhoo Airport (VRMD) | 2026-08-11 03:10 UTC | 2026-08-11 03:11 UTC | 1m |
| N722WD |  | Rocky Mountain Metro Airport (KBJC) | Laramie Regional Airport (KLAR) | 2026-08-11 02:38 UTC | 2026-08-11 03:10 UTC | 31m |
| N510PR |  | Talkeetna Village Strip (AK44) | Nugget Bench Airport (33AK) | 2026-08-11 02:21 UTC | 2026-08-11 03:09 UTC | 47m |
| N4632F |  | Rocky Mountain Metro Airport (KBJC) | Mertens Airport (3CO2) | 2026-08-11 02:17 UTC | 2026-08-11 03:08 UTC | 50m |
| TKR181 | TKR | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-08-11 02:57 UTC | 2026-08-11 03:07 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
