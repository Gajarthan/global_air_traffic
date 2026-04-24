# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_23:43:51_UTC-green)

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

**Latest saved flight:** 2026-04-23 23:43:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 23:43:51 UTC

- **50,529** saved flights
- **20,333** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,529** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **603,402.4 tonnes** estimated CO2 emissions
- **34,979,851 km** total distance flown
- **832 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2129 |
| 2 | SkyWest Airlines | 1939 |
| 3 | IndiGo | 1169 |
| 4 | EJA | 875 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 720 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 580 |
| 9 | Vueling | 502 |
| 10 | AXM | 496 |
| 11 | LATAM Airlines | 492 |
| 12 | All Nippon Airways | 455 |
| 13 | AZU | 430 |
| 14 | Delta Air Lines | 418 |
| 15 | WIF | 417 |
| 16 | QLK | 406 |
| 17 | LXJ | 380 |
| 18 | Swiss International | 376 |
| 19 | AEE | 343 |
| 20 | Alaska Airlines | 334 |
| 21 | EJU | 325 |
| 22 | VIV | 321 |
| 23 | easyJet | 317 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 284 |
| 26 | AXB | 268 |
| 27 | Cathay Pacific | 266 |
| 28 | JetBlue | 263 |
| 29 | United Airlines | 263 |
| 30 | AIQ | 256 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40291 |
| 2 | 🇮🇳 IN | 3668 |
| 3 | 🇪🇸 ES | 3638 |
| 4 | 🇦🇺 AU | 3494 |
| 5 | 🇧🇷 BR | 2932 |
| 6 | 🇯🇵 JP | 2744 |
| 7 | 🇮🇹 IT | 2699 |
| 8 | 🇩🇪 DE | 2681 |
| 9 | 🇨🇦 CA | 2528 |
| 10 | 🇨🇴 CO | 2342 |
| 11 | 🇬🇧 GB | 2069 |
| 12 | 🇫🇷 FR | 1927 |
| 13 | 🇲🇽 MX | 1565 |
| 14 | 🇬🇷 GR | 1530 |
| 15 | 🇨🇭 CH | 1384 |
| 16 | 🇳🇴 NO | 1350 |
| 17 | 🇲🇾 MY | 1209 |
| 18 | 🇿🇦 ZA | 1038 |
| 19 | 🇳🇿 NZ | 964 |
| 20 | 🇹🇭 TH | 914 |
| 21 | 🇹🇷 TR | 890 |
| 22 | 🇵🇭 PH | 872 |
| 23 | 🇰🇷 KR | 835 |
| 24 | 🇵🇱 PL | 811 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 622 |
| 27 | 🇲🇪 ME | 537 |
| 28 | 🇳🇱 NL | 508 |
| 29 | 🇲🇴 MO | 471 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 931 |
| 3 | Denver International Airport |  | US | 843 |
| 4 | El Dorado International Airport |  | CO | 800 |
| 5 | Indira Gandhi International Airport |  | IN | 785 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 756 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 664 |
| 9 | Zurich Airport |  | CH | 587 |
| 10 | La Aurora Airport |  | GT | 574 |
| 11 | Frankfurt am Main International Airport |  | DE | 560 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 494 |
| 14 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 15 | Kuala Lumpur International Airport |  | MY | 482 |
| 16 | Macau International Airport |  | MO | 471 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 459 |
| 18 | Madrid Barajas International Airport |  | ES | 458 |
| 19 | Bengaluru International Airport |  | IN | 438 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 420 |
| 22 | Malpensa International Airport |  | IT | 413 |
| 23 | Tenerife Norte Airport |  | ES | 408 |
| 24 | Ninoy Aquino International Airport |  | PH | 402 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Salt Lake City International Airport |  | US | 376 |
| 27 | Charles de Gaulle International Airport |  | FR | 375 |
| 28 | Daniel K Inouye International Airport |  | US | 372 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 33 | Vitoria/Foronda Airport |  | ES | 340 |
| 34 | Reno/Tahoe International Airport |  | US | 339 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 337 |
| 36 | Barcelona International Airport |  | ES | 334 |
| 37 | O. R. Tambo International Airport |  | ZA | 332 |
| 38 | Don Mueang International Airport |  | TH | 311 |
| 39 | Calgary International Airport |  | CA | 307 |
| 40 | Viracopos International Airport |  | BR | 299 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 235 | 1h 7m | 706 km | 2,861.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 193 | 14m | 114 km | 378.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 152 | 21m | 244 km | 640.0 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 150 | 28m | 304 km | 786.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 103 | 44m | 452 km | 802.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 88 | 1h 11m | 770 km | 1,169.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 86 | 20m | 250 km | 371.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL2433 | United Airlines | Philadelphia International Airport (KPHL) | Denver International Airport (KDEN) | 2026-04-23 20:01 UTC | 2026-04-23 23:43 UTC | 3h 42m |
| N9815L |  | Kenosha Regional Airport (KENW) | Batten International Airport (KRAC) | 2026-04-23 23:08 UTC | 2026-04-23 23:38 UTC | 30m |
| CFDYL | CFD | Victoria International Airport (CYYJ) | Vancouver International Airport (CYVR) | 2026-04-23 23:03 UTC | 2026-04-23 23:32 UTC | 29m |
| N750GJ |  | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-23 22:39 UTC | 2026-04-23 23:30 UTC | 51m |
| ERU6 | ERU | AZ86 (AZ86) | 42AZ (42AZ) | 2026-04-23 23:14 UTC | 2026-04-23 23:28 UTC | 13m |
| N232TB |  | Arlington Municipal Airport (KAWO) | 89WA (89WA) | 2026-04-23 23:18 UTC | 2026-04-23 23:21 UTC | 3m |
| IUJ | IUJ | Warrnambool Airport (YWBL) | Peterborough Airport (YPBH) | 2026-04-23 22:51 UTC | 2026-04-23 23:20 UTC | 28m |
| EJA548 | EJA | Henderson Executive Airport (KHND) | Harris River Ranch Airport (9CA7) | 2026-04-23 22:36 UTC | 2026-04-23 23:19 UTC | 43m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Wetaskiwin Regional Airport (CEX3) | 2026-04-23 22:47 UTC | 2026-04-23 23:18 UTC | 30m |
| JUTE25 | JUT | Wichita Valley Airport (KF14) | Quanah Municipal Airport (KF01) | 2026-04-23 23:05 UTC | 2026-04-23 23:15 UTC | 10m |
| N814WS |  | Prescott Regional/Ernest A Love Field (KPRC) | Montezuma Airport (19AZ) | 2026-04-23 22:56 UTC | 2026-04-23 23:11 UTC | 15m |
| PTLUE | PTL | San Antonio International Airport (KSAT) | Calgary International Airport (CYYC) | 2026-04-23 19:17 UTC | 2026-04-23 23:11 UTC | 3h 54m |
| KATT21 | KAT | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Trent Lott International Airport (KPQL) | 2026-04-23 22:50 UTC | 2026-04-23 23:11 UTC | 20m |
| CNS46 | CNS | Pope Valley Airport (05CL) | Oakland San Francisco Bay Airport (KOAK) | 2026-04-23 22:43 UTC | 2026-04-23 23:09 UTC | 26m |
| EJA537 | EJA | Fort Worth Meacham International Airport (KFTW) | 5TA4 (5TA4) | 2026-04-23 22:29 UTC | 2026-04-23 23:08 UTC | 39m |
| KNIFE30 | KNI | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-04-23 21:42 UTC | 2026-04-23 23:07 UTC | 1h 24m |
| N114EM |  | Boca Raton Airport (KBCT) | Matzie Airport (30MO) | 2026-04-23 20:49 UTC | 2026-04-23 23:06 UTC | 2h 16m |
| N229WC |  | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-04-23 21:50 UTC | 2026-04-23 23:05 UTC | 1h 15m |
| ENY3598 | ENY | Chicago O'Hare International Airport (KORD) | 61II (61II) | 2026-04-23 22:43 UTC | 2026-04-23 23:05 UTC | 21m |
| MXY808 | MXY | Orlando International Airport (KMCO) | Lancaster Airport (KLNS) | 2026-04-23 20:58 UTC | 2026-04-23 23:05 UTC | 2h 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
