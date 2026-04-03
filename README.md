# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_04:25:34_UTC-green)

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

**Latest saved flight:** 2026-04-03 04:25:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-03 04:25:34 UTC

- **12,628** saved flights
- **7,178** unique routes
- **111** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **12,628** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **157,436.1 tonnes** estimated CO2 emissions
- **9,126,732 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 559 |
| 2 | Ryanair | 482 |
| 3 | IndiGo | 333 |
| 4 | EJA | 254 |
| 5 | American Airlines | 233 |
| 6 | Lufthansa | 194 |
| 7 | Southwest Airlines | 189 |
| 8 | ENY | 166 |
| 9 | Vueling | 131 |
| 10 | LATAM Airlines | 127 |
| 11 | AXM | 123 |
| 12 | LXJ | 117 |
| 13 | QLK | 114 |
| 14 | All Nippon Airways | 110 |
| 15 | Delta Air Lines | 99 |
| 16 | AZU | 95 |
| 17 | Swiss International | 95 |
| 18 | WIF | 95 |
| 19 | VIV | 93 |
| 20 | Cathay Pacific | 85 |
| 21 | Alaska Airlines | 84 |
| 22 | United Airlines | 84 |
| 23 | AXB | 81 |
| 24 | Japan Airlines | 79 |
| 25 | EDV | 78 |
| 26 | easyJet | 77 |
| 27 | EJU | 73 |
| 28 | BRC | 72 |
| 29 | Avianca | 71 |
| 30 | ANZ | 70 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 10315 |
| 2 | 🇮🇳 IN | 1036 |
| 3 | 🇦🇺 AU | 1002 |
| 4 | 🇪🇸 ES | 956 |
| 5 | 🇧🇷 BR | 705 |
| 6 | 🇩🇪 DE | 674 |
| 7 | 🇯🇵 JP | 634 |
| 8 | 🇨🇴 CO | 619 |
| 9 | 🇨🇦 CA | 601 |
| 10 | 🇮🇹 IT | 560 |
| 11 | 🇬🇧 GB | 469 |
| 12 | 🇲🇽 MX | 462 |
| 13 | 🇫🇷 FR | 399 |
| 14 | 🇳🇿 NZ | 308 |
| 15 | 🇬🇷 GR | 305 |
| 16 | 🇳🇴 NO | 301 |
| 17 | 🇨🇭 CH | 297 |
| 18 | 🇲🇾 MY | 280 |
| 19 | 🇿🇦 ZA | 237 |
| 20 | 🇵🇭 PH | 236 |
| 21 | 🇬🇹 GT | 234 |
| 22 | 🇹🇷 TR | 217 |
| 23 | 🇰🇷 KR | 213 |
| 24 | 🇵🇱 PL | 176 |
| 25 | 🇹🇭 TH | 157 |
| 26 | 🇲🇴 MO | 154 |
| 27 | 🇮🇩 ID | 153 |
| 28 | 🇲🇦 MA | 146 |
| 29 | 🇧🇸 BS | 128 |
| 30 | 🇲🇪 ME | 122 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 312 |
| 2 | Denver International Airport |  | US | 232 |
| 3 | Tokyo International Airport |  | JP | 223 |
| 4 | Indira Gandhi International Airport |  | IN | 222 |
| 5 | El Dorado International Airport |  | CO | 216 |
| 6 | Frankfurt am Main International Airport |  | DE | 185 |
| 7 | Harry Reid International Airport |  | US | 176 |
| 8 | La Aurora Airport |  | GT | 163 |
| 9 | Macau International Airport |  | MO | 154 |
| 10 | Guaymaral Airport |  | CO | 153 |
| 11 | Sydney Kingsford Smith International Airport |  | AU | 149 |
| 12 | Zurich Airport |  | CH | 148 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 144 |
| 14 | Eleftherios Venizelos International Airport |  | GR | 138 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 125 |
| 16 | Chicago O'Hare International Airport |  | US | 123 |
| 17 | Bengaluru International Airport |  | IN | 116 |
| 18 | Atizapan De Zaragoza Airport |  | MX | 114 |
| 19 | Charlotte/Douglas International Airport |  | US | 112 |
| 20 | Congonhas Airport |  | BR | 109 |
| 21 | Madrid Barajas International Airport |  | ES | 108 |
| 22 | Ninoy Aquino International Airport |  | PH | 106 |
| 23 | Tenerife Norte Airport |  | ES | 106 |
| 24 | Kuala Lumpur International Airport |  | MY | 106 |
| 25 | Reno/Tahoe International Airport |  | US | 97 |
| 26 | Salt Lake City International Airport |  | US | 96 |
| 27 | Daniel K Inouye International Airport |  | US | 94 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 93 |
| 29 | Vitoria/Foronda Airport |  | ES | 92 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 92 |
| 31 | Malpensa International Airport |  | IT | 91 |
| 32 | Barcelona International Airport |  | ES | 88 |
| 33 | Charles de Gaulle International Airport |  | FR | 87 |
| 34 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 86 |
| 35 | Austin-Bergstrom International Airport |  | US | 84 |
| 36 | Pune Airport |  | IN | 84 |
| 37 | Seattle-Tacoma International Airport |  | US | 84 |
| 38 | George Bush Intcntl/Houston Airport |  | US | 82 |
| 39 | Miami International Airport |  | US | 79 |
| 40 | Bodø Airport |  | NO | 78 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 60 | 14m | 114 km | 117.7 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 60 | 27m | - | - |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 53 | 1h 7m | 706 km | 645.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 44 | 24m | 225 km | 170.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 41 | 29m | 304 km | 214.9 t |
| 6 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 38 | 1h 46m | 1,156 km | 758.1 t |
| 7 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 36 | 4m | - | - |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 35 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 33 | 20m | 165 km | 93.9 t |
| 10 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 32 | 15m | 206 km | 113.8 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 32 | 23m | 99 km | 54.8 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 31 | 1h 26m | 910 km | 486.5 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 30 | 26m | 152 km | 78.4 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 29 | 29m | 275 km | 137.4 t |
| 15 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 29 | 53m | 556 km | 278.0 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 28 | 53m | 546 km | 263.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 27 | 30m | 369 km | 171.9 t |
| 18 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 27 | 1h 55m | 1,304 km | 607.4 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 26 | 1h 42m | 1,423 km | 638.1 t |
| 20 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 24 | 1h 10m | 770 km | 318.8 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 24 | 8m | - | - |
| 22 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 22 | 23m | 252 km | 95.5 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 22 | 11m | 127 km | 48.2 t |
| 24 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 21 | 1h 0m | 723 km | 261.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 21 | 13m | 99 km | 36.0 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 19 | 44m | 452 km | 148.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 18 | 20m | 147 km | 45.6 t |
| 28 | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 18 | 1h 16m | 924 km | 287.1 t |
| 29 | El Dorado International Airport (SKBO) | Chaparral Airport (SKHA) | 18 | 17m | 183 km | 56.8 t |
| 30 | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 18 | 33m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU68 | ERU | Robin Airport (59AZ) | AZ86 (AZ86) | 2026-04-03 04:22 UTC | 2026-04-03 04:25 UTC | 3m |
| QLK1525 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-04-03 03:23 UTC | 2026-04-03 04:20 UTC | 56m |
| N19HT |  | Bermuda Dunes Airport (KUDD) | Portland-Hillsboro Airport (KHIO) | 2026-04-03 02:27 UTC | 2026-04-03 04:19 UTC | 1h 52m |
| ERU25 | ERU | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-03 04:13 UTC | 2026-04-03 04:18 UTC | 4m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-03 03:32 UTC | 2026-04-03 04:15 UTC | 43m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-03 03:56 UTC | 2026-04-03 04:14 UTC | 18m |
| LBQ865 | LBQ | Tallahassee International Airport (KTLH) | Tampa Executive Airport (KVDF) | 2026-04-03 03:21 UTC | 2026-04-03 04:10 UTC | 48m |
| JST650 | JST | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 2026-04-03 02:55 UTC | 2026-04-03 04:10 UTC | 1h 14m |
| STT228 | STT | Daniel K Inouye International Airport (PHNL) | Kaluakoi Airport (HI49) | 2026-04-03 03:59 UTC | 2026-04-03 04:09 UTC | 9m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-04-03 03:53 UTC | 2026-04-03 04:04 UTC | 11m |
| FDA353 | FDA | Nagoya Airport (RJNA) | Yamagata Airport (RJSC) | 2026-04-03 03:25 UTC | 2026-04-03 04:02 UTC | 37m |
| RAM325 | Royal Air Maroc | Mohammed V International Airport (GMMN) | Blaise Diagne International Airport (GOBD) | 2026-04-03 01:08 UTC | 2026-04-03 04:02 UTC | 2h 53m |
| JAL259 | Japan Airlines | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-03 03:08 UTC | 2026-04-03 04:02 UTC | 54m |
| JES3062 | JES | Jorge Newbery Airpark (SABE) | Bella Vista Airport (SA26) | 2026-04-03 03:06 UTC | 2026-04-03 03:59 UTC | 52m |
| CEB1133 | CEB | Diosdado Macapagal International Airport (RPLC) | Godofredo P. Ramos Airport (RPVE) | 2026-04-03 03:19 UTC | 2026-04-03 03:56 UTC | 36m |
| NJZ3 | NJZ | Youngberg Ranch Airport (NV17) | San Francisco International Airport (KSFO) | 2026-04-03 03:03 UTC | 2026-04-03 03:55 UTC | 51m |
| PE993 |  | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-04-03 03:04 UTC | 2026-04-03 03:53 UTC | 49m |
| AXM6126 | AXM | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 2026-04-03 03:41 UTC | 2026-04-03 03:52 UTC | 11m |
| QTR62J | Qatar Airways | Hamad International Airport (OTHH) | VGZR (VGZR) | 2026-04-02 23:10 UTC | 2026-04-03 03:51 UTC | 4h 41m |
| ASI85 | ASI | Chandler Municipal Airport (KCHD) | Pilots Rest Airport (AZ57) | 2026-04-03 02:43 UTC | 2026-04-03 03:51 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
