# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_12:35:18_UTC-green)

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

**Latest saved flight:** 2026-08-17 12:35:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 12:35:18 UTC

- **207,853** saved flights
- **66,073** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **207,853** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,500,225.5 tonnes** estimated CO2 emissions
- **144,940,611 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8206 |
| 2 | SkyWest Airlines | 7461 |
| 3 | EJA | 4038 |
| 4 | IndiGo | 3560 |
| 5 | American Airlines | 3456 |
| 6 | Southwest Airlines | 3330 |
| 7 | Delta Air Lines | 2667 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1954 |
| 10 | AZU | 1878 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1727 |
| 13 | WIF | 1672 |
| 14 | LXJ | 1643 |
| 15 | easyJet | 1435 |
| 16 | Swiss International | 1385 |
| 17 | AXM | 1361 |
| 18 | United Airlines | 1306 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1267 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1144 |
| 24 | GLO | 1121 |
| 25 | Air France | 1115 |
| 26 | PGT | 1115 |
| 27 | AEE | 1063 |
| 28 | JetBlue | 1063 |
| 29 | WMT | 1051 |
| 30 | Wizz Air | 1027 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176102 |
| 2 | 🇪🇸 ES | 13291 |
| 3 | 🇧🇷 BR | 11895 |
| 4 | 🇦🇺 AU | 11741 |
| 5 | 🇨🇦 CA | 11467 |
| 6 | 🇮🇳 IN | 11097 |
| 7 | 🇮🇹 IT | 10861 |
| 8 | 🇩🇪 DE | 10279 |
| 9 | 🇬🇧 GB | 9685 |
| 10 | 🇯🇵 JP | 8643 |
| 11 | 🇨🇴 CO | 8248 |
| 12 | 🇫🇷 FR | 8233 |
| 13 | 🇬🇷 GR | 6126 |
| 14 | 🇹🇷 TR | 5909 |
| 15 | 🇲🇽 MX | 5842 |
| 16 | 🇨🇭 CH | 5545 |
| 17 | 🇳🇴 NO | 5180 |
| 18 | 🇲🇾 MY | 3588 |
| 19 | 🇿🇦 ZA | 3494 |
| 20 | 🇵🇱 PL | 3424 |
| 21 | 🇹🇭 TH | 3332 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2771 |
| 24 | 🇬🇹 GT | 2652 |
| 25 | 🇰🇷 KR | 2544 |
| 26 | 🇭🇷 HR | 2231 |
| 27 | 🇲🇦 MA | 2098 |
| 28 | 🇳🇱 NL | 1849 |
| 29 | 🇲🇪 ME | 1761 |
| 30 | 🇮🇩 ID | 1721 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4365 |
| 2 | Denver International Airport |  | US | 3394 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2523 |
| 5 | Guaymaral Airport |  | CO | 2498 |
| 6 | Harry Reid International Airport |  | US | 2344 |
| 7 | Zurich Airport |  | CH | 2169 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2167 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2150 |
| 10 | La Aurora Airport |  | GT | 2019 |
| 11 | Chicago O'Hare International Airport |  | US | 1922 |
| 12 | El Dorado International Airport |  | CO | 1892 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1857 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1731 |
| 16 | Frankfurt am Main International Airport |  | DE | 1712 |
| 17 | Madrid Barajas International Airport |  | ES | 1634 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1578 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1575 |
| 20 | Capua Airport |  | IT | 1573 |
| 21 | Macau International Airport |  | MO | 1544 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1506 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1441 |
| 25 | Charles de Gaulle International Airport |  | FR | 1428 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1325 |
| 28 | Ninoy Aquino International Airport |  | PH | 1313 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1284 |
| 30 | Bengaluru International Airport |  | IN | 1284 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Barcelona International Airport |  | ES | 1244 |
| 33 | Seattle-Tacoma International Airport |  | US | 1238 |
| 34 | Viracopos International Airport |  | BR | 1204 |
| 35 | Calgary International Airport |  | CA | 1174 |
| 36 | Oslo Gardermoen Airport |  | NO | 1150 |
| 37 | Vitoria/Foronda Airport |  | ES | 1147 |
| 38 | Reno/Tahoe International Airport |  | US | 1143 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1114 |
| 40 | Daniel K Inouye International Airport |  | US | 1110 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1027 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 471 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 348 | 27m | 275 km | 1,649.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 303 | 1h 49m | 1,423 km | 7,436.1 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 263 | 24m | 218 km | 990.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 257 | 19m | 99 km | 440.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 253 | 27m | 215 km | 937.0 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 247 | 1h 37m | 1,156 km | 4,927.6 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 238 | 19m | 144 km | 592.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFAB123 | FFA | Atsugi Naval Air Facility (RJTA) | Kisarazu Airport (RJTK) | 2026-08-17 12:22 UTC | 2026-08-17 12:35 UTC | 12m |
| SUI785 | SUI | Kassel-Calden Airport (EDVK) | Friedrichshafen Airport (EDNY) | 2026-08-17 11:35 UTC | 2026-08-17 12:29 UTC | 53m |
| GCNDK | GCN | Wellesbourne Mountford Airport (EGBW) | Leicester Airport (EGBG) | 2026-08-17 11:52 UTC | 2026-08-17 12:19 UTC | 27m |
| MILAN78 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Nimes-Arles-Camargue Airport (LFTW) | 2026-08-17 11:48 UTC | 2026-08-17 12:15 UTC | 26m |
| N4084E |  | TA29 (TA29) | Four Square Ranch Airport (3TA0) | 2026-08-17 11:56 UTC | 2026-08-17 12:10 UTC | 13m |
| HK1479G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-17 11:33 UTC | 2026-08-17 12:06 UTC | 32m |
| N585M |  | Chippewa Valley Regional Airport (KEAU) | Joe Foss Field (KFSD) | 2026-08-17 11:22 UTC | 2026-08-17 12:03 UTC | 40m |
| AWH34E | AWH | Hannover Airport (EDDV) | Brussels Airport (EBBR) | 2026-08-17 10:59 UTC | 2026-08-17 12:02 UTC | 1h 3m |
| FD629 |  | Perth Jandakot Airport (YPJT) | Wagin Airport (YWGN) | 2026-08-17 11:32 UTC | 2026-08-17 12:00 UTC | 28m |
| N1NP |  | Columbus Municipal Airport (KOLU) | Lincoln Airport (KLNK) | 2026-08-17 11:45 UTC | 2026-08-17 12:00 UTC | 14m |
| POL5490 | POL | Stockholm-Arlanda Airport (ESSA) | Stockholm-Bromma Airport (ESSB) | 2026-08-17 11:22 UTC | 2026-08-17 11:55 UTC | 32m |
| DKBXP | DKB | Chateau-Arnoux-Saint-Auban Airport (LFMX) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-08-17 11:02 UTC | 2026-08-17 11:54 UTC | 51m |
| EFC25D | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-08-17 11:37 UTC | 2026-08-17 11:50 UTC | 13m |
| EFC57P | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-08-17 10:40 UTC | 2026-08-17 11:47 UTC | 1h 6m |
| ENT8PS | ENT | Palma De Mallorca Airport (LEPA) | Francisco de Sá Carneiro Airport (LPPR) | 2026-08-17 10:20 UTC | 2026-08-17 11:44 UTC | 1h 24m |
| JIA5301 | JIA | Patrick Leahy Burlington International Airport (KBTV) | Philadelphia International Airport (KPHL) | 2026-08-17 10:36 UTC | 2026-08-17 11:40 UTC | 1h 3m |
| N4012J |  | HOPA (HOPA) | HOPA (HOPA) | 2026-08-17 11:21 UTC | 2026-08-17 11:39 UTC | 17m |
| ANE87AT | ANE | Madrid Barajas International Airport (LEMD) | Armilla Airport (LEGA) | 2026-08-17 10:56 UTC | 2026-08-17 11:38 UTC | 42m |
| N767KC |  | Green Bay/Austin Straubel International Airport (KGRB) | South Fox Island Airport (3MI2) | 2026-08-17 11:18 UTC | 2026-08-17 11:38 UTC | 20m |
| N560PY |  | New River Valley Airport (KPSK) | Jamestown Municipal Airport (K2A1) | 2026-08-17 11:01 UTC | 2026-08-17 11:36 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
