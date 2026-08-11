# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_22:37:21_UTC-green)

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

**Latest saved flight:** 2026-08-11 22:37:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 22:37:21 UTC

- **188,235** saved flights
- **59,611** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **188,235** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,257,075.7 tonnes** estimated CO2 emissions
- **130,844,968 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7478 |
| 2 | SkyWest Airlines | 6847 |
| 3 | EJA | 3717 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2947 |
| 6 | American Airlines | 2933 |
| 7 | ENY | 2336 |
| 8 | Delta Air Lines | 2213 |
| 9 | LATAM Airlines | 1759 |
| 10 | AZU | 1694 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1563 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1474 |
| 15 | easyJet | 1297 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1156 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1122 |
| 22 | VIV | 1042 |
| 23 | GLO | 1015 |
| 24 | Air France | 978 |
| 25 | AEE | 969 |
| 26 | PGT | 966 |
| 27 | CXK | 965 |
| 28 | United Airlines | 964 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160705 |
| 2 | 🇪🇸 ES | 12132 |
| 3 | 🇧🇷 BR | 10815 |
| 4 | 🇦🇺 AU | 10492 |
| 5 | 🇨🇦 CA | 10305 |
| 6 | 🇮🇳 IN | 10266 |
| 7 | 🇮🇹 IT | 9759 |
| 8 | 🇩🇪 DE | 9297 |
| 9 | 🇬🇧 GB | 8757 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7527 |
| 12 | 🇨🇴 CO | 7162 |
| 13 | 🇬🇷 GR | 5518 |
| 14 | 🇲🇽 MX | 5368 |
| 15 | 🇨🇭 CH | 5033 |
| 16 | 🇹🇷 TR | 4980 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3120 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2678 |
| 23 | 🇵🇭 PH | 2481 |
| 24 | 🇬🇹 GT | 2399 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1914 |
| 27 | 🇭🇷 HR | 1910 |
| 28 | 🇲🇪 ME | 1684 |
| 29 | 🇳🇱 NL | 1677 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3912 |
| 2 | Denver International Airport |  | US | 3105 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2310 |
| 6 | Harry Reid International Airport |  | US | 2203 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 8 | Zurich Airport |  | CH | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1951 |
| 10 | La Aurora Airport |  | GT | 1843 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1709 |
| 12 | El Dorado International Airport |  | CO | 1693 |
| 13 | Salt Lake City International Airport |  | US | 1676 |
| 14 | Chicago O'Hare International Airport |  | US | 1658 |
| 15 | Frankfurt am Main International Airport |  | DE | 1614 |
| 16 | Congonhas Airport |  | BR | 1574 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1485 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1460 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1396 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1347 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1299 |
| 25 | Charles de Gaulle International Airport |  | FR | 1285 |
| 26 | Charlotte/Douglas International Airport |  | US | 1264 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1180 |
| 30 | Ninoy Aquino International Airport |  | PH | 1171 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1157 |
| 32 | Barcelona International Airport |  | ES | 1127 |
| 33 | Reno/Tahoe International Airport |  | US | 1088 |
| 34 | Viracopos International Airport |  | BR | 1086 |
| 35 | Seattle-Tacoma International Airport |  | US | 1082 |
| 36 | Calgary International Airport |  | CA | 1071 |
| 37 | Daniel K Inouye International Airport |  | US | 1060 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1035 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 952 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 688 | 21m | 244 km | 2,897.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 439 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 316 | 27m | 275 km | 1,497.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 305 | 14m | 114 km | 598.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 284 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 231 | 50m | 556 km | 2,214.3 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 231 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 224 | 19m | 144 km | 557.2 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 204 | 1h 49m | 1,304 km | 4,589.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R20658 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-11 21:34 UTC | 2026-08-11 22:37 UTC | 1h 2m |
| N7091G |  | Hartford-Brainard Airport (KHFD) | New Bedford Regional Airport (KEWB) | 2026-08-11 21:52 UTC | 2026-08-11 22:34 UTC | 42m |
| MAFFS4 | MAF | Mc Clellan Airfield (KMCC) | NV44 (NV44) | 2026-08-11 22:02 UTC | 2026-08-11 22:29 UTC | 26m |
| N680ND |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-11 21:37 UTC | 2026-08-11 22:24 UTC | 46m |
| HRCLS63 | HRC | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-11 21:30 UTC | 2026-08-11 22:23 UTC | 53m |
| ZKTPW | ZKT | Napier Airport (NZNR) | Napier Airport (NZNR) | 2026-08-11 22:10 UTC | 2026-08-11 22:21 UTC | 10m |
| EYY | EYY | Quirindi Airport (YQDI) | Tamworth Airport (YSTW) | 2026-08-11 22:01 UTC | 2026-08-11 22:20 UTC | 18m |
| N343KT |  | Mc Kinley Country Airport (81AK) | Helio Airport (2AK7) | 2026-08-11 22:07 UTC | 2026-08-11 22:18 UTC | 10m |
| N362Q |  | Palo Alto Airport (KPAO) | San Carlos Airport (KSQL) | 2026-08-11 21:34 UTC | 2026-08-11 22:18 UTC | 43m |
| N388BB |  | Tebow Airport (LA77) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-08-11 21:56 UTC | 2026-08-11 22:17 UTC | 20m |
| N466CC |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-11 21:46 UTC | 2026-08-11 22:16 UTC | 30m |
| MAFFS6 | MAF | Mc Clellan Airfield (KMCC) | NV44 (NV44) | 2026-08-11 21:46 UTC | 2026-08-11 22:16 UTC | 29m |
| N950RF |  | Provo Municipal Airport (KPVU) | Canyonlands Regional Airport (KCNY) | 2026-08-11 19:55 UTC | 2026-08-11 22:13 UTC | 2h 17m |
| YGI | YGI | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-11 21:37 UTC | 2026-08-11 22:11 UTC | 33m |
| N42BV |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-11 22:00 UTC | 2026-08-11 22:11 UTC | 11m |
| N164RD |  | Hector International Airport (KFAR) | St Paul Downtown Holman Field (KSTP) | 2026-08-11 21:20 UTC | 2026-08-11 22:10 UTC | 50m |
| N73761 |  | Waukesha County Airport (KUES) | Watertown Municipal Airport (KRYV) | 2026-08-11 21:30 UTC | 2026-08-11 22:07 UTC | 37m |
| N631WL |  | Trenton Mercer Airport (KTTN) | Trenton Mercer Airport (KTTN) | 2026-08-11 20:56 UTC | 2026-08-11 22:06 UTC | 1h 9m |
| N565TA |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-11 21:31 UTC | 2026-08-11 22:00 UTC | 28m |
| ZKTPW | ZKT | Napier Airport (NZNR) | Napier Airport (NZNR) | 2026-08-11 20:49 UTC | 2026-08-11 21:59 UTC | 1h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
