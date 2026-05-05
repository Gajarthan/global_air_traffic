# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_00:55:25_UTC-green)

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

**Latest saved flight:** 2026-05-05 00:55:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-05 00:55:25 UTC

- **68,789** saved flights
- **25,797** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **68,789** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **845,234.9 tonnes** estimated CO2 emissions
- **48,999,126 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2948 |
| 2 | SkyWest Airlines | 2557 |
| 3 | IndiGo | 1581 |
| 4 | EJA | 1241 |
| 5 | American Airlines | 1068 |
| 6 | Southwest Airlines | 978 |
| 7 | Lufthansa | 880 |
| 8 | ENY | 851 |
| 9 | Vueling | 675 |
| 10 | AXM | 659 |
| 11 | LATAM Airlines | 640 |
| 12 | All Nippon Airways | 580 |
| 13 | Delta Air Lines | 579 |
| 14 | WIF | 579 |
| 15 | AZU | 559 |
| 16 | QLK | 530 |
| 17 | Swiss International | 529 |
| 18 | LXJ | 495 |
| 19 | Alaska Airlines | 472 |
| 20 | easyJet | 455 |
| 21 | AEE | 451 |
| 22 | EJU | 447 |
| 23 | VIV | 429 |
| 24 | Cathay Pacific | 415 |
| 25 | Air France | 404 |
| 26 | Japan Airlines | 403 |
| 27 | AXB | 387 |
| 28 | CXK | 348 |
| 29 | AIQ | 346 |
| 30 | MXY | 337 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 54618 |
| 2 | 🇪🇸 ES | 5025 |
| 3 | 🇮🇳 IN | 4981 |
| 4 | 🇦🇺 AU | 4551 |
| 5 | 🇧🇷 BR | 3862 |
| 6 | 🇩🇪 DE | 3833 |
| 7 | 🇮🇹 IT | 3763 |
| 8 | 🇯🇵 JP | 3687 |
| 9 | 🇨🇦 CA | 3396 |
| 10 | 🇬🇧 GB | 2978 |
| 11 | 🇫🇷 FR | 2722 |
| 12 | 🇨🇴 CO | 2657 |
| 13 | 🇲🇽 MX | 2191 |
| 14 | 🇬🇷 GR | 2061 |
| 15 | 🇨🇭 CH | 1903 |
| 16 | 🇳🇴 NO | 1871 |
| 17 | 🇲🇾 MY | 1641 |
| 18 | 🇿🇦 ZA | 1373 |
| 19 | 🇳🇿 NZ | 1278 |
| 20 | 🇹🇭 TH | 1237 |
| 21 | 🇹🇷 TR | 1227 |
| 22 | 🇵🇭 PH | 1149 |
| 23 | 🇵🇱 PL | 1125 |
| 24 | 🇬🇹 GT | 1113 |
| 25 | 🇰🇷 KR | 1097 |
| 26 | 🇲🇦 MA | 835 |
| 27 | 🇲🇴 MO | 779 |
| 28 | 🇲🇪 ME | 743 |
| 29 | 🇳🇱 NL | 714 |
| 30 | 🇮🇩 ID | 582 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1523 |
| 2 | Tokyo International Airport |  | JP | 1244 |
| 3 | Denver International Airport |  | US | 1130 |
| 4 | Indira Gandhi International Airport |  | IN | 1043 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1007 |
| 6 | Frankfurt am Main International Airport |  | DE | 881 |
| 7 | El Dorado International Airport |  | CO | 878 |
| 8 | Harry Reid International Airport |  | US | 858 |
| 9 | Guaymaral Airport |  | CO | 852 |
| 10 | La Aurora Airport |  | GT | 828 |
| 11 | Zurich Airport |  | CH | 814 |
| 12 | Macau International Airport |  | MO | 779 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 680 |
| 14 | Chicago O'Hare International Airport |  | US | 659 |
| 15 | Kuala Lumpur International Airport |  | MY | 657 |
| 16 | Madrid Barajas International Airport |  | ES | 654 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 616 |
| 18 | Bengaluru International Airport |  | IN | 603 |
| 19 | Malpensa International Airport |  | IT | 599 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 595 |
| 21 | Congonhas Airport |  | BR | 552 |
| 22 | Salt Lake City International Airport |  | US | 551 |
| 23 | Charlotte/Douglas International Airport |  | US | 543 |
| 24 | Tenerife Norte Airport |  | ES | 540 |
| 25 | Charles de Gaulle International Airport |  | FR | 539 |
| 26 | Capua Airport |  | IT | 528 |
| 27 | Ninoy Aquino International Airport |  | PH | 522 |
| 28 | Netaji Subhash Chandra Bose International Airport |  | IN | 502 |
| 29 | Daniel K Inouye International Airport |  | US | 500 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 486 |
| 31 | Barcelona International Airport |  | ES | 477 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 469 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 457 |
| 34 | Vitoria/Foronda Airport |  | ES | 455 |
| 35 | O. R. Tambo International Airport |  | ZA | 434 |
| 36 | Don Mueang International Airport |  | TH | 433 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 430 |
| 38 | Amsterdam Airport Schiphol |  | NL | 421 |
| 39 | Reno/Tahoe International Airport |  | US | 410 |
| 40 | Calgary International Airport |  | CA | 408 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 352 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 261 | 1h 7m | 706 km | 3,177.7 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 235 | 21m | 244 km | 989.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 208 | 24m | 225 km | 806.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 195 | 1h 27m | 910 km | 3,060.0 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 194 | 28m | 304 km | 1,017.0 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 171 | 20m | 165 km | 486.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 171 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 162 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 154 | 26m | 275 km | 729.7 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 153 | 1h 12m | 770 km | 2,032.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 131 | 21m | 99 km | 224.4 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 125 | 44m | 452 km | 974.2 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 116 | 31m | 369 km | 738.4 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 108 | 20m | 250 km | 466.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 105 | 27m | 215 km | 388.9 t |
| 19 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 104 | 20m | 147 km | 263.2 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 97 | 14m | 154 km | 257.0 t |
| 23 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 96 | 58m | 493 km | 816.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 95 | 1h 2m | 695 km | 1,138.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 93 | 1h 43m | 1,423 km | 2,282.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 91 | 12m | - | - |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 88 | 23m | 55 km | 83.6 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 87 | 1h 19m | 961 km | 1,442.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N463RS |  | Tallahassee International Airport (KTLH) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-05-04 23:57 UTC | 2026-05-05 00:55 UTC | 58m |
| N407SH |  | Modesto City-County-Harry Sham Field (KMOD) | Oakdale Airport (KO27) | 2026-05-05 00:37 UTC | 2026-05-05 00:48 UTC | 11m |
| FFAB123 | FFA | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-05-04 21:32 UTC | 2026-05-05 00:47 UTC | 3h 15m |
| N707KA |  | 80WA (80WA) | Boeing Field/King County International Airport (KBFI) | 2026-05-05 00:28 UTC | 2026-05-05 00:44 UTC | 15m |
| ZMV | ZMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-05-05 00:25 UTC | 2026-05-05 00:43 UTC | 18m |
| NVP | NVP | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-05-05 00:30 UTC | 2026-05-05 00:41 UTC | 11m |
| C6018 |  | Merle K (Mudhole) Smith Airport (PACV) | Merle K (Mudhole) Smith Airport (PACV) | 2026-05-05 00:04 UTC | 2026-05-05 00:34 UTC | 29m |
| XBERM | XBE | General Abelardo L. Rodriguez International Airport (MMTJ) | General Abelardo L. Rodriguez International Airport (MMTJ) | 2026-05-05 00:18 UTC | 2026-05-05 00:23 UTC | 5m |
| N911LG |  | 7IA3 (7IA3) | IA28 (IA28) | 2026-05-05 00:12 UTC | 2026-05-05 00:18 UTC | 6m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Trading Bay Production Airport (5AK0) | 2026-05-05 00:04 UTC | 2026-05-05 00:16 UTC | 11m |
| ZFO | ZFO | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-04 23:47 UTC | 2026-05-05 00:15 UTC | 28m |
| SVX42 | SVX | Ted Stevens Anchorage International Airport (PANC) | Teller Airport (PATE) | 2026-05-04 22:31 UTC | 2026-05-05 00:15 UTC | 1h 43m |
| N2131W |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-05-04 23:44 UTC | 2026-05-05 00:14 UTC | 30m |
| N327TL |  | Teterboro Airport (KTEB) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-04 22:31 UTC | 2026-05-05 00:12 UTC | 1h 40m |
| RPC8526 | RPC | Plaridel Airport (RPUX) | Plaridel Airport (RPUX) | 2026-05-04 23:54 UTC | 2026-05-05 00:12 UTC | 17m |
| N161DA |  | Phoenix Deer Valley Airport (KDVT) | Montezuma Airport (19AZ) | 2026-05-04 23:47 UTC | 2026-05-05 00:11 UTC | 24m |
| N554SC |  | Christmas Flying Service Airport (MS03) | Christmas Flying Service Airport (MS03) | 2026-05-04 23:16 UTC | 2026-05-05 00:11 UTC | 55m |
| ZKKAZ | ZKK | Paraparaumu Airport (NZPP) | Paraparaumu Airport (NZPP) | 2026-05-04 23:56 UTC | 2026-05-05 00:11 UTC | 14m |
| HLC260 | HLC | Osan Air Base (RKSO) | Osan Air Base (RKSO) | 2026-05-05 00:10 UTC | 2026-05-05 00:10 UTC | 0m |
| SFJ73 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-05-04 22:55 UTC | 2026-05-05 00:10 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
