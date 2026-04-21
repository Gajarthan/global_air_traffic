# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_20:19:13_UTC-green)

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

**Latest saved flight:** 2026-04-21 20:19:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-21 20:19:13 UTC

- **47,214** saved flights
- **19,298** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **47,214** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **567,243.3 tonnes** estimated CO2 emissions
- **32,883,670 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2009 |
| 2 | SkyWest Airlines | 1824 |
| 3 | IndiGo | 1107 |
| 4 | EJA | 806 |
| 5 | American Airlines | 782 |
| 6 | Southwest Airlines | 676 |
| 7 | ENY | 613 |
| 8 | Lufthansa | 509 |
| 9 | Vueling | 475 |
| 10 | AXM | 470 |
| 11 | LATAM Airlines | 465 |
| 12 | All Nippon Airways | 422 |
| 13 | AZU | 403 |
| 14 | Delta Air Lines | 393 |
| 15 | WIF | 380 |
| 16 | QLK | 376 |
| 17 | LXJ | 365 |
| 18 | Swiss International | 363 |
| 19 | AEE | 321 |
| 20 | Alaska Airlines | 321 |
| 21 | EJU | 315 |
| 22 | easyJet | 303 |
| 23 | VIV | 300 |
| 24 | Japan Airlines | 283 |
| 25 | Air France | 268 |
| 26 | Cathay Pacific | 251 |
| 27 | JetBlue | 251 |
| 28 | AXB | 248 |
| 29 | United Airlines | 248 |
| 30 | GLO | 240 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 37523 |
| 2 | 🇮🇳 IN | 3442 |
| 3 | 🇪🇸 ES | 3435 |
| 4 | 🇦🇺 AU | 3235 |
| 5 | 🇧🇷 BR | 2775 |
| 6 | 🇮🇹 IT | 2574 |
| 7 | 🇯🇵 JP | 2571 |
| 8 | 🇩🇪 DE | 2448 |
| 9 | 🇨🇦 CA | 2314 |
| 10 | 🇨🇴 CO | 2196 |
| 11 | 🇬🇧 GB | 1930 |
| 12 | 🇫🇷 FR | 1803 |
| 13 | 🇲🇽 MX | 1461 |
| 14 | 🇬🇷 GR | 1442 |
| 15 | 🇨🇭 CH | 1298 |
| 16 | 🇳🇴 NO | 1211 |
| 17 | 🇲🇾 MY | 1147 |
| 18 | 🇿🇦 ZA | 974 |
| 19 | 🇳🇿 NZ | 913 |
| 20 | 🇹🇭 TH | 846 |
| 21 | 🇵🇭 PH | 833 |
| 22 | 🇹🇷 TR | 831 |
| 23 | 🇰🇷 KR | 772 |
| 24 | 🇵🇱 PL | 743 |
| 25 | 🇬🇹 GT | 743 |
| 26 | 🇲🇦 MA | 585 |
| 27 | 🇲🇪 ME | 505 |
| 28 | 🇳🇱 NL | 482 |
| 29 | 🇲🇴 MO | 444 |
| 30 | 🇧🇸 BS | 424 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1112 |
| 2 | Tokyo International Airport |  | JP | 874 |
| 3 | Denver International Airport |  | US | 784 |
| 4 | El Dorado International Airport |  | CO | 764 |
| 5 | Indira Gandhi International Airport |  | IN | 737 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 713 |
| 7 | Guaymaral Airport |  | CO | 613 |
| 8 | Harry Reid International Airport |  | US | 607 |
| 9 | Zurich Airport |  | CH | 562 |
| 10 | La Aurora Airport |  | GT | 550 |
| 11 | Frankfurt am Main International Airport |  | DE | 481 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 470 |
| 13 | Chicago O'Hare International Airport |  | US | 462 |
| 14 | Kuala Lumpur International Airport |  | MY | 460 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 453 |
| 16 | Macau International Airport |  | MO | 444 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 425 |
| 18 | Madrid Barajas International Airport |  | ES | 420 |
| 19 | Bengaluru International Airport |  | IN | 417 |
| 20 | Charlotte/Douglas International Airport |  | US | 405 |
| 21 | Malpensa International Airport |  | IT | 401 |
| 22 | Tenerife Norte Airport |  | ES | 395 |
| 23 | Congonhas Airport |  | BR | 395 |
| 24 | Ninoy Aquino International Airport |  | PH | 385 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 357 |
| 26 | Salt Lake City International Airport |  | US | 355 |
| 27 | Daniel K Inouye International Airport |  | US | 353 |
| 28 | Charles de Gaulle International Airport |  | FR | 351 |
| 29 | Capua Airport |  | IT | 351 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 344 |
| 31 | Reno/Tahoe International Airport |  | US | 326 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 326 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 322 |
| 34 | Vitoria/Foronda Airport |  | ES | 319 |
| 35 | O. R. Tambo International Airport |  | ZA | 313 |
| 36 | Barcelona International Airport |  | ES | 313 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 312 |
| 38 | Don Mueang International Airport |  | TH | 285 |
| 39 | Calgary International Airport |  | CA | 282 |
| 40 | Viracopos International Airport |  | BR | 281 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 246 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 221 | 1h 7m | 706 km | 2,690.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 180 | 14m | 114 km | 353.0 t |
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
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 75 | 52m | 556 km | 718.9 t |
| 21 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 73 | 26m | 215 km | 270.4 t |
| 22 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 68 | 1h 42m | 1,156 km | 1,356.6 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 65 | 1h 41m | 1,423 km | 1,595.2 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 65 | 57m | 493 km | 553.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 65 | 13m | - | - |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 65 | 1h 0m | 695 km | 779.2 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 64 | 16m | 162 km | 179.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 62 | 12m | 15 km | 16.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BALL19 | BAL | 75OK (75OK) | Hsh Airstrip (5OK9) | 2026-04-21 19:35 UTC | 2026-04-21 20:19 UTC | 44m |
| AXLE11 | AXL | 75OK (75OK) | Lariat Ranch Airport (OK42) | 2026-04-21 19:50 UTC | 2026-04-21 20:16 UTC | 26m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-21 09:01 UTC | 2026-04-21 20:12 UTC | 11h 10m |
| JOLLY92 | JOL | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-04-21 19:28 UTC | 2026-04-21 20:11 UTC | 43m |
| N54739 |  | Robco Airport (MN12) | Up Yonder Airport (98MN) | 2026-04-21 19:45 UTC | 2026-04-21 20:09 UTC | 24m |
| QTR8410 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-21 13:10 UTC | 2026-04-21 20:06 UTC | 6h 56m |
| N999HE |  | Mc Clellan-Palomar Airport (KCRQ) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-21 19:47 UTC | 2026-04-21 20:03 UTC | 16m |
| N812KC |  | Midland International Air And Space Port Airport (KMAF) | Mc Neill Ranch Airport (6TE7) | 2026-04-21 19:38 UTC | 2026-04-21 20:03 UTC | 25m |
| N4496F |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-04-21 19:51 UTC | 2026-04-21 20:02 UTC | 10m |
| N52GM |  | Pensacola International Airport (KPNS) | Horak Airport (7AL9) | 2026-04-21 19:46 UTC | 2026-04-21 20:01 UTC | 14m |
| N39688 |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-04-21 19:32 UTC | 2026-04-21 20:01 UTC | 28m |
| CGKCN | CGK | Calgary / Springbank Airport (CYBW) | Claresholm Industrial Airport (CEJ4) | 2026-04-21 19:02 UTC | 2026-04-21 20:00 UTC | 58m |
| N11PP |  | Ronald Reagan Washington Ntl Airport (KDCA) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-04-21 19:38 UTC | 2026-04-21 19:58 UTC | 20m |
| LSJ641 | LSJ | Québec City Jean Lesage International Airport (CYQB) | Ile-aux-Grues Airport (CSH2) | 2026-04-21 19:37 UTC | 2026-04-21 19:52 UTC | 15m |
| N6338D |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-04-21 19:17 UTC | 2026-04-21 19:48 UTC | 30m |
| N514VK |  | Wings Field (KLOM) | Lancaster Airport (KLNS) | 2026-04-21 19:31 UTC | 2026-04-21 19:47 UTC | 16m |
| N530JT |  | Hub Field (8TX0) | Throckmorton Municipal Airport (K72F) | 2026-04-21 18:58 UTC | 2026-04-21 19:46 UTC | 47m |
| CNUK91 | CNU | CFB Trenton (CYTR) | CFB Trenton (CYTR) | 2026-04-21 19:36 UTC | 2026-04-21 19:45 UTC | 9m |
| N93EC |  | Louis Armstrong New Orleans International Airport (KMSY) | Clay Airport (MS50) | 2026-04-21 19:29 UTC | 2026-04-21 19:45 UTC | 16m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-04-21 05:55 UTC | 2026-04-21 19:45 UTC | 13h 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
