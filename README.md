# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_17:05:19_UTC-green)

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

**Latest saved flight:** 2026-09-23 17:05:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 17:05:19 UTC

- **267,392** saved flights
- **78,563** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,392** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,243,035.4 tonnes** estimated CO2 emissions
- **188,002,050 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10559 |
| 2 | SkyWest Airlines | 9299 |
| 3 | EJA | 5199 |
| 4 | IndiGo | 4486 |
| 5 | American Airlines | 4165 |
| 6 | Southwest Airlines | 3930 |
| 7 | Delta Air Lines | 3324 |
| 8 | ENY | 3143 |
| 9 | LATAM Airlines | 2579 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2239 |
| 12 | WIF | 2170 |
| 13 | LXJ | 2098 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1795 |
| 16 | Swiss International | 1759 |
| 17 | QLK | 1722 |
| 18 | EJU | 1685 |
| 19 | AXM | 1671 |
| 20 | United Airlines | 1639 |
| 21 | Alaska Airlines | 1581 |
| 22 | All Nippon Airways | 1542 |
| 23 | PGT | 1507 |
| 24 | WMT | 1500 |
| 25 | GLO | 1491 |
| 26 | Air France | 1470 |
| 27 | VIV | 1462 |
| 28 | Wizz Air | 1452 |
| 29 | CXK | 1304 |
| 30 | AEE | 1287 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222264 |
| 2 | 🇪🇸 ES | 16794 |
| 3 | 🇧🇷 BR | 15634 |
| 4 | 🇦🇺 AU | 15362 |
| 5 | 🇨🇦 CA | 14897 |
| 6 | 🇮🇹 IT | 14519 |
| 7 | 🇮🇳 IN | 14189 |
| 8 | 🇩🇪 DE | 12879 |
| 9 | 🇬🇧 GB | 12407 |
| 10 | 🇨🇴 CO | 12214 |
| 11 | 🇫🇷 FR | 10658 |
| 12 | 🇯🇵 JP | 10302 |
| 13 | 🇹🇷 TR | 8108 |
| 14 | 🇬🇷 GR | 7734 |
| 15 | 🇲🇽 MX | 7375 |
| 16 | 🇨🇭 CH | 7133 |
| 17 | 🇳🇴 NO | 6621 |
| 18 | 🇹🇭 TH | 4792 |
| 19 | 🇲🇾 MY | 4506 |
| 20 | 🇿🇦 ZA | 4482 |
| 21 | 🇵🇱 PL | 4389 |
| 22 | 🇳🇿 NZ | 3726 |
| 23 | 🇵🇭 PH | 3549 |
| 24 | 🇬🇹 GT | 3389 |
| 25 | 🇭🇷 HR | 3050 |
| 26 | 🇰🇷 KR | 3033 |
| 27 | 🇲🇦 MA | 2668 |
| 28 | 🇲🇪 ME | 2510 |
| 29 | 🇳🇱 NL | 2399 |
| 30 | 🇮🇩 ID | 2230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5449 |
| 2 | Denver International Airport |  | US | 4342 |
| 3 | Indira Gandhi International Airport |  | IN | 3209 |
| 4 | Tokyo International Airport |  | JP | 3082 |
| 5 | El Dorado International Airport |  | CO | 2882 |
| 6 | Harry Reid International Airport |  | US | 2857 |
| 7 | Guaymaral Airport |  | CO | 2801 |
| 8 | Zurich Airport |  | CH | 2779 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2681 |
| 10 | La Aurora Airport |  | GT | 2575 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2574 |
| 12 | Salt Lake City International Airport |  | US | 2359 |
| 13 | Chicago O'Hare International Airport |  | US | 2293 |
| 14 | Congonhas Airport |  | BR | 2278 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2182 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2056 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1905 |
| 22 | Charles de Gaulle International Airport |  | FR | 1897 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1877 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1874 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1778 |
| 27 | Ninoy Aquino International Airport |  | PH | 1742 |
| 28 | Charlotte/Douglas International Airport |  | US | 1668 |
| 29 | Barcelona International Airport |  | ES | 1664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1614 |
| 33 | Seattle-Tacoma International Airport |  | US | 1566 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1563 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1517 |
| 37 | Bengaluru International Airport |  | IN | 1511 |
| 38 | Oslo Gardermoen Airport |  | NO | 1506 |
| 39 | Vancouver International Airport |  | CA | 1497 |
| 40 | Antalya International Airport |  | TR | 1428 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1117 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1002 | 21m | 244 km | 4,219.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 674 | 1h 6m | 770 km | 8,953.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 595 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 427 | 27m | 275 km | 2,023.4 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 409 | 44m | 241 km | 1,698.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 382 | 24m | 218 km | 1,439.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 363 | 21m | 250 km | 1,567.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 353 | 23m | 55 km | 335.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 341 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 337 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 311 | 19m | 144 km | 773.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 284 | 18m | 14 km | 71.0 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HK1886G |  | Enrique Olaya Herrera Airport (SKMD) | La Nubia Airport (SKMZ) | 2026-09-23 16:07 UTC | 2026-09-23 17:05 UTC | 58m |
| NSZ6FY | NSZ | Palma De Mallorca Airport (LEPA) | Stockholm-Arlanda Airport (ESSA) | 2026-09-23 13:42 UTC | 2026-09-23 17:03 UTC | 3h 21m |
| N289ST |  | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-23 15:52 UTC | 2026-09-23 17:01 UTC | 1h 8m |
| N9305N |  | French Valley Airport (KF70) | Brown Field Municipal Airport (KSDM) | 2026-09-23 16:09 UTC | 2026-09-23 16:55 UTC | 46m |
| OKNGX | OKN | Warsaw Chopin Airport (EPWA) | Poznań-Ławica Airport (EPPO) | 2026-09-23 16:09 UTC | 2026-09-23 16:52 UTC | 42m |
| N350KA |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-09-23 16:20 UTC | 2026-09-23 16:48 UTC | 28m |
| N811LV |  | 2PA0 (2PA0) | Tidmore Airport (7PN0) | 2026-09-23 16:36 UTC | 2026-09-23 16:46 UTC | 10m |
| ECOTN | ECO | Casarrubios Del Monte Airport (LEMT) | Cuatro Vientos Airport (LECU) | 2026-09-23 16:28 UTC | 2026-09-23 16:43 UTC | 15m |
| N789TR |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-09-23 16:23 UTC | 2026-09-23 16:43 UTC | 19m |
| ARCAS04 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-09-23 16:27 UTC | 2026-09-23 16:40 UTC | 13m |
| BOX502 | BOX | Leipzig Halle Airport (EDDP) | Chek Lap Kok International Airport (VHHH) | 2026-09-23 06:11 UTC | 2026-09-23 16:38 UTC | 10h 27m |
| VAR503 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-09-23 15:27 UTC | 2026-09-23 16:37 UTC | 1h 9m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tlaxcala Airport (MMTA) | 2026-09-23 16:19 UTC | 2026-09-23 16:35 UTC | 16m |
| N16WG |  | Fort Worth Meacham International Airport (KFTW) | 5TA4 (5TA4) | 2026-09-23 15:28 UTC | 2026-09-23 16:34 UTC | 1h 5m |
| N8WC |  | Level Acres Farm Airport (PA84) | Abilene Municipal Airport (KK78) | 2026-09-23 13:53 UTC | 2026-09-23 16:33 UTC | 2h 39m |
| N6SR |  | Buchanan Field (KCCR) | Sacramento Mather Airport (KMHR) | 2026-09-23 15:43 UTC | 2026-09-23 16:31 UTC | 47m |
| N249WT |  | Greeley-Weld County Airport (KGXY) | Granby-Grand County Airport (KGNB) | 2026-09-23 16:06 UTC | 2026-09-23 16:31 UTC | 25m |
| N82KW |  | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Capital City Airport (KCXY) | 2026-09-23 16:12 UTC | 2026-09-23 16:30 UTC | 18m |
| SAS2002 | Scandinavian Airlines | Stockholm-Arlanda Airport (ESSA) | Pitea Airport (ESNP) | 2026-09-23 15:32 UTC | 2026-09-23 16:30 UTC | 57m |
| N500RW |  | Oberpfaffenhofen Airport (EDMO) | Zurich Airport (LSZH) | 2026-09-23 15:51 UTC | 2026-09-23 16:27 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
