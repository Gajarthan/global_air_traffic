# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_23:26:25_UTC-green)

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

**Latest saved flight:** 2026-05-25 23:26:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-25 23:26:25 UTC

- **94,741** saved flights
- **33,424** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,741** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,165,173.8 tonnes** estimated CO2 emissions
- **67,546,304 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3996 |
| 2 | SkyWest Airlines | 3525 |
| 3 | IndiGo | 1960 |
| 4 | EJA | 1794 |
| 5 | American Airlines | 1440 |
| 6 | Southwest Airlines | 1378 |
| 7 | ENY | 1173 |
| 8 | Lufthansa | 1138 |
| 9 | Delta Air Lines | 1038 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 851 |
| 12 | AXM | 836 |
| 13 | WIF | 827 |
| 14 | AZU | 759 |
| 15 | LXJ | 716 |
| 16 | Swiss International | 709 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 658 |
| 19 | QLK | 658 |
| 20 | easyJet | 622 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 570 |
| 24 | VIV | 562 |
| 25 | Air France | 559 |
| 26 | CXK | 506 |
| 27 | MXY | 504 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78350 |
| 2 | 🇪🇸 ES | 6647 |
| 3 | 🇮🇳 IN | 6188 |
| 4 | 🇦🇺 AU | 5784 |
| 5 | 🇩🇪 DE | 5204 |
| 6 | 🇧🇷 BR | 5197 |
| 7 | 🇮🇹 IT | 5140 |
| 8 | 🇨🇦 CA | 4808 |
| 9 | 🇯🇵 JP | 4526 |
| 10 | 🇬🇧 GB | 4048 |
| 11 | 🇫🇷 FR | 3830 |
| 12 | 🇨🇴 CO | 3284 |
| 13 | 🇲🇽 MX | 2916 |
| 14 | 🇬🇷 GR | 2722 |
| 15 | 🇳🇴 NO | 2637 |
| 16 | 🇨🇭 CH | 2489 |
| 17 | 🇲🇾 MY | 2113 |
| 18 | 🇹🇷 TR | 1754 |
| 19 | 🇿🇦 ZA | 1711 |
| 20 | 🇳🇿 NZ | 1602 |
| 21 | 🇹🇭 TH | 1600 |
| 22 | 🇵🇱 PL | 1554 |
| 23 | 🇰🇷 KR | 1534 |
| 24 | 🇵🇭 PH | 1426 |
| 25 | 🇬🇹 GT | 1423 |
| 26 | 🇲🇦 MA | 1084 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 953 |
| 29 | 🇲🇪 ME | 940 |
| 30 | 🇭🇷 HR | 862 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2049 |
| 2 | Denver International Airport |  | US | 1605 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1347 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1250 |
| 6 | Harry Reid International Airport |  | US | 1222 |
| 7 | Frankfurt am Main International Airport |  | DE | 1153 |
| 8 | Guaymaral Airport |  | CO | 1151 |
| 9 | Zurich Airport |  | CH | 1107 |
| 10 | La Aurora Airport |  | GT | 1089 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1030 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1029 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 948 |
| 15 | Chicago O'Hare International Airport |  | US | 918 |
| 16 | Madrid Barajas International Airport |  | ES | 843 |
| 17 | Kuala Lumpur International Airport |  | MY | 839 |
| 18 | Salt Lake City International Airport |  | US | 801 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 798 |
| 20 | Capua Airport |  | IT | 785 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 755 |
| 22 | Malpensa International Airport |  | IT | 745 |
| 23 | Bengaluru International Airport |  | IN | 742 |
| 24 | Charles de Gaulle International Airport |  | FR | 741 |
| 25 | Congonhas Airport |  | BR | 722 |
| 26 | Charlotte/Douglas International Airport |  | US | 721 |
| 27 | Daniel K Inouye International Airport |  | US | 677 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 650 |
| 30 | Barcelona International Airport |  | ES | 639 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 638 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 616 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 607 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 588 |
| 36 | Vitoria/Foronda Airport |  | ES | 587 |
| 37 | Don Mueang International Airport |  | TH | 586 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 562 |
| 40 | O. R. Tambo International Airport |  | ZA | 543 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 472 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 348 | 21m | 244 km | 1,465.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 254 | 24m | 225 km | 985.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 252 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 238 | 28m | 304 km | 1,247.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 216 | 1h 10m | 770 km | 2,869.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 189 | 26m | 275 km | 895.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 142 | 27m | 215 km | 525.9 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 139 | 14m | 154 km | 368.3 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 122 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 119 | 1h 39m | 1,156 km | 2,374.0 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 114 | 1h 52m | 1,304 km | 2,564.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N70052 |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-05-25 23:02 UTC | 2026-05-25 23:26 UTC | 23m |
| N217AT |  | Redlands Municipal Airport (KREI) | Big Bear City Airport (KL35) | 2026-05-25 23:00 UTC | 2026-05-25 23:25 UTC | 25m |
| CFL08 | CFL | Wellington International Airport (NZWN) | Wellington International Airport (NZWN) | 2026-05-25 23:20 UTC | 2026-05-25 23:23 UTC | 3m |
| N974PA |  | Mc Clellan-Palomar Airport (KCRQ) | Hemet-Ryan Airport (KHMT) | 2026-05-25 22:55 UTC | 2026-05-25 23:21 UTC | 25m |
| STT60 | STT | Santa Ynez/Kunkle Field (KIZA) | Santa Monica Municipal Airport (KSMO) | 2026-05-25 22:47 UTC | 2026-05-25 23:17 UTC | 29m |
| N75N |  | Keysa Airport (NY79) | Knowlesville Airport (NY01) | 2026-05-25 22:12 UTC | 2026-05-25 23:14 UTC | 1h 2m |
| N3952S |  | Taunton Municipal/King Field (KTAN) | New Bedford Regional Airport (KEWB) | 2026-05-25 22:29 UTC | 2026-05-25 23:08 UTC | 39m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | 51CO (51CO) | 2026-05-25 22:21 UTC | 2026-05-25 23:03 UTC | 42m |
| FTO382 | FTO | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-05-25 22:29 UTC | 2026-05-25 23:03 UTC | 33m |
| ZKJCJ | ZKJ | Queenstown International Airport (NZQN) | Omaka Blenheim Airport (NZOM) | 2026-05-25 22:18 UTC | 2026-05-25 22:57 UTC | 39m |
| N716MK |  | Hector International Airport (KFAR) | 08IS (08IS) | 2026-05-25 20:54 UTC | 2026-05-25 22:56 UTC | 2h 2m |
| SWA2050 | Southwest Airlines | Harry Reid International Airport (KLAS) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-25 21:56 UTC | 2026-05-25 22:53 UTC | 57m |
| N118JK |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-05-25 22:15 UTC | 2026-05-25 22:51 UTC | 36m |
| N3NJ |  | 8NJ0 (8NJ0) | NJ58 (NJ58) | 2026-05-25 22:45 UTC | 2026-05-25 22:50 UTC | 5m |
| N10EA |  | 22LL (22LL) | 22LL (22LL) | 2026-05-25 22:33 UTC | 2026-05-25 22:47 UTC | 14m |
| N546JB |  | Zamperini Field (KTOA) | San Bernardino International Airport (KSBD) | 2026-05-25 22:06 UTC | 2026-05-25 22:47 UTC | 41m |
| N405D |  | Westchester County Airport (KHPN) | Washington Dulles International Airport (KIAD) | 2026-05-25 22:02 UTC | 2026-05-25 22:45 UTC | 42m |
| N60244 |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-05-25 21:57 UTC | 2026-05-25 22:43 UTC | 46m |
| N775AM |  | Zamperini Field (KTOA) | Santa Monica Municipal Airport (KSMO) | 2026-05-25 22:23 UTC | 2026-05-25 22:43 UTC | 19m |
| LR453 |  | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-05-25 22:05 UTC | 2026-05-25 22:39 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
