# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_11:45:56_UTC-green)

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

**Latest saved flight:** 2026-05-03 11:45:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 11:45:56 UTC

- **65,578** saved flights
- **24,833** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,578** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **805,252.7 tonnes** estimated CO2 emissions
- **46,681,318 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2788 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1523 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1011 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 846 |
| 8 | ENY | 806 |
| 9 | Vueling | 649 |
| 10 | AXM | 643 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 574 |
| 13 | Delta Air Lines | 547 |
| 14 | WIF | 543 |
| 15 | AZU | 527 |
| 16 | QLK | 513 |
| 17 | Swiss International | 504 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 448 |
| 20 | easyJet | 436 |
| 21 | AEE | 427 |
| 22 | EJU | 423 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 394 |
| 25 | Japan Airlines | 388 |
| 26 | Air France | 383 |
| 27 | AXB | 366 |
| 28 | AIQ | 338 |
| 29 | CXK | 334 |
| 30 | GLO | 318 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51721 |
| 2 | 🇪🇸 ES | 4813 |
| 3 | 🇮🇳 IN | 4784 |
| 4 | 🇦🇺 AU | 4406 |
| 5 | 🇧🇷 BR | 3678 |
| 6 | 🇩🇪 DE | 3671 |
| 7 | 🇯🇵 JP | 3593 |
| 8 | 🇮🇹 IT | 3573 |
| 9 | 🇨🇦 CA | 3204 |
| 10 | 🇬🇧 GB | 2835 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2595 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1967 |
| 15 | 🇨🇭 CH | 1843 |
| 16 | 🇳🇴 NO | 1779 |
| 17 | 🇲🇾 MY | 1580 |
| 18 | 🇿🇦 ZA | 1342 |
| 19 | 🇳🇿 NZ | 1222 |
| 20 | 🇹🇭 TH | 1205 |
| 21 | 🇹🇷 TR | 1186 |
| 22 | 🇵🇭 PH | 1104 |
| 23 | 🇵🇱 PL | 1075 |
| 24 | 🇰🇷 KR | 1072 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 805 |
| 27 | 🇲🇴 MO | 739 |
| 28 | 🇲🇪 ME | 713 |
| 29 | 🇳🇱 NL | 697 |
| 30 | 🇮🇩 ID | 565 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1211 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 999 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 958 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 843 |
| 8 | Guaymaral Airport |  | CO | 840 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 781 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 739 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Kuala Lumpur International Airport |  | MY | 628 |
| 15 | Madrid Barajas International Airport |  | ES | 625 |
| 16 | Chicago O'Hare International Airport |  | US | 623 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 583 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 579 |
| 20 | Malpensa International Airport |  | IT | 564 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 524 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 515 |
| 25 | Charles de Gaulle International Airport |  | FR | 512 |
| 26 | Ninoy Aquino International Airport |  | PH | 502 |
| 27 | Capua Airport |  | IT | 492 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 482 |
| 29 | Daniel K Inouye International Airport |  | US | 481 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 448 |
| 32 | Vitoria/Foronda Airport |  | ES | 439 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 437 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 436 |
| 35 | O. R. Tambo International Airport |  | ZA | 423 |
| 36 | Don Mueang International Airport |  | TH | 421 |
| 37 | Amsterdam Airport Schiphol |  | NL | 409 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 222 | 21m | 244 km | 934.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 203 | 24m | 225 km | 787.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 192 | 1h 27m | 910 km | 3,012.9 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 191 | 28m | 304 km | 1,001.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 163 | 20m | 165 km | 463.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 154 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 149 | 26m | 275 km | 706.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 146 | 1h 11m | 770 km | 1,939.5 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 123 | 44m | 452 km | 958.6 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 107 | 20m | 250 km | 462.2 t |
| 17 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 101 | 27m | 215 km | 374.1 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 98 | 20m | 147 km | 248.0 t |
| 21 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 92 | 57m | 493 km | 782.7 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 23 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 90 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 88 | 14m | 154 km | 233.2 t |
| 28 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DKKSU | DKK | Schanis Airport (LSZX) | Bad Ragaz Airport (LSZE) | 2026-05-03 10:08 UTC | 2026-05-03 11:45 UTC | 1h 37m |
| CXK550 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-03 11:21 UTC | 2026-05-03 11:43 UTC | 21m |
| CXK435 | CXK | Gold Hill Airport (NC25) | Mid-Carolina Regional Airport (KRUQ) | 2026-05-03 11:21 UTC | 2026-05-03 11:32 UTC | 11m |
| AIZ364 | AIZ | Dolna Banya Airport (LBDB) | Paphos International Airport (LCPH) | 2026-05-03 10:02 UTC | 2026-05-03 11:27 UTC | 1h 24m |
| CSN3038 | China Southern | Soekarno-Hatta International Airport (WIII) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-05-03 06:54 UTC | 2026-05-03 11:23 UTC | 4h 29m |
| CXK528 | CXK | Akron-Canton Regional Airport (KCAK) | Akron Fulton International Airport (KAKR) | 2026-05-03 10:32 UTC | 2026-05-03 11:22 UTC | 49m |
| GPD437 | GPD | Nantucket Memorial Airport (KACK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-03 10:55 UTC | 2026-05-03 11:20 UTC | 24m |
| AM266 |  | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-05-03 10:49 UTC | 2026-05-03 11:14 UTC | 25m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-03 11:00 UTC | 2026-05-03 11:14 UTC | 13m |
| GAWGB | GAW | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-05-03 11:08 UTC | 2026-05-03 11:13 UTC | 4m |
| ABF9 | ABF | Vigo Airport (LEVX) | A Coruna Airport (LECO) | 2026-05-03 10:51 UTC | 2026-05-03 11:12 UTC | 21m |
| ABY1830 | ABY | Sharjah International Airport (OMSJ) | Simara Airport (VNSI) | 2026-05-03 07:29 UTC | 2026-05-03 11:09 UTC | 3h 39m |
| AIQ3925 | AIQ | Don Mueang International Airport (VTBD) | Tak Airport (VTPT) | 2026-05-03 10:34 UTC | 2026-05-03 11:05 UTC | 31m |
| N111P |  | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-03 09:17 UTC | 2026-05-03 11:05 UTC | 1h 47m |
|  |  | Sydney Kingsford Smith International Airport (YSSY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-03 10:31 UTC | 2026-05-03 11:02 UTC | 31m |
| BTN776 | BTN | Bagdogra Airport (VEBD) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-03 10:19 UTC | 2026-05-03 11:01 UTC | 42m |
| RYR1512 | Ryanair | Perugia / San Egidio Airport (LIRZ) | Decimomannu Airport (LIED) | 2026-05-03 10:17 UTC | 2026-05-03 10:58 UTC | 41m |
| RYR5YZ | Ryanair | Bristol International Airport (EGGD) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-03 08:43 UTC | 2026-05-03 10:53 UTC | 2h 9m |
| IGO411Y | IndiGo | Juhu Aerodrome (VAJJ) | Baglung Airport (VNBL) | 2026-05-03 09:15 UTC | 2026-05-03 10:52 UTC | 1h 36m |
| WIF77P | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-05-03 10:01 UTC | 2026-05-03 10:52 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
