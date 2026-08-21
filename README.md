# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_14:32:29_UTC-green)

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

**Latest saved flight:** 2026-08-21 14:32:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 14:32:29 UTC

- **222,294** saved flights
- **69,525** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **222,294** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,676,766.6 tonnes** estimated CO2 emissions
- **155,174,876 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8915 |
| 2 | SkyWest Airlines | 7892 |
| 3 | EJA | 4291 |
| 4 | IndiGo | 3772 |
| 5 | American Airlines | 3672 |
| 6 | Southwest Airlines | 3491 |
| 7 | Delta Air Lines | 2853 |
| 8 | ENY | 2725 |
| 9 | LATAM Airlines | 2116 |
| 10 | AZU | 2041 |
| 11 | Vueling | 1873 |
| 12 | Lufthansa | 1840 |
| 13 | WIF | 1781 |
| 14 | LXJ | 1746 |
| 15 | easyJet | 1540 |
| 16 | Swiss International | 1479 |
| 17 | AXM | 1466 |
| 18 | QLK | 1405 |
| 19 | EJU | 1392 |
| 20 | United Airlines | 1392 |
| 21 | Alaska Airlines | 1353 |
| 22 | All Nippon Airways | 1332 |
| 23 | PGT | 1219 |
| 24 | GLO | 1215 |
| 25 | VIV | 1209 |
| 26 | Air France | 1205 |
| 27 | WMT | 1184 |
| 28 | Wizz Air | 1142 |
| 29 | JetBlue | 1119 |
| 30 | AEE | 1110 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 186493 |
| 2 | 🇪🇸 ES | 14247 |
| 3 | 🇧🇷 BR | 12853 |
| 4 | 🇦🇺 AU | 12651 |
| 5 | 🇨🇦 CA | 12266 |
| 6 | 🇮🇹 IT | 11849 |
| 7 | 🇮🇳 IN | 11766 |
| 8 | 🇩🇪 DE | 10975 |
| 9 | 🇬🇧 GB | 10434 |
| 10 | 🇨🇴 CO | 9139 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8863 |
| 13 | 🇬🇷 GR | 6492 |
| 14 | 🇹🇷 TR | 6450 |
| 15 | 🇲🇽 MX | 6165 |
| 16 | 🇨🇭 CH | 5861 |
| 17 | 🇳🇴 NO | 5537 |
| 18 | 🇲🇾 MY | 3885 |
| 19 | 🇿🇦 ZA | 3831 |
| 20 | 🇹🇭 TH | 3770 |
| 21 | 🇵🇱 PL | 3691 |
| 22 | 🇳🇿 NZ | 3089 |
| 23 | 🇵🇭 PH | 3016 |
| 24 | 🇬🇹 GT | 2802 |
| 25 | 🇰🇷 KR | 2656 |
| 26 | 🇭🇷 HR | 2483 |
| 27 | 🇲🇦 MA | 2238 |
| 28 | 🇲🇪 ME | 1976 |
| 29 | 🇳🇱 NL | 1973 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4650 |
| 2 | Denver International Airport |  | US | 3618 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2703 |
| 5 | Guaymaral Airport |  | CO | 2612 |
| 6 | Harry Reid International Airport |  | US | 2445 |
| 7 | Zurich Airport |  | CH | 2304 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2276 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2257 |
| 10 | La Aurora Airport |  | GT | 2134 |
| 11 | El Dorado International Airport |  | CO | 2077 |
| 12 | Chicago O'Hare International Airport |  | US | 2026 |
| 13 | Salt Lake City International Airport |  | US | 1949 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1910 |
| 15 | Congonhas Airport |  | BR | 1877 |
| 16 | Frankfurt am Main International Airport |  | DE | 1804 |
| 17 | Madrid Barajas International Airport |  | ES | 1739 |
| 18 | Capua Airport |  | IT | 1698 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1662 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1639 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1625 |
| 22 | Macau International Airport |  | MO | 1588 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1559 |
| 25 | Charles de Gaulle International Airport |  | FR | 1531 |
| 26 | Charlotte/Douglas International Airport |  | US | 1472 |
| 27 | Ninoy Aquino International Airport |  | PH | 1436 |
| 28 | Kuala Lumpur International Airport |  | MY | 1418 |
| 29 | Barcelona International Airport |  | ES | 1370 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1348 |
| 31 | Bengaluru International Airport |  | IN | 1332 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1316 |
| 33 | Seattle-Tacoma International Airport |  | US | 1313 |
| 34 | Viracopos International Airport |  | BR | 1306 |
| 35 | Calgary International Airport |  | CA | 1258 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1247 |
| 37 | Oslo Gardermoen Airport |  | NO | 1239 |
| 38 | Don Mueang International Airport |  | TH | 1238 |
| 39 | Vitoria/Foronda Airport |  | ES | 1233 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1193 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1067 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 801 | 21m | 244 km | 3,372.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 503 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 500 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 374 | 27m | 275 km | 1,772.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 351 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 330 | 1h 50m | 1,423 km | 8,098.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 325 | 44m | 241 km | 1,350.0 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 296 | 21m | 250 km | 1,278.5 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 280 | 1h 39m | 1,156 km | 5,585.9 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 277 | 24m | 218 km | 1,043.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 19 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 273 | 44m | 555 km | 2,614.1 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 273 | 19m | 99 km | 467.6 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 262 | 1h 14m | 961 km | 4,342.8 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 253 | 19m | 144 km | 629.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 241 | 1h 50m | 1,304 km | 5,421.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 233 | 28m | 152 km | 608.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1424V |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-08-21 13:41 UTC | 2026-08-21 14:32 UTC | 51m |
| N498SP |  | Monroe County Airport (KBMG) | Monroe County Airport (KBMG) | 2026-08-21 13:47 UTC | 2026-08-21 14:24 UTC | 36m |
| N4004M |  | Kissimmee Gateway Airport (KISM) | Gentry Airport (FD37) | 2026-08-21 13:52 UTC | 2026-08-21 14:24 UTC | 32m |
| N9161T |  | North Texas Regional/Perrin Field (KGYI) | Sandy Creek Ranch Airport (TX47) | 2026-08-21 13:54 UTC | 2026-08-21 14:22 UTC | 27m |
| AFL273 | AFL | Suvarnabhumi Airport (VTBS) | Bezymyanka Airfield (UWWG) | 2026-08-21 06:41 UTC | 2026-08-21 14:22 UTC | 7h 41m |
| N31192 |  | Caldwell Executive Airport (KEUL) | Caldwell Executive Airport (KEUL) | 2026-08-21 14:11 UTC | 2026-08-21 14:22 UTC | 10m |
| N345CJ |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-08-21 14:02 UTC | 2026-08-21 14:22 UTC | 19m |
| N827DB |  | Wauchula Municipal Airport (KCHN) | Wauchula Municipal Airport (KCHN) | 2026-08-21 14:08 UTC | 2026-08-21 14:21 UTC | 13m |
| N227SK |  | Dubuque Regional Airport (KDBQ) | Maquoketa Municipal Airport (KOQW) | 2026-08-21 13:49 UTC | 2026-08-21 14:20 UTC | 31m |
| GDVII | GDV | London City Airport (EGLC) | Farnborough Airport (EGLF) | 2026-08-21 14:03 UTC | 2026-08-21 14:19 UTC | 16m |
| WZZ824 | Wizz Air | Warsaw Chopin Airport (EPWA) | Malpensa International Airport (LIMC) | 2026-08-21 12:25 UTC | 2026-08-21 14:19 UTC | 1h 54m |
| N374BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-08-21 13:08 UTC | 2026-08-21 14:18 UTC | 1h 10m |
| CONGO63 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-21 13:57 UTC | 2026-08-21 14:13 UTC | 16m |
| ABD5014 | ABD | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-08-20 20:43 UTC | 2026-08-21 14:12 UTC | 17h 29m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Consort Airport (CFG3) | 2026-08-21 13:35 UTC | 2026-08-21 14:08 UTC | 32m |
| GLO2095 | GLO | Viracopos International Airport (SBKP) | Marica Airport (SDMC) | 2026-08-21 13:19 UTC | 2026-08-21 14:07 UTC | 48m |
| N808W |  | Rocky Mountain Metro Airport (KBJC) | Mc Elroy Airfield (K20V) | 2026-08-21 13:55 UTC | 2026-08-21 14:06 UTC | 11m |
| CXK505 | CXK | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-21 13:51 UTC | 2026-08-21 14:05 UTC | 14m |
| N6642J |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-08-21 13:07 UTC | 2026-08-21 14:04 UTC | 57m |
| N43813 |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-21 13:56 UTC | 2026-08-21 14:03 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
