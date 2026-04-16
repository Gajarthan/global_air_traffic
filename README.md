# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_14:19:31_UTC-green)

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

**Latest saved flight:** 2026-04-16 14:19:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 14:19:31 UTC

- **37,304** saved flights
- **16,151** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,304** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **451,310.6 tonnes** estimated CO2 emissions
- **26,162,932 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1581 |
| 2 | SkyWest Airlines | 1461 |
| 3 | IndiGo | 926 |
| 4 | EJA | 631 |
| 5 | American Airlines | 624 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 485 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | LATAM Airlines | 378 |
| 11 | Vueling | 375 |
| 12 | All Nippon Airways | 337 |
| 13 | AZU | 332 |
| 14 | Delta Air Lines | 317 |
| 15 | QLK | 313 |
| 16 | LXJ | 295 |
| 17 | Swiss International | 280 |
| 18 | WIF | 280 |
| 19 | AEE | 250 |
| 20 | Alaska Airlines | 247 |
| 21 | EJU | 245 |
| 22 | easyJet | 245 |
| 23 | VIV | 236 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 213 |
| 26 | United Airlines | 207 |
| 27 | EDV | 206 |
| 28 | AIQ | 198 |
| 29 | GLO | 196 |
| 30 | Avianca | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29180 |
| 2 | 🇮🇳 IN | 2833 |
| 3 | 🇪🇸 ES | 2774 |
| 4 | 🇦🇺 AU | 2650 |
| 5 | 🇧🇷 BR | 2194 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 1978 |
| 8 | 🇩🇪 DE | 1918 |
| 9 | 🇨🇴 CO | 1835 |
| 10 | 🇨🇦 CA | 1823 |
| 11 | 🇬🇧 GB | 1539 |
| 12 | 🇫🇷 FR | 1425 |
| 13 | 🇲🇽 MX | 1169 |
| 14 | 🇬🇷 GR | 1129 |
| 15 | 🇨🇭 CH | 1029 |
| 16 | 🇲🇾 MY | 962 |
| 17 | 🇳🇴 NO | 906 |
| 18 | 🇿🇦 ZA | 797 |
| 19 | 🇳🇿 NZ | 787 |
| 20 | 🇵🇭 PH | 700 |
| 21 | 🇹🇭 TH | 689 |
| 22 | 🇹🇷 TR | 672 |
| 23 | 🇬🇹 GT | 640 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 584 |
| 26 | 🇲🇦 MA | 470 |
| 27 | 🇳🇱 NL | 372 |
| 28 | 🇲🇪 ME | 366 |
| 29 | 🇧🇸 BS | 359 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 872 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 653 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 610 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 556 |
| 7 | Harry Reid International Airport |  | US | 487 |
| 8 | La Aurora Airport |  | GT | 471 |
| 9 | Guaymaral Airport |  | CO | 464 |
| 10 | Zurich Airport |  | CH | 452 |
| 11 | Kuala Lumpur International Airport |  | MY | 374 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 371 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Frankfurt am Main International Airport |  | DE | 345 |
| 17 | Madrid Barajas International Airport |  | ES | 338 |
| 18 | Macau International Airport |  | MO | 337 |
| 19 | Tenerife Norte Airport |  | ES | 332 |
| 20 | Charlotte/Douglas International Airport |  | US | 330 |
| 21 | Bengaluru International Airport |  | IN | 326 |
| 22 | Congonhas Airport |  | BR | 325 |
| 23 | Ninoy Aquino International Airport |  | PH | 324 |
| 24 | Malpensa International Airport |  | IT | 304 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 289 |
| 26 | Salt Lake City International Airport |  | US | 281 |
| 27 | Daniel K Inouye International Airport |  | US | 278 |
| 28 | Charles de Gaulle International Airport |  | FR | 278 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 265 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 264 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | O. R. Tambo International Airport |  | ZA | 255 |
| 33 | Reno/Tahoe International Airport |  | US | 255 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 252 |
| 35 | Vitoria/Foronda Airport |  | ES | 247 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 37 | Barcelona International Airport |  | ES | 240 |
| 38 | Don Mueang International Airport |  | TH | 235 |
| 39 | Viracopos International Airport |  | BR | 232 |
| 40 | Seattle-Tacoma International Airport |  | US | 229 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 182 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 93 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 89 | 21m | 244 km | 374.8 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 81 | 27m | 275 km | 383.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 81 | 21m | 99 km | 138.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 55 | 1h 41m | 1,423 km | 1,349.8 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 55 | 16m | 162 km | 154.2 t |
| 27 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 54 | 26m | 215 km | 200.0 t |
| 28 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEA89MM | AEA | Madrid Barajas International Airport (LEMD) | A Coruna Airport (LECO) | 2026-04-16 13:32 UTC | 2026-04-16 14:19 UTC | 47m |
| BULLY23 | BUL | Bertani Ranch Airport (23TS) | TA29 (TA29) | 2026-04-16 13:54 UTC | 2026-04-16 14:11 UTC | 17m |
| N7669G |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-16 13:30 UTC | 2026-04-16 14:08 UTC | 38m |
| N53FF |  | Rocky Mountain Metro Airport (KBJC) | Boulder Municipal Airport (KBDU) | 2026-04-16 13:33 UTC | 2026-04-16 14:06 UTC | 32m |
| HB2475 |  | Lodrino Air Base (LSML) | Lodrino Air Base (LSML) | 2026-04-16 11:45 UTC | 2026-04-16 14:06 UTC | 2h 20m |
| N714FW |  | Hicks Airfield (KT67) | Jim Sears Airport (3TA7) | 2026-04-16 13:43 UTC | 2026-04-16 14:04 UTC | 21m |
| KATT12 | KAT | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Shade Tree Field (MS82) | 2026-04-16 13:27 UTC | 2026-04-16 14:01 UTC | 34m |
| N3063G |  | Christmas Flying Service Airport (MS03) | Christmas Flying Service Airport (MS03) | 2026-04-16 12:54 UTC | 2026-04-16 14:01 UTC | 1h 6m |
| BELIGOUB | Brussels Airlines | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-04-16 13:05 UTC | 2026-04-16 13:59 UTC | 54m |
| ELY1366 | ELY | Budapest Ferenc Liszt International Airport (LHBP) | Herzliya Airport (LLHZ) | 2026-04-16 11:13 UTC | 2026-04-16 13:58 UTC | 2h 44m |
| FLC73 | FLC | Lea County Regional Airport (KHOB) | Midland International Air And Space Port Airport (KMAF) | 2026-04-16 13:34 UTC | 2026-04-16 13:58 UTC | 23m |
| N7882N |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-04-16 13:22 UTC | 2026-04-16 13:54 UTC | 31m |
| SCU6 | SCU | OK13 (OK13) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-04-16 13:35 UTC | 2026-04-16 13:54 UTC | 19m |
| CXK633 | CXK | Essex County Airport (KCDW) | Lancaster Airport (KLNS) | 2026-04-16 12:36 UTC | 2026-04-16 13:54 UTC | 1h 18m |
| N660ME |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-16 13:44 UTC | 2026-04-16 13:54 UTC | 9m |
| FHPHI | FHP | Lyon-Bron Airport (LFLY) | Perouges - Meximieux Airport (LFHC) | 2026-04-16 13:18 UTC | 2026-04-16 13:53 UTC | 35m |
| FHBVF | FHB | Dax Seyresse Airport (LFBY) | Dax Seyresse Airport (LFBY) | 2026-04-16 13:09 UTC | 2026-04-16 13:50 UTC | 41m |
| HK5463X |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-04-16 13:30 UTC | 2026-04-16 13:50 UTC | 19m |
| CXK293 | CXK | Harrisburg International Airport (KMDT) | Lancaster Airport (KLNS) | 2026-04-16 13:26 UTC | 2026-04-16 13:44 UTC | 17m |
| N1910R |  | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-04-16 13:31 UTC | 2026-04-16 13:42 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
