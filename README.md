# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_08:33:45_UTC-green)

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

**Latest saved flight:** 2026-04-18 08:33:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 08:33:45 UTC

- **40,792** saved flights
- **17,326** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,792** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **491,160.2 tonnes** estimated CO2 emissions
- **28,473,053 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1707 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 998 |
| 4 | EJA | 712 |
| 5 | American Airlines | 681 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 425 |
| 9 | Vueling | 409 |
| 10 | LATAM Airlines | 400 |
| 11 | Lufthansa | 390 |
| 12 | All Nippon Airways | 366 |
| 13 | AZU | 362 |
| 14 | Delta Air Lines | 347 |
| 15 | QLK | 341 |
| 16 | LXJ | 325 |
| 17 | WIF | 317 |
| 18 | Swiss International | 309 |
| 19 | Alaska Airlines | 276 |
| 20 | AEE | 272 |
| 21 | EJU | 267 |
| 22 | easyJet | 266 |
| 23 | VIV | 264 |
| 24 | Japan Airlines | 254 |
| 25 | Air France | 229 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 209 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32294 |
| 2 | 🇮🇳 IN | 3050 |
| 3 | 🇪🇸 ES | 3005 |
| 4 | 🇦🇺 AU | 2902 |
| 5 | 🇧🇷 BR | 2411 |
| 6 | 🇯🇵 JP | 2233 |
| 7 | 🇮🇹 IT | 2120 |
| 8 | 🇩🇪 DE | 2038 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1649 |
| 12 | 🇫🇷 FR | 1549 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1229 |
| 15 | 🇨🇭 CH | 1112 |
| 16 | 🇲🇾 MY | 1032 |
| 17 | 🇳🇴 NO | 1007 |
| 18 | 🇳🇿 NZ | 844 |
| 19 | 🇿🇦 ZA | 833 |
| 20 | 🇵🇭 PH | 746 |
| 21 | 🇹🇭 TH | 725 |
| 22 | 🇹🇷 TR | 707 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 670 |
| 25 | 🇵🇱 PL | 628 |
| 26 | 🇲🇦 MA | 501 |
| 27 | 🇳🇱 NL | 413 |
| 28 | 🇲🇪 ME | 410 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇮🇩 ID | 375 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 764 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 677 |
| 5 | Indira Gandhi International Airport |  | IN | 658 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 611 |
| 7 | Harry Reid International Airport |  | US | 530 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 489 |
| 11 | Kuala Lumpur International Airport |  | MY | 405 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 404 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 391 |
| 16 | Macau International Airport |  | MO | 372 |
| 17 | Madrid Barajas International Airport |  | ES | 369 |
| 18 | Bengaluru International Airport |  | IN | 360 |
| 19 | Charlotte/Douglas International Airport |  | US | 358 |
| 20 | Tenerife Norte Airport |  | ES | 358 |
| 21 | Frankfurt am Main International Airport |  | DE | 355 |
| 22 | Congonhas Airport |  | BR | 353 |
| 23 | Ninoy Aquino International Airport |  | PH | 347 |
| 24 | Malpensa International Airport |  | IT | 329 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 306 |
| 28 | Charles de Gaulle International Airport |  | FR | 298 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 293 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Vitoria/Foronda Airport |  | ES | 283 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 281 |
| 33 | Reno/Tahoe International Airport |  | US | 280 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 270 |
| 36 | O. R. Tambo International Airport |  | ZA | 268 |
| 37 | Barcelona International Airport |  | ES | 261 |
| 38 | Viracopos International Airport |  | BR | 248 |
| 39 | Calgary International Airport |  | CA | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 192 | 1h 7m | 706 km | 2,337.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 149 | 24m | 225 km | 578.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 121 | 28m | 304 km | 634.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 118 | 1h 27m | 910 km | 1,851.7 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 109 | 21m | 244 km | 459.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 108 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 108 | 19m | 165 km | 307.2 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 96 | 26m | 275 km | 454.9 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 89 | 54m | 546 km | 837.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 83 | 44m | 452 km | 646.9 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 74 | 31m | 369 km | 471.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 64 | 20m | 147 km | 162.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 64 | 20m | 250 km | 276.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 62 | 1h 41m | 1,423 km | 1,521.6 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 57 | 14m | 154 km | 151.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N240GS |  | Old Sarum Airfield (EGLS) | Old Sarum Airfield (EGLS) | 2026-04-18 07:55 UTC | 2026-04-18 08:33 UTC | 38m |
| N98CF |  | Maribor Airport (LJMB) | Maribor Airport (LJMB) | 2026-04-18 08:14 UTC | 2026-04-18 08:21 UTC | 6m |
| IOZZD | IOZ | Forli Airport (LIPK) | Bologna / Borgo Panigale Airport (LIPE) | 2026-04-18 07:55 UTC | 2026-04-18 08:19 UTC | 23m |
| DEOLL | DEO | Schonhagen Airport (EDAZ) | Reinsdorf Airport (EDOD) | 2026-04-18 08:09 UTC | 2026-04-18 08:14 UTC | 5m |
| SEH3JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-04-18 07:39 UTC | 2026-04-18 08:04 UTC | 25m |
| HBZPA | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-04-18 07:38 UTC | 2026-04-18 08:03 UTC | 25m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-04-18 07:37 UTC | 2026-04-18 07:59 UTC | 22m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Hosur Airport (VO95) | 2026-04-18 07:23 UTC | 2026-04-18 07:59 UTC | 35m |
| VLG9GD | Vueling | Malaga Airport (LEMG) | Brussels Airport (EBBR) | 2026-04-18 05:40 UTC | 2026-04-18 07:58 UTC | 2h 17m |
| AFR26AP | Air France | Charles de Gaulle International Airport (LFPG) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-18 06:46 UTC | 2026-04-18 07:57 UTC | 1h 10m |
| VLG1HY | Vueling | Malaga Airport (LEMG) | Palma De Mallorca Airport (LEPA) | 2026-04-18 06:52 UTC | 2026-04-18 07:56 UTC | 1h 3m |
| SEH2JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-18 07:22 UTC | 2026-04-18 07:49 UTC | 27m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-18 05:55 UTC | 2026-04-18 07:48 UTC | 1h 53m |
| SWR564 | Swiss International | Zurich Airport (LSZH) | Cuneo / Levaldigi Airport (LIMZ) | 2026-04-18 06:55 UTC | 2026-04-18 07:46 UTC | 51m |
| KASET547 | KAS | Chiang Mai International Airport (VTCC) | Loikaw Airport (VYLK) | 2026-04-18 07:25 UTC | 2026-04-18 07:44 UTC | 19m |
| FGRDR | FGR | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | Pontoise - Cormeilles-en-Vexin Airport (LFPT) | 2026-04-18 07:43 UTC | 2026-04-18 07:44 UTC | 1m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-04-18 07:27 UTC | 2026-04-18 07:43 UTC | 15m |
| KAL1823 | Korean Air | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 2026-04-18 07:11 UTC | 2026-04-18 07:37 UTC | 26m |
| N685GT |  | Zurich Airport (LSZH) | Ambri Airport (LSPM) | 2026-04-18 06:49 UTC | 2026-04-18 07:37 UTC | 47m |
| POK | POK | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-18 07:22 UTC | 2026-04-18 07:37 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
