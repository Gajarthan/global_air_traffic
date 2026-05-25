# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_17:09:43_UTC-green)

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

**Latest saved flight:** 2026-05-25 17:09:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-25 17:09:43 UTC

- **94,626** saved flights
- **33,383** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **94,626** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,164,115.6 tonnes** estimated CO2 emissions
- **67,484,959 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3996 |
| 2 | SkyWest Airlines | 3518 |
| 3 | IndiGo | 1959 |
| 4 | EJA | 1787 |
| 5 | American Airlines | 1440 |
| 6 | Southwest Airlines | 1374 |
| 7 | ENY | 1173 |
| 8 | Lufthansa | 1138 |
| 9 | Delta Air Lines | 1036 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 849 |
| 12 | AXM | 836 |
| 13 | WIF | 827 |
| 14 | AZU | 756 |
| 15 | LXJ | 712 |
| 16 | Swiss International | 709 |
| 17 | All Nippon Airways | 698 |
| 18 | Alaska Airlines | 657 |
| 19 | QLK | 657 |
| 20 | easyJet | 622 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 570 |
| 24 | VIV | 562 |
| 25 | Air France | 559 |
| 26 | CXK | 506 |
| 27 | MXY | 503 |
| 28 | Japan Airlines | 489 |
| 29 | AXB | 479 |
| 30 | AIQ | 455 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78185 |
| 2 | 🇪🇸 ES | 6647 |
| 3 | 🇮🇳 IN | 6186 |
| 4 | 🇦🇺 AU | 5778 |
| 5 | 🇩🇪 DE | 5204 |
| 6 | 🇧🇷 BR | 5187 |
| 7 | 🇮🇹 IT | 5140 |
| 8 | 🇨🇦 CA | 4801 |
| 9 | 🇯🇵 JP | 4526 |
| 10 | 🇬🇧 GB | 4048 |
| 11 | 🇫🇷 FR | 3830 |
| 12 | 🇨🇴 CO | 3284 |
| 13 | 🇲🇽 MX | 2913 |
| 14 | 🇬🇷 GR | 2722 |
| 15 | 🇳🇴 NO | 2637 |
| 16 | 🇨🇭 CH | 2489 |
| 17 | 🇲🇾 MY | 2113 |
| 18 | 🇹🇷 TR | 1754 |
| 19 | 🇿🇦 ZA | 1711 |
| 20 | 🇹🇭 TH | 1600 |
| 21 | 🇳🇿 NZ | 1596 |
| 22 | 🇵🇱 PL | 1554 |
| 23 | 🇰🇷 KR | 1528 |
| 24 | 🇵🇭 PH | 1424 |
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
| 2 | Denver International Airport |  | US | 1602 |
| 3 | Tokyo International Airport |  | JP | 1505 |
| 4 | Indira Gandhi International Airport |  | IN | 1346 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1250 |
| 6 | Harry Reid International Airport |  | US | 1216 |
| 7 | Frankfurt am Main International Airport |  | DE | 1153 |
| 8 | Guaymaral Airport |  | CO | 1151 |
| 9 | Zurich Airport |  | CH | 1107 |
| 10 | La Aurora Airport |  | GT | 1089 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1030 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1027 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 946 |
| 15 | Chicago O'Hare International Airport |  | US | 914 |
| 16 | Madrid Barajas International Airport |  | ES | 843 |
| 17 | Kuala Lumpur International Airport |  | MY | 839 |
| 18 | Salt Lake City International Airport |  | US | 800 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 797 |
| 20 | Capua Airport |  | IT | 785 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 754 |
| 22 | Malpensa International Airport |  | IT | 745 |
| 23 | Bengaluru International Airport |  | IN | 742 |
| 24 | Charles de Gaulle International Airport |  | FR | 741 |
| 25 | Charlotte/Douglas International Airport |  | US | 721 |
| 26 | Congonhas Airport |  | BR | 720 |
| 27 | Daniel K Inouye International Airport |  | US | 676 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 650 |
| 30 | Barcelona International Airport |  | ES | 639 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 636 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 615 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 606 |
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
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 347 | 21m | 244 km | 1,461.1 t |
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
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 118 | 1h 40m | 1,156 km | 2,354.1 t |
| 26 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 28 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 113 | 1h 52m | 1,304 km | 2,542.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N33JP |  | Regan Ranch Airport (6ID1) | Driftwood Air Ranch Airport (ID65) | 2026-05-25 15:43 UTC | 2026-05-25 17:09 UTC | 1h 26m |
| N32711 |  | Three Rivers Municipal/Dr Haines Airport (KHAI) | Wolfe Field (IN65) | 2026-05-25 16:32 UTC | 2026-05-25 17:07 UTC | 34m |
| N280CA |  | Lincoln Regional/Karl Harder Field (KLHM) | Lincoln Regional/Karl Harder Field (KLHM) | 2026-05-25 16:52 UTC | 2026-05-25 16:54 UTC | 2m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-25 16:34 UTC | 2026-05-25 16:52 UTC | 17m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-25 16:33 UTC | 2026-05-25 16:51 UTC | 18m |
| N118JK |  | Chino Airport (KCNO) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-25 16:39 UTC | 2026-05-25 16:51 UTC | 12m |
| FGAHV | FGA | Albertville Airport (LFKA) | Megeve Airport (LFHM) | 2026-05-25 16:26 UTC | 2026-05-25 16:42 UTC | 15m |
| N13AL |  | Ted Stevens Anchorage International Airport (PANC) | Valdez Pioneer Field (PAVD) | 2026-05-25 15:51 UTC | 2026-05-25 16:39 UTC | 48m |
| PNC0106 | PNC | Guaymaral Airport (SKGY) | El Dorado International Airport (SKBO) | 2026-05-25 16:23 UTC | 2026-05-25 16:39 UTC | 15m |
| N811AT |  | Arlington Municipal Airport (KGKY) | Cleburne Regional Airport (KCPT) | 2026-05-25 15:59 UTC | 2026-05-25 16:36 UTC | 36m |
| ERU979 | ERU | Deland Municipal-Sidney H Taylor Field (KDED) | Skinners Wholesale Nursery Airport (16FD) | 2026-05-25 16:01 UTC | 2026-05-25 16:33 UTC | 31m |
| CONGO65 | CON | City Of Colorado Springs Municipal Airport (KCOS) | Usaf Academy Davis Airfield (KAFF) | 2026-05-25 16:13 UTC | 2026-05-25 16:33 UTC | 19m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Laramie Regional Airport (KLAR) | 2026-05-25 16:11 UTC | 2026-05-25 16:32 UTC | 20m |
| N216CW |  | Kenosha Regional Airport (KENW) | Antrim County Airport (KACB) | 2026-05-25 15:52 UTC | 2026-05-25 16:31 UTC | 39m |
| HK5309G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-25 16:06 UTC | 2026-05-25 16:31 UTC | 24m |
| N3858Q |  | City Of Slaton/Larry T Neal Memorial Airport (KF49) | City Of Slaton/Larry T Neal Memorial Airport (KF49) | 2026-05-25 16:20 UTC | 2026-05-25 16:31 UTC | 11m |
| N45BE |  | Central Nebraska Regional Airport (KGRI) | Lake County Airport (KLXV) | 2026-05-25 15:26 UTC | 2026-05-25 16:31 UTC | 1h 4m |
| CXK602 | CXK | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-25 15:38 UTC | 2026-05-25 16:28 UTC | 50m |
| N3079Y |  | Cottonwood Airport (0MT5) | Laurel Municipal Airport (K6S8) | 2026-05-25 16:23 UTC | 2026-05-25 16:27 UTC | 3m |
| N3128T |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-05-25 16:18 UTC | 2026-05-25 16:26 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
