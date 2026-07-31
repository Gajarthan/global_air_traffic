# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_21:32:18_UTC-green)

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

**Latest saved flight:** 2026-07-31 21:32:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 21:32:18 UTC

- **163,472** saved flights
- **53,850** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,472** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,961,168.9 tonnes** estimated CO2 emissions
- **113,690,949 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6528 |
| 2 | SkyWest Airlines | 5966 |
| 3 | EJA | 3247 |
| 4 | IndiGo | 2860 |
| 5 | American Airlines | 2580 |
| 6 | Southwest Airlines | 2556 |
| 7 | ENY | 2034 |
| 8 | Delta Air Lines | 1950 |
| 9 | Lufthansa | 1530 |
| 10 | LATAM Airlines | 1530 |
| 11 | AZU | 1434 |
| 12 | WIF | 1378 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1271 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1071 |
| 18 | Alaska Airlines | 1013 |
| 19 | QLK | 1003 |
| 20 | EJU | 1001 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 901 |
| 23 | CXK | 878 |
| 24 | Cathay Pacific | 861 |
| 25 | United Airlines | 860 |
| 26 | GLO | 854 |
| 27 | AEE | 852 |
| 28 | Air France | 844 |
| 29 | MXY | 844 |
| 30 | JetBlue | 834 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141335 |
| 2 | 🇪🇸 ES | 10466 |
| 3 | 🇧🇷 BR | 9330 |
| 4 | 🇦🇺 AU | 9202 |
| 5 | 🇮🇳 IN | 8988 |
| 6 | 🇨🇦 CA | 8903 |
| 7 | 🇮🇹 IT | 8410 |
| 8 | 🇩🇪 DE | 8207 |
| 9 | 🇬🇧 GB | 7506 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6461 |
| 12 | 🇨🇴 CO | 5851 |
| 13 | 🇲🇽 MX | 4692 |
| 14 | 🇬🇷 GR | 4689 |
| 15 | 🇳🇴 NO | 4308 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3906 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2773 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2387 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1648 |
| 27 | 🇭🇷 HR | 1537 |
| 28 | 🇲🇪 ME | 1535 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1370 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3338 |
| 2 | Denver International Airport |  | US | 2724 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2061 |
| 5 | Indira Gandhi International Airport |  | IN | 1997 |
| 6 | Harry Reid International Airport |  | US | 1981 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1797 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1721 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1519 |
| 12 | El Dorado International Airport |  | CO | 1499 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1480 |
| 15 | Salt Lake City International Airport |  | US | 1471 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1373 |
| 17 | Macau International Airport |  | MO | 1370 |
| 18 | Congonhas Airport |  | BR | 1350 |
| 19 | Madrid Barajas International Airport |  | ES | 1290 |
| 20 | Capua Airport |  | IT | 1280 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1247 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1157 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 24 | Charlotte/Douglas International Airport |  | US | 1148 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1114 |
| 27 | Malpensa International Airport |  | IT | 1079 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1004 |
| 30 | Ninoy Aquino International Airport |  | PH | 1002 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 998 |
| 32 | Barcelona International Airport |  | ES | 967 |
| 33 | Daniel K Inouye International Airport |  | US | 958 |
| 34 | Seattle-Tacoma International Airport |  | US | 946 |
| 35 | Calgary International Airport |  | CA | 932 |
| 36 | Viracopos International Airport |  | BR | 927 |
| 37 | Scottsdale Airport |  | US | 916 |
| 38 | Tenerife Norte Airport |  | ES | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 897 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 596 | 21m | 244 km | 2,509.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 243 | 22m | 55 km | 231.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 200 | 30m | 49 km | 169.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 194 | 1h 15m | 961 km | 3,215.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5264K |  | Salisbury-Ocean City Wicomico Regional Airport (KSBY) | Kent Fort Manor Airport (7MD8) | 2026-07-31 19:53 UTC | 2026-07-31 21:32 UTC | 1h 39m |
| N118JK |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-31 20:26 UTC | 2026-07-31 21:31 UTC | 1h 4m |
| N46315 |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | Coeur D'Alene/Pappy Boyington Field (KCOE) | 2026-07-31 20:27 UTC | 2026-07-31 21:30 UTC | 1h 2m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-07-31 17:39 UTC | 2026-07-31 21:28 UTC | 3h 48m |
| N401AV |  | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-07-31 20:38 UTC | 2026-07-31 21:26 UTC | 47m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-07-31 10:37 UTC | 2026-07-31 21:24 UTC | 10h 46m |
| N20143 |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-07-31 20:34 UTC | 2026-07-31 21:22 UTC | 47m |
| DRACO71 | DRA | Dave Eby Field (4XA5) | Halliburton Field (KDUC) | 2026-07-31 20:48 UTC | 2026-07-31 21:19 UTC | 30m |
| JBU2260 | JetBlue | Madrid Barajas International Airport (LEMD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 13:45 UTC | 2026-07-31 21:18 UTC | 7h 33m |
| ETD931 | Etihad Airways | Al Bateen Executive Airport (OMAD) | Zhuhai Airport (ZGSD) | 2026-07-31 13:44 UTC | 2026-07-31 21:17 UTC | 7h 32m |
| DAL155 | Delta Air Lines | Dublin Airport (EIDW) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 14:44 UTC | 2026-07-31 21:16 UTC | 6h 31m |
| N401TD |  | Nevada County Airport (KGOO) | Alta Sierra Airport (09CL) | 2026-07-31 20:57 UTC | 2026-07-31 21:15 UTC | 18m |
| DAL1205 | Delta Air Lines | Palm Beach International Airport (KPBI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-31 17:55 UTC | 2026-07-31 21:14 UTC | 3h 19m |
| N407JM |  | Steamboat Springs/Bob Adams Field (KSBS) | Elk Park Ranch Airport (34CD) | 2026-07-31 20:32 UTC | 2026-07-31 21:10 UTC | 38m |
| N5298D |  | Seattle Paine Field International Airport (KPAE) | Oomrang Air Airport (15WA) | 2026-07-31 20:29 UTC | 2026-07-31 21:06 UTC | 36m |
| HKE235 | HKE | Beijing Nanyuan Airport (ZBNY) | Macau International Airport (VMMC) | 2026-07-31 18:41 UTC | 2026-07-31 21:05 UTC | 2h 24m |
| N78842 |  | Headwaters Airport (25XA) | Boerne Stage Airfield (K5C1) | 2026-07-31 19:09 UTC | 2026-07-31 21:03 UTC | 1h 54m |
| N3620C |  | Jim & Julie's Airport (96WA) | Easton State Airport (KESW) | 2026-07-31 20:28 UTC | 2026-07-31 21:01 UTC | 32m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-07-31 20:39 UTC | 2026-07-31 21:01 UTC | 21m |
| N734M |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-07-31 19:52 UTC | 2026-07-31 21:00 UTC | 1h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
