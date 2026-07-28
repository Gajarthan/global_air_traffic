# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_12:57:51_UTC-green)

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

**Latest saved flight:** 2026-07-28 12:57:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 12:57:51 UTC

- **156,296** saved flights
- **51,936** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **156,296** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,876,256.4 tonnes** estimated CO2 emissions
- **108,768,487 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6289 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2771 |
| 5 | American Airlines | 2491 |
| 6 | Southwest Airlines | 2458 |
| 7 | ENY | 1950 |
| 8 | Delta Air Lines | 1862 |
| 9 | Lufthansa | 1501 |
| 10 | LATAM Airlines | 1456 |
| 11 | AZU | 1367 |
| 12 | WIF | 1318 |
| 13 | Vueling | 1309 |
| 14 | LXJ | 1199 |
| 15 | AXM | 1102 |
| 16 | Swiss International | 1088 |
| 17 | easyJet | 1021 |
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 973 |
| 20 | QLK | 972 |
| 21 | EJU | 957 |
| 22 | VIV | 858 |
| 23 | United Airlines | 837 |
| 24 | CXK | 826 |
| 25 | AEE | 817 |
| 26 | Cathay Pacific | 817 |
| 27 | GLO | 817 |
| 28 | MXY | 815 |
| 29 | Air France | 812 |
| 30 | JetBlue | 812 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134853 |
| 2 | 🇪🇸 ES | 10073 |
| 3 | 🇧🇷 BR | 8909 |
| 4 | 🇦🇺 AU | 8853 |
| 5 | 🇮🇳 IN | 8712 |
| 6 | 🇨🇦 CA | 8420 |
| 7 | 🇮🇹 IT | 8064 |
| 8 | 🇩🇪 DE | 7932 |
| 9 | 🇬🇧 GB | 7174 |
| 10 | 🇯🇵 JP | 6420 |
| 11 | 🇫🇷 FR | 6180 |
| 12 | 🇨🇴 CO | 5429 |
| 13 | 🇲🇽 MX | 4479 |
| 14 | 🇬🇷 GR | 4444 |
| 15 | 🇳🇴 NO | 4129 |
| 16 | 🇨🇭 CH | 4082 |
| 17 | 🇹🇷 TR | 3732 |
| 18 | 🇲🇾 MY | 2871 |
| 19 | 🇵🇱 PL | 2666 |
| 20 | 🇿🇦 ZA | 2536 |
| 21 | 🇳🇿 NZ | 2329 |
| 22 | 🇹🇭 TH | 2261 |
| 23 | 🇰🇷 KR | 2091 |
| 24 | 🇵🇭 PH | 2066 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1595 |
| 27 | 🇲🇪 ME | 1513 |
| 28 | 🇭🇷 HR | 1440 |
| 29 | 🇳🇱 NL | 1428 |
| 30 | 🇲🇴 MO | 1289 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3211 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2035 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1937 |
| 6 | Harry Reid International Airport |  | US | 1918 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1733 |
| 8 | Zurich Airport |  | CH | 1687 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1637 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 12 | Frankfurt am Main International Airport |  | DE | 1451 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | El Dorado International Airport |  | CO | 1413 |
| 15 | Salt Lake City International Airport |  | US | 1409 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1289 |
| 18 | Congonhas Airport |  | BR | 1277 |
| 19 | Madrid Barajas International Airport |  | ES | 1242 |
| 20 | Capua Airport |  | IT | 1229 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1124 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1107 |
| 25 | Kuala Lumpur International Airport |  | MY | 1099 |
| 26 | Charles de Gaulle International Airport |  | FR | 1071 |
| 27 | Bengaluru International Airport |  | IN | 1035 |
| 28 | Malpensa International Airport |  | IT | 1024 |
| 29 | Ninoy Aquino International Airport |  | PH | 968 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 950 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 944 |
| 32 | Barcelona International Airport |  | ES | 930 |
| 33 | Daniel K Inouye International Airport |  | US | 924 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 895 |
| 36 | Tenerife Norte Airport |  | ES | 893 |
| 37 | Viracopos International Airport |  | BR | 887 |
| 38 | Scottsdale Airport |  | US | 884 |
| 39 | Amsterdam Airport Schiphol |  | NL | 863 |
| 40 | Oslo Gardermoen Airport |  | NO | 859 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 563 | 21m | 244 km | 2,370.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 361 | 1h 9m | 770 km | 4,795.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 288 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 276 | 27m | 275 km | 1,307.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 216 | 44m | 241 km | 897.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 210 | 1h 47m | 1,423 km | 5,153.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 205 | 26m | 215 km | 759.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 200 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 199 | 20m | 250 km | 859.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 185 | 18m | 144 km | 460.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 176 | 1h 39m | 1,156 km | 3,511.1 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 1m | 695 km | 2,073.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPNWD | SPN | Leszno Strzyzewi Airport (EPLS) | Leszno Strzyzewi Airport (EPLS) | 2026-07-28 12:44 UTC | 2026-07-28 12:57 UTC | 13m |
| N106VU |  | Colby Airport (99KY) | Blue Grass Airport (KLEX) | 2026-07-28 12:44 UTC | 2026-07-28 12:56 UTC | 11m |
|  |  | Brookhaven Airport (KHWV) | Teterboro Airport (KTEB) | 2026-07-28 12:22 UTC | 2026-07-28 12:50 UTC | 28m |
| NSZ2047 | NSZ | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-07-28 10:44 UTC | 2026-07-28 12:47 UTC | 2h 3m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Jesse Viertel Memorial Airport (KVER) | 2026-07-28 12:29 UTC | 2026-07-28 12:47 UTC | 17m |
| RDF4 | RDF | EDPR (EDPR) | EDPR (EDPR) | 2026-07-28 12:10 UTC | 2026-07-28 12:46 UTC | 36m |
| BB096 |  | Thomas Farms Airport (85FL) | Monroe County Aeroplex Airport (KMVC) | 2026-07-28 12:07 UTC | 2026-07-28 12:41 UTC | 34m |
| HB2233 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-07-28 12:27 UTC | 2026-07-28 12:37 UTC | 10m |
| UAE328 | Emirates | Dubai International Airport (OMDB) | Lashio Airport (VYLS) | 2026-07-28 07:36 UTC | 2026-07-28 12:35 UTC | 4h 58m |
| WNG11A | WNG | Denton Enterprise Airport (KDTO) | Denton Enterprise Airport (KDTO) | 2026-07-28 12:32 UTC | 2026-07-28 12:33 UTC | 1m |
| N602XX |  | Iowa Falls Municipal Airport (KIFA) | Iowa Falls Municipal Airport (KIFA) | 2026-07-28 12:32 UTC | 2026-07-28 12:33 UTC | 0m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-07-28 11:50 UTC | 2026-07-28 12:29 UTC | 39m |
| ABY834 | ABY | Nariya Airport (OENR) | Sharjah International Airport (OMSJ) | 2026-07-28 11:33 UTC | 2026-07-28 12:27 UTC | 54m |
| RYR86GY | Ryanair | Edinburgh Airport (EGPH) | Dublin Airport (EIDW) | 2026-07-28 11:30 UTC | 2026-07-28 12:21 UTC | 50m |
| CPA683 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | VYNT (VYNT) | 2026-07-28 09:58 UTC | 2026-07-28 12:18 UTC | 2h 20m |
| N800GM |  | XS89 (XS89) | 74XS (74XS) | 2026-07-28 11:45 UTC | 2026-07-28 12:17 UTC | 32m |
| PROVA21 | PRO | Vergiate Airport (LILG) | Alzate Brianza Airport (LILB) | 2026-07-28 12:04 UTC | 2026-07-28 12:13 UTC | 8m |
| N957GV |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-07-28 11:31 UTC | 2026-07-28 12:13 UTC | 41m |
| N79CS |  | Des Moines International Airport (KDSM) | Columbia Regional Airport (KCOU) | 2026-07-28 11:27 UTC | 2026-07-28 12:12 UTC | 44m |
| N495CS |  | Topsail Airpark (01NC) | Camp Davis Mcolf Airport (14NC) | 2026-07-28 11:56 UTC | 2026-07-28 12:10 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
