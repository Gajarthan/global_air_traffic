# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_14:37:14_UTC-green)

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

**Latest saved flight:** 2026-08-12 14:37:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 14:37:14 UTC

- **189,483** saved flights
- **59,887** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,483** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,269,445.2 tonnes** estimated CO2 emissions
- **131,562,040 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7517 |
| 2 | SkyWest Airlines | 6864 |
| 3 | EJA | 3728 |
| 4 | IndiGo | 3300 |
| 5 | Southwest Airlines | 2957 |
| 6 | American Airlines | 2935 |
| 7 | ENY | 2345 |
| 8 | Delta Air Lines | 2223 |
| 9 | LATAM Airlines | 1772 |
| 10 | AZU | 1707 |
| 11 | Lufthansa | 1654 |
| 12 | Vueling | 1574 |
| 13 | WIF | 1570 |
| 14 | LXJ | 1479 |
| 15 | easyJet | 1305 |
| 16 | Swiss International | 1292 |
| 17 | AXM | 1253 |
| 18 | EJU | 1168 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1047 |
| 23 | GLO | 1019 |
| 24 | Air France | 987 |
| 25 | PGT | 977 |
| 26 | AEE | 972 |
| 27 | United Airlines | 971 |
| 28 | CXK | 967 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 940 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161402 |
| 2 | 🇪🇸 ES | 12217 |
| 3 | 🇧🇷 BR | 10877 |
| 4 | 🇦🇺 AU | 10650 |
| 5 | 🇨🇦 CA | 10354 |
| 6 | 🇮🇳 IN | 10345 |
| 7 | 🇮🇹 IT | 9828 |
| 8 | 🇩🇪 DE | 9369 |
| 9 | 🇬🇧 GB | 8826 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7579 |
| 12 | 🇨🇴 CO | 7223 |
| 13 | 🇬🇷 GR | 5548 |
| 14 | 🇲🇽 MX | 5387 |
| 15 | 🇨🇭 CH | 5090 |
| 16 | 🇹🇷 TR | 5036 |
| 17 | 🇳🇴 NO | 4877 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3186 |
| 20 | 🇵🇱 PL | 3137 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2506 |
| 24 | 🇬🇹 GT | 2403 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1932 |
| 27 | 🇲🇦 MA | 1924 |
| 28 | 🇳🇱 NL | 1693 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3925 |
| 2 | Denver International Airport |  | US | 3117 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Indira Gandhi International Airport |  | IN | 2331 |
| 5 | Guaymaral Airport |  | CO | 2328 |
| 6 | Harry Reid International Airport |  | US | 2214 |
| 7 | Zurich Airport |  | CH | 2014 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2007 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1958 |
| 10 | La Aurora Airport |  | GT | 1847 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1703 |
| 13 | Salt Lake City International Airport |  | US | 1681 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1623 |
| 16 | Congonhas Airport |  | BR | 1581 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1492 |
| 19 | Capua Airport |  | IT | 1473 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1470 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1356 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1304 |
| 25 | Charles de Gaulle International Airport |  | FR | 1295 |
| 26 | Charlotte/Douglas International Airport |  | US | 1267 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1221 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1186 |
| 30 | Ninoy Aquino International Airport |  | PH | 1184 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1136 |
| 33 | Viracopos International Airport |  | BR | 1097 |
| 34 | Reno/Tahoe International Airport |  | US | 1094 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1079 |
| 37 | Daniel K Inouye International Airport |  | US | 1065 |
| 38 | Oslo Gardermoen Airport |  | NO | 1058 |
| 39 | Tenerife Norte Airport |  | ES | 1041 |
| 40 | Vitoria/Foronda Airport |  | ES | 1028 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 960 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 693 | 21m | 244 km | 2,918.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 441 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 317 | 27m | 275 km | 1,502.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 308 | 14m | 114 km | 604.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 291 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 274 | 22m | 55 km | 260.4 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 272 | 1h 49m | 1,423 km | 6,675.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 252 | 20m | 250 km | 1,088.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 236 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 226 | 19m | 144 km | 562.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 223 | 24m | 218 km | 840.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 207 | 1h 48m | 1,304 km | 4,657.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N801FA |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-08-12 14:09 UTC | 2026-08-12 14:37 UTC | 28m |
| A7GQB |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-12 11:51 UTC | 2026-08-12 14:32 UTC | 2h 41m |
| ETD8JZ | Etihad Airways | Václav Havel Airport (LKPR) | Abu Dhabi International Airport (OMAA) | 2026-08-12 09:21 UTC | 2026-08-12 14:32 UTC | 5h 11m |
| 96FUJ |  | Fujairah International Airport (OMFJ) | Ras Al Khaimah International Airport (OMRK) | 2026-08-12 13:55 UTC | 2026-08-12 14:31 UTC | 35m |
| HSORJ5 | HSO | De Kooy Airport (EHKD) | De Kooy Airport (EHKD) | 2026-08-12 14:16 UTC | 2026-08-12 14:29 UTC | 13m |
| N268DS |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Williamson/Sodus Airport (KSDC) | 2026-08-12 13:41 UTC | 2026-08-12 14:28 UTC | 46m |
| N34EF |  | Lehigh Valley International Airport (KABE) | Lancaster Airport (KLNS) | 2026-08-12 14:00 UTC | 2026-08-12 14:28 UTC | 28m |
| PNTHR76 | PNT | Middle Wallop Airfield (EGVP) | Middle Wallop Airfield (EGVP) | 2026-08-12 13:07 UTC | 2026-08-12 14:26 UTC | 1h 19m |
| N1401E |  | Usaf Academy Davis Airfield (KAFF) | High Plains Airport Airport (CD15) | 2026-08-12 13:54 UTC | 2026-08-12 14:19 UTC | 25m |
| NSZ4381 | NSZ | Stockholm-Arlanda Airport (ESSA) | Vainode Airport (EVFA) | 2026-08-12 13:42 UTC | 2026-08-12 14:15 UTC | 33m |
| OEKHI | OEK | Memmingen Allgau Airport (EDJA) | Friedrichshafen Airport (EDNY) | 2026-08-12 13:13 UTC | 2026-08-12 14:15 UTC | 1h 1m |
| LDX11 | LDX | Blackpool International Airport (EGNH) | Keflavik International Airport (BIKF) | 2026-08-12 12:00 UTC | 2026-08-12 14:14 UTC | 2h 14m |
| N476SP |  | Greenwood Lake Airport (K4N1) | Bridgeport/Sikorsky Airport (KBDR) | 2026-08-12 13:41 UTC | 2026-08-12 14:14 UTC | 32m |
| N9137H |  | Old Bridge Airport (K3N6) | Old Bridge Airport (K3N6) | 2026-08-12 13:12 UTC | 2026-08-12 14:12 UTC | 1h 0m |
| N552TJ |  | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-08-12 14:07 UTC | 2026-08-12 14:09 UTC | 1m |
| N325F |  | Telluride Regional Airport (KTEX) | Hopkins Field (KAIB) | 2026-08-12 13:32 UTC | 2026-08-12 14:09 UTC | 36m |
| N421JJ |  | Hanford Municipal Airport (KHJO) | Meadows Field (KBFL) | 2026-08-12 13:38 UTC | 2026-08-12 14:09 UTC | 31m |
| N664JH |  | Laurence G Hanscom Field (KBED) | Fitchburg Municipal Airport (KFIT) | 2026-08-12 13:34 UTC | 2026-08-12 14:07 UTC | 33m |
| N678SS |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-08-12 13:45 UTC | 2026-08-12 14:07 UTC | 21m |
| HK5463G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-12 14:04 UTC | 2026-08-12 14:07 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
