# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_18:07:59_UTC-green)

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

**Latest saved flight:** 2026-04-13 18:07:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 18:07:59 UTC

- **32,707** saved flights
- **14,684** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,707** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **402,179.9 tonnes** estimated CO2 emissions
- **23,314,776 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1391 |
| 2 | SkyWest Airlines | 1313 |
| 3 | IndiGo | 839 |
| 4 | EJA | 569 |
| 5 | American Airlines | 562 |
| 6 | Southwest Airlines | 470 |
| 7 | ENY | 435 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 345 |
| 10 | Vueling | 334 |
| 11 | LATAM Airlines | 328 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 290 |
| 14 | Delta Air Lines | 274 |
| 15 | QLK | 266 |
| 16 | LXJ | 265 |
| 17 | Swiss International | 251 |
| 18 | WIF | 224 |
| 19 | EJU | 219 |
| 20 | Alaska Airlines | 218 |
| 21 | easyJet | 218 |
| 22 | AEE | 212 |
| 23 | VIV | 211 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 191 |
| 26 | United Airlines | 185 |
| 27 | Air France | 178 |
| 28 | GLO | 177 |
| 29 | JetBlue | 175 |
| 30 | Avianca | 173 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25633 |
| 2 | 🇮🇳 IN | 2563 |
| 3 | 🇪🇸 ES | 2469 |
| 4 | 🇦🇺 AU | 2253 |
| 5 | 🇧🇷 BR | 1924 |
| 6 | 🇯🇵 JP | 1778 |
| 7 | 🇮🇹 IT | 1747 |
| 8 | 🇩🇪 DE | 1660 |
| 9 | 🇨🇴 CO | 1630 |
| 10 | 🇨🇦 CA | 1588 |
| 11 | 🇬🇧 GB | 1341 |
| 12 | 🇫🇷 FR | 1215 |
| 13 | 🇲🇽 MX | 1037 |
| 14 | 🇬🇷 GR | 959 |
| 15 | 🇨🇭 CH | 920 |
| 16 | 🇲🇾 MY | 835 |
| 17 | 🇳🇴 NO | 746 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇵🇭 PH | 613 |
| 21 | 🇹🇷 TR | 610 |
| 22 | 🇹🇭 TH | 597 |
| 23 | 🇬🇹 GT | 596 |
| 24 | 🇰🇷 KR | 559 |
| 25 | 🇵🇱 PL | 512 |
| 26 | 🇲🇦 MA | 421 |
| 27 | 🇧🇸 BS | 337 |
| 28 | 🇲🇪 ME | 327 |
| 29 | 🇳🇱 NL | 320 |
| 30 | 🇮🇩 ID | 311 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 774 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 576 |
| 4 | Denver International Airport |  | US | 545 |
| 5 | Indira Gandhi International Airport |  | IN | 543 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 468 |
| 7 | La Aurora Airport |  | GT | 433 |
| 8 | Harry Reid International Airport |  | US | 423 |
| 9 | Zurich Airport |  | CH | 411 |
| 10 | Guaymaral Airport |  | CO | 402 |
| 11 | Chicago O'Hare International Airport |  | US | 337 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 335 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 334 |
| 14 | Frankfurt am Main International Airport |  | DE | 325 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 307 |
| 18 | Madrid Barajas International Airport |  | ES | 300 |
| 19 | Bengaluru International Airport |  | IN | 296 |
| 20 | Charlotte/Douglas International Airport |  | US | 294 |
| 21 | Tenerife Norte Airport |  | ES | 291 |
| 22 | Congonhas Airport |  | BR | 285 |
| 23 | Ninoy Aquino International Airport |  | PH | 284 |
| 24 | Malpensa International Airport |  | IT | 266 |
| 25 | Daniel K Inouye International Airport |  | US | 251 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 248 |
| 27 | Salt Lake City International Airport |  | US | 247 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 232 |
| 31 | Capua Airport |  | IT | 231 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 226 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 34 | O. R. Tambo International Airport |  | ZA | 223 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 222 |
| 36 | Vitoria/Foronda Airport |  | ES | 220 |
| 37 | Miami International Airport |  | US | 212 |
| 38 | Barcelona International Airport |  | ES | 210 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Don Mueang International Airport |  | TH | 202 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 156 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 136 | 14m | 114 km | 266.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 79 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 72 | 27m | 275 km | 341.2 t |
| 13 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 70 | 21m | 244 km | 294.8 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 52 | 20m | 147 km | 131.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 46 | 12m | 15 km | 12.1 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 45 | 1h 21m | 961 km | 745.9 t |
| 29 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 45 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N400DG |  | Colonel James Jabara Airport (KAAO) | Colonel James Jabara Airport (KAAO) | 2026-04-13 17:30 UTC | 2026-04-13 18:07 UTC | 37m |
| BOXER01 | BOX | Dunbar Ranch Airport (0XS8) | Dunbar Ranch Airport (0XS8) | 2026-04-13 17:50 UTC | 2026-04-13 18:01 UTC | 11m |
| C6569 |  | Grand View International Airport (WN23) | William R Fairchild International Airport (KCLM) | 2026-04-13 17:00 UTC | 2026-04-13 17:59 UTC | 59m |
| LLN106 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | 69XA (69XA) | 2026-04-13 17:33 UTC | 2026-04-13 17:59 UTC | 26m |
| N6338D |  | Centennial Airport (KAPA) | Erie Municipal Airport (KEIK) | 2026-04-13 17:39 UTC | 2026-04-13 17:55 UTC | 16m |
| HTY292 | HTY | Malaga Airport (LEMG) | Gibraltar Airport (LXGB) | 2026-04-13 16:52 UTC | 2026-04-13 17:54 UTC | 1h 2m |
| BRG632 | BRG | Ralph Wien Memorial Airport (PAOT) | Kivalina Airport (PAVL) | 2026-04-13 17:22 UTC | 2026-04-13 17:54 UTC | 31m |
| N479FG |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-04-13 17:29 UTC | 2026-04-13 17:49 UTC | 20m |
| JTL89 | JTL | 51CO (51CO) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-04-13 17:19 UTC | 2026-04-13 17:49 UTC | 30m |
| N681K |  | Teterboro Airport (KTEB) | Laurence G Hanscom Field (KBED) | 2026-04-13 17:10 UTC | 2026-04-13 17:48 UTC | 37m |
| CNS245 | CNS | Portsmouth International At Pease Airport (KPSM) | Concord Municipal Airport (KCON) | 2026-04-13 17:30 UTC | 2026-04-13 17:46 UTC | 16m |
| JEDDA66 | JED | Pilots Landing Airport (81TE) | J R Ranch Airport (15TA) | 2026-04-13 17:25 UTC | 2026-04-13 17:38 UTC | 13m |
|  |  | Pickens County Airport (KJZP) | Pickens County Airport (KJZP) | 2026-04-13 17:33 UTC | 2026-04-13 17:35 UTC | 1m |
| JBU1380 | JetBlue | Fort Lauderdale/Hollywood International Airport (KFLL) | La Aurora Airport (MGGT) | 2026-04-13 15:10 UTC | 2026-04-13 17:33 UTC | 2h 22m |
|  |  | Nairobi Wilson Airport (HKNW) | Nairobi Wilson Airport (HKNW) | 2026-04-13 17:21 UTC | 2026-04-13 17:32 UTC | 10m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-13 16:32 UTC | 2026-04-13 17:31 UTC | 58m |
| N2569Q |  | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-04-13 16:38 UTC | 2026-04-13 17:28 UTC | 49m |
| N272BG |  | Seattle Paine Field International Airport (KPAE) | Moffett Federal Airfield (KNUQ) | 2026-04-13 15:53 UTC | 2026-04-13 17:27 UTC | 1h 34m |
| N479AK |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-04-13 17:05 UTC | 2026-04-13 17:25 UTC | 20m |
| N724EH |  | Tallahassee International Airport (KTLH) | Bibb County Airport (K0A8) | 2026-04-13 16:50 UTC | 2026-04-13 17:24 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
