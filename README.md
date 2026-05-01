# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_19:44:16_UTC-green)

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

**Latest saved flight:** 2026-05-01 19:44:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 19:44:16 UTC

- **63,008** saved flights
- **24,115** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,008** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **768,970.0 tonnes** estimated CO2 emissions
- **44,577,971 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2646 |
| 2 | SkyWest Airlines | 2345 |
| 3 | IndiGo | 1435 |
| 4 | EJA | 1136 |
| 5 | American Airlines | 979 |
| 6 | Southwest Airlines | 891 |
| 7 | Lufthansa | 811 |
| 8 | ENY | 776 |
| 9 | Vueling | 615 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 591 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 521 |
| 15 | AZU | 517 |
| 16 | QLK | 498 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 450 |
| 19 | Alaska Airlines | 431 |
| 20 | easyJet | 410 |
| 21 | AEE | 409 |
| 22 | EJU | 403 |
| 23 | VIV | 395 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 366 |
| 26 | Air France | 364 |
| 27 | AXB | 348 |
| 28 | AIQ | 320 |
| 29 | CXK | 316 |
| 30 | MXY | 309 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49968 |
| 2 | 🇪🇸 ES | 4559 |
| 3 | 🇮🇳 IN | 4528 |
| 4 | 🇦🇺 AU | 4289 |
| 5 | 🇧🇷 BR | 3580 |
| 6 | 🇩🇪 DE | 3510 |
| 7 | 🇮🇹 IT | 3423 |
| 8 | 🇯🇵 JP | 3410 |
| 9 | 🇨🇦 CA | 3101 |
| 10 | 🇬🇧 GB | 2684 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2479 |
| 13 | 🇲🇽 MX | 1995 |
| 14 | 🇬🇷 GR | 1872 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1491 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1128 |
| 21 | 🇹🇷 TR | 1109 |
| 22 | 🇵🇭 PH | 1063 |
| 23 | 🇵🇱 PL | 1021 |
| 24 | 🇰🇷 KR | 1008 |
| 25 | 🇬🇹 GT | 985 |
| 26 | 🇲🇦 MA | 771 |
| 27 | 🇲🇴 MO | 704 |
| 28 | 🇲🇪 ME | 684 |
| 29 | 🇳🇱 NL | 659 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1393 |
| 2 | Tokyo International Airport |  | JP | 1153 |
| 3 | Denver International Airport |  | US | 1038 |
| 4 | Indira Gandhi International Airport |  | IN | 952 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 914 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 811 |
| 9 | Harry Reid International Airport |  | US | 802 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 737 |
| 12 | Macau International Airport |  | MO | 704 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 621 |
| 14 | Chicago O'Hare International Airport |  | US | 597 |
| 15 | Madrid Barajas International Airport |  | ES | 594 |
| 16 | Kuala Lumpur International Airport |  | MY | 591 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 574 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 545 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 516 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 496 |
| 24 | Tenerife Norte Airport |  | ES | 488 |
| 25 | Charles de Gaulle International Airport |  | FR | 488 |
| 26 | Ninoy Aquino International Airport |  | PH | 483 |
| 27 | Capua Airport |  | IT | 468 |
| 28 | Daniel K Inouye International Airport |  | US | 466 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 456 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 453 |
| 31 | Barcelona International Airport |  | ES | 424 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 419 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 413 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 395 |
| 37 | Reno/Tahoe International Airport |  | US | 393 |
| 38 | Amsterdam Airport Schiphol |  | NL | 392 |
| 39 | Don Mueang International Airport |  | TH | 388 |
| 40 | Calgary International Airport |  | CA | 372 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 212 | 21m | 244 km | 892.7 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 156 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 114 | 21m | 99 km | 195.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 102 | 28m | 152 km | 266.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 1m | 695 km | 1,042.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 85 | 1h 53m | 1,304 km | 1,912.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 81 | 1h 43m | 1,423 km | 1,987.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 80 | 1h 20m | 961 km | 1,326.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N104UV |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-01 19:22 UTC | 2026-05-01 19:44 UTC | 21m |
| N759PA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-05-01 19:14 UTC | 2026-05-01 19:33 UTC | 18m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-01 19:11 UTC | 2026-05-01 19:31 UTC | 20m |
| CGMBX | CGM | Cornwall Regional Airport (CYCC) | Ste-Agnes-de-Dundee Airport (CDD3) | 2026-05-01 18:52 UTC | 2026-05-01 19:31 UTC | 38m |
| JAL74 | Japan Airlines | Tokyo International Airport (RJTT) | Kalaeloa (John Rodgers Field) Airport (PHJR) | 2026-05-01 12:29 UTC | 2026-05-01 19:26 UTC | 6h 57m |
| TGLOP | TGL | La Aurora Airport (MGGT) | MHLE (MHLE) | 2026-05-01 18:57 UTC | 2026-05-01 19:24 UTC | 27m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-01 19:09 UTC | 2026-05-01 19:22 UTC | 12m |
| AAL3219 | American Airlines | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-01 18:08 UTC | 2026-05-01 19:17 UTC | 1h 9m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-05-01 19:02 UTC | 2026-05-01 19:15 UTC | 13m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-01 18:58 UTC | 2026-05-01 19:13 UTC | 14m |
| N7399J |  | Polecat Aerodrome (SC67) | Polecat Aerodrome (SC67) | 2026-05-01 19:08 UTC | 2026-05-01 19:11 UTC | 3m |
| N128SH |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Tracy Municipal Airport (KTCY) | 2026-05-01 18:25 UTC | 2026-05-01 19:11 UTC | 46m |
| N344BL |  | Winter Haven Regional Airport (KGIF) | Winter Haven Regional Airport (KGIF) | 2026-05-01 19:10 UTC | 2026-05-01 19:10 UTC | 0m |
| TGRYV | TGR | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 18:27 UTC | 2026-05-01 19:10 UTC | 42m |
| N786MM |  | Vancouver International Airport (CYVR) | Harry Reid International Airport (KLAS) | 2026-05-01 16:49 UTC | 2026-05-01 19:09 UTC | 2h 19m |
| TGCYC | TGC | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-05-01 18:48 UTC | 2026-05-01 19:09 UTC | 21m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-01 18:51 UTC | 2026-05-01 19:05 UTC | 14m |
| N555NL |  | Waterbury-Oxford Airport (KOXC) | Laguardia Airport (KLGA) | 2026-05-01 18:39 UTC | 2026-05-01 19:05 UTC | 25m |
| N2711R |  | Renton Municipal Airport (KRNT) | William R Fairchild International Airport (KCLM) | 2026-05-01 18:14 UTC | 2026-05-01 19:04 UTC | 50m |
| N66AA |  | Plymouth Municipal Airport (KPYM) | Provincetown Municipal Airport (KPVC) | 2026-05-01 18:47 UTC | 2026-05-01 19:03 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
