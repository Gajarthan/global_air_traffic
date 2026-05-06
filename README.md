# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_23:51:35_UTC-green)

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

**Latest saved flight:** 2026-05-05 23:51:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 23:51:35 UTC

- **70,061** saved flights
- **26,153** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **70,061** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **862,952.1 tonnes** estimated CO2 emissions
- **50,026,208 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3007 |
| 2 | SkyWest Airlines | 2622 |
| 3 | IndiGo | 1599 |
| 4 | EJA | 1281 |
| 5 | American Airlines | 1096 |
| 6 | Southwest Airlines | 1015 |
| 7 | Lufthansa | 899 |
| 8 | ENY | 876 |
| 9 | Vueling | 690 |
| 10 | AXM | 668 |
| 11 | LATAM Airlines | 656 |
| 12 | WIF | 596 |
| 13 | Delta Air Lines | 593 |
| 14 | All Nippon Airways | 585 |
| 15 | AZU | 570 |
| 16 | QLK | 539 |
| 17 | Swiss International | 539 |
| 18 | LXJ | 508 |
| 19 | Alaska Airlines | 490 |
| 20 | easyJet | 468 |
| 21 | EJU | 453 |
| 22 | AEE | 452 |
| 23 | VIV | 440 |
| 24 | Cathay Pacific | 427 |
| 25 | Air France | 411 |
| 26 | Japan Airlines | 409 |
| 27 | AXB | 389 |
| 28 | AIQ | 354 |
| 29 | CXK | 349 |
| 30 | MXY | 341 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 55805 |
| 2 | 🇪🇸 ES | 5104 |
| 3 | 🇮🇳 IN | 5029 |
| 4 | 🇦🇺 AU | 4639 |
| 5 | 🇧🇷 BR | 3953 |
| 6 | 🇩🇪 DE | 3900 |
| 7 | 🇮🇹 IT | 3833 |
| 8 | 🇯🇵 JP | 3724 |
| 9 | 🇨🇦 CA | 3463 |
| 10 | 🇬🇧 GB | 3038 |
| 11 | 🇫🇷 FR | 2769 |
| 12 | 🇨🇴 CO | 2659 |
| 13 | 🇲🇽 MX | 2226 |
| 14 | 🇬🇷 GR | 2086 |
| 15 | 🇨🇭 CH | 1923 |
| 16 | 🇳🇴 NO | 1913 |
| 17 | 🇲🇾 MY | 1666 |
| 18 | 🇿🇦 ZA | 1391 |
| 19 | 🇳🇿 NZ | 1294 |
| 20 | 🇹🇭 TH | 1262 |
| 21 | 🇹🇷 TR | 1261 |
| 22 | 🇵🇭 PH | 1160 |
| 23 | 🇵🇱 PL | 1151 |
| 24 | 🇬🇹 GT | 1129 |
| 25 | 🇰🇷 KR | 1113 |
| 26 | 🇲🇦 MA | 843 |
| 27 | 🇲🇴 MO | 802 |
| 28 | 🇲🇪 ME | 755 |
| 29 | 🇳🇱 NL | 728 |
| 30 | 🇮🇩 ID | 588 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1569 |
| 2 | Tokyo International Airport |  | JP | 1257 |
| 3 | Denver International Airport |  | US | 1164 |
| 4 | Indira Gandhi International Airport |  | IN | 1056 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1021 |
| 6 | Frankfurt am Main International Airport |  | DE | 895 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 878 |
| 9 | Guaymaral Airport |  | CO | 854 |
| 10 | La Aurora Airport |  | GT | 839 |
| 11 | Zurich Airport |  | CH | 827 |
| 12 | Macau International Airport |  | MO | 802 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 701 |
| 14 | Chicago O'Hare International Airport |  | US | 675 |
| 15 | Kuala Lumpur International Airport |  | MY | 668 |
| 16 | Madrid Barajas International Airport |  | ES | 666 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 629 |
| 18 | Malpensa International Airport |  | IT | 609 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 608 |
| 20 | Bengaluru International Airport |  | IN | 605 |
| 21 | Salt Lake City International Airport |  | US | 568 |
| 22 | Congonhas Airport |  | BR | 562 |
| 23 | Charlotte/Douglas International Airport |  | US | 555 |
| 24 | Charles de Gaulle International Airport |  | FR | 550 |
| 25 | Tenerife Norte Airport |  | ES | 544 |
| 26 | Capua Airport |  | IT | 544 |
| 27 | Ninoy Aquino International Airport |  | PH | 527 |
| 28 | Daniel K Inouye International Airport |  | US | 512 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 510 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 494 |
| 31 | Barcelona International Airport |  | ES | 486 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 477 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 467 |
| 34 | Vitoria/Foronda Airport |  | ES | 464 |
| 35 | Don Mueang International Airport |  | TH | 445 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 442 |
| 37 | O. R. Tambo International Airport |  | ZA | 438 |
| 38 | Amsterdam Airport Schiphol |  | NL | 430 |
| 39 | Reno/Tahoe International Airport |  | US | 416 |
| 40 | Calgary International Airport |  | CA | 415 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 353 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 262 | 1h 7m | 706 km | 3,189.9 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 242 | 21m | 244 km | 1,019.0 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 209 | 24m | 225 km | 810.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 195 | 28m | 304 km | 1,022.2 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 175 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 172 | 20m | 165 km | 489.3 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 168 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 157 | 26m | 275 km | 744.0 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 155 | 1h 12m | 770 km | 2,059.1 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 128 | 44m | 452 km | 997.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 105 | 20m | 147 km | 265.7 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 99 | 14m | 154 km | 262.3 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 97 | 1h 2m | 695 km | 1,162.7 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 94 | 1h 43m | 1,423 km | 2,306.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |
| 30 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| R21236 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-05 23:07 UTC | 2026-05-05 23:51 UTC | 44m |
| QXE2077 | QXE | Boise Air Trml/Gowen Field (KBOI) | Seattle-Tacoma International Airport (KSEA) | 2026-05-05 22:42 UTC | 2026-05-05 23:50 UTC | 1h 8m |
| N661WA |  | Bear Valley Skyranch Airport (WN47) | Sanderson Field (KSHN) | 2026-05-05 23:34 UTC | 2026-05-05 23:49 UTC | 14m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-05 23:09 UTC | 2026-05-05 23:40 UTC | 31m |
| N125CL |  | Easton State Airport (KESW) | Burnett Landing Airport (WN15) | 2026-05-05 23:21 UTC | 2026-05-05 23:40 UTC | 18m |
| TQR | TQR | Romsey (Riddell/Penfield) Airport (YRSY) | Melbourne Essendon Airport (YMEN) | 2026-05-05 23:21 UTC | 2026-05-05 23:39 UTC | 18m |
| URSA06 | URS | Gold King Creek Airport (PAAN) | Ladd Army Air Field (PAFB) | 2026-05-05 22:31 UTC | 2026-05-05 23:33 UTC | 1h 2m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 23:19 UTC | 2026-05-05 23:31 UTC | 12m |
| ABB852 | ABB | Brussels Airport (EBBR) | Macau International Airport (VMMC) | 2026-05-05 11:39 UTC | 2026-05-05 23:27 UTC | 11h 47m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-05 11:45 UTC | 2026-05-05 23:20 UTC | 11h 35m |
| ARCAT55 | ARC | Gillespie Field (KSEE) | Osborne Airport (8CA0) | 2026-05-05 22:54 UTC | 2026-05-05 23:19 UTC | 24m |
| N2123L |  | Yuba County Airport (KMYV) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-05 22:41 UTC | 2026-05-05 23:17 UTC | 35m |
| ES807 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-05 23:08 UTC | 2026-05-05 23:16 UTC | 8m |
| MSA61P | MSA | Brescia / Montichiari Airport (LIPO) | Ghisonaccia Alzitone Airport (LFKG) | 2026-05-05 22:33 UTC | 2026-05-05 23:14 UTC | 40m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-05 23:07 UTC | 2026-05-05 23:12 UTC | 5m |
| EJM304 | EJM | Teterboro Airport (KTEB) | Scottsdale Airport (KSDL) | 2026-05-05 17:09 UTC | 2026-05-05 23:09 UTC | 6h 0m |
| N39CK |  | Melbourne Orlando International Airport (KMLB) | Sebastian Municipal Airport (KX26) | 2026-05-05 22:40 UTC | 2026-05-05 23:08 UTC | 28m |
| AM235 |  | Port Macquarie Airport (YPMQ) | Woodville Airport (YWVL) | 2026-05-05 22:37 UTC | 2026-05-05 23:04 UTC | 27m |
| VOZ9235 | Virgin Australia | Perth International Airport (YPPH) | Denmark Airport (YDEK) | 2026-05-05 22:31 UTC | 2026-05-05 23:04 UTC | 33m |
| SWA2300 | Southwest Airlines | El Paso International Airport (KELP) | San Antonio International Airport (KSAT) | 2026-05-05 22:01 UTC | 2026-05-05 22:59 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
