# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_08:39:15_UTC-green)

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

**Latest saved flight:** 2026-05-02 08:39:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 08:39:15 UTC

- **63,679** saved flights
- **24,306** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,679** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **779,046.2 tonnes** estimated CO2 emissions
- **45,162,096 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2669 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1457 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 991 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 814 |
| 8 | ENY | 784 |
| 9 | Vueling | 624 |
| 10 | AXM | 619 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 560 |
| 13 | WIF | 533 |
| 14 | Delta Air Lines | 530 |
| 15 | AZU | 517 |
| 16 | QLK | 502 |
| 17 | Swiss International | 487 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 439 |
| 20 | easyJet | 414 |
| 21 | AEE | 410 |
| 22 | EJU | 408 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 385 |
| 25 | Japan Airlines | 374 |
| 26 | Air France | 364 |
| 27 | AXB | 353 |
| 28 | AIQ | 325 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50524 |
| 2 | 🇮🇳 IN | 4601 |
| 3 | 🇪🇸 ES | 4593 |
| 4 | 🇦🇺 AU | 4337 |
| 5 | 🇧🇷 BR | 3593 |
| 6 | 🇩🇪 DE | 3533 |
| 7 | 🇯🇵 JP | 3476 |
| 8 | 🇮🇹 IT | 3447 |
| 9 | 🇨🇦 CA | 3136 |
| 10 | 🇬🇧 GB | 2703 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2494 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1889 |
| 15 | 🇨🇭 CH | 1765 |
| 16 | 🇳🇴 NO | 1742 |
| 17 | 🇲🇾 MY | 1517 |
| 18 | 🇿🇦 ZA | 1288 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1157 |
| 21 | 🇹🇷 TR | 1121 |
| 22 | 🇵🇭 PH | 1081 |
| 23 | 🇰🇷 KR | 1033 |
| 24 | 🇵🇱 PL | 1029 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 776 |
| 27 | 🇲🇴 MO | 717 |
| 28 | 🇲🇪 ME | 688 |
| 29 | 🇳🇱 NL | 667 |
| 30 | 🇮🇩 ID | 539 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1174 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 968 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 921 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 817 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 753 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 717 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 627 |
| 14 | Chicago O'Hare International Airport |  | US | 607 |
| 15 | Kuala Lumpur International Airport |  | MY | 602 |
| 16 | Madrid Barajas International Airport |  | ES | 599 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 555 |
| 20 | Malpensa International Airport |  | IT | 544 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 502 |
| 24 | Ninoy Aquino International Airport |  | PH | 491 |
| 25 | Charles de Gaulle International Airport |  | FR | 491 |
| 26 | Tenerife Norte Airport |  | ES | 488 |
| 27 | Daniel K Inouye International Airport |  | US | 472 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 464 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 431 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 418 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Don Mueang International Airport |  | TH | 399 |
| 37 | Amsterdam Airport Schiphol |  | NL | 396 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 39 | Reno/Tahoe International Airport |  | US | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 258 | 1h 7m | 706 km | 3,141.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 216 | 21m | 244 km | 909.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 200 | 24m | 225 km | 775.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 187 | 1h 27m | 910 km | 2,934.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 184 | 28m | 304 km | 964.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 150 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 137 | 1h 12m | 770 km | 1,819.9 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 118 | 44m | 452 km | 919.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 107 | 31m | 369 km | 681.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 96 | 20m | 147 km | 242.9 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 89 | 1h 42m | 1,156 km | 1,775.5 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 88 | 1h 3m | 695 km | 1,054.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 87 | 57m | 493 km | 740.2 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CAI6ZN | CAI | Antalya International Airport (LTAI) | LHGR (LHGR) | 2026-05-02 06:38 UTC | 2026-05-02 08:39 UTC | 2h 0m |
| BOX630 | BOX | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-05-01 19:09 UTC | 2026-05-02 08:37 UTC | 13h 28m |
| ZSMBR | ZSM | Wonderboom Airport (FAWB) | Secunda Airport (FASC) | 2026-05-02 08:15 UTC | 2026-05-02 08:30 UTC | 15m |
| CLX4755 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-05-01 21:39 UTC | 2026-05-02 08:30 UTC | 10h 51m |
| EWG4HM | EWG | Dusseldorf International Airport (EDDL) | Palma De Mallorca Airport (LEPA) | 2026-05-02 06:16 UTC | 2026-05-02 08:28 UTC | 2h 11m |
| VLG1GJ | Vueling | Zurich Airport (LSZH) | Palma De Mallorca Airport (LEPA) | 2026-05-02 06:50 UTC | 2026-05-02 08:28 UTC | 1h 37m |
| EDC912R | EDC | Birmingham International Airport (EGBB) | Southampton Airport (EGHI) | 2026-05-02 08:00 UTC | 2026-05-02 08:27 UTC | 26m |
| OEKFC | OEK | Stadtlohn-Vreden Airport (EDLS) | Stadtlohn-Vreden Airport (EDLS) | 2026-05-02 08:02 UTC | 2026-05-02 08:26 UTC | 23m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-05-02 07:23 UTC | 2026-05-02 08:15 UTC | 51m |
| UAE9788 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-05-02 01:52 UTC | 2026-05-02 08:14 UTC | 6h 22m |
| CGAPC | CGA | Ottawa / Macdonald-Cartier International Airport (CYOW) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-05-02 05:21 UTC | 2026-05-02 08:04 UTC | 2h 42m |
| HBZPV | HBZ | Sitterdorf Airport (LSZV) | LSMF (LSMF) | 2026-05-02 07:29 UTC | 2026-05-02 08:02 UTC | 32m |
| RYR8NQ | Ryanair | Bari / Palese International Airport (LIBD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-02 06:21 UTC | 2026-05-02 07:59 UTC | 1h 38m |
| RYR653Z | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-05-02 06:44 UTC | 2026-05-02 07:55 UTC | 1h 10m |
| TVJ132 | TVJ | Suvarnabhumi Airport (VTBS) | VLXL (VLXL) | 2026-05-02 07:01 UTC | 2026-05-02 07:54 UTC | 53m |
| AXM6073 | AXM | Kota Kinabalu International Airport (WBKK) | Anduki Airport (WBAK) | 2026-05-02 07:29 UTC | 2026-05-02 07:53 UTC | 23m |
| RYR41ZK | Ryanair | Brindisi / Casale Airport (LIBR) | Malpensa International Airport (LIMC) | 2026-05-02 06:20 UTC | 2026-05-02 07:51 UTC | 1h 31m |
| DFANO | DFA | Æra Airfield (ENAE) | Æra Airfield (ENAE) | 2026-05-02 07:40 UTC | 2026-05-02 07:50 UTC | 10m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-05-02 07:35 UTC | 2026-05-02 07:48 UTC | 12m |
| SWR41D | Swiss International | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-05-02 07:15 UTC | 2026-05-02 07:47 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
