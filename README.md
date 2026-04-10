# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_19:15:05_UTC-green)

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

**Latest saved flight:** 2026-04-10 19:15:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 19:15:05 UTC

- **27,429** saved flights
- **12,926** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **27,429** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **334,395.8 tonnes** estimated CO2 emissions
- **19,385,265 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1125 |
| 2 | SkyWest Airlines | 1111 |
| 3 | IndiGo | 733 |
| 4 | EJA | 486 |
| 5 | American Airlines | 481 |
| 6 | Southwest Airlines | 388 |
| 7 | ENY | 365 |
| 8 | Lufthansa | 339 |
| 9 | AXM | 284 |
| 10 | Vueling | 281 |
| 11 | LATAM Airlines | 269 |
| 12 | QLK | 245 |
| 13 | All Nippon Airways | 241 |
| 14 | Delta Air Lines | 230 |
| 15 | LXJ | 226 |
| 16 | AZU | 223 |
| 17 | Swiss International | 194 |
| 18 | Alaska Airlines | 184 |
| 19 | easyJet | 179 |
| 20 | VIV | 179 |
| 21 | WIF | 179 |
| 22 | AEE | 178 |
| 23 | Japan Airlines | 177 |
| 24 | EJU | 176 |
| 25 | EDV | 162 |
| 26 | United Airlines | 161 |
| 27 | Avianca | 155 |
| 28 | AXB | 147 |
| 29 | JetBlue | 146 |
| 30 | Air France | 141 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 21626 |
| 2 | 🇮🇳 IN | 2249 |
| 3 | 🇪🇸 ES | 2032 |
| 4 | 🇦🇺 AU | 1996 |
| 5 | 🇧🇷 BR | 1545 |
| 6 | 🇯🇵 JP | 1490 |
| 7 | 🇩🇪 DE | 1389 |
| 8 | 🇮🇹 IT | 1382 |
| 9 | 🇨🇴 CO | 1374 |
| 10 | 🇨🇦 CA | 1320 |
| 11 | 🇬🇧 GB | 1108 |
| 12 | 🇫🇷 FR | 1021 |
| 13 | 🇲🇽 MX | 869 |
| 14 | 🇬🇷 GR | 797 |
| 15 | 🇨🇭 CH | 753 |
| 16 | 🇲🇾 MY | 684 |
| 17 | 🇳🇴 NO | 602 |
| 18 | 🇳🇿 NZ | 602 |
| 19 | 🇿🇦 ZA | 566 |
| 20 | 🇵🇭 PH | 512 |
| 21 | 🇹🇷 TR | 506 |
| 22 | 🇬🇹 GT | 503 |
| 23 | 🇹🇭 TH | 480 |
| 24 | 🇰🇷 KR | 473 |
| 25 | 🇵🇱 PL | 418 |
| 26 | 🇲🇦 MA | 339 |
| 27 | 🇧🇸 BS | 291 |
| 28 | 🇲🇪 ME | 276 |
| 29 | 🇳🇱 NL | 269 |
| 30 | 🇮🇩 ID | 267 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 648 |
| 2 | El Dorado International Airport |  | CO | 500 |
| 3 | Tokyo International Airport |  | JP | 500 |
| 4 | Indira Gandhi International Airport |  | IN | 466 |
| 5 | Denver International Airport |  | US | 456 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 388 |
| 7 | Harry Reid International Airport |  | US | 352 |
| 8 | La Aurora Airport |  | GT | 350 |
| 9 | Zurich Airport |  | CH | 325 |
| 10 | Guaymaral Airport |  | CO | 303 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 289 |
| 12 | Frankfurt am Main International Airport |  | DE | 289 |
| 13 | Chicago O'Hare International Airport |  | US | 287 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 277 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 276 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Kuala Lumpur International Airport |  | MY | 254 |
| 18 | Bengaluru International Airport |  | IN | 251 |
| 19 | Charlotte/Douglas International Airport |  | US | 250 |
| 20 | Ninoy Aquino International Airport |  | PH | 238 |
| 21 | Tenerife Norte Airport |  | ES | 235 |
| 22 | Madrid Barajas International Airport |  | ES | 234 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 217 |
| 24 | Congonhas Airport |  | BR | 217 |
| 25 | Malpensa International Airport |  | IT | 215 |
| 26 | Salt Lake City International Airport |  | US | 211 |
| 27 | Daniel K Inouye International Airport |  | US | 209 |
| 28 | Reno/Tahoe International Airport |  | US | 199 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 188 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 186 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 33 | Miami International Airport |  | US | 184 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 183 |
| 35 | O. R. Tambo International Airport |  | ZA | 179 |
| 36 | Barcelona International Airport |  | ES | 175 |
| 37 | Vitoria/Foronda Airport |  | ES | 174 |
| 38 | Seattle-Tacoma International Airport |  | US | 172 |
| 39 | Capua Airport |  | IT | 171 |
| 40 | Don Mueang International Airport |  | TH | 168 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 129 | 1h 8m | 706 km | 1,570.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 115 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 111 | 14m | 114 km | 217.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 94 | 28m | 304 km | 492.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 78 | 1h 27m | 910 km | 1,224.0 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 72 | 21m | 99 km | 123.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 69 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 68 | 19m | 165 km | 193.4 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 56 | 27m | 275 km | 265.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 48 | 45m | 452 km | 374.1 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 48 | 52m | 556 km | 460.1 t |
| 19 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 48 | 9m | - | - |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 23 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 43 | 20m | 147 km | 108.8 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 27 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 37 | 1h 20m | 961 km | 613.3 t |
| 30 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 36 | 26m | 215 km | 133.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OAL053 | OAL | Dionysios Solomos Airport (LGZA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-10 18:33 UTC | 2026-04-10 19:15 UTC | 41m |
| EJA436 | EJA | Sacramento International Airport (KSMF) | Bermuda Dunes Airport (KUDD) | 2026-04-10 18:00 UTC | 2026-04-10 19:08 UTC | 1h 7m |
| VAR630 | VAR | Phoenix Goodyear Airport (KGYR) | 13AZ (13AZ) | 2026-04-10 17:47 UTC | 2026-04-10 19:06 UTC | 1h 19m |
| N64017 |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-04-10 18:11 UTC | 2026-04-10 19:00 UTC | 48m |
| N1536Y |  | Cross Keys Airport (K17N) | Millville Municipal Airport (KMIV) | 2026-04-10 18:43 UTC | 2026-04-10 18:59 UTC | 15m |
| N386ES |  | Iowa City Municipal Airport (KIOW) | Iowa City Municipal Airport (KIOW) | 2026-04-10 18:30 UTC | 2026-04-10 18:59 UTC | 28m |
| N44MK |  | Williston Regional Airport (KX60) | Tampa International Airport (KTPA) | 2026-04-10 18:31 UTC | 2026-04-10 18:57 UTC | 25m |
| N993JB |  | Prineville Airport (KS39) | OR02 (OR02) | 2026-04-10 18:21 UTC | 2026-04-10 18:56 UTC | 34m |
| PBD6544 | PBD | Koltsovo Airport (USSS) | Sheremetyevo International Airport (UUEE) | 2026-04-10 16:53 UTC | 2026-04-10 18:55 UTC | 2h 1m |
| CGIXO | CGI | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Cooking Lake Airport (CEZ3) | 2026-04-10 18:47 UTC | 2026-04-10 18:53 UTC | 5m |
| N62KW |  | Muscatine Municipal Airport (KMUT) | Jefferson City Memorial Airport (KJEF) | 2026-04-10 18:21 UTC | 2026-04-10 18:50 UTC | 28m |
| N484LP |  | Glendale Regional Airport (KGEU) | Indian Hills Airpark (2AZ1) | 2026-04-10 17:38 UTC | 2026-04-10 18:49 UTC | 1h 11m |
| N243SD |  | Huron Regional Airport (KHON) | Brookings Regional Airport (KBKX) | 2026-04-10 17:47 UTC | 2026-04-10 18:49 UTC | 1h 1m |
| N530ST |  | Lake Havasu City Airport (KHII) | Chemehuevi Valley Airport (K49X) | 2026-04-10 18:25 UTC | 2026-04-10 18:48 UTC | 23m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | General Mariano Matamoros Airport (MMCB) | 2026-04-10 18:36 UTC | 2026-04-10 18:46 UTC | 10m |
| SGE69 | SGE | Fort Worth Meacham International Airport (KFTW) | Kenneth Copeland Airport (K4T2) | 2026-04-10 17:59 UTC | 2026-04-10 18:46 UTC | 47m |
| GRZLY39 | GRZ | Miramar Mcas (Joe Foss Field) Airport (KNKX) | KL04 (KL04) | 2026-04-10 18:27 UTC | 2026-04-10 18:45 UTC | 18m |
| N7199D |  | Rostex Airport (55GE) | R M Harris Airport (4GA4) | 2026-04-10 18:36 UTC | 2026-04-10 18:42 UTC | 5m |
| N6038V |  | Centennial Airport (KAPA) | Geary Ranch Airport (CO65) | 2026-04-10 17:44 UTC | 2026-04-10 18:40 UTC | 55m |
| RYR2TJ | Ryanair | Ciampino Airport (LIRA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-10 16:56 UTC | 2026-04-10 18:40 UTC | 1h 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
