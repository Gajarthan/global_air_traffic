# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_01:12:10_UTC-green)

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

**Latest saved flight:** 2026-05-16 01:12:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 01:12:10 UTC

- **84,112** saved flights
- **30,346** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,112** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,034,283.0 tonnes** estimated CO2 emissions
- **59,958,437 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3595 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1810 |
| 4 | EJA | 1593 |
| 5 | American Airlines | 1295 |
| 6 | Southwest Airlines | 1235 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 921 |
| 10 | Vueling | 795 |
| 11 | LATAM Airlines | 762 |
| 12 | AXM | 752 |
| 13 | WIF | 726 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 654 |
| 16 | Swiss International | 648 |
| 17 | QLK | 619 |
| 18 | LXJ | 618 |
| 19 | Alaska Airlines | 595 |
| 20 | easyJet | 552 |
| 21 | EJU | 534 |
| 22 | AEE | 530 |
| 23 | Cathay Pacific | 525 |
| 24 | VIV | 505 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 469 |
| 27 | CXK | 446 |
| 28 | AXB | 444 |
| 29 | MXY | 420 |
| 30 | United Airlines | 415 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69094 |
| 2 | 🇪🇸 ES | 5936 |
| 3 | 🇮🇳 IN | 5661 |
| 4 | 🇦🇺 AU | 5378 |
| 5 | 🇩🇪 DE | 4667 |
| 6 | 🇧🇷 BR | 4637 |
| 7 | 🇮🇹 IT | 4633 |
| 8 | 🇯🇵 JP | 4215 |
| 9 | 🇨🇦 CA | 4200 |
| 10 | 🇬🇧 GB | 3574 |
| 11 | 🇫🇷 FR | 3323 |
| 12 | 🇨🇴 CO | 2817 |
| 13 | 🇲🇽 MX | 2562 |
| 14 | 🇬🇷 GR | 2430 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2218 |
| 17 | 🇲🇾 MY | 1892 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1492 |
| 20 | 🇳🇿 NZ | 1485 |
| 21 | 🇹🇭 TH | 1454 |
| 22 | 🇵🇱 PL | 1393 |
| 23 | 🇵🇭 PH | 1314 |
| 24 | 🇰🇷 KR | 1286 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 976 |
| 27 | 🇲🇴 MO | 963 |
| 28 | 🇲🇪 ME | 886 |
| 29 | 🇳🇱 NL | 860 |
| 30 | 🇭🇷 HR | 752 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1847 |
| 2 | Denver International Airport |  | US | 1419 |
| 3 | Tokyo International Airport |  | JP | 1411 |
| 4 | Indira Gandhi International Airport |  | IN | 1203 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1180 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1057 |
| 8 | Zurich Airport |  | CH | 994 |
| 9 | La Aurora Airport |  | GT | 965 |
| 10 | Macau International Airport |  | MO | 963 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 907 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 847 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 765 |
| 17 | Kuala Lumpur International Airport |  | MY | 752 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 705 |
| 20 | Salt Lake City International Airport |  | US | 704 |
| 21 | Malpensa International Airport |  | IT | 700 |
| 22 | Bengaluru International Airport |  | IN | 695 |
| 23 | Capua Airport |  | IT | 683 |
| 24 | Congonhas Airport |  | BR | 656 |
| 25 | Charlotte/Douglas International Airport |  | US | 655 |
| 26 | Charles de Gaulle International Airport |  | FR | 654 |
| 27 | Daniel K Inouye International Airport |  | US | 607 |
| 28 | Tenerife Norte Airport |  | ES | 606 |
| 29 | Ninoy Aquino International Airport |  | PH | 601 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 569 |
| 32 | Barcelona International Airport |  | ES | 562 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 561 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 527 |
| 37 | Don Mueang International Airport |  | TH | 524 |
| 38 | Amsterdam Airport Schiphol |  | NL | 521 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 493 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 305 | 21m | 244 km | 1,284.3 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 274 | 1h 8m | 706 km | 3,336.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 238 | 24m | 225 km | 923.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 222 | 1h 26m | 910 km | 3,483.7 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 216 | 14m | 114 km | 423.6 t |
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
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XGN | XGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 00:58 UTC | 2026-05-16 01:12 UTC | 13m |
| N407SL |  | Cortez Municipal Airport (KCEZ) | Tanner Field (CO27) | 2026-05-16 00:20 UTC | 2026-05-16 01:09 UTC | 48m |
| R1651 |  | Watts Bridge Airport (YWSG) | Caloundra Airport (YCDR) | 2026-05-16 00:30 UTC | 2026-05-16 01:02 UTC | 31m |
| ZFO | ZFO | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-16 00:29 UTC | 2026-05-16 00:58 UTC | 29m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-16 00:22 UTC | 2026-05-16 00:58 UTC | 36m |
| JTL717 | JTL | Hot Springs Municipal Airport (KHSR) | Denver International Airport (KDEN) | 2026-05-16 00:03 UTC | 2026-05-16 00:54 UTC | 50m |
| NRF | NRF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 00:38 UTC | 2026-05-16 00:53 UTC | 14m |
| 83B |  | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 00:37 UTC | 2026-05-16 00:52 UTC | 14m |
| UAL4199 | United Airlines | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-16 00:37 UTC | 2026-05-16 00:52 UTC | 14m |
| N1334P |  | Space Coast Regional Airport (KTIX) | Space Coast Regional Airport (KTIX) | 2026-05-16 00:38 UTC | 2026-05-16 00:50 UTC | 12m |
| XCW | XCW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 00:35 UTC | 2026-05-16 00:49 UTC | 14m |
| CLX7625 | CLX | Luxembourg-Findel International Airport (ELLX) | Zhuhai Airport (ZGSD) | 2026-05-15 10:54 UTC | 2026-05-16 00:49 UTC | 13h 54m |
| N430CC |  | Charleston Afb/International Airport (KCHS) | Summerville Airport (KDYB) | 2026-05-16 00:05 UTC | 2026-05-16 00:48 UTC | 43m |
| N913SB |  | Peg Field (42CN) | Henderson Executive Airport (KHND) | 2026-05-15 23:54 UTC | 2026-05-16 00:44 UTC | 50m |
| AXEL90 | AXE | Roswell Air Center Airport (KROW) | NV13 (NV13) | 2026-05-15 22:35 UTC | 2026-05-16 00:43 UTC | 2h 8m |
| XGN | XGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-05-16 00:31 UTC | 2026-05-16 00:43 UTC | 11m |
| PCM7721 | PCM | Petaluma Municipal Airport (KO69) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-16 00:18 UTC | 2026-05-16 00:38 UTC | 20m |
| AMF1901 | AMF | Inyokern Airport (KIYK) | Mojave Air & Space Port/Rutan Field (KMHV) | 2026-05-16 00:25 UTC | 2026-05-16 00:37 UTC | 12m |
| N3584S |  | Shafter-Minter Field (KMIT) | Van Nuys Airport (KVNY) | 2026-05-15 23:45 UTC | 2026-05-16 00:36 UTC | 51m |
| N8241X |  | Chuckster Airport (XA17) | Chuckster Airport (XA17) | 2026-05-16 00:14 UTC | 2026-05-16 00:35 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
