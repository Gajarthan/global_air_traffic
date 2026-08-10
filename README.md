# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_09:17:04_UTC-green)

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

**Latest saved flight:** 2026-08-10 09:17:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 09:17:04 UTC

- **183,550** saved flights
- **58,514** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,550** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,206,394.0 tonnes** estimated CO2 emissions
- **127,906,896 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7278 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3209 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1716 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1620 |
| 12 | WIF | 1516 |
| 13 | Vueling | 1512 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1257 |
| 16 | Swiss International | 1255 |
| 17 | AXM | 1231 |
| 18 | QLK | 1133 |
| 19 | EJU | 1127 |
| 20 | All Nippon Airways | 1121 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1012 |
| 23 | GLO | 984 |
| 24 | AEE | 956 |
| 25 | CXK | 953 |
| 26 | Air France | 950 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 933 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156986 |
| 2 | 🇪🇸 ES | 11782 |
| 3 | 🇧🇷 BR | 10535 |
| 4 | 🇦🇺 AU | 10288 |
| 5 | 🇮🇳 IN | 10050 |
| 6 | 🇨🇦 CA | 9995 |
| 7 | 🇮🇹 IT | 9487 |
| 8 | 🇩🇪 DE | 9076 |
| 9 | 🇬🇧 GB | 8507 |
| 10 | 🇯🇵 JP | 7473 |
| 11 | 🇫🇷 FR | 7303 |
| 12 | 🇨🇴 CO | 6864 |
| 13 | 🇬🇷 GR | 5379 |
| 14 | 🇲🇽 MX | 5248 |
| 15 | 🇨🇭 CH | 4894 |
| 16 | 🇹🇷 TR | 4777 |
| 17 | 🇳🇴 NO | 4713 |
| 18 | 🇲🇾 MY | 3207 |
| 19 | 🇵🇱 PL | 3071 |
| 20 | 🇿🇦 ZA | 3051 |
| 21 | 🇹🇭 TH | 2825 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2431 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2280 |
| 26 | 🇲🇦 MA | 1852 |
| 27 | 🇭🇷 HR | 1832 |
| 28 | 🇲🇪 ME | 1658 |
| 29 | 🇳🇱 NL | 1647 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2316 |
| 4 | Indira Gandhi International Airport |  | IN | 2251 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2149 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1967 |
| 8 | Zurich Airport |  | CH | 1959 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1645 |
| 13 | Salt Lake City International Airport |  | US | 1638 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1586 |
| 16 | Congonhas Airport |  | BR | 1528 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1442 |
| 20 | Capua Airport |  | IT | 1435 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1287 |
| 24 | Malpensa International Airport |  | IT | 1270 |
| 25 | Charles de Gaulle International Airport |  | FR | 1249 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1203 |
| 28 | Bengaluru International Airport |  | IN | 1192 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1148 |
| 30 | Ninoy Aquino International Airport |  | PH | 1146 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1085 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1046 |
| 37 | Calgary International Airport |  | CA | 1046 |
| 38 | Oslo Gardermoen Airport |  | NO | 1016 |
| 39 | Tenerife Norte Airport |  | ES | 1000 |
| 40 | Amsterdam Airport Schiphol |  | NL | 994 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 674 | 21m | 244 km | 2,838.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 440 | 1h 8m | 770 km | 5,845.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 272 | 44m | 241 km | 1,129.8 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 259 | 1h 48m | 1,423 km | 6,356.3 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 220 | 19m | 144 km | 547.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 217 | 1h 38m | 1,156 km | 4,329.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 213 | 31m | 369 km | 1,355.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FDB2RS | flydubai | Dubai International Airport (OMDB) | HE13 (HE13) | 2026-08-10 06:29 UTC | 2026-08-10 09:17 UTC | 2h 47m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-08-10 08:21 UTC | 2026-08-10 09:16 UTC | 54m |
| EFC65G | EFC | Al Maktoum International Airport (OMDW) | Ras Al Khaimah International Airport (OMRK) | 2026-08-10 08:27 UTC | 2026-08-10 09:13 UTC | 45m |
| A6FTK |  | Al Minhad Air Base (OMDM) | Dubai International Airport (OMDB) | 2026-08-10 08:45 UTC | 2026-08-10 09:12 UTC | 27m |
| JMU | JMU | Melbourne Essendon Airport (YMEN) | Sydney Bankstown Airport (YSBK) | 2026-08-10 07:49 UTC | 2026-08-10 09:11 UTC | 1h 22m |
| OKFUG94 | OKF | Dvur Kralove Nad Labem Airport (LKDK) | Vrchlabi Airport (LKVR) | 2026-08-10 08:12 UTC | 2026-08-10 09:06 UTC | 54m |
| TWI414 | TWI | Tautii Magheraus Airport (LRBM) | Golyama Smolnitsa Airport (LB35) | 2026-08-10 08:21 UTC | 2026-08-10 09:00 UTC | 39m |
| MSR967 | EgyptAir | Sharjah International Airport (OMSJ) | Hulwan (HE15) | 2026-08-10 05:52 UTC | 2026-08-10 08:49 UTC | 2h 56m |
| FR140 |  | Al Ain International Airport (OMAL) | Al Ain International Airport (OMAL) | 2026-08-10 08:45 UTC | 2026-08-10 08:48 UTC | 3m |
| GAF627 | GAF | Cologne Bonn Airport (EDDK) | Tivat Airport (LYTV) | 2026-08-10 07:17 UTC | 2026-08-10 08:47 UTC | 1h 30m |
| RYR68JT | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Santorini Airport (LGSR) | 2026-08-10 06:39 UTC | 2026-08-10 08:40 UTC | 2h 1m |
| EZS98NZ | EZS | Menorca Airport (LEMH) | Bex Airport (LSGB) | 2026-08-10 07:25 UTC | 2026-08-10 08:39 UTC | 1h 14m |
| RYR9TN | Ryanair | Luqa Airport (LMML) | Poznań-Ławica Airport (EPPO) | 2026-08-10 06:09 UTC | 2026-08-10 08:38 UTC | 2h 28m |
| EFC72E | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-10 08:21 UTC | 2026-08-10 08:36 UTC | 14m |
| AXB1069 | AXB | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-08-10 06:36 UTC | 2026-08-10 08:34 UTC | 1h 57m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-08-10 08:17 UTC | 2026-08-10 08:34 UTC | 16m |
| LLR831 | LLR | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-08-10 07:59 UTC | 2026-08-10 08:32 UTC | 32m |
| EFC13H | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-10 08:17 UTC | 2026-08-10 08:30 UTC | 12m |
| BNO92J | BNO | Sandefjord Airport Torp (ENTO) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-10 07:49 UTC | 2026-08-10 08:29 UTC | 39m |
| BBC603 | BBC | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-08-10 08:08 UTC | 2026-08-10 08:29 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
