# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_07:49:29_UTC-green)

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

**Latest saved flight:** 2026-04-11 07:49:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-11 07:49:29 UTC

- **28,270** saved flights
- **13,242** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **28,270** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **343,494.7 tonnes** estimated CO2 emissions
- **19,912,738 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1155 |
| 2 | Ryanair | 1150 |
| 3 | IndiGo | 735 |
| 4 | EJA | 502 |
| 5 | American Airlines | 495 |
| 6 | Southwest Airlines | 406 |
| 7 | ENY | 382 |
| 8 | Lufthansa | 344 |
| 9 | AXM | 298 |
| 10 | Vueling | 289 |
| 11 | LATAM Airlines | 275 |
| 12 | QLK | 254 |
| 13 | All Nippon Airways | 252 |
| 14 | Delta Air Lines | 239 |
| 15 | AZU | 234 |
| 16 | LXJ | 232 |
| 17 | Swiss International | 201 |
| 18 | Alaska Airlines | 190 |
| 19 | Japan Airlines | 185 |
| 20 | VIV | 183 |
| 21 | EJU | 182 |
| 22 | easyJet | 181 |
| 23 | WIF | 180 |
| 24 | AEE | 179 |
| 25 | United Airlines | 173 |
| 26 | EDV | 166 |
| 27 | Avianca | 159 |
| 28 | JetBlue | 150 |
| 29 | AXB | 148 |
| 30 | PGT | 144 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 22450 |
| 2 | 🇮🇳 IN | 2272 |
| 3 | 🇦🇺 AU | 2074 |
| 4 | 🇪🇸 ES | 2063 |
| 5 | 🇧🇷 BR | 1593 |
| 6 | 🇯🇵 JP | 1548 |
| 7 | 🇮🇹 IT | 1414 |
| 8 | 🇨🇴 CO | 1407 |
| 9 | 🇩🇪 DE | 1407 |
| 10 | 🇨🇦 CA | 1393 |
| 11 | 🇬🇧 GB | 1129 |
| 12 | 🇫🇷 FR | 1032 |
| 13 | 🇲🇽 MX | 898 |
| 14 | 🇬🇷 GR | 811 |
| 15 | 🇨🇭 CH | 770 |
| 16 | 🇲🇾 MY | 713 |
| 17 | 🇳🇿 NZ | 634 |
| 18 | 🇳🇴 NO | 607 |
| 19 | 🇿🇦 ZA | 577 |
| 20 | 🇵🇭 PH | 538 |
| 21 | 🇬🇹 GT | 525 |
| 22 | 🇹🇷 TR | 510 |
| 23 | 🇹🇭 TH | 493 |
| 24 | 🇰🇷 KR | 486 |
| 25 | 🇵🇱 PL | 420 |
| 26 | 🇲🇦 MA | 347 |
| 27 | 🇧🇸 BS | 296 |
| 28 | 🇲🇪 ME | 280 |
| 29 | 🇮🇩 ID | 274 |
| 30 | 🇳🇱 NL | 272 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 676 |
| 2 | Tokyo International Airport |  | JP | 521 |
| 3 | El Dorado International Airport |  | CO | 511 |
| 4 | Denver International Airport |  | US | 478 |
| 5 | Indira Gandhi International Airport |  | IN | 473 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 395 |
| 7 | La Aurora Airport |  | GT | 370 |
| 8 | Harry Reid International Airport |  | US | 364 |
| 9 | Zurich Airport |  | CH | 333 |
| 10 | Guaymaral Airport |  | CO | 312 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 297 |
| 12 | Chicago O'Hare International Airport |  | US | 293 |
| 13 | Frankfurt am Main International Airport |  | DE | 292 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 290 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 289 |
| 16 | Kuala Lumpur International Airport |  | MY | 266 |
| 17 | Macau International Airport |  | MO | 262 |
| 18 | Charlotte/Douglas International Airport |  | US | 257 |
| 19 | Bengaluru International Airport |  | IN | 253 |
| 20 | Ninoy Aquino International Airport |  | PH | 248 |
| 21 | Madrid Barajas International Airport |  | ES | 239 |
| 22 | Tenerife Norte Airport |  | ES | 237 |
| 23 | Congonhas Airport |  | BR | 227 |
| 24 | Atizapan De Zaragoza Airport |  | MX | 220 |
| 25 | Salt Lake City International Airport |  | US | 220 |
| 26 | Daniel K Inouye International Airport |  | US | 219 |
| 27 | Malpensa International Airport |  | IT | 218 |
| 28 | Reno/Tahoe International Airport |  | US | 210 |
| 29 | Charles de Gaulle International Airport |  | FR | 195 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 194 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 190 |
| 32 | Miami International Airport |  | US | 189 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 186 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 184 |
| 35 | O. R. Tambo International Airport |  | ZA | 182 |
| 36 | Seattle-Tacoma International Airport |  | US | 179 |
| 37 | Capua Airport |  | IT | 179 |
| 38 | Barcelona International Airport |  | ES | 178 |
| 39 | Vitoria/Foronda Airport |  | ES | 177 |
| 40 | Calgary International Airport |  | CA | 170 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 132 | 1h 8m | 706 km | 1,607.1 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 119 | 27m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 115 | 14m | 114 km | 225.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 109 | 24m | 225 km | 422.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 97 | 28m | 304 km | 508.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 82 | 1h 27m | 910 km | 1,286.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 74 | 21m | 99 km | 126.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 71 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 70 | 19m | 165 km | 199.1 t |
| 10 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 11 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 63 | 55m | 546 km | 593.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 62 | 1h 12m | 770 km | 823.6 t |
| 14 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 57 | 27m | 275 km | 270.1 t |
| 16 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 55 | 9m | - | - |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 54 | 31m | 369 km | 343.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 52 | 46m | 452 km | 405.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 51 | 52m | 556 km | 488.9 t |
| 20 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 45 | 13m | 99 km | 77.2 t |
| 23 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 25 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 44 | 21m | 244 km | 185.3 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 44 | 20m | 147 km | 111.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 28 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 38 | 1h 20m | 961 km | 629.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL946 | United Airlines | Washington Dulles International Airport (KIAD) | Amsterdam Airport Schiphol (EHAM) | 2026-04-11 00:26 UTC | 2026-04-11 07:49 UTC | 7h 22m |
| THY70 | Turkish Airlines | Ataturk International Airport (LTBA) | Macau International Airport (VMMC) | 2026-04-10 22:59 UTC | 2026-04-11 07:48 UTC | 8h 49m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-04-11 07:17 UTC | 2026-04-11 07:39 UTC | 22m |
| SWR1DL | Swiss International | Zurich Airport (LSZH) | Malpensa International Airport (LIMC) | 2026-04-10 19:40 UTC | 2026-04-11 07:38 UTC | 11h 58m |
| EJU42HR | EJU | Faro Airport (LPFR) | Bristol International Airport (EGGD) | 2026-04-11 05:18 UTC | 2026-04-11 07:26 UTC | 2h 8m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Chiang Mai International Airport (VTCC) | 2026-04-11 07:06 UTC | 2026-04-11 07:25 UTC | 19m |
| ZSIZB | ZSI | Cape Town International Airport (FACT) | Grand Central Airport (FAGC) | 2026-04-11 05:10 UTC | 2026-04-11 07:23 UTC | 2h 13m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-04-11 07:11 UTC | 2026-04-11 07:19 UTC | 8m |
| EAG9HS | EAG | George Best Belfast City Airport (EGAC) | Southampton Airport (EGHI) | 2026-04-11 05:51 UTC | 2026-04-11 07:18 UTC | 1h 27m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Courchevel Airport (LFLJ) | 2026-04-11 06:54 UTC | 2026-04-11 07:17 UTC | 23m |
| LNK174M | LNK | O. R. Tambo International Airport (FAOR) | Dwaalboom Airport (FADB) | 2026-04-11 06:52 UTC | 2026-04-11 07:15 UTC | 23m |
| APG223 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-04-11 06:50 UTC | 2026-04-11 07:14 UTC | 24m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-04-11 06:18 UTC | 2026-04-11 07:12 UTC | 54m |
| CHX80 | CHX | Weiden in der Oberpfalz Airport (EDQW) | Rosenthal-Field Plossen Airport (EDQP) | 2026-04-11 07:04 UTC | 2026-04-11 07:10 UTC | 5m |
| JA09TR |  | Utsunomiya Airport (RJTU) | Fukushima Airport (RJSF) | 2026-04-11 06:56 UTC | 2026-04-11 07:09 UTC | 13m |
| NJE8RJ | NJE | Linate Airport (LIML) | Samedan Airport (LSZS) | 2026-04-11 06:49 UTC | 2026-04-11 07:08 UTC | 18m |
| HBZUR | HBZ | Wangen-Lachen Airport (LSPV) | Ambri Airport (LSPM) | 2026-04-11 06:14 UTC | 2026-04-11 07:06 UTC | 52m |
| OAL063 | OAL | Paros Airport (LGPA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-11 06:31 UTC | 2026-04-11 07:01 UTC | 30m |
| DAH2610 | DAH | El Bayadh Airport (DAOY) | Pamplona Airport (LEPP) | 2026-04-11 05:36 UTC | 2026-04-11 07:01 UTC | 1h 24m |
| RYR55HB | Ryanair | London Stansted Airport (EGSS) | Perugia / San Egidio Airport (LIRZ) | 2026-04-11 05:17 UTC | 2026-04-11 06:57 UTC | 1h 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
