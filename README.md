# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_20:30:01_UTC-green)

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

**Latest saved flight:** 2026-05-17 20:30:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 20:30:01 UTC

- **86,840** saved flights
- **31,098** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,840** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,074,539.1 tonnes** estimated CO2 emissions
- **62,292,122 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3726 |
| 2 | SkyWest Airlines | 3216 |
| 3 | IndiGo | 1866 |
| 4 | EJA | 1635 |
| 5 | American Airlines | 1332 |
| 6 | Southwest Airlines | 1263 |
| 7 | Lufthansa | 1098 |
| 8 | ENY | 1076 |
| 9 | Delta Air Lines | 952 |
| 10 | Vueling | 828 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 782 |
| 13 | WIF | 742 |
| 14 | AZU | 679 |
| 15 | Swiss International | 674 |
| 16 | All Nippon Airways | 667 |
| 17 | LXJ | 641 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 614 |
| 20 | easyJet | 575 |
| 21 | EJU | 560 |
| 22 | Cathay Pacific | 550 |
| 23 | AEE | 542 |
| 24 | VIV | 521 |
| 25 | Air France | 510 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 458 |
| 28 | AXB | 455 |
| 29 | MXY | 439 |
| 30 | AIQ | 427 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 71083 |
| 2 | 🇪🇸 ES | 6166 |
| 3 | 🇮🇳 IN | 5836 |
| 4 | 🇦🇺 AU | 5478 |
| 5 | 🇩🇪 DE | 4847 |
| 6 | 🇮🇹 IT | 4816 |
| 7 | 🇧🇷 BR | 4760 |
| 8 | 🇯🇵 JP | 4322 |
| 9 | 🇨🇦 CA | 4310 |
| 10 | 🇬🇧 GB | 3720 |
| 11 | 🇫🇷 FR | 3478 |
| 12 | 🇨🇴 CO | 2926 |
| 13 | 🇲🇽 MX | 2689 |
| 14 | 🇬🇷 GR | 2527 |
| 15 | 🇳🇴 NO | 2400 |
| 16 | 🇨🇭 CH | 2310 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1574 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1503 |
| 22 | 🇵🇱 PL | 1445 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1304 |
| 26 | 🇲🇦 MA | 1010 |
| 27 | 🇲🇴 MO | 1007 |
| 28 | 🇲🇪 ME | 904 |
| 29 | 🇳🇱 NL | 886 |
| 30 | 🇭🇷 HR | 782 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1902 |
| 2 | Denver International Airport |  | US | 1454 |
| 3 | Tokyo International Airport |  | JP | 1444 |
| 4 | Indira Gandhi International Airport |  | IN | 1252 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1203 |
| 6 | Frankfurt am Main International Airport |  | DE | 1110 |
| 7 | Harry Reid International Airport |  | US | 1102 |
| 8 | Zurich Airport |  | CH | 1038 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | La Aurora Airport |  | GT | 991 |
| 11 | Guaymaral Airport |  | CO | 990 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 961 |
| 13 | El Dorado International Airport |  | CO | 938 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 875 |
| 15 | Chicago O'Hare International Airport |  | US | 840 |
| 16 | Madrid Barajas International Airport |  | ES | 792 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 748 |
| 19 | Capua Airport |  | IT | 731 |
| 20 | Salt Lake City International Airport |  | US | 725 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 716 |
| 22 | Malpensa International Airport |  | IT | 713 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 678 |
| 25 | Charlotte/Douglas International Airport |  | US | 672 |
| 26 | Congonhas Airport |  | BR | 667 |
| 27 | Tenerife Norte Airport |  | ES | 639 |
| 28 | Daniel K Inouye International Airport |  | US | 635 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 593 |
| 32 | Barcelona International Airport |  | ES | 583 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 577 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 558 |
| 35 | Vitoria/Foronda Airport |  | ES | 555 |
| 36 | Don Mueang International Airport |  | TH | 545 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 545 |
| 38 | Amsterdam Airport Schiphol |  | NL | 541 |
| 39 | O. R. Tambo International Airport |  | ZA | 510 |
| 40 | Calgary International Airport |  | CA | 510 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 322 | 21m | 244 km | 1,355.9 t |
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
| BNOR | BNO | Brønnøysund Airport (ENBN) | Sandnessjoen Airport Stokka (ENST) | 2026-05-17 20:15 UTC | 2026-05-17 20:30 UTC | 14m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-17 20:14 UTC | 2026-05-17 20:25 UTC | 11m |
| ASI577 | ASI | Phoenix Deer Valley Airport (KDVT) | Lake Havasu City Airport (KHII) | 2026-05-17 19:03 UTC | 2026-05-17 20:24 UTC | 1h 20m |
| N355MJ |  | Cobb County International/Mccollum Field (KRYY) | Austin Executive Airport (KEDC) | 2026-05-17 13:45 UTC | 2026-05-17 20:21 UTC | 6h 36m |
| ANA968 | All Nippon Airways | Nagasaki Airport (RJFU) | Tokyo International Airport (RJTT) | 2026-05-17 19:01 UTC | 2026-05-17 20:21 UTC | 1h 19m |
| N103FD |  | Miami Homestead General Aviation Airport (KX51) | Miami Executive Airport (KTMB) | 2026-05-17 20:11 UTC | 2026-05-17 20:18 UTC | 7m |
| N699SU |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-05-17 20:16 UTC | 2026-05-17 20:17 UTC | 0m |
| N20FH |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-05-17 18:51 UTC | 2026-05-17 20:17 UTC | 1h 26m |
| N520AF |  | Morristown Municipal Airport (KMMU) | Blairstown Airport (K1N7) | 2026-05-17 19:33 UTC | 2026-05-17 20:15 UTC | 41m |
| N379VM |  | Georgetown Executive Airport (KGTU) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-05-17 18:53 UTC | 2026-05-17 20:13 UTC | 1h 20m |
| TMN121 | TMN | Sydney Kingsford Smith International Airport (YSSY) | Chek Lap Kok International Airport (VHHH) | 2026-05-17 10:55 UTC | 2026-05-17 20:13 UTC | 9h 17m |
| N981BB |  | Wasilla Airport (PAWS) | Wasilla Airport (PAWS) | 2026-05-17 19:36 UTC | 2026-05-17 20:13 UTC | 36m |
| N707AT |  | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-05-17 19:12 UTC | 2026-05-17 20:12 UTC | 1h 0m |
| LXJ444 | LXJ | Scottsdale Airport (KSDL) | Santa Barbara Municipal Airport (KSBA) | 2026-05-17 18:16 UTC | 2026-05-17 20:08 UTC | 1h 52m |
| N515KS |  | Des Moines International Airport (KDSM) | Phillips Field (MO23) | 2026-05-17 19:39 UTC | 2026-05-17 20:06 UTC | 27m |
| N560RH |  | Ogden-Hinckley Airport (KOGD) | H A Clark Memorial Field (KCMR) | 2026-05-17 19:07 UTC | 2026-05-17 20:04 UTC | 56m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-17 19:50 UTC | 2026-05-17 20:04 UTC | 14m |
| N58SS |  | Ruth Field (WV28) | Lorain County Regional Airport (KLPR) | 2026-05-17 19:08 UTC | 2026-05-17 20:03 UTC | 55m |
| EJA472 | EJA | Livermore Municipal Airport (KLVK) | Phoenix Sky Harbor International Airport (KPHX) | 2026-05-17 18:34 UTC | 2026-05-17 20:02 UTC | 1h 28m |
| BXCAR84 | BXC | KS98 (KS98) | Richland Airport (KRLD) | 2026-05-17 20:00 UTC | 2026-05-17 20:02 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
