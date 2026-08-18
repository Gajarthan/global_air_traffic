# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_09:35:54_UTC-green)

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

**Latest saved flight:** 2026-08-18 09:35:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 09:35:54 UTC

- **211,326** saved flights
- **67,093** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,326** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,540,472.5 tonnes** estimated CO2 emissions
- **147,273,766 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8366 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3603 |
| 5 | American Airlines | 3533 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1913 |
| 11 | Lufthansa | 1771 |
| 12 | Vueling | 1764 |
| 13 | WIF | 1697 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1464 |
| 16 | Swiss International | 1411 |
| 17 | AXM | 1382 |
| 18 | United Airlines | 1341 |
| 19 | QLK | 1319 |
| 20 | Alaska Airlines | 1302 |
| 21 | EJU | 1295 |
| 22 | All Nippon Airways | 1284 |
| 23 | VIV | 1164 |
| 24 | GLO | 1139 |
| 25 | Air France | 1135 |
| 26 | PGT | 1131 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1073 |
| 29 | AEE | 1070 |
| 30 | Wizz Air | 1048 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178877 |
| 2 | 🇪🇸 ES | 13521 |
| 3 | 🇧🇷 BR | 12097 |
| 4 | 🇦🇺 AU | 11944 |
| 5 | 🇨🇦 CA | 11694 |
| 6 | 🇮🇳 IN | 11235 |
| 7 | 🇮🇹 IT | 11058 |
| 8 | 🇩🇪 DE | 10416 |
| 9 | 🇬🇧 GB | 9830 |
| 10 | 🇯🇵 JP | 8760 |
| 11 | 🇨🇴 CO | 8486 |
| 12 | 🇫🇷 FR | 8387 |
| 13 | 🇬🇷 GR | 6194 |
| 14 | 🇹🇷 TR | 6026 |
| 15 | 🇲🇽 MX | 5930 |
| 16 | 🇨🇭 CH | 5602 |
| 17 | 🇳🇴 NO | 5260 |
| 18 | 🇲🇾 MY | 3644 |
| 19 | 🇿🇦 ZA | 3545 |
| 20 | 🇵🇱 PL | 3489 |
| 21 | 🇹🇭 TH | 3402 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2809 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2578 |
| 26 | 🇭🇷 HR | 2276 |
| 27 | 🇲🇦 MA | 2128 |
| 28 | 🇳🇱 NL | 1883 |
| 29 | 🇲🇪 ME | 1805 |
| 30 | 🇮🇩 ID | 1759 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4447 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2628 |
| 4 | Indira Gandhi International Airport |  | IN | 2563 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2373 |
| 7 | Zurich Airport |  | CH | 2199 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2182 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1940 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1725 |
| 17 | Madrid Barajas International Airport |  | ES | 1655 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1592 |
| 21 | Macau International Airport |  | MO | 1550 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1464 |
| 25 | Charles de Gaulle International Airport |  | FR | 1447 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1344 |
| 28 | Ninoy Aquino International Airport |  | PH | 1331 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1295 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1275 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1169 |
| 37 | Vitoria/Foronda Airport |  | ES | 1166 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1142 |
| 40 | Don Mueang International Airport |  | TH | 1127 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 751 | 21m | 244 km | 3,162.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 522 | 1h 7m | 770 km | 6,934.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 492 | 24m | 225 km | 1,908.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 351 | 27m | 275 km | 1,663.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 348 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 310 | 1h 49m | 1,423 km | 7,607.9 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 273 | 21m | 250 km | 1,179.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 256 | 1h 37m | 1,156 km | 5,107.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 249 | 19m | 165 km | 708.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 242 | 19m | 144 km | 602.0 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 241 | 31m | 369 km | 1,534.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| S3BRA |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-18 09:13 UTC | 2026-08-18 09:35 UTC | 22m |
| HBXYZ | HBX | Bad Ragaz Airport (LSZE) | Bad Ragaz Airport (LSZE) | 2026-08-18 09:21 UTC | 2026-08-18 09:32 UTC | 11m |
| CAN31 | CAN | Malpensa International Airport (LIMC) | Calcinate Del Pesce Airport (LILC) | 2026-08-18 09:13 UTC | 2026-08-18 09:26 UTC | 12m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-08-17 22:09 UTC | 2026-08-18 09:18 UTC | 11h 9m |
| UAL20 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | Amsterdam Airport Schiphol (EHAM) | 2026-08-18 00:38 UTC | 2026-08-18 09:17 UTC | 8h 39m |
| DEAPR | DEA | Lubeck Blankensee Airport (EDHL) | Lubeck Blankensee Airport (EDHL) | 2026-08-18 09:00 UTC | 2026-08-18 09:15 UTC | 14m |
| ARCTS02 | ARC | Zerbst Airport (EDUZ) | Zerbst Airport (EDUZ) | 2026-08-18 09:07 UTC | 2026-08-18 09:11 UTC | 3m |
| G72234 |  | Laredo International Airport (KLRD) | Quetzalcoatl International Airport (MMNL) | 2026-08-18 08:25 UTC | 2026-08-18 09:09 UTC | 43m |
| STW283 | STW | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-08-18 06:20 UTC | 2026-08-18 09:04 UTC | 2h 44m |
| UFX61 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-18 08:24 UTC | 2026-08-18 08:59 UTC | 35m |
| VJT768 | VJT | Vienna International Airport (LOWW) | Vienna International Airport (LOWW) | 2026-08-18 08:39 UTC | 2026-08-18 08:58 UTC | 18m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-18 08:40 UTC | 2026-08-18 08:57 UTC | 17m |
| RYR23VD | Ryanair | Dublin Airport (EIDW) | Liverpool John Lennon Airport (EGGP) | 2026-08-18 08:25 UTC | 2026-08-18 08:53 UTC | 28m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Bareilly Air Force Station (VIBY) | 2026-08-18 08:15 UTC | 2026-08-18 08:51 UTC | 36m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-18 08:12 UTC | 2026-08-18 08:50 UTC | 37m |
| DKADV | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-08-18 08:19 UTC | 2026-08-18 08:49 UTC | 30m |
| QTR9950 | Qatar Airways | Doha International Airport (OTBD) | Doha International Airport (OTBD) | 2026-08-18 08:42 UTC | 2026-08-18 08:44 UTC | 2m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-08-18 08:13 UTC | 2026-08-18 08:39 UTC | 25m |
| TVF68FN | TVF | Paris-Orly Airport (LFPO) | Menorca Airport (LEMH) | 2026-08-18 07:11 UTC | 2026-08-18 08:39 UTC | 1h 28m |
| FR139 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-18 08:38 UTC | 2026-08-18 08:38 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
