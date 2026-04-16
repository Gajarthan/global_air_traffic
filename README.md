# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_21:34:28_UTC-green)

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

**Latest saved flight:** 2026-04-16 21:34:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-16 21:34:28 UTC

- **38,153** saved flights
- **16,490** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,153** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **461,319.4 tonnes** estimated CO2 emissions
- **26,743,155 km** total distance flown
- **841 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1608 |
| 2 | SkyWest Airlines | 1501 |
| 3 | IndiGo | 932 |
| 4 | EJA | 664 |
| 5 | American Airlines | 641 |
| 6 | Southwest Airlines | 528 |
| 7 | ENY | 496 |
| 8 | AXM | 401 |
| 9 | Lufthansa | 385 |
| 10 | Vueling | 385 |
| 11 | LATAM Airlines | 383 |
| 12 | AZU | 341 |
| 13 | All Nippon Airways | 337 |
| 14 | Delta Air Lines | 324 |
| 15 | QLK | 313 |
| 16 | LXJ | 307 |
| 17 | WIF | 287 |
| 18 | Swiss International | 283 |
| 19 | AEE | 254 |
| 20 | Alaska Airlines | 253 |
| 21 | easyJet | 250 |
| 22 | EJU | 249 |
| 23 | VIV | 243 |
| 24 | Japan Airlines | 227 |
| 25 | Air France | 215 |
| 26 | United Airlines | 211 |
| 27 | EDV | 210 |
| 28 | GLO | 199 |
| 29 | AIQ | 198 |
| 30 | JetBlue | 198 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30140 |
| 2 | 🇮🇳 IN | 2854 |
| 3 | 🇪🇸 ES | 2835 |
| 4 | 🇦🇺 AU | 2655 |
| 5 | 🇧🇷 BR | 2249 |
| 6 | 🇯🇵 JP | 2037 |
| 7 | 🇮🇹 IT | 2014 |
| 8 | 🇩🇪 DE | 1945 |
| 9 | 🇨🇴 CO | 1882 |
| 10 | 🇨🇦 CA | 1870 |
| 11 | 🇬🇧 GB | 1573 |
| 12 | 🇫🇷 FR | 1446 |
| 13 | 🇲🇽 MX | 1204 |
| 14 | 🇬🇷 GR | 1149 |
| 15 | 🇨🇭 CH | 1037 |
| 16 | 🇲🇾 MY | 963 |
| 17 | 🇳🇴 NO | 923 |
| 18 | 🇿🇦 ZA | 799 |
| 19 | 🇳🇿 NZ | 791 |
| 20 | 🇵🇭 PH | 704 |
| 21 | 🇹🇭 TH | 690 |
| 22 | 🇹🇷 TR | 683 |
| 23 | 🇬🇹 GT | 651 |
| 24 | 🇰🇷 KR | 627 |
| 25 | 🇵🇱 PL | 597 |
| 26 | 🇲🇦 MA | 477 |
| 27 | 🇳🇱 NL | 380 |
| 28 | 🇲🇪 ME | 377 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 353 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 894 |
| 2 | Tokyo International Airport |  | JP | 693 |
| 3 | El Dorado International Airport |  | CO | 662 |
| 4 | Denver International Airport |  | US | 642 |
| 5 | Indira Gandhi International Airport |  | IN | 617 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 568 |
| 7 | Harry Reid International Airport |  | US | 498 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 478 |
| 10 | Zurich Airport |  | CH | 457 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 381 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 377 |
| 13 | Kuala Lumpur International Airport |  | MY | 375 |
| 14 | Chicago O'Hare International Airport |  | US | 370 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 361 |
| 16 | Macau International Airport |  | MO | 348 |
| 17 | Madrid Barajas International Airport |  | ES | 347 |
| 18 | Frankfurt am Main International Airport |  | DE | 346 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 340 |
| 21 | Congonhas Airport |  | BR | 331 |
| 22 | Bengaluru International Airport |  | IN | 328 |
| 23 | Ninoy Aquino International Airport |  | PH | 327 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 296 |
| 26 | Salt Lake City International Airport |  | US | 290 |
| 27 | Daniel K Inouye International Airport |  | US | 284 |
| 28 | Charles de Gaulle International Airport |  | FR | 281 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 268 |
| 31 | Capua Airport |  | IT | 262 |
| 32 | Vitoria/Foronda Airport |  | ES | 260 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 257 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 251 |
| 37 | Barcelona International Airport |  | ES | 246 |
| 38 | Don Mueang International Airport |  | TH | 236 |
| 39 | Viracopos International Airport |  | BR | 235 |
| 40 | Seattle-Tacoma International Airport |  | US | 230 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 174 | 1h 8m | 706 km | 2,118.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 154 | 14m | 114 km | 302.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 136 | 24m | 225 km | 527.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 109 | 1h 27m | 910 km | 1,710.5 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 96 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 94 | 21m | 244 km | 395.8 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 94 | 9m | - | - |
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
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 54 | 1h 53m | 1,304 km | 1,214.9 t |
| 29 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 53 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SHARP41 | SHA | 75OK (75OK) | Ramey 1 Airport (0OK8) | 2026-04-16 21:21 UTC | 2026-04-16 21:34 UTC | 12m |
| GOAT52 | GOA | Randolph Afb Airport (KRND) | Card Airfield (4XA2) | 2026-04-16 21:08 UTC | 2026-04-16 21:33 UTC | 24m |
| N7288F |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-04-16 20:55 UTC | 2026-04-16 21:31 UTC | 36m |
| N55297 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-04-16 20:43 UTC | 2026-04-16 21:27 UTC | 44m |
| QXE2099 | QXE | Boise Air Trml/Gowen Field (KBOI) | Palm Springs International Airport (KPSP) | 2026-04-16 19:43 UTC | 2026-04-16 21:23 UTC | 1h 40m |
| BRG594 | BRG | Buckland Airport (PABL) | Selawik Airport (PASK) | 2026-04-16 20:59 UTC | 2026-04-16 21:19 UTC | 20m |
| N183BA |  | Norwood Memorial Airport (KOWD) | Boire Field (KASH) | 2026-04-16 20:28 UTC | 2026-04-16 21:18 UTC | 49m |
| N7820C |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Kansas City/Lee's Summit Regional Airport (KLXT) | 2026-04-16 21:13 UTC | 2026-04-16 21:13 UTC | 0m |
| SWA2069 | Southwest Airlines | St Louis Lambert International Airport (KSTL) | High Valley Airpark (GA87) | 2026-04-16 19:41 UTC | 2026-04-16 21:11 UTC | 1h 29m |
| PVL834 | PVL | Québec City Jean Lesage International Airport (CYQB) | Grandes-Bergeronnes Airport (CTH3) | 2026-04-16 20:48 UTC | 2026-04-16 21:09 UTC | 20m |
| N800VP |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-04-16 20:36 UTC | 2026-04-16 21:07 UTC | 30m |
| SRD336 | SRD | Anglesey Airport (EGOV) | Caernarfon Airport (EGCK) | 2026-04-16 20:56 UTC | 2026-04-16 21:06 UTC | 10m |
| N311ZZ |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-04-16 20:45 UTC | 2026-04-16 21:05 UTC | 19m |
| N786SA |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-04-16 19:54 UTC | 2026-04-16 21:04 UTC | 1h 10m |
| DLX25 | DLX | Brown Field Municipal Airport (KSDM) | Scottsdale Airport (KSDL) | 2026-04-16 20:17 UTC | 2026-04-16 21:03 UTC | 46m |
| N503QF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-16 20:58 UTC | 2026-04-16 21:02 UTC | 3m |
| TRF587 | TRF | Addison Airport (KADS) | Commerce Municipal Airport (K2F7) | 2026-04-16 20:32 UTC | 2026-04-16 20:59 UTC | 27m |
| ARG1788 | ARG | Jorge Newbery Airpark (SABE) | El Dorado Airport (SATD) | 2026-04-16 19:42 UTC | 2026-04-16 20:57 UTC | 1h 15m |
| EJM205 | EJM | Norman Y Mineta San Jose International Airport (KSJC) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-16 20:45 UTC | 2026-04-16 20:56 UTC | 10m |
| ITY1625 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Taranto / Grottaglie Airport (LIBG) | 2026-04-16 20:06 UTC | 2026-04-16 20:53 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
