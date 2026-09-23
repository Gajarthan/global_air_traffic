# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_20:13:44_UTC-green)

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

**Latest saved flight:** 2026-09-23 20:13:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 20:13:44 UTC

- **267,582** saved flights
- **78,613** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,582** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,245,056.0 tonnes** estimated CO2 emissions
- **188,119,188 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10568 |
| 2 | SkyWest Airlines | 9309 |
| 3 | EJA | 5204 |
| 4 | IndiGo | 4486 |
| 5 | American Airlines | 4169 |
| 6 | Southwest Airlines | 3931 |
| 7 | Delta Air Lines | 3328 |
| 8 | ENY | 3146 |
| 9 | LATAM Airlines | 2579 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2240 |
| 12 | WIF | 2172 |
| 13 | LXJ | 2100 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1797 |
| 16 | Swiss International | 1759 |
| 17 | QLK | 1722 |
| 18 | EJU | 1685 |
| 19 | AXM | 1671 |
| 20 | United Airlines | 1640 |
| 21 | Alaska Airlines | 1582 |
| 22 | All Nippon Airways | 1542 |
| 23 | PGT | 1508 |
| 24 | WMT | 1500 |
| 25 | GLO | 1492 |
| 26 | Air France | 1470 |
| 27 | VIV | 1462 |
| 28 | Wizz Air | 1454 |
| 29 | CXK | 1307 |
| 30 | AEE | 1287 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222502 |
| 2 | 🇪🇸 ES | 16803 |
| 3 | 🇧🇷 BR | 15640 |
| 4 | 🇦🇺 AU | 15362 |
| 5 | 🇨🇦 CA | 14917 |
| 6 | 🇮🇹 IT | 14527 |
| 7 | 🇮🇳 IN | 14189 |
| 8 | 🇩🇪 DE | 12880 |
| 9 | 🇬🇧 GB | 12413 |
| 10 | 🇨🇴 CO | 12229 |
| 11 | 🇫🇷 FR | 10663 |
| 12 | 🇯🇵 JP | 10303 |
| 13 | 🇹🇷 TR | 8111 |
| 14 | 🇬🇷 GR | 7740 |
| 15 | 🇲🇽 MX | 7378 |
| 16 | 🇨🇭 CH | 7133 |
| 17 | 🇳🇴 NO | 6625 |
| 18 | 🇹🇭 TH | 4792 |
| 19 | 🇲🇾 MY | 4506 |
| 20 | 🇿🇦 ZA | 4482 |
| 21 | 🇵🇱 PL | 4392 |
| 22 | 🇳🇿 NZ | 3726 |
| 23 | 🇵🇭 PH | 3549 |
| 24 | 🇬🇹 GT | 3389 |
| 25 | 🇭🇷 HR | 3054 |
| 26 | 🇰🇷 KR | 3033 |
| 27 | 🇲🇦 MA | 2671 |
| 28 | 🇲🇪 ME | 2510 |
| 29 | 🇳🇱 NL | 2399 |
| 30 | 🇮🇩 ID | 2230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5455 |
| 2 | Denver International Airport |  | US | 4345 |
| 3 | Indira Gandhi International Airport |  | IN | 3209 |
| 4 | Tokyo International Airport |  | JP | 3083 |
| 5 | El Dorado International Airport |  | CO | 2886 |
| 6 | Harry Reid International Airport |  | US | 2859 |
| 7 | Guaymaral Airport |  | CO | 2805 |
| 8 | Zurich Airport |  | CH | 2779 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2685 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2577 |
| 11 | La Aurora Airport |  | GT | 2575 |
| 12 | Salt Lake City International Airport |  | US | 2359 |
| 13 | Chicago O'Hare International Airport |  | US | 2294 |
| 14 | Congonhas Airport |  | BR | 2280 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2187 |
| 16 | Capua Airport |  | IT | 2086 |
| 17 | Madrid Barajas International Airport |  | ES | 2060 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1925 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1907 |
| 22 | Charles de Gaulle International Airport |  | FR | 1898 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1877 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1874 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1816 |
| 26 | Macau International Airport |  | MO | 1778 |
| 27 | Ninoy Aquino International Airport |  | PH | 1742 |
| 28 | Charlotte/Douglas International Airport |  | US | 1671 |
| 29 | Barcelona International Airport |  | ES | 1665 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1614 |
| 33 | Seattle-Tacoma International Airport |  | US | 1566 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1564 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1517 |
| 37 | Bengaluru International Airport |  | IN | 1511 |
| 38 | Oslo Gardermoen Airport |  | NO | 1506 |
| 39 | Vancouver International Airport |  | CA | 1497 |
| 40 | Antalya International Airport |  | TR | 1429 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1003 | 21m | 244 km | 4,223.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 674 | 1h 6m | 770 km | 8,953.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 595 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 428 | 27m | 275 km | 2,028.1 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 409 | 44m | 241 km | 1,698.9 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 363 | 21m | 250 km | 1,567.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 355 | 23m | 55 km | 337.4 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 339 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 333 | 26m | 215 km | 1,233.3 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 285 | 18m | 14 km | 71.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N328KT |  | Bend Municipal Airport (KBDN) | Madras Municipal Airport (KS33) | 2026-09-23 19:39 UTC | 2026-09-23 20:13 UTC | 34m |
| N49950 |  | Fremont Municipal Airport (KFET) | Scribner State Airport (KSCB) | 2026-09-23 19:59 UTC | 2026-09-23 20:10 UTC | 10m |
| N716AT |  | Ralph Wien Memorial Airport (PAOT) | Bob Baker Memorial Airport (PAIK) | 2026-09-23 19:37 UTC | 2026-09-23 20:05 UTC | 28m |
| CGLZD | CGL | Peterborough Airport (CYPQ) | Billy Bishop Toronto City Airport (CYTZ) | 2026-09-23 19:39 UTC | 2026-09-23 20:01 UTC | 21m |
| N359RX |  | Eagles Mere Field (40PN) | 3PA4 (3PA4) | 2026-09-23 17:11 UTC | 2026-09-23 19:59 UTC | 2h 48m |
| HKE623 | HKE | Tokyo International Airport (RJTT) | Chek Lap Kok International Airport (VHHH) | 2026-09-23 16:05 UTC | 2026-09-23 19:59 UTC | 3h 54m |
| N8486R |  | S.C. Stagner Field (26AL) | Jeremiah Denton Airport (K4R9) | 2026-09-23 19:36 UTC | 2026-09-23 19:53 UTC | 16m |
| N42477 |  | Riverside Airport (KRAL) | Ramona Airport (KRNM) | 2026-09-23 19:13 UTC | 2026-09-23 19:52 UTC | 38m |
| BOX714 | BOX | Dubai International Airport (OMDB) | Zhuhai Airport (ZGSD) | 2026-09-23 13:07 UTC | 2026-09-23 19:48 UTC | 6h 41m |
| ANVIL11 | ANV | Fairchild Afb Airport (KSKA) | Fairchild Afb Airport (KSKA) | 2026-09-23 19:07 UTC | 2026-09-23 19:48 UTC | 41m |
| CGMPP | CGM | Winnipeg James Armstrong Richardson International Airport (CYWG) | Matheson Island Airport (CJT2) | 2026-09-23 19:16 UTC | 2026-09-23 19:48 UTC | 31m |
| BULET47 | BUL | Catalina Airport (KAVX) | San Clemente Island Nalf Airport (KNUC) | 2026-09-23 19:26 UTC | 2026-09-23 19:47 UTC | 20m |
| PAT171 | PAT | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-09-23 19:09 UTC | 2026-09-23 19:47 UTC | 38m |
| UPS4 | UPS | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-09-23 08:33 UTC | 2026-09-23 19:46 UTC | 11h 13m |
| RYR2QU | Ryanair | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-09-23 18:45 UTC | 2026-09-23 19:43 UTC | 58m |
| N5252N |  | 5FD3 (5FD3) | Marianna Municipal Airport (KMAI) | 2026-09-23 19:29 UTC | 2026-09-23 19:36 UTC | 6m |
| N87PW |  | Boise Air Trml/Gowen Field (KBOI) | Freedom Air Ranch Airport (0WY0) | 2026-09-23 18:58 UTC | 2026-09-23 19:36 UTC | 37m |
| N800VP |  | Payson Airport (KPAN) | Payson Airport (KPAN) | 2026-09-23 19:33 UTC | 2026-09-23 19:33 UTC | 0m |
| N904SH |  | Joe Foss Field (KFSD) | Carlson Ag Airport (1MY1) | 2026-09-23 18:53 UTC | 2026-09-23 19:32 UTC | 38m |
| N204CF |  | Kalamazoo/Battle Creek International Airport (KAZO) | Boyne Mountain Airport (KBFA) | 2026-09-23 18:56 UTC | 2026-09-23 19:31 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
