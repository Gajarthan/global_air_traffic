# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_18:05:42_UTC-green)

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

**Latest saved flight:** 2026-08-18 18:05:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-18 18:05:42 UTC

- **212,857** saved flights
- **67,397** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **212,857** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,559,010.2 tonnes** estimated CO2 emissions
- **148,348,417 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8441 |
| 2 | SkyWest Airlines | 7625 |
| 3 | EJA | 4142 |
| 4 | IndiGo | 3643 |
| 5 | American Airlines | 3549 |
| 6 | Southwest Airlines | 3394 |
| 7 | Delta Air Lines | 2743 |
| 8 | ENY | 2639 |
| 9 | LATAM Airlines | 2006 |
| 10 | AZU | 1936 |
| 11 | Lufthansa | 1784 |
| 12 | Vueling | 1779 |
| 13 | WIF | 1709 |
| 14 | LXJ | 1680 |
| 15 | easyJet | 1478 |
| 16 | Swiss International | 1427 |
| 17 | AXM | 1391 |
| 18 | United Airlines | 1346 |
| 19 | QLK | 1320 |
| 20 | EJU | 1310 |
| 21 | Alaska Airlines | 1305 |
| 22 | All Nippon Airways | 1286 |
| 23 | VIV | 1171 |
| 24 | GLO | 1153 |
| 25 | PGT | 1153 |
| 26 | Air France | 1149 |
| 27 | WMT | 1095 |
| 28 | JetBlue | 1086 |
| 29 | AEE | 1075 |
| 30 | Wizz Air | 1062 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 179790 |
| 2 | 🇪🇸 ES | 13638 |
| 3 | 🇧🇷 BR | 12222 |
| 4 | 🇦🇺 AU | 11964 |
| 5 | 🇨🇦 CA | 11753 |
| 6 | 🇮🇳 IN | 11353 |
| 7 | 🇮🇹 IT | 11213 |
| 8 | 🇩🇪 DE | 10526 |
| 9 | 🇬🇧 GB | 9932 |
| 10 | 🇯🇵 JP | 8782 |
| 11 | 🇨🇴 CO | 8609 |
| 12 | 🇫🇷 FR | 8464 |
| 13 | 🇬🇷 GR | 6235 |
| 14 | 🇹🇷 TR | 6111 |
| 15 | 🇲🇽 MX | 5964 |
| 16 | 🇨🇭 CH | 5649 |
| 17 | 🇳🇴 NO | 5300 |
| 18 | 🇲🇾 MY | 3674 |
| 19 | 🇿🇦 ZA | 3604 |
| 20 | 🇵🇱 PL | 3513 |
| 21 | 🇹🇭 TH | 3449 |
| 22 | 🇳🇿 NZ | 2945 |
| 23 | 🇵🇭 PH | 2829 |
| 24 | 🇬🇹 GT | 2722 |
| 25 | 🇰🇷 KR | 2583 |
| 26 | 🇭🇷 HR | 2313 |
| 27 | 🇲🇦 MA | 2146 |
| 28 | 🇳🇱 NL | 1899 |
| 29 | 🇲🇪 ME | 1836 |
| 30 | 🇮🇩 ID | 1771 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4469 |
| 2 | Denver International Airport |  | US | 3471 |
| 3 | Tokyo International Airport |  | JP | 2633 |
| 4 | Indira Gandhi International Airport |  | IN | 2592 |
| 5 | Guaymaral Airport |  | CO | 2546 |
| 6 | Harry Reid International Airport |  | US | 2380 |
| 7 | Zurich Airport |  | CH | 2221 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2194 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2192 |
| 10 | La Aurora Airport |  | GT | 2069 |
| 11 | El Dorado International Airport |  | CO | 1966 |
| 12 | Chicago O'Hare International Airport |  | US | 1966 |
| 13 | Salt Lake City International Airport |  | US | 1881 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1876 |
| 15 | Congonhas Airport |  | BR | 1782 |
| 16 | Frankfurt am Main International Airport |  | DE | 1739 |
| 17 | Madrid Barajas International Airport |  | ES | 1666 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1608 |
| 19 | Capua Airport |  | IT | 1607 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1601 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1556 |
| 22 | Macau International Airport |  | MO | 1554 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1490 |
| 24 | Malpensa International Airport |  | IT | 1479 |
| 25 | Charles de Gaulle International Airport |  | FR | 1466 |
| 26 | Charlotte/Douglas International Airport |  | US | 1434 |
| 27 | Kuala Lumpur International Airport |  | MY | 1355 |
| 28 | Ninoy Aquino International Airport |  | PH | 1341 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1309 |
| 30 | Bengaluru International Airport |  | IN | 1304 |
| 31 | Barcelona International Airport |  | ES | 1289 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1282 |
| 33 | Seattle-Tacoma International Airport |  | US | 1263 |
| 34 | Viracopos International Airport |  | BR | 1237 |
| 35 | Calgary International Airport |  | CA | 1203 |
| 36 | Oslo Gardermoen Airport |  | NO | 1179 |
| 37 | Vitoria/Foronda Airport |  | ES | 1174 |
| 38 | Reno/Tahoe International Airport |  | US | 1155 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1148 |
| 40 | Don Mueang International Airport |  | TH | 1138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1042 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 757 | 21m | 244 km | 3,187.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 525 | 1h 7m | 770 km | 6,974.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 493 | 24m | 225 km | 1,912.6 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 481 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 448 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 353 | 27m | 275 km | 1,672.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 349 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 314 | 1h 49m | 1,423 km | 7,706.1 t |
| 10 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 311 | 44m | 241 km | 1,291.8 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 292 | 22m | 55 km | 277.5 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 280 | 21m | 250 km | 1,209.4 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 265 | 19m | 99 km | 453.9 t |
| 18 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 264 | 1h 38m | 1,156 km | 5,266.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 261 | 27m | 215 km | 966.6 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 252 | 1h 14m | 961 km | 4,177.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 251 | 19m | 165 km | 714.0 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 249 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 244 | 31m | 369 km | 1,553.1 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 244 | 19m | 144 km | 606.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 228 | 1h 49m | 1,304 km | 5,129.4 t |
| 30 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 223 | 44m | 555 km | 2,135.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7620U |  | Gerald R Ford International Airport (KGRR) | James M Cox Dayton International Airport (KDAY) | 2026-08-18 16:45 UTC | 2026-08-18 18:05 UTC | 1h 19m |
| N362SP |  | Clermont County Airport (KI69) | 1OA5 (1OA5) | 2026-08-18 17:48 UTC | 2026-08-18 18:05 UTC | 16m |
| N98EG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-18 16:26 UTC | 2026-08-18 18:01 UTC | 1h 34m |
| BLIND91 | BLI | Princeton-Caldwell County Airport (K2M0) | Barkley Regional Airport (KPAH) | 2026-08-18 17:05 UTC | 2026-08-18 17:56 UTC | 50m |
| N26CF |  | Johnson Airport (3AK4) | Trading Bay Production Airport (5AK0) | 2026-08-18 17:44 UTC | 2026-08-18 17:55 UTC | 11m |
| N108EH |  | John Wayne/Orange County Airport (KSNA) | Corona Municipal Airport (KAJO) | 2026-08-18 17:39 UTC | 2026-08-18 17:55 UTC | 16m |
| N734VX |  | San Bernardino International Airport (KSBD) | Hemet-Ryan Airport (KHMT) | 2026-08-18 17:29 UTC | 2026-08-18 17:49 UTC | 19m |
| OXF6881 | OXF | Falcon Field (KFFZ) | Rimrock Airport (48AZ) | 2026-08-18 17:00 UTC | 2026-08-18 17:48 UTC | 47m |
| N330DD |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-08-18 17:27 UTC | 2026-08-18 17:48 UTC | 20m |
| N828WW |  | Dupage Airport (KDPA) | IS63 (IS63) | 2026-08-18 16:54 UTC | 2026-08-18 17:39 UTC | 44m |
| N327JZ |  | Cincinnati Municipal/Lunken Field (KLUK) | VA75 (VA75) | 2026-08-18 16:28 UTC | 2026-08-18 17:35 UTC | 1h 7m |
| XBJMV | XBJ | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-08-18 17:05 UTC | 2026-08-18 17:34 UTC | 29m |
| WAKE49 | WAK | Albuquerque International Sunport Airport (KABQ) | Albuquerque International Sunport Airport (KABQ) | 2026-08-18 17:22 UTC | 2026-08-18 17:32 UTC | 10m |
| EAG36B | EAG | George Best Belfast City Airport (EGAC) | Birmingham International Airport (EGBB) | 2026-08-18 16:40 UTC | 2026-08-18 17:32 UTC | 51m |
| N866US |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-08-18 16:34 UTC | 2026-08-18 17:30 UTC | 56m |
| SXS1 | SXS | Antalya International Airport (LTAI) | Frankfurt am Main International Airport (EDDF) | 2026-08-18 13:57 UTC | 2026-08-18 17:30 UTC | 3h 32m |
| BOX748 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-08-18 03:25 UTC | 2026-08-18 17:30 UTC | 14h 4m |
| CAN10 | CAN | Calcinate Del Pesce Airport (LILC) | Calcinate Del Pesce Airport (LILC) | 2026-08-18 16:54 UTC | 2026-08-18 17:26 UTC | 31m |
| UAE9408 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-18 06:39 UTC | 2026-08-18 17:24 UTC | 10h 45m |
| N714LM |  | Addison Airport (KADS) | KH21 (KH21) | 2026-08-18 16:20 UTC | 2026-08-18 17:24 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
