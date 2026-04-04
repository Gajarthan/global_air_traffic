# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_18:47:56_UTC-green)

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

**Latest saved flight:** 2026-04-04 18:47:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 18:47:56 UTC

- **16,470** saved flights
- **8,736** unique routes
- **113** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **16,470** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **204,451.6 tonnes** estimated CO2 emissions
- **11,852,264 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 703 |
| 2 | Ryanair | 668 |
| 3 | IndiGo | 477 |
| 4 | EJA | 311 |
| 5 | American Airlines | 294 |
| 6 | Lufthansa | 236 |
| 7 | Southwest Airlines | 234 |
| 8 | ENY | 212 |
| 9 | Vueling | 183 |
| 10 | LATAM Airlines | 175 |
| 11 | AXM | 160 |
| 12 | All Nippon Airways | 141 |
| 13 | LXJ | 140 |
| 14 | QLK | 137 |
| 15 | Delta Air Lines | 135 |
| 16 | AZU | 125 |
| 17 | Swiss International | 123 |
| 18 | VIV | 120 |
| 19 | EJU | 109 |
| 20 | Japan Airlines | 107 |
| 21 | Alaska Airlines | 106 |
| 22 | AEE | 105 |
| 23 | Avianca | 104 |
| 24 | AXB | 103 |
| 25 | WIF | 102 |
| 26 | easyJet | 101 |
| 27 | EDV | 99 |
| 28 | United Airlines | 99 |
| 29 | BRC | 97 |
| 30 | GLO | 95 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 13001 |
| 2 | 🇮🇳 IN | 1451 |
| 3 | 🇪🇸 ES | 1357 |
| 4 | 🇦🇺 AU | 1210 |
| 5 | 🇧🇷 BR | 959 |
| 6 | 🇩🇪 DE | 865 |
| 7 | 🇯🇵 JP | 860 |
| 8 | 🇨🇴 CO | 831 |
| 9 | 🇮🇹 IT | 765 |
| 10 | 🇨🇦 CA | 729 |
| 11 | 🇬🇧 GB | 642 |
| 12 | 🇫🇷 FR | 605 |
| 13 | 🇲🇽 MX | 560 |
| 14 | 🇬🇷 GR | 457 |
| 15 | 🇨🇭 CH | 442 |
| 16 | 🇳🇿 NZ | 379 |
| 17 | 🇲🇾 MY | 368 |
| 18 | 🇿🇦 ZA | 348 |
| 19 | 🇳🇴 NO | 338 |
| 20 | 🇬🇹 GT | 314 |
| 21 | 🇵🇭 PH | 305 |
| 22 | 🇹🇷 TR | 302 |
| 23 | 🇰🇷 KR | 291 |
| 24 | 🇵🇱 PL | 235 |
| 25 | 🇹🇭 TH | 232 |
| 26 | 🇲🇦 MA | 201 |
| 27 | 🇧🇸 BS | 180 |
| 28 | 🇮🇩 ID | 177 |
| 29 | 🇲🇪 ME | 169 |
| 30 | 🇲🇴 MO | 165 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 387 |
| 2 | El Dorado International Airport |  | CO | 311 |
| 3 | Indira Gandhi International Airport |  | IN | 300 |
| 4 | Tokyo International Airport |  | JP | 299 |
| 5 | Denver International Airport |  | US | 295 |
| 6 | La Aurora Airport |  | GT | 221 |
| 7 | Harry Reid International Airport |  | US | 217 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 215 |
| 9 | Frankfurt am Main International Airport |  | DE | 212 |
| 10 | Zurich Airport |  | CH | 201 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 177 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 175 |
| 13 | Guaymaral Airport |  | CO | 175 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 166 |
| 15 | Macau International Airport |  | MO | 165 |
| 16 | Bengaluru International Airport |  | IN | 160 |
| 17 | Chicago O'Hare International Airport |  | US | 152 |
| 18 | Charlotte/Douglas International Airport |  | US | 151 |
| 19 | Madrid Barajas International Airport |  | ES | 150 |
| 20 | Congonhas Airport |  | BR | 150 |
| 21 | Tenerife Norte Airport |  | ES | 146 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 144 |
| 23 | Ninoy Aquino International Airport |  | PH | 140 |
| 24 | Netaji Subhash Chandra Bose International Airport |  | IN | 136 |
| 25 | Reno/Tahoe International Airport |  | US | 130 |
| 26 | Kuala Lumpur International Airport |  | MY | 130 |
| 27 | Malpensa International Airport |  | IT | 128 |
| 28 | Daniel K Inouye International Airport |  | US | 127 |
| 29 | Salt Lake City International Airport |  | US | 127 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 125 |
| 31 | Charles de Gaulle International Airport |  | FR | 122 |
| 32 | Vitoria/Foronda Airport |  | ES | 121 |
| 33 | Barcelona International Airport |  | ES | 117 |
| 34 | George Bush Intcntl/Houston Airport |  | US | 112 |
| 35 | Miami International Airport |  | US | 110 |
| 36 | Pune Airport |  | IN | 110 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 109 |
| 38 | General Edward Lawrence Logan International Airport |  | US | 108 |
| 39 | Austin-Bergstrom International Airport |  | US | 103 |
| 40 | Gimpo International Airport |  | KR | 101 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 75 | 14m | 114 km | 147.1 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 73 | 1h 8m | 706 km | 888.8 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 67 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 59 | 24m | 225 km | 228.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 57 | 29m | 304 km | 298.8 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 49 | 1h 45m | 1,156 km | 977.5 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 49 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 47 | 1h 26m | 910 km | 737.5 t |
| 9 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 45 | 26m | 152 km | 117.6 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 43 | 22m | 99 km | 73.7 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 41 | 16m | 206 km | 145.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 37 | 28m | 275 km | 175.3 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 36 | 19m | 165 km | 102.4 t |
| 14 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 36 | 52m | 556 km | 345.1 t |
| 16 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 34 | 1h 11m | 770 km | 451.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 34 | 30m | 369 km | 216.4 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 34 | 1h 54m | 1,304 km | 764.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 31 | 1h 43m | 1,423 km | 760.8 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 31 | 23m | 252 km | 134.6 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 30 | 9m | - | - |
| 23 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 29 | 59m | 723 km | 361.5 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 28 | 13m | 99 km | 48.0 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 28 | 11m | 127 km | 61.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 27 | 20m | 147 km | 68.3 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 27 | 46m | 452 km | 210.4 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 25 | 16m | 183 km | 78.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 24 | 52m | 493 km | 204.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 24 | 1h 20m | 961 km | 397.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-04-04 18:26 UTC | 2026-04-04 18:47 UTC | 21m |
| N1931H |  | Salt Lake City International Airport (KSLC) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-04 18:23 UTC | 2026-04-04 18:44 UTC | 21m |
| CXK699 | CXK | Centennial Airport (KAPA) | Colorado Plains Regional Airport (KAKO) | 2026-04-04 17:51 UTC | 2026-04-04 18:42 UTC | 51m |
| N9863L |  | Republic Airport (KFRG) | Francis S Gabreski Airport (KFOK) | 2026-04-04 18:06 UTC | 2026-04-04 18:36 UTC | 29m |
| ACA43 | Air Canada | Indira Gandhi International Airport (VIDP) | Sirsa Air Force Station (VISA) | 2026-04-04 18:17 UTC | 2026-04-04 18:35 UTC | 18m |
| N108RF |  | Pensacola International Airport (KPNS) | Spencer Nolf Airport (KNRQ) | 2026-04-04 18:04 UTC | 2026-04-04 18:35 UTC | 31m |
| N357PA |  | Sheep Mountain Airport (PASP) | Sheep Mountain Airport (PASP) | 2026-04-04 18:34 UTC | 2026-04-04 18:35 UTC | 1m |
| N848BG |  | Neversweat Airport (1OK0) | Cushing Municipal Airport (KCUH) | 2026-04-04 18:23 UTC | 2026-04-04 18:34 UTC | 10m |
| MEECMMS | MEE | Zaragoza Air Base (LEZG) | Zaragoza Air Base (LEZG) | 2026-04-04 18:19 UTC | 2026-04-04 18:30 UTC | 11m |
| N74SW |  | Logan-Cache Airport (KLGU) | K36U (K36U) | 2026-04-04 17:50 UTC | 2026-04-04 18:28 UTC | 38m |
| N5178S |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-04 17:43 UTC | 2026-04-04 18:27 UTC | 43m |
| N6776A |  | Coopers Landing Airport (0WN2) | Rugg Ranches Airport (45OG) | 2026-04-04 17:48 UTC | 2026-04-04 18:21 UTC | 33m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-04 18:13 UTC | 2026-04-04 18:20 UTC | 6m |
| N38HL |  | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-04-04 17:56 UTC | 2026-04-04 18:19 UTC | 22m |
| OST10 | OST | Stillwater Regional Airport (KSWO) | Chandler Regional Airport (KCQB) | 2026-04-04 18:03 UTC | 2026-04-04 18:19 UTC | 16m |
| N217AT |  | Redlands Municipal Airport (KREI) | Big Bear City Airport (KL35) | 2026-04-04 18:01 UTC | 2026-04-04 18:18 UTC | 17m |
| N90LE |  | Orlando International Airport (KMCO) | Toronto Pearson International Airport (CYYZ) | 2026-04-04 16:04 UTC | 2026-04-04 18:16 UTC | 2h 12m |
| BRCAT14 | BRC | 81NM (81NM) | Roswell Air Center Airport (KROW) | 2026-04-04 17:32 UTC | 2026-04-04 18:16 UTC | 44m |
| N65474 |  | Ohkay Owingeh Airport (KE14) | Ohkay Owingeh Airport (KE14) | 2026-04-04 17:54 UTC | 2026-04-04 18:16 UTC | 21m |
| N7103Q |  | Jim & Julie's Airport (96WA) | 3WA1 (3WA1) | 2026-04-04 17:51 UTC | 2026-04-04 18:14 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
