# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_20:58:06_UTC-green)

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

**Latest saved flight:** 2026-09-19 20:58:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 20:58:06 UTC

- **263,918** saved flights
- **77,925** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,918** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,197,295.0 tonnes** estimated CO2 emissions
- **185,350,436 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10442 |
| 2 | SkyWest Airlines | 9172 |
| 3 | EJA | 5130 |
| 4 | IndiGo | 4437 |
| 5 | American Airlines | 4130 |
| 6 | Southwest Airlines | 3883 |
| 7 | Delta Air Lines | 3288 |
| 8 | ENY | 3111 |
| 9 | LATAM Airlines | 2545 |
| 10 | AZU | 2484 |
| 11 | Vueling | 2216 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2068 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1742 |
| 17 | QLK | 1701 |
| 18 | EJU | 1665 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1618 |
| 21 | Alaska Airlines | 1563 |
| 22 | All Nippon Airways | 1522 |
| 23 | PGT | 1486 |
| 24 | WMT | 1484 |
| 25 | GLO | 1470 |
| 26 | Air France | 1445 |
| 27 | VIV | 1441 |
| 28 | Wizz Air | 1431 |
| 29 | CXK | 1278 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219293 |
| 2 | 🇪🇸 ES | 16633 |
| 3 | 🇧🇷 BR | 15450 |
| 4 | 🇦🇺 AU | 15107 |
| 5 | 🇨🇦 CA | 14697 |
| 6 | 🇮🇹 IT | 14357 |
| 7 | 🇮🇳 IN | 14017 |
| 8 | 🇩🇪 DE | 12748 |
| 9 | 🇬🇧 GB | 12251 |
| 10 | 🇨🇴 CO | 11971 |
| 11 | 🇫🇷 FR | 10547 |
| 12 | 🇯🇵 JP | 10206 |
| 13 | 🇹🇷 TR | 7999 |
| 14 | 🇬🇷 GR | 7656 |
| 15 | 🇲🇽 MX | 7259 |
| 16 | 🇨🇭 CH | 7047 |
| 17 | 🇳🇴 NO | 6514 |
| 18 | 🇹🇭 TH | 4732 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4350 |
| 22 | 🇳🇿 NZ | 3654 |
| 23 | 🇵🇭 PH | 3509 |
| 24 | 🇬🇹 GT | 3364 |
| 25 | 🇭🇷 HR | 3010 |
| 26 | 🇰🇷 KR | 2992 |
| 27 | 🇲🇦 MA | 2642 |
| 28 | 🇲🇪 ME | 2474 |
| 29 | 🇳🇱 NL | 2366 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5394 |
| 2 | Denver International Airport |  | US | 4269 |
| 3 | Indira Gandhi International Airport |  | IN | 3167 |
| 4 | Tokyo International Airport |  | JP | 3047 |
| 5 | Harry Reid International Airport |  | US | 2807 |
| 6 | El Dorado International Airport |  | CO | 2806 |
| 7 | Guaymaral Airport |  | CO | 2783 |
| 8 | Zurich Airport |  | CH | 2746 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2652 |
| 10 | La Aurora Airport |  | GT | 2556 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2555 |
| 12 | Salt Lake City International Airport |  | US | 2326 |
| 13 | Chicago O'Hare International Airport |  | US | 2267 |
| 14 | Congonhas Airport |  | BR | 2255 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2156 |
| 16 | Capua Airport |  | IT | 2065 |
| 17 | Madrid Barajas International Airport |  | ES | 2039 |
| 18 | Frankfurt am Main International Airport |  | DE | 2014 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1990 |
| 20 | Malpensa International Airport |  | IT | 1902 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1890 |
| 22 | Charles de Gaulle International Airport |  | FR | 1863 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1857 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1832 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1803 |
| 26 | Macau International Airport |  | MO | 1754 |
| 27 | Ninoy Aquino International Airport |  | PH | 1723 |
| 28 | Barcelona International Airport |  | ES | 1647 |
| 29 | Charlotte/Douglas International Airport |  | US | 1646 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1623 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1602 |
| 33 | Seattle-Tacoma International Airport |  | US | 1547 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1539 |
| 35 | Calgary International Airport |  | CA | 1505 |
| 36 | Don Mueang International Airport |  | TH | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1498 |
| 38 | Oslo Gardermoen Airport |  | NO | 1486 |
| 39 | Vancouver International Airport |  | CA | 1476 |
| 40 | Antalya International Airport |  | TR | 1414 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 987 | 21m | 244 km | 4,156.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 724 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 662 | 1h 6m | 770 km | 8,794.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 657 | 24m | 225 km | 2,548.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 417 | 1h 50m | 1,423 km | 10,233.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 377 | 24m | 218 km | 1,420.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 335 | 12m | - | - |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 283 | 42m | 535 km | 2,613.7 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 263 | 18m | 14 km | 65.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-09-19 06:00 UTC | 2026-09-19 20:58 UTC | 14h 57m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-19 20:37 UTC | 2026-09-19 20:53 UTC | 16m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Macau International Airport (VMMC) | 2026-09-19 06:17 UTC | 2026-09-19 20:52 UTC | 14h 35m |
| SLICK26 | SLI | WV23 (WV23) | WV23 (WV23) | 2026-09-19 20:08 UTC | 2026-09-19 20:47 UTC | 39m |
| CGPKA | CGP | Prince George Airport (CYXS) | Beaverley Airport (CBA8) | 2026-09-19 20:19 UTC | 2026-09-19 20:47 UTC | 27m |
| N100J |  | Rogue Valley International/Medford Airport (KMFR) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-19 19:43 UTC | 2026-09-19 20:38 UTC | 54m |
| N406M |  | Merrill Field (PAMR) | Tin Creek Airport (PAFL) | 2026-09-19 19:51 UTC | 2026-09-19 20:34 UTC | 43m |
| ERU938 | ERU | Daytona Beach International Airport (KDAB) | Deland Municipal-Sidney H Taylor Field (KDED) | 2026-09-19 19:49 UTC | 2026-09-19 20:34 UTC | 45m |
| N1818G |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-09-19 18:28 UTC | 2026-09-19 20:34 UTC | 2h 6m |
| HCCRE | HCC | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | Nuevo Aeropuerto Internacional Mariscal Sucre (SEQM) | 2026-09-19 19:35 UTC | 2026-09-19 20:33 UTC | 57m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-09-19 18:12 UTC | 2026-09-19 20:33 UTC | 2h 20m |
| QTR15P | Qatar Airways | Oslo Gardermoen Airport (ENGM) | Al Udeid Air Base (OTBH) | 2026-09-19 14:42 UTC | 2026-09-19 20:33 UTC | 5h 50m |
| N453GB |  | Lake Riverside Estates Airport (54CL) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-19 20:15 UTC | 2026-09-19 20:31 UTC | 16m |
| ES801 |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Mather Airport (KMHR) | 2026-09-19 19:53 UTC | 2026-09-19 20:29 UTC | 36m |
| XE1180 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-09-19 19:28 UTC | 2026-09-19 20:29 UTC | 1h 0m |
| N551HQ |  | Groveland/Yosemite Airport (KE45) | Groveland/Yosemite Airport (KE45) | 2026-09-19 20:27 UTC | 2026-09-19 20:28 UTC | 1m |
| HGO810 | HGO | East Midlands Airport (EGNX) | Zhuhai Airport (ZGSD) | 2026-09-19 08:24 UTC | 2026-09-19 20:27 UTC | 12h 3m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-09-19 20:10 UTC | 2026-09-19 20:26 UTC | 16m |
| N466JG |  | Boerne Stage Airfield (K5C1) | Minden-Tahoe Airport (KMEV) | 2026-09-19 17:20 UTC | 2026-09-19 20:24 UTC | 3h 3m |
| XCLMO | XCL | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-09-19 20:19 UTC | 2026-09-19 20:24 UTC | 4m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
