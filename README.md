# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_08:05:55_UTC-green)

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

**Latest saved flight:** 2026-08-18 08:05:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 08:05:55 UTC

- **211,171** saved flights
- **67,074** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,171** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,538,324.9 tonnes** estimated CO2 emissions
- **147,149,269 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8355 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3599 |
| 5 | American Airlines | 3533 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1913 |
| 11 | Lufthansa | 1771 |
| 12 | Vueling | 1760 |
| 13 | WIF | 1697 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1411 |
| 17 | AXM | 1378 |
| 18 | United Airlines | 1340 |
| 19 | QLK | 1319 |
| 20 | Alaska Airlines | 1302 |
| 21 | EJU | 1290 |
| 22 | All Nippon Airways | 1281 |
| 23 | VIV | 1164 |
| 24 | GLO | 1139 |
| 25 | Air France | 1134 |
| 26 | PGT | 1129 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1072 |
| 29 | AEE | 1070 |
| 30 | Wizz Air | 1048 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178871 |
| 2 | 🇪🇸 ES | 13492 |
| 3 | 🇧🇷 BR | 12097 |
| 4 | 🇦🇺 AU | 11932 |
| 5 | 🇨🇦 CA | 11692 |
| 6 | 🇮🇳 IN | 11225 |
| 7 | 🇮🇹 IT | 11039 |
| 8 | 🇩🇪 DE | 10401 |
| 9 | 🇬🇧 GB | 9820 |
| 10 | 🇯🇵 JP | 8743 |
| 11 | 🇨🇴 CO | 8484 |
| 12 | 🇫🇷 FR | 8372 |
| 13 | 🇬🇷 GR | 6192 |
| 14 | 🇹🇷 TR | 6016 |
| 15 | 🇲🇽 MX | 5929 |
| 16 | 🇨🇭 CH | 5599 |
| 17 | 🇳🇴 NO | 5251 |
| 18 | 🇲🇾 MY | 3635 |
| 19 | 🇿🇦 ZA | 3537 |
| 20 | 🇵🇱 PL | 3488 |
| 21 | 🇹🇭 TH | 3391 |
| 22 | 🇳🇿 NZ | 2943 |
| 23 | 🇵🇭 PH | 2805 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2575 |
| 26 | 🇭🇷 HR | 2271 |
| 27 | 🇲🇦 MA | 2125 |
| 28 | 🇳🇱 NL | 1878 |
| 29 | 🇲🇪 ME | 1801 |
| 30 | 🇮🇩 ID | 1753 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4447 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2624 |
| 4 | Indira Gandhi International Airport |  | IN | 2560 |
| 5 | Guaymaral Airport |  | CO | 2531 |
| 6 | Harry Reid International Airport |  | US | 2373 |
| 7 | Zurich Airport |  | CH | 2198 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2183 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2182 |
| 10 | La Aurora Airport |  | GT | 2056 |
| 11 | Chicago O'Hare International Airport |  | US | 1956 |
| 12 | El Dorado International Airport |  | CO | 1939 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1875 |
| 14 | Salt Lake City International Airport |  | US | 1874 |
| 15 | Congonhas Airport |  | BR | 1759 |
| 16 | Frankfurt am Main International Airport |  | DE | 1725 |
| 17 | Madrid Barajas International Airport |  | ES | 1651 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1589 |
| 21 | Macau International Airport |  | MO | 1548 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1462 |
| 25 | Charles de Gaulle International Airport |  | FR | 1446 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1342 |
| 28 | Ninoy Aquino International Airport |  | PH | 1329 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1295 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1272 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1164 |
| 37 | Vitoria/Foronda Airport |  | ES | 1162 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1138 |
| 40 | Daniel K Inouye International Airport |  | US | 1125 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 751 | 21m | 244 km | 3,162.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 521 | 1h 7m | 770 km | 6,921.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 491 | 24m | 225 km | 1,904.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 351 | 27m | 275 km | 1,663.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 347 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 310 | 1h 49m | 1,423 km | 7,607.9 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 271 | 21m | 250 km | 1,170.6 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 254 | 1h 37m | 1,156 km | 5,067.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 249 | 19m | 165 km | 708.3 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 241 | 31m | 369 km | 1,534.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 227 | 1h 49m | 1,304 km | 5,106.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UFX61 | UFX | Humberside Airport (EGNJ) | Blackpool International Airport (EGNH) | 2026-08-18 07:06 UTC | 2026-08-18 08:05 UTC | 59m |
| EFC22C | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-08-18 06:56 UTC | 2026-08-18 08:02 UTC | 1h 5m |
| SCR137 | SCR | Dusseldorf International Airport (EDDL) | Cannes-Mandelieu Airport (LFMD) | 2026-08-18 06:23 UTC | 2026-08-18 07:52 UTC | 1h 29m |
| SKYHWK3 | SKY | Nordholz Airport (ETMN) | Bopfingen Airport (EDNQ) | 2026-08-18 06:58 UTC | 2026-08-18 07:43 UTC | 45m |
| EAI41D | EAI | Donegal Airport (EIDL) | Dublin Airport (EIDW) | 2026-08-18 07:01 UTC | 2026-08-18 07:42 UTC | 40m |
| IAM3182 | IAM | Ciampino Airport (LIRA) | Gioia Del Colle Airport (LIBV) | 2026-08-18 07:05 UTC | 2026-08-18 07:34 UTC | 29m |
| EFC70F | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-18 07:19 UTC | 2026-08-18 07:29 UTC | 9m |
| AFR25XW | Air France | Charles de Gaulle International Airport (LFPG) | Dublin Airport (EIDW) | 2026-08-18 05:49 UTC | 2026-08-18 07:22 UTC | 1h 33m |
| VLW | VLW | Sydney Bankstown Airport (YSBK) | Bathurst Airport (YBTH) | 2026-08-18 06:48 UTC | 2026-08-18 07:18 UTC | 30m |
| ASLAN03 | ASL | Cildir Airport (LTBD) | Cildir Airport (LTBD) | 2026-08-17 19:27 UTC | 2026-08-18 07:18 UTC | 11h 50m |
| OKALT | OKA | Kunovice Airport (LKKU) | Otocac Airport (LDRO) | 2026-08-18 06:04 UTC | 2026-08-18 07:17 UTC | 1h 12m |
| GNS118 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-08-18 07:15 UTC | 2026-08-18 07:16 UTC | 1m |
| SWR3L | Swiss International | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-18 06:29 UTC | 2026-08-18 07:15 UTC | 46m |
| RYR80PC | Ryanair | L'Aquila / Preturo Airport (LIAP) | Malpensa International Airport (LIMC) | 2026-08-18 06:03 UTC | 2026-08-18 07:15 UTC | 1h 11m |
| RYR9929 | Ryanair | Malaga Airport (LEMG) | Bremen Airport (EDDW) | 2026-08-18 04:21 UTC | 2026-08-18 07:15 UTC | 2h 54m |
| IGO127 | IndiGo | Barrackpore Air Force Station (VEPI) | Yongphulla Airport (VQ10) | 2026-08-18 06:36 UTC | 2026-08-18 07:14 UTC | 37m |
| OHDAN | OHD | Pori Airport (EFPO) | Turku Airport (EFTU) | 2026-08-18 06:18 UTC | 2026-08-18 07:13 UTC | 54m |
| VLG1PL | Vueling | Barcelona International Airport (LEBL) | Bilbao Airport (LEBB) | 2026-08-18 06:28 UTC | 2026-08-18 07:11 UTC | 43m |
| KLC25X | KLC | Amsterdam Airport Schiphol (EHAM) | Lager Hammelburg Airport (EDFJ) | 2026-08-18 06:23 UTC | 2026-08-18 07:10 UTC | 47m |
| SAS1314 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-18 06:38 UTC | 2026-08-18 07:10 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
