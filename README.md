# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_15:56:55_UTC-green)

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

**Latest saved flight:** 2026-07-29 15:56:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 15:56:55 UTC

- **158,448** saved flights
- **52,482** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **158,448** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,901,770.6 tonnes** estimated CO2 emissions
- **110,247,571 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6369 |
| 2 | SkyWest Airlines | 5782 |
| 3 | EJA | 3127 |
| 4 | IndiGo | 2800 |
| 5 | American Airlines | 2516 |
| 6 | Southwest Airlines | 2485 |
| 7 | ENY | 1972 |
| 8 | Delta Air Lines | 1876 |
| 9 | Lufthansa | 1515 |
| 10 | LATAM Airlines | 1485 |
| 11 | AZU | 1393 |
| 12 | WIF | 1339 |
| 13 | Vueling | 1331 |
| 14 | LXJ | 1220 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1093 |
| 17 | easyJet | 1034 |
| 18 | Alaska Airlines | 991 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 970 |
| 22 | VIV | 869 |
| 23 | CXK | 840 |
| 24 | United Airlines | 838 |
| 25 | Cathay Pacific | 833 |
| 26 | GLO | 832 |
| 27 | AEE | 828 |
| 28 | Air France | 825 |
| 29 | MXY | 824 |
| 30 | JetBlue | 817 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 136556 |
| 2 | 🇪🇸 ES | 10201 |
| 3 | 🇧🇷 BR | 9056 |
| 4 | 🇦🇺 AU | 8952 |
| 5 | 🇮🇳 IN | 8806 |
| 6 | 🇨🇦 CA | 8581 |
| 7 | 🇮🇹 IT | 8186 |
| 8 | 🇩🇪 DE | 8043 |
| 9 | 🇬🇧 GB | 7276 |
| 10 | 🇯🇵 JP | 6480 |
| 11 | 🇫🇷 FR | 6279 |
| 12 | 🇨🇴 CO | 5564 |
| 13 | 🇲🇽 MX | 4542 |
| 14 | 🇬🇷 GR | 4537 |
| 15 | 🇳🇴 NO | 4194 |
| 16 | 🇨🇭 CH | 4160 |
| 17 | 🇹🇷 TR | 3789 |
| 18 | 🇲🇾 MY | 2892 |
| 19 | 🇵🇱 PL | 2699 |
| 20 | 🇿🇦 ZA | 2570 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2274 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2031 |
| 26 | 🇲🇦 MA | 1615 |
| 27 | 🇲🇪 ME | 1521 |
| 28 | 🇭🇷 HR | 1466 |
| 29 | 🇳🇱 NL | 1449 |
| 30 | 🇲🇴 MO | 1311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3246 |
| 2 | Denver International Airport |  | US | 2641 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 1987 |
| 5 | Indira Gandhi International Airport |  | IN | 1958 |
| 6 | Harry Reid International Airport |  | US | 1929 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1755 |
| 8 | Zurich Airport |  | CH | 1700 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1661 |
| 10 | La Aurora Airport |  | GT | 1575 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1476 |
| 12 | Frankfurt am Main International Airport |  | DE | 1461 |
| 13 | El Dorado International Airport |  | CO | 1445 |
| 14 | Chicago O'Hare International Airport |  | US | 1433 |
| 15 | Salt Lake City International Airport |  | US | 1422 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1324 |
| 17 | Macau International Airport |  | MO | 1311 |
| 18 | Congonhas Airport |  | BR | 1309 |
| 19 | Madrid Barajas International Airport |  | ES | 1260 |
| 20 | Capua Airport |  | IT | 1248 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1215 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1137 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1128 |
| 24 | Charlotte/Douglas International Airport |  | US | 1114 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1089 |
| 27 | Bengaluru International Airport |  | IN | 1049 |
| 28 | Malpensa International Airport |  | IT | 1043 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 962 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 960 |
| 32 | Barcelona International Airport |  | ES | 947 |
| 33 | Daniel K Inouye International Airport |  | US | 934 |
| 34 | Seattle-Tacoma International Airport |  | US | 923 |
| 35 | Calgary International Airport |  | CA | 908 |
| 36 | Viracopos International Airport |  | BR | 905 |
| 37 | Tenerife Norte Airport |  | ES | 896 |
| 38 | Scottsdale Airport |  | US | 895 |
| 39 | Oslo Gardermoen Airport |  | NO | 881 |
| 40 | Amsterdam Airport Schiphol |  | NL | 872 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 833 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 573 | 21m | 244 km | 2,412.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 378 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 224 | 44m | 241 km | 930.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 213 | 1h 47m | 1,423 km | 5,227.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 208 | 26m | 215 km | 770.3 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 204 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 190 | 30m | 49 km | 160.6 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 187 | 1h 15m | 961 km | 3,099.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 187 | 18m | 144 km | 465.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 180 | 50m | 556 km | 1,725.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 178 | 1h 39m | 1,156 km | 3,551.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 175 | 1h 1m | 695 km | 2,097.7 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 49m | 1,304 km | 3,779.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MGETS | MGE | Denham Aerodrome (EGLD) | Alderney Airport (EGJA) | 2026-07-29 15:09 UTC | 2026-07-29 15:56 UTC | 47m |
| TOTES72 | TOT | Troy Municipal At N Kenneth Campbell Field (KTOI) | AL37 (AL37) | 2026-07-29 15:38 UTC | 2026-07-29 15:52 UTC | 13m |
| SCU38 | SCU | Ragwing Acres Airport (2OK4) | Ragwing Acres Airport (2OK4) | 2026-07-29 15:36 UTC | 2026-07-29 15:49 UTC | 12m |
| RTY592 | RTY | Northern Colorado Regional Airport (KFNL) | Fort Morgan Municipal Airport (KFMM) | 2026-07-29 15:13 UTC | 2026-07-29 15:48 UTC | 34m |
| N5991W |  | Chickasha Municipal Airport (KCHK) | Anadarko Municipal Airport (KF68) | 2026-07-29 14:38 UTC | 2026-07-29 15:41 UTC | 1h 2m |
| OXF3076 | OXF | Falcon Field (KFFZ) | Phoenix Goodyear Airport (KGYR) | 2026-07-29 13:43 UTC | 2026-07-29 15:41 UTC | 1h 57m |
| CSN378 | China Southern | Madrid Barajas International Airport (LEMD) | Guangzhou Baiyun International Airport (ZGGG) | 2026-07-28 19:19 UTC | 2026-07-29 15:40 UTC | 20h 21m |
| XBMFB | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-29 14:57 UTC | 2026-07-29 15:31 UTC | 34m |
| N2355E |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-07-29 14:57 UTC | 2026-07-29 15:29 UTC | 31m |
| SPAIK | SPA | Malbork Military Air Base (EPMB) | Malbork Military Air Base (EPMB) | 2026-07-29 14:56 UTC | 2026-07-29 15:26 UTC | 30m |
| XSN37 | XSN | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-07-29 14:48 UTC | 2026-07-29 15:24 UTC | 36m |
| N312BD |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-07-29 15:17 UTC | 2026-07-29 15:24 UTC | 6m |
| N8344V |  | Lake In The Hills Airport (K3CK) | Dubuque Regional Airport (KDBQ) | 2026-07-29 14:20 UTC | 2026-07-29 15:23 UTC | 1h 2m |
| FTO381 | FTO | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-07-29 14:44 UTC | 2026-07-29 15:21 UTC | 37m |
| N13524 |  | Fairfield County Airport (KLHQ) | Fairfield County Airport (KLHQ) | 2026-07-29 15:02 UTC | 2026-07-29 15:21 UTC | 19m |
| N172UF |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-07-29 14:57 UTC | 2026-07-29 15:21 UTC | 23m |
| DHK813 | DHK | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-07-29 04:29 UTC | 2026-07-29 15:19 UTC | 10h 50m |
| HK1886G |  | Santa Ana Airport (SKGO) | Matecana International Airport (SKPE) | 2026-07-29 15:02 UTC | 2026-07-29 15:19 UTC | 16m |
| N407AP |  | Lake Tahoe Airport (KTVL) | Alpine County Airport (KM45) | 2026-07-29 14:59 UTC | 2026-07-29 15:18 UTC | 19m |
| N334BG |  | Wood County Airport (K1G0) | 72OI (72OI) | 2026-07-29 14:51 UTC | 2026-07-29 15:17 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
