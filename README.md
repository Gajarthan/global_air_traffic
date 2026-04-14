# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_11:24:29_UTC-green)

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

**Latest saved flight:** 2026-04-14 11:24:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 11:24:29 UTC

- **33,823** saved flights
- **15,022** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,823** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **416,490.7 tonnes** estimated CO2 emissions
- **24,144,390 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1445 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 855 |
| 4 | American Airlines | 585 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 379 |
| 9 | AXM | 360 |
| 10 | Vueling | 344 |
| 11 | LATAM Airlines | 337 |
| 12 | All Nippon Airways | 309 |
| 13 | AZU | 298 |
| 14 | QLK | 289 |
| 15 | Delta Air Lines | 286 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 261 |
| 18 | WIF | 238 |
| 19 | easyJet | 229 |
| 20 | Alaska Airlines | 228 |
| 21 | EJU | 225 |
| 22 | AEE | 220 |
| 23 | VIV | 218 |
| 24 | Japan Airlines | 214 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 184 |
| 28 | Air France | 183 |
| 29 | Avianca | 181 |
| 30 | JetBlue | 180 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26449 |
| 2 | 🇮🇳 IN | 2624 |
| 3 | 🇪🇸 ES | 2540 |
| 4 | 🇦🇺 AU | 2413 |
| 5 | 🇧🇷 BR | 1981 |
| 6 | 🇯🇵 JP | 1864 |
| 7 | 🇮🇹 IT | 1817 |
| 8 | 🇩🇪 DE | 1713 |
| 9 | 🇨🇴 CO | 1675 |
| 10 | 🇨🇦 CA | 1646 |
| 11 | 🇬🇧 GB | 1387 |
| 12 | 🇫🇷 FR | 1253 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 989 |
| 15 | 🇨🇭 CH | 937 |
| 16 | 🇲🇾 MY | 869 |
| 17 | 🇳🇴 NO | 777 |
| 18 | 🇳🇿 NZ | 726 |
| 19 | 🇿🇦 ZA | 704 |
| 20 | 🇵🇭 PH | 650 |
| 21 | 🇹🇷 TR | 629 |
| 22 | 🇹🇭 TH | 615 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 582 |
| 25 | 🇵🇱 PL | 529 |
| 26 | 🇲🇦 MA | 429 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 338 |
| 29 | 🇳🇱 NL | 329 |
| 30 | 🇮🇩 ID | 326 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 803 |
| 2 | Tokyo International Airport |  | JP | 635 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 559 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 482 |
| 7 | Harry Reid International Airport |  | US | 443 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 423 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Kuala Lumpur International Airport |  | MY | 333 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 331 |
| 16 | Frankfurt am Main International Airport |  | DE | 330 |
| 17 | Macau International Airport |  | MO | 320 |
| 18 | Madrid Barajas International Airport |  | ES | 309 |
| 19 | Charlotte/Douglas International Airport |  | US | 306 |
| 20 | Bengaluru International Airport |  | IN | 303 |
| 21 | Ninoy Aquino International Airport |  | PH | 300 |
| 22 | Tenerife Norte Airport |  | ES | 298 |
| 23 | Congonhas Airport |  | BR | 296 |
| 24 | Malpensa International Airport |  | IT | 278 |
| 25 | Daniel K Inouye International Airport |  | US | 259 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Charles de Gaulle International Airport |  | FR | 247 |
| 29 | Capua Airport |  | IT | 247 |
| 30 | Reno/Tahoe International Airport |  | US | 243 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 237 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 236 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 232 |
| 34 | O. R. Tambo International Airport |  | ZA | 230 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 36 | Vitoria/Foronda Airport |  | ES | 226 |
| 37 | Barcelona International Airport |  | ES | 219 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 212 |
| 40 | Viracopos International Airport |  | BR | 206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 160 | 1h 8m | 706 km | 1,948.0 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 126 | 24m | 225 km | 488.8 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 112 | 28m | 304 km | 587.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 98 | 1h 27m | 910 km | 1,537.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 90 | 19m | 165 km | 256.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 85 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 76 | 21m | 244 km | 320.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 74 | 27m | 275 km | 350.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 72 | 1h 11m | 770 km | 956.5 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 66 | 31m | 369 km | 420.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 63 | 45m | 452 km | 491.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 59 | 20m | 250 km | 254.8 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 55 | 20m | 147 km | 139.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 51 | 16m | 162 km | 143.0 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 49 | 23m | 252 km | 212.7 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 47 | 14m | 154 km | 124.5 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DKADC | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-14 11:02 UTC | 2026-04-14 11:24 UTC | 22m |
| N79018 |  | Tagua Agropecuaria Airport (SWUJ) | Tagua Agropecuaria Airport (SWUJ) | 2026-04-14 10:57 UTC | 2026-04-14 11:16 UTC | 18m |
| DEMON3 | DEM | Eindhoven Airport (EHEH) | Volkel Air Base (EHVK) | 2026-04-14 10:56 UTC | 2026-04-14 11:10 UTC | 14m |
| FCOOO | FCO | Lyon Corbas Airport (LFHJ) | Lyon Corbas Airport (LFHJ) | 2026-04-14 10:52 UTC | 2026-04-14 11:08 UTC | 15m |
| GOBBI | GOB | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-04-14 10:38 UTC | 2026-04-14 11:06 UTC | 28m |
| WIF5WP | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-14 10:43 UTC | 2026-04-14 10:54 UTC | 10m |
| ZSSGO | ZSS | Frankfort Airport (FAFF) | Heidelburg Airport (FAHG) | 2026-04-14 10:26 UTC | 2026-04-14 10:43 UTC | 16m |
| RYR769V | Ryanair | Lamezia Terme Airport (LICA) | Malpensa International Airport (LIMC) | 2026-04-14 09:06 UTC | 2026-04-14 10:38 UTC | 1h 32m |
| UN32 |  | Daegu Airport (RKTN) | Muan International Airport (RKJB) | 2026-04-14 09:37 UTC | 2026-04-14 10:27 UTC | 50m |
| AXB1752 | AXB | Netaji Subhash Chandra Bose International Airport (VECC) | Agartala Airport (VEAT) | 2026-04-14 09:52 UTC | 2026-04-14 10:27 UTC | 35m |
| ANE1121 | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-04-14 09:51 UTC | 2026-04-14 10:27 UTC | 35m |
| RYR877 | Ryanair | Torino / Caselle International Airport (LIMF) | Crotone Airport (LIBC) | 2026-04-14 09:00 UTC | 2026-04-14 10:24 UTC | 1h 24m |
| SFJ69 | SFJ | Matsumoto Airport (RJAF) | Ozuki Airport (RJOZ) | 2026-04-14 09:36 UTC | 2026-04-14 10:24 UTC | 47m |
| HMZ8268 | HMZ | Sheremetyevo International Airport (UUEE) | Tbilisi International Airport (UGTB) | 2026-04-14 07:36 UTC | 2026-04-14 10:22 UTC | 2h 45m |
| AEE204 | AEE | Eleftherios Venizelos International Airport (LGAV) | Diagoras Airport (LGRP) | 2026-04-14 09:41 UTC | 2026-04-14 10:21 UTC | 40m |
| ROT643C | ROT | Henri Coanda International Airport (LROP) | Cluj-Napoca International Airport (LRCL) | 2026-04-14 09:32 UTC | 2026-04-14 10:20 UTC | 48m |
| FJO66L | FJO | Malaga Airport (LEMG) | Berlin Brandenburg Airport (EDDB) | 2026-04-14 07:13 UTC | 2026-04-14 10:18 UTC | 3h 5m |
| IGO411Y | IndiGo | Biju Patnaik Airport (VEBS) | Baglung Airport (VNBL) | 2026-04-14 05:24 UTC | 2026-04-14 10:17 UTC | 4h 53m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-14 09:47 UTC | 2026-04-14 10:17 UTC | 30m |
| 13009R4 |  | Hamburg-Finkenwerder Airport (EDHI) | Hamburg-Finkenwerder Airport (EDHI) | 2026-04-14 10:17 UTC | 2026-04-14 10:17 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
