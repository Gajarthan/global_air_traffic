# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_04:41:42_UTC-green)

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

**Latest saved flight:** 2026-09-03 04:41:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 04:41:42 UTC

- **245,515** saved flights
- **74,171** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,515** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,956,573.2 tonnes** estimated CO2 emissions
- **171,395,546 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9845 |
| 2 | SkyWest Airlines | 8596 |
| 3 | EJA | 4736 |
| 4 | IndiGo | 4109 |
| 5 | American Airlines | 3942 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3122 |
| 8 | ENY | 2944 |
| 9 | LATAM Airlines | 2360 |
| 10 | AZU | 2281 |
| 11 | Vueling | 2100 |
| 12 | Lufthansa | 1964 |
| 13 | WIF | 1961 |
| 14 | LXJ | 1898 |
| 15 | easyJet | 1705 |
| 16 | Swiss International | 1654 |
| 17 | AXM | 1614 |
| 18 | EJU | 1580 |
| 19 | QLK | 1577 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1468 |
| 22 | All Nippon Airways | 1447 |
| 23 | WMT | 1383 |
| 24 | GLO | 1370 |
| 25 | VIV | 1346 |
| 26 | PGT | 1345 |
| 27 | Air France | 1342 |
| 28 | Wizz Air | 1329 |
| 29 | JetBlue | 1212 |
| 30 | AEE | 1211 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203470 |
| 2 | 🇪🇸 ES | 15752 |
| 3 | 🇧🇷 BR | 14312 |
| 4 | 🇦🇺 AU | 13980 |
| 5 | 🇨🇦 CA | 13671 |
| 6 | 🇮🇹 IT | 13450 |
| 7 | 🇮🇳 IN | 12809 |
| 8 | 🇩🇪 DE | 12102 |
| 9 | 🇬🇧 GB | 11565 |
| 10 | 🇨🇴 CO | 10657 |
| 11 | 🇫🇷 FR | 9904 |
| 12 | 🇯🇵 JP | 9765 |
| 13 | 🇹🇷 TR | 7299 |
| 14 | 🇬🇷 GR | 7240 |
| 15 | 🇲🇽 MX | 6775 |
| 16 | 🇨🇭 CH | 6593 |
| 17 | 🇳🇴 NO | 6088 |
| 18 | 🇹🇭 TH | 4438 |
| 19 | 🇲🇾 MY | 4325 |
| 20 | 🇿🇦 ZA | 4259 |
| 21 | 🇵🇱 PL | 4118 |
| 22 | 🇳🇿 NZ | 3369 |
| 23 | 🇵🇭 PH | 3359 |
| 24 | 🇬🇹 GT | 3075 |
| 25 | 🇰🇷 KR | 2877 |
| 26 | 🇭🇷 HR | 2825 |
| 27 | 🇲🇦 MA | 2479 |
| 28 | 🇲🇪 ME | 2296 |
| 29 | 🇳🇱 NL | 2220 |
| 30 | 🇮🇩 ID | 2138 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5057 |
| 2 | Denver International Airport |  | US | 3964 |
| 3 | Indira Gandhi International Airport |  | IN | 2991 |
| 4 | Tokyo International Airport |  | JP | 2912 |
| 5 | Guaymaral Airport |  | CO | 2718 |
| 6 | Harry Reid International Airport |  | US | 2614 |
| 7 | Zurich Airport |  | CH | 2577 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2496 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2445 |
| 10 | El Dorado International Airport |  | CO | 2428 |
| 11 | La Aurora Airport |  | GT | 2340 |
| 12 | Salt Lake City International Airport |  | US | 2178 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2100 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2028 |
| 16 | Frankfurt am Main International Airport |  | DE | 1935 |
| 17 | Capua Airport |  | IT | 1929 |
| 18 | Madrid Barajas International Airport |  | ES | 1927 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1844 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1804 |
| 21 | Malpensa International Airport |  | IT | 1757 |
| 22 | Charles de Gaulle International Airport |  | FR | 1727 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1724 |
| 25 | Ninoy Aquino International Airport |  | PH | 1635 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1588 |
| 28 | Charlotte/Douglas International Airport |  | US | 1565 |
| 29 | Kuala Lumpur International Airport |  | MY | 1559 |
| 30 | Barcelona International Airport |  | ES | 1553 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1492 |
| 32 | Viracopos International Airport |  | BR | 1457 |
| 33 | Seattle-Tacoma International Airport |  | US | 1443 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1427 |
| 35 | Don Mueang International Airport |  | TH | 1427 |
| 36 | Bengaluru International Airport |  | IN | 1417 |
| 37 | Calgary International Airport |  | CA | 1415 |
| 38 | Oslo Gardermoen Airport |  | NO | 1383 |
| 39 | Vancouver International Airport |  | CA | 1369 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1341 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 909 | 21m | 244 km | 3,827.5 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 638 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 617 | 1h 6m | 770 km | 8,196.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 551 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 388 | 1h 50m | 1,423 km | 9,522.1 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 348 | 21m | 250 km | 1,503.2 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 338 | 24m | 218 km | 1,273.4 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 328 | 1h 39m | 1,156 km | 6,543.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 328 | 22m | 55 km | 311.8 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 300 | 27m | 215 km | 1,111.1 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 290 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 283 | 1h 14m | 961 km | 4,690.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 278 | 19m | 144 km | 691.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 265 | 1h 50m | 1,304 km | 5,961.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-03 04:27 UTC | 2026-09-03 04:41 UTC | 14m |
| N621FJ |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-03 03:56 UTC | 2026-09-03 04:41 UTC | 44m |
| N113UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-03 03:34 UTC | 2026-09-03 04:36 UTC | 1h 2m |
| A7GAC |  | Doha International Airport (OTBD) | Das Island Airport (OMAS) | 2026-09-03 04:00 UTC | 2026-09-03 04:33 UTC | 33m |
| VAR408 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-09-03 04:21 UTC | 2026-09-03 04:29 UTC | 7m |
| N116UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-03 03:13 UTC | 2026-09-03 04:13 UTC | 1h 0m |
| N108UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-09-03 03:41 UTC | 2026-09-03 04:09 UTC | 28m |
| N119UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-09-03 03:12 UTC | 2026-09-03 04:09 UTC | 57m |
| EJA407 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-09-03 03:25 UTC | 2026-09-03 04:08 UTC | 42m |
| BT12 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-03 04:02 UTC | 2026-09-03 04:03 UTC | 1m |
| N106UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-09-03 03:40 UTC | 2026-09-03 04:03 UTC | 23m |
| SEH2SO | SEH | Eleftherios Venizelos International Airport (LGAV) | Kastoria National Airport (LGKA) | 2026-09-03 03:10 UTC | 2026-09-03 04:02 UTC | 52m |
| OXW | OXW | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-03 03:46 UTC | 2026-09-03 04:01 UTC | 15m |
| N705SG |  | Phoenix Sky Harbor International Airport (KPHX) | 8CL0 (8CL0) | 2026-09-03 03:11 UTC | 2026-09-03 04:01 UTC | 50m |
| ERU50 | ERU | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-09-03 03:33 UTC | 2026-09-03 04:01 UTC | 27m |
| VJQ | VJQ | Mangalore Airport (YMNG) | Melbourne Essendon Airport (YMEN) | 2026-09-03 03:27 UTC | 2026-09-03 03:59 UTC | 32m |
| AAH42 | AAH | Daniel K Inouye International Airport (PHNL) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-09-03 03:27 UTC | 2026-09-03 03:54 UTC | 26m |
| WEN3623 | WEN | Calgary International Airport (CYYC) | Valleyview Airport (CEL5) | 2026-09-03 03:00 UTC | 2026-09-03 03:54 UTC | 53m |
| 1804BL |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-03 02:58 UTC | 2026-09-03 03:51 UTC | 52m |
| AIQ3037 | AIQ | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-09-03 03:03 UTC | 2026-09-03 03:48 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
