# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_07:01:29_UTC-green)

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

**Latest saved flight:** 2026-05-17 07:01:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 07:01:29 UTC

- **85,640** saved flights
- **30,736** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,640** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,058,301.6 tonnes** estimated CO2 emissions
- **61,350,814 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3667 |
| 2 | SkyWest Airlines | 3172 |
| 3 | IndiGo | 1842 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1317 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1085 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 936 |
| 10 | Vueling | 811 |
| 11 | LATAM Airlines | 778 |
| 12 | AXM | 773 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | All Nippon Airways | 663 |
| 16 | Swiss International | 662 |
| 17 | LXJ | 628 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 563 |
| 21 | Cathay Pacific | 545 |
| 22 | EJU | 541 |
| 23 | AEE | 538 |
| 24 | VIV | 515 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 477 |
| 27 | CXK | 453 |
| 28 | AXB | 451 |
| 29 | MXY | 427 |
| 30 | AIQ | 420 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70204 |
| 2 | 🇪🇸 ES | 6043 |
| 3 | 🇮🇳 IN | 5771 |
| 4 | 🇦🇺 AU | 5463 |
| 5 | 🇩🇪 DE | 4760 |
| 6 | 🇧🇷 BR | 4711 |
| 7 | 🇮🇹 IT | 4708 |
| 8 | 🇯🇵 JP | 4294 |
| 9 | 🇨🇦 CA | 4255 |
| 10 | 🇬🇧 GB | 3643 |
| 11 | 🇫🇷 FR | 3392 |
| 12 | 🇨🇴 CO | 2876 |
| 13 | 🇲🇽 MX | 2641 |
| 14 | 🇬🇷 GR | 2482 |
| 15 | 🇳🇴 NO | 2374 |
| 16 | 🇨🇭 CH | 2246 |
| 17 | 🇲🇾 MY | 1942 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1533 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1487 |
| 22 | 🇵🇱 PL | 1416 |
| 23 | 🇵🇭 PH | 1344 |
| 24 | 🇰🇷 KR | 1324 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇴 MO | 997 |
| 27 | 🇲🇦 MA | 994 |
| 28 | 🇲🇪 ME | 892 |
| 29 | 🇳🇱 NL | 869 |
| 30 | 🇭🇷 HR | 763 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Denver International Airport |  | US | 1441 |
| 3 | Tokyo International Airport |  | JP | 1434 |
| 4 | Indira Gandhi International Airport |  | IN | 1238 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1191 |
| 6 | Frankfurt am Main International Airport |  | DE | 1096 |
| 7 | Harry Reid International Airport |  | US | 1083 |
| 8 | Zurich Airport |  | CH | 1015 |
| 9 | Macau International Airport |  | MO | 997 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 925 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 864 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 778 |
| 17 | Kuala Lumpur International Airport |  | MY | 771 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 714 |
| 20 | Salt Lake City International Airport |  | US | 711 |
| 21 | Malpensa International Airport |  | IT | 709 |
| 22 | Capua Airport |  | IT | 700 |
| 23 | Bengaluru International Airport |  | IN | 700 |
| 24 | Charles de Gaulle International Airport |  | FR | 665 |
| 25 | Charlotte/Douglas International Airport |  | US | 664 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 630 |
| 28 | Tenerife Norte Airport |  | ES | 621 |
| 29 | Ninoy Aquino International Airport |  | PH | 616 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 582 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 572 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 549 |
| 35 | Vitoria/Foronda Airport |  | ES | 541 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 541 |
| 37 | Don Mueang International Airport |  | TH | 537 |
| 38 | Amsterdam Airport Schiphol |  | NL | 529 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 501 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 319 | 21m | 244 km | 1,343.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 227 | 1h 26m | 910 km | 3,562.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 225 | 28m | 304 km | 1,179.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 196 | 1h 11m | 770 km | 2,603.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 178 | 26m | 275 km | 843.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 134 | 31m | 369 km | 852.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASTR332 | AST | RAAF Base Richmond (YSRI) | RAAF Base Richmond (YSRI) | 2026-05-17 06:51 UTC | 2026-05-17 07:01 UTC | 10m |
| ASTR316 | AST | RAAF Base Richmond (YSRI) | RAAF Base Richmond (YSRI) | 2026-05-17 06:48 UTC | 2026-05-17 06:59 UTC | 11m |
| MXD184 | MXD | Kuala Lumpur International Airport (WMKK) | Simara Airport (VNSI) | 2026-05-17 02:45 UTC | 2026-05-17 06:58 UTC | 4h 12m |
| ISR889 | ISR | Ben Gurion International Airport (LLBG) | Erzincan Airport (LTCD) | 2026-05-17 05:27 UTC | 2026-05-17 06:57 UTC | 1h 29m |
| CPA256 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-16 19:38 UTC | 2026-05-17 06:56 UTC | 11h 18m |
| JLK | JLK | Moruya Airport (YMRY) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-17 05:54 UTC | 2026-05-17 06:56 UTC | 1h 1m |
| DLH796 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-05-16 19:59 UTC | 2026-05-17 06:54 UTC | 10h 55m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Vauxhall Airport (CEN6) | 2026-05-17 06:06 UTC | 2026-05-17 06:32 UTC | 26m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-05-16 18:42 UTC | 2026-05-17 06:31 UTC | 11h 48m |
| N879MH |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-05-17 06:04 UTC | 2026-05-17 06:28 UTC | 24m |
| AWH91A | AWH | Hannover Airport (EDDV) | Berlin Brandenburg Airport (EDDB) | 2026-05-17 05:54 UTC | 2026-05-17 06:25 UTC | 31m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-05-17 05:40 UTC | 2026-05-17 06:24 UTC | 43m |
| VLG3505 | Vueling | Ibiza Airport (LEIB) | Barcelona International Airport (LEBL) | 2026-05-17 05:43 UTC | 2026-05-17 06:21 UTC | 37m |
| CLX4796 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-16 19:14 UTC | 2026-05-17 06:16 UTC | 11h 1m |
| WZZ5SD | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Catania / Fontanarossa Airport (LICC) | 2026-05-17 04:23 UTC | 2026-05-17 06:07 UTC | 1h 43m |
| APG225 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-05-17 05:41 UTC | 2026-05-17 06:07 UTC | 26m |
| UAE382 | Emirates | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-05-16 23:45 UTC | 2026-05-17 06:06 UTC | 6h 21m |
| ANE87CJ | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-05-17 05:33 UTC | 2026-05-17 06:06 UTC | 33m |
| ASTR332 | AST | RAAF Base Richmond (YSRI) | RAAF Base Richmond (YSRI) | 2026-05-17 05:46 UTC | 2026-05-17 06:01 UTC | 15m |
| JAL375 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-17 05:00 UTC | 2026-05-17 06:01 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
