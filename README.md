# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_16:46:41_UTC-green)

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

**Latest saved flight:** 2026-09-21 16:46:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 16:46:41 UTC

- **265,585** saved flights
- **78,241** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,585** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,219,138.6 tonnes** estimated CO2 emissions
- **186,616,729 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10509 |
| 2 | SkyWest Airlines | 9239 |
| 3 | EJA | 5161 |
| 4 | IndiGo | 4463 |
| 5 | American Airlines | 4145 |
| 6 | Southwest Airlines | 3909 |
| 7 | Delta Air Lines | 3304 |
| 8 | ENY | 3128 |
| 9 | LATAM Airlines | 2559 |
| 10 | AZU | 2499 |
| 11 | Vueling | 2229 |
| 12 | WIF | 2149 |
| 13 | LXJ | 2084 |
| 14 | Lufthansa | 2038 |
| 15 | easyJet | 1787 |
| 16 | Swiss International | 1751 |
| 17 | QLK | 1716 |
| 18 | EJU | 1677 |
| 19 | AXM | 1664 |
| 20 | United Airlines | 1626 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1530 |
| 23 | WMT | 1493 |
| 24 | PGT | 1492 |
| 25 | GLO | 1480 |
| 26 | Air France | 1460 |
| 27 | VIV | 1452 |
| 28 | Wizz Air | 1443 |
| 29 | CXK | 1286 |
| 30 | AEE | 1284 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220704 |
| 2 | 🇪🇸 ES | 16700 |
| 3 | 🇧🇷 BR | 15540 |
| 4 | 🇦🇺 AU | 15208 |
| 5 | 🇨🇦 CA | 14784 |
| 6 | 🇮🇹 IT | 14461 |
| 7 | 🇮🇳 IN | 14107 |
| 8 | 🇩🇪 DE | 12800 |
| 9 | 🇬🇧 GB | 12325 |
| 10 | 🇨🇴 CO | 12093 |
| 11 | 🇫🇷 FR | 10608 |
| 12 | 🇯🇵 JP | 10244 |
| 13 | 🇹🇷 TR | 8041 |
| 14 | 🇬🇷 GR | 7692 |
| 15 | 🇲🇽 MX | 7313 |
| 16 | 🇨🇭 CH | 7086 |
| 17 | 🇳🇴 NO | 6564 |
| 18 | 🇹🇭 TH | 4767 |
| 19 | 🇲🇾 MY | 4487 |
| 20 | 🇿🇦 ZA | 4466 |
| 21 | 🇵🇱 PL | 4367 |
| 22 | 🇳🇿 NZ | 3689 |
| 23 | 🇵🇭 PH | 3529 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3028 |
| 26 | 🇰🇷 KR | 3008 |
| 27 | 🇲🇦 MA | 2654 |
| 28 | 🇲🇪 ME | 2488 |
| 29 | 🇳🇱 NL | 2379 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5417 |
| 2 | Denver International Airport |  | US | 4303 |
| 3 | Indira Gandhi International Airport |  | IN | 3191 |
| 4 | Tokyo International Airport |  | JP | 3062 |
| 5 | El Dorado International Airport |  | CO | 2838 |
| 6 | Harry Reid International Airport |  | US | 2833 |
| 7 | Guaymaral Airport |  | CO | 2791 |
| 8 | Zurich Airport |  | CH | 2761 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2663 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2564 |
| 12 | Salt Lake City International Airport |  | US | 2346 |
| 13 | Chicago O'Hare International Airport |  | US | 2279 |
| 14 | Congonhas Airport |  | BR | 2265 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2173 |
| 16 | Capua Airport |  | IT | 2081 |
| 17 | Madrid Barajas International Airport |  | ES | 2048 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2006 |
| 20 | Malpensa International Airport |  | IT | 1918 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1898 |
| 22 | Charles de Gaulle International Airport |  | FR | 1884 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1869 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1859 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1808 |
| 26 | Macau International Airport |  | MO | 1767 |
| 27 | Ninoy Aquino International Airport |  | PH | 1733 |
| 28 | Charlotte/Douglas International Airport |  | US | 1659 |
| 29 | Barcelona International Airport |  | ES | 1658 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1637 |
| 31 | Viracopos International Airport |  | BR | 1611 |
| 32 | Kuala Lumpur International Airport |  | MY | 1609 |
| 33 | Seattle-Tacoma International Airport |  | US | 1558 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1549 |
| 35 | Calgary International Airport |  | CA | 1516 |
| 36 | Don Mueang International Airport |  | TH | 1513 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1494 |
| 39 | Vancouver International Airport |  | CA | 1484 |
| 40 | Antalya International Airport |  | TR | 1422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1115 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 993 | 21m | 244 km | 4,181.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 734 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 667 | 1h 6m | 770 km | 8,860.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 661 | 24m | 225 km | 2,564.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 438 | 44m | 555 km | 4,194.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 351 | 23m | 55 km | 333.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 339 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 335 | 1h 6m | 706 km | 4,078.6 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 332 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 330 | 26m | 215 km | 1,222.2 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 309 | 19m | 144 km | 768.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 288 | 42m | 535 km | 2,659.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 288 | 1h 50m | 1,304 km | 6,479.3 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 275 | 18m | 14 km | 68.8 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3077M |  | Hartford-Brainard Airport (KHFD) | Hartford-Brainard Airport (KHFD) | 2026-09-21 16:08 UTC | 2026-09-21 16:46 UTC | 37m |
| NIT237 | NIT | Heart Of Georgia Regional Airport (KEZM) | Telfair-Wheeler Airport (KMQW) | 2026-09-21 16:30 UTC | 2026-09-21 16:46 UTC | 15m |
| N341P |  | Mesa Gateway Airport (KIWA) | Phoenix Sky Harbor International Airport (KPHX) | 2026-09-21 16:30 UTC | 2026-09-21 16:43 UTC | 12m |
| SAMU13 | SAM | Gap - Tallard Airport (LFNA) | Marseille Provence Airport (LFML) | 2026-09-21 16:02 UTC | 2026-09-21 16:42 UTC | 40m |
| N362BZ |  | Chicago Executive Airport (KPWK) | West Bend Municipal Airport (KETB) | 2026-09-21 15:50 UTC | 2026-09-21 16:36 UTC | 46m |
| N97681 |  | Fernando Luis Ribas Dominicci Airport (TJIG) | Cuylers Airport (02PR) | 2026-09-21 16:03 UTC | 2026-09-21 16:36 UTC | 33m |
| N208W |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-09-21 16:05 UTC | 2026-09-21 16:29 UTC | 24m |
| AHK769 | AHK | Beijing Capital International Airport (ZBAA) | Zhuhai Airport (ZGSD) | 2026-09-21 13:55 UTC | 2026-09-21 16:28 UTC | 2h 33m |
| GFLOH | GFL | EG32 (EG32) | EG32 (EG32) | 2026-09-21 15:40 UTC | 2026-09-21 16:27 UTC | 47m |
| N6601K |  | Usaf Academy Davis Airfield (KAFF) | High Plains Airport Airport (CD15) | 2026-09-21 15:53 UTC | 2026-09-21 16:27 UTC | 33m |
| VIR24M | Virgin Atlantic | Los Angeles International Airport (KLAX) | London Heathrow Airport (EGLL) | 2026-09-21 06:53 UTC | 2026-09-21 16:26 UTC | 9h 32m |
| DUKE40 | DUK | Wiesbaden Army Airfield (ETOU) | Wiesbaden Army Airfield (ETOU) | 2026-09-21 16:10 UTC | 2026-09-21 16:25 UTC | 14m |
| UAE9840 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-21 09:15 UTC | 2026-09-21 16:24 UTC | 7h 9m |
| N50PA |  | Reading Regional/Carl A Spaatz Field (KRDG) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-09-21 16:08 UTC | 2026-09-21 16:21 UTC | 12m |
| CXK475 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Mc Clellan-Palomar Airport (KCRQ) | 2026-09-21 15:23 UTC | 2026-09-21 16:19 UTC | 56m |
| N139PS |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-21 15:34 UTC | 2026-09-21 16:16 UTC | 42m |
| TJT37DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-09-21 15:00 UTC | 2026-09-21 16:15 UTC | 1h 14m |
| EMD305 | EMD | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-09-21 15:58 UTC | 2026-09-21 16:15 UTC | 16m |
| WNG20B | WNG | Denton Enterprise Airport (KDTO) | Decatur Municipal Airport (KLUD) | 2026-09-21 14:53 UTC | 2026-09-21 16:14 UTC | 1h 21m |
| WIF6T | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-21 16:02 UTC | 2026-09-21 16:13 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
