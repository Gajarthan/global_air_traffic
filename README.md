# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_18:04:08_UTC-green)

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

**Latest saved flight:** 2026-08-25 18:04:08 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 18:04:08 UTC

- **236,040** saved flights
- **72,127** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **236,040** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,842,306.2 tonnes** estimated CO2 emissions
- **164,771,375 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9466 |
| 2 | SkyWest Airlines | 8325 |
| 3 | EJA | 4578 |
| 4 | IndiGo | 3984 |
| 5 | American Airlines | 3831 |
| 6 | Southwest Airlines | 3601 |
| 7 | Delta Air Lines | 3004 |
| 8 | ENY | 2866 |
| 9 | LATAM Airlines | 2265 |
| 10 | AZU | 2197 |
| 11 | Vueling | 2022 |
| 12 | Lufthansa | 1918 |
| 13 | WIF | 1878 |
| 14 | LXJ | 1847 |
| 15 | easyJet | 1647 |
| 16 | Swiss International | 1586 |
| 17 | AXM | 1575 |
| 18 | EJU | 1514 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1490 |
| 21 | Alaska Airlines | 1418 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1318 |
| 24 | GLO | 1314 |
| 25 | VIV | 1301 |
| 26 | PGT | 1288 |
| 27 | Air France | 1283 |
| 28 | Wizz Air | 1261 |
| 29 | AEE | 1173 |
| 30 | JetBlue | 1170 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 196016 |
| 2 | 🇪🇸 ES | 15175 |
| 3 | 🇧🇷 BR | 13772 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13051 |
| 6 | 🇮🇹 IT | 12878 |
| 7 | 🇮🇳 IN | 12412 |
| 8 | 🇩🇪 DE | 11647 |
| 9 | 🇬🇧 GB | 11140 |
| 10 | 🇨🇴 CO | 9993 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9486 |
| 13 | 🇹🇷 TR | 7008 |
| 14 | 🇬🇷 GR | 6959 |
| 15 | 🇲🇽 MX | 6553 |
| 16 | 🇨🇭 CH | 6312 |
| 17 | 🇳🇴 NO | 5855 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4145 |
| 21 | 🇵🇱 PL | 3939 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2955 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2718 |
| 27 | 🇲🇦 MA | 2391 |
| 28 | 🇲🇪 ME | 2196 |
| 29 | 🇳🇱 NL | 2121 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4896 |
| 2 | Denver International Airport |  | US | 3814 |
| 3 | Indira Gandhi International Airport |  | IN | 2881 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2685 |
| 6 | Harry Reid International Airport |  | US | 2524 |
| 7 | Zurich Airport |  | CH | 2475 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2412 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2364 |
| 10 | La Aurora Airport |  | GT | 2253 |
| 11 | El Dorado International Airport |  | CO | 2239 |
| 12 | Chicago O'Hare International Airport |  | US | 2127 |
| 13 | Salt Lake City International Airport |  | US | 2077 |
| 14 | Congonhas Airport |  | BR | 2010 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1977 |
| 16 | Frankfurt am Main International Airport |  | DE | 1878 |
| 17 | Capua Airport |  | IT | 1855 |
| 18 | Madrid Barajas International Airport |  | ES | 1854 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1774 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1741 |
| 21 | Malpensa International Airport |  | IT | 1690 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1672 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1645 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1523 |
| 29 | Barcelona International Airport |  | ES | 1491 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1473 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1427 |
| 32 | Viracopos International Airport |  | BR | 1406 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1382 |
| 35 | Seattle-Tacoma International Airport |  | US | 1381 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1348 |
| 38 | Oslo Gardermoen Airport |  | NO | 1325 |
| 39 | O. R. Tambo International Airport |  | ZA | 1288 |
| 40 | Vancouver International Airport |  | CA | 1288 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 866 | 21m | 244 km | 3,646.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 597 | 8m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 529 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 367 | 1h 50m | 1,423 km | 9,006.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 334 | 21m | 250 km | 1,442.7 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 312 | 1h 40m | 1,156 km | 6,224.3 t |
| 16 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 311 | 22m | 55 km | 295.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 252 | 1h 50m | 1,304 km | 5,669.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N627RG |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-08-25 17:29 UTC | 2026-08-25 18:04 UTC | 34m |
| TIBBI | TIB | Tobias Bolanos International Airport (MRPV) | Juan Santamaria International Airport (MROC) | 2026-08-25 17:35 UTC | 2026-08-25 17:57 UTC | 21m |
| N729EL |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-25 17:42 UTC | 2026-08-25 17:53 UTC | 11m |
| N6812W |  | Merritt Airport (CAD5) | Quilchena Airport (CBT6) | 2026-08-25 17:36 UTC | 2026-08-25 17:51 UTC | 15m |
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-08-25 17:33 UTC | 2026-08-25 17:51 UTC | 17m |
| FSF304A | FSF | Bologna / Borgo Panigale Airport (LIPE) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-25 16:44 UTC | 2026-08-25 17:51 UTC | 1h 7m |
| N260FL |  | Trenton Mercer Airport (KTTN) | Ocean County Airport (KMJX) | 2026-08-25 17:05 UTC | 2026-08-25 17:48 UTC | 42m |
| N280C |  | Erie-Ottawa International Airport (KPCW) | Tweed/New Haven Airport (KHVN) | 2026-08-25 16:36 UTC | 2026-08-25 17:47 UTC | 1h 10m |
| LIFE7 | LIF | West Houston Airport (KIWS) | Houston/Southwest Airport (KAXH) | 2026-08-25 17:40 UTC | 2026-08-25 17:45 UTC | 5m |
| TROIKA9 | TRO | Bertani Ranch Airport (23TS) | Rio Vista Ranch Airport (TS04) | 2026-08-25 17:33 UTC | 2026-08-25 17:45 UTC | 11m |
| RFS732 | RFS | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-25 17:28 UTC | 2026-08-25 17:43 UTC | 14m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-25 17:24 UTC | 2026-08-25 17:42 UTC | 18m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-25 17:28 UTC | 2026-08-25 17:42 UTC | 13m |
| AATK309 | AAT | Provo Municipal Airport (KPVU) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 15:31 UTC | 2026-08-25 17:41 UTC | 2h 9m |
| USC32 | USC | Bob Hope Airport (KBUR) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-25 16:48 UTC | 2026-08-25 17:38 UTC | 50m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 17:26 UTC | 2026-08-25 17:38 UTC | 11m |
| TKR855 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 17:24 UTC | 2026-08-25 17:35 UTC | 11m |
| MLDYS | MLD | Nice-Cote d'Azur Airport (LFMN) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-25 17:29 UTC | 2026-08-25 17:35 UTC | 5m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 17:24 UTC | 2026-08-25 17:35 UTC | 11m |
| N550HJ |  | 4II2 (4II2) | Indianapolis Regional Airport (KMQJ) | 2026-08-25 17:17 UTC | 2026-08-25 17:34 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
