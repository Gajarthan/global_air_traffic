# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_07:36:47_UTC-green)

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

**Latest saved flight:** 2026-05-08 07:36:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-08 07:36:47 UTC

- **72,845** saved flights
- **27,026** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **72,845** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **897,851.2 tonnes** estimated CO2 emissions
- **52,049,343 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3133 |
| 2 | SkyWest Airlines | 2714 |
| 3 | IndiGo | 1646 |
| 4 | EJA | 1340 |
| 5 | American Airlines | 1137 |
| 6 | Southwest Airlines | 1058 |
| 7 | Lufthansa | 933 |
| 8 | ENY | 915 |
| 9 | Vueling | 711 |
| 10 | AXM | 689 |
| 11 | LATAM Airlines | 677 |
| 12 | WIF | 627 |
| 13 | Delta Air Lines | 617 |
| 14 | All Nippon Airways | 601 |
| 15 | AZU | 585 |
| 16 | QLK | 566 |
| 17 | Swiss International | 556 |
| 18 | LXJ | 535 |
| 19 | Alaska Airlines | 513 |
| 20 | easyJet | 481 |
| 21 | EJU | 469 |
| 22 | AEE | 467 |
| 23 | Cathay Pacific | 456 |
| 24 | VIV | 448 |
| 25 | Japan Airlines | 432 |
| 26 | Air France | 423 |
| 27 | AXB | 403 |
| 28 | CXK | 368 |
| 29 | AIQ | 363 |
| 30 | United Airlines | 351 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 58407 |
| 2 | 🇪🇸 ES | 5268 |
| 3 | 🇮🇳 IN | 5165 |
| 4 | 🇦🇺 AU | 4865 |
| 5 | 🇧🇷 BR | 4074 |
| 6 | 🇩🇪 DE | 4041 |
| 7 | 🇮🇹 IT | 3987 |
| 8 | 🇯🇵 JP | 3853 |
| 9 | 🇨🇦 CA | 3639 |
| 10 | 🇬🇧 GB | 3125 |
| 11 | 🇫🇷 FR | 2867 |
| 12 | 🇨🇴 CO | 2679 |
| 13 | 🇲🇽 MX | 2281 |
| 14 | 🇬🇷 GR | 2153 |
| 15 | 🇳🇴 NO | 2024 |
| 16 | 🇨🇭 CH | 1978 |
| 17 | 🇲🇾 MY | 1723 |
| 18 | 🇿🇦 ZA | 1427 |
| 19 | 🇳🇿 NZ | 1326 |
| 20 | 🇹🇷 TR | 1306 |
| 21 | 🇹🇭 TH | 1301 |
| 22 | 🇵🇱 PL | 1211 |
| 23 | 🇵🇭 PH | 1190 |
| 24 | 🇬🇹 GT | 1147 |
| 25 | 🇰🇷 KR | 1141 |
| 26 | 🇲🇦 MA | 864 |
| 27 | 🇲🇴 MO | 852 |
| 28 | 🇲🇪 ME | 773 |
| 29 | 🇳🇱 NL | 756 |
| 30 | 🇧🇸 BS | 611 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1620 |
| 2 | Tokyo International Airport |  | JP | 1294 |
| 3 | Denver International Airport |  | US | 1218 |
| 4 | Indira Gandhi International Airport |  | IN | 1090 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1053 |
| 6 | Frankfurt am Main International Airport |  | DE | 930 |
| 7 | Harry Reid International Airport |  | US | 910 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 874 |
| 10 | Zurich Airport |  | CH | 860 |
| 11 | La Aurora Airport |  | GT | 854 |
| 12 | Macau International Airport |  | MO | 852 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 732 |
| 14 | Chicago O'Hare International Airport |  | US | 705 |
| 15 | Kuala Lumpur International Airport |  | MY | 691 |
| 16 | Madrid Barajas International Airport |  | ES | 684 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 647 |
| 18 | Malpensa International Airport |  | IT | 635 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 632 |
| 20 | Bengaluru International Airport |  | IN | 632 |
| 21 | Salt Lake City International Airport |  | US | 595 |
| 22 | Congonhas Airport |  | BR | 575 |
| 23 | Charlotte/Douglas International Airport |  | US | 574 |
| 24 | Capua Airport |  | IT | 572 |
| 25 | Charles de Gaulle International Airport |  | FR | 567 |
| 26 | Tenerife Norte Airport |  | ES | 550 |
| 27 | Ninoy Aquino International Airport |  | PH | 541 |
| 28 | Daniel K Inouye International Airport |  | US | 534 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 525 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 505 |
| 31 | Barcelona International Airport |  | ES | 503 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 495 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 486 |
| 34 | Vitoria/Foronda Airport |  | ES | 476 |
| 35 | Don Mueang International Airport |  | TH | 458 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 458 |
| 37 | Amsterdam Airport Schiphol |  | NL | 451 |
| 38 | O. R. Tambo International Airport |  | ZA | 448 |
| 39 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 443 |
| 40 | Calgary International Airport |  | CA | 435 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 363 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 266 | 1h 7m | 706 km | 3,238.6 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 257 | 21m | 244 km | 1,082.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 216 | 24m | 225 km | 838.0 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 204 | 28m | 304 km | 1,069.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 202 | 1h 27m | 910 km | 3,169.8 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 180 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 176 | 20m | 165 km | 500.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 173 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 161 | 26m | 275 km | 762.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 161 | 1h 12m | 770 km | 2,138.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 135 | 21m | 99 km | 231.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 119 | 31m | 369 km | 757.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 108 | 20m | 147 km | 273.3 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 107 | 14m | 154 km | 283.5 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 100 | 1h 2m | 695 km | 1,198.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 98 | 58m | 493 km | 833.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 97 | 1h 43m | 1,423 km | 2,380.5 t |
| 26 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 93 | 12m | - | - |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 93 | 23m | 55 km | 88.4 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EZY39DR | easyJet | London Luton Airport (EGGW) | Napoli / Capodichino International Airport (LIRN) | 2026-05-08 05:14 UTC | 2026-05-08 07:36 UTC | 2h 22m |
| ETD6PX | Etihad Airways | General Edward Lawrence Logan International Airport (KBOS) | Queen Alia International Airport (OJAI) | 2026-05-07 22:27 UTC | 2026-05-08 07:35 UTC | 9h 7m |
| ELY002 | ELY | John F Kennedy International Airport (KJFK) | Queen Alia International Airport (OJAI) | 2026-05-07 22:08 UTC | 2026-05-08 07:31 UTC | 9h 22m |
| TRD22 | TRD | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-05-08 07:03 UTC | 2026-05-08 07:17 UTC | 14m |
| AUR202 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-05-08 07:04 UTC | 2026-05-08 07:17 UTC | 13m |
| RGA03 | RGA | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-05-08 06:54 UTC | 2026-05-08 07:13 UTC | 18m |
| QLK1808 | QLK | Adelaide International Airport (YPAD) | Renmark Airport (YREN) | 2026-05-08 06:44 UTC | 2026-05-08 07:08 UTC | 23m |
| JCB02 | JCB | East Midlands Airport (EGNX) | Tatenhill Airfield (EGBM) | 2026-05-08 06:56 UTC | 2026-05-08 07:07 UTC | 11m |
| RSCU330 | RSC | Melbourne Essendon Airport (YMEN) | Mount Beauty Airport (YMBT) | 2026-05-08 04:33 UTC | 2026-05-08 07:06 UTC | 2h 32m |
|  |  | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-08 04:47 UTC | 2026-05-08 07:04 UTC | 2h 16m |
| V632 |  | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-05-08 06:18 UTC | 2026-05-08 07:03 UTC | 44m |
| HBZLW | HBZ | Courchevel Airport (LFLJ) | Muenster Aero Airport (LSPU) | 2026-05-08 05:46 UTC | 2026-05-08 07:03 UTC | 1h 16m |
| WA669 |  | Tamworth Airport (YSTW) | Bathurst Airport (YBTH) | 2026-05-08 06:17 UTC | 2026-05-08 07:02 UTC | 45m |
| GFD98 | GFD | Siegerland Airport (EDGS) | Siegerland Airport (EDGS) | 2026-05-08 06:50 UTC | 2026-05-08 06:56 UTC | 5m |
| WIF1X | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-08 06:43 UTC | 2026-05-08 06:54 UTC | 10m |
| RYR28GH | Ryanair | Copernicus Wrocław Airport (EPWR) | Valencia Airport (LEVC) | 2026-05-08 04:01 UTC | 2026-05-08 06:46 UTC | 2h 44m |
| RYR2HU | Ryanair | Dublin Airport (EIDW) | La Roche-sur-Yon Airport (LFRI) | 2026-05-08 05:38 UTC | 2026-05-08 06:42 UTC | 1h 3m |
| TVF44LU | TVF | Toulon-Hyeres Airport (LFTH) | Paris-Orly Airport (LFPO) | 2026-05-08 05:32 UTC | 2026-05-08 06:41 UTC | 1h 9m |
| SEH2VS | SEH | Mytilene International Airport (LGMT) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-08 05:50 UTC | 2026-05-08 06:41 UTC | 51m |
| WMT5QD | WMT | Henri Coanda International Airport (LROP) | Bilbao Airport (LEBB) | 2026-05-08 03:22 UTC | 2026-05-08 06:40 UTC | 3h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
