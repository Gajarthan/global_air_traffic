# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_17:43:24_UTC-green)

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

**Latest saved flight:** 2026-09-18 17:43:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 17:43:24 UTC

- **262,535** saved flights
- **77,654** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,535** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,180,229.3 tonnes** estimated CO2 emissions
- **184,361,117 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10391 |
| 2 | SkyWest Airlines | 9132 |
| 3 | EJA | 5090 |
| 4 | IndiGo | 4413 |
| 5 | American Airlines | 4115 |
| 6 | Southwest Airlines | 3854 |
| 7 | Delta Air Lines | 3279 |
| 8 | ENY | 3097 |
| 9 | LATAM Airlines | 2528 |
| 10 | AZU | 2465 |
| 11 | Vueling | 2209 |
| 12 | WIF | 2123 |
| 13 | LXJ | 2054 |
| 14 | Lufthansa | 2029 |
| 15 | easyJet | 1775 |
| 16 | Swiss International | 1736 |
| 17 | QLK | 1698 |
| 18 | AXM | 1655 |
| 19 | EJU | 1655 |
| 20 | United Airlines | 1609 |
| 21 | Alaska Airlines | 1556 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1479 |
| 24 | PGT | 1474 |
| 25 | GLO | 1465 |
| 26 | Air France | 1441 |
| 27 | VIV | 1433 |
| 28 | Wizz Air | 1427 |
| 29 | TKR | 1275 |
| 30 | CXK | 1272 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218061 |
| 2 | 🇪🇸 ES | 16564 |
| 3 | 🇧🇷 BR | 15361 |
| 4 | 🇦🇺 AU | 15072 |
| 5 | 🇨🇦 CA | 14605 |
| 6 | 🇮🇹 IT | 14276 |
| 7 | 🇮🇳 IN | 13931 |
| 8 | 🇩🇪 DE | 12701 |
| 9 | 🇬🇧 GB | 12197 |
| 10 | 🇨🇴 CO | 11858 |
| 11 | 🇫🇷 FR | 10508 |
| 12 | 🇯🇵 JP | 10179 |
| 13 | 🇹🇷 TR | 7947 |
| 14 | 🇬🇷 GR | 7621 |
| 15 | 🇲🇽 MX | 7219 |
| 16 | 🇨🇭 CH | 7014 |
| 17 | 🇳🇴 NO | 6493 |
| 18 | 🇹🇭 TH | 4707 |
| 19 | 🇲🇾 MY | 4463 |
| 20 | 🇿🇦 ZA | 4430 |
| 21 | 🇵🇱 PL | 4332 |
| 22 | 🇳🇿 NZ | 3639 |
| 23 | 🇵🇭 PH | 3499 |
| 24 | 🇬🇹 GT | 3348 |
| 25 | 🇭🇷 HR | 2999 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2625 |
| 28 | 🇲🇪 ME | 2465 |
| 29 | 🇳🇱 NL | 2346 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5369 |
| 2 | Denver International Airport |  | US | 4242 |
| 3 | Indira Gandhi International Airport |  | IN | 3157 |
| 4 | Tokyo International Airport |  | JP | 3038 |
| 5 | Harry Reid International Airport |  | US | 2792 |
| 6 | Guaymaral Airport |  | CO | 2778 |
| 7 | El Dorado International Airport |  | CO | 2770 |
| 8 | Zurich Airport |  | CH | 2738 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2641 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2545 |
| 11 | La Aurora Airport |  | GT | 2544 |
| 12 | Salt Lake City International Airport |  | US | 2317 |
| 13 | Chicago O'Hare International Airport |  | US | 2263 |
| 14 | Congonhas Airport |  | BR | 2241 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2142 |
| 16 | Capua Airport |  | IT | 2051 |
| 17 | Madrid Barajas International Airport |  | ES | 2031 |
| 18 | Frankfurt am Main International Airport |  | DE | 2004 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1979 |
| 20 | Malpensa International Airport |  | IT | 1888 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1883 |
| 22 | Charles de Gaulle International Airport |  | FR | 1858 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1805 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1797 |
| 26 | Macau International Airport |  | MO | 1743 |
| 27 | Ninoy Aquino International Airport |  | PH | 1716 |
| 28 | Barcelona International Airport |  | ES | 1639 |
| 29 | Charlotte/Douglas International Airport |  | US | 1635 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1614 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1593 |
| 33 | Seattle-Tacoma International Airport |  | US | 1540 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1528 |
| 35 | Don Mueang International Airport |  | TH | 1498 |
| 36 | Calgary International Airport |  | CA | 1497 |
| 37 | Bengaluru International Airport |  | IN | 1489 |
| 38 | Oslo Gardermoen Airport |  | NO | 1477 |
| 39 | Vancouver International Airport |  | CA | 1468 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1405 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 979 | 21m | 244 km | 4,122.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 714 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 426 | 44m | 555 km | 4,079.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 400 | 44m | 241 km | 1,661.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 369 | 24m | 218 km | 1,390.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 325 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 305 | 19m | 144 km | 758.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 280 | 42m | 535 km | 2,586.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 279 | 28m | 152 km | 729.1 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N305UM |  | Coral Creek Airport (FA54) | 69FL (69FL) | 2026-09-18 17:32 UTC | 2026-09-18 17:43 UTC | 11m |
| CUL558 | CUL | Lee Vining Airport (KO24) | 6CL4 (6CL4) | 2026-09-18 17:10 UTC | 2026-09-18 17:39 UTC | 28m |
| AFR218 | Air France | Charles de Gaulle International Airport (LFPG) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-18 09:13 UTC | 2026-09-18 17:32 UTC | 8h 19m |
| BOE088 | BOE | Boeing Field/King County International Airport (KBFI) | Othello Municipal Airport (KS70) | 2026-09-18 16:14 UTC | 2026-09-18 17:29 UTC | 1h 14m |
| N92AG |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-09-18 16:15 UTC | 2026-09-18 17:28 UTC | 1h 12m |
| SPTWN | SPT | Gdańsk Lech Wałęsa Airport (EPGD) | Gdańsk Lech Wałęsa Airport (EPGD) | 2026-09-18 17:00 UTC | 2026-09-18 17:25 UTC | 25m |
| N419AM |  | Ravenwood Airport (IL02) | Ravenwood Airport (IL02) | 2026-09-18 16:28 UTC | 2026-09-18 17:22 UTC | 54m |
| G72481 |  | Salt Lake City International Airport (KSLC) | KU42 (KU42) | 2026-09-18 16:45 UTC | 2026-09-18 17:22 UTC | 37m |
| VTHMA | VTH | Jamnagar Airport (VAJM) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-18 16:27 UTC | 2026-09-18 17:20 UTC | 53m |
| FH040 |  | Santa Rosa Nolf Airport (KNGS) | Whiting Field Nas South Airport (KNDZ) | 2026-09-18 16:56 UTC | 2026-09-18 17:19 UTC | 22m |
| N33NE |  | Ted Stevens Anchorage International Airport (PANC) | King Salmon Airport (PAKN) | 2026-09-18 16:03 UTC | 2026-09-18 17:19 UTC | 1h 15m |
| N13715 |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-09-18 17:07 UTC | 2026-09-18 17:18 UTC | 11m |
| N321AP |  | Philadelphia International Airport (KPHL) | Scottsdale Airport (KSDL) | 2026-09-18 13:06 UTC | 2026-09-18 17:16 UTC | 4h 10m |
| N944VB |  | Hampton Roads Executive Airport (KPVG) | Hampton Roads Executive Airport (KPVG) | 2026-09-18 16:55 UTC | 2026-09-18 17:16 UTC | 20m |
| DFTTT | DFT | Graz Airport (LOWG) | Bonn-Hangelar Airport (EDKB) | 2026-09-18 15:40 UTC | 2026-09-18 17:16 UTC | 1h 35m |
| N160EA |  | Glendale Regional Airport (KGEU) | Montezuma Airport (19AZ) | 2026-09-18 16:29 UTC | 2026-09-18 17:16 UTC | 46m |
| N74685 |  | Albany International Airport (KALB) | Albany International Airport (KALB) | 2026-09-18 17:09 UTC | 2026-09-18 17:14 UTC | 5m |
| N387TX |  | Phoenix Deer Valley Airport (KDVT) | AZ86 (AZ86) | 2026-09-18 16:50 UTC | 2026-09-18 17:13 UTC | 22m |
| LXJ306 | LXJ | Dekalb-Peachtree Airport (KPDK) | Godspeed Airpark (8MS2) | 2026-09-18 16:34 UTC | 2026-09-18 17:10 UTC | 36m |
| CNS5625 | CNS | Washington Dulles International Airport (KIAD) | Lincoln Airport (KLNK) | 2026-09-18 14:43 UTC | 2026-09-18 17:09 UTC | 2h 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
