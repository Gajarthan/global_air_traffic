# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_19:18:17_UTC-green)

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

**Latest saved flight:** 2026-05-09 19:18:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 19:18:17 UTC

- **75,865** saved flights
- **27,895** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **75,865** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **935,900.4 tonnes** estimated CO2 emissions
- **54,255,094 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3245 |
| 2 | SkyWest Airlines | 2811 |
| 3 | IndiGo | 1696 |
| 4 | EJA | 1393 |
| 5 | American Airlines | 1177 |
| 6 | Southwest Airlines | 1106 |
| 7 | Lufthansa | 991 |
| 8 | ENY | 947 |
| 9 | Delta Air Lines | 747 |
| 10 | Vueling | 731 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 701 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 610 |
| 16 | QLK | 579 |
| 17 | Swiss International | 577 |
| 18 | LXJ | 558 |
| 19 | Alaska Airlines | 532 |
| 20 | easyJet | 502 |
| 21 | AEE | 489 |
| 22 | EJU | 485 |
| 23 | Cathay Pacific | 476 |
| 24 | VIV | 458 |
| 25 | Japan Airlines | 443 |
| 26 | Air France | 442 |
| 27 | AXB | 419 |
| 28 | CXK | 390 |
| 29 | AIQ | 377 |
| 30 | MXY | 369 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61155 |
| 2 | 🇪🇸 ES | 5430 |
| 3 | 🇮🇳 IN | 5315 |
| 4 | 🇦🇺 AU | 4954 |
| 5 | 🇩🇪 DE | 4279 |
| 6 | 🇧🇷 BR | 4252 |
| 7 | 🇮🇹 IT | 4151 |
| 8 | 🇯🇵 JP | 3960 |
| 9 | 🇨🇦 CA | 3781 |
| 10 | 🇬🇧 GB | 3255 |
| 11 | 🇫🇷 FR | 3009 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2344 |
| 14 | 🇬🇷 GR | 2235 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2067 |
| 17 | 🇲🇾 MY | 1773 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1366 |
| 20 | 🇹🇷 TR | 1362 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1271 |
| 23 | 🇵🇭 PH | 1216 |
| 24 | 🇬🇹 GT | 1195 |
| 25 | 🇰🇷 KR | 1179 |
| 26 | 🇲🇦 MA | 895 |
| 27 | 🇲🇴 MO | 880 |
| 28 | 🇲🇪 ME | 805 |
| 29 | 🇳🇱 NL | 793 |
| 30 | 🇭🇷 HR | 646 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1676 |
| 2 | Tokyo International Airport |  | JP | 1330 |
| 3 | Denver International Airport |  | US | 1267 |
| 4 | Indira Gandhi International Airport |  | IN | 1116 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1097 |
| 6 | Frankfurt am Main International Airport |  | DE | 988 |
| 7 | Harry Reid International Airport |  | US | 943 |
| 8 | Zurich Airport |  | CH | 897 |
| 9 | La Aurora Airport |  | GT | 896 |
| 10 | Guaymaral Airport |  | CO | 890 |
| 11 | Macau International Airport |  | MO | 880 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 761 |
| 14 | Chicago O'Hare International Airport |  | US | 740 |
| 15 | Kuala Lumpur International Airport |  | MY | 713 |
| 16 | Madrid Barajas International Airport |  | ES | 706 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 672 |
| 18 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 665 |
| 19 | Bengaluru International Airport |  | IN | 660 |
| 20 | Malpensa International Airport |  | IT | 652 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 651 |
| 22 | Salt Lake City International Airport |  | US | 622 |
| 23 | Congonhas Airport |  | BR | 601 |
| 24 | Charlotte/Douglas International Airport |  | US | 595 |
| 25 | Charles de Gaulle International Airport |  | FR | 590 |
| 26 | Capua Airport |  | IT | 589 |
| 27 | Tenerife Norte Airport |  | ES | 564 |
| 28 | Daniel K Inouye International Airport |  | US | 553 |
| 29 | Ninoy Aquino International Airport |  | PH | 551 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 541 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 521 |
| 32 | Barcelona International Airport |  | ES | 512 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 510 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 502 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 476 |
| 37 | Amsterdam Airport Schiphol |  | NL | 475 |
| 38 | Don Mueang International Airport |  | TH | 475 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 450 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 270 | 21m | 244 km | 1,136.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 219 | 24m | 225 km | 849.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 211 | 28m | 304 km | 1,106.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 206 | 1h 27m | 910 km | 3,232.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 194 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 182 | 19m | 165 km | 517.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 179 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 167 | 1h 12m | 770 km | 2,218.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 134 | 44m | 452 km | 1,044.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 121 | 31m | 369 km | 770.2 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 101 | 1h 42m | 1,423 km | 2,478.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 101 | 57m | 493 km | 859.3 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 96 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 94 | 1h 19m | 961 km | 1,558.1 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 94 | 52m | 556 km | 901.1 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BOX712 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-05-09 12:46 UTC | 2026-05-09 19:18 UTC | 6h 32m |
| EDV4852 | EDV | Tappen Airstrip (8NA0) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:25 UTC | 2026-05-09 19:17 UTC | 52m |
| N715MT |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-05-09 18:28 UTC | 2026-05-09 19:14 UTC | 46m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-09 18:29 UTC | 2026-05-09 19:12 UTC | 42m |
| N285CS |  | Livermore Municipal Airport (KLVK) | Palo Alto Airport (KPAO) | 2026-05-09 18:31 UTC | 2026-05-09 19:11 UTC | 40m |
|  |  | Toronto Pearson International Airport (CYYZ) | Toronto Pearson International Airport (CYYZ) | 2026-05-09 19:05 UTC | 2026-05-09 19:05 UTC | 0m |
| DAL2245 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:46 UTC | 2026-05-09 19:00 UTC | 13m |
| SKW4144 | SkyWest Airlines | Ripplinger Strip (NA33) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:03 UTC | 2026-05-09 18:55 UTC | 52m |
| N733EP |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-05-09 18:35 UTC | 2026-05-09 18:54 UTC | 19m |
| N7651F |  | Aero Valley Airport (K52F) | Decatur Municipal Airport (KLUD) | 2026-05-09 18:27 UTC | 2026-05-09 18:53 UTC | 25m |
| N25BQ |  | Green Bay/Austin Straubel International Airport (KGRB) | Willadae Farms Airport (4LL7) | 2026-05-09 17:16 UTC | 2026-05-09 18:51 UTC | 1h 34m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-09 18:32 UTC | 2026-05-09 18:49 UTC | 17m |
| DAL2185 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:28 UTC | 2026-05-09 18:49 UTC | 21m |
| SKW3699 | SkyWest Airlines | Washington Dulles International Airport (KIAD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 16:21 UTC | 2026-05-09 18:49 UTC | 2h 28m |
| DAL2414 | Delta Air Lines | John F Kennedy International Airport (KJFK) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 16:06 UTC | 2026-05-09 18:47 UTC | 2h 40m |
| N415XT |  | Gnoss Field (KDVO) | Mammoth Yosemite Airport (KMMH) | 2026-05-09 18:04 UTC | 2026-05-09 18:45 UTC | 40m |
| DAL9936 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 07:10 UTC | 2026-05-09 18:45 UTC | 11h 34m |
| WSN1 | WSN | Albuquerque International Sunport Airport (KABQ) | Casas Adobes Airpark (NM69) | 2026-05-09 18:07 UTC | 2026-05-09 18:44 UTC | 37m |
| DAL1641 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 18:30 UTC | 2026-05-09 18:44 UTC | 13m |
| N880HP |  | Fulton County Executive/Charlie Brown Field (KFTY) | Weaver Field (SC94) | 2026-05-09 18:10 UTC | 2026-05-09 18:43 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
