# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_06:05:45_UTC-green)

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

**Latest saved flight:** 2026-08-17 06:05:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 06:05:45 UTC

- **207,143** saved flights
- **65,959** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,143** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,490,892.2 tonnes** estimated CO2 emissions
- **144,399,546 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8155 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3540 |
| 5 | American Airlines | 3455 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2666 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1951 |
| 10 | AZU | 1875 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1659 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1377 |
| 17 | AXM | 1351 |
| 18 | United Airlines | 1304 |
| 19 | Alaska Airlines | 1287 |
| 20 | QLK | 1283 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1256 |
| 23 | VIV | 1143 |
| 24 | GLO | 1121 |
| 25 | PGT | 1104 |
| 26 | Air France | 1103 |
| 27 | JetBlue | 1063 |
| 28 | AEE | 1054 |
| 29 | WMT | 1043 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176049 |
| 2 | 🇪🇸 ES | 13188 |
| 3 | 🇧🇷 BR | 11877 |
| 4 | 🇦🇺 AU | 11656 |
| 5 | 🇨🇦 CA | 11457 |
| 6 | 🇮🇳 IN | 11032 |
| 7 | 🇮🇹 IT | 10780 |
| 8 | 🇩🇪 DE | 10211 |
| 9 | 🇬🇧 GB | 9629 |
| 10 | 🇯🇵 JP | 8545 |
| 11 | 🇨🇴 CO | 8245 |
| 12 | 🇫🇷 FR | 8169 |
| 13 | 🇬🇷 GR | 6080 |
| 14 | 🇹🇷 TR | 5867 |
| 15 | 🇲🇽 MX | 5841 |
| 16 | 🇨🇭 CH | 5516 |
| 17 | 🇳🇴 NO | 5142 |
| 18 | 🇲🇾 MY | 3557 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3407 |
| 21 | 🇹🇭 TH | 3285 |
| 22 | 🇳🇿 NZ | 2886 |
| 23 | 🇵🇭 PH | 2757 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2525 |
| 26 | 🇭🇷 HR | 2210 |
| 27 | 🇲🇦 MA | 2083 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1745 |
| 30 | 🇮🇩 ID | 1710 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2573 |
| 4 | Indira Gandhi International Airport |  | IN | 2505 |
| 5 | Guaymaral Airport |  | CO | 2496 |
| 6 | Harry Reid International Airport |  | US | 2342 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2155 |
| 8 | Zurich Airport |  | CH | 2155 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1920 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1854 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1729 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1619 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1543 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1505 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1457 |
| 24 | Malpensa International Airport |  | IT | 1427 |
| 25 | Charlotte/Douglas International Airport |  | US | 1413 |
| 26 | Charles de Gaulle International Airport |  | FR | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1316 |
| 28 | Ninoy Aquino International Airport |  | PH | 1306 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1280 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Seattle-Tacoma International Airport |  | US | 1236 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1202 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Reno/Tahoe International Airport |  | US | 1143 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Daniel K Inouye International Airport |  | US | 1110 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1107 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 506 | 1h 7m | 770 km | 6,721.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 483 | 24m | 225 km | 1,873.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 343 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 300 | 1h 49m | 1,423 km | 7,362.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 245 | 1h 37m | 1,156 km | 4,887.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 238 | 31m | 369 km | 1,514.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N700JV |  | Aurillac Airport (LFLW) | Lyon-Bron Airport (LFLY) | 2026-08-17 05:29 UTC | 2026-08-17 06:05 UTC | 36m |
| WIF862 | WIF | Bodø Airport (ENBO) | Harstad/Narvik Airport Evenes (ENEV) | 2026-08-17 05:38 UTC | 2026-08-17 06:04 UTC | 26m |
| XPP | XPP | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-17 05:20 UTC | 2026-08-17 05:32 UTC | 12m |
| DFEEL | DFE | Geneva Cointrin International Airport (LSGG) | Trento / Mattarello Airport (LIDT) | 2026-08-17 04:23 UTC | 2026-08-17 05:27 UTC | 1h 4m |
| ONI01 | ONI | Kisarazu Airport (RJTK) | Kisarazu Airport (RJTK) | 2026-08-17 05:24 UTC | 2026-08-17 05:24 UTC | 0m |
| WZZ33YN | Wizz Air | Katowice International Airport (EPKT) | Billund Airport (EKBI) | 2026-08-17 04:03 UTC | 2026-08-17 05:24 UTC | 1h 20m |
| EFC71A | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-17 05:12 UTC | 2026-08-17 05:23 UTC | 10m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bombala Airport (YBOM) | 2026-08-17 04:40 UTC | 2026-08-17 05:23 UTC | 42m |
| PSDN19 | PSD | Garden Island (Military) Airport (YGAD) | Garden Island (Military) Airport (YGAD) | 2026-08-17 05:09 UTC | 2026-08-17 05:21 UTC | 11m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-08-17 04:48 UTC | 2026-08-17 05:16 UTC | 27m |
| WMT102 | WMT | Cluj-Napoca International Airport (LRCL) | Memmingen Allgau Airport (EDJA) | 2026-08-17 03:42 UTC | 2026-08-17 05:14 UTC | 1h 31m |
| JTE216 | JTE | Adelaide International Airport (YPAD) | Mount Vivian Airport (YVIV) | 2026-08-17 04:13 UTC | 2026-08-17 05:12 UTC | 59m |
| ONI01 | ONI | Atsugi Naval Air Facility (RJTA) | Kisarazu Airport (RJTK) | 2026-08-17 04:33 UTC | 2026-08-17 05:11 UTC | 38m |
| ANZ317L | ANZ | Wellington International Airport (NZWN) | Nelson Airport (NZNS) | 2026-08-17 04:51 UTC | 2026-08-17 05:10 UTC | 19m |
| IGO479 | IndiGo | Chennai International Airport (VOMM) | Mysore Airport (VOMY) | 2026-08-17 04:37 UTC | 2026-08-17 05:09 UTC | 31m |
| BH102 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-17 04:48 UTC | 2026-08-17 05:08 UTC | 20m |
| VOZ610 | Virgin Australia | Mackay Airport (YBMK) | Brisbane International Airport (YBBN) | 2026-08-17 04:05 UTC | 2026-08-17 05:08 UTC | 1h 2m |
| RYR46FX | Ryanair | Malpensa International Airport (LIMC) | Tortoli' / Arbatax Airport (LIET) | 2026-08-17 04:11 UTC | 2026-08-17 05:07 UTC | 55m |
| RYR7GF | Ryanair | Henri Coanda International Airport (LROP) | Malpensa International Airport (LIMC) | 2026-08-17 03:05 UTC | 2026-08-17 05:07 UTC | 2h 1m |
| RYR45TN | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Bari / Palese International Airport (LIBD) | 2026-08-17 04:06 UTC | 2026-08-17 05:06 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
