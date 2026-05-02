# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_07:40:45_UTC-green)

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

**Latest saved flight:** 2026-05-02 07:40:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-02 07:40:45 UTC

- **63,593** saved flights
- **24,282** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **63,593** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **777,544.0 tonnes** estimated CO2 emissions
- **45,075,013 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2662 |
| 2 | SkyWest Airlines | 2365 |
| 3 | IndiGo | 1453 |
| 4 | EJA | 1144 |
| 5 | American Airlines | 991 |
| 6 | Southwest Airlines | 904 |
| 7 | Lufthansa | 812 |
| 8 | ENY | 784 |
| 9 | Vueling | 621 |
| 10 | AXM | 617 |
| 11 | LATAM Airlines | 594 |
| 12 | All Nippon Airways | 559 |
| 13 | WIF | 532 |
| 14 | Delta Air Lines | 530 |
| 15 | AZU | 517 |
| 16 | QLK | 502 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 455 |
| 19 | Alaska Airlines | 439 |
| 20 | easyJet | 411 |
| 21 | AEE | 410 |
| 22 | EJU | 406 |
| 23 | VIV | 401 |
| 24 | Cathay Pacific | 385 |
| 25 | Japan Airlines | 371 |
| 26 | Air France | 364 |
| 27 | AXB | 351 |
| 28 | AIQ | 323 |
| 29 | CXK | 320 |
| 30 | GLO | 310 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 50517 |
| 2 | 🇪🇸 ES | 4584 |
| 3 | 🇮🇳 IN | 4581 |
| 4 | 🇦🇺 AU | 4335 |
| 5 | 🇧🇷 BR | 3593 |
| 6 | 🇩🇪 DE | 3519 |
| 7 | 🇯🇵 JP | 3464 |
| 8 | 🇮🇹 IT | 3440 |
| 9 | 🇨🇦 CA | 3134 |
| 10 | 🇬🇧 GB | 2696 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2488 |
| 13 | 🇲🇽 MX | 2021 |
| 14 | 🇬🇷 GR | 1884 |
| 15 | 🇨🇭 CH | 1760 |
| 16 | 🇳🇴 NO | 1738 |
| 17 | 🇲🇾 MY | 1513 |
| 18 | 🇿🇦 ZA | 1286 |
| 19 | 🇳🇿 NZ | 1205 |
| 20 | 🇹🇭 TH | 1152 |
| 21 | 🇹🇷 TR | 1115 |
| 22 | 🇵🇭 PH | 1077 |
| 23 | 🇰🇷 KR | 1030 |
| 24 | 🇵🇱 PL | 1025 |
| 25 | 🇬🇹 GT | 992 |
| 26 | 🇲🇦 MA | 776 |
| 27 | 🇲🇴 MO | 716 |
| 28 | 🇲🇪 ME | 687 |
| 29 | 🇳🇱 NL | 664 |
| 30 | 🇮🇩 ID | 539 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1404 |
| 2 | Tokyo International Airport |  | JP | 1170 |
| 3 | Denver International Airport |  | US | 1047 |
| 4 | Indira Gandhi International Airport |  | IN | 965 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 920 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 813 |
| 9 | Harry Reid International Airport |  | US | 807 |
| 10 | Zurich Airport |  | CH | 749 |
| 11 | La Aurora Airport |  | GT | 743 |
| 12 | Macau International Airport |  | MO | 716 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 626 |
| 14 | Chicago O'Hare International Airport |  | US | 607 |
| 15 | Kuala Lumpur International Airport |  | MY | 601 |
| 16 | Madrid Barajas International Airport |  | ES | 599 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 575 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 563 |
| 19 | Bengaluru International Airport |  | IN | 554 |
| 20 | Malpensa International Airport |  | IT | 543 |
| 21 | Congonhas Airport |  | BR | 520 |
| 22 | Charlotte/Douglas International Airport |  | US | 502 |
| 23 | Salt Lake City International Airport |  | US | 502 |
| 24 | Charles de Gaulle International Airport |  | FR | 491 |
| 25 | Ninoy Aquino International Airport |  | PH | 490 |
| 26 | Tenerife Norte Airport |  | ES | 488 |
| 27 | Daniel K Inouye International Airport |  | US | 472 |
| 28 | Capua Airport |  | IT | 468 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 462 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 459 |
| 31 | Barcelona International Airport |  | ES | 429 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 425 |
| 33 | Vitoria/Foronda Airport |  | ES | 419 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 416 |
| 35 | O. R. Tambo International Airport |  | ZA | 407 |
| 36 | Don Mueang International Airport |  | TH | 396 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 396 |
| 38 | Reno/Tahoe International Airport |  | US | 394 |
| 39 | Amsterdam Airport Schiphol |  | NL | 394 |
| 40 | Calgary International Airport |  | CA | 378 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 257 | 1h 7m | 706 km | 3,129.0 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 216 | 21m | 244 km | 909.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 199 | 24m | 225 km | 772.0 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 187 | 1h 27m | 910 km | 2,934.5 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 183 | 28m | 304 km | 959.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 157 | 20m | 165 km | 446.6 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 157 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 149 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 137 | 1h 12m | 770 km | 1,819.9 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 117 | 44m | 452 km | 911.8 t |
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
| 24 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 53m | 1,304 km | 1,957.3 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 86 | 57m | 493 km | 731.7 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 85 | 23m | 55 km | 80.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 82 | 1h 43m | 1,423 km | 2,012.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 81 | 1h 20m | 961 km | 1,342.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HSDZT | HSD | U-Tapao International Airport (VTBU) | U-Tapao International Airport (VTBU) | 2026-05-02 07:06 UTC | 2026-05-02 07:40 UTC | 33m |
| SRG199 | SRG | Oban Airport (EGEO) | Glasgow International Airport (EGPF) | 2026-05-02 07:14 UTC | 2026-05-02 07:35 UTC | 20m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-01 19:02 UTC | 2026-05-02 07:04 UTC | 12h 2m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-05-02 06:56 UTC | 2026-05-02 07:00 UTC | 4m |
| RYR9BR | Ryanair | Stockholm-Arlanda Airport (ESSA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-02 05:20 UTC | 2026-05-02 06:58 UTC | 1h 38m |
| ITY218 | ITY | Linate Airport (LIML) | London City Airport (EGLC) | 2026-05-02 05:27 UTC | 2026-05-02 06:52 UTC | 1h 25m |
| BBC601 | BBC | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-05-02 06:29 UTC | 2026-05-02 06:49 UTC | 19m |
| IGO291 | IndiGo | Indira Gandhi International Airport (VIDP) | Lengpui Airport (VELP) | 2026-05-02 04:58 UTC | 2026-05-02 06:47 UTC | 1h 49m |
| AUA30P | Austrian Airlines | Amsterdam Airport Schiphol (EHAM) | Vienna International Airport (LOWW) | 2026-05-02 05:13 UTC | 2026-05-02 06:44 UTC | 1h 31m |
| LGL851W | LGL | Luxembourg-Findel International Airport (ELLX) | Voslau Airport (LOAV) | 2026-05-02 05:10 UTC | 2026-05-02 06:44 UTC | 1h 33m |
| TRA97X | TRA | Rotterdam Airport (EHRD) | Ajdovscina Airport (LJAJ) | 2026-05-02 05:15 UTC | 2026-05-02 06:44 UTC | 1h 28m |
| IGO7304 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-05-02 05:28 UTC | 2026-05-02 06:42 UTC | 1h 14m |
| DAL228 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Charles de Gaulle International Airport (LFPG) | 2026-05-01 23:03 UTC | 2026-05-02 06:42 UTC | 7h 38m |
| LOG32MW | LOG | Glasgow International Airport (EGPF) | XPLO (XPLO) | 2026-05-02 06:18 UTC | 2026-05-02 06:41 UTC | 22m |
| UBG147 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-05-02 06:05 UTC | 2026-05-02 06:38 UTC | 33m |
| VLG1DP | Vueling | Barcelona International Airport (LEBL) | Pamplona Airport (LEPP) | 2026-05-02 06:00 UTC | 2026-05-02 06:35 UTC | 35m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Simara Airport (VNSI) | 2026-05-02 03:28 UTC | 2026-05-02 06:34 UTC | 3h 5m |
| CYP31A | CYP | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-02 04:54 UTC | 2026-05-02 06:31 UTC | 1h 37m |
| VOE76RL | VOE | Nantes Atlantique Airport (LFRS) | Menorca Airport (LEMH) | 2026-05-02 05:15 UTC | 2026-05-02 06:31 UTC | 1h 16m |
| GTI4355 | GTI | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-05-01 19:09 UTC | 2026-05-02 06:29 UTC | 11h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
