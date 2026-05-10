# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_03:51:21_UTC-green)

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

**Latest saved flight:** 2026-05-10 03:51:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 03:51:21 UTC

- **76,474** saved flights
- **28,042** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,474** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **946,090.7 tonnes** estimated CO2 emissions
- **54,845,835 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3270 |
| 2 | SkyWest Airlines | 2847 |
| 3 | IndiGo | 1700 |
| 4 | EJA | 1410 |
| 5 | American Airlines | 1201 |
| 6 | Southwest Airlines | 1118 |
| 7 | Lufthansa | 994 |
| 8 | ENY | 961 |
| 9 | Delta Air Lines | 789 |
| 10 | Vueling | 734 |
| 11 | AXM | 715 |
| 12 | LATAM Airlines | 707 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 618 |
| 15 | AZU | 610 |
| 16 | QLK | 583 |
| 17 | Swiss International | 578 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 539 |
| 20 | easyJet | 503 |
| 21 | Cathay Pacific | 494 |
| 22 | AEE | 491 |
| 23 | EJU | 490 |
| 24 | VIV | 458 |
| 25 | Japan Airlines | 445 |
| 26 | Air France | 443 |
| 27 | AXB | 423 |
| 28 | CXK | 391 |
| 29 | AIQ | 379 |
| 30 | MXY | 376 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61861 |
| 2 | 🇪🇸 ES | 5462 |
| 3 | 🇮🇳 IN | 5341 |
| 4 | 🇦🇺 AU | 4978 |
| 5 | 🇩🇪 DE | 4293 |
| 6 | 🇧🇷 BR | 4272 |
| 7 | 🇮🇹 IT | 4181 |
| 8 | 🇯🇵 JP | 3977 |
| 9 | 🇨🇦 CA | 3812 |
| 10 | 🇬🇧 GB | 3273 |
| 11 | 🇫🇷 FR | 3022 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2357 |
| 14 | 🇬🇷 GR | 2244 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2070 |
| 17 | 🇲🇾 MY | 1782 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1382 |
| 20 | 🇹🇷 TR | 1368 |
| 21 | 🇹🇭 TH | 1354 |
| 22 | 🇵🇱 PL | 1273 |
| 23 | 🇵🇭 PH | 1225 |
| 24 | 🇬🇹 GT | 1199 |
| 25 | 🇰🇷 KR | 1194 |
| 26 | 🇲🇦 MA | 903 |
| 27 | 🇲🇴 MO | 898 |
| 28 | 🇲🇪 ME | 809 |
| 29 | 🇳🇱 NL | 797 |
| 30 | 🇭🇷 HR | 655 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1707 |
| 2 | Tokyo International Airport |  | JP | 1336 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1125 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1101 |
| 6 | Frankfurt am Main International Airport |  | DE | 993 |
| 7 | Harry Reid International Airport |  | US | 951 |
| 8 | La Aurora Airport |  | GT | 900 |
| 9 | Zurich Airport |  | CH | 900 |
| 10 | Macau International Airport |  | MO | 898 |
| 11 | Guaymaral Airport |  | CO | 890 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 14 | Chicago O'Hare International Airport |  | US | 751 |
| 15 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 742 |
| 16 | Kuala Lumpur International Airport |  | MY | 716 |
| 17 | Madrid Barajas International Airport |  | ES | 711 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Bengaluru International Airport |  | IN | 663 |
| 20 | Malpensa International Airport |  | IT | 658 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 658 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Charlotte/Douglas International Airport |  | US | 604 |
| 24 | Congonhas Airport |  | BR | 604 |
| 25 | Charles de Gaulle International Airport |  | FR | 594 |
| 26 | Capua Airport |  | IT | 594 |
| 27 | Tenerife Norte Airport |  | ES | 569 |
| 28 | Daniel K Inouye International Airport |  | US | 559 |
| 29 | Ninoy Aquino International Airport |  | PH | 556 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 546 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 517 |
| 33 | Barcelona International Airport |  | ES | 517 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 502 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Don Mueang International Airport |  | TH | 480 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 38 | Amsterdam Airport Schiphol |  | NL | 479 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 274 | 21m | 244 km | 1,153.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 220 | 24m | 225 km | 853.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 213 | 28m | 304 km | 1,116.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 168 | 1h 12m | 770 km | 2,231.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 122 | 31m | 369 km | 776.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 102 | 57m | 493 km | 867.8 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-05-09 16:19 UTC | 2026-05-10 03:51 UTC | 11h 31m |
| AXB1131 | AXB | Bengaluru International Airport (VOBL) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-10 01:50 UTC | 2026-05-10 03:45 UTC | 1h 55m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-05-10 03:07 UTC | 2026-05-10 03:31 UTC | 24m |
| ELY082 | ELY | Suvarnabhumi Airport (VTBS) | Queen Alia International Airport (OJAI) | 2026-05-09 17:12 UTC | 2026-05-10 03:15 UTC | 10h 3m |
| ABB858 | ABB | Brussels Airport (EBBR) | Macau International Airport (VMMC) | 2026-05-09 15:33 UTC | 2026-05-10 03:13 UTC | 11h 40m |
| XSR723 | XSR | Norman Y Mineta San Jose International Airport (KSJC) | Austin-Bergstrom International Airport (KAUS) | 2026-05-10 00:17 UTC | 2026-05-10 03:13 UTC | 2h 55m |
| N9769F |  | Las Cruces International Airport (KLRU) | Deming Municipal Airport (KDMN) | 2026-05-10 02:28 UTC | 2026-05-10 03:10 UTC | 42m |
| TRP1 | TRP | Martin State Airport (KMTN) | Lee Airport (KANP) | 2026-05-10 02:48 UTC | 2026-05-10 03:02 UTC | 13m |
| N653ND |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-05-10 02:15 UTC | 2026-05-10 03:00 UTC | 45m |
| LNI | LNI | Jurien Bay Airport (YJNB) | Jurien Bay Airport (YJNB) | 2026-05-10 02:46 UTC | 2026-05-10 02:57 UTC | 11m |
| N143TJ |  | Bolingbrook's Clow International Airport (K1C5) | 22LL (22LL) | 2026-05-10 02:05 UTC | 2026-05-10 02:57 UTC | 51m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-05-10 02:14 UTC | 2026-05-10 02:51 UTC | 36m |
| TCN621 | TCN | Scottsdale Airport (KSDL) | Cherokee County Regional Airport (KCKP) | 2026-05-10 00:52 UTC | 2026-05-10 02:50 UTC | 1h 58m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-05-10 02:19 UTC | 2026-05-10 02:49 UTC | 30m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-05-10 02:23 UTC | 2026-05-10 02:47 UTC | 23m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-10 01:28 UTC | 2026-05-10 02:46 UTC | 1h 18m |
| HYS474 | HYS | Dublin Airport (EIDW) | Iasi Airport (LRIA) | 2026-05-09 23:47 UTC | 2026-05-10 02:41 UTC | 2h 53m |
| CBY02 | CBY | Don Mueang International Airport (VTBD) | Takhli Airport (VTPI) | 2026-05-10 02:15 UTC | 2026-05-10 02:40 UTC | 25m |
| N781KC |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-05-10 02:17 UTC | 2026-05-10 02:37 UTC | 19m |
| BTK6804 | BTK | Soekarno-Hatta International Airport (WIII) | Bentayan Airport (WIPY) | 2026-05-10 01:55 UTC | 2026-05-10 02:36 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
