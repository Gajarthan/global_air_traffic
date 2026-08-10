# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_02:47:07_UTC-green)

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

**Latest saved flight:** 2026-08-10 02:47:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 02:47:07 UTC

- **183,214** saved flights
- **58,458** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,214** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,202,137.4 tonnes** estimated CO2 emissions
- **127,660,140 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7262 |
| 2 | SkyWest Airlines | 6682 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3198 |
| 5 | Southwest Airlines | 2877 |
| 6 | American Airlines | 2866 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2171 |
| 9 | LATAM Airlines | 1715 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1508 |
| 14 | LXJ | 1450 |
| 15 | easyJet | 1255 |
| 16 | Swiss International | 1252 |
| 17 | AXM | 1227 |
| 18 | EJU | 1124 |
| 19 | QLK | 1119 |
| 20 | All Nippon Airways | 1112 |
| 21 | Alaska Airlines | 1102 |
| 22 | VIV | 1011 |
| 23 | GLO | 984 |
| 24 | AEE | 955 |
| 25 | CXK | 953 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 927 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156910 |
| 2 | 🇪🇸 ES | 11752 |
| 3 | 🇧🇷 BR | 10534 |
| 4 | 🇦🇺 AU | 10236 |
| 5 | 🇮🇳 IN | 10014 |
| 6 | 🇨🇦 CA | 9989 |
| 7 | 🇮🇹 IT | 9472 |
| 8 | 🇩🇪 DE | 9057 |
| 9 | 🇬🇧 GB | 8489 |
| 10 | 🇯🇵 JP | 7416 |
| 11 | 🇫🇷 FR | 7283 |
| 12 | 🇨🇴 CO | 6864 |
| 13 | 🇬🇷 GR | 5368 |
| 14 | 🇲🇽 MX | 5242 |
| 15 | 🇨🇭 CH | 4879 |
| 16 | 🇹🇷 TR | 4756 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3199 |
| 19 | 🇵🇱 PL | 3067 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2807 |
| 22 | 🇳🇿 NZ | 2615 |
| 23 | 🇵🇭 PH | 2422 |
| 24 | 🇬🇹 GT | 2349 |
| 25 | 🇰🇷 KR | 2273 |
| 26 | 🇲🇦 MA | 1851 |
| 27 | 🇭🇷 HR | 1828 |
| 28 | 🇲🇪 ME | 1651 |
| 29 | 🇳🇱 NL | 1643 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3807 |
| 2 | Denver International Airport |  | US | 3034 |
| 3 | Tokyo International Airport |  | JP | 2297 |
| 4 | Indira Gandhi International Airport |  | IN | 2238 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2146 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1964 |
| 8 | Zurich Airport |  | CH | 1953 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1907 |
| 10 | La Aurora Airport |  | GT | 1803 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1645 |
| 13 | Salt Lake City International Airport |  | US | 1637 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1438 |
| 20 | Capua Airport |  | IT | 1434 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1313 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1272 |
| 24 | Malpensa International Airport |  | IT | 1267 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1188 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1147 |
| 30 | Ninoy Aquino International Airport |  | PH | 1141 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1126 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Calgary International Airport |  | CA | 1046 |
| 37 | Daniel K Inouye International Airport |  | US | 1044 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 1000 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 672 | 21m | 244 km | 2,829.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 435 | 1h 8m | 770 km | 5,778.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 429 | 24m | 225 km | 1,664.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 225 | 19m | 99 km | 385.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 213 | 31m | 369 km | 1,355.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| A7GQE |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-08-10 02:11 UTC | 2026-08-10 02:47 UTC | 35m |
| N2334J |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-10 02:27 UTC | 2026-08-10 02:29 UTC | 1m |
| N817FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-09 23:33 UTC | 2026-08-10 02:21 UTC | 2h 48m |
| JA883B |  | Kagoshima Airport (RJFK) | Kumamoto Airport (RJFT) | 2026-08-09 23:06 UTC | 2026-08-10 02:19 UTC | 3h 13m |
| N51885 |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-10 00:28 UTC | 2026-08-10 02:18 UTC | 1h 49m |
| GCR6438 | GCR | Tianjin Binhai International Airport (ZBTJ) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-10 01:43 UTC | 2026-08-10 02:17 UTC | 34m |
| MSR796 | EgyptAir | Manchester Airport (EGCC) | HE42 (HE42) | 2026-08-09 21:58 UTC | 2026-08-10 02:16 UTC | 4h 17m |
| EPI230 | EPI | Tully Rv Airpark (2FD6) | Melbourne Orlando International Airport (KMLB) | 2026-08-10 01:05 UTC | 2026-08-10 02:10 UTC | 1h 5m |
| MSR740 | EgyptAir | Queen Alia International Airport (OJAI) | Hulwan (HE15) | 2026-08-10 01:11 UTC | 2026-08-10 02:00 UTC | 49m |
| TKR910 | TKR | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-10 01:46 UTC | 2026-08-10 02:00 UTC | 13m |
| EJA526 | EJA | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Austin-Bergstrom International Airport (KAUS) | 2026-08-09 23:34 UTC | 2026-08-10 01:58 UTC | 2h 23m |
| N122JM |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-10 01:21 UTC | 2026-08-10 01:56 UTC | 35m |
| NTR222 | NTR | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-08-10 01:10 UTC | 2026-08-10 01:54 UTC | 43m |
| N532LW |  | Mc Clellan-Palomar Airport (KCRQ) | Heiner Airport (WY60) | 2026-08-10 00:02 UTC | 2026-08-10 01:54 UTC | 1h 51m |
| SWA1316 | Southwest Airlines | Los Angeles International Airport (KLAX) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-10 01:02 UTC | 2026-08-10 01:53 UTC | 51m |
| CGF5959 | CGF | Leipzig Halle Airport (EDDP) | Bydgoszcz Ignacy Jan Paderewski Airport (EPBY) | 2026-08-10 01:16 UTC | 2026-08-10 01:51 UTC | 34m |
| KAP1881 | KAP | General Edward Lawrence Logan International Airport (KBOS) | Lebanon Municipal Airport (KLEB) | 2026-08-10 00:59 UTC | 2026-08-10 01:49 UTC | 50m |
| FYC | FYC | Hamilton Island Airport (YBHM) | Lakeside Airpark (YLAK) | 2026-08-10 01:36 UTC | 2026-08-10 01:49 UTC | 12m |
| N180JF |  | Nenana Municipal Airport (PANN) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-10 00:04 UTC | 2026-08-10 01:48 UTC | 1h 44m |
| IBX46 | IBX | Chitose Air Base (RJCJ) | Sendai Airport (RJSS) | 2026-08-10 01:06 UTC | 2026-08-10 01:47 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
