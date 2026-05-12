# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_19:49:49_UTC-green)

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

**Latest saved flight:** 2026-05-12 19:49:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-12 19:49:49 UTC

- **79,472** saved flights
- **28,901** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **79,472** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **982,508.7 tonnes** estimated CO2 emissions
- **56,957,023 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3433 |
| 2 | SkyWest Airlines | 2952 |
| 3 | IndiGo | 1761 |
| 4 | EJA | 1463 |
| 5 | American Airlines | 1236 |
| 6 | Southwest Airlines | 1162 |
| 7 | Lufthansa | 1048 |
| 8 | ENY | 989 |
| 9 | Delta Air Lines | 867 |
| 10 | Vueling | 763 |
| 11 | AXM | 729 |
| 12 | LATAM Airlines | 721 |
| 13 | WIF | 690 |
| 14 | All Nippon Airways | 636 |
| 15 | AZU | 623 |
| 16 | Swiss International | 617 |
| 17 | QLK | 592 |
| 18 | LXJ | 576 |
| 19 | Alaska Airlines | 557 |
| 20 | easyJet | 532 |
| 21 | EJU | 515 |
| 22 | AEE | 513 |
| 23 | Cathay Pacific | 503 |
| 24 | VIV | 472 |
| 25 | Air France | 470 |
| 26 | Japan Airlines | 453 |
| 27 | AXB | 438 |
| 28 | CXK | 410 |
| 29 | AIQ | 397 |
| 30 | MXY | 396 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 64367 |
| 2 | 🇪🇸 ES | 5684 |
| 3 | 🇮🇳 IN | 5512 |
| 4 | 🇦🇺 AU | 5089 |
| 5 | 🇩🇪 DE | 4511 |
| 6 | 🇮🇹 IT | 4423 |
| 7 | 🇧🇷 BR | 4385 |
| 8 | 🇯🇵 JP | 4073 |
| 9 | 🇨🇦 CA | 3959 |
| 10 | 🇬🇧 GB | 3425 |
| 11 | 🇫🇷 FR | 3163 |
| 12 | 🇨🇴 CO | 2707 |
| 13 | 🇲🇽 MX | 2398 |
| 14 | 🇬🇷 GR | 2342 |
| 15 | 🇳🇴 NO | 2211 |
| 16 | 🇨🇭 CH | 2150 |
| 17 | 🇲🇾 MY | 1828 |
| 18 | 🇿🇦 ZA | 1510 |
| 19 | 🇹🇷 TR | 1433 |
| 20 | 🇹🇭 TH | 1408 |
| 21 | 🇳🇿 NZ | 1402 |
| 22 | 🇵🇱 PL | 1329 |
| 23 | 🇵🇭 PH | 1260 |
| 24 | 🇰🇷 KR | 1224 |
| 25 | 🇬🇹 GT | 1222 |
| 26 | 🇲🇦 MA | 938 |
| 27 | 🇲🇴 MO | 924 |
| 28 | 🇲🇪 ME | 854 |
| 29 | 🇳🇱 NL | 827 |
| 30 | 🇭🇷 HR | 703 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1743 |
| 2 | Tokyo International Airport |  | JP | 1370 |
| 3 | Denver International Airport |  | US | 1331 |
| 4 | Indira Gandhi International Airport |  | IN | 1166 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1148 |
| 6 | Frankfurt am Main International Airport |  | DE | 1051 |
| 7 | Harry Reid International Airport |  | US | 984 |
| 8 | Zurich Airport |  | CH | 948 |
| 9 | Macau International Airport |  | MO | 924 |
| 10 | La Aurora Airport |  | GT | 920 |
| 11 | Guaymaral Airport |  | CO | 899 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 888 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 806 |
| 15 | Chicago O'Hare International Airport |  | US | 775 |
| 16 | Madrid Barajas International Airport |  | ES | 732 |
| 17 | Kuala Lumpur International Airport |  | MY | 730 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 699 |
| 19 | Malpensa International Airport |  | IT | 684 |
| 20 | Bengaluru International Airport |  | IN | 679 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 675 |
| 22 | Salt Lake City International Airport |  | US | 650 |
| 23 | Capua Airport |  | IT | 650 |
| 24 | Charlotte/Douglas International Airport |  | US | 626 |
| 25 | Charles de Gaulle International Airport |  | FR | 624 |
| 26 | Congonhas Airport |  | BR | 618 |
| 27 | Tenerife Norte Airport |  | ES | 592 |
| 28 | Daniel K Inouye International Airport |  | US | 577 |
| 29 | Ninoy Aquino International Airport |  | PH | 574 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 570 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 534 |
| 32 | Barcelona International Airport |  | ES | 534 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 529 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 522 |
| 35 | Vitoria/Foronda Airport |  | ES | 507 |
| 36 | Don Mueang International Airport |  | TH | 504 |
| 37 | Amsterdam Airport Schiphol |  | NL | 500 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 492 |
| 39 | O. R. Tambo International Airport |  | ZA | 477 |
| 40 | Calgary International Airport |  | CA | 467 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 374 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 285 | 21m | 244 km | 1,200.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 227 | 24m | 225 km | 880.7 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 212 | 1h 27m | 910 km | 3,326.8 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 202 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 190 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 177 | 1h 11m | 770 km | 2,351.3 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 169 | 26m | 275 km | 800.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 125 | 31m | 369 km | 795.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 117 | 20m | 147 km | 296.1 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 115 | 20m | 250 km | 496.7 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 113 | 14m | 154 km | 299.4 t |
| 22 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 108 | 23m | 55 km | 102.7 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 106 | 57m | 493 km | 901.8 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 105 | 1h 42m | 1,423 km | 2,576.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 105 | 1h 2m | 695 km | 1,258.6 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 101 | 18m | 144 km | 251.2 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 100 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 100 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N256J |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-05-12 18:51 UTC | 2026-05-12 19:49 UTC | 58m |
| DAL824 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Harry Reid International Airport (KLAS) | 2026-05-12 15:50 UTC | 2026-05-12 19:41 UTC | 3h 50m |
| YETI36 | YET | Elmendorf Afb Airport (PAED) | Highland Airport (47AK) | 2026-05-12 18:26 UTC | 2026-05-12 19:39 UTC | 1h 13m |
| N227AT |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-05-12 19:03 UTC | 2026-05-12 19:39 UTC | 35m |
| N916J |  | Alexandria Regional/Chandler Field (KAXN) | 6KS6 (6KS6) | 2026-05-12 18:19 UTC | 2026-05-12 19:37 UTC | 1h 17m |
| N2207E |  | KS67 (KS67) | Emmett Municipal Airport (KS78) | 2026-05-12 19:19 UTC | 2026-05-12 19:37 UTC | 18m |
| WAH | WAH | Trading Bay Production Airport (5AK0) | Kenai Municipal Airport (PAEN) | 2026-05-12 19:21 UTC | 2026-05-12 19:36 UTC | 15m |
| N1978F |  | Truckee-Tahoe Airport (KTRK) | Sacramento Executive Airport (KSAC) | 2026-05-12 19:00 UTC | 2026-05-12 19:35 UTC | 35m |
| N219TX |  | Rolla Ntl Airport (KVIH) | Austin-Bergstrom International Airport (KAUS) | 2026-05-12 17:06 UTC | 2026-05-12 19:30 UTC | 2h 24m |
|  |  | Eielson Afb Airport (PAEI) | Eielson Afb Airport (PAEI) | 2026-05-12 19:01 UTC | 2026-05-12 19:29 UTC | 28m |
| CGNUE | CGN | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-05-12 18:49 UTC | 2026-05-12 19:29 UTC | 40m |
| N870BR |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-05-12 18:57 UTC | 2026-05-12 19:27 UTC | 30m |
| N140CD |  | Duluth International Airport (KDLH) | Richard B Helgeson Airport (KTWM) | 2026-05-12 19:14 UTC | 2026-05-12 19:25 UTC | 11m |
| N53HT |  | Triangle North Executive Airport (KLHZ) | Triangle North Executive Airport (KLHZ) | 2026-05-12 19:10 UTC | 2026-05-12 19:24 UTC | 13m |
| RYR12YU | Ryanair | Palma De Mallorca Airport (LEPA) | Bournemouth Airport (EGHH) | 2026-05-12 17:20 UTC | 2026-05-12 19:23 UTC | 2h 2m |
| RYR4171 | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-05-12 19:05 UTC | 2026-05-12 19:22 UTC | 17m |
| N7426 |  | Eugene F Kranz Toledo Express Airport (KTOL) | John Glenn Columbus International Airport (KCMH) | 2026-05-12 18:55 UTC | 2026-05-12 19:21 UTC | 25m |
| N793FS |  | Bob Hope Airport (KBUR) | Meadows Field (KBFL) | 2026-05-12 18:53 UTC | 2026-05-12 19:19 UTC | 26m |
| N665PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Los Alamitos Army Air Field (KSLI) | 2026-05-12 19:05 UTC | 2026-05-12 19:17 UTC | 11m |
| N628G |  | Scottsdale Airport (KSDL) | Conway-Horry County Airport (KHYW) | 2026-05-12 15:52 UTC | 2026-05-12 19:16 UTC | 3h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
