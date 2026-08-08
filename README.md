# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_06:11:12_UTC-green)

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

**Latest saved flight:** 2026-08-08 06:11:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 06:11:12 UTC

- **177,468** saved flights
- **57,123** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,468** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,132,566.0 tonnes** estimated CO2 emissions
- **123,627,014 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7023 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3506 |
| 4 | IndiGo | 3111 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1581 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1208 |
| 16 | AXM | 1201 |
| 17 | easyJet | 1200 |
| 18 | QLK | 1089 |
| 19 | EJU | 1082 |
| 20 | Alaska Airlines | 1080 |
| 21 | All Nippon Airways | 1078 |
| 22 | VIV | 978 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 942 |
| 25 | GLO | 939 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 896 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152705 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10039 |
| 5 | 🇮🇳 IN | 9751 |
| 6 | 🇨🇦 CA | 9722 |
| 7 | 🇮🇹 IT | 9152 |
| 8 | 🇩🇪 DE | 8742 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7137 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6525 |
| 13 | 🇬🇷 GR | 5158 |
| 14 | 🇲🇽 MX | 5094 |
| 15 | 🇨🇭 CH | 4688 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4405 |
| 18 | 🇲🇾 MY | 3132 |
| 19 | 🇵🇱 PL | 2941 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2651 |
| 22 | 🇳🇿 NZ | 2577 |
| 23 | 🇵🇭 PH | 2341 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2217 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1742 |
| 28 | 🇲🇪 ME | 1609 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1508 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2223 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2170 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1916 |
| 8 | Zurich Airport |  | CH | 1880 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1589 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1508 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1386 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1243 |
| 24 | Malpensa International Airport |  | IT | 1213 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1181 |
| 28 | Bengaluru International Airport |  | IN | 1159 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1102 |
| 30 | Ninoy Aquino International Airport |  | PH | 1101 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1025 |
| 34 | Daniel K Inouye International Airport |  | US | 1024 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 654 | 21m | 244 km | 2,753.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 416 | 24m | 225 km | 1,613.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 410 | 1h 8m | 770 km | 5,446.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 246 | 1h 48m | 1,423 km | 6,037.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKFUG94 | OKF | Kromeriz Airport (LKKM) | Kromeriz Airport (LKKM) | 2026-08-08 06:00 UTC | 2026-08-08 06:11 UTC | 10m |
| 4LGCG |  | Yerevan Yegvard Airport (UD21) | UB13 (UB13) | 2026-08-08 05:44 UTC | 2026-08-08 06:09 UTC | 25m |
| KDI | KDI | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-08-08 04:22 UTC | 2026-08-08 05:47 UTC | 1h 25m |
| N758NL |  | Mc Clellan-Palomar Airport (KCRQ) | Whiteman Airport (KWHP) | 2026-08-08 04:37 UTC | 2026-08-08 05:33 UTC | 55m |
| WWF287 | WWF | Portland International Airport (KPDX) | Cottonwood Creek Ranch Airport (OG50) | 2026-08-08 02:52 UTC | 2026-08-08 05:30 UTC | 2h 37m |
| AHX802 | AHX | Osaka International Airport (RJOO) | Kumamoto Airport (RJFT) | 2026-08-08 04:27 UTC | 2026-08-08 05:25 UTC | 57m |
| OAL048 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiros Airport (LGSY) | 2026-08-08 04:55 UTC | 2026-08-08 05:19 UTC | 23m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 04:47 UTC | 2026-08-08 05:18 UTC | 31m |
| WZZ52LD | Wizz Air | Katowice International Airport (EPKT) | LRPV (LRPV) | 2026-08-08 04:11 UTC | 2026-08-08 05:17 UTC | 1h 5m |
| VAR448 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-08 05:08 UTC | 2026-08-08 05:14 UTC | 5m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-08-08 04:18 UTC | 2026-08-08 05:12 UTC | 54m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-08-08 04:46 UTC | 2026-08-08 05:08 UTC | 21m |
| YEL11 | YEL | Long Beach (Daugherty Field) Airport (KLGB) | Scottsdale Airport (KSDL) | 2026-08-08 04:06 UTC | 2026-08-08 05:07 UTC | 1h 0m |
| RYR7KL | Ryanair | Bari / Palese International Airport (LIBD) | Kasteli Airport (LGTL) | 2026-08-08 03:57 UTC | 2026-08-08 05:05 UTC | 1h 7m |
| RYR7YG | Ryanair | Malpensa International Airport (LIMC) | Tivat Airport (LYTV) | 2026-08-08 04:00 UTC | 2026-08-08 05:05 UTC | 1h 5m |
| LLR873 | LLR | Indira Gandhi International Airport (VIDP) | Pantnagar Airport (VIPT) | 2026-08-08 04:25 UTC | 2026-08-08 05:02 UTC | 37m |
| CEB911 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-08 04:31 UTC | 2026-08-08 05:02 UTC | 30m |
| N241H |  | Santa Fe Regional Airport (KSAF) | 49AZ (49AZ) | 2026-08-08 04:13 UTC | 2026-08-08 04:57 UTC | 43m |
| GLO1468 | GLO | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Agropastoril bom Pastor Airport (SDRO) | 2026-08-08 03:23 UTC | 2026-08-08 04:56 UTC | 1h 33m |
| IGO5268 | IndiGo | Juhu Aerodrome (VAJJ) | Ambala Air Force Station (VIAM) | 2026-08-08 03:19 UTC | 2026-08-08 04:56 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
