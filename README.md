# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_03:38:48_UTC-green)

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

**Latest saved flight:** 2026-05-03 03:38:48 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-03 03:38:48 UTC

- **65,216** saved flights
- **24,758** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **65,216** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **798,877.4 tonnes** estimated CO2 emissions
- **46,311,736 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2763 |
| 2 | SkyWest Airlines | 2419 |
| 3 | IndiGo | 1499 |
| 4 | EJA | 1160 |
| 5 | American Airlines | 1011 |
| 6 | Southwest Airlines | 919 |
| 7 | Lufthansa | 834 |
| 8 | ENY | 806 |
| 9 | Vueling | 640 |
| 10 | AXM | 634 |
| 11 | LATAM Airlines | 609 |
| 12 | All Nippon Airways | 567 |
| 13 | Delta Air Lines | 546 |
| 14 | WIF | 539 |
| 15 | AZU | 526 |
| 16 | QLK | 507 |
| 17 | Swiss International | 499 |
| 18 | LXJ | 470 |
| 19 | Alaska Airlines | 447 |
| 20 | easyJet | 425 |
| 21 | AEE | 420 |
| 22 | EJU | 416 |
| 23 | VIV | 409 |
| 24 | Cathay Pacific | 392 |
| 25 | Japan Airlines | 383 |
| 26 | Air France | 377 |
| 27 | AXB | 363 |
| 28 | AIQ | 331 |
| 29 | CXK | 331 |
| 30 | GLO | 317 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 51702 |
| 2 | 🇪🇸 ES | 4756 |
| 3 | 🇮🇳 IN | 4722 |
| 4 | 🇦🇺 AU | 4370 |
| 5 | 🇧🇷 BR | 3673 |
| 6 | 🇩🇪 DE | 3637 |
| 7 | 🇯🇵 JP | 3550 |
| 8 | 🇮🇹 IT | 3529 |
| 9 | 🇨🇦 CA | 3201 |
| 10 | 🇬🇧 GB | 2797 |
| 11 | 🇨🇴 CO | 2645 |
| 12 | 🇫🇷 FR | 2571 |
| 13 | 🇲🇽 MX | 2075 |
| 14 | 🇬🇷 GR | 1943 |
| 15 | 🇨🇭 CH | 1820 |
| 16 | 🇳🇴 NO | 1766 |
| 17 | 🇲🇾 MY | 1558 |
| 18 | 🇿🇦 ZA | 1322 |
| 19 | 🇳🇿 NZ | 1220 |
| 20 | 🇹🇭 TH | 1182 |
| 21 | 🇹🇷 TR | 1165 |
| 22 | 🇵🇭 PH | 1093 |
| 23 | 🇰🇷 KR | 1066 |
| 24 | 🇵🇱 PL | 1061 |
| 25 | 🇬🇹 GT | 1000 |
| 26 | 🇲🇦 MA | 800 |
| 27 | 🇲🇴 MO | 735 |
| 28 | 🇲🇪 ME | 701 |
| 29 | 🇳🇱 NL | 686 |
| 30 | 🇮🇩 ID | 549 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1435 |
| 2 | Tokyo International Airport |  | JP | 1195 |
| 3 | Denver International Airport |  | US | 1079 |
| 4 | Indira Gandhi International Airport |  | IN | 993 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 945 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 840 |
| 8 | Frankfurt am Main International Airport |  | DE | 834 |
| 9 | Harry Reid International Airport |  | US | 820 |
| 10 | Zurich Airport |  | CH | 769 |
| 11 | La Aurora Airport |  | GT | 750 |
| 12 | Macau International Airport |  | MO | 735 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 642 |
| 14 | Chicago O'Hare International Airport |  | US | 623 |
| 15 | Madrid Barajas International Airport |  | ES | 619 |
| 16 | Kuala Lumpur International Airport |  | MY | 619 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 588 |
| 18 | Bengaluru International Airport |  | IN | 571 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 568 |
| 20 | Malpensa International Airport |  | IT | 560 |
| 21 | Congonhas Airport |  | BR | 529 |
| 22 | Tenerife Norte Airport |  | ES | 518 |
| 23 | Charlotte/Douglas International Airport |  | US | 517 |
| 24 | Salt Lake City International Airport |  | US | 515 |
| 25 | Charles de Gaulle International Airport |  | FR | 505 |
| 26 | Ninoy Aquino International Airport |  | PH | 497 |
| 27 | Daniel K Inouye International Airport |  | US | 480 |
| 28 | Capua Airport |  | IT | 480 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 475 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 465 |
| 31 | Barcelona International Airport |  | ES | 442 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 435 |
| 33 | Vitoria/Foronda Airport |  | ES | 432 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 430 |
| 35 | O. R. Tambo International Airport |  | ZA | 417 |
| 36 | Don Mueang International Airport |  | TH | 410 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 407 |
| 38 | Amsterdam Airport Schiphol |  | NL | 403 |
| 39 | Reno/Tahoe International Airport |  | US | 399 |
| 40 | Calgary International Airport |  | CA | 383 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 346 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 260 | 1h 7m | 706 km | 3,165.5 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 222 | 21m | 244 km | 934.8 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 202 | 24m | 225 km | 783.7 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 190 | 28m | 304 km | 996.0 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 190 | 1h 27m | 910 km | 2,981.5 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 161 | 20m | 165 km | 458.0 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 160 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 153 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 148 | 26m | 275 km | 701.3 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 142 | 1h 11m | 770 km | 1,886.4 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 120 | 44m | 452 km | 935.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 115 | 21m | 99 km | 197.0 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 110 | 31m | 369 km | 700.2 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 105 | 20m | 250 km | 453.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 103 | 28m | 152 km | 269.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 97 | 20m | 147 km | 245.5 t |
| 21 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 91 | 1h 42m | 1,156 km | 1,815.4 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 90 | 52m | 556 km | 862.7 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 90 | 1h 2m | 695 km | 1,078.8 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 89 | 57m | 493 km | 757.2 t |
| 25 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 89 | 12m | - | - |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 89 | 1h 53m | 1,304 km | 2,002.3 t |
| 27 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 87 | 23m | 55 km | 82.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 86 | 14m | 154 km | 227.9 t |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 85 | 1h 42m | 1,423 km | 2,086.0 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 84 | 1h 19m | 961 km | 1,392.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 03:27 UTC | 2026-05-03 03:38 UTC | 11m |
| ERU7 | ERU | Robin Airport (59AZ) | Pilots Rest Airport (AZ57) | 2026-05-03 03:23 UTC | 2026-05-03 03:34 UTC | 10m |
| N7151G |  | Shiprock Airstrip (K5V5) | Blanding Municipal Airport (KBDG) | 2026-05-03 03:13 UTC | 2026-05-03 03:33 UTC | 19m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-03 03:10 UTC | 2026-05-03 03:21 UTC | 11m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-05-03 02:41 UTC | 2026-05-03 03:05 UTC | 23m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-05-03 02:38 UTC | 2026-05-03 03:02 UTC | 24m |
| JAL2795 | Japan Airlines | Okadama Airport (RJCO) | RJCY (RJCY) | 2026-05-03 02:37 UTC | 2026-05-03 03:02 UTC | 24m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-03 02:37 UTC | 2026-05-03 03:00 UTC | 22m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-05-03 02:17 UTC | 2026-05-03 02:57 UTC | 40m |
| QLK109D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-05-03 02:25 UTC | 2026-05-03 02:57 UTC | 31m |
| ASA67 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Prince Rupert Airport (CYPR) | 2026-05-03 01:30 UTC | 2026-05-03 02:53 UTC | 1h 22m |
| AIC3BT | Air India | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-05-03 02:27 UTC | 2026-05-03 02:50 UTC | 23m |
| MXD2407 | MXD | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-03 02:26 UTC | 2026-05-03 02:47 UTC | 21m |
| FDA144 | FDA | Fukuoka Airport (RJFF) | Mt. Fuji Shizuoka Airport (RJNS) | 2026-05-03 01:53 UTC | 2026-05-03 02:45 UTC | 51m |
| N811HW |  | Sullivan Field (27LL) | St Louis Downtown Airport (KCPS) | 2026-05-03 02:34 UTC | 2026-05-03 02:44 UTC | 10m |
| JTZ433 | JTZ | Clark Regional Airport (KJVY) | Kosciusko-Attala County Airport (KOSX) | 2026-05-03 01:44 UTC | 2026-05-03 02:44 UTC | 1h 0m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Wellington Airport (YWEL) | 2026-05-03 02:11 UTC | 2026-05-03 02:42 UTC | 31m |
| N245DJ |  | Harry Reid International Airport (KLAS) | Oakland San Francisco Bay Airport (KOAK) | 2026-05-03 01:35 UTC | 2026-05-03 02:42 UTC | 1h 7m |
| AXM6077 | AXM | Kota Kinabalu International Airport (WBKK) | Marudi Airport (WBGM) | 2026-05-03 02:19 UTC | 2026-05-03 02:42 UTC | 22m |
| JST281 | JST | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-05-03 01:27 UTC | 2026-05-03 02:40 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
