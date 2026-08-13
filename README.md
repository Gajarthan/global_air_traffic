# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_01:28:32_UTC-green)

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

**Latest saved flight:** 2026-08-13 01:28:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 01:28:32 UTC

- **191,237** saved flights
- **60,343** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,237** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,288,363.4 tonnes** estimated CO2 emissions
- **132,658,745 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7581 |
| 2 | SkyWest Airlines | 6934 |
| 3 | EJA | 3784 |
| 4 | IndiGo | 3311 |
| 5 | Southwest Airlines | 2991 |
| 6 | American Airlines | 2970 |
| 7 | ENY | 2374 |
| 8 | Delta Air Lines | 2251 |
| 9 | LATAM Airlines | 1795 |
| 10 | AZU | 1729 |
| 11 | Lufthansa | 1661 |
| 12 | Vueling | 1584 |
| 13 | WIF | 1584 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1254 |
| 18 | EJU | 1179 |
| 19 | QLK | 1170 |
| 20 | All Nippon Airways | 1156 |
| 21 | Alaska Airlines | 1139 |
| 22 | VIV | 1054 |
| 23 | GLO | 1033 |
| 24 | Air France | 995 |
| 25 | PGT | 988 |
| 26 | CXK | 983 |
| 27 | United Airlines | 977 |
| 28 | AEE | 975 |
| 29 | WMT | 949 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163228 |
| 2 | 🇪🇸 ES | 12303 |
| 3 | 🇧🇷 BR | 11010 |
| 4 | 🇦🇺 AU | 10692 |
| 5 | 🇨🇦 CA | 10492 |
| 6 | 🇮🇳 IN | 10371 |
| 7 | 🇮🇹 IT | 9919 |
| 8 | 🇩🇪 DE | 9442 |
| 9 | 🇬🇧 GB | 8897 |
| 10 | 🇯🇵 JP | 7781 |
| 11 | 🇫🇷 FR | 7634 |
| 12 | 🇨🇴 CO | 7375 |
| 13 | 🇬🇷 GR | 5580 |
| 14 | 🇲🇽 MX | 5418 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5099 |
| 17 | 🇳🇴 NO | 4915 |
| 18 | 🇲🇾 MY | 3278 |
| 19 | 🇿🇦 ZA | 3214 |
| 20 | 🇵🇱 PL | 3157 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2692 |
| 23 | 🇵🇭 PH | 2518 |
| 24 | 🇬🇹 GT | 2422 |
| 25 | 🇰🇷 KR | 2335 |
| 26 | 🇭🇷 HR | 1964 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1705 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3980 |
| 2 | Denver International Airport |  | US | 3141 |
| 3 | Tokyo International Airport |  | JP | 2400 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2228 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2018 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1861 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 12 | El Dorado International Airport |  | CO | 1729 |
| 13 | Salt Lake City International Airport |  | US | 1707 |
| 14 | Chicago O'Hare International Airport |  | US | 1678 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1481 |
| 20 | Capua Airport |  | IT | 1481 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1413 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1374 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1327 |
| 24 | Malpensa International Airport |  | IT | 1318 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1277 |
| 27 | Kuala Lumpur International Airport |  | MY | 1227 |
| 28 | Bengaluru International Airport |  | IN | 1225 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1195 |
| 30 | Ninoy Aquino International Airport |  | PH | 1190 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1176 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1112 |
| 34 | Seattle-Tacoma International Airport |  | US | 1103 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1095 |
| 37 | Daniel K Inouye International Airport |  | US | 1073 |
| 38 | Oslo Gardermoen Airport |  | NO | 1069 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 701 | 21m | 244 km | 2,951.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 463 | 1h 7m | 770 km | 6,150.6 t |
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
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 233 | 19m | 99 km | 399.1 t |
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
| SKQ48 | SKQ | Burlington/Alamance Regional Airport (KBUY) | Hurst Airport (69PA) | 2026-08-12 23:55 UTC | 2026-08-13 01:28 UTC | 1h 33m |
| KII587 | KII | Cincinnati/Northern Kentucky International Airport (KCVG) | Lancaster Airport (KLNS) | 2026-08-13 00:13 UTC | 2026-08-13 01:28 UTC | 1h 15m |
| N73924 |  | Lee Gilmer Memorial Airport (KGVL) | Dekalb-Peachtree Airport (KPDK) | 2026-08-13 00:49 UTC | 2026-08-13 01:16 UTC | 27m |
| AAL2269 | American Airlines | Eppley Airfield (KOMA) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-12 23:44 UTC | 2026-08-13 01:12 UTC | 1h 28m |
| N19650 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-13 00:47 UTC | 2026-08-13 01:11 UTC | 24m |
| LICHEN9 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-12 23:14 UTC | 2026-08-13 01:10 UTC | 1h 56m |
| N297ME |  | Ocean County Airport (KMJX) | Ocean County Airport (KMJX) | 2026-08-13 00:22 UTC | 2026-08-13 01:02 UTC | 40m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Spanish Peaks Airfield (K4V1) | 2026-08-13 00:42 UTC | 2026-08-13 01:02 UTC | 19m |
| PCM7679 | PCM | Monterey Regional Airport (KMRY) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-13 00:19 UTC | 2026-08-13 00:58 UTC | 39m |
| TKR10 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | OG12 (OG12) | 2026-08-13 00:50 UTC | 2026-08-13 00:56 UTC | 6m |
| URSA19 | URS | Moen's Ranch Airport (AK52) | Ladd Army Air Field (PAFB) | 2026-08-13 00:42 UTC | 2026-08-13 00:53 UTC | 11m |
| N1539E |  | Chino Airport (KCNO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-12 23:30 UTC | 2026-08-13 00:53 UTC | 1h 22m |
| TKR104 | TKR | Simonson Field (80CO) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-13 00:31 UTC | 2026-08-13 00:46 UTC | 15m |
| N7866Y |  | Essex County Airport (KCDW) | Essex County Airport (KCDW) | 2026-08-12 22:48 UTC | 2026-08-13 00:45 UTC | 1h 56m |
| CXK668 | CXK | Camarillo Airport (KCMA) | Lompoc Airport (KLPC) | 2026-08-12 23:48 UTC | 2026-08-13 00:44 UTC | 55m |
|  |  | Roberts Field/Redmond Municipal Airport (KRDM) | Tailwheel Airport (6OR4) | 2026-08-13 00:37 UTC | 2026-08-13 00:43 UTC | 6m |
| N562JL |  | Long Beach (Daugherty Field) Airport (KLGB) | San Francisco International Airport (KSFO) | 2026-08-12 23:47 UTC | 2026-08-13 00:42 UTC | 55m |
| N848AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-13 00:24 UTC | 2026-08-13 00:39 UTC | 14m |
| N12161 |  | Charles M Schulz/Sonoma County Airport (KSTS) | Sacramento Executive Airport (KSAC) | 2026-08-12 23:59 UTC | 2026-08-13 00:39 UTC | 40m |
| N96281 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-12 23:58 UTC | 2026-08-13 00:38 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
