# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_05:38:19_UTC-green)

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

**Latest saved flight:** 2026-09-08 05:38:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-08 05:38:19 UTC

- **251,256** saved flights
- **75,370** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **251,256** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,025,321.0 tonnes** estimated CO2 emissions
- **175,380,925 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10051 |
| 2 | SkyWest Airlines | 8786 |
| 3 | EJA | 4857 |
| 4 | IndiGo | 4204 |
| 5 | American Airlines | 4018 |
| 6 | Southwest Airlines | 3723 |
| 7 | Delta Air Lines | 3182 |
| 8 | ENY | 3001 |
| 9 | LATAM Airlines | 2419 |
| 10 | AZU | 2334 |
| 11 | Vueling | 2142 |
| 12 | WIF | 2013 |
| 13 | Lufthansa | 1987 |
| 14 | LXJ | 1962 |
| 15 | easyJet | 1728 |
| 16 | Swiss International | 1686 |
| 17 | AXM | 1629 |
| 18 | QLK | 1618 |
| 19 | EJU | 1613 |
| 20 | United Airlines | 1571 |
| 21 | Alaska Airlines | 1501 |
| 22 | All Nippon Airways | 1472 |
| 23 | WMT | 1424 |
| 24 | GLO | 1395 |
| 25 | PGT | 1380 |
| 26 | VIV | 1376 |
| 27 | Air France | 1366 |
| 28 | Wizz Air | 1366 |
| 29 | AEE | 1230 |
| 30 | JetBlue | 1230 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 208442 |
| 2 | 🇪🇸 ES | 16053 |
| 3 | 🇧🇷 BR | 14641 |
| 4 | 🇦🇺 AU | 14305 |
| 5 | 🇨🇦 CA | 13942 |
| 6 | 🇮🇹 IT | 13757 |
| 7 | 🇮🇳 IN | 13123 |
| 8 | 🇩🇪 DE | 12332 |
| 9 | 🇬🇧 GB | 11773 |
| 10 | 🇨🇴 CO | 11064 |
| 11 | 🇫🇷 FR | 10106 |
| 12 | 🇯🇵 JP | 9896 |
| 13 | 🇹🇷 TR | 7508 |
| 14 | 🇬🇷 GR | 7382 |
| 15 | 🇲🇽 MX | 6941 |
| 16 | 🇨🇭 CH | 6764 |
| 17 | 🇳🇴 NO | 6221 |
| 18 | 🇹🇭 TH | 4526 |
| 19 | 🇲🇾 MY | 4375 |
| 20 | 🇿🇦 ZA | 4315 |
| 21 | 🇵🇱 PL | 4192 |
| 22 | 🇳🇿 NZ | 3432 |
| 23 | 🇵🇭 PH | 3409 |
| 24 | 🇬🇹 GT | 3137 |
| 25 | 🇰🇷 KR | 2905 |
| 26 | 🇭🇷 HR | 2885 |
| 27 | 🇲🇦 MA | 2537 |
| 28 | 🇲🇪 ME | 2363 |
| 29 | 🇳🇱 NL | 2267 |
| 30 | 🇮🇩 ID | 2149 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5189 |
| 2 | Denver International Airport |  | US | 4073 |
| 3 | Indira Gandhi International Airport |  | IN | 3054 |
| 4 | Tokyo International Airport |  | JP | 2953 |
| 5 | Guaymaral Airport |  | CO | 2740 |
| 6 | Harry Reid International Airport |  | US | 2672 |
| 7 | Zurich Airport |  | CH | 2628 |
| 8 | El Dorado International Airport |  | CO | 2552 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2550 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2485 |
| 11 | La Aurora Airport |  | GT | 2392 |
| 12 | Salt Lake City International Airport |  | US | 2225 |
| 13 | Chicago O'Hare International Airport |  | US | 2191 |
| 14 | Congonhas Airport |  | BR | 2150 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2070 |
| 16 | Capua Airport |  | IT | 1982 |
| 17 | Madrid Barajas International Airport |  | ES | 1976 |
| 18 | Frankfurt am Main International Airport |  | DE | 1957 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1882 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1829 |
| 21 | Malpensa International Airport |  | IT | 1805 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1768 |
| 23 | Charles de Gaulle International Airport |  | FR | 1757 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1748 |
| 25 | Ninoy Aquino International Airport |  | PH | 1664 |
| 26 | Enrique Olaya Herrera Airport |  | CO | 1660 |
| 27 | Macau International Airport |  | MO | 1651 |
| 28 | Barcelona International Airport |  | ES | 1587 |
| 29 | Charlotte/Douglas International Airport |  | US | 1586 |
| 30 | Kuala Lumpur International Airport |  | MY | 1575 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1540 |
| 32 | Viracopos International Airport |  | BR | 1500 |
| 33 | Seattle-Tacoma International Airport |  | US | 1484 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1459 |
| 35 | Don Mueang International Airport |  | TH | 1451 |
| 36 | Calgary International Airport |  | CA | 1445 |
| 37 | Bengaluru International Airport |  | IN | 1435 |
| 38 | Oslo Gardermoen Airport |  | NO | 1414 |
| 39 | Vancouver International Airport |  | CA | 1402 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1361 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 933 | 21m | 244 km | 3,928.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 665 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 635 | 24m | 225 km | 2,463.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 630 | 1h 6m | 770 km | 8,369.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 564 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 412 | 27m | 275 km | 1,952.3 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 401 | 1h 50m | 1,423 km | 9,841.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 394 | 44m | 555 km | 3,772.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 374 | 44m | 241 km | 1,553.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 371 | 35m | - | - |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 352 | 21m | 250 km | 1,520.4 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 350 | 24m | 218 km | 1,318.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 335 | 23m | 55 km | 318.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 310 | 26m | 215 km | 1,148.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 305 | 19m | 99 km | 522.4 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 300 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 292 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 289 | 1h 14m | 961 km | 4,790.3 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 272 | 1h 50m | 1,304 km | 6,119.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 27 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 259 | 41m | 535 km | 2,392.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 257 | 28m | 152 km | 671.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC130 | Air India | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 20:34 UTC | 2026-09-08 05:38 UTC | 9h 3m |
| ZFH | ZFH | Bacchus Marsh Airport (YBSS) | Melbourne Essendon Airport (YMEN) | 2026-09-08 05:14 UTC | 2026-09-08 05:36 UTC | 22m |
| ERE | ERE | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-09-08 05:01 UTC | 2026-09-08 05:28 UTC | 26m |
| ETD1CB | Etihad Airways | Abu Dhabi International Airport (OMAA) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 02:46 UTC | 2026-09-08 05:20 UTC | 2h 34m |
| CUM | CUM | Melbourne Moorabbin Airport (YMMB) | Tooradin Airport (YTDN) | 2026-09-08 04:59 UTC | 2026-09-08 05:14 UTC | 15m |
| LAE2547 | LAE | Fort Lauderdale/Hollywood International Airport (KFLL) | El Dorado International Airport (SKBO) | 2026-09-08 01:55 UTC | 2026-09-08 05:09 UTC | 3h 14m |
| RYR4QJ | Ryanair | Paris Beauvais Tille Airport (LFOB) | Malpensa International Airport (LIMC) | 2026-09-08 04:01 UTC | 2026-09-08 05:09 UTC | 1h 8m |
| LT610 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-09-08 03:44 UTC | 2026-09-08 05:01 UTC | 1h 17m |
| SJX1901 | SJX | Gimhae International Airport (RKPK) | Taiwan Taoyuan International Airport (RCTP) | 2026-09-08 03:11 UTC | 2026-09-08 05:00 UTC | 1h 49m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Kerikeri Airport (NZKK) | 2026-09-08 04:29 UTC | 2026-09-08 04:59 UTC | 29m |
| IGO57Y | IndiGo | Abu Dhabi International Airport (OMAA) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-08 02:24 UTC | 2026-09-08 04:58 UTC | 2h 34m |
| OUN | OUN | Port Pirie Airport (YPIR) | Port Pirie Airport (YPIR) | 2026-09-08 04:37 UTC | 2026-09-08 04:57 UTC | 19m |
| BRU9808 | BRU | Antalya International Airport (LTAI) | Smolensk North Airport (XUBS) | 2026-09-07 20:45 UTC | 2026-09-08 04:55 UTC | 8h 9m |
| IGO24V | IndiGo | London Heathrow Airport (EGLL) | Pune Airport (VAPO) | 2026-09-07 19:40 UTC | 2026-09-08 04:50 UTC | 9h 10m |
| BAW199 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-07 20:30 UTC | 2026-09-08 04:46 UTC | 8h 15m |
| AM235 |  | Sydney Kingsford Smith International Airport (YSSY) | Mudgee Airport (YMDG) | 2026-09-08 04:13 UTC | 2026-09-08 04:41 UTC | 28m |
| TTW247 | TTW | Saga Airport (RJFS) | Hsinchu Air Base (RCPO) | 2026-09-08 02:50 UTC | 2026-09-08 04:41 UTC | 1h 50m |
| AZU4411 | AZU | Fazenda Saco da Tapera Airport (SSOT) | Benedito Mutran Airport (SIBD) | 2026-09-08 03:04 UTC | 2026-09-08 04:35 UTC | 1h 31m |
| JAL6787 | Japan Airlines | Narita International Airport (RJAA) | Hsinchu Air Base (RCPO) | 2026-09-08 01:27 UTC | 2026-09-08 04:34 UTC | 3h 7m |
| N403SP |  | Roberts Field/Redmond Municipal Airport (KRDM) | OG05 (OG05) | 2026-09-08 03:24 UTC | 2026-09-08 04:33 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
