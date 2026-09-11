# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_00:40:28_UTC-green)

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

**Latest saved flight:** 2026-09-11 00:40:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-11 00:40:28 UTC

- **254,496** saved flights
- **76,052** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **254,496** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,070,372.5 tonnes** estimated CO2 emissions
- **177,992,608 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10154 |
| 2 | SkyWest Airlines | 8881 |
| 3 | EJA | 4919 |
| 4 | IndiGo | 4255 |
| 5 | American Airlines | 4040 |
| 6 | Southwest Airlines | 3754 |
| 7 | Delta Air Lines | 3198 |
| 8 | ENY | 3032 |
| 9 | LATAM Airlines | 2453 |
| 10 | AZU | 2370 |
| 11 | Vueling | 2163 |
| 12 | WIF | 2037 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1991 |
| 15 | easyJet | 1738 |
| 16 | Swiss International | 1705 |
| 17 | QLK | 1643 |
| 18 | AXM | 1633 |
| 19 | EJU | 1628 |
| 20 | United Airlines | 1583 |
| 21 | Alaska Airlines | 1514 |
| 22 | All Nippon Airways | 1485 |
| 23 | WMT | 1438 |
| 24 | GLO | 1418 |
| 25 | PGT | 1396 |
| 26 | VIV | 1391 |
| 27 | Wizz Air | 1384 |
| 28 | Air France | 1383 |
| 29 | JetBlue | 1239 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 211381 |
| 2 | 🇪🇸 ES | 16210 |
| 3 | 🇧🇷 BR | 14863 |
| 4 | 🇦🇺 AU | 14513 |
| 5 | 🇨🇦 CA | 14164 |
| 6 | 🇮🇹 IT | 13921 |
| 7 | 🇮🇳 IN | 13328 |
| 8 | 🇩🇪 DE | 12435 |
| 9 | 🇬🇧 GB | 11886 |
| 10 | 🇨🇴 CO | 11286 |
| 11 | 🇫🇷 FR | 10217 |
| 12 | 🇯🇵 JP | 9961 |
| 13 | 🇹🇷 TR | 7615 |
| 14 | 🇬🇷 GR | 7433 |
| 15 | 🇲🇽 MX | 7016 |
| 16 | 🇨🇭 CH | 6830 |
| 17 | 🇳🇴 NO | 6304 |
| 18 | 🇹🇭 TH | 4564 |
| 19 | 🇲🇾 MY | 4396 |
| 20 | 🇿🇦 ZA | 4339 |
| 21 | 🇵🇱 PL | 4223 |
| 22 | 🇳🇿 NZ | 3505 |
| 23 | 🇵🇭 PH | 3435 |
| 24 | 🇬🇹 GT | 3164 |
| 25 | 🇰🇷 KR | 2926 |
| 26 | 🇭🇷 HR | 2915 |
| 27 | 🇲🇦 MA | 2567 |
| 28 | 🇲🇪 ME | 2392 |
| 29 | 🇳🇱 NL | 2287 |
| 30 | 🇮🇩 ID | 2171 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5231 |
| 2 | Denver International Airport |  | US | 4115 |
| 3 | Indira Gandhi International Airport |  | IN | 3081 |
| 4 | Tokyo International Airport |  | JP | 2973 |
| 5 | Guaymaral Airport |  | CO | 2755 |
| 6 | Harry Reid International Airport |  | US | 2699 |
| 7 | Zurich Airport |  | CH | 2660 |
| 8 | El Dorado International Airport |  | CO | 2611 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2574 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2497 |
| 11 | La Aurora Airport |  | GT | 2413 |
| 12 | Salt Lake City International Airport |  | US | 2246 |
| 13 | Chicago O'Hare International Airport |  | US | 2219 |
| 14 | Congonhas Airport |  | BR | 2183 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2082 |
| 16 | Capua Airport |  | IT | 2006 |
| 17 | Madrid Barajas International Airport |  | ES | 1990 |
| 18 | Frankfurt am Main International Airport |  | DE | 1967 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1909 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1845 |
| 21 | Malpensa International Airport |  | IT | 1827 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1788 |
| 23 | Charles de Gaulle International Airport |  | FR | 1783 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1770 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1704 |
| 26 | Macau International Airport |  | MO | 1680 |
| 27 | Ninoy Aquino International Airport |  | PH | 1679 |
| 28 | Barcelona International Airport |  | ES | 1603 |
| 29 | Charlotte/Douglas International Airport |  | US | 1600 |
| 30 | Kuala Lumpur International Airport |  | MY | 1584 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1562 |
| 32 | Viracopos International Airport |  | BR | 1522 |
| 33 | Seattle-Tacoma International Airport |  | US | 1496 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1481 |
| 35 | Calgary International Airport |  | CA | 1466 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1448 |
| 38 | Oslo Gardermoen Airport |  | NO | 1437 |
| 39 | Vancouver International Airport |  | CA | 1427 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1372 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1108 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 945 | 21m | 244 km | 3,979.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 679 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 638 | 1h 6m | 770 km | 8,475.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 569 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 416 | 27m | 275 km | 1,971.2 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 404 | 1h 50m | 1,423 km | 9,914.8 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 402 | 44m | 555 km | 3,849.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 383 | 44m | 241 km | 1,590.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 373 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 354 | 24m | 218 km | 1,333.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 354 | 21m | 250 km | 1,529.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 339 | 23m | 55 km | 322.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 309 | 19m | 99 km | 529.3 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 307 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 297 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 292 | 1h 14m | 961 km | 4,840.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 290 | 19m | 144 km | 721.4 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 264 | 41m | 535 km | 2,438.2 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZES | ZES | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-11 00:06 UTC | 2026-09-11 00:40 UTC | 34m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-09-10 13:55 UTC | 2026-09-11 00:35 UTC | 10h 39m |
| N856FG |  | Williamsport Regional Airport (KIPT) | Lancaster Airport (KLNS) | 2026-09-10 23:42 UTC | 2026-09-11 00:32 UTC | 50m |
| MPH9441 | MPH | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-09-10 13:23 UTC | 2026-09-11 00:32 UTC | 11h 9m |
| QTR8434 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-09-10 16:53 UTC | 2026-09-11 00:31 UTC | 7h 37m |
| SND4 | SND | Corowa Airport (YCOR) | Corowa Airport (YCOR) | 2026-09-11 00:10 UTC | 2026-09-11 00:29 UTC | 18m |
| UAL941 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-09-10 16:24 UTC | 2026-09-11 00:27 UTC | 8h 2m |
| N203DH |  | Merle K (Mudhole) Smith Airport (PACV) | Merle K (Mudhole) Smith Airport (PACV) | 2026-09-11 00:12 UTC | 2026-09-11 00:26 UTC | 13m |
| N405B |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-09-11 00:01 UTC | 2026-09-11 00:26 UTC | 24m |
| N215DA |  | Napa County Airport (KAPC) | Cecil Ranch Airport (37CN) | 2026-09-11 00:00 UTC | 2026-09-11 00:24 UTC | 24m |
| 00000000 |  | General Downing - Peoria International Airport (KPIA) | Westchester County Airport (KHPN) | 2026-09-10 22:30 UTC | 2026-09-11 00:21 UTC | 1h 51m |
| N12VU |  | Ocala International-Jim Taylor Field (KOCF) | Cherokee County Regional Airport (KCKP) | 2026-09-10 21:46 UTC | 2026-09-11 00:19 UTC | 2h 33m |
| UPS5012 | UPS | Ontario International Airport (KONT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-09-10 19:51 UTC | 2026-09-11 00:19 UTC | 4h 27m |
| AE930 |  | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-09-10 23:58 UTC | 2026-09-11 00:16 UTC | 18m |
| SIL1403 | SIL | Ted Stevens Anchorage International Airport (PANC) | Homer Airport (PAHO) | 2026-09-10 23:46 UTC | 2026-09-11 00:16 UTC | 30m |
| JOLLY11 | JOL | 8NJ0 (8NJ0) | Warren Grove Range Airport (NJ24) | 2026-09-10 23:45 UTC | 2026-09-11 00:15 UTC | 29m |
| N714F |  | Dupage Airport (KDPA) | Logan-Cache Airport (KLGU) | 2026-09-10 21:32 UTC | 2026-09-11 00:14 UTC | 2h 42m |
| ZKTTL | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-09-10 23:57 UTC | 2026-09-11 00:09 UTC | 12m |
| RPC8521 | RPC | Plaridel Airport (RPUX) | Plaridel Airport (RPUX) | 2026-09-11 00:04 UTC | 2026-09-11 00:08 UTC | 4m |
| N781LA |  | Northeast Philadelphia Airport (KPNE) | Lancaster Airport (KLNS) | 2026-09-10 23:21 UTC | 2026-09-11 00:06 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
