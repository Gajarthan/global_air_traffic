# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_11:28:24_UTC-green)

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

**Latest saved flight:** 2026-04-13 11:28:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-13 11:28:24 UTC

- **31,985** saved flights
- **14,429** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **31,985** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **394,490.9 tonnes** estimated CO2 emissions
- **22,869,037 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1353 |
| 2 | SkyWest Airlines | 1295 |
| 3 | IndiGo | 823 |
| 4 | EJA | 556 |
| 5 | American Airlines | 554 |
| 6 | Southwest Airlines | 464 |
| 7 | ENY | 429 |
| 8 | Lufthansa | 376 |
| 9 | AXM | 340 |
| 10 | Vueling | 326 |
| 11 | LATAM Airlines | 324 |
| 12 | All Nippon Airways | 296 |
| 13 | AZU | 285 |
| 14 | QLK | 266 |
| 15 | Delta Air Lines | 265 |
| 16 | LXJ | 254 |
| 17 | Swiss International | 240 |
| 18 | Alaska Airlines | 215 |
| 19 | easyJet | 213 |
| 20 | WIF | 212 |
| 21 | EJU | 211 |
| 22 | AEE | 205 |
| 23 | VIV | 204 |
| 24 | Japan Airlines | 203 |
| 25 | EDV | 189 |
| 26 | United Airlines | 184 |
| 27 | GLO | 174 |
| 28 | Air France | 172 |
| 29 | Avianca | 171 |
| 30 | JetBlue | 169 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 25069 |
| 2 | 🇮🇳 IN | 2518 |
| 3 | 🇪🇸 ES | 2389 |
| 4 | 🇦🇺 AU | 2246 |
| 5 | 🇧🇷 BR | 1894 |
| 6 | 🇯🇵 JP | 1766 |
| 7 | 🇮🇹 IT | 1694 |
| 8 | 🇩🇪 DE | 1628 |
| 9 | 🇨🇴 CO | 1598 |
| 10 | 🇨🇦 CA | 1543 |
| 11 | 🇬🇧 GB | 1305 |
| 12 | 🇫🇷 FR | 1179 |
| 13 | 🇲🇽 MX | 1015 |
| 14 | 🇬🇷 GR | 931 |
| 15 | 🇨🇭 CH | 892 |
| 16 | 🇲🇾 MY | 821 |
| 17 | 🇳🇴 NO | 713 |
| 18 | 🇳🇿 NZ | 688 |
| 19 | 🇿🇦 ZA | 660 |
| 20 | 🇵🇭 PH | 602 |
| 21 | 🇹🇭 TH | 591 |
| 22 | 🇹🇷 TR | 588 |
| 23 | 🇬🇹 GT | 587 |
| 24 | 🇰🇷 KR | 553 |
| 25 | 🇵🇱 PL | 489 |
| 26 | 🇲🇦 MA | 414 |
| 27 | 🇧🇸 BS | 331 |
| 28 | 🇲🇪 ME | 318 |
| 29 | 🇮🇩 ID | 309 |
| 30 | 🇳🇱 NL | 308 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 766 |
| 2 | Tokyo International Airport |  | JP | 596 |
| 3 | El Dorado International Airport |  | CO | 568 |
| 4 | Denver International Airport |  | US | 538 |
| 5 | Indira Gandhi International Airport |  | IN | 536 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 457 |
| 7 | La Aurora Airport |  | GT | 425 |
| 8 | Harry Reid International Airport |  | US | 416 |
| 9 | Zurich Airport |  | CH | 395 |
| 10 | Guaymaral Airport |  | CO | 388 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 330 |
| 12 | Chicago O'Hare International Airport |  | US | 330 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 327 |
| 14 | Frankfurt am Main International Airport |  | DE | 321 |
| 15 | Kuala Lumpur International Airport |  | MY | 314 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 312 |
| 17 | Macau International Airport |  | MO | 305 |
| 18 | Charlotte/Douglas International Airport |  | US | 289 |
| 19 | Bengaluru International Airport |  | IN | 288 |
| 20 | Madrid Barajas International Airport |  | ES | 286 |
| 21 | Tenerife Norte Airport |  | ES | 285 |
| 22 | Ninoy Aquino International Airport |  | PH | 278 |
| 23 | Congonhas Airport |  | BR | 278 |
| 24 | Malpensa International Airport |  | IT | 259 |
| 25 | Daniel K Inouye International Airport |  | US | 246 |
| 26 | Salt Lake City International Airport |  | US | 244 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 243 |
| 28 | Reno/Tahoe International Airport |  | US | 242 |
| 29 | Charles de Gaulle International Airport |  | FR | 233 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 230 |
| 31 | Capua Airport |  | IT | 222 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 221 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 220 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 217 |
| 35 | O. R. Tambo International Airport |  | ZA | 216 |
| 36 | Vitoria/Foronda Airport |  | ES | 212 |
| 37 | Miami International Airport |  | US | 210 |
| 38 | Barcelona International Airport |  | ES | 203 |
| 39 | Seattle-Tacoma International Airport |  | US | 202 |
| 40 | Don Mueang International Airport |  | TH | 199 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 151 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 150 | 1h 8m | 706 km | 1,826.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 134 | 14m | 114 km | 262.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 119 | 24m | 225 km | 461.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 105 | 28m | 304 km | 550.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 92 | 1h 28m | 910 km | 1,443.7 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 82 | 19m | 165 km | 233.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 80 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 76 | 9m | - | - |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 73 | 54m | 546 km | 687.3 t |
| 12 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 69 | 27m | 275 km | 327.0 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 68 | 1h 12m | 770 km | 903.3 t |
| 15 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 67 | 21m | 244 km | 282.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 63 | 31m | 369 km | 401.0 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 60 | 45m | 452 km | 467.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 55 | 20m | 250 km | 237.6 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 51 | 20m | 147 km | 129.1 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 51 | 13m | 99 km | 87.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 50 | 1h 42m | 1,423 km | 1,227.1 t |
| 25 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 26 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 48 | 16m | 162 km | 134.6 t |
| 27 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 29 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 44 | 12m | 15 km | 11.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 44 | 1h 21m | 961 km | 729.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N438H |  | Bradley International Airport (KBDL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-13 10:58 UTC | 2026-04-13 11:28 UTC | 29m |
| YOP | YOP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-13 10:39 UTC | 2026-04-13 11:20 UTC | 40m |
| N3300D |  | Crisp County-Cordele Airport (KCKF) | Crisp County-Cordele Airport (KCKF) | 2026-04-13 10:52 UTC | 2026-04-13 11:16 UTC | 23m |
| BCS538 | BCS | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-04-13 00:19 UTC | 2026-04-13 11:07 UTC | 10h 48m |
| APACHE3 | APA | Eindhoven Airport (EHEH) | Volkel Air Base (EHVK) | 2026-04-13 10:42 UTC | 2026-04-13 11:06 UTC | 24m |
| UAE9848 | Emirates | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-04-13 04:37 UTC | 2026-04-13 10:54 UTC | 6h 17m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-04-12 19:30 UTC | 2026-04-13 10:51 UTC | 15h 21m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-04-13 10:39 UTC | 2026-04-13 10:51 UTC | 12m |
| EJU39DC | EJU | Sevilla Airport (LEZL) | Mollis Airport (LSZM) | 2026-04-13 08:10 UTC | 2026-04-13 10:35 UTC | 2h 24m |
| SPLFP | SPL | Piotrkow Trybunalski-Bujny Airport (EPPT) | Łódź Władysław Reymont Airport (EPLL) | 2026-04-13 10:05 UTC | 2026-04-13 10:33 UTC | 27m |
| ANA683 | All Nippon Airways | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 2026-04-13 09:39 UTC | 2026-04-13 10:31 UTC | 52m |
| EZY41PQ | easyJet | London Gatwick Airport (EGKK) | Linate Airport (LIML) | 2026-04-13 08:52 UTC | 2026-04-13 10:30 UTC | 1h 38m |
| WZZ4937 | Wizz Air | Hamburg Airport (EDDH) | Cewice Military Airport (EPCE) | 2026-04-13 09:42 UTC | 2026-04-13 10:29 UTC | 46m |
| EXS7TF | EXS | Manchester Airport (EGCC) | Ampuriabrava Airport (LEAP) | 2026-04-13 08:44 UTC | 2026-04-13 10:28 UTC | 1h 43m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-13 09:58 UTC | 2026-04-13 10:28 UTC | 29m |
| RYR13QJ | Ryanair | Luqa Airport (LMML) | L'Aquila / Preturo Airport (LIAP) | 2026-04-13 09:32 UTC | 2026-04-13 10:27 UTC | 55m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-04-13 10:00 UTC | 2026-04-13 10:25 UTC | 24m |
| FDR288 | FDR | O. R. Tambo International Airport (FAOR) | Walkersons Field (FADU) | 2026-04-13 09:51 UTC | 2026-04-13 10:23 UTC | 31m |
| SWR5MW | Swiss International | Tivat Airport (LYTV) | Zurich Airport (LSZH) | 2026-04-13 08:52 UTC | 2026-04-13 10:21 UTC | 1h 29m |
| ANA387 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-04-13 09:41 UTC | 2026-04-13 10:20 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
