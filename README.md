# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_08:49:30_UTC-green)

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

**Latest saved flight:** 2026-08-18 08:49:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 08:49:30 UTC

- **211,237** saved flights
- **67,084** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **211,237** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,539,328.4 tonnes** estimated CO2 emissions
- **147,207,444 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8361 |
| 2 | SkyWest Airlines | 7600 |
| 3 | EJA | 4113 |
| 4 | IndiGo | 3601 |
| 5 | American Airlines | 3533 |
| 6 | Southwest Airlines | 3386 |
| 7 | Delta Air Lines | 2729 |
| 8 | ENY | 2625 |
| 9 | LATAM Airlines | 1987 |
| 10 | AZU | 1913 |
| 11 | Lufthansa | 1771 |
| 12 | Vueling | 1763 |
| 13 | WIF | 1697 |
| 14 | LXJ | 1669 |
| 15 | easyJet | 1464 |
| 16 | Swiss International | 1411 |
| 17 | AXM | 1380 |
| 18 | United Airlines | 1340 |
| 19 | QLK | 1319 |
| 20 | Alaska Airlines | 1302 |
| 21 | EJU | 1293 |
| 22 | All Nippon Airways | 1282 |
| 23 | VIV | 1164 |
| 24 | GLO | 1139 |
| 25 | Air France | 1135 |
| 26 | PGT | 1129 |
| 27 | JetBlue | 1080 |
| 28 | WMT | 1072 |
| 29 | AEE | 1070 |
| 30 | Wizz Air | 1048 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178871 |
| 2 | 🇪🇸 ES | 13506 |
| 3 | 🇧🇷 BR | 12097 |
| 4 | 🇦🇺 AU | 11936 |
| 5 | 🇨🇦 CA | 11692 |
| 6 | 🇮🇳 IN | 11231 |
| 7 | 🇮🇹 IT | 11046 |
| 8 | 🇩🇪 DE | 10408 |
| 9 | 🇬🇧 GB | 9825 |
| 10 | 🇯🇵 JP | 8747 |
| 11 | 🇨🇴 CO | 8486 |
| 12 | 🇫🇷 FR | 8382 |
| 13 | 🇬🇷 GR | 6193 |
| 14 | 🇹🇷 TR | 6020 |
| 15 | 🇲🇽 MX | 5929 |
| 16 | 🇨🇭 CH | 5600 |
| 17 | 🇳🇴 NO | 5254 |
| 18 | 🇲🇾 MY | 3638 |
| 19 | 🇿🇦 ZA | 3543 |
| 20 | 🇵🇱 PL | 3489 |
| 21 | 🇹🇭 TH | 3396 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2807 |
| 24 | 🇬🇹 GT | 2703 |
| 25 | 🇰🇷 KR | 2575 |
| 26 | 🇭🇷 HR | 2276 |
| 27 | 🇲🇦 MA | 2127 |
| 28 | 🇳🇱 NL | 1881 |
| 29 | 🇲🇪 ME | 1804 |
| 30 | 🇮🇩 ID | 1755 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4447 |
| 2 | Denver International Airport |  | US | 3457 |
| 3 | Tokyo International Airport |  | JP | 2625 |
| 4 | Indira Gandhi International Airport |  | IN | 2561 |
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
| 17 | Madrid Barajas International Airport |  | ES | 1652 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1599 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1595 |
| 20 | Capua Airport |  | IT | 1590 |
| 21 | Macau International Airport |  | MO | 1548 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1538 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1489 |
| 24 | Malpensa International Airport |  | IT | 1462 |
| 25 | Charles de Gaulle International Airport |  | FR | 1447 |
| 26 | Charlotte/Douglas International Airport |  | US | 1426 |
| 27 | Kuala Lumpur International Airport |  | MY | 1342 |
| 28 | Ninoy Aquino International Airport |  | PH | 1330 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1306 |
| 30 | Bengaluru International Airport |  | IN | 1295 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1281 |
| 32 | Barcelona International Airport |  | ES | 1274 |
| 33 | Seattle-Tacoma International Airport |  | US | 1262 |
| 34 | Viracopos International Airport |  | BR | 1224 |
| 35 | Calgary International Airport |  | CA | 1201 |
| 36 | Oslo Gardermoen Airport |  | NO | 1166 |
| 37 | Vitoria/Foronda Airport |  | ES | 1165 |
| 38 | Reno/Tahoe International Airport |  | US | 1150 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1140 |
| 40 | Daniel K Inouye International Airport |  | US | 1125 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 751 | 21m | 244 km | 3,162.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 521 | 1h 7m | 770 km | 6,921.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 492 | 24m | 225 km | 1,908.7 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 430 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 351 | 27m | 275 km | 1,663.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 347 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 311 | 14m | 114 km | 610.0 t |
| 10 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 310 | 1h 49m | 1,423 km | 7,607.9 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 309 | 44m | 241 km | 1,283.5 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 290 | 22m | 55 km | 275.6 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 272 | 21m | 250 km | 1,174.9 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 258 | 27m | 215 km | 955.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 255 | 1h 37m | 1,156 km | 5,087.2 t |
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
| DKADV | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-08-18 08:19 UTC | 2026-08-18 08:49 UTC | 30m |
| GRZLY51 | GRZ | EHDB (EHDB) | Eindhoven Airport (EHEH) | 2026-08-18 08:01 UTC | 2026-08-18 08:38 UTC | 36m |
| FGTHA | FGT | Gap - Tallard Airport (LFNA) | Gap - Tallard Airport (LFNA) | 2026-08-18 06:07 UTC | 2026-08-18 08:35 UTC | 2h 28m |
| OKFTR | OKF | Memmingen Allgau Airport (EDJA) | Vienna International Airport (LOWW) | 2026-08-18 07:21 UTC | 2026-08-18 08:22 UTC | 1h 1m |
| MRNR06 | MRN | RAAF Base Edinburgh (YPED) | Loxton Airport (YLOX) | 2026-08-18 07:27 UTC | 2026-08-18 08:20 UTC | 53m |
| SAS4082 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Harstad/Narvik Airport Evenes (ENEV) | 2026-08-18 06:59 UTC | 2026-08-18 08:20 UTC | 1h 20m |
| THY70 | Turkish Airlines | Istanbul Hezarfen Airfield (LTBW) | Zhuhai Airport (ZGSD) | 2026-08-17 22:56 UTC | 2026-08-18 08:16 UTC | 9h 20m |
| RYR21NF | Ryanair | Dublin Airport (EIDW) | Paris Beauvais Tille Airport (LFOB) | 2026-08-18 07:05 UTC | 2026-08-18 08:08 UTC | 1h 3m |
| UFX61 | UFX | Humberside Airport (EGNJ) | Blackpool International Airport (EGNH) | 2026-08-18 07:06 UTC | 2026-08-18 08:05 UTC | 59m |
| EFC22C | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-08-18 06:56 UTC | 2026-08-18 08:02 UTC | 1h 5m |
| NOZ1264 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | LTGP (LTGP) | 2026-08-18 04:12 UTC | 2026-08-18 08:00 UTC | 3h 48m |
| HFA802 | HFA | Larnaca International Airport (LCLK) | Haifa International Airport (LLHA) | 2026-08-18 07:12 UTC | 2026-08-18 07:57 UTC | 45m |
| EZY5721 | easyJet | Southend Airport (EGMC) | Armilla Airport (LEGA) | 2026-08-18 05:48 UTC | 2026-08-18 07:54 UTC | 2h 5m |
| OYO3 | OYO | Paris-Le Bourget Airport (LFPB) | Otocac Airport (LDRO) | 2026-08-18 06:18 UTC | 2026-08-18 07:53 UTC | 1h 35m |
| SCR137 | SCR | Dusseldorf International Airport (EDDL) | Cannes-Mandelieu Airport (LFMD) | 2026-08-18 06:23 UTC | 2026-08-18 07:52 UTC | 1h 29m |
| VOE9EF | VOE | Malaga Airport (LEMG) | Bilbao Airport (LEBB) | 2026-08-18 06:49 UTC | 2026-08-18 07:51 UTC | 1h 2m |
| VOE8DL | VOE | Valencia Airport (LEVC) | La Morgal Airport (LEMR) | 2026-08-18 06:54 UTC | 2026-08-18 07:47 UTC | 52m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-08-18 07:23 UTC | 2026-08-18 07:47 UTC | 23m |
| MMA361 | MMA | Don Mueang International Airport (VTBD) | Naypyidaw Airport (VYEL) | 2026-08-18 06:25 UTC | 2026-08-18 07:46 UTC | 1h 21m |
| SAS62Y | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Kalixfors Airport (ESUK) | 2026-08-18 06:37 UTC | 2026-08-18 07:45 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
