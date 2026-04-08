# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_18:44:13_UTC-green)

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

**Latest saved flight:** 2026-04-08 18:44:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 18:44:13 UTC

- **23,728** saved flights
- **11,522** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **23,728** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **293,465.3 tonnes** estimated CO2 emissions
- **17,012,479 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 986 |
| 2 | Ryanair | 979 |
| 3 | IndiGo | 663 |
| 4 | American Airlines | 430 |
| 5 | EJA | 426 |
| 6 | Southwest Airlines | 335 |
| 7 | Lufthansa | 308 |
| 8 | ENY | 308 |
| 9 | Vueling | 248 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 235 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 202 |
| 15 | LXJ | 193 |
| 16 | AZU | 186 |
| 17 | Swiss International | 173 |
| 18 | Japan Airlines | 162 |
| 19 | VIV | 162 |
| 20 | Alaska Airlines | 159 |
| 21 | easyJet | 159 |
| 22 | EJU | 155 |
| 23 | AEE | 150 |
| 24 | WIF | 150 |
| 25 | United Airlines | 147 |
| 26 | Avianca | 142 |
| 27 | EDV | 138 |
| 28 | AXB | 137 |
| 29 | Air France | 125 |
| 30 | Wizz Air | 121 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18457 |
| 2 | 🇮🇳 IN | 2021 |
| 3 | 🇪🇸 ES | 1823 |
| 4 | 🇦🇺 AU | 1750 |
| 5 | 🇯🇵 JP | 1349 |
| 6 | 🇧🇷 BR | 1322 |
| 7 | 🇩🇪 DE | 1224 |
| 8 | 🇮🇹 IT | 1214 |
| 9 | 🇨🇴 CO | 1209 |
| 10 | 🇨🇦 CA | 1068 |
| 11 | 🇬🇧 GB | 974 |
| 12 | 🇫🇷 FR | 881 |
| 13 | 🇲🇽 MX | 765 |
| 14 | 🇬🇷 GR | 685 |
| 15 | 🇨🇭 CH | 663 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇿🇦 ZA | 516 |
| 18 | 🇳🇴 NO | 510 |
| 19 | 🇳🇿 NZ | 499 |
| 20 | 🇬🇹 GT | 476 |
| 21 | 🇹🇷 TR | 459 |
| 22 | 🇵🇭 PH | 449 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 390 |
| 25 | 🇵🇱 PL | 350 |
| 26 | 🇲🇦 MA | 289 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇧🇸 BS | 247 |
| 29 | 🇲🇪 ME | 245 |
| 30 | 🇳🇱 NL | 239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 560 |
| 2 | El Dorado International Airport |  | CO | 449 |
| 3 | Tokyo International Airport |  | JP | 448 |
| 4 | Indira Gandhi International Airport |  | IN | 415 |
| 5 | Denver International Airport |  | US | 413 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 334 |
| 7 | La Aurora Airport |  | GT | 328 |
| 8 | Harry Reid International Airport |  | US | 312 |
| 9 | Zurich Airport |  | CH | 286 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Guaymaral Airport |  | CO | 248 |
| 12 | Chicago O'Hare International Airport |  | US | 247 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 246 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 243 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 16 | Bengaluru International Airport |  | IN | 227 |
| 17 | Macau International Airport |  | MO | 226 |
| 18 | Charlotte/Douglas International Airport |  | US | 222 |
| 19 | Kuala Lumpur International Airport |  | MY | 211 |
| 20 | Madrid Barajas International Airport |  | ES | 209 |
| 21 | Tenerife Norte Airport |  | ES | 208 |
| 22 | Ninoy Aquino International Airport |  | PH | 207 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 193 |
| 25 | Congonhas Airport |  | BR | 190 |
| 26 | Salt Lake City International Airport |  | US | 185 |
| 27 | Daniel K Inouye International Airport |  | US | 179 |
| 28 | Reno/Tahoe International Airport |  | US | 178 |
| 29 | Charles de Gaulle International Airport |  | FR | 173 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 165 |
| 32 | O. R. Tambo International Airport |  | ZA | 161 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 157 |
| 34 | Miami International Airport |  | US | 157 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 157 |
| 36 | Vitoria/Foronda Airport |  | ES | 154 |
| 37 | Pune Airport |  | IN | 154 |
| 38 | Barcelona International Airport |  | ES | 153 |
| 39 | Seattle-Tacoma International Airport |  | US | 151 |
| 40 | Gimpo International Airport |  | KR | 141 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 97 | 14m | 114 km | 190.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 91 | 26m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 64 | 1h 42m | 1,156 km | 1,276.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 46 | 52m | 556 km | 440.9 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 41 | 1h 43m | 1,423 km | 1,006.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 35 | 12m | 15 km | 9.2 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N983FA |  | Breezy Knoll Airport (VA13) | 94VA (94VA) | 2026-04-08 18:22 UTC | 2026-04-08 18:44 UTC | 21m |
| C02 |  | Krems Airport (LOAG) | Brumowski  Air Base (LOXT) | 2026-04-08 18:33 UTC | 2026-04-08 18:43 UTC | 10m |
| N15MJ |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-04-08 18:02 UTC | 2026-04-08 18:36 UTC | 34m |
| RYR49CF | Ryanair | London Stansted Airport (EGSS) | Olbia / Costa Smeralda Airport (LIEO) | 2026-04-08 16:44 UTC | 2026-04-08 18:36 UTC | 1h 51m |
| N54803 |  | Schenectady County Airport (KSCH) | Hiserts Airpark Inc Airport (3NY7) | 2026-04-08 18:14 UTC | 2026-04-08 18:35 UTC | 20m |
| N2946B |  | Reading Regional/Carl A Spaatz Field (KRDG) | Penn Valley Airport (KSEG) | 2026-04-08 18:14 UTC | 2026-04-08 18:35 UTC | 20m |
| BLZR250 | BLZ | Kingsville Nas Airport (KNQI) | Duval County Ranch Company Airport (28TA) | 2026-04-08 18:11 UTC | 2026-04-08 18:34 UTC | 22m |
| N742TW |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-08 18:17 UTC | 2026-04-08 18:33 UTC | 16m |
| N831X |  | Roberts Field (KRDM) | Dry Creek Airpark (OG21) | 2026-04-08 18:04 UTC | 2026-04-08 18:27 UTC | 23m |
| RFS721 | RFS | Auburn Municipal Airport (KS50) | Jim & Julie's Airport (96WA) | 2026-04-08 17:41 UTC | 2026-04-08 18:27 UTC | 46m |
| BRCAT11 | BRC | Jenkins Airport (NM87) | 81NM (81NM) | 2026-04-08 17:40 UTC | 2026-04-08 18:19 UTC | 39m |
| PSLMS | PSL | Fazenda Nossa Senhora das Gracas Airport (SWNG) | Fazenda Nossa Senhora das Gracas Airport (SWNG) | 2026-04-08 17:01 UTC | 2026-04-08 18:18 UTC | 1h 17m |
| CGFDG | CGF | Three Hills Airport (CEN3) | Calgary / Springbank Airport (CYBW) | 2026-04-08 17:34 UTC | 2026-04-08 18:16 UTC | 42m |
| N613KA |  | Madison Regional Airport (KIMS) | Owen Air Park (0KY0) | 2026-04-08 18:01 UTC | 2026-04-08 18:15 UTC | 14m |
| SH124 |  | Thomas Farms Airport (85FL) | Atmore Municipal Airport (K0R1) | 2026-04-08 17:39 UTC | 2026-04-08 18:13 UTC | 34m |
|  |  | Whidbey Island Nas (Ault Field) Airport (KNUW) | Mineral County Airport (K9S4) | 2026-04-08 17:22 UTC | 2026-04-08 18:09 UTC | 46m |
| ARCAS31 | ARC | 4TA5 (4TA5) | TX20 (TX20) | 2026-04-08 17:51 UTC | 2026-04-08 18:08 UTC | 17m |
| N445B |  | Doylestown Airport (KDYL) | Quakertown Airport (KUKT) | 2026-04-08 17:52 UTC | 2026-04-08 18:08 UTC | 15m |
| N528LP |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-08 17:24 UTC | 2026-04-08 18:06 UTC | 42m |
| SUMIT17 | SUM | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-08 17:19 UTC | 2026-04-08 18:06 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
