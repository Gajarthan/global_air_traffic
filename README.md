# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_19:24:29_UTC-green)

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

**Latest saved flight:** 2026-08-25 19:24:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 19:24:29 UTC

- **236,355** saved flights
- **72,192** unique routes
- **145** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,355** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,846,362.2 tonnes** estimated CO2 emissions
- **165,006,505 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9484 |
| 2 | SkyWest Airlines | 8339 |
| 3 | EJA | 4586 |
| 4 | IndiGo | 3985 |
| 5 | American Airlines | 3839 |
| 6 | Southwest Airlines | 3604 |
| 7 | Delta Air Lines | 3011 |
| 8 | ENY | 2870 |
| 9 | LATAM Airlines | 2268 |
| 10 | AZU | 2203 |
| 11 | Vueling | 2023 |
| 12 | Lufthansa | 1920 |
| 13 | WIF | 1880 |
| 14 | LXJ | 1847 |
| 15 | easyJet | 1652 |
| 16 | Swiss International | 1587 |
| 17 | AXM | 1576 |
| 18 | EJU | 1519 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1492 |
| 21 | Alaska Airlines | 1419 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1320 |
| 24 | GLO | 1316 |
| 25 | VIV | 1306 |
| 26 | PGT | 1288 |
| 27 | Air France | 1284 |
| 28 | Wizz Air | 1264 |
| 29 | AEE | 1175 |
| 30 | JetBlue | 1174 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196335 |
| 2 | 🇪🇸 ES | 15195 |
| 3 | 🇧🇷 BR | 13797 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13069 |
| 6 | 🇮🇹 IT | 12900 |
| 7 | 🇮🇳 IN | 12415 |
| 8 | 🇩🇪 DE | 11657 |
| 9 | 🇬🇧 GB | 11160 |
| 10 | 🇨🇴 CO | 10016 |
| 11 | 🇯🇵 JP | 9546 |
| 12 | 🇫🇷 FR | 9498 |
| 13 | 🇹🇷 TR | 7014 |
| 14 | 🇬🇷 GR | 6969 |
| 15 | 🇲🇽 MX | 6568 |
| 16 | 🇨🇭 CH | 6317 |
| 17 | 🇳🇴 NO | 5860 |
| 18 | 🇲🇾 MY | 4225 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4147 |
| 21 | 🇵🇱 PL | 3941 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2961 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2726 |
| 27 | 🇲🇦 MA | 2393 |
| 28 | 🇲🇪 ME | 2199 |
| 29 | 🇳🇱 NL | 2122 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4907 |
| 2 | Denver International Airport |  | US | 3820 |
| 3 | Indira Gandhi International Airport |  | IN | 2882 |
| 4 | Tokyo International Airport |  | JP | 2843 |
| 5 | Guaymaral Airport |  | CO | 2685 |
| 6 | Harry Reid International Airport |  | US | 2526 |
| 7 | Zurich Airport |  | CH | 2477 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2415 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2368 |
| 10 | La Aurora Airport |  | GT | 2257 |
| 11 | El Dorado International Airport |  | CO | 2244 |
| 12 | Chicago O'Hare International Airport |  | US | 2128 |
| 13 | Salt Lake City International Airport |  | US | 2085 |
| 14 | Congonhas Airport |  | BR | 2013 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1980 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Madrid Barajas International Airport |  | ES | 1858 |
| 18 | Capua Airport |  | IT | 1858 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1776 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1745 |
| 21 | Malpensa International Airport |  | IT | 1694 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1677 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1646 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1524 |
| 29 | Barcelona International Airport |  | ES | 1493 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1475 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1435 |
| 32 | Viracopos International Airport |  | BR | 1411 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1383 |
| 35 | Seattle-Tacoma International Airport |  | US | 1383 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1352 |
| 38 | Oslo Gardermoen Airport |  | NO | 1327 |
| 39 | Vancouver International Airport |  | CA | 1290 |
| 40 | O. R. Tambo International Airport |  | ZA | 1289 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 867 | 21m | 244 km | 3,650.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 598 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 529 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 342 | 44m | 241 km | 1,420.6 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 335 | 21m | 250 km | 1,447.0 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 317 | 24m | 218 km | 1,194.3 t |
| 14 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 313 | 1h 40m | 1,156 km | 6,244.2 t |
| 16 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 311 | 22m | 55 km | 295.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 293 | 19m | 99 km | 501.9 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 274 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 254 | 1h 50m | 1,304 km | 5,714.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N849UM |  | Atizapan De Zaragoza Airport (MMJC) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-08-25 18:39 UTC | 2026-08-25 19:24 UTC | 45m |
| QTR61G | Qatar Airways | Hamad International Airport (OTHH) | Cairo International Airport (HECA) | 2026-08-25 16:49 UTC | 2026-08-25 19:23 UTC | 2h 34m |
| LS16 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-25 17:42 UTC | 2026-08-25 19:21 UTC | 1h 39m |
| N80389 |  | Joliet Regional Airport (KJOT) | 2LL1 (2LL1) | 2026-08-25 18:48 UTC | 2026-08-25 19:15 UTC | 27m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-25 17:32 UTC | 2026-08-25 19:14 UTC | 1h 42m |
| N2608J |  | Jim Benson Field (WI16) | Dane County Regional/Truax Field (KMSN) | 2026-08-25 18:45 UTC | 2026-08-25 19:14 UTC | 28m |
| N4381L |  | Trenton-Robbinsville Airport (KN87) | Trenton-Robbinsville Airport (KN87) | 2026-08-25 18:47 UTC | 2026-08-25 19:12 UTC | 24m |
| IPBOE | IPB | Bolzano Airport (LIPB) | Trento / Mattarello Airport (LIDT) | 2026-08-25 19:01 UTC | 2026-08-25 19:08 UTC | 7m |
| N739WR |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-25 18:52 UTC | 2026-08-25 19:07 UTC | 15m |
| N916GW |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-25 18:32 UTC | 2026-08-25 19:04 UTC | 32m |
| N381Z |  | Chickasha Municipal Airport (KCHK) | KF29 (KF29) | 2026-08-25 18:23 UTC | 2026-08-25 19:04 UTC | 40m |
| N363K |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-25 18:34 UTC | 2026-08-25 19:00 UTC | 25m |
| GH11 |  | North Island Nas (Halsey Field) Airport (KNZY) | Catalina Airport (KAVX) | 2026-08-25 18:11 UTC | 2026-08-25 18:59 UTC | 48m |
| 021464 |  | Redding Regional Airport (KRDD) | OR26 (OR26) | 2026-08-25 18:05 UTC | 2026-08-25 18:58 UTC | 53m |
| N3641R |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-08-25 17:49 UTC | 2026-08-25 18:57 UTC | 1h 7m |
| N824PF |  | Northeast Philadelphia Airport (KPNE) | Central Jersey Regional Airport (K47N) | 2026-08-25 18:22 UTC | 2026-08-25 18:51 UTC | 28m |
| N235U |  | Dallas Love Field (KDAL) | Dekalb-Peachtree Airport (KPDK) | 2026-08-25 17:11 UTC | 2026-08-25 18:50 UTC | 1h 39m |
| N874EB |  | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-08-25 17:19 UTC | 2026-08-25 18:50 UTC | 1h 31m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-25 18:04 UTC | 2026-08-25 18:50 UTC | 46m |
| N315EF |  | Hammond Northshore Regional Airport (KHDC) | Stennis International Airport (KHSA) | 2026-08-25 18:15 UTC | 2026-08-25 18:48 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
