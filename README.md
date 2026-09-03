# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_17:20:32_UTC-green)

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

**Latest saved flight:** 2026-09-03 17:20:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 17:20:32 UTC

- **246,009** saved flights
- **74,283** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **246,009** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,961,262.3 tonnes** estimated CO2 emissions
- **171,667,379 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9864 |
| 2 | SkyWest Airlines | 8601 |
| 3 | EJA | 4742 |
| 4 | IndiGo | 4121 |
| 5 | American Airlines | 3947 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3124 |
| 8 | ENY | 2946 |
| 9 | LATAM Airlines | 2368 |
| 10 | AZU | 2285 |
| 11 | Vueling | 2108 |
| 12 | WIF | 1970 |
| 13 | Lufthansa | 1968 |
| 14 | LXJ | 1904 |
| 15 | easyJet | 1708 |
| 16 | Swiss International | 1658 |
| 17 | AXM | 1616 |
| 18 | EJU | 1586 |
| 19 | QLK | 1577 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1468 |
| 22 | All Nippon Airways | 1448 |
| 23 | WMT | 1385 |
| 24 | GLO | 1372 |
| 25 | PGT | 1349 |
| 26 | VIV | 1348 |
| 27 | Air France | 1346 |
| 28 | Wizz Air | 1334 |
| 29 | AEE | 1213 |
| 30 | JetBlue | 1213 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203785 |
| 2 | 🇪🇸 ES | 15797 |
| 3 | 🇧🇷 BR | 14350 |
| 4 | 🇦🇺 AU | 13989 |
| 5 | 🇨🇦 CA | 13686 |
| 6 | 🇮🇹 IT | 13485 |
| 7 | 🇮🇳 IN | 12848 |
| 8 | 🇩🇪 DE | 12135 |
| 9 | 🇬🇧 GB | 11594 |
| 10 | 🇨🇴 CO | 10684 |
| 11 | 🇫🇷 FR | 9940 |
| 12 | 🇯🇵 JP | 9773 |
| 13 | 🇹🇷 TR | 7310 |
| 14 | 🇬🇷 GR | 7255 |
| 15 | 🇲🇽 MX | 6786 |
| 16 | 🇨🇭 CH | 6629 |
| 17 | 🇳🇴 NO | 6110 |
| 18 | 🇹🇭 TH | 4446 |
| 19 | 🇲🇾 MY | 4329 |
| 20 | 🇿🇦 ZA | 4275 |
| 21 | 🇵🇱 PL | 4128 |
| 22 | 🇳🇿 NZ | 3370 |
| 23 | 🇵🇭 PH | 3364 |
| 24 | 🇬🇹 GT | 3081 |
| 25 | 🇰🇷 KR | 2878 |
| 26 | 🇭🇷 HR | 2832 |
| 27 | 🇲🇦 MA | 2487 |
| 28 | 🇲🇪 ME | 2301 |
| 29 | 🇳🇱 NL | 2227 |
| 30 | 🇮🇩 ID | 2142 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5065 |
| 2 | Denver International Airport |  | US | 3968 |
| 3 | Indira Gandhi International Airport |  | IN | 2999 |
| 4 | Tokyo International Airport |  | JP | 2914 |
| 5 | Guaymaral Airport |  | CO | 2721 |
| 6 | Harry Reid International Airport |  | US | 2617 |
| 7 | Zurich Airport |  | CH | 2585 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2505 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2451 |
| 10 | El Dorado International Airport |  | CO | 2439 |
| 11 | La Aurora Airport |  | GT | 2344 |
| 12 | Salt Lake City International Airport |  | US | 2180 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2103 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2028 |
| 16 | Frankfurt am Main International Airport |  | DE | 1938 |
| 17 | Capua Airport |  | IT | 1937 |
| 18 | Madrid Barajas International Airport |  | ES | 1929 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1851 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1804 |
| 21 | Malpensa International Airport |  | IT | 1764 |
| 22 | Charles de Gaulle International Airport |  | FR | 1732 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1725 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 25 | Ninoy Aquino International Airport |  | PH | 1637 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1593 |
| 28 | Charlotte/Douglas International Airport |  | US | 1566 |
| 29 | Barcelona International Airport |  | ES | 1561 |
| 30 | Kuala Lumpur International Airport |  | MY | 1560 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1496 |
| 32 | Viracopos International Airport |  | BR | 1460 |
| 33 | Seattle-Tacoma International Airport |  | US | 1444 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1428 |
| 35 | Don Mueang International Airport |  | TH | 1428 |
| 36 | Bengaluru International Airport |  | IN | 1423 |
| 37 | Calgary International Airport |  | CA | 1415 |
| 38 | Oslo Gardermoen Airport |  | NO | 1386 |
| 39 | Vancouver International Airport |  | CA | 1371 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1343 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 910 | 21m | 244 km | 3,831.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 640 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 552 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 390 | 1h 50m | 1,423 km | 9,571.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 341 | 24m | 218 km | 1,284.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 330 | 1h 39m | 1,156 km | 6,583.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 329 | 22m | 55 km | 312.7 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 304 | 26m | 215 km | 1,125.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 304 | 19m | 99 km | 520.7 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 290 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 285 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 284 | 1h 14m | 961 km | 4,707.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 279 | 19m | 144 km | 694.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 265 | 1h 50m | 1,304 km | 5,961.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N418PJ |  | 64CN (64CN) | 64CN (64CN) | 2026-09-03 15:20 UTC | 2026-09-03 17:20 UTC | 2h 0m |
| N802E |  | Holland Field (1IL9) | Holland Field (1IL9) | 2026-09-03 15:12 UTC | 2026-09-03 17:17 UTC | 2h 4m |
| 652SP |  | New Century Aircenter Airport (KIXD) | Michael Airport (54KS) | 2026-09-03 16:49 UTC | 2026-09-03 17:13 UTC | 23m |
| ASI1 | ASI | Georgetown Executive Airport (KGTU) | Georgetown Executive Airport (KGTU) | 2026-09-03 16:54 UTC | 2026-09-03 17:09 UTC | 14m |
| N3555L |  | Goering Ranches / Chocheta Estates Airport (50OR) | Prineville Airport (KS39) | 2026-09-03 16:55 UTC | 2026-09-03 17:08 UTC | 13m |
| N586EF |  | Monmouth Executive Airport (KBLM) | Somerset Airport (KSMQ) | 2026-09-03 16:32 UTC | 2026-09-03 17:01 UTC | 29m |
| N313DP |  | Gillespie Field (KSEE) | On The Rocks Airport (1CA6) | 2026-09-03 16:15 UTC | 2026-09-03 17:01 UTC | 45m |
| CAN25 | CAN | Reggio Calabria Airport (LICR) | Reggio Calabria Airport (LICR) | 2026-09-03 14:59 UTC | 2026-09-03 17:00 UTC | 2h 1m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-03 15:50 UTC | 2026-09-03 16:56 UTC | 1h 6m |
| N622TP |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-09-03 16:25 UTC | 2026-09-03 16:54 UTC | 28m |
| N955JA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-09-03 16:09 UTC | 2026-09-03 16:53 UTC | 43m |
| N855CP |  | Erie Municipal Airport (KEIK) | Rocky Mountain Metro Airport (KBJC) | 2026-09-03 16:39 UTC | 2026-09-03 16:51 UTC | 12m |
| N733HH |  | Linden Airport (KLDJ) | Central Jersey Regional Airport (K47N) | 2026-09-03 15:55 UTC | 2026-09-03 16:51 UTC | 55m |
| N23ND |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-09-03 16:10 UTC | 2026-09-03 16:49 UTC | 39m |
| N560FT |  | Santa Fe Regional Airport (KSAF) | Jicarilla Apache Nation Airport (K24N) | 2026-09-03 16:35 UTC | 2026-09-03 16:47 UTC | 12m |
| N233AK |  | Chino Airport (KCNO) | Riverside Airport (KRAL) | 2026-09-03 16:33 UTC | 2026-09-03 16:45 UTC | 12m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-09-03 16:05 UTC | 2026-09-03 16:45 UTC | 39m |
| ROCK11 | ROC | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-09-03 16:33 UTC | 2026-09-03 16:44 UTC | 10m |
| N8611C |  | Auburn Municipal Airport (KAUN) | Auburn Municipal Airport (KAUN) | 2026-09-03 16:31 UTC | 2026-09-03 16:44 UTC | 12m |
| N135RF |  | Modesto City-County-Harry Sham Field (KMOD) | 6CL4 (6CL4) | 2026-09-03 15:25 UTC | 2026-09-03 16:43 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
