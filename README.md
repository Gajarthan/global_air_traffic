# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_23:54:06_UTC-green)

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

**Latest saved flight:** 2026-04-16 23:54:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 23:54:06 UTC

- **38,306** saved flights
- **16,552** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,306** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **463,132.7 tonnes** estimated CO2 emissions
- **26,848,269 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1608 |
| 2 | SkyWest Airlines | 1507 |
| 3 | IndiGo | 932 |
| 4 | EJA | 666 |
| 5 | American Airlines | 644 |
| 6 | Southwest Airlines | 532 |
| 7 | ENY | 500 |
| 8 | AXM | 401 |
| 9 | LATAM Airlines | 386 |
| 10 | Lufthansa | 385 |
| 11 | Vueling | 385 |
| 12 | AZU | 342 |
| 13 | All Nippon Airways | 337 |
| 14 | Delta Air Lines | 326 |
| 15 | QLK | 315 |
| 16 | LXJ | 308 |
| 17 | WIF | 287 |
| 18 | Swiss International | 283 |
| 19 | Alaska Airlines | 255 |
| 20 | AEE | 254 |
| 21 | easyJet | 250 |
| 22 | EJU | 249 |
| 23 | VIV | 244 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 215 |
| 26 | EDV | 211 |
| 27 | United Airlines | 211 |
| 28 | GLO | 200 |
| 29 | JetBlue | 199 |
| 30 | AIQ | 198 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30327 |
| 2 | 🇮🇳 IN | 2854 |
| 3 | 🇪🇸 ES | 2835 |
| 4 | 🇦🇺 AU | 2676 |
| 5 | 🇧🇷 BR | 2261 |
| 6 | 🇯🇵 JP | 2039 |
| 7 | 🇮🇹 IT | 2014 |
| 8 | 🇩🇪 DE | 1946 |
| 9 | 🇨🇴 CO | 1888 |
| 10 | 🇨🇦 CA | 1888 |
| 11 | 🇬🇧 GB | 1573 |
| 12 | 🇫🇷 FR | 1447 |
| 13 | 🇲🇽 MX | 1210 |
| 14 | 🇬🇷 GR | 1149 |
| 15 | 🇨🇭 CH | 1038 |
| 16 | 🇲🇾 MY | 963 |
| 17 | 🇳🇴 NO | 923 |
| 18 | 🇳🇿 NZ | 800 |
| 19 | 🇿🇦 ZA | 799 |
| 20 | 🇵🇭 PH | 708 |
| 21 | 🇹🇭 TH | 690 |
| 22 | 🇹🇷 TR | 685 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 597 |
| 26 | 🇲🇦 MA | 477 |
| 27 | 🇳🇱 NL | 381 |
| 28 | 🇲🇪 ME | 377 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 901 |
| 2 | Tokyo International Airport |  | JP | 694 |
| 3 | El Dorado International Airport |  | CO | 665 |
| 4 | Denver International Airport |  | US | 645 |
| 5 | Indira Gandhi International Airport |  | IN | 617 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 568 |
| 7 | Harry Reid International Airport |  | US | 502 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 458 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 378 |
| 13 | Kuala Lumpur International Airport |  | MY | 375 |
| 14 | Chicago O'Hare International Airport |  | US | 372 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 366 |
| 16 | Macau International Airport |  | MO | 353 |
| 17 | Madrid Barajas International Airport |  | ES | 347 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Congonhas Airport |  | BR | 334 |
| 22 | Ninoy Aquino International Airport |  | PH | 329 |
| 23 | Bengaluru International Airport |  | IN | 328 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 298 |
| 26 | Salt Lake City International Airport |  | US | 291 |
| 27 | Daniel K Inouye International Airport |  | US | 285 |
| 28 | Charles de Gaulle International Airport |  | FR | 282 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 268 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Vitoria/Foronda Airport |  | ES | 260 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 246 |
| 38 | Viracopos International Airport |  | BR | 236 |
| 39 | Don Mueang International Airport |  | TH | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 232 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 175 | 1h 8m | 706 km | 2,130.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 155 | 14m | 114 km | 304.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 138 | 24m | 225 km | 535.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 95 | 21m | 244 km | 400.0 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 87 | 26m | 275 km | 412.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 82 | 54m | 546 km | 772.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 77 | 1h 11m | 770 km | 1,022.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 72 | 45m | 452 km | 561.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 57 | 1h 41m | 1,423 km | 1,398.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 57 | 13m | 99 km | 97.7 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 56 | 26m | 215 km | 207.4 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 29 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 53 | 1h 21m | 961 km | 878.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N871US |  | Pompano Beach Airpark (KPMP) | Miami Homestead General Aviation Airport (KX51) | 2026-04-16 22:20 UTC | 2026-04-16 23:54 UTC | 1h 33m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-16 21:02 UTC | 2026-04-16 23:49 UTC | 2h 47m |
| GRYHK21 | GRY | Miramar Mcas (Joe Foss Field) Airport (KNKX) | CA84 (CA84) | 2026-04-16 22:31 UTC | 2026-04-16 23:47 UTC | 1h 15m |
| N72NG |  | Los Angeles International Airport (KLAX) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-04-16 23:23 UTC | 2026-04-16 23:38 UTC | 14m |
| ASA425 | Alaska Airlines | Portland International Airport (KPDX) | Palm Springs International Airport (KPSP) | 2026-04-16 21:52 UTC | 2026-04-16 23:37 UTC | 1h 44m |
| N129WM |  | Martin State Airport (KMTN) | Martin State Airport (KMTN) | 2026-04-16 23:09 UTC | 2026-04-16 23:37 UTC | 27m |
| BULET53 | BUL | John Wayne/Orange County Airport (KSNA) | Corona Municipal Airport (KAJO) | 2026-04-16 22:33 UTC | 2026-04-16 23:29 UTC | 55m |
| N625MC |  | Spokane International Airport (KGEG) | Boeing Field/King County International Airport (KBFI) | 2026-04-16 22:21 UTC | 2026-04-16 23:23 UTC | 1h 2m |
| G9426581 |  | 0PN4 (0PN4) | Yingst Airport (3PS8) | 2026-04-16 23:06 UTC | 2026-04-16 23:23 UTC | 16m |
| RCA828 | RCA | Billings Logan International Airport (KBIL) | Fort Smith Landing Strip (K5U7) | 2026-04-16 23:09 UTC | 2026-04-16 23:21 UTC | 12m |
| N2936Q |  | Denton Enterprise Airport (KDTO) | 8XS6 (8XS6) | 2026-04-16 22:35 UTC | 2026-04-16 23:19 UTC | 44m |
| N139HN |  | West Virginia International Yeager Airport (KCRW) | West Virginia International Yeager Airport (KCRW) | 2026-04-16 23:17 UTC | 2026-04-16 23:18 UTC | 1m |
| N503RP |  | Oakland County International Airport (KPTK) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-04-16 22:21 UTC | 2026-04-16 23:17 UTC | 56m |
| N21585 |  | Harford County Airport (K0W3) | New Castle Airport (KILG) | 2026-04-16 22:56 UTC | 2026-04-16 23:17 UTC | 20m |
| N317KC |  | Merrill Field (PAMR) | PAFW (PAFW) | 2026-04-16 22:29 UTC | 2026-04-16 23:10 UTC | 41m |
| N749CP |  | Lewis University Airport (KLOT) | Three Cross Ranch Airport (3MT3) | 2026-04-16 21:06 UTC | 2026-04-16 23:10 UTC | 2h 4m |
| N172WG |  | Denton Enterprise Airport (KDTO) | Hardy Field (3XA1) | 2026-04-16 22:59 UTC | 2026-04-16 23:09 UTC | 10m |
| N792BP |  | Portland International Airport (KPDX) | Spokane International Airport (KGEG) | 2026-04-16 22:13 UTC | 2026-04-16 23:07 UTC | 54m |
| QLK9D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-04-16 22:45 UTC | 2026-04-16 23:07 UTC | 21m |
| N224CC |  | West Houston Airport (KIWS) | Gillespie County Airport (KT82) | 2026-04-16 22:03 UTC | 2026-04-16 23:01 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
