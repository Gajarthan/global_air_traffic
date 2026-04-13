# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_12:27:34_UTC-green)

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

**Latest saved flight:** 2026-04-13 12:27:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 12:27:34 UTC

- **32,082** saved flights
- **14,456** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **32,082** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **395,549.6 tonnes** estimated CO2 emissions
- **22,930,410 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1363 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 828 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 464 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 376 |
| 9 | AXM | 342 |
| 10 | Vueling | 328 |
| 11 | LATAM Airlines | 324 |
| 12 | All Nippon Airways | 296 |
| 13 | AZU | 286 |
| 14 | QLK | 266 |
| 15 | Delta Air Lines | 265 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 241 |
| 18 | Alaska Airlines | 215 |
| 19 | easyJet | 213 |
| 20 | WIF | 213 |
| 21 | EJU | 212 |
| 22 | AEE | 206 |
| 23 | Japan Airlines | 205 |
| 24 | VIV | 205 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 174 |
| 28 | Air France | 172 |
| 29 | Avianca | 171 |
| 30 | JetBlue | 170 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25088 |
| 2 | 🇮🇳 IN | 2532 |
| 3 | 🇪🇸 ES | 2410 |
| 4 | 🇦🇺 AU | 2250 |
| 5 | 🇧🇷 BR | 1896 |
| 6 | 🇯🇵 JP | 1774 |
| 7 | 🇮🇹 IT | 1708 |
| 8 | 🇩🇪 DE | 1631 |
| 9 | 🇨🇴 CO | 1606 |
| 10 | 🇨🇦 CA | 1547 |
| 11 | 🇬🇧 GB | 1314 |
| 12 | 🇫🇷 FR | 1186 |
| 13 | 🇲🇽 MX | 1017 |
| 14 | 🇬🇷 GR | 937 |
| 15 | 🇨🇭 CH | 895 |
| 16 | 🇲🇾 MY | 829 |
| 17 | 🇳🇴 NO | 718 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 664 |
| 20 | 🇵🇭 PH | 608 |
| 21 | 🇹🇭 TH | 591 |
| 22 | 🇹🇷 TR | 591 |
| 23 | 🇬🇹 GT | 587 |
| 24 | 🇰🇷 KR | 557 |
| 25 | 🇵🇱 PL | 490 |
| 26 | 🇲🇦 MA | 417 |
| 27 | 🇧🇸 BS | 332 |
| 28 | 🇲🇪 ME | 319 |
| 29 | 🇮🇩 ID | 309 |
| 30 | 🇳🇱 NL | 308 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 766 |
| 2 | Tokyo International Airport |  | JP | 600 |
| 3 | El Dorado International Airport |  | CO | 571 |
| 4 | Indira Gandhi International Airport |  | IN | 539 |
| 5 | Denver International Airport |  | US | 538 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 459 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 417 |
| 9 | Zurich Airport |  | CH | 397 |
| 10 | Guaymaral Airport |  | CO | 389 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 12 | Chicago O'Hare International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 321 |
| 15 | Kuala Lumpur International Airport |  | MY | 317 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 305 |
| 18 | Madrid Barajas International Airport |  | ES | 291 |
| 19 | Bengaluru International Airport |  | IN | 290 |
| 20 | Charlotte/Douglas International Airport |  | US | 289 |
| 21 | Tenerife Norte Airport |  | ES | 287 |
| 22 | Ninoy Aquino International Airport |  | PH | 281 |
| 23 | Congonhas Airport |  | BR | 278 |
| 24 | Malpensa International Airport |  | IT | 261 |
| 25 | Daniel K Inouye International Airport |  | US | 246 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 244 |
| 27 | Salt Lake City International Airport |  | US | 244 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 233 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 230 |
| 31 | Capua Airport |  | IT | 222 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 222 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 221 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 218 |
| 35 | O. R. Tambo International Airport |  | ZA | 217 |
| 36 | Vitoria/Foronda Airport |  | ES | 212 |
| 37 | Miami International Airport |  | US | 210 |
| 38 | Barcelona International Airport |  | ES | 206 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Don Mueang International Airport |  | TH | 199 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 83 | 19m | 165 km | 236.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 69 | 27m | 275 km | 327.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 67 | 21m | 244 km | 282.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 56 | 20m | 250 km | 241.9 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 48 | 16m | 162 km | 134.6 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 45 | 12m | 15 km | 11.9 t |
| 28 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK126 | CXK | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-04-13 12:04 UTC | 2026-04-13 12:27 UTC | 23m |
| LTA438 | LTA | Indianapolis International Airport (KIND) | II29 (II29) | 2026-04-13 12:04 UTC | 2026-04-13 12:26 UTC | 22m |
| N76AX |  | Bellingham International Airport (KBLI) | Boeing Field/King County International Airport (KBFI) | 2026-04-13 12:06 UTC | 2026-04-13 12:25 UTC | 19m |
| N563M |  | Chippewa Valley Regional Airport (KEAU) | Joe Foss Field (KFSD) | 2026-04-13 11:33 UTC | 2026-04-13 12:21 UTC | 47m |
| IAM3185 | IAM | Ciampino Airport (LIRA) | Torino / Caselle International Airport (LIMF) | 2026-04-13 11:07 UTC | 2026-04-13 12:15 UTC | 1h 8m |
| EIX10E | EIX | Farnborough Airport (EGLF) | Lydd Airport (EGMD) | 2026-04-13 11:24 UTC | 2026-04-13 12:11 UTC | 47m |
| RYR4QJ | Ryanair | Paris Beauvais Tille Airport (LFOB) | Malpensa International Airport (LIMC) | 2026-04-13 10:40 UTC | 2026-04-13 12:02 UTC | 1h 22m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Birsa Munda Airport (VERC) | 2026-04-13 11:12 UTC | 2026-04-13 11:56 UTC | 43m |
| CGCOM | CGC | Victoriaville Airport (CSR3) | Montréal / St-Hubert Airport (CYHU) | 2026-04-13 11:30 UTC | 2026-04-13 11:51 UTC | 21m |
| PJ601 |  | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-13 11:21 UTC | 2026-04-13 11:50 UTC | 28m |
| EJU79QN | EJU | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Barcelonnette - Saint-Pons Airport (LFMR) | 2026-04-13 11:03 UTC | 2026-04-13 11:49 UTC | 46m |
| SEH6JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-04-13 11:19 UTC | 2026-04-13 11:47 UTC | 27m |
| AVR4833 | AVR | El Dorado International Airport (SKBO) | Tolemaida Air Base (SKTI) | 2026-04-13 11:33 UTC | 2026-04-13 11:43 UTC | 10m |
| NIVAL07 | NIV | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-04-13 10:58 UTC | 2026-04-13 11:42 UTC | 44m |
| ANE78XP | ANE | Madrid Barajas International Airport (LEMD) | Santo Tome Del Puerto Airport (LETP) | 2026-04-13 11:16 UTC | 2026-04-13 11:41 UTC | 24m |
| AZU4158 | AZU | Viracopos International Airport (SBKP) | Clube de Marte Ibira de Para-Quedismo Airport (SWYV) | 2026-04-13 10:54 UTC | 2026-04-13 11:40 UTC | 46m |
| FHBKH | FHB | Dax Seyresse Airport (LFBY) | Pau Pyrenees Airport (LFBP) | 2026-04-13 11:16 UTC | 2026-04-13 11:40 UTC | 24m |
| N53695 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-04-13 11:20 UTC | 2026-04-13 11:39 UTC | 19m |
| ANGEL07 | ANG | Cuatro Vientos Airport (LECU) | Cuatro Vientos Airport (LECU) | 2026-04-13 11:35 UTC | 2026-04-13 11:39 UTC | 3m |
| N529WM |  | Delta Municipal Airport (KDTA) | Savage Field (KU01) | 2026-04-13 10:52 UTC | 2026-04-13 11:34 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
