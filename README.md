# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_22:46:36_UTC-green)

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

**Latest saved flight:** 2026-05-09 22:46:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-09 22:46:36 UTC

- **76,311** saved flights
- **28,013** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,311** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **942,816.2 tonnes** estimated CO2 emissions
- **54,656,013 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3269 |
| 2 | SkyWest Airlines | 2844 |
| 3 | IndiGo | 1696 |
| 4 | EJA | 1409 |
| 5 | American Airlines | 1197 |
| 6 | Southwest Airlines | 1117 |
| 7 | Lufthansa | 994 |
| 8 | ENY | 956 |
| 9 | Delta Air Lines | 777 |
| 10 | Vueling | 734 |
| 11 | AXM | 712 |
| 12 | LATAM Airlines | 706 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 617 |
| 15 | AZU | 610 |
| 16 | QLK | 579 |
| 17 | Swiss International | 578 |
| 18 | LXJ | 563 |
| 19 | Alaska Airlines | 537 |
| 20 | easyJet | 503 |
| 21 | AEE | 491 |
| 22 | EJU | 490 |
| 23 | Cathay Pacific | 488 |
| 24 | VIV | 458 |
| 25 | Air France | 443 |
| 26 | Japan Airlines | 443 |
| 27 | AXB | 419 |
| 28 | CXK | 391 |
| 29 | AIQ | 377 |
| 30 | MXY | 373 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61716 |
| 2 | 🇪🇸 ES | 5458 |
| 3 | 🇮🇳 IN | 5318 |
| 4 | 🇦🇺 AU | 4958 |
| 5 | 🇩🇪 DE | 4289 |
| 6 | 🇧🇷 BR | 4268 |
| 7 | 🇮🇹 IT | 4181 |
| 8 | 🇯🇵 JP | 3961 |
| 9 | 🇨🇦 CA | 3808 |
| 10 | 🇬🇧 GB | 3271 |
| 11 | 🇫🇷 FR | 3022 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2355 |
| 14 | 🇬🇷 GR | 2243 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2070 |
| 17 | 🇲🇾 MY | 1773 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1372 |
| 20 | 🇹🇷 TR | 1367 |
| 21 | 🇹🇭 TH | 1343 |
| 22 | 🇵🇱 PL | 1273 |
| 23 | 🇵🇭 PH | 1218 |
| 24 | 🇬🇹 GT | 1197 |
| 25 | 🇰🇷 KR | 1181 |
| 26 | 🇲🇦 MA | 902 |
| 27 | 🇲🇴 MO | 888 |
| 28 | 🇲🇪 ME | 809 |
| 29 | 🇳🇱 NL | 797 |
| 30 | 🇭🇷 HR | 655 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1700 |
| 2 | Tokyo International Airport |  | JP | 1330 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1118 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1100 |
| 6 | Frankfurt am Main International Airport |  | DE | 991 |
| 7 | Harry Reid International Airport |  | US | 949 |
| 8 | Zurich Airport |  | CH | 900 |
| 9 | La Aurora Airport |  | GT | 898 |
| 10 | Guaymaral Airport |  | CO | 890 |
| 11 | Macau International Airport |  | MO | 888 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 767 |
| 14 | Chicago O'Hare International Airport |  | US | 749 |
| 15 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 723 |
| 16 | Kuala Lumpur International Airport |  | MY | 713 |
| 17 | Madrid Barajas International Airport |  | ES | 711 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Bengaluru International Airport |  | IN | 660 |
| 20 | Malpensa International Airport |  | IT | 658 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 651 |
| 22 | Salt Lake City International Airport |  | US | 627 |
| 23 | Congonhas Airport |  | BR | 604 |
| 24 | Charlotte/Douglas International Airport |  | US | 600 |
| 25 | Charles de Gaulle International Airport |  | FR | 594 |
| 26 | Capua Airport |  | IT | 594 |
| 27 | Tenerife Norte Airport |  | ES | 569 |
| 28 | Daniel K Inouye International Airport |  | US | 558 |
| 29 | Ninoy Aquino International Airport |  | PH | 552 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 541 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 515 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 514 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 502 |
| 35 | Vitoria/Foronda Airport |  | ES | 481 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 37 | Amsterdam Airport Schiphol |  | NL | 479 |
| 38 | Don Mueang International Airport |  | TH | 475 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 273 | 21m | 244 km | 1,149.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
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
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 122 | 31m | 369 km | 776.6 t |
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
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DAL2683 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:35 UTC | 2026-05-09 22:46 UTC | 11m |
| DAL2006 | Delta Air Lines | General Mitchell International Airport (KMKE) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 21:49 UTC | 2026-05-09 22:46 UTC | 57m |
| N8636Q |  | Meadowmist Airport (WN35) | Boeing Field/King County International Airport (KBFI) | 2026-05-09 22:07 UTC | 2026-05-09 22:42 UTC | 34m |
| DAL2983 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:26 UTC | 2026-05-09 22:41 UTC | 14m |
| OXF5940 | OXF | Falcon Field (KFFZ) | 2AZ8 (2AZ8) | 2026-05-09 21:17 UTC | 2026-05-09 22:35 UTC | 1h 17m |
| DAL1641 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:23 UTC | 2026-05-09 22:34 UTC | 11m |
| N9842G |  | Nut Tree Airport (KVCB) | Sacramento Executive Airport (KSAC) | 2026-05-09 22:13 UTC | 2026-05-09 22:29 UTC | 16m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-05-09 10:27 UTC | 2026-05-09 22:25 UTC | 11h 58m |
| WUP651 | WUP | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:11 UTC | 2026-05-09 22:24 UTC | 12m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Zhuhai Airport (ZGSD) | 2026-05-09 11:47 UTC | 2026-05-09 22:24 UTC | 10h 36m |
| DAL2414 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:05 UTC | 2026-05-09 22:23 UTC | 17m |
| DAL941 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 19:22 UTC | 2026-05-09 22:23 UTC | 3h 0m |
| DAL2819 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 22:07 UTC | 2026-05-09 22:22 UTC | 14m |
| CPA294 | Cathay Pacific | Brussels Airport (EBBR) | Zhuhai Airport (ZGSD) | 2026-05-09 11:18 UTC | 2026-05-09 22:21 UTC | 11h 2m |
| DAL170 | Delta Air Lines | Incheon International Airport (RKSI) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 10:53 UTC | 2026-05-09 22:18 UTC | 11h 24m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-05-09 11:28 UTC | 2026-05-09 22:16 UTC | 10h 48m |
| EDV5175 | EDV | St Louis Lambert International Airport (KSTL) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 21:03 UTC | 2026-05-09 22:14 UTC | 1h 11m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-05-09 14:09 UTC | 2026-05-09 22:11 UTC | 8h 2m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-09 21:50 UTC | 2026-05-09 22:04 UTC | 14m |
| DAL2528 | Delta Air Lines | San Antonio International Airport (KSAT) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-09 19:45 UTC | 2026-05-09 22:04 UTC | 2h 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
