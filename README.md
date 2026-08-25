# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_14:44:03_UTC-green)

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

**Latest saved flight:** 2026-08-25 14:44:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 14:44:03 UTC

- **235,289** saved flights
- **71,983** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,289** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,834,636.1 tonnes** estimated CO2 emissions
- **164,326,732 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9434 |
| 2 | SkyWest Airlines | 8301 |
| 3 | EJA | 4558 |
| 4 | IndiGo | 3980 |
| 5 | American Airlines | 3817 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2994 |
| 8 | ENY | 2855 |
| 9 | LATAM Airlines | 2261 |
| 10 | AZU | 2194 |
| 11 | Vueling | 2017 |
| 12 | Lufthansa | 1915 |
| 13 | WIF | 1872 |
| 14 | LXJ | 1845 |
| 15 | easyJet | 1644 |
| 16 | Swiss International | 1582 |
| 17 | AXM | 1575 |
| 18 | EJU | 1504 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1485 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | GLO | 1310 |
| 24 | WMT | 1309 |
| 25 | VIV | 1297 |
| 26 | PGT | 1283 |
| 27 | Air France | 1280 |
| 28 | Wizz Air | 1252 |
| 29 | AEE | 1169 |
| 30 | JetBlue | 1163 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195328 |
| 2 | 🇪🇸 ES | 15128 |
| 3 | 🇧🇷 BR | 13738 |
| 4 | 🇦🇺 AU | 13336 |
| 5 | 🇨🇦 CA | 13003 |
| 6 | 🇮🇹 IT | 12814 |
| 7 | 🇮🇳 IN | 12394 |
| 8 | 🇩🇪 DE | 11603 |
| 9 | 🇬🇧 GB | 11104 |
| 10 | 🇨🇴 CO | 9925 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9439 |
| 13 | 🇹🇷 TR | 6979 |
| 14 | 🇬🇷 GR | 6937 |
| 15 | 🇲🇽 MX | 6533 |
| 16 | 🇨🇭 CH | 6295 |
| 17 | 🇳🇴 NO | 5825 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4212 |
| 20 | 🇿🇦 ZA | 4123 |
| 21 | 🇵🇱 PL | 3925 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2945 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2707 |
| 27 | 🇲🇦 MA | 2384 |
| 28 | 🇲🇪 ME | 2186 |
| 29 | 🇳🇱 NL | 2113 |
| 30 | 🇮🇩 ID | 2055 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4876 |
| 2 | Denver International Airport |  | US | 3802 |
| 3 | Indira Gandhi International Airport |  | IN | 2874 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2682 |
| 6 | Harry Reid International Airport |  | US | 2522 |
| 7 | Zurich Airport |  | CH | 2467 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2398 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2359 |
| 10 | La Aurora Airport |  | GT | 2244 |
| 11 | El Dorado International Airport |  | CO | 2218 |
| 12 | Chicago O'Hare International Airport |  | US | 2119 |
| 13 | Salt Lake City International Airport |  | US | 2070 |
| 14 | Congonhas Airport |  | BR | 2002 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1875 |
| 17 | Madrid Barajas International Airport |  | ES | 1849 |
| 18 | Capua Airport |  | IT | 1849 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1773 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1734 |
| 21 | Malpensa International Airport |  | IT | 1686 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1667 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1638 |
| 25 | Macau International Airport |  | MO | 1612 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1516 |
| 29 | Barcelona International Airport |  | ES | 1489 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1457 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1423 |
| 32 | Viracopos International Airport |  | BR | 1403 |
| 33 | Bengaluru International Airport |  | IN | 1382 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1378 |
| 35 | Seattle-Tacoma International Airport |  | US | 1378 |
| 36 | Don Mueang International Airport |  | TH | 1366 |
| 37 | Calgary International Airport |  | CA | 1346 |
| 38 | Oslo Gardermoen Airport |  | NO | 1321 |
| 39 | Vancouver International Airport |  | CA | 1284 |
| 40 | O. R. Tambo International Airport |  | ZA | 1282 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1087 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 863 | 21m | 244 km | 3,633.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 590 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 526 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 387 | 27m | 275 km | 1,833.8 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 364 | 1h 50m | 1,423 km | 8,933.1 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 341 | 44m | 555 km | 3,265.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 331 | 21m | 250 km | 1,429.7 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 310 | 1h 40m | 1,156 km | 6,184.4 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 289 | 27m | 215 km | 1,070.3 t |
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
| N390TC |  | Orlando Apopka Airport (KX04) | Leesburg International Airport (KLEE) | 2026-08-25 14:22 UTC | 2026-08-25 14:44 UTC | 21m |
| PGT11YN | PGT | Brussels Airport (EBBR) | Antalya International Airport (LTAI) | 2026-08-25 11:24 UTC | 2026-08-25 14:42 UTC | 3h 18m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 14:26 UTC | 2026-08-25 14:41 UTC | 14m |
| N21019 |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-08-25 13:45 UTC | 2026-08-25 14:40 UTC | 55m |
| PNC0106 | PNC | Guaymaral Airport (SKGY) | El Dorado International Airport (SKBO) | 2026-08-25 14:00 UTC | 2026-08-25 14:36 UTC | 35m |
| BOMR765 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Aransas County Airport (KRKP) | 2026-08-25 13:49 UTC | 2026-08-25 14:35 UTC | 46m |
| SCU28 | SCU | Tulsa Riverside Airport (KRVS) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-25 14:01 UTC | 2026-08-25 14:29 UTC | 28m |
| ARCAT55 | ARC | Montgomery-Gibbs Executive Airport (KMYF) | Osborne Airport (8CA0) | 2026-08-25 14:04 UTC | 2026-08-25 14:29 UTC | 24m |
| EXS084T | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-25 13:15 UTC | 2026-08-25 14:25 UTC | 1h 10m |
| CXK1140 | CXK | Clark Regional Airport (KJVY) | Clark Regional Airport (KJVY) | 2026-08-25 14:23 UTC | 2026-08-25 14:24 UTC | 0m |
| N247EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-08-25 13:11 UTC | 2026-08-25 14:19 UTC | 1h 7m |
| AMU615 | AMU | Macau International Airport (VMMC) | Macau International Airport (VMMC) | 2026-08-25 14:12 UTC | 2026-08-25 14:18 UTC | 5m |
| DAH1535 | DAH | Charles de Gaulle International Airport (LFPG) | Ain Oussera Airport (DAAQ) | 2026-08-25 12:27 UTC | 2026-08-25 14:18 UTC | 1h 50m |
| N800U |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-25 14:02 UTC | 2026-08-25 14:18 UTC | 15m |
| FTO501 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-25 13:41 UTC | 2026-08-25 14:17 UTC | 35m |
| N778SA |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-25 14:05 UTC | 2026-08-25 14:16 UTC | 11m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-08-25 13:58 UTC | 2026-08-25 14:16 UTC | 18m |
| N5334D |  | Holmes County Airport (K10G) | Richard Downing Airport (KI40) | 2026-08-25 13:33 UTC | 2026-08-25 14:15 UTC | 41m |
| N8182E |  | K5T6 (K5T6) | NM26 (NM26) | 2026-08-25 13:32 UTC | 2026-08-25 14:14 UTC | 42m |
| DESERT3 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 14:00 UTC | 2026-08-25 14:14 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
