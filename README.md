# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_19:38:17_UTC-green)

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

**Latest saved flight:** 2026-10-01 19:38:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-01 19:38:17 UTC

- **274,000** saved flights
- **79,958** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **274,000** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,316,625.5 tonnes** estimated CO2 emissions
- **192,268,145 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10761 |
| 2 | SkyWest Airlines | 9533 |
| 3 | EJA | 5368 |
| 4 | IndiGo | 4567 |
| 5 | American Airlines | 4243 |
| 6 | Southwest Airlines | 4026 |
| 7 | Delta Air Lines | 3402 |
| 8 | ENY | 3210 |
| 9 | LATAM Airlines | 2650 |
| 10 | AZU | 2580 |
| 11 | Vueling | 2275 |
| 12 | WIF | 2231 |
| 13 | LXJ | 2161 |
| 14 | Lufthansa | 2068 |
| 15 | easyJet | 1823 |
| 16 | Swiss International | 1793 |
| 17 | QLK | 1772 |
| 18 | EJU | 1708 |
| 19 | AXM | 1683 |
| 20 | United Airlines | 1671 |
| 21 | Alaska Airlines | 1614 |
| 22 | All Nippon Airways | 1565 |
| 23 | PGT | 1543 |
| 24 | GLO | 1529 |
| 25 | WMT | 1528 |
| 26 | Air France | 1505 |
| 27 | VIV | 1503 |
| 28 | Wizz Air | 1484 |
| 29 | CXK | 1353 |
| 30 | AEE | 1308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228490 |
| 2 | 🇪🇸 ES | 17142 |
| 3 | 🇧🇷 BR | 16095 |
| 4 | 🇦🇺 AU | 15819 |
| 5 | 🇨🇦 CA | 15272 |
| 6 | 🇮🇹 IT | 14790 |
| 7 | 🇮🇳 IN | 14455 |
| 8 | 🇩🇪 DE | 13130 |
| 9 | 🇨🇴 CO | 12686 |
| 10 | 🇬🇧 GB | 12627 |
| 11 | 🇫🇷 FR | 10852 |
| 12 | 🇯🇵 JP | 10454 |
| 13 | 🇹🇷 TR | 8290 |
| 14 | 🇬🇷 GR | 7884 |
| 15 | 🇲🇽 MX | 7573 |
| 16 | 🇨🇭 CH | 7271 |
| 17 | 🇳🇴 NO | 6762 |
| 18 | 🇹🇭 TH | 4900 |
| 19 | 🇲🇾 MY | 4559 |
| 20 | 🇿🇦 ZA | 4553 |
| 21 | 🇵🇱 PL | 4475 |
| 22 | 🇳🇿 NZ | 3869 |
| 23 | 🇵🇭 PH | 3612 |
| 24 | 🇬🇹 GT | 3434 |
| 25 | 🇭🇷 HR | 3118 |
| 26 | 🇰🇷 KR | 3084 |
| 27 | 🇲🇦 MA | 2707 |
| 28 | 🇲🇪 ME | 2572 |
| 29 | 🇳🇱 NL | 2453 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5564 |
| 2 | Denver International Airport |  | US | 4469 |
| 3 | Indira Gandhi International Airport |  | IN | 3270 |
| 4 | Tokyo International Airport |  | JP | 3134 |
| 5 | El Dorado International Airport |  | CO | 3014 |
| 6 | Harry Reid International Airport |  | US | 2947 |
| 7 | Guaymaral Airport |  | CO | 2845 |
| 8 | Zurich Airport |  | CH | 2843 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2741 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2624 |
| 11 | La Aurora Airport |  | GT | 2610 |
| 12 | Salt Lake City International Airport |  | US | 2432 |
| 13 | Congonhas Airport |  | BR | 2341 |
| 14 | Chicago O'Hare International Airport |  | US | 2321 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2242 |
| 16 | Capua Airport |  | IT | 2128 |
| 17 | Madrid Barajas International Airport |  | ES | 2108 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2083 |
| 19 | Frankfurt am Main International Airport |  | DE | 2064 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1958 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1944 |
| 22 | Malpensa International Airport |  | IT | 1943 |
| 23 | Charles de Gaulle International Airport |  | FR | 1941 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1928 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1832 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1775 |
| 28 | Charlotte/Douglas International Airport |  | US | 1714 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1700 |
| 30 | Barcelona International Airport |  | ES | 1693 |
| 31 | Viracopos International Airport |  | BR | 1643 |
| 32 | Kuala Lumpur International Airport |  | MY | 1632 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1609 |
| 34 | Seattle-Tacoma International Airport |  | US | 1604 |
| 35 | Calgary International Airport |  | CA | 1557 |
| 36 | Don Mueang International Airport |  | TH | 1547 |
| 37 | Oslo Gardermoen Airport |  | NO | 1534 |
| 38 | Vancouver International Airport |  | CA | 1534 |
| 39 | Bengaluru International Airport |  | IN | 1533 |
| 40 | Reno/Tahoe International Airport |  | US | 1480 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1132 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1030 | 21m | 244 km | 4,337.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 693 | 1h 6m | 770 km | 9,206.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 686 | 24m | 225 km | 2,661.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 604 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 458 | 44m | 555 km | 4,385.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 441 | 27m | 275 km | 2,089.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 421 | 44m | 241 km | 1,748.7 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 371 | 23m | 55 km | 352.6 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 352 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 342 | 19m | 99 km | 585.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 313 | 18m | 14 km | 78.3 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 311 | 1h 14m | 961 km | 5,155.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 303 | 42m | 535 km | 2,798.4 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N234FF |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-10-01 18:51 UTC | 2026-10-01 19:38 UTC | 47m |
| N567FL |  | Trenton Mercer Airport (KTTN) | Ocean City Municipal Airport (KOXB) | 2026-10-01 18:38 UTC | 2026-10-01 19:37 UTC | 58m |
| DLH7K | Lufthansa | Frankfurt am Main International Airport (EDDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-10-01 12:17 UTC | 2026-10-01 19:36 UTC | 7h 19m |
| CGNNQ | CGN | Colonial Airport (NY24) | Colonial Airport (NY24) | 2026-10-01 17:45 UTC | 2026-10-01 19:35 UTC | 1h 50m |
| N974PA |  | Mc Clellan-Palomar Airport (KCRQ) | French Valley Airport (KF70) | 2026-10-01 19:12 UTC | 2026-10-01 19:35 UTC | 23m |
| N388L |  | John Glenn Columbus International Airport (KCMH) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-10-01 18:54 UTC | 2026-10-01 19:35 UTC | 40m |
| N256AA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-10-01 18:43 UTC | 2026-10-01 19:28 UTC | 45m |
| N5525L |  | KU77 (KU77) | Logan-Cache Airport (KLGU) | 2026-10-01 18:48 UTC | 2026-10-01 19:28 UTC | 39m |
| N288SF |  | Columbus Airport (KCSG) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-10-01 18:59 UTC | 2026-10-01 19:25 UTC | 26m |
| ENSAIO52 | ENS | Professor Urbano Ernesto Stumpf Airport (SBSJ) | Guaratingueta Airport (SBGW) | 2026-10-01 18:16 UTC | 2026-10-01 19:25 UTC | 1h 8m |
| N248SG |  | Essex County Airport (KCDW) | Blairstown Airport (K1N7) | 2026-10-01 19:04 UTC | 2026-10-01 19:20 UTC | 15m |
| N359RX |  | Skyland Airport (NC50) | Twin County Airport (KHLX) | 2026-10-01 18:51 UTC | 2026-10-01 19:18 UTC | 26m |
| N402DS |  | Delaware Airpark (K33N) | Delaware Airpark (K33N) | 2026-10-01 19:07 UTC | 2026-10-01 19:18 UTC | 10m |
| TORA71 | TOR | 2TX3 (2TX3) | Fort Clark Springs Airport (74TX) | 2026-10-01 19:07 UTC | 2026-10-01 19:18 UTC | 10m |
| N503GF |  | Baton Rouge Metro, Ryan Field (KBTR) | St Pete-Clearwater International Airport (KPIE) | 2026-10-01 17:56 UTC | 2026-10-01 19:17 UTC | 1h 20m |
| SPZOD | SPZ | Gdańsk Lech Wałęsa Airport (EPGD) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-10-01 19:15 UTC | 2026-10-01 19:17 UTC | 2m |
| ARCAS25 | ARC | Kickapoo Downtown Airport (KCWC) | TX20 (TX20) | 2026-10-01 18:52 UTC | 2026-10-01 19:17 UTC | 24m |
| N230DF |  | Louisville Muhammad Ali International Airport (KSDF) | Lincoln Airport (KLNK) | 2026-10-01 17:38 UTC | 2026-10-01 19:16 UTC | 1h 38m |
| MWJ7 | MWJ | Port Alberni Airport (CBS8) | 11CL (11CL) | 2026-10-01 17:08 UTC | 2026-10-01 19:09 UTC | 2h 1m |
| N91966 |  | Atlanta Regional Falcon Field (KFFC) | Atlanta Regional Falcon Field (KFFC) | 2026-10-01 18:58 UTC | 2026-10-01 19:09 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
