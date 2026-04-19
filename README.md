# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_22:42:50_UTC-green)

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

**Latest saved flight:** 2026-04-19 22:42:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-19 22:42:50 UTC

- **44,309** saved flights
- **18,424** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **44,309** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **533,790.2 tonnes** estimated CO2 emissions
- **30,944,362 km** total distance flown
- **839 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1868 |
| 2 | SkyWest Airlines | 1732 |
| 3 | IndiGo | 1071 |
| 4 | EJA | 776 |
| 5 | American Airlines | 736 |
| 6 | Southwest Airlines | 630 |
| 7 | ENY | 578 |
| 8 | AXM | 446 |
| 9 | Vueling | 444 |
| 10 | LATAM Airlines | 439 |
| 11 | Lufthansa | 438 |
| 12 | All Nippon Airways | 397 |
| 13 | AZU | 387 |
| 14 | Delta Air Lines | 380 |
| 15 | QLK | 355 |
| 16 | LXJ | 354 |
| 17 | WIF | 344 |
| 18 | Swiss International | 339 |
| 19 | Alaska Airlines | 303 |
| 20 | AEE | 301 |
| 21 | EJU | 291 |
| 22 | easyJet | 284 |
| 23 | VIV | 283 |
| 24 | Japan Airlines | 269 |
| 25 | Air France | 250 |
| 26 | United Airlines | 238 |
| 27 | JetBlue | 235 |
| 28 | AXB | 232 |
| 29 | GLO | 232 |
| 30 | EDV | 225 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 35196 |
| 2 | 🇮🇳 IN | 3301 |
| 3 | 🇪🇸 ES | 3260 |
| 4 | 🇦🇺 AU | 3046 |
| 5 | 🇧🇷 BR | 2642 |
| 6 | 🇯🇵 JP | 2413 |
| 7 | 🇮🇹 IT | 2344 |
| 8 | 🇩🇪 DE | 2241 |
| 9 | 🇨🇦 CA | 2164 |
| 10 | 🇨🇴 CO | 2045 |
| 11 | 🇬🇧 GB | 1796 |
| 12 | 🇫🇷 FR | 1684 |
| 13 | 🇲🇽 MX | 1380 |
| 14 | 🇬🇷 GR | 1360 |
| 15 | 🇨🇭 CH | 1204 |
| 16 | 🇳🇴 NO | 1095 |
| 17 | 🇲🇾 MY | 1090 |
| 18 | 🇿🇦 ZA | 917 |
| 19 | 🇳🇿 NZ | 885 |
| 20 | 🇵🇭 PH | 794 |
| 21 | 🇹🇷 TR | 781 |
| 22 | 🇹🇭 TH | 780 |
| 23 | 🇬🇹 GT | 730 |
| 24 | 🇰🇷 KR | 728 |
| 25 | 🇵🇱 PL | 702 |
| 26 | 🇲🇦 MA | 550 |
| 27 | 🇲🇪 ME | 467 |
| 28 | 🇳🇱 NL | 452 |
| 29 | 🇧🇸 BS | 411 |
| 30 | 🇲🇴 MO | 409 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1043 |
| 2 | Tokyo International Airport |  | JP | 825 |
| 3 | Denver International Airport |  | US | 741 |
| 4 | El Dorado International Airport |  | CO | 713 |
| 5 | Indira Gandhi International Airport |  | IN | 711 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 676 |
| 7 | Harry Reid International Airport |  | US | 569 |
| 8 | Guaymaral Airport |  | CO | 560 |
| 9 | La Aurora Airport |  | GT | 538 |
| 10 | Zurich Airport |  | CH | 528 |
| 11 | Chicago O'Hare International Airport |  | US | 439 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 437 |
| 13 | Kuala Lumpur International Airport |  | MY | 432 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 431 |
| 15 | Frankfurt am Main International Airport |  | DE | 412 |
| 16 | Macau International Airport |  | MO | 409 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 408 |
| 18 | Madrid Barajas International Airport |  | ES | 394 |
| 19 | Bengaluru International Airport |  | IN | 392 |
| 20 | Tenerife Norte Airport |  | ES | 390 |
| 21 | Charlotte/Douglas International Airport |  | US | 387 |
| 22 | Congonhas Airport |  | BR | 378 |
| 23 | Malpensa International Airport |  | IT | 371 |
| 24 | Ninoy Aquino International Airport |  | PH | 368 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 335 |
| 26 | Salt Lake City International Airport |  | US | 335 |
| 27 | Daniel K Inouye International Airport |  | US | 328 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 328 |
| 29 | Charles de Gaulle International Airport |  | FR | 325 |
| 30 | Reno/Tahoe International Airport |  | US | 309 |
| 31 | Vitoria/Foronda Airport |  | ES | 307 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 306 |
| 33 | Capua Airport |  | IT | 305 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 300 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 296 |
| 36 | O. R. Tambo International Airport |  | ZA | 294 |
| 37 | Barcelona International Airport |  | ES | 286 |
| 38 | Calgary International Airport |  | CA | 271 |
| 39 | Viracopos International Airport |  | BR | 269 |
| 40 | Don Mueang International Airport |  | TH | 265 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 225 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 204 | 1h 8m | 706 km | 2,483.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 167 | 14m | 114 km | 327.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 160 | 24m | 225 km | 620.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 132 | 28m | 304 km | 692.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 128 | 1h 27m | 910 km | 2,008.6 t |
| 7 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 124 | 21m | 244 km | 522.1 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 118 | 19m | 165 km | 335.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 117 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 109 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 102 | 26m | 275 km | 483.3 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 96 | 54m | 546 km | 903.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 91 | 44m | 452 km | 709.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 83 | 1h 11m | 770 km | 1,102.6 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 78 | 31m | 369 km | 496.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 72 | 20m | 147 km | 182.2 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 72 | 20m | 250 km | 311.0 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 71 | 52m | 556 km | 680.6 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 68 | 26m | 215 km | 251.8 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 63 | 1h 41m | 1,423 km | 1,546.1 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 62 | 13m | 99 km | 106.3 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 62 | 1h 52m | 1,304 km | 1,394.8 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 61 | 57m | 493 km | 519.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 60 | 1h 0m | 695 km | 719.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N781AC |  | Iowa City Municipal Airport (KIOW) | Iowa City Municipal Airport (KIOW) | 2026-04-19 21:54 UTC | 2026-04-19 22:42 UTC | 47m |
| N1910R |  | Esquipulas Airport (MGES) | La Aurora Airport (MGGT) | 2026-04-19 22:08 UTC | 2026-04-19 22:41 UTC | 32m |
| YNH | YNH | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-04-19 21:34 UTC | 2026-04-19 22:36 UTC | 1h 1m |
| BOE919 | BOE | Grant County International Airport (KMWH) | Boeing Field/King County International Airport (KBFI) | 2026-04-19 22:06 UTC | 2026-04-19 22:32 UTC | 26m |
| GAF729 | GAF | Cologne Bonn Airport (EDDK) | Salt Lake City International Airport (KSLC) | 2026-04-19 08:53 UTC | 2026-04-19 22:26 UTC | 13h 32m |
| N127KC |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-04-19 21:17 UTC | 2026-04-19 22:21 UTC | 1h 4m |
| N234WL |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-04-19 21:43 UTC | 2026-04-19 22:21 UTC | 37m |
| CPA068 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-04-19 11:40 UTC | 2026-04-19 22:21 UTC | 10h 40m |
| ZHU | ZHU | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-04-19 21:56 UTC | 2026-04-19 22:20 UTC | 24m |
| LFA323 | LFA | Orlando Sanford International Airport (KSFB) | Leesburg International Airport (KLEE) | 2026-04-19 21:26 UTC | 2026-04-19 22:20 UTC | 54m |
| N8288R |  | Kansas City Downtown/Wheeler Field (KMKC) | Alford Airpark (IN03) | 2026-04-19 21:26 UTC | 2026-04-19 22:18 UTC | 52m |
| AAE117 | AAE | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-04-19 07:37 UTC | 2026-04-19 22:15 UTC | 14h 37m |
| TKR40 | TKR | Skyotee Ranch Airport (CL74) | Agro-West Airport (5CA7) | 2026-04-19 21:53 UTC | 2026-04-19 22:14 UTC | 21m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-04-19 14:14 UTC | 2026-04-19 22:13 UTC | 7h 58m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-04-19 10:19 UTC | 2026-04-19 22:10 UTC | 11h 51m |
| N7013G |  | Hicks Airfield (KT67) | Kenneth Copeland Airport (K4T2) | 2026-04-19 22:05 UTC | 2026-04-19 22:10 UTC | 5m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-04-19 21:51 UTC | 2026-04-19 22:09 UTC | 18m |
| TKR12 | TKR | General Wm J Fox Airfield (KWJF) | Big Bear City Airport (KL35) | 2026-04-19 21:51 UTC | 2026-04-19 22:07 UTC | 15m |
| N151LN |  | Robins Afb Airport (KWRB) | Rollins Airport (GA53) | 2026-04-19 21:18 UTC | 2026-04-19 22:05 UTC | 46m |
| N532CP |  | Chino Airport (KCNO) | Meadows Field (KBFL) | 2026-04-19 21:38 UTC | 2026-04-19 22:03 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
