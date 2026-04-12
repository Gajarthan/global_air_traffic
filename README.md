# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_09:44:12_UTC-green)

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

**Latest saved flight:** 2026-04-12 09:44:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-12 09:44:12 UTC

- **30,187** saved flights
- **13,836** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **30,187** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **369,578.6 tonnes** estimated CO2 emissions
- **21,424,845 km** total distance flown
- **847 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1239 |
| 2 | SkyWest Airlines | 1230 |
| 3 | IndiGo | 787 |
| 4 | American Airlines | 524 |
| 5 | EJA | 523 |
| 6 | Southwest Airlines | 436 |
| 7 | ENY | 408 |
| 8 | Lufthansa | 363 |
| 9 | AXM | 326 |
| 10 | Vueling | 310 |
| 11 | LATAM Airlines | 295 |
| 12 | All Nippon Airways | 280 |
| 13 | AZU | 262 |
| 14 | QLK | 259 |
| 15 | Delta Air Lines | 247 |
| 16 | LXJ | 240 |
| 17 | Swiss International | 218 |
| 18 | Alaska Airlines | 201 |
| 19 | easyJet | 198 |
| 20 | Japan Airlines | 197 |
| 21 | VIV | 196 |
| 22 | EJU | 195 |
| 23 | AEE | 191 |
| 24 | WIF | 189 |
| 25 | United Airlines | 179 |
| 26 | EDV | 178 |
| 27 | Avianca | 167 |
| 28 | GLO | 160 |
| 29 | AIQ | 159 |
| 30 | JetBlue | 159 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 23812 |
| 2 | 🇮🇳 IN | 2416 |
| 3 | 🇪🇸 ES | 2228 |
| 4 | 🇦🇺 AU | 2158 |
| 5 | 🇧🇷 BR | 1733 |
| 6 | 🇯🇵 JP | 1681 |
| 7 | 🇮🇹 IT | 1553 |
| 8 | 🇨🇴 CO | 1518 |
| 9 | 🇩🇪 DE | 1508 |
| 10 | 🇨🇦 CA | 1477 |
| 11 | 🇬🇧 GB | 1216 |
| 12 | 🇫🇷 FR | 1105 |
| 13 | 🇲🇽 MX | 974 |
| 14 | 🇬🇷 GR | 861 |
| 15 | 🇨🇭 CH | 845 |
| 16 | 🇲🇾 MY | 781 |
| 17 | 🇳🇿 NZ | 665 |
| 18 | 🇳🇴 NO | 637 |
| 19 | 🇿🇦 ZA | 618 |
| 20 | 🇵🇭 PH | 569 |
| 21 | 🇹🇭 TH | 557 |
| 22 | 🇬🇹 GT | 553 |
| 23 | 🇹🇷 TR | 550 |
| 24 | 🇰🇷 KR | 520 |
| 25 | 🇵🇱 PL | 455 |
| 26 | 🇲🇦 MA | 378 |
| 27 | 🇧🇸 BS | 318 |
| 28 | 🇲🇪 ME | 303 |
| 29 | 🇳🇱 NL | 287 |
| 30 | 🇮🇩 ID | 287 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 720 |
| 2 | Tokyo International Airport |  | JP | 566 |
| 3 | El Dorado International Airport |  | CO | 541 |
| 4 | Denver International Airport |  | US | 512 |
| 5 | Indira Gandhi International Airport |  | IN | 509 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 421 |
| 7 | La Aurora Airport |  | GT | 394 |
| 8 | Harry Reid International Airport |  | US | 391 |
| 9 | Zurich Airport |  | CH | 360 |
| 10 | Guaymaral Airport |  | CO | 359 |
| 11 | Chicago O'Hare International Airport |  | US | 314 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 313 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 311 |
| 14 | Frankfurt am Main International Airport |  | DE | 305 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 300 |
| 16 | Kuala Lumpur International Airport |  | MY | 295 |
| 17 | Macau International Airport |  | MO | 286 |
| 18 | Bengaluru International Airport |  | IN | 274 |
| 19 | Charlotte/Douglas International Airport |  | US | 271 |
| 20 | Madrid Barajas International Airport |  | ES | 264 |
| 21 | Tenerife Norte Airport |  | ES | 263 |
| 22 | Ninoy Aquino International Airport |  | PH | 261 |
| 23 | Congonhas Airport |  | BR | 253 |
| 24 | Malpensa International Airport |  | IT | 242 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 234 |
| 26 | Daniel K Inouye International Airport |  | US | 231 |
| 27 | Reno/Tahoe International Airport |  | US | 230 |
| 28 | Salt Lake City International Airport |  | US | 230 |
| 29 | Charles de Gaulle International Airport |  | FR | 215 |
| 30 | Capua Airport |  | IT | 209 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 207 |
| 32 | Netaji Subhash Chandra Bose International Airport |  | IN | 205 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 204 |
| 34 | Miami International Airport |  | US | 202 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 201 |
| 36 | O. R. Tambo International Airport |  | ZA | 197 |
| 37 | Vitoria/Foronda Airport |  | ES | 196 |
| 38 | Seattle-Tacoma International Airport |  | US | 192 |
| 39 | Barcelona International Airport |  | ES | 190 |
| 40 | Don Mueang International Airport |  | TH | 189 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 144 | 1h 8m | 706 km | 1,753.2 t |
| 2 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 139 | 26m | - | - |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 126 | 14m | 114 km | 247.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 112 | 24m | 225 km | 434.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 103 | 28m | 304 km | 540.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 89 | 1h 27m | 910 km | 1,396.6 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 77 | 19m | 165 km | 219.0 t |
| 8 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 76 | 21m | 99 km | 130.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 73 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 69 | 55m | 546 km | 649.6 t |
| 11 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 69 | 27m | 152 km | 180.3 t |
| 12 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 13 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 65 | 9m | - | - |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 64 | 1h 12m | 770 km | 850.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 63 | 27m | 275 km | 298.5 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 59 | 31m | 369 km | 375.5 t |
| 17 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 57 | 45m | 452 km | 444.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 57 | 52m | 556 km | 546.4 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 54 | 21m | 244 km | 227.4 t |
| 21 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 50 | 13m | 99 km | 85.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 50 | 20m | 250 km | 216.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 47 | 20m | 147 km | 118.9 t |
| 24 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 46 | 1h 42m | 1,423 km | 1,128.9 t |
| 26 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 42 | 1h 19m | 961 km | 696.2 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 41 | 12m | 15 km | 10.8 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 40 | 14m | 154 km | 106.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-12 08:41 UTC | 2026-04-12 09:44 UTC | 1h 2m |
| EVA218 | EVA Air | Kuala Lumpur International Airport (WMKK) | Taiwan Taoyuan International Airport (RCTP) | 2026-04-12 05:31 UTC | 2026-04-12 09:31 UTC | 4h 0m |
| ZKIWG | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-04-12 09:08 UTC | 2026-04-12 09:28 UTC | 20m |
| YOJ | YOJ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-12 08:28 UTC | 2026-04-12 09:23 UTC | 54m |
| WIF3T | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-04-12 08:58 UTC | 2026-04-12 09:11 UTC | 13m |
| N7344L |  | CA40 (CA40) | Sequoia Field (KD86) | 2026-04-12 07:50 UTC | 2026-04-12 09:03 UTC | 1h 12m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-04-12 08:42 UTC | 2026-04-12 08:57 UTC | 14m |
| RGA03 | RGA | Reichenbach Air Base (LSGR) | Bern Belp Airport (LSZB) | 2026-04-12 08:37 UTC | 2026-04-12 08:52 UTC | 14m |
| DRK541 | DRK | Singapore Changi International Airport (WSSS) | Shillong Airport (VEBI) | 2026-04-12 04:58 UTC | 2026-04-12 08:48 UTC | 3h 50m |
| SEH1SM | SEH | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-12 08:19 UTC | 2026-04-12 08:46 UTC | 26m |
| IGO874 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Sarsawa Air Force Station (VISP) | 2026-04-12 06:36 UTC | 2026-04-12 08:44 UTC | 2h 7m |
| EZY85PB | easyJet | London Gatwick Airport (EGKK) | Capua Airport (LIAU) | 2026-04-12 06:35 UTC | 2026-04-12 08:43 UTC | 2h 8m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 07:01 UTC | 2026-04-12 08:43 UTC | 1h 42m |
| FD618 |  | Perth Jandakot Airport (YPJT) | Dongara Airport (YDRA) | 2026-04-12 07:58 UTC | 2026-04-12 08:43 UTC | 44m |
| OAL084 | OAL | Thessaloniki Macedonia International Airport (LGTS) | Olimboi Airport (LG56) | 2026-04-12 08:04 UTC | 2026-04-12 08:43 UTC | 38m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-12 07:05 UTC | 2026-04-12 08:42 UTC | 1h 37m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Simara Airport (VNSI) | 2026-04-12 05:23 UTC | 2026-04-12 08:41 UTC | 3h 17m |
| FDR304 | FDR | O. R. Tambo International Airport (FAOR) | Pilanesberg International Airport (FAPN) | 2026-04-12 07:58 UTC | 2026-04-12 08:40 UTC | 41m |
| PGT1863 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-04-12 07:43 UTC | 2026-04-12 08:39 UTC | 56m |
| ITY1463 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Venezia / Tessera -  Marco Polo Airport (LIPZ) | 2026-04-12 07:59 UTC | 2026-04-12 08:39 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
