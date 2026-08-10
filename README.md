# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_19:45:37_UTC-green)

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

**Latest saved flight:** 2026-08-10 19:45:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 19:45:37 UTC

- **185,046** saved flights
- **58,856** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,046** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,222,549.9 tonnes** estimated CO2 emissions
- **128,843,475 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7341 |
| 2 | SkyWest Airlines | 6731 |
| 3 | EJA | 3658 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2901 |
| 6 | American Airlines | 2883 |
| 7 | ENY | 2307 |
| 8 | Delta Air Lines | 2178 |
| 9 | LATAM Airlines | 1731 |
| 10 | AZU | 1661 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1531 |
| 13 | Vueling | 1527 |
| 14 | LXJ | 1456 |
| 15 | easyJet | 1269 |
| 16 | Swiss International | 1267 |
| 17 | AXM | 1235 |
| 18 | EJU | 1143 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1107 |
| 22 | VIV | 1019 |
| 23 | GLO | 991 |
| 24 | AEE | 961 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 944 |
| 29 | United Airlines | 943 |
| 30 | MXY | 920 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158134 |
| 2 | 🇪🇸 ES | 11900 |
| 3 | 🇧🇷 BR | 10625 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10093 |
| 7 | 🇮🇹 IT | 9567 |
| 8 | 🇩🇪 DE | 9145 |
| 9 | 🇬🇧 GB | 8589 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7402 |
| 12 | 🇨🇴 CO | 6970 |
| 13 | 🇬🇷 GR | 5428 |
| 14 | 🇲🇽 MX | 5281 |
| 15 | 🇨🇭 CH | 4944 |
| 16 | 🇹🇷 TR | 4845 |
| 17 | 🇳🇴 NO | 4758 |
| 18 | 🇲🇾 MY | 3220 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3088 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2441 |
| 24 | 🇬🇹 GT | 2368 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1872 |
| 27 | 🇭🇷 HR | 1860 |
| 28 | 🇲🇪 ME | 1668 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3837 |
| 2 | Denver International Airport |  | US | 3056 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2265 |
| 6 | Harry Reid International Airport |  | US | 2162 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1982 |
| 8 | Zurich Airport |  | CH | 1977 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1919 |
| 10 | La Aurora Airport |  | GT | 1817 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1686 |
| 12 | El Dorado International Airport |  | CO | 1658 |
| 13 | Salt Lake City International Airport |  | US | 1649 |
| 14 | Chicago O'Hare International Airport |  | US | 1647 |
| 15 | Frankfurt am Main International Airport |  | DE | 1595 |
| 16 | Congonhas Airport |  | BR | 1544 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1452 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1378 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1321 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1278 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1253 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1158 |
| 30 | Ninoy Aquino International Airport |  | PH | 1151 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1134 |
| 32 | Barcelona International Airport |  | ES | 1096 |
| 33 | Viracopos International Airport |  | BR | 1066 |
| 34 | Reno/Tahoe International Airport |  | US | 1062 |
| 35 | Seattle-Tacoma International Airport |  | US | 1061 |
| 36 | Calgary International Airport |  | CA | 1052 |
| 37 | Daniel K Inouye International Airport |  | US | 1051 |
| 38 | Oslo Gardermoen Airport |  | NO | 1031 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1004 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 934 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 679 | 21m | 244 km | 2,859.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 431 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 276 | 44m | 241 km | 1,146.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 264 | 8m | - | - |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 227 | 1h 15m | 961 km | 3,762.6 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 222 | 50m | 556 km | 2,128.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 222 | 19m | 144 km | 552.2 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 218 | 24m | 218 km | 821.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R21200 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-10 18:12 UTC | 2026-08-10 19:45 UTC | 1h 33m |
| N471AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-08-10 18:51 UTC | 2026-08-10 19:39 UTC | 48m |
| CXK685 | CXK | Baton Rouge Metro, Ryan Field (KBTR) | False River Regional Airport (KHZR) | 2026-08-10 19:10 UTC | 2026-08-10 19:36 UTC | 25m |
| BOBCT81 | BOB | Rose Field (14MS) | Smith County Airport (MS39) | 2026-08-10 19:21 UTC | 2026-08-10 19:32 UTC | 10m |
| XBMGH | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-10 19:02 UTC | 2026-08-10 19:32 UTC | 29m |
| N542JJ |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-10 18:48 UTC | 2026-08-10 19:30 UTC | 42m |
| OXF6154 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-08-10 18:07 UTC | 2026-08-10 19:27 UTC | 1h 19m |
| AXLE11 | AXL | 75OK (75OK) | Blackwell-Tonkawa Municipal Airport (KBKN) | 2026-08-10 19:00 UTC | 2026-08-10 19:26 UTC | 26m |
| N501SC |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-08-10 18:52 UTC | 2026-08-10 19:26 UTC | 34m |
| RK02 |  | Kempten-Durach Airport (EDMK) | Erbach Airport (EDNE) | 2026-08-10 18:59 UTC | 2026-08-10 19:23 UTC | 24m |
| SRG897 | SRG | Carlisle Airport (EGNC) | CARK (CARK) | 2026-08-10 19:07 UTC | 2026-08-10 19:22 UTC | 15m |
| FLAME91 | FLA | Sandy Creek Airport (73TX) | Chaparrosa Ranch Airport (72TE) | 2026-08-10 18:50 UTC | 2026-08-10 19:14 UTC | 24m |
| N616ML |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-10 19:04 UTC | 2026-08-10 19:14 UTC | 9m |
| SKW5970 | SkyWest Airlines | Salt Lake City International Airport (KSLC) | San Francisco International Airport (KSFO) | 2026-08-10 17:29 UTC | 2026-08-10 19:13 UTC | 1h 43m |
| N8372L |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-08-10 18:50 UTC | 2026-08-10 19:12 UTC | 22m |
| N38700 |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-08-10 19:11 UTC | 2026-08-10 19:12 UTC | 0m |
| TKR136 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | Collins Landing Strip (04OR) | 2026-08-10 18:58 UTC | 2026-08-10 19:11 UTC | 13m |
| BUZZ31 | BUZ | Laughlin Afb Aux Nr 1 Airport (KT70) | Dunbar Ranch Airport (0XS8) | 2026-08-10 18:41 UTC | 2026-08-10 19:11 UTC | 29m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 18:53 UTC | 2026-08-10 19:10 UTC | 17m |
| LXJ343 | LXJ | Truckee-Tahoe Airport (KTRK) | Meadows Field (KBFL) | 2026-08-10 18:22 UTC | 2026-08-10 19:10 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
