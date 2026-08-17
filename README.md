# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_03:58:15_UTC-green)

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

**Latest saved flight:** 2026-08-17 03:58:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 03:58:15 UTC

- **207,001** saved flights
- **65,941** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,001** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,489,294.0 tonnes** estimated CO2 emissions
- **144,306,897 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8147 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4037 |
| 4 | IndiGo | 3535 |
| 5 | American Airlines | 3454 |
| 6 | Southwest Airlines | 3327 |
| 7 | Delta Air Lines | 2666 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1347 |
| 18 | United Airlines | 1304 |
| 19 | Alaska Airlines | 1285 |
| 20 | QLK | 1276 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1254 |
| 23 | VIV | 1143 |
| 24 | GLO | 1121 |
| 25 | PGT | 1104 |
| 26 | Air France | 1103 |
| 27 | JetBlue | 1062 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176018 |
| 2 | 🇪🇸 ES | 13187 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11605 |
| 5 | 🇨🇦 CA | 11452 |
| 6 | 🇮🇳 IN | 11022 |
| 7 | 🇮🇹 IT | 10770 |
| 8 | 🇩🇪 DE | 10209 |
| 9 | 🇬🇧 GB | 9629 |
| 10 | 🇯🇵 JP | 8519 |
| 11 | 🇨🇴 CO | 8243 |
| 12 | 🇫🇷 FR | 8167 |
| 13 | 🇬🇷 GR | 6071 |
| 14 | 🇹🇷 TR | 5863 |
| 15 | 🇲🇽 MX | 5839 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3547 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3405 |
| 21 | 🇹🇭 TH | 3268 |
| 22 | 🇳🇿 NZ | 2869 |
| 23 | 🇵🇭 PH | 2749 |
| 24 | 🇬🇹 GT | 2648 |
| 25 | 🇰🇷 KR | 2520 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2082 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1744 |
| 30 | 🇮🇩 ID | 1710 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4364 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2568 |
| 4 | Indira Gandhi International Airport |  | IN | 2501 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2152 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2017 |
| 11 | Chicago O'Hare International Airport |  | US | 1920 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1854 |
| 14 | Salt Lake City International Airport |  | US | 1837 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1619 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1451 |
| 24 | Malpensa International Airport |  | IT | 1425 |
| 25 | Charlotte/Douglas International Airport |  | US | 1413 |
| 26 | Charles de Gaulle International Airport |  | FR | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1314 |
| 28 | Ninoy Aquino International Airport |  | PH | 1303 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1280 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1258 |
| 32 | Seattle-Tacoma International Airport |  | US | 1235 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Daniel K Inouye International Airport |  | US | 1107 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 733 | 21m | 244 km | 3,086.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 505 | 1h 7m | 770 km | 6,708.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 483 | 24m | 225 km | 1,873.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 256 | 19m | 99 km | 438.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 245 | 1h 37m | 1,156 km | 4,887.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 236 | 31m | 369 km | 1,502.2 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXJ345 | LXJ | Chicago Executive Airport (KPWK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-16 23:47 UTC | 2026-08-17 03:58 UTC | 4h 10m |
| KUR | KUR | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 03:32 UTC | 2026-08-17 03:47 UTC | 15m |
| A7GQD |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-17 02:25 UTC | 2026-08-17 03:45 UTC | 1h 20m |
| ELY010 | ELY | John F Kennedy International Airport (KJFK) | Queen Alia International Airport (OJAI) | 2026-08-16 18:00 UTC | 2026-08-17 03:40 UTC | 9h 39m |
| YHH | YHH | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 03:22 UTC | 2026-08-17 03:38 UTC | 15m |
| JPT7 | JPT | Halim Perdanakusuma International Airport (WIHH) | Pondok Cabe Air Base (WIHP) | 2026-08-17 03:20 UTC | 2026-08-17 03:37 UTC | 16m |
| PVF | PVF | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 03:14 UTC | 2026-08-17 03:33 UTC | 18m |
| N360DA |  | Melbourne Moorabbin Airport (YMMB) | Benambra Airport (YBRA) | 2026-08-17 02:36 UTC | 2026-08-17 03:32 UTC | 55m |
| N991MH |  | Appalachee Bluff Riverfront Airpark (67GA) | Appalachee Bluff Riverfront Airpark (67GA) | 2026-08-17 02:32 UTC | 2026-08-17 03:24 UTC | 51m |
|  |  | Al Bateen Executive Airport (OMAD) | Ras Al Khaimah International Airport (OMRK) | 2026-08-17 02:37 UTC | 2026-08-17 03:18 UTC | 40m |
| SWA2826 | Southwest Airlines | Seattle-Tacoma International Airport (KSEA) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-17 01:30 UTC | 2026-08-17 03:16 UTC | 1h 45m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-17 02:51 UTC | 2026-08-17 03:15 UTC | 23m |
| QLK1573 | QLK | Gold Coast Airport (YBCG) | Melbourne International Airport (YMML) | 2026-08-17 01:14 UTC | 2026-08-17 03:06 UTC | 1h 51m |
| FD264 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-17 02:41 UTC | 2026-08-17 03:03 UTC | 22m |
| T77 |  | Serpentine Airport (YSEN) | Serpentine Airport (YSEN) | 2026-08-17 02:51 UTC | 2026-08-17 03:03 UTC | 12m |
| JAL2791 | Japan Airlines | Hakodate Airport (RJCH) | Aomori Airport (RJSA) | 2026-08-17 02:50 UTC | 2026-08-17 03:02 UTC | 12m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-08-17 01:58 UTC | 2026-08-17 03:00 UTC | 1h 1m |
| LXJ332 | LXJ | Harry Reid International Airport (KLAS) | Santa Fe Regional Airport (KSAF) | 2026-08-17 01:54 UTC | 2026-08-17 03:00 UTC | 1h 5m |
| ANA693 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-08-17 01:56 UTC | 2026-08-17 03:00 UTC | 1h 3m |
| FDA413 | FDA | Nagoya Airport (RJNA) | Izumo Airport (RJOC) | 2026-08-17 02:22 UTC | 2026-08-17 02:58 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
