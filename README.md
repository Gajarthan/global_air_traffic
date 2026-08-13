# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_09:18:10_UTC-green)

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

**Latest saved flight:** 2026-08-13 09:18:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 09:18:10 UTC

- **191,728** saved flights
- **60,435** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,728** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,293,707.0 tonnes** estimated CO2 emissions
- **132,968,524 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7608 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3323 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2256 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1664 |
| 12 | Vueling | 1591 |
| 13 | WIF | 1588 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1321 |
| 16 | Swiss International | 1302 |
| 17 | AXM | 1258 |
| 18 | EJU | 1184 |
| 19 | QLK | 1184 |
| 20 | All Nippon Airways | 1162 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 999 |
| 25 | PGT | 991 |
| 26 | CXK | 983 |
| 27 | AEE | 980 |
| 28 | United Airlines | 977 |
| 29 | WMT | 951 |
| 30 | Wizz Air | 951 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163377 |
| 2 | 🇪🇸 ES | 12333 |
| 3 | 🇧🇷 BR | 11014 |
| 4 | 🇦🇺 AU | 10794 |
| 5 | 🇨🇦 CA | 10510 |
| 6 | 🇮🇳 IN | 10408 |
| 7 | 🇮🇹 IT | 9970 |
| 8 | 🇩🇪 DE | 9476 |
| 9 | 🇬🇧 GB | 8925 |
| 10 | 🇯🇵 JP | 7850 |
| 11 | 🇫🇷 FR | 7652 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5594 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇨🇭 CH | 5136 |
| 16 | 🇹🇷 TR | 5133 |
| 17 | 🇳🇴 NO | 4926 |
| 18 | 🇲🇾 MY | 3294 |
| 19 | 🇿🇦 ZA | 3230 |
| 20 | 🇵🇱 PL | 3163 |
| 21 | 🇹🇭 TH | 2967 |
| 22 | 🇳🇿 NZ | 2706 |
| 23 | 🇵🇭 PH | 2528 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2344 |
| 26 | 🇭🇷 HR | 1975 |
| 27 | 🇲🇦 MA | 1941 |
| 28 | 🇳🇱 NL | 1715 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1545 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3143 |
| 3 | Tokyo International Airport |  | JP | 2417 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2344 |
| 6 | Harry Reid International Airport |  | US | 2229 |
| 7 | Zurich Airport |  | CH | 2029 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2025 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1710 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1628 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1509 |
| 19 | Capua Airport |  | IT | 1484 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1341 |
| 24 | Malpensa International Airport |  | IT | 1324 |
| 25 | Charles de Gaulle International Airport |  | FR | 1312 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Bengaluru International Airport |  | IN | 1231 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 30 | Ninoy Aquino International Airport |  | PH | 1195 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1145 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1104 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1078 |
| 38 | Oslo Gardermoen Airport |  | NO | 1075 |
| 39 | Tenerife Norte Airport |  | ES | 1050 |
| 40 | Vitoria/Foronda Airport |  | ES | 1037 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 706 | 21m | 244 km | 2,972.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 468 | 1h 7m | 770 km | 6,217.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 322 | 27m | 275 km | 1,525.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 285 | 44m | 241 km | 1,183.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 275 | 1h 49m | 1,423 km | 6,748.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 257 | 20m | 250 km | 1,110.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 230 | 24m | 218 km | 866.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OYSNS | OYS | Wyk auf Fohr Airport (EDXY) | Helgoland-Dune Airport (EDXH) | 2026-08-13 08:55 UTC | 2026-08-13 09:18 UTC | 22m |
| UFX63 | UFX | Humberside Airport (EGNJ) | Blackpool International Airport (EGNH) | 2026-08-13 08:28 UTC | 2026-08-13 09:16 UTC | 47m |
| RYR83UV | Ryanair | Biarritz-Anglet-Bayonne Airport (LFBZ) | Dublin Airport (EIDW) | 2026-08-13 07:33 UTC | 2026-08-13 09:14 UTC | 1h 41m |
| DETRY | DET | Aschaffenburg Airport (EDFC) | Mainbullau Airport (EDFU) | 2026-08-13 08:37 UTC | 2026-08-13 09:07 UTC | 29m |
| FR127 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-13 08:30 UTC | 2026-08-13 09:04 UTC | 33m |
| EZY35JL | easyJet | Manchester Airport (EGCC) | Luqa Airport (LMML) | 2026-08-13 05:55 UTC | 2026-08-13 09:03 UTC | 3h 8m |
| YOP | YOP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-13 08:34 UTC | 2026-08-13 08:56 UTC | 22m |
| ZFP | ZFP | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-13 08:11 UTC | 2026-08-13 08:48 UTC | 37m |
| HKH1 | HKH | Budapest Ferenc Liszt International Airport (LHBP) | Raron Airport (LSTA) | 2026-08-13 07:23 UTC | 2026-08-13 08:47 UTC | 1h 23m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-13 08:35 UTC | 2026-08-13 08:46 UTC | 11m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-08-13 08:06 UTC | 2026-08-13 08:43 UTC | 36m |
| PVF | PVF | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-13 08:21 UTC | 2026-08-13 08:36 UTC | 15m |
| FR139 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-13 08:32 UTC | 2026-08-13 08:36 UTC | 3m |
| HBFWU | HBF | Buochs Airport (LSZC) | Raron Airport (LSTA) | 2026-08-13 07:30 UTC | 2026-08-13 08:35 UTC | 1h 5m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-08-12 21:51 UTC | 2026-08-13 08:34 UTC | 10h 43m |
| AOJ69Y | AOJ | Graz Airport (LOWG) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-08-13 08:09 UTC | 2026-08-13 08:34 UTC | 25m |
| WZZ9NL | Wizz Air | Dortmund Airport (EDLW) | Tuzla Jegin Lug Sport Airfield (LQJL) | 2026-08-13 07:10 UTC | 2026-08-13 08:33 UTC | 1h 23m |
| R21235 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-13 07:16 UTC | 2026-08-13 08:29 UTC | 1h 13m |
| RUK80AJ | RUK | London Stansted Airport (EGSS) | Saiss Airport (GMFF) | 2026-08-13 05:49 UTC | 2026-08-13 08:29 UTC | 2h 39m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Kiruna Airport (ESNQ) | 2026-08-13 07:03 UTC | 2026-08-13 08:28 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
