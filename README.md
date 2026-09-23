# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_12:06:56_UTC-green)

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

**Latest saved flight:** 2026-09-23 12:06:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-23 12:06:56 UTC

- **267,147** saved flights
- **78,514** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **267,147** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,240,307.3 tonnes** estimated CO2 emissions
- **187,843,902 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10550 |
| 2 | SkyWest Airlines | 9290 |
| 3 | EJA | 5194 |
| 4 | IndiGo | 4482 |
| 5 | American Airlines | 4162 |
| 6 | Southwest Airlines | 3930 |
| 7 | Delta Air Lines | 3321 |
| 8 | ENY | 3139 |
| 9 | LATAM Airlines | 2578 |
| 10 | AZU | 2508 |
| 11 | Vueling | 2239 |
| 12 | WIF | 2166 |
| 13 | LXJ | 2095 |
| 14 | Lufthansa | 2043 |
| 15 | easyJet | 1794 |
| 16 | Swiss International | 1759 |
| 17 | QLK | 1722 |
| 18 | EJU | 1684 |
| 19 | AXM | 1671 |
| 20 | United Airlines | 1638 |
| 21 | Alaska Airlines | 1580 |
| 22 | All Nippon Airways | 1542 |
| 23 | PGT | 1507 |
| 24 | WMT | 1500 |
| 25 | GLO | 1491 |
| 26 | Air France | 1468 |
| 27 | VIV | 1461 |
| 28 | Wizz Air | 1452 |
| 29 | CXK | 1300 |
| 30 | AEE | 1286 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 222001 |
| 2 | 🇪🇸 ES | 16777 |
| 3 | 🇧🇷 BR | 15632 |
| 4 | 🇦🇺 AU | 15362 |
| 5 | 🇨🇦 CA | 14885 |
| 6 | 🇮🇹 IT | 14512 |
| 7 | 🇮🇳 IN | 14175 |
| 8 | 🇩🇪 DE | 12861 |
| 9 | 🇬🇧 GB | 12396 |
| 10 | 🇨🇴 CO | 12196 |
| 11 | 🇫🇷 FR | 10655 |
| 12 | 🇯🇵 JP | 10302 |
| 13 | 🇹🇷 TR | 8102 |
| 14 | 🇬🇷 GR | 7729 |
| 15 | 🇲🇽 MX | 7367 |
| 16 | 🇨🇭 CH | 7130 |
| 17 | 🇳🇴 NO | 6612 |
| 18 | 🇹🇭 TH | 4792 |
| 19 | 🇲🇾 MY | 4506 |
| 20 | 🇿🇦 ZA | 4478 |
| 21 | 🇵🇱 PL | 4386 |
| 22 | 🇳🇿 NZ | 3726 |
| 23 | 🇵🇭 PH | 3549 |
| 24 | 🇬🇹 GT | 3386 |
| 25 | 🇭🇷 HR | 3046 |
| 26 | 🇰🇷 KR | 3033 |
| 27 | 🇲🇦 MA | 2666 |
| 28 | 🇲🇪 ME | 2507 |
| 29 | 🇳🇱 NL | 2395 |
| 30 | 🇮🇩 ID | 2230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5441 |
| 2 | Denver International Airport |  | US | 4339 |
| 3 | Indira Gandhi International Airport |  | IN | 3206 |
| 4 | Tokyo International Airport |  | JP | 3082 |
| 5 | El Dorado International Airport |  | CO | 2876 |
| 6 | Harry Reid International Airport |  | US | 2856 |
| 7 | Guaymaral Airport |  | CO | 2800 |
| 8 | Zurich Airport |  | CH | 2777 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2677 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2573 |
| 11 | La Aurora Airport |  | GT | 2572 |
| 12 | Salt Lake City International Airport |  | US | 2357 |
| 13 | Chicago O'Hare International Airport |  | US | 2293 |
| 14 | Congonhas Airport |  | BR | 2277 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2181 |
| 16 | Capua Airport |  | IT | 2084 |
| 17 | Madrid Barajas International Airport |  | ES | 2055 |
| 18 | Frankfurt am Main International Airport |  | DE | 2033 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2023 |
| 20 | Malpensa International Airport |  | IT | 1924 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1904 |
| 22 | Charles de Gaulle International Airport |  | FR | 1895 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1874 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1874 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1813 |
| 26 | Macau International Airport |  | MO | 1778 |
| 27 | Ninoy Aquino International Airport |  | PH | 1742 |
| 28 | Charlotte/Douglas International Airport |  | US | 1666 |
| 29 | Barcelona International Airport |  | ES | 1664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1655 |
| 31 | Viracopos International Airport |  | BR | 1618 |
| 32 | Kuala Lumpur International Airport |  | MY | 1614 |
| 33 | Seattle-Tacoma International Airport |  | US | 1565 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1562 |
| 35 | Calgary International Airport |  | CA | 1527 |
| 36 | Don Mueang International Airport |  | TH | 1517 |
| 37 | Bengaluru International Airport |  | IN | 1509 |
| 38 | Oslo Gardermoen Airport |  | NO | 1504 |
| 39 | Vancouver International Airport |  | CA | 1497 |
| 40 | Antalya International Airport |  | TR | 1428 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1117 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1001 | 21m | 244 km | 4,214.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 740 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 674 | 1h 6m | 770 km | 8,953.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 667 | 24m | 225 km | 2,587.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 594 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 440 | 44m | 555 km | 4,213.2 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 427 | 27m | 275 km | 2,023.4 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 424 | 1h 50m | 1,423 km | 10,405.6 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 408 | 44m | 241 km | 1,694.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 382 | 24m | 218 km | 1,439.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 341 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 338 | 1h 6m | 706 km | 4,115.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 336 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 331 | 26m | 215 km | 1,225.9 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 292 | 42m | 535 km | 2,696.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 283 | 18m | 14 km | 70.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 271 | 15m | 154 km | 718.0 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK672 | CXK | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-09-23 11:54 UTC | 2026-09-23 12:06 UTC | 12m |
| T334 |  | Payerne Airport (LSMP) | Dubendorf Airport (LSMD) | 2026-09-23 11:22 UTC | 2026-09-23 11:55 UTC | 33m |
| YOF | YOF | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-09-23 11:06 UTC | 2026-09-23 11:51 UTC | 44m |
| SMGLR31 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-09-23 11:14 UTC | 2026-09-23 11:49 UTC | 34m |
| HBPPX | HBP | Wangen-Lachen Airport (LSPV) | Speck-Fehraltorf Airport (LSZK) | 2026-09-23 11:30 UTC | 2026-09-23 11:48 UTC | 17m |
| GAM266B | GAM | Buckeburg Airport (ETHB) | Buckeburg Airport (ETHB) | 2026-09-23 10:49 UTC | 2026-09-23 11:45 UTC | 56m |
| MRL53 | MRL | San Javier Airport (LELC) | Alhama De Murcia Airport (LELH) | 2026-09-23 11:01 UTC | 2026-09-23 11:38 UTC | 36m |
| CPA805 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-22 21:16 UTC | 2026-09-23 11:34 UTC | 14h 18m |
| UBG129 | UBG | VGZR (VGZR) | Jessore Airport (VGJR) | 2026-09-23 11:07 UTC | 2026-09-23 11:33 UTC | 25m |
| HBZGK | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-09-23 11:21 UTC | 2026-09-23 11:30 UTC | 9m |
| ROF1104 | ROF | Henri Coanda International Airport (LROP) | Kainardzha Airport (LBKJ) | 2026-09-23 10:54 UTC | 2026-09-23 11:22 UTC | 28m |
| IJM409 | IJM | Karlsruhe Baden-Baden Airport (EDSB) | Samedan Airport (LSZS) | 2026-09-23 10:51 UTC | 2026-09-23 11:19 UTC | 28m |
| IGO515 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Dehradun Airport (VIDN) | 2026-09-23 10:36 UTC | 2026-09-23 11:17 UTC | 40m |
| FHY1548 | FHY | Václav Havel Airport (LKPR) | Karain Airport (LTXE) | 2026-09-23 08:49 UTC | 2026-09-23 11:14 UTC | 2h 25m |
| SFJ87 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-23 10:05 UTC | 2026-09-23 11:13 UTC | 1h 8m |
| AUA617 | Austrian Airlines | Vienna International Airport (LOWW) | Otocac Airport (LDRO) | 2026-09-23 10:37 UTC | 2026-09-23 11:12 UTC | 34m |
| N728MV |  | Fernando Luis Ribas Dominicci Airport (TJIG) | PR07 (PR07) | 2026-09-23 10:44 UTC | 2026-09-23 11:10 UTC | 25m |
| AFR96EU | Air France | Charles de Gaulle International Airport (LFPG) | Nantes Atlantique Airport (LFRS) | 2026-09-23 10:25 UTC | 2026-09-23 11:10 UTC | 45m |
| SEH5JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-09-23 10:43 UTC | 2026-09-23 11:09 UTC | 26m |
| GCBJZ | GCB | Stapleford Aerodrome (EGSG) | Stapleford Aerodrome (EGSG) | 2026-09-23 10:56 UTC | 2026-09-23 11:08 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
