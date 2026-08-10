# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_22:09:33_UTC-green)

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

**Latest saved flight:** 2026-08-10 22:09:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 22:09:33 UTC

- **185,380** saved flights
- **58,926** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,380** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,225,907.8 tonnes** estimated CO2 emissions
- **129,038,132 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7353 |
| 2 | SkyWest Airlines | 6762 |
| 3 | EJA | 3671 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2909 |
| 6 | American Airlines | 2891 |
| 7 | ENY | 2309 |
| 8 | Delta Air Lines | 2183 |
| 9 | LATAM Airlines | 1732 |
| 10 | AZU | 1666 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1457 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1235 |
| 18 | EJU | 1146 |
| 19 | QLK | 1136 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1109 |
| 22 | VIV | 1021 |
| 23 | GLO | 994 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 947 |
| 29 | United Airlines | 947 |
| 30 | MXY | 921 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158527 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10644 |
| 4 | 🇦🇺 AU | 10310 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10126 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9151 |
| 9 | 🇬🇧 GB | 8602 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7404 |
| 12 | 🇨🇴 CO | 6996 |
| 13 | 🇬🇷 GR | 5438 |
| 14 | 🇲🇽 MX | 5290 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4863 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3221 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3090 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2633 |
| 23 | 🇵🇭 PH | 2443 |
| 24 | 🇬🇹 GT | 2371 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1876 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3844 |
| 2 | Denver International Airport |  | US | 3065 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2272 |
| 6 | Harry Reid International Airport |  | US | 2168 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1927 |
| 10 | La Aurora Airport |  | GT | 1819 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1690 |
| 12 | El Dorado International Airport |  | CO | 1664 |
| 13 | Salt Lake City International Airport |  | US | 1655 |
| 14 | Chicago O'Hare International Airport |  | US | 1651 |
| 15 | Frankfurt am Main International Airport |  | DE | 1596 |
| 16 | Congonhas Airport |  | BR | 1549 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1382 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1322 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1254 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1161 |
| 30 | Ninoy Aquino International Airport |  | PH | 1152 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1137 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Viracopos International Airport |  | BR | 1068 |
| 34 | Seattle-Tacoma International Airport |  | US | 1065 |
| 35 | Reno/Tahoe International Airport |  | US | 1064 |
| 36 | Calgary International Airport |  | CA | 1054 |
| 37 | Daniel K Inouye International Airport |  | US | 1052 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 680 | 21m | 244 km | 2,863.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 431 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 265 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 228 | 12m | - | - |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 224 | 50m | 556 km | 2,147.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N205BT |  | Auburn Municipal Airport (KAUN) | Alta Sierra Airport (09CL) | 2026-08-10 21:59 UTC | 2026-08-10 22:09 UTC | 10m |
| STGRY57 | STG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Fall Creek Ranch Airport (XA43) | 2026-08-10 21:03 UTC | 2026-08-10 22:08 UTC | 1h 5m |
| COBRA43 | COB | Edwards Af Aux North Base Airport (K9L2) | California City Municipal Airport (KL71) | 2026-08-10 21:43 UTC | 2026-08-10 22:08 UTC | 24m |
| N685DW |  | Lebanon Municipal Airport (KLEB) | Concord Municipal Airport (KCON) | 2026-08-10 21:40 UTC | 2026-08-10 22:07 UTC | 27m |
| N216SR |  | Camp Bullis Als (Cals) Airport (9TX5) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-08-10 21:24 UTC | 2026-08-10 22:05 UTC | 40m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 21:43 UTC | 2026-08-10 22:01 UTC | 18m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Skypark Airport (KBTF) | 2026-08-10 21:42 UTC | 2026-08-10 22:00 UTC | 17m |
| SGE67 | SGE | Aero Valley Airport (K52F) | Aero Valley Airport (K52F) | 2026-08-10 21:20 UTC | 2026-08-10 21:58 UTC | 38m |
| N75972 |  | Airlake Airport (KLVN) | Faribault Municipal-Liz Wall Strohfus Field (KFBL) | 2026-08-10 21:41 UTC | 2026-08-10 21:54 UTC | 12m |
| N782AZ |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-08-10 21:49 UTC | 2026-08-10 21:52 UTC | 3m |
| N760C |  | Jacksonville International Airport (KJAX) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-10 20:07 UTC | 2026-08-10 21:52 UTC | 1h 45m |
| N8382A |  | Kansas City Downtown/Wheeler Field (KMKC) | K4K3 (K4K3) | 2026-08-10 21:31 UTC | 2026-08-10 21:51 UTC | 20m |
| TKR137 | TKR | Mc Clellan Airfield (KMCC) | Sierraville Dearwater Airport (KO79) | 2026-08-10 21:37 UTC | 2026-08-10 21:50 UTC | 13m |
| N182KQ |  | Decatur Shores Airport (WN07) | Boeing Field/King County International Airport (KBFI) | 2026-08-10 21:11 UTC | 2026-08-10 21:47 UTC | 35m |
| OAE271 | OAE | Perot Field/Fort Worth Alliance Airport (KAFW) | Seattle-Tacoma International Airport (KSEA) | 2026-08-10 18:04 UTC | 2026-08-10 21:43 UTC | 3h 38m |
| N438SP |  | Hesler/Noble Field (KLUL) | Kinder Ag Service Airport (LA57) | 2026-08-10 21:11 UTC | 2026-08-10 21:42 UTC | 30m |
| EJU42YF | EJU | Madeira Airport (LPMA) | Francisco de Sá Carneiro Airport (LPPR) | 2026-08-10 20:03 UTC | 2026-08-10 21:41 UTC | 1h 37m |
| ARCAS21 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-08-10 21:25 UTC | 2026-08-10 21:38 UTC | 13m |
| N4975F |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-08-10 21:21 UTC | 2026-08-10 21:38 UTC | 17m |
| N31831 |  | Tweed/New Haven Airport (KHVN) | Tweed/New Haven Airport (KHVN) | 2026-08-10 19:54 UTC | 2026-08-10 21:36 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
