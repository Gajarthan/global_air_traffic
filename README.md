# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_21:56:47_UTC-green)

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

**Latest saved flight:** 2026-04-21 21:56:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 21:56:47 UTC

- **47,409** saved flights
- **19,372** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,409** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **570,409.0 tonnes** estimated CO2 emissions
- **33,067,189 km** total distance flown
- **838 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2019 |
| 2 | SkyWest Airlines | 1840 |
| 3 | IndiGo | 1108 |
| 4 | EJA | 817 |
| 5 | American Airlines | 788 |
| 6 | Southwest Airlines | 681 |
| 7 | ENY | 617 |
| 8 | Lufthansa | 509 |
| 9 | Vueling | 476 |
| 10 | AXM | 470 |
| 11 | LATAM Airlines | 467 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 405 |
| 14 | Delta Air Lines | 395 |
| 15 | WIF | 380 |
| 16 | QLK | 377 |
| 17 | LXJ | 370 |
| 18 | Swiss International | 364 |
| 19 | Alaska Airlines | 322 |
| 20 | AEE | 321 |
| 21 | EJU | 315 |
| 22 | easyJet | 303 |
| 23 | VIV | 302 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 256 |
| 27 | JetBlue | 252 |
| 28 | United Airlines | 250 |
| 29 | AXB | 248 |
| 30 | GLO | 241 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37767 |
| 2 | 🇮🇳 IN | 3445 |
| 3 | 🇪🇸 ES | 3440 |
| 4 | 🇦🇺 AU | 3240 |
| 5 | 🇧🇷 BR | 2787 |
| 6 | 🇮🇹 IT | 2586 |
| 7 | 🇯🇵 JP | 2571 |
| 8 | 🇩🇪 DE | 2451 |
| 9 | 🇨🇦 CA | 2335 |
| 10 | 🇨🇴 CO | 2204 |
| 11 | 🇬🇧 GB | 1938 |
| 12 | 🇫🇷 FR | 1805 |
| 13 | 🇲🇽 MX | 1473 |
| 14 | 🇬🇷 GR | 1444 |
| 15 | 🇨🇭 CH | 1299 |
| 16 | 🇳🇴 NO | 1211 |
| 17 | 🇲🇾 MY | 1147 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 917 |
| 20 | 🇹🇭 TH | 847 |
| 21 | 🇵🇭 PH | 833 |
| 22 | 🇹🇷 TR | 832 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 745 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 586 |
| 27 | 🇲🇪 ME | 506 |
| 28 | 🇳🇱 NL | 484 |
| 29 | 🇲🇴 MO | 449 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1121 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 790 |
| 4 | El Dorado International Airport |  | CO | 767 |
| 5 | Indira Gandhi International Airport |  | IN | 737 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 715 |
| 7 | Guaymaral Airport |  | CO | 615 |
| 8 | Harry Reid International Airport |  | US | 614 |
| 9 | Zurich Airport |  | CH | 563 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 482 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 475 |
| 13 | Chicago O'Hare International Airport |  | US | 463 |
| 14 | Kuala Lumpur International Airport |  | MY | 460 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 454 |
| 16 | Macau International Airport |  | MO | 449 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 426 |
| 18 | Madrid Barajas International Airport |  | ES | 421 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 407 |
| 21 | Malpensa International Airport |  | IT | 401 |
| 22 | Congonhas Airport |  | BR | 398 |
| 23 | Tenerife Norte Airport |  | ES | 395 |
| 24 | Ninoy Aquino International Airport |  | PH | 385 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 359 |
| 26 | Salt Lake City International Airport |  | US | 357 |
| 27 | Daniel K Inouye International Airport |  | US | 354 |
| 28 | Charles de Gaulle International Airport |  | FR | 352 |
| 29 | Capua Airport |  | IT | 352 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 345 |
| 31 | Reno/Tahoe International Airport |  | US | 329 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 327 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 322 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | Barcelona International Airport |  | ES | 314 |
| 36 | O. R. Tambo International Airport |  | ZA | 313 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 284 |
| 40 | Viracopos International Airport |  | BR | 282 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 246 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 181 | 14m | 114 km | 355.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 166 | 24m | 225 km | 644.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 141 | 28m | 304 km | 739.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 139 | 21m | 244 km | 585.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 135 | 1h 27m | 910 km | 2,118.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 125 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 125 | 19m | 165 km | 355.6 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 113 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 109 | 26m | 275 km | 516.5 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 99 | 54m | 546 km | 932.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 94 | 44m | 452 km | 732.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 93 | 20m | 99 km | 159.3 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 86 | 1h 11m | 770 km | 1,142.4 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 82 | 31m | 369 km | 522.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 78 | 20m | 250 km | 336.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 76 | 20m | 147 km | 192.3 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 0m | 695 km | 791.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 27 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 64 | 16m | 162 km | 179.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 64 | 1h 20m | 961 km | 1,060.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N733QJ |  | VA14 (VA14) | Melville Airstrip (2VA2) | 2026-04-21 21:17 UTC | 2026-04-21 21:56 UTC | 39m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-04-21 10:17 UTC | 2026-04-21 21:55 UTC | 11h 38m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Macau International Airport (VMMC) | 2026-04-21 10:59 UTC | 2026-04-21 21:53 UTC | 10h 53m |
| LXJ449 | LXJ | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-21 21:45 UTC | 2026-04-21 21:45 UTC | 0m |
| N182KQ |  | Anacortes Airport (K74S) | Boeing Field/King County International Airport (KBFI) | 2026-04-21 21:12 UTC | 2026-04-21 21:44 UTC | 32m |
| N93QM |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-04-21 21:36 UTC | 2026-04-21 21:40 UTC | 3m |
| N555BG |  | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-04-21 20:54 UTC | 2026-04-21 21:35 UTC | 41m |
| N4969N |  | Morehaven Airport (MA43) | Tweed/New Haven Airport (KHVN) | 2026-04-21 21:09 UTC | 2026-04-21 21:34 UTC | 24m |
| JDW828 | JDW | RAF Brize Norton (EGVN) | RAF Abingdon (EGUD) | 2026-04-21 20:43 UTC | 2026-04-21 21:33 UTC | 49m |
| XABNT | XAB | Licenciado Benito Juarez International Airport (MMMX) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-04-21 21:13 UTC | 2026-04-21 21:33 UTC | 20m |
| CKS701 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-04-21 09:44 UTC | 2026-04-21 21:33 UTC | 11h 49m |
| RYR82ZE | Ryanair | Dublin Airport (EIDW) | Cardiff International Airport (EGFF) | 2026-04-21 21:00 UTC | 2026-04-21 21:33 UTC | 33m |
| LXJ449 | LXJ | Laurence G Hanscom Field (KBED) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-21 19:54 UTC | 2026-04-21 21:33 UTC | 1h 39m |
| N216AF |  | Montgomery-Gibbs Executive Airport (KMYF) | Ramona Airport (KRNM) | 2026-04-21 20:31 UTC | 2026-04-21 21:31 UTC | 1h 0m |
| N17UC |  | Newport News/Williamsburg International Airport (KPHF) | Virginia Highlands Airport (KVJI) | 2026-04-21 20:49 UTC | 2026-04-21 21:31 UTC | 41m |
| N922EH |  | John Wayne/Orange County Airport (KSNA) | Bermuda Dunes Airport (KUDD) | 2026-04-21 21:12 UTC | 2026-04-21 21:29 UTC | 16m |
| AWH98Z | AWH | Berlin Brandenburg Airport (EDDB) | Frankfurt am Main International Airport (EDDF) | 2026-04-21 20:23 UTC | 2026-04-21 21:22 UTC | 59m |
| N65112 |  | Sky Blue Airfield (6MN0) | Sky Blue Airfield (6MN0) | 2026-04-21 21:16 UTC | 2026-04-21 21:21 UTC | 5m |
| GPD127 | GPD | Luis Munoz Marin International Airport (TJSJ) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-04-21 21:06 UTC | 2026-04-21 21:21 UTC | 15m |
| N8958V |  | Plymouth Municipal Airport (KPYM) | Norwood Memorial Airport (KOWD) | 2026-04-21 21:01 UTC | 2026-04-21 21:21 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
