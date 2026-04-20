# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_23:45:54_UTC-green)

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

**Latest saved flight:** 2026-04-20 23:45:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-20 23:45:54 UTC

- **46,177** saved flights
- **19,013** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **46,177** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **556,971.5 tonnes** estimated CO2 emissions
- **32,288,202 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1957 |
| 2 | SkyWest Airlines | 1797 |
| 3 | IndiGo | 1092 |
| 4 | EJA | 799 |
| 5 | American Airlines | 767 |
| 6 | Southwest Airlines | 669 |
| 7 | ENY | 606 |
| 8 | Lufthansa | 477 |
| 9 | Vueling | 465 |
| 10 | AXM | 458 |
| 11 | LATAM Airlines | 458 |
| 12 | All Nippon Airways | 406 |
| 13 | AZU | 395 |
| 14 | Delta Air Lines | 388 |
| 15 | QLK | 368 |
| 16 | WIF | 362 |
| 17 | LXJ | 360 |
| 18 | Swiss International | 355 |
| 19 | Alaska Airlines | 317 |
| 20 | AEE | 313 |
| 21 | EJU | 308 |
| 22 | VIV | 298 |
| 23 | easyJet | 292 |
| 24 | Japan Airlines | 276 |
| 25 | Air France | 263 |
| 26 | Cathay Pacific | 248 |
| 27 | JetBlue | 248 |
| 28 | United Airlines | 245 |
| 29 | AXB | 240 |
| 30 | GLO | 236 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 36801 |
| 2 | 🇮🇳 IN | 3384 |
| 3 | 🇪🇸 ES | 3378 |
| 4 | 🇦🇺 AU | 3157 |
| 5 | 🇧🇷 BR | 2710 |
| 6 | 🇯🇵 JP | 2493 |
| 7 | 🇮🇹 IT | 2490 |
| 8 | 🇩🇪 DE | 2366 |
| 9 | 🇨🇦 CA | 2260 |
| 10 | 🇨🇴 CO | 2128 |
| 11 | 🇬🇧 GB | 1891 |
| 12 | 🇫🇷 FR | 1750 |
| 13 | 🇲🇽 MX | 1441 |
| 14 | 🇬🇷 GR | 1403 |
| 15 | 🇨🇭 CH | 1254 |
| 16 | 🇳🇴 NO | 1152 |
| 17 | 🇲🇾 MY | 1124 |
| 18 | 🇿🇦 ZA | 954 |
| 19 | 🇳🇿 NZ | 905 |
| 20 | 🇵🇭 PH | 819 |
| 21 | 🇹🇭 TH | 817 |
| 22 | 🇹🇷 TR | 813 |
| 23 | 🇰🇷 KR | 751 |
| 24 | 🇬🇹 GT | 737 |
| 25 | 🇵🇱 PL | 732 |
| 26 | 🇲🇦 MA | 569 |
| 27 | 🇲🇪 ME | 485 |
| 28 | 🇳🇱 NL | 468 |
| 29 | 🇲🇴 MO | 435 |
| 30 | 🇧🇸 BS | 420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1093 |
| 2 | Tokyo International Airport |  | JP | 851 |
| 3 | Denver International Airport |  | US | 773 |
| 4 | El Dorado International Airport |  | CO | 742 |
| 5 | Indira Gandhi International Airport |  | IN | 731 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 698 |
| 7 | Harry Reid International Airport |  | US | 600 |
| 8 | Guaymaral Airport |  | CO | 583 |
| 9 | Zurich Airport |  | CH | 549 |
| 10 | La Aurora Airport |  | GT | 545 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 460 |
| 12 | Chicago O'Hare International Airport |  | US | 459 |
| 13 | Frankfurt am Main International Airport |  | DE | 450 |
| 14 | Kuala Lumpur International Airport |  | MY | 449 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 447 |
| 16 | Macau International Airport |  | MO | 435 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 422 |
| 18 | Madrid Barajas International Airport |  | ES | 412 |
| 19 | Bengaluru International Airport |  | IN | 405 |
| 20 | Charlotte/Douglas International Airport |  | US | 400 |
| 21 | Malpensa International Airport |  | IT | 396 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 388 |
| 24 | Ninoy Aquino International Airport |  | PH | 380 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 354 |
| 26 | Daniel K Inouye International Airport |  | US | 345 |
| 27 | Salt Lake City International Airport |  | US | 344 |
| 28 | Charles de Gaulle International Airport |  | FR | 341 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 339 |
| 30 | Capua Airport |  | IT | 334 |
| 31 | Reno/Tahoe International Airport |  | US | 321 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 318 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 318 |
| 34 | Vitoria/Foronda Airport |  | ES | 317 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 311 |
| 36 | O. R. Tambo International Airport |  | ZA | 306 |
| 37 | Barcelona International Airport |  | ES | 303 |
| 38 | Calgary International Airport |  | CA | 280 |
| 39 | Viracopos International Airport |  | BR | 276 |
| 40 | Don Mueang International Airport |  | TH | 275 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 234 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 215 | 1h 7m | 706 km | 2,617.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 173 | 14m | 114 km | 339.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 165 | 24m | 225 km | 640.1 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 137 | 28m | 304 km | 718.2 t |
| 6 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 133 | 21m | 244 km | 560.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 129 | 1h 27m | 910 km | 2,024.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 123 | 31m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 123 | 19m | 165 km | 349.9 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 111 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 108 | 26m | 275 km | 511.8 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 98 | 54m | 546 km | 922.7 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 93 | 44m | 452 km | 724.8 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 92 | 20m | 99 km | 157.6 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 85 | 1h 11m | 770 km | 1,129.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 81 | 31m | 369 km | 515.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 77 | 20m | 250 km | 332.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 74 | 52m | 556 km | 709.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 73 | 20m | 147 km | 184.7 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 71 | 26m | 215 km | 263.0 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 68 | 13m | 99 km | 116.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 24 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 52m | 1,304 km | 1,462.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 64 | 1h 41m | 1,423 km | 1,570.7 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 64 | 1h 0m | 695 km | 767.2 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 63 | 58m | 493 km | 536.0 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 63 | 16m | 162 km | 176.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 62 | 1h 20m | 961 km | 1,027.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-04-20 20:26 UTC | 2026-04-20 23:45 UTC | 3h 19m |
| ASI985 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-04-20 22:56 UTC | 2026-04-20 23:45 UTC | 48m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-04-20 22:57 UTC | 2026-04-20 23:43 UTC | 46m |
| N156SH |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-04-20 23:24 UTC | 2026-04-20 23:39 UTC | 15m |
| N246SF |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-04-20 22:45 UTC | 2026-04-20 23:35 UTC | 50m |
| SNBD1 | SNB | Comox Airport (CYQQ) | Courtenay Airpark (CAH3) | 2026-04-20 23:26 UTC | 2026-04-20 23:31 UTC | 5m |
| CNS119 | CNS | New Bedford Regional Airport (KEWB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-04-20 23:08 UTC | 2026-04-20 23:28 UTC | 19m |
| TRF559 | TRF | North Texas Regional/Perrin Field (KGYI) | 2XS4 (2XS4) | 2026-04-20 23:15 UTC | 2026-04-20 23:27 UTC | 11m |
| N67738 |  | 7TS0 (7TS0) | 7TS0 (7TS0) | 2026-04-20 23:24 UTC | 2026-04-20 23:24 UTC | 0m |
| N115TW |  | Indianapolis Metro Airport (KUMP) | Indianapolis Metro Airport (KUMP) | 2026-04-20 22:43 UTC | 2026-04-20 23:21 UTC | 37m |
| VTE9874 | VTE | Smyrna Airport (KMQY) | Smithville Municipal Airport (K0A3) | 2026-04-20 23:09 UTC | 2026-04-20 23:19 UTC | 10m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-20 20:34 UTC | 2026-04-20 23:19 UTC | 2h 45m |
| PDU55 | PDU | Purdue University Airport (KLAF) | Frankfort Clinton County Regional Airport (KFKR) | 2026-04-20 21:55 UTC | 2026-04-20 23:16 UTC | 1h 21m |
| N17BM |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-20 22:42 UTC | 2026-04-20 23:14 UTC | 32m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-04-20 11:38 UTC | 2026-04-20 23:12 UTC | 11h 34m |
| N24886 |  | Jack W Watson Airport (0IL9) | Wade Airport (56LL) | 2026-04-20 23:07 UTC | 2026-04-20 23:12 UTC | 4m |
| N500FT |  | Richwood Municipal Airport (K3I4) | Richwood Municipal Airport (K3I4) | 2026-04-20 23:00 UTC | 2026-04-20 23:03 UTC | 3m |
| N604D |  | Teterboro Airport (KTEB) | Norfolk International Airport (KORF) | 2026-04-20 22:15 UTC | 2026-04-20 23:03 UTC | 48m |
| MVJ57 | MVJ | Palm Beach International Airport (KPBI) | Harry Reid International Airport (KLAS) | 2026-04-20 18:21 UTC | 2026-04-20 23:03 UTC | 4h 42m |
| N444BU |  | KU77 (KU77) | KU42 (KU42) | 2026-04-20 21:44 UTC | 2026-04-20 23:03 UTC | 1h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
