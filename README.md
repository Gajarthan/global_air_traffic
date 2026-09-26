# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_21:35:51_UTC-green)

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

**Latest saved flight:** 2026-09-26 21:35:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-26 21:35:51 UTC

- **270,495** saved flights
- **79,241** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,495** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,281,080.0 tonnes** estimated CO2 emissions
- **190,207,534 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10645 |
| 2 | SkyWest Airlines | 9415 |
| 3 | EJA | 5286 |
| 4 | IndiGo | 4525 |
| 5 | American Airlines | 4205 |
| 6 | Southwest Airlines | 3983 |
| 7 | Delta Air Lines | 3360 |
| 8 | ENY | 3179 |
| 9 | LATAM Airlines | 2603 |
| 10 | AZU | 2537 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2198 |
| 13 | LXJ | 2128 |
| 14 | Lufthansa | 2053 |
| 15 | easyJet | 1813 |
| 16 | Swiss International | 1772 |
| 17 | QLK | 1738 |
| 18 | EJU | 1695 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1655 |
| 21 | Alaska Airlines | 1598 |
| 22 | All Nippon Airways | 1553 |
| 23 | PGT | 1524 |
| 24 | WMT | 1513 |
| 25 | GLO | 1507 |
| 26 | Air France | 1485 |
| 27 | VIV | 1476 |
| 28 | Wizz Air | 1470 |
| 29 | CXK | 1330 |
| 30 | AEE | 1296 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225348 |
| 2 | 🇪🇸 ES | 16943 |
| 3 | 🇧🇷 BR | 15817 |
| 4 | 🇦🇺 AU | 15527 |
| 5 | 🇨🇦 CA | 15082 |
| 6 | 🇮🇹 IT | 14629 |
| 7 | 🇮🇳 IN | 14323 |
| 8 | 🇩🇪 DE | 12985 |
| 9 | 🇬🇧 GB | 12516 |
| 10 | 🇨🇴 CO | 12415 |
| 11 | 🇫🇷 FR | 10744 |
| 12 | 🇯🇵 JP | 10372 |
| 13 | 🇹🇷 TR | 8187 |
| 14 | 🇬🇷 GR | 7806 |
| 15 | 🇲🇽 MX | 7468 |
| 16 | 🇨🇭 CH | 7191 |
| 17 | 🇳🇴 NO | 6682 |
| 18 | 🇹🇭 TH | 4831 |
| 19 | 🇲🇾 MY | 4532 |
| 20 | 🇿🇦 ZA | 4516 |
| 21 | 🇵🇱 PL | 4429 |
| 22 | 🇳🇿 NZ | 3785 |
| 23 | 🇵🇭 PH | 3582 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3086 |
| 26 | 🇰🇷 KR | 3051 |
| 27 | 🇲🇦 MA | 2686 |
| 28 | 🇲🇪 ME | 2537 |
| 29 | 🇳🇱 NL | 2418 |
| 30 | 🇮🇩 ID | 2251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5509 |
| 2 | Denver International Airport |  | US | 4404 |
| 3 | Indira Gandhi International Airport |  | IN | 3238 |
| 4 | Tokyo International Airport |  | JP | 3105 |
| 5 | El Dorado International Airport |  | CO | 2940 |
| 6 | Harry Reid International Airport |  | US | 2901 |
| 7 | Guaymaral Airport |  | CO | 2821 |
| 8 | Zurich Airport |  | CH | 2804 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2716 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2599 |
| 12 | Salt Lake City International Airport |  | US | 2386 |
| 13 | Chicago O'Hare International Airport |  | US | 2308 |
| 14 | Congonhas Airport |  | BR | 2307 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2212 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2084 |
| 18 | Frankfurt am Main International Airport |  | DE | 2048 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2043 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1919 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1904 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1888 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1758 |
| 28 | Charlotte/Douglas International Airport |  | US | 1694 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1682 |
| 30 | Barcelona International Airport |  | ES | 1681 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1624 |
| 33 | Seattle-Tacoma International Airport |  | US | 1585 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1584 |
| 35 | Calgary International Airport |  | CA | 1540 |
| 36 | Don Mueang International Airport |  | TH | 1528 |
| 37 | Bengaluru International Airport |  | IN | 1523 |
| 38 | Oslo Gardermoen Airport |  | NO | 1515 |
| 39 | Vancouver International Airport |  | CA | 1511 |
| 40 | Antalya International Airport |  | TR | 1445 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1014 | 21m | 244 km | 4,269.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 749 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 682 | 1h 6m | 770 km | 9,059.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 676 | 24m | 225 km | 2,622.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 446 | 44m | 555 km | 4,270.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 435 | 27m | 275 km | 2,061.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 412 | 44m | 241 km | 1,711.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 345 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 306 | 1h 14m | 961 km | 5,072.1 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 298 | 42m | 535 km | 2,752.2 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 294 | 18m | 14 km | 73.5 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 291 | 1h 50m | 1,304 km | 6,546.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N125PM |  | Erie Municipal Airport (KEIK) | Vance Brand Airport (KLMO) | 2026-09-26 16:22 UTC | 2026-09-26 21:35 UTC | 5h 12m |
| N9824V |  | Olympia Regional Airport (KOLM) | WN36 (WN36) | 2026-09-26 21:01 UTC | 2026-09-26 21:33 UTC | 31m |
| N895CA |  | Boise Air Trml/Gowen Field (KBOI) | Animas Air Park (K00C) | 2026-09-26 20:14 UTC | 2026-09-26 21:31 UTC | 1h 16m |
| N512FA |  | Easterwood Field (KCLL) | Austin Executive Airport (KEDC) | 2026-09-26 20:51 UTC | 2026-09-26 21:30 UTC | 38m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-26 17:45 UTC | 2026-09-26 21:27 UTC | 3h 42m |
| PBR680 | PBR | Boundary Bay Airport (CZBB) | Alert Bay Airport (CYAL) | 2026-09-26 20:21 UTC | 2026-09-26 21:16 UTC | 55m |
| N6523D |  | Camarillo Airport (KCMA) | Oxnard Airport (KOXR) | 2026-09-26 20:40 UTC | 2026-09-26 21:15 UTC | 35m |
| VAR663 | VAR | Phoenix Goodyear Airport (KGYR) | Chiriaco Summit Airport (KL77) | 2026-09-26 19:51 UTC | 2026-09-26 21:15 UTC | 1h 24m |
| CNS919 | CNS | Aurora State Airport (KUAO) | OL04 (OL04) | 2026-09-26 20:50 UTC | 2026-09-26 21:12 UTC | 22m |
| N939AM |  | Hayward Executive Airport (KHWD) | Lincoln Airport (KLNK) | 2026-09-26 18:10 UTC | 2026-09-26 21:08 UTC | 2h 57m |
| CFC520 | CFC | Masonry Field (93MT) | Lethbridge Airport (CYQL) | 2026-09-26 20:49 UTC | 2026-09-26 21:07 UTC | 18m |
| N36JC |  | Olympia Regional Airport (KOLM) | Olympia Regional Airport (KOLM) | 2026-09-26 21:04 UTC | 2026-09-26 21:04 UTC | 0m |
| EJA621 | EJA | Indianapolis International Airport (KIND) | Purdue University Airport (KLAF) | 2026-09-26 20:47 UTC | 2026-09-26 21:02 UTC | 14m |
| UBG341 | UBG | VGZR (VGZR) | Fujairah International Airport (OMFJ) | 2026-09-26 16:46 UTC | 2026-09-26 21:01 UTC | 4h 15m |
| BOE471 | BOE | Renton Municipal Airport (KRNT) | 8WA5 (8WA5) | 2026-09-26 19:16 UTC | 2026-09-26 21:00 UTC | 1h 44m |
| TKR914 | TKR | Robert Gray Army Air Field (KGRK) | 14TE (14TE) | 2026-09-26 20:45 UTC | 2026-09-26 21:00 UTC | 15m |
| RYR63GU | Ryanair | Malaga Airport (LEMG) | Leeds Bradford Airport (EGNM) | 2026-09-26 18:28 UTC | 2026-09-26 20:58 UTC | 2h 30m |
| N443BG |  | Wood County Regional Airport (K1G0) | Findlay Airport (KFDY) | 2026-09-26 20:08 UTC | 2026-09-26 20:58 UTC | 50m |
| N1293E |  | Harpers Fly-In Ranch Airport (0FL0) | Airglades Airport (K2IS) | 2026-09-26 20:48 UTC | 2026-09-26 20:58 UTC | 10m |
| QTR58A | Qatar Airways | Edinburgh Airport (EGPH) | Hamad International Airport (OTHH) | 2026-09-26 14:38 UTC | 2026-09-26 20:56 UTC | 6h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
