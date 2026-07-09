# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_08:12:11_UTC-green)

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

**Latest saved flight:** 2026-07-09 08:12:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-09 08:12:11 UTC

- **133,773** saved flights
- **45,294** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **133,773** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,609,830.6 tonnes** estimated CO2 emissions
- **93,323,510 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5431 |
| 2 | SkyWest Airlines | 4937 |
| 3 | EJA | 2623 |
| 4 | IndiGo | 2491 |
| 5 | American Airlines | 2090 |
| 6 | Southwest Airlines | 2009 |
| 7 | ENY | 1681 |
| 8 | Delta Air Lines | 1599 |
| 9 | Lufthansa | 1384 |
| 10 | LATAM Airlines | 1227 |
| 11 | Vueling | 1174 |
| 12 | WIF | 1166 |
| 13 | AZU | 1137 |
| 14 | LXJ | 1026 |
| 15 | AXM | 1021 |
| 16 | Swiss International | 950 |
| 17 | All Nippon Airways | 875 |
| 18 | easyJet | 865 |
| 19 | Alaska Airlines | 850 |
| 20 | QLK | 841 |
| 21 | EJU | 821 |
| 22 | VIV | 738 |
| 23 | AEE | 727 |
| 24 | Air France | 719 |
| 25 | Cathay Pacific | 719 |
| 26 | CXK | 719 |
| 27 | United Airlines | 709 |
| 28 | JetBlue | 705 |
| 29 | MXY | 693 |
| 30 | GLO | 681 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 114733 |
| 2 | 🇪🇸 ES | 8875 |
| 3 | 🇮🇳 IN | 7811 |
| 4 | 🇦🇺 AU | 7761 |
| 5 | 🇧🇷 BR | 7524 |
| 6 | 🇨🇦 CA | 7058 |
| 7 | 🇩🇪 DE | 6978 |
| 8 | 🇮🇹 IT | 6952 |
| 9 | 🇬🇧 GB | 5999 |
| 10 | 🇯🇵 JP | 5741 |
| 11 | 🇫🇷 FR | 5308 |
| 12 | 🇨🇴 CO | 4173 |
| 13 | 🇲🇽 MX | 3896 |
| 14 | 🇬🇷 GR | 3826 |
| 15 | 🇳🇴 NO | 3625 |
| 16 | 🇨🇭 CH | 3454 |
| 17 | 🇹🇷 TR | 3036 |
| 18 | 🇲🇾 MY | 2651 |
| 19 | 🇵🇱 PL | 2206 |
| 20 | 🇿🇦 ZA | 2201 |
| 21 | 🇳🇿 NZ | 2102 |
| 22 | 🇹🇭 TH | 2056 |
| 23 | 🇰🇷 KR | 1977 |
| 24 | 🇵🇭 PH | 1841 |
| 25 | 🇬🇹 GT | 1810 |
| 26 | 🇲🇦 MA | 1420 |
| 27 | 🇲🇪 ME | 1331 |
| 28 | 🇳🇱 NL | 1254 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1185 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2789 |
| 2 | Denver International Airport |  | US | 2262 |
| 3 | Tokyo International Airport |  | JP | 1875 |
| 4 | Indira Gandhi International Airport |  | IN | 1722 |
| 5 | Harry Reid International Airport |  | US | 1664 |
| 6 | Guaymaral Airport |  | CO | 1627 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1569 |
| 8 | Zurich Airport |  | CH | 1489 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1421 |
| 10 | La Aurora Airport |  | GT | 1398 |
| 11 | Frankfurt am Main International Airport |  | DE | 1339 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1291 |
| 13 | Chicago O'Hare International Airport |  | US | 1278 |
| 14 | Salt Lake City International Airport |  | US | 1190 |
| 15 | Macau International Airport |  | MO | 1186 |
| 16 | El Dorado International Airport |  | CO | 1184 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1157 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1096 |
| 19 | Capua Airport |  | IT | 1095 |
| 20 | Madrid Barajas International Airport |  | ES | 1094 |
| 21 | Congonhas Airport |  | BR | 1065 |
| 22 | Kuala Lumpur International Airport |  | MY | 1030 |
| 23 | Charlotte/Douglas International Airport |  | US | 986 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 974 |
| 25 | Charles de Gaulle International Airport |  | FR | 959 |
| 26 | Bengaluru International Airport |  | IN | 943 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 917 |
| 28 | Malpensa International Airport |  | IT | 883 |
| 29 | Ninoy Aquino International Airport |  | PH | 856 |
| 30 | Daniel K Inouye International Airport |  | US | 832 |
| 31 | Barcelona International Airport |  | ES | 824 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 817 |
| 33 | Tenerife Norte Airport |  | ES | 803 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 787 |
| 35 | Calgary International Airport |  | CA | 776 |
| 36 | Seattle-Tacoma International Airport |  | US | 767 |
| 37 | Scottsdale Airport |  | US | 764 |
| 38 | Viracopos International Airport |  | BR | 761 |
| 39 | Vitoria/Foronda Airport |  | ES | 758 |
| 40 | Amsterdam Airport Schiphol |  | NL | 753 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 684 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 484 | 21m | 244 km | 2,038.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 334 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 333 | 24m | 225 km | 1,291.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 323 | 1h 10m | 770 km | 4,290.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 285 | 14m | 114 km | 559.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 251 | 26m | 275 km | 1,189.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 243 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 196 | 22m | 55 km | 186.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 185 | 26m | 215 km | 685.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 184 | 20m | 99 km | 315.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 179 | 1h 46m | 1,423 km | 4,392.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 179 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 162 | 20m | 250 km | 699.7 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 160 | 44m | 452 km | 1,247.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 160 | 30m | 49 km | 135.2 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 156 | 1h 1m | 695 km | 1,870.0 t |
| 26 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 155 | 1h 16m | 961 km | 2,569.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 151 | 1h 38m | 1,156 km | 3,012.4 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 148 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-09 08:02 UTC | 2026-07-09 08:12 UTC | 10m |
| EAG101T | EAG | Durham Tees Valley Airport (EGNV) | Durham Tees Valley Airport (EGNV) | 2026-07-09 07:21 UTC | 2026-07-09 08:11 UTC | 50m |
| N774PT |  | Lugano Airport (LSZA) | Muenster Aero Airport (LSPU) | 2026-07-09 07:27 UTC | 2026-07-09 07:57 UTC | 30m |
| PHWPB | PHW | Budel Airport (EHBD) | Decimomannu Airport (LIED) | 2026-07-09 05:09 UTC | 2026-07-09 07:57 UTC | 2h 47m |
| IGO1157 | IndiGo | Juhu Aerodrome (VAJJ) | Tribhuvan International Airport (VNKT) | 2026-07-09 05:50 UTC | 2026-07-09 07:55 UTC | 2h 5m |
| 88K |  | Adelaide International Airport (YPAD) | Adelaide International Airport (YPAD) | 2026-07-09 07:37 UTC | 2026-07-09 07:54 UTC | 17m |
| FDB1YT | flydubai | Bahrain International Airport (OBBI) | Dubai International Airport (OMDB) | 2026-07-09 06:51 UTC | 2026-07-09 07:48 UTC | 56m |
| OMAMG | Oman Air | M. R. Stefanik Airport (LZIB) | Livno Brda Bosni Airport (LQLV) | 2026-07-09 07:03 UTC | 2026-07-09 07:47 UTC | 43m |
| RYR88GF | Ryanair | Treviso / Sant'Angelo Airport (LIPH) | Leszno Strzyzewi Airport (EPLS) | 2026-07-09 06:15 UTC | 2026-07-09 07:46 UTC | 1h 31m |
| KOC02 | KOC | Sabiha Gokcen International Airport (LTFJ) | Cardak Airport (LTAY) | 2026-07-09 07:09 UTC | 2026-07-09 07:45 UTC | 35m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-07-09 07:18 UTC | 2026-07-09 07:44 UTC | 25m |
| RSCU208 | RSC | Wollongong Airport (YWOL) | Sydney Kingsford Smith International Airport (YSSY) | 2026-07-09 07:21 UTC | 2026-07-09 07:43 UTC | 22m |
| PE315 |  | Newcastle Airport (YWLM) | Goulburn Airport (YGLB) | 2026-07-09 06:54 UTC | 2026-07-09 07:43 UTC | 49m |
| QTR1039 | Qatar Airways | Sharjah International Airport (OMSJ) | Sharjah International Airport (OMSJ) | 2026-07-09 07:38 UTC | 2026-07-09 07:39 UTC | 0m |
| WIF1DK | WIF | Sogndal Airport (ENSG) | Sandane Airport Anda (ENSD) | 2026-07-09 07:21 UTC | 2026-07-09 07:32 UTC | 11m |
| N81NG |  | San Antonio International Airport (KSAT) | Cavern City Air Trml Airport (KCNM) | 2026-07-09 06:11 UTC | 2026-07-09 07:31 UTC | 1h 19m |
| AIC8UF | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-07-09 07:08 UTC | 2026-07-09 07:28 UTC | 20m |
| FYS16ON | FYS | Muchamiel Airport (LEMU) | Muchamiel Airport (LEMU) | 2026-07-09 07:14 UTC | 2026-07-09 07:26 UTC | 12m |
| UIA8681 | UIA | Tainan Airport (RCNN) | Makung Airport (RCQC) | 2026-07-09 07:10 UTC | 2026-07-09 07:25 UTC | 15m |
| WIF8XA | WIF | Trondheim Airport Vaernes (ENVA) | Bardufoss Airport (ENDU) | 2026-07-09 06:08 UTC | 2026-07-09 07:24 UTC | 1h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
