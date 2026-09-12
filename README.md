# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_22:19:29_UTC-green)

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

**Latest saved flight:** 2026-09-12 22:19:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-12 22:19:29 UTC

- **256,743** saved flights
- **76,500** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **256,743** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,103,419.2 tonnes** estimated CO2 emissions
- **179,908,357 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10214 |
| 2 | SkyWest Airlines | 8945 |
| 3 | EJA | 4961 |
| 4 | IndiGo | 4301 |
| 5 | American Airlines | 4064 |
| 6 | Southwest Airlines | 3780 |
| 7 | Delta Air Lines | 3215 |
| 8 | ENY | 3046 |
| 9 | LATAM Airlines | 2470 |
| 10 | AZU | 2390 |
| 11 | Vueling | 2172 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2011 |
| 14 | LXJ | 2003 |
| 15 | easyJet | 1756 |
| 16 | Swiss International | 1721 |
| 17 | QLK | 1653 |
| 18 | AXM | 1642 |
| 19 | EJU | 1637 |
| 20 | United Airlines | 1592 |
| 21 | Alaska Airlines | 1525 |
| 22 | All Nippon Airways | 1493 |
| 23 | WMT | 1451 |
| 24 | GLO | 1431 |
| 25 | PGT | 1418 |
| 26 | VIV | 1405 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1397 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213172 |
| 2 | 🇪🇸 ES | 16308 |
| 3 | 🇧🇷 BR | 14978 |
| 4 | 🇦🇺 AU | 14617 |
| 5 | 🇨🇦 CA | 14306 |
| 6 | 🇮🇹 IT | 14029 |
| 7 | 🇮🇳 IN | 13481 |
| 8 | 🇩🇪 DE | 12516 |
| 9 | 🇬🇧 GB | 11983 |
| 10 | 🇨🇴 CO | 11482 |
| 11 | 🇫🇷 FR | 10311 |
| 12 | 🇯🇵 JP | 10017 |
| 13 | 🇹🇷 TR | 7717 |
| 14 | 🇬🇷 GR | 7487 |
| 15 | 🇲🇽 MX | 7086 |
| 16 | 🇨🇭 CH | 6894 |
| 17 | 🇳🇴 NO | 6347 |
| 18 | 🇹🇭 TH | 4613 |
| 19 | 🇲🇾 MY | 4415 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4257 |
| 22 | 🇳🇿 NZ | 3541 |
| 23 | 🇵🇭 PH | 3448 |
| 24 | 🇬🇹 GT | 3257 |
| 25 | 🇭🇷 HR | 2946 |
| 26 | 🇰🇷 KR | 2938 |
| 27 | 🇲🇦 MA | 2585 |
| 28 | 🇲🇪 ME | 2417 |
| 29 | 🇳🇱 NL | 2315 |
| 30 | 🇮🇩 ID | 2178 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5264 |
| 2 | Denver International Airport |  | US | 4154 |
| 3 | Indira Gandhi International Airport |  | IN | 3103 |
| 4 | Tokyo International Airport |  | JP | 2991 |
| 5 | Guaymaral Airport |  | CO | 2760 |
| 6 | Harry Reid International Airport |  | US | 2719 |
| 7 | Zurich Airport |  | CH | 2691 |
| 8 | El Dorado International Airport |  | CO | 2664 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2588 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2509 |
| 11 | La Aurora Airport |  | GT | 2474 |
| 12 | Salt Lake City International Airport |  | US | 2260 |
| 13 | Chicago O'Hare International Airport |  | US | 2235 |
| 14 | Congonhas Airport |  | BR | 2199 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2097 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2004 |
| 18 | Frankfurt am Main International Airport |  | DE | 1983 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1927 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1857 |
| 21 | Malpensa International Airport |  | IT | 1850 |
| 22 | Charles de Gaulle International Airport |  | FR | 1804 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1800 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1780 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1740 |
| 26 | Macau International Airport |  | MO | 1700 |
| 27 | Ninoy Aquino International Airport |  | PH | 1687 |
| 28 | Barcelona International Airport |  | ES | 1616 |
| 29 | Charlotte/Douglas International Airport |  | US | 1608 |
| 30 | Kuala Lumpur International Airport |  | MY | 1588 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1573 |
| 32 | Viracopos International Airport |  | BR | 1533 |
| 33 | Seattle-Tacoma International Airport |  | US | 1504 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1492 |
| 35 | Don Mueang International Airport |  | TH | 1475 |
| 36 | Calgary International Airport |  | CA | 1470 |
| 37 | Bengaluru International Airport |  | IN | 1457 |
| 38 | Oslo Gardermoen Airport |  | NO | 1449 |
| 39 | Vancouver International Airport |  | CA | 1442 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1388 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 957 | 21m | 244 km | 4,029.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 691 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 643 | 1h 6m | 770 km | 8,541.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 640 | 24m | 225 km | 2,482.9 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 412 | 44m | 555 km | 3,945.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 409 | 1h 50m | 1,423 km | 10,037.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 359 | 24m | 218 km | 1,352.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 295 | 1h 14m | 961 km | 4,889.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 295 | 19m | 144 km | 733.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 269 | 41m | 535 km | 2,484.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Macau International Airport (VMMC) | 2026-09-12 11:10 UTC | 2026-09-12 22:19 UTC | 11h 8m |
| N692DA |  | 3WI1 (3WI1) | 3WI1 (3WI1) | 2026-09-12 22:01 UTC | 2026-09-12 22:17 UTC | 15m |
| BOX622 | BOX | Frankfurt am Main International Airport (EDDF) | Ozar Airport (VAOZ) | 2026-09-12 14:26 UTC | 2026-09-12 22:15 UTC | 7h 48m |
| N938BS |  | Charles M Schulz/Sonoma County Airport (KSTS) | Mc Clellan Airfield (KMCC) | 2026-09-12 21:52 UTC | 2026-09-12 22:13 UTC | 20m |
| N3558E |  | KM90 (KM90) | Mineta San Jose International Airport (KSJC) | 2026-09-12 21:25 UTC | 2026-09-12 22:11 UTC | 46m |
| COS4 | COS | Oxnard Airport (KOXR) | Santa Barbara Municipal Airport (KSBA) | 2026-09-12 21:59 UTC | 2026-09-12 22:10 UTC | 11m |
| EZY56ZC | easyJet | London Gatwick Airport (EGKK) | Luqa Airport (LMML) | 2026-09-12 19:30 UTC | 2026-09-12 22:09 UTC | 2h 38m |
| CXK670 | CXK | Hanford Municipal Airport (KHJO) | Riverside Airport (KRAL) | 2026-09-12 20:13 UTC | 2026-09-12 22:08 UTC | 1h 54m |
| N559BM |  | Saskatoon John G. Diefenbaker International Airport (CYXE) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-09-12 21:38 UTC | 2026-09-12 22:07 UTC | 29m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-12 10:53 UTC | 2026-09-12 22:04 UTC | 11h 10m |
| N10EH |  | Coeur D'Alene Airport (KCOE) | Southfork Airport (23ID) | 2026-09-12 21:23 UTC | 2026-09-12 22:02 UTC | 38m |
| UTA731 | UTA | Staroselye Airport (UUBK) | Ukhta Airport (UUYH) | 2026-09-12 08:52 UTC | 2026-09-12 21:59 UTC | 13h 7m |
| SGA2552 | SGA | Sharjah International Airport (OMSJ) | Zhuhai Airport (ZGSD) | 2026-09-12 08:30 UTC | 2026-09-12 21:57 UTC | 13h 26m |
| N224LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | 2026-09-12 20:16 UTC | 2026-09-12 21:56 UTC | 1h 39m |
| N4854G |  | General Mitchell International Airport (KMKE) | Batten International Airport (KRAC) | 2026-09-12 21:43 UTC | 2026-09-12 21:55 UTC | 11m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-12 10:37 UTC | 2026-09-12 21:54 UTC | 11h 17m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-09-12 11:30 UTC | 2026-09-12 21:54 UTC | 10h 24m |
| N916LF |  | Rutland/Southern Vermont Regional Airport (KRUT) | Lebanon Municipal Airport (KLEB) | 2026-09-12 21:39 UTC | 2026-09-12 21:54 UTC | 14m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-12 21:03 UTC | 2026-09-12 21:49 UTC | 45m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-09-12 20:47 UTC | 2026-09-12 21:48 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
