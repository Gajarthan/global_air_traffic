# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_15:03:51_UTC-green)

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

**Latest saved flight:** 2026-08-15 15:03:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 15:03:51 UTC

- **198,725** saved flights
- **62,125** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **198,725** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,373,992.1 tonnes** estimated CO2 emissions
- **137,622,729 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7904 |
| 2 | SkyWest Airlines | 7117 |
| 3 | EJA | 3900 |
| 4 | IndiGo | 3440 |
| 5 | Southwest Airlines | 3071 |
| 6 | American Airlines | 3055 |
| 7 | ENY | 2446 |
| 8 | Delta Air Lines | 2350 |
| 9 | LATAM Airlines | 1867 |
| 10 | AZU | 1806 |
| 11 | Lufthansa | 1702 |
| 12 | Vueling | 1669 |
| 13 | WIF | 1639 |
| 14 | LXJ | 1572 |
| 15 | easyJet | 1364 |
| 16 | Swiss International | 1344 |
| 17 | AXM | 1307 |
| 18 | EJU | 1231 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1096 |
| 23 | GLO | 1075 |
| 24 | Air France | 1052 |
| 25 | PGT | 1047 |
| 26 | AEE | 1023 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1007 |
| 29 | WMT | 1001 |
| 30 | Wizz Air | 983 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168371 |
| 2 | 🇪🇸 ES | 12838 |
| 3 | 🇧🇷 BR | 11450 |
| 4 | 🇦🇺 AU | 11146 |
| 5 | 🇨🇦 CA | 10852 |
| 6 | 🇮🇳 IN | 10748 |
| 7 | 🇮🇹 IT | 10401 |
| 8 | 🇩🇪 DE | 9871 |
| 9 | 🇬🇧 GB | 9347 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7925 |
| 12 | 🇨🇴 CO | 7853 |
| 13 | 🇬🇷 GR | 5862 |
| 14 | 🇲🇽 MX | 5613 |
| 15 | 🇹🇷 TR | 5498 |
| 16 | 🇨🇭 CH | 5394 |
| 17 | 🇳🇴 NO | 5072 |
| 18 | 🇲🇾 MY | 3427 |
| 19 | 🇿🇦 ZA | 3364 |
| 20 | 🇵🇱 PL | 3288 |
| 21 | 🇹🇭 TH | 3127 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2537 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2104 |
| 27 | 🇲🇦 MA | 2012 |
| 28 | 🇳🇱 NL | 1786 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1631 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4121 |
| 2 | Denver International Airport |  | US | 3222 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2450 |
| 5 | Indira Gandhi International Airport |  | IN | 2436 |
| 6 | Harry Reid International Airport |  | US | 2270 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2103 |
| 8 | Zurich Airport |  | CH | 2102 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2053 |
| 10 | La Aurora Airport |  | GT | 1945 |
| 11 | El Dorado International Airport |  | CO | 1824 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1761 |
| 14 | Chicago O'Hare International Airport |  | US | 1737 |
| 15 | Congonhas Airport |  | BR | 1674 |
| 16 | Frankfurt am Main International Airport |  | DE | 1674 |
| 17 | Madrid Barajas International Airport |  | ES | 1565 |
| 18 | Macau International Airport |  | MO | 1535 |
| 19 | Capua Airport |  | IT | 1519 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1511 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1460 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1433 |
| 23 | Malpensa International Airport |  | IT | 1382 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1381 |
| 25 | Charles de Gaulle International Airport |  | FR | 1367 |
| 26 | Charlotte/Douglas International Airport |  | US | 1311 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1255 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1241 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1197 |
| 33 | Viracopos International Airport |  | BR | 1161 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1118 |
| 37 | Reno/Tahoe International Airport |  | US | 1116 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1094 |
| 40 | Tenerife Norte Airport |  | ES | 1090 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1009 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 362 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 340 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 334 | 27m | 275 km | 1,582.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 290 | 1h 49m | 1,423 km | 7,117.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 242 | 1h 15m | 961 km | 4,011.3 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 237 | 1h 38m | 1,156 km | 4,728.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 232 | 19m | 144 km | 577.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 215 | 1h 3m | 695 km | 2,577.2 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 215 | 1h 48m | 1,304 km | 4,837.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-14 20:44 UTC | 2026-08-15 15:03 UTC | 18h 19m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-15 14:38 UTC | 2026-08-15 15:03 UTC | 24m |
| N801JA |  | Pru Field (K33S) | Pru Field (K33S) | 2026-08-15 14:44 UTC | 2026-08-15 15:01 UTC | 16m |
| N4692Q |  | Rogue Valley International/Medford Airport (KMFR) | Rogue Valley International/Medford Airport (KMFR) | 2026-08-15 13:50 UTC | 2026-08-15 14:56 UTC | 1h 6m |
| OKBWR | OKB | Kromeriz Airport (LKKM) | LKSP (LKSP) | 2026-08-15 14:43 UTC | 2026-08-15 14:53 UTC | 10m |
| N629LE |  | Skypark Airport (KBTF) | Skypark Airport (KBTF) | 2026-08-15 14:42 UTC | 2026-08-15 14:53 UTC | 10m |
| CAP2776 | CAP | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-08-15 13:28 UTC | 2026-08-15 14:49 UTC | 1h 21m |
| N892MM |  | Dubuque Regional Airport (KDBQ) | Mason County Airport (KLDM) | 2026-08-15 13:35 UTC | 2026-08-15 14:47 UTC | 1h 12m |
| N39688 |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-08-15 14:34 UTC | 2026-08-15 14:45 UTC | 10m |
| RAX747 | RAX | Oakland County International Airport (KPTK) | Grayling Army Air Field (KGOV) | 2026-08-15 14:02 UTC | 2026-08-15 14:40 UTC | 37m |
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-08-15 14:18 UTC | 2026-08-15 14:34 UTC | 16m |
| PH1529 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-08-15 14:27 UTC | 2026-08-15 14:34 UTC | 7m |
| AWG4220 | AWG | Henri Coanda International Airport (LROP) | Isparta Airport (LTBM) | 2026-08-15 13:21 UTC | 2026-08-15 14:33 UTC | 1h 12m |
| N5229H |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-08-15 14:09 UTC | 2026-08-15 14:33 UTC | 23m |
| N3628H |  | Heritage Field (KPTW) | 1PA9 (1PA9) | 2026-08-15 13:59 UTC | 2026-08-15 14:30 UTC | 31m |
| N115GK |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-08-15 14:04 UTC | 2026-08-15 14:29 UTC | 24m |
| N742FH |  | Morgan County Airport (K42U) | Flying R Airport (11UT) | 2026-08-15 14:22 UTC | 2026-08-15 14:28 UTC | 5m |
| OKPUL | OKP | Pribram Airport (LKPM) | Hosin Airport (LKHS) | 2026-08-15 13:52 UTC | 2026-08-15 14:25 UTC | 33m |
| N728GD |  | Morgan County Airport (K42U) | Cavok Ranch Airport (UT90) | 2026-08-15 14:09 UTC | 2026-08-15 14:20 UTC | 10m |
| N383AA |  | Malin Airport (SOML) | Quiruvilca Airport (SPQR) | 2026-08-15 14:07 UTC | 2026-08-15 14:18 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
