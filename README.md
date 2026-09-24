# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_16:52:40_UTC-green)

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

**Latest saved flight:** 2026-09-24 16:52:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-24 16:52:40 UTC

- **268,322** saved flights
- **78,754** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,322** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,254,603.3 tonnes** estimated CO2 emissions
- **188,672,657 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10589 |
| 2 | SkyWest Airlines | 9337 |
| 3 | EJA | 5215 |
| 4 | IndiGo | 4499 |
| 5 | American Airlines | 4177 |
| 6 | Southwest Airlines | 3943 |
| 7 | Delta Air Lines | 3336 |
| 8 | ENY | 3152 |
| 9 | LATAM Airlines | 2583 |
| 10 | AZU | 2513 |
| 11 | Vueling | 2242 |
| 12 | WIF | 2181 |
| 13 | LXJ | 2109 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1803 |
| 16 | Swiss International | 1760 |
| 17 | QLK | 1732 |
| 18 | EJU | 1687 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1644 |
| 21 | Alaska Airlines | 1586 |
| 22 | All Nippon Airways | 1546 |
| 23 | PGT | 1509 |
| 24 | WMT | 1502 |
| 25 | GLO | 1494 |
| 26 | Air France | 1477 |
| 27 | VIV | 1464 |
| 28 | Wizz Air | 1458 |
| 29 | CXK | 1312 |
| 30 | AEE | 1291 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223161 |
| 2 | 🇪🇸 ES | 16846 |
| 3 | 🇧🇷 BR | 15670 |
| 4 | 🇦🇺 AU | 15443 |
| 5 | 🇨🇦 CA | 14962 |
| 6 | 🇮🇹 IT | 14550 |
| 7 | 🇮🇳 IN | 14228 |
| 8 | 🇩🇪 DE | 12897 |
| 9 | 🇬🇧 GB | 12439 |
| 10 | 🇨🇴 CO | 12275 |
| 11 | 🇫🇷 FR | 10689 |
| 12 | 🇯🇵 JP | 10332 |
| 13 | 🇹🇷 TR | 8131 |
| 14 | 🇬🇷 GR | 7765 |
| 15 | 🇲🇽 MX | 7396 |
| 16 | 🇨🇭 CH | 7143 |
| 17 | 🇳🇴 NO | 6642 |
| 18 | 🇹🇭 TH | 4805 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4490 |
| 21 | 🇵🇱 PL | 4402 |
| 22 | 🇳🇿 NZ | 3749 |
| 23 | 🇵🇭 PH | 3558 |
| 24 | 🇬🇹 GT | 3400 |
| 25 | 🇭🇷 HR | 3060 |
| 26 | 🇰🇷 KR | 3041 |
| 27 | 🇲🇦 MA | 2678 |
| 28 | 🇲🇪 ME | 2517 |
| 29 | 🇳🇱 NL | 2403 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5465 |
| 2 | Denver International Airport |  | US | 4357 |
| 3 | Indira Gandhi International Airport |  | IN | 3218 |
| 4 | Tokyo International Airport |  | JP | 3091 |
| 5 | El Dorado International Airport |  | CO | 2902 |
| 6 | Harry Reid International Airport |  | US | 2870 |
| 7 | Guaymaral Airport |  | CO | 2806 |
| 8 | Zurich Airport |  | CH | 2783 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2696 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2588 |
| 11 | La Aurora Airport |  | GT | 2584 |
| 12 | Salt Lake City International Airport |  | US | 2363 |
| 13 | Chicago O'Hare International Airport |  | US | 2299 |
| 14 | Congonhas Airport |  | BR | 2283 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2194 |
| 16 | Capua Airport |  | IT | 2089 |
| 17 | Madrid Barajas International Airport |  | ES | 2069 |
| 18 | Frankfurt am Main International Airport |  | DE | 2037 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2028 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1914 |
| 22 | Charles de Gaulle International Airport |  | FR | 1906 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1883 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1879 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1817 |
| 26 | Macau International Airport |  | MO | 1786 |
| 27 | Ninoy Aquino International Airport |  | PH | 1746 |
| 28 | Charlotte/Douglas International Airport |  | US | 1675 |
| 29 | Barcelona International Airport |  | ES | 1670 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1658 |
| 31 | Viracopos International Airport |  | BR | 1622 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1572 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1568 |
| 35 | Calgary International Airport |  | CA | 1528 |
| 36 | Don Mueang International Airport |  | TH | 1522 |
| 37 | Bengaluru International Airport |  | IN | 1513 |
| 38 | Oslo Gardermoen Airport |  | NO | 1508 |
| 39 | Vancouver International Airport |  | CA | 1503 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1119 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1006 | 21m | 244 km | 4,236.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 676 | 1h 6m | 770 km | 8,980.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 669 | 24m | 225 km | 2,595.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 442 | 44m | 555 km | 4,232.4 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 383 | 24m | 218 km | 1,442.9 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 359 | 23m | 55 km | 341.2 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 342 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 341 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 339 | 1h 6m | 706 km | 4,127.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 337 | 19m | 99 km | 577.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 334 | 26m | 215 km | 1,237.0 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 312 | 19m | 144 km | 776.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 286 | 18m | 14 km | 71.5 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIC4HH | Air India | Indira Gandhi International Airport (VIDP) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-24 13:57 UTC | 2026-09-24 16:52 UTC | 2h 55m |
| DHFEJ | DHF | Reichelsheim Airport (EDFB) | Reichelsheim Airport (EDFB) | 2026-09-24 16:29 UTC | 2026-09-24 16:44 UTC | 15m |
| CXK238 | CXK | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-09-24 15:56 UTC | 2026-09-24 16:43 UTC | 47m |
| ARCAS02 | ARC | Kickapoo Downtown Airport (KCWC) | TX20 (TX20) | 2026-09-24 16:28 UTC | 2026-09-24 16:42 UTC | 14m |
| SFE1 | SFE | Bud Dryden Airport (TX05) | Bud Dryden Airport (TX05) | 2026-09-24 15:41 UTC | 2026-09-24 16:40 UTC | 58m |
| TGCMB | TGC | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-09-24 16:17 UTC | 2026-09-24 16:34 UTC | 17m |
| CUL558 | CUL | 6CL4 (6CL4) | 6CL4 (6CL4) | 2026-09-24 16:23 UTC | 2026-09-24 16:34 UTC | 11m |
| N24350 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-09-24 16:17 UTC | 2026-09-24 16:30 UTC | 12m |
| N6038V |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-09-24 16:09 UTC | 2026-09-24 16:30 UTC | 20m |
| N58FF |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-09-24 15:40 UTC | 2026-09-24 16:30 UTC | 49m |
|  |  | Okc Will Rogers International Airport (KOKC) | Page Airport (WA10) | 2026-09-24 13:49 UTC | 2026-09-24 16:29 UTC | 2h 40m |
| N814SS |  | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-09-24 16:19 UTC | 2026-09-24 16:29 UTC | 9m |
| N48FF |  | Rocky Mountain Metro Airport (KBJC) | Rocky Mountain Metro Airport (KBJC) | 2026-09-24 16:06 UTC | 2026-09-24 16:28 UTC | 21m |
| AUR209 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-09-24 16:13 UTC | 2026-09-24 16:27 UTC | 14m |
| N53LT |  | Van Nuys Airport (KVNY) | Buchanan Field (KCCR) | 2026-09-24 15:30 UTC | 2026-09-24 16:26 UTC | 55m |
| N600SL |  | Council Bluffs Municipal Airport (KCBF) | Ankeny Regional Airport (KIKV) | 2026-09-24 15:50 UTC | 2026-09-24 16:24 UTC | 34m |
| RFS717 | RFS | Seattle Paine Field International Airport (KPAE) | Arlington Municipal Airport (KAWO) | 2026-09-24 16:11 UTC | 2026-09-24 16:24 UTC | 13m |
| SNAKE2 | SNA | 4XA5 (4XA5) | Halliburton Field (KDUC) | 2026-09-24 15:45 UTC | 2026-09-24 16:18 UTC | 33m |
| MNB6041 | MNB | Sharjah International Airport (OMSJ) | Macau International Airport (VMMC) | 2026-09-24 09:01 UTC | 2026-09-24 16:15 UTC | 7h 14m |
| N911VU |  | Grand Junction Regional Airport (KGJT) | Telluride Regional Airport (KTEX) | 2026-09-24 15:52 UTC | 2026-09-24 16:14 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
