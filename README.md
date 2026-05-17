# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_22:39:27_UTC-green)

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

**Latest saved flight:** 2026-05-17 22:39:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 22:39:27 UTC

- **86,979** saved flights
- **31,146** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,979** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,076,482.2 tonnes** estimated CO2 emissions
- **62,404,766 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3730 |
| 2 | SkyWest Airlines | 3222 |
| 3 | IndiGo | 1866 |
| 4 | EJA | 1643 |
| 5 | American Airlines | 1333 |
| 6 | Southwest Airlines | 1265 |
| 7 | Lufthansa | 1098 |
| 8 | ENY | 1079 |
| 9 | Delta Air Lines | 953 |
| 10 | Vueling | 828 |
| 11 | LATAM Airlines | 784 |
| 12 | AXM | 782 |
| 13 | WIF | 742 |
| 14 | AZU | 684 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 641 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 616 |
| 20 | easyJet | 575 |
| 21 | EJU | 560 |
| 22 | Cathay Pacific | 553 |
| 23 | AEE | 542 |
| 24 | VIV | 522 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 459 |
| 28 | AXB | 455 |
| 29 | MXY | 439 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71252 |
| 2 | 🇪🇸 ES | 6169 |
| 3 | 🇮🇳 IN | 5837 |
| 4 | 🇦🇺 AU | 5480 |
| 5 | 🇩🇪 DE | 4848 |
| 6 | 🇮🇹 IT | 4820 |
| 7 | 🇧🇷 BR | 4775 |
| 8 | 🇯🇵 JP | 4323 |
| 9 | 🇨🇦 CA | 4322 |
| 10 | 🇬🇧 GB | 3721 |
| 11 | 🇫🇷 FR | 3480 |
| 12 | 🇨🇴 CO | 2928 |
| 13 | 🇲🇽 MX | 2699 |
| 14 | 🇬🇷 GR | 2527 |
| 15 | 🇳🇴 NO | 2401 |
| 16 | 🇨🇭 CH | 2310 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1576 |
| 20 | 🇳🇿 NZ | 1513 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1445 |
| 23 | 🇵🇭 PH | 1354 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1307 |
| 26 | 🇲🇴 MO | 1011 |
| 27 | 🇲🇦 MA | 1010 |
| 28 | 🇲🇪 ME | 904 |
| 29 | 🇳🇱 NL | 889 |
| 30 | 🇭🇷 HR | 783 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1908 |
| 2 | Denver International Airport |  | US | 1456 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1253 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1203 |
| 6 | Frankfurt am Main International Airport |  | DE | 1110 |
| 7 | Harry Reid International Airport |  | US | 1102 |
| 8 | Zurich Airport |  | CH | 1038 |
| 9 | Macau International Airport |  | MO | 1011 |
| 10 | La Aurora Airport |  | GT | 993 |
| 11 | Guaymaral Airport |  | CO | 990 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 963 |
| 13 | El Dorado International Airport |  | CO | 939 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 876 |
| 15 | Chicago O'Hare International Airport |  | US | 843 |
| 16 | Madrid Barajas International Airport |  | ES | 793 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 748 |
| 19 | Capua Airport |  | IT | 731 |
| 20 | Salt Lake City International Airport |  | US | 726 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 716 |
| 22 | Malpensa International Airport |  | IT | 714 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 679 |
| 25 | Charlotte/Douglas International Airport |  | US | 675 |
| 26 | Congonhas Airport |  | BR | 668 |
| 27 | Tenerife Norte Airport |  | ES | 639 |
| 28 | Daniel K Inouye International Airport |  | US | 637 |
| 29 | Ninoy Aquino International Airport |  | PH | 620 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 594 |
| 32 | Barcelona International Airport |  | ES | 584 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 578 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 558 |
| 35 | Vitoria/Foronda Airport |  | ES | 555 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 547 |
| 37 | Don Mueang International Airport |  | TH | 545 |
| 38 | Amsterdam Airport Schiphol |  | NL | 543 |
| 39 | Calgary International Airport |  | CA | 511 |
| 40 | O. R. Tambo International Airport |  | ZA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 323 | 21m | 244 km | 1,360.1 t |
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
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 111 | 18m | 144 km | 276.1 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 105 | 1h 52m | 1,304 km | 2,362.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N38HF |  | Groton-New London Airport (KGON) | Francis S Gabreski Airport (KFOK) | 2026-05-17 22:20 UTC | 2026-05-17 22:39 UTC | 18m |
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Cuchara Valley At La Veta Airport (K07V) | 2026-05-17 22:05 UTC | 2026-05-17 22:28 UTC | 22m |
| GPD82 | GPD | Nantucket Memorial Airport (KACK) | Teterboro Airport (KTEB) | 2026-05-17 21:23 UTC | 2026-05-17 22:20 UTC | 56m |
| N123TN |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-05-17 20:05 UTC | 2026-05-17 22:14 UTC | 2h 9m |
| TKR104 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Springfield Municipal Airport (K8V7) | 2026-05-17 21:46 UTC | 2026-05-17 22:14 UTC | 27m |
| TKR102 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | 6CO3 (6CO3) | 2026-05-17 21:53 UTC | 2026-05-17 22:14 UTC | 21m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-17 22:01 UTC | 2026-05-17 22:12 UTC | 11m |
| N684TH |  | Norfolk International Airport (KORF) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-17 20:47 UTC | 2026-05-17 22:12 UTC | 1h 24m |
| TKR136 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Tercio Ranch Airstrip (3CO4) | 2026-05-17 21:37 UTC | 2026-05-17 22:07 UTC | 29m |
| ZKHWD | ZKH | Christchurch International Airport (NZCH) | Christchurch International Airport (NZCH) | 2026-05-17 21:50 UTC | 2026-05-17 22:04 UTC | 13m |
| N236ZK |  | Republic Airport (KFRG) | Groton-New London Airport (KGON) | 2026-05-17 21:15 UTC | 2026-05-17 22:03 UTC | 48m |
| N949SP |  | St Mary's County Regional Airport (K2W6) | St Mary's County Regional Airport (K2W6) | 2026-05-17 22:00 UTC | 2026-05-17 22:03 UTC | 2m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-05-17 10:43 UTC | 2026-05-17 22:02 UTC | 11h 18m |
| N393BZ |  | Boeing Field/King County International Airport (KBFI) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-17 20:32 UTC | 2026-05-17 22:01 UTC | 1h 29m |
| N74ZC |  | Boeing Field/King County International Airport (KBFI) | MT88 (MT88) | 2026-05-17 21:18 UTC | 2026-05-17 22:00 UTC | 42m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-05-17 11:08 UTC | 2026-05-17 21:57 UTC | 10h 48m |
| XAUKI | XAU | General Heriberto Jara International Airport (MMVR) | Licenciado Adolfo Lopez Mateos International Airport (MMTO) | 2026-05-17 21:02 UTC | 2026-05-17 21:54 UTC | 52m |
| N738AE |  | Rhines Roost Airport (91TA) | Pritchard Airport (99TE) | 2026-05-17 21:13 UTC | 2026-05-17 21:53 UTC | 39m |
| BALL11 | BAL | Mesa Gateway Airport (KIWA) | H A Clark Memorial Field (KCMR) | 2026-05-17 21:16 UTC | 2026-05-17 21:48 UTC | 31m |
| AZG5792 | AZG | Václav Havel Airport (LKPR) | Macau International Airport (VMMC) | 2026-05-17 06:42 UTC | 2026-05-17 21:47 UTC | 15h 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
