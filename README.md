# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_01:15:55_UTC-green)

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

**Latest saved flight:** 2026-10-01 01:15:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-01 01:15:55 UTC

- **273,524** saved flights
- **79,861** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **273,524** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,311,715.6 tonnes** estimated CO2 emissions
- **191,983,516 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10743 |
| 2 | SkyWest Airlines | 9519 |
| 3 | EJA | 5359 |
| 4 | IndiGo | 4562 |
| 5 | American Airlines | 4238 |
| 6 | Southwest Airlines | 4025 |
| 7 | Delta Air Lines | 3395 |
| 8 | ENY | 3206 |
| 9 | LATAM Airlines | 2642 |
| 10 | AZU | 2572 |
| 11 | Vueling | 2270 |
| 12 | WIF | 2224 |
| 13 | LXJ | 2154 |
| 14 | Lufthansa | 2065 |
| 15 | easyJet | 1822 |
| 16 | Swiss International | 1789 |
| 17 | QLK | 1768 |
| 18 | EJU | 1706 |
| 19 | AXM | 1682 |
| 20 | United Airlines | 1671 |
| 21 | Alaska Airlines | 1613 |
| 22 | All Nippon Airways | 1564 |
| 23 | PGT | 1540 |
| 24 | WMT | 1526 |
| 25 | GLO | 1525 |
| 26 | Air France | 1504 |
| 27 | VIV | 1499 |
| 28 | Wizz Air | 1482 |
| 29 | CXK | 1352 |
| 30 | AEE | 1306 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228099 |
| 2 | 🇪🇸 ES | 17096 |
| 3 | 🇧🇷 BR | 16054 |
| 4 | 🇦🇺 AU | 15795 |
| 5 | 🇨🇦 CA | 15251 |
| 6 | 🇮🇹 IT | 14759 |
| 7 | 🇮🇳 IN | 14434 |
| 8 | 🇩🇪 DE | 13106 |
| 9 | 🇨🇴 CO | 12651 |
| 10 | 🇬🇧 GB | 12610 |
| 11 | 🇫🇷 FR | 10841 |
| 12 | 🇯🇵 JP | 10447 |
| 13 | 🇹🇷 TR | 8273 |
| 14 | 🇬🇷 GR | 7869 |
| 15 | 🇲🇽 MX | 7557 |
| 16 | 🇨🇭 CH | 7257 |
| 17 | 🇳🇴 NO | 6746 |
| 18 | 🇹🇭 TH | 4891 |
| 19 | 🇲🇾 MY | 4557 |
| 20 | 🇿🇦 ZA | 4551 |
| 21 | 🇵🇱 PL | 4469 |
| 22 | 🇳🇿 NZ | 3867 |
| 23 | 🇵🇭 PH | 3606 |
| 24 | 🇬🇹 GT | 3430 |
| 25 | 🇭🇷 HR | 3111 |
| 26 | 🇰🇷 KR | 3084 |
| 27 | 🇲🇦 MA | 2704 |
| 28 | 🇲🇪 ME | 2568 |
| 29 | 🇳🇱 NL | 2447 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5560 |
| 2 | Denver International Airport |  | US | 4460 |
| 3 | Indira Gandhi International Airport |  | IN | 3263 |
| 4 | Tokyo International Airport |  | JP | 3131 |
| 5 | El Dorado International Airport |  | CO | 3008 |
| 6 | Harry Reid International Airport |  | US | 2944 |
| 7 | Guaymaral Airport |  | CO | 2841 |
| 8 | Zurich Airport |  | CH | 2836 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2737 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2620 |
| 11 | La Aurora Airport |  | GT | 2607 |
| 12 | Salt Lake City International Airport |  | US | 2422 |
| 13 | Congonhas Airport |  | BR | 2336 |
| 14 | Chicago O'Hare International Airport |  | US | 2320 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2241 |
| 16 | Capua Airport |  | IT | 2116 |
| 17 | Madrid Barajas International Airport |  | ES | 2104 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2073 |
| 19 | Frankfurt am Main International Airport |  | DE | 2062 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1945 |
| 21 | Malpensa International Airport |  | IT | 1943 |
| 22 | Hartsfield/Jackson Atlanta International Airport |  | US | 1942 |
| 23 | Charles de Gaulle International Airport |  | FR | 1940 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1922 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1772 |
| 28 | Charlotte/Douglas International Airport |  | US | 1710 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1690 |
| 31 | Viracopos International Airport |  | BR | 1642 |
| 32 | Kuala Lumpur International Airport |  | MY | 1632 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1606 |
| 34 | Seattle-Tacoma International Airport |  | US | 1602 |
| 35 | Calgary International Airport |  | CA | 1554 |
| 36 | Don Mueang International Airport |  | TH | 1545 |
| 37 | Vancouver International Airport |  | CA | 1531 |
| 38 | Bengaluru International Airport |  | IN | 1531 |
| 39 | Oslo Gardermoen Airport |  | NO | 1530 |
| 40 | Reno/Tahoe International Airport |  | US | 1477 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1130 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1029 | 21m | 244 km | 4,332.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 762 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 691 | 1h 6m | 770 km | 9,179.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 685 | 24m | 225 km | 2,657.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 603 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 457 | 44m | 555 km | 4,376.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 439 | 27m | 275 km | 2,080.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 381 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 370 | 23m | 55 km | 351.7 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 350 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 339 | 26m | 215 km | 1,255.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 310 | 1h 14m | 961 km | 5,138.4 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 309 | 18m | 14 km | 77.3 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N227NH |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-10-01 00:55 UTC | 2026-10-01 01:15 UTC | 20m |
| HATED55 | HAT | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | Biggs Army Air Field (Fort Bliss) Airport (KBIF) | 2026-10-01 00:42 UTC | 2026-10-01 01:13 UTC | 31m |
|  |  | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-10-01 00:34 UTC | 2026-10-01 01:09 UTC | 34m |
| N3547H |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-10-01 00:48 UTC | 2026-10-01 01:08 UTC | 20m |
| SWR | Swiss International | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-09-30 23:33 UTC | 2026-10-01 01:08 UTC | 1h 34m |
| N221TJ |  | Olympia Regional Airport (KOLM) | Olympia Regional Airport (KOLM) | 2026-10-01 00:40 UTC | 2026-10-01 01:07 UTC | 26m |
| N19JG |  | Fall City Airport (1WA6) | West Valley Airport (48WA) | 2026-10-01 00:29 UTC | 2026-10-01 01:04 UTC | 35m |
| TWY206 | TWY | Floyd Ranch Airport (TA56) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-30 22:38 UTC | 2026-10-01 00:59 UTC | 2h 20m |
| N4411X |  | Montgomery-Gibbs Executive Airport (KMYF) | Mc Clellan-Palomar Airport (KCRQ) | 2026-10-01 00:24 UTC | 2026-10-01 00:55 UTC | 31m |
| N611GV |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-10-01 00:30 UTC | 2026-10-01 00:54 UTC | 23m |
| N159M |  | Fond Du Lac County Airport (KFLD) | Park Falls Municipal Airport (KPKF) | 2026-10-01 00:27 UTC | 2026-10-01 00:53 UTC | 25m |
| N669FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-10-01 00:00 UTC | 2026-10-01 00:48 UTC | 47m |
| N808ET |  | John Wayne/Orange County Airport (KSNA) | Big Bear City Airport (KL35) | 2026-10-01 00:11 UTC | 2026-10-01 00:45 UTC | 34m |
| N384CA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-10-01 00:22 UTC | 2026-10-01 00:42 UTC | 19m |
| EJM24 | EJM | St Paul Downtown Holman Field (KSTP) | Washington Dulles International Airport (KIAD) | 2026-09-30 22:47 UTC | 2026-10-01 00:37 UTC | 1h 50m |
| N50GP |  | Redding Regional Airport (KRDD) | Ennis Big Sky Airport (KEKS) | 2026-09-30 23:22 UTC | 2026-10-01 00:37 UTC | 1h 14m |
| EJA941 | EJA | Boeing Field/King County International Airport (KBFI) | Plains Airport (KS34) | 2026-09-30 23:50 UTC | 2026-10-01 00:33 UTC | 43m |
| QLK863D | QLK | Brisbane International Airport (YBBN) | Cooma/Polo Flat (Unlic) Airport (YPFT) | 2026-09-30 22:42 UTC | 2026-10-01 00:32 UTC | 1h 50m |
| N4871V |  | Stockton Metro Airport (KSCK) | Tracy Municipal Airport (KTCY) | 2026-09-30 23:33 UTC | 2026-10-01 00:27 UTC | 54m |
| SRG899 | SRG | Islay Airport (EGPI) | Glasgow International Airport (EGPF) | 2026-10-01 00:06 UTC | 2026-10-01 00:27 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
