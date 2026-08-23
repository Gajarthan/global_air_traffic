# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_18:07:16_UTC-green)

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

**Latest saved flight:** 2026-08-23 18:07:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 18:07:16 UTC

- **229,501** saved flights
- **70,917** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **229,501** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,767,578.1 tonnes** estimated CO2 emissions
- **160,439,308 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9217 |
| 2 | SkyWest Airlines | 8138 |
| 3 | EJA | 4427 |
| 4 | IndiGo | 3880 |
| 5 | American Airlines | 3752 |
| 6 | Southwest Airlines | 3554 |
| 7 | Delta Air Lines | 2934 |
| 8 | ENY | 2801 |
| 9 | LATAM Airlines | 2204 |
| 10 | AZU | 2129 |
| 11 | Vueling | 1949 |
| 12 | Lufthansa | 1873 |
| 13 | WIF | 1808 |
| 14 | LXJ | 1801 |
| 15 | easyJet | 1601 |
| 16 | Swiss International | 1533 |
| 17 | AXM | 1520 |
| 18 | EJU | 1464 |
| 19 | United Airlines | 1452 |
| 20 | QLK | 1448 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1276 |
| 24 | VIV | 1259 |
| 25 | WMT | 1256 |
| 26 | PGT | 1255 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1204 |
| 29 | JetBlue | 1146 |
| 30 | AEE | 1144 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 191490 |
| 2 | 🇪🇸 ES | 14742 |
| 3 | 🇧🇷 BR | 13400 |
| 4 | 🇦🇺 AU | 12963 |
| 5 | 🇨🇦 CA | 12655 |
| 6 | 🇮🇹 IT | 12430 |
| 7 | 🇮🇳 IN | 12096 |
| 8 | 🇩🇪 DE | 11310 |
| 9 | 🇬🇧 GB | 10806 |
| 10 | 🇨🇴 CO | 9469 |
| 11 | 🇯🇵 JP | 9314 |
| 12 | 🇫🇷 FR | 9200 |
| 13 | 🇹🇷 TR | 6765 |
| 14 | 🇬🇷 GR | 6752 |
| 15 | 🇲🇽 MX | 6384 |
| 16 | 🇨🇭 CH | 6102 |
| 17 | 🇳🇴 NO | 5644 |
| 18 | 🇲🇾 MY | 4062 |
| 19 | 🇿🇦 ZA | 4007 |
| 20 | 🇹🇭 TH | 3997 |
| 21 | 🇵🇱 PL | 3822 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3144 |
| 24 | 🇬🇹 GT | 2886 |
| 25 | 🇰🇷 KR | 2706 |
| 26 | 🇭🇷 HR | 2625 |
| 27 | 🇲🇦 MA | 2330 |
| 28 | 🇲🇪 ME | 2100 |
| 29 | 🇳🇱 NL | 2057 |
| 30 | 🇮🇩 ID | 1978 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4793 |
| 2 | Denver International Airport |  | US | 3730 |
| 3 | Indira Gandhi International Airport |  | IN | 2797 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2652 |
| 6 | Harry Reid International Airport |  | US | 2480 |
| 7 | Zurich Airport |  | CH | 2393 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2345 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2314 |
| 10 | La Aurora Airport |  | GT | 2199 |
| 11 | El Dorado International Airport |  | CO | 2102 |
| 12 | Chicago O'Hare International Airport |  | US | 2076 |
| 13 | Salt Lake City International Airport |  | US | 2018 |
| 14 | Congonhas Airport |  | BR | 1956 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1942 |
| 16 | Frankfurt am Main International Airport |  | DE | 1842 |
| 17 | Madrid Barajas International Airport |  | ES | 1801 |
| 18 | Capua Airport |  | IT | 1799 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1718 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1706 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1652 |
| 22 | Malpensa International Airport |  | IT | 1642 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1597 |
| 25 | Charles de Gaulle International Airport |  | FR | 1596 |
| 26 | Ninoy Aquino International Airport |  | PH | 1509 |
| 27 | Charlotte/Douglas International Airport |  | US | 1499 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1438 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1391 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1369 |
| 32 | Viracopos International Airport |  | BR | 1362 |
| 33 | Bengaluru International Airport |  | IN | 1358 |
| 34 | Seattle-Tacoma International Airport |  | US | 1350 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1347 |
| 36 | Don Mueang International Airport |  | TH | 1307 |
| 37 | Calgary International Airport |  | CA | 1301 |
| 38 | Oslo Gardermoen Airport |  | NO | 1277 |
| 39 | Vitoria/Foronda Airport |  | ES | 1250 |
| 40 | O. R. Tambo International Airport |  | ZA | 1246 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 834 | 21m | 244 km | 3,511.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 555 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 515 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 352 | 1h 50m | 1,423 km | 8,638.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 332 | 44m | 241 km | 1,379.1 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 321 | 21m | 250 km | 1,386.5 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 310 | 44m | 555 km | 2,968.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 306 | 22m | 55 km | 290.8 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 297 | 24m | 218 km | 1,118.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 295 | 1h 38m | 1,156 km | 5,885.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 280 | 27m | 215 km | 1,037.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 269 | 1h 14m | 961 km | 4,458.8 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 241 | 28m | 152 km | 629.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-23 17:25 UTC | 2026-08-23 18:07 UTC | 41m |
| N25476 |  | Ruffatto Field (LL51) | 2LL1 (2LL1) | 2026-08-23 17:29 UTC | 2026-08-23 17:53 UTC | 24m |
| N565E |  | Cricket Field (4WA2) | Sunnyside Municipal Airport (K1S5) | 2026-08-23 16:42 UTC | 2026-08-23 17:50 UTC | 1h 7m |
| N971KC |  | Centennial Airport (KAPA) | Bijou Bottom Strip (9CO8) | 2026-08-23 16:55 UTC | 2026-08-23 17:48 UTC | 52m |
| N451VL |  | 95CA (95CA) | Whiteman Airport (KWHP) | 2026-08-23 16:56 UTC | 2026-08-23 17:46 UTC | 49m |
| N186FM |  | San Marcos Regional Airport (KHYI) | San Marcos Regional Airport (KHYI) | 2026-08-23 17:43 UTC | 2026-08-23 17:45 UTC | 2m |
| LXJ617 | LXJ | Franke Field (79AR) | Orlando Executive Airport (KORL) | 2026-08-23 15:59 UTC | 2026-08-23 17:41 UTC | 1h 42m |
| N901MJ |  | Purdue University Airport (KLAF) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-23 17:08 UTC | 2026-08-23 17:41 UTC | 33m |
| CNS119 | CNS | Harry Reid International Airport (KLAS) | Telluride Regional Airport (KTEX) | 2026-08-23 16:38 UTC | 2026-08-23 17:41 UTC | 1h 2m |
| N399LG |  | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2026-08-23 17:32 UTC | 2026-08-23 17:37 UTC | 5m |
| N3Q |  | Gunnison-Crested Butte Regional Airport (KGUC) | Edwards Grass Strip (2KS3) | 2026-08-23 16:16 UTC | 2026-08-23 17:36 UTC | 1h 19m |
| N560RW |  | Telluride Regional Airport (KTEX) | Telluride Regional Airport (KTEX) | 2026-08-23 17:20 UTC | 2026-08-23 17:35 UTC | 15m |
| N8224K |  | Chino Airport (KCNO) | Riverside Airport (KRAL) | 2026-08-23 17:15 UTC | 2026-08-23 17:34 UTC | 18m |
| TRF509 | TRF | Addison Airport (KADS) | Klutts Field (20XS) | 2026-08-23 16:59 UTC | 2026-08-23 17:31 UTC | 32m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-23 17:13 UTC | 2026-08-23 17:31 UTC | 18m |
| JIA5526 | JIA | Charlotte/Douglas International Airport (KCLT) | Pensacola International Airport (KPNS) | 2026-08-23 16:16 UTC | 2026-08-23 17:30 UTC | 1h 13m |
| SWR2EZ | Swiss International | Geneva Cointrin International Airport (LSGG) | Zurich Airport (LSZH) | 2026-08-23 16:56 UTC | 2026-08-23 17:28 UTC | 31m |
| N208MF |  | Chicago Executive Airport (KPWK) | NM67 (NM67) | 2026-08-23 15:21 UTC | 2026-08-23 17:26 UTC | 2h 5m |
| N80945 |  | Talkeetna Village Strip (AK44) | Helio Airport (2AK7) | 2026-08-23 16:56 UTC | 2026-08-23 17:26 UTC | 30m |
| AAL76 | American Airlines | John F Kennedy International Airport (KJFK) | San Francisco International Airport (KSFO) | 2026-08-23 11:43 UTC | 2026-08-23 17:25 UTC | 5h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
