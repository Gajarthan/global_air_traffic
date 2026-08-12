# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_13:33:03_UTC-green)

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

**Latest saved flight:** 2026-08-12 13:33:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 13:33:03 UTC

- **189,327** saved flights
- **59,849** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **189,327** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,268,154.9 tonnes** estimated CO2 emissions
- **131,487,240 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7511 |
| 2 | SkyWest Airlines | 6863 |
| 3 | EJA | 3727 |
| 4 | IndiGo | 3297 |
| 5 | Southwest Airlines | 2957 |
| 6 | American Airlines | 2935 |
| 7 | ENY | 2344 |
| 8 | Delta Air Lines | 2221 |
| 9 | LATAM Airlines | 1767 |
| 10 | AZU | 1703 |
| 11 | Lufthansa | 1654 |
| 12 | Vueling | 1574 |
| 13 | WIF | 1570 |
| 14 | LXJ | 1478 |
| 15 | easyJet | 1305 |
| 16 | Swiss International | 1291 |
| 17 | AXM | 1253 |
| 18 | QLK | 1168 |
| 19 | EJU | 1166 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1045 |
| 23 | GLO | 1017 |
| 24 | Air France | 987 |
| 25 | PGT | 977 |
| 26 | AEE | 972 |
| 27 | United Airlines | 971 |
| 28 | CXK | 967 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 939 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161296 |
| 2 | 🇪🇸 ES | 12214 |
| 3 | 🇧🇷 BR | 10853 |
| 4 | 🇦🇺 AU | 10650 |
| 5 | 🇨🇦 CA | 10345 |
| 6 | 🇮🇳 IN | 10340 |
| 7 | 🇮🇹 IT | 9819 |
| 8 | 🇩🇪 DE | 9361 |
| 9 | 🇬🇧 GB | 8812 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7572 |
| 12 | 🇨🇴 CO | 7203 |
| 13 | 🇬🇷 GR | 5548 |
| 14 | 🇲🇽 MX | 5383 |
| 15 | 🇨🇭 CH | 5083 |
| 16 | 🇹🇷 TR | 5029 |
| 17 | 🇳🇴 NO | 4875 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3180 |
| 20 | 🇵🇱 PL | 3134 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2506 |
| 24 | 🇬🇹 GT | 2401 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1927 |
| 27 | 🇲🇦 MA | 1924 |
| 28 | 🇳🇱 NL | 1691 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3924 |
| 2 | Denver International Airport |  | US | 3116 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Indira Gandhi International Airport |  | IN | 2330 |
| 5 | Guaymaral Airport |  | CO | 2320 |
| 6 | Harry Reid International Airport |  | US | 2212 |
| 7 | Zurich Airport |  | CH | 2013 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2007 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1956 |
| 10 | La Aurora Airport |  | GT | 1845 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1714 |
| 12 | El Dorado International Airport |  | CO | 1703 |
| 13 | Salt Lake City International Airport |  | US | 1681 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1623 |
| 16 | Congonhas Airport |  | BR | 1577 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1492 |
| 19 | Capua Airport |  | IT | 1473 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1469 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1398 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1354 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1323 |
| 24 | Malpensa International Airport |  | IT | 1304 |
| 25 | Charles de Gaulle International Airport |  | FR | 1295 |
| 26 | Charlotte/Douglas International Airport |  | US | 1265 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1220 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1184 |
| 30 | Ninoy Aquino International Airport |  | PH | 1184 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1161 |
| 32 | Barcelona International Airport |  | ES | 1136 |
| 33 | Reno/Tahoe International Airport |  | US | 1094 |
| 34 | Viracopos International Airport |  | BR | 1093 |
| 35 | Seattle-Tacoma International Airport |  | US | 1090 |
| 36 | Calgary International Airport |  | CA | 1077 |
| 37 | Daniel K Inouye International Airport |  | US | 1065 |
| 38 | Oslo Gardermoen Airport |  | NO | 1057 |
| 39 | Tenerife Norte Airport |  | ES | 1041 |
| 40 | Vitoria/Foronda Airport |  | ES | 1027 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 956 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 693 | 21m | 244 km | 2,918.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 440 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 317 | 27m | 275 km | 1,502.1 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 308 | 14m | 114 km | 604.1 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 287 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 273 | 22m | 55 km | 259.5 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 272 | 1h 49m | 1,423 km | 6,675.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 252 | 20m | 250 km | 1,088.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 236 | 27m | 215 km | 874.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 236 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 230 | 1h 15m | 961 km | 3,812.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 226 | 19m | 144 km | 562.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 223 | 24m | 218 km | 840.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 206 | 1h 48m | 1,304 km | 4,634.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N36393 |  | Tweed/New Haven Airport (KHVN) | Chester Airport (KSNC) | 2026-08-12 13:19 UTC | 2026-08-12 13:33 UTC | 13m |
| N3563Q |  | Schaumburg Regional Airport (K06C) | Schaumburg Regional Airport (K06C) | 2026-08-12 12:34 UTC | 2026-08-12 13:31 UTC | 57m |
| OKIDA | OKI | Gera-Leumnitz Airport (EDAJ) | Jicin Airport (LKJC) | 2026-08-12 12:27 UTC | 2026-08-12 13:28 UTC | 1h 1m |
| N739TS |  | Mckinney Ntl Airport (KTKI) | 52TA (52TA) | 2026-08-12 12:53 UTC | 2026-08-12 13:27 UTC | 34m |
| RTY690 | RTY | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-08-12 12:55 UTC | 2026-08-12 13:27 UTC | 31m |
| N1103S |  | Newport State Airport (KUUU) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-12 12:58 UTC | 2026-08-12 13:25 UTC | 27m |
| N52522 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-12 12:03 UTC | 2026-08-12 13:25 UTC | 1h 22m |
| N749DS |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-12 12:37 UTC | 2026-08-12 13:24 UTC | 47m |
| N6338F |  | Sky Manor Airport (KN40) | Doylestown Airport (KDYL) | 2026-08-12 13:12 UTC | 2026-08-12 13:24 UTC | 12m |
| SCA42 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-08-12 13:11 UTC | 2026-08-12 13:23 UTC | 12m |
| ERU820 | ERU | Daytona Beach International Airport (KDAB) | North Exuma Airport (85FA) | 2026-08-12 13:03 UTC | 2026-08-12 13:22 UTC | 18m |
| ARCAS07 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-08-12 13:05 UTC | 2026-08-12 13:21 UTC | 15m |
| N701BP |  | Denton Enterprise Airport (KDTO) | Bass Aero Airport (OK17) | 2026-08-12 12:45 UTC | 2026-08-12 13:14 UTC | 29m |
| WIF69D | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-12 12:33 UTC | 2026-08-12 13:11 UTC | 37m |
| N14C |  | Deland Municipal-Sidney H Taylor Field (KDED) | Arthur Dunn Air Park (KX21) | 2026-08-12 12:45 UTC | 2026-08-12 13:08 UTC | 23m |
| TGNLA | TGN | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-08-12 12:41 UTC | 2026-08-12 13:08 UTC | 26m |
| SPUTF | SPU | Zielona Góra-Babimost Airport (EPZG) | EPZB (EPZB) | 2026-08-12 12:44 UTC | 2026-08-12 13:06 UTC | 22m |
| N56319 |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 2026-08-12 12:58 UTC | 2026-08-12 13:03 UTC | 4m |
| N6338F |  | Princeton Airport (K39N) | Sky Manor Airport (KN40) | 2026-08-12 12:49 UTC | 2026-08-12 13:02 UTC | 12m |
| N5166Y |  | Mckinney Ntl Airport (KTKI) | J Ranch Airport (41TX) | 2026-08-12 12:29 UTC | 2026-08-12 13:00 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
