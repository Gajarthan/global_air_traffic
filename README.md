# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_00:55:10_UTC-green)

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

**Latest saved flight:** 2026-07-29 00:55:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 00:55:10 UTC

- **157,623** saved flights
- **52,299** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **157,623** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,890,655.7 tonnes** estimated CO2 emissions
- **109,603,228 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6334 |
| 2 | SkyWest Airlines | 5777 |
| 3 | EJA | 3123 |
| 4 | IndiGo | 2776 |
| 5 | American Airlines | 2513 |
| 6 | Southwest Airlines | 2480 |
| 7 | ENY | 1967 |
| 8 | Delta Air Lines | 1870 |
| 9 | Lufthansa | 1508 |
| 10 | LATAM Airlines | 1477 |
| 11 | AZU | 1383 |
| 12 | WIF | 1328 |
| 13 | Vueling | 1321 |
| 14 | LXJ | 1216 |
| 15 | AXM | 1104 |
| 16 | Swiss International | 1090 |
| 17 | easyJet | 1029 |
| 18 | Alaska Airlines | 989 |
| 19 | QLK | 979 |
| 20 | All Nippon Airways | 974 |
| 21 | EJU | 966 |
| 22 | VIV | 866 |
| 23 | United Airlines | 838 |
| 24 | CXK | 837 |
| 25 | Cathay Pacific | 830 |
| 26 | GLO | 828 |
| 27 | AEE | 824 |
| 28 | MXY | 821 |
| 29 | Air France | 817 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136139 |
| 2 | 🇪🇸 ES | 10144 |
| 3 | 🇧🇷 BR | 9006 |
| 4 | 🇦🇺 AU | 8895 |
| 5 | 🇮🇳 IN | 8732 |
| 6 | 🇨🇦 CA | 8541 |
| 7 | 🇮🇹 IT | 8125 |
| 8 | 🇩🇪 DE | 7975 |
| 9 | 🇬🇧 GB | 7234 |
| 10 | 🇯🇵 JP | 6435 |
| 11 | 🇫🇷 FR | 6219 |
| 12 | 🇨🇴 CO | 5538 |
| 13 | 🇲🇽 MX | 4528 |
| 14 | 🇬🇷 GR | 4488 |
| 15 | 🇳🇴 NO | 4162 |
| 16 | 🇨🇭 CH | 4115 |
| 17 | 🇹🇷 TR | 3767 |
| 18 | 🇲🇾 MY | 2875 |
| 19 | 🇵🇱 PL | 2683 |
| 20 | 🇿🇦 ZA | 2546 |
| 21 | 🇳🇿 NZ | 2343 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2097 |
| 24 | 🇵🇭 PH | 2071 |
| 25 | 🇬🇹 GT | 2021 |
| 26 | 🇲🇦 MA | 1605 |
| 27 | 🇲🇪 ME | 1517 |
| 28 | 🇭🇷 HR | 1454 |
| 29 | 🇳🇱 NL | 1434 |
| 30 | 🇲🇴 MO | 1297 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3240 |
| 2 | Denver International Airport |  | US | 2639 |
| 3 | Tokyo International Airport |  | JP | 2038 |
| 4 | Guaymaral Airport |  | CO | 1982 |
| 5 | Indira Gandhi International Airport |  | IN | 1944 |
| 6 | Harry Reid International Airport |  | US | 1926 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1743 |
| 8 | Zurich Airport |  | CH | 1692 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1656 |
| 10 | La Aurora Airport |  | GT | 1567 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1473 |
| 12 | Frankfurt am Main International Airport |  | DE | 1458 |
| 13 | El Dorado International Airport |  | CO | 1437 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1421 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Congonhas Airport |  | BR | 1299 |
| 18 | Macau International Airport |  | MO | 1297 |
| 19 | Madrid Barajas International Airport |  | ES | 1250 |
| 20 | Capua Airport |  | IT | 1237 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1211 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1129 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1125 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1100 |
| 26 | Charles de Gaulle International Airport |  | FR | 1079 |
| 27 | Bengaluru International Airport |  | IN | 1037 |
| 28 | Malpensa International Airport |  | IT | 1036 |
| 29 | Ninoy Aquino International Airport |  | PH | 971 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 961 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 954 |
| 32 | Barcelona International Airport |  | ES | 941 |
| 33 | Daniel K Inouye International Airport |  | US | 930 |
| 34 | Seattle-Tacoma International Airport |  | US | 922 |
| 35 | Calgary International Airport |  | CA | 905 |
| 36 | Tenerife Norte Airport |  | ES | 895 |
| 37 | Viracopos International Airport |  | BR | 894 |
| 38 | Scottsdale Airport |  | US | 890 |
| 39 | Oslo Gardermoen Airport |  | NO | 871 |
| 40 | Amsterdam Airport Schiphol |  | NL | 865 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 832 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 569 | 21m | 244 km | 2,395.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 377 | 24m | 225 km | 1,462.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 376 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 362 | 1h 9m | 770 km | 4,808.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 277 | 27m | 275 km | 1,312.6 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 220 | 44m | 241 km | 913.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 206 | 26m | 215 km | 762.9 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 202 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 189 | 30m | 49 km | 159.8 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 187 | 1h 15m | 961 km | 3,099.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 183 | 31m | 369 km | 1,164.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 183 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 179 | 50m | 556 km | 1,715.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 1m | 695 km | 2,085.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 49m | 1,304 km | 3,779.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N970AE |  | San Carlos Apache Airport (KP13) | Phoenix Sky Harbor International Airport (KPHX) | 2026-07-29 00:22 UTC | 2026-07-29 00:55 UTC | 32m |
| BT11 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-28 22:58 UTC | 2026-07-29 00:48 UTC | 1h 49m |
| OST4 | OST | Stillwater Regional Airport (KSWO) | Perry Municipal Airport (KF22) | 2026-07-29 00:20 UTC | 2026-07-29 00:46 UTC | 25m |
| N524AR |  | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-07-28 23:34 UTC | 2026-07-29 00:46 UTC | 1h 12m |
| N971MB |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-07-29 00:25 UTC | 2026-07-29 00:46 UTC | 20m |
| N127ZW |  | Red Deer / South 40 Airstrip (CRD4) | Rimbey Airport (CFC7) | 2026-07-29 00:29 UTC | 2026-07-29 00:45 UTC | 15m |
| DLH493 | Lufthansa | Vancouver International Airport (CYVR) | Grimshaw Airport (CFD5) | 2026-07-28 23:42 UTC | 2026-07-29 00:40 UTC | 58m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-07-29 00:20 UTC | 2026-07-29 00:34 UTC | 14m |
| URSA10 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-29 00:31 UTC | 2026-07-29 00:33 UTC | 1m |
| CLX9932 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-07-28 13:39 UTC | 2026-07-29 00:31 UTC | 10h 52m |
| URSA26 | URS | Scotts Airport (0AK0) | Ladd Army Air Field (PAFB) | 2026-07-28 23:49 UTC | 2026-07-29 00:30 UTC | 40m |
| N78TJ |  | Concord-Padgett Regional Airport (KJQF) | Scottsboro Municipal-Word Field (K4A6) | 2026-07-28 23:12 UTC | 2026-07-29 00:28 UTC | 1h 16m |
| N261JS |  | Gregg Airport (7OK1) | Stillwater Regional Airport (KSWO) | 2026-07-28 23:43 UTC | 2026-07-29 00:27 UTC | 43m |
| ZOB | ZOB | Toowoomba Airport (YTWB) | Toowoomba Airport (YTWB) | 2026-07-28 23:36 UTC | 2026-07-29 00:25 UTC | 49m |
| N111WG |  | Merrill Field (PAMR) | Big Creek Airport (AK51) | 2026-07-28 23:43 UTC | 2026-07-29 00:22 UTC | 39m |
| CREEP31 | CRE | Ramey 1 Airport (0OK8) | Ramey 1 Airport (0OK8) | 2026-07-28 23:39 UTC | 2026-07-29 00:17 UTC | 38m |
| CPA3144 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-07-28 13:15 UTC | 2026-07-29 00:16 UTC | 11h 0m |
| N897MT |  | Moore Ranch Airport (24TA) | Coulter Field (KCFD) | 2026-07-28 23:55 UTC | 2026-07-29 00:16 UTC | 20m |
| N325TC |  | Tstc Waco Airport (KCNW) | Echo Lake Airport (TX40) | 2026-07-28 23:28 UTC | 2026-07-29 00:15 UTC | 46m |
| 8L8 |  | Sydney Bankstown Airport (YSBK) | Coonabarabran Airport (YCBB) | 2026-07-28 23:10 UTC | 2026-07-29 00:14 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
