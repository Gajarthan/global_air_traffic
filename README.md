# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_19:33:36_UTC-green)

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

**Latest saved flight:** 2026-04-07 19:33:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 19:33:36 UTC

- **22,045** saved flights
- **10,869** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,045** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **273,841.2 tonnes** estimated CO2 emissions
- **15,874,852 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 946 |
| 2 | Ryanair | 924 |
| 3 | IndiGo | 620 |
| 4 | American Airlines | 413 |
| 5 | EJA | 407 |
| 6 | Southwest Airlines | 314 |
| 7 | ENY | 294 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 227 |
| 11 | AXM | 214 |
| 12 | All Nippon Airways | 193 |
| 13 | Delta Air Lines | 191 |
| 14 | LXJ | 187 |
| 15 | QLK | 183 |
| 16 | AZU | 173 |
| 17 | Swiss International | 162 |
| 18 | VIV | 158 |
| 19 | Alaska Airlines | 150 |
| 20 | easyJet | 149 |
| 21 | Japan Airlines | 148 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | WIF | 134 |
| 27 | EDV | 128 |
| 28 | AXB | 126 |
| 29 | Air France | 119 |
| 30 | Wizz Air | 114 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17299 |
| 2 | 🇮🇳 IN | 1892 |
| 3 | 🇪🇸 ES | 1738 |
| 4 | 🇦🇺 AU | 1553 |
| 5 | 🇧🇷 BR | 1248 |
| 6 | 🇯🇵 JP | 1210 |
| 7 | 🇨🇴 CO | 1179 |
| 8 | 🇮🇹 IT | 1124 |
| 9 | 🇩🇪 DE | 1107 |
| 10 | 🇨🇦 CA | 974 |
| 11 | 🇬🇧 GB | 874 |
| 12 | 🇫🇷 FR | 814 |
| 13 | 🇲🇽 MX | 731 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 604 |
| 16 | 🇲🇾 MY | 501 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇴 NO | 465 |
| 19 | 🇬🇹 GT | 465 |
| 20 | 🇳🇿 NZ | 444 |
| 21 | 🇹🇷 TR | 428 |
| 22 | 🇵🇭 PH | 413 |
| 23 | 🇰🇷 KR | 388 |
| 24 | 🇹🇭 TH | 349 |
| 25 | 🇵🇱 PL | 318 |
| 26 | 🇲🇦 MA | 268 |
| 27 | 🇧🇸 BS | 236 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 534 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 410 |
| 4 | Denver International Airport |  | US | 395 |
| 5 | Indira Gandhi International Airport |  | IN | 381 |
| 6 | La Aurora Airport |  | GT | 320 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 8 | Harry Reid International Airport |  | US | 287 |
| 9 | Zurich Airport |  | CH | 269 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 234 |
| 12 | Chicago O'Hare International Airport |  | US | 234 |
| 13 | Guaymaral Airport |  | CO | 234 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 233 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 217 |
| 16 | Bengaluru International Airport |  | IN | 213 |
| 17 | Charlotte/Douglas International Airport |  | US | 209 |
| 18 | Macau International Airport |  | MO | 201 |
| 19 | Tenerife Norte Airport |  | ES | 201 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 22 | Ninoy Aquino International Airport |  | PH | 189 |
| 23 | Congonhas Airport |  | BR | 182 |
| 24 | Salt Lake City International Airport |  | US | 178 |
| 25 | Kuala Lumpur International Airport |  | MY | 178 |
| 26 | Malpensa International Airport |  | IT | 172 |
| 27 | Daniel K Inouye International Airport |  | US | 172 |
| 28 | Reno/Tahoe International Airport |  | US | 170 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 169 |
| 30 | Charles de Gaulle International Airport |  | FR | 162 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 160 |
| 32 | Miami International Airport |  | US | 153 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 149 |
| 36 | Vitoria/Foronda Airport |  | ES | 147 |
| 37 | Pune Airport |  | IN | 147 |
| 38 | Barcelona International Airport |  | ES | 145 |
| 39 | Seattle-Tacoma International Airport |  | US | 140 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 138 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 103 | 1h 8m | 706 km | 1,254.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 86 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 82 | 24m | 225 km | 318.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 61 | 1h 43m | 1,156 km | 1,216.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 51 | 19m | 165 km | 145.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 46 | 55m | 546 km | 433.1 t |
| 17 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 44 | 31m | 369 km | 280.1 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 44 | 52m | 556 km | 421.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 41 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 37 | 58m | 723 km | 461.3 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 32 | 20m | 147 km | 81.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAGO13 | DRA | Marseille Provence Airport (LFML) | Marseille Provence Airport (LFML) | 2026-04-07 18:49 UTC | 2026-04-07 19:33 UTC | 44m |
| N1213S |  | Seattle Paine Field International Airport (KPAE) | Vancouver International Airport (CYVR) | 2026-04-07 18:41 UTC | 2026-04-07 19:30 UTC | 49m |
| N6533W |  | Scottsdale Airport (KSDL) | Phoenix Deer Valley Airport (KDVT) | 2026-04-07 19:15 UTC | 2026-04-07 19:29 UTC | 13m |
| N234KQ |  | Oxnard Airport (KOXR) | Meadows Field (KBFL) | 2026-04-07 18:48 UTC | 2026-04-07 19:28 UTC | 40m |
| N255CB |  | Camarillo Airport (KCMA) | Riverside Airport (KRAL) | 2026-04-07 18:25 UTC | 2026-04-07 19:28 UTC | 1h 2m |
| N64WG |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-07 19:01 UTC | 2026-04-07 19:18 UTC | 16m |
| GPD28 | GPD | Laurence G Hanscom Field (KBED) | Teterboro Airport (KTEB) | 2026-04-07 18:14 UTC | 2026-04-07 19:15 UTC | 1h 1m |
| N12441 |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-07 19:09 UTC | 2026-04-07 19:13 UTC | 4m |
| BOE203 | BOE | Boeing Field/King County International Airport (KBFI) | Franz Ranch Airport (33WA) | 2026-04-07 17:53 UTC | 2026-04-07 19:09 UTC | 1h 15m |
| THA313 | Thai Airways | Suvarnabhumi Airport (VTBS) | Behala Airport (VEBA) | 2026-04-07 16:53 UTC | 2026-04-07 19:07 UTC | 2h 13m |
| CXK475 | CXK | Ogden-Hinckley Airport (KOGD) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-04-07 18:24 UTC | 2026-04-07 19:04 UTC | 39m |
| UAL1547 | United Airlines | Denver International Airport (KDEN) | Lakeside Airport (MT03) | 2026-04-07 17:26 UTC | 2026-04-07 19:03 UTC | 1h 37m |
| ACA1048 | Air Canada | Castlegar Airport (CYCG) | Chicago O'Hare International Airport (KORD) | 2026-04-07 16:13 UTC | 2026-04-07 19:00 UTC | 2h 47m |
| N800RL |  | Rice Lake Regional/Carl's Field (KRPD) | Schilson Field (IS51) | 2026-04-07 18:17 UTC | 2026-04-07 19:00 UTC | 42m |
| N112FS |  | Tracy Municipal Airport (KTCY) | Tracy Municipal Airport (KTCY) | 2026-04-07 18:49 UTC | 2026-04-07 18:59 UTC | 10m |
| N419BR |  | Montgomery-Gibbs Executive Airport (KMYF) | Reno/Tahoe International Airport (KRNO) | 2026-04-07 17:51 UTC | 2026-04-07 18:59 UTC | 1h 7m |
| N26ND |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-04-07 17:45 UTC | 2026-04-07 18:56 UTC | 1h 10m |
| SH184 |  | Sturdy Oak Farm Airport (AL33) | Sturdy Oak Farm Airport (AL33) | 2026-04-07 18:53 UTC | 2026-04-07 18:55 UTC | 2m |
| GLO1669 | GLO | SWUD (SWUD) | Monte Verde Airport (SNEJ) | 2026-04-07 18:25 UTC | 2026-04-07 18:53 UTC | 27m |
| CXK434 | CXK | Centennial Airport (KAPA) | Chaparral Airport (CO18) | 2026-04-07 17:06 UTC | 2026-04-07 18:52 UTC | 1h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
