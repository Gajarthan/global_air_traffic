# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_00:33:17_UTC-green)

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

**Latest saved flight:** 2026-09-12 00:33:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 00:33:17 UTC

- **255,672** saved flights
- **76,297** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **255,672** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,086,914.7 tonnes** estimated CO2 emissions
- **178,951,576 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10181 |
| 2 | SkyWest Airlines | 8918 |
| 3 | EJA | 4941 |
| 4 | IndiGo | 4273 |
| 5 | American Airlines | 4054 |
| 6 | Southwest Airlines | 3764 |
| 7 | Delta Air Lines | 3203 |
| 8 | ENY | 3039 |
| 9 | LATAM Airlines | 2464 |
| 10 | AZU | 2382 |
| 11 | Vueling | 2164 |
| 12 | WIF | 2053 |
| 13 | Lufthansa | 2001 |
| 14 | LXJ | 1996 |
| 15 | easyJet | 1740 |
| 16 | Swiss International | 1711 |
| 17 | QLK | 1651 |
| 18 | AXM | 1639 |
| 19 | EJU | 1629 |
| 20 | United Airlines | 1586 |
| 21 | Alaska Airlines | 1518 |
| 22 | All Nippon Airways | 1491 |
| 23 | WMT | 1444 |
| 24 | GLO | 1426 |
| 25 | PGT | 1409 |
| 26 | VIV | 1401 |
| 27 | Air France | 1395 |
| 28 | Wizz Air | 1389 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1243 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 212369 |
| 2 | 🇪🇸 ES | 16254 |
| 3 | 🇧🇷 BR | 14933 |
| 4 | 🇦🇺 AU | 14589 |
| 5 | 🇨🇦 CA | 14247 |
| 6 | 🇮🇹 IT | 13965 |
| 7 | 🇮🇳 IN | 13390 |
| 8 | 🇩🇪 DE | 12473 |
| 9 | 🇬🇧 GB | 11929 |
| 10 | 🇨🇴 CO | 11382 |
| 11 | 🇫🇷 FR | 10262 |
| 12 | 🇯🇵 JP | 9988 |
| 13 | 🇹🇷 TR | 7660 |
| 14 | 🇬🇷 GR | 7456 |
| 15 | 🇲🇽 MX | 7059 |
| 16 | 🇨🇭 CH | 6854 |
| 17 | 🇳🇴 NO | 6339 |
| 18 | 🇹🇭 TH | 4590 |
| 19 | 🇲🇾 MY | 4409 |
| 20 | 🇿🇦 ZA | 4354 |
| 21 | 🇵🇱 PL | 4235 |
| 22 | 🇳🇿 NZ | 3535 |
| 23 | 🇵🇭 PH | 3442 |
| 24 | 🇬🇹 GT | 3209 |
| 25 | 🇰🇷 KR | 2933 |
| 26 | 🇭🇷 HR | 2925 |
| 27 | 🇲🇦 MA | 2576 |
| 28 | 🇲🇪 ME | 2401 |
| 29 | 🇳🇱 NL | 2300 |
| 30 | 🇮🇩 ID | 2175 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5245 |
| 2 | Denver International Airport |  | US | 4135 |
| 3 | Indira Gandhi International Airport |  | IN | 3087 |
| 4 | Tokyo International Airport |  | JP | 2983 |
| 5 | Guaymaral Airport |  | CO | 2759 |
| 6 | Harry Reid International Airport |  | US | 2708 |
| 7 | Zurich Airport |  | CH | 2675 |
| 8 | El Dorado International Airport |  | CO | 2632 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2580 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2501 |
| 11 | La Aurora Airport |  | GT | 2443 |
| 12 | Salt Lake City International Airport |  | US | 2256 |
| 13 | Chicago O'Hare International Airport |  | US | 2227 |
| 14 | Congonhas Airport |  | BR | 2193 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2092 |
| 16 | Capua Airport |  | IT | 2013 |
| 17 | Madrid Barajas International Airport |  | ES | 1995 |
| 18 | Frankfurt am Main International Airport |  | DE | 1976 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1919 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1850 |
| 21 | Malpensa International Airport |  | IT | 1838 |
| 22 | Charles de Gaulle International Airport |  | FR | 1799 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1797 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1777 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1722 |
| 26 | Macau International Airport |  | MO | 1694 |
| 27 | Ninoy Aquino International Airport |  | PH | 1683 |
| 28 | Barcelona International Airport |  | ES | 1606 |
| 29 | Charlotte/Douglas International Airport |  | US | 1602 |
| 30 | Kuala Lumpur International Airport |  | MY | 1587 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1571 |
| 32 | Viracopos International Airport |  | BR | 1528 |
| 33 | Seattle-Tacoma International Airport |  | US | 1500 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1486 |
| 35 | Calgary International Airport |  | CA | 1470 |
| 36 | Don Mueang International Airport |  | TH | 1469 |
| 37 | Bengaluru International Airport |  | IN | 1451 |
| 38 | Oslo Gardermoen Airport |  | NO | 1445 |
| 39 | Vancouver International Airport |  | CA | 1436 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1380 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 949 | 21m | 244 km | 3,996.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 684 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 640 | 1h 6m | 770 km | 8,501.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 638 | 24m | 225 km | 2,475.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 573 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 408 | 44m | 555 km | 3,906.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 405 | 1h 50m | 1,423 km | 9,939.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 386 | 44m | 241 km | 1,603.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 356 | 24m | 218 km | 1,341.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 341 | 23m | 55 km | 324.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 313 | 19m | 99 km | 536.1 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 309 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 303 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 294 | 1h 14m | 961 km | 4,873.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 293 | 19m | 144 km | 728.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 267 | 41m | 535 km | 2,465.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 265 | 28m | 152 km | 692.5 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N444ZG |  | Francis S Gabreski Airport (KFOK) | Brookhaven Airport (KHWV) | 2026-09-12 00:20 UTC | 2026-09-12 00:33 UTC | 12m |
| N3SA |  | Wexford County Airport (KCAD) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-09-11 20:29 UTC | 2026-09-12 00:22 UTC | 3h 53m |
| N798KA |  | Boehm's Field (2PA1) | Lehigh Valley International Airport (KABE) | 2026-09-11 23:58 UTC | 2026-09-12 00:22 UTC | 24m |
| N224JA |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-09-11 23:00 UTC | 2026-09-12 00:13 UTC | 1h 12m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-12 00:02 UTC | 2026-09-12 00:13 UTC | 10m |
| N356MH |  | Seward Airport (PAWD) | Seward Airport (PAWD) | 2026-09-11 23:46 UTC | 2026-09-12 00:06 UTC | 20m |
| N950TT |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-09-11 23:45 UTC | 2026-09-12 00:02 UTC | 17m |
| TKR104 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-09-11 23:52 UTC | 2026-09-11 23:59 UTC | 7m |
| LFT05 | LFT | Hamilton International Airport (NZHN) | Whakatane Airport (NZWK) | 2026-09-11 23:35 UTC | 2026-09-11 23:59 UTC | 23m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-09-11 23:40 UTC | 2026-09-11 23:57 UTC | 16m |
| N208W |  | Merrill Field (PAMR) | Tin Creek Airport (PAFL) | 2026-09-11 23:19 UTC | 2026-09-11 23:56 UTC | 36m |
| TKR15 | TKR | Boise Air Trml/Gowen Field (KBOI) | Oasis Airpark (1ID4) | 2026-09-11 23:46 UTC | 2026-09-11 23:54 UTC | 8m |
| SDM6964 | SDM | Istanbul Airport (LTFM) | Bezymyanka Airfield (UWWG) | 2026-09-11 20:29 UTC | 2026-09-11 23:54 UTC | 3h 24m |
| N816CT |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-09-11 22:46 UTC | 2026-09-11 23:47 UTC | 1h 1m |
| SKW3164 | SkyWest Airlines | San Francisco International Airport (KSFO) | Palm Springs International Airport (KPSP) | 2026-09-11 22:48 UTC | 2026-09-11 23:46 UTC | 57m |
| N958AL |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-09-11 23:37 UTC | 2026-09-11 23:45 UTC | 7m |
| TGCCC | TGC | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2026-09-11 23:24 UTC | 2026-09-11 23:45 UTC | 20m |
| DCM4063 | DCM | St Louis Downtown Airport (KCPS) | Mc Elroy Airfield (K20V) | 2026-09-11 21:48 UTC | 2026-09-11 23:43 UTC | 1h 54m |
| LPE2482 | LPE | Jorge Chavez International Airport (SPJC) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-09-11 17:11 UTC | 2026-09-11 23:43 UTC | 6h 31m |
| QLK221D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-09-11 23:03 UTC | 2026-09-11 23:42 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
