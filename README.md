# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_22:49:09_UTC-green)

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

**Latest saved flight:** 2026-08-12 22:49:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 22:49:09 UTC

- **191,000** saved flights
- **60,276** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,000** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,286,084.7 tonnes** estimated CO2 emissions
- **132,526,651 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7580 |
| 2 | SkyWest Airlines | 6922 |
| 3 | EJA | 3778 |
| 4 | IndiGo | 3310 |
| 5 | Southwest Airlines | 2985 |
| 6 | American Airlines | 2967 |
| 7 | ENY | 2369 |
| 8 | Delta Air Lines | 2245 |
| 9 | LATAM Airlines | 1792 |
| 10 | AZU | 1729 |
| 11 | Lufthansa | 1661 |
| 12 | WIF | 1584 |
| 13 | Vueling | 1583 |
| 14 | LXJ | 1500 |
| 15 | easyJet | 1317 |
| 16 | Swiss International | 1300 |
| 17 | AXM | 1253 |
| 18 | EJU | 1179 |
| 19 | QLK | 1169 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1138 |
| 22 | VIV | 1053 |
| 23 | GLO | 1031 |
| 24 | Air France | 995 |
| 25 | PGT | 987 |
| 26 | CXK | 981 |
| 27 | United Airlines | 976 |
| 28 | AEE | 975 |
| 29 | WMT | 949 |
| 30 | Cathay Pacific | 947 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 162923 |
| 2 | 🇪🇸 ES | 12302 |
| 3 | 🇧🇷 BR | 10999 |
| 4 | 🇦🇺 AU | 10666 |
| 5 | 🇨🇦 CA | 10477 |
| 6 | 🇮🇳 IN | 10369 |
| 7 | 🇮🇹 IT | 9918 |
| 8 | 🇩🇪 DE | 9441 |
| 9 | 🇬🇧 GB | 8895 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7633 |
| 12 | 🇨🇴 CO | 7367 |
| 13 | 🇬🇷 GR | 5579 |
| 14 | 🇲🇽 MX | 5413 |
| 15 | 🇨🇭 CH | 5109 |
| 16 | 🇹🇷 TR | 5093 |
| 17 | 🇳🇴 NO | 4912 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3214 |
| 20 | 🇵🇱 PL | 3156 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2512 |
| 24 | 🇬🇹 GT | 2416 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1964 |
| 27 | 🇲🇦 MA | 1936 |
| 28 | 🇳🇱 NL | 1704 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3973 |
| 2 | Denver International Airport |  | US | 3138 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2336 |
| 6 | Harry Reid International Airport |  | US | 2227 |
| 7 | Zurich Airport |  | CH | 2024 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2018 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1981 |
| 10 | La Aurora Airport |  | GT | 1857 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1729 |
| 12 | El Dorado International Airport |  | CO | 1728 |
| 13 | Salt Lake City International Airport |  | US | 1697 |
| 14 | Chicago O'Hare International Airport |  | US | 1672 |
| 15 | Frankfurt am Main International Airport |  | DE | 1627 |
| 16 | Congonhas Airport |  | BR | 1599 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1506 |
| 19 | Capua Airport |  | IT | 1481 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1479 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1411 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1372 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1318 |
| 25 | Charles de Gaulle International Airport |  | FR | 1306 |
| 26 | Charlotte/Douglas International Airport |  | US | 1276 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1225 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1194 |
| 30 | Ninoy Aquino International Airport |  | PH | 1187 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1172 |
| 32 | Barcelona International Airport |  | ES | 1139 |
| 33 | Viracopos International Airport |  | BR | 1112 |
| 34 | Seattle-Tacoma International Airport |  | US | 1100 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1092 |
| 37 | Daniel K Inouye International Airport |  | US | 1071 |
| 38 | Oslo Gardermoen Airport |  | NO | 1067 |
| 39 | Tenerife Norte Airport |  | ES | 1047 |
| 40 | Vitoria/Foronda Airport |  | ES | 1035 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 699 | 21m | 244 km | 2,943.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 444 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
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
| N48842 |  | Piedmont Triad International Airport (KGSO) | Burlington/Alamance Regional Airport (KBUY) | 2026-08-12 22:22 UTC | 2026-08-12 22:49 UTC | 26m |
| JOLLY91 | JOL | Watsonville Municipal Airport (KWVI) | Moffett Federal Airfield (KNUQ) | 2026-08-12 22:06 UTC | 2026-08-12 22:47 UTC | 41m |
| CFR652 | CFR | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-08-12 22:04 UTC | 2026-08-12 22:39 UTC | 35m |
| N42SH |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-08-12 21:44 UTC | 2026-08-12 22:39 UTC | 55m |
| CGHAP | CGH | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-08-12 22:03 UTC | 2026-08-12 22:34 UTC | 30m |
| SLH560 | SLH | NE37 (NE37) | Joe Foss Field (KFSD) | 2026-08-12 22:05 UTC | 2026-08-12 22:29 UTC | 24m |
| N525RA |  | Middleton Municipal/Morey Field (KC29) | 4WI2 (4WI2) | 2026-08-12 21:53 UTC | 2026-08-12 22:26 UTC | 33m |
| N714F |  | Rogers Executive - Carter Field (KROG) | Logan-Cache Airport (KLGU) | 2026-08-12 20:12 UTC | 2026-08-12 22:24 UTC | 2h 12m |
| ICY49 | ICY | Highland Airport (47AK) | Elmendorf Afb Airport (PAED) | 2026-08-12 21:03 UTC | 2026-08-12 22:24 UTC | 1h 20m |
| N314LM |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-08-12 22:00 UTC | 2026-08-12 22:23 UTC | 22m |
| N1934F |  | Willow Run Airport (KYIP) | Boyne Mountain Airport (KBFA) | 2026-08-12 21:49 UTC | 2026-08-12 22:22 UTC | 32m |
| N18JA |  | Aurora Municipal Airport (KARR) | 0IL8 (0IL8) | 2026-08-12 21:45 UTC | 2026-08-12 22:19 UTC | 33m |
| N98485 |  | Livermore Municipal Airport (KLVK) | Sacramento Executive Airport (KSAC) | 2026-08-12 21:26 UTC | 2026-08-12 22:18 UTC | 51m |
| N1424V |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-12 21:35 UTC | 2026-08-12 22:17 UTC | 42m |
| N929KT |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-12 21:45 UTC | 2026-08-12 22:16 UTC | 30m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Perry Stokes Airport (KTAD) | 2026-08-12 21:55 UTC | 2026-08-12 22:14 UTC | 19m |
| OKC548 | OKC | City Of Colorado Springs Municipal Airport (KCOS) | South Fox Island Airport (3MI2) | 2026-08-12 20:08 UTC | 2026-08-12 22:12 UTC | 2h 4m |
| N821FR |  | Santa Monica Municipal Airport (KSMO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-12 21:19 UTC | 2026-08-12 22:12 UTC | 52m |
| N643WM |  | Viburnum Airport (MO84) | Domeyer Airport (13MO) | 2026-08-12 21:31 UTC | 2026-08-12 22:04 UTC | 33m |
| EJA696 | EJA | Chain-O-Lakes Airport (3IN7) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-12 21:27 UTC | 2026-08-12 22:03 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
