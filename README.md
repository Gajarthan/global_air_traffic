# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_12:26:42_UTC-green)

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

**Latest saved flight:** 2026-05-01 12:26:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 12:26:42 UTC

- **61,968** saved flights
- **23,790** unique routes
- **125** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **61,968** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **757,024.5 tonnes** estimated CO2 emissions
- **43,885,477 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2595 |
| 2 | SkyWest Airlines | 2302 |
| 3 | IndiGo | 1419 |
| 4 | EJA | 1117 |
| 5 | American Airlines | 965 |
| 6 | Southwest Airlines | 877 |
| 7 | Lufthansa | 790 |
| 8 | ENY | 765 |
| 9 | Vueling | 610 |
| 10 | AXM | 606 |
| 11 | LATAM Airlines | 587 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 521 |
| 14 | Delta Air Lines | 515 |
| 15 | AZU | 503 |
| 16 | QLK | 498 |
| 17 | Swiss International | 480 |
| 18 | LXJ | 439 |
| 19 | Alaska Airlines | 427 |
| 20 | AEE | 404 |
| 21 | easyJet | 404 |
| 22 | EJU | 396 |
| 23 | VIV | 389 |
| 24 | Cathay Pacific | 379 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 359 |
| 27 | AXB | 342 |
| 28 | AIQ | 319 |
| 29 | CXK | 306 |
| 30 | United Airlines | 303 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 48983 |
| 2 | 🇮🇳 IN | 4482 |
| 3 | 🇪🇸 ES | 4472 |
| 4 | 🇦🇺 AU | 4285 |
| 5 | 🇧🇷 BR | 3499 |
| 6 | 🇩🇪 DE | 3431 |
| 7 | 🇯🇵 JP | 3408 |
| 8 | 🇮🇹 IT | 3359 |
| 9 | 🇨🇦 CA | 3061 |
| 10 | 🇬🇧 GB | 2634 |
| 11 | 🇨🇴 CO | 2629 |
| 12 | 🇫🇷 FR | 2430 |
| 13 | 🇲🇽 MX | 1948 |
| 14 | 🇬🇷 GR | 1839 |
| 15 | 🇨🇭 CH | 1728 |
| 16 | 🇳🇴 NO | 1709 |
| 17 | 🇲🇾 MY | 1481 |
| 18 | 🇿🇦 ZA | 1265 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1124 |
| 21 | 🇹🇷 TR | 1099 |
| 22 | 🇵🇭 PH | 1062 |
| 23 | 🇰🇷 KR | 1008 |
| 24 | 🇵🇱 PL | 994 |
| 25 | 🇬🇹 GT | 926 |
| 26 | 🇲🇦 MA | 762 |
| 27 | 🇲🇴 MO | 698 |
| 28 | 🇲🇪 ME | 675 |
| 29 | 🇳🇱 NL | 646 |
| 30 | 🇮🇩 ID | 529 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1370 |
| 2 | Tokyo International Airport |  | JP | 1151 |
| 3 | Denver International Airport |  | US | 1025 |
| 4 | Indira Gandhi International Airport |  | IN | 943 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 902 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 824 |
| 8 | Harry Reid International Airport |  | US | 791 |
| 9 | Frankfurt am Main International Airport |  | DE | 787 |
| 10 | Zurich Airport |  | CH | 738 |
| 11 | Macau International Airport |  | MO | 698 |
| 12 | La Aurora Airport |  | GT | 694 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 610 |
| 14 | Kuala Lumpur International Airport |  | MY | 586 |
| 15 | Chicago O'Hare International Airport |  | US | 584 |
| 16 | Madrid Barajas International Airport |  | ES | 578 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 564 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 537 |
| 20 | Malpensa International Airport |  | IT | 536 |
| 21 | Congonhas Airport |  | BR | 505 |
| 22 | Charlotte/Douglas International Airport |  | US | 492 |
| 23 | Salt Lake City International Airport |  | US | 485 |
| 24 | Ninoy Aquino International Airport |  | PH | 482 |
| 25 | Tenerife Norte Airport |  | ES | 480 |
| 26 | Charles de Gaulle International Airport |  | FR | 477 |
| 27 | Capua Airport |  | IT | 467 |
| 28 | Daniel K Inouye International Airport |  | US | 460 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 449 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 446 |
| 31 | Barcelona International Airport |  | ES | 416 |
| 32 | Vitoria/Foronda Airport |  | ES | 413 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 410 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 403 |
| 35 | O. R. Tambo International Airport |  | ZA | 398 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 390 |
| 37 | Reno/Tahoe International Airport |  | US | 387 |
| 38 | Don Mueang International Airport |  | TH | 387 |
| 39 | Amsterdam Airport Schiphol |  | NL | 381 |
| 40 | Calgary International Airport |  | CA | 367 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 338 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 207 | 21m | 244 km | 871.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 155 | 20m | 165 km | 440.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 149 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 139 | 26m | 275 km | 658.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 108 | 20m | 99 km | 185.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 100 | 20m | 250 km | 431.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 94 | 20m | 147 km | 237.9 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 92 | 28m | 152 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 87 | 1h 42m | 1,156 km | 1,735.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 1m | 695 km | 1,018.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 84 | 57m | 493 km | 714.6 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 83 | 1h 53m | 1,304 km | 1,867.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 82 | 14m | 154 km | 217.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 82 | 12m | - | - |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 82 | 23m | 55 km | 77.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 79 | 1h 43m | 1,423 km | 1,938.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N110LU |  | Boca Raton Airport (KBCT) | William P Gwinn Airport (06FA) | 2026-05-01 11:27 UTC | 2026-05-01 12:26 UTC | 58m |
| OEFDI | OEF | Klatovy Airport (LKKT) | Klatovy Airport (LKKT) | 2026-05-01 10:51 UTC | 2026-05-01 12:26 UTC | 1h 34m |
| HB1835 |  | Winterthur Airport (LSPH) | LSMF (LSMF) | 2026-05-01 10:27 UTC | 2026-05-01 12:26 UTC | 1h 58m |
| TGKBG | TGK | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-01 11:59 UTC | 2026-05-01 12:24 UTC | 24m |
| HPK54 | HPK | Republic Airport (KFRG) | Talmage Field (03NY) | 2026-05-01 11:42 UTC | 2026-05-01 12:22 UTC | 40m |
| N15CH |  | Orlando Apopka Airport (KX04) | Albert Whitted Airport (KSPG) | 2026-05-01 11:27 UTC | 2026-05-01 12:20 UTC | 52m |
| CPA801 | Cathay Pacific | Chicago O'Hare International Airport (KORD) | Macau International Airport (VMMC) | 2026-04-30 21:47 UTC | 2026-05-01 12:13 UTC | 14h 26m |
| ZER | ZER | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-01 11:39 UTC | 2026-05-01 12:09 UTC | 29m |
| N53695 |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-05-01 11:43 UTC | 2026-05-01 12:07 UTC | 24m |
| N694SP |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-01 11:17 UTC | 2026-05-01 12:05 UTC | 48m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-01 11:54 UTC | 2026-05-01 12:04 UTC | 10m |
| N89869 |  | Stocker Airport (XA72) | Jbj Ranch Airport (XA98) | 2026-05-01 11:48 UTC | 2026-05-01 12:00 UTC | 11m |
| OMBIK | OMB | Martin Glider Airport (LZMA) | Martin Glider Airport (LZMA) | 2026-05-01 11:03 UTC | 2026-05-01 12:00 UTC | 56m |
| N528SV |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-05-01 11:06 UTC | 2026-05-01 11:59 UTC | 53m |
| N476LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-05-01 10:55 UTC | 2026-05-01 11:58 UTC | 1h 2m |
| AUA10B | Austrian Airlines | Vienna International Airport (LOWW) | Wolfsberg Airport (LOKW) | 2026-05-01 11:30 UTC | 2026-05-01 11:56 UTC | 26m |
| PAV631 | PAV | Ibiza Airport (LEIB) | Saint-Rambert-d'Albon Airport (LFLR) | 2026-05-01 10:23 UTC | 2026-05-01 11:56 UTC | 1h 33m |
| TVF77FX | TVF | Paris-Orly Airport (LFPO) | Vinon Sur Verdon Airport (LFNF) | 2026-05-01 10:41 UTC | 2026-05-01 11:56 UTC | 1h 14m |
| N146SG |  | Clearwater Executive Airport (KCLW) | Peter O Knight Airport (KTPF) | 2026-05-01 11:43 UTC | 2026-05-01 11:54 UTC | 11m |
| IGO5EC | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Jamshedpur Airport (VEJS) | 2026-05-01 11:12 UTC | 2026-05-01 11:53 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
