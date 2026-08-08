# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_00:16:14_UTC-green)

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

**Latest saved flight:** 2026-08-08 00:16:14 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 00:16:14 UTC

- **177,132** saved flights
- **57,066** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,132** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,129,187.8 tonnes** estimated CO2 emissions
- **123,431,174 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7015 |
| 2 | SkyWest Airlines | 6491 |
| 3 | EJA | 3504 |
| 4 | IndiGo | 3094 |
| 5 | Southwest Airlines | 2797 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2099 |
| 9 | LATAM Airlines | 1644 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1580 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1394 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1200 |
| 17 | AXM | 1196 |
| 18 | QLK | 1083 |
| 19 | EJU | 1082 |
| 20 | Alaska Airlines | 1073 |
| 21 | All Nippon Airways | 1071 |
| 22 | VIV | 975 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 941 |
| 25 | GLO | 937 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 892 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152468 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10129 |
| 4 | 🇦🇺 AU | 9975 |
| 5 | 🇨🇦 CA | 9706 |
| 6 | 🇮🇳 IN | 9700 |
| 7 | 🇮🇹 IT | 9143 |
| 8 | 🇩🇪 DE | 8741 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7090 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6522 |
| 13 | 🇬🇷 GR | 5150 |
| 14 | 🇲🇽 MX | 5073 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4397 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2939 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2624 |
| 22 | 🇳🇿 NZ | 2563 |
| 23 | 🇵🇭 PH | 2334 |
| 24 | 🇬🇹 GT | 2264 |
| 25 | 🇰🇷 KR | 2208 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1741 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2945 |
| 3 | Tokyo International Airport |  | JP | 2212 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2155 |
| 6 | Harry Reid International Airport |  | US | 2109 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1914 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1853 |
| 10 | La Aurora Airport |  | GT | 1742 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1626 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1588 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1470 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1427 |
| 19 | Capua Airport |  | IT | 1383 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1252 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1238 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1098 |
| 30 | Ninoy Aquino International Airport |  | PH | 1098 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1095 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1023 |
| 34 | Daniel K Inouye International Airport |  | US | 1016 |
| 35 | Viracopos International Airport |  | BR | 1015 |
| 36 | Reno/Tahoe International Airport |  | US | 1010 |
| 37 | Calgary International Airport |  | CA | 1009 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 646 | 21m | 244 km | 2,720.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 415 | 24m | 225 km | 1,610.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 407 | 1h 8m | 770 km | 5,406.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 218 | 20m | 99 km | 373.4 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 206 | 1h 38m | 1,156 km | 4,109.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 193 | 1h 2m | 695 km | 2,313.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZEJ | ZEJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-08 00:03 UTC | 2026-08-08 00:16 UTC | 12m |
| CXK569 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-07 22:56 UTC | 2026-08-08 00:08 UTC | 1h 12m |
| BYF41 | BYF | San Carlos Airport (KSQL) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-07 22:43 UTC | 2026-08-08 00:06 UTC | 1h 22m |
| N240MB |  | Mc Gee Field (24NC) | Mc Gee Field (24NC) | 2026-08-07 23:51 UTC | 2026-08-08 00:04 UTC | 13m |
| N339B |  | John Wayne/Orange County Airport (KSNA) | Buchanan Field (KCCR) | 2026-08-07 23:04 UTC | 2026-08-08 00:04 UTC | 59m |
| JUMP17 | JUM | MT88 (MT88) | Carson Field (MT53) | 2026-08-07 23:46 UTC | 2026-08-07 23:57 UTC | 10m |
| CGGUC | CGG | Barrie-Orillia (Lake Simcoe Regional Airport) (CYLS) | Barrie-Orillia (Lake Simcoe Regional Airport) (CYLS) | 2026-08-07 23:32 UTC | 2026-08-07 23:52 UTC | 20m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-07 23:31 UTC | 2026-08-07 23:52 UTC | 20m |
| BEQ | BEQ | Redcliffe Airport (YRED) | Sunshine Coast Airport (YBMC) | 2026-08-07 23:26 UTC | 2026-08-07 23:49 UTC | 23m |
| TKR102 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-07 23:41 UTC | 2026-08-07 23:49 UTC | 7m |
| TKR104 | TKR | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-08-07 23:37 UTC | 2026-08-07 23:48 UTC | 11m |
| N303JD |  | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-08-07 23:13 UTC | 2026-08-07 23:48 UTC | 34m |
| HAM | HAM | Tyagarah Airport (YTYH) | Tyagarah Airport (YTYH) | 2026-08-07 23:31 UTC | 2026-08-07 23:46 UTC | 15m |
| UPS5012 | UPS | Ontario International Airport (KONT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-07 18:44 UTC | 2026-08-07 23:43 UTC | 4h 59m |
| TKR168 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-08-07 23:31 UTC | 2026-08-07 23:41 UTC | 9m |
| N61NG |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-08-07 23:01 UTC | 2026-08-07 23:38 UTC | 37m |
| N9655B |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-07 23:18 UTC | 2026-08-07 23:38 UTC | 19m |
| N747TA |  | Mc Clellan-Palomar Airport (KCRQ) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-08-07 23:25 UTC | 2026-08-07 23:36 UTC | 11m |
| N20BQ |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-07 23:23 UTC | 2026-08-07 23:35 UTC | 11m |
| TKR186 | TKR | Ephrata Municipal Airport (KEPH) | Rules Roost Airport (5WA5) | 2026-08-07 22:47 UTC | 2026-08-07 23:34 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
