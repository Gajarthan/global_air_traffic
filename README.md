# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_09:08:36_UTC-green)

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

**Latest saved flight:** 2026-04-29 09:08:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-29 09:08:36 UTC

- **58,896** saved flights
- **22,862** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **58,896** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **715,305.4 tonnes** estimated CO2 emissions
- **41,466,978 km** total distance flown
- **848 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2502 |
| 2 | SkyWest Airlines | 2204 |
| 3 | IndiGo | 1349 |
| 4 | EJA | 1039 |
| 5 | American Airlines | 924 |
| 6 | Southwest Airlines | 839 |
| 7 | Lufthansa | 751 |
| 8 | ENY | 732 |
| 9 | Vueling | 587 |
| 10 | AXM | 578 |
| 11 | LATAM Airlines | 558 |
| 12 | All Nippon Airways | 527 |
| 13 | WIF | 492 |
| 14 | Delta Air Lines | 487 |
| 15 | AZU | 486 |
| 16 | Swiss International | 468 |
| 17 | QLK | 463 |
| 18 | LXJ | 416 |
| 19 | Alaska Airlines | 404 |
| 20 | AEE | 393 |
| 21 | easyJet | 386 |
| 22 | EJU | 382 |
| 23 | VIV | 372 |
| 24 | Air France | 345 |
| 25 | Japan Airlines | 344 |
| 26 | Cathay Pacific | 339 |
| 27 | AXB | 323 |
| 28 | AIQ | 299 |
| 29 | JetBlue | 295 |
| 30 | United Airlines | 295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 46523 |
| 2 | 🇪🇸 ES | 4281 |
| 3 | 🇮🇳 IN | 4261 |
| 4 | 🇦🇺 AU | 4021 |
| 5 | 🇧🇷 BR | 3327 |
| 6 | 🇩🇪 DE | 3267 |
| 7 | 🇮🇹 IT | 3227 |
| 8 | 🇯🇵 JP | 3209 |
| 9 | 🇨🇦 CA | 2908 |
| 10 | 🇨🇴 CO | 2607 |
| 11 | 🇬🇧 GB | 2487 |
| 12 | 🇫🇷 FR | 2336 |
| 13 | 🇲🇽 MX | 1855 |
| 14 | 🇬🇷 GR | 1763 |
| 15 | 🇨🇭 CH | 1651 |
| 16 | 🇳🇴 NO | 1604 |
| 17 | 🇲🇾 MY | 1403 |
| 18 | 🇿🇦 ZA | 1198 |
| 19 | 🇳🇿 NZ | 1108 |
| 20 | 🇹🇷 TR | 1066 |
| 21 | 🇹🇭 TH | 1065 |
| 22 | 🇵🇭 PH | 1000 |
| 23 | 🇵🇱 PL | 948 |
| 24 | 🇰🇷 KR | 947 |
| 25 | 🇬🇹 GT | 860 |
| 26 | 🇲🇦 MA | 741 |
| 27 | 🇲🇪 ME | 639 |
| 28 | 🇲🇴 MO | 634 |
| 29 | 🇳🇱 NL | 616 |
| 30 | 🇮🇩 ID | 507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1321 |
| 2 | Tokyo International Airport |  | JP | 1091 |
| 3 | Denver International Airport |  | US | 982 |
| 4 | Indira Gandhi International Airport |  | IN | 893 |
| 5 | El Dorado International Airport |  | CO | 878 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 869 |
| 7 | Guaymaral Airport |  | CO | 803 |
| 8 | Harry Reid International Airport |  | US | 748 |
| 9 | Frankfurt am Main International Airport |  | DE | 739 |
| 10 | Zurich Airport |  | CH | 711 |
| 11 | La Aurora Airport |  | GT | 649 |
| 12 | Macau International Airport |  | MO | 634 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 581 |
| 14 | Chicago O'Hare International Airport |  | US | 560 |
| 15 | Kuala Lumpur International Airport |  | MY | 552 |
| 16 | Madrid Barajas International Airport |  | ES | 547 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 543 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 518 |
| 19 | Bengaluru International Airport |  | IN | 514 |
| 20 | Malpensa International Airport |  | IT | 509 |
| 21 | Congonhas Airport |  | BR | 479 |
| 22 | Charlotte/Douglas International Airport |  | US | 468 |
| 23 | Tenerife Norte Airport |  | ES | 461 |
| 24 | Ninoy Aquino International Airport |  | PH | 459 |
| 25 | Charles de Gaulle International Airport |  | FR | 457 |
| 26 | Salt Lake City International Airport |  | US | 454 |
| 27 | Capua Airport |  | IT | 453 |
| 28 | Daniel K Inouye International Airport |  | US | 442 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 429 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 424 |
| 31 | Barcelona International Airport |  | ES | 400 |
| 32 | Vitoria/Foronda Airport |  | ES | 397 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 390 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 388 |
| 35 | O. R. Tambo International Airport |  | ZA | 382 |
| 36 | Reno/Tahoe International Airport |  | US | 376 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 374 |
| 38 | Don Mueang International Airport |  | TH | 364 |
| 39 | Amsterdam Airport Schiphol |  | NL | 359 |
| 40 | Calgary International Airport |  | CA | 347 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 328 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 253 | 1h 7m | 706 km | 3,080.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 4 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 195 | 21m | 244 km | 821.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 187 | 24m | 225 km | 725.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 175 | 1h 27m | 910 km | 2,746.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 167 | 28m | 304 km | 875.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 145 | 19m | 165 km | 412.5 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 142 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 140 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 133 | 26m | 275 km | 630.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 124 | 1h 12m | 770 km | 1,647.2 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 111 | 44m | 452 km | 865.1 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 101 | 20m | 99 km | 173.0 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 98 | 31m | 369 km | 623.8 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 96 | 27m | 215 km | 355.5 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 94 | 20m | 250 km | 406.0 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 88 | 52m | 556 km | 843.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 88 | 27m | 152 km | 230.0 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 87 | 20m | 147 km | 220.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 82 | 1h 1m | 695 km | 982.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 81 | 1h 43m | 1,156 km | 1,615.9 t |
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 81 | 1h 53m | 1,304 km | 1,822.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 80 | 58m | 493 km | 680.6 t |
| 26 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 78 | 23m | 55 km | 74.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 76 | 1h 42m | 1,423 km | 1,865.2 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 76 | 12m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 74 | 14m | 154 km | 196.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ISR563 | ISR | Ben Gurion International Airport (LLBG) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-29 07:19 UTC | 2026-04-29 09:08 UTC | 1h 49m |
| DLH9WF | Lufthansa | Munich International Airport (EDDM) | Stockholm-Arlanda Airport (ESSA) | 2026-04-29 07:03 UTC | 2026-04-29 09:04 UTC | 2h 0m |
| HLC238 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-04-29 08:49 UTC | 2026-04-29 09:02 UTC | 13m |
| IOS210 | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-04-29 08:33 UTC | 2026-04-29 09:00 UTC | 27m |
| KUR | KUR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-29 08:06 UTC | 2026-04-29 08:57 UTC | 51m |
| ORLIK13 | ORL | Radom-Sadkow Airport (EPRA) | Radom-Sadkow Airport (EPRA) | 2026-04-29 08:05 UTC | 2026-04-29 08:56 UTC | 50m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-04-28 21:50 UTC | 2026-04-29 08:55 UTC | 11h 4m |
| CFH23 | CFH | Wollomombi Airport (YWMM) | Woodville Airport (YWVL) | 2026-04-29 08:37 UTC | 2026-04-29 08:47 UTC | 10m |
| DEOME | DEO | Stadtlohn-Vreden Airport (EDLS) | Stadtlohn-Vreden Airport (EDLS) | 2026-04-29 08:15 UTC | 2026-04-29 08:42 UTC | 27m |
| ITY1617 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Bari / Palese International Airport (LIBD) | 2026-04-29 07:59 UTC | 2026-04-29 08:40 UTC | 41m |
| M28B |  | Jever Airport (ETNJ) | Jever Airport (ETNJ) | 2026-04-29 08:08 UTC | 2026-04-29 08:37 UTC | 29m |
| RYR6A | Ryanair | Paris Beauvais Tille Airport (LFOB) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-04-29 06:51 UTC | 2026-04-29 08:34 UTC | 1h 43m |
| HSOMR3 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-04-29 07:56 UTC | 2026-04-29 08:31 UTC | 34m |
| AXM6082 | AXM | Kluang Airport (WMAP) | Jendarata Airport (WMAJ) | 2026-04-29 08:00 UTC | 2026-04-29 08:30 UTC | 29m |
| VTHNB | VTH | Juhu Aerodrome (VAJJ) | Juhu Aerodrome (VAJJ) | 2026-04-29 07:38 UTC | 2026-04-29 08:29 UTC | 51m |
| AWA473 | AWA | VGZR (VGZR) | Balurghat Airport (VEBG) | 2026-04-29 07:45 UTC | 2026-04-29 08:25 UTC | 39m |
| EVA183 | EVA Air | Narita International Airport (RJAA) | Taiwan Taoyuan International Airport (RCTP) | 2026-04-29 05:13 UTC | 2026-04-29 08:21 UTC | 3h 8m |
| ANA697 | All Nippon Airways | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-04-29 07:10 UTC | 2026-04-29 08:21 UTC | 1h 11m |
| IGO6542 | IndiGo | Bengaluru International Airport (VOBL) | Hosur Airport (VO95) | 2026-04-29 08:02 UTC | 2026-04-29 08:21 UTC | 19m |
| FHY542 | FHY | Linz Airport (LOWL) | Vienna International Airport (LOWW) | 2026-04-29 07:51 UTC | 2026-04-29 08:21 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
