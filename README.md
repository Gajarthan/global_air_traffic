# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_12:54:57_UTC-green)

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

**Latest saved flight:** 2026-06-01 12:54:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-01 12:54:57 UTC

- **100,280** saved flights
- **35,616** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **100,280** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,227,791.3 tonnes** estimated CO2 emissions
- **71,176,308 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4153 |
| 2 | SkyWest Airlines | 3757 |
| 3 | IndiGo | 2027 |
| 4 | EJA | 1915 |
| 5 | American Airlines | 1625 |
| 6 | Southwest Airlines | 1516 |
| 7 | ENY | 1248 |
| 8 | Delta Air Lines | 1179 |
| 9 | Lufthansa | 1176 |
| 10 | Vueling | 939 |
| 11 | LATAM Airlines | 893 |
| 12 | WIF | 878 |
| 13 | AXM | 864 |
| 14 | AZU | 808 |
| 15 | LXJ | 760 |
| 16 | Swiss International | 732 |
| 17 | All Nippon Airways | 714 |
| 18 | Alaska Airlines | 701 |
| 19 | QLK | 676 |
| 20 | easyJet | 655 |
| 21 | EJU | 633 |
| 22 | Cathay Pacific | 596 |
| 23 | AEE | 588 |
| 24 | VIV | 581 |
| 25 | Air France | 580 |
| 26 | United Airlines | 561 |
| 27 | CXK | 540 |
| 28 | MXY | 536 |
| 29 | Japan Airlines | 506 |
| 30 | AXB | 497 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 83928 |
| 2 | 🇪🇸 ES | 6958 |
| 3 | 🇮🇳 IN | 6397 |
| 4 | 🇦🇺 AU | 6054 |
| 5 | 🇧🇷 BR | 5486 |
| 6 | 🇩🇪 DE | 5442 |
| 7 | 🇮🇹 IT | 5359 |
| 8 | 🇨🇦 CA | 5145 |
| 9 | 🇯🇵 JP | 4663 |
| 10 | 🇬🇧 GB | 4274 |
| 11 | 🇫🇷 FR | 4016 |
| 12 | 🇨🇴 CO | 3493 |
| 13 | 🇲🇽 MX | 3041 |
| 14 | 🇬🇷 GR | 2868 |
| 15 | 🇳🇴 NO | 2782 |
| 16 | 🇨🇭 CH | 2597 |
| 17 | 🇲🇾 MY | 2197 |
| 18 | 🇹🇷 TR | 1907 |
| 19 | 🇿🇦 ZA | 1753 |
| 20 | 🇳🇿 NZ | 1677 |
| 21 | 🇹🇭 TH | 1665 |
| 22 | 🇰🇷 KR | 1621 |
| 23 | 🇵🇱 PL | 1611 |
| 24 | 🇬🇹 GT | 1489 |
| 25 | 🇵🇭 PH | 1465 |
| 26 | 🇲🇦 MA | 1126 |
| 27 | 🇲🇴 MO | 1058 |
| 28 | 🇳🇱 NL | 1003 |
| 29 | 🇲🇪 ME | 960 |
| 30 | 🇭🇷 HR | 889 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2190 |
| 2 | Denver International Airport |  | US | 1719 |
| 3 | Tokyo International Airport |  | JP | 1546 |
| 4 | Indira Gandhi International Airport |  | IN | 1391 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1294 |
| 6 | Harry Reid International Airport |  | US | 1279 |
| 7 | Guaymaral Airport |  | CO | 1260 |
| 8 | Frankfurt am Main International Airport |  | DE | 1180 |
| 9 | Zurich Airport |  | CH | 1151 |
| 10 | La Aurora Airport |  | GT | 1145 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1084 |
| 12 | El Dorado International Airport |  | CO | 1074 |
| 13 | Macau International Airport |  | MO | 1058 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1020 |
| 15 | Chicago O'Hare International Airport |  | US | 1005 |
| 16 | Madrid Barajas International Airport |  | ES | 875 |
| 17 | Kuala Lumpur International Airport |  | MY | 868 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 865 |
| 19 | Salt Lake City International Airport |  | US | 848 |
| 20 | Capua Airport |  | IT | 832 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 781 |
| 22 | Charlotte/Douglas International Airport |  | US | 779 |
| 23 | Charles de Gaulle International Airport |  | FR | 770 |
| 24 | Bengaluru International Airport |  | IN | 767 |
| 25 | Malpensa International Airport |  | IT | 766 |
| 26 | Congonhas Airport |  | BR | 764 |
| 27 | Daniel K Inouye International Airport |  | US | 695 |
| 28 | Tenerife Norte Airport |  | ES | 691 |
| 29 | Ninoy Aquino International Airport |  | PH | 669 |
| 30 | Barcelona International Airport |  | ES | 664 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 656 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 654 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 639 |
| 34 | Amsterdam Airport Schiphol |  | NL | 619 |
| 35 | Vitoria/Foronda Airport |  | ES | 611 |
| 36 | Don Mueang International Airport |  | TH | 609 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 587 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 573 |
| 40 | Seattle-Tacoma International Airport |  | US | 573 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 519 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 365 | 21m | 244 km | 1,536.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 269 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 264 | 24m | 225 km | 1,024.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 256 | 14m | 114 km | 502.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 246 | 1h 26m | 910 km | 3,860.3 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 243 | 28m | 304 km | 1,273.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 229 | 1h 10m | 770 km | 3,042.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 210 | 19m | 165 km | 597.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 197 | 26m | 275 km | 933.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 156 | 20m | 99 km | 267.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 149 | 27m | 215 km | 551.8 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 141 | 31m | 369 km | 897.5 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 141 | 27m | 152 km | 368.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 132 | 13m | - | - |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 130 | 20m | 147 km | 329.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 130 | 18m | 144 km | 323.4 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 127 | 1h 39m | 1,156 km | 2,533.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 126 | 1h 1m | 695 km | 1,510.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 119 | 1h 43m | 1,423 km | 2,920.4 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 117 | 1h 18m | 961 km | 1,939.3 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N61822 |  | Perot Field/Fort Worth Alliance Airport (KAFW) | Possum Kingdom Airport (KF35) | 2026-06-01 12:22 UTC | 2026-06-01 12:54 UTC | 32m |
| N9898M |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-01 12:30 UTC | 2026-06-01 12:51 UTC | 20m |
| BELIGOUE | Brussels Airlines | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-06-01 11:33 UTC | 2026-06-01 12:47 UTC | 1h 14m |
| N902TV |  | Leesburg Executive Airport (KJYO) | Lancaster Airport (KLNS) | 2026-06-01 11:59 UTC | 2026-06-01 12:46 UTC | 47m |
| SUI721 | SUI | Payerne Airport (LSMP) | Dubendorf Airport (LSMD) | 2026-06-01 12:14 UTC | 2026-06-01 12:45 UTC | 30m |
| HBZVU | HBZ | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-06-01 11:37 UTC | 2026-06-01 12:40 UTC | 1h 3m |
| DESERT8 | DES | Lake Havasu City Airport (KHII) | Lake Havasu City Airport (KHII) | 2026-06-01 12:17 UTC | 2026-06-01 12:38 UTC | 21m |
| HBKOR | HBK | Buochs Airport (LSZC) | Bern Belp Airport (LSZB) | 2026-06-01 11:47 UTC | 2026-06-01 12:38 UTC | 51m |
| NSZ2ES | NSZ | London Gatwick Airport (EGKK) | Stockholm-Arlanda Airport (ESSA) | 2026-06-01 10:33 UTC | 2026-06-01 12:32 UTC | 1h 58m |
| LFA533 | LFA | Orlando Sanford International Airport (KSFB) | Witham Field (KSUA) | 2026-06-01 11:17 UTC | 2026-06-01 12:27 UTC | 1h 9m |
| N9898M |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-01 11:47 UTC | 2026-06-01 12:20 UTC | 32m |
| NOJ88 | NOJ | Saint John Airport (CYSJ) | Bangor International Airport (KBGR) | 2026-06-01 11:48 UTC | 2026-06-01 12:16 UTC | 27m |
| ROT7205 | ROT | Henri Coanda International Airport (LROP) | Fetesti Air Base (LR80) | 2026-06-01 11:58 UTC | 2026-06-01 12:13 UTC | 14m |
| LOT1MH | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Rzeszow-Jasionka Airport (EPRZ) | 2026-06-01 11:41 UTC | 2026-06-01 12:12 UTC | 31m |
| N58FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-06-01 11:48 UTC | 2026-06-01 12:09 UTC | 21m |
| AXB2819 | AXB | Yelahanka Air Force Station (VOYK) | VEVZ (VEVZ) | 2026-06-01 09:32 UTC | 2026-06-01 12:08 UTC | 2h 36m |
| LXC87 | LXC | Dinard-Pleurtuit-Saint-Malo Airport (LFRD) | Dinard-Pleurtuit-Saint-Malo Airport (LFRD) | 2026-06-01 11:42 UTC | 2026-06-01 12:08 UTC | 25m |
| N364EA |  | Glendale Regional Airport (KGEU) | Western Sky Airpark (0AZ2) | 2026-06-01 10:56 UTC | 2026-06-01 12:07 UTC | 1h 11m |
| N650CW |  | Addison Airport (KADS) | Dorton Airport (03MO) | 2026-06-01 11:04 UTC | 2026-06-01 12:05 UTC | 1h 0m |
| N36HF |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-06-01 11:21 UTC | 2026-06-01 12:04 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
