# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_20:03:37_UTC-green)

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

**Latest saved flight:** 2026-08-17 20:03:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 20:03:37 UTC

- **209,809** saved flights
- **66,810** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,809** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,522,744.6 tonnes** estimated CO2 emissions
- **146,246,065 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8307 |
| 2 | SkyWest Airlines | 7539 |
| 3 | EJA | 4090 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3506 |
| 6 | Southwest Airlines | 3374 |
| 7 | Delta Air Lines | 2715 |
| 8 | ENY | 2614 |
| 9 | LATAM Airlines | 1977 |
| 10 | AZU | 1900 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1747 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1656 |
| 15 | easyJet | 1457 |
| 16 | Swiss International | 1402 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1331 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1290 |
| 21 | EJU | 1283 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1156 |
| 24 | GLO | 1136 |
| 25 | Air France | 1133 |
| 26 | PGT | 1122 |
| 27 | JetBlue | 1071 |
| 28 | AEE | 1068 |
| 29 | WMT | 1065 |
| 30 | Wizz Air | 1041 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177789 |
| 2 | 🇪🇸 ES | 13433 |
| 3 | 🇧🇷 BR | 12042 |
| 4 | 🇦🇺 AU | 11751 |
| 5 | 🇨🇦 CA | 11592 |
| 6 | 🇮🇳 IN | 11156 |
| 7 | 🇮🇹 IT | 10983 |
| 8 | 🇩🇪 DE | 10370 |
| 9 | 🇬🇧 GB | 9796 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8389 |
| 12 | 🇫🇷 FR | 8339 |
| 13 | 🇬🇷 GR | 6173 |
| 14 | 🇹🇷 TR | 5978 |
| 15 | 🇲🇽 MX | 5896 |
| 16 | 🇨🇭 CH | 5581 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3468 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2696 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2258 |
| 27 | 🇲🇦 MA | 2118 |
| 28 | 🇳🇱 NL | 1872 |
| 29 | 🇲🇪 ME | 1787 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4406 |
| 2 | Denver International Airport |  | US | 3426 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2539 |
| 5 | Guaymaral Airport |  | CO | 2524 |
| 6 | Harry Reid International Airport |  | US | 2359 |
| 7 | Zurich Airport |  | CH | 2189 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2180 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2173 |
| 10 | La Aurora Airport |  | GT | 2050 |
| 11 | Chicago O'Hare International Airport |  | US | 1944 |
| 12 | El Dorado International Airport |  | CO | 1913 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1870 |
| 14 | Salt Lake City International Airport |  | US | 1858 |
| 15 | Congonhas Airport |  | BR | 1752 |
| 16 | Frankfurt am Main International Airport |  | DE | 1721 |
| 17 | Madrid Barajas International Airport |  | ES | 1643 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1592 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 20 | Capua Airport |  | IT | 1583 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1530 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1452 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1421 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1298 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1270 |
| 32 | Barcelona International Airport |  | ES | 1259 |
| 33 | Seattle-Tacoma International Airport |  | US | 1243 |
| 34 | Viracopos International Airport |  | BR | 1218 |
| 35 | Calgary International Airport |  | CA | 1188 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1156 |
| 38 | Reno/Tahoe International Airport |  | US | 1148 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1132 |
| 40 | Don Mueang International Airport |  | TH | 1114 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1037 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 739 | 21m | 244 km | 3,111.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 477 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 422 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 250 | 1h 37m | 1,156 km | 4,987.4 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 225 | 1h 49m | 1,304 km | 5,061.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CAP433 | CAP | Chino Airport (KCNO) | Santa Monica Municipal Airport (KSMO) | 2026-08-17 19:34 UTC | 2026-08-17 20:03 UTC | 28m |
| CGJDB | CGJ | St-Mathieu-De-Beloeil Airport (CSB3) | St-Mathieu-De-Beloeil Airport (CSB3) | 2026-08-17 19:35 UTC | 2026-08-17 20:02 UTC | 27m |
| N15AN |  | Dubuque Regional Airport (KDBQ) | 01IA (01IA) | 2026-08-17 19:27 UTC | 2026-08-17 19:53 UTC | 26m |
| CGNSS | CGN | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-17 19:26 UTC | 2026-08-17 19:49 UTC | 23m |
| N234FF |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-17 19:19 UTC | 2026-08-17 19:49 UTC | 29m |
| N5043J |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-08-17 19:08 UTC | 2026-08-17 19:48 UTC | 40m |
| N608HG |  | North Perry Airport (KHWO) | Palm Beach County Park Airport (KLNA) | 2026-08-17 19:04 UTC | 2026-08-17 19:45 UTC | 41m |
| RYS3061 | RYS | Katowice International Airport (EPKT) | Aktion National Airport (LGPZ) | 2026-08-17 18:02 UTC | 2026-08-17 19:45 UTC | 1h 42m |
| N13394 |  | Harford County Airport (K0W3) | Harford County Airport (K0W3) | 2026-08-17 18:57 UTC | 2026-08-17 19:45 UTC | 47m |
| TAUNT11 | TAU | 75OK (75OK) | Kegelman Af Aux Field (KCKA) | 2026-08-17 19:26 UTC | 2026-08-17 19:44 UTC | 17m |
| N565DS |  | Centennial Airport (KAPA) | Rocky Mountain Metro Airport (KBJC) | 2026-08-17 19:04 UTC | 2026-08-17 19:42 UTC | 37m |
| TKR16 | TKR | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-08-17 19:28 UTC | 2026-08-17 19:40 UTC | 12m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-17 19:04 UTC | 2026-08-17 19:40 UTC | 35m |
| ERU838 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-08-17 19:25 UTC | 2026-08-17 19:39 UTC | 13m |
| RENO71 | REN | Enix Airport (OK51) | Lariat Ranch Airport (OK42) | 2026-08-17 19:10 UTC | 2026-08-17 19:37 UTC | 27m |
| N47448 |  | Block Island State Airport (KBID) | Teterboro Airport (KTEB) | 2026-08-17 18:43 UTC | 2026-08-17 19:36 UTC | 52m |
| BLINR17 | BLI | H Bar H Airport (NV09) | Travis Afb Airport (KSUU) | 2026-08-17 18:17 UTC | 2026-08-17 19:35 UTC | 1h 18m |
| PLF693 | PLF | Oksywie Military Air Base (EPOK) | Oksywie Military Air Base (EPOK) | 2026-08-17 18:53 UTC | 2026-08-17 19:35 UTC | 41m |
| TGCYE | TGC | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-08-17 19:05 UTC | 2026-08-17 19:34 UTC | 28m |
| N522RK |  | Scottsdale Airport (KSDL) | Rimrock Airport (48AZ) | 2026-08-17 19:03 UTC | 2026-08-17 19:32 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
