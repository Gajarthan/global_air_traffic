# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_00:13:11_UTC-green)

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

**Latest saved flight:** 2026-09-16 00:13:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-16 00:13:11 UTC

- **259,833** saved flights
- **77,107** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,833** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,147,238.0 tonnes** estimated CO2 emissions
- **182,448,579 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10287 |
| 2 | SkyWest Airlines | 9065 |
| 3 | EJA | 5044 |
| 4 | IndiGo | 4353 |
| 5 | American Airlines | 4097 |
| 6 | Southwest Airlines | 3822 |
| 7 | Delta Air Lines | 3248 |
| 8 | ENY | 3076 |
| 9 | LATAM Airlines | 2501 |
| 10 | AZU | 2439 |
| 11 | Vueling | 2193 |
| 12 | WIF | 2086 |
| 13 | LXJ | 2034 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1766 |
| 16 | Swiss International | 1731 |
| 17 | QLK | 1679 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1601 |
| 21 | Alaska Airlines | 1542 |
| 22 | All Nippon Airways | 1506 |
| 23 | WMT | 1465 |
| 24 | GLO | 1449 |
| 25 | PGT | 1447 |
| 26 | VIV | 1426 |
| 27 | Air France | 1419 |
| 28 | Wizz Air | 1413 |
| 29 | TKR | 1260 |
| 30 | AEE | 1254 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215818 |
| 2 | 🇪🇸 ES | 16440 |
| 3 | 🇧🇷 BR | 15193 |
| 4 | 🇦🇺 AU | 14839 |
| 5 | 🇨🇦 CA | 14471 |
| 6 | 🇮🇹 IT | 14133 |
| 7 | 🇮🇳 IN | 13714 |
| 8 | 🇩🇪 DE | 12609 |
| 9 | 🇬🇧 GB | 12085 |
| 10 | 🇨🇴 CO | 11694 |
| 11 | 🇫🇷 FR | 10418 |
| 12 | 🇯🇵 JP | 10101 |
| 13 | 🇹🇷 TR | 7840 |
| 14 | 🇬🇷 GR | 7548 |
| 15 | 🇲🇽 MX | 7169 |
| 16 | 🇨🇭 CH | 6969 |
| 17 | 🇳🇴 NO | 6412 |
| 18 | 🇹🇭 TH | 4662 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4288 |
| 22 | 🇳🇿 NZ | 3601 |
| 23 | 🇵🇭 PH | 3481 |
| 24 | 🇬🇹 GT | 3317 |
| 25 | 🇭🇷 HR | 2971 |
| 26 | 🇰🇷 KR | 2963 |
| 27 | 🇲🇦 MA | 2605 |
| 28 | 🇲🇪 ME | 2445 |
| 29 | 🇳🇱 NL | 2329 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5326 |
| 2 | Denver International Airport |  | US | 4211 |
| 3 | Indira Gandhi International Airport |  | IN | 3132 |
| 4 | Tokyo International Airport |  | JP | 3014 |
| 5 | Guaymaral Airport |  | CO | 2769 |
| 6 | Harry Reid International Airport |  | US | 2760 |
| 7 | El Dorado International Airport |  | CO | 2727 |
| 8 | Zurich Airport |  | CH | 2720 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2613 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2528 |
| 11 | La Aurora Airport |  | GT | 2516 |
| 12 | Salt Lake City International Airport |  | US | 2295 |
| 13 | Chicago O'Hare International Airport |  | US | 2253 |
| 14 | Congonhas Airport |  | BR | 2223 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2126 |
| 16 | Capua Airport |  | IT | 2028 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1996 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1954 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1870 |
| 21 | Malpensa International Airport |  | IT | 1868 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1831 |
| 23 | Charles de Gaulle International Airport |  | FR | 1830 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1790 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1770 |
| 26 | Macau International Airport |  | MO | 1722 |
| 27 | Ninoy Aquino International Airport |  | PH | 1708 |
| 28 | Barcelona International Airport |  | ES | 1625 |
| 29 | Charlotte/Douglas International Airport |  | US | 1624 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1599 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1571 |
| 33 | Seattle-Tacoma International Airport |  | US | 1526 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1512 |
| 35 | Don Mueang International Airport |  | TH | 1489 |
| 36 | Calgary International Airport |  | CA | 1486 |
| 37 | Bengaluru International Airport |  | IN | 1474 |
| 38 | Oslo Gardermoen Airport |  | NO | 1461 |
| 39 | Vancouver International Airport |  | CA | 1456 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1397 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 968 | 21m | 244 km | 4,076.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 702 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 649 | 1h 6m | 770 km | 8,621.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 583 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 420 | 44m | 555 km | 4,021.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 394 | 44m | 241 km | 1,636.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 330 | 19m | 99 km | 565.3 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 323 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 315 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 299 | 1h 14m | 961 km | 4,956.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 281 | 1h 50m | 1,304 km | 6,321.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 275 | 28m | 152 km | 718.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N95HF |  | Lincoln Regional/Karl Harder Field (KLHM) | Yuba County Airport (KMYV) | 2026-09-15 23:09 UTC | 2026-09-16 00:13 UTC | 1h 3m |
| N17598 |  | 1WA9 (1WA9) | Boeing Field/King County International Airport (KBFI) | 2026-09-15 23:32 UTC | 2026-09-16 00:11 UTC | 38m |
| N40057 |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-09-15 23:24 UTC | 2026-09-16 00:09 UTC | 44m |
| N9131K |  | Capital City Airport (KCXY) | Chester County G O Carlson Airport (KMQS) | 2026-09-15 23:27 UTC | 2026-09-16 00:08 UTC | 40m |
| N707JG |  | Lawrence Municipal Airport (KLWM) | ME66 (ME66) | 2026-09-15 23:37 UTC | 2026-09-16 00:05 UTC | 28m |
| BOMR837 | BOM | Gritz Field (XS46) | Gritz Field (XS46) | 2026-09-15 23:37 UTC | 2026-09-16 00:05 UTC | 27m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-15 23:51 UTC | 2026-09-16 00:03 UTC | 11m |
| N6EE |  | Coeur D'Alene Airport (KCOE) | Coeur D'Alene Airport (KCOE) | 2026-09-15 23:42 UTC | 2026-09-15 23:58 UTC | 16m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-15 23:38 UTC | 2026-09-15 23:55 UTC | 17m |
| N47AM |  | City Of Colorado Springs Municipal Airport (KCOS) | High Plains Airport Airport (CD15) | 2026-09-15 23:29 UTC | 2026-09-15 23:54 UTC | 25m |
| N40NW |  | Hollywood Burbank Airport (KBUR) | Dry Pen Airport (16CO) | 2026-09-15 22:37 UTC | 2026-09-15 23:51 UTC | 1h 14m |
| LT612 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-15 22:30 UTC | 2026-09-15 23:50 UTC | 1h 20m |
| N403AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-09-15 23:20 UTC | 2026-09-15 23:48 UTC | 28m |
| ALDN62 | ALD | Sale Airport (YSLT) | Yarram Airport (YYRM) | 2026-09-15 23:29 UTC | 2026-09-15 23:46 UTC | 17m |
| N14HX |  | Monterey Regional Airport (KMRY) | 3CA9 (3CA9) | 2026-09-15 23:19 UTC | 2026-09-15 23:46 UTC | 27m |
| N298PC |  | Redding Regional Airport (KRDD) | Portland-Hillsboro Airport (KHIO) | 2026-09-15 22:48 UTC | 2026-09-15 23:45 UTC | 56m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-09-15 22:40 UTC | 2026-09-15 23:38 UTC | 57m |
| N987TT |  | 63TE (63TE) | Austin-Bergstrom International Airport (KAUS) | 2026-09-15 22:36 UTC | 2026-09-15 23:38 UTC | 1h 1m |
| SJN5 | SJN | Friday Harbor Airport (KFHR) | 61WA (61WA) | 2026-09-15 23:31 UTC | 2026-09-15 23:34 UTC | 3m |
| EJA443 | EJA | San Diego International Airport (KSAN) | Joe Foss Field (KFSD) | 2026-09-15 20:56 UTC | 2026-09-15 23:34 UTC | 2h 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
