# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_22:01:15_UTC-green)

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

**Latest saved flight:** 2026-09-15 22:01:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-15 22:01:15 UTC

- **259,655** saved flights
- **77,073** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **259,655** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,144,753.2 tonnes** estimated CO2 emissions
- **182,304,531 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10287 |
| 2 | SkyWest Airlines | 9053 |
| 3 | EJA | 5040 |
| 4 | IndiGo | 4353 |
| 5 | American Airlines | 4097 |
| 6 | Southwest Airlines | 3819 |
| 7 | Delta Air Lines | 3241 |
| 8 | ENY | 3075 |
| 9 | LATAM Airlines | 2498 |
| 10 | AZU | 2437 |
| 11 | Vueling | 2193 |
| 12 | WIF | 2086 |
| 13 | LXJ | 2032 |
| 14 | Lufthansa | 2022 |
| 15 | easyJet | 1766 |
| 16 | Swiss International | 1731 |
| 17 | QLK | 1675 |
| 18 | AXM | 1649 |
| 19 | EJU | 1643 |
| 20 | United Airlines | 1601 |
| 21 | Alaska Airlines | 1542 |
| 22 | All Nippon Airways | 1503 |
| 23 | WMT | 1465 |
| 24 | GLO | 1447 |
| 25 | PGT | 1446 |
| 26 | VIV | 1424 |
| 27 | Air France | 1419 |
| 28 | Wizz Air | 1413 |
| 29 | TKR | 1256 |
| 30 | AEE | 1254 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 215622 |
| 2 | 🇪🇸 ES | 16440 |
| 3 | 🇧🇷 BR | 15179 |
| 4 | 🇦🇺 AU | 14800 |
| 5 | 🇨🇦 CA | 14458 |
| 6 | 🇮🇹 IT | 14133 |
| 7 | 🇮🇳 IN | 13708 |
| 8 | 🇩🇪 DE | 12606 |
| 9 | 🇬🇧 GB | 12085 |
| 10 | 🇨🇴 CO | 11685 |
| 11 | 🇫🇷 FR | 10418 |
| 12 | 🇯🇵 JP | 10093 |
| 13 | 🇹🇷 TR | 7836 |
| 14 | 🇬🇷 GR | 7548 |
| 15 | 🇲🇽 MX | 7164 |
| 16 | 🇨🇭 CH | 6969 |
| 17 | 🇳🇴 NO | 6412 |
| 18 | 🇹🇭 TH | 4662 |
| 19 | 🇲🇾 MY | 4437 |
| 20 | 🇿🇦 ZA | 4398 |
| 21 | 🇵🇱 PL | 4288 |
| 22 | 🇳🇿 NZ | 3592 |
| 23 | 🇵🇭 PH | 3479 |
| 24 | 🇬🇹 GT | 3311 |
| 25 | 🇭🇷 HR | 2971 |
| 26 | 🇰🇷 KR | 2961 |
| 27 | 🇲🇦 MA | 2605 |
| 28 | 🇲🇪 ME | 2445 |
| 29 | 🇳🇱 NL | 2329 |
| 30 | 🇮🇩 ID | 2198 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5324 |
| 2 | Denver International Airport |  | US | 4207 |
| 3 | Indira Gandhi International Airport |  | IN | 3132 |
| 4 | Tokyo International Airport |  | JP | 3010 |
| 5 | Guaymaral Airport |  | CO | 2769 |
| 6 | Harry Reid International Airport |  | US | 2756 |
| 7 | El Dorado International Airport |  | CO | 2723 |
| 8 | Zurich Airport |  | CH | 2720 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2611 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2528 |
| 11 | La Aurora Airport |  | GT | 2512 |
| 12 | Salt Lake City International Airport |  | US | 2290 |
| 13 | Chicago O'Hare International Airport |  | US | 2252 |
| 14 | Congonhas Airport |  | BR | 2219 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2121 |
| 16 | Capua Airport |  | IT | 2028 |
| 17 | Madrid Barajas International Airport |  | ES | 2017 |
| 18 | Frankfurt am Main International Airport |  | DE | 1994 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1952 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1869 |
| 21 | Malpensa International Airport |  | IT | 1868 |
| 22 | Charles de Gaulle International Airport |  | FR | 1830 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1826 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1789 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1770 |
| 26 | Macau International Airport |  | MO | 1721 |
| 27 | Ninoy Aquino International Airport |  | PH | 1706 |
| 28 | Barcelona International Airport |  | ES | 1625 |
| 29 | Charlotte/Douglas International Airport |  | US | 1623 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1597 |
| 31 | Kuala Lumpur International Airport |  | MY | 1595 |
| 32 | Viracopos International Airport |  | BR | 1571 |
| 33 | Seattle-Tacoma International Airport |  | US | 1523 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1512 |
| 35 | Don Mueang International Airport |  | TH | 1489 |
| 36 | Calgary International Airport |  | CA | 1484 |
| 37 | Bengaluru International Airport |  | IN | 1473 |
| 38 | Oslo Gardermoen Airport |  | NO | 1461 |
| 39 | Vancouver International Airport |  | CA | 1454 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1397 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1110 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 968 | 21m | 244 km | 4,076.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 702 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 649 | 1h 6m | 770 km | 8,621.5 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 647 | 24m | 225 km | 2,510.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 582 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 420 | 27m | 275 km | 1,990.2 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 420 | 44m | 555 km | 4,021.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 412 | 1h 50m | 1,423 km | 10,111.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 394 | 44m | 241 km | 1,636.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 365 | 24m | 218 km | 1,375.1 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 357 | 21m | 250 km | 1,542.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 328 | 19m | 99 km | 561.8 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 326 | 1h 6m | 706 km | 3,969.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 321 | 26m | 215 km | 1,188.8 t |
| 19 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 319 | 12m | - | - |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 315 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 299 | 1h 14m | 961 km | 4,956.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 280 | 1h 50m | 1,304 km | 6,299.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 275 | 42m | 535 km | 2,539.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 275 | 28m | 152 km | 718.7 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N879FZ |  | 17KY (17KY) | 93KY (93KY) | 2026-09-15 21:50 UTC | 2026-09-15 22:01 UTC | 10m |
| N181GP |  | Old Bridge Airport (K3N6) | Atlantic City International Airport (KACY) | 2026-09-15 21:23 UTC | 2026-09-15 21:57 UTC | 34m |
| UAL3916 | United Airlines | London Heathrow Airport (EGLL) | Washington Dulles International Airport (KIAD) | 2026-09-15 14:07 UTC | 2026-09-15 21:51 UTC | 7h 43m |
| N443LF |  | K5S9 (K5S9) | 07OR (07OR) | 2026-09-15 21:22 UTC | 2026-09-15 21:47 UTC | 24m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-09-15 11:12 UTC | 2026-09-15 21:44 UTC | 10h 31m |
| N4883G |  | KL38 (KL38) | LA36 (LA36) | 2026-09-15 21:20 UTC | 2026-09-15 21:42 UTC | 21m |
| VM714 |  | Joint Base Andrews Airport (KADW) | Michael J Smith Field (KMRH) | 2026-09-15 20:54 UTC | 2026-09-15 21:37 UTC | 42m |
| N858CP |  | Laconia Municipal Airport (KLCI) | Lawrence Municipal Airport (KLWM) | 2026-09-15 21:04 UTC | 2026-09-15 21:37 UTC | 32m |
| N509TJ |  | 3NY9 (3NY9) | Fort Erie Airport (CNJ3) | 2026-09-15 21:16 UTC | 2026-09-15 21:36 UTC | 20m |
| TGVAL | TGV | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-09-15 21:11 UTC | 2026-09-15 21:35 UTC | 23m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-15 10:43 UTC | 2026-09-15 21:35 UTC | 10h 51m |
| CGXPO | CGX | Naicam Airport (CJR9) | Naicam Airport (CJR9) | 2026-09-15 20:42 UTC | 2026-09-15 21:31 UTC | 49m |
| EJA872 | EJA | Hayward Executive Airport (KHWD) | Abilene Municipal Airport (KK78) | 2026-09-15 19:05 UTC | 2026-09-15 21:28 UTC | 2h 22m |
| EFY7838 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-09-15 20:58 UTC | 2026-09-15 21:27 UTC | 29m |
| BGST312 | BGS | Corpus Christi Nas (Truax Field) Airport (KNGP) | Vaughn Farm Airport (XS76) | 2026-09-15 20:24 UTC | 2026-09-15 21:26 UTC | 1h 2m |
| N984LH |  | Indianapolis Executive Airport (KTYQ) | Lincoln Airport (KLNK) | 2026-09-15 20:04 UTC | 2026-09-15 21:25 UTC | 1h 21m |
| TKR01 | TKR | Albuquerque International Sunport Airport (KABQ) | Albany Municipal Airport (KT23) | 2026-09-15 19:21 UTC | 2026-09-15 21:24 UTC | 2h 3m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-09-15 17:43 UTC | 2026-09-15 21:24 UTC | 3h 41m |
| N7QD |  | Linden Airport (KLDJ) | Linden Airport (KLDJ) | 2026-09-15 19:09 UTC | 2026-09-15 21:24 UTC | 2h 14m |
| N101WL |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-15 20:29 UTC | 2026-09-15 21:23 UTC | 53m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
