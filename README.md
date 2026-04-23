# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_13:34:18_UTC-green)

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

**Latest saved flight:** 2026-04-23 13:34:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 13:34:18 UTC

- **49,725** saved flights
- **20,047** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,725** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **593,982.8 tonnes** estimated CO2 emissions
- **34,433,786 km** total distance flown
- **832 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2110 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1165 |
| 4 | EJA | 855 |
| 5 | American Airlines | 811 |
| 6 | Southwest Airlines | 703 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 579 |
| 9 | AXM | 495 |
| 10 | Vueling | 494 |
| 11 | LATAM Airlines | 486 |
| 12 | All Nippon Airways | 455 |
| 13 | AZU | 423 |
| 14 | WIF | 414 |
| 15 | Delta Air Lines | 406 |
| 16 | QLK | 404 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 376 |
| 19 | AEE | 338 |
| 20 | Alaska Airlines | 330 |
| 21 | EJU | 320 |
| 22 | easyJet | 315 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 298 |
| 25 | Air France | 281 |
| 26 | AXB | 268 |
| 27 | Cathay Pacific | 259 |
| 28 | JetBlue | 259 |
| 29 | United Airlines | 258 |
| 30 | AIQ | 256 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39333 |
| 2 | 🇮🇳 IN | 3658 |
| 3 | 🇪🇸 ES | 3603 |
| 4 | 🇦🇺 AU | 3471 |
| 5 | 🇧🇷 BR | 2890 |
| 6 | 🇯🇵 JP | 2739 |
| 7 | 🇮🇹 IT | 2683 |
| 8 | 🇩🇪 DE | 2647 |
| 9 | 🇨🇦 CA | 2462 |
| 10 | 🇨🇴 CO | 2308 |
| 11 | 🇬🇧 GB | 2055 |
| 12 | 🇫🇷 FR | 1907 |
| 13 | 🇲🇽 MX | 1529 |
| 14 | 🇬🇷 GR | 1518 |
| 15 | 🇨🇭 CH | 1381 |
| 16 | 🇳🇴 NO | 1328 |
| 17 | 🇲🇾 MY | 1207 |
| 18 | 🇿🇦 ZA | 1026 |
| 19 | 🇳🇿 NZ | 956 |
| 20 | 🇹🇭 TH | 914 |
| 21 | 🇹🇷 TR | 879 |
| 22 | 🇵🇭 PH | 871 |
| 23 | 🇰🇷 KR | 827 |
| 24 | 🇵🇱 PL | 800 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 610 |
| 27 | 🇲🇪 ME | 534 |
| 28 | 🇳🇱 NL | 504 |
| 29 | 🇲🇴 MO | 458 |
| 30 | 🇧🇸 BS | 438 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 930 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 795 |
| 5 | Indira Gandhi International Airport |  | IN | 780 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 751 |
| 7 | Guaymaral Airport |  | CO | 667 |
| 8 | Harry Reid International Airport |  | US | 643 |
| 9 | Zurich Airport |  | CH | 586 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 558 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 488 |
| 13 | Chicago O'Hare International Airport |  | US | 488 |
| 14 | Kuala Lumpur International Airport |  | MY | 482 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 468 |
| 16 | Macau International Airport |  | MO | 458 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 18 | Madrid Barajas International Airport |  | ES | 454 |
| 19 | Bengaluru International Airport |  | IN | 437 |
| 20 | Charlotte/Douglas International Airport |  | US | 419 |
| 21 | Congonhas Airport |  | BR | 415 |
| 22 | Malpensa International Airport |  | IT | 408 |
| 23 | Tenerife Norte Airport |  | ES | 406 |
| 24 | Ninoy Aquino International Airport |  | PH | 402 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 377 |
| 26 | Salt Lake City International Airport |  | US | 369 |
| 27 | Charles de Gaulle International Airport |  | FR | 369 |
| 28 | Daniel K Inouye International Airport |  | US | 368 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 366 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | Vitoria/Foronda Airport |  | ES | 339 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 338 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 335 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 333 |
| 35 | Reno/Tahoe International Airport |  | US | 329 |
| 36 | O. R. Tambo International Airport |  | ZA | 328 |
| 37 | Barcelona International Airport |  | ES | 327 |
| 38 | Don Mueang International Airport |  | TH | 311 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 295 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 269 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 235 | 1h 7m | 706 km | 2,861.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 192 | 14m | 114 km | 376.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 171 | 24m | 225 km | 663.4 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 149 | 21m | 244 km | 627.4 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 149 | 28m | 304 km | 781.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 143 | 1h 27m | 910 km | 2,244.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 134 | 19m | 165 km | 381.2 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 117 | 26m | 275 km | 554.4 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 103 | 44m | 452 km | 802.7 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 86 | 31m | 369 km | 547.4 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 85 | 20m | 250 km | 367.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 81 | 26m | 215 km | 300.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 69 | 58m | 493 km | 587.0 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 66 | 11m | 15 km | 17.4 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SYS137 | SYS | RAF Shawbury (EGOS) | RAF Shawbury (EGOS) | 2026-04-23 12:22 UTC | 2026-04-23 13:34 UTC | 1h 12m |
| RGAIE | RGA | Megeve Airport (LFHM) | Muenster Aero Airport (LSPU) | 2026-04-23 13:16 UTC | 2026-04-23 13:34 UTC | 17m |
| N459CP |  | Salinas Municipal Airport (KSNS) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-04-23 13:10 UTC | 2026-04-23 13:30 UTC | 19m |
| RSQ118 | RSQ | Belmullet Aerodrome (EIBT) | Ireland West Knock Airport (EIKN) | 2026-04-23 13:15 UTC | 2026-04-23 13:27 UTC | 11m |
| N412EX |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-04-23 13:06 UTC | 2026-04-23 13:26 UTC | 19m |
| HBKSM | HBK | St Gallen Altenrhein Airport (LSZR) | Bad Ragaz Airport (LSZE) | 2026-04-23 12:58 UTC | 2026-04-23 13:25 UTC | 26m |
| N50PE |  | Harrisburg International Airport (KMDT) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-04-23 12:30 UTC | 2026-04-23 13:22 UTC | 51m |
| N2772P |  | Clermont County Airport (KI69) | Gene Snyder Airport (KK62) | 2026-04-23 13:07 UTC | 2026-04-23 13:18 UTC | 11m |
| N321KS |  | 09FL (09FL) | FL00 (FL00) | 2026-04-23 12:56 UTC | 2026-04-23 13:14 UTC | 18m |
| ERU902 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-04-23 12:51 UTC | 2026-04-23 13:13 UTC | 21m |
| HBLMA | HBL | Grenchen Airport (LSZG) | Grenchen Airport (LSZG) | 2026-04-23 12:36 UTC | 2026-04-23 13:12 UTC | 36m |
| JEDI18 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bay Minette Municipal Airport (K1R8) | 2026-04-23 12:50 UTC | 2026-04-23 13:10 UTC | 19m |
| ELY396 | ELY | Madrid Barajas International Airport (LEMD) | Herzliya Airport (LLHZ) | 2026-04-23 09:13 UTC | 2026-04-23 13:10 UTC | 3h 56m |
| RGAIE | RGA | Grenchen Airport (LSZG) | St Stephan Airport (LSTS) | 2026-04-23 12:16 UTC | 2026-04-23 13:06 UTC | 50m |
| N125LT |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-04-23 12:53 UTC | 2026-04-23 13:04 UTC | 10m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-04-23 12:52 UTC | 2026-04-23 13:02 UTC | 10m |
| ERU908 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-23 12:20 UTC | 2026-04-23 13:02 UTC | 41m |
| ELY2372 | ELY | Berlin Brandenburg Airport (EDDB) | LLSD (LLSD) | 2026-04-23 09:21 UTC | 2026-04-23 12:57 UTC | 3h 36m |
| MOLOCH71 | MOL | Cognac-Chateaubernard (BA 709) Air Base (LFBG) | St Jean D'angely Airport (LFIY) | 2026-04-23 12:45 UTC | 2026-04-23 12:56 UTC | 11m |
| WIF8GH | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-23 12:28 UTC | 2026-04-23 12:55 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
