# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_03:36:16_UTC-green)

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

**Latest saved flight:** 2026-04-18 03:36:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 03:36:16 UTC

- **40,509** saved flights
- **17,261** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,509** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **487,917.9 tonnes** estimated CO2 emissions
- **28,285,096 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1692 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 983 |
| 4 | EJA | 712 |
| 5 | American Airlines | 680 |
| 6 | Southwest Airlines | 574 |
| 7 | ENY | 523 |
| 8 | AXM | 416 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 398 |
| 11 | Lufthansa | 386 |
| 12 | AZU | 360 |
| 13 | All Nippon Airways | 358 |
| 14 | Delta Air Lines | 347 |
| 15 | QLK | 336 |
| 16 | LXJ | 325 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 272 |
| 20 | AEE | 267 |
| 21 | easyJet | 264 |
| 22 | VIV | 264 |
| 23 | EJU | 262 |
| 24 | Japan Airlines | 245 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 205 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32231 |
| 2 | 🇮🇳 IN | 3001 |
| 3 | 🇪🇸 ES | 2980 |
| 4 | 🇦🇺 AU | 2846 |
| 5 | 🇧🇷 BR | 2403 |
| 6 | 🇯🇵 JP | 2177 |
| 7 | 🇮🇹 IT | 2099 |
| 8 | 🇩🇪 DE | 2022 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1641 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1289 |
| 14 | 🇬🇷 GR | 1204 |
| 15 | 🇨🇭 CH | 1100 |
| 16 | 🇲🇾 MY | 1013 |
| 17 | 🇳🇴 NO | 1005 |
| 18 | 🇳🇿 NZ | 835 |
| 19 | 🇿🇦 ZA | 827 |
| 20 | 🇵🇭 PH | 730 |
| 21 | 🇹🇭 TH | 718 |
| 22 | 🇹🇷 TR | 707 |
| 23 | 🇬🇹 GT | 688 |
| 24 | 🇰🇷 KR | 654 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 497 |
| 27 | 🇳🇱 NL | 405 |
| 28 | 🇲🇪 ME | 402 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 370 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 742 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 677 |
| 5 | Indira Gandhi International Airport |  | IN | 646 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 600 |
| 7 | Harry Reid International Airport |  | US | 528 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 508 |
| 10 | Zurich Airport |  | CH | 485 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 402 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 13 | Kuala Lumpur International Airport |  | MY | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 387 |
| 16 | Macau International Airport |  | MO | 370 |
| 17 | Madrid Barajas International Airport |  | ES | 364 |
| 18 | Charlotte/Douglas International Airport |  | US | 358 |
| 19 | Tenerife Norte Airport |  | ES | 358 |
| 20 | Congonhas Airport |  | BR | 353 |
| 21 | Frankfurt am Main International Airport |  | DE | 352 |
| 22 | Bengaluru International Airport |  | IN | 351 |
| 23 | Ninoy Aquino International Airport |  | PH | 339 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 302 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 288 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 279 |
| 32 | Reno/Tahoe International Airport |  | US | 278 |
| 33 | Vitoria/Foronda Airport |  | ES | 276 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Calgary International Airport |  | CA | 247 |
| 39 | Viracopos International Airport |  | BR | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 186 | 1h 8m | 706 km | 2,264.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 143 | 24m | 225 km | 554.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 117 | 28m | 304 km | 613.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 113 | 1h 27m | 910 km | 1,773.2 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 107 | 21m | 244 km | 450.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 107 | 19m | 165 km | 304.4 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 103 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 85 | 21m | 99 km | 145.6 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 81 | 44m | 452 km | 631.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 73 | 31m | 369 km | 464.7 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 65 | 52m | 556 km | 623.1 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 61 | 1h 41m | 1,423 km | 1,497.0 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 57 | 59m | 695 km | 683.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXA825 | CXA | Melbourne International Airport (YMML) | St. Peter-Ording Airport (EDXO) | 2026-04-17 01:39 UTC | 2026-04-18 03:36 UTC | 25h 56m |
| CAP4349 | CAP | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-04-18 02:53 UTC | 2026-04-18 03:31 UTC | 38m |
| DRAFT85 | DRA | Imperial County Airport (KIPL) | Desert Air Sky Ranch Airport (63CA) | 2026-04-18 03:10 UTC | 2026-04-18 03:31 UTC | 20m |
| ETW | ETW | Corryong Airport (YCRG) | Corryong Airport (YCRG) | 2026-04-18 03:12 UTC | 2026-04-18 03:21 UTC | 9m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-18 02:49 UTC | 2026-04-18 03:14 UTC | 24m |
| SKW5039 | SkyWest Airlines | Denver International Airport (KDEN) | TX20 (TX20) | 2026-04-18 01:54 UTC | 2026-04-18 03:05 UTC | 1h 11m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-04-18 02:39 UTC | 2026-04-18 03:02 UTC | 22m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-18 01:31 UTC | 2026-04-18 03:00 UTC | 1h 29m |
| BOV739 | BOV | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Laja Airport (SLLJ) | 2026-04-17 22:17 UTC | 2026-04-18 03:00 UTC | 4h 43m |
| LXJ603 | LXJ | Palm Springs International Airport (KPSP) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-18 02:04 UTC | 2026-04-18 02:53 UTC | 49m |
| DCDSO | DCD | Frankfurt am Main International Airport (EDDF) | Hamburg Airport (EDDH) | 2026-04-18 02:07 UTC | 2026-04-18 02:52 UTC | 45m |
| SWA169 | Southwest Airlines | Harry Reid International Airport (KLAS) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-18 02:03 UTC | 2026-04-18 02:51 UTC | 48m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-04-18 02:14 UTC | 2026-04-18 02:46 UTC | 31m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-18 02:17 UTC | 2026-04-18 02:45 UTC | 28m |
| TWB923 | TWB | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-18 02:15 UTC | 2026-04-18 02:44 UTC | 28m |
| ANA1262 | All Nippon Airways | New Chitose Airport (RJCC) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-04-18 01:12 UTC | 2026-04-18 02:43 UTC | 1h 31m |
| N741SM |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-04-18 01:09 UTC | 2026-04-18 02:43 UTC | 1h 33m |
| BBC535 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-18 02:12 UTC | 2026-04-18 02:42 UTC | 30m |
| CFKAB | CFK | Sudbury Airport (CYSB) | Bar River Airport (CPF2) | 2026-04-18 02:02 UTC | 2026-04-18 02:42 UTC | 39m |
| DAL2581 | Delta Air Lines | Austin-Bergstrom International Airport (KAUS) | Salt Lake City International Airport (KSLC) | 2026-04-17 23:58 UTC | 2026-04-18 02:41 UTC | 2h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
