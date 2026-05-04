# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_08:54:28_UTC-green)

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

**Latest saved flight:** 2026-05-04 08:54:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 08:54:28 UTC

- **67,320** saved flights
- **25,347** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,320** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **828,006.8 tonnes** estimated CO2 emissions
- **48,000,393 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2873 |
| 2 | SkyWest Airlines | 2488 |
| 3 | IndiGo | 1560 |
| 4 | EJA | 1202 |
| 5 | American Airlines | 1041 |
| 6 | Southwest Airlines | 946 |
| 7 | Lufthansa | 861 |
| 8 | ENY | 829 |
| 9 | Vueling | 664 |
| 10 | AXM | 655 |
| 11 | LATAM Airlines | 626 |
| 12 | All Nippon Airways | 577 |
| 13 | Delta Air Lines | 564 |
| 14 | WIF | 561 |
| 15 | AZU | 543 |
| 16 | QLK | 523 |
| 17 | Swiss International | 517 |
| 18 | LXJ | 489 |
| 19 | Alaska Airlines | 457 |
| 20 | easyJet | 450 |
| 21 | AEE | 441 |
| 22 | EJU | 434 |
| 23 | VIV | 419 |
| 24 | Cathay Pacific | 409 |
| 25 | Japan Airlines | 396 |
| 26 | Air France | 394 |
| 27 | AXB | 381 |
| 28 | AIQ | 343 |
| 29 | CXK | 342 |
| 30 | MXY | 328 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53177 |
| 2 | 🇪🇸 ES | 4934 |
| 3 | 🇮🇳 IN | 4915 |
| 4 | 🇦🇺 AU | 4486 |
| 5 | 🇧🇷 BR | 3774 |
| 6 | 🇩🇪 DE | 3758 |
| 7 | 🇮🇹 IT | 3677 |
| 8 | 🇯🇵 JP | 3642 |
| 9 | 🇨🇦 CA | 3294 |
| 10 | 🇬🇧 GB | 2909 |
| 11 | 🇫🇷 FR | 2667 |
| 12 | 🇨🇴 CO | 2651 |
| 13 | 🇲🇽 MX | 2137 |
| 14 | 🇬🇷 GR | 2018 |
| 15 | 🇨🇭 CH | 1880 |
| 16 | 🇳🇴 NO | 1830 |
| 17 | 🇲🇾 MY | 1621 |
| 18 | 🇿🇦 ZA | 1361 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1224 |
| 21 | 🇹🇷 TR | 1207 |
| 22 | 🇵🇭 PH | 1130 |
| 23 | 🇵🇱 PL | 1100 |
| 24 | 🇬🇹 GT | 1091 |
| 25 | 🇰🇷 KR | 1088 |
| 26 | 🇲🇦 MA | 821 |
| 27 | 🇲🇴 MO | 766 |
| 28 | 🇲🇪 ME | 731 |
| 29 | 🇳🇱 NL | 709 |
| 30 | 🇮🇩 ID | 579 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1482 |
| 2 | Tokyo International Airport |  | JP | 1226 |
| 3 | Denver International Airport |  | US | 1109 |
| 4 | Indira Gandhi International Airport |  | IN | 1026 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 984 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 868 |
| 8 | Guaymaral Airport |  | CO | 846 |
| 9 | Harry Reid International Airport |  | US | 839 |
| 10 | La Aurora Airport |  | GT | 810 |
| 11 | Zurich Airport |  | CH | 797 |
| 12 | Macau International Airport |  | MO | 766 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 663 |
| 14 | Kuala Lumpur International Airport |  | MY | 648 |
| 15 | Chicago O'Hare International Airport |  | US | 645 |
| 16 | Madrid Barajas International Airport |  | ES | 644 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 600 |
| 18 | Bengaluru International Airport |  | IN | 600 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 20 | Malpensa International Airport |  | IT | 584 |
| 21 | Congonhas Airport |  | BR | 541 |
| 22 | Salt Lake City International Airport |  | US | 536 |
| 23 | Tenerife Norte Airport |  | ES | 533 |
| 24 | Charlotte/Douglas International Airport |  | US | 529 |
| 25 | Charles de Gaulle International Airport |  | FR | 529 |
| 26 | Ninoy Aquino International Airport |  | PH | 514 |
| 27 | Capua Airport |  | IT | 509 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 494 |
| 29 | Daniel K Inouye International Airport |  | US | 490 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 473 |
| 31 | Barcelona International Airport |  | ES | 465 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 453 |
| 33 | Vitoria/Foronda Airport |  | ES | 448 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 445 |
| 35 | O. R. Tambo International Airport |  | ZA | 429 |
| 36 | Don Mueang International Airport |  | TH | 428 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 423 |
| 38 | Amsterdam Airport Schiphol |  | NL | 416 |
| 39 | Reno/Tahoe International Airport |  | US | 405 |
| 40 | Calgary International Airport |  | CA | 392 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 349 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 229 | 21m | 244 km | 964.3 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 193 | 1h 27m | 910 km | 3,028.6 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 168 | 20m | 165 km | 477.9 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 168 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 161 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 151 | 26m | 275 km | 715.5 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 148 | 1h 12m | 770 km | 1,966.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 112 | 31m | 369 km | 712.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 112 | 27m | 152 km | 292.7 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 103 | 27m | 215 km | 381.5 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 100 | 20m | 147 km | 253.1 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 94 | 57m | 493 km | 799.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 94 | 14m | 154 km | 249.1 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 2m | 695 km | 1,102.8 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 91 | 1h 53m | 1,304 km | 2,047.3 t |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 90 | 1h 43m | 1,423 km | 2,208.7 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-05-04 08:21 UTC | 2026-05-04 08:54 UTC | 32m |
| SJV651 | SJV | Soekarno-Hatta International Airport (WIII) | Halim Perdanakusuma International Airport (WIHH) | 2026-05-04 08:30 UTC | 2026-05-04 08:44 UTC | 14m |
| GFLIA | GFL | Fife Airport (EGPJ) | Fife Airport (EGPJ) | 2026-05-04 08:22 UTC | 2026-05-04 08:33 UTC | 10m |
| FUU231A | FUU | Izgrev Airport (LBWV) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-04 07:11 UTC | 2026-05-04 08:32 UTC | 1h 20m |
| CPA391 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-04 01:23 UTC | 2026-05-04 08:27 UTC | 7h 3m |
| A7GQD |  | Doha International Airport (OTBD) | Al Khawr Airport (OTBK) | 2026-05-04 07:59 UTC | 2026-05-04 08:27 UTC | 28m |
| QTR8400 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-05-04 01:27 UTC | 2026-05-04 08:20 UTC | 6h 52m |
| LSI191 | LSI | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-05-03 21:05 UTC | 2026-05-04 08:19 UTC | 11h 13m |
| SEH6HS | SEH | Dolna Banya Airport (LBDB) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-04 06:53 UTC | 2026-05-04 08:16 UTC | 1h 22m |
| SAN21 | SAN | Emmen Airport (LSME) | Samedan Airport (LSZS) | 2026-05-04 07:57 UTC | 2026-05-04 08:12 UTC | 15m |
| N37CJ |  | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-04 07:30 UTC | 2026-05-04 08:12 UTC | 42m |
| SUI721 | SUI | Emmen Airport (LSME) | Nuremberg Airport (EDDN) | 2026-05-04 06:57 UTC | 2026-05-04 08:11 UTC | 1h 13m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-05-04 07:46 UTC | 2026-05-04 08:03 UTC | 17m |
| NOZ44A | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-05-04 07:19 UTC | 2026-05-04 08:03 UTC | 43m |
| VIR449 | Virgin Atlantic | London Heathrow Airport (EGLL) | Vereeniging Airport (FAVV) | 2026-05-03 21:48 UTC | 2026-05-04 08:02 UTC | 10h 14m |
| SAS336 | Scandinavian Airlines | Oslo Gardermoen Airport (ENGM) | Trondheim Airport Vaernes (ENVA) | 2026-05-04 07:21 UTC | 2026-05-04 08:02 UTC | 41m |
| 9HFAE |  | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-05-04 07:08 UTC | 2026-05-04 08:02 UTC | 53m |
| EZY25RN | easyJet | London Gatwick Airport (EGKK) | Lesce Bled Glider Airport (LJBL) | 2026-05-04 06:15 UTC | 2026-05-04 08:01 UTC | 1h 46m |
| VOE4MT | VOE | Barcelona International Airport (LEBL) | Vitoria/Foronda Airport (LEVT) | 2026-05-04 07:11 UTC | 2026-05-04 07:53 UTC | 41m |
| VOE9TX | VOE | Sevilla Airport (LEZL) | La Morgal Airport (LEMR) | 2026-05-04 06:56 UTC | 2026-05-04 07:52 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
