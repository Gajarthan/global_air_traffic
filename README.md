# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_10:04:59_UTC-green)

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

**Latest saved flight:** 2026-04-16 10:04:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 10:04:59 UTC

- **37,044** saved flights
- **16,078** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **37,044** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **449,065.5 tonnes** estimated CO2 emissions
- **26,032,784 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1570 |
| 2 | SkyWest Airlines | 1460 |
| 3 | IndiGo | 920 |
| 4 | EJA | 630 |
| 5 | American Airlines | 623 |
| 6 | Southwest Airlines | 517 |
| 7 | ENY | 484 |
| 8 | AXM | 397 |
| 9 | Lufthansa | 384 |
| 10 | LATAM Airlines | 374 |
| 11 | Vueling | 371 |
| 12 | All Nippon Airways | 334 |
| 13 | AZU | 327 |
| 14 | Delta Air Lines | 313 |
| 15 | QLK | 313 |
| 16 | LXJ | 293 |
| 17 | Swiss International | 277 |
| 18 | WIF | 274 |
| 19 | AEE | 249 |
| 20 | Alaska Airlines | 247 |
| 21 | easyJet | 243 |
| 22 | EJU | 238 |
| 23 | VIV | 234 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 210 |
| 26 | EDV | 206 |
| 27 | United Airlines | 205 |
| 28 | AIQ | 197 |
| 29 | GLO | 196 |
| 30 | JetBlue | 193 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 29057 |
| 2 | 🇮🇳 IN | 2813 |
| 3 | 🇪🇸 ES | 2749 |
| 4 | 🇦🇺 AU | 2650 |
| 5 | 🇧🇷 BR | 2170 |
| 6 | 🇯🇵 JP | 2021 |
| 7 | 🇮🇹 IT | 1967 |
| 8 | 🇩🇪 DE | 1898 |
| 9 | 🇨🇦 CA | 1821 |
| 10 | 🇨🇴 CO | 1817 |
| 11 | 🇬🇧 GB | 1525 |
| 12 | 🇫🇷 FR | 1392 |
| 13 | 🇲🇽 MX | 1161 |
| 14 | 🇬🇷 GR | 1117 |
| 15 | 🇨🇭 CH | 1013 |
| 16 | 🇲🇾 MY | 952 |
| 17 | 🇳🇴 NO | 890 |
| 18 | 🇿🇦 ZA | 787 |
| 19 | 🇳🇿 NZ | 787 |
| 20 | 🇵🇭 PH | 698 |
| 21 | 🇹🇭 TH | 687 |
| 22 | 🇹🇷 TR | 667 |
| 23 | 🇬🇹 GT | 626 |
| 24 | 🇰🇷 KR | 621 |
| 25 | 🇵🇱 PL | 579 |
| 26 | 🇲🇦 MA | 465 |
| 27 | 🇳🇱 NL | 367 |
| 28 | 🇲🇪 ME | 360 |
| 29 | 🇧🇸 BS | 356 |
| 30 | 🇮🇩 ID | 348 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 871 |
| 2 | Tokyo International Airport |  | JP | 687 |
| 3 | El Dorado International Airport |  | CO | 648 |
| 4 | Denver International Airport |  | US | 624 |
| 5 | Indira Gandhi International Airport |  | IN | 606 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 551 |
| 7 | Harry Reid International Airport |  | US | 482 |
| 8 | La Aurora Airport |  | GT | 459 |
| 9 | Guaymaral Airport |  | CO | 458 |
| 10 | Zurich Airport |  | CH | 449 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 372 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 370 |
| 13 | Kuala Lumpur International Airport |  | MY | 368 |
| 14 | Chicago O'Hare International Airport |  | US | 362 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Frankfurt am Main International Airport |  | DE | 342 |
| 17 | Macau International Airport |  | MO | 337 |
| 18 | Madrid Barajas International Airport |  | ES | 336 |
| 19 | Charlotte/Douglas International Airport |  | US | 329 |
| 20 | Tenerife Norte Airport |  | ES | 328 |
| 21 | Bengaluru International Airport |  | IN | 326 |
| 22 | Ninoy Aquino International Airport |  | PH | 323 |
| 23 | Congonhas Airport |  | BR | 322 |
| 24 | Malpensa International Airport |  | IT | 299 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 288 |
| 26 | Daniel K Inouye International Airport |  | US | 278 |
| 27 | Salt Lake City International Airport |  | US | 278 |
| 28 | Charles de Gaulle International Airport |  | FR | 275 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 261 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 261 |
| 32 | Reno/Tahoe International Airport |  | US | 255 |
| 33 | O. R. Tambo International Airport |  | ZA | 252 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 250 |
| 35 | Vitoria/Foronda Airport |  | ES | 245 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 241 |
| 37 | Barcelona International Airport |  | ES | 239 |
| 38 | Don Mueang International Airport |  | TH | 234 |
| 39 | Viracopos International Airport |  | BR | 230 |
| 40 | Seattle-Tacoma International Airport |  | US | 228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 180 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 173 | 1h 8m | 706 km | 2,106.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 153 | 14m | 114 km | 300.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 108 | 1h 27m | 910 km | 1,694.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 99 | 19m | 165 km | 281.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 93 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 89 | 21m | 244 km | 374.8 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 88 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 81 | 27m | 275 km | 383.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 81 | 54m | 546 km | 762.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 79 | 21m | 99 km | 135.3 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 71 | 45m | 452 km | 553.3 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 70 | 31m | 369 km | 445.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 61 | 20m | 147 km | 154.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 56 | 13m | 99 km | 96.0 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 55 | 1h 41m | 1,423 km | 1,349.8 t |
| 26 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 53 | 26m | 215 km | 196.3 t |
| 27 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 28 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 52 | 12m | 15 km | 13.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 52 | 1h 21m | 961 km | 861.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TUTOR862 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-04-16 09:37 UTC | 2026-04-16 10:04 UTC | 27m |
| RMZ | RMZ | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-16 09:23 UTC | 2026-04-16 09:45 UTC | 22m |
| VALK06 | VAL | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-04-16 08:13 UTC | 2026-04-16 09:43 UTC | 1h 29m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-16 08:31 UTC | 2026-04-16 09:40 UTC | 1h 8m |
| SDM6315 | SDM | Pulkovo Airport (ULLI) | Staroselye Airport (UUBK) | 2026-04-16 08:59 UTC | 2026-04-16 09:36 UTC | 36m |
| UFX62 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-04-16 08:47 UTC | 2026-04-16 09:34 UTC | 47m |
| SWE22V | SWE | Lulea Airport (ESPA) | Kalixfors Airport (ESUK) | 2026-04-16 09:09 UTC | 2026-04-16 09:34 UTC | 25m |
| URSA01 | URS | Allen Army Air Field (PABI) | Ladd Army Air Field (PAFB) | 2026-04-16 08:51 UTC | 2026-04-16 09:28 UTC | 37m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-16 09:00 UTC | 2026-04-16 09:19 UTC | 19m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-04-16 08:52 UTC | 2026-04-16 09:16 UTC | 24m |
| HBMGB | HBM | St Gallen Altenrhein Airport (LSZR) | St Gallen Altenrhein Airport (LSZR) | 2026-04-16 08:56 UTC | 2026-04-16 09:07 UTC | 10m |
| OEDDJ | OED | LIAA (LIAA) | Ancona / Falconara Airport (LIPY) | 2026-04-16 08:18 UTC | 2026-04-16 09:05 UTC | 46m |
| URSA05 | URS | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-16 08:35 UTC | 2026-04-16 09:04 UTC | 29m |
| RYR3MG | Ryanair | Manchester Airport (EGCC) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-16 07:03 UTC | 2026-04-16 09:01 UTC | 1h 57m |
| RYR40HE | Ryanair | Torino / Caselle International Airport (LIMF) | Decimomannu Airport (LIED) | 2026-04-16 08:10 UTC | 2026-04-16 09:00 UTC | 50m |
| AFR34UP | Air France | Charles de Gaulle International Airport (LFPG) | Václav Havel Airport (LKPR) | 2026-04-16 07:39 UTC | 2026-04-16 08:59 UTC | 1h 19m |
| AFR29FN | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-04-16 08:01 UTC | 2026-04-16 08:58 UTC | 56m |
| KLM1523 | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | San Sebastian Airport (LESO) | 2026-04-16 07:25 UTC | 2026-04-16 08:58 UTC | 1h 33m |
| MB55G |  | Perth International Airport (YPPH) | Rothsay Mine Airport (YROT) | 2026-04-16 08:11 UTC | 2026-04-16 08:55 UTC | 44m |
| EZS87TF | EZS | Mollis Airport (LSZM) | Kukes Airport (LAKU) | 2026-04-16 07:20 UTC | 2026-04-16 08:54 UTC | 1h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
