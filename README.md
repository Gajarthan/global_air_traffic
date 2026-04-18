# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_05:20:39_UTC-green)

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

**Latest saved flight:** 2026-04-18 05:20:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-18 05:20:39 UTC

- **40,577** saved flights
- **17,273** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **40,577** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **488,593.3 tonnes** estimated CO2 emissions
- **28,324,252 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1693 |
| 2 | SkyWest Airlines | 1590 |
| 3 | IndiGo | 989 |
| 4 | EJA | 712 |
| 5 | American Airlines | 680 |
| 6 | Southwest Airlines | 576 |
| 7 | ENY | 523 |
| 8 | AXM | 419 |
| 9 | Vueling | 401 |
| 10 | LATAM Airlines | 398 |
| 11 | Lufthansa | 387 |
| 12 | All Nippon Airways | 362 |
| 13 | AZU | 360 |
| 14 | Delta Air Lines | 347 |
| 15 | QLK | 338 |
| 16 | LXJ | 325 |
| 17 | WIF | 316 |
| 18 | Swiss International | 306 |
| 19 | Alaska Airlines | 272 |
| 20 | AEE | 270 |
| 21 | easyJet | 264 |
| 22 | VIV | 264 |
| 23 | EJU | 262 |
| 24 | Japan Airlines | 246 |
| 25 | Air France | 227 |
| 26 | United Airlines | 222 |
| 27 | JetBlue | 220 |
| 28 | EDV | 216 |
| 29 | GLO | 212 |
| 30 | AXB | 206 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 32253 |
| 2 | 🇮🇳 IN | 3017 |
| 3 | 🇪🇸 ES | 2980 |
| 4 | 🇦🇺 AU | 2870 |
| 5 | 🇧🇷 BR | 2403 |
| 6 | 🇯🇵 JP | 2195 |
| 7 | 🇮🇹 IT | 2099 |
| 8 | 🇩🇪 DE | 2022 |
| 9 | 🇨🇦 CA | 2010 |
| 10 | 🇨🇴 CO | 1952 |
| 11 | 🇬🇧 GB | 1641 |
| 12 | 🇫🇷 FR | 1533 |
| 13 | 🇲🇽 MX | 1291 |
| 14 | 🇬🇷 GR | 1216 |
| 15 | 🇨🇭 CH | 1100 |
| 16 | 🇲🇾 MY | 1019 |
| 17 | 🇳🇴 NO | 1005 |
| 18 | 🇳🇿 NZ | 837 |
| 19 | 🇿🇦 ZA | 827 |
| 20 | 🇵🇭 PH | 736 |
| 21 | 🇹🇭 TH | 720 |
| 22 | 🇹🇷 TR | 707 |
| 23 | 🇬🇹 GT | 690 |
| 24 | 🇰🇷 KR | 657 |
| 25 | 🇵🇱 PL | 622 |
| 26 | 🇲🇦 MA | 498 |
| 27 | 🇳🇱 NL | 405 |
| 28 | 🇲🇪 ME | 402 |
| 29 | 🇧🇸 BS | 387 |
| 30 | 🇲🇴 MO | 370 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 946 |
| 2 | Tokyo International Airport |  | JP | 749 |
| 3 | El Dorado International Airport |  | CO | 688 |
| 4 | Denver International Airport |  | US | 677 |
| 5 | Indira Gandhi International Airport |  | IN | 651 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 605 |
| 7 | Harry Reid International Airport |  | US | 529 |
| 8 | Guaymaral Airport |  | CO | 516 |
| 9 | La Aurora Airport |  | GT | 509 |
| 10 | Zurich Airport |  | CH | 485 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 403 |
| 12 | Kuala Lumpur International Airport |  | MY | 402 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 399 |
| 14 | Chicago O'Hare International Airport |  | US | 392 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 388 |
| 16 | Macau International Airport |  | MO | 370 |
| 17 | Madrid Barajas International Airport |  | ES | 364 |
| 18 | Charlotte/Douglas International Airport |  | US | 358 |
| 19 | Tenerife Norte Airport |  | ES | 358 |
| 20 | Bengaluru International Airport |  | IN | 353 |
| 21 | Congonhas Airport |  | BR | 353 |
| 22 | Frankfurt am Main International Airport |  | DE | 352 |
| 23 | Ninoy Aquino International Airport |  | PH | 342 |
| 24 | Malpensa International Airport |  | IT | 327 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 322 |
| 26 | Salt Lake City International Airport |  | US | 313 |
| 27 | Daniel K Inouye International Airport |  | US | 303 |
| 28 | Charles de Gaulle International Airport |  | FR | 295 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 289 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 283 |
| 31 | Reno/Tahoe International Airport |  | US | 279 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 279 |
| 33 | Vitoria/Foronda Airport |  | ES | 276 |
| 34 | Capua Airport |  | IT | 274 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 266 |
| 36 | O. R. Tambo International Airport |  | ZA | 265 |
| 37 | Barcelona International Airport |  | ES | 257 |
| 38 | Calgary International Airport |  | CA | 247 |
| 39 | Viracopos International Airport |  | BR | 247 |
| 40 | Miami International Airport |  | US | 241 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 206 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 187 | 1h 8m | 706 km | 2,276.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 160 | 14m | 114 km | 313.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 145 | 24m | 225 km | 562.5 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 118 | 28m | 304 km | 618.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 114 | 1h 27m | 910 km | 1,788.9 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 108 | 19m | 165 km | 307.2 t |
| 8 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 107 | 21m | 244 km | 450.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 104 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 103 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 93 | 26m | 275 km | 440.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 87 | 54m | 546 km | 819.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 86 | 21m | 99 km | 147.3 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 82 | 44m | 452 km | 639.1 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 81 | 1h 11m | 770 km | 1,076.0 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 75 | 27m | 152 km | 196.0 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 74 | 31m | 369 km | 471.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 66 | 52m | 556 km | 632.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 63 | 20m | 147 km | 159.4 t |
| 21 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 62 | 1h 41m | 1,423 km | 1,521.6 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 62 | 20m | 250 km | 267.8 t |
| 23 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 61 | 26m | 215 km | 225.9 t |
| 24 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 61 | 16m | 162 km | 171.0 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 60 | 13m | 99 km | 102.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 59 | 1h 53m | 1,304 km | 1,327.3 t |
| 27 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 58 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 57 | 1h 21m | 961 km | 944.8 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 57 | 59m | 695 km | 683.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEE105 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-18 04:43 UTC | 2026-04-18 05:20 UTC | 36m |
| HGB703 | HGB | Taiwan Taoyuan International Airport (RCTP) | Chek Lap Kok International Airport (VHHH) | 2026-04-18 03:53 UTC | 2026-04-18 05:18 UTC | 1h 25m |
| NTR232 | NTR | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-04-18 04:25 UTC | 2026-04-18 05:05 UTC | 39m |
| ASI998 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-18 04:10 UTC | 2026-04-18 05:04 UTC | 53m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-18 04:36 UTC | 2026-04-18 05:03 UTC | 26m |
| NYV | NYV | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-04-18 04:26 UTC | 2026-04-18 04:59 UTC | 32m |
| OAL040 | OAL | Eleftherios Venizelos International Airport (LGAV) | Ikaria Airport (LGIK) | 2026-04-18 04:29 UTC | 2026-04-18 04:57 UTC | 28m |
| SWA4397 | Southwest Airlines | John Wayne/Orange County Airport (KSNA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-04-18 04:01 UTC | 2026-04-18 04:55 UTC | 53m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-04-18 04:17 UTC | 2026-04-18 04:38 UTC | 20m |
| AM395 |  | Melbourne Essendon Airport (YMEN) | Strathbogie Airport (YSBG) | 2026-04-18 04:15 UTC | 2026-04-18 04:35 UTC | 20m |
| MVJ44 | MVJ | Washington Dulles International Airport (KIAD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-17 22:45 UTC | 2026-04-18 04:33 UTC | 5h 47m |
| KYW | KYW | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-18 04:01 UTC | 2026-04-18 04:32 UTC | 31m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-18 03:58 UTC | 2026-04-18 04:31 UTC | 32m |
| NKS361 | NKS | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 2026-04-18 03:36 UTC | 2026-04-18 04:28 UTC | 52m |
| ANZ623 | ANZ | Auckland International Airport (NZAA) | Queenstown International Airport (NZQN) | 2026-04-18 03:01 UTC | 2026-04-18 04:27 UTC | 1h 25m |
| IGO531P | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-18 03:41 UTC | 2026-04-18 04:25 UTC | 43m |
| UBG121 | UBG | VGZR (VGZR) | Jessore Airport (VGJR) | 2026-04-18 03:52 UTC | 2026-04-18 04:24 UTC | 32m |
| N553CP |  | Bolton Field (KTZR) | Bolton Field (KTZR) | 2026-04-18 03:53 UTC | 2026-04-18 04:23 UTC | 30m |
| FD613 |  | Perth Jandakot Airport (YPJT) | Hillman Farm Airport (YHLM) | 2026-04-18 03:56 UTC | 2026-04-18 04:22 UTC | 25m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-04-18 03:23 UTC | 2026-04-18 04:20 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
