# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_07:35:03_UTC-green)

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

**Latest saved flight:** 2026-04-23 07:35:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-23 07:35:03 UTC

- **49,281** saved flights
- **19,944** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **49,281** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **588,731.6 tonnes** estimated CO2 emissions
- **34,129,367 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2080 |
| 2 | SkyWest Airlines | 1899 |
| 3 | IndiGo | 1150 |
| 4 | EJA | 852 |
| 5 | American Airlines | 810 |
| 6 | Southwest Airlines | 703 |
| 7 | ENY | 639 |
| 8 | Lufthansa | 557 |
| 9 | Vueling | 489 |
| 10 | AXM | 488 |
| 11 | LATAM Airlines | 481 |
| 12 | All Nippon Airways | 446 |
| 13 | AZU | 421 |
| 14 | WIF | 407 |
| 15 | Delta Air Lines | 405 |
| 16 | QLK | 402 |
| 17 | LXJ | 377 |
| 18 | Swiss International | 371 |
| 19 | AEE | 333 |
| 20 | Alaska Airlines | 330 |
| 21 | EJU | 320 |
| 22 | easyJet | 312 |
| 23 | VIV | 312 |
| 24 | Japan Airlines | 294 |
| 25 | Air France | 277 |
| 26 | AXB | 260 |
| 27 | Cathay Pacific | 259 |
| 28 | United Airlines | 258 |
| 29 | JetBlue | 257 |
| 30 | AIQ | 251 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 39224 |
| 2 | 🇮🇳 IN | 3596 |
| 3 | 🇪🇸 ES | 3553 |
| 4 | 🇦🇺 AU | 3448 |
| 5 | 🇧🇷 BR | 2870 |
| 6 | 🇯🇵 JP | 2699 |
| 7 | 🇮🇹 IT | 2647 |
| 8 | 🇩🇪 DE | 2587 |
| 9 | 🇨🇦 CA | 2452 |
| 10 | 🇨🇴 CO | 2289 |
| 11 | 🇬🇧 GB | 2022 |
| 12 | 🇫🇷 FR | 1868 |
| 13 | 🇲🇽 MX | 1528 |
| 14 | 🇬🇷 GR | 1497 |
| 15 | 🇨🇭 CH | 1336 |
| 16 | 🇳🇴 NO | 1296 |
| 17 | 🇲🇾 MY | 1192 |
| 18 | 🇿🇦 ZA | 1006 |
| 19 | 🇳🇿 NZ | 955 |
| 20 | 🇹🇭 TH | 892 |
| 21 | 🇹🇷 TR | 864 |
| 22 | 🇵🇭 PH | 859 |
| 23 | 🇰🇷 KR | 811 |
| 24 | 🇵🇱 PL | 783 |
| 25 | 🇬🇹 GT | 759 |
| 26 | 🇲🇦 MA | 600 |
| 27 | 🇲🇪 ME | 520 |
| 28 | 🇳🇱 NL | 498 |
| 29 | 🇲🇴 MO | 455 |
| 30 | 🇧🇸 BS | 437 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1156 |
| 2 | Tokyo International Airport |  | JP | 917 |
| 3 | Denver International Airport |  | US | 822 |
| 4 | El Dorado International Airport |  | CO | 787 |
| 5 | Indira Gandhi International Airport |  | IN | 763 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 740 |
| 7 | Guaymaral Airport |  | CO | 661 |
| 8 | Harry Reid International Airport |  | US | 642 |
| 9 | Zurich Airport |  | CH | 578 |
| 10 | La Aurora Airport |  | GT | 565 |
| 11 | Frankfurt am Main International Airport |  | DE | 535 |
| 12 | Chicago O'Hare International Airport |  | US | 488 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 487 |
| 14 | Kuala Lumpur International Airport |  | MY | 476 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 465 |
| 16 | Sydney Kingsford Smith International Airport |  | AU | 457 |
| 17 | Macau International Airport |  | MO | 455 |
| 18 | Madrid Barajas International Airport |  | ES | 443 |
| 19 | Bengaluru International Airport |  | IN | 435 |
| 20 | Charlotte/Douglas International Airport |  | US | 418 |
| 21 | Congonhas Airport |  | BR | 413 |
| 22 | Malpensa International Airport |  | IT | 407 |
| 23 | Tenerife Norte Airport |  | ES | 405 |
| 24 | Ninoy Aquino International Airport |  | PH | 397 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 377 |
| 26 | Salt Lake City International Airport |  | US | 369 |
| 27 | Daniel K Inouye International Airport |  | US | 366 |
| 28 | Charles de Gaulle International Airport |  | FR | 364 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 357 |
| 30 | Capua Airport |  | IT | 353 |
| 31 | Vitoria/Foronda Airport |  | ES | 335 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 335 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 333 |
| 34 | Reno/Tahoe International Airport |  | US | 329 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 326 |
| 36 | O. R. Tambo International Airport |  | ZA | 324 |
| 37 | Barcelona International Airport |  | ES | 322 |
| 38 | Don Mueang International Airport |  | TH | 304 |
| 39 | Calgary International Airport |  | CA | 298 |
| 40 | Viracopos International Airport |  | BR | 293 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 267 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 232 | 1h 7m | 706 km | 2,824.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 189 | 14m | 114 km | 370.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 170 | 24m | 225 km | 659.5 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 148 | 21m | 244 km | 623.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 146 | 28m | 304 km | 765.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 142 | 1h 27m | 910 km | 2,228.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 130 | 19m | 165 km | 369.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 126 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 119 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 115 | 26m | 275 km | 544.9 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 101 | 44m | 452 km | 787.1 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 101 | 54m | 546 km | 950.9 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 87 | 1h 11m | 770 km | 1,155.7 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 85 | 31m | 369 km | 541.0 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 83 | 20m | 250 km | 358.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 79 | 26m | 215 km | 292.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 79 | 20m | 147 km | 199.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 76 | 52m | 556 km | 728.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 69 | 1h 0m | 695 km | 827.1 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 66 | 58m | 493 km | 561.5 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 29 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 64 | 11m | 15 km | 16.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EWQ | EWQ | Toowoomba Airport (YTWB) | Sunshine Coast Airport (YBMC) | 2026-04-23 07:11 UTC | 2026-04-23 07:35 UTC | 23m |
| CCA968 | Air China | Malpensa International Airport (LIMC) | Hang Nadim Airport (WIDD) | 2026-04-22 10:35 UTC | 2026-04-23 07:34 UTC | 20h 58m |
| DKADC | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-23 06:26 UTC | 2026-04-23 07:15 UTC | 48m |
| HBLMD | HBL | Grenchen Airport (LSZG) | Raron Airport (LSTA) | 2026-04-23 06:34 UTC | 2026-04-23 07:02 UTC | 28m |
| RNA206 | RNA | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-04-23 05:40 UTC | 2026-04-23 07:02 UTC | 1h 21m |
| NGH28 | NGH | Newark Liberty International Airport (KEWR) | Iowa City Municipal Airport (KIOW) | 2026-04-23 04:54 UTC | 2026-04-23 07:02 UTC | 2h 7m |
| N911WJ |  | Bartow Executive Airport (KBOW) | Bartow Executive Airport (KBOW) | 2026-04-23 06:30 UTC | 2026-04-23 07:00 UTC | 29m |
| IGO7304 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-04-23 05:35 UTC | 2026-04-23 06:59 UTC | 1h 24m |
| RYR4MZ | Ryanair | Sandefjord Airport Torp (ENTO) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-04-23 05:46 UTC | 2026-04-23 06:52 UTC | 1h 6m |
| M28B |  | Altenstadt Army Airfield (ETHA) | Altenstadt Army Airfield (ETHA) | 2026-04-23 06:38 UTC | 2026-04-23 06:49 UTC | 11m |
| EXC08M | EXC | Malacca Airport (WMKM) | Batu Pahat Airport (WMAB) | 2026-04-23 06:23 UTC | 2026-04-23 06:49 UTC | 26m |
| PXT680 | PXT | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-04-23 05:56 UTC | 2026-04-23 06:47 UTC | 51m |
| VOE76RL | VOE | Nantes Atlantique Airport (LFRS) | Menorca Airport (LEMH) | 2026-04-23 05:33 UTC | 2026-04-23 06:46 UTC | 1h 13m |
| VOZ656 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Canberra International Airport (YSCB) | 2026-04-23 06:13 UTC | 2026-04-23 06:42 UTC | 28m |
| RYR18PG | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Fes Sefrou Airport (GMFU) | 2026-04-23 04:06 UTC | 2026-04-23 06:41 UTC | 2h 35m |
| UBG147 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-04-23 06:09 UTC | 2026-04-23 06:40 UTC | 31m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-23 06:04 UTC | 2026-04-23 06:40 UTC | 36m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Tribhuvan International Airport (VNKT) | 2026-04-23 03:31 UTC | 2026-04-23 06:39 UTC | 3h 7m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-04-23 04:47 UTC | 2026-04-23 06:38 UTC | 1h 50m |
| RYR78YR | Ryanair | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Palermo / Bocca Di Falco Airport (LICP) | 2026-04-23 06:04 UTC | 2026-04-23 06:36 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
