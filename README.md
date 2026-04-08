# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_21:39:52_UTC-green)

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

**Latest saved flight:** 2026-04-08 21:39:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 21:39:52 UTC

- **24,057** saved flights
- **11,671** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,057** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **297,504.4 tonnes** estimated CO2 emissions
- **17,246,630 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1004 |
| 2 | Ryanair | 999 |
| 3 | IndiGo | 666 |
| 4 | American Airlines | 441 |
| 5 | EJA | 439 |
| 6 | Southwest Airlines | 344 |
| 7 | ENY | 315 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 238 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 215 |
| 14 | Delta Air Lines | 204 |
| 15 | LXJ | 196 |
| 16 | AZU | 189 |
| 17 | Swiss International | 174 |
| 18 | Alaska Airlines | 162 |
| 19 | Japan Airlines | 162 |
| 20 | VIV | 162 |
| 21 | easyJet | 160 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 148 |
| 26 | Avianca | 142 |
| 27 | EDV | 139 |
| 28 | AXB | 138 |
| 29 | Air France | 125 |
| 30 | BRC | 123 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18855 |
| 2 | 🇮🇳 IN | 2030 |
| 3 | 🇪🇸 ES | 1830 |
| 4 | 🇦🇺 AU | 1758 |
| 5 | 🇯🇵 JP | 1351 |
| 6 | 🇧🇷 BR | 1339 |
| 7 | 🇩🇪 DE | 1229 |
| 8 | 🇨🇴 CO | 1228 |
| 9 | 🇮🇹 IT | 1228 |
| 10 | 🇨🇦 CA | 1097 |
| 11 | 🇬🇧 GB | 978 |
| 12 | 🇫🇷 FR | 889 |
| 13 | 🇲🇽 MX | 773 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇿🇦 ZA | 516 |
| 18 | 🇳🇴 NO | 515 |
| 19 | 🇳🇿 NZ | 509 |
| 20 | 🇬🇹 GT | 477 |
| 21 | 🇹🇷 TR | 463 |
| 22 | 🇵🇭 PH | 449 |
| 23 | 🇰🇷 KR | 428 |
| 24 | 🇹🇭 TH | 390 |
| 25 | 🇵🇱 PL | 356 |
| 26 | 🇲🇦 MA | 294 |
| 27 | 🇮🇩 ID | 251 |
| 28 | 🇧🇸 BS | 250 |
| 29 | 🇲🇪 ME | 250 |
| 30 | 🇳🇱 NL | 239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 573 |
| 2 | El Dorado International Airport |  | CO | 454 |
| 3 | Tokyo International Airport |  | JP | 448 |
| 4 | Denver International Airport |  | US | 420 |
| 5 | Indira Gandhi International Airport |  | IN | 418 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 329 |
| 8 | Harry Reid International Airport |  | US | 315 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Guaymaral Airport |  | CO | 257 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 252 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 251 |
| 14 | Chicago O'Hare International Airport |  | US | 249 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 241 |
| 16 | Macau International Airport |  | MO | 229 |
| 17 | Bengaluru International Airport |  | IN | 228 |
| 18 | Charlotte/Douglas International Airport |  | US | 223 |
| 19 | Kuala Lumpur International Airport |  | MY | 211 |
| 20 | Madrid Barajas International Airport |  | ES | 210 |
| 21 | Tenerife Norte Airport |  | ES | 209 |
| 22 | Ninoy Aquino International Airport |  | PH | 207 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 195 |
| 25 | Congonhas Airport |  | BR | 191 |
| 26 | Salt Lake City International Airport |  | US | 189 |
| 27 | Daniel K Inouye International Airport |  | US | 183 |
| 28 | Reno/Tahoe International Airport |  | US | 182 |
| 29 | Charles de Gaulle International Airport |  | FR | 174 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 166 |
| 32 | Miami International Airport |  | US | 164 |
| 33 | O. R. Tambo International Airport |  | ZA | 161 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 160 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 36 | Pune Airport |  | IN | 158 |
| 37 | Barcelona International Airport |  | ES | 155 |
| 38 | Seattle-Tacoma International Airport |  | US | 154 |
| 39 | Vitoria/Foronda Airport |  | ES | 154 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 142 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 98 | 14m | 114 km | 192.2 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 95 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 90 | 24m | 225 km | 349.2 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 84 | 28m | 304 km | 440.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 70 | 1h 27m | 910 km | 1,098.5 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 70 | 22m | 99 km | 119.9 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 67 | 27m | 152 km | 175.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 66 | 1h 42m | 1,156 km | 1,316.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 58 | 19m | 165 km | 165.0 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 52 | 55m | 546 km | 489.6 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 51 | 1h 13m | 770 km | 677.5 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 46 | 31m | 369 km | 292.8 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 46 | 52m | 556 km | 440.9 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 44 | 46m | 452 km | 342.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 44 | 20m | 250 km | 190.1 t |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 43 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 41 | 1h 43m | 1,423 km | 1,006.2 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 40 | 13m | 99 km | 68.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 36 | 20m | 147 km | 91.1 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 36 | 12m | 15 km | 9.5 t |
| 29 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-04-08 17:27 UTC | 2026-04-08 21:39 UTC | 4h 11m |
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-04-08 11:17 UTC | 2026-04-08 21:38 UTC | 10h 20m |
| TRP7 | TRP | Sandy Point Airport (62MD) | Joint Base Andrews Airport (KADW) | 2026-04-08 21:23 UTC | 2026-04-08 21:36 UTC | 13m |
| AXE6809 | AXE | Billund Airport (EKBI) | Cologne Bonn Airport (EDDK) | 2026-04-08 20:32 UTC | 2026-04-08 21:35 UTC | 1h 3m |
| BLZR250 | BLZ | Kingsville Nas Airport (KNQI) | TE63 (TE63) | 2026-04-08 21:11 UTC | 2026-04-08 21:32 UTC | 21m |
| N5102D |  | Wadsworth Municipal Airport (K3G3) | Wadsworth Municipal Airport (K3G3) | 2026-04-08 20:38 UTC | 2026-04-08 21:31 UTC | 53m |
| LXJ428 | LXJ | Mc Clellan-Palomar Airport (KCRQ) | San Francisco International Airport (KSFO) | 2026-04-08 20:23 UTC | 2026-04-08 21:28 UTC | 1h 4m |
| N26SQ |  | Long Beach (Daugherty Field) Airport (KLGB) | Riverside Airport (KRAL) | 2026-04-08 21:06 UTC | 2026-04-08 21:25 UTC | 18m |
| TGO996 | TGO | Edmonton / Villeneuve (Rose Field) (CRF3) | Barrhead Airport (CEP3) | 2026-04-08 21:10 UTC | 2026-04-08 21:23 UTC | 12m |
| CXK288 | CXK | Fort Worth Meacham International Airport (KFTW) | TX37 (TX37) | 2026-04-08 21:05 UTC | 2026-04-08 21:21 UTC | 16m |
| RYR5YF | Ryanair | Vilnius International Airport (EYVI) | Bamberg-Breitenau Airfield (EDQA) | 2026-04-08 19:47 UTC | 2026-04-08 21:21 UTC | 1h 33m |
| 494LG |  | Simonson Field (80CO) | 14CO (14CO) | 2026-04-08 20:47 UTC | 2026-04-08 21:20 UTC | 33m |
| RANGR41 | RAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-04-08 20:57 UTC | 2026-04-08 21:20 UTC | 23m |
| CGDKX | CGD | Ottawa / Rockcliffe Airport (CYRO) | CPF3 (CPF3) | 2026-04-08 20:44 UTC | 2026-04-08 21:19 UTC | 35m |
| N258EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-04-08 20:24 UTC | 2026-04-08 21:18 UTC | 54m |
| N373EF |  | K7K8 (K7K8) | Ness City Municipal Airport (K48K) | 2026-04-08 20:36 UTC | 2026-04-08 21:17 UTC | 40m |
| CAL007 | CAL | Los Angeles International Airport (KLAX) | Longtan Air Base (RCDI) | 2026-04-08 07:40 UTC | 2026-04-08 21:14 UTC | 13h 34m |
| N406WT |  | Stennis International Airport (KHSA) | Columbia/Marion County Airport (K0R0) | 2026-04-08 20:49 UTC | 2026-04-08 21:14 UTC | 24m |
| N590ER |  | Northern Colorado Regional Airport (KFNL) | 51CO (51CO) | 2026-04-08 20:25 UTC | 2026-04-08 21:13 UTC | 47m |
| N810HW |  | Jackson Regional Airport (KMKL) | Jonesboro Municipal Airport (KJBR) | 2026-04-08 20:31 UTC | 2026-04-08 21:12 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
