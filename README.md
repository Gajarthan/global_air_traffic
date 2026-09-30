# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_18:23:32_UTC-green)

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

**Latest saved flight:** 2026-09-30 18:23:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-30 18:23:32 UTC

- **273,234** saved flights
- **79,793** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **273,234** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,309,317.4 tonnes** estimated CO2 emissions
- **191,844,489 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10735 |
| 2 | SkyWest Airlines | 9509 |
| 3 | EJA | 5349 |
| 4 | IndiGo | 4562 |
| 5 | American Airlines | 4236 |
| 6 | Southwest Airlines | 4017 |
| 7 | Delta Air Lines | 3392 |
| 8 | ENY | 3204 |
| 9 | LATAM Airlines | 2640 |
| 10 | AZU | 2567 |
| 11 | Vueling | 2270 |
| 12 | WIF | 2224 |
| 13 | LXJ | 2154 |
| 14 | Lufthansa | 2065 |
| 15 | easyJet | 1822 |
| 16 | Swiss International | 1788 |
| 17 | QLK | 1760 |
| 18 | EJU | 1706 |
| 19 | AXM | 1681 |
| 20 | United Airlines | 1668 |
| 21 | Alaska Airlines | 1611 |
| 22 | All Nippon Airways | 1563 |
| 23 | PGT | 1540 |
| 24 | GLO | 1524 |
| 25 | WMT | 1524 |
| 26 | Air France | 1504 |
| 27 | VIV | 1495 |
| 28 | Wizz Air | 1482 |
| 29 | CXK | 1351 |
| 30 | AEE | 1306 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 227751 |
| 2 | 🇪🇸 ES | 17093 |
| 3 | 🇧🇷 BR | 16036 |
| 4 | 🇦🇺 AU | 15762 |
| 5 | 🇨🇦 CA | 15229 |
| 6 | 🇮🇹 IT | 14754 |
| 7 | 🇮🇳 IN | 14434 |
| 8 | 🇩🇪 DE | 13104 |
| 9 | 🇨🇴 CO | 12629 |
| 10 | 🇬🇧 GB | 12605 |
| 11 | 🇫🇷 FR | 10841 |
| 12 | 🇯🇵 JP | 10437 |
| 13 | 🇹🇷 TR | 8271 |
| 14 | 🇬🇷 GR | 7868 |
| 15 | 🇲🇽 MX | 7542 |
| 16 | 🇨🇭 CH | 7255 |
| 17 | 🇳🇴 NO | 6746 |
| 18 | 🇹🇭 TH | 4891 |
| 19 | 🇲🇾 MY | 4554 |
| 20 | 🇿🇦 ZA | 4551 |
| 21 | 🇵🇱 PL | 4468 |
| 22 | 🇳🇿 NZ | 3854 |
| 23 | 🇵🇭 PH | 3604 |
| 24 | 🇬🇹 GT | 3430 |
| 25 | 🇭🇷 HR | 3108 |
| 26 | 🇰🇷 KR | 3076 |
| 27 | 🇲🇦 MA | 2703 |
| 28 | 🇲🇪 ME | 2564 |
| 29 | 🇳🇱 NL | 2447 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5558 |
| 2 | Denver International Airport |  | US | 4452 |
| 3 | Indira Gandhi International Airport |  | IN | 3263 |
| 4 | Tokyo International Airport |  | JP | 3127 |
| 5 | El Dorado International Airport |  | CO | 3002 |
| 6 | Harry Reid International Airport |  | US | 2936 |
| 7 | Guaymaral Airport |  | CO | 2841 |
| 8 | Zurich Airport |  | CH | 2834 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2735 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2620 |
| 11 | La Aurora Airport |  | GT | 2607 |
| 12 | Salt Lake City International Airport |  | US | 2421 |
| 13 | Congonhas Airport |  | BR | 2332 |
| 14 | Chicago O'Hare International Airport |  | US | 2320 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2235 |
| 16 | Capua Airport |  | IT | 2116 |
| 17 | Madrid Barajas International Airport |  | ES | 2104 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2073 |
| 19 | Frankfurt am Main International Airport |  | DE | 2062 |
| 20 | Malpensa International Airport |  | IT | 1941 |
| 21 | Enrique Olaya Herrera Airport |  | CO | 1940 |
| 22 | Charles de Gaulle International Airport |  | FR | 1940 |
| 23 | Hartsfield/Jackson Atlanta International Airport |  | US | 1939 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1916 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1771 |
| 28 | Charlotte/Douglas International Airport |  | US | 1709 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1689 |
| 31 | Viracopos International Airport |  | BR | 1641 |
| 32 | Kuala Lumpur International Airport |  | MY | 1631 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1602 |
| 34 | Seattle-Tacoma International Airport |  | US | 1600 |
| 35 | Calgary International Airport |  | CA | 1551 |
| 36 | Don Mueang International Airport |  | TH | 1545 |
| 37 | Bengaluru International Airport |  | IN | 1531 |
| 38 | Oslo Gardermoen Airport |  | NO | 1530 |
| 39 | Vancouver International Airport |  | CA | 1528 |
| 40 | Reno/Tahoe International Airport |  | US | 1468 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1130 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1028 | 21m | 244 km | 4,328.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 761 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 689 | 1h 6m | 770 km | 9,152.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 684 | 24m | 225 km | 2,653.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 603 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 457 | 44m | 555 km | 4,376.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 439 | 27m | 275 km | 2,080.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 418 | 44m | 241 km | 1,736.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 391 | 24m | 218 km | 1,473.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 381 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 368 | 23m | 55 km | 349.8 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 350 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 339 | 26m | 215 km | 1,255.5 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 309 | 1h 14m | 961 km | 5,121.8 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 307 | 18m | 14 km | 76.8 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6977B |  | Auburn Municipal Airport (KAUN) | Sacramento Executive Airport (KSAC) | 2026-09-30 18:03 UTC | 2026-09-30 18:23 UTC | 19m |
| OEKOC | OEK | Salzburg Airport (LOWS) | Linz Airport (LOWL) | 2026-09-30 17:27 UTC | 2026-09-30 18:13 UTC | 45m |
| INR2130 | INR | Villaframil Airport (LEVF) | Villaframil Airport (LEVF) | 2026-09-30 17:53 UTC | 2026-09-30 18:12 UTC | 19m |
| N319EG |  | Ramona Airport (KRNM) | Santa Barbara Municipal Airport (KSBA) | 2026-09-30 16:30 UTC | 2026-09-30 18:10 UTC | 1h 39m |
| N738VV |  | 74OR (74OR) | Mc Minnville Municipal Airport (KMMV) | 2026-09-30 17:53 UTC | 2026-09-30 18:10 UTC | 17m |
| N682MA |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-09-30 17:54 UTC | 2026-09-30 18:09 UTC | 15m |
| N9055F |  | Fairbanks International Airport (PAFA) | Fairbanks International Airport (PAFA) | 2026-09-30 16:31 UTC | 2026-09-30 18:09 UTC | 1h 38m |
| BAW139 | British Airways | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-30 08:56 UTC | 2026-09-30 18:07 UTC | 9h 10m |
| N24336 |  | Felts Field (KSFF) | Felts Field (KSFF) | 2026-09-30 17:55 UTC | 2026-09-30 18:02 UTC | 7m |
| N986GA |  | Atkinson Municipal Airport (KPTS) | Warsaw Municipal Airport (KRAW) | 2026-09-30 17:47 UTC | 2026-09-30 17:59 UTC | 11m |
| N481SA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-09-30 17:42 UTC | 2026-09-30 17:57 UTC | 14m |
| WIF9PM | WIF | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-30 17:08 UTC | 2026-09-30 17:56 UTC | 48m |
| N448US |  | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-09-30 17:11 UTC | 2026-09-30 17:56 UTC | 44m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-09-30 16:20 UTC | 2026-09-30 17:55 UTC | 1h 34m |
| COOL51 | COO | Fisher County Airport (K56F) | Fisher County Airport (K56F) | 2026-09-30 17:47 UTC | 2026-09-30 17:53 UTC | 6m |
| AER121 | AER | Ted Stevens Anchorage International Airport (PANC) | Fairbanks International Airport (PAFA) | 2026-09-30 16:59 UTC | 2026-09-30 17:52 UTC | 53m |
| N5184J |  | Riverside Airport (KRAL) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-30 17:04 UTC | 2026-09-30 17:51 UTC | 47m |
| N235CD |  | Iberlin Strip (WY23) | Iberlin Strip (WY23) | 2026-09-30 17:35 UTC | 2026-09-30 17:51 UTC | 15m |
| N807TA |  | Washington Executive/Stafford Regional Airport (KRMN) | 1VA9 (1VA9) | 2026-09-30 17:26 UTC | 2026-09-30 17:50 UTC | 23m |
| N813JE |  | Renton Municipal Airport (KRNT) | Renton Municipal Airport (KRNT) | 2026-09-30 16:18 UTC | 2026-09-30 17:49 UTC | 1h 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
