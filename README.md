# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_23:56:34_UTC-green)

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

**Latest saved flight:** 2026-04-13 23:56:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 23:56:34 UTC

- **33,314** saved flights
- **14,895** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,314** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **410,459.3 tonnes** estimated CO2 emissions
- **23,794,740 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1414 |
| 2 | SkyWest Airlines | 1353 |
| 3 | IndiGo | 839 |
| 4 | American Airlines | 582 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 484 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 346 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 335 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 296 |
| 14 | Delta Air Lines | 282 |
| 15 | QLK | 273 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 252 |
| 18 | Alaska Airlines | 226 |
| 19 | WIF | 225 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | VIV | 217 |
| 23 | AEE | 216 |
| 24 | Japan Airlines | 206 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | Avianca | 181 |
| 28 | GLO | 181 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26341 |
| 2 | 🇮🇳 IN | 2564 |
| 3 | 🇪🇸 ES | 2497 |
| 4 | 🇦🇺 AU | 2293 |
| 5 | 🇧🇷 BR | 1963 |
| 6 | 🇯🇵 JP | 1785 |
| 7 | 🇮🇹 IT | 1772 |
| 8 | 🇨🇴 CO | 1669 |
| 9 | 🇩🇪 DE | 1666 |
| 10 | 🇨🇦 CA | 1638 |
| 11 | 🇬🇧 GB | 1360 |
| 12 | 🇫🇷 FR | 1222 |
| 13 | 🇲🇽 MX | 1067 |
| 14 | 🇬🇷 GR | 969 |
| 15 | 🇨🇭 CH | 922 |
| 16 | 🇲🇾 MY | 837 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 708 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇵🇭 PH | 623 |
| 21 | 🇹🇷 TR | 618 |
| 22 | 🇬🇹 GT | 600 |
| 23 | 🇹🇭 TH | 597 |
| 24 | 🇰🇷 KR | 562 |
| 25 | 🇵🇱 PL | 518 |
| 26 | 🇲🇦 MA | 425 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 330 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇲🇴 MO | 316 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 802 |
| 2 | Tokyo International Airport |  | JP | 606 |
| 3 | El Dorado International Airport |  | CO | 596 |
| 4 | Denver International Airport |  | US | 569 |
| 5 | Indira Gandhi International Airport |  | IN | 544 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 473 |
| 7 | Harry Reid International Airport |  | US | 437 |
| 8 | La Aurora Airport |  | GT | 437 |
| 9 | Zurich Airport |  | CH | 413 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 342 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Frankfurt am Main International Airport |  | DE | 326 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Macau International Airport |  | MO | 316 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 316 |
| 18 | Charlotte/Douglas International Airport |  | US | 305 |
| 19 | Madrid Barajas International Airport |  | ES | 303 |
| 20 | Bengaluru International Airport |  | IN | 296 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 292 |
| 23 | Ninoy Aquino International Airport |  | PH | 290 |
| 24 | Malpensa International Airport |  | IT | 272 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 255 |
| 26 | Daniel K Inouye International Airport |  | US | 255 |
| 27 | Salt Lake City International Airport |  | US | 252 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 235 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Miami International Airport |  | US | 214 |
| 38 | Barcelona International Airport |  | ES | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 211 |
| 40 | Calgary International Airport |  | CA | 205 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 154 | 1h 8m | 706 km | 1,875.0 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 138 | 14m | 114 km | 270.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 122 | 24m | 225 km | 473.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 73 | 21m | 244 km | 307.4 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 53 | 20m | 147 km | 134.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |
| 30 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ETD870 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Macau International Airport (VMMC) | 2026-04-13 17:45 UTC | 2026-04-13 23:56 UTC | 6h 10m |
| N13UA |  | Oakland San Francisco Bay Airport (KOAK) | Santa Monica Municipal Airport (KSMO) | 2026-04-13 22:23 UTC | 2026-04-13 23:39 UTC | 1h 16m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-13 23:05 UTC | 2026-04-13 23:38 UTC | 33m |
| N703EX |  | Chandler Municipal Airport (KCHD) | Pegasus Airpark (5AZ3) | 2026-04-13 22:34 UTC | 2026-04-13 23:37 UTC | 1h 3m |
| CXK685 | CXK | Georgetown Executive Airport (KGTU) | Georgetown Executive Airport (KGTU) | 2026-04-13 23:04 UTC | 2026-04-13 23:36 UTC | 31m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-13 11:45 UTC | 2026-04-13 23:32 UTC | 11h 46m |
| TKR16 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Perry Stokes Airport (KTAD) | 2026-04-13 23:12 UTC | 2026-04-13 23:31 UTC | 19m |
| SCOFF71 | SCO | 4TA5 (4TA5) | Quanah Municipal Airport (KF01) | 2026-04-13 23:14 UTC | 2026-04-13 23:30 UTC | 16m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-04-13 22:50 UTC | 2026-04-13 23:28 UTC | 38m |
| N2441D |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-13 22:39 UTC | 2026-04-13 23:27 UTC | 48m |
| CFI031 | CFI | Shenzhen Bao'an International Airport (ZGSZ) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-04-13 22:39 UTC | 2026-04-13 23:24 UTC | 45m |
| SCJ80 | SCJ | Marco Island Executive Airport (KMKY) | 9WI9 (9WI9) | 2026-04-13 19:22 UTC | 2026-04-13 23:19 UTC | 3h 56m |
| TCF609 | TCF | Melbourne Orlando International Airport (KMLB) | Orlando Sanford International Airport (KSFB) | 2026-04-13 22:44 UTC | 2026-04-13 23:17 UTC | 33m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Orange Airport (YORG) | 2026-04-13 22:49 UTC | 2026-04-13 23:15 UTC | 25m |
| MSA61P | MSA | Brescia / Montichiari Airport (LIPO) | Corte Airport (LFKT) | 2026-04-13 22:36 UTC | 2026-04-13 23:15 UTC | 38m |
| NJM2022 | NJM | Burke Lakefront Airport (KBKL) | Witham Field (KSUA) | 2026-04-13 20:57 UTC | 2026-04-13 23:15 UTC | 2h 17m |
| N323NE |  | Scottsdale Airport (KSDL) | Quincy Flying Service Airport (WA74) | 2026-04-13 20:52 UTC | 2026-04-13 23:13 UTC | 2h 20m |
| QXE2315 | QXE | Seattle Paine Field International Airport (KPAE) | Yucca Valley Airport (KL22) | 2026-04-13 21:04 UTC | 2026-04-13 23:12 UTC | 2h 8m |
| N76YT |  | Mc Clellan-Palomar Airport (KCRQ) | Borrego Valley Airport (KL08) | 2026-04-13 22:56 UTC | 2026-04-13 23:11 UTC | 15m |
| N29WN |  | Peter O Knight Airport (KTPF) | Peter O Knight Airport (KTPF) | 2026-04-13 22:58 UTC | 2026-04-13 23:09 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
