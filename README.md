# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_19:44:18_UTC-green)

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

**Latest saved flight:** 2026-05-17 19:44:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 19:44:18 UTC

- **86,715** saved flights
- **31,052** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,715** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,072,824.6 tonnes** estimated CO2 emissions
- **62,192,730 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3722 |
| 2 | SkyWest Airlines | 3205 |
| 3 | IndiGo | 1866 |
| 4 | EJA | 1630 |
| 5 | American Airlines | 1327 |
| 6 | Southwest Airlines | 1260 |
| 7 | Lufthansa | 1098 |
| 8 | ENY | 1074 |
| 9 | Delta Air Lines | 949 |
| 10 | Vueling | 826 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 781 |
| 13 | WIF | 742 |
| 14 | AZU | 677 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 666 |
| 17 | LXJ | 638 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 613 |
| 20 | easyJet | 574 |
| 21 | EJU | 558 |
| 22 | Cathay Pacific | 550 |
| 23 | AEE | 542 |
| 24 | VIV | 521 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 458 |
| 28 | AXB | 455 |
| 29 | MXY | 436 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70927 |
| 2 | 🇪🇸 ES | 6158 |
| 3 | 🇮🇳 IN | 5836 |
| 4 | 🇦🇺 AU | 5477 |
| 5 | 🇩🇪 DE | 4844 |
| 6 | 🇮🇹 IT | 4808 |
| 7 | 🇧🇷 BR | 4751 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4303 |
| 10 | 🇬🇧 GB | 3716 |
| 11 | 🇫🇷 FR | 3475 |
| 12 | 🇨🇴 CO | 2923 |
| 13 | 🇲🇽 MX | 2687 |
| 14 | 🇬🇷 GR | 2525 |
| 15 | 🇳🇴 NO | 2396 |
| 16 | 🇨🇭 CH | 2310 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1571 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1444 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1303 |
| 26 | 🇲🇦 MA | 1010 |
| 27 | 🇲🇴 MO | 1007 |
| 28 | 🇲🇪 ME | 902 |
| 29 | 🇳🇱 NL | 885 |
| 30 | 🇭🇷 HR | 780 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1895 |
| 2 | Denver International Airport |  | US | 1451 |
| 3 | Tokyo International Airport |  | JP | 1443 |
| 4 | Indira Gandhi International Airport |  | IN | 1252 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1203 |
| 6 | Frankfurt am Main International Airport |  | DE | 1110 |
| 7 | Harry Reid International Airport |  | US | 1099 |
| 8 | Zurich Airport |  | CH | 1038 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | La Aurora Airport |  | GT | 990 |
| 11 | Guaymaral Airport |  | CO | 989 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 958 |
| 13 | El Dorado International Airport |  | CO | 936 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 872 |
| 15 | Chicago O'Hare International Airport |  | US | 837 |
| 16 | Madrid Barajas International Airport |  | ES | 791 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 746 |
| 19 | Capua Airport |  | IT | 729 |
| 20 | Salt Lake City International Airport |  | US | 724 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 22 | Malpensa International Airport |  | IT | 712 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 678 |
| 25 | Charlotte/Douglas International Airport |  | US | 671 |
| 26 | Congonhas Airport |  | BR | 666 |
| 27 | Tenerife Norte Airport |  | ES | 638 |
| 28 | Daniel K Inouye International Airport |  | US | 634 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 593 |
| 32 | Barcelona International Airport |  | ES | 581 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 577 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 558 |
| 35 | Vitoria/Foronda Airport |  | ES | 555 |
| 36 | Don Mueang International Airport |  | TH | 545 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 544 |
| 38 | Amsterdam Airport Schiphol |  | NL | 540 |
| 39 | O. R. Tambo International Airport |  | ZA | 510 |
| 40 | Calgary International Airport |  | CA | 509 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 321 | 21m | 244 km | 1,351.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 223 | 14m | 114 km | 437.4 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 221 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 131 | 27m | 152 km | 342.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 111 | 18m | 144 km | 276.1 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 110 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 105 | 1h 52m | 1,304 km | 2,362.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGNND | CGN | Colonial Airport (NY24) | Colonial Airport (NY24) | 2026-05-17 18:11 UTC | 2026-05-17 19:44 UTC | 1h 33m |
| CXK678 | CXK | Santa Barbara Municipal Airport (KSBA) | Riverside Airport (KRAL) | 2026-05-17 18:20 UTC | 2026-05-17 19:37 UTC | 1h 16m |
| VTM434 | VTM | Plan De Guadalupe International Airport (MMIO) | Monclova International Airport (MMMV) | 2026-05-17 19:17 UTC | 2026-05-17 19:36 UTC | 19m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-17 19:22 UTC | 2026-05-17 19:36 UTC | 14m |
| THA925 | Thai Airways | Munich International Airport (EDDM) | Jhansi Airport (VIJN) | 2026-05-17 12:38 UTC | 2026-05-17 19:32 UTC | 6h 54m |
| N89770 |  | Zamperini Field (KTOA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-05-17 18:47 UTC | 2026-05-17 19:30 UTC | 43m |
| N1285W |  | John Wayne/Orange County Airport (KSNA) | Santa Barbara Municipal Airport (KSBA) | 2026-05-17 18:27 UTC | 2026-05-17 19:27 UTC | 1h 0m |
| N875JP |  | Lykes Silver Lake Airport (FL36) | Orlando Executive Airport (KORL) | 2026-05-17 19:02 UTC | 2026-05-17 19:26 UTC | 23m |
| N751FB |  | Johnson County Executive Airport (KOJC) | Rosenberg Airport (MY80) | 2026-05-17 18:16 UTC | 2026-05-17 19:25 UTC | 1h 8m |
| N981BB |  | Ted Stevens Anchorage International Airport (PANC) | Wasilla Airport (PAWS) | 2026-05-17 18:54 UTC | 2026-05-17 19:24 UTC | 29m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-17 19:06 UTC | 2026-05-17 19:23 UTC | 17m |
| N26T |  | Birmingham-Shuttlesworth International Airport (KBHM) | Southwest Georgia Regional Airport (KABY) | 2026-05-17 18:45 UTC | 2026-05-17 19:20 UTC | 35m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-17 18:41 UTC | 2026-05-17 19:19 UTC | 38m |
| N750LC |  | John C Tune Airport (KJWN) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-17 18:08 UTC | 2026-05-17 19:13 UTC | 1h 5m |
| N700FP |  | Palo Alto Airport (KPAO) | Fall River Mills Airport (KO89) | 2026-05-17 18:12 UTC | 2026-05-17 19:12 UTC | 59m |
| N267JK |  | Venice Municipal Airport (KVNC) | White Oak Stand Airport (VA11) | 2026-05-17 17:07 UTC | 2026-05-17 19:10 UTC | 2h 2m |
| N541WS |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-05-17 18:51 UTC | 2026-05-17 19:10 UTC | 18m |
| N8224K |  | Chino Airport (KCNO) | Riverside Airport (KRAL) | 2026-05-17 18:52 UTC | 2026-05-17 19:08 UTC | 16m |
| N423LL |  | Herr Brothers Airport (NJ95) | Sky Manor Airport (KN40) | 2026-05-17 18:40 UTC | 2026-05-17 19:08 UTC | 27m |
| CGNTZ | CGN | Tucson International Airport (KTUS) | UT09 (UT09) | 2026-05-17 17:24 UTC | 2026-05-17 19:05 UTC | 1h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
