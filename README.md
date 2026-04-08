# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_22:22:53_UTC-green)

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

**Latest saved flight:** 2026-04-08 22:22:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 22:22:53 UTC

- **24,176** saved flights
- **11,723** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **24,176** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **298,865.7 tonnes** estimated CO2 emissions
- **17,325,547 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 1007 |
| 2 | Ryanair | 1000 |
| 3 | IndiGo | 666 |
| 4 | American Airlines | 442 |
| 5 | EJA | 440 |
| 6 | Southwest Airlines | 347 |
| 7 | ENY | 317 |
| 8 | Lufthansa | 308 |
| 9 | Vueling | 250 |
| 10 | AXM | 244 |
| 11 | LATAM Airlines | 241 |
| 12 | All Nippon Airways | 218 |
| 13 | QLK | 216 |
| 14 | Delta Air Lines | 206 |
| 15 | LXJ | 196 |
| 16 | AZU | 190 |
| 17 | Swiss International | 174 |
| 18 | Alaska Airlines | 164 |
| 19 | Japan Airlines | 162 |
| 20 | VIV | 162 |
| 21 | easyJet | 160 |
| 22 | EJU | 156 |
| 23 | AEE | 151 |
| 24 | WIF | 150 |
| 25 | United Airlines | 148 |
| 26 | Avianca | 142 |
| 27 | EDV | 141 |
| 28 | AXB | 138 |
| 29 | Air France | 125 |
| 30 | ANZ | 125 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18996 |
| 2 | 🇮🇳 IN | 2031 |
| 3 | 🇪🇸 ES | 1830 |
| 4 | 🇦🇺 AU | 1764 |
| 5 | 🇯🇵 JP | 1351 |
| 6 | 🇧🇷 BR | 1349 |
| 7 | 🇨🇴 CO | 1234 |
| 8 | 🇮🇹 IT | 1231 |
| 9 | 🇩🇪 DE | 1231 |
| 10 | 🇨🇦 CA | 1105 |
| 11 | 🇬🇧 GB | 980 |
| 12 | 🇫🇷 FR | 890 |
| 13 | 🇲🇽 MX | 777 |
| 14 | 🇬🇷 GR | 690 |
| 15 | 🇨🇭 CH | 664 |
| 16 | 🇲🇾 MY | 577 |
| 17 | 🇳🇴 NO | 517 |
| 18 | 🇳🇿 NZ | 517 |
| 19 | 🇿🇦 ZA | 516 |
| 20 | 🇬🇹 GT | 480 |
| 21 | 🇹🇷 TR | 464 |
| 22 | 🇵🇭 PH | 451 |
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
| 1 | Dallas-Fort Worth International Airport |  | US | 576 |
| 2 | El Dorado International Airport |  | CO | 457 |
| 3 | Tokyo International Airport |  | JP | 448 |
| 4 | Denver International Airport |  | US | 423 |
| 5 | Indira Gandhi International Airport |  | IN | 419 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 336 |
| 7 | La Aurora Airport |  | GT | 331 |
| 8 | Harry Reid International Airport |  | US | 316 |
| 9 | Zurich Airport |  | CH | 287 |
| 10 | Frankfurt am Main International Airport |  | DE | 263 |
| 11 | Guaymaral Airport |  | CO | 257 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 255 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 252 |
| 14 | Chicago O'Hare International Airport |  | US | 250 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 243 |
| 16 | Macau International Airport |  | MO | 233 |
| 17 | Bengaluru International Airport |  | IN | 228 |
| 18 | Charlotte/Douglas International Airport |  | US | 226 |
| 19 | Kuala Lumpur International Airport |  | MY | 211 |
| 20 | Madrid Barajas International Airport |  | ES | 210 |
| 21 | Tenerife Norte Airport |  | ES | 209 |
| 22 | Ninoy Aquino International Airport |  | PH | 208 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 197 |
| 24 | Malpensa International Airport |  | IT | 196 |
| 25 | Congonhas Airport |  | BR | 193 |
| 26 | Salt Lake City International Airport |  | US | 189 |
| 27 | Daniel K Inouye International Airport |  | US | 183 |
| 28 | Reno/Tahoe International Airport |  | US | 182 |
| 29 | Charles de Gaulle International Airport |  | FR | 175 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 171 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 168 |
| 32 | Miami International Airport |  | US | 164 |
| 33 | O. R. Tambo International Airport |  | ZA | 161 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 160 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 160 |
| 36 | Pune Airport |  | IN | 158 |
| 37 | Seattle-Tacoma International Airport |  | US | 156 |
| 38 | Barcelona International Airport |  | ES | 155 |
| 39 | Vitoria/Foronda Airport |  | ES | 154 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 143 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 114 | 1h 8m | 706 km | 1,388.0 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 99 | 14m | 114 km | 194.2 t |
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
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 47 | 31m | 369 km | 299.2 t |
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
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 34 | 1h 21m | 961 km | 563.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CCDVR | CCD | Comodoro Arturo Merino Benitez International Airport (SCEL) | Eulogio Sanchez Airport (SCTB) | 2026-04-08 22:10 UTC | 2026-04-08 22:22 UTC | 12m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-08 10:32 UTC | 2026-04-08 22:22 UTC | 11h 50m |
| N64256 |  | Ramona Airport (KRNM) | Mc Clellan-Palomar Airport (KCRQ) | 2026-04-08 21:38 UTC | 2026-04-08 22:18 UTC | 39m |
| BLADE35 | BLA | Dave Eby Field (4XA5) | 85OL (85OL) | 2026-04-08 21:22 UTC | 2026-04-08 22:15 UTC | 53m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-04-08 14:18 UTC | 2026-04-08 22:13 UTC | 7h 55m |
| RANGR41 | RAN | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-04-08 21:42 UTC | 2026-04-08 22:12 UTC | 29m |
| N802MM |  | Raleigh-Durham International Airport (KRDU) | Auburn University Regional Airport (KAUO) | 2026-04-08 20:18 UTC | 2026-04-08 22:10 UTC | 1h 52m |
| BCS692 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-08 11:20 UTC | 2026-04-08 22:10 UTC | 10h 49m |
| COBRA67 | COB | California City Municipal Airport (KL71) | Big Bear City Airport (KL35) | 2026-04-08 21:50 UTC | 2026-04-08 22:04 UTC | 13m |
| N293J |  | Gillespie Field (KSEE) | Gillespie Field (KSEE) | 2026-04-08 21:40 UTC | 2026-04-08 22:03 UTC | 22m |
| N9002H |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-04-08 21:32 UTC | 2026-04-08 22:02 UTC | 30m |
| AMMO73 | AMM | California City Municipal Airport (KL71) | Boron Airstrip (57CL) | 2026-04-08 21:50 UTC | 2026-04-08 22:02 UTC | 11m |
| N700JL |  | Indianapolis Regional Airport (KMQJ) | Purdue University Airport (KLAF) | 2026-04-08 21:33 UTC | 2026-04-08 22:01 UTC | 28m |
| N946SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-04-08 21:59 UTC | 2026-04-08 22:00 UTC | 1m |
| N2662B |  | Fort Worth Meacham International Airport (KFTW) | Decatur Municipal Airport (KLUD) | 2026-04-08 21:39 UTC | 2026-04-08 22:00 UTC | 20m |
| N9305N |  | French Valley Airport (KF70) | Hemet-Ryan Airport (KHMT) | 2026-04-08 21:45 UTC | 2026-04-08 21:59 UTC | 14m |
| N92291 |  | Carson City Airport (KCXP) | Carson City Airport (KCXP) | 2026-04-08 21:58 UTC | 2026-04-08 21:58 UTC | 0m |
| N777JQ |  | Palm Springs International Airport (KPSP) | Van Nuys Airport (KVNY) | 2026-04-08 21:30 UTC | 2026-04-08 21:57 UTC | 27m |
| CFNFD | CFN | Edmonton / Villeneuve Airport (CZVL) | Stony Plain (Lichtner Farms) Airport (CSP3) | 2026-04-08 21:43 UTC | 2026-04-08 21:57 UTC | 14m |
| N600WE |  | Birmingham-Shuttlesworth International Airport (KBHM) | Aiken Regional Airport (KAIK) | 2026-04-08 21:09 UTC | 2026-04-08 21:56 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
