# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_20:51:49_UTC-green)

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

**Latest saved flight:** 2026-08-11 20:51:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 20:51:49 UTC

- **187,971** saved flights
- **59,552** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,971** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,254,401.4 tonnes** estimated CO2 emissions
- **130,689,937 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7471 |
| 2 | SkyWest Airlines | 6828 |
| 3 | EJA | 3706 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2939 |
| 6 | American Airlines | 2928 |
| 7 | ENY | 2330 |
| 8 | Delta Air Lines | 2212 |
| 9 | LATAM Airlines | 1757 |
| 10 | AZU | 1691 |
| 11 | Lufthansa | 1645 |
| 12 | Vueling | 1562 |
| 13 | WIF | 1556 |
| 14 | LXJ | 1472 |
| 15 | easyJet | 1296 |
| 16 | Swiss International | 1283 |
| 17 | AXM | 1247 |
| 18 | EJU | 1163 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1119 |
| 22 | VIV | 1038 |
| 23 | GLO | 1012 |
| 24 | Air France | 977 |
| 25 | AEE | 969 |
| 26 | CXK | 965 |
| 27 | PGT | 965 |
| 28 | United Airlines | 958 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 935 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 160407 |
| 2 | 🇪🇸 ES | 12121 |
| 3 | 🇧🇷 BR | 10791 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇨🇦 CA | 10272 |
| 6 | 🇮🇳 IN | 10266 |
| 7 | 🇮🇹 IT | 9753 |
| 8 | 🇩🇪 DE | 9297 |
| 9 | 🇬🇧 GB | 8749 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7522 |
| 12 | 🇨🇴 CO | 7134 |
| 13 | 🇬🇷 GR | 5514 |
| 14 | 🇲🇽 MX | 5355 |
| 15 | 🇨🇭 CH | 5033 |
| 16 | 🇹🇷 TR | 4977 |
| 17 | 🇳🇴 NO | 4833 |
| 18 | 🇲🇾 MY | 3263 |
| 19 | 🇿🇦 ZA | 3156 |
| 20 | 🇵🇱 PL | 3116 |
| 21 | 🇹🇭 TH | 2895 |
| 22 | 🇳🇿 NZ | 2668 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2395 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1913 |
| 27 | 🇭🇷 HR | 1909 |
| 28 | 🇲🇪 ME | 1683 |
| 29 | 🇳🇱 NL | 1677 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3902 |
| 2 | Denver International Airport |  | US | 3097 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2308 |
| 6 | Harry Reid International Airport |  | US | 2198 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2000 |
| 8 | Zurich Airport |  | CH | 2000 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1946 |
| 10 | La Aurora Airport |  | GT | 1840 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1708 |
| 12 | El Dorado International Airport |  | CO | 1688 |
| 13 | Salt Lake City International Airport |  | US | 1676 |
| 14 | Chicago O'Hare International Airport |  | US | 1655 |
| 15 | Frankfurt am Main International Airport |  | DE | 1614 |
| 16 | Congonhas Airport |  | BR | 1572 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1483 |
| 19 | Capua Airport |  | IT | 1470 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1460 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1396 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1344 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1297 |
| 25 | Charles de Gaulle International Airport |  | FR | 1284 |
| 26 | Charlotte/Douglas International Airport |  | US | 1262 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1177 |
| 30 | Ninoy Aquino International Airport |  | PH | 1169 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1154 |
| 32 | Barcelona International Airport |  | ES | 1126 |
| 33 | Viracopos International Airport |  | BR | 1083 |
| 34 | Reno/Tahoe International Airport |  | US | 1081 |
| 35 | Seattle-Tacoma International Airport |  | US | 1078 |
| 36 | Calgary International Airport |  | CA | 1066 |
| 37 | Daniel K Inouye International Airport |  | US | 1059 |
| 38 | Oslo Gardermoen Airport |  | NO | 1051 |
| 39 | Tenerife Norte Airport |  | ES | 1032 |
| 40 | Vitoria/Foronda Airport |  | ES | 1019 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 952 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 687 | 21m | 244 km | 2,892.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 438 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 316 | 27m | 275 km | 1,497.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 304 | 14m | 114 km | 596.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 282 | 44m | 241 km | 1,171.4 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 280 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 271 | 22m | 55 km | 257.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 234 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 231 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 230 | 19m | 99 km | 394.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 229 | 1h 15m | 961 km | 3,795.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 229 | 50m | 556 km | 2,195.2 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 222 | 24m | 218 km | 836.4 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 203 | 1h 49m | 1,304 km | 4,567.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N2746C |  | Mesquite Metro Airport (KHQZ) | Mesquite Metro Airport (KHQZ) | 2026-08-11 19:41 UTC | 2026-08-11 20:51 UTC | 1h 10m |
| N924S |  | New Castle Airport (KILG) | Lakefront Airport (KNEW) | 2026-08-11 18:31 UTC | 2026-08-11 20:44 UTC | 2h 13m |
| TKR804 | TKR | Alice International Airport (KALI) | Alice International Airport (KALI) | 2026-08-11 20:00 UTC | 2026-08-11 20:39 UTC | 39m |
| ZKTPW | ZKT | Waipukurau Airport (NZYP) | Napier Airport (NZNR) | 2026-08-11 19:19 UTC | 2026-08-11 20:36 UTC | 1h 17m |
| N756EP |  | K1A0 (K1A0) | 2GA6 (2GA6) | 2026-08-11 20:21 UTC | 2026-08-11 20:34 UTC | 12m |
| N738GM |  | Mayport Ns (Adm David L Mcdonald Field) Airport (KNRB) | St Augustine Airport (KSGJ) | 2026-08-11 20:14 UTC | 2026-08-11 20:33 UTC | 19m |
| BULET47 | BUL | San Clemente Island Nalf Airport (KNUC) | San Clemente Island Nalf Airport (KNUC) | 2026-08-11 19:43 UTC | 2026-08-11 20:33 UTC | 50m |
| TIGER31 | TIG | Maverick County Memorial International Airport (K5T9) | Hughes Ranch Airport (50XS) | 2026-08-11 20:13 UTC | 2026-08-11 20:31 UTC | 18m |
| AIRTAC67 | AIR | Chamberlain Airport (OR60) | Chamberlain Airport (OR60) | 2026-08-11 18:53 UTC | 2026-08-11 20:31 UTC | 1h 37m |
| N473CA |  | Oxnard Airport (KOXR) | Bob Maxwell Memorial Airfield (KOKB) | 2026-08-11 18:44 UTC | 2026-08-11 20:28 UTC | 1h 43m |
| SHADO76 | SHA | Albuquerque International Sunport Airport (KABQ) | Curtis And Curtis Airport (65NM) | 2026-08-11 17:13 UTC | 2026-08-11 20:26 UTC | 3h 12m |
| MAFFS4 | MAF | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-11 20:07 UTC | 2026-08-11 20:24 UTC | 16m |
|  |  | SKAN (SKAN) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-11 20:23 UTC | 2026-08-11 20:24 UTC | 0m |
| BTZ119 | BTZ | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-08-11 20:09 UTC | 2026-08-11 20:21 UTC | 12m |
| MSTG89 | MST | Saskatoon John G. Diefenbaker International Airport (CYXE) | Lethbridge (Mercer Field) (CMF3) | 2026-08-11 18:34 UTC | 2026-08-11 20:21 UTC | 1h 46m |
| N454NC |  | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-11 19:41 UTC | 2026-08-11 20:19 UTC | 38m |
| N869CP |  | Lyall Airport (37CL) | Ramona Airport (KRNM) | 2026-08-11 20:07 UTC | 2026-08-11 20:19 UTC | 11m |
| N288CH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-11 20:10 UTC | 2026-08-11 20:16 UTC | 6m |
| 494LG |  | Simonson Field (80CO) | 14CO (14CO) | 2026-08-11 20:02 UTC | 2026-08-11 20:14 UTC | 12m |
| N101CC |  | 2KY3 (2KY3) | C A Moore Airport (K19M) | 2026-08-11 18:53 UTC | 2026-08-11 20:12 UTC | 1h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
