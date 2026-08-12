# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_23:41:57_UTC-green)

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

**Latest saved flight:** 2026-08-12 23:41:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 23:41:57 UTC

- **191,106** saved flights
- **60,308** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,106** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,287,245.2 tonnes** estimated CO2 emissions
- **132,593,923 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7581 |
| 2 | SkyWest Airlines | 6924 |
| 3 | EJA | 3780 |
| 4 | IndiGo | 3310 |
| 5 | Southwest Airlines | 2988 |
| 6 | American Airlines | 2968 |
| 7 | ENY | 2372 |
| 8 | Delta Air Lines | 2248 |
| 9 | LATAM Airlines | 1795 |
| 10 | AZU | 1729 |
| 11 | Lufthansa | 1661 |
| 12 | Vueling | 1584 |
| 13 | WIF | 1584 |
| 14 | LXJ | 1504 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1179 |
| 19 | QLK | 1169 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1138 |
| 22 | VIV | 1053 |
| 23 | GLO | 1033 |
| 24 | Air France | 995 |
| 25 | PGT | 987 |
| 26 | CXK | 981 |
| 27 | United Airlines | 977 |
| 28 | AEE | 975 |
| 29 | WMT | 949 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163064 |
| 2 | 🇪🇸 ES | 12303 |
| 3 | 🇧🇷 BR | 11010 |
| 4 | 🇦🇺 AU | 10672 |
| 5 | 🇨🇦 CA | 10484 |
| 6 | 🇮🇳 IN | 10369 |
| 7 | 🇮🇹 IT | 9919 |
| 8 | 🇩🇪 DE | 9442 |
| 9 | 🇬🇧 GB | 8895 |
| 10 | 🇯🇵 JP | 7771 |
| 11 | 🇫🇷 FR | 7634 |
| 12 | 🇨🇴 CO | 7371 |
| 13 | 🇬🇷 GR | 5579 |
| 14 | 🇲🇽 MX | 5413 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5094 |
| 17 | 🇳🇴 NO | 4913 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3214 |
| 20 | 🇵🇱 PL | 3156 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2688 |
| 23 | 🇵🇭 PH | 2514 |
| 24 | 🇬🇹 GT | 2418 |
| 25 | 🇰🇷 KR | 2335 |
| 26 | 🇭🇷 HR | 1964 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1705 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3978 |
| 2 | Denver International Airport |  | US | 3138 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2227 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2018 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1859 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 12 | El Dorado International Airport |  | CO | 1729 |
| 13 | Salt Lake City International Airport |  | US | 1699 |
| 14 | Chicago O'Hare International Airport |  | US | 1675 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | Capua Airport |  | IT | 1481 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1479 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1412 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1374 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1318 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1277 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1225 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1194 |
| 30 | Ninoy Aquino International Airport |  | PH | 1188 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1174 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1112 |
| 34 | Seattle-Tacoma International Airport |  | US | 1102 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1093 |
| 37 | Daniel K Inouye International Airport |  | US | 1072 |
| 38 | Oslo Gardermoen Airport |  | NO | 1068 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 700 | 21m | 244 km | 2,947.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 443 | 24m | 225 km | 1,718.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 321 | 27m | 275 km | 1,521.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 284 | 44m | 241 km | 1,179.7 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 274 | 1h 49m | 1,423 km | 6,724.4 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 256 | 20m | 250 km | 1,105.8 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 239 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 228 | 24m | 218 km | 859.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N317KC |  | Merrill Field (PAMR) | Juneau International Airport (PAJN) | 2026-08-12 20:41 UTC | 2026-08-12 23:41 UTC | 3h 0m |
| AER171 | AER | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-08-12 23:04 UTC | 2026-08-12 23:37 UTC | 32m |
| N520HH |  | Mckinney Ntl Airport (KTKI) | 4 S Ranch Airport (TS25) | 2026-08-12 23:01 UTC | 2026-08-12 23:37 UTC | 35m |
| N125MG |  | Shaniko Cattle Airport (OG54) | Ochs Private Airport (72OR) | 2026-08-12 23:18 UTC | 2026-08-12 23:34 UTC | 16m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-12 23:23 UTC | 2026-08-12 23:33 UTC | 10m |
| TKR104 | TKR | 46CO (46CO) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-12 23:18 UTC | 2026-08-12 23:29 UTC | 10m |
| N761AZ |  | 0NJ5 (0NJ5) | Solberg/Hunterdon Airport (KN51) | 2026-08-12 22:39 UTC | 2026-08-12 23:28 UTC | 49m |
| FGD561 | FGD | Abbotsford Airport (CYXX) | Merritt Airport (CAD5) | 2026-08-12 23:01 UTC | 2026-08-12 23:28 UTC | 26m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-08-12 23:22 UTC | 2026-08-12 23:24 UTC | 2m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-08-12 21:36 UTC | 2026-08-12 23:22 UTC | 1h 46m |
| N26WR |  | Santa Ynez/Kunkle Field (KIZA) | Santa Monica Municipal Airport (KSMO) | 2026-08-12 22:50 UTC | 2026-08-12 23:18 UTC | 27m |
| N3144V |  | Napa County Airport (KAPC) | Stockton Metro Airport (KSCK) | 2026-08-12 22:39 UTC | 2026-08-12 23:15 UTC | 35m |
| N234WL |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-08-12 22:40 UTC | 2026-08-12 23:15 UTC | 34m |
| SWA1162 | Southwest Airlines | Orlando International Airport (KMCO) | Dallas Love Field (KDAL) | 2026-08-12 20:59 UTC | 2026-08-12 23:14 UTC | 2h 14m |
| N8519V |  | Holland Field (1IL9) | Holland Field (1IL9) | 2026-08-12 22:09 UTC | 2026-08-12 23:13 UTC | 1h 3m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-08-12 22:36 UTC | 2026-08-12 23:11 UTC | 34m |
| JCY301 | JCY | Austin-Bergstrom International Airport (KAUS) | Portland-Hillsboro Airport (KHIO) | 2026-08-12 19:37 UTC | 2026-08-12 23:11 UTC | 3h 34m |
| TKR210 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-12 22:25 UTC | 2026-08-12 23:10 UTC | 44m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-08-12 22:29 UTC | 2026-08-12 23:10 UTC | 40m |
| N893AP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-12 22:41 UTC | 2026-08-12 23:09 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
