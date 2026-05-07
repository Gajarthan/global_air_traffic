# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_09:44:51_UTC-green)

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

**Latest saved flight:** 2026-05-07 09:44:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-07 09:44:51 UTC

- **71,821** saved flights
- **26,675** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,821** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **885,959.8 tonnes** estimated CO2 emissions
- **51,359,987 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3090 |
| 2 | SkyWest Airlines | 2671 |
| 3 | IndiGo | 1627 |
| 4 | EJA | 1314 |
| 5 | American Airlines | 1124 |
| 6 | Southwest Airlines | 1045 |
| 7 | Lufthansa | 923 |
| 8 | ENY | 900 |
| 9 | Vueling | 703 |
| 10 | AXM | 688 |
| 11 | LATAM Airlines | 668 |
| 12 | WIF | 615 |
| 13 | Delta Air Lines | 602 |
| 14 | All Nippon Airways | 599 |
| 15 | AZU | 580 |
| 16 | QLK | 554 |
| 17 | Swiss International | 551 |
| 18 | LXJ | 521 |
| 19 | Alaska Airlines | 507 |
| 20 | easyJet | 477 |
| 21 | AEE | 461 |
| 22 | EJU | 460 |
| 23 | Cathay Pacific | 448 |
| 24 | VIV | 445 |
| 25 | Japan Airlines | 425 |
| 26 | Air France | 420 |
| 27 | AXB | 399 |
| 28 | AIQ | 359 |
| 29 | CXK | 357 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 57372 |
| 2 | 🇪🇸 ES | 5216 |
| 3 | 🇮🇳 IN | 5114 |
| 4 | 🇦🇺 AU | 4797 |
| 5 | 🇧🇷 BR | 4020 |
| 6 | 🇩🇪 DE | 3993 |
| 7 | 🇮🇹 IT | 3938 |
| 8 | 🇯🇵 JP | 3827 |
| 9 | 🇨🇦 CA | 3567 |
| 10 | 🇬🇧 GB | 3100 |
| 11 | 🇫🇷 FR | 2832 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2264 |
| 14 | 🇬🇷 GR | 2129 |
| 15 | 🇳🇴 NO | 1977 |
| 16 | 🇨🇭 CH | 1957 |
| 17 | 🇲🇾 MY | 1713 |
| 18 | 🇿🇦 ZA | 1420 |
| 19 | 🇳🇿 NZ | 1320 |
| 20 | 🇹🇭 TH | 1293 |
| 21 | 🇹🇷 TR | 1292 |
| 22 | 🇵🇱 PL | 1195 |
| 23 | 🇵🇭 PH | 1174 |
| 24 | 🇬🇹 GT | 1140 |
| 25 | 🇰🇷 KR | 1135 |
| 26 | 🇲🇦 MA | 854 |
| 27 | 🇲🇴 MO | 842 |
| 28 | 🇲🇪 ME | 768 |
| 29 | 🇳🇱 NL | 747 |
| 30 | 🇧🇸 BS | 605 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1602 |
| 2 | Tokyo International Airport |  | JP | 1287 |
| 3 | Denver International Airport |  | US | 1200 |
| 4 | Indira Gandhi International Airport |  | IN | 1077 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1041 |
| 6 | Frankfurt am Main International Airport |  | DE | 917 |
| 7 | Harry Reid International Airport |  | US | 898 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | Zurich Airport |  | CH | 851 |
| 11 | La Aurora Airport |  | GT | 849 |
| 12 | Macau International Airport |  | MO | 842 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 724 |
| 14 | Chicago O'Hare International Airport |  | US | 699 |
| 15 | Kuala Lumpur International Airport |  | MY | 688 |
| 16 | Madrid Barajas International Airport |  | ES | 679 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 641 |
| 18 | Malpensa International Airport |  | IT | 626 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 624 |
| 20 | Bengaluru International Airport |  | IN | 623 |
| 21 | Salt Lake City International Airport |  | US | 582 |
| 22 | Congonhas Airport |  | BR | 570 |
| 23 | Charlotte/Douglas International Airport |  | US | 565 |
| 24 | Capua Airport |  | IT | 563 |
| 25 | Charles de Gaulle International Airport |  | FR | 562 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 534 |
| 28 | Daniel K Inouye International Airport |  | US | 530 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 518 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 503 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 491 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 480 |
| 34 | Vitoria/Foronda Airport |  | ES | 473 |
| 35 | Don Mueang International Airport |  | TH | 454 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 452 |
| 37 | Amsterdam Airport Schiphol |  | NL | 445 |
| 38 | O. R. Tambo International Airport |  | ZA | 444 |
| 39 | Calgary International Airport |  | CA | 431 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 265 | 1h 7m | 706 km | 3,226.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 253 | 21m | 244 km | 1,065.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 211 | 24m | 225 km | 818.6 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 201 | 28m | 304 km | 1,053.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 200 | 1h 27m | 910 km | 3,138.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 179 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 175 | 20m | 165 km | 497.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 159 | 1h 12m | 770 km | 2,112.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 134 | 21m | 99 km | 229.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 133 | 44m | 452 km | 1,036.5 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 105 | 14m | 154 km | 278.2 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 96 | 1h 43m | 1,423 km | 2,356.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-07 09:34 UTC | 2026-05-07 09:44 UTC | 10m |
| ICV9263 | ICV | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-05-06 22:59 UTC | 2026-05-07 09:44 UTC | 10h 45m |
| AUA801C | Austrian Airlines | Vienna International Airport (LOWW) | Eleftherios Venizelos International Airport (LGAV) | 2026-05-07 07:48 UTC | 2026-05-07 09:38 UTC | 1h 50m |
| IAM2840 | IAM | Pratica Di Mare Airport (LIRE) | Olbia / Costa Smeralda Airport (LIEO) | 2026-05-07 09:00 UTC | 2026-05-07 09:34 UTC | 33m |
| FKH8011 | FKH | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-06 07:01 UTC | 2026-05-07 09:31 UTC | 26h 30m |
| CKS703 | CKS | Ben Gurion International Airport (LLBG) | Zhuhai Airport (ZGSD) | 2026-05-06 20:33 UTC | 2026-05-07 09:30 UTC | 12h 56m |
| KNG51 | KNG | RNZAF Base Ohakea (NZOH) | RNZAF Base Ohakea (NZOH) | 2026-05-07 07:32 UTC | 2026-05-07 09:30 UTC | 1h 57m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-05-06 22:03 UTC | 2026-05-07 09:28 UTC | 11h 24m |
| NAK317T | NAK | Annecy-Haute-Savoie-Mont Blanc Airport (LFLP) | Lyon-Bron Airport (LFLY) | 2026-05-07 08:59 UTC | 2026-05-07 09:26 UTC | 27m |
| GKWAK | GKW | Bristol International Airport (EGGD) | Bristol International Airport (EGGD) | 2026-05-07 09:03 UTC | 2026-05-07 09:25 UTC | 21m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-06 21:37 UTC | 2026-05-07 09:21 UTC | 11h 43m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-05-07 09:01 UTC | 2026-05-07 09:11 UTC | 10m |
| KLH71 | KLH | Gaziemir Airport (LTBK) | Karain Airport (LTXE) | 2026-05-07 08:33 UTC | 2026-05-07 09:11 UTC | 37m |
| WZZ442 | Wizz Air | Paris-Orly Airport (LFPO) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-05-07 07:15 UTC | 2026-05-07 09:06 UTC | 1h 50m |
| WIF1B | WIF | Bergen Airport Flesland (ENBR) | Haugesund Airport (ENHD) | 2026-05-07 08:48 UTC | 2026-05-07 09:04 UTC | 16m |
| WZZ1628 | Wizz Air | London Luton Airport (EGGW) | Khrabrovo Airport (UMKK) | 2026-05-07 07:15 UTC | 2026-05-07 09:04 UTC | 1h 49m |
| H125V |  | Marseille Provence Airport (LFML) | Berre La Fare Airport (LFNR) | 2026-05-07 08:59 UTC | 2026-05-07 09:04 UTC | 4m |
| RYR8XK | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Crotone Airport (LIBC) | 2026-05-07 07:56 UTC | 2026-05-07 09:02 UTC | 1h 5m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-06 21:46 UTC | 2026-05-07 09:00 UTC | 11h 14m |
| WIF6F | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-05-07 08:43 UTC | 2026-05-07 09:00 UTC | 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
