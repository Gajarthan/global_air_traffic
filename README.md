# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_13:56:55_UTC-green)

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

**Latest saved flight:** 2026-08-24 13:56:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 13:56:55 UTC

- **231,933** saved flights
- **71,370** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,933** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,796,938.8 tonnes** estimated CO2 emissions
- **162,141,381 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9316 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4473 |
| 4 | IndiGo | 3932 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3576 |
| 7 | Delta Air Lines | 2960 |
| 8 | ENY | 2819 |
| 9 | LATAM Airlines | 2231 |
| 10 | AZU | 2154 |
| 11 | Vueling | 1984 |
| 12 | Lufthansa | 1891 |
| 13 | WIF | 1838 |
| 14 | LXJ | 1825 |
| 15 | easyJet | 1626 |
| 16 | Swiss International | 1552 |
| 17 | AXM | 1551 |
| 18 | EJU | 1486 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1471 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1386 |
| 23 | GLO | 1291 |
| 24 | WMT | 1284 |
| 25 | VIV | 1272 |
| 26 | PGT | 1267 |
| 27 | Air France | 1260 |
| 28 | Wizz Air | 1225 |
| 29 | AEE | 1156 |
| 30 | JetBlue | 1153 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192968 |
| 2 | 🇪🇸 ES | 14896 |
| 3 | 🇧🇷 BR | 13546 |
| 4 | 🇦🇺 AU | 13162 |
| 5 | 🇨🇦 CA | 12765 |
| 6 | 🇮🇹 IT | 12621 |
| 7 | 🇮🇳 IN | 12247 |
| 8 | 🇩🇪 DE | 11438 |
| 9 | 🇬🇧 GB | 10953 |
| 10 | 🇨🇴 CO | 9632 |
| 11 | 🇯🇵 JP | 9446 |
| 12 | 🇫🇷 FR | 9287 |
| 13 | 🇹🇷 TR | 6858 |
| 14 | 🇬🇷 GR | 6833 |
| 15 | 🇲🇽 MX | 6435 |
| 16 | 🇨🇭 CH | 6188 |
| 17 | 🇳🇴 NO | 5726 |
| 18 | 🇲🇾 MY | 4142 |
| 19 | 🇹🇭 TH | 4101 |
| 20 | 🇿🇦 ZA | 4059 |
| 21 | 🇵🇱 PL | 3856 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3184 |
| 24 | 🇬🇹 GT | 2909 |
| 25 | 🇰🇷 KR | 2726 |
| 26 | 🇭🇷 HR | 2670 |
| 27 | 🇲🇦 MA | 2354 |
| 28 | 🇲🇪 ME | 2136 |
| 29 | 🇳🇱 NL | 2081 |
| 30 | 🇮🇩 ID | 2015 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2835 |
| 4 | Tokyo International Airport |  | JP | 2818 |
| 5 | Guaymaral Airport |  | CO | 2658 |
| 6 | Harry Reid International Airport |  | US | 2495 |
| 7 | Zurich Airport |  | CH | 2423 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2365 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2333 |
| 10 | La Aurora Airport |  | GT | 2215 |
| 11 | El Dorado International Airport |  | CO | 2149 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1976 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1851 |
| 17 | Capua Airport |  | IT | 1822 |
| 18 | Madrid Barajas International Airport |  | ES | 1821 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1744 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1720 |
| 21 | Malpensa International Airport |  | IT | 1665 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1657 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1610 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1533 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1498 |
| 29 | Barcelona International Airport |  | ES | 1464 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1401 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1397 |
| 32 | Viracopos International Airport |  | BR | 1377 |
| 33 | Bengaluru International Airport |  | IN | 1370 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1339 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1299 |
| 39 | O. R. Tambo International Airport |  | ZA | 1261 |
| 40 | Vitoria/Foronda Airport |  | ES | 1258 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1078 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 846 | 21m | 244 km | 3,562.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 586 | 1h 6m | 770 km | 7,784.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 567 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 382 | 27m | 275 km | 1,810.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 359 | 1h 50m | 1,423 km | 8,810.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 358 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 337 | 44m | 241 km | 1,399.8 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 307 | 24m | 218 km | 1,156.6 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 302 | 1h 38m | 1,156 km | 6,024.8 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 288 | 19m | 99 km | 493.3 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 283 | 27m | 215 km | 1,048.1 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 268 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 264 | 19m | 144 km | 656.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 251 | 15m | 154 km | 665.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N552MD |  | Roberts Field/Redmond Municipal Airport (KRDM) | Madras Municipal Airport (KS33) | 2026-08-24 13:23 UTC | 2026-08-24 13:56 UTC | 33m |
| TVF99SL | TVF | Paris-Orly Airport (LFPO) | Radomir Dolni Rakovets Airfield (LB13) | 2026-08-24 11:44 UTC | 2026-08-24 13:56 UTC | 2h 11m |
| SXS9ZL | SXS | Adana Airport (LTAF) | Isparta Airport (LTBM) | 2026-08-24 13:16 UTC | 2026-08-24 13:51 UTC | 34m |
| N737TY |  | Mckinney Ntl Airport (KTKI) | TA22 (TA22) | 2026-08-24 13:22 UTC | 2026-08-24 13:50 UTC | 27m |
| ANA811 | All Nippon Airways | Narita International Airport (RJAA) | Zhuhai Airport (ZGSD) | 2026-08-24 10:05 UTC | 2026-08-24 13:49 UTC | 3h 43m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-24 13:35 UTC | 2026-08-24 13:49 UTC | 13m |
| CXK676 | CXK | Indy South Greenwood Airport (KHFY) | Purdue University Airport (KLAF) | 2026-08-24 13:02 UTC | 2026-08-24 13:48 UTC | 45m |
| N824RN |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-24 13:02 UTC | 2026-08-24 13:47 UTC | 44m |
| N600BM |  | Kearney Regional Airport (KEAR) | Lincoln Airport (KLNK) | 2026-08-24 13:22 UTC | 2026-08-24 13:46 UTC | 24m |
| CXK523 | CXK | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-24 13:24 UTC | 2026-08-24 13:43 UTC | 19m |
| RN162 |  | J-22 Ranch Airport (16FL) | Brewton Municipal Airport (K12J) | 2026-08-24 12:47 UTC | 2026-08-24 13:42 UTC | 55m |
| OM1010 |  | Schanis Airport (LSZX) | Samedan Airport (LSZS) | 2026-08-24 12:13 UTC | 2026-08-24 13:40 UTC | 1h 26m |
| N33SU |  | UT80 (UT80) | General Dick Stout Field (K1L8) | 2026-08-24 13:27 UTC | 2026-08-24 13:39 UTC | 11m |
| N261PJ |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-24 12:57 UTC | 2026-08-24 13:36 UTC | 39m |
| NAF298A | NAF | Laupheim Airport (ETHL) | Hoefen Airport (LOIR) | 2026-08-24 12:34 UTC | 2026-08-24 13:36 UTC | 1h 1m |
| CSN392 | China Southern | VGZR (VGZR) | Khrabrovo Airport (UMKK) | 2026-08-23 17:29 UTC | 2026-08-24 13:33 UTC | 20h 4m |
| FHOKE | FHO | Lille/Marcq-en-Baroeul Airport (LFQO) | Lille/Marcq-en-Baroeul Airport (LFQO) | 2026-08-24 13:12 UTC | 2026-08-24 13:33 UTC | 20m |
| A6FTT |  | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-24 13:02 UTC | 2026-08-24 13:31 UTC | 28m |
| ARCTS01 | ARC | Wunstorf Airport (ETNW) | Nordholz Airport (ETMN) | 2026-08-24 12:34 UTC | 2026-08-24 13:24 UTC | 49m |
| EXCEL01 | EXC | 2TX3 (2TX3) | TA29 (TA29) | 2026-08-24 13:14 UTC | 2026-08-24 13:22 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
