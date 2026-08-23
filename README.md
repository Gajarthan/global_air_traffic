# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_13:45:43_UTC-green)

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

**Latest saved flight:** 2026-08-23 13:45:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-23 13:45:43 UTC

- **228,543** saved flights
- **70,712** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **228,543** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,756,757.3 tonnes** estimated CO2 emissions
- **159,812,016 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9180 |
| 2 | SkyWest Airlines | 8104 |
| 3 | EJA | 4394 |
| 4 | IndiGo | 3871 |
| 5 | American Airlines | 3740 |
| 6 | Southwest Airlines | 3549 |
| 7 | Delta Air Lines | 2921 |
| 8 | ENY | 2791 |
| 9 | LATAM Airlines | 2194 |
| 10 | AZU | 2119 |
| 11 | Vueling | 1942 |
| 12 | Lufthansa | 1870 |
| 13 | WIF | 1802 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1597 |
| 16 | Swiss International | 1525 |
| 17 | AXM | 1520 |
| 18 | EJU | 1450 |
| 19 | QLK | 1448 |
| 20 | United Airlines | 1446 |
| 21 | Alaska Airlines | 1385 |
| 22 | All Nippon Airways | 1372 |
| 23 | GLO | 1265 |
| 24 | VIV | 1253 |
| 25 | PGT | 1252 |
| 26 | WMT | 1248 |
| 27 | Air France | 1242 |
| 28 | Wizz Air | 1190 |
| 29 | JetBlue | 1142 |
| 30 | AEE | 1139 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190729 |
| 2 | 🇪🇸 ES | 14668 |
| 3 | 🇧🇷 BR | 13327 |
| 4 | 🇦🇺 AU | 12959 |
| 5 | 🇨🇦 CA | 12625 |
| 6 | 🇮🇹 IT | 12342 |
| 7 | 🇮🇳 IN | 12065 |
| 8 | 🇩🇪 DE | 11252 |
| 9 | 🇬🇧 GB | 10762 |
| 10 | 🇨🇴 CO | 9394 |
| 11 | 🇯🇵 JP | 9312 |
| 12 | 🇫🇷 FR | 9159 |
| 13 | 🇹🇷 TR | 6735 |
| 14 | 🇬🇷 GR | 6715 |
| 15 | 🇲🇽 MX | 6358 |
| 16 | 🇨🇭 CH | 6064 |
| 17 | 🇳🇴 NO | 5620 |
| 18 | 🇲🇾 MY | 4060 |
| 19 | 🇿🇦 ZA | 3985 |
| 20 | 🇹🇭 TH | 3984 |
| 21 | 🇵🇱 PL | 3804 |
| 22 | 🇳🇿 NZ | 3169 |
| 23 | 🇵🇭 PH | 3140 |
| 24 | 🇬🇹 GT | 2875 |
| 25 | 🇰🇷 KR | 2705 |
| 26 | 🇭🇷 HR | 2605 |
| 27 | 🇲🇦 MA | 2316 |
| 28 | 🇲🇪 ME | 2083 |
| 29 | 🇳🇱 NL | 2045 |
| 30 | 🇮🇩 ID | 1976 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4771 |
| 2 | Denver International Airport |  | US | 3714 |
| 3 | Indira Gandhi International Airport |  | IN | 2790 |
| 4 | Tokyo International Airport |  | JP | 2781 |
| 5 | Guaymaral Airport |  | CO | 2648 |
| 6 | Harry Reid International Airport |  | US | 2474 |
| 7 | Zurich Airport |  | CH | 2378 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2333 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2305 |
| 10 | La Aurora Airport |  | GT | 2190 |
| 11 | El Dorado International Airport |  | CO | 2084 |
| 12 | Chicago O'Hare International Airport |  | US | 2071 |
| 13 | Salt Lake City International Airport |  | US | 2010 |
| 14 | Congonhas Airport |  | BR | 1943 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1938 |
| 16 | Frankfurt am Main International Airport |  | DE | 1834 |
| 17 | Madrid Barajas International Airport |  | ES | 1786 |
| 18 | Capua Airport |  | IT | 1779 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1709 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1699 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1649 |
| 22 | Malpensa International Airport |  | IT | 1632 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1612 |
| 24 | Macau International Airport |  | MO | 1596 |
| 25 | Charles de Gaulle International Airport |  | FR | 1581 |
| 26 | Ninoy Aquino International Airport |  | PH | 1506 |
| 27 | Charlotte/Douglas International Airport |  | US | 1492 |
| 28 | Kuala Lumpur International Airport |  | MY | 1471 |
| 29 | Barcelona International Airport |  | ES | 1430 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1384 |
| 31 | Bengaluru International Airport |  | IN | 1355 |
| 32 | Enrique Olaya Herrera Airport |  | CO | 1354 |
| 33 | Viracopos International Airport |  | BR | 1354 |
| 34 | Seattle-Tacoma International Airport |  | US | 1347 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1345 |
| 36 | Don Mueang International Airport |  | TH | 1305 |
| 37 | Calgary International Airport |  | CA | 1299 |
| 38 | Oslo Gardermoen Airport |  | NO | 1268 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | O. R. Tambo International Airport |  | ZA | 1236 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 833 | 21m | 244 km | 3,507.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 575 | 1h 6m | 770 km | 7,638.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 567 | 24m | 225 km | 2,199.7 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 549 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 350 | 1h 50m | 1,423 km | 8,589.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 315 | 1h 7m | 706 km | 3,835.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 315 | 21m | 250 km | 1,360.6 t |
| 13 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 14 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 308 | 44m | 555 km | 2,949.2 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 16 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 293 | 1h 38m | 1,156 km | 5,845.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 292 | 24m | 218 km | 1,100.1 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 277 | 27m | 215 km | 1,025.9 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 266 | 12m | - | - |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 261 | 19m | 144 km | 649.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 241 | 15m | 154 km | 638.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N427GB |  | Mason County Airport (KT92) | Llano Municipal Airport (KAQO) | 2026-08-23 13:34 UTC | 2026-08-23 13:45 UTC | 10m |
| HK5445 |  | Santiago Vila Airport (SKGI) | Santiago Vila Airport (SKGI) | 2026-08-23 13:31 UTC | 2026-08-23 13:42 UTC | 11m |
| N290JK |  | Little Rock Afb Airport (KLRF) | Scott Afb/Midamerica St Louis Airport (KBLV) | 2026-08-23 12:26 UTC | 2026-08-23 13:42 UTC | 1h 15m |
| N31192 |  | Caldwell Executive Airport (KEUL) | Emmett Municipal Airport (KS78) | 2026-08-23 13:24 UTC | 2026-08-23 13:37 UTC | 13m |
| N576JA |  | Lovell Field (KCHA) | Wabash Municipal Airport (KIWH) | 2026-08-23 12:27 UTC | 2026-08-23 13:32 UTC | 1h 5m |
| ABX1520 | ABX | Cincinnati/Northern Kentucky International Airport (KCVG) | George Bush Intcntl/Houston Airport (KIAH) | 2026-08-23 11:39 UTC | 2026-08-23 13:32 UTC | 1h 52m |
| PH1483 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-08-23 13:13 UTC | 2026-08-23 13:31 UTC | 18m |
| PH1692 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-08-23 12:56 UTC | 2026-08-23 13:29 UTC | 32m |
| N2135F |  | Perry Stokes Airport (KTAD) | Spanish Peaks Airfield (K4V1) | 2026-08-23 13:11 UTC | 2026-08-23 13:28 UTC | 17m |
| ILRHQ | ILR | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-08-23 13:00 UTC | 2026-08-23 13:27 UTC | 26m |
| DFRED | DFR | Leutkirch-Unterzeil Airport (EDNL) | Leutkirch-Unterzeil Airport (EDNL) | 2026-08-23 13:05 UTC | 2026-08-23 13:23 UTC | 18m |
| DKDPV | DKD | Aschaffenburg Airport (EDFC) | Aschaffenburg Airport (EDFC) | 2026-08-23 13:09 UTC | 2026-08-23 13:21 UTC | 11m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-23 11:44 UTC | 2026-08-23 13:19 UTC | 1h 34m |
| N733NB |  | Mckinney Ntl Airport (KTKI) | 4 S Ranch Airport (TS25) | 2026-08-23 13:00 UTC | 2026-08-23 13:19 UTC | 18m |
| N778SA |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-08-23 12:58 UTC | 2026-08-23 13:17 UTC | 19m |
| N499GT |  | Valdosta Regional Airport (KVLD) | Valdosta Regional Airport (KVLD) | 2026-08-23 12:59 UTC | 2026-08-23 13:15 UTC | 16m |
| N224JA |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-08-23 12:02 UTC | 2026-08-23 13:14 UTC | 1h 11m |
| 4XCDE |  | Haifa International Airport (LLHA) | Haifa International Airport (LLHA) | 2026-08-23 12:53 UTC | 2026-08-23 13:12 UTC | 19m |
| EJU307A | EJU | Paris-Orly Airport (LFPO) | Toulouse-Blagnac Airport (LFBO) | 2026-08-23 12:14 UTC | 2026-08-23 13:11 UTC | 56m |
| N405CA |  | Dallas Executive Airport (KRBD) | Seagoville Airport (5TA9) | 2026-08-23 12:09 UTC | 2026-08-23 13:08 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
