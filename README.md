# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_12:24:10_UTC-green)

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

**Latest saved flight:** 2026-08-16 12:24:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 12:24:10 UTC

- **204,438** saved flights
- **65,359** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,438** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,458,056.4 tonnes** estimated CO2 emissions
- **142,496,024 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8047 |
| 2 | SkyWest Airlines | 7352 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3501 |
| 5 | American Airlines | 3402 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2612 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1908 |
| 10 | AZU | 1840 |
| 11 | Lufthansa | 1741 |
| 12 | Vueling | 1693 |
| 13 | WIF | 1645 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1412 |
| 16 | Swiss International | 1362 |
| 17 | AXM | 1335 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1261 |
| 21 | EJU | 1250 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1120 |
| 24 | GLO | 1095 |
| 25 | Air France | 1090 |
| 26 | PGT | 1090 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1044 |
| 29 | WMT | 1023 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173816 |
| 2 | 🇪🇸 ES | 13071 |
| 3 | 🇧🇷 BR | 11657 |
| 4 | 🇦🇺 AU | 11482 |
| 5 | 🇨🇦 CA | 11281 |
| 6 | 🇮🇳 IN | 10932 |
| 7 | 🇮🇹 IT | 10619 |
| 8 | 🇩🇪 DE | 10114 |
| 9 | 🇬🇧 GB | 9535 |
| 10 | 🇯🇵 JP | 8452 |
| 11 | 🇫🇷 FR | 8098 |
| 12 | 🇨🇴 CO | 8052 |
| 13 | 🇬🇷 GR | 6009 |
| 14 | 🇹🇷 TR | 5754 |
| 15 | 🇲🇽 MX | 5744 |
| 16 | 🇨🇭 CH | 5476 |
| 17 | 🇳🇴 NO | 5096 |
| 18 | 🇲🇾 MY | 3516 |
| 19 | 🇿🇦 ZA | 3424 |
| 20 | 🇵🇱 PL | 3359 |
| 21 | 🇹🇭 TH | 3229 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2727 |
| 24 | 🇬🇹 GT | 2557 |
| 25 | 🇰🇷 KR | 2500 |
| 26 | 🇭🇷 HR | 2172 |
| 27 | 🇲🇦 MA | 2055 |
| 28 | 🇳🇱 NL | 1819 |
| 29 | 🇲🇪 ME | 1708 |
| 30 | 🇮🇩 ID | 1678 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4288 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2549 |
| 4 | Indira Gandhi International Airport |  | IN | 2482 |
| 5 | Guaymaral Airport |  | CO | 2476 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2137 |
| 8 | Zurich Airport |  | CH | 2129 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 10 | La Aurora Airport |  | GT | 1959 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1863 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1697 |
| 16 | Frankfurt am Main International Airport |  | DE | 1696 |
| 17 | Madrid Barajas International Airport |  | ES | 1599 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1551 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1407 |
| 25 | Charles de Gaulle International Airport |  | FR | 1398 |
| 26 | Charlotte/Douglas International Airport |  | US | 1391 |
| 27 | Kuala Lumpur International Airport |  | MY | 1302 |
| 28 | Ninoy Aquino International Airport |  | PH | 1292 |
| 29 | Bengaluru International Airport |  | IN | 1271 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1258 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1221 |
| 33 | Seattle-Tacoma International Airport |  | US | 1213 |
| 34 | Viracopos International Airport |  | BR | 1179 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1127 |
| 38 | Vitoria/Foronda Airport |  | ES | 1127 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 343 | 27m | 275 km | 1,625.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 300 | 44m | 241 km | 1,246.1 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 267 | 21m | 250 km | 1,153.3 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 254 | 24m | 218 km | 956.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 240 | 1h 37m | 1,156 km | 4,787.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 235 | 19m | 144 km | 584.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 232 | 31m | 369 km | 1,476.7 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 217 | 28m | 152 km | 567.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N46JG |  | Brandywine Regional Airport (KOQN) | Lancaster Airport (KLNS) | 2026-08-16 11:39 UTC | 2026-08-16 12:24 UTC | 44m |
| N835FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-08-16 12:02 UTC | 2026-08-16 12:23 UTC | 21m |
| N608PT |  | Miami Executive Airport (KTMB) | Marco Island Executive Airport (KMKY) | 2026-08-16 11:28 UTC | 2026-08-16 12:17 UTC | 49m |
| N108PT |  | Essex County Airport (KCDW) | Lewis Landing Airport (NK79) | 2026-08-16 11:52 UTC | 2026-08-16 12:14 UTC | 22m |
|  |  | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 11:55 UTC | 2026-08-16 12:05 UTC | 10m |
| SKW6407 | SkyWest Airlines | Mc Allen International Airport (KMFE) | Terrell County Airport (K6R6) | 2026-08-16 11:19 UTC | 2026-08-16 12:05 UTC | 45m |
| N738QN |  | Pearland Regional Airport (KLVJ) | Evans Aerodrome (XS39) | 2026-08-16 11:45 UTC | 2026-08-16 11:59 UTC | 14m |
| TGJOE | TGJ | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-08-16 11:26 UTC | 2026-08-16 11:58 UTC | 32m |
| RYR2689 | Ryanair | Parma Airport (LIMP) | North Weald Airport (EGSX) | 2026-08-16 10:10 UTC | 2026-08-16 11:56 UTC | 1h 46m |
| THY3443 | Turkish Airlines | Beirut Rafic Hariri International Airport (OLBA) | Queen Alia International Airport (OJAI) | 2026-08-16 11:29 UTC | 2026-08-16 11:56 UTC | 26m |
| AFR34MZ | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-08-16 11:04 UTC | 2026-08-16 11:53 UTC | 48m |
| N62SA |  | Pueblo Memorial Airport (KPUB) | Dalhart Municipal Airport (KDHT) | 2026-08-16 11:11 UTC | 2026-08-16 11:52 UTC | 40m |
| UBG165 | UBG | VGZR (VGZR) | Shah Mokhdum Airport (VGRJ) | 2026-08-16 11:23 UTC | 2026-08-16 11:52 UTC | 28m |
| SAMU05 | SAM | Gap - Tallard Airport (LFNA) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-08-16 11:32 UTC | 2026-08-16 11:51 UTC | 19m |
| GIPPS | GIP | Chichester/Goodwood Airport (EGHR) | Chichester/Goodwood Airport (EGHR) | 2026-08-16 11:41 UTC | 2026-08-16 11:51 UTC | 10m |
| AEE6DS | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-16 11:29 UTC | 2026-08-16 11:50 UTC | 21m |
| SAS63Z | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Linate Airport (LIML) | 2026-08-16 09:22 UTC | 2026-08-16 11:48 UTC | 2h 26m |
| JYRJK | JYR | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-08-16 11:17 UTC | 2026-08-16 11:48 UTC | 31m |
| AWH92B | AWH | Budapest Ferenc Liszt International Airport (LHBP) | Kiel-Holtenau Airport (EDHK) | 2026-08-16 09:25 UTC | 2026-08-16 11:47 UTC | 2h 21m |
| AZU4158 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-08-16 11:00 UTC | 2026-08-16 11:46 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
