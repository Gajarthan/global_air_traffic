# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_08:03:59_UTC-green)

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

**Latest saved flight:** 2026-04-24 08:03:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-24 08:03:59 UTC

- **50,744** saved flights
- **20,385** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **50,744** saved routes in the archive
- **1h 13m** average flight duration

### Carbon Footprint Estimate

- **606,732.6 tonnes** estimated CO2 emissions
- **35,172,901 km** total distance flown
- **833 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2133 |
| 2 | SkyWest Airlines | 1940 |
| 3 | IndiGo | 1174 |
| 4 | EJA | 878 |
| 5 | American Airlines | 822 |
| 6 | Southwest Airlines | 723 |
| 7 | ENY | 651 |
| 8 | Lufthansa | 582 |
| 9 | Vueling | 505 |
| 10 | AXM | 497 |
| 11 | LATAM Airlines | 492 |
| 12 | All Nippon Airways | 458 |
| 13 | AZU | 430 |
| 14 | Delta Air Lines | 418 |
| 15 | WIF | 418 |
| 16 | QLK | 410 |
| 17 | LXJ | 382 |
| 18 | Swiss International | 380 |
| 19 | AEE | 344 |
| 20 | Alaska Airlines | 337 |
| 21 | EJU | 325 |
| 22 | VIV | 322 |
| 23 | easyJet | 318 |
| 24 | Japan Airlines | 302 |
| 25 | Air France | 284 |
| 26 | AXB | 270 |
| 27 | Cathay Pacific | 266 |
| 28 | JetBlue | 263 |
| 29 | United Airlines | 263 |
| 30 | AIQ | 259 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 40376 |
| 2 | 🇮🇳 IN | 3692 |
| 3 | 🇪🇸 ES | 3657 |
| 4 | 🇦🇺 AU | 3540 |
| 5 | 🇧🇷 BR | 2932 |
| 6 | 🇯🇵 JP | 2772 |
| 7 | 🇮🇹 IT | 2710 |
| 8 | 🇩🇪 DE | 2688 |
| 9 | 🇨🇦 CA | 2540 |
| 10 | 🇨🇴 CO | 2346 |
| 11 | 🇬🇧 GB | 2074 |
| 12 | 🇫🇷 FR | 1932 |
| 13 | 🇲🇽 MX | 1571 |
| 14 | 🇬🇷 GR | 1535 |
| 15 | 🇨🇭 CH | 1397 |
| 16 | 🇳🇴 NO | 1358 |
| 17 | 🇲🇾 MY | 1215 |
| 18 | 🇿🇦 ZA | 1040 |
| 19 | 🇳🇿 NZ | 984 |
| 20 | 🇹🇭 TH | 927 |
| 21 | 🇹🇷 TR | 899 |
| 22 | 🇵🇭 PH | 886 |
| 23 | 🇰🇷 KR | 843 |
| 24 | 🇵🇱 PL | 814 |
| 25 | 🇬🇹 GT | 771 |
| 26 | 🇲🇦 MA | 623 |
| 27 | 🇲🇪 ME | 540 |
| 28 | 🇳🇱 NL | 511 |
| 29 | 🇲🇴 MO | 479 |
| 30 | 🇧🇸 BS | 444 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1176 |
| 2 | Tokyo International Airport |  | JP | 942 |
| 3 | Denver International Airport |  | US | 844 |
| 4 | El Dorado International Airport |  | CO | 802 |
| 5 | Indira Gandhi International Airport |  | IN | 792 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 759 |
| 7 | Guaymaral Airport |  | CO | 688 |
| 8 | Harry Reid International Airport |  | US | 666 |
| 9 | Zurich Airport |  | CH | 590 |
| 10 | La Aurora Airport |  | GT | 574 |
| 11 | Frankfurt am Main International Airport |  | DE | 563 |
| 12 | Chicago O'Hare International Airport |  | US | 503 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 495 |
| 14 | Kuala Lumpur International Airport |  | MY | 485 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 482 |
| 16 | Macau International Airport |  | MO | 479 |
| 17 | Sydney Kingsford Smith International Airport |  | AU | 464 |
| 18 | Madrid Barajas International Airport |  | ES | 462 |
| 19 | Bengaluru International Airport |  | IN | 439 |
| 20 | Charlotte/Douglas International Airport |  | US | 426 |
| 21 | Congonhas Airport |  | BR | 420 |
| 22 | Malpensa International Airport |  | IT | 415 |
| 23 | Ninoy Aquino International Airport |  | PH | 408 |
| 24 | Tenerife Norte Airport |  | ES | 408 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 383 |
| 26 | Salt Lake City International Airport |  | US | 377 |
| 27 | Charles de Gaulle International Airport |  | FR | 375 |
| 28 | Daniel K Inouye International Airport |  | US | 374 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 367 |
| 30 | Capua Airport |  | IT | 354 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 345 |
| 32 | Reno/Tahoe International Airport |  | US | 342 |
| 33 | Vitoria/Foronda Airport |  | ES | 342 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 342 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 338 |
| 36 | Barcelona International Airport |  | ES | 336 |
| 37 | O. R. Tambo International Airport |  | ZA | 333 |
| 38 | Don Mueang International Airport |  | TH | 314 |
| 39 | Calgary International Airport |  | CA | 309 |
| 40 | Viracopos International Airport |  | BR | 299 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 278 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 238 | 1h 7m | 706 km | 2,897.7 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 194 | 14m | 114 km | 380.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 174 | 24m | 225 km | 675.0 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 153 | 21m | 244 km | 644.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 151 | 28m | 304 km | 791.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 145 | 1h 27m | 910 km | 2,275.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 135 | 19m | 165 km | 384.0 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 127 | 31m | - | - |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 122 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 118 | 26m | 275 km | 559.2 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 104 | 44m | 452 km | 810.5 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 94 | 20m | 99 km | 161.0 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 89 | 1h 11m | 770 km | 1,182.3 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 87 | 31m | 369 km | 553.8 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 87 | 20m | 250 km | 375.8 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 82 | 26m | 215 km | 303.7 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 80 | 20m | 147 km | 202.4 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 80 | 52m | 556 km | 766.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 77 | 27m | 152 km | 201.2 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 73 | 1h 41m | 1,156 km | 1,456.3 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 72 | 13m | 99 km | 123.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 72 | 1h 0m | 695 km | 863.1 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 70 | 58m | 493 km | 595.5 t |
| 26 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 67 | 12m | 15 km | 17.7 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 66 | 1h 41m | 1,423 km | 1,619.7 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 66 | 13m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 66 | 1h 53m | 1,304 km | 1,484.8 t |
| 30 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 65 | 16m | 162 km | 182.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| YOQ | YOQ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-04-24 07:39 UTC | 2026-04-24 08:03 UTC | 24m |
| 2612 |  | Chiang Mai International Airport (VTCC) | Chiang Mai International Airport (VTCC) | 2026-04-24 07:32 UTC | 2026-04-24 07:53 UTC | 21m |
| QTR818 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-24 01:07 UTC | 2026-04-24 07:53 UTC | 6h 46m |
| 21199 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-24 06:47 UTC | 2026-04-24 07:48 UTC | 1h 0m |
| GPMMC | GPM | Norwich International Airport (EGSH) | Norwich International Airport (EGSH) | 2026-04-24 07:15 UTC | 2026-04-24 07:47 UTC | 31m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-04-23 20:44 UTC | 2026-04-24 07:40 UTC | 10h 56m |
| BNOR | BNO | Brønnøysund Airport (ENBN) | Sandnessjoen Airport Stokka (ENST) | 2026-04-24 07:25 UTC | 2026-04-24 07:36 UTC | 11m |
| HBSGW | HBS | Lommis Airfield (LSZT) | Lommis Airfield (LSZT) | 2026-04-24 07:20 UTC | 2026-04-24 07:32 UTC | 11m |
| AUR201 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-04-24 07:11 UTC | 2026-04-24 07:25 UTC | 13m |
| SAS38H | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-24 04:16 UTC | 2026-04-24 07:25 UTC | 3h 8m |
| RYR518E | Ryanair | Baneasa International Airport (LRBS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-24 06:04 UTC | 2026-04-24 07:24 UTC | 1h 20m |
| MCK307 | MCK | Sion Airport (LSGS) | Trento / Mattarello Airport (LIDT) | 2026-04-24 06:34 UTC | 2026-04-24 07:20 UTC | 46m |
| PTN97E | PTN | Munich International Airport (EDDM) | Raron Airport (LSTA) | 2026-04-24 06:29 UTC | 2026-04-24 07:20 UTC | 51m |
| SWR3L | Swiss International | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-04-24 06:26 UTC | 2026-04-24 07:17 UTC | 50m |
| RYR5XE | Ryanair | Pescara International Airport (LIBP) | Malpensa International Airport (LIMC) | 2026-04-24 06:12 UTC | 2026-04-24 07:17 UTC | 1h 5m |
| SLR | SLR | Cessnock Airport (YCNK) | Sydney Bankstown Airport (YSBK) | 2026-04-24 06:35 UTC | 2026-04-24 07:16 UTC | 41m |
| SAS211 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Kristiansand Airport (ENCN) | 2026-04-24 06:41 UTC | 2026-04-24 07:13 UTC | 32m |
| RYR59GQ | Ryanair | Torino / Caselle International Airport (LIMF) | Bari / Palese International Airport (LIBD) | 2026-04-24 05:59 UTC | 2026-04-24 07:12 UTC | 1h 13m |
| SNJ95 | SNJ | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-04-24 06:01 UTC | 2026-04-24 07:11 UTC | 1h 10m |
| BHA171 | BHA | Tribhuvan International Airport (VNKT) | Rajbiraj Airport (VNRB) | 2026-04-24 06:46 UTC | 2026-04-24 07:10 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
