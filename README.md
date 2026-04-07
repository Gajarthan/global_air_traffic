# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_04:56:06_UTC-green)

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

**Latest saved flight:** 2026-04-07 04:56:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 04:56:06 UTC

- **21,237** saved flights
- **10,553** unique routes
- **116** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **21,237** saved routes in the archive
- **1h 16m** average flight duration

### Carbon Footprint Estimate

- **265,789.0 tonnes** estimated CO2 emissions
- **15,408,055 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 933 |
| 2 | Ryanair | 873 |
| 3 | IndiGo | 590 |
| 4 | American Airlines | 411 |
| 5 | EJA | 404 |
| 6 | Southwest Airlines | 308 |
| 7 | ENY | 292 |
| 8 | Lufthansa | 264 |
| 9 | Vueling | 225 |
| 10 | LATAM Airlines | 224 |
| 11 | AXM | 201 |
| 12 | Delta Air Lines | 189 |
| 13 | LXJ | 186 |
| 14 | All Nippon Airways | 181 |
| 15 | QLK | 175 |
| 16 | AZU | 168 |
| 17 | VIV | 155 |
| 18 | Swiss International | 154 |
| 19 | Alaska Airlines | 145 |
| 20 | easyJet | 143 |
| 21 | United Airlines | 143 |
| 22 | Avianca | 139 |
| 23 | EJU | 135 |
| 24 | Japan Airlines | 135 |
| 25 | AEE | 128 |
| 26 | EDV | 127 |
| 27 | WIF | 126 |
| 28 | AXB | 120 |
| 29 | Air France | 111 |
| 30 | BRC | 111 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 16934 |
| 2 | 🇮🇳 IN | 1791 |
| 3 | 🇪🇸 ES | 1667 |
| 4 | 🇦🇺 AU | 1477 |
| 5 | 🇧🇷 BR | 1223 |
| 6 | 🇨🇴 CO | 1175 |
| 7 | 🇯🇵 JP | 1112 |
| 8 | 🇮🇹 IT | 1035 |
| 9 | 🇩🇪 DE | 1030 |
| 10 | 🇨🇦 CA | 956 |
| 11 | 🇬🇧 GB | 826 |
| 12 | 🇫🇷 FR | 758 |
| 13 | 🇲🇽 MX | 722 |
| 14 | 🇬🇷 GR | 584 |
| 15 | 🇨🇭 CH | 566 |
| 16 | 🇲🇾 MY | 469 |
| 17 | 🇬🇹 GT | 464 |
| 18 | 🇿🇦 ZA | 461 |
| 19 | 🇳🇴 NO | 433 |
| 20 | 🇳🇿 NZ | 430 |
| 21 | 🇹🇷 TR | 412 |
| 22 | 🇵🇭 PH | 400 |
| 23 | 🇰🇷 KR | 351 |
| 24 | 🇹🇭 TH | 313 |
| 25 | 🇵🇱 PL | 306 |
| 26 | 🇲🇦 MA | 258 |
| 27 | 🇧🇸 BS | 235 |
| 28 | 🇲🇪 ME | 220 |
| 29 | 🇮🇩 ID | 217 |
| 30 | 🇳🇱 NL | 209 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 531 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Denver International Airport |  | US | 393 |
| 4 | Tokyo International Airport |  | JP | 384 |
| 5 | Indira Gandhi International Airport |  | IN | 367 |
| 6 | La Aurora Airport |  | GT | 319 |
| 7 | Harry Reid International Airport |  | US | 283 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 277 |
| 9 | Zurich Airport |  | CH | 256 |
| 10 | Frankfurt am Main International Airport |  | DE | 236 |
| 11 | Chicago O'Hare International Airport |  | US | 232 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 231 |
| 13 | Guaymaral Airport |  | CO | 230 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 229 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 209 |
| 16 | Charlotte/Douglas International Airport |  | US | 208 |
| 17 | Bengaluru International Airport |  | IN | 202 |
| 18 | Macau International Airport |  | MO | 200 |
| 19 | Madrid Barajas International Airport |  | ES | 195 |
| 20 | Tenerife Norte Airport |  | ES | 191 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 189 |
| 22 | Ninoy Aquino International Airport |  | PH | 183 |
| 23 | Congonhas Airport |  | BR | 181 |
| 24 | Salt Lake City International Airport |  | US | 170 |
| 25 | Reno/Tahoe International Airport |  | US | 168 |
| 26 | Daniel K Inouye International Airport |  | US | 166 |
| 27 | Kuala Lumpur International Airport |  | MY | 164 |
| 28 | Malpensa International Airport |  | IT | 162 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 157 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 156 |
| 31 | Charles de Gaulle International Airport |  | FR | 153 |
| 32 | Miami International Airport |  | US | 152 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 147 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 146 |
| 35 | Vitoria/Foronda Airport |  | ES | 146 |
| 36 | O. R. Tambo International Airport |  | ZA | 143 |
| 37 | Pune Airport |  | IN | 142 |
| 38 | Barcelona International Airport |  | ES | 140 |
| 39 | George Bush Intcntl/Houston Airport |  | US | 137 |
| 40 | Seattle-Tacoma International Airport |  | US | 137 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 97 | 1h 8m | 706 km | 1,181.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 84 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 79 | 24m | 225 km | 306.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 69 | 28m | 304 km | 361.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 65 | 27m | 152 km | 169.9 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 61 | 1h 27m | 910 km | 957.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 60 | 1h 43m | 1,156 km | 1,197.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 58 | 31m | - | - |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 47 | 19m | 165 km | 133.7 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 45 | 1h 12m | 770 km | 597.8 t |
| 15 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 44 | 23m | 252 km | 191.0 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 43 | 55m | 546 km | 404.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 43 | 52m | 556 km | 412.2 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 42 | 30m | 369 km | 267.3 t |
| 20 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 39 | 4m | - | - |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 39 | 20m | 250 km | 168.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 25 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 37 | 46m | 452 km | 288.4 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 32 | 1h 22m | 961 km | 530.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YTU | YTU | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-04-07 04:04 UTC | 2026-04-07 04:56 UTC | 51m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-07 04:40 UTC | 2026-04-07 04:48 UTC | 7m |
| N824PM |  | Indianapolis International Airport (KIND) | Bottoms Brothers Airport (1IN5) | 2026-04-07 04:27 UTC | 2026-04-07 04:44 UTC | 17m |
| N492DS |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-07 03:38 UTC | 2026-04-07 04:43 UTC | 1h 5m |
| EJA560 | EJA | Van Nuys Airport (KVNY) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-07 03:43 UTC | 2026-04-07 04:30 UTC | 46m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-04-07 04:09 UTC | 2026-04-07 04:29 UTC | 19m |
| ANA859 | All Nippon Airways | Tokyo International Airport (RJTT) | Chek Lap Kok International Airport (VHHH) | 2026-04-07 00:03 UTC | 2026-04-07 04:28 UTC | 4h 25m |
| N4056V |  | Portland-Troutdale Airport (KTTD) | Lambert Field (4OR3) | 2026-04-07 03:30 UTC | 2026-04-07 04:18 UTC | 48m |
| ERU8 | ERU | Robin Airport (59AZ) | Pilots Rest Airport (AZ57) | 2026-04-07 03:52 UTC | 2026-04-07 04:17 UTC | 24m |
| IGO531P | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-07 03:36 UTC | 2026-04-07 04:14 UTC | 38m |
| CEB911 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-07 03:48 UTC | 2026-04-07 04:13 UTC | 25m |
| N102LJ |  | Livermore Municipal Airport (KLVK) | 0AR1 (0AR1) | 2026-04-07 01:13 UTC | 2026-04-07 04:10 UTC | 2h 56m |
| QFA683 | Qantas | Melbourne International Airport (YMML) | Adelaide International Airport (YPAD) | 2026-04-07 02:58 UTC | 2026-04-07 04:07 UTC | 1h 8m |
| ERU33 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | Scottsdale Airport (KSDL) | 2026-04-07 03:28 UTC | 2026-04-07 04:07 UTC | 38m |
| LNI | LNI | Cervantes Airport (YCVS) | Jurien Bay Airport (YJNB) | 2026-04-07 03:56 UTC | 2026-04-07 04:05 UTC | 8m |
| SFJ77 | SFJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-07 02:46 UTC | 2026-04-07 04:02 UTC | 1h 15m |
| WZZ409 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Berane Airport (LYBR) | 2026-04-07 03:18 UTC | 2026-04-07 04:00 UTC | 42m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-07 03:52 UTC | 2026-04-07 03:58 UTC | 6m |
| N159U |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-04-07 02:56 UTC | 2026-04-07 03:58 UTC | 1h 1m |
| AXM6126 | AXM | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 2026-04-07 03:43 UTC | 2026-04-07 03:57 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
