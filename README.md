# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_16:50:58_UTC-green)

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

**Latest saved flight:** 2026-05-04 16:50:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-04 16:50:58 UTC

- **67,907** saved flights
- **25,523** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **67,907** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **834,212.4 tonnes** estimated CO2 emissions
- **48,360,141 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2916 |
| 2 | SkyWest Airlines | 2496 |
| 3 | IndiGo | 1579 |
| 4 | EJA | 1211 |
| 5 | American Airlines | 1049 |
| 6 | Southwest Airlines | 953 |
| 7 | Lufthansa | 873 |
| 8 | ENY | 832 |
| 9 | Vueling | 669 |
| 10 | AXM | 658 |
| 11 | LATAM Airlines | 632 |
| 12 | All Nippon Airways | 579 |
| 13 | WIF | 572 |
| 14 | Delta Air Lines | 567 |
| 15 | AZU | 549 |
| 16 | Swiss International | 527 |
| 17 | QLK | 523 |
| 18 | LXJ | 492 |
| 19 | Alaska Airlines | 459 |
| 20 | easyJet | 452 |
| 21 | AEE | 451 |
| 22 | EJU | 442 |
| 23 | VIV | 423 |
| 24 | Cathay Pacific | 410 |
| 25 | Air France | 401 |
| 26 | Japan Airlines | 399 |
| 27 | AXB | 385 |
| 28 | AIQ | 346 |
| 29 | CXK | 345 |
| 30 | MXY | 330 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 53571 |
| 2 | 🇪🇸 ES | 4978 |
| 3 | 🇮🇳 IN | 4973 |
| 4 | 🇦🇺 AU | 4497 |
| 5 | 🇧🇷 BR | 3811 |
| 6 | 🇩🇪 DE | 3809 |
| 7 | 🇮🇹 IT | 3727 |
| 8 | 🇯🇵 JP | 3667 |
| 9 | 🇨🇦 CA | 3334 |
| 10 | 🇬🇧 GB | 2950 |
| 11 | 🇫🇷 FR | 2703 |
| 12 | 🇨🇴 CO | 2655 |
| 13 | 🇲🇽 MX | 2155 |
| 14 | 🇬🇷 GR | 2054 |
| 15 | 🇨🇭 CH | 1898 |
| 16 | 🇳🇴 NO | 1854 |
| 17 | 🇲🇾 MY | 1635 |
| 18 | 🇿🇦 ZA | 1369 |
| 19 | 🇳🇿 NZ | 1264 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1218 |
| 22 | 🇵🇭 PH | 1137 |
| 23 | 🇵🇱 PL | 1113 |
| 24 | 🇬🇹 GT | 1102 |
| 25 | 🇰🇷 KR | 1089 |
| 26 | 🇲🇦 MA | 828 |
| 27 | 🇲🇴 MO | 768 |
| 28 | 🇲🇪 ME | 736 |
| 29 | 🇳🇱 NL | 713 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1487 |
| 2 | Tokyo International Airport |  | JP | 1235 |
| 3 | Denver International Airport |  | US | 1114 |
| 4 | Indira Gandhi International Airport |  | IN | 1039 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1002 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Frankfurt am Main International Airport |  | DE | 876 |
| 8 | Guaymaral Airport |  | CO | 850 |
| 9 | Harry Reid International Airport |  | US | 842 |
| 10 | La Aurora Airport |  | GT | 819 |
| 11 | Zurich Airport |  | CH | 812 |
| 12 | Macau International Airport |  | MO | 768 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 665 |
| 14 | Kuala Lumpur International Airport |  | MY | 656 |
| 15 | Madrid Barajas International Airport |  | ES | 650 |
| 16 | Chicago O'Hare International Airport |  | US | 648 |
| 17 | Bengaluru International Airport |  | IN | 603 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 602 |
| 19 | Malpensa International Airport |  | IT | 593 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 591 |
| 21 | Congonhas Airport |  | BR | 547 |
| 22 | Salt Lake City International Airport |  | US | 539 |
| 23 | Charles de Gaulle International Airport |  | FR | 536 |
| 24 | Tenerife Norte Airport |  | ES | 535 |
| 25 | Charlotte/Douglas International Airport |  | US | 534 |
| 26 | Capua Airport |  | IT | 520 |
| 27 | Ninoy Aquino International Airport |  | PH | 517 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 501 |
| 29 | Daniel K Inouye International Airport |  | US | 492 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 478 |
| 31 | Barcelona International Airport |  | ES | 472 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 459 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 451 |
| 34 | Vitoria/Foronda Airport |  | ES | 450 |
| 35 | O. R. Tambo International Airport |  | ZA | 433 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 425 |
| 38 | Amsterdam Airport Schiphol |  | NL | 420 |
| 39 | Reno/Tahoe International Airport |  | US | 406 |
| 40 | Calgary International Airport |  | CA | 400 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 351 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 230 | 21m | 244 km | 968.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 194 | 1h 27m | 910 km | 3,044.3 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 170 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 152 | 26m | 275 km | 720.3 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 151 | 1h 12m | 770 km | 2,005.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 129 | 21m | 99 km | 221.0 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 124 | 44m | 452 km | 966.4 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 114 | 27m | 152 km | 297.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 113 | 31m | 369 km | 719.3 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 97 | 1h 41m | 1,156 km | 1,935.1 t |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 96 | 14m | 154 km | 254.4 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 94 | 1h 2m | 695 km | 1,126.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 92 | 1h 43m | 1,423 km | 2,257.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 92 | 1h 53m | 1,304 km | 2,069.8 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 91 | 52m | 556 km | 872.3 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 86 | 1h 19m | 961 km | 1,425.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR851 | VAR | Avi Suquilla Airport (KP20) | Lake Havasu City Airport (KHII) | 2026-05-04 16:32 UTC | 2026-05-04 16:50 UTC | 18m |
| DHK890 | DHK | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-05-04 09:58 UTC | 2026-05-04 16:50 UTC | 6h 52m |
| N172KJ |  | Aurora Municipal Airport (KARR) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-04 16:27 UTC | 2026-05-04 16:45 UTC | 17m |
| CGBCM | CGB | Sechelt-Gibsons Airport (CAP3) | Vancouver International Airport (CYVR) | 2026-05-04 16:23 UTC | 2026-05-04 16:36 UTC | 13m |
| HOOK52 | HOO | 75OK (75OK) | Anthony Municipal Airport (KANY) | 2026-05-04 15:45 UTC | 2026-05-04 16:32 UTC | 46m |
| N702LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Brookneal/Campbell County Airport (K0V4) | 2026-05-04 16:19 UTC | 2026-05-04 16:30 UTC | 10m |
| N96EX |  | Steamboat Springs/Bob Adams Field (KSBS) | Steamboat Springs/Bob Adams Field (KSBS) | 2026-05-04 16:15 UTC | 2026-05-04 16:29 UTC | 14m |
| N171SF |  | Dupage Airport (KDPA) | IS63 (IS63) | 2026-05-04 15:59 UTC | 2026-05-04 16:29 UTC | 29m |
| N924MC |  | Nashville International Airport (KBNA) | Bowling Green-Warren County Regional Airport (KBWG) | 2026-05-04 15:32 UTC | 2026-05-04 16:26 UTC | 53m |
| ATAC11 | ATA | Luke Afb Airport (KLUF) | AZ00 (AZ00) | 2026-05-04 16:05 UTC | 2026-05-04 16:25 UTC | 19m |
| N6640F |  | Manassas Regional/Harry P Davis Field (KHEF) | Rular Airport (VG07) | 2026-05-04 15:24 UTC | 2026-05-04 16:23 UTC | 58m |
| N862MC |  | 6FD7 (6FD7) | 6FD7 (6FD7) | 2026-05-04 16:10 UTC | 2026-05-04 16:23 UTC | 12m |
| EJM71 | EJM | Philadelphia International Airport (KPHL) | Nashville International Airport (KBNA) | 2026-05-04 14:34 UTC | 2026-05-04 16:23 UTC | 1h 49m |
| SCU8 | SCU | Haskell Airport (K2K9) | Haskell Airport (K2K9) | 2026-05-04 16:14 UTC | 2026-05-04 16:20 UTC | 6m |
| CFMES | CFM | Calgary International Airport (CYYC) | Ponoka Industrial Airport (CEH3) | 2026-05-04 16:01 UTC | 2026-05-04 16:20 UTC | 18m |
| VLG83HR | Vueling | Barcelona International Airport (LEBL) | Federico Garcia Lorca Airport (LEGR) | 2026-05-04 15:18 UTC | 2026-05-04 16:20 UTC | 1h 2m |
| N885G |  | K00V (K00V) | Limon Municipal Airport (KLIC) | 2026-05-04 15:51 UTC | 2026-05-04 16:19 UTC | 28m |
| N600ML |  | Roberts Field (KRDM) | Bowers Field (KELN) | 2026-05-04 15:33 UTC | 2026-05-04 16:19 UTC | 45m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-05-04 15:46 UTC | 2026-05-04 16:18 UTC | 32m |
| N121NG |  | KM33 (KM33) | KM33 (KM33) | 2026-05-04 15:58 UTC | 2026-05-04 16:18 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
