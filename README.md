# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_04:29:19_UTC-green)

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

**Latest saved flight:** 2026-05-16 04:29:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 04:29:19 UTC

- **84,189** saved flights
- **30,361** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,189** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,035,177.2 tonnes** estimated CO2 emissions
- **60,010,273 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3595 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1813 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1296 |
| 6 | Southwest Airlines | 1237 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 921 |
| 10 | Vueling | 795 |
| 11 | LATAM Airlines | 763 |
| 12 | AXM | 758 |
| 13 | WIF | 726 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 655 |
| 16 | Swiss International | 648 |
| 17 | QLK | 620 |
| 18 | LXJ | 619 |
| 19 | Alaska Airlines | 597 |
| 20 | easyJet | 552 |
| 21 | EJU | 534 |
| 22 | AEE | 530 |
| 23 | Cathay Pacific | 526 |
| 24 | VIV | 505 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 470 |
| 27 | CXK | 446 |
| 28 | AXB | 445 |
| 29 | MXY | 420 |
| 30 | United Airlines | 415 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69151 |
| 2 | 🇪🇸 ES | 5936 |
| 3 | 🇮🇳 IN | 5673 |
| 4 | 🇦🇺 AU | 5396 |
| 5 | 🇩🇪 DE | 4667 |
| 6 | 🇧🇷 BR | 4639 |
| 7 | 🇮🇹 IT | 4634 |
| 8 | 🇯🇵 JP | 4222 |
| 9 | 🇨🇦 CA | 4203 |
| 10 | 🇬🇧 GB | 3576 |
| 11 | 🇫🇷 FR | 3323 |
| 12 | 🇨🇴 CO | 2821 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2430 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2218 |
| 17 | 🇲🇾 MY | 1904 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1492 |
| 20 | 🇳🇿 NZ | 1489 |
| 21 | 🇹🇭 TH | 1458 |
| 22 | 🇵🇱 PL | 1393 |
| 23 | 🇵🇭 PH | 1317 |
| 24 | 🇰🇷 KR | 1289 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 976 |
| 27 | 🇲🇴 MO | 965 |
| 28 | 🇲🇪 ME | 886 |
| 29 | 🇳🇱 NL | 860 |
| 30 | 🇭🇷 HR | 752 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1847 |
| 2 | Denver International Airport |  | US | 1419 |
| 3 | Tokyo International Airport |  | JP | 1413 |
| 4 | Indira Gandhi International Airport |  | IN | 1206 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1180 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1058 |
| 8 | Zurich Airport |  | CH | 994 |
| 9 | La Aurora Airport |  | GT | 965 |
| 10 | Macau International Airport |  | MO | 965 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 849 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 765 |
| 17 | Kuala Lumpur International Airport |  | MY | 756 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 705 |
| 20 | Salt Lake City International Airport |  | US | 704 |
| 21 | Malpensa International Airport |  | IT | 701 |
| 22 | Bengaluru International Airport |  | IN | 696 |
| 23 | Capua Airport |  | IT | 683 |
| 24 | Congonhas Airport |  | BR | 656 |
| 25 | Charlotte/Douglas International Airport |  | US | 655 |
| 26 | Charles de Gaulle International Airport |  | FR | 654 |
| 27 | Daniel K Inouye International Airport |  | US | 609 |
| 28 | Tenerife Norte Airport |  | ES | 606 |
| 29 | Ninoy Aquino International Airport |  | PH | 603 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 590 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 562 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 561 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 528 |
| 37 | Don Mueang International Airport |  | TH | 525 |
| 38 | Amsterdam Airport Schiphol |  | NL | 521 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 307 | 21m | 244 km | 1,292.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 274 | 1h 8m | 706 km | 3,336.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 239 | 24m | 225 km | 927.2 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 223 | 1h 26m | 910 km | 3,499.4 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 217 | 14m | 114 km | 425.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 189 | 1h 11m | 770 km | 2,510.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 130 | 31m | 369 km | 827.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 111 | 57m | 493 km | 944.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4360F |  | Mc Clellan-Palomar Airport (KCRQ) | Riverside Airport (KRAL) | 2026-05-16 03:42 UTC | 2026-05-16 04:29 UTC | 47m |
| DHK855 | DHK | East Midlands Airport (EGNX) | Malpensa International Airport (LIMC) | 2026-05-16 02:28 UTC | 2026-05-16 04:05 UTC | 1h 37m |
| CPA238 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-15 16:38 UTC | 2026-05-16 04:02 UTC | 11h 24m |
| N418CF |  | Bud Dryden Airport (TX05) | Austin Executive Airport (KEDC) | 2026-05-16 03:53 UTC | 2026-05-16 04:01 UTC | 8m |
| ERU26 | ERU | AZ86 (AZ86) | Phoenix Deer Valley Airport (KDVT) | 2026-05-16 03:26 UTC | 2026-05-16 04:00 UTC | 34m |
| N554VP |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Sequoia Field (KD86) | 2026-05-16 03:15 UTC | 2026-05-16 03:46 UTC | 31m |
| TAM3690 | LATAM Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Fazenda Santa Dulcina Airport (SJWN) | 2026-05-16 03:10 UTC | 2026-05-16 03:43 UTC | 32m |
| N214NX |  | Aurora State Airport (KUAO) | Ajax Airport (OR46) | 2026-05-16 03:17 UTC | 2026-05-16 03:41 UTC | 24m |
| ASA69 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-05-16 02:22 UTC | 2026-05-16 03:39 UTC | 1h 17m |
| AXM6040 | AXM | Kuala Lumpur International Airport (WMKK) | Kluang Airport (WMAP) | 2026-05-16 03:21 UTC | 2026-05-16 03:39 UTC | 17m |
| EJA471 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Moffett Federal Airfield (KNUQ) | 2026-05-16 03:17 UTC | 2026-05-16 03:34 UTC | 17m |
| IGO146 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Yongphulla Airport (VQ10) | 2026-05-16 02:26 UTC | 2026-05-16 03:32 UTC | 1h 6m |
| CLX4325 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-15 16:38 UTC | 2026-05-16 03:31 UTC | 10h 53m |
| XGN | XGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 03:20 UTC | 2026-05-16 03:31 UTC | 10m |
| ANZ647M | ANZ | Christchurch International Airport (NZCH) | Wanaka Airport (NZWF) | 2026-05-16 02:48 UTC | 2026-05-16 03:30 UTC | 41m |
| LAO442 | LAO | Suvarnabhumi Airport (VTBS) | Xieng Khouang Airport (VLXK) | 2026-05-16 02:41 UTC | 2026-05-16 03:28 UTC | 46m |
| AIC1DJ | Air India | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-05-16 02:35 UTC | 2026-05-16 03:28 UTC | 52m |
| IGO1151 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-05-16 02:20 UTC | 2026-05-16 03:27 UTC | 1h 6m |
| XHE | XHE | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 03:13 UTC | 2026-05-16 03:26 UTC | 13m |
| N699SU |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-05-16 03:24 UTC | 2026-05-16 03:25 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
