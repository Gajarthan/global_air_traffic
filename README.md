# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_22:08:59_UTC-green)

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

**Latest saved flight:** 2026-04-13 22:08:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 22:08:59 UTC

- **33,104** saved flights
- **14,834** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,104** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **407,678.0 tonnes** estimated CO2 emissions
- **23,633,508 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1411 |
| 2 | SkyWest Airlines | 1338 |
| 3 | IndiGo | 839 |
| 4 | American Airlines | 579 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 481 |
| 7 | ENY | 444 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 345 |
| 10 | Vueling | 340 |
| 11 | LATAM Airlines | 331 |
| 12 | All Nippon Airways | 297 |
| 13 | AZU | 293 |
| 14 | Delta Air Lines | 276 |
| 15 | LXJ | 270 |
| 16 | QLK | 267 |
| 17 | Swiss International | 252 |
| 18 | WIF | 225 |
| 19 | Alaska Airlines | 223 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | AEE | 215 |
| 23 | VIV | 215 |
| 24 | Japan Airlines | 206 |
| 25 | United Airlines | 193 |
| 26 | EDV | 192 |
| 27 | GLO | 180 |
| 28 | JetBlue | 179 |
| 29 | Air France | 178 |
| 30 | Avianca | 177 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26125 |
| 2 | 🇮🇳 IN | 2564 |
| 3 | 🇪🇸 ES | 2492 |
| 4 | 🇦🇺 AU | 2263 |
| 5 | 🇧🇷 BR | 1946 |
| 6 | 🇯🇵 JP | 1781 |
| 7 | 🇮🇹 IT | 1770 |
| 8 | 🇩🇪 DE | 1663 |
| 9 | 🇨🇴 CO | 1647 |
| 10 | 🇨🇦 CA | 1619 |
| 11 | 🇬🇧 GB | 1357 |
| 12 | 🇫🇷 FR | 1219 |
| 13 | 🇲🇽 MX | 1052 |
| 14 | 🇬🇷 GR | 968 |
| 15 | 🇨🇭 CH | 921 |
| 16 | 🇲🇾 MY | 835 |
| 17 | 🇳🇴 NO | 747 |
| 18 | 🇳🇿 NZ | 698 |
| 19 | 🇿🇦 ZA | 682 |
| 20 | 🇹🇷 TR | 618 |
| 21 | 🇵🇭 PH | 616 |
| 22 | 🇬🇹 GT | 598 |
| 23 | 🇹🇭 TH | 597 |
| 24 | 🇰🇷 KR | 560 |
| 25 | 🇵🇱 PL | 518 |
| 26 | 🇲🇦 MA | 423 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 330 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇲🇴 MO | 312 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 790 |
| 2 | Tokyo International Airport |  | JP | 604 |
| 3 | El Dorado International Airport |  | CO | 585 |
| 4 | Denver International Airport |  | US | 561 |
| 5 | Indira Gandhi International Airport |  | IN | 544 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 473 |
| 7 | La Aurora Airport |  | GT | 435 |
| 8 | Harry Reid International Airport |  | US | 431 |
| 9 | Zurich Airport |  | CH | 412 |
| 10 | Guaymaral Airport |  | CO | 405 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 341 |
| 12 | Chicago O'Hare International Airport |  | US | 340 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 336 |
| 14 | Frankfurt am Main International Airport |  | DE | 325 |
| 15 | Kuala Lumpur International Airport |  | MY | 321 |
| 16 | Macau International Airport |  | MO | 312 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 18 | Madrid Barajas International Airport |  | ES | 302 |
| 19 | Charlotte/Douglas International Airport |  | US | 300 |
| 20 | Bengaluru International Airport |  | IN | 296 |
| 21 | Tenerife Norte Airport |  | ES | 294 |
| 22 | Congonhas Airport |  | BR | 290 |
| 23 | Ninoy Aquino International Airport |  | PH | 286 |
| 24 | Malpensa International Airport |  | IT | 271 |
| 25 | Daniel K Inouye International Airport |  | US | 254 |
| 26 | Atizapan De Zaragoza Airport |  | MX | 252 |
| 27 | Salt Lake City International Airport |  | US | 248 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 240 |
| 30 | Capua Airport |  | IT | 236 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 233 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 227 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 226 |
| 35 | O. R. Tambo International Airport |  | ZA | 223 |
| 36 | Vitoria/Foronda Airport |  | ES | 222 |
| 37 | Miami International Airport |  | US | 214 |
| 38 | Barcelona International Airport |  | ES | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 207 |
| 40 | Calgary International Airport |  | CA | 204 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 152 | 1h 8m | 706 km | 1,850.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 136 | 14m | 114 km | 266.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 106 | 28m | 304 km | 555.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 93 | 1h 27m | 910 km | 1,459.4 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 85 | 19m | 165 km | 241.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 80 | 9m | - | - |
| 10 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 74 | 54m | 546 km | 696.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 72 | 21m | 244 km | 303.2 t |
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
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 47 | 12m | 15 km | 12.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 46 | 1h 53m | 1,304 km | 1,034.9 t |
| 30 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-13 10:57 UTC | 2026-04-13 22:08 UTC | 11h 11m |
| BCS642 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-13 04:23 UTC | 2026-04-13 22:06 UTC | 17h 42m |
| CPA2040 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-13 10:36 UTC | 2026-04-13 22:02 UTC | 11h 26m |
| TRP7 | TRP | Robinson Airport (MD14) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-04-13 21:46 UTC | 2026-04-13 21:57 UTC | 11m |
| BB253 |  | Collier/Pine Barren Airpark (FD89) | I H Bass Jr Memorial Airport (K4R1) | 2026-04-13 21:00 UTC | 2026-04-13 21:51 UTC | 51m |
| N334AM |  | Truckee-Tahoe Airport (KTRK) | Santa Monica Municipal Airport (KSMO) | 2026-04-13 20:30 UTC | 2026-04-13 21:50 UTC | 1h 20m |
| CXK447 | CXK | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-04-13 20:58 UTC | 2026-04-13 21:50 UTC | 51m |
| N874C |  | Van Nuys Airport (KVNY) | Moffett Federal Airfield (KNUQ) | 2026-04-13 20:56 UTC | 2026-04-13 21:46 UTC | 49m |
| XSN06 | XSN | Buchanan Field (KCCR) | North Las Vegas Airport (KVGT) | 2026-04-13 20:10 UTC | 2026-04-13 21:45 UTC | 1h 35m |
| N904PJ |  | Oakland San Francisco Bay Airport (KOAK) | Garberville Airport (KO16) | 2026-04-13 20:52 UTC | 2026-04-13 21:39 UTC | 47m |
| N7227Q |  | Amacher Strip (TN39) | Amacher Strip (TN39) | 2026-04-13 21:24 UTC | 2026-04-13 21:37 UTC | 12m |
| N172SX |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-04-13 21:17 UTC | 2026-04-13 21:36 UTC | 18m |
| N75UM |  | Livingston County/Spencer J Hardy Airport (KOZW) | Delta County Airport (KESC) | 2026-04-13 20:58 UTC | 2026-04-13 21:32 UTC | 33m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-04-13 21:01 UTC | 2026-04-13 21:30 UTC | 29m |
| SL84 |  | Rota Naval Station Airport (LERT) | Rota Naval Station Airport (LERT) | 2026-04-13 19:45 UTC | 2026-04-13 21:29 UTC | 1h 44m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-04-13 17:37 UTC | 2026-04-13 21:28 UTC | 3h 51m |
| QXE2099 | QXE | Boise Air Trml/Gowen Field (KBOI) | Palm Springs International Airport (KPSP) | 2026-04-13 19:43 UTC | 2026-04-13 21:28 UTC | 1h 44m |
| JRE301 | JRE | Nashville International Airport (KBNA) | Dubuque Regional Airport (KDBQ) | 2026-04-13 19:59 UTC | 2026-04-13 21:28 UTC | 1h 29m |
| AAL418 | American Airlines | Chicago O'Hare International Airport (KORD) | St Louis Lambert International Airport (KSTL) | 2026-04-13 20:38 UTC | 2026-04-13 21:27 UTC | 49m |
| CRN811 | CRN | Vancouver International Airport (CYVR) | Kaslo Airport (CBR2) | 2026-04-13 20:33 UTC | 2026-04-13 21:26 UTC | 52m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
