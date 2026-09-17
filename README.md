# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_06:37:56_UTC-green)

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

**Latest saved flight:** 2026-09-17 06:37:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-17 06:37:56 UTC

- **261,019** saved flights
- **77,338** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **261,019** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,161,778.2 tonnes** estimated CO2 emissions
- **183,291,493 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10335 |
| 2 | SkyWest Airlines | 9091 |
| 3 | EJA | 5059 |
| 4 | IndiGo | 4379 |
| 5 | American Airlines | 4103 |
| 6 | Southwest Airlines | 3837 |
| 7 | Delta Air Lines | 3262 |
| 8 | ENY | 3085 |
| 9 | LATAM Airlines | 2518 |
| 10 | AZU | 2450 |
| 11 | Vueling | 2198 |
| 12 | WIF | 2097 |
| 13 | LXJ | 2039 |
| 14 | Lufthansa | 2025 |
| 15 | easyJet | 1769 |
| 16 | Swiss International | 1733 |
| 17 | QLK | 1687 |
| 18 | AXM | 1650 |
| 19 | EJU | 1647 |
| 20 | United Airlines | 1605 |
| 21 | Alaska Airlines | 1550 |
| 22 | All Nippon Airways | 1515 |
| 23 | WMT | 1470 |
| 24 | GLO | 1455 |
| 25 | PGT | 1455 |
| 26 | Air France | 1431 |
| 27 | VIV | 1429 |
| 28 | Wizz Air | 1417 |
| 29 | TKR | 1274 |
| 30 | AEE | 1261 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 216796 |
| 2 | 🇪🇸 ES | 16496 |
| 3 | 🇧🇷 BR | 15270 |
| 4 | 🇦🇺 AU | 14961 |
| 5 | 🇨🇦 CA | 14547 |
| 6 | 🇮🇹 IT | 14204 |
| 7 | 🇮🇳 IN | 13799 |
| 8 | 🇩🇪 DE | 12646 |
| 9 | 🇬🇧 GB | 12131 |
| 10 | 🇨🇴 CO | 11751 |
| 11 | 🇫🇷 FR | 10450 |
| 12 | 🇯🇵 JP | 10149 |
| 13 | 🇹🇷 TR | 7878 |
| 14 | 🇬🇷 GR | 7575 |
| 15 | 🇲🇽 MX | 7187 |
| 16 | 🇨🇭 CH | 6984 |
| 17 | 🇳🇴 NO | 6434 |
| 18 | 🇹🇭 TH | 4682 |
| 19 | 🇲🇾 MY | 4446 |
| 20 | 🇿🇦 ZA | 4410 |
| 21 | 🇵🇱 PL | 4307 |
| 22 | 🇳🇿 NZ | 3621 |
| 23 | 🇵🇭 PH | 3494 |
| 24 | 🇬🇹 GT | 3330 |
| 25 | 🇭🇷 HR | 2982 |
| 26 | 🇰🇷 KR | 2976 |
| 27 | 🇲🇦 MA | 2610 |
| 28 | 🇲🇪 ME | 2457 |
| 29 | 🇳🇱 NL | 2332 |
| 30 | 🇮🇩 ID | 2205 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5348 |
| 2 | Denver International Airport |  | US | 4220 |
| 3 | Indira Gandhi International Airport |  | IN | 3143 |
| 4 | Tokyo International Airport |  | JP | 3029 |
| 5 | Guaymaral Airport |  | CO | 2774 |
| 6 | Harry Reid International Airport |  | US | 2772 |
| 7 | El Dorado International Airport |  | CO | 2741 |
| 8 | Zurich Airport |  | CH | 2726 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2627 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2535 |
| 11 | La Aurora Airport |  | GT | 2527 |
| 12 | Salt Lake City International Airport |  | US | 2303 |
| 13 | Chicago O'Hare International Airport |  | US | 2260 |
| 14 | Congonhas Airport |  | BR | 2229 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2130 |
| 16 | Capua Airport |  | IT | 2037 |
| 17 | Madrid Barajas International Airport |  | ES | 2019 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1969 |
| 20 | Malpensa International Airport |  | IT | 1879 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1875 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1843 |
| 23 | Charles de Gaulle International Airport |  | FR | 1843 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1795 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1781 |
| 26 | Macau International Airport |  | MO | 1730 |
| 27 | Ninoy Aquino International Airport |  | PH | 1714 |
| 28 | Barcelona International Airport |  | ES | 1629 |
| 29 | Charlotte/Douglas International Airport |  | US | 1627 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1604 |
| 31 | Kuala Lumpur International Airport |  | MY | 1596 |
| 32 | Viracopos International Airport |  | BR | 1581 |
| 33 | Seattle-Tacoma International Airport |  | US | 1530 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1520 |
| 35 | Don Mueang International Airport |  | TH | 1495 |
| 36 | Calgary International Airport |  | CA | 1492 |
| 37 | Bengaluru International Airport |  | IN | 1480 |
| 38 | Oslo Gardermoen Airport |  | NO | 1466 |
| 39 | Vancouver International Airport |  | CA | 1465 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1111 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 974 | 21m | 244 km | 4,101.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 705 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 655 | 1h 6m | 770 km | 8,701.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 653 | 24m | 225 km | 2,533.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 585 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 423 | 44m | 555 km | 4,050.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 421 | 27m | 275 km | 1,994.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 396 | 44m | 241 km | 1,644.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 367 | 24m | 218 km | 1,382.6 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 329 | 1h 6m | 706 km | 4,005.6 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 323 | 26m | 215 km | 1,196.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 317 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 301 | 1h 14m | 961 km | 4,989.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 300 | 19m | 144 km | 746.2 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 282 | 1h 50m | 1,304 km | 6,344.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BHA281 | BHA | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-09-17 06:17 UTC | 2026-09-17 06:37 UTC | 20m |
| TTJ600 | TTJ | M. R. Stefanik Airport (LZIB) | Spisska Nova Glider Airport (LZSV) | 2026-09-17 05:52 UTC | 2026-09-17 06:19 UTC | 27m |
| AIC44K | Air India | Newark Liberty International Airport (KEWR) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-16 15:46 UTC | 2026-09-17 06:14 UTC | 14h 28m |
| N628SR |  | Sacramento International Airport (KSMF) | Truckee-Tahoe Airport (KTRK) | 2026-09-17 05:46 UTC | 2026-09-17 06:08 UTC | 22m |
| IGO17FP | IndiGo | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 2026-09-17 04:53 UTC | 2026-09-17 06:04 UTC | 1h 11m |
| N412CF |  | Brushy Creek Airport (69XS) | Dallas Love Field (KDAL) | 2026-09-17 05:22 UTC | 2026-09-17 05:58 UTC | 35m |
| HL1269 |  | G 530 Airport (RK49) | G 417 Airport (RK34) | 2026-09-17 04:42 UTC | 2026-09-17 05:57 UTC | 1h 15m |
| VPCAL | VPC | Taipei Songshan Airport (RCSS) | Macau International Airport (VMMC) | 2026-09-17 04:41 UTC | 2026-09-17 05:51 UTC | 1h 9m |
| LR455 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-09-17 05:19 UTC | 2026-09-17 05:49 UTC | 30m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-09-17 04:57 UTC | 2026-09-17 05:47 UTC | 49m |
| NGX | NGX | Narembeen Airport (YNRB) | Perth Jandakot Airport (YPJT) | 2026-09-17 05:12 UTC | 2026-09-17 05:47 UTC | 34m |
| QLK491D | QLK | Toowoomba Wellcamp Airport (YBWW) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-17 04:22 UTC | 2026-09-17 05:46 UTC | 1h 24m |
| GNS105 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-09-17 05:16 UTC | 2026-09-17 05:44 UTC | 28m |
| WZZ3BR | Wizz Air | M. R. Stefanik Airport (LZIB) | Pristina International Airport (BKPR) | 2026-09-17 04:38 UTC | 2026-09-17 05:43 UTC | 1h 4m |
| TNU5530 | TNU | Soekarno-Hatta International Airport (WIII) | Tunggul Wulung Airport (WIHL) | 2026-09-17 05:15 UTC | 2026-09-17 05:40 UTC | 25m |
| FIN50C | Finnair | Helsinki Vantaa Airport (EFHK) | Hamburg Airport (EDDH) | 2026-09-17 04:00 UTC | 2026-09-17 05:40 UTC | 1h 39m |
| LMS | LMS | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-17 05:39 UTC | 2026-09-17 05:39 UTC | 0m |
| N26XM |  | San Francisco International Airport (KSFO) | K36U (K36U) | 2026-09-17 03:35 UTC | 2026-09-17 05:39 UTC | 2h 4m |
| IGO7626 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-09-17 05:03 UTC | 2026-09-17 05:37 UTC | 33m |
| WIF5E | WIF | Gol Airport (ENKL) | Oslo Gardermoen Airport (ENGM) | 2026-09-17 04:54 UTC | 2026-09-17 05:36 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
