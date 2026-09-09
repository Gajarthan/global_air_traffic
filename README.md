# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_11:24:05_UTC-green)

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

**Latest saved flight:** 2026-09-09 11:24:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-09 11:24:05 UTC

- **252,383** saved flights
- **75,593** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **252,383** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,041,172.3 tonnes** estimated CO2 emissions
- **176,299,845 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10090 |
| 2 | SkyWest Airlines | 8812 |
| 3 | EJA | 4874 |
| 4 | IndiGo | 4228 |
| 5 | American Airlines | 4025 |
| 6 | Southwest Airlines | 3735 |
| 7 | Delta Air Lines | 3188 |
| 8 | ENY | 3012 |
| 9 | LATAM Airlines | 2428 |
| 10 | AZU | 2346 |
| 11 | Vueling | 2145 |
| 12 | WIF | 2021 |
| 13 | Lufthansa | 1993 |
| 14 | LXJ | 1967 |
| 15 | easyJet | 1730 |
| 16 | Swiss International | 1699 |
| 17 | AXM | 1630 |
| 18 | QLK | 1622 |
| 19 | EJU | 1618 |
| 20 | United Airlines | 1573 |
| 21 | Alaska Airlines | 1505 |
| 22 | All Nippon Airways | 1477 |
| 23 | WMT | 1431 |
| 24 | GLO | 1400 |
| 25 | PGT | 1385 |
| 26 | VIV | 1379 |
| 27 | Air France | 1377 |
| 28 | Wizz Air | 1373 |
| 29 | JetBlue | 1235 |
| 30 | AEE | 1233 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 209386 |
| 2 | 🇪🇸 ES | 16107 |
| 3 | 🇧🇷 BR | 14713 |
| 4 | 🇦🇺 AU | 14381 |
| 5 | 🇨🇦 CA | 14015 |
| 6 | 🇮🇹 IT | 13816 |
| 7 | 🇮🇳 IN | 13212 |
| 8 | 🇩🇪 DE | 12375 |
| 9 | 🇬🇧 GB | 11815 |
| 10 | 🇨🇴 CO | 11137 |
| 11 | 🇫🇷 FR | 10147 |
| 12 | 🇯🇵 JP | 9922 |
| 13 | 🇹🇷 TR | 7547 |
| 14 | 🇬🇷 GR | 7401 |
| 15 | 🇲🇽 MX | 6955 |
| 16 | 🇨🇭 CH | 6811 |
| 17 | 🇳🇴 NO | 6244 |
| 18 | 🇹🇭 TH | 4546 |
| 19 | 🇲🇾 MY | 4385 |
| 20 | 🇿🇦 ZA | 4325 |
| 21 | 🇵🇱 PL | 4205 |
| 22 | 🇳🇿 NZ | 3450 |
| 23 | 🇵🇭 PH | 3423 |
| 24 | 🇬🇹 GT | 3141 |
| 25 | 🇰🇷 KR | 2914 |
| 26 | 🇭🇷 HR | 2899 |
| 27 | 🇲🇦 MA | 2550 |
| 28 | 🇲🇪 ME | 2375 |
| 29 | 🇳🇱 NL | 2276 |
| 30 | 🇮🇩 ID | 2160 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5204 |
| 2 | Denver International Airport |  | US | 4080 |
| 3 | Indira Gandhi International Airport |  | IN | 3065 |
| 4 | Tokyo International Airport |  | JP | 2960 |
| 5 | Guaymaral Airport |  | CO | 2744 |
| 6 | Harry Reid International Airport |  | US | 2680 |
| 7 | Zurich Airport |  | CH | 2648 |
| 8 | El Dorado International Airport |  | CO | 2573 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2556 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2491 |
| 11 | La Aurora Airport |  | GT | 2396 |
| 12 | Salt Lake City International Airport |  | US | 2230 |
| 13 | Chicago O'Hare International Airport |  | US | 2199 |
| 14 | Congonhas Airport |  | BR | 2159 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2074 |
| 16 | Capua Airport |  | IT | 1990 |
| 17 | Madrid Barajas International Airport |  | ES | 1982 |
| 18 | Frankfurt am Main International Airport |  | DE | 1963 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1889 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1835 |
| 21 | Malpensa International Airport |  | IT | 1814 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1772 |
| 23 | Charles de Gaulle International Airport |  | FR | 1771 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1758 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1678 |
| 26 | Ninoy Aquino International Airport |  | PH | 1672 |
| 27 | Macau International Airport |  | MO | 1666 |
| 28 | Charlotte/Douglas International Airport |  | US | 1590 |
| 29 | Barcelona International Airport |  | ES | 1590 |
| 30 | Kuala Lumpur International Airport |  | MY | 1579 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1549 |
| 32 | Viracopos International Airport |  | BR | 1506 |
| 33 | Seattle-Tacoma International Airport |  | US | 1490 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1463 |
| 35 | Don Mueang International Airport |  | TH | 1456 |
| 36 | Calgary International Airport |  | CA | 1453 |
| 37 | Bengaluru International Airport |  | IN | 1439 |
| 38 | Oslo Gardermoen Airport |  | NO | 1422 |
| 39 | Vancouver International Airport |  | CA | 1412 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1364 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 937 | 21m | 244 km | 3,945.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 672 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 634 | 1h 6m | 770 km | 8,422.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 565 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 414 | 27m | 275 km | 1,961.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 402 | 1h 50m | 1,423 km | 9,865.7 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 398 | 44m | 555 km | 3,811.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 376 | 44m | 241 km | 1,561.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 352 | 24m | 218 km | 1,326.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 337 | 23m | 55 km | 320.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 311 | 26m | 215 km | 1,151.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 296 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 273 | 1h 50m | 1,304 km | 6,141.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 262 | 41m | 535 km | 2,419.7 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZZZ | HBZ | Birrfeld Airport (LSZF) | Birrfeld Airport (LSZF) | 2026-09-09 11:04 UTC | 2026-09-09 11:24 UTC | 19m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-09 10:44 UTC | 2026-09-09 11:23 UTC | 38m |
| N288SF |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-09-09 10:58 UTC | 2026-09-09 11:22 UTC | 24m |
| N4325R |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-09-09 11:03 UTC | 2026-09-09 11:16 UTC | 12m |
| SYS35 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-09-09 10:42 UTC | 2026-09-09 11:12 UTC | 30m |
| FIH30 | FIH | Tampere-Pirkkala Airport (EFTP) | Tampere-Pirkkala Airport (EFTP) | 2026-09-09 11:06 UTC | 2026-09-09 11:12 UTC | 5m |
| NIT268 | NIT | Heart Of Georgia Regional Airport (KEZM) | Duke Strip 2 Airport (GE26) | 2026-09-09 10:41 UTC | 2026-09-09 11:05 UTC | 24m |
| YGZ | YGZ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-09 10:36 UTC | 2026-09-09 11:03 UTC | 27m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-09-08 23:22 UTC | 2026-09-09 11:00 UTC | 11h 37m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-09-09 10:38 UTC | 2026-09-09 10:51 UTC | 12m |
| GCJCT | GCJ | Lasham Airport (EGHL) | Popham Airport (EGHP) | 2026-09-09 10:35 UTC | 2026-09-09 10:50 UTC | 15m |
| DBETI | DBE | Bolzano Airport (LIPB) | Linz Airport (LOWL) | 2026-09-09 10:13 UTC | 2026-09-09 10:48 UTC | 35m |
| NAY8WQ | NAY | Lanzarote Airport (GCRR) | Tenerife Norte Airport (GCXO) | 2026-09-09 10:17 UTC | 2026-09-09 10:48 UTC | 31m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-09-09 10:05 UTC | 2026-09-09 10:46 UTC | 40m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-09-09 10:17 UTC | 2026-09-09 10:45 UTC | 27m |
| S5DTG |  | Maribor Airport (LJMB) | Maribor Airport (LJMB) | 2026-09-09 10:36 UTC | 2026-09-09 10:40 UTC | 3m |
| RYR3TY | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Santorini Airport (LGSR) | 2026-09-09 09:02 UTC | 2026-09-09 10:37 UTC | 1h 34m |
| N933SC |  | Grand Prairie Municipal Airport (KGPM) | Mid-Way Regional Airport (KJWY) | 2026-09-09 10:23 UTC | 2026-09-09 10:35 UTC | 12m |
| JAF3NE | JAF | Malaga Airport (LEMG) | Brussels Airport (EBBR) | 2026-09-09 08:06 UTC | 2026-09-09 10:33 UTC | 2h 26m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-09-09 09:55 UTC | 2026-09-09 10:31 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
