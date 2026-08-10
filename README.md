# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_00:28:07_UTC-green)

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

**Latest saved flight:** 2026-08-10 00:28:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 00:28:07 UTC

- **183,104** saved flights
- **58,437** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,104** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,200,992.8 tonnes** estimated CO2 emissions
- **127,593,786 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7262 |
| 2 | SkyWest Airlines | 6677 |
| 3 | EJA | 3627 |
| 4 | IndiGo | 3195 |
| 5 | Southwest Airlines | 2873 |
| 6 | American Airlines | 2863 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2170 |
| 9 | LATAM Airlines | 1715 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1508 |
| 14 | LXJ | 1449 |
| 15 | easyJet | 1254 |
| 16 | Swiss International | 1252 |
| 17 | AXM | 1227 |
| 18 | EJU | 1124 |
| 19 | QLK | 1118 |
| 20 | All Nippon Airways | 1109 |
| 21 | Alaska Airlines | 1100 |
| 22 | VIV | 1010 |
| 23 | GLO | 984 |
| 24 | AEE | 955 |
| 25 | CXK | 953 |
| 26 | Air France | 948 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 926 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156798 |
| 2 | 🇪🇸 ES | 11750 |
| 3 | 🇧🇷 BR | 10534 |
| 4 | 🇦🇺 AU | 10223 |
| 5 | 🇮🇳 IN | 10009 |
| 6 | 🇨🇦 CA | 9984 |
| 7 | 🇮🇹 IT | 9471 |
| 8 | 🇩🇪 DE | 9055 |
| 9 | 🇬🇧 GB | 8487 |
| 10 | 🇯🇵 JP | 7399 |
| 11 | 🇫🇷 FR | 7283 |
| 12 | 🇨🇴 CO | 6862 |
| 13 | 🇬🇷 GR | 5367 |
| 14 | 🇲🇽 MX | 5240 |
| 15 | 🇨🇭 CH | 4879 |
| 16 | 🇹🇷 TR | 4753 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3199 |
| 19 | 🇵🇱 PL | 3066 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2805 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2416 |
| 24 | 🇬🇹 GT | 2349 |
| 25 | 🇰🇷 KR | 2269 |
| 26 | 🇲🇦 MA | 1851 |
| 27 | 🇭🇷 HR | 1828 |
| 28 | 🇲🇪 ME | 1651 |
| 29 | 🇳🇱 NL | 1643 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3805 |
| 2 | Denver International Airport |  | US | 3034 |
| 3 | Tokyo International Airport |  | JP | 2293 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2145 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1964 |
| 8 | Zurich Airport |  | CH | 1953 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1906 |
| 10 | La Aurora Airport |  | GT | 1803 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1669 |
| 12 | El Dorado International Airport |  | CO | 1645 |
| 13 | Chicago O'Hare International Airport |  | US | 1637 |
| 14 | Salt Lake City International Airport |  | US | 1635 |
| 15 | Frankfurt am Main International Airport |  | DE | 1585 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1449 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1434 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1313 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1271 |
| 24 | Malpensa International Airport |  | IT | 1266 |
| 25 | Charles de Gaulle International Airport |  | FR | 1247 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1146 |
| 30 | Ninoy Aquino International Airport |  | PH | 1138 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1123 |
| 32 | Barcelona International Airport |  | ES | 1082 |
| 33 | Viracopos International Airport |  | BR | 1054 |
| 34 | Seattle-Tacoma International Airport |  | US | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Calgary International Airport |  | CA | 1046 |
| 37 | Daniel K Inouye International Airport |  | US | 1043 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 999 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 671 | 21m | 244 km | 2,825.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
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
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 223 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 212 | 31m | 369 km | 1,349.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 200 | 1h 1m | 695 km | 2,397.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NMA301 | NMA | Malpensa International Airport (LIMC) | Giza Embaba Airport (HEEM) | 2026-08-09 21:22 UTC | 2026-08-10 00:28 UTC | 3h 5m |
| N406AP |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-09 17:19 UTC | 2026-08-10 00:20 UTC | 7h 0m |
| 9MLIZ |  | Senai International Airport (WMKJ) | Senai International Airport (WMKJ) | 2026-08-09 23:51 UTC | 2026-08-10 00:17 UTC | 25m |
| TKR101 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-10 00:09 UTC | 2026-08-10 00:12 UTC | 2m |
| MSR965 | EgyptAir | Narita International Airport (RJAA) | HE12 (HE12) | 2026-08-09 11:42 UTC | 2026-08-09 23:55 UTC | 12h 12m |
| TKR168 | TKR | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-08-09 23:49 UTC | 2026-08-09 23:54 UTC | 5m |
| AEE930 | AEE | Eleftherios Venizelos International Airport (LGAV) | Giza Embaba Airport (HEEM) | 2026-08-09 22:29 UTC | 2026-08-09 23:53 UTC | 1h 24m |
| N8288R |  | Newton Municipal-Earl Johnson Field (KTNU) | Daviess County Airport (KDCY) | 2026-08-09 22:55 UTC | 2026-08-09 23:53 UTC | 57m |
| RUK3YJ | RUK | Ibn Batouta Airport (GMTT) | North Weald Airport (EGSX) | 2026-08-09 21:15 UTC | 2026-08-09 23:50 UTC | 2h 35m |
| RYR87XN | Ryanair | Dublin Airport (EIDW) | Sywell Aerodrome (EGBK) | 2026-08-09 23:01 UTC | 2026-08-09 23:50 UTC | 49m |
| RYR8JV | Ryanair | Helsinki Vantaa Airport (EFHK) | Elmsett Airport (EGST) | 2026-08-09 21:05 UTC | 2026-08-09 23:50 UTC | 2h 45m |
| N122JM |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-08-09 23:11 UTC | 2026-08-09 23:50 UTC | 38m |
| EXS70VV | EXS | Diagoras Airport (LGRP) | Cranfield Airport (EGTC) | 2026-08-09 19:48 UTC | 2026-08-09 23:50 UTC | 4h 1m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-09 23:33 UTC | 2026-08-09 23:47 UTC | 13m |
| N4872L |  | Harry Clever Field (KPHD) | Plane Country Airport (45OI) | 2026-08-09 23:03 UTC | 2026-08-09 23:44 UTC | 41m |
|  |  | Cairo International Airport (HECA) | Hulwan (HE15) | 2026-08-09 19:05 UTC | 2026-08-09 23:42 UTC | 4h 37m |
| ENY4255 | ENY | Dallas-Fort Worth International Airport (KDFW) | Fox Station Airport (78II) | 2026-08-09 21:55 UTC | 2026-08-09 23:42 UTC | 1h 46m |
| VKG809 | VKG | Diagoras Airport (LGRP) | Leszno Strzyzewi Airport (EPLS) | 2026-08-09 21:08 UTC | 2026-08-09 23:41 UTC | 2h 33m |
| RJA507 | Royal Jordanian | Queen Alia International Airport (OJAI) | Hulwan (HE15) | 2026-08-09 22:50 UTC | 2026-08-09 23:40 UTC | 50m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-08-09 22:56 UTC | 2026-08-09 23:40 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
