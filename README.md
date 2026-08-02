# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_18:19:19_UTC-green)

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

**Latest saved flight:** 2026-08-02 18:19:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 18:19:19 UTC

- **167,303** saved flights
- **54,745** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **167,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,015,345.8 tonnes** estimated CO2 emissions
- **116,831,642 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6678 |
| 2 | SkyWest Airlines | 6082 |
| 3 | EJA | 3319 |
| 4 | IndiGo | 2950 |
| 5 | American Airlines | 2637 |
| 6 | Southwest Airlines | 2631 |
| 7 | ENY | 2081 |
| 8 | Delta Air Lines | 1996 |
| 9 | LATAM Airlines | 1551 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1472 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1380 |
| 14 | LXJ | 1301 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1148 |
| 17 | easyJet | 1123 |
| 18 | EJU | 1032 |
| 19 | Alaska Airlines | 1026 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 921 |
| 23 | CXK | 890 |
| 24 | Cathay Pacific | 889 |
| 25 | United Airlines | 879 |
| 26 | AEE | 878 |
| 27 | GLO | 878 |
| 28 | Air France | 865 |
| 29 | MXY | 862 |
| 30 | JetBlue | 844 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 144165 |
| 2 | 🇪🇸 ES | 10721 |
| 3 | 🇧🇷 BR | 9522 |
| 4 | 🇦🇺 AU | 9344 |
| 5 | 🇮🇳 IN | 9251 |
| 6 | 🇨🇦 CA | 9064 |
| 7 | 🇮🇹 IT | 8647 |
| 8 | 🇩🇪 DE | 8362 |
| 9 | 🇬🇧 GB | 7765 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6645 |
| 12 | 🇨🇴 CO | 6015 |
| 13 | 🇬🇷 GR | 4861 |
| 14 | 🇲🇽 MX | 4784 |
| 15 | 🇨🇭 CH | 4412 |
| 16 | 🇳🇴 NO | 4378 |
| 17 | 🇹🇷 TR | 4044 |
| 18 | 🇲🇾 MY | 3009 |
| 19 | 🇵🇱 PL | 2829 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇬🇹 GT | 2164 |
| 25 | 🇰🇷 KR | 2147 |
| 26 | 🇲🇦 MA | 1689 |
| 27 | 🇭🇷 HR | 1603 |
| 28 | 🇲🇪 ME | 1550 |
| 29 | 🇳🇱 NL | 1523 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3423 |
| 2 | Denver International Airport |  | US | 2772 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2088 |
| 5 | Indira Gandhi International Airport |  | IN | 2049 |
| 6 | Harry Reid International Airport |  | US | 2009 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1839 |
| 8 | Zurich Airport |  | CH | 1784 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1757 |
| 10 | La Aurora Airport |  | GT | 1673 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1542 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Chicago O'Hare International Airport |  | US | 1511 |
| 14 | Frankfurt am Main International Airport |  | DE | 1508 |
| 15 | Salt Lake City International Airport |  | US | 1495 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1390 |
| 18 | Congonhas Airport |  | BR | 1376 |
| 19 | Madrid Barajas International Airport |  | ES | 1318 |
| 20 | Capua Airport |  | IT | 1303 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1274 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1178 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1169 |
| 25 | Charles de Gaulle International Airport |  | FR | 1143 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1123 |
| 28 | Bengaluru International Airport |  | IN | 1095 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1030 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1024 |
| 32 | Barcelona International Airport |  | ES | 987 |
| 33 | Daniel K Inouye International Airport |  | US | 974 |
| 34 | Seattle-Tacoma International Airport |  | US | 969 |
| 35 | Viracopos International Airport |  | BR | 953 |
| 36 | Calgary International Airport |  | CA | 945 |
| 37 | Tenerife Norte Airport |  | ES | 932 |
| 38 | Oslo Gardermoen Airport |  | NO | 929 |
| 39 | Scottsdale Airport |  | US | 929 |
| 40 | Reno/Tahoe International Airport |  | US | 922 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 869 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 608 | 21m | 244 km | 2,560.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 401 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 213 | 31m | 49 km | 180.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 197 | 19m | 144 km | 490.0 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 190 | 50m | 556 km | 1,821.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 182 | 24m | 218 km | 685.7 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LXJ602 | LXJ | Boca Raton Airport (KBCT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-02 15:09 UTC | 2026-08-02 18:19 UTC | 3h 10m |
| N5327G |  | Georgetown Executive Airport (KGTU) | New Braunfels Ntl Airport (KBAZ) | 2026-08-02 17:43 UTC | 2026-08-02 18:19 UTC | 35m |
| N7718J |  | Allentown Queen City Municipal Airport (KXLL) | Ocean City Municipal Airport (KOXB) | 2026-08-02 16:56 UTC | 2026-08-02 18:18 UTC | 1h 21m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-08-02 18:03 UTC | 2026-08-02 18:14 UTC | 11m |
| N2997L |  | Fullerton Municipal Airport (KFUL) | Brackett Field (KPOC) | 2026-08-02 17:59 UTC | 2026-08-02 18:11 UTC | 12m |
| N324MG |  | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-08-02 17:09 UTC | 2026-08-02 18:10 UTC | 1h 1m |
| HK5431G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-02 16:42 UTC | 2026-08-02 18:09 UTC | 1h 27m |
| N388EE |  | Sechelt-Gibsons Airport (CAP3) | Vancouver International Airport (CYVR) | 2026-08-02 17:49 UTC | 2026-08-02 18:06 UTC | 17m |
| QTR21X | Qatar Airways | Hamad International Airport (OTHH) | Fairview Airport (CEB5) | 2026-08-02 05:06 UTC | 2026-08-02 18:05 UTC | 12h 58m |
| MUS704 | MUS | Martinique Aime Cesaire International Airport (TFFF) | Martinique Aime Cesaire International Airport (TFFF) | 2026-08-02 17:59 UTC | 2026-08-02 18:04 UTC | 4m |
| CAP451 | CAP | Riverside Airport (KRAL) | Big Bear City Airport (KL35) | 2026-08-02 17:21 UTC | 2026-08-02 18:03 UTC | 41m |
| N538SV |  | NM74 (NM74) | NM74 (NM74) | 2026-08-02 17:47 UTC | 2026-08-02 17:59 UTC | 11m |
| CES554 | China Eastern | Charles de Gaulle International Airport (LFPG) | Sharypovo Airport (UNKO) | 2026-08-02 11:50 UTC | 2026-08-02 17:59 UTC | 6h 8m |
| IGO9023 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Chaudhary Charan Singh International Airport (VILK) | 2026-08-02 16:44 UTC | 2026-08-02 17:57 UTC | 1h 13m |
| N8224K |  | Chino Airport (KCNO) | San Bernardino International Airport (KSBD) | 2026-08-02 17:35 UTC | 2026-08-02 17:57 UTC | 21m |
| N21709 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-02 17:24 UTC | 2026-08-02 17:54 UTC | 29m |
| QTR1035 | Qatar Airways | Sharjah International Airport (OMSJ) | Das Island Airport (OMAS) | 2026-08-02 17:33 UTC | 2026-08-02 17:53 UTC | 20m |
| N169DR |  | Chicago Executive Airport (KPWK) | Hintzman Airport (4MN1) | 2026-08-02 15:49 UTC | 2026-08-02 17:52 UTC | 2h 2m |
| EZY473K | easyJet | Václav Havel Airport (LKPR) | Bristol International Airport (EGGD) | 2026-08-02 15:53 UTC | 2026-08-02 17:52 UTC | 1h 58m |
| EJA268 | EJA | Blue Grass Airport (KLEX) | Tucker-Guthrie Memorial Airport (KI35) | 2026-08-02 17:34 UTC | 2026-08-02 17:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
