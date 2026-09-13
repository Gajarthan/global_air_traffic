# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_17:25:05_UTC-green)

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

**Latest saved flight:** 2026-09-13 17:25:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 17:25:05 UTC

- **257,448** saved flights
- **76,631** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **257,448** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,114,723.0 tonnes** estimated CO2 emissions
- **180,563,654 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10229 |
| 2 | SkyWest Airlines | 8962 |
| 3 | EJA | 4978 |
| 4 | IndiGo | 4322 |
| 5 | American Airlines | 4066 |
| 6 | Southwest Airlines | 3787 |
| 7 | Delta Air Lines | 3221 |
| 8 | ENY | 3050 |
| 9 | LATAM Airlines | 2473 |
| 10 | AZU | 2402 |
| 11 | Vueling | 2180 |
| 12 | WIF | 2065 |
| 13 | Lufthansa | 2015 |
| 14 | LXJ | 2011 |
| 15 | easyJet | 1759 |
| 16 | Swiss International | 1723 |
| 17 | QLK | 1660 |
| 18 | AXM | 1646 |
| 19 | EJU | 1638 |
| 20 | United Airlines | 1594 |
| 21 | Alaska Airlines | 1528 |
| 22 | All Nippon Airways | 1497 |
| 23 | WMT | 1454 |
| 24 | GLO | 1434 |
| 25 | PGT | 1428 |
| 26 | Air France | 1408 |
| 27 | VIV | 1408 |
| 28 | Wizz Air | 1401 |
| 29 | AEE | 1247 |
| 30 | TKR | 1247 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213621 |
| 2 | 🇪🇸 ES | 16353 |
| 3 | 🇧🇷 BR | 15014 |
| 4 | 🇦🇺 AU | 14661 |
| 5 | 🇨🇦 CA | 14338 |
| 6 | 🇮🇹 IT | 14050 |
| 7 | 🇮🇳 IN | 13564 |
| 8 | 🇩🇪 DE | 12547 |
| 9 | 🇬🇧 GB | 12009 |
| 10 | 🇨🇴 CO | 11538 |
| 11 | 🇫🇷 FR | 10354 |
| 12 | 🇯🇵 JP | 10042 |
| 13 | 🇹🇷 TR | 7744 |
| 14 | 🇬🇷 GR | 7506 |
| 15 | 🇲🇽 MX | 7099 |
| 16 | 🇨🇭 CH | 6915 |
| 17 | 🇳🇴 NO | 6366 |
| 18 | 🇹🇭 TH | 4639 |
| 19 | 🇲🇾 MY | 4425 |
| 20 | 🇿🇦 ZA | 4386 |
| 21 | 🇵🇱 PL | 4272 |
| 22 | 🇳🇿 NZ | 3556 |
| 23 | 🇵🇭 PH | 3466 |
| 24 | 🇬🇹 GT | 3258 |
| 25 | 🇭🇷 HR | 2958 |
| 26 | 🇰🇷 KR | 2948 |
| 27 | 🇲🇦 MA | 2587 |
| 28 | 🇲🇪 ME | 2424 |
| 29 | 🇳🇱 NL | 2319 |
| 30 | 🇮🇩 ID | 2185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5272 |
| 2 | Denver International Airport |  | US | 4160 |
| 3 | Indira Gandhi International Airport |  | IN | 3116 |
| 4 | Tokyo International Airport |  | JP | 2997 |
| 5 | Guaymaral Airport |  | CO | 2764 |
| 6 | Harry Reid International Airport |  | US | 2727 |
| 7 | Zurich Airport |  | CH | 2700 |
| 8 | El Dorado International Airport |  | CO | 2681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2598 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2514 |
| 11 | La Aurora Airport |  | GT | 2475 |
| 12 | Salt Lake City International Airport |  | US | 2267 |
| 13 | Chicago O'Hare International Airport |  | US | 2241 |
| 14 | Congonhas Airport |  | BR | 2202 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2101 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2008 |
| 18 | Frankfurt am Main International Airport |  | DE | 1987 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1929 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1859 |
| 21 | Malpensa International Airport |  | IT | 1856 |
| 22 | Charles de Gaulle International Airport |  | FR | 1816 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1809 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1782 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1746 |
| 26 | Macau International Airport |  | MO | 1707 |
| 27 | Ninoy Aquino International Airport |  | PH | 1697 |
| 28 | Barcelona International Airport |  | ES | 1618 |
| 29 | Charlotte/Douglas International Airport |  | US | 1608 |
| 30 | Kuala Lumpur International Airport |  | MY | 1592 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1578 |
| 32 | Viracopos International Airport |  | BR | 1543 |
| 33 | Seattle-Tacoma International Airport |  | US | 1508 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1497 |
| 35 | Don Mueang International Airport |  | TH | 1483 |
| 36 | Calgary International Airport |  | CA | 1473 |
| 37 | Bengaluru International Airport |  | IN | 1462 |
| 38 | Oslo Gardermoen Airport |  | NO | 1453 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1389 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 693 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 644 | 24m | 225 km | 2,498.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 418 | 44m | 555 km | 4,002.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 411 | 1h 50m | 1,423 km | 10,086.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 388 | 44m | 241 km | 1,611.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 361 | 24m | 218 km | 1,360.0 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 319 | 26m | 215 km | 1,181.4 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 307 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 299 | 19m | 144 km | 743.7 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 296 | 1h 14m | 961 km | 4,906.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 273 | 42m | 535 km | 2,521.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EPI235 | EPI | Melbourne Orlando International Airport (KMLB) | Kissimmee Gateway Airport (KISM) | 2026-09-13 16:46 UTC | 2026-09-13 17:25 UTC | 38m |
| QTR8454 | Qatar Airways | Doha International Airport (OTBD) | Zhuhai Airport (ZGSD) | 2026-09-13 05:16 UTC | 2026-09-13 17:24 UTC | 12h 7m |
| N92LC |  | 2KY1 (2KY1) | Stuart Powell Field (KDVK) | 2026-09-13 15:28 UTC | 2026-09-13 17:22 UTC | 1h 54m |
| UAL135 | United Airlines | Zurich Airport (LSZH) | Newark Liberty International Airport (KEWR) | 2026-09-13 08:36 UTC | 2026-09-13 17:19 UTC | 8h 43m |
| BSO5AC | BSO | Sabadell Airport (LELL) | Reus Air Base (LERS) | 2026-09-13 16:35 UTC | 2026-09-13 17:17 UTC | 42m |
| AFR218 | Air France | Charles de Gaulle International Airport (LFPG) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-13 09:14 UTC | 2026-09-13 17:16 UTC | 8h 2m |
| N4100Q |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-09-13 16:57 UTC | 2026-09-13 17:16 UTC | 18m |
| N7675W |  | Conroe/North Houston Regional Airport (KCXO) | Mid-Way Regional Airport (KJWY) | 2026-09-13 16:00 UTC | 2026-09-13 17:14 UTC | 1h 13m |
| N193TH |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-09-13 16:31 UTC | 2026-09-13 17:14 UTC | 43m |
| N69FH |  | KPBI (KPBI) | Southwest Georgia Regional Airport (KABY) | 2026-09-13 16:06 UTC | 2026-09-13 17:08 UTC | 1h 2m |
| IGO5149 | IndiGo | Chennai International Airport (VOMM) | Pune Airport (VAPO) | 2026-09-13 15:48 UTC | 2026-09-13 17:07 UTC | 1h 19m |
| AIC9DK | Air India | Trivandrum International Airport (VOTV) | Pune Airport (VAPO) | 2026-09-13 15:21 UTC | 2026-09-13 17:06 UTC | 1h 44m |
| N1377M |  | Dupage Airport (KDPA) | IS63 (IS63) | 2026-09-13 16:43 UTC | 2026-09-13 17:06 UTC | 22m |
| JST113 | JST | Sydney Kingsford Smith International Airport (YSSY) | Rarotonga International Airport (NCRG) | 2026-09-13 11:58 UTC | 2026-09-13 17:05 UTC | 5h 6m |
| N100LE |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-13 16:43 UTC | 2026-09-13 17:03 UTC | 20m |
| TVP7450 | TVP | Copernicus Wrocław Airport (EPWR) | Kasteli Airport (LGTL) | 2026-09-13 14:46 UTC | 2026-09-13 16:58 UTC | 2h 11m |
| N415SD |  | Hector International Airport (KFAR) | Ankeny Regional Airport (KIKV) | 2026-09-13 16:03 UTC | 2026-09-13 16:57 UTC | 54m |
| N23NW |  | Lubbock Preston Smith International Airport (KLBB) | Chaney San Francisco Ranch Airport (92TE) | 2026-09-13 16:01 UTC | 2026-09-13 16:57 UTC | 55m |
| VIKNG61 | VIK | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Cox-Coyour Memorial Field (59MN) | 2026-09-13 15:58 UTC | 2026-09-13 16:56 UTC | 57m |
| N3989S |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-09-13 16:48 UTC | 2026-09-13 16:55 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
