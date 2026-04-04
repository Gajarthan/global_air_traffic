# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_04:06:02_UTC-green)

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

**Latest saved flight:** 2026-04-04 04:06:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-04 04:06:02 UTC

- **14,936** saved flights
- **8,136** unique routes
- **112** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **14,936** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **184,588.6 tonnes** estimated CO2 emissions
- **10,700,787 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 672 |
| 2 | Ryanair | 565 |
| 3 | IndiGo | 419 |
| 4 | EJA | 302 |
| 5 | American Airlines | 282 |
| 6 | Southwest Airlines | 223 |
| 7 | Lufthansa | 210 |
| 8 | ENY | 196 |
| 9 | LATAM Airlines | 159 |
| 10 | Vueling | 157 |
| 11 | AXM | 145 |
| 12 | QLK | 135 |
| 13 | LXJ | 134 |
| 14 | All Nippon Airways | 126 |
| 15 | Delta Air Lines | 123 |
| 16 | AZU | 115 |
| 17 | Swiss International | 111 |
| 18 | VIV | 110 |
| 19 | Alaska Airlines | 103 |
| 20 | United Airlines | 98 |
| 21 | WIF | 97 |
| 22 | Avianca | 95 |
| 23 | Japan Airlines | 94 |
| 24 | EDV | 93 |
| 25 | easyJet | 90 |
| 26 | AXB | 89 |
| 27 | AEE | 88 |
| 28 | BRC | 87 |
| 29 | EJU | 87 |
| 30 | Cathay Pacific | 86 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 12212 |
| 2 | 🇮🇳 IN | 1268 |
| 3 | 🇦🇺 AU | 1159 |
| 4 | 🇪🇸 ES | 1114 |
| 5 | 🇧🇷 BR | 869 |
| 6 | 🇯🇵 JP | 765 |
| 7 | 🇩🇪 DE | 758 |
| 8 | 🇨🇴 CO | 751 |
| 9 | 🇨🇦 CA | 692 |
| 10 | 🇮🇹 IT | 628 |
| 11 | 🇬🇧 GB | 565 |
| 12 | 🇲🇽 MX | 521 |
| 13 | 🇫🇷 FR | 503 |
| 14 | 🇬🇷 GR | 392 |
| 15 | 🇨🇭 CH | 374 |
| 16 | 🇳🇿 NZ | 370 |
| 17 | 🇲🇾 MY | 324 |
| 18 | 🇳🇴 NO | 315 |
| 19 | 🇿🇦 ZA | 299 |
| 20 | 🇵🇭 PH | 278 |
| 21 | 🇹🇷 TR | 270 |
| 22 | 🇬🇹 GT | 267 |
| 23 | 🇰🇷 KR | 249 |
| 24 | 🇵🇱 PL | 202 |
| 25 | 🇹🇭 TH | 198 |
| 26 | 🇲🇦 MA | 179 |
| 27 | 🇮🇩 ID | 166 |
| 28 | 🇧🇸 BS | 159 |
| 29 | 🇲🇴 MO | 157 |
| 30 | 🇲🇪 ME | 150 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 374 |
| 2 | El Dorado International Airport |  | CO | 283 |
| 3 | Denver International Airport |  | US | 279 |
| 4 | Indira Gandhi International Airport |  | IN | 269 |
| 5 | Tokyo International Airport |  | JP | 265 |
| 6 | Harry Reid International Airport |  | US | 209 |
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
| 18 | Bengaluru International Airport |  | IN | 142 |
| 19 | Atizapan De Zaragoza Airport |  | MX | 135 |
| 20 | Congonhas Airport |  | BR | 135 |
| 21 | Ninoy Aquino International Airport |  | PH | 128 |
| 22 | Madrid Barajas International Airport |  | ES | 128 |
| 23 | Salt Lake City International Airport |  | US | 120 |
| 24 | Reno/Tahoe International Airport |  | US | 118 |
| 25 | Kuala Lumpur International Airport |  | MY | 118 |
| 26 | Daniel K Inouye International Airport |  | US | 115 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 115 |
| 28 | Tenerife Norte Airport |  | ES | 114 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 114 |
| 30 | Vitoria/Foronda Airport |  | ES | 111 |
| 31 | Charles de Gaulle International Airport |  | FR | 104 |
| 32 | George Bush Intcntl/Houston Airport |  | US | 104 |
| 33 | Malpensa International Airport |  | IT | 103 |
| 34 | Austin-Bergstrom International Airport |  | US | 102 |
| 35 | Pune Airport |  | IN | 102 |
| 36 | Seattle-Tacoma International Airport |  | US | 98 |
| 37 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 98 |
| 38 | Barcelona International Airport |  | ES | 97 |
| 39 | Miami International Airport |  | US | 96 |
| 40 | General Edward Lawrence Logan International Airport |  | US | 94 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 70 | 14m | 114 km | 137.3 t |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 64 | 1h 7m | 706 km | 779.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 55 | 24m | 225 km | 213.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 47 | 29m | 304 km | 246.4 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 44 | 1h 46m | 1,156 km | 877.8 t |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 42 | 31m | - | - |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 39 | 1h 26m | 910 km | 612.0 t |
| 9 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 37 | 16m | 206 km | 131.5 t |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 37 | 22m | 99 km | 63.4 t |
| 11 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 35 | 27m | 152 km | 91.5 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 34 | 28m | 275 km | 161.1 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 34 | 20m | 165 km | 96.7 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 32 | 1h 54m | 1,304 km | 719.9 t |
| 16 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 32 | 53m | 556 km | 306.7 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 31 | 53m | 546 km | 291.9 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 31 | 30m | 369 km | 197.3 t |
| 19 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 29 | 1h 10m | 770 km | 385.2 t |
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
| VAR515 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-04-04 03:16 UTC | 2026-04-04 04:06 UTC | 49m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 03:50 UTC | 2026-04-04 04:03 UTC | 13m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-04-03 16:39 UTC | 2026-04-04 03:55 UTC | 11h 15m |
| AAR522 | AAR | London Heathrow Airport (EGLL) | Incheon International Airport (RKSI) | 2026-04-03 16:11 UTC | 2026-04-04 03:37 UTC | 11h 26m |
| N495LP |  | K00V (K00V) | Cuchara Ranch Airport (CD48) | 2026-04-04 02:50 UTC | 2026-04-04 03:32 UTC | 41m |
| RXA2113 | RXA | Perth International Airport (YPPH) | Denmark Airport (YDEK) | 2026-04-04 02:42 UTC | 2026-04-04 03:25 UTC | 42m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-04 03:13 UTC | 2026-04-04 03:25 UTC | 11m |
| VIR155M | Virgin Atlantic | London Heathrow Airport (EGLL) | Harry Reid International Airport (KLAS) | 2026-04-03 17:31 UTC | 2026-04-04 03:23 UTC | 9h 52m |
| TOG30 | TOG | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-04-04 02:40 UTC | 2026-04-04 03:20 UTC | 40m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Annette Island Airport (PANT) | 2026-04-04 01:47 UTC | 2026-04-04 03:20 UTC | 1h 32m |
| DAL710 | Delta Air Lines | Laguardia Airport (KLGA) | Denver International Airport (KDEN) | 2026-04-03 23:19 UTC | 2026-04-04 03:18 UTC | 3h 59m |
| FD604 |  | Perth Jandakot Airport (YPJT) | Leeman Airport (YLEA) | 2026-04-04 02:35 UTC | 2026-04-04 03:17 UTC | 41m |
| MABTE | MAB | London Stansted Airport (EGSS) | Tenerife South Airport (GCTS) | 2026-04-03 23:17 UTC | 2026-04-04 03:10 UTC | 3h 53m |
| AXM1491 | AXM | Tan Son Nhat International Airport (VVTS) | Mersing Airport (WMAU) | 2026-04-04 01:51 UTC | 2026-04-04 03:09 UTC | 1h 18m |
| QXE2414 | QXE | Seattle-Tacoma International Airport (KSEA) | 3 Rivers Recreation Area Airport (OG00) | 2026-04-04 02:35 UTC | 2026-04-04 03:08 UTC | 33m |
| ANA375 | All Nippon Airways | Tokyo International Airport (RJTT) | Asahikawa Airport (RJEC) | 2026-04-04 02:01 UTC | 2026-04-04 03:07 UTC | 1h 6m |
| ASA1182 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Kahului Airport (PHOG) | 2026-04-04 02:46 UTC | 2026-04-04 03:02 UTC | 16m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-04-04 02:37 UTC | 2026-04-04 03:02 UTC | 24m |
| N57BF |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-04-04 02:43 UTC | 2026-04-04 03:02 UTC | 19m |
| EJA157 | EJA | Oakland San Francisco Bay Airport (KOAK) | Napa County Airport (KAPC) | 2026-04-04 02:47 UTC | 2026-04-04 03:01 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
