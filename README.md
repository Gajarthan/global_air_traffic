# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_19:19:37_UTC-green)

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

**Latest saved flight:** 2026-04-18 19:19:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 19:19:37 UTC

- **41,849** saved flights
- **17,646** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **41,849** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **503,221.0 tonnes** estimated CO2 emissions
- **29,172,233 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1758 |
| 2 | SkyWest Airlines | 1626 |
| 3 | IndiGo | 1027 |
| 4 | EJA | 724 |
| 5 | American Airlines | 692 |
| 6 | Southwest Airlines | 590 |
| 7 | ENY | 535 |
| 8 | AXM | 434 |
| 9 | Vueling | 420 |
| 10 | LATAM Airlines | 413 |
| 11 | Lufthansa | 411 |
| 12 | All Nippon Airways | 377 |
| 13 | AZU | 373 |
| 14 | Delta Air Lines | 354 |
| 15 | QLK | 341 |
| 16 | LXJ | 328 |
| 17 | WIF | 324 |
| 18 | Swiss International | 323 |
| 19 | Alaska Airlines | 283 |
| 20 | AEE | 281 |
| 21 | EJU | 277 |
| 22 | easyJet | 270 |
| 23 | VIV | 269 |
| 24 | Japan Airlines | 257 |
| 25 | Air France | 236 |
| 26 | JetBlue | 224 |
| 27 | United Airlines | 223 |
| 28 | GLO | 222 |
| 29 | AXB | 220 |
| 30 | EDV | 218 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 33048 |
| 2 | 🇮🇳 IN | 3143 |
| 3 | 🇪🇸 ES | 3086 |
| 4 | 🇦🇺 AU | 2918 |
| 5 | 🇧🇷 BR | 2502 |
| 6 | 🇯🇵 JP | 2291 |
| 7 | 🇮🇹 IT | 2177 |
| 8 | 🇩🇪 DE | 2123 |
| 9 | 🇨🇦 CA | 2043 |
| 10 | 🇨🇴 CO | 1965 |
| 11 | 🇬🇧 GB | 1700 |
| 12 | 🇫🇷 FR | 1614 |
| 13 | 🇲🇽 MX | 1319 |
| 14 | 🇬🇷 GR | 1273 |
| 15 | 🇨🇭 CH | 1177 |
| 16 | 🇲🇾 MY | 1053 |
| 17 | 🇳🇴 NO | 1031 |
| 18 | 🇿🇦 ZA | 869 |
| 19 | 🇳🇿 NZ | 844 |
| 20 | 🇵🇭 PH | 756 |
| 21 | 🇹🇭 TH | 741 |
| 22 | 🇹🇷 TR | 730 |
| 23 | 🇬🇹 GT | 705 |
| 24 | 🇰🇷 KR | 687 |
| 25 | 🇵🇱 PL | 663 |
| 26 | 🇲🇦 MA | 518 |
| 27 | 🇳🇱 NL | 430 |
| 28 | 🇲🇪 ME | 428 |
| 29 | 🇧🇸 BS | 395 |
| 30 | 🇮🇩 ID | 380 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 963 |
| 2 | Tokyo International Airport |  | JP | 783 |
| 3 | El Dorado International Airport |  | CO | 689 |
| 4 | Denver International Airport |  | US | 687 |
| 5 | Indira Gandhi International Airport |  | IN | 678 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 630 |
| 7 | Harry Reid International Airport |  | US | 537 |
| 8 | Guaymaral Airport |  | CO | 527 |
| 9 | La Aurora Airport |  | GT | 520 |
| 10 | Zurich Airport |  | CH | 506 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 415 |
| 12 | Kuala Lumpur International Airport |  | MY | 415 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 407 |
| 14 | Chicago O'Hare International Airport |  | US | 403 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 394 |
| 16 | Frankfurt am Main International Airport |  | DE | 381 |
| 17 | Madrid Barajas International Airport |  | ES | 378 |
| 18 | Macau International Airport |  | MO | 377 |
| 19 | Bengaluru International Airport |  | IN | 370 |
| 20 | Tenerife Norte Airport |  | ES | 368 |
| 21 | Charlotte/Douglas International Airport |  | US | 364 |
| 22 | Congonhas Airport |  | BR | 362 |
| 23 | Ninoy Aquino International Airport |  | PH | 351 |
| 24 | Malpensa International Airport |  | IT | 338 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 325 |
| 26 | Salt Lake City International Airport |  | US | 321 |
| 27 | Daniel K Inouye International Airport |  | US | 313 |
| 28 | Charles de Gaulle International Airport |  | FR | 306 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 305 |
| 30 | Vitoria/Foronda Airport |  | ES | 299 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 291 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 288 |
| 33 | Reno/Tahoe International Airport |  | US | 286 |
| 34 | O. R. Tambo International Airport |  | ZA | 282 |
| 35 | Capua Airport |  | IT | 282 |
| 36 | John Paul II International Airport Kraków-Balice Airport |  | PL | 281 |
| 37 | Barcelona International Airport |  | ES | 266 |
| 38 | Viracopos International Airport |  | BR | 258 |
| 39 | Calgary International Airport |  | CA | 250 |
| 40 | Seattle-Tacoma International Airport |  | US | 247 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 211 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 196 | 1h 7m | 706 km | 2,386.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 150 | 24m | 225 km | 581.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 124 | 28m | 304 km | 650.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 121 | 1h 27m | 910 km | 1,898.8 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 115 | 21m | 244 km | 484.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 112 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 112 | 19m | 165 km | 318.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 105 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 99 | 26m | 275 km | 469.1 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 91 | 54m | 546 km | 856.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 88 | 21m | 99 km | 150.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 85 | 44m | 452 km | 662.5 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 82 | 1h 11m | 770 km | 1,089.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 76 | 27m | 152 km | 198.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 75 | 31m | 369 km | 477.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 70 | 20m | 250 km | 302.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 66 | 20m | 147 km | 167.0 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 22 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 63 | 26m | 215 km | 233.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 59 | 12m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 28 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 58 | 1h 21m | 961 km | 961.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N132CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-04-18 17:18 UTC | 2026-04-18 19:19 UTC | 2h 1m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-18 18:51 UTC | 2026-04-18 19:15 UTC | 23m |
| N545GC |  | Lompoc Airport (KLPC) | Lompoc Airport (KLPC) | 2026-04-18 18:53 UTC | 2026-04-18 19:14 UTC | 20m |
| N4566R |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-04-18 18:59 UTC | 2026-04-18 19:09 UTC | 10m |
| N692DA |  | General Mariano Matamoros Airport (MMCB) | Hermanos Serdan International Airport (MMPB) | 2026-04-18 18:12 UTC | 2026-04-18 19:04 UTC | 51m |
| THA313 | Thai Airways | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-04-18 16:46 UTC | 2026-04-18 19:01 UTC | 2h 14m |
| FXC22 | FXC | Westchester County Airport (KHPN) | Teterboro Airport (KTEB) | 2026-04-18 18:43 UTC | 2026-04-18 18:56 UTC | 12m |
| CFR614 | CFR | Bonny Doon Airport (CL77) | Bonny Doon Airport (CL77) | 2026-04-18 17:26 UTC | 2026-04-18 18:54 UTC | 1h 28m |
| N156U |  | Preston Airport (KU10) | Preston Airport (KU10) | 2026-04-18 18:12 UTC | 2026-04-18 18:48 UTC | 35m |
| FLTVL18 | FLT | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-04-18 18:09 UTC | 2026-04-18 18:48 UTC | 38m |
|  |  | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-04-18 18:46 UTC | 2026-04-18 18:46 UTC | 0m |
| N254EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-18 17:45 UTC | 2026-04-18 18:42 UTC | 57m |
| N2936Q |  | Bfs Airport (TE70) | Decatur Municipal Airport (KLUD) | 2026-04-18 18:16 UTC | 2026-04-18 18:38 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-18 18:34 UTC | 2026-04-18 18:38 UTC | 4m |
| N709CB |  | Wiley Post Airport (KPWA) | Las Arenas Earth And Sky Observatory Airport (2CO2) | 2026-04-18 17:14 UTC | 2026-04-18 18:36 UTC | 1h 22m |
| N265RV |  | Peeler Airpark (TS47) | Lazy 9 Ranch Airport (TX64) | 2026-04-18 17:39 UTC | 2026-04-18 18:34 UTC | 54m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-04-18 18:12 UTC | 2026-04-18 18:33 UTC | 20m |
| LXJ618 | LXJ | Coral Creek Airport (FA54) | Akron-Canton Regional Airport (KCAK) | 2026-04-18 16:18 UTC | 2026-04-18 18:30 UTC | 2h 12m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-04-18 17:53 UTC | 2026-04-18 18:30 UTC | 36m |
| N322PL |  | Santa Barbara Municipal Airport (KSBA) | Southeast Colorado Regional Airport (KLAA) | 2026-04-18 16:01 UTC | 2026-04-18 18:28 UTC | 2h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
