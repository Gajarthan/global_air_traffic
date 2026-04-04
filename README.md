# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_02:01:48_UTC-green)

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

**Latest saved flight:** 2026-04-04 02:01:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 02:01:48 UTC

- **14,870** saved flights
- **8,120** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,870** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **183,462.1 tonnes** estimated CO2 emissions
- **10,635,482 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 565 |
| 3 | IndiGo | 410 |
| 4 | EJA | 301 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 221 |
| 7 | Lufthansa | 210 |
| 8 | ENY | 196 |
| 9 | LATAM Airlines | 159 |
| 10 | Vueling | 157 |
| 11 | AXM | 143 |
| 12 | LXJ | 134 |
| 13 | QLK | 132 |
| 14 | All Nippon Airways | 124 |
| 15 | Delta Air Lines | 122 |
| 16 | AZU | 115 |
| 17 | Swiss International | 111 |
| 18 | VIV | 110 |
| 19 | Alaska Airlines | 100 |
| 20 | United Airlines | 98 |
| 21 | WIF | 97 |
| 22 | Avianca | 95 |
| 23 | EDV | 93 |
| 24 | Japan Airlines | 92 |
| 25 | easyJet | 90 |
| 26 | AXB | 89 |
| 27 | AEE | 88 |
| 28 | BRC | 87 |
| 29 | EJU | 87 |
| 30 | Cathay Pacific | 85 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12174 |
| 2 | 🇮🇳 IN | 1248 |
| 3 | 🇦🇺 AU | 1142 |
| 4 | 🇪🇸 ES | 1113 |
| 5 | 🇧🇷 BR | 869 |
| 6 | 🇩🇪 DE | 757 |
| 7 | 🇯🇵 JP | 752 |
| 8 | 🇨🇴 CO | 749 |
| 9 | 🇨🇦 CA | 690 |
| 10 | 🇮🇹 IT | 628 |
| 11 | 🇬🇧 GB | 561 |
| 12 | 🇲🇽 MX | 517 |
| 13 | 🇫🇷 FR | 503 |
| 14 | 🇬🇷 GR | 392 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 363 |
| 17 | 🇲🇾 MY | 321 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇵🇭 PH | 274 |
| 21 | 🇹🇷 TR | 269 |
| 22 | 🇬🇹 GT | 267 |
| 23 | 🇰🇷 KR | 245 |
| 24 | 🇵🇱 PL | 202 |
| 25 | 🇹🇭 TH | 196 |
| 26 | 🇲🇦 MA | 179 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇧🇸 BS | 159 |
| 29 | 🇲🇴 MO | 157 |
| 30 | 🇲🇪 ME | 150 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 374 |
| 2 | El Dorado International Airport |  | CO | 282 |
| 3 | Denver International Airport |  | US | 278 |
| 4 | Indira Gandhi International Airport |  | IN | 265 |
| 5 | Tokyo International Airport |  | JP | 260 |
| 6 | Harry Reid International Airport |  | US | 206 |
| 7 | Frankfurt am Main International Airport |  | DE | 196 |
| 8 | La Aurora Airport |  | GT | 187 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 183 |
| 10 | Zurich Airport |  | CH | 175 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 172 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 166 |
| 13 | Macau International Airport |  | MO | 157 |
| 14 | Guaymaral Airport |  | CO | 157 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 152 |
| 16 | Chicago O'Hare International Airport |  | US | 147 |
| 17 | Charlotte/Douglas International Airport |  | US | 142 |
| 18 | Bengaluru International Airport |  | IN | 141 |
| 19 | Congonhas Airport |  | BR | 135 |
| 20 | Atizapan De Zaragoza Airport |  | MX | 134 |
| 21 | Madrid Barajas International Airport |  | ES | 128 |
| 22 | Ninoy Aquino International Airport |  | PH | 126 |
| 23 | Salt Lake City International Airport |  | US | 120 |
| 24 | Kuala Lumpur International Airport |  | MY | 118 |
| 25 | Reno/Tahoe International Airport |  | US | 117 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 115 |
| 27 | Tenerife Norte Airport |  | ES | 114 |
| 28 | Daniel K Inouye International Airport |  | US | 112 |
| 29 | Vitoria/Foronda Airport |  | ES | 111 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 110 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 33 | Malpensa International Airport |  | IT | 103 |
| 34 | Austin-Bergstrom International Airport |  | US | 102 |
| 35 | Pune Airport |  | IN | 101 |
| 36 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 37 | Barcelona International Airport |  | ES | 97 |
| 38 | Miami International Airport |  | US | 96 |
| 39 | Seattle-Tacoma International Airport |  | US | 96 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 94 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 69 | 14m | 114 km | 135.3 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 64 | 1h 7m | 706 km | 779.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 53 | 24m | 225 km | 205.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 46 | 29m | 304 km | 241.1 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 43 | 1h 46m | 1,156 km | 857.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 41 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 37 | 1h 26m | 910 km | 580.6 t |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 36 | 16m | 206 km | 128.0 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 31 | 30m | 369 km | 197.3 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 28 | 1h 10m | 770 km | 372.0 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 27 | 1h 43m | 1,423 km | 662.6 t |
| 21 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 27 | 59m | 723 km | 336.6 t |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 26 | 23m | 252 km | 112.9 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 26 | 9m | - | - |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 25 | 20m | 147 km | 63.3 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 24 | 11m | 127 km | 52.5 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 23 | 13m | 99 km | 39.4 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 22 | 44m | 452 km | 171.5 t |
| 28 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 22 | 16m | 183 km | 69.4 t |
| 29 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 21 | 1h 15m | 924 km | 334.9 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 20 | 12m | 15 km | 5.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TRP7 | TRP | St Mary's County Regional Airport (K2W6) | Joint Base Andrews Airport (KADW) | 2026-04-04 01:29 UTC | 2026-04-04 02:01 UTC | 32m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-04-04 01:21 UTC | 2026-04-04 01:32 UTC | 10m |
| LBQ783 | LBQ | Gainesville Regional Airport (KGNV) | Tampa Executive Airport (KVDF) | 2026-04-04 01:04 UTC | 2026-04-04 01:31 UTC | 27m |
| EJA818 | EJA | Moffett Federal Airfield (KNUQ) | Truckee-Tahoe Airport (KTRK) | 2026-04-04 00:58 UTC | 2026-04-04 01:28 UTC | 30m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 01:17 UTC | 2026-04-04 01:27 UTC | 10m |
| QLK223D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-04-04 00:41 UTC | 2026-04-04 01:18 UTC | 36m |
| DRK203 | DRK | Indira Gandhi International Airport (VIDP) | Bagdogra Airport (VEBD) | 2026-04-03 23:52 UTC | 2026-04-04 01:15 UTC | 1h 22m |
| N363K |  | Palo Alto Airport (KPAO) | San Martin Airport (KE16) | 2026-04-03 23:31 UTC | 2026-04-04 01:13 UTC | 1h 42m |
| UAL599 | United Airlines | Washington Dulles International Airport (KIAD) | Denver International Airport (KDEN) | 2026-04-03 21:46 UTC | 2026-04-04 01:12 UTC | 3h 26m |
| EJA477 | EJA | San Francisco International Airport (KSFO) | Sierraville Dearwater Airport (KO79) | 2026-04-04 00:42 UTC | 2026-04-04 01:10 UTC | 27m |
| ANZ268L | ANZ | Auckland International Airport (NZAA) | Whangarei Airport (NZWR) | 2026-04-04 00:47 UTC | 2026-04-04 01:09 UTC | 21m |
| AXEL10 | AXE | Roswell Air Center Airport (KROW) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-04-04 00:27 UTC | 2026-04-04 01:08 UTC | 40m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-04 00:49 UTC | 2026-04-04 01:08 UTC | 19m |
| EJA526 | EJA | Chicago O'Hare International Airport (KORD) | Springhill Airport (KSPH) | 2026-04-03 23:26 UTC | 2026-04-04 01:05 UTC | 1h 39m |
| N831MT |  | Mobile International Airport (KBFM) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-03 20:39 UTC | 2026-04-04 01:00 UTC | 4h 20m |
| SKW768J | SkyWest Airlines | Denver International Airport (KDEN) | Smith Field (8NE3) | 2026-04-04 00:38 UTC | 2026-04-04 00:59 UTC | 20m |
| CFH24 | CFH | Newcastle Airport (YWLM) | Walcha Airport (YWCH) | 2026-04-04 00:27 UTC | 2026-04-04 00:59 UTC | 31m |
| AAL2912 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Laguardia Airport (KLGA) | 2026-04-03 23:30 UTC | 2026-04-04 00:58 UTC | 1h 28m |
| POE247 | POE | Ottawa / Macdonald-Cartier International Airport (CYOW) | Stanley Airport (CCW4) | 2026-04-03 23:57 UTC | 2026-04-04 00:57 UTC | 1h 0m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 00:44 UTC | 2026-04-04 00:57 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
